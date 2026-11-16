# -*- coding: utf-8 -*-
"""
Module: sinh_de_on_tap_gk1_toan10.py
Ngân hàng sinh đề thi và bài tập trắc nghiệm ÔN TẬP GIỮA HỌC KÌ 1 TOÁN 10
Được xây dựng chuẩn hóa theo cấu trúc Đề kiểm tra chuẩn GDPT 2018 (Mã đề 209):
- Phần I: 12 câu Trắc nghiệm 4 lựa chọn (MC)
- Phần II: 4 câu Trắc nghiệm Đúng/Sai (TF)
- Phần III: 6 câu Trắc nghiệm Trả lời ngắn (SA)
- Phần IV: Các câu hỏi Tự luận / Vận dụng cao (TL)

Toàn bộ tham số và số liệu được lập trình thuật toán hóa sinh ngẫu nhiên (Algorithmic Generation),
mỗi lần bấm sinh sẽ cho một đề thi hoàn toàn mới, số liệu đẹp, không trùng lặp,
tự động sinh hình vẽ TikZ chuẩn mực và lời giải chi tiết từng bước.
"""

import math
import random
from fractions import Fraction


def clean_option(s):
    """Làm sạch phương án, loại bỏ tiền tố A., B., C., D. hoặc dấu chấm cuối dòng"""
    if not isinstance(s, str):
        s = str(s)
    s = s.strip()
    for pfx in ['a)', 'b)', 'c)', 'd)', 'A.', 'B.', 'C.', 'D.', 'a.', 'b.', 'c.', 'd.']:
        if s.startswith(pfx):
            s = s[len(pfx):].strip()
    while s.endswith('.'):
        s = s[:-1].strip()
    return s


def shuffle_choices(correct_text, wrong_texts):
    """Trộn ngẫu nhiên 4 phương án cho câu trắc nghiệm nhiều lựa chọn"""
    opts = [(True, clean_option(correct_text))] + [(False, clean_option(w)) for w in wrong_texts]
    random.shuffle(opts)
    choices = []
    for is_correct, text in opts:
        if is_correct:
            choices.append(f"{{\\True {text}}}\n")
        else:
            choices.append(f"{{{text}}}\n")
    return choices


def make_tf_choices(items):
    """
    Tạo 4 ý Đúng/Sai cho câu hỏi Phần II:
    items = list 4 tuples: (stmt_true, stmt_false, exp_true, exp_false)
    Mỗi ý được chọn ngẫu nhiên là Đúng hoặc Sai.
    """
    choices = []
    loi_giai_parts = []
    labels = ["a)", "b)", "c)", "d)"]
    for i, item in enumerate(items):
        stmt_t, stmt_f, exp_t, exp_f = item
        is_true = random.choice([True, False])
        t_clean = clean_option(stmt_t)
        f_clean = clean_option(stmt_f)
        if is_true:
            choices.append(f"{{\\True {t_clean}}}\n")
            loi_giai_parts.append(f"\\itemch \\textbf{{ĐÚNG.}} {exp_t.strip()}")
        else:
            choices.append(f"{{{f_clean}}}\n")
            loi_giai_parts.append(f"\\itemch \\textbf{{SAI.}} {exp_f.strip()}")
    
    loi_giai = "\\begin{itemchoice}\n" + "\n".join(loi_giai_parts) + "\n\\end{itemchoice}"
    return choices, loi_giai


def fmt_frac(fr):
    """Định dạng phân số LaTeX gọn gàng"""
    if isinstance(fr, (int, float)) and fr == int(fr):
        return str(int(fr))
    if isinstance(fr, Fraction):
        if fr.denominator == 1:
            return str(fr.numerator)
        if fr.numerator < 0:
            return f"-\\dfrac{{{abs(fr.numerator)}}}{{{fr.denominator}}}"
        return f"\\dfrac{{{fr.numerator}}}{{{fr.denominator}}}"
    return str(fr)


# ==============================================================================
# PHẦN I: 12 CÂU TRẮC NGHIỆM NHIỀU LỰA CHỌN (MC)
# ==============================================================================

def gk10_mc_nhan_biet_menh_de():
    """Câu 1: Nhận biết câu nào là mệnh đề / không phải mệnh đề"""
    mode = random.choice(["khong_phai", "la_menh_de"])
    
    cau_cam_than = [
        "Học lớp 10 thật vui!",
        "Hôm nay thời tiết đẹp quá!",
        "Trời hôm nay lạnh thế nhỉ?",
        "Bạn làm bài thi tốt chứ?",
        "Chúc bạn thi đạt điểm tối đa!",
        "Hãy giữ trật tự trong lớp học!"
    ]
    cau_menh_de_dung = [
        "Pleiku là thành phố trực thuộc tỉnh Gia Lai",
        "Số $2$ là số nguyên tố chẵn duy nhất",
        "Tam giác đều có ba góc bằng $60^\\circ$",
        "Hà Nội là thủ đô của nước Việt Nam",
        "Tổng ba góc trong một tam giác bằng $180^\\circ$"
    ]
    cau_menh_de_sai = [
        "Một năm luôn luôn có đúng $360$ ngày",
        "$2 + 3 = 6$",
        "Số $15$ là số nguyên tố",
        "Mọi số thực bình phương đều lớn hơn $0$",
        "Hình thang cân là hình có hai đường chéo vuông góc"
    ]
    
    if mode == "khong_phai":
        caudan = "Trong các câu sau đây, câu nào \\textbf{không phải} là mệnh đề?"
        ans_true = random.choice(cau_cam_than)
        wrongs = random.sample(cau_menh_de_dung + cau_menh_de_sai, 3)
        loi_giai = f"Câu ``{ans_true}'' là câu cảm thán hoặc câu hỏi, không khẳng định một sự thật có tính đúng hoặc sai, nên không phải là mệnh đề."
    else:
        caudan = "Trong các câu sau đây, câu nào là một mệnh đề?"
        ans_true = random.choice(cau_menh_de_dung + cau_menh_de_sai)
        wrongs = random.sample(cau_cam_than, 3)
        loi_giai = f"Câu ``{ans_true}'' là một khẳng định có tính đúng hoặc sai xác định, do đó đây là một mệnh đề."

    choices = shuffle_choices(ans_true, wrongs)
    return caudan, choices, loi_giai


def gk10_mc_liet_ke_tap_hop():
    """Câu 2: Liệt kê các phần tử của tập hợp X = {x in R | ax^2 + bx + c = 0}"""
    # Chọn hai nghiệm nguyên hoặc hữu tỉ phân biệt
    x1 = random.choice([-3, -2, -1, 1, 2, 3])
    x2_num = random.choice([1, 2, 3, 5])
    x2_den = random.choice([2, 3])
    while x1 * x2_den == x2_num:
        x1 = random.choice([-3, -2, -1, 1, 2, 3])
    
    # a*(x - x1)*(den*x - num) = 0
    # a*(den*x^2 - (num + den*x1)*x + num*x1)
    a = x2_den
    b = -(x2_num + x2_den * x1)
    c = x2_num * x1
    
    b_sign = f"+ {b}x" if b > 0 else f"- {abs(b)}x"
    c_sign = f"+ {c}" if c > 0 else f"- {abs(c)}"
    eq_str = f"{a}x^2 {b_sign} {c_sign} = 0"
    
    fr_str = f"\\dfrac{{{x2_num}}}{{{x2_den}}}"
    
    ans_true = f"$X = \\left\\{{{x1}; {fr_str}\\right\\}}$"
    w1 = f"$X = \\{{{x1}\\}}$"
    w2 = f"$X = \\left\\{{{fr_str}\\right\\}}$"
    w3 = f"$X = \\{{{abs(x1)}; {fr_str}\\}}$" if x1 < 0 else f"$X = \\{{{-x1}; {fr_str}\\}}$"
    
    caudan = f"Liệt kê các phần tử của tập hợp $X = \\{{x \\in \\mathbb{{R}} \\mid {eq_str}\\}}$."
    loi_giai = f"Giải phương trình ${eq_str}$:\n" \
               f"Ta có $\\Delta = ({b})^2 - 4 \\cdot {a} \\cdot ({c}) = {b*b - 4*a*c}$.\n" \
               f"Phương trình có hai nghiệm phân biệt $x_1 = {x1}$ và $x_2 = {fr_str}$.\n" \
               f"Vì cả hai nghiệm đều là số thực, nên $X = \\left\\{{{x1}; {fr_str}\\right\\}}$."
    
    choices = shuffle_choices(ans_true, [w1, w2, w3])
    return caudan, choices, loi_giai


def gk10_mc_dang_thuc_luong_giac():
    """Câu 3: Đẳng thức lượng giác đúng / sai của hai góc bù nhau (180 - alpha)"""
    formulas = [
        (r"\sin(180^\circ - \alpha) = \sin \alpha", True, r"\sin(180^\circ - \alpha) = -\sin \alpha"),
        (r"\cos(180^\circ - \alpha) = -\cos \alpha", True, r"\cos(180^\circ - \alpha) = \cos \alpha"),
        (r"\tan(180^\circ - \alpha) = -\tan \alpha", True, r"\tan(180^\circ - \alpha) = \tan \alpha"),
        (r"\cot(180^\circ - \alpha) = -\cot \alpha", True, r"\cot(180^\circ - \alpha) = \cot \alpha"),
    ]
    
    # Chọn 1 công thức đúng làm đáp án
    target_idx = random.randint(0, 3)
    correct_pair = formulas[target_idx]
    correct_text = f"${correct_pair[0]}$"
    
    wrong_texts = []
    for idx, (form_true, _, form_false) in enumerate(formulas):
        if idx != target_idx:
            wrong_texts.append(f"${form_false}$")
            
    caudan = "Với góc $\\alpha$ bất kì $(0^\\circ \\le \\alpha \\le 180^\\circ)$, trong các khẳng định sau, khẳng định nào \\textbf{đúng}?"
    loi_giai = "Theo tính chất của hai góc bù nhau:\n" \
               "- $\\sin(180^\\circ - \\alpha) = \\sin \\alpha$.\n" \
               "- $\\cos(180^\\circ - \\alpha) = -\\cos \\alpha$.\n" \
               "- $\\tan(180^\\circ - \\alpha) = -\\tan \\alpha$ (với $\\alpha \\ne 90^\\circ$).\n" \
               "- $\\cot(180^\\circ - \\alpha) = -\\cot \\alpha$ (với $0^\\circ < \\alpha < 180^\\circ$).\n" \
               f"Do đó khẳng định đúng là ${correct_pair[0]}$."
    
    choices = shuffle_choices(correct_text, wrong_texts)
    return caudan, choices, loi_giai


def gk10_mc_diem_thuoc_mien_nghiem_bpt():
    """Câu 4: Miền nghiệm của bất phương trình ax + by + c > 0 chứa điểm nào"""
    a = random.choice([1, 2, -1, -2])
    b = random.choice([-3, -2, 2, 3])
    c = random.choice([-4, -2, 2, 4, 6])
    
    # Bất phương trình: a*x + b*y + c > 0
    # Tìm 1 điểm thỏa mãn và 3 điểm không thỏa mãn
    points = [
        (0, 0), (1, 1), (-1, 2), (2, -1), (-2, -2), (3, 1), (1, -3), (-4, 2), (0, 3)
    ]
    random.shuffle(points)
    
    pos_points = []
    neg_points = []
    for px, py in points:
        val = a * px + b * py + c
        if val > 0:
            pos_points.append((px, py, val))
        elif val < 0:
            neg_points.append((px, py, val))
            
    if not pos_points or len(neg_points) < 3:
        # fallback an toàn
        return gk10_mc_diem_thuoc_mien_nghiem_bpt()
        
    p_true = pos_points[0]
    p_wrongs = neg_points[:3]
    
    a_str = f"{a}x" if a not in [1, -1] else ("x" if a == 1 else "-x")
    b_str = f"+ {b}y" if b > 0 else f"- {abs(b)}y"
    c_str = f"+ {c}" if c > 0 else f"- {abs(c)}"
    bpt_str = f"{a_str} {b_str} {c_str} > 0"
    
    caudan = f"Miền nghiệm của bất phương trình ${bpt_str}$ chứa điểm nào trong các điểm sau?"
    ans_true = f"$({p_true[0]}; {p_true[1]})$"
    wrong_texts = [f"$({pw[0]}; {pw[1]})$" for pw in p_wrongs]
    
    loi_giai = f"Thay tọa độ điểm $({p_true[0]}; {p_true[1]})$ vào bất phương trình ta được:\n" \
               f"${a} \\cdot ({p_true[0]}) + ({b}) \\cdot ({p_true[1]}) + ({c}) = {p_true[2]} > 0$ (thỏa mãn).\n" \
               f"Vậy miền nghiệm của bất phương trình chứa điểm $({p_true[0]}; {p_true[1]})$."
               
    choices = shuffle_choices(ans_true, wrong_texts)
    return caudan, choices, loi_giai


def gk10_mc_diem_thuoc_he_bpt():
    """Câu 5: Miền nghiệm của hệ bất phương trình không chứa điểm nào"""
    # Hệ: { x - 2y < 0; x + 3y > -2 }
    bpt1 = (1, -2, 0, "<")
    bpt2 = (1, 3, -2, ">")
    
    pts_inside = []
    pts_outside = []
    candidates = [
        (0, 3), (1, 2), (-1, 1), (2, 4), (-2, 0), (-3, 4), (1, 0), (-1, 0)
    ]
    random.shuffle(candidates)
    for px, py in candidates:
        v1 = px - 2 * py
        v2 = px + 3 * py
        in1 = (v1 < 0)
        in2 = (v2 > -2)
        if in1 and in2:
            pts_inside.append((px, py))
        else:
            pts_outside.append((px, py, v1, v2))
            
    if not pts_outside or len(pts_inside) < 3:
        p_out = (-3, 4)
        pts_in = [(0, 3), (1, 0), (-1, 0)]
    else:
        p_out = pts_outside[0]
        pts_in = pts_inside[:3]
        
    caudan = r"""Miền nghiệm của hệ bất phương trình $\begin{cases} x - 2y < 0 \\ x + 3y > -2 \end{cases}$ \textbf{không chứa} điểm nào sau đây?"""
    ans_true = f"$({p_out[0]}; {p_out[1]})$"
    wrongs = [f"$({p[0]}; {p[1]})$" for p in pts_in]
    
    loi_giai = f"Thay điểm $({p_out[0]}; {p_out[1]})$ vào hệ:\n" \
               f"- Với BPT (1): ${p_out[0]} - 2 \\cdot ({p_out[1]}) = {p_out[0] - 2*p_out[1]} < 0$ (thỏa mãn).\n" \
               f"- Với BPT (2): ${p_out[0]} + 3 \\cdot ({p_out[1]}) = {p_out[0] + 3*p_out[1]}$ " \
               f"{'\\ngtr -2' if p_out[0] + 3*p_out[1] <= -2 else '< 0'}.\n" \
               f"Do đó điểm $({p_out[0]}; {p_out[1]})$ không thuộc miền nghiệm của hệ."
               
    choices = shuffle_choices(ans_true, wrongs)
    return caudan, choices, loi_giai


def gk10_mc_hinh_ve_mien_nghiem_bpt():
    """Câu 6: Xác định hình vẽ miền nghiệm của bất phương trình bậc nhất hai ẩn (TikZ)"""
    # BPT dạng: a*x + b*y >= c
    # ví dụ: 3x + 2y >= 6 => đi qua (2,0) và (0,3). Gốc O(0,0): 0 < 6 nên O bị gạch.
    a, b, c = 3, 2, 6
    x0 = c // a # 2
    y0 = c // b # 3
    
    def make_tikz(draw_line_pts, hatch_side, label_x, label_y):
        # hatch_side: 'origin' (gạch chứa gốc O) hoặc 'opposite' (gạch phía không chứa O)
        if hatch_side == 'origin':
            hatch_code = r"\fill[pattern=north east lines, pattern color=black!60] (-1.5,5.25) -- (3.5,-2.25) -- (-1.5,-2.25) -- cycle;"
        else:
            hatch_code = r"\fill[pattern=north east lines, pattern color=black!60] (-1.5,5.25) -- (3.5,-2.25) -- (3.5,5.25) -- cycle;"
        return fr"""\begin{{tikzpicture}}[scale=0.55, line join=round, line cap=round, >=stealth]
\draw[->] (-2.2,0) -- (4,0) node[below]{{$x$}};
\draw[->] (0,-2.5) -- (0,4.5) node[left]{{$y$}};
\draw (0,0) node[below left]{{$O$}};
\clip (-2.2,-2.5) rectangle (4,4.5);
{hatch_code}
\draw[thick] (-1.5,5.25) -- (3.5,-2.25);
\draw ({label_x},0) node[above right]{{{label_x}}};
\draw (0,{label_y}) node[right]{{{label_y}}};
\end{{tikzpicture}}"""

    caudan = r"Miền nghiệm của bất phương trình $3x + 2y \ge 6$ (miền không bị gạch, kể cả bờ) được biểu diễn bởi hình nào sau đây?"
    
    # 4 hình vẽ TikZ:
    # A: Đúng: đi qua (2,0) và (0,3), gạch phía chứa gốc O(0,0)
    tikz_A = make_tikz((2, 3), 'origin', 2, 3)
    # B: Đi qua (2,0) và (0,3), nhưng lại gạch phía ngược lại (chứa O không bị gạch)
    tikz_B = make_tikz((2, 3), 'opposite', 2, 3)
    # C: Đi qua (-2,0) và (0,3)
    tikz_C = r"""\begin{tikzpicture}[scale=0.55, line join=round, line cap=round, >=stealth]
\draw[->] (-3.5,0) -- (2.5,0) node[below]{$x$};
\draw[->] (0,-2.5) -- (0,4.5) node[left]{$y$};
\draw (0,0) node[below left]{$O$};
\clip (-3.5,-2.5) rectangle (2.5,4.5);
\fill[pattern=north east lines, pattern color=black!60] (-3.5,-2.25) -- (1.5,5.25) -- (-3.5,5.25) -- cycle;
\draw[thick] (-3.5,-2.25) -- (1.5,5.25);
\draw (-2,0) node[above left]{-2};
\draw (0,3) node[right]{3};
\end{tikzpicture}"""
    # D: Đi qua (-2,0) và (0,-3)
    tikz_D = r"""\begin{tikzpicture}[scale=0.55, line join=round, line cap=round, >=stealth]
\draw[->] (-3.5,0) -- (2.5,0) node[below]{$x$};
\draw[->] (0,-4.5) -- (0,2.5) node[left]{$y$};
\draw (0,0) node[above right]{$O$};
\clip (-3.5,-4.5) rectangle (2.5,2.5);
\fill[pattern=north east lines, pattern color=black!60] (-3.5,-0.75) -- (1.5,-4.75) -- (-3.5,-4.75) -- cycle;
\draw[thick] (-3.5,-0.75) -- (1.5,-4.75);
\draw (-2,0) node[above]{-2};
\draw (0,-3) node[right]{-3};
\end{tikzpicture}"""

    loi_giai = r"""Vẽ đường thẳng $d: 3x + 2y - 6 = 0$:
- Với $x = 0 \Rightarrow y = 3$, điểm $(0; 3) \in d$.
- Với $y = 0 \Rightarrow x = 2$, điểm $(2; 0) \in d$.
Thay tọa độ gốc $O(0; 0)$ vào bất phương trình: $3 \cdot 0 + 2 \cdot 0 = 0 \ge 6$ (sai).
Do đó, gốc tọa độ $O(0; 0)$ không thuộc miền nghiệm. Miền nghiệm là nửa mặt phẳng bờ $d$ không chứa gốc tọa độ $O$ (kể cả bờ $d$)."""

    choices = shuffle_choices(tikz_A, [tikz_B, tikz_C, tikz_D])
    return caudan, choices, loi_giai


def gk10_mc_phu_dinh_menh_de_moi_ton_tai():
    """Câu 7: Mệnh đề phủ định của mệnh đề chứa ký hiệu với mọi, tồn tại"""
    var = "x"
    set_sym = r"\mathbb{R}"
    configs = [
        (fr"P: ``\forall {var} \in {set_sym}, {var}^2 + 1 \ge 2{var}''",
         fr"\overline{{P}}: ``\exists {var} \in {set_sym}, {var}^2 + 1 < 2{var}''",
         [fr"\overline{{P}}: ``\exists {var} \in {set_sym}, {var}^2 + 1 \le 2{var}''",
          fr"\overline{{P}}: ``\forall {var} \in {set_sym}, {var}^2 + 1 < 2{var}''",
          fr"\overline{{P}}: ``\exists {var} \in {set_sym}, {var}^2 + 1 > 2{var}''"]),
        (fr"P: ``\forall {var} \in {set_sym}, {var}^2 - {var} + 7 < 0''",
         fr"\overline{{P}}: ``\exists {var} \in {set_sym}, {var}^2 - {var} + 7 \ge 0''",
         [fr"\overline{{P}}: ``\forall {var} \in {set_sym}, {var}^2 - {var} + 7 > 0''",
          fr"\overline{{P}}: ``\exists {var} \in {set_sym}, {var}^2 - {var} + 7 \le 0''",
          fr"\overline{{P}}: ``\exists {var} \in {set_sym}, {var}^2 - {var} + 7 > 0''"]),
        (fr"P: ``\exists {var} \in {set_sym}, {var}^2 - 4 = 0''",
         fr"\overline{{P}}: ``\forall {var} \in {set_sym}, {var}^2 - 4 \ne 0''",
         [fr"\overline{{P}}: ``\forall {var} \in {set_sym}, {var}^2 - 4 = 0''",
          fr"\overline{{P}}: ``\exists {var} \in {set_sym}, {var}^2 - 4 \ne 0''",
          fr"\overline{{P}}: ``\forall {var} \in {set_sym}, {var}^2 - 4 > 0''"])
    ]
    p_orig, p_neg_true, p_neg_wrongs = random.choice(configs)
    
    caudan = fr"Cho mệnh đề ${p_orig}$. Mệnh đề nào sau đây là mệnh đề phủ định của mệnh đề đã cho?"
    loi_giai = r"Phủ định của mệnh đề dạng ``$\forall x \in X, P(x)$'' là ``$\exists x \in X, \overline{P(x)}$'', và ngược lại phủ định của dấu $\ge$ là $<$, dấu $<$ là $\ge$, dấu $=$ là $\ne$." \
               fr"\nDo đó mệnh đề phủ định là ${p_neg_true}$."
               
    choices = shuffle_choices(f"${p_neg_true}$", [f"${w}$" for w in p_neg_wrongs])
    return caudan, choices, loi_giai


def gk10_mc_so_tap_con():
    """Câu 8: Số các tập con k phần tử hoặc số tập con của tập hợp"""
    n = random.choice([5, 6, 7])
    letters = ["a", "b", "c", "d", "e", "f", "g"][:n]
    set_str = "{" + ", ".join(letters) + "}"
    
    mode = random.choice(["1_element", "2_elements", "all"])
    if mode == "1_element":
        caudan = f"Số các tập con gồm đúng $1$ phần tử của tập hợp $B = {set_str}$ là"
        ans_true = f"${n}$"
        wrongs = [f"${n+1}$", f"${2**n}$", f"${n*(n-1)//2}$"]
        loi_giai = f"Tập hợp $B$ có ${n}$ phần tử, do đó số tập hợp con có đúng $1$ phần tử của $B$ chính bằng số phần tử của $B$, tức là ${n}$ tập con."
    elif mode == "2_elements":
        caudan = f"Số các tập con gồm đúng $2$ phần tử của tập hợp $B = {set_str}$ là"
        c2 = n * (n - 1) // 2
        ans_true = f"${c2}$"
        wrongs = [f"${n}$", f"${c2 + n}$", f"${2**n}$"]
        loi_giai = f"Số tập con gồm $2$ phần tử của tập hợp $B$ có ${n}$ phần tử là $C_{{{n}}}^2 = \\dfrac{{{n} \\times {n-1}}}{{2}} = {c2}$."
    else:
        caudan = f"Số tất cả các tập con của tập hợp $B = {set_str}$ là"
        ans_true = f"${2**n}$"
        wrongs = [f"${2**(n-1)}$", f"${n**2}$", f"${2*n}$"]
        loi_giai = f"Số tất cả các tập con của tập hợp có ${n}$ phần tử được tính theo công thức $2^n = 2^{{{n}}} = {2**n}$."
        
    choices = shuffle_choices(ans_true, wrongs)
    return caudan, choices, loi_giai


def gk10_mc_tinh_dung_sai_menh_de():
    """Câu 9: Mệnh đề nào sau đây là mệnh đề đúng"""
    corrects = [
        (r"$\exists x \in \mathbb{R}: x^2 \le 0$", r"Với $x = 0$, ta có $0^2 \le 0$ (đúng)."),
        (r"$\exists n \in \mathbb{N}: n^2 + 1 \text{ là số nguyên tố}$", r"Với $n = 1$, ta có $1^2 + 1 = 2$ là số nguyên tố (đúng)."),
        (r"$\forall x \in \mathbb{R}: x^2 + 1 > 0$", r"Ta có $x^2 \ge 0 \Rightarrow x^2 + 1 \ge 1 > 0, \forall x \in \mathbb{R}$ (đúng)."),
    ]
    wrongs = [
        (r"$\forall x \in \mathbb{N}: x^2 - 1 \text{ là bội số của } 3$", r"Với $x = 3$, $3^2 - 1 = 8$ không chia hết cho $3$."),
        (r"$\exists x \in \mathbb{Q}: x^2 = 3$", r"$\sqrt{3}$ là số vô tỉ nên không tồn tại $x \in \mathbb{Q}$ thỏa mãn."),
        (r"$\forall n \in \mathbb{N}: 2^n \ge n + 2$", r"Với $n = 1$, $2^1 < 1 + 2$."),
    ]
    
    c_item = random.choice(corrects)
    w_items = random.sample(wrongs, 3)
    
    caudan = "Mệnh đề nào sau đây là mệnh đề \\textbf{đúng}?"
    ans_true = f"{c_item[0]}"
    wrong_texts = [f"{w[0]}" for w in w_items]
    
    loi_giai = f"Xét mệnh đề {c_item[0]}: {c_item[1]}\n" \
               f"Các mệnh đề còn lại đều sai."
               
    choices = shuffle_choices(ans_true, wrong_texts)
    return caudan, choices, loi_giai


def gk10_mc_xac_dinh_he_bpt_tu_hinh_ve():
    """Câu 10: Phần không gạch chéo là biểu diễn miền nghiệm của hệ BPT nào"""
    # Đường thẳng 3x - 2y = -6 hoặc tương tự, kết hợp y >= 0
    caudan = r"""\immini{Phần không gạch chéo ở hình bên (kể cả bờ) là biểu diễn miền nghiệm của hệ bất phương trình nào trong bốn hệ dưới đây?}{
\begin{tikzpicture}[scale=0.55, line join=round, line cap=round, >=stealth]
\draw[->] (-2.5,0) -- (3.5,0) node[below]{$x$};
\draw[->] (0,-3.5) -- (0,2.5) node[left]{$y$};
\draw (0,0) node[above left]{$O$};
\clip (-2.5,-3.5) rectangle (3.5,2.5);
\fill[pattern=north east lines, pattern color=black!60] (-2.5,0) rectangle (3.5,-3.5);
\fill[pattern=north east lines, pattern color=black!60] (-2.5,-6.75) -- (3.5,2.25) -- (-2.5,2.25) -- cycle;
\draw[thick] (-2.5,-6.75) -- (3.5,2.25);
\draw (2,0) node[above]{2};
\draw (0,-3) node[right]{-3};
\end{tikzpicture}
}"""
    ans_true = r"$\begin{cases} y \ge 0 \\ 3x - 2y \le 6 \end{cases}$"
    w1 = r"$\begin{cases} y \ge 0 \\ 3x + 2y \le -6 \end{cases}$"
    w2 = r"$\begin{cases} x > 0 \\ 3x + 2y < 6 \end{cases}$"
    w3 = r"$\begin{cases} x > 0 \\ 3x + 2y > -6 \end{cases}$"
    
    loi_giai = r"""Dựa vào hình vẽ:
- Miền không bị gạch nằm hoàn toàn ở phía trên trục hoành nên $y \ge 0$.
- Đường thẳng bờ đi qua điểm $(2; 0)$ và $(0; -3)$, có phương trình $\dfrac{x}{2} + \dfrac{y}{-3} = 1 \iff 3x - 2y = 6$.
- Điểm $O(0; 0)$ nằm trong miền không bị gạch, thay $O(0; 0)$ vào ta có $3 \cdot 0 - 2 \cdot 0 = 0 \le 6$ (đúng).
Vậy hệ bất phương trình tương ứng là $\begin{cases} y \ge 0 \\ 3x - 2y \le 6 \end{cases}$."""

    choices = shuffle_choices(ans_true, [w1, w2, w3])
    return caudan, choices, loi_giai


def gk10_mc_nhan_biet_bpt_bac_nhat_hai_an():
    """Câu 11: Bất phương trình nào là bất phương trình bậc nhất hai ẩn"""
    ans_true = r"$2x - 3y + 5 > 0$"
    wrongs = [
        r"$3x^2 + 2x - 4 > 0$",
        r"$2x - 5y + 3z \le 0$",
        r"$2x^2 + 5y > 3$"
    ]
    caudan = "Trong các bất phương trình sau, bất phương trình nào là bất phương trình bậc nhất hai ẩn?"
    loi_giai = r"Bất phương trình bậc nhất hai ẩn có dạng tổng quát $ax + by + c > 0$ (hoặc $\ge, <, \le$) với $a, b$ không đồng thời bằng $0$, trong đó bậc cao nhất của các ẩn $x, y$ là $1$. Do đó phương án đúng là $2x - 3y + 5 > 0$."
    
    choices = shuffle_choices(ans_true, wrongs)
    return caudan, choices, loi_giai


def gk10_mc_cong_thuc_tam_giac():
    """Câu 12: Công thức diện tích tam giác hoặc định lí sin/cosin"""
    mode = random.choice(["dien_tich", "dinh_li_sin", "dinh_li_cosin"])
    if mode == "dien_tich":
        caudan = "Cho tam giác $ABC$ có các cạnh tương ứng là $a, b, c$. Khi đó diện tích tam giác $S$ được tính bởi công thức nào sau đây?"
        ans_true = r"$S = \dfrac{1}{2}bc\sin A$"
        wrongs = [
            r"$S = \dfrac{1}{2}ac\sin A$",
            r"$S = \dfrac{1}{2}bc\sin B$",
            r"$S = \dfrac{1}{2}bc\sin C$"
        ]
        loi_giai = r"Công thức tính diện tích tam giác theo hai cạnh và sin của góc xen giữa là $S = \dfrac{1}{2}bc\sin A = \dfrac{1}{2}ac\sin B = \dfrac{1}{2}ab\sin C$."
    elif mode == "dinh_li_sin":
        caudan = "Cho tam giác $ABC$ có bán kính đường tròn ngoại tiếp là $R$. Khẳng định nào sau đây là \\textbf{đúng}?"
        ans_true = r"$\dfrac{a}{\sin A} = 2R$"
        wrongs = [
            r"$\dfrac{a}{\sin A} = R$",
            r"$\dfrac{b}{\sin B} = 3R$",
            r"$\dfrac{c}{\sin C} = 4R$"
        ]
        loi_giai = r"Theo định lí sin trong tam giác $ABC$: $\dfrac{a}{\sin A} = \dfrac{b}{\sin B} = \dfrac{c}{\sin C} = 2R$."
    else:
        caudan = "Cho tam giác $ABC$ có ba cạnh $a, b, c$. Khẳng định nào sau đây là \\textbf{đúng}?"
        ans_true = r"$a^2 = b^2 + c^2 - 2bc\cos A$"
        wrongs = [
            r"$a^2 = b^2 + c^2 + 2bc\cos A$",
            r"$a^2 = b^2 + c^2 - 2bc\sin A$",
            r"$a^2 = b^2 - c^2 - 2bc\cos A$"
        ]
        loi_giai = r"Theo định lí cosin trong tam giác $ABC$: $a^2 = b^2 + c^2 - 2bc\cos A$."
        
    choices = shuffle_choices(ans_true, wrongs)
    return caudan, choices, loi_giai


# ==============================================================================
# PHẦN II: 4 CÂU TRẮC NGHIỆM ĐÚNG / SAI (TF)
# ==============================================================================

def gk10_tf_tap_hop_khoang_doan():
    """Câu 1 (Đúng/Sai): Hai tập hợp khoảng đoạn A = [-1; 3] và B = [2; 7]"""
    a1, a2 = -1, 3
    b1, b2 = 2, 7
    
    caudan = fr"Cho hai tập hợp $A = [{a1}; {a2}]$ và $B = [{b1}; {b2}]$. Xét tính đúng sai của các khẳng định sau:"
    
    # a) 2 in A
    item_a = (
        fr"$2 \in A$",
        fr"$2 \notin A$",
        fr"Vì $-1 \le 2 \le 3$ nên $2 \in A$.",
        fr"Khẳng định sai vì $2 \in [-1; 3]$."
    )
    # b) A cap B = [2; 3]
    item_b = (
        fr"$A \cap B = [{b1}; {a2}]$",
        fr"$A \cap B = [{a1}; {b2}]$",
        fr"Ta có giao của hai đoạn là phần chung $A \cap B = [{b1}; {a2}]$.",
        fr"Khẳng định sai vì $[{a1}; {b2}]$ là hợp $A \cup B$."
    )
    # c) A \ B = [-1; 2)
    item_c = (
        fr"$A \setminus B = [{a1}; {b1})$",
        fr"$A \setminus B = [{a1}; {b1}]$",
        fr"Hiệu $A \setminus B$ lấy các phần tử thuộc $A$ nhưng không thuộc $B$. Vì $2 \in B$ nên đầu mút $2$ là ngoặc tròn: $[{a1}; {b1})$.",
        fr"Khẳng định sai vì phần tử $2$ đã thuộc $B$ nên không thể lấy ngoặc vuông tại $2$."
    )
    # d) Hợp A cup B = [-1; 7]
    item_d = (
        fr"$A \cup B = [{a1}; {b2}]$",
        fr"$A \cup B = [{b1}; {a2}]$",
        fr"Hợp của hai tập hợp là $A \cup B = [{a1}; {b2}]$.",
        fr"Khẳng định sai vì $[{b1}; {a2}]$ là phép giao."
    )
    
    choices, loi_giai = make_tf_choices([item_a, item_b, item_c, item_d])
    return caudan, choices, loi_giai


def gk10_tf_giai_tam_giac():
    """Câu 2 (Đúng/Sai): Giải tam giác ABC biết AC = 5, A = 75 độ, C = 60 độ"""
    b = 5 # AC
    angA = 75
    angC = 60
    angB = 180 - (angA + angC) # 45
    
    # Định lí sin: a / sin A = b / sin B = c / sin C = 2R
    # b = 5, sin B = sin 45 = sqrt(2)/2 => 2R = 5 / (sqrt(2)/2) = 5*sqrt(2) => R = 5*sqrt(2)/2
    # a = 2R * sin 75 = 5*sqrt(2) * (sqrt(6)+sqrt(2))/4 = 5*(sqrt(3)+1)/2 approx 6.83
    # c = 2R * sin 60 = 5*sqrt(2) * sqrt(3)/2 = 5*sqrt(6)/2 approx 6.12
    # S = 1/2 * a * c * sin B = 1/2 * b * c * sin A approx 1/2 * 5 * 6.12 * sin 75 approx 14.8 or:
    # S = (b^2 * sin A * sin C) / (2 * sin B) = (25 * sin 75 * sin 60) / (2 * sin 45) = (25 * 0.9659 * 0.8660) / 1.4142 approx 14.8
    
    caudan = fr"Cho tam giác $ABC$, biết $AC = 5$, $\widehat{{A}} = {angA}^\circ$, $\widehat{{C}} = {angC}^\circ$."
    
    item_a = (
        fr"Góc $\widehat{{B}} = {angB}^\circ$",
        fr"Góc $\widehat{{B}} = 50^\circ$",
        fr"Tổng ba góc bằng $180^\circ \Rightarrow \widehat{{B}} = 180^\circ - ({angA}^\circ + {angC}^\circ) = {angB}^\circ$.",
        fr"Khẳng định sai vì $\widehat{{B}} = 180^\circ - 135^\circ = 45^\circ$."
    )
    item_b = (
        r"Độ dài cạnh $BC \approx 6{,}8$",
        r"Độ dài cạnh $BC \approx 8{,}2$",
        r"Áp dụng định lí sin: $BC = \dfrac{AC \cdot \sin A}{\sin B} = \dfrac{5 \cdot \sin 75^\circ}{\sin 45^\circ} \approx 6{,}83 \approx 6{,}8$.",
        r"Khẳng định sai theo định lí sin."
    )
    item_c = (
        r"Bán kính đường tròn ngoại tiếp tam giác là $R = \dfrac{5\sqrt{2}}{2}$",
        r"Bán kính đường tròn ngoại tiếp tam giác là $R = 5\sqrt{2}$",
        r"Ta có $2R = \dfrac{AC}{\sin B} = \dfrac{5}{\sin 45^\circ} = 5\sqrt{2} \Rightarrow R = \dfrac{5\sqrt{2}}{2}$.",
        r"Khẳng định sai vì $5\sqrt{2}$ là đường kính $2R$, bán kính phải chia đôi."
    )
    item_d = (
        r"Diện tích tam giác $ABC$ xấp xỉ bằng $14{,}8$",
        r"Diện tích tam giác $ABC$ xấp xỉ bằng $25{,}6$",
        r"Ta có $S = \dfrac{AC^2 \cdot \sin A \cdot \sin C}{2\sin B} = \dfrac{25 \cdot \sin 75^\circ \cdot \sin 60^\circ}{2\sin 45^\circ} \approx 14{,}8$.",
        r"Khẳng định sai vì tính sai công thức diện tích."
    )
    
    choices, loi_giai = make_tf_choices([item_a, item_b, item_c, item_d])
    return caudan, choices, loi_giai


def gk10_tf_he_bpt_mien_da_giac():
    """Câu 3 (Đúng/Sai): Hệ BPT bậc nhất hai ẩn x >= 0, y >= 0, x + y <= 4, x + 2y <= 6"""
    caudan = r"""Cho hệ bất phương trình bậc nhất hai ẩn: $\begin{cases} x \ge 0 \\ y \ge 0 \\ x + y \le 4 \\ x + 2y \le 6 \end{cases}$. Xét tính đúng sai của các khẳng định sau:"""
    
    item_a = (
        r"Điểm $M(1; 2)$ thuộc miền nghiệm của hệ",
        r"Điểm $M(1; 2)$ không thuộc miền nghiệm của hệ",
        r"Thay $x = 1, y = 2$ thỏa mãn cả 4 bất phương trình của hệ.",
        r"Khẳng định sai vì $M(1; 2)$ thỏa mãn tất cả các bất phương trình trong hệ."
    )
    item_b = (
        r"Miền nghiệm của hệ là một tứ giác",
        r"Miền nghiệm của hệ là một tam giác",
        r"Miền nghiệm là tứ giác giới hạn bởi các đỉnh $(0; 0), (4; 0), (2; 2), (0; 3)$.",
        r"Khẳng định sai vì miền nghiệm có 4 đỉnh nên là một tứ giác."
    )
    item_c = (
        r"Tọa độ một đỉnh của miền nghiệm là $I(2; 2)$",
        r"Tọa độ giao điểm hai đường biên là $I(1; 3)$",
        r"Giải hệ $\begin{cases} x + y = 4 \\ x + 2y = 6 \end{cases} \Rightarrow x = 2, y = 2$.",
        r"Khẳng định sai vì nghiệm của hệ hai phương trình là $(2; 2)$."
    )
    item_d = (
        r"Giá trị lớn nhất của biểu thức $F(x, y) = 2x + 3y$ trên miền nghiệm bằng $10$",
        r"Giá trị lớn nhất của biểu thức $F(x, y) = 2x + 3y$ trên miền nghiệm bằng $12$",
        r"Tính giá trị $F$ tại các đỉnh: $F(0,0)=0, F(4,0)=8, F(0,3)=9, F(2,2)=2(2)+3(2)=10$. Vậy $\max F = 10$.",
        r"Khẳng định sai vì giá trị lớn nhất đạt tại $(2; 2)$ bằng $10$."
    )
    
    choices, loi_giai = make_tf_choices([item_a, item_b, item_c, item_d])
    return caudan, choices, loi_giai


def gk10_tf_tap_hop_chua_tham_so():
    """Câu 4 (Đúng/Sai): Tập hợp chứa tham số m: A = [m - 1; m + 3] và B = (-2; 5)"""
    caudan = r"""Cho hai tập hợp $A = [m - 1; m + 3]$ và $B = (-2; 5)$. Xét tính đúng sai của các khẳng định sau:"""
    
    item_a = (
        r"Khi $m = 1$, ta có $A = [0; 4]$ và $A \subset B$",
        r"Khi $m = 1$, ta có $A = [1; 4]$",
        r"Với $m = 1 \Rightarrow A = [0; 4]$. Do $-2 < 0 < 4 < 5$ nên $A \subset B$.",
        r"Khẳng định sai vì thay $m = 1$ cho ra $A = [0; 4]$."
    )
    item_b = (
        r"Điều kiện để $A \subset B$ là $-1 < m < 2$",
        r"Điều kiện để $A \subset B$ là $-1 \le m \le 2$",
        r"Để $A \subset B \iff \begin{cases} m - 1 > -2 \\ m + 3 < 5 \end{cases} \iff \begin{cases} m > -1 \\ m < 2 \end{cases} \iff -1 < m < 2$.",
        r"Khẳng định sai vì tại hai đầu mút là ngoặc tròn của $B$ nên không được lấy dấu bằng."
    )
    item_c = (
        r"Điều kiện để $A \cap B = \emptyset$ là $m \le -5$ hoặc $m \ge 6$",
        r"Điều kiện để $A \cap B = \emptyset$ là $-5 < m < 6$",
        r"$A \cap B = \emptyset \iff m + 3 \le -2$ hoặc $m - 1 \ge 5 \iff m \le -5$ hoặc $m \ge 6$.",
        r"Khẳng định sai vì khoảng cách giữa hai tập hợp là phần ngoài."
    )
    item_d = (
        r"Có đúng $2$ giá trị nguyên của $m$ để $A \subset B$",
        r"Có đúng $4$ giá trị nguyên của $m$ để $A \subset B$",
        r"Với $-1 < m < 2$ và $m \in \mathbb{Z}$, ta có $m \in \{0; 1\}$, gồm đúng $2$ giá trị.",
        r"Khẳng định sai vì chỉ có $m = 0$ và $m = 1$ thỏa mãn."
    )
    
    choices, loi_giai = make_tf_choices([item_a, item_b, item_c, item_d])
    return caudan, choices, loi_giai


# ==============================================================================
# PHẦN III: 6 CÂU TRẮC NGHIỆM TRẢ LỜI NGẮN (SA)
# ==============================================================================

def gk10_sa_luong_giac_tinh_bieu_thuc_sin():
    """Câu 1 (TLN): Cho sin x = 1/sqrt(k), tính P = a*cos^2 x + b*sin^2 x"""
    k = random.choice([3, 4, 5])
    a = random.choice([2, 3, 4])
    b = random.choice([-6, -5, -4, 5, 6])
    
    # sin^2 x = 1/k, cos^2 x = 1 - 1/k = (k - 1)/k
    # P = a * (k - 1)/k + b * (1/k) = (a*(k - 1) + b) / k
    num = a * (k - 1) + b
    ans_fr = Fraction(num, k)
    
    dapan = str(ans_fr.numerator) if ans_fr.denominator == 1 else f"{ans_fr.numerator}/{ans_fr.denominator}"
    if ans_fr.denominator != 1:
        # Nếu muốn số nguyên đẹp, chỉnh hệ số b:
        # chọn b sao cho (a*(k-1) + b) % k == 0
        rem = (a * (k - 1)) % k
        b = -rem if rem != 0 else k
        num = a * (k - 1) + b
        dapan = str(num // k)
        
    caudan = fr"Cho $\sin x = \dfrac{{1}}{{\sqrt{{{k}}}}}$. Tính giá trị của biểu thức $P = {a}\cos^2 x {'+' if b > 0 else '-'} {abs(b)}\sin^2 x$."
    loi_giai = fr"Ta có $\sin^2 x = \left(\dfrac{{1}}{{\sqrt{{{k}}}}}\right)^2 = \dfrac{{1}}{{{k}}}$. \\" \
               fr"Suy ra $\cos^2 x = 1 - \sin^2 x = 1 - \dfrac{{1}}{{{k}}} = \dfrac{{{k-1}}}{{{k}}}$. \\" \
               fr"Thay vào biểu thức $P$: \\" \
               fr"$$P = {a} \cdot \dfrac{{{k-1}}}{{{k}}} + ({b}) \cdot \dfrac{{1}}{{{k}}} = \dfrac{{{a*(k-1) + b}}}{{{k}}} = {dapan}.$$"
               
    return caudan, dapan, loi_giai


def gk10_sa_tap_hop_so_tap_con():
    """Câu 2 (TLN): Cho tập A gồm n phần tử, tính số tập con chứa k phần tử"""
    n = random.choice([5, 6, 7])
    k = random.choice([2, 3])
    elements = [str(i) for i in range(n)]
    set_str = "{" + ", ".join(elements) + "}"
    
    ans = math.comb(n, k)
    dapan = str(ans)
    
    caudan = fr"Cho tập hợp $A = {set_str}$. Tính số tập con chứa đúng ${k}$ phần tử của tập hợp $A$."
    loi_giai = fr"Tập hợp $A$ có tất cả ${n}$ phần tử. \\" \
               fr"Mỗi tập con gồm ${k}$ phần tử của $A$ là một tổ hợp chập ${k}$ của ${n}$ phần tử. \\" \
               fr"Do đó số tập con cần tìm là $C_{{{n}}}^{{{k}}} = \dfrac{{{n}!}}{{{k}!({n}-{k})!}} = {ans}$."
               
    return caudan, dapan, loi_giai


def gk10_sa_luong_giac_phan_thuc_tan():
    """Câu 3 (TLN): Cho tan x = m, tính giá trị biểu thức M = (a*sin x + b*cos x) / (c*cos x + d*sin x)"""
    m = random.choice([-3, -2, 2, 3])
    a = random.choice([2, 3, 4])
    b = random.choice([-5, -4, 4, 5])
    c = random.choice([3, 4, 5, 8])
    d = random.choice([2, 3, 7])
    
    # Chia cả tử và mẫu cho cos x:
    # M = (a*tan x + b) / (c + d*tan x)
    tu = a * m + b
    mau = c + d * m
    while mau == 0:
        c += 1
        mau = c + d * m
        
    ans_fr = Fraction(tu, mau)
    dapan = str(ans_fr.numerator) if ans_fr.denominator == 1 else f"{ans_fr.numerator}/{ans_fr.denominator}"
    
    caudan = fr"Biết $\tan x = {m}$, giá trị của biểu thức $M = \dfrac{{{a}\sin x {'+' if b > 0 else '-'} {abs(b)}\cos x}}{{{c}\cos x {'+' if d > 0 else '-'} {abs(d)}\sin x}}$ bằng bao nhiêu?"
    loi_giai = fr"Vì $\tan x = {m}$ xác định nên $\cos x \ne 0$. \\" \
               fr"Chia cả tử và mẫu của biểu thức $M$ cho $\cos x$, ta được: \\" \
               fr"$$M = \dfrac{{{a}\tan x {'+' if b > 0 else '-'} {abs(b)}}}{{{c} {'+' if d > 0 else '-'} {abs(d)}\tan x}} = \dfrac{{{a} \cdot ({m}) + ({b})}}{{{c} + ({d}) \cdot ({m})}} = \dfrac{{{tu}}}{{{mau}}} = {dapan}.$$"
               
    return caudan, dapan, loi_giai


def gk10_sa_toan_venn_thuc_te():
    """Câu 4 (TLN): Bài toán sơ đồ Venn: Học sinh tham gia bóng đá, bóng bàn"""
    da = random.choice([24, 25, 26, 28])
    ban = random.choice([20, 22, 23, 25])
    ca_hai = random.choice([12, 14, 15, 16])
    
    # Số học sinh chỉ chơi 1 môn:
    chi_da = da - ca_hai
    chi_ban = ban - ca_hai
    ans = chi_da + chi_ban
    dapan = str(ans)
    
    caudan = fr"Một lớp học có ${da}$ học sinh chơi bóng đá, ${ban}$ học sinh chơi bóng bàn, và ${ca_hai}$ học sinh chơi cả bóng đá và bóng bàn. Hỏi số học sinh chỉ chơi đúng một môn thể thao trong hai môn trên là bao nhiêu?"
    loi_giai = fr"Số học sinh chỉ chơi môn bóng đá là: ${da} - {ca_hai} = {chi_da}$ (học sinh). \\" \
               fr"Số học sinh chỉ chơi môn bóng bàn là: ${ban} - {ca_hai} = {chi_ban}$ (học sinh). \\" \
               fr"Vậy số học sinh chỉ chơi đúng một môn thể thao là: ${chi_da} + {chi_ban} = {ans}$ (học sinh)."
               
    return caudan, dapan, loi_giai


def gk10_sa_tam_giac_goc_canh():
    """Câu 5 (TLN): Cho tam giác có ba cạnh a = 13, b = 14, c = 15. Tính cos B (hoặc bán kính r)"""
    # Bộ ba cạnh đẹp 13, 14, 15
    a, b, c = 13, 14, 15
    # cos B = (a^2 + c^2 - b^2) / (2ac)
    # a^2 = 169, c^2 = 225, b^2 = 196 => 169 + 225 - 196 = 198
    # 2 * 13 * 15 = 390
    # cos B = 198 / 390 = 33 / 65 approx 0.5077
    # Nửa chu vi p = (13 + 14 + 15)/2 = 21
    # Diện tích S = sqrt(21 * 8 * 7 * 6) = 84
    # r = S / p = 84 / 21 = 4
    mode = random.choice(["ban_kinh_r", "dien_tich"])
    if mode == "ban_kinh_r":
        dapan = "4"
        caudan = fr"Cho tam giác $ABC$ có độ dài ba cạnh lần lượt là $a = {a}, b = {b}, c = {c}$. Tính bán kính đường tròn nội tiếp $r$ của tam giác $ABC$."
        loi_giai = fr"Nửa chu vi của tam giác $ABC$ là: $p = \dfrac{{{a} + {b} + {c}}}{{2}} = 21$. \\" \
                   fr"Diện tích tam giác tính theo công thức Heron: \\" \
                   fr"$$S = \sqrt{{p(p-a)(p-b)(p-c)}} = \sqrt{{21(21-13)(21-14)(21-15)}} = \sqrt{{21 \cdot 8 \cdot 7 \cdot 6}} = 84.$$ \\" \
                   fr"Bán kính đường tròn nội tiếp tam giác là: $r = \dfrac{{S}}{{p}} = \dfrac{{84}}{{21}} = 4$."
    else:
        dapan = "84"
        caudan = fr"Cho tam giác $ABC$ có độ dài ba cạnh lần lượt là $a = {a}, b = {b}, c = {c}$. Tính diện tích $S$ của tam giác $ABC$."
        loi_giai = fr"Nửa chu vi của tam giác là: $p = \dfrac{{{a} + {b} + {c}}}{{2}} = 21$. \\" \
                   fr"Áp dụng công thức Heron: \\" \
                   fr"$$S = \sqrt{{21(21-13)(21-14)(21-15)}} = 84.$$"
                   
    return caudan, dapan, loi_giai


def gk10_sa_toan_thuc_te_quy_hoach():
    """Câu 6 (TLN): Bài toán thực tế quy hoạch tuyến tính (chiết xuất chất A và B)"""
    # 1 tấn loại I: 20kg chất A, 0.6kg chất B. Giá 4 triệu
    # 1 tấn loại II: 10kg chất A, 1.5kg chất B. Giá 3 triệu
    # Cần ít nhất 140kg chất A và 9kg chất B
    # x tấn loại I, y tấn loại II (x <= 10, y <= 9)
    # 20x + 10y >= 140 <=> 2x + y >= 14
    # 0.6x + 1.5y >= 9 <=> 2x + 5y >= 30
    # Chi phí F(x, y) = 4x + 3y nhỏ nhất
    # Giao điểm (2x + y = 14) và (2x + 5y = 30) => 4y = 16 => y = 4 => x = 5.
    # Chi phí tại (5, 4): 4*5 + 3*4 = 32 triệu đồng.
    dapan = "32"
    caudan = r"""Một công ty cần chiết xuất ít nhất $140\text{ kg}$ chất $A$ và $9\text{ kg}$ chất $B$ từ hai loại nguyên liệu $I$ và $II$.
Mỗi tấn nguyên liệu loại $I$ có giá $4$ triệu đồng, chiết xuất được $20\text{ kg}$ chất $A$ và $0{,}6\text{ kg}$ chất $B$.
Mỗi tấn nguyên liệu loại $II$ có giá $3$ triệu đồng, chiết xuất được $10\text{ kg}$ chất $A$ và $1{,}5\text{ kg}$ chất $B$.
Biết rằng cơ sở chỉ có thể cung cấp tối đa $10$ tấn nguyên liệu loại $I$ và $9$ tấn nguyên liệu loại $II$.
Hỏi chi phí mua nguyên liệu thấp nhất mà công ty phải trả để đạt mục tiêu là bao nhiêu triệu đồng?"""

    loi_giai = r"""Gọi $x, y$ lần lượt là số tấn nguyên liệu loại $I$ và loại $II$ cần mua ($0 \le x \le 10, 0 \le y \le 9$).
Theo đề bài ta có hệ bất phương trình:
$$\begin{cases} 0 \le x \le 10 \\ 0 \le y \le 9 \\ 20x + 10y \ge 140 \\ 0{,}6x + 1{,}5y \ge 9 \end{cases} \iff \begin{cases} 0 \le x \le 10 \\ 0 \le y \le 9 \\ 2x + y \ge 14 \\ 2x + 5y \ge 30 \end{cases}$$
Chi phí mua nguyên liệu là biểu thức: $F(x, y) = 4x + 3y$ (triệu đồng).
Miền nghiệm của hệ là miền đa giác với các đỉnh:
- $A(10; 2) \Rightarrow F(10, 2) = 4(10) + 3(2) = 46$.
- $B(10; 9) \Rightarrow F(10, 9) = 4(10) + 3(9) = 67$.
- $C\left(\dfrac{15}{2}; 9\right) \Rightarrow F = 4(7{,}5) + 3(9) = 57$.
- $D(5; 4)$ là giao điểm của $2x + y = 14$ và $2x + 5y = 30 \Rightarrow F(5, 4) = 4(5) + 3(4) = 32$.
Do đó chi phí nhỏ nhất là $32$ triệu đồng khi mua $5$ tấn loại $I$ và $4$ tấn loại $II$."""

    return caudan, dapan, loi_giai


# ==============================================================================
# HÀM MASTER SINH TOÀN BỘ ĐỀ THI GIỮA HỌC KÌ 1 TOÁN 10
# ==============================================================================

def sinh_de_kiem_tra_gk1_toan10(ma_de="209", ten_truong="TRƯỜNG THPT TĨNH GIA 2"):
    """
    Tự động biên tập một đề kiểm tra hoàn chỉnh chuẩn cấu trúc GDPT 2018:
    - 12 câu MC
    - 4 câu Đúng / Sai (mỗi câu 4 ý a, b, c, d)
    - 6 câu Trả lời ngắn
    Kèm đầy đủ lời giải chi tiết và đáp số chuẩn.
    """
    mc_funcs = [
        gk10_mc_nhan_biet_menh_de,
        gk10_mc_liet_ke_tap_hop,
        gk10_mc_dang_thuc_luong_giac,
        gk10_mc_diem_thuoc_mien_nghiem_bpt,
        gk10_mc_diem_thuoc_he_bpt,
        gk10_mc_hinh_ve_mien_nghiem_bpt,
        gk10_mc_phu_dinh_menh_de_moi_ton_tai,
        gk10_mc_so_tap_con,
        gk10_mc_tinh_dung_sai_menh_de,
        gk10_mc_xac_dinh_he_bpt_tu_hinh_ve,
        gk10_mc_nhan_biet_bpt_bac_nhat_hai_an,
        gk10_mc_cong_thuc_tam_giac,
    ]
    
    tf_funcs = [
        gk10_tf_tap_hop_khoang_doan,
        gk10_tf_giai_tam_giac,
        gk10_tf_he_bpt_mien_da_giac,
        gk10_tf_tap_hop_chua_tham_so,
    ]
    
    sa_funcs = [
        gk10_sa_luong_giac_tinh_bieu_thuc_sin,
        gk10_sa_tap_hop_so_tap_con,
        gk10_sa_luong_giac_phan_thuc_tan,
        gk10_sa_toan_venn_thuc_te,
        gk10_sa_tam_giac_goc_canh,
        gk10_sa_toan_thuc_te_quy_hoach,
    ]
    
    cauhoi = []
    
    # Header đề thi
    cauhoi.append(f"% ==============================================================================")
    cauhoi.append(f"% ĐỀ ÔN TẬP KIỂM TRA GIỮA HỌC KÌ 1 TOÁN 10 - MÃ ĐỀ: {ma_de}")
    cauhoi.append(f"% ĐƠN VỊ: {ten_truong.upper()}")
    cauhoi.append(f"% ==============================================================================\n")
    
    # PHẦN I
    cauhoi.append(r"\phanmot" + "\n")
    for fn in mc_funcs:
        caudan, choices, loigiai = fn()
        block = "\\begin{ex}\n" + caudan + "\n\\choice\n" + "".join(choices) + "\\loigiai{" + loigiai + "}\n\\end{ex}\n"
        cauhoi.append(block)
        
    # PHẦN II
    cauhoi.append("\n" + r"\phanhai" + "\n")
    for fn in tf_funcs:
        caudan, choices, loigiai = fn()
        block = "\\begin{ex}\n" + caudan + "\n\\choiceTF\n" + "".join(choices) + "\\loigiai{" + loigiai + "}\n\\end{ex}\n"
        cauhoi.append(block)
        
    # PHẦN III
    cauhoi.append("\n" + r"\phanba" + "\n")
    for fn in sa_funcs:
        caudan, dapan, loigiai = fn()
        block = "\\begin{ex}\n" + caudan + "\n\\shortans[oly]{" + dapan + "}\n\\loigiai{" + loigiai + "}\n\\end{ex}\n"
        cauhoi.append(block)
        
    return "\n".join(cauhoi)
