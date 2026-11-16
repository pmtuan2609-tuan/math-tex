# -*- coding: utf-8 -*-
"""
MathTex Web API - Backend Serverless chạy trên Vercel
Xử lý sinh câu hỏi ngẫu nhiên, tự động chuyển TikZ sang hình ảnh và xuất file Word (.docx)
"""
from fastapi import FastAPI, Response, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
from typing import List, Optional
import io
import re
import random
import zipfile
import urllib.request
import urllib.parse

from docx import Document
from docx.shared import Inches, Pt, RGBColor
from docx.enum.text import WD_ALIGN_PARAGRAPH
from docx.enum.table import WD_TABLE_ALIGNMENT

app = FastAPI(title="MathTex Web API", version="2026.2")

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# ----------------- HÀM CHUYỂN TIKZ SANG ẢNH PNG -----------------
def render_tikz_to_png(tikz_code: str) -> Optional[bytes]:
    """
    Chuyển mã TikZ sang ảnh PNG để chèn vào Word.
    Ưu tiên 1: Gọi Kroki.io (Dịch vụ render mã nguồn mở miễn phí, hỗ trợ TikZ trực tiếp).
    Ưu tiên 2: Gọi QuickLaTeX API (Biên dịch TeX trực tuyến).
    """
    clean_tikz = tikz_code.strip()
    if not clean_tikz.startswith("\\begin{tikzpicture}"):
        clean_tikz = f"\\begin{{tikzpicture}}\n{clean_tikz}\n\\end{{tikzpicture}}"

    # 1. Thử Kroki.io
    try:
        url = "https://kroki.io/tikz/png"
        req = urllib.request.Request(
            url,
            data=clean_tikz.encode("utf-8"),
            headers={"Content-Type": "text/plain; charset=utf-8", "User-Agent": "MathTex-Web"},
            method="POST"
        )
        with urllib.request.urlopen(req, timeout=6) as resp:
            if resp.status == 200:
                data = resp.read()
                if len(data) > 100:
                    return data
    except Exception:
        pass

    # 2. Thử QuickLaTeX API
    try:
        ql_url = "https://quicklatex.com/robot3.asp"
        payload = urllib.parse.urlencode({
            "formula": clean_tikz,
            "fsize": "17px",
            "fcolor": "000000",
            "mode": "0",
            "out": "1",
            "preamble": r"\usepackage{amsmath}\usepackage{amsfonts}\usepackage{amssymb}\usepackage{tikz}\usetikzlibrary{calc,patterns,arrows}"
        }).encode("utf-8")
        req = urllib.request.Request(ql_url, data=payload, method="POST")
        with urllib.request.urlopen(req, timeout=6) as response:
            res_text = response.read().decode("utf-8", errors="ignore")
            lines = res_text.strip().splitlines()
            if lines and lines[0].strip() == "0" and len(lines) > 1:
                img_url = lines[1].split()[0]
                with urllib.request.urlopen(img_url, timeout=6) as img_resp:
                    return img_resp.read()
    except Exception:
        pass

    return None

# ----------------- SINH ĐỒ THỊ VẬN ĐỘNG VIÊN -----------------
def generate_runners_graph_png() -> Optional[bytes]:
    """Vẽ đồ thị 2 vận động viên: Ưu tiên TikZ qua Kroki/QuickLaTeX, dự phòng matplotlib"""
    tikz_vdv = r"""\begin{tikzpicture}[>=stealth, scale=0.15]
\draw[->] (-2,0) -- (36,0) node[below] {$t$};
\draw[->] (0,-1) -- (0,10.5) node[left] {$v$};
\fill[pattern=north east lines] plot[domain=0:10] (\x, {-(\x/10)^3/6 + 7*\x/60 + 5}) -- plot[domain=10:0] (\x, {-1/150*(\x^2 - 40*\x - 600)}) -- cycle;
\fill[pattern=north east lines] plot[domain=10:30] (\x, {-1/150*(\x^2 - 40*\x - 600)}) -- plot[domain=30:10] (\x, {-(\x/10)^3/6 + 7*\x/60 + 5}) -- cycle;
\draw[thick, blue, domain=0:33] plot (\x, {-(\x/10)^3/6 + 7*\x/60 + 5});
\draw[thick, red, domain=0:33] plot (\x, {-1/150*(\x^2 - 40*\x - 600)});
\end{tikzpicture}"""
    img = render_tikz_to_png(tikz_vdv)
    if img:
        return img

    try:
        import matplotlib
        matplotlib.use('Agg')
        import matplotlib.pyplot as plt
        import numpy as np

        t = np.linspace(0, 33, 200)
        v1 = -1/6000 * t**3 + 7/60 * t + 5
        v2 = -1/150 * (t**2 - 40*t - 600)

        fig, ax = plt.subplots(figsize=(4.2, 2.6), dpi=150)
        ax.plot(t, v1, label=r'$v_1(t)$', color='#1d4ed8', lw=1.8)
        ax.plot(t, v2, label=r'$v_2(t)$', color='#dc2626', lw=1.8)
        t_sub1 = np.linspace(0, 10, 50)
        ax.fill_between(t_sub1, -1/6000 * t_sub1**3 + 7/60 * t_sub1 + 5, -1/150 * (t_sub1**2 - 40*t_sub1 - 600), 
                        hatch='//', facecolor='none', edgecolor='#64748b', lw=0.5)
        t_sub2 = np.linspace(10, 30, 80)
        ax.fill_between(t_sub2, -1/6000 * t_sub2**3 + 7/60 * t_sub2 + 5, -1/150 * (t_sub2**2 - 40*t_sub2 - 600), 
                        hatch='//', facecolor='none', edgecolor='#64748b', lw=0.5)
        ax.axvline(10, color='#94a3b8', linestyle='--', lw=0.8)
        ax.axvline(30, color='#94a3b8', linestyle='--', lw=0.8)
        ax.set_xlabel('t (giây)', fontsize=9)
        ax.set_ylabel('v (m/s)', fontsize=9)
        ax.legend(loc='lower center', fontsize=8, frameon=False, ncol=2)
        plt.tight_layout()

        buf = io.BytesIO()
        plt.savefig(buf, format='png', bbox_inches='tight')
        plt.close(fig)
        buf.seek(0)
        return buf.getvalue()
    except Exception:
        return None

# ----------------- DANH MỤC DẠNG TOÁN -----------------
TOPICS = [
    {
        "id": "k12_c1_khao_sat",
        "name": "Toán 12 — Khảo sát hàm số (Cực trị, Tính đơn điệu)",
        "type": "mc"
    },
    {
        "id": "k12_c3_thong_ke_mot",
        "name": "Toán 12 — Thống kê: Tìm mốt của mẫu ghép nhóm",
        "type": "mc"
    },
    {
        "id": "k12_c4_tich_phan_vđv",
        "name": "Toán 12 — Đúng/Sai: Tích phân chuyển động 2 vận động viên (Có hình đồ thị)",
        "type": "tf"
    },
    {
        "id": "k12_c4_phong_xa",
        "name": "Toán 12 — Đúng/Sai: Phân rã phóng xạ vi phân m'(t)",
        "type": "tf"
    },
    {
        "id": "k12_sa_bieu_thuc",
        "name": "Toán 12 — Trả lời ngắn: Biểu thức tham số",
        "type": "sa"
    }
]

@app.get("/api/health")
def health_check():
    return {"status": "ok", "app": "MathTex Pro Web 2026", "platform": "Vercel Serverless"}

@app.get("/api/topics")
def get_topics():
    return TOPICS

# ----------------- HÀM SINH CÂU HỎI NGẪU NHIÊN -----------------
def generate_question_data(topic_id: str):
    if topic_id == "k12_c3_thong_ke_mot":
        m1 = random.randint(10, 18)
        m2 = random.randint(30, 40)
        m3 = random.randint(45, 55)
        m4 = random.randint(20, 28)
        tu = m3 - m2
        mau = (m3 - m2) + (m3 - m4)
        mo_val = round(15 + (tu / mau) * 5, 2)
        
        caudan = (
            f"Mức thưởng Tết (triệu đồng) mà các công nhân một nhà máy nhận được như sau:\n"
            f"[5; 10): {m1} công nhân | [10; 15): {m2} công nhân | [15; 20): {m3} công nhân | [20; 25): {m4} công nhân.\n"
            f"Mốt của mẫu số liệu ghép nhóm trên gần nhất với giá trị nào sau đây?"
        )
        c_true = f"{mo_val:.2f}"
        c_w1 = f"{mo_val + 1.0:.2f}"
        c_w2 = f"{mo_val - 0.9:.2f}"
        c_w3 = f"{mo_val + 0.85:.2f}"
        choices = [f"A. {c_w1}", f"B. {c_w2}", f"C. {c_w3}", f"D. {c_true} (Đúng)"]
        random.shuffle(choices)
        loigiai = (
            f"Nhóm chứa mốt là [15; 20) với tần số lớn nhất m_3 = {m3}.\n"
            f"Áp dụng công thức: M_0 = 15 + [{m3} - {m2}] / [({m3} - {m2}) + ({m3} - {m4})] * 5 = {mo_val:.2f}."
        )
        return {"caudan": caudan, "choices": choices, "loigiai": loigiai, "type": "mc", "image_bytes": None}

    elif topic_id == "k12_c4_tich_phan_vđv":
        caudan = (
            "Có hai vận động viên A và B chạy trên đường thẳng với vận tốc v_1(t) = -1/6000*t^3 + 7/60*t + 5 (m/s) "
            "và v_2(t) = -1/150*(t^2 - 40t - 600) (m/s) như hình vẽ bên dưới. Hai người xuất phát cùng lúc tại cùng một vị trí. "
            "Các mệnh đề sau đúng hay sai?"
        )
        choices = [
            "a) Quãng đường vận động viên A đi được sau 30 giây là tích phân từ 0 đến 30 của v_1(t) dt. [ĐÚNG]",
            "b) Tổng diện tích phần tô đậm giữa hai đồ thị bằng khoảng cách giữa 2 người sau 30 giây. [SAI]",
            "c) Biểu thức vận tốc của vận động viên B là parabol v_2(t) = -1/150*(t^2 - 40t - 600). [ĐÚNG]",
            "d) Tại thời điểm 10 giây, vận động viên B dẫn trước vận động viên A khoảng 4,3 m. [SAI]"
        ]
        loigiai = (
            "a) Đúng theo định nghĩa tích phân của vận tốc.\n"
            "b) Sai vì khoảng cách là trị tuyệt đối hiệu tích phân |S1 - S2|, không phải tổng diện tích S1 + S2.\n"
            "c) Đúng theo phương trình parabol qua đỉnh và điểm mút.\n"
            "d) Sai vì tại t = 10s vận động viên A đi được 55,4m > B đi được 51,1m nên A dẫn trước B."
        )
        img_bytes = generate_runners_graph_png()
        return {"caudan": caudan, "choices": choices, "loigiai": loigiai, "type": "tf", "image_bytes": img_bytes}

    elif topic_id == "k12_c4_phong_xa":
        m0 = random.choice([400, 600, 800, 1000])
        half_m = m0 // 2
        caudan = (
            f"Một mẫu chất phóng xạ có khối lượng ban đầu {m0} mg. Sau 5 ngày phân rã còn lại {half_m} mg. "
            f"Biết tốc độ phân rã tỉ lệ thuận với khối lượng hiện có m'(t) = k*m(t) (k khác 0, t >= 0). "
            f"Các mệnh đề sau đúng hay sai?"
        )
        choices = [
            "a) Hằng số tốc độ phân rã của mẫu chất là k = -1/5 * ln(2). [ĐÚNG]",
            f"b) Sau 15 ngày kể từ ban đầu, khối lượng mẫu chất còn lại là {m0 // 8} mg. [ĐÚNG]",
            f"c) Khối lượng mẫu phóng xạ tính bởi công thức m(t) = {half_m} * e^(kt). [SAI]",
            "d) Để khối lượng chỉ còn 1/16 ban đầu, cần đúng 10 ngày. [SAI]"
        ]
        loigiai = (
            f"Từ m'(t) = k*m(t) suy ra m(t) = m0 * e^(kt) = {m0} * e^(kt).\n"
            "Tại t = 5: e^(5k) = 1/2 => k = -1/5*ln(2).\n"
            "Sau 15 ngày = 3 chu kỳ bán rã, còn m0 / 8 mg."
        )
        return {"caudan": caudan, "choices": choices, "loigiai": loigiai, "type": "tf", "image_bytes": None}

    elif topic_id == "k12_c1_don_dieu":
        a = random.randint(1, 4)
        caudan = f"Hàm số y = x^3 - 3x^2 + {a} đồng biến trên khoảng nào dưới đây?"
        choices = ["A. (0; 2)", "B. (-∞; 0) và (2; +∞) (Đúng)", "C. (2; +∞)", "D. (-∞; 2)"]
        loigiai = "Ta có y' = 3x^2 - 6x = 3x(x - 2). Cho y' > 0 <=> x < 0 hoặc x > 2. Do đó hàm số đồng biến trên (-∞; 0) và (2; +∞)."
        return {"caudan": caudan, "choices": choices, "loigiai": loigiai, "type": "mc", "image_bytes": None}

    elif topic_id == "k12_c1_tiem_can":
        a = random.randint(1, 5)
        caudan = f"Số đường tiệm cận đứng và tiệm cận ngang của đồ thị hàm số y = (2x - 1) / (x - {a}) là:"
        choices = ["A. 1", "B. 2 (Đúng)", "C. 3", "D. 0"]
        loigiai = f"Tiệm cận đứng x = {a} (do mẫu bằng 0 tại x = {a}). Tiệm cận ngang y = 2 (do lim y khi x -> vô cùng = 2). Tổng cộng có 2 đường tiệm cận."
        return {"caudan": caudan, "choices": choices, "loigiai": loigiai, "type": "mc", "image_bytes": None}

    elif topic_id == "k12_c1_gtln_gtnn":
        caudan = "Giá trị lớn nhất của hàm số f(x) = x^4 - 2x^2 + 3 trên đoạn [0; 2] bằng:"
        choices = ["A. 3", "B. 2", "C. 11 (Đúng)", "D. 12"]
        loigiai = "f'(x) = 4x^3 - 4x = 4x(x^2 - 1). Nghiệm trên [0; 2] là x = 0, x = 1. Ta có f(0) = 3, f(1) = 2, f(2) = 11. Vậy GTLN = 11."
        return {"caudan": caudan, "choices": choices, "loigiai": loigiai, "type": "mc", "image_bytes": None}

    elif topic_id == "k11_c1_luong_giac":
        caudan = "Tất cả các nghiệm của phương trình sin(x) = 1/2 là:"
        choices = ["A. x = π/6 + k2π và x = 5π/6 + k2π (Đúng)", "B. x = π/3 + k2π", "C. x = ±π/6 + k2π", "D. x = π/6 + kπ"]
        loigiai = "sin(x) = sin(π/6) <=> x = π/6 + k2π hoặc x = π - π/6 + k2π = 5π/6 + k2π (k thuộc Z)."
        return {"caudan": caudan, "choices": choices, "loigiai": loigiai, "type": "mc", "image_bytes": None}

    elif topic_id == "k10_c2_bpt":
        caudan = "Điểm nào sau đây thuộc miền nghiệm của bất phương trình 2x + y - 3 > 0?"
        choices = ["A. (0; 0)", "B. (1; 1)", "C. (2; 1) (Đúng)", "D. (-1; 2)"]
        loigiai = "Thay tọa độ (2; 1) vào: 2*(2) + 1 - 3 = 2 > 0 (thỏa mãn). Vậy điểm (2; 1) thuộc miền nghiệm."
        return {"caudan": caudan, "choices": choices, "loigiai": loigiai, "type": "mc", "image_bytes": None}

    elif topic_id == "k10_sa_vecto":
        caudan = "Cho tam giác ABC đều cạnh a = 4. Tính độ dài của vectơ tổng u = AB + AC?"
        choices = ["Đáp án: 6,93 (4√3)"]
        loigiai = "Gọi M là trung điểm BC, ta có AB + AC = 2AM = 2*(a*sqrt(3)/2) = a*sqrt(3) = 4*sqrt(3) ≈ 6,93."
        return {"caudan": caudan, "choices": choices, "loigiai": loigiai, "type": "sa", "image_bytes": None}

    elif topic_id == "k12_sa_bieu_thuc":
        a = random.randint(2, 6)
        b = random.randint(1, 5)
        ans = 2 * a - b
        caudan = f"Cho biết biểu thức P = 2a - b với a = {a} và b = {b}. Hãy tính giá trị của P?"
        choices = [f"Đáp án: {ans}"]
        loigiai = f"Thay a = {a}, b = {b} vào biểu thức: P = 2*({a}) - ({b}) = {ans}."
        return {"caudan": caudan, "choices": choices, "loigiai": loigiai, "type": "sa", "image_bytes": None}

    else:
        a = random.randint(1, 3)
        caudan = f"Cho hàm số f(x) có đạo hàm f'(x) = (x + {a})^2 * (x - 1)^3 * (2 - x). Hàm số f(x) đạt cực đại tại điểm:"
        choices = [f"A. x = -{a}", "B. x = 1", "C. x = 2 (Đúng)", f"D. x = -{a} và x = 2"]
        random.shuffle(choices)
        loigiai = f"Nghiệm x = -{a} là bội chẵn không đổi dấu. Nghiệm x = 2 làm f'(x) đổi dấu từ dương sang âm nên x = 2 là điểm cực đại."
        return {"caudan": caudan, "choices": choices, "loigiai": loigiai, "type": "mc", "image_bytes": None}

@app.get("/api/generate")
def generate_endpoint(topic: str = "k12_c1_khao_sat"):
    data = generate_question_data(topic)
    # Loại bỏ image_bytes khỏi response JSON cho nhẹ, chỉ giữ cờ has_image
    return {
        "caudan": data["caudan"],
        "choices": data["choices"],
        "loigiai": data["loigiai"],
        "type": data["type"],
        "has_image": data.get("image_bytes") is not None
    }

# ----------------- HÀM TẠO FILE WORD CHÈN ẢNH TỰ ĐỘNG -----------------
def create_styled_word_document(title: str, questions: list, show_solution: bool = True):
    doc = Document()
    
    for section in doc.sections:
        section.top_margin = Inches(0.8)
        section.bottom_margin = Inches(0.8)
        section.left_margin = Inches(0.8)
        section.right_margin = Inches(0.8)

    # Tiêu đề trường / kỳ thi
    header_table = doc.add_table(rows=2, cols=2)
    header_table.alignment = WD_TABLE_ALIGNMENT.CENTER
    header_table.autofit = True
    
    cell_l1 = header_table.cell(0, 0)
    p_l1 = cell_l1.paragraphs[0]
    p_l1.alignment = WD_ALIGN_PARAGRAPH.CENTER
    r_l1 = p_l1.add_run("SỞ GD&ĐT ..........................\nTRƯỜNG THPT ..........................")
    r_l1.font.name = "Times New Roman"
    r_l1.font.size = Pt(11)
    r_l1.bold = True

    cell_r1 = header_table.cell(0, 1)
    p_r1 = cell_r1.paragraphs[0]
    p_r1.alignment = WD_ALIGN_PARAGRAPH.CENTER
    r_r1 = p_r1.add_run(f"{title.upper()}\nNĂM HỌC 2025 - 2026")
    r_r1.font.name = "Times New Roman"
    r_r1.font.size = Pt(11)
    r_r1.bold = True
    r_r1.font.color.rgb = RGBColor(0, 78, 152)

    cell_l2 = header_table.cell(1, 0)
    p_l2 = cell_l2.paragraphs[0]
    p_l2.alignment = WD_ALIGN_PARAGRAPH.LEFT
    r_l2 = p_l2.add_run("Họ và tên thí sinh: ....................................................\nSố báo danh: .............................................................")
    r_l2.font.name = "Times New Roman"
    r_l2.font.size = Pt(10)
    r_l2.italic = True

    cell_r2 = header_table.cell(1, 1)
    p_r2 = cell_r2.paragraphs[0]
    p_r2.alignment = WD_ALIGN_PARAGRAPH.CENTER
    r_r2 = p_r2.add_run("Thời gian làm bài: 90 phút\n(Không kể thời gian phát đề)")
    r_r2.font.name = "Times New Roman"
    r_r2.font.size = Pt(10)
    r_r2.italic = True

    doc.add_paragraph().paragraph_format.space_after = Pt(8)

    # Thêm từng câu hỏi
    for idx, q in enumerate(questions, 1):
        p_q = doc.add_paragraph()
        p_q.paragraph_format.space_before = Pt(6)
        p_q.paragraph_format.space_after = Pt(3)
        
        r_num = p_q.add_run(f"Câu {idx}. ")
        r_num.bold = True
        r_num.font.name = "Times New Roman"
        r_num.font.color.rgb = RGBColor(0, 78, 152)
        
        r_cau = p_q.add_run(q.get("caudan", ""))
        r_cau.font.name = "Times New Roman"
        r_cau.font.size = Pt(12)

        # NẾU CÓ HÌNH ẢNH (TỪ TIKZ HOẶC MATPLOTLIB) -> CHÈN VÀO GIỮA FILE WORD
        img_data = q.get("image_bytes")
        if img_data:
            try:
                p_img = doc.add_paragraph()
                p_img.alignment = WD_ALIGN_PARAGRAPH.CENTER
                p_img.paragraph_format.space_before = Pt(4)
                p_img.paragraph_format.space_after = Pt(6)
                run_img = p_img.add_run()
                run_img.add_picture(io.BytesIO(img_data), width=Inches(3.3))
            except Exception:
                pass

        # Các phương án lựa chọn
        choices = q.get("choices", [])
        for c in choices:
            p_c = doc.add_paragraph()
            p_c.paragraph_format.left_indent = Inches(0.3)
            p_c.paragraph_format.space_after = Pt(2)
            
            run_c = p_c.add_run(c)
            run_c.font.name = "Times New Roman"
            run_c.font.size = Pt(11.5)
            
            # Gạch chân đáp án đúng
            if "(Đúng)" in c or "[ĐÚNG]" in c:
                run_c.underline = True
                run_c.bold = True
                run_c.font.color.rgb = RGBColor(180, 0, 0)

        # Lời giải chi tiết
        if show_solution and q.get("loigiai"):
            p_sol = doc.add_paragraph()
            p_sol.paragraph_format.left_indent = Inches(0.3)
            p_sol.paragraph_format.space_before = Pt(3)
            p_sol.paragraph_format.space_after = Pt(6)
            
            r_slbl = p_sol.add_run("Lời giải: ")
            r_slbl.bold = True
            r_slbl.italic = True
            r_slbl.font.name = "Times New Roman"
            r_slbl.font.color.rgb = RGBColor(4, 120, 87)
            
            r_stxt = p_sol.add_run(q.get("loigiai"))
            r_stxt.italic = True
            r_stxt.font.name = "Times New Roman"
            r_stxt.font.size = Pt(11)

    return doc

@app.get("/api/download-word")
def download_word_endpoint(topic: str = "k12_c1_khao_sat", show_solution: bool = True):
    q_data = generate_question_data(topic)
    doc = create_styled_word_document(
        title="ĐỀ THI TRẮC NGHIỆM GDPT 2018",
        questions=[q_data],
        show_solution=show_solution
    )
    
    stream = io.BytesIO()
    doc.save(stream)
    stream.seek(0)
    
    filename = f"MathTex_{topic}.docx"
    return Response(
        content=stream.getvalue(),
        media_type="application/vnd.openxmlformats-officedocument.wordprocessingml.document",
        headers={"Content-Disposition": f"attachment; filename={filename}"}
    )

# ----------------- ĐẢO ĐỀ VÀ TỰ ĐỘNG CHUYỂN TIKZ SANG ẢNH -----------------
class ShuffleRequest(BaseModel):
    raw_text: str
    num_codes: int = 4
    start_code: int = 101
    show_solution: bool = True

def parse_raw_exam_with_tikz(text: str):
    """
    Bóc tách câu hỏi và tự động trích xuất các khối TikZ,
    sau đó chuyển TikZ thành ảnh PNG để chèn vào Word.
    """
    questions = []
    blocks = re.findall(r"\\begin\{ex\}(.*?)\\end\{ex\}", text, re.DOTALL)
    if blocks:
        for b in blocks:
            caudan = b
            choices = []
            loigiai = ""
            img_bytes = None

            # 1. Trích xuất hình TikZ nếu có
            tikz_match = re.search(r"\\begin\{tikzpicture\}(.*?)\\end\{tikzpicture\}", caudan, re.DOTALL)
            if tikz_match:
                full_tikz = tikz_match.group(0)
                img_bytes = render_tikz_to_png(full_tikz)
                caudan = caudan.replace(full_tikz, "")

            # 2. Bóc tách lời giải
            lg_match = re.search(r"\\loigiai\{(.*?)\}", caudan, re.DOTALL)
            if lg_match:
                loigiai = lg_match.group(1).strip()
                caudan = caudan.replace(lg_match.group(0), "")

            # 3. Bóc tách các phương án lựa chọn \choice
            if "\\choice" in caudan:
                parts = re.split(r"\\choice", caudan, maxsplit=1)
                cd = parts[0].strip()
                ans_str = parts[1].strip()
                c_items = re.findall(r"\{([^{}]*(?:\{[^{}]*\}[^{}]*)*)\}", ans_str)
                tags = ["A", "B", "C", "D"]
                for i, c in enumerate(c_items[:4]):
                    prefix = f"{tags[i]}. "
                    is_true = "\\True" in c
                    clean_c = c.replace("\\True", "").strip()
                    choices.append(f"{prefix}{clean_c}{' (Đúng)' if is_true else ''}")
                questions.append({"caudan": cd, "choices": choices, "loigiai": loigiai, "type": "mc", "image_bytes": img_bytes})
            else:
                questions.append({"caudan": caudan.strip(), "choices": [], "loigiai": loigiai, "type": "sa", "image_bytes": img_bytes})
    else:
        # Nhập văn bản thông thường
        cau_splits = re.split(r"(?:Câu|\bCÂU)\s*\d+[\.\:]", text)
        for c in cau_splits:
            c = c.strip()
            if c:
                lines = [l.strip() for l in c.splitlines() if l.strip()]
                if lines:
                    questions.append({"caudan": lines[0], "choices": lines[1:], "loigiai": "", "type": "mc", "image_bytes": None})
    
    return questions

@app.post("/api/shuffle-word")
def shuffle_word_endpoint(req: ShuffleRequest):
    questions = parse_raw_exam_with_tikz(req.raw_text)
    if not questions:
        questions = [
            generate_question_data("k12_c1_khao_sat"),
            generate_question_data("k12_c3_thong_ke_mot"),
            generate_question_data("k12_c4_tich_phan_vđv"),
            generate_question_data("k12_c4_phong_xa")
        ]

    zip_stream = io.BytesIO()
    with zipfile.ZipFile(zip_stream, "w", zipfile.ZIP_DEFLATED) as zf:
        for i in range(req.num_codes):
            code_num = req.start_code + i
            shuffled_q = list(questions)
            random.seed(code_num)
            random.shuffle(shuffled_q)
            
            final_q = []
            for q in shuffled_q:
                q_copy = dict(q)
                if q_copy.get("type") == "mc" and q_copy.get("choices"):
                    ch_list = list(q_copy["choices"])
                    random.shuffle(ch_list)
                    relabeled = []
                    tags = ["A", "B", "C", "D"]
                    for idx_c, ch in enumerate(ch_list):
                        raw_text = re.sub(r"^[A-D]\.\s*", "", ch)
                        relabeled.append(f"{tags[idx_c]}. {raw_text}")
                    q_copy["choices"] = relabeled
                final_q.append(q_copy)

            doc = create_styled_word_document(
                title=f"ĐỀ THI TRẮC NGHIỆM — MÃ ĐỀ {code_num}",
                questions=final_q,
                show_solution=req.show_solution
            )
            file_stream = io.BytesIO()
            doc.save(file_stream)
            zf.writestr(f"De_Thi_Ma_{code_num}.docx", file_stream.getvalue())

    zip_stream.seek(0)
    return Response(
        content=zip_stream.getvalue(),
        media_type="application/zip",
        headers={"Content-Disposition": f"attachment; filename=Bo_De_Thi_Dao_Word_{req.start_code}.zip"}
    )
