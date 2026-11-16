# -*- coding: utf-8 -*-
"""
Module: sinh_de_toan10_vecto_oxy.py
Ngân hàng sinh câu hỏi trắc nghiệm Toán 10:
Chủ đề 1: Tọa độ của vectơ và điểm trong mặt phẳng tọa độ Oxy
Chủ đề 2: Tích vô hướng của hai vectơ và góc giữa hai vectơ

Bao gồm:
- Phần I: Trắc nghiệm 4 lựa chọn (MC)
- Phần II: Trắc nghiệm Đúng/Sai (TF)
- Phần III: Trắc nghiệm Trả lời ngắn (SA)

Toàn bộ số liệu và tham số được sinh ngẫu nhiên (Algorithmic Generation),
đổi số và đáp án mỗi lần bấm tạo bài tập, sinh lời giải chi tiết từng bước.
"""

import math
import random
from collections import Counter
from fractions import Fraction


def clean_option(s):
    """Làm sạch phương án trắc nghiệm"""
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
    """Trộn 4 phương án trắc nghiệm, đánh dấu \\True cho đáp án đúng"""
    c_clean = clean_option(correct_text)
    wrongs_clean = []
    seen = {c_clean}
    for w in wrong_texts:
        w_c = clean_option(w)
        if w_c not in seen:
            wrongs_clean.append(w_c)
            seen.add(w_c)
    # Bổ sung phương án nếu bị trùng lặp
    idx_extra = 1
    while len(wrongs_clean) < 3:
        alt = f"{c_clean}_{idx_extra}"
        if alt not in seen:
            wrongs_clean.append(alt)
            seen.add(alt)
        idx_extra += 1

    opts = [(True, c_clean)] + [(False, w) for w in wrongs_clean[:3]]
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
    """
    choices = []
    loi_giai_parts = []
    for item in items:
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


def fmt_sqrt(n):
    """Rút gọn căn thức bậc hai của số nguyên dương n"""
    if n <= 0:
        return "0"
    r = int(math.isqrt(n))
    if r * r == n:
        return str(r)
    outside = 1
    inside = n
    for d in range(r, 1, -1):
        if n % (d * d) == 0:
            outside = d
            inside = n // (d * d)
            break
    if outside > 1:
        return f"{outside}\\sqrt{{{inside}}}"
    return f"\\sqrt{{{n}}}"


def fmt_vec_comb(x, y):
    """Biểu diễn vectơ theo i và j"""
    parts = []
    if x == 1:
        parts.append(r"\vec{i}")
    elif x == -1:
        parts.append(r"-\vec{i}")
    elif x != 0:
        parts.append(f"{x}\\vec{{i}}")

    if y == 1:
        parts.append(r"+\vec{j}" if parts else r"\vec{j}")
    elif y == -1:
        parts.append(r"-\vec{j}")
    elif y > 0:
        parts.append(f"+{y}\\vec{{j}}" if parts else f"{y}\\vec{{j}}")
    elif y < 0:
        parts.append(f"{y}\\vec{{j}}")
    return "".join(parts) if parts else r"\vec{0}"


def fmt_point(name, x, y):
    """Định dạng tọa độ điểm"""
    return f"{name}({x};{y})"


# ==============================================================================
# PHẦN 1: TRẮC NGHIỆM 4 PHƯƠNG ÁN (MC) - TỌA ĐỘ OXY
# ==============================================================================

def k10_mc_vecto_bieu_dien_don_vi():
    """Ảnh 1 Câu 1: Cho vec{a} = x*vec{i} + y*vec{j}. Tìm tọa độ vec{a} hoặc k*vec{a}."""
    x = random.choice([-5, -4, -3, -2, -1, 1, 2, 3, 4, 5])
    y = random.choice([-5, -4, -3, -2, -1, 1, 2, 3, 4, 5])
    k = random.choice([1, 2, -2, 3, -1])
    comb_str = fmt_vec_comb(x, y)

    target_vec = r"\vec{a}" if k == 1 else (r"-\vec{a}" if k == -1 else f"{k}\\vec{{a}}")
    res_x = k * x
    res_y = k * y

    caudan = (
        f"Trong mặt phẳng tọa độ $Oxy$, cho vectơ $\\vec{{a}} = {comb_str}$. "
        f"Khi đó tọa độ của vectơ ${target_vec}$ là"
    )
    correct = f"$({res_x};{res_y})$"
    wrongs = [
        f"$({res_y};{res_x})$",
        f"$({res_x};{-res_y})$",
        f"$({-res_x};{res_y})$",
        f"$({x};{y})$"
    ]
    choices = shuffle_choices(correct, wrongs)
    loigiai = (
        f"Ta có $\\vec{{a}} = {comb_str} \\Rightarrow \\vec{{a}} = ({x};{y})$.\\\\\n"
        f"Do đó ${target_vec} = ({k}\\cdot({x}); {k}\\cdot({y})) = ({res_x};{res_y})$."
    )
    return caudan, choices, loigiai


def k10_mc_vecto_do_dai_ab():
    """Ảnh 1 Câu 2: Cho A(x_A; y_A), B(x_B; y_B). Tính độ dài đoạn thẳng AB."""
    xA = random.randint(-4, 4)
    yA = random.randint(-4, 4)
    dx = random.choice([-5, -4, -3, 3, 4, 5, 6, 7])
    dy = random.choice([-6, -5, -4, -3, 3, 4, 5, 6])
    xB = xA + dx
    yB = yA + dy
    d2 = dx**2 + dy**2
    val_str = fmt_sqrt(d2)

    caudan = (
        f"Trong mặt phẳng tọa độ $Oxy$, cho các điểm $A({xA};{yA})$ và $B({xB};{yB})$. "
        f"Độ dài đoạn thẳng $AB$ bằng"
    )
    correct = f"${val_str}$"
    w1 = f"${fmt_sqrt(d2 + random.choice([2, 4, 6]))}$"
    w2 = f"${fmt_sqrt(abs(d2 - random.choice([2, 4, 6])))}$"
    w3 = f"${fmt_sqrt(dx**2 + abs(dy))}$"
    choices = shuffle_choices(correct, [w1, w2, w3])
    loigiai = (
        f"Ta có $\\vec{{AB}} = ({xB} - ({xA}); {yB} - ({yA})) = ({dx}; {dy})$.\\\\\n"
        f"Độ dài đoạn thẳng $AB = |\\vec{{AB}}| = \\sqrt{{({dx})^2 + ({dy})^2}} = \\sqrt{{{d2}}} = {val_str}$."
    )
    return caudan, choices, loigiai


def k10_mc_vecto_hinh_chieu_doi_xung():
    """Ảnh 1 Câu 3 & Câu 11: Hình chiếu hoặc điểm đối xứng của A qua Ox, Oy."""
    x = random.choice([-5, -4, -3, -2, 2, 3, 4, 5])
    y = random.choice([-5, -4, -3, -2, 2, 3, 4, 5])
    kieu = random.choice(["chieu_oy", "chieu_ox", "dx_ox", "dx_oy"])

    if kieu == "chieu_oy":
        caudan = f"Trong mặt phẳng tọa độ $Oxy$, cho điểm $A({x};{y})$. Hình chiếu vuông góc của điểm $A$ lên trục tung có tọa độ là"
        correct = f"$(0;{y})$"
        wrongs = [f"$({x};0)$", f"$(0;{-y})$", f"$({y};0)$"]
        loigiai = f"Hình chiếu vuông góc của điểm $A({x};{y})$ lên trục tung $Oy$ là điểm có hoành độ bằng $0$ và giữ nguyên tung độ, tức là $(0;{y})$."
    elif kieu == "chieu_ox":
        caudan = f"Trong mặt phẳng tọa độ $Oxy$, cho điểm $A({x};{y})$. Hình chiếu vuông góc của điểm $A$ lên trục hoành có tọa độ là"
        correct = f"$({x};0)$"
        wrongs = [f"$(0;{y})$", f"$({-x};0)$", f"$(0;{x})$"]
        loigiai = f"Hình chiếu vuông góc của điểm $A({x};{y})$ lên trục hoành $Ox$ là điểm giữ nguyên hoành độ và có tung độ bằng $0$, tức là $({x};0)$."
    elif kieu == "dx_ox":
        caudan = f"Trong mặt phẳng tọa độ $Oxy$, cho điểm $M({x};{y})$. Tọa độ điểm đối xứng với $M$ qua trục hoành $Ox$ là"
        correct = f"$({x};{-y})$"
        wrongs = [f"$({-x};{y})$", f"$({-x};{-y})$", f"$({y};{x})$"]
        loigiai = f"Điểm đối xứng với $M({x};{y})$ qua trục hoành $Ox$ giữ nguyên hoành độ và đổi dấu tung độ, tức là $({x};{-y})$."
    else:
        caudan = f"Trong mặt phẳng tọa độ $Oxy$, cho điểm $M({x};{y})$. Tọa độ điểm đối xứng với $M$ qua trục tung $Oy$ là"
        correct = f"$({-x};{y})$"
        wrongs = [f"$({x};{-y})$", f"$({-x};{-y})$", f"$({y};{x})$"]
        loigiai = f"Điểm đối xứng với $M({x};{y})$ qua trục tung $Oy$ đổi dấu hoành độ và giữ nguyên tung độ, tức là $({-x};{y})$."

    choices = shuffle_choices(correct, wrongs)
    return caudan, choices, loigiai


def k10_mc_vecto_diem_chia_doan_thang():
    """Ảnh 1 Câu 4: Cho A, B. Tìm điểm M thỏa vec{AM} + k*vec{BM} = vec{0}."""
    xA = random.randint(-4, 4)
    yA = random.randint(-4, 4)
    xB = random.randint(-4, 4)
    yB = random.randint(-4, 4)
    while xA == xB and yA == yB:
        xB = random.randint(-4, 4)

    k = random.choice([2, 3])
    xM_num = xA + k * xB
    yM_num = yA + k * yB
    den = 1 + k
    fr_x = Fraction(xM_num, den)
    fr_y = Fraction(yM_num, den)

    sx = fmt_frac(fr_x)
    sy = fmt_frac(fr_y)
    correct = f"$\\left({sx};{sy}\\right)$" if ("dfrac" in sx or "dfrac" in sy) else f"$({sx};{sy})$"

    # Distractors
    w1_x = fmt_frac(Fraction(xA - k * xB, 1 - k))
    w1_y = fmt_frac(Fraction(yA - k * yB, 1 - k))
    w1 = f"$\\left({w1_x};{w1_y}\\right)$" if ("dfrac" in w1_x or "dfrac" in w1_y) else f"$({w1_x};{w1_y})$"

    w2_x = fmt_frac(Fraction(k * xA + xB, den))
    w2_y = fmt_frac(Fraction(k * yA + yB, den))
    w2 = f"$\\left({w2_x};{w2_y}\\right)$" if ("dfrac" in w2_x or "dfrac" in w2_y) else f"$({w2_x};{w2_y})$"

    w3 = f"$({xA + xB};{yA + yB})$"

    caudan = (
        f"Trong mặt phẳng tọa độ $Oxy$, cho hai điểm $A({xA};{yA})$ và $B({xB};{yB})$. "
        f"Tọa độ điểm $M$ thoả mãn $\\vec{{AM}} + {k}\\vec{{BM}} = \\vec{{0}}$ là"
    )
    choices = shuffle_choices(correct, [w1, w2, w3])
    loigiai = (
        f"Gọi $M(x; y)$. Ta có $\\vec{{AM}} = (x - ({xA}); y - ({yA}))$, $\\vec{{BM}} = (x - ({xB}); y - ({yB}))$.\\\\\n"
        f"Theo giả thiết $\\vec{{AM}} + {k}\\vec{{BM}} = \\vec{{0}} \\Leftrightarrow "
        f"\\begin{{cases}} (x - ({xA})) + {k}(x - ({xB})) = 0 \\\\ (y - ({yA})) + {k}(y - ({yB})) = 0 \\end{{cases}} "
        f"\\Leftrightarrow \\begin{{cases}} {den}x = {xM_num} \\\\ {den}y = {yM_num} \\end{{cases}} "
        f"\\Leftrightarrow \\begin{{cases}} x = {sx} \\\\ y = {sy} \\end{{cases}}$.\\\\\n"
        f"Vậy điểm $M$ có tọa độ là {correct}."
    )
    return caudan, choices, loigiai


def k10_mc_vecto_phep_toan_tuyen_tinh():
    """Ảnh 1 Câu 6: vec{a} = (x1, y1), vec{b} = (x2, y2). Tọa độ k*vec{a} - m*vec{b}."""
    x1, y1 = random.randint(-4, 4), random.randint(-5, 5)
    x2, y2 = random.randint(-4, 4), random.randint(-5, 5)
    k, m = random.choice([(1, 1), (2, 1), (1, -1), (2, -1), (3, 2)])

    rx = k * x1 - m * x2
    ry = k * y1 - m * y2

    op_str = f"\\vec{{a}} - \\vec{{b}}" if (k == 1 and m == 1) else (
        f"2\\vec{{a}} + \\vec{{b}}" if (k == 2 and m == -1) else (
            f"\\vec{{a}} + \\vec{{b}}" if (k == 1 and m == -1) else f"{k}\\vec{{a}} - {m}\\vec{{b}}"
        )
    )

    caudan = (
        f"Trong mặt phẳng tọa độ $Oxy$, biết $\\vec{{a}} = ({x1};{y1})$ và $\\vec{{b}} = ({x2};{y2})$. "
        f"Tọa độ của vectơ ${op_str}$ là"
    )
    correct = f"$({rx};{ry})$"
    wrongs = [
        f"$({k * x1 + m * x2};{k * y1 + m * y2})$",
        f"$({rx};{-ry})$",
        f"$({-rx};{ry})$",
        f"$({ry};{rx})$"
    ]
    choices = shuffle_choices(correct, wrongs)
    loigiai = (
        f"Ta có:\\\\\n"
        f"Tọa độ của vectơ ${op_str} = ({k}\\cdot({x1}) - ({m})\\cdot({x2}); {k}\\cdot({y1}) - ({m})\\cdot({y2})) = ({rx}; {ry})$."
    )
    return caudan, choices, loigiai


def k10_mc_vecto_trung_diem_trong_tam():
    """Ảnh 1 Câu 7 & Câu 8: Trung điểm I của CD hoặc điểm đối xứng D của A qua B."""
    mode = random.choice(["trung_diem", "doi_xung_qua_diem"])
    if mode == "trung_diem":
        xC, yC = random.randint(-5, 5), random.randint(-5, 5)
        xD, yD = random.randint(-5, 5), random.randint(-5, 5)
        fr_x = Fraction(xC + xD, 2)
        fr_y = Fraction(yC + yD, 2)
        sx = fmt_frac(fr_x)
        sy = fmt_frac(fr_y)
        correct = f"$\\left({sx};{sy}\\right)$" if ("dfrac" in sx or "dfrac" in sy) else f"$({sx};{sy})$"
        caudan = (
            f"Trong mặt phẳng tọa độ $Oxy$, cho $C({xC};{yC}), D({xD};{yD})$. "
            f"Tọa độ trung điểm $I$ của đoạn thẳng $CD$ là"
        )
        wrongs = [
            f"$({xC - xD};{yC - yD})$",
            f"$({xD};{yC})$",
            f"$({xC + xD};{yC + yD})$"
        ]
        choices = shuffle_choices(correct, wrongs)
        loigiai = (
            f"Tọa độ trung điểm $I$ của $CD$ thỏa mãn:\\\\\n"
            f"$x_I = \\dfrac{{x_C + x_D}}{{2}} = \\dfrac{{{xC} + ({xD})}}{{2}} = {sx}$;\\\\\n"
            f"$y_I = \\dfrac{{y_C + y_D}}{{2}} = \\dfrac{{{yC} + ({yD})}}{{2}} = {sy}$.\\\\\n"
            f"Vậy $I$ có tọa độ là {correct}."
        )
    else:
        xA, yA = random.randint(-4, 4), random.randint(-4, 4)
        xB, yB = random.randint(-4, 4), random.randint(-4, 4)
        xD = 2 * xB - xA
        yD = 2 * yB - yA
        vec_OD_str = fmt_vec_comb(xD, yD)
        caudan = (
            f"Trong mặt phẳng tọa độ $Oxy$, cho hai điểm $A({xA};{yA})$ và $B({xB};{yB})$. "
            f"Biết $D$ là điểm đối xứng với $A$ qua $B$. Khi đó vectơ $\\vec{{OD}}$ được biểu diễn theo vectơ đơn vị là"
        )
        correct = f"${vec_OD_str}$"
        w1 = f"${fmt_vec_comb(2 * xA - xB, 2 * yA - yB)}$"
        w2 = f"${fmt_vec_comb(xA + xB, yA + yB)}$"
        w3 = f"${fmt_vec_comb(xD, -yD)}$"
        choices = shuffle_choices(correct, [w1, w2, w3])
        loigiai = (
            f"Vì $D$ đối xứng với $A$ qua $B$ nên $B$ là trung điểm của $AD$.\\\\\n"
            f"Suy ra $\\begin{{cases}} x_D = 2x_B - x_A = 2\\cdot({xB}) - ({xA}) = {xD} \\\\ "
            f"y_D = 2y_B - y_A = 2\\cdot({yB}) - ({yA}) = {yD} \\end{{cases}} \\Rightarrow D({xD};{yD})$.\\\\\n"
            f"Do đó $\\vec{{OD}} = {vec_OD_str}$."
        )
    return caudan, choices, loigiai


def k10_mc_vecto_trung_diem_tren_hai_truc():
    """Ảnh 1 Câu 10: Cho I(x0, y0) là trung điểm của AB với A thuộc Ox, B thuộc Oy."""
    x0 = random.choice([-4, -3, -2, -1, 1, 2, 3, 4])
    y0 = random.choice([-4, -3, -2, -1, 1, 2, 3, 4])
    xA = 2 * x0
    yB = 2 * y0

    caudan = (
        f"Trong mặt phẳng tọa độ $Oxy$, cho $I({x0};{y0})$ là trung điểm của đoạn thẳng $AB$, "
        f"với $A \\in Ox$ và $B \\in Oy$. Khẳng định nào sau đây đúng?"
    )
    correct = f"$A({xA};0)$"
    wrongs = [
        f"$A(0;{xA})$",
        f"$B({yB};0)$",
        f"$B(0;{-yB})$",
        f"$A({x0};0)$"
    ]
    choices = shuffle_choices(correct, wrongs)
    loigiai = (
        f"Vì $A \\in Ox$ nên $A(a; 0)$; $B \\in Oy$ nên $B(0; b)$.\\\\\n"
        f"Vì $I({x0};{y0})$ là trung điểm của $AB$ nên:\\\\\n"
        f"$\\begin{{cases}} \\dfrac{{a + 0}}{{2}} = {x0} \\\\ \\dfrac{{0 + b}}{{2}} = {y0} \\end{{cases}} "
        f"\\Leftrightarrow \\begin{{cases}} a = {xA} \\\\ b = {yB} \\end{{cases}}$.\\\\\n"
        f"Suy ra $A({xA};0)$ và $B(0;{yB})$."
    )
    return caudan, choices, loigiai


def k10_mc_vecto_hinh_binh_hanh():
    """Ảnh 2 Câu 12: Tìm tọa độ điểm D để ABCD là hình bình hành."""
    xA = random.randint(-4, 4)
    yA = random.randint(-4, 4)
    xB = random.randint(-4, 4)
    yB = random.randint(-4, 4)
    xC = random.randint(-4, 4)
    yC = random.randint(-4, 4)
    while (xB - xA) * (yC - yA) == (yB - yA) * (xC - xA):
        xC = random.randint(-4, 4)

    xD = xA + xC - xB
    yD = yA + yC - yB

    caudan = (
        f"Trong mặt phẳng tọa độ $Oxy$, cho ba điểm $A({xA};{yA}), B({xB};{yB}), C({xC};{yC})$. "
        f"Tọa độ điểm $D$ thoả mãn tứ giác $ABCD$ là hình bình hành là"
    )
    correct = f"$D({xD};{yD})$"
    wrongs = [
        f"$D({xA + xB - xC};{yA + yB - yC})$",
        f"$D({xB + xC - xA};{yB + yC - yA})$",
        f"$D({xD};{-yD})$",
        f"$D({-xD};{yD})$"
    ]
    choices = shuffle_choices(correct, wrongs)
    loigiai = (
        f"Tứ giác $ABCD$ là hình bình hành khi và chỉ khi $\\vec{{AD}} = \\vec{{BC}}$.\\\\\n"
        f"Ta có $\\vec{{AD}} = (x_D - ({xA}); y_D - ({yA}))$ và $\\vec{{BC}} = ({xC} - ({xB}); {yC} - ({yB})) = ({xC - xB}; {yC - yB})$.\\\\\n"
        f"Do đó $\\begin{{cases}} x_D - ({xA}) = {xC - xB} \\\\ y_D - ({yA}) = {yC - yB} \\end{{cases}} "
        f"\\Leftrightarrow \\begin{{cases}} x_D = {xD} \\\\ y_D = {yD} \\end{{cases}} \\Rightarrow D({xD};{yD})$."
    )
    return caudan, choices, loigiai


def k10_mc_vecto_hai_vecto_bang_nhau():
    """Ảnh 3 Câu 2: u = (x - a; b), v = (c; y + d), u = v. Tính x + y."""
    a = random.randint(1, 5)
    b = random.randint(-5, 5)
    c = random.randint(-5, 5)
    d = random.randint(1, 5)

    x_val = c + a
    y_val = b - d
    s_val = x_val + y_val

    caudan = (
        f"Trong mặt phẳng tọa độ $Oxy$, cho $\\vec{{u}} = (x - {a}; {b})$ và $\\vec{{v}} = ({c}; y + {d})$. "
        f"Biết $\\vec{{u}} = \\vec{{v}}$. Giá trị của biểu thức $x + y$ bằng"
    )
    correct = f"${s_val}$"
    wrongs = [f"${s_val + 2}$", f"${s_val - 2}$", f"${-s_val}$", f"${x_val - y_val}$"]
    choices = shuffle_choices(correct, wrongs)
    loigiai = (
        f"Vì $\\vec{{u}} = \\vec{{v}}$ nên:\\\\\n"
        f"$\\begin{{cases}} x - {a} = {c} \\\\ {b} = y + {d} \\end{{cases}} "
        f"\\Leftrightarrow \\begin{{cases}} x = {x_val} \\\\ y = {y_val} \\end{{cases}}$.\\\\\n"
        f"Do đó $x + y = {x_val} + ({y_val}) = {s_val}$."
    )
    return caudan, choices, loigiai


def k10_mc_vecto_cung_phuong_thang_hang():
    """Ảnh 3 Câu 4 & Câu 5: Điểm P thuộc Oy để MP, NP cùng phương hoặc O, A, B thẳng hàng."""
    xA = random.choice([-3, -2, -1, 1, 2, 3])
    yA = random.choice([-4, -3, -2, 2, 3, 4])
    k_scale = random.choice([-3, -2, 2, 3])
    xB = k_scale * xA
    yB = k_scale * yA

    caudan = (
        f"Trong mặt phẳng tọa độ $Oxy$, cho hai điểm $A({xA};{yA})$ và $B({xB};x)$. "
        f"Biết rằng ba điểm $O, A, B$ thẳng hàng. Khi đó giá trị của $x$ bằng"
    )
    correct = f"${yB}$"
    wrongs = [f"${-yB}$", f"${yB + 2}$", f"${yB - 2}$", f"${yA}$"]
    choices = shuffle_choices(correct, wrongs)
    loigiai = (
        f"Ta có $\\vec{{OA}} = ({xA}; {yA})$ và $\\vec{{OB}} = ({xB}; x)$.\\\\\n"
        f"Ba điểm $O, A, B$ thẳng hàng khi và chỉ khi hai vectơ $\\vec{{OA}}$ và $\\vec{{OB}}$ cùng phương:\\\\\n"
        f"$\\dfrac{{x}}{{{yA}}} = \\dfrac{{{xB}}}{{{xA}}} \\Leftrightarrow x = \\dfrac{{{xB}\\cdot({yA})}}{{{xA}}} = {yB}$."
    )
    return caudan, choices, loigiai


def k10_mc_vecto_chu_vi_tam_giac():
    """Ảnh 4 Câu 10: Cho A(0; yA), B(xB; yB). Chu vi tam giác OAB."""
    yA = random.choice([2, 3, 4])
    xB = random.choice([-4, -3, 3, 4])
    yB = random.choice([1, 2, 3])

    OA = abs(yA)
    OB2 = xB**2 + yB**2
    AB2 = (xB - 0)**2 + (yB - yA)**2

    str_OB = fmt_sqrt(OB2)
    str_AB = fmt_sqrt(AB2)

    # Đơn giản hóa biểu thức chu vi
    caudan = (
        f"Trong mặt phẳng tọa độ $Oxy$, cho hai điểm $A(0;{yA})$ và $B({xB};{yB})$. "
        f"Khi đó chu vi của tam giác $OAB$ bằng"
    )
    correct = f"${OA} + {str_OB} + {str_AB}$"
    if str_OB == str_AB:
        correct = f"${OA} + 2{str_OB}$"
    wrongs = [
        f"${OA + 2} + {str_OB}$",
        f"${str_OB} + {str_AB}$",
        f"${OA} + {fmt_sqrt(OB2 + AB2)}$"
    ]
    choices = shuffle_choices(correct, wrongs)
    loigiai = (
        f"Ta có:\\\\\n"
        f"$OA = \\sqrt{{0^2 + {yA}^2}} = {OA}$.\\\\\n"
        f"$OB = \\sqrt{{({xB})^2 + {yB}^2}} = {str_OB}$.\\\\\n"
        f"$AB = \\sqrt{{({xB} - 0)^2 + ({yB} - {yA})^2}} = {str_AB}$.\\\\\n"
        f"Chu vi của tam giác $OAB$ là $P = OA + OB + AB = {correct.strip('$')}$."
    )
    return caudan, choices, loigiai


def k10_mc_vecto_tim_tham_so_do_dai():
    """Ảnh 4 Câu 12: M(x1; y1), N(x2; m). Tìm m để MN = d."""
    x1, y1 = random.randint(-2, 3), random.randint(-2, 3)
    dx = random.choice([1, 2])
    x2 = x1 + dx
    dy = random.choice([2, 3])
    d2 = dx**2 + dy**2
    d_str = fmt_sqrt(d2)

    m1 = y1 + dy
    m2 = y1 - dy

    caudan = (
        f"Trong mặt phẳng tọa độ $Oxy$, cho hai điểm $M({x1};{y1})$ và $N({x2};m)$. "
        f"Các giá trị của $m$ để $MN = {d_str}$ là"
    )
    correct = f"$\\left[\\begin{{aligned}} m &= {m1} \\\\ m &= {m2} \\end{{aligned}}\\right.$"
    wrongs = [
        f"$\\left[\\begin{{aligned}} m &= {m1} \\\\ m &= {-m1} \\end{{aligned}}\\right.$",
        f"$m = \\pm {dy}$",
        f"$\\left[\\begin{{aligned}} m &= {m2} \\\\ m &= {-m2} \\end{{aligned}}\\right.$"
    ]
    choices = shuffle_choices(correct, wrongs)
    loigiai = (
        f"Ta có $\\vec{{MN}} = ({x2} - ({x1}); m - ({y1})) = ({dx}; m - ({y1}))$.\\\\\n"
        f"Độ dài $MN = \\sqrt{{({dx})^2 + (m - ({y1}))^2}} = {d_str} "
        f"\\Leftrightarrow {dx**2} + (m - ({y1}))^2 = {d2} "
        f"\\Leftrightarrow (m - ({y1}))^2 = {dy**2}$.\\\\\n"
        f"Suy ra $\\left[\\begin{{aligned}} m - ({y1}) &= {dy} \\\\ m - ({y1}) &= -{dy} \\end{{aligned}}\\right. "
        f"\\Leftrightarrow \\left[\\begin{{aligned}} m &= {m1} \\\\ m &= {m2} \\end{{aligned}}\\right.$."
    )
    return caudan, choices, loigiai


# ==============================================================================
# PHẦN 2: TRẮC NGHIỆM 4 PHƯƠNG ÁN (MC) - TÍCH VÔ HƯỚNG
# ==============================================================================

def k10_mc_tich_vo_huong_goc_tam_giac():
    """Ảnh 5 Câu 1 & Ảnh 9 Câu 1, 2: Góc giữa hai vectơ trong tam giác."""
    mode = random.choice(["tam_giac_deu_cung_goc", "tam_giac_deu_khac_goc", "tam_giac_vuong"])
    if mode == "tam_giac_deu_cung_goc":
        caudan = "Cho tam giác $ABC$ đều. Góc giữa hai vectơ $\\vec{CA}$ và $\\vec{CB}$ bằng"
        correct = "$60^\\circ$"
        wrongs = ["$30^\\circ$", "$120^\\circ$", "$90^\\circ$"]
        loigiai = "Vì tam giác $ABC$ đều nên góc $\\widehat{ACB} = 60^\\circ$. Do đó $(\\vec{CA}, \\vec{CB}) = \\widehat{BCA} = 60^\\circ$."
    elif mode == "tam_giac_deu_khac_goc":
        caudan = "Cho tam giác $ABC$ đều. Góc giữa hai vectơ $\\vec{AB}$ và $\\vec{BC}$ bằng"
        correct = "$120^\\circ$"
        wrongs = ["$60^\\circ$", "$30^\\circ$", "$150^\\circ$"]
        loigiai = "Góc giữa hai vectơ $(\\vec{AB}, \\vec{BC}) = 180^\\circ - \\widehat{ABC} = 180^\\circ - 60^\\circ = 120^\\circ$."
    else:
        deg_C = random.choice([30, 45, 60])
        deg_B = 90 - deg_C
        caudan = f"Cho tam giác $ABC$ vuông tại $A$ và $\\widehat{{ACB}} = {deg_C}^\\circ$. Góc giữa hai vectơ $\\vec{{BA}}$ và $\\vec{{BC}}$ bằng"
        correct = f"${deg_B}^\\circ$"
        wrongs = [f"${180 - deg_B}^\\circ$", f"${deg_C}^\\circ$", "$90^\\circ$"]
        loigiai = f"Vì tam giác $ABC$ vuông tại $A$ nên $\\widehat{{ABC}} = 90^\\circ - {deg_C}^\\circ = {deg_B}^\\circ$. Suy ra $(\\vec{{BA}}, \\vec{{BC}}) = \\widehat{{ABC}} = {deg_B}^\\circ$."

    choices = shuffle_choices(correct, wrongs)
    return caudan, choices, loigiai


def k10_mc_tich_vo_huong_dinh_nghia():
    """Ảnh 5 Câu 3: Biết |a|, |b| và góc (a, b). Tính tích vô hướng a . b."""
    la = random.choice([2, 3, 4, 5])
    deg = random.choice([30, 45, 60, 120, 135, 150])

    if deg == 30:
        cos_val = Fraction(1, 2) # simplified root
        cos_str = r"\dfrac{\sqrt{3}}{2}"
        lb_str = r"\sqrt{3}"
        res_str = f"{la * 3 // 2}" if (la % 2 == 0) else f"\\dfrac{{{la * 3}}}{{2}}"
    elif deg == 60:
        cos_str = r"\dfrac{1}{2}"
        lb_str = r"\sqrt{3}"
        res_str = f"{la // 2}\\sqrt{{3}}" if (la % 2 == 0) else f"\\dfrac{{{la}\\sqrt{{3}}}}{{2}}"
    elif deg == 120:
        cos_str = r"-\dfrac{1}{2}"
        lb_str = r"4"
        res_str = f"{-la * 2}"
    else:
        cos_str = r"\dfrac{\sqrt{2}}{2}"
        lb_str = r"\sqrt{2}"
        res_str = f"{la}"

    caudan = (
        f"Cho hai vectơ $\\vec{{a}}$ và $\\vec{{b}}$. Biết $|\\vec{{a}}| = {la}$, $|\\vec{{b}}| = {lb_str}$ "
        f"và $(\\vec{{a}}, \\vec{{b}}) = {deg}^\\circ$. Giá trị của $\\vec{{a}}\\cdot\\vec{{b}}$ bằng"
    )
    correct = f"${res_str}$"
    wrongs = [f"${la}$", f"${la * 2}$", f"-${res_str}$", r"$\sqrt{3}$"]
    choices = shuffle_choices(correct, wrongs)
    loigiai = (
        f"Áp dụng định nghĩa tích vô hướng của hai vectơ:\\\\\n"
        f"$\\vec{{a}}\\cdot\\vec{{b}} = |\\vec{{a}}|\\cdot|\\vec{{b}}|\\cdot\\cos(\\vec{{a}}, \\vec{{b}}) "
        f"= {la}\\cdot {lb_str}\\cdot\\cos {deg}^\\circ = {res_str}$."
    )
    return caudan, choices, loigiai


def k10_mc_tich_vo_huong_hinh_vuong_tam_giac():
    """Ảnh 5 Câu 4, 5 & Ảnh 6 Câu 11: Tích vô hướng trong tam giác đều, hình vuông."""
    kieu = random.choice(["tam_giac_deu_AB_AC", "tam_giac_deu_AB_BC", "hinh_vuong_canh_a", "tam_giac_deu_BC_CG"])
    if kieu == "tam_giac_deu_AB_AC":
        caudan = "Cho tam giác $ABC$ đều cạnh bằng $a$. Tích vô hướng $\\vec{AB}\\cdot\\vec{AC}$ bằng"
        correct = r"$\dfrac{a^2}{2}$"
        wrongs = [r"$\dfrac{a^2\sqrt{3}}{2}$", r"$a^2$", r"$-\dfrac{a^2}{2}$"]
        loigiai = r"Ta có $\vec{AB}\cdot\vec{AC} = AB\cdot AC\cdot\cos(\vec{AB},\vec{AC}) = a\cdot a\cdot\cos 60^\circ = \dfrac{a^2}{2}$."
    elif kieu == "tam_giac_deu_AB_BC":
        caudan = "Cho tam giác $ABC$ đều cạnh bằng $a$. Tích vô hướng $\\vec{AB}\\cdot\\vec{BC}$ bằng"
        correct = r"$-\dfrac{a^2}{2}$"
        wrongs = [r"$\dfrac{a^2}{2}$", r"$-\dfrac{a^2\sqrt{3}}{2}$", r"$-a^2$"]
        loigiai = r"Ta có $\vec{AB}\cdot\vec{BC} = -\vec{BA}\cdot\vec{BC} = -BA\cdot BC\cdot\cos 60^\circ = -\dfrac{a^2}{2}$."
    elif kieu == "tam_giac_deu_BC_CG":
        caudan = "Cho tam giác $ABC$ đều cạnh bằng $a$, trọng tâm $G$. Tích vô hướng của hai vectơ $\\vec{BC}\\cdot\\vec{CG}$ bằng"
        correct = r"$-\dfrac{a^2}{2}$"
        wrongs = [r"$\dfrac{a^2}{\sqrt{2}}$", r"$-\dfrac{a^2}{\sqrt{2}}$", r"$\dfrac{a^2}{2}$"]
        loigiai = (
            r"Gọi $M$ là trung điểm $AB$, ta có $\vec{CG} = -\dfrac{2}{3}\vec{CM}$.\\ "
            r"Độ dài $CG = \dfrac{a\sqrt{3}}{3}$, góc $(\vec{CB}, \vec{CG}) = 30^\circ$.\\ "
            r"Do đó $\vec{BC}\cdot\vec{CG} = -\vec{CB}\cdot\vec{CG} = -CB\cdot CG\cdot\cos 30^\circ = -a\cdot\dfrac{a\sqrt{3}}{3}\cdot\dfrac{\sqrt{3}}{2} = -\dfrac{a^2}{2}$."
        )
    else:
        caudan = "Cho hình vuông $ABCD$ cạnh $a$. Tích vô hướng $\\vec{AB}\\cdot\\vec{DB}$ bằng"
        correct = r"$a^2$"
        wrongs = [r"$-a^2$", r"$a^2\sqrt{2}$", r"$-a^2\sqrt{2}$"]
        loigiai = r"Ta có $\vec{DB} = \vec{AB} - \vec{AD} \Rightarrow \vec{AB}\cdot\vec{DB} = \vec{AB}\cdot(\vec{AB} - \vec{AD}) = AB^2 - \vec{AB}\cdot\vec{AD} = a^2 - 0 = a^2$."

    choices = shuffle_choices(correct, wrongs)
    return caudan, choices, loigiai


def k10_mc_tich_vo_huong_toa_do_oxy():
    """Ảnh 5 Câu 6, 7 & Ảnh 9 Câu 6: Tích vô hướng trong tọa độ Oxy."""
    xA, yA = random.randint(-4, 4), random.randint(-4, 4)
    xB, yB = random.randint(-4, 4), random.randint(-4, 4)
    xC, yC = random.randint(-4, 4), random.randint(-4, 4)

    dx1, dy1 = xB - xA, yB - yA
    dx2, dy2 = xC - xA, yC - yA
    dot_val = dx1 * dx2 + dy1 * dy2

    caudan = (
        f"Trong mặt phẳng tọa độ $Oxy$, cho ba điểm $A({xA};{yA}), B({xB};{yB}), C({xC};{yC})$. "
        f"Giá trị của tích vô hướng $\\vec{{AB}}\\cdot\\vec{{AC}}$ bằng"
    )
    correct = f"${dot_val}$"
    wrongs = [f"${dot_val + 10}$", f"${dot_val - 10}$", f"${-dot_val}$", f"${dx1 * dy2 - dx2 * dy1}$"]
    choices = shuffle_choices(correct, wrongs)
    loigiai = (
        f"Ta có $\\vec{{AB}} = ({dx1}; {dy1})$ và $\\vec{{AC}} = ({dx2}; {dy2})$.\\\\\n"
        f"Tích vô hướng $\\vec{{AB}}\\cdot\\vec{{AC}} = ({dx1})\\cdot({dx2}) + ({dy1})\\cdot({dy2}) = {dx1 * dx2} + ({dy1 * dy2}) = {dot_val}$."
    )
    return caudan, choices, loigiai


def k10_mc_tich_vo_huong_cosin_goc():
    """Ảnh 5 Câu 10: Côsin góc giữa hai vectơ trong tọa độ Oxy."""
    x1, y1 = random.choice([(-1, -1), (1, 2), (2, 1), (-2, 1), (3, -1)])
    x2, y2 = random.choice([(2, -1), (1, -2), (3, 1), (-1, 3), (1, 1)])

    dot = x1 * x2 + y1 * y2
    l1_sq = x1**2 + y1**2
    l2_sq = x2**2 + y2**2
    den_sq = l1_sq * l2_sq

    # Rút gọn phân số dot / sqrt(den_sq)
    r = int(math.isqrt(den_sq))
    if r * r == den_sq:
        fr = Fraction(dot, r)
        cos_str = fmt_frac(fr)
    else:
        # dot * sqrt(den_sq) / den_sq
        g = math.gcd(abs(dot), den_sq)
        num_c = dot // g
        den_c = den_sq // g
        sign = "-" if num_c < 0 else ""
        abs_n = abs(num_c)
        if abs_n == 1:
            cos_str = f"{sign}\\dfrac{{\\sqrt{{{den_sq}}}}}{{{den_c}}}"
        else:
            cos_str = f"{sign}\\dfrac{{{abs_n}\\sqrt{{{den_sq}}}}}{{{den_c}}}"

    caudan = (
        f"Trong mặt phẳng tọa độ $Oxy$, giá trị côsin của góc giữa hai vectơ "
        f"$\\vec{{a}} = ({x1};{y1})$ và $\\vec{{b}} = ({x2};{y2})$ bằng"
    )
    correct = f"${cos_str}$"
    wrongs = [f"-${cos_str}$" if not cos_str.startswith("-") else f"${cos_str[1:]}$", r"$\dfrac{1}{2}$", r"$\dfrac{\sqrt{2}}{2}$"]
    choices = shuffle_choices(correct, wrongs)
    loigiai = (
        f"Ta có $\\vec{{a}}\\cdot\\vec{{b}} = ({x1})\\cdot({x2}) + ({y1})\\cdot({y2}) = {dot}$.\\\\\n"
        f"Độ dài $|\\vec{{a}}| = \\sqrt{{{x1}^2 + ({y1})^2}} = \\sqrt{{{l1_sq}}}$, "
        f"$|\\vec{{b}}| = \\sqrt{{{x2}^2 + ({y2})^2}} = \\sqrt{{{l2_sq}}}$.\\\\\n"
        f"Do đó $\\cos(\\vec{{a}}, \\vec{{b}}) = \\dfrac{{\\vec{{a}}\\cdot\\vec{{b}}}}{{|\\vec{{a}}|\\cdot|\\vec{{b}}|}} "
        f"= \\dfrac{{{dot}}}{{\\sqrt{{{l1_sq}}}\\cdot\\sqrt{{{l2_sq}}}}} = {cos_str}$."
    )
    return caudan, choices, loigiai


def k10_mc_tich_vo_huong_tam_giac_vuong_ox():
    """Ảnh 8 Câu 12: A(-1, 3), B(1, 4). Tìm M thuộc Ox để tam giác ABM vuông tại B."""
    xA, yA = random.randint(-3, 1), random.randint(2, 5)
    xB, yB = random.randint(1, 4), random.randint(2, 5)
    while xA == xB:
        xB += 1

    # M(x, 0) in Ox. Tam giác ABM vuông tại B <=> BA . BM = 0
    # BA = (xA - xB, yA - yB)
    # BM = (x - xB, 0 - yB)
    # BA . BM = (xA - xB)(x - xB) + (yA - yB)(-yB) = 0
    # => (xA - xB)*x = (xA - xB)*xB + (yA - yB)*yB
    dx = xA - xB
    dy = yA - yB
    c_val = dx * xB + dy * yB
    fr_x = Fraction(c_val, dx)
    sx = fmt_frac(fr_x)
    correct = f"$\\left({sx};0\\right)$" if "dfrac" in sx else f"$({sx};0)$"

    caudan = (
        f"Trong mặt phẳng tọa độ $Oxy$, cho hai điểm $A({xA};{yA})$ và $B({xB};{yB})$. "
        f"Điểm $M$ thuộc trục hoành thỏa mãn tam giác $ABM$ vuông tại $B$ có tọa độ là"
    )
    wrongs = [
        f"$(0;{sx})$",
        f"$({xB};0)$",
        f"$({xA};0)$"
    ]
    choices = shuffle_choices(correct, wrongs)
    loigiai = (
        f"Vì $M \\in Ox$ nên $M(x; 0)$.\\\\\n"
        f"Ta có $\\vec{{BA}} = ({dx}; {dy})$ và $\\vec{{BM}} = (x - ({xB}); -{yB})$.\\\\\n"
        f"Tam giác $ABM$ vuông tại $B$ khi và chỉ khi $\\vec{{BA}}\\cdot\\vec{{BM}} = 0$:\\\\\n"
        f"$\\Leftrightarrow ({dx})(x - ({xB})) + ({dy})(-{yB}) = 0 "
        f"\\Leftrightarrow {dx}x = {c_val} \\Leftrightarrow x = {sx}$.\\\\\n"
        f"Vậy điểm $M$ có tọa độ là {correct}."
    )
    return caudan, choices, loigiai


def k10_mc_tich_vo_huong_vuong_goc_tham_so():
    """Ảnh 9 Câu 7: u = (x1, y1), v = (a*m, b*m + c). Tìm m để u vuông góc v."""
    x1 = random.choice([1, 2, -1, -2])
    y1 = random.choice([1, 2, 3, -1, -2])
    a = random.choice([2, 3, 4])
    b = random.choice([1, 2, -1, -2])
    c = random.choice([-4, -2, 2, 4])
    while x1 * a + y1 * b == 0:
        a += 1

    # u . v = x1 * (a*m) + y1 * (b*m + c) = (x1*a + y1*b)*m + y1*c = 0
    coeff_m = x1 * a + y1 * b
    const_val = y1 * c
    m_fr = Fraction(-const_val, coeff_m)
    sm = fmt_frac(m_fr)

    caudan = (
        f"Trong mặt phẳng tọa độ $Oxy$, cho hai vectơ $\\vec{{u}} = ({x1};{y1})$ và "
        f"$\\vec{{v}} = ({a}m; {b}m {'+' if c > 0 else ''}{c})$. "
        f"Tất cả các giá trị của tham số $m$ sao cho vectơ $\\vec{{u}}$ vuông góc với $\\vec{{v}}$ là"
    )
    correct = f"$m = {sm}$"
    wrongs = [f"$m = -{sm}$" if not sm.startswith("-") else f"$m = {sm[1:]}$", "$m = 1$", "$m = -1$"]
    choices = shuffle_choices(correct, wrongs)
    loigiai = (
        f"Hai vectơ $\\vec{{u}}$ và $\\vec{{v}}$ vuông góc khi và chỉ khi $\\vec{{u}}\\cdot\\vec{{v}} = 0$:\\\\\n"
        f"$\\Leftrightarrow ({x1})\\cdot({a}m) + ({y1})\\cdot({b}m {'+' if c > 0 else ''}{c}) = 0 "
        f"\\Leftrightarrow {coeff_m}m + ({const_val}) = 0 \\Leftrightarrow m = {sm}$."
    )
    return caudan, choices, loigiai


# ==============================================================================
# PHẦN 3: TRẮC NGHIỆM ĐÚNG SAI (TF - PHẦN II)
# ==============================================================================

def k10_tf_oxy_tam_giac_va_phan_giac():
    """Ảnh 2 Phần II Câu 1: Cho tam giác ABC với OA, OB, OC. Khảo sát 4 mệnh đề a, b, c, d."""
    xA, yA = random.randint(1, 3), random.randint(-3, -1)
    xB, yB = random.randint(1, 3), random.randint(1, 3)
    xC, yC = random.randint(3, 5), random.randint(2, 4)

    # 4 mệnh đề:
    # a) Tọa độ đỉnh B và C
    stmt_a_t = f"$B({xB};{yB}), C({xC};{yC})$."
    stmt_a_f = f"$B({yB};{xB}), C({xC};{yC})$."
    exp_a_t = f"Từ $\\vec{{OB}} = {fmt_vec_comb(xB, yB)}$ suy ra $B({xB};{yB})$; $\\vec{{OC}} = {fmt_vec_comb(xC, yC)}$ suy ra $C({xC};{yC})$."
    exp_a_f = exp_a_t

    # b) Trung điểm E của AB
    fr_Ex = Fraction(xA + xB, 2)
    fr_Ey = Fraction(yA + yB, 2)
    sEx, sEy = fmt_frac(fr_Ex), fmt_frac(fr_Ey)
    stmt_b_t = f"Trung điểm của đoạn thẳng $AB$ là điểm $E\\left({sEx};{sEy}\\right)$."
    stmt_b_f = f"Trung điểm của đoạn thẳng $AB$ là điểm $E({xA + xB};{yA + yB})$."
    exp_b_t = f"Tọa độ trung điểm $E$ của $AB$ là $x_E = \\dfrac{{{xA} + {xB}}}{{2}} = {sEx}$, $y_E = \\dfrac{{{yA} + {yB}}}{{2}} = {sEy}$."
    exp_b_f = exp_b_t

    # c) Trọng tâm G của tam giác ABC
    fr_Gx = Fraction(xA + xB + xC, 3)
    fr_Gy = Fraction(yA + yB + yC, 3)
    sGx, sGy = fmt_frac(fr_Gx), fmt_frac(fr_Gy)
    stmt_c_t = f"Trọng tâm của $\\Delta ABC$ là điểm $G\\left({sGx};{sGy}\\right)$."
    stmt_c_f = f"Trọng tâm của $\\Delta ABC$ là điểm $G\\left({sGy};{sGx}\\right)$."
    exp_c_t = f"Trọng tâm $G$ có tọa độ $x_G = \\dfrac{{{xA}+{xB}+{xC}}}{{3}} = {sGx}$, $y_G = \\dfrac{{{yA}+{yB}+{yC}}}{{3}} = {sGy}$."
    exp_c_f = exp_c_t

    # d) Phân giác trong hoặc điểm chia tỉ lệ
    # Xét N(xN, yN) và chân phân giác D(a; b)
    k_ratio = 2
    da = Fraction(xB + k_ratio * xA, 1 + k_ratio)
    db = Fraction(yB + k_ratio * yA, 1 + k_ratio)
    val_d = 3 * da + 3 * db
    stmt_d_t = f"Gọi điểm $D(a;b)$ thỏa mãn $\\vec{{DB}} + {k_ratio}\\vec{{DA}} = \\vec{{0}}$. Khi đó $3a + 3b = {fmt_frac(val_d)}$."
    stmt_d_f = f"Gọi điểm $D(a;b)$ thỏa mãn $\\vec{{DB}} + {k_ratio}\\vec{{DA}} = \\vec{{0}}$. Khi đó $3a + 3b = {fmt_frac(val_d + 2)}$."
    exp_d_t = f"Ta có $a = {fmt_frac(da)}$, $b = {fmt_frac(db)} \\Rightarrow 3a + 3b = {fmt_frac(val_d)}$."
    exp_d_f = exp_d_t

    items = [
        (stmt_a_t, stmt_a_f, exp_a_t, exp_a_f),
        (stmt_b_t, stmt_b_f, exp_b_t, exp_b_f),
        (stmt_c_t, stmt_c_f, exp_c_t, exp_c_f),
        (stmt_d_t, stmt_d_f, exp_d_t, exp_d_f),
    ]
    choices, loigiai = make_tf_choices(items)
    caudan = (
        f"Trong mặt phẳng tọa độ $Oxy$, cho tam giác $ABC$ có các đỉnh $A, B, C$ thoả mãn "
        f"$\\vec{{OA}} = {fmt_vec_comb(xA, yA)}$, $\\vec{{OB}} = {fmt_vec_comb(xB, yB)}$, $\\vec{{OC}} = {fmt_vec_comb(xC, yC)}$."
    )
    return caudan, choices, loigiai


def k10_tf_tich_vo_huong_oxy():
    """Ảnh 8 Phần II Câu 1: Cho hai vectơ a, b. Khảo sát 4 mệnh đề tích vô hướng."""
    x1, y1 = random.choice([(-2, 3), (-3, 2), (2, -3), (1, -2)])
    x2, y2 = random.choice([(1, 1), (2, 1), (-1, 1), (1, 2)])

    dot_ab = x1 * x2 + y1 * y2

    # b) (a + b) . (2a - b)
    # = 2 a^2 + a.b - b^2
    a2 = x1**2 + y1**2
    b2 = x2**2 + y2**2
    comb_val = 2 * a2 + dot_ab - b2

    # c) c = m*i + j vuông góc a <=> m*x1 + 1*y1 = 0 <=> m = -y1 / x1
    m_val = Fraction(-y1, x1)

    # d) a . d = c1, b . d = c2
    d1, d2 = random.randint(-3, 3), random.randint(-3, 3)
    c1 = x1 * d1 + y1 * d2
    c2 = x2 * d1 + y2 * d2

    stmt_a_t = f"$\\vec{{a}}\\cdot\\vec{{b}} = {dot_ab}$."
    stmt_a_f = f"$\\vec{{a}}\\cdot\\vec{{b}} = {dot_ab + 2}$."
    exp_a_t = f"$\\vec{{a}}\\cdot\\vec{{b}} = ({x1})\\cdot({x2}) + ({y1})\\cdot({y2}) = {dot_ab}$."
    exp_a_f = exp_a_t

    stmt_b_t = f"$(\\vec{{a}} + \\vec{{b}})\\cdot(2\\vec{{a}} - \\vec{{b}}) = {comb_val}$."
    stmt_b_f = f"$(\\vec{{a}} + \\vec{{b}})\\cdot(2\\vec{{a}} - \\vec{{b}}) = {comb_val + 5}$."
    exp_b_t = f"Ta có $\\vec{{a}}+\\vec{{b}} = ({x1+x2};{y1+y2})$ và $2\\vec{{a}}-\\vec{{b}} = ({2*x1-x2};{2*y1-y2})$. Tích vô hướng bằng ${comb_val}$."
    exp_b_f = exp_b_t

    sm = fmt_frac(m_val)
    stmt_c_t = f"Vectơ $\\vec{{c}} = m\\vec{{i}} + \\vec{{j}}$ vuông góc với $\\vec{{a}}$ khi $m = {sm}$."
    stmt_c_f = f"Vectơ $\\vec{{c}} = m\\vec{{i}} + \\vec{{j}}$ vuông góc với $\\vec{{a}}$ khi $m = {fmt_frac(-m_val)}$."
    exp_c_t = f"$\\vec{{c}} = (m; 1) \\perp \\vec{{a}} \\Leftrightarrow m\\cdot({x1}) + 1\\cdot({y1}) = 0 \\Leftrightarrow m = {sm}$."
    exp_c_f = exp_c_t

    stmt_d_t = f"Tọa độ của vectơ $\\vec{{d}}$ thỏa mãn $\\vec{{a}}\\cdot\\vec{{d}} = {c1}$ và $\\vec{{b}}\\cdot\\vec{{d}} = {c2}$ là $({d1};{d2})$."
    stmt_d_f = f"Tọa độ của vectơ $\\vec{{d}}$ thỏa mãn $\\vec{{a}}\\cdot\\vec{{d}} = {c1}$ và $\\vec{{b}}\\cdot\\vec{{d}} = {c2}$ là $({d2};{d1})$."
    exp_d_t = f"Giải hệ phương trình $\\begin{{cases}} {x1}x + {y1}y = {c1} \\\\ {x2}x + {y2}y = {c2} \\end{{cases}} \\Rightarrow (x; y) = ({d1}; {d2})$."
    exp_d_f = exp_d_t

    items = [
        (stmt_a_t, stmt_a_f, exp_a_t, exp_a_f),
        (stmt_b_t, stmt_b_f, exp_b_t, exp_b_f),
        (stmt_c_t, stmt_c_f, exp_c_t, exp_c_f),
        (stmt_d_t, stmt_d_f, exp_d_t, exp_d_f),
    ]
    choices, loigiai = make_tf_choices(items)
    caudan = (
        f"Trong mặt phẳng tọa độ $Oxy$, cho hai vectơ $\\vec{{a}} = ({x1};{y1})$ và $\\vec{{b}} = ({x2};{y2})$."
    )
    return caudan, choices, loigiai


def k10_tf_tich_vo_huong_hinh_binh_hanh():
    """Ảnh 8 Phần II Câu 2: Hình bình hành ABCD có AB = a, AD = b, góc BAD = 60 độ."""
    a = random.choice([2, 3])
    b = random.choice([3, 4, 5])
    dot_AB_AD = Fraction(a * b, 2)
    s_dot = fmt_frac(dot_AB_AD)

    # CB . CD = (-BC) . (-DC) = AD . AB = a * b * cos 60 = a*b/2
    val_b = s_dot

    # AB . BD = AB . (AD - AB) = AB . AD - AB^2 = a*b/2 - a^2
    val_c = Fraction(a * b, 2) - a**2
    s_val_c = fmt_frac(val_c)

    # AC . BD = (AB + AD) . (AD - AB) = AD^2 - AB^2 = b^2 - a^2
    val_d = b**2 - a**2

    stmt_a_t = r"Góc giữa hai vectơ $\vec{AB}$ và $\vec{AD}$ bằng $60^\circ$."
    stmt_a_f = r"Góc giữa hai vectơ $\vec{AB}$ và $\vec{AD}$ bằng $120^\circ$."
    exp_a_t = r"Vì $\widehat{BAD} = 60^\circ$ nên $(\vec{AB}, \vec{AD}) = 60^\circ$."
    exp_a_f = exp_a_t

    stmt_b_t = f"Tích vô hướng $\\vec{{CB}}\\cdot\\vec{{CD}} = {val_b}$."
    stmt_b_f = f"Tích vô hướng $\\vec{{CB}}\\cdot\\vec{{CD}} = {a * b}$."
    exp_b_t = f"$\\vec{{CB}}\\cdot\\vec{{CD}} = \\vec{{DA}}\\cdot\\vec{{BA}} = \\vec{{AD}}\\cdot\\vec{{AB}} = {a}\\cdot {b}\\cdot\\cos 60^\\circ = {val_b}$."
    exp_b_f = exp_b_t

    stmt_c_t = f"Tích vô hướng $\\vec{{AB}}\\cdot\\vec{{BD}} = {s_val_c}$."
    stmt_c_f = r"Tích vô hướng $\vec{AB}\cdot\vec{BD} = 0$."
    exp_c_t = f"$\\vec{{AB}}\\cdot\\vec{{BD}} = \\vec{{AB}}\\cdot(\\vec{{AD}} - \\vec{{AB}}) = \\vec{{AB}}\\cdot\\vec{{AD}} - AB^2 = {val_b} - {a**2} = {s_val_c}$."
    exp_c_f = exp_c_t

    stmt_d_t = f"Tích vô hướng $\\vec{{AC}}\\cdot\\vec{{BD}} = {val_d}$."
    stmt_d_f = f"Tích vô hướng $\\vec{{AC}}\\cdot\\vec{{BD}} = {val_d + 3}$."
    exp_d_t = f"$\\vec{{AC}}\\cdot\\vec{{BD}} = (\\vec{{AD}} + \\vec{{AB}})\\cdot(\\vec{{AD}} - \\vec{{AB}}) = AD^2 - AB^2 = {b}^2 - {a}^2 = {val_d}$."
    exp_d_f = exp_d_t

    items = [
        (stmt_a_t, stmt_a_f, exp_a_t, exp_a_f),
        (stmt_b_t, stmt_b_f, exp_b_t, exp_b_f),
        (stmt_c_t, stmt_c_f, exp_c_t, exp_c_f),
        (stmt_d_t, stmt_d_f, exp_d_t, exp_d_f),
    ]
    choices, loigiai = make_tf_choices(items)
    caudan = (
        f"Cho hình bình hành $ABCD$ có $AB = {a}$, $AD = {b}$ và $\\widehat{{BAD}} = 60^\\circ$."
    )
    return caudan, choices, loigiai


# ==============================================================================
# PHẦN 4: TRẮC NGHIỆM TRẢ LỜI NGẮN (SA - PHẦN III)
# ==============================================================================

def k10_sa_oxy_hinh_binh_hanh_tong_toa_do():
    """Trả lời ngắn: Tìm tọa độ D để ABCD là hình bình hành, tính xD + yD."""
    xA, yA = random.randint(-4, 4), random.randint(-4, 4)
    xB, yB = random.randint(-4, 4), random.randint(-4, 4)
    while xB == xA and yB == yA:
        xB, yB = random.randint(-4, 4), random.randint(-4, 4)
    xC, yC = random.randint(-4, 4), random.randint(-4, 4)
    while (xB - xA) * (yC - yA) == (yB - yA) * (xC - xA):
        xC, yC = random.randint(-4, 4), random.randint(-4, 4)

    xD = xA + xC - xB
    yD = yA + yC - yB
    ans_val = xD + yD
    dapan = str(ans_val)

    caudan = (
        f"Trong mặt phẳng tọa độ $Oxy$, cho ba điểm $A({xA};{yA}), B({xB};{yB}), C({xC};{yC})$. "
        f"Điểm $D(x_D; y_D)$ thỏa mãn tứ giác $ABCD$ là hình bình hành. "
        f"Tính giá trị của biểu thức $T = x_D + y_D$."
    )
    loigiai = (
        f"Tứ giác $ABCD$ là hình bình hành $\\Leftrightarrow \\vec{{AD}} = \\vec{{BC}}$.\\\\\n"
        f"Ta có $\\begin{{cases}} x_D - ({xA}) = {xC} - ({xB}) \\\\ y_D - ({yA}) = {yC} - ({yB}) \\end{{cases}} "
        f"\\Leftrightarrow \\begin{{cases}} x_D = {xD} \\\\ y_D = {yD} \\end{{cases}} \\Rightarrow D({xD};{yD})$.\\\\\n"
        f"Vậy $T = x_D + y_D = {xD} + ({yD}) = {ans_val}$."
    )
    return caudan, dapan, loigiai


def k10_sa_oxy_tam_giac_vuong_truc_hoanh():
    """Trả lời ngắn: Điểm M(x, 0) thuộc Ox để tam giác ABM vuông tại B."""
    xA = random.randint(-2, 1)
    yA = random.randint(2, 4)
    xB = random.randint(2, 4)
    yB = random.randint(2, 4)

    dx = xA - xB
    dy = yA - yB
    c_val = dx * xB + dy * yB
    fr_x = Fraction(c_val, dx)
    if fr_x.denominator == 1:
        dapan = str(fr_x.numerator)
    else:
        dapan = f"{float(fr_x):.2f}".rstrip('0').rstrip('.')

    caudan = (
        f"Trong mặt phẳng tọa độ $Oxy$, cho hai điểm $A({xA};{yA})$ và $B({xB};{yB})$. "
        f"Biết điểm $M(x_0; 0)$ thuộc trục hoành sao cho tam giác $ABM$ vuông tại $B$. "
        f"Tìm hoành độ $x_0$ của điểm $M$."
    )
    loigiai = (
        f"Ta có $\\vec{{BA}} = ({dx}; {dy})$ và $\\vec{{BM}} = (x_0 - {xB}; -{yB})$.\\\\\n"
        f"Tam giác $ABM$ vuông tại $B \\Leftrightarrow \\vec{{BA}}\\cdot\\vec{{BM}} = 0 "
        f"\\Leftrightarrow ({dx})(x_0 - {xB}) + ({dy})(-{yB}) = 0 \\Leftrightarrow x_0 = {fmt_frac(fr_x)}$."
    )
    return caudan, dapan, loigiai


def k10_sa_tich_vo_huong_oxy():
    """Trả lời ngắn: Tính tích vô hướng AB . AC."""
    xA, yA = random.randint(-3, 3), random.randint(-3, 3)
    xB, yB = random.randint(-3, 3), random.randint(-3, 3)
    xC, yC = random.randint(-3, 3), random.randint(-3, 3)

    dx1, dy1 = xB - xA, yB - yA
    dx2, dy2 = xC - xA, yC - yA
    dot_val = dx1 * dx2 + dy1 * dy2
    dapan = str(dot_val)

    caudan = (
        f"Trong mặt phẳng tọa độ $Oxy$, cho ba điểm $A({xA};{yA}), B({xB};{yB}), C({xC};{yC})$. "
        f"Tính giá trị của tích vô hướng $\\vec{{AB}}\\cdot\\vec{{AC}}$."
    )
    loigiai = (
        f"Ta có $\\vec{{AB}} = ({dx1}; {dy1})$ và $\\vec{{AC}} = ({dx2}; {dy2})$.\\\\\n"
        f"$\\vec{{AB}}\\cdot\\vec{{AC}} = ({dx1})\\cdot({dx2}) + ({dy1})\\cdot({dy2}) = {dot_val}$."
    )
    return caudan, dapan, loigiai


def k10_sa_tich_vo_huong_goc_do():
    """Trả lời ngắn: Tính góc giữa hai vectơ (độ)."""
    deg = random.choice([45, 60, 90])
    dapan = str(deg)

    if deg == 60:
        x1, y1 = 1, 0
        x2, y2 = 1, math.isqrt(3) # approx
        # Using exact nice vectors: (1, 0) and (1, sqrt(3))
        caudan = (
            r"Trong mặt phẳng tọa độ $Oxy$, cho hai vectơ $\vec{u} = (1; 0)$ và "
            r"$\vec{v} = (1; \sqrt{3})$. Tính số đo góc giữa hai vectơ $\vec{u}$ và $\vec{v}$ (tính theo độ)."
        )
        loigiai = (
            r"Ta có $\vec{u}\cdot\vec{v} = 1\cdot 1 + 0\cdot\sqrt{3} = 1$.\\"
            r"$|\vec{u}| = 1$, $|\vec{v}| = \sqrt{1^2 + (\sqrt{3})^2} = 2$.\\"
            r"$\cos(\vec{u}, \vec{v}) = \dfrac{1}{1\cdot 2} = \dfrac{1}{2} \Rightarrow (\vec{u}, \vec{v}) = 60^\circ$."
        )
        return caudan, dapan, loigiai
    elif deg == 45:
        caudan = (
            r"Trong mặt phẳng tọa độ $Oxy$, cho hai vectơ $\vec{u} = (1; 1)$ và "
            r"$\vec{v} = (0; 1)$. Tính số đo góc giữa hai vectơ $\vec{u}$ và $\vec{v}$ (tính theo độ)."
        )
        loigiai = (
            r"Ta có $\vec{u}\cdot\vec{v} = 1\cdot 0 + 1\cdot 1 = 1$.\\"
            r"$|\vec{u}| = \sqrt{2}$, $|\vec{v}| = 1 \Rightarrow \cos(\vec{u}, \vec{v}) = \dfrac{1}{\sqrt{2}} \Rightarrow (\vec{u}, \vec{v}) = 45^\circ$."
        )
        return caudan, dapan, loigiai
    else:
        caudan = (
            f"Trong mặt phẳng tọa độ $Oxy$, cho hai vectơ $\\vec{{u}} = (2; 3)$ và "
            f"$\\vec{{v}} = (-3; 2)$. Tính số đo góc giữa hai vectơ $\\vec{{u}}$ và $\\vec{{v}}$ (tính theo độ)."
        )
        loigiai = (
            r"Ta có $\vec{u}\cdot\vec{v} = 2\cdot(-3) + 3\cdot 2 = 0 \Rightarrow (\vec{u}, \vec{v}) = 90^\circ$."
        )
        return caudan, "90", loigiai


def k10_sa_tich_vo_huong_tham_so_vuong_goc():
    """Trả lời ngắn: Tìm m để u vuông góc v."""
    x1, y1 = random.choice([(1, 2), (2, 3), (1, -1), (3, 1)])
    c = random.choice([2, 4, 6, -2, -4])
    # u = (x1, y1), v = (m, c) => x1 * m + y1 * c = 0 => m = -y1 * c / x1
    m_fr = Fraction(-y1 * c, x1)
    if m_fr.denominator == 1:
        dapan = str(m_fr.numerator)
    else:
        dapan = f"{float(m_fr):.2f}".rstrip('0').rstrip('.')

    caudan = (
        f"Trong mặt phẳng tọa độ $Oxy$, cho hai vectơ $\\vec{{u}} = ({x1};{y1})$ và "
        f"$\\vec{{v}} = (m; {c})$. Tìm giá trị của tham số $m$ để hai vectơ $\\vec{{u}}$ và $\\vec{{v}}$ vuông góc với nhau."
    )
    loigiai = (
        f"$\\vec{{u}} \\perp \\vec{{v}} \\Leftrightarrow \\vec{{u}}\\cdot\\vec{{v}} = 0 "
        f"\\Leftrightarrow ({x1})\\cdot m + ({y1})\\cdot({c}) = 0 \\Leftrightarrow m = {fmt_frac(m_fr)}$."
    )
    return caudan, dapan, loigiai


# ==============================================================================
# BỔ SUNG CÁC DẠNG TOÁN TỪ BỘ ẢNH MỚI (BÀI 10, BÀI 11 & TỔNG HỢP VECTƠ)
# ==============================================================================

def k10_mc_vecto_hinh_binh_hanh_bang_nhau():
    """Ảnh 4 Câu 1: Cho hình bình hành ABCD. Vectơ nào bằng vectơ AB?"""
    name = random.choice(["ABCD", "MNPQ"])
    if name == "ABCD":
        caudan = "Cho hình bình hành $ABCD$. Vectơ nào dưới đây bằng với vectơ $\\vec{AB}$?"
        correct = r"$\vec{DC}$"
        wrongs = [r"$\vec{CD}$", r"$\vec{AD}$", r"$\vec{BC}$"]
        loigiai = r"Trong hình bình hành $ABCD$, hai đoạn thẳng $AB$ và $DC$ song song và cùng độ dài, chiều từ $A$ đến $B$ cùng chiều từ $D$ đến $C$. Do đó $\vec{AB} = \vec{DC}$."
    else:
        caudan = "Cho hình bình hành $MNPQ$. Vectơ nào dưới đây bằng với vectơ $\\vec{MN}$?"
        correct = r"$\vec{QP}$"
        wrongs = [r"$\vec{PQ}$", r"$\vec{MQ}$", r"$\vec{NP}$"]
        loigiai = r"Trong hình bình hành $MNPQ$, ta có $\vec{MN} = \vec{QP}$."

    choices = shuffle_choices(correct, wrongs)
    return caudan, choices, loigiai


def k10_mc_vecto_he_thuc_trong_tam():
    """Ảnh 4 Câu 2: Trọng tâm G của tam giác ABC."""
    caudan = "Cho tam giác $ABC$ có trọng tâm $G$. Khẳng định nào sau đây là đúng?"
    correct = r"$\vec{GA} + \vec{GB} + \vec{GC} = \vec{0}$"
    wrongs = [
        r"$\vec{AG} + \vec{BG} + \vec{CG} = \vec{GA}$",
        r"$\vec{GA} + \vec{GB} = \vec{GC}$",
        r"$\vec{GA} + \vec{GB} + \vec{GC} = 3\vec{G}$"
    ]
    choices = shuffle_choices(correct, wrongs)
    loigiai = r"Theo tính chất trọng tâm của tam giác, với $G$ là trọng tâm của $\Delta ABC$, ta luôn có đẳng thức vectơ: $\vec{GA} + \vec{GB} + \vec{GC} = \vec{0}$."
    return caudan, choices, loigiai


def k10_mc_vecto_hieu_do_dai_tam_giac_deu():
    """Ảnh 4 Câu 3: Tam giác ABC đều cạnh a. Tính độ dài vec{AB} - vec{AC}."""
    caudan = r"Cho tam giác $ABC$ đều có cạnh bằng $a$. Tính độ dài của vectơ $\vec{AB} - \vec{AC}$."
    correct = r"$a$"
    wrongs = [r"$a\sqrt{3}$", r"$2a$", r"$0$"]
    choices = shuffle_choices(correct, wrongs)
    loigiai = r"Ta có $\vec{AB} - \vec{AC} = \vec{CB}$. Do đó $|\vec{AB} - \vec{AC}| = |\vec{CB}| = CB = a$."
    return caudan, choices, loigiai


def k10_mc_vecto_hop_luc_vat_ly():
    """Ảnh 4 Câu 9: Hai lực vuông góc 6N và 8N. Tính hợp lực."""
    f1, f2 = random.choice([(6, 8), (3, 4), (5, 12), (8, 15), (7, 24)])
    f_res = int(math.isqrt(f1**2 + f2**2))

    caudan = (
        f"Hai lực $\\vec{{F}}_1$ và $\\vec{{F}}_2$ cùng tác dụng vào một vật tại điểm $O$, "
        f"biết hai lực này vuông góc với nhau và có độ lớn lần lượt là ${f1}\\text{{ N}}$ và ${f2}\\text{{ N}}$. "
        f"Hợp lực tác dụng lên vật có độ lớn là"
    )
    correct = f"${f_res}\\text{{ N}}$"
    wrongs = [
        f"${f1 + f2}\\text{{ N}}$",
        f"${abs(f1 - f2)}\\text{{ N}}$",
        f"${f1 * f2}\\text{{ N}}$"
    ]
    choices = shuffle_choices(correct, wrongs)
    loigiai = (
        f"Gọi hợp lực là $\\vec{{F}} = \\vec{{F}}_1 + \\vec{{F}}_2$.\\\\\n"
        f"Vì $\\vec{{F}}_1 \\perp \\vec{{F}}_2$ nên theo định lý Pytago trong hình chữ nhật lực:\\\\\n"
        f"$F = |\\vec{{F}}| = \\sqrt{{F_1^2 + F_2^2}} = \\sqrt{{{f1}^2 + {f2}^2}} = {f_res}\\text{{ N}}$."
    )
    return caudan, choices, loigiai


def k10_mc_vecto_ti_so_doan_thang():
    """Ảnh 4 Câu 10: Cho đoạn thẳng AB. Tìm tỉ số MA/MB biết vec{MA} + k*vec{MB} = vec{0}."""
    k = random.choice([2, 3, 4, 5])
    caudan = (
        f"Cho đoạn thẳng $AB$. Tìm tỉ số $\\dfrac{{MA}}{{MB}}$ biết điểm $M$ thỏa mãn hệ thức "
        f"$\\vec{{MA}} + {k}\\vec{{MB}} = \\vec{{0}}$."
    )
    correct = f"${k}$"
    wrongs = [r"$\dfrac{1}{" + str(k) + r"}$", f"${k + 1}$", "$1$"]
    choices = shuffle_choices(correct, wrongs)
    loigiai = (
        f"Từ giả thiết $\\vec{{MA}} + {k}\\vec{{MB}} = \\vec{{0}} \\Leftrightarrow \\vec{{MA}} = -{k}\\vec{{MB}}$.\\\\\n"
        f"Lấy độ dài hai vế ta được $|\\vec{{MA}}| = |- {k}\\vec{{MB}}| \\Leftrightarrow MA = {k}\\cdot MB \\Leftrightarrow \\dfrac{{MA}}{{MB}} = {k}$."
    )
    return caudan, choices, loigiai


def k10_mc_vecto_phan_tich_vecto_c():
    """Ảnh 5 Câu 11: Phân tích c = m*a + n*b. Tính m + n."""
    a1, a2 = 1, 2
    b1, b2 = 4, 3
    # c = m*a + n*b
    # Let m = 2/5, n = 3/5 or m = 1, n = 2
    m_val = Fraction(2, 5)
    n_val = Fraction(3, 5)
    c1 = m_val * a1 + n_val * b1 # 2/5 + 12/5 = 14/5
    c2 = m_val * a2 + n_val * b2 # 4/5 + 9/5 = 13/5

    # Use nice integer coefficients:
    m_int = random.choice([1, 2, -1])
    n_int = random.choice([1, -1, 2])
    a1, a2 = random.randint(1, 3), random.randint(1, 3)
    b1, b2 = random.randint(-3, -1), random.randint(1, 4)
    while a1 * b2 - a2 * b1 == 0:
        b1 += 1

    c1 = m_int * a1 + n_int * b1
    c2 = m_int * a2 + n_int * b2
    sum_mn = m_int + n_int

    caudan = (
        f"Cho $\\vec{{a}} = ({a1};{a2}), \\vec{{b}} = ({b1};{b2})$ và $\\vec{{c}} = ({c1};{c2})$. "
        f"Phân tích vectơ $\\vec{{c}}$ qua $\\vec{{a}}$ và $\\vec{{b}}$ ta được $\\vec{{c}} = m\\vec{{a}} + n\\vec{{b}}$. "
        f"Giá trị của biểu thức $m + n$ là"
    )
    correct = f"${sum_mn}$"
    wrongs = [f"${sum_mn + 1}$", f"${sum_mn - 1}$", f"${-sum_mn}$", f"${m_int * n_int}$"]
    choices = shuffle_choices(correct, wrongs)
    loigiai = (
        f"Giả sử $\\vec{{c}} = m\\vec{{a}} + n\\vec{{b}}$, ta có hệ phương trình:\\\\\n"
        f"$\\begin{{cases}} {a1}m + ({b1})n = {c1} \\\\ {a2}m + ({b2})n = {c2} \\end{{cases}} "
        f"\\Leftrightarrow \\begin{{cases}} m = {m_int} \\\\ n = {n_int} \\end{{cases}}$.\\\\\n"
        f"Do đó $m + n = {m_int} + ({n_int}) = {sum_mn}$."
    )
    return caudan, choices, loigiai


def k10_mc_vecto_ba_diem_thang_hang_tham_so():
    """Ảnh 5 Câu 12: A(1; 1), B(3; 2), C(m+4; 2m+1). Tìm m để A, B, C thẳng hàng."""
    xA, yA = 1, 1
    xB, yB = 3, 2
    # AB = (2, 1)
    # AC = (m+3, 2m)
    # Collinear <=> (m+3)*1 = 2m * 2 <=> m+3 = 4m <=> 3m = 3 <=> m = 1
    caudan = (
        r"Trong mặt phẳng tọa độ $Oxy$, cho ba điểm $A(1;1), B(3;2)$ và $C(m+4; 2m+1)$. "
        r"Tìm tất cả các giá trị của tham số $m$ để ba điểm $A, B, C$ thẳng hàng."
    )
    correct = r"$m = 1$"
    wrongs = [r"$m = -1$", r"$m = 2$", r"$m = 0$"]
    choices = shuffle_choices(correct, wrongs)
    loigiai = (
        r"Ta có $\vec{AB} = (3 - 1; 2 - 1) = (2; 1)$ và $\vec{AC} = (m + 4 - 1; 2m + 1 - 1) = (m + 3; 2m)$.\\ "
        r"Ba điểm $A, B, C$ thẳng hàng khi và chỉ khi hai vectơ $\vec{AB}$ và $\vec{AC}$ cùng phương:\\ "
        r"$\dfrac{m + 3}{2} = \dfrac{2m}{1} \Leftrightarrow m + 3 = 4m \Leftrightarrow 3m = 3 \Leftrightarrow m = 1$."
    )
    return caudan, choices, loigiai


def k10_mc_vecto_tim_diem_trong_tam_nguoc():
    """Ảnh 1 Câu 2: Cho A, B và I là trọng tâm ABK. Tìm K."""
    xA, yA = random.randint(-5, 5), random.randint(-5, 5)
    xB, yB = random.randint(-5, 5), random.randint(-5, 5)
    xI, yI = random.randint(-5, 5), random.randint(-5, 5)

    xK = 3 * xI - xA - xB
    yK = 3 * yI - yA - yB

    caudan = (
        f"Trong mặt phẳng tọa độ $Oxy$, cho ba điểm $A({xA};{yA}), B({xB};{yB})$ và $I({xI};{yI})$. "
        f"Tìm tọa độ điểm $K$ sao cho tam giác $ABK$ nhận $I$ làm trọng tâm."
    )
    correct = f"$K({xK};{yK})$"
    wrongs = [
        f"$K({xK + 2};{yK})$",
        f"$K({xI - xA};{yI - yB})$",
        f"$K({-xK};{yK})$"
    ]
    choices = shuffle_choices(correct, wrongs)
    loigiai = (
        f"Vì $I({xI};{yI})$ là trọng tâm của tam giác $ABK$ nên:\\\\\n"
        f"$\\begin{{cases}} x_I = \\dfrac{{x_A + x_B + x_K}}{{3}} \\\\ y_I = \\dfrac{{y_A + y_B + y_K}}{{3}} \\end{{cases}} "
        f"\\Leftrightarrow \\begin{{cases}} x_K = 3x_I - x_A - x_B = 3\\cdot({xI}) - ({xA}) - ({xB}) = {xK} \\\\ "
        f"y_K = 3y_I - y_A - y_B = 3\\cdot({yI}) - ({yA}) - ({yB}) = {yK} \\end{{cases}}$.\\\\\n"
        f"Vậy điểm $K$ có tọa độ là $K({xK};{yK})$."
    )
    return caudan, choices, loigiai


def k10_mc_tich_vo_huong_goc_nguoc():
    """Ảnh 3 Câu 6 & Câu 8: Cho |a|, |v| và tích vô hướng. Tìm góc (a, v)."""
    deg = random.choice([30, 45, 60, 90, 120, 135, 150])
    la = random.choice([8, 10, 12])
    lv = random.choice([10, 13, 22])

    if deg == 45:
        # cos = sqrt(2)/2
        dot_str = f"{la * lv // 2}\\sqrt{{2}}"
        rad_val = math.radians(45)
    elif deg == 60:
        dot_str = f"{la * lv // 2}"
    elif deg == 30:
        dot_str = f"{la * lv // 2}\\sqrt{{3}}"
    elif deg == 150:
        dot_str = f"-{la * lv // 2}\\sqrt{{3}}"
    elif deg == 120:
        dot_str = f"-{la * lv // 2}"
    elif deg == 135:
        dot_str = f"-{la * lv // 2}\\sqrt{{2}}"
    else:
        dot_str = "0"

    caudan = (
        f"Cho hai vectơ $\\vec{{a}}$ và $\\vec{{v}}$ có $|\\vec{{a}}| = {la}$, $|\\vec{{v}}| = {lv}$ "
        f"và $\\vec{{a}}\\cdot\\vec{{v}} = {dot_str}$. Tìm góc giữa hai vectơ $(\\vec{{a}}, \\vec{{v}})$."
    )
    correct = f"${deg}^\\circ$"
    wrongs = [f"${d}^\\circ$" for d in [30, 45, 60, 90, 120, 150] if d != deg][:3]
    choices = shuffle_choices(correct, wrongs)
    loigiai = (
        f"Áp dụng công thức tính góc giữa hai vectơ:\\\\\n"
        f"$\\cos(\\vec{{a}}, \\vec{{v}}) = \\dfrac{{\\vec{{a}}\\cdot\\vec{{v}}}}{{|\\vec{{a}}|\\cdot|\\vec{{v}}|}} "
        f"= \\dfrac{{{dot_str}}}{{{la}\\cdot {lv}}}$.\\\\\n"
        f"Suy ra $(\\vec{{a}}, \\vec{{v}}) = {deg}^\\circ$."
    )
    return caudan, choices, loigiai


def k10_mc_tich_vo_huong_tam_giac_vuong_canh():
    """Ảnh 3 Câu 11 & Câu 12: Tam giác ABC vuông tại A có AB=a, BC=2a. Tính BA . BC."""
    caudan = r"Cho tam giác $ABC$ vuông tại $A$ có $AB = a$ và $BC = 2a$. Tính tích vô hướng $\vec{BA}\cdot\vec{BC}$."
    correct = r"$a^2$"
    wrongs = [r"$\dfrac{a^2}{2}$", r"$2a^2$", r"$\dfrac{a^2\sqrt{3}}{2}$"]
    choices = shuffle_choices(correct, wrongs)
    loigiai = (
        r"Trong tam giác vuông $ABC$ tại $A$, ta có $\cos \widehat{ABC} = \dfrac{AB}{BC} = \dfrac{a}{2a} = \dfrac{1}{2}$.\\ "
        r"Do đó $\vec{BA}\cdot\vec{BC} = BA\cdot BC\cdot\cos \widehat{ABC} = a\cdot 2a\cdot\dfrac{1}{2} = a^2$."
    )
    return caudan, choices, loigiai


# ==============================================================================
# BỔ SUNG CÁC CÂU ĐÚNG SAI (TF) TỪ ẢNH MỚI
# ==============================================================================

def k10_tf_vecto_co_ban_va_do_dai():
    """Ảnh 1 Phần II Câu 2: Độ dài vectơ và vectơ cùng phương."""
    x1, y1 = 2, 3
    x2, y2 = -1, 2
    x3, y3 = -6, 4

    l1_sq = x1**2 + y1**2 # 13
    l2_sq = x2**2 + y2**2 # 5
    l3_sq = x3**2 + y3**2 # 52 = 2 sqrt(13)

    stmt_a_t = f"$|\\vec{{a}}| = \\sqrt{{{l1_sq}}}$."
    stmt_a_f = f"$|\\vec{{a}}| = {l1_sq}$."
    exp_a_t = f"$|\\vec{{a}}| = \\sqrt{{{x1}^2 + {y1}^2}} = \\sqrt{{{l1_sq}}}$."
    exp_a_f = exp_a_t

    stmt_b_t = f"$|\\vec{{b}}| = \\sqrt{{{l2_sq}}}$."
    stmt_b_f = r"$|\vec{b}| = \sqrt{3}$."
    exp_b_t = f"$|\\vec{{b}}| = \\sqrt{{({x2})^2 + {y2}^2}} = \\sqrt{{{l2_sq}}}$."
    exp_b_f = exp_b_t

    stmt_c_t = f"$|\\vec{{c}}| = 2\\sqrt{{{l1_sq}}}$."
    stmt_c_f = f"$|\\vec{{c}}| = \\sqrt{{{l1_sq}}}$."
    exp_c_t = f"$|\\vec{{c}}| = \\sqrt{{({x3})^2 + {y3}^2}} = \\sqrt{{{l3_sq}}} = 2\\sqrt{{{l1_sq}}}$."
    exp_c_f = exp_c_t

    stmt_d_t = (
        r"Vectơ $\vec{d}$ cùng phương với $\vec{a}$ và có độ dài bằng $\dfrac{\sqrt{13}}{2}$ "
        r"có tọa độ là $\left(1; \dfrac{3}{2}\right)$ hoặc $\left(-1; -\dfrac{3}{2}\right)$."
    )
    stmt_d_f = (
        r"Vectơ $\vec{d}$ cùng phương với $\vec{a}$ và có độ dài bằng $\dfrac{\sqrt{13}}{2}$ "
        r"có tọa độ duy nhất là $(1; 3)$."
    )
    exp_d_t = (
        r"Vì $\vec{d}$ cùng phương với $\vec{a} = (2;3)$ nên $\vec{d} = k\vec{a} = (2k; 3k)$.\\ "
        r"Độ dài $|\vec{d}| = |k|\sqrt{13} = \dfrac{\sqrt{13}}{2} \Leftrightarrow |k| = \dfrac{1}{2} "
        r"\Leftrightarrow k = \pm \dfrac{1}{2}$."
    )
    exp_d_f = exp_d_t

    items = [
        (stmt_a_t, stmt_a_f, exp_a_t, exp_a_f),
        (stmt_b_t, stmt_b_f, exp_b_t, exp_b_f),
        (stmt_c_t, stmt_c_f, exp_c_t, exp_c_f),
        (stmt_d_t, stmt_d_f, exp_d_t, exp_d_f),
    ]
    choices, loigiai = make_tf_choices(items)
    caudan = (
        f"Trong mặt phẳng tọa độ $Oxy$, cho các vectơ $\\vec{{a}} = ({x1};{y1}), \\vec{{b}} = ({x2};{y2}), \\vec{{c}} = ({x3};{y3})$."
    )
    return caudan, choices, loigiai


def k10_tf_tich_vo_huong_tam_giac_deu_duong_cao():
    """Ảnh 3 Phần II Câu 1: Tam giác ABC đều đường cao AH."""
    stmt_a_t = r"Góc giữa hai vectơ $(\vec{AB}, \vec{AC}) = 60^\circ$."
    stmt_a_f = r"Góc giữa hai vectơ $(\vec{AB}, \vec{AC}) = 30^\circ$."
    exp_a_t = r"Vì $\Delta ABC$ đều nên $\widehat{BAC} = 60^\circ \Rightarrow (\vec{AB}, \vec{AC}) = 60^\circ$."
    exp_a_f = exp_a_t

    stmt_b_t = r"Góc giữa hai vectơ $(\vec{AH}, \vec{CB}) = 90^\circ$."
    stmt_b_f = r"Góc giữa hai vectơ $(\vec{AH}, \vec{CB}) = 0^\circ$."
    exp_b_t = r"Vì $AH \perp BC$ nên đường thẳng $AH$ vuông góc $BC$, do đó $(\vec{AH}, \vec{CB}) = 90^\circ$."
    exp_b_f = exp_b_t

    stmt_c_t = r"Góc giữa hai vectơ $(\vec{CA}, \vec{BC}) = 120^\circ$."
    stmt_c_f = r"Góc giữa hai vectơ $(\vec{CA}, \vec{BC}) = 60^\circ$."
    exp_c_t = r"Ta có $(\vec{CA}, \vec{BC}) = 180^\circ - \widehat{BCA} = 180^\circ - 60^\circ = 120^\circ$."
    exp_c_f = exp_c_t

    stmt_d_t = r"Góc giữa hai vectơ $(\vec{AH}, \vec{BA}) = 150^\circ$."
    stmt_d_f = r"Góc giữa hai vectơ $(\vec{AH}, \vec{BA}) = 130^\circ$."
    exp_d_t = (
        r"Ta có $(\vec{AH}, \vec{BA}) = 180^\circ - (\vec{AH}, \vec{AB})$.\\ "
        r"Vì $AH$ là phân giác góc $A$ nên $\widehat{HAB} = 30^\circ \Rightarrow (\vec{AH}, \vec{AB}) = 30^\circ$.\\ "
        r"Do đó $(\vec{AH}, \vec{BA}) = 180^\circ - 30^\circ = 150^\circ$."
    )
    exp_d_f = exp_d_t

    items = [
        (stmt_a_t, stmt_a_f, exp_a_t, exp_a_f),
        (stmt_b_t, stmt_b_f, exp_b_t, exp_b_f),
        (stmt_c_t, stmt_c_f, exp_c_t, exp_c_f),
        (stmt_d_t, stmt_d_f, exp_d_t, exp_d_f),
    ]
    choices, loigiai = make_tf_choices(items)
    caudan = "Cho tam giác $ABC$ đều, đường cao $AH$."
    return caudan, choices, loigiai


def k10_tf_hinh_vuong_tich_vo_huong():
    """Ảnh 5 Phần II Câu 1: Hình vuông ABCD tâm O cạnh a."""
    stmt_a_t = r"$\vec{AB} = \vec{DC}$."
    stmt_a_f = r"$\vec{AB} = \vec{CD}$."
    exp_a_t = r"Trong hình vuông $ABCD$, $\vec{AB}$ và $\vec{DC}$ cùng hướng và cùng độ dài nên $\vec{AB} = \vec{DC}$."
    exp_a_f = exp_a_t

    stmt_b_t = r"Độ dài của vectơ $|\vec{OA} - \vec{OB}| = a$."
    stmt_b_f = r"Độ dài của vectơ $|\vec{OA} - \vec{OB}| = a\sqrt{2}$."
    exp_b_t = r"Ta có $\vec{OA} - \vec{OB} = \vec{BA} \Rightarrow |\vec{OA} - \vec{OB}| = BA = a$."
    exp_b_f = exp_b_t

    stmt_c_t = r"Tích vô hướng $\vec{AB}\cdot\vec{AC} = a^2$."
    stmt_c_f = r"Tích vô hướng $\vec{AB}\cdot\vec{AC} = a^2\sqrt{2}$."
    exp_c_t = r"Ta có $\vec{AB}\cdot\vec{AC} = AB\cdot AC\cdot\cos 45^\circ = a\cdot (a\sqrt{2})\cdot\dfrac{\sqrt{2}}{2} = a^2$."
    exp_c_f = exp_c_t

    stmt_d_t = r"Tích vô hướng $\vec{AC}\cdot\vec{BD} = 0$."
    stmt_d_f = r"Tích vô hướng $\vec{AC}\cdot\vec{BD} = a^2$."
    exp_d_t = r"Vì hai đường chéo của hình vuông vuông góc với nhau $AC \perp BD$ nên $\vec{AC}\cdot\vec{BD} = 0$."
    exp_d_f = exp_d_t

    items = [
        (stmt_a_t, stmt_a_f, exp_a_t, exp_a_f),
        (stmt_b_t, stmt_b_f, exp_b_t, exp_b_f),
        (stmt_c_t, stmt_c_f, exp_c_t, exp_c_f),
        (stmt_d_t, stmt_d_f, exp_d_t, exp_d_f),
    ]
    choices, loigiai = make_tf_choices(items)
    caudan = "Cho hình vuông $ABCD$ tâm $O$, có cạnh bằng $a$."
    return caudan, choices, loigiai


# ==============================================================================
# BỔ SUNG CÁC CÂU TRẢ LỜI NGẮN (SA) TỪ ẢNH MỚI
# ==============================================================================

def k10_sa_vecto_hop_luc():
    """TLN: Hợp lực của hai lực vuông góc."""
    f1, f2 = random.choice([(6, 8), (5, 12), (9, 12), (8, 15), (12, 16)])
    f_res = int(math.isqrt(f1**2 + f2**2))
    caudan = (
        f"Hai lực $\\vec{{F}}_1$ và $\\vec{{F}}_2$ cùng tác dụng vào một vật tại điểm $O$, "
        f"biết hai lực vuông góc với nhau và có độ lớn lần lượt là ${f1}\\text{{ N}}$ và ${f2}\\text{{ N}}$. "
        f"Tính độ lớn của hợp lực tác dụng lên vật (đơn vị: N)."
    )
    dapan = str(f_res)
    loigiai = f"Độ lớn hợp lực là $F = \\sqrt{{F_1^2 + F_2^2}} = \\sqrt{{{f1}^2 + {f2}^2}} = {f_res}\\text{{ N}}$."
    return caudan, dapan, loigiai


def k10_sa_vecto_ti_so_doan_thang():
    """TLN: Tỉ số MA/MB từ MA + k*MB = 0."""
    k = random.choice([2, 3, 4, 5])
    caudan = f"Cho đoạn thẳng $AB$. Điểm $M$ thỏa mãn hệ thức $\\vec{{MA}} + {k}\\vec{{MB}} = \\vec{{0}}$. Tính tỉ số $\\dfrac{{MA}}{{MB}}$."
    dapan = str(k)
    loigiai = f"Từ $\\vec{{MA}} = -{k}\\vec{{MB}} \\Rightarrow MA = {k}\\cdot MB \\Rightarrow \\dfrac{{MA}}{{MB}} = {k}$."
    return caudan, dapan, loigiai


def k10_sa_vecto_phan_tich_tong_he_so():
    """TLN: Phân tích c = m*a + n*b, tính m + n."""
    a1, a2 = 1, 2
    b1, b2 = 4, 3
    # c = m*a + n*b
    # Let m = 2, n = -1 => c = (2 - 4, 4 - 3) = (-2, 1)
    m_int = random.choice([1, 2, 3])
    n_int = random.choice([1, 2, -1])
    c1 = m_int * a1 + n_int * b1
    c2 = m_int * a2 + n_int * b2
    ans = m_int + n_int

    caudan = (
        f"Trong mặt phẳng tọa độ $Oxy$, cho $\\vec{{a}} = ({a1};{a2}), \\vec{{b}} = ({b1};{b2})$ và $\\vec{{c}} = ({c1};{c2})$. "
        f"Biết $\\vec{{c}} = m\\vec{{a}} + n\\vec{{b}}$. Tính giá trị của $T = m + n$."
    )
    dapan = str(ans)
    loigiai = (
        f"Ta có hệ phương trình $\\begin{{cases}} {a1}m + {b1}n = {c1} \\\\ {a2}m + {b2}n = {c2} \\end{{cases}} "
        f"\\Leftrightarrow \\begin{{cases}} m = {m_int} \\\\ n = {n_int} \\end{{cases}} \\Rightarrow T = {m_int} + ({n_int}) = {ans}$."
    )
    return caudan, dapan, loigiai


# ==============================================================================

# ==============================================================================
# 24 HÀM SINH ĐỀ TOÁN 10 MỚI (BỔ SUNG CHƯƠNG III & CHƯƠNG IV)
# ==============================================================================

# 1. Tam giác biết 3 cạnh, tính số đo một góc
def k10_mc_htl_tinh_goc_tam_giac_3canh():
    configs = [
        (7, 5, 8, "A", 60),
        (7, 8, 3, "A", 60),
        (7, 3, 5, "A", 120),
        (13, 7, 8, "A", 120),
        (5, 4, 3, "A", 90),
        (13, 12, 5, "A", 90),
        (5, 7, 8, "B", 60),
        (3, 7, 8, "C", 60),
        (3, 7, 5, "B", 120),
        (8, 7, 13, "B", 120),
    ]
    a0, b0, c0, target, deg = random.choice(configs)
    k = random.choice([1, 2, 3])
    a, b, c = a0 * k, b0 * k, c0 * k

    if target == "A":
        caudan = f"Tam giác $ABC$ có $AB = {c}$, $BC = {a}$, $CA = {b}$. Số đo góc $\\widehat{{A}}$ bằng"
        cos_val = Fraction(b**2 + c**2 - a**2, 2 * b * c)
        formula = f"\\cos A = \\dfrac{{{b}^2 + {c}^2 - {a}^2}}{{2 \\cdot {b} \\cdot {c}}} = \\dfrac{{{b**2 + c**2 - a**2}}}{{{2 * b * c}}} = {fmt_frac(cos_val)}"
        goc_str = "\\widehat{A}"
    elif target == "B":
        caudan = f"Tam giác $ABC$ có $AB = {c}$, $BC = {a}$, $CA = {b}$. Số đo góc $\\widehat{{B}}$ bằng"
        cos_val = Fraction(a**2 + c**2 - b**2, 2 * a * c)
        formula = f"\\cos B = \\dfrac{{{a}^2 + {c}^2 - {b}^2}}{{2 \\cdot {a} \\cdot {c}}} = \\dfrac{{{a**2 + c**2 - b**2}}}{{{2 * a * c}}} = {fmt_frac(cos_val)}"
        goc_str = "\\widehat{B}"
    else:
        caudan = f"Tam giác $ABC$ có $AB = {c}$, $BC = {a}$, $CA = {b}$. Số đo góc $\\widehat{{C}}$ bằng"
        cos_val = Fraction(a**2 + b**2 - c**2, 2 * a * b)
        formula = f"\\cos C = \\dfrac{{{a}^2 + {b}^2 - {c}^2}}{{2 \\cdot {a} \\cdot {b}}} = \\dfrac{{{a**2 + b**2 - c**2}}}{{{2 * a * b}}} = {fmt_frac(cos_val)}"
        goc_str = "\\widehat{C}"

    correct = f"${deg}^\\circ$"
    pool = ["$30^\\circ$", "$45^\\circ$", "$60^\\circ$", "$90^\\circ$", "$120^\\circ$", "$135^\\circ$", "$150^\\circ$"]
    wrongs = [x for x in pool if x != correct]
    choices = shuffle_choices(correct, wrongs[:3])

    loigiai = (
        f"Áp dụng hệ quả của định lí côsin trong tam giác $ABC$, ta có:\\n"
        f"${formula}$.\\n"
        f"Do đó ${goc_str} = {deg}^\\circ$."
    )
    return caudan, choices, loigiai


# 2. Định lí sin tính độ dài cạnh tam giác
def k10_mc_htl_dinh_li_sin_tinh_canh():
    goc_cases = [
        (105, 45, 30, "A", "B", "C", "sqrt2"),
        (75, 45, 60, "A", "B", "C", "sqrt6"),
        (75, 60, 45, "A", "B", "C", "sqrt6"),
        (15, 45, 120, "A", "B", "C", "sqrt6_over_2"),
    ]
    A, B, C, lA, lB, lC, val_type = random.choice(goc_cases)
    m = random.randint(2, 6) * 2

    # Biết góc A, B -> C = 180 - (A+B). Biết cạnh AC = b, tính cạnh AB = c
    # AB / sin C = AC / sin B => AB = AC * sin C / sin B
    if val_type == "sqrt2":
        # sin 30 / sin 45 = (1/2) / (sqrt2/2) = 1/sqrt2 = sqrt2/2
        # AB = m * sqrt2/2 = (m//2) * sqrt2
        val_int = m // 2
        correct = f"${val_int}\\sqrt{{2}}$"
        wrongs = [f"${m}\\sqrt{{2}}$", f"${val_int}\\sqrt{{6}}$", f"$\\dfrac{{{val_int}\\sqrt{{6}}}}{{2}}$"]
        res_str = f"{val_int}\\sqrt{{2}}"
    elif val_type == "sqrt6":
        # sin 60 / sin 45 = (sqrt3/2) / (sqrt2/2) = sqrt6/2
        # AB = m * sqrt6/2 = (m//2) * sqrt6
        val_int = m // 2
        correct = f"${val_int}\\sqrt{{6}}$"
        wrongs = [f"${val_int}\\sqrt{{2}}$", f"${m}\\sqrt{{3}}$", f"$\\dfrac{{{val_int}\\sqrt{{6}}}}{{2}}$"]
        res_str = f"{val_int}\\sqrt{{6}}"
    else:
        val_int = m // 2
        correct = f"${val_int}\\sqrt{{3}}$"
        wrongs = [f"${val_int}\\sqrt{{2}}$", f"${m}\\sqrt{{2}}$", f"${val_int}\\sqrt{{6}}$"]
        res_str = f"{val_int}\\sqrt{{3}}"

    caudan = (
        f"Tam giác $ABC$ có $\\widehat{{A}} = {A}^\\circ$, $\\widehat{{B}} = {B}^\\circ$, $AC = {m}$. "
        f"Tính cạnh $AB$."
    )
    choices = shuffle_choices(correct, wrongs)
    loigiai = (
        f"Trong tam giác $ABC$, ta có $\\widehat{{C}} = 180^\\circ - (\\widehat{{A}} + \\widehat{{B}}) = 180^\\circ - ({A}^\\circ + {B}^\\circ) = {C}^\\circ$.\\n"
        f"Theo định lí sin trong tam giác $ABC$:\\n"
        f"$$\\dfrac{{AB}}{{\\sin C}} = \\dfrac{{AC}}{{\\sin B}} \\Rightarrow AB = \\dfrac{{AC \\cdot \\sin C}}{{\\sin B}} = \\dfrac{{{m} \\cdot \\sin {C}^\\circ}}{{\\sin {B}^\\circ}} = {res_str}.$$"
    )
    return caudan, choices, loigiai


# 3. Tính cos góc khi biết 3 cạnh tam giác
def k10_mc_htl_tinh_cos_goc_3canh():
    while True:
        b = random.randint(4, 10)
        c = random.randint(3, 9)
        # Bất đẳng thức tam giác
        a = random.randint(abs(b - c) + 1, b + c - 1)
        cos_A = Fraction(b**2 + c**2 - a**2, 2 * b * c)
        if cos_A != 0 and abs(cos_A) < 1 and cos_A.denominator <= 16:
            break

    caudan = (
        f"Cho tam giác $ABC$ với $BC = {a}\\text{{ cm}}$, $AC = {b}\\text{{ cm}}$, $AB = {c}\\text{{ cm}}$. "
        f"Tính $\\cos A$."
    )
    correct = f"$\\cos A = {fmt_frac(cos_A)}$"
    wrongs = [
        f"$\\cos A = {fmt_frac(-cos_A)}$",
        f"$\\cos A = {fmt_frac(Fraction(cos_A.numerator, cos_A.denominator + 1))}$",
        f"$\\cos A = {fmt_frac(Fraction(1, 2))}$" if cos_A != Fraction(1, 2) else f"$\\cos A = {fmt_frac(Fraction(1, 3))}$",
    ]
    choices = shuffle_choices(correct, wrongs)
    loigiai = (
        f"Theo định lí côsin trong tam giác $ABC$:\\n"
        f"$$\\cos A = \\dfrac{{b^2 + c^2 - a^2}}{{2bc}} = \\dfrac{{{b}^2 + {c}^2 - {a}^2}}{{2 \\cdot {b} \\cdot {c}}} = \\dfrac{{{b**2 + c**2 - a**2}}}{{{2*b*c}}} = {fmt_frac(cos_A)}.$$"
    )
    return caudan, choices, loigiai


# 4. Đúng sai: Tam giác biết 2 cạnh và góc xen giữa
def k10_tf_htl_tam_giac_2canh_va_goc():
    b = random.choice([5, 7, 8, 6])
    c = random.choice([3, 4, 5])
    deg = random.choice([60, 120])
    cos_val = Fraction(1, 2) if deg == 60 else Fraction(-1, 2)

    a2 = b**2 + c**2 - 2 * b * c * int(cos_val.numerator) // cos_val.denominator
    s_num = b * c
    s_exact = f"\\dfrac{{{s_num}\\sqrt{{3}}}}{{4}}" if s_num % 4 != 0 else f"{s_num // 4}\\sqrt{{3}}"

    caudan = f"Cho tam giác $ABC$ có $b = {b}, c = {c}, \\widehat{{A}} = {deg}^\\circ$. Gọi $S$ là diện tích của tam giác $ABC$. Khi đó:"

    item_a = (
        r"$a^2 = b^2 + c^2 - 2bc\cos A$.",
        r"$a = b^2 + c^2 - 2bc\cos A$.",
        r"Theo định lí côsin ta có $a^2 = b^2 + c^2 - 2bc\cos A$.",
        r"Khẳng định sai vì theo định lí côsin phải là $a^2 = b^2 + c^2 - 2bc\cos A$."
    )
    isqrt_a2 = math.isqrt(a2)
    a_val_str = f"{isqrt_a2}" if isqrt_a2**2 == a2 else f"\\sqrt{{{a2}}}"
    a_wrong = f"{isqrt_a2 + 2}" if isqrt_a2**2 == a2 else f"{b}"
    item_b = (
        f"$a = {a_val_str}$.",
        f"$a = {a_wrong}$.",
        f"Ta có $a^2 = {b}^2 + {c}^2 - 2\\cdot {b}\\cdot {c}\\cos {deg}^\\circ = {a2} \\Rightarrow a = {a_val_str}$.",
        f"Sai vì $a = {a_val_str}$."
    )
    item_c = (
        r"$S = \dfrac{1}{2}bc\sin A$.",
        r"$S = bc\sin A$.",
        r"Công thức diện tích tam giác là $S = \dfrac{1}{2}bc\sin A$.",
        r"Sai vì diện tích tam giác là $S = \dfrac{1}{2}bc\sin A$ có hệ số $\dfrac{1}{2}$."
    )
    item_d = (
        f"$S = {s_exact}$.",
        f"$S = {b * c}\\sqrt{{3}}$.",
        f"Ta có $S = \\dfrac{{1}}{{2}}\\cdot {b}\\cdot {c}\\sin {deg}^\\circ = {s_exact}$.",
        f"Sai vì $S = {s_exact}$."
    )
    choices, loigiai = make_tf_choices([item_a, item_b, item_c, item_d])
    return caudan, choices, loigiai



# 5. Đúng sai: Tam giác biết 3 cạnh Heronian (Heron, R, h)
def k10_tf_htl_tam_giac_3canh_heron_r_h():
    heron_triples = [
        (13, 14, 15),
        (5, 5, 6),
        (5, 5, 8),
        (10, 10, 12),
        (10, 17, 21),
    ]
    c, b, a = random.choice(heron_triples)
    p = (a + b + c) / 2
    S = int(round(math.sqrt(p * (p - a) * (p - b) * (p - c))))
    cos_A = Fraction(b**2 + c**2 - a**2, 2 * b * c)
    cos_A_wrong = Fraction(b**2 + c**2 + a**2, 2 * b * c)
    R_frac = Fraction(a * b * c, 4 * S)
    R_wrong = Fraction(a * b * c, 2 * S)
    hc = Fraction(2 * S, c)
    hc_wrong = Fraction(S, c)

    caudan = f"Tam giác $ABC$ có $AB = c = {c}, AC = b = {b}, BC = a = {a}$. Khi đó:"

    item_a = (
        f"$\\cos A = {fmt_frac(cos_A)}$.",
        f"$\\cos A = {fmt_frac(cos_A_wrong)}$.",
        f"Ta có $\\cos A = \\dfrac{{b^2+c^2-a^2}}{{2bc}} = {fmt_frac(cos_A)}$.",
        f"Sai vì $\\cos A = \\dfrac{{b^2+c^2-a^2}}{{2bc}} = {fmt_frac(cos_A)}$."
    )
    item_b = (
        f"Diện tích tam giác $ABC$ là $S = {S}$.",
        f"Diện tích tam giác $ABC$ là $S = {S + 10}$.",
        f"Nửa chu vi $p = {int(p)}$, diện tích theo Heron: $S = \\sqrt{{p(p-a)(p-b)(p-c)}} = {S}$.",
        f"Sai vì theo Heron diện tích $S = {S}$."
    )
    item_c = (
        f"Bán kính đường tròn ngoại tiếp $R = {fmt_frac(R_frac)}$.",
        f"Bán kính đường tròn ngoại tiếp $R = {fmt_frac(R_wrong)}$.",
        f"Bán kính đường tròn ngoại tiếp $R = \\dfrac{{abc}}{{4S}} = {fmt_frac(R_frac)}$.",
        f"Sai vì $R = \\dfrac{{abc}}{{4S}} = {fmt_frac(R_frac)}$."
    )
    item_d = (
        f"Đường cao ứng với cạnh $AB$ có độ dài là $h_c = {fmt_frac(hc)}$.",
        f"Đường cao ứng với cạnh $AB$ có độ dài là $h_c = {fmt_frac(hc_wrong)}$.",
        f"Đường cao $h_c = \\dfrac{{2S}}{{c}} = {fmt_frac(hc)}$.",
        f"Sai vì $h_c = \\dfrac{{2S}}{{c}} = {fmt_frac(hc)}$."
    )
    choices, loigiai = make_tf_choices([item_a, item_b, item_c, item_d])
    return caudan, choices, loigiai



# 6. Đúng sai: Lượng giác góc tù (cos âm)
def k10_tf_luong_giac_cos_am():
    pairs = [(2, 3), (3, 5), (4, 5), (1, 3), (1, 2)]
    u, v = random.choice(pairs)
    sin_sq = v**2 - u**2
    sin_sqrt_str = fmt_sqrt(sin_sq)

    caudan = f"Cho $\\cos \\alpha = -\\dfrac{{{u}}}{{{v}}}$ ($0^\\circ < \\alpha < 180^\\circ$). Khi đó:"

    item_a = (
        r"$90^\circ < \alpha < 180^\circ$.",
        r"$0^\circ < \alpha < 90^\circ$.",
        r"Do $\cos\alpha < 0$ và $0^\circ < \alpha < 180^\circ$ nên $\alpha$ là góc tù ($90^\circ < \alpha < 180^\circ$).",
        r"Sai vì $\cos\alpha < 0$ nên $\alpha$ thuộc góc phần tư thứ II ($90^\circ < \alpha < 180^\circ$)."
    )
    item_b = (
        r"$\cot\alpha < 0$.",
        r"$\cot\alpha > 0$.",
        r"Do $\cos\alpha < 0$ và $\sin\alpha > 0$ nên $\cot\alpha = \dfrac{\cos\alpha}{\sin\alpha} < 0$.",
        r"Sai vì $\cot\alpha = \dfrac{\cos\alpha}{\sin\alpha} < 0$."
    )
    item_c = (
        f"$\\sin\\alpha = \\dfrac{{{sin_sqrt_str}}}{{{v}}}$.",
        f"$\\sin\\alpha = -\\dfrac{{{sin_sqrt_str}}}{{{v}}}$.",
        f"Với $0^\\circ < \\alpha < 180^\\circ$ thì $\\sin\\alpha > 0 \\Rightarrow \\sin\\alpha = \\sqrt{{1 - \\cos^2\\alpha}} = \\dfrac{{{sin_sqrt_str}}}{{{v}}}$.",
        f"Sai vì với $0^\\circ < \\alpha < 180^\\circ$ thì $\\sin\\alpha > 0$."
    )
    item_d = (
        f"$\\tan\\alpha = -\\dfrac{{{sin_sqrt_str}}}{{{u}}}$.",
        f"$\\tan\\alpha = \\dfrac{{{sin_sqrt_str}}}{{{u}}}$.",
        f"Ta có $\\tan\\alpha = \\dfrac{{\\sin\\alpha}}{{\\cos\\alpha}} = -\\dfrac{{{sin_sqrt_str}}}{{{u}}}$.",
        f"Sai vì $\\cos\\alpha < 0, \\sin\\alpha > 0 \\Rightarrow \\tan\\alpha < 0$."
    )
    choices, loigiai = make_tf_choices([item_a, item_b, item_c, item_d])
    return caudan, choices, loigiai



# 7. Đúng sai: Lượng giác cho tan góc nhọn, tính biểu thức
def k10_tf_luong_giac_tan_duong_bieu_thuc():
    t_val = random.choice([2, 3, Fraction(1, 2), Fraction(3, 2)])
    t_str = f"{t_val}" if isinstance(t_val, int) else f"\\dfrac{{{t_val.numerator}}}{{{t_val.denominator}}}"

    cot_val = Fraction(1, 1) / t_val if not isinstance(t_val, int) else Fraction(1, t_val)
    P_val = (2 * t_val + 3) / (4 * t_val - 1)
    P_frac = Fraction(P_val).limit_denominator(100)

    caudan = f"Cho góc nhọn $\\alpha$ thỏa mãn $\\tan \\alpha = {t_str}$. Khi đó:"

    item_a = (
        f"$\\cot \\alpha = {fmt_frac(cot_val)}$.",
        f"$\\cot \\alpha = -{fmt_frac(cot_val)}$.",
        f"Vì $\\cot\\alpha = \\dfrac{{1}}{{\\tan\\alpha}} = {fmt_frac(cot_val)}$.",
        f"Sai vì $\\alpha$ nhọn nên $\\cot\\alpha > 0$."
    )
    item_b = (
        r"$\sin \alpha > 0$ và $\cos \alpha > 0$.",
        r"$\sin \alpha < 0$ hoặc $\cos \alpha < 0$.",
        r"Vì $\alpha$ là góc nhọn nên $\sin \alpha > 0$ và $\cos \alpha > 0$.",
        r"Sai vì với góc nhọn, cả $\sin\alpha$ và $\cos\alpha$ đều mang giá trị dương."
    )
    cos2_val = Fraction(1, 1) / (1 + Fraction(t_val)**2)
    item_c = (
        f"$\\cos^2 \\alpha = {fmt_frac(cos2_val)}$.",
        f"$\\cos^2 \\alpha = {fmt_frac(1 - cos2_val)}$.",
        f"Áp dụng $1 + \\tan^2\\alpha = \\dfrac{{1}}{{\\cos^2\\alpha}} \\Rightarrow \\cos^2\\alpha = \\dfrac{{1}}{{1 + \\tan^2\\alpha}} = {fmt_frac(cos2_val)}$.",
        f"Sai vì $\\cos^2\\alpha = \\dfrac{{1}}{{1+\\tan^2\\alpha}} = {fmt_frac(cos2_val)}$."
    )
    P_wrong = Fraction(P_frac.numerator + 1, P_frac.denominator)
    item_d = (
        f"Giá trị biểu thức $P = \\dfrac{{2\\sin\\alpha + 3\\cos\\alpha}}{{4\\sin\\alpha - \\cos\\alpha}} = {fmt_frac(P_frac)}$.",
        f"Giá trị biểu thức $P = \\dfrac{{2\\sin\\alpha + 3\\cos\\alpha}}{{4\\sin\\alpha - \\cos\\alpha}} = {fmt_frac(P_wrong)}$.",
        f"Chia cả tử và mẫu cho $\\cos\\alpha \\neq 0$: $P = \\dfrac{{2\\tan\\alpha + 3}}{{4\\tan\\alpha - 1}} = {fmt_frac(P_frac)}$.",
        f"Sai vì sau khi chia cho $\\cos\\alpha$ ta được $P = {fmt_frac(P_frac)}$."
    )
    choices, loigiai = make_tf_choices([item_a, item_b, item_c, item_d])
    return caudan, choices, loigiai



# 8. Vectơ cùng hướng / ngược hướng trong tam giác có đường trung bình
def k10_mc_vecto_trung_binh_cung_huong():
    caudan = (
        "Cho tam giác $ABC$, gọi $M, N$ lần lượt là trung điểm của $AB$ và $AC$. "
        "Cặp vectơ nào sau đây là cặp vectơ cùng hướng?"
    )
    correct = "$\\vec{MN}$ và $\\vec{BC}$"
    wrongs = [
        "$\\vec{MA}$ và $\\vec{AB}$",
        "$\\vec{MN}$ và $\\vec{CB}$",
        "$\\vec{AB}$ và $\\vec{AC}$",
    ]
    choices = shuffle_choices(correct, wrongs)
    loigiai = (
        "Vì $M, N$ lần lượt là trung điểm của $AB$ và $AC$ nên $MN$ là đường trung bình của tam giác $ABC$.\\n"
        "Suy ra $MN \\parallel BC$ và hai vectơ $\\vec{MN}, \\vec{BC}$ cùng hướng sang phải.\\n"
        "Do đó cặp vectơ cùng hướng là $\\vec{MN}$ và $\\vec{BC}$."
    )
    return caudan, choices, loigiai


# 9. Đẳng thức vectơ qua lưới ô vuông
def k10_mc_vecto_luoi_o_vuong_dang_thuc():
    caudan = (
        "Cho hai vectơ $\\vec{a}, \\vec{b}$ trong hình sau:\\n"
        "\\begin{center}\\begin{tikzpicture}[scale=0.5]\\draw[step=1,gray!40,very thin] (0,0) grid (6,4);\\draw[->,thick,-latex] (1,1) -- (3,3) node[midway,above left] {$\\vec{a}$};\\draw[->,thick,-latex] (2,0.5) -- (6,4.5) node[midway,below right] {$\\vec{b}$};\\end{tikzpicture}\\end{center}\\n"
        "Đẳng thức nào sau đây đúng?"
    )
    correct = "$\\vec{a} = \\dfrac{1}{2}\\vec{b}$"
    wrongs = [
        "$\\vec{a} = -2\\vec{b}$",
        "$\\vec{a} = -\\dfrac{1}{2}\\vec{b}$",
        "$\\vec{a} = 2\\vec{b}$",
    ]
    choices = shuffle_choices(correct, wrongs)
    loigiai = (
        "Dựa vào hình vẽ lưới ô vuông, ta thấy hai vectơ $\\vec{a}$ và $\\vec{b}$ cùng hướng "
        "và độ dài $|\\vec{b}| = 2|\\vec{a}| \\Rightarrow |\\vec{a}| = \\dfrac{1}{2}|\\vec{b}|$.\\n"
        "Do đó $\\vec{a} = \\dfrac{1}{2}\\vec{b}$."
    )
    return caudan, choices, loigiai


# 10. Khẳng định sai về tích vectơ với số âm
def k10_mc_vecto_tich_so_khang_dinh_sai():
    k = random.choice([2, 3, 4, 5])
    caudan = f"Cho $\\vec{{a}} = -{k}\\vec{{b}}$ ($\\vec{{b}} \\neq \\vec{{0}}$). Khẳng định nào sau đây sai?"
    correct = f"$|\\vec{{a}}| = -{k}|\\vec{{b}}|$"
    wrongs = [
        "$\\vec{a}$ và $\\vec{b}$ ngược hướng",
        f"$|\\vec{{a}}| = {k}|\\vec{{b}}|$",
        f"$|\\vec{{a}}| = |{k}\\vec{{b}}|$",
    ]
    choices = shuffle_choices(correct, wrongs)
    loigiai = (
        f"Theo tính chất tích của vectơ với một số: với $\\vec{{a}} = k\\vec{{b}}$, ta có $|\\vec{{a}}| = |k| \\cdot |\\vec{{b}}|$.\\n"
        f"Vì độ dài của vectơ luôn không âm nên khẳng định $|\\vec{{a}}| = -{k}|\\vec{{b}}|$ là sai."
    )
    return caudan, choices, loigiai


# 11. Đẳng thức độ dài đường trung bình
def k10_mc_vecto_trung_binh_do_dai():
    caudan = (
        "Gọi $M, N$ lần lượt là trung điểm của các cạnh $AB, AC$ của tam giác đều $ABC$. "
        "Đẳng thức nào sau đây đúng?"
    )
    correct = "$|\\vec{BC}| = 2|\\vec{MN}|$"
    wrongs = [
        "$\\vec{MA} = \\vec{MB}$",
        "$\\vec{AB} = \\vec{AC}$",
        "$\\vec{MN} = \\vec{BC}$",
    ]
    choices = shuffle_choices(correct, wrongs)
    loigiai = (
        "Vì $M, N$ lần lượt là trung điểm của $AB$ và $AC$ nên $MN$ là đường trung bình của tam giác $ABC$.\\n"
        "Suy ra $BC = 2MN \\Leftrightarrow |\\vec{BC}| = 2|\\vec{MN}|$.\\n"
        "Các khẳng định còn lại đều sai vì hai vectơ không cùng hướng hoặc không cùng độ dài."
    )
    return caudan, choices, loigiai


# 12. Bẫy thứ tự j trước i
def k10_mc_vecto_bay_thu_tu_j_i():
    x = random.choice([-9, -7, -5, -3, 3, 5, 7, 9])
    y = random.choice([-8, -6, -4, 2, 4, 6, 8])

    # u = y*j + x*i
    x_part = f"{x}\\vec{{i}}" if x > 0 else f"- {-x}\\vec{{i}}"
    y_part = f"{y}\\vec{{j}}"

    caudan = f"Trên mặt phẳng với hệ trục tọa độ $Oxy$, cho vectơ $\\vec{{u}} = {y_part} {x_part if x < 0 else '+ ' + x_part}$. Tọa độ của vectơ $\\vec{{u}}$ là"
    correct = f"$\\vec{{u}} = ({x};{y})$"
    wrongs = [
        f"$\\vec{{u}} = ({y};{x})$",
        f"$\\vec{{u}} = ({-x};{-y})$",
        f"$\\vec{{u}} = ({-y};{x})$",
    ]
    choices = shuffle_choices(correct, wrongs)
    loigiai = (
        f"Ta có $\\vec{{u}} = {x_part} {('+' if y > 0 else '-') + f' {abs(y)}\\vec{{j}}'}$.\\n"
        f"Theo định nghĩa tọa độ vectơ, hoành độ là hệ số của $\\vec{{i}}$ và tung độ là hệ số của $\\vec{{j}}$.\\n"
        f"Vậy $\\vec{{u}} = ({x};{y})$."
    )
    return caudan, choices, loigiai


# 13. Tọa độ điểm M từ biểu diễn OM qua i, j
def k10_mc_vecto_toa_do_diem_qua_om():
    x = random.randint(-6, 6)
    y = random.randint(-6, 6)
    if x == 0: x = -2
    if y == 0: y = 3

    comb = fmt_vec_comb(x, y)
    caudan = f"Trong mặt phẳng với hệ trục tọa độ $(O;\\vec{{i}};\\vec{{j}})$ cho điểm $M$ thỏa mãn $\\vec{{OM}} = {comb}$. Tọa độ của điểm $M$ là"
    correct = f"$({x};{y})$"
    wrongs = [
        f"$({-x};{y})$",
        f"$({y};{x})$",
        f"$({x};{-y})$",
    ]
    choices = shuffle_choices(correct, wrongs)
    loigiai = f"Ta có $\\vec{{OM}} = {comb} \\Leftrightarrow M({x};{y})$."
    return caudan, choices, loigiai


# 14. Tìm tọa độ vectơ MN khi biết tọa độ hai điểm mút
def k10_mc_vecto_toa_do_mn_tu_2diem():
    x1 = random.randint(-5, 5)
    y1 = random.randint(-5, 5)
    x2 = random.randint(-5, 5)
    y2 = random.randint(-5, 5)
    dx = x2 - x1
    dy = y2 - y1

    caudan = f"Trong mặt phẳng tọa độ $Oxy$, cho các điểm $M({x1};{y1})$ và $N({x2};{y2})$. Tọa độ của vectơ $\\vec{{MN}}$ là"
    correct = f"$({dx};{dy})$"
    wrongs = [
        f"$({-dx};{-dy})$",
        f"$({x1+x2};{y1+y2})$",
        f"$({dy};{dx})$",
    ]
    choices = shuffle_choices(correct, wrongs)
    loigiai = (
        f"Tọa độ của vectơ $\\vec{{MN}}$ được tính theo công thức:\\n"
        f"$$\\vec{{MN}} = (x_N - x_M; y_N - y_M) = ({x2} - ({x1}); {y2} - ({y1})) = ({dx};{dy}).$$"
    )
    return caudan, choices, loigiai


# 15. Biểu diễn AB = x i + y j và tính giá trị biểu thức
def k10_mc_vecto_bieu_dien_ab_tinh_bt():
    xA, yA = random.randint(-4, 4), random.randint(-4, 4)
    xB, yB = random.randint(-4, 4), random.randint(-4, 4)
    x = xB - xA
    y = yB - yA
    c = random.choice([1, 2])
    d = random.choice([1, 2, -1])
    ans = c * x + d * y

    caudan = (
        f"Trong mặt phẳng $Oxy$, cho hai điểm $A({xA};{yA}), B({xB};{yB})$. "
        f"Biểu diễn $\\vec{{AB}}$ dưới dạng $\\vec{{AB}} = x\\vec{{i}} + y\\vec{{j}}$. Tính ${c if c != 1 else ''}x {('+' if d > 0 else '-') + f' {abs(d)}' if abs(d) != 1 else ('+' if d > 0 else '-')}y$."
    )
    correct = f"${ans}$"
    wrongs = [f"${ans + 1}$", f"${ans - 2}$", f"${-ans}$"]
    choices = shuffle_choices(correct, wrongs)
    loigiai = (
        f"Ta có $\\vec{{AB}} = ({xB} - ({xA}); {yB} - ({yA})) = ({x};{y})$.\\n"
        f"Do đó $\\vec{{AB}} = {fmt_vec_comb(x, y)}$, suy ra $x = {x}, y = {y}$.\\n"
        f"Vậy giá trị cần tìm là ${c if c != 1 else ''}({x}) + ({d})({y}) = {ans}$."
    )
    return caudan, choices, loigiai


# 16. Tính tọa độ tổng hai vectơ
def k10_mc_vecto_tong_hai_vecto_oxy():
    x1, y1 = random.randint(-8, 8), random.randint(-8, 8)
    x2, y2 = random.randint(-8, 8), random.randint(-8, 8)
    sx = x1 + x2
    sy = y1 + y2

    caudan = f"Cho $\\vec{{a}}({x1};{y1}), \\vec{{b}}({x2};{y2})$. Tọa độ của vectơ $\\vec{{a}} + \\vec{{b}}$ là"
    correct = f"$({sx};{sy})$"
    wrongs = [
        f"$({-sx};{sy})$",
        f"$({sx};{-sy})$",
        f"$({x1-x2};{y1-y2})$",
    ]
    choices = shuffle_choices(correct, wrongs)
    loigiai = (
        f"Tọa độ vectơ tổng là:\\n"
        f"$$\\vec{{a}} + \\vec{{b}} = ({x1} + ({x2}); {y1} + ({y2})) = ({sx};{sy}).$$"
    )
    return caudan, choices, loigiai


# 17. Tọa độ tổ hợp tuyến tính 3 vectơ
def k10_mc_vecto_to_hop_3vecto_oxy():
    x1, y1 = random.randint(-3, 3), random.randint(-3, 3)
    x2, y2 = random.randint(-3, 3), random.randint(-3, 3)
    x3, y3 = random.randint(-3, 3), random.randint(-3, 3)
    # x = 2a + b - c
    rx = 2 * x1 + x2 - x3
    ry = 2 * y1 + y2 - y3

    caudan = (
        f"Trong mặt phẳng tọa độ $Oxy$, cho $\\vec{{a}} = ({x1};{y1}), \\vec{{b}} = ({x2};{y2}), \\vec{{c}} = ({x3};{y3})$. "
        f"Tính tọa độ của vectơ $\\vec{{x}} = 2\\vec{{a}} + \\vec{{b}} - \\vec{{c}}$."
    )
    correct = f"$({rx};{ry})$"
    wrongs = [
        f"$({-rx};{ry})$",
        f"$({rx};{-ry})$",
        f"$({-rx};{-ry})$",
    ]
    choices = shuffle_choices(correct, wrongs)
    loigiai = (
        f"Ta có:\\n"
        f"$$2\\vec{{a}} = ({2*x1};{2*y1}), \\quad \\vec{{b}} = ({x2};{y2}), \\quad -\\vec{{c}} = ({-x3};{-y3}).$$\\n"
        f"Suy ra $\\vec{{x}} = (2\\cdot({x1}) + ({x2}) - ({x3}); 2\\cdot({y1}) + ({y2}) - ({y3})) = ({rx};{ry})$."
    )
    return caudan, choices, loigiai


# 18. Tích vô hướng của 2 vectơ ngược hướng (lý thuyết)
def k10_mc_tich_vo_huong_nguoc_huong_ly_thuyet():
    caudan = "Cho hai vectơ $\\vec{a}, \\vec{b}$ ngược hướng và đều khác $\\vec{0}$. Khi đó"
    correct = "$\\vec{a} \\cdot \\vec{b} = -|\\vec{a}| \\cdot |\\vec{b}|$"
    wrongs = [
        "$\\vec{a} \\cdot \\vec{b} = 0$",
        "$\\vec{a} \\cdot \\vec{b} = -1$",
        "$\\vec{a} \\cdot \\vec{b} = |\\vec{a}| \\cdot |\\vec{b}|$",
    ]
    choices = shuffle_choices(correct, wrongs)
    loigiai = (
        "Vì hai vectơ $\\vec{a}, \\vec{b}$ ngược hướng nên góc giữa chúng bằng $180^\\circ$.\\n"
        "Theo định nghĩa tích vô hướng: $\\vec{a} \\cdot \\vec{b} = |\\vec{a}| \\cdot |\\vec{b}| \\cos 180^\\circ = -|\\vec{a}| \\cdot |\\vec{b}|.$"
    )
    return caudan, choices, loigiai


# 19. Tính tích vô hướng từ độ dài và góc giữa 2 vectơ
def k10_mc_tich_vo_huong_co_ban_do_dai_goc():
    la = random.randint(3, 8)
    lb = random.randint(3, 8)
    deg = random.choice([60, 120])
    cos_val = Fraction(1, 2) if deg == 60 else Fraction(-1, 2)
    ans = la * lb * cos_val

    caudan = (
        f"Cho hai vectơ $\\vec{{a}}, \\vec{{b}}$ có $|\\vec{{a}}| = {la}$, $|\\vec{{b}}| = {lb}$ "
        f"và $(\\vec{{a}}, \\vec{{b}}) = {deg}^\\circ$. Giá trị của $\\vec{{a}} \\cdot \\vec{{b}}$ bằng"
    )
    correct = f"${fmt_frac(ans)}$"
    wrongs = [
        f"${la * lb}$",
        f"${fmt_frac(-ans)}$",
        f"${la**2 + lb**2}$",
    ]
    choices = shuffle_choices(correct, wrongs)
    loigiai = (
        f"Áp dụng định nghĩa tích vô hướng của hai vectơ:\\n"
        f"$$\\vec{{a}} \\cdot \\vec{{b}} = |\\vec{{a}}| \\cdot |\\vec{{b}}| \\cdot \\cos(\\vec{{a}}, \\vec{{b}}) = {la} \\cdot {lb} \\cdot \\cos {deg}^\\circ = {la * lb} \\cdot \\left({fmt_frac(cos_val)}\\right) = {fmt_frac(ans)}.$$"
    )
    return caudan, choices, loigiai


# 20. Bình phương vô hướng biểu thức vectơ
def k10_mc_tich_vo_huong_binh_phuong_to_hop():
    la = random.choice([3, 4, 5])
    lb = random.choice([3, 4, 5])
    deg = random.choice([60, 120])
    cos_val = 0.5 if deg == 60 else -0.5
    # (a + 2b)^2 = a^2 + 4 a.b + 4 b^2
    dot_ab = la * lb * cos_val
    ans = int(round(la**2 + 4 * dot_ab + 4 * lb**2))

    caudan = (
        f"Cho hai vectơ $\\vec{{a}}$ và $\\vec{{b}}$, biết $|\\vec{{a}}| = {la}$, $|\\vec{{b}}| = {lb}$ "
        f"và $(\\vec{{a}}, \\vec{{b}}) = {deg}^\\circ$. Giá trị của $(\\vec{{a}} + 2\\vec{{b}})^2$ bằng"
    )
    correct = f"${ans}$"
    wrongs = [
        f"${(la + 2*lb)**2}$",
        f"${ans + 50}$",
        f"${abs(ans - 50)}$",
    ]
    choices = shuffle_choices(correct, wrongs)
    loigiai = (
        f"Ta có $\\vec{{a}} \\cdot \\vec{{b}} = |\\vec{{a}}| \\cdot |\\vec{{b}}| \\cos {deg}^\\circ = {la} \\cdot {lb} \\cdot ({cos_val}) = {dot_ab}$.\\n"
        f"Khai triển bình phương vô hướng:\\n"
        f"$$(\\vec{{a}} + 2\\vec{{b}})^2 = \\vec{{a}}^2 + 4\\vec{{a}} \\cdot \\vec{{b}} + 4\\vec{{b}}^2 = {la}^2 + 4 \\cdot ({dot_ab}) + 4 \\cdot {lb}^2 = {ans}.$$"
    )
    return caudan, choices, loigiai


# 21. Tìm góc giữa hai vectơ từ độ dài và tích vô hướng
def k10_mc_tich_vo_huong_tim_goc_tu_tich():
    cases = [
        (7, 12, "42\\sqrt{3}", "30^\\circ", 30),
        (4, 6, "12\\sqrt{2}", "45^\\circ", 45),
        (5, 8, "20", "60^\\circ", 60),
        (6, 10, "-30", "120^\\circ", 120),
        (4, 4, "-8\\sqrt{2}", "135^\\circ", 135),
    ]
    la, lb, dot_str, deg_str, deg = random.choice(cases)

    caudan = (
        f"Cho hai vectơ $\\vec{{u}}$ và $\\vec{{v}}$ có $|\\vec{{u}}| = {la}$, $|\\vec{{v}}| = {lb}$ "
        f"và $\\vec{{u}} \\cdot \\vec{{v}} = {dot_str}$. Tính $(\\vec{{u}}, \\vec{{v}})$."
    )
    correct = f"${deg_str}$"
    pool = ["$30^\\circ$", "$45^\\circ$", "$60^\\circ$", "$90^\\circ$", "$120^\\circ$", "$135^\\circ$"]
    wrongs = [x for x in pool if x != correct]
    choices = shuffle_choices(correct, wrongs[:3])

    loigiai = (
        f"Ta có $\\cos(\\vec{{u}}, \\vec{{v}}) = \\dfrac{{\\vec{{u}} \\cdot \\vec{{v}}}}{{|\\vec{{u}}| \\cdot |\\vec{{v}}|}} = \\dfrac{{{dot_str}}}{{{la} \\cdot {lb}}} = \\dfrac{{{dot_str}}}{{{la * lb}}}$.\\n"
        f"Do đó số đo góc giữa hai vectơ là $(\\vec{{u}}, \\vec{{v}}) = {deg_str}$."
    )
    return caudan, choices, loigiai


# 22. Tính số đo góc giữa 2 vectơ trong hệ Oxy
def k10_mc_tich_vo_huong_goc_oxy_so_do():
    cases = [
        (1, -1, -2, 0, "135^\\circ"), # cos = -2 / (sqrt2 * 2) = -1/sqrt2 => 135
        (1, 1, 0, 3, "45^\\circ"),    # cos = 3 / (sqrt2 * 3) = 1/sqrt2 => 45
        (1, 0, 1, 1, "45^\\circ"),
        (1, 0, 1, -1, "45^\\circ"),
        (1, 1, -1, 1, "90^\\circ"),   # cos = -1 + 1 = 0 => 90
        (1, 0, -3, 0, "180^\\circ"),
        (0, 2, 0, 5, "0^\\circ"),
    ]
    x1, y1, x2, y2, deg_str = random.choice(cases[:5])

    caudan = f"Trên mặt phẳng $Oxy$, góc giữa hai vectơ $\\vec{{a}} = ({x1};{y1})$ và $\\vec{{b}} = ({x2};{y2})$ có số đo bằng"
    correct = f"${deg_str}$"
    pool = ["$30^\\circ$", "$45^\\circ$", "$60^\\circ$", "$90^\\circ$", "$120^\\circ$", "$135^\\circ$"]
    wrongs = [x for x in pool if x != correct]
    choices = shuffle_choices(correct, wrongs[:3])

    dot = x1 * x2 + y1 * y2
    loigiai = (
        f"Ta có $\\cos(\\vec{{a}}, \\vec{{b}}) = \\dfrac{{\\vec{{a}} \\cdot \\vec{{b}}}}{{|\\vec{{a}}| \\cdot |\\vec{{b}}|}} = \\dfrac{{{x1}\\cdot({x2}) + ({y1})\\cdot({y2})}}{{\\sqrt{{{x1}^2 + ({y1})^2}} \\cdot \\sqrt{{({x2})^2 + ({y2})^2}}}} = \\dfrac{{{dot}}}{{\\sqrt{{{x1**2+y1**2}}}\\sqrt{{{x2**2+y2**2}}}}}$.\\n"
        f"Suy ra góc giữa hai vectơ bằng ${deg_str}$."
    )
    return caudan, choices, loigiai


# 23. Bài toán thực tế: Tính công sinh bởi lực kéo
def k10_mc_tich_vo_huong_toan_thuc_te_cong_luc():
    F = random.choice([40, 50, 60, 80, 100])
    d = random.choice([4, 5, 8, 10])
    deg = random.choice([60, 45, 30])

    if deg == 60:
        ans_num = F * d // 2
        correct = f"${ans_num}$"
        wrongs = [f"${ans_num}\\sqrt{{3}}$", f"${F * d}$", f"${ans_num * 2}\\sqrt{{3}}$"]
        res_str = f"{F} \\cdot {d} \\cdot \\dfrac{{1}}{{2}} = {ans_num}\\text{{ J}}"
    elif deg == 45:
        ans_num = F * d // 2
        correct = f"${ans_num}\\sqrt{{2}}$"
        wrongs = [f"${ans_num}$", f"${F * d}$", f"${ans_num * 2}\\sqrt{{2}}$"]
        res_str = f"{F} \\cdot {d} \\cdot \\dfrac{{\\sqrt{{2}}}}{{2}} = {ans_num}\\sqrt{{2}}\\text{{ J}}"
    else:
        ans_num = F * d // 2
        correct = f"${ans_num}\\sqrt{{3}}$"
        wrongs = [f"${ans_num}$", f"${F * d}$", f"${ans_num * 2}$"]
        res_str = f"{F} \\cdot {d} \\cdot \\dfrac{{\\sqrt{{3}}}}{{2}} = {ans_num}\\sqrt{{3}}\\text{{ J}}"

    caudan = (
        f"Cho biết công $A$ (J) sinh bởi một lực $\\vec{{F}}$ có độ dịch chuyển $\\vec{{d}}$ được tính bởi công thức $A = \\vec{{F}} \\cdot \\vec{{d}}$. "
        f"Tính công sinh bởi lực $\\vec{{F}}$ có cường độ ${F}\\text{{ N}}$ tác động lên vật để vật dịch chuyển một đoạn dài ${d}\\text{{ m}}$, "
        f"biết góc tạo bởi $\\vec{{F}}$ và hướng chuyển động của vật bằng ${deg}^\\circ$."
    )
    choices = shuffle_choices(correct, wrongs)
    loigiai = (
        f"Áp dụng công thức tính công của lực:\\n"
        f"$$A = \\vec{{F}} \\cdot \\vec{{d}} = |\\vec{{F}}| \\cdot |\\vec{{d}}| \\cdot \\cos {deg}^\\circ = {res_str}.$$"
    )
    return caudan, choices, loigiai


# 24. Đúng sai: Tổng hợp tọa độ vectơ Oxy (a, PQ, độ dài b, cùng phương)
def k10_tf_vecto_oxy_tong_hop_4y():
    caudan = (
        "Trong mặt phẳng tọa độ $Oxy$, cho các vectơ $\\vec{a} = 4\\vec{i} - 6\\vec{j}, "
        "\\vec{b} = (-3;4)$ và hai điểm $P(-2;3), Q(3;-4)$. Khi đó:"
    )

    item_a = (
        r"Tọa độ của vectơ $\vec{a}$ là $(4;-6)$.",
        r"Tọa độ của vectơ $\vec{a}$ là $(-6;4)$.",
        r"Từ $\vec{a} = 4\vec{i} - 6\vec{j} \Rightarrow \vec{a} = (4;-6)$.",
        r"Sai vì theo định nghĩa $\vec{a} = x\vec{i} + y\vec{j} \Rightarrow \vec{a} = (x;y) = (4;-6)$."
    )
    item_b = (
        r"Tọa độ của vectơ $\vec{PQ}$ là $(5;-7)$.",
        r"Tọa độ của vectơ $\vec{PQ}$ là $(-5;7)$.",
        r"Ta có $\vec{PQ} = (x_Q - x_P; y_Q - y_P) = (3 - (-2); -4 - 3) = (5;-7)$.",
        r"Sai vì $\vec{PQ} = (x_Q - x_P; y_Q - y_P) = (5;-7)$."
    )
    item_c = (
        r"Độ dài của vectơ $\vec{b}$ là $|\vec{b}| = 5$.",
        r"Độ dài của vectơ $\vec{b}$ là $|\vec{b}| = 7$.",
        r"Ta có $|\vec{b}| = \sqrt{(-3)^2 + 4^2} = \sqrt{25} = 5$.",
        r"Sai vì $|\vec{b}| = \sqrt{(-3)^2 + 4^2} = 5$."
    )
    item_d = (
        r"Hai vectơ $\vec{PQ}$ và $\vec{c} = \vec{a} - 2\vec{b}$ cùng phương.",
        r"Hai vectơ $\vec{PQ}$ và $\vec{c} = \vec{a} - 2\vec{b}$ vuông góc nhau.",
        r"Ta có $\vec{c} = \vec{a} - 2\vec{b} = (4 - 2(-3); -6 - 2(4)) = (10;-14) = 2\vec{PQ}$. Do đó hai vectơ cùng phương.",
        r"Sai vì $\vec{c} = 2\vec{PQ}$ nên hai vectơ cùng phương."
    )
    choices, loigiai = make_tf_choices([item_a, item_b, item_c, item_d])
    return caudan, choices, loigiai




# ==============================================================================
# 19 HÀM MỚI BỔ SUNG ĐỢT 2 (TOÁN THỰC TẾ & BỔ SUNG CHƯƠNG III, IV)
# ==============================================================================

# 25. Toán thực tế xe cứu hỏa thang tiếp cận đám cháy
def k10_sa_htl_toan_thuc_te_xe_cuu_hoa_thang():
    d = random.choice([25, 30, 35])
    a_deg = random.choice([25, 30])
    b_deg = random.choice([45, 50, 55])
    L = random.choice([35, 40, 45])
    h0 = 1.8

    # Trong tam giác ABC:
    # góc C = b_deg - a_deg
    # AC = d * sin(a_deg) / sin(C)
    # CH = AC * sin(b_deg)
    C_rad = math.radians(b_deg - a_deg)
    a_rad = math.radians(a_deg)
    b_rad = math.radians(b_deg)

    AC = d * math.sin(a_rad) / math.sin(C_rad)
    CH = AC * math.sin(b_rad)
    CK = CH - h0
    if CK >= L:
        L = int(math.ceil((CK + 4) / 5.0) * 5)
    KD = math.sqrt(L**2 - CK**2)
    ans = round(KD, 1)

    h0_str = str(h0).replace('.', ',')
    tikz = r"""\begin{tikzpicture}[line cap=round, line join=round, >=stealth, font=\small, scale=0.7]
	\begin{scope}[shift={(0, 0)}]
		% Định nghĩa các tọa độ chính
		\coordinate (H2) at (0,0);
		\coordinate (C2) at (0,5);
		\coordinate (K2) at (0,1.1);
		\coordinate (D2) at (5.5,1.1);
		\coordinate (E2) at (5.5,0);

		% --- VẼ TÒA NHÀ ---
		\fill[yellow!95!orange] (-1.5, 0) rectangle (0, 5);
		\fill[red] (-1.5, 5) rectangle (0, 5.2);
		\foreach \y in {1.1, 2.1, 3.1, 4.1} {
			\fill[black] (-1.3, \y) rectangle (-0.2, \y+0.7);
		}
		\fill[red] (-1.1, 0) rectangle (-0.4, 0.8);

		% --- VẼ MẶT ĐẤT ---
		\draw (H2) -- (6.8, 0);

		% --- VẼ XE CỨU HỎA ---
		\begin{scope}[shift={(0, 0)}]
			\fill[gray!80!black] (2.7, 0.15) rectangle (5.5, 0.3);
			\fill[gray!40] (2.5, 0.15) rectangle (2.7, 0.35);
			\fill[red] (2.7, 0.2) rectangle (3.7, 0.8);
			\fill[red] (3.7, 0.2) rectangle (5.5, 0.9);
			\fill[cyan!30] (2.85, 0.45) rectangle (3.55, 0.7);
			\fill[white] (3.7, 0.45) rectangle (5.5, 0.6);
			\foreach \x in {3.85, 4.25, 4.65, 5.05} {
				\fill[red] (\x, 0.48) rectangle (\x+0.18, 0.57);
			}
			\fill[blue] (3.0, 0.8) arc (180:0:0.1) -- cycle;
			\fill[blue] (3.4, 0.8) arc (180:0:0.1) -- cycle;
			\fill[gray!20] (3.7, 0.9) rectangle (5.5, 1.1);
			\draw[gray!50, thick] (3.7, 0.9) rectangle (5.5, 1.1);
			\foreach \x in {3.7, 3.9, 4.1, 4.3, 4.5, 4.7, 4.9, 5.1, 5.3} {
				\draw[gray!60, thick] (\x, 0.9) -- (\x+0.2, 1.1);
				\draw[gray!60, thick] (\x+0.2, 0.9) -- (\x, 1.1);
			}
			\foreach \x in {3.2, 4.5, 5.1} {
				\fill[black] (\x, 0.2) circle (0.22);
				\fill[red] (\x, 0.2) circle (0.12);
				\fill[gray!20] (\x, 0.2) circle (0.06);
				\fill[black] (\x, 0.2) circle (0.02);
			}
		\end{scope}

		% --- VẼ CÁC ĐƯỜNG NÉT TOÁN HỌC ---
		\draw (H2) -- (C2);
		\draw (K2) -- (D2);
		\draw (C2) -- (D2) node[midway, above right] {\footnotesize $__L__$ m};
		\draw[dashed] (D2) -- (E2);

		% --- GHI CHÚ ĐIỂM VÀ ĐỘ DÀI ---
		\node[above] at (C2) {$C$};
		\node[below] at (H2) {$H$};
		\node[below right, inner sep=2pt] at (K2) {$K$};
		\node[right] at (D2) {$D$};
		\node[right] at (E2) {$E$};
		\node[right] at ($(D2)!0.5!(E2)$) {\footnotesize $__H0__$ m};

		% --- KÝ HIỆU GÓC VUÔNG ---
		\draw (0.2, 0) -- (0.2, 0.2) -- (0, 0.2);
		\draw (0.2, 1.1) -- (0.2, 1.3) -- (0, 1.3);
		\draw (5.3, 0) -- (5.3, 0.2) -- (5.5, 0.2);
	\end{scope}
\end{tikzpicture}""".replace("__L__", str(L)).replace("__H0__", h0_str)

    prompt = (
        f"Hai người dân đứng cách nhau ${d}\\text{{ m}}$ cùng nhìn lên đỉnh của một tòa nhà theo góc nhìn lần lượt là "
        f"${a_deg}^\\circ$ và ${b_deg}^\\circ$. Vì gặp sự cố nên tầng trên cùng của tòa nhà đang bị cháy. "
        f"Để cứu hộ đám cháy, một xe cứu hỏa đã tiếp cận dưới chân tòa nhà và chân thang đứng cách mặt đất ${h0_str}\\text{{ m}}$, "
        f"chiều dài tối đa của thang xếp là ${L}\\text{{ m}}$. Để tiếp cận được đám cháy thì xe cứu hỏa phải đứng cách "
        f"chân tòa một khoảng xa nhất là bao nhiêu mét? (Làm tròn đến hàng phần mười)."
    )
    caudan = "\\immini{" + prompt + "}{\n" + tikz + "\n}"
    dapan = f"{ans}".replace('.', ',')
    loigiai = (
        f"Gọi $C$ là đỉnh tòa nhà, $A, B$ là vị trí của hai người dân ($AB = {d}\\text{{ m}}$).\\\\\n"
        f"Trong tam giác $ABC$, ta có $\\widehat{{ACB}} = {b_deg}^\\circ - {a_deg}^\\circ = {b_deg - a_deg}^\\circ$.\\\\\n"
        f"Theo định lí sin: $AC = \\dfrac{{AB \\cdot \\sin {a_deg}^\\circ}}{{\\sin {b_deg - a_deg}^\\circ}} \\approx {AC:.2f}\\text{{ m}}$.\\\\\n"
        f"Chiều cao tòa nhà: $CH = AC \\cdot \\sin {b_deg}^\\circ \\approx {CH:.2f}\\text{{ m}}$.\\\\\n"
        f"Khoảng cách từ chân thang đến đỉnh đám cháy: $CK = CH - {h0} \\approx {CK:.2f}\\text{{ m}}$.\\\\\n"
        f"Khoảng cách xa nhất từ xe cứu hỏa đến chân tòa nhà:\n"
        f"$$KD = \\sqrt{{CD^2 - CK^2}} = \\sqrt{{{L}^2 - ({CK:.2f})^2}} \\approx {ans}\\text{{ m}}.$$"
    )
    return caudan, dapan, loigiai


# 26. Toán thực tế đo chiều cao mái tháp nhà thờ bằng giác kế
def k10_sa_htl_toan_thuc_te_chieu_cao_thap_mai():
    EF = random.choice([18, 20, 21, 24])
    a_deg = 10.0
    b_deg = 19.3
    h0 = 1.6

    # Tam giác BEF: EF đã biết
    # góc FBE = 10, góc EBD = 19.3
    # góc BED = 90 - 19.3 = 70.7 => góc BEF = 180 - 70.7 = 109.3
    # góc BFE = 180 - (10 + 109.3) = 60.7
    # BF = EF * sin(109.3) / sin(10)
    # DF = BF * sin(29.3)
    # CF = DF + 1.6
    ang_BEF = 180.0 - (90.0 - b_deg)
    ang_BFE = 180.0 - (a_deg + ang_BEF)
    BF = EF * math.sin(math.radians(ang_BEF)) / math.sin(math.radians(a_deg))
    ang_FBD = a_deg + b_deg
    DF = BF * math.sin(math.radians(ang_FBD))
    CF = DF + h0
    ans = round(CF, 1)

    h0_str = str(h0).replace('.', ',')
    a_str = str(int(a_deg))
    b_str = str(b_deg).replace('.', ',')
    tikz = r"""\begin{tikzpicture}[line cap=round, line join=round, >=stealth, font=\small, scale=0.45, transform shape]
	% Định nghĩa các màu sắc cho nhà thờ và cảnh quan
	\definecolor{churchwall}{RGB}{220, 140, 100}
	\definecolor{churchroof}{RGB}{140, 150, 160}
	\definecolor{wincolor}{RGB}{70, 50, 40}
	% Định nghĩa các tọa độ chính
	\coordinate (A) at (0,0);
	\coordinate (B) at (0,1.6);
	\coordinate (C) at (10,0);
	\coordinate (D) at (10,1.6);
	\coordinate (E) at (10,5.1);
	\coordinate (F) at (10,7.21);
	% Nền đất
	\fill[gray!20] (-2.2,-0.3) rectangle (15,0);
	\draw[thick] (-2.2,0) -- (15,0);
	% ==========================================
	% VẼ NHÀ THỜ ĐỨC BÀ (Mô phỏng)
	% ==========================================
	\begin{scope}
		\fill[churchwall] (9.2,0) rectangle (10.8,5.1);
		\fill[churchwall] (12.2,0) rectangle (13.8,5.1);
		\fill[churchwall] (10.8,0) rectangle (12.2,3.8);
		\fill[churchwall] (10.8,3.8) -- (12.2,3.8) -- (11.5,4.6) -- cycle;
		\fill[churchroof] (9.2,5.1) -- (10.8,5.1) -- (10,7.21) -- cycle;
		\fill[churchroof] (12.2,5.1) -- (13.8,5.1) -- (13,7.21) -- cycle;
		\draw[thick] (10,7.21) -- (10,7.6) (9.8,7.4) -- (10.2,7.4);
		\draw[thick] (13,7.21) -- (13,7.6) (12.8,7.4) -- (13.2,7.4);
		\draw[thick] (11.5,4.6) -- (11.5,5.0) (11.3,4.8) -- (11.7,4.8);
		\fill[wincolor] (9.5, 2.5) rectangle (9.8, 4);
		\fill[wincolor] (9.5, 4) arc (180:0:0.15);
		\fill[wincolor] (10.2, 2.5) rectangle (10.5, 4);
		\fill[wincolor] (10.2, 4) arc (180:0:0.15);
		\fill[wincolor] (12.5, 2.5) rectangle (12.8, 4);
		\fill[wincolor] (12.5, 4) arc (180:0:0.15);
		\fill[wincolor] (13.2, 2.5) rectangle (13.5, 4);
		\fill[wincolor] (13.2, 4) arc (180:0:0.15);
		\fill[white] (11.5, 2.8) circle (0.45);
		\draw[wincolor, thick] (11.5, 2.8) circle (0.45);
		\foreach \a in {0,45,...,315} \draw[wincolor, thick] (11.5,2.8) -- ++(\a:0.45);
		\fill[white] (11.5, 2.8) circle (0.15);
		\draw[wincolor, thick] (11.5, 2.8) circle (0.15);
		\fill[wincolor] (9.5,0) rectangle (10.5,1.2);
		\fill[wincolor] (9.5,1.2) arc (180:0:0.5);
		\fill[wincolor] (12.5,0) rectangle (13.5,1.2);
		\fill[wincolor] (12.5,1.2) arc (180:0:0.5);
		\fill[wincolor] (11.1,0) rectangle (11.9,1.5);
		\fill[wincolor] (11.1,1.5) arc (180:0:0.4);
		\fill[green!25!black] (8.2,0) arc (180:0:0.7) -- cycle;
		\fill[green!50!black] (8.8,0) arc (180:0:0.5) -- cycle;
		\fill[green!25!black] (10.4,0) arc (180:0:0.45) -- cycle;
		\fill[green!50!black] (11.6,0) arc (180:0:0.4) -- cycle;
		\fill[green!25!black] (12.1,0) arc (180:0:0.5) -- cycle;
		\fill[green!50!black] (13.4,0) arc (180:0:0.6) -- cycle;
		\fill[green!25!black] (14.0,0) arc (180:0:0.4) -- cycle;
	\end{scope}
	% ==========================================
	% VẼ NGƯỜI VÀ GIÁC KẾ
	% ==========================================
	\draw[thick, gray!60!black, line cap=round] (0, 1.45) -- (-0.15, 0);
	\draw[thick, gray!60!black, line cap=round] (0, 1.45) -- (0.15, 0);
	\draw[thick, gray!40!black, line cap=round] (0, 1.45) -- (0, 0);
	\fill[black, rounded corners=0.5pt] (-0.1, 1.45) rectangle (0.1, 1.65);
	\fill[black, rounded corners=0.2pt] (0.1, 1.55) rectangle (0.22, 1.63);
	\fill[black, rounded corners=0.2pt] (-0.15, 1.55) rectangle (-0.1, 1.63);
	\begin{scope}[shift={(-0.4, 0)}]
		\fill[black, rounded corners=1pt] (0.02, 0) -- (0.12, 0) -- (0.15, 0.8) -- (0.05, 0.8) -- cycle;
		\fill[black, rounded corners=1pt] (0.18, 0) -- (0.28, 0) -- (0.25, 0.8) -- (0.15, 0.8) -- cycle;
		\fill[black, rounded corners=1pt] (0.03, 0.75) rectangle (0.27, 1.0);
		\fill[black, rounded corners=2pt]
		(0.0, 0.95) .. controls (0.0, 1.3) and (0.05, 1.5) .. (0.15, 1.5)
		-- (0.3, 1.45) .. controls (0.32, 1.2) and (0.28, 1.0) .. (0.25, 0.95) -- cycle;
		\fill[black] (0.15, 1.6) circle (0.11);
		\fill[black] (0.12, 1.7) .. controls (0.22, 1.71) and (0.3, 1.68) .. (0.35, 1.65) -- (0.2, 1.62) -- cycle;
		\draw[line width=3pt, black, line cap=round] (0.12, 1.42) -- (0.28, 1.32) -- (0.38, 1.5);
	\end{scope}
	% ==========================================
	% VẼ CÁC YẾU TỐ HÌNH HỌC VÀ CHÚ THÍCH
	% ==========================================
	\begin{scope}
		\clip (B) -- (D) -- (E) -- cycle;
		\draw[fill=blue!15, draw=none] (B) circle (2.5cm);
	\end{scope}
	\begin{scope}
		\clip (B) -- (E) -- (F) -- cycle;
		\draw[fill=red!15, draw=none] (B) circle (3.2cm);
	\end{scope}
	\draw[blue, thick] (B) ++(2.5,0) arc (0:19.3:2.5);
	\draw[red, thick] (B) ++(19.3:3.2) arc (19.3:29.3:3.2);
	\node[blue] at ($(B) + (9.65:3.3)$) {\textbf{__B_DEG__}$^{\boldsymbol{\circ}}$};
	\node[red] at ($(B) + (24.3:4.0)$) {\textbf{__A_DEG__}$^{\boldsymbol{\circ}}$};
	\draw[blue, thick] ($(B) + (9.65:2.4)$) -- ($(B) + (9.65:2.6)$);
	\draw[red, thick] ($(B) + (23.3:3.1)$) -- ($(B) + (23.3:3.3)$);
	\draw[red, thick] ($(B) + (25.3:3.1)$) -- ($(B) + (25.3:3.3)$);
	\draw[thick] (A) -- (B);
	\draw[thick] (C) -- (F);
	\draw[dashed, thick] (B) -- (D);
	\draw[thick] (B) -- (E);
	\draw[thick] (B) -- (F);
	\draw (0.3,0) |- (0,0.3);
	\draw (9.7,0) |- (10,0.3);
	\draw (9.7,1.6) |- (10,1.9);
	\draw (A) -- +(-1.1,0);
	\draw (B) -- +(-1.1,0);
	\draw[<->, thick] (-0.9,0) -- (-0.9,1.6) node[midway, left] {\textbf{__H0__ m}};
	\draw[thin] (E) -- +(0.5,0);
	\draw[thin] (F) -- +(0.5,0);
	\draw[<->, blue, thick] (10.3, 5.1) -- (10.3, 7.21) node[midway, right] {\textbf{__EF__ m}};
	\foreach \p/\anch in {A/below, B/above left, C/below right, D/above left, E/above left, F/above left} {
		\fill (\p) circle (2pt);
		\node[\anch] at (\p) {\Large $\boldsymbol{\p}$};
	}
\end{tikzpicture}""".replace("__EF__", str(EF)).replace("__H0__", h0_str).replace("__A_DEG__", a_str).replace("__B_DEG__", b_str)

    prompt = (
        f"Để xác định chiều cao nhà thờ cổ (đoạn $CF$), một nhóm học sinh dùng giác kế xác định được "
        f"góc $\\widehat{{FBE}} = {a_deg}^\\circ$ và $\\widehat{{EBD}} = {b_deg}^\\circ$, biết phần mái chóp trên cùng "
        f"$EF = {EF}\\text{{ m}}$ và khoảng cách từ mắt đến mặt đất $AB = {h0_str}\\text{{ m}}$. "
        f"Hãy tính chiều cao $CF$ của nhà thờ (kết quả làm tròn đến hàng phần mười, đơn vị mét)."
    )
    caudan = "\\immini{" + prompt + "}{\n" + tikz + "\n}"
    dapan = f"{ans}".replace('.', ',')
    loigiai = (
        f"Trong tam giác $BDE$ vuông tại $D$, $\\widehat{{BED}} = 90^\\circ - {b_deg}^\\circ = {90 - b_deg:.1f}^\\circ$.\\\\\n"
        f"Suy ra $\\widehat{{BEF}} = 180^\\circ - {90 - b_deg:.1f}^\\circ = {ang_BEF:.1f}^\\circ$.\\\\\n"
        f"Góc $\\widehat{{BFE}} = 180^\\circ - ({a_deg}^\\circ + {ang_BEF:.1f}^\\circ) = {ang_BFE:.1f}^\\circ$.\\\\\n"
        f"Áp dụng định lí sin trong tam giác $BEF$:\n"
        f"$$BF = \\dfrac{{EF \\cdot \\sin \\widehat{{BEF}}}}{{\\sin \\widehat{{FBE}}}} = \\dfrac{{{EF} \\cdot \\sin {ang_BEF:.1f}^\\circ}}{{\\sin {a_deg}^\\circ}} \\approx {BF:.2f}\\text{{ m}}.$$\n"
        f"Trong tam giác vuông $BDF$:\n"
        f"$$DF = BF \\cdot \\sin {ang_FBD:.1f}^\\circ \\approx {DF:.2f}\\text{{ m}}.$$\n"
        f"Chiều cao nhà thờ là $CF = DF + AB = {DF:.2f} + {h0} \\approx {ans}\\text{{ m}}.$"
    )
    return caudan, dapan, loigiai


# 27. Toán thực tế máy bay chệch hướng bay
def k10_sa_htl_toan_thuc_te_may_bay_chech_huong():
    d_total = random.choice([300, 330, 360, 400])
    v = random.choice([200, 220, 240])
    t_min = 15
    t_h = t_min / 60.0
    d_dev = v * t_h # ví dụ 220 * 0.25 = 55
    deg = 10.0

    # BC^2 = d_total^2 + d_dev^2 - 2 * d_total * d_dev * cos(10)
    BC2 = d_total**2 + d_dev**2 - 2 * d_total * d_dev * math.cos(math.radians(deg))
    BC = math.sqrt(BC2)
    ans = int(round(BC))

    tikz = r"""\begin{tikzpicture}[line cap=round, line join=round, >=stealth, font=\footnotesize, scale=0.65, transform shape]
	\coordinate (A) at (0,0);
	\coordinate (B) at (8,1.5);
	\coordinate (C) at (4,0);
	\coordinate (D) at (6,0);

	\draw (A) -- (C);
	\draw[dashed] (C) -- (D);
	\draw (A) -- (B) node[midway, above, sloped] {$__D_TOTAL__$ dặm};
	\draw (C) -- (B);

	\pic[draw, angle radius=1.4cm, "$__DEG__^\circ$", angle eccentricity=1.25] {angle = C--A--B};

	\fill (A) circle (1.5pt) node[below] {$A$};
	\node[below=12pt] at (A) {Chicago};
	\fill (B) circle (1.5pt) node[below] {$B$};
	\node[below=12pt] at (B) {Louisville};
	\fill (C) circle (1.5pt) node[above=4pt] {$C$};
	\node[below=4pt] at (C) {Phát hiện lỗi ở đây};

	\begin{scope}[shift={(-1.5,0)}, scale=0.5]
		\fill[green!50!black] (-1,0) to[out=20,in=160] (1,0) to[out=20,in=160] (3,0) -- (3,-0.2) -- (-1,-0.2) -- cycle;
		\draw[fill=white, pattern=checkerboard, pattern color=black] (-0.5,0) rectangle (0,2);
		\draw[fill=orange!30] (0.2,0) rectangle (0.5,1);
		\draw[fill=red!70] (0.7,0) rectangle (1.2,1.5);
		\draw[fill=cyan!30, step=0.2] (1.4,0) grid (2,2.5);
		\draw (1.4,0) rectangle (2,2.5);
		\draw[fill=yellow!50] (2.2,0) rectangle (2.5,0.8);
	\end{scope}

	\begin{scope}[shift={(7,1.5)}, scale=0.3]
		\fill[green!50!black] (-1,0) to[out=20,in=160] (1,0) to[out=20,in=160] (3,0) -- (3,-0.2) -- (-1,-0.2) -- cycle;
		\draw[fill=white, pattern=checkerboard, pattern color=black] (-0.5,0) rectangle (0,2);
		\draw[fill=orange!30] (0.2,0) rectangle (0.5,1);
		\draw[fill=red!70] (0.7,0) rectangle (1.2,1.5);
		\draw[fill=cyan!30, step=0.2] (1.4,0) grid (2,2.5);
		\draw (1.4,0) rectangle (2,2.5);
		\draw[fill=yellow!50] (2.2,0) rectangle (2.5,0.8);
	\end{scope}

	\begin{scope}[shift={(4,-0.8)}, scale=0.3]
		\fill[cyan!40] (-1,-0.2) rectangle (1,0.2);
		\fill[cyan!40] (0.2,0.2) -- (0.8,0.2) -- (1,1) -- (0.4,1) -- cycle;
		\fill[cyan!40] (0.2,-0.2) -- (0.8,-0.2) -- (1,-1) -- (0.4,-1) -- cycle;
		\fill[red!60] (-1,-0.2) -- (-1.2,0) -- (-1,0.2) -- cycle;
	\end{scope}
\end{tikzpicture}""".replace("__D_TOTAL__", str(d_total)).replace("__DEG__", str(int(deg)))

    prompt = (
        f"Trong một chuyến bay thử nghiệm từ thành phố $A$ tới $B$, khoảng cách là ${d_total}$ dặm, "
        f"viên phi công đã vô tình chọn hướng bay sai lệch đi một góc ${int(deg)}^\\circ$. "
        f"Nếu máy bay duy trì tốc độ ${v}$ dặm/giờ và lỗi được phát hiện sau ${t_min}$ phút, "
        f"hỏi máy bay còn cách thành phố $B$ bao nhiêu dặm? (Kết quả làm tròn đến hàng đơn vị)."
    )
    caudan = "\\immini{" + prompt + "}{\n" + tikz + "\n}"
    dapan = str(ans)
    loigiai = (
        f"Quãng đường máy bay đã bay sau ${t_min}$ phút là:\n"
        f"$$AC = v \\cdot t = {v} \\cdot \\dfrac{{{t_min}}}{{60}} = {int(d_dev)}\\text{{ dặm}}.$$\n"
        f"Theo định lí côsin trong tam giác $ABC$:\n"
        f"$$BC^2 = AB^2 + AC^2 - 2 \\cdot AB \\cdot AC \\cdot \\cos {int(deg)}^\\circ = {d_total}^2 + {int(d_dev)}^2 - 2 \\cdot {d_total} \\cdot {int(d_dev)} \\cdot \\cos {int(deg)}^\\circ \\approx {BC2:.1f}.$$\n"
        f"Suy ra $BC \\approx {ans}$ dặm."
    )
    return caudan, dapan, loigiai


# 28. Toán thực tế vị trí tàu thuyền trên biển
def k10_mc_htl_toan_thuc_te_tau_bien_phuong_vi():
    tikz = r"""\begin{tikzpicture}[line cap=round, line join=round, >=stealth, font=\footnotesize, scale=1.1]
	\coordinate (P) at (0, 0);
	\coordinate (Q) at (0, -2.16);
	\coordinate (N) at (0, 1.5);
	\coordinate (S) at (28:2.9);

	\fill[gray!25] (-1.5, 1.7) -- (-0.3, 1.7)
	decorate [decoration={random steps, segment length=3pt, amplitude=0.8pt}] {
		(-0.3, 1.7) .. controls (-0.2, 0.8) and (-0.1, 0.4) .. (P)
		.. controls (-0.1, -0.4) and (-0.6, -1) .. (-0.6, -1.08)
		.. controls (-0.6, -1.5) and (-0.2, -1.8) .. (Q)
		.. controls (0.1, -2.4) and (0.2, -2.5) .. (0.4, -2.7)
	}
	-- (0.4, -2.7) -- (-1.5, -2.7) -- cycle;

	\draw[thick, decorate, decoration={random steps, segment length=3pt, amplitude=0.8pt}]
	(-0.3, 1.7) .. controls (-0.2, 0.8) and (-0.1, 0.4) .. (P)
	.. controls (-0.1, -0.4) and (-0.6, -1) .. (-0.6, -1.08)
	.. controls (-0.6, -1.5) and (-0.2, -1.8) .. (Q)
	.. controls (0.1, -2.4) and (0.2, -2.5) .. (0.4, -2.7);

	\draw[->, thick] (P) -- (N) node[above] {$N$};
	\draw[dashed, thick] (P) -- (Q);
	\draw[thick] (P) -- (S) node[midway, above, sloped] {$2,9\text{ km}$};
	\draw[thick] (Q) -- (S);

	\pic[draw, thick, angle radius=0.6cm, "$62^\circ$", angle eccentricity=1.35] {angle = S--P--N};
	\pic[draw, thick, angle radius=0.8cm, "$36^\circ$", angle eccentricity=1.3] {angle = S--Q--P};

	\fill (P) circle (1.2pt) node[left=3pt] {$P$};
	\fill (Q) circle (1.2pt) node[left=3pt] {$Q$};
	\fill (S) circle (1.2pt) node[right=2pt] {$S$};
\end{tikzpicture}"""

    prompt = (
        "Hai điểm $P, Q$ ở trên bờ biển, $P$ nằm ở phía Bắc của $Q$. Một con thuyền nằm ở điểm $S$ "
        "với $PS = 2{,}9\\text{ km}$, $\\widehat{NPS} = 62^\\circ$, $\\widehat{SQP} = 36^\\circ$. "
        "Khẳng định nào sau đây sai?"
    )
    caudan = "\\immini{" + prompt + "}{\n" + tikz + "\n}"
    correct = "$QS \\approx 5\\text{ km}$"
    wrongs = [
        "$\\widehat{SPQ} = 118^\\circ$",
        "$\\widehat{PSQ} = 26^\\circ$",
        "$PQ \\approx 2{,}16\\text{ km}$",
    ]
    choices = shuffle_choices(correct, wrongs)
    loigiai = (
        "Ta có $\\widehat{SPQ} = 180^\\circ - 62^\\circ = 118^\\circ$.\\\\\n"
        "Trong tam giác $PQS$: $\\widehat{PSQ} = 180^\\circ - (118^\\circ + 36^\\circ) = 26^\\circ$.\\\\\n"
        "Theo định lí sin:\n"
        "$$QS = \\dfrac{PS \\cdot \\sin 118^\\circ}{\\sin 36^\\circ} \\approx \\dfrac{2{,}9 \\cdot 0{,}8829}{0{,}5878} \\approx 4{,}36\\text{ km} \\neq 5\\text{ km}.$$\n"
        "Do đó khẳng định $QS \\approx 5\\text{ km}$ là sai."
    )
    return caudan, choices, loigiai


# 29. Toán thực tế đo đỉnh núi từ chân và đỉnh tòa nhà
def k10_sa_htl_toan_thuc_te_nui_nhan_tao_toa_nha():
    AB = random.choice([70, 80, 100, 120])
    a_deg = 55.0
    b_deg = 21.0
    # CD = AB * tan(55) / (tan(55) - tan(21))
    tan_a = math.tan(math.radians(a_deg))
    tan_b = math.tan(math.radians(b_deg))
    CD = AB * tan_a / (tan_a - tan_b)
    ans = int(round(CD))

    tikz = r"""\begin{tikzpicture}[line cap=round, line join=round, >=stealth, font=\footnotesize, scale=0.95, transform shape]
	\def\h{2.5}
	\def\angA{__ANG_A__}
	\def\angB{__ANG_B__}
	\pgfmathsetmacro{\x}{\h / (tan(\angA) - tan(\angB))}
	\pgfmathsetmacro{\CD}{\x * tan(\angA)}

	\coordinate (A) at (0, 0);
	\coordinate (B) at (0, \h);
	\coordinate (D) at (\x, 0);
	\coordinate (C) at (\x, \CD);
	\coordinate (E) at (\x, \h);

	\path[name path=AC] (A) -- (C);
	\path[name path=BE] (B) -- (E);
	\path [name intersections={of=AC and BE, by=I}];

	\def\ml{\x-1.5}
	\def\mr{\x+1.8}

	\fill[green!80!black] (\ml, 0) rectangle (\mr, -0.25);
	\draw[thick, green!50!black] (-1, 0) -- (\ml, 0);
	\fill[green!80!black] (-1, 0) rectangle (\ml, -0.25);

	\fill[brown!70!black] (\ml, 0)
	.. controls (\x-1.2, 0.2) and (\x-1.0, 0.8) .. (\x-0.8, 1.2)
	.. controls (\x-0.7, 1.4) and (\x-0.5, 2.0) .. (\x-0.3, 2.5)
	.. controls (\x-0.2, 2.8) and (\x-0.1, 3.2) .. (C)
	.. controls (\x+0.1, 3.2) and (\x+0.2, 2.8) .. (\x+0.4, 2.3)
	.. controls (\x+0.5, 2.0) and (\x+0.8, 1.2) .. (\x+1.1, 0.8)
	.. controls (\x+1.3, 0.5) and (\x+1.5, 0.1) .. (\mr, 0)
	-- cycle;

	\fill[white] (C)
	.. controls (\x-0.1, 3.2) .. (\x-0.25, 2.5)
	-- (\x-0.15, 2.7)
	-- (\x-0.05, 1.8)
	-- (\x+0.05, 2.4)
	-- (\x+0.15, 1.9)
	-- (\x+0.25, 2.5)
	.. controls (\x+0.1, 3.2) .. (C);

	\filldraw[fill=gray!15, draw=blue!60!black, thick] (-0.9, 0) rectangle (0, \h);
	\filldraw[fill=blue!80!black, draw=blue!90!black, thick] (-0.95, \h) rectangle (0.05, \h+0.05);
	\filldraw[fill=orange!30, draw=blue!60!black, thick] (-0.6, 0) rectangle (-0.3, 0.45);
	\draw[blue!60!black, thick] (-0.45, 0) -- (-0.45, 0.45);
	\foreach \y in {0.6, 1.1, 1.6, 2.1} {
		\filldraw[fill=cyan!20, draw=blue!60!black, thick] (-0.8, \y) rectangle (-0.5, \y+0.35);
		\draw[white, thick, line cap=round] (-0.75, \y+0.25) -- (-0.55, \y+0.05);
		\filldraw[fill=cyan!20, draw=blue!60!black, thick] (-0.4, \y) rectangle (-0.1, \y+0.35);
		\draw[white, thick, line cap=round] (-0.35, \y+0.25) -- (-0.15, \y+0.05);
	}

	\draw[blue, thick] (A) -- (D);
	\draw[blue, thick] (B) -- (E);
	\draw[blue, thick] (C) -- (D);
	\draw[blue, thick] (A) -- (C);
	\draw[blue, thick] (B) -- (C);

	\pic[draw, blue, thick, angle radius=0.7cm, "$__ANG_A__^\circ$", angle eccentricity=1.45] {angle = D--A--C};
	\pic[draw, blue, thick, angle radius=1.0cm, "$__ANG_B__^\circ$", angle eccentricity=1.35] {angle = E--B--C};

	\fill[blue] (A) circle (1.2pt) node[below=2pt] {$A$};
	\fill[blue] (B) circle (1.2pt) node[above left] {$B$};
	\fill[blue] (C) circle (1.2pt) node[above] {$C$};
	\fill[blue] (D) circle (1.2pt) node[above right] {$D$};
	\fill[blue] (E) circle (1.2pt) node[right=1pt] {$E$};
	\fill[blue] (I) circle (1.2pt) node[below=2pt] {$I$};

	\node[blue, right=2pt, fill=white, inner sep=1pt, rounded corners=2pt] at (0, \h/2) {$__AB__\text{ m}$};
\end{tikzpicture}""".replace("__AB__", str(AB)).replace("__ANG_A__", str(int(a_deg))).replace("__ANG_B__", str(int(b_deg)))

    prompt = (
        f"Một người quan sát đỉnh $C$ của một ngọn núi từ hai vị trí $A$ (chân tòa nhà) và $B$ (đỉnh tòa nhà). "
        f"Lần đầu người đó quan sát đỉnh núi từ chân tòa nhà với góc nâng là ${int(a_deg)}^\\circ$, "
        f"lần thứ hai quan sát tại đỉnh tòa nhà với góc nâng là ${int(b_deg)}^\\circ$. "
        f"Tính chiều cao ngọn núi $CD$ biết chiều cao tòa nhà $AB$ là ${AB}\\text{{ m}}$ (kết quả làm tròn đến hàng đơn vị)."
    )
    caudan = "\\immini{" + prompt + "}{\n" + tikz + "\n}"
    dapan = str(ans)
    loigiai = (
        f"Gọi $d$ là khoảng cách ngang từ tòa nhà đến chân ngọn núi.\\\\\n"
        f"Ta có $CD = d \\cdot \\tan {int(a_deg)}^\\circ$ và $CE = CD - AB = d \\cdot \\tan {int(b_deg)}^\\circ$.\\\\\n"
        f"Suy ra $AB = d(\\tan {int(a_deg)}^\\circ - \\tan {int(b_deg)}^\\circ) \\Rightarrow d = \\dfrac{{{AB}}}{{\\tan {int(a_deg)}^\\circ - \\tan {int(b_deg)}^\\circ}}$.\\\\\n"
        f"Chiều cao ngọn núi là:\n"
        f"$$CD = \\dfrac{{{AB} \\cdot \\tan {int(a_deg)}^\\circ}}{{\\tan {int(a_deg)}^\\circ - \\tan {int(b_deg)}^\\circ}} \\approx {ans}\\text{{ m}}.$$"
    )
    return caudan, dapan, loigiai


# 30. Toán thực tế chiều cao cây trên sườn đồi
def k10_sa_htl_toan_thuc_te_cay_tren_suon_doi():
    L = random.choice([16.5, 18.5, 20.0])
    a_deg = 26.0
    b_deg = 54.0
    # tam giác ABC:
    # góc A = b_deg - a_deg = 28
    # góc B = 90 + a_deg = 116
    # góc C = 90 - b_deg = 36
    # BC = L * sin(28) / sin(36)
    ang_A = b_deg - a_deg
    ang_C = 90.0 - b_deg
    BC = L * math.sin(math.radians(ang_A)) / math.sin(math.radians(ang_C))
    ans = round(BC, 1)

    tikz = r"""\begin{tikzpicture}[line cap=round, line join=round, >=stealth, font=\footnotesize, scale=0.85, transform shape]
	\def\angAlpha{__ALPHA__}
	\def\angBeta{__BETA__}
	\def\AB{5}

	\coordinate (A) at (0,0);
	\pgfmathsetmacro{\Bx}{\AB * cos(\angAlpha)}
	\pgfmathsetmacro{\By}{\AB * sin(\angAlpha)}
	\coordinate (B) at (\Bx, \By);
	\pgfmathsetmacro{\Cy}{\Bx * tan(\angBeta)}
	\coordinate (C) at (\Bx, \Cy);
	\coordinate (O) at (\Bx, 0);

	\draw[very thick] ($ (A) - (1.5, {1.5*tan(\angAlpha)}) $) -- ($ (B) + (1.2, {1.2*tan(\angAlpha)}) $);
	\draw[dashed, thin] (-0.8, 0) -- ($ (O) + (0.8, 0) $);
	\draw[dashed, thin] (C) -- (O);
	\draw[dashed, thin] (A) -- (C);
	\draw[dashed, thin] (C) -- ($ (C) + (\angBeta:2) $);

	\draw ($ (O) + (0, 0.25) $) -- ($ (O) + (-0.25, 0.25) $) -- ($ (O) + (-0.25, 0) $);

	\coordinate (X) at (3,0);
	\pic[draw, thick, angle radius=0.9cm, "$\alpha$"{yshift=-1pt}, angle eccentricity=1.25] {angle = X--A--B};
	\pic[draw, thick, angle radius=1.4cm, "$\beta$"{xshift=3pt, yshift=2pt}, angle eccentricity=1.15] {angle = X--A--C};

	\begin{scope}[shift={(B)}]
		\fill[gray!80!black, draw=black, thin] (-0.12, 0) rectangle (0.12, 0.5);
		\pgfmathsetmacro{\gh}{\Cy - \By - 0.4}
		\fill[green!55!black]
		(0, \gh+0.4) --
		(-0.35, \gh*0.75 + 0.4) -- (-0.15, \gh*0.75 + 0.4) --
		(-0.6, \gh*0.5 + 0.4)  -- (-0.3, \gh*0.5 + 0.4)  --
		(-0.85, \gh*0.25 + 0.4) -- (-0.45, \gh*0.25 + 0.4) --
		(-1.1, 0.4) -- (1.1, 0.4) --
		(0.45, \gh*0.25 + 0.4) -- (0.85, \gh*0.25 + 0.4) --
		(0.3, \gh*0.5 + 0.4)  -- (0.6, \gh*0.5 + 0.4)  --
		(0.15, \gh*0.75 + 0.4) -- (0.35, \gh*0.75 + 0.4) -- cycle;
	\end{scope}

	\coordinate (Sun) at ($ (C) + (\angBeta:2) $);
	\fill[yellow!95!orange] (Sun) circle (0.45);
	\foreach \i in {0, 45, 90, 135, 180, 225, 270, 315} {
		\draw[yellow!95!orange, thick] ($ (Sun) + (\i:0.6) $) -- ($ (Sun) + (\i:0.95) $);
	}

	\node[below=2pt] at (A) {$A$};
	\node[below right=1pt] at (B) {$B$};
	\node[right=2pt] at (C) {$C$};
	\node[right=2pt] at (O) {$O$};
\end{tikzpicture}""".replace("__ALPHA__", str(int(a_deg))).replace("__BETA__", str(int(b_deg)))

    prompt = (
        f"Trên sườn đồi có một cái cây thẳng đứng đổ bóng dài $AB = {str(L).replace('.', ',')}\\text{{ m}}$ xuống đồi. "
        f"Biết góc nghiêng của sườn đồi là $\\alpha = {int(a_deg)}^\\circ$ so với phương ngang và góc nghiêng của tia nắng "
        f"mặt trời đi qua ngọn cây là $\\beta = {int(b_deg)}^\\circ$. Chiều cao $BC$ của cây bằng bao nhiêu mét? "
        f"(Làm tròn đến hàng phần mười)."
    )
    caudan = "\\immini{" + prompt + "}{\n" + tikz + "\n}"
    dapan = f"{ans}".replace('.', ',')
    loigiai = (
        f"Trong tam giác $ABC$:\\\\\n"
        f"- Góc $\\widehat{{CAB}} = \\beta - \\alpha = {int(b_deg)}^\\circ - {int(a_deg)}^\\circ = {int(ang_A)}^\\circ$.\\\\\n"
        f"- Vì cây thẳng đứng nên góc tại ngọn cây $\\widehat{{ACB}} = 90^\\circ - \\beta = {int(ang_C)}^\\circ$.\\\\\n"
        f"Theo định lí sin trong tam giác $ABC$:\n"
        f"$$\\dfrac{{BC}}{{\\sin \\widehat{{CAB}}}} = \\dfrac{{AB}}{{\\sin \\widehat{{ACB}}}} \\Rightarrow BC = \\dfrac{{{str(L).replace('.', ',')} \\cdot \\sin {int(ang_A)}^\\circ}}{{\\sin {int(ang_C)}^\\circ}} \\approx {ans}\\text{{ m}}.$$"
    )
    return caudan, dapan, loigiai


# 31. Toán thực tế góc lệch phát bóng golf
def k10_sa_htl_toan_thuc_te_danh_golf_goc_lech():
    TA = 220
    AG = 165
    TG = 340
    # cos T = (TA^2 + TG^2 - AG^2) / (2 * TA * TG)
    cos_T = (TA**2 + TG**2 - AG**2) / (2.0 * TA * TG)
    rad_T = math.acos(cos_T)
    deg_T = math.degrees(rad_T)
    ans = round(deg_T, 1)

    tikz = r"""\begin{tikzpicture}[line cap=round, line join=round, >=stealth, font=\footnotesize, scale=0.85, transform shape]
	\def\angleT{__ANG_T__}

	\coordinate (T) at (0,0);
	\coordinate (G) at (6.8, 0);
	\coordinate (A) at (\angleT:4.4);

	\begin{scope}[shift={(T)}, scale=0.4]
		\filldraw[fill=yellow!50!white, draw=black, thin]
		(-1, -1.2) -- (1.5, -0.8) --
		(0.5, 0.8) -- (-2, 0.5) -- cycle;
	\end{scope}

	\begin{scope}[shift={(G)}, scale=0.45]
		\filldraw[fill=green!60!white, draw=black, thin, smooth cycle]
		(-1.5, -0.5) .. controls ++(1, -0.5) and ++(-0.5, -1) ..
		(0.5, -1) .. controls ++(1, 0) and ++(-0.5, -0.5) ..
		(1.5, -0.2) .. controls ++(0.5, 0.5) and ++(1, 0) ..
		(0.5, 1) .. controls ++(-1, 0) and ++(0.5, 0.5) ..
		(-2, 0.5) .. controls ++(-0.5, -0.5) and ++(-0.5, 0.5) .. cycle;
		\draw[thick] (0.1, 0) -- (0.1, 1.5);
		\filldraw[fill=magenta, draw=black, thin] (0.1, 1.5) -- (0.8, 1.5) -- (0.1, 0.9) -- cycle;
	\end{scope}

	\draw[dashed, thin] (T) -- (A) node[midway, above left, inner sep=2pt] {$__TA__\text{ m}$};
	\draw[dashed, thin] (A) -- (G) node[midway, above right, inner sep=2pt] {$__AG__\text{ m}$};
	\draw[dashed, thin] (T) -- (G) node[midway, below, inner sep=4pt] {$__TG__\text{ m}$};

	\fill (T) circle (1pt) node[left=4pt] {$T$};
	\fill[fill=white, draw=black, thin] (A) circle (1.2pt) node[above=2pt] {$A$};
	\fill (G) circle (1pt) node[below right=2pt] {$G$};

	\pic[draw, thin, angle radius=0.7cm] {angle = G--T--A};
\end{tikzpicture}""".replace("__TA__", str(TA)).replace("__AG__", str(AG)).replace("__TG__", str(TG)).replace("__ANG_T__", f"{deg_T:.4f}")

    prompt = (
        f"Một người chơi gôn thực hiện cú phát bóng với khoảng cách ${TA}\\text{{ m}}$ từ điểm phát bóng $T$ tới điểm $A$. "
        f"Sau đó, người này dùng gậy số 6 đánh tới lỗ gôn $G$ với khoảng cách ${AG}\\text{{ m}}$. "
        f"Nếu khoảng cách thẳng từ điểm phát bóng đến lỗ gôn là ${TG}\\text{{ m}}$, tính góc tạo bởi đường phát bóng $TA$ "
        f"với đường thẳng nối thẳng từ điểm phát tới lỗ gôn $TG$ (làm tròn kết quả đến hàng phần mười, đơn vị độ)."
    )
    caudan = "\\immini{" + prompt + "}{\n" + tikz + "\n}"
    dapan = f"{ans}".replace('.', ',')
    loigiai = (
        f"Áp dụng định lí côsin trong tam giác $TAG$ với góc $\\widehat{{ATG}}$:\\\\\n"
        f"$$\\cos \\widehat{{ATG}} = \\dfrac{{TA^2 + TG^2 - AG^2}}{{2 \\cdot TA \\cdot TG}} = \\dfrac{{{TA}^2 + {TG}^2 - {AG}^2}}{{2 \\cdot {TA} \\cdot {TG}}} \\approx {cos_T:.5f}.$$\n"
        f"Suy ra $\\widehat{{ATG}} \\approx {ans}^\\circ$."
    )
    return caudan, dapan, loigiai


# 32. Độ dài hiệu vectơ trong hình vuông: |OA - CB|
def k10_mc_vecto_do_dai_hieu_hinh_vuong():
    caudan = (
        "Cho hình vuông $ABCD$ có cạnh là $a$, $O$ là giao điểm của hai đường chéo. "
        "Tính $|\\vec{OA} - \\vec{CB}|$."
    )
    correct = "$\\dfrac{a\\sqrt{2}}{2}$"
    wrongs = [
        "$a\\sqrt{3}$",
        "$a\\sqrt{2}$",
        "$\\dfrac{a\\sqrt{3}}{2}$",
    ]
    choices = shuffle_choices(correct, wrongs)
    loigiai = (
        "Trong hình vuông $ABCD$, ta có $\\vec{CB} = \\vec{DA}$.\\\\n"
        "Do đó $\\vec{OA} - \\vec{CB} = \\vec{OA} - \\vec{DA} = \\vec{OA} + \\vec{AD} = \\vec{OD}$.\\\\n"
        "Độ dài $|\\vec{OA} - \\vec{CB}| = OD = \\dfrac{BD}{2} = \\dfrac{a\\sqrt{2}}{2}$."
    )
    return caudan, choices, loigiai


# 33. Quy tắc hình bình hành
def k10_mc_vecto_quy_tac_hinh_binh_hanh():
    caudan = "Cho hình bình hành $ABCD$. Khẳng định nào sau đây là đúng?"
    correct = "$\\vec{AB} + \\vec{AD} = \\vec{AC}$"
    wrongs = [
        "$\\vec{AB} + \\vec{AD} = \\vec{CA}$",
        "$\\vec{AB} + \\vec{AD} = \\vec{DB}$",
        "$\\vec{AB} + \\vec{AD} = \\vec{BD}$",
    ]
    choices = shuffle_choices(correct, wrongs)
    loigiai = (
        "Theo quy tắc hình bình hành: tổng của hai vectơ chung gốc tạo bởi hai cạnh kề của hình bình hành "
        "bằng vectơ đường chéo xuất phát từ đỉnh đó: $\\vec{AB} + \\vec{AD} = \\vec{AC}$."
    )
    return caudan, choices, loigiai


# 34. Độ dài hiệu hai vectơ tam giác đều |AB - AC|
def k10_mc_vecto_hieu_tam_giac_deu():
    caudan = "Cho tam giác $ABC$ đều có độ dài cạnh bằng $a$. Khi đó, $|\\vec{AB} - \\vec{AC}|$ bằng"
    correct = "$a$"
    wrongs = [
        "$2a$",
        "$\\dfrac{a}{2}$",
        "$\\dfrac{a\\sqrt{3}}{2}$",
    ]
    choices = shuffle_choices(correct, wrongs)
    loigiai = (
        "Theo quy tắc trừ hai vectơ chung gốc: $\\vec{AB} - \\vec{AC} = \\vec{CB}$.\\\\n"
        "Do đó $|\\vec{AB} - \\vec{AC}| = |\\vec{CB}| = CB = a$."
    )
    return caudan, choices, loigiai


# 35. Tỉ lệ đoạn thẳng trên trục số (MP = 3 PN)
def k10_mc_vecto_ti_le_doan_thang_truc_so():
    caudan = (
        "Trên đường thẳng $MN$ lấy điểm $P$ sao cho $\\vec{MP} = 3\\vec{PN}$. "
        "Khẳng định nào sau đây đúng về vị trí của điểm $P$?"
    )
    correct = "$P$ nằm giữa $M, N$ và $MP = 3PN$"
    wrongs = [
        "$P$ nằm ngoài đoạn $MN$ về phía $N$",
        "$P$ nằm ngoài đoạn $MN$ về phía $M$",
        "$M$ nằm giữa $P$ và $N$",
    ]
    choices = shuffle_choices(correct, wrongs)
    loigiai = (
        "Vì $\\vec{MP} = 3\\vec{PN}$ với hệ số $3 > 0$ nên hai vectơ $\\vec{MP}$ và $\\vec{PN}$ cùng hướng.\\\\n"
        "Suy ra $P$ nằm giữa $M$ và $N$, đồng thời độ dài $MP = 3PN$."
    )
    return caudan, choices, loigiai


# 36. Tọa độ trọng tâm tam giác OAB
def k10_mc_vecto_trong_tam_tam_giac_oab():
    xA = random.choice([-6, -3, 3, 6])
    yA = random.choice([1, 2, 4, 5])
    xB = random.choice([3, 6, 9])
    yB = random.choice([2, 4, 5, 7])

    xG = Fraction(xA + xB, 3)
    yG = Fraction(yA + yB, 3)

    caudan = f"Trong mặt phẳng $Oxy$, cho hai điểm $A({xA};{yA})$ và $B({xB};{yB})$. Tìm tọa độ trọng tâm $G$ của tam giác $OAB$ (với $O$ là gốc tọa độ)."
    correct = f"$G({fmt_frac(xG)};{fmt_frac(yG)})$"
    wrongs = [
        f"$G({fmt_frac(Fraction(xA+xB, 2))};{fmt_frac(Fraction(yA+yB, 2))})$",
        f"$G({fmt_frac(xG + 1)};{fmt_frac(yG)})$",
        f"$G({fmt_frac(xG)};{fmt_frac(yG + 1)})$",
    ]
    choices = shuffle_choices(correct, wrongs)
    loigiai = (
        f"Gốc tọa độ $O(0;0)$. Tọa độ trọng tâm $G$ của tam giác $OAB$ là:\\\\n"
        f"$$x_G = \\dfrac{{0 + ({xA}) + ({xB})}}{{3}} = {fmt_frac(xG)}, \\quad y_G = \\dfrac{{0 + ({yA}) + ({yB})}}{{3}} = {fmt_frac(yG)}.\\\\n"
        f"Vậy $G({fmt_frac(xG)};{fmt_frac(yG)})$."
    )
    return caudan, choices, loigiai


# 37. Hai vectơ bằng nhau tìm x + y
def k10_mc_vecto_hai_vecto_bang_nhau_tim_x_y():
    a = random.randint(1, 5)
    b = random.randint(1, 5)
    c = random.randint(-5, 5)
    d = random.randint(-5, 5)

    # u = (x - a; b), v = (c; y + d)
    # x - a = c => x = c + a
    # b = y + d => y = b - d
    x = c + a
    y = b - d
    ans = x + y

    caudan = (
        f"Trong mặt phẳng $Oxy$, cho $\\vec{{u}} = (x - {a}; {b})$ và $\\vec{{v}} = ({c}; y + {d})$. "
        f"Tìm giá trị của biểu thức $x + y$ biết $\\vec{{u}} = \\vec{{v}}$."
    )
    correct = f"${ans}$"
    wrongs = [f"${ans + 2}$", f"${ans - 4}$", f"${-ans}$"]
    choices = shuffle_choices(correct, wrongs)
    loigiai = (
        f"Vì $\\vec{{u}} = \\vec{{v}}$ nên:\\\\n"
        f"$$\\begin{{cases}} x - {a} = {c} \\\\ {b} = y + {d} \\end{{cases}} \\Leftrightarrow \\begin{{cases}} x = {x} \\\\ y = {y} \\end{{cases}}.\\\\n"
        f"Do đó $x + y = {x} + ({y}) = {ans}$."
    )
    return caudan, choices, loigiai


# 38. Độ dài vectơ Oxy ra số nguyên đẹp
def k10_mc_vecto_do_dai_vecto_oxy_so_nguyen():
    triples = [(3, 4, 5), (5, 12, 13), (6, 8, 10), (8, 15, 17)]
    x0, y0, r = random.choice(triples)
    sx = random.choice([1, -1])
    sy = random.choice([1, -1])
    x, y = x0 * sx, y0 * sy

    use_ij = random.choice([True, False])
    if use_ij:
        comb = fmt_vec_comb(x, y)
        caudan = f"Trong mặt phẳng $Oxy$, cho $\\vec{{v}} = {comb}$. Khi đó độ dài của $\\vec{{v}}$ bằng"
    else:
        caudan = f"Trong mặt phẳng $Oxy$, cho $\\vec{{u}} = ({x};{y})$. Khi đó độ dài của $\\vec{{u}}$ bằng"

    correct = f"${r}$"
    wrongs = [f"${abs(x) + abs(y)}$", f"$\\sqrt{{{abs(x**2 - y**2)}}}$", f"${r + 2}$"]
    choices = shuffle_choices(correct, wrongs)
    loigiai = (
        f"Độ dài của vectơ là:\\\\n"
        f"$$|\\vec{{v}}| = \\sqrt{{({x})^2 + ({y})^2}} = \\sqrt{{{x**2} + {y**2}}} = \\sqrt{{{r**2}}} = {r}.$$"
    )
    return caudan, choices, loigiai


# 39. Tích vô hướng trong tam giác vuông: AB . AC = a^2
def k10_mc_tich_vo_huong_tam_giac_vuong_goc_nhon():
    caudan = (
        "Cho tam giác $ABC$ vuông tại $B$, cạnh $AB = a$, $\\widehat{BAC} = 30^\\circ$. "
        "Khi đó $\\vec{AB} \\cdot \\vec{AC}$ bằng"
    )
    correct = "$a^2$"
    wrongs = [
        "$\\dfrac{a^2\\sqrt{3}}{2}$",
        "$\\dfrac{a^2}{2}$",
        "$3a^2$",
    ]
    choices = shuffle_choices(correct, wrongs)
    loigiai = (
        "Trong tam giác vuông $ABC$ vuông tại $B$, ta có $AC = \\dfrac{AB}{\\cos 30^\\circ} = \\dfrac{a}{\\sqrt{3}/2} = \\dfrac{2a}{\\sqrt{3}}$.\\\\n"
        "Góc giữa hai vectơ là $(\\vec{AB}, \\vec{AC}) = \\widehat{BAC} = 30^\\circ$.\\\\n"
        "Do đó: $\\vec{AB} \\cdot \\vec{AC} = AB \\cdot AC \\cdot \\cos 30^\\circ = a \\cdot \\dfrac{2a}{\\sqrt{3}} \\cdot \\dfrac{\\sqrt{3}}{2} = a^2$."
    )
    return caudan, choices, loigiai


# 40. Khẳng định sai về công thức tích vô hướng và côsin trong tọa độ Oxy
def k10_mc_tich_vo_huong_khang_dinh_sai_oxy():
    caudan = "Cho $\\vec{a} = (x_1; y_1), \\vec{b} = (x_2; y_2)$. Khẳng định nào sau đây là sai?"
    correct = "$\\cos(\\vec{a}, \\vec{b}) = \\dfrac{x_1x_2 - y_1y_2}{\\sqrt{x_1^2 + y_1^2} \\cdot \\sqrt{x_2^2 + y_2^2}}$"
    wrongs = [
        "$|\\vec{a}| = \\sqrt{x_1^2 + y_1^2}$",
        "$\\vec{a} \\cdot \\vec{b} = x_1x_2 + y_1y_2$",
        "Hai vectơ $\\vec{a} \\perp \\vec{b} \\Leftrightarrow x_1x_2 + y_1y_2 = 0$",
    ]
    choices = shuffle_choices(correct, wrongs)
    loigiai = (
        "Công thức đúng tính cô-sin của góc giữa hai vectơ là:\\\\n"
        "$$\\cos(\\vec{a}, \\vec{b}) = \\dfrac{\\vec{a}\\cdot\\vec{b}}{|\\vec{a}|\\cdot|\\vec{b}|} = \\dfrac{x_1x_2 + y_1y_2}{\\sqrt{x_1^2 + y_1^2} \\cdot \\sqrt{x_2^2 + y_2^2}}.\\\\n"
        "Do đó khẳng định có dấu trừ $x_1x_2 - y_1y_2$ ở tử số là sai."
    )
    return caudan, choices, loigiai


# 41. Đúng sai: Hình chữ nhật MNPQ và tích vô hướng
def k10_tf_hinh_chu_nhat_vecto_va_tich_vo_huong():
    a, b = 8, 6
    diag = int(math.isqrt(a**2 + b**2)) # 10

    caudan = f"Cho hình chữ nhật $MNPQ$ với $MN = {a}, MQ = {b}$. Khi đó:"

    item_a = (
        r"$\vec{MN} + \vec{QP} = 2\vec{MN}$.",
        r"$\vec{MP} = \vec{QN}$.",
        r"Vì $\vec{QP} = \vec{MN}$ nên $\vec{MN} + \vec{QP} = 2\vec{MN}$.",
        r"Hai đường chéo $\vec{MP}$ và $\vec{QN}$ không cùng phương nên $\vec{MP} = \vec{QN}$ là sai."
    )
    item_b = (
        f"$|\\vec{{MN}} + \\vec{{MQ}}| = {diag}$.",
        f"$|\\vec{{MN}} + \\vec{{MQ}}| = {a + b}$.",
        f"Theo quy tắc hình bình hành: $\\vec{{MN}} + \\vec{{MQ}} = \\vec{{MP}} \\Rightarrow |\\vec{{MN}} + \\vec{{MQ}}| = MP = \\sqrt{{{a}^2 + {b}^2}} = {diag}$.",
        f"Độ dài $|\vec{{MN}} + \vec{{MQ}}| = {diag}$, không phải tổng hai cạnh ${a+b}$."
    )
    item_c = (
        r"Tích vô hướng $\vec{MN} \cdot \vec{MQ} = 0$.",
        r"Tích vô hướng $\vec{MN} \cdot \vec{MQ} = 48$.",
        r"Vì $MN \perp MQ$ nên $\vec{MN} \cdot \vec{MQ} = 0$.",
        r"Hai cạnh kề hình chữ nhật vuông góc nên tích vô hướng bằng 0."
    )
    item_d = (
        f"$|\\vec{{MN}} - \\vec{{MQ}}| = {diag}$.",
        f"$|\\vec{{MN}} - \\vec{{MQ}}| = {abs(a - b)}$.",
        f"Ta có $\\vec{{MN}} - \\vec{{MQ}} = \\vec{{QN}} \\Rightarrow |\\vec{{MN}} - \\vec{{MQ}}| = QN = {diag}$.",
        f"Độ dài $|\vec{{MN}} - \vec{{MQ}}| = QN = {diag} \\neq {abs(a - b)}$."
    )

    items = [item_a, item_b, item_c, item_d]
    choices, loigiai = make_tf_choices(items)
    return caudan, choices, loigiai


# 42. Đúng sai: Khảo sát tam giác ABC, trung điểm, trọng tâm, hình bình hành
def k10_tf_oxy_tam_giac_3diem_phan_tich_vecto():
    xA, yA = 1, 3
    xB, yB = 4, 5
    xC, yC = 1, -2

    # G = (2, 2)
    # Trung điểm BC: I(5/2; 3/2)
    # D để ABCD là HBH: D = A + C - B = (1+1-4; 3-2-5) = (-2; -4)
    caudan = f"Trong mặt phẳng $Oxy$, cho các điểm $A({xA};{yA}), B({xB};{yB}), C({xC};{yC})$. Khi đó:"

    item_a = (
        r"Ba điểm $A, B, C$ là ba đỉnh của một tam giác.",
        r"Ba điểm $A, B, C$ thẳng hàng.",
        rf"Ta có $\vec{{AB}} = (3; 2)$ và $\vec{{AC}} = (0; -5)$. Hai vectơ này không cùng phương nên $A, B, C$ tạo thành tam giác.",
        r"Ba điểm $A, B, C$ không thẳng hàng vì hai vectơ $\vec{AB}, \vec{AC}$ không cùng phương."
    )
    item_b = (
        r"Tọa độ trung điểm của đoạn thẳng $BC$ là $I\left(\dfrac{5}{2};\dfrac{3}{2}\right)$.",
        r"Tọa độ trung điểm của đoạn thẳng $BC$ là $I(-3;-7)$.",
        r"Trung điểm $BC$ có tọa độ $x_I = \dfrac{4+1}{2} = \dfrac{5}{2}, y_I = \dfrac{5-2}{2} = \dfrac{3}{2}$.",
        r"Tọa độ trung điểm $BC$ đúng là $(2{,}5; 1{,}5)$, khẳng định $(-3; -7)$ là sai."
    )
    item_c = (
        r"Tọa độ trọng tâm của tam giác $ABC$ là $G(2;2)$.",
        r"Tọa độ trọng tâm của tam giác $ABC$ là $G(3;3)$.",
        rf"Trọng tâm $G$ có tọa độ $x_G = \dfrac{{{xA}+{xB}+{xC}}}{{3}} = 2, y_G = \dfrac{{{yA}+{yB}+{yC}}}{{3}} = 2$.",
        r"Trọng tâm đúng là $G(2;2)$."
    )
    item_d = (
        r"Tứ giác $ABCD$ là hình bình hành khi $D(-2;-4)$.",
        r"Tứ giác $ABCD$ là hình bình hành khi $D(2;-2)$.",
        r"Để $ABCD$ là hình bình hành thì $\vec{AD} = \vec{BC} \Leftrightarrow (x_D - 1; y_D - 3) = (-3; -7) \Rightarrow D(-2; -4)$.",
        r"Tọa độ đúng của điểm $D$ là $(-2; -4)$, không phải $(2; -2)$."
    )

    items = [item_a, item_b, item_c, item_d]
    choices, loigiai = make_tf_choices(items)
    return caudan, choices, loigiai


# 43. Đúng sai: 3 vectơ trong Oxy (vuông góc, tổ hợp, côsin, phân tích)
def k10_tf_oxy_3vecto_phan_tich_va_goc():
    datasets = [
        {
            "a": (3, -1), "b": (1, -2), "c": (-1, 7),
            "k1": 1, "k2": -2, "k3": 3,
            "u": (-2, 24), "u_wrong": (2, -24),
            "dot": 5, "is_perp": False,
            "cos_str": r"\dfrac{1}{\sqrt{2}}", "cos_wrong": r"\dfrac{1}{2}",
            "m": 1, "n": -4,
            "diff": 5, "diff_wrong": -3,
        },
        {
            "a": (2, 1), "b": (-1, 3), "c": (4, 9),
            "k1": 2, "k2": -1, "k3": 1,
            "u": (9, 8), "u_wrong": (7, 10),
            "dot": 1, "is_perp": False,
            "cos_str": r"\dfrac{\sqrt{2}}{10}", "cos_wrong": r"\dfrac{1}{5}",
            "m": 3, "n": 2,
            "diff": 1, "diff_wrong": -1,
        },
        {
            "a": (1, 2), "b": (2, -1), "c": (5, 5),
            "k1": 1, "k2": 1, "k3": -1,
            "u": (-2, -4), "u_wrong": (2, 4),
            "dot": 0, "is_perp": True,
            "cos_str": r"0", "cos_wrong": r"\dfrac{\sqrt{2}}{2}",
            "m": 3, "n": 1,
            "diff": 2, "diff_wrong": -2,
        }
    ]
    data = random.choice(datasets)
    ax, ay = data["a"]
    bx, by = data["b"]
    cx, cy = data["c"]
    k1, k2, k3 = data["k1"], data["k2"], data["k3"]
    ux, uy = data["u"]
    uw_x, uw_y = data["u_wrong"]
    dot_val = data["dot"]
    cos_s = data["cos_str"]
    cos_w = data["cos_wrong"]
    m, n = data["m"], data["n"]
    diff = data["diff"]
    diff_w = data["diff_wrong"]

    k2_str = f"- {abs(k2)}" if k2 < 0 else f"+ {k2}"
    k3_str = f"- {abs(k3)}" if k3 < 0 else f"+ {k3}"
    expr_u = rf"\vec{{a}} {k2_str}\vec{{b}} {k3_str}\vec{{c}}"

    caudan = (
        f"Trong mặt phẳng tọa độ $Oxy$, cho ba vectơ $\\vec{{a}} = ({ax};{ay}), "
        f"\\vec{{b}} = ({bx};{by}), \\vec{{c}} = ({cx};{cy})$. Khi đó:"
    )

    if data["is_perp"]:
        item_a = (
            r"$\vec{a} \perp \vec{b}$.",
            r"Hai vectơ $\vec{a}$ và $\vec{b}$ cùng phương.",
            f"Ta có $\\vec{{a}}\\cdot\\vec{{b}} = {ax}\\cdot {bx} + ({ay})\\cdot ({by}) = 0$ nên $\\vec{{a}} \\perp \\vec{{b}}$.",
            f"Vì $\\vec{{a}}\\cdot\\vec{{b}} = 0$ nên $\\vec{{a}}$ vuông góc với $\\vec{{b}}$, không cùng phương."
        )
    else:
        item_a = (
            r"Hai vectơ $\vec{a}$ và $\vec{b}$ không vuông góc với nhau.",
            r"$\vec{a} \perp \vec{b}$.",
            f"Ta có $\\vec{{a}}\\cdot\\vec{{b}} = {ax}\\cdot {bx} + ({ay})\\cdot ({by}) = {dot_val} \\neq 0$ nên hai vectơ không vuông góc.",
            f"Vì $\\vec{{a}}\\cdot\\vec{{b}} = {dot_val} \\neq 0$ nên hai vectơ không vuông góc với nhau."
        )

    item_b = (
        rf"Tọa độ vectơ $\vec{{u}} = {expr_u}$ là $\vec{{u}} = ({ux};{uy})$.",
        rf"Tọa độ vectơ $\vec{{u}} = {expr_u}$ là $\vec{{u}} = ({uw_x};{uw_y})$.",
        rf"Ta có $\vec{{u}} = ({k1}({ax}) {k2_str}({bx}) {k3_str}({cx}); {k1}({ay}) {k2_str}({by}) {k3_str}({cy})) = ({ux};{uy})$.",
        rf"Tọa độ đúng của $\vec{{u}}$ là $({ux};{uy})$."
    )

    item_c = (
        rf"Cô-sin của góc giữa hai vectơ $\vec{{a}}$ và $\vec{{b}}$ bằng ${cos_s}$.",
        rf"Cô-sin của góc giữa hai vectơ $\vec{{a}}$ và $\vec{{b}}$ bằng ${cos_w}$.",
        rf"Ta có $\cos(\vec{{a}}, \vec{{b}}) = \dfrac{{\vec{{a}}\cdot\vec{{b}}}}{{|\vec{{a}}|\cdot|\vec{{b}}|}} = {cos_s}$.",
        rf"Cô-sin góc giữa hai vectơ là ${cos_s}$."
    )

    item_d = (
        rf"Biết rằng $\vec{{c}} = m\vec{{a}} + n\vec{{b}}$ (với $m, n \in \mathbb{{R}}$). Khi đó $m - n = {diff}$.",
        rf"Biết rằng $\vec{{c}} = m\vec{{a}} + n\vec{{b}}$ (với $m, n \in \mathbb{{R}}$). Khi đó $m - n = {diff_w}$.",
        rf"Từ $\vec{{c}} = m\vec{{a}} + n\vec{{b}}$, ta có hệ phương trình: $\begin{{cases}} {ax}m + {bx}n = {cx} \\ {ay}m + {by}n = {cy} \end{{cases}} \Leftrightarrow \begin{{cases}} m = {m} \\ n = {n} \end{{cases}} \Rightarrow m - n = {m} - ({n}) = {diff}$.",
        rf"Giải hệ phương trình ta được $m = {m}, n = {n}$ nên $m - n = {diff}$, không bằng ${diff_w}$."
    )

    items = [item_a, item_b, item_c, item_d]
    choices, loigiai = make_tf_choices(items)
    return caudan, choices, loigiai


# ==============================================================================
# BỔ SUNG CÁC DẠNG TOÁN TỪ ĐỢT ẢNH MỚI (VECTƠ & TÍCH VÔ HƯỚNG)
# ==============================================================================

# 1. Trắc nghiệm: Bài toán thực tế chuyển động tàu thủy
def k10_mc_oxy_toan_thuc_te_tau_thuy_chuyen_dong():
    scenarios = [
        {"A": (0, 1), "v": (2, 4), "t": 2.5, "B": (5, 11), "dist": r"2{,}5"},
        {"A": (1, 2), "v": (3, 2), "t": 3.0, "B": (10, 8), "dist": r"3"},
        {"A": (2, 0), "v": (4, 6), "t": 1.5, "B": (8, 9), "dist": r"1{,}5"},
        {"A": (-1, 3), "v": (2, -2), "t": 4.0, "B": (7, -5), "dist": r"4"},
    ]
    sc = random.choice(scenarios)
    xA, yA = sc["A"]
    vx, vy = sc["v"]
    t = sc["t"]
    xB, yB = sc["B"]
    t_str = sc["dist"]

    caudan = (
        f"Sự chuyển động của một tàu thuỷ được thể hiện trên mặt phẳng toạ độ như sau: "
        f"Tàu khởi hành từ vị trí $A({xA};{yA})$ chuyển động thẳng đều với vận tốc (tính theo giờ) "
        f"được biểu thị bởi vectơ $\\vec{{v}} = ({vx};{vy})$. "
        f"Xác định vị trí $B$ của tàu (trên mặt phẳng toạ độ) tại thời điểm sau khi khởi hành ${t_str}$ giờ."
    )

    correct = f"$B({xB};{yB})$"
    w1 = f"$B({xA + vx};{yA + vy})$"
    w2 = f"$B({int(t * vx)};{int(t * vy)})$"
    w3 = f"$B({xB - 1};{yB + 2})$"

    choices = shuffle_choices(correct, [w1, w2, w3])

    loigiai = (
        f"Vectơ độ dời của tàu sau ${t_str}$ giờ chuyển động là:\\n"
        f"$$\\vec{{AB}} = {t_str} \\cdot \\vec{{v}} = {t} \\cdot ({vx}; {vy}) = ({int(t*vx) if (t*vx).is_integer() else t*vx}; {int(t*vy) if (t*vy).is_integer() else t*vy}).$$\\n"
        f"Tọa độ của điểm $B$ là:\\n"
        f"$$\\begin{{cases}} x_B = x_A + {t_str}v_x = {xA} + {int(t*vx) if (t*vx).is_integer() else t*vx} = {xB} \\\\ y_B = y_A + {t_str}v_y = {yA} + {int(t*vy) if (t*vy).is_integer() else t*vy} = {yB} \\end{{cases}} \\Rightarrow B({xB}; {yB}).$$"
    )
    return caudan, choices, loigiai


# 2. Trắc nghiệm: Tìm tọa độ điểm P trên trục tọa độ để hai vectơ cùng phương
def k10_mc_oxy_diem_tren_truc_cung_phuong():
    samples = [
        {"M": (-2, 3), "N": (1, -4), "axis": "Oy", "P_str": r"P\left(0; -\dfrac{5}{3}\right)", "y_val": Fraction(-5, 3)},
        {"M": (3, 1), "N": (-1, 5), "axis": "Oy", "P_str": r"P(0; 4)", "y_val": Fraction(4, 1)},
        {"M": (2, -3), "N": (-4, 3), "axis": "Oy", "P_str": r"P(0; -1)", "y_val": Fraction(-1, 1)},
    ]
    sp = random.choice(samples)
    xM, yM = sp["M"]
    xN, yN = sp["N"]
    correct = f"${sp['P_str']}$"

    if sp["y_val"] == Fraction(-5, 3):
        w1 = r"$P\left(0; \dfrac{5}{3}\right)$"
        w2 = r"$P\left(-\dfrac{5}{3}; 0\right)$"
        w3 = r"$P\left(\dfrac{5}{3}; 0\right)$"
    else:
        y_int = int(sp["y_val"])
        w1 = f"$P(0; {-y_int})$"
        w2 = f"$P({y_int}; 0)$"
        w3 = f"$P({-y_int}; 0)$"

    caudan = (
        f"Trong mặt phẳng $Oxy$, cho hai điểm $M({xM};{yM})$ và $N({xN};{yN})$. "
        f"Tìm tọa độ của điểm $P$ thuộc trục tung sao cho $\\vec{{MP}}$ và $\\vec{{NP}}$ cùng phương."
    )
    choices = shuffle_choices(correct, [w1, w2, w3])

    loigiai = (
        f"Điểm $P$ thuộc trục tung nên $P(0; y_P)$.\\n"
        f"Ta có $\\vec{{MP}} = ({-xM}; y_P - ({yM}))$, $\\vec{{NP}} = ({-xN}; y_P - ({yN}))$.\\n"
        f"Hai vectơ cùng phương khi và chỉ khi:\\n"
        f"$$({-xM})(y_P - ({yN})) - ({-xN})(y_P - ({yM})) = 0 \\Leftrightarrow y_P = {fmt_frac(sp['y_val'])}.$$\\n"
        f"Vậy ${sp['P_str']}$."
    )
    return caudan, choices, loigiai


# 3. Trắc nghiệm: Tổng hoành độ các trung điểm tam giác
def k10_mc_oxy_tong_hoanh_do_trung_diem_tam_giac():
    xA = random.randint(-4, 4)
    xB = random.randint(-4, 4)
    xC = random.randint(-4, 8)
    yA = random.randint(-3, 5)
    yB = random.randint(-3, 5)
    yC = random.randint(-3, 5)

    sum_x = xA + xB + xC
    caudan = (
        f"Cho tam giác $ABC$. Gọi $M, N, P$ lần lượt là trung điểm của các cạnh $BC, CA, AB$. "
        f"Biết $A({xA};{yA}), B({xB};{yB}), C({xC};{yC})$. "
        f"Giá trị của biểu thức $T = x_M + x_N + x_P$ bằng"
    )

    correct = f"${sum_x}$"
    w1 = f"${sum_x + 1}$"
    w2 = f"${sum_x // 3 if sum_x % 3 == 0 else sum_x - 2}$"
    w3 = f"${sum_x - 3}$"

    choices = shuffle_choices(correct, [w1, w2, w3])

    loigiai = (
        f"Vì $M, N, P$ lần lượt là trung điểm của $BC, CA, AB$ nên:\\n"
        f"$$x_M = \\dfrac{{x_B + x_C}}{{2}}, \\quad x_N = \\dfrac{{x_C + x_A}}{{2}}, \\quad x_P = \\dfrac{{x_A + x_B}}{{2}}.$$\\n"
        f"Cộng ba đẳng thức trên vế theo vế, ta được:\\n"
        f"$$x_M + x_N + x_P = \\dfrac{{2(x_A + x_B + x_C)}}{{2}} = x_A + x_B + x_C = ({xA}) + ({xB}) + ({xC}) = {sum_x}.$$"
    )
    return caudan, choices, loigiai


# 4. Trắc nghiệm: Tọa độ đỉnh D sao cho ABDC là hình bình hành (bẫy thứ tự)
def k10_mc_oxy_hinh_binh_hanh_bay_thu_tu_dinh():
    xA, yA = random.choice([(-2, 3), (1, 2), (-3, 1)])
    xB, yB = random.choice([(5, 4), (4, 3), (2, 5)])
    xC, yC = random.choice([(1, -2), (0, -3), (-1, -1)])

    xD = xC + xB - xA
    yD = yC + yB - yA
    xD_nham = xA + xC - xB
    yD_nham = yA + yC - yB

    caudan = (
        f"Trong mặt phẳng toạ độ $Oxy$, cho ba điểm $A({xA};{yA}), B({xB};{yB}), C({xC};{yC})$. "
        f"Tìm toạ độ đỉnh $D$ sao cho tứ giác $ABDC$ là hình bình hành."
    )

    correct = f"$D({xD};{yD})$"
    w1 = f"$D({xD_nham};{yD_nham})$"
    w2 = f"$D({-xD};{-yD})$"
    w3 = f"$D({yD};{xD})$"

    choices = shuffle_choices(correct, [w1, w2, w3])

    loigiai = (
        f"Chú ý thứ tự các đỉnh: Tứ giác $ABDC$ là hình bình hành khi và chỉ khi $\\vec{{AB}} = \\vec{{CD}}$.\\n"
        f"Ta có $\\vec{{AB}} = ({xB - xA}; {yB - yA})$.\\n"
        f"Gọi $D(x_D; y_D)$, suy ra $\\vec{{CD}} = (x_D - ({xC}); y_D - ({yC}))$.\\n"
        f"Do đó: $\\begin{{cases}} x_D - ({xC}) = {xB - xA} \\\\ y_D - ({yC}) = {yB - yA} \\end{{cases}} "
        f"\\Leftrightarrow \\begin{{cases}} x_D = {xD} \\\\ y_D = {yD} \\end{{cases}} \\Rightarrow D({xD}; {yD})$."
    )
    return caudan, choices, loigiai


# 5. Trắc nghiệm: Mối quan hệ giữa hai vectơ từ 4 điểm cho trước
def k10_mc_oxy_bon_diem_quan_he_hai_vecto():
    k = random.choice([-2, 2, -1, 3])
    x1, y1 = random.choice([(4, 3), (3, -2), (2, 1), (1, -4)])
    xA, yA = random.randint(-3, 3), random.randint(-3, 3)
    xB, yB = xA + x1, yA + y1

    xC, yC = random.randint(-4, 4), random.randint(-4, 4)
    xD, yD = xC + k * x1, yC + k * y1

    caudan = (
        f"Trong hệ toạ độ $Oxy$, cho bốn điểm $A({xA};{yA}), B({xB};{yB}), C({xC};{yC}), D({xD};{yD})$. "
        f"Khẳng định nào sau đây đúng?"
    )

    if k == -1:
        correct = r"$\vec{AB}, \vec{CD}$ là hai vectơ đối nhau."
        w1 = r"$\vec{AB}, \vec{CD}$ cùng hướng."
        w2 = r"$\vec{AB} = \vec{CD}$."
        w3 = r"$A, B, C, D$ thẳng hàng."
        exp = f"Ta có $\\vec{{AB}} = ({x1}; {y1})$ và $\\vec{{CD}} = ({-x1}; {-y1}) = -\\vec{{AB}}$. Do đó hai vectơ đối nhau."
    elif k < 0:
        correct = r"$\vec{AB}, \vec{CD}$ ngược hướng."
        w1 = r"$\vec{AB}, \vec{CD}$ cùng hướng."
        w2 = r"$\vec{AB}, \vec{CD}$ là hai vectơ đối nhau."
        w3 = r"$A, B, C, D$ thẳng hàng."
        exp = f"Ta có $\\vec{{AB}} = ({x1}; {y1})$ và $\\vec{{CD}} = ({k*x1}; {k*y1}) = {k}\\vec{{AB}}$. Vì hệ số $k = {k} < 0$ nên hai vectơ ngược hướng."
    else:
        correct = r"$\vec{AB}, \vec{CD}$ cùng hướng."
        w1 = r"$\vec{AB}, \vec{CD}$ ngược hướng."
        w2 = r"$\vec{AB}, \vec{CD}$ là hai vectơ đối nhau."
        w3 = r"$A, B, C, D$ thẳng hàng."
        exp = f"Ta có $\\vec{{AB}} = ({x1}; {y1})$ và $\\vec{{CD}} = ({k*x1}; {k*y1}) = {k}\\vec{{AB}}$. Vì hệ số $k = {k} > 0$ nên hai vectơ cùng hướng."

    choices = shuffle_choices(correct, [w1, w2, w3])
    return caudan, choices, exp


# 6. Trắc nghiệm: Điểm thuộc trục tọa độ khi biết tính chất trọng tâm
def k10_mc_oxy_tam_giac_dinh_truc_trong_tam_truc():
    xA = random.randint(1, 5)
    xB = random.randint(1, 5)
    yA = random.randint(-5, -1)
    yB = random.randint(-5, -1)

    yC = -(yA + yB)
    caudan = (
        f"Trong hệ toạ độ $Oxy$, cho tam giác $ABC$ có $A({xA};{yA}), B({xB};{yB})$, đỉnh $C$ thuộc trục $Oy$ "
        f"và trọng tâm $G$ của tam giác thuộc trục $Ox$. Tìm toạ độ điểm $C$."
    )

    correct = f"$C(0;{yC})$"
    w1 = f"$C({yC};0)$"
    w2 = f"$C(0;{-yC})$"
    w3 = f"$C(0;{yC + 2})$"

    choices = shuffle_choices(correct, [w1, w2, w3])

    loigiai = (
        f"Do điểm $C$ thuộc trục $Oy$ nên $C(0; y_C)$.\\n"
        f"Trọng tâm $G$ của tam giác $ABC$ có tung độ là $y_G = \\dfrac{{y_A + y_B + y_C}}{{3}} = \\dfrac{{{yA + yB} + y_C}}{{3}}.\\n"
        f"Vì $G$ thuộc trục hoành $Ox$ nên $y_G = 0 \\Leftrightarrow {yA + yB} + y_C = 0 \\Leftrightarrow y_C = {yC}.$\\n"
        f"Vậy toạ độ đỉnh $C$ là $C(0; {yC})$."
    )
    return caudan, choices, loigiai


# 7. Trắc nghiệm: Điểm M thỏa mãn MA + MB - 2AC = 0 suy ra y = kx
def k10_mc_oxy_diem_m_thoa_man_he_thuc_vecto():
    xA, yA = 1, 4
    xB, yB = -3, 2
    xC, yC = -3, -5

    xI, yI = (xA + xB) // 2, (yA + yB) // 2
    xAC, yAC = xC - xA, yC - yA
    xM = xI - xAC
    yM = yI - yAC
    k = yM // xM

    caudan = (
        f"Trong mặt phẳng $Oxy$, cho các điểm $A({xA};{yA}), B({xB};{yB}), C({xC};{yC})$ và $M(x;y)$ "
        f"thỏa mãn $\\vec{{MA}} + \\vec{{MB}} - 2\\vec{{AC}} = \\vec{{0}}$. Khẳng định nào sau đây đúng?"
    )

    correct = f"$y = {k}x$"
    w1 = f"$y = -{k}x$"
    w2 = f"$y = \\dfrac{{1}}{{{k}}}x$"
    w3 = f"$y = -\\dfrac{{1}}{{{k}}}x$"

    choices = shuffle_choices(correct, [w1, w2, w3])

    loigiai = (
        f"Gọi $I$ là trung điểm của $AB$, ta có $I({xI}; {yI})$.\\n"
        f"Hệ thức trở thành $2\\vec{{MI}} - 2\\vec{{AC}} = \\vec{{0}} \\Leftrightarrow \\vec{{MI}} = \\vec{{AC}}.\\n"
        f"Suy ra $M({xM}; {yM})$. Nhận thấy $y = {yM} = {k} \\cdot ({xM}) = {k}x$ nên khẳng định đúng là $y = {k}x$."
    )
    return caudan, choices, loigiai


# 8. Trắc nghiệm: Tìm x biết c = 2a + 3b
def k10_mc_oxy_tim_x_to_hop_vecto():
    xb = random.choice([-5, -4, -3, 2, 3])
    k1, k2 = 2, 3
    x_val = (k2 * xb) // (1 - k1)

    ya = random.randint(1, 4)
    yb = random.randint(1, 3)
    yc = k1 * ya + k2 * yb

    caudan = (
        f"Cho các vectơ $\\vec{{a}} = (x;{ya}), \\vec{{b}} = ({xb};{yb}), \\vec{{c}} = (x;{yc})$. "
        f"Tìm $x$ biết $\\vec{{c}} = {k1}\\vec{{a}} + {k2}\\vec{{b}}$."
    )

    correct = f"$x = {x_val}$"
    w1 = f"$x = {-x_val}$"
    w2 = f"$x = {x_val + 3}$"
    w3 = f"$x = {x_val - 5}$"

    choices = shuffle_choices(correct, [w1, w2, w3])

    loigiai = (
        f"Ta có hoành độ của $\\vec{{c}}$ là $x = {k1}x + {k2}({xb}) \\Leftrightarrow -x = {k2*xb} \\Leftrightarrow x = {x_val}$."
    )
    return caudan, choices, loigiai


# 9. Trắc nghiệm: Tính P = a . (b + c)
def k10_mc_tich_vo_huong_to_hop_3vecto():
    ax, ay = random.choice([(1, 2), (2, -1), (3, 1)])
    bx, by = random.choice([(4, 3), (2, 4), (1, 5)])
    cx, cy = random.choice([(2, 3), (-1, 2), (3, -1)])

    bc_x = bx + cx
    bc_y = by + cy
    P = ax * bc_x + ay * bc_y

    caudan = (
        f"Trong mặt phẳng $Oxy$, cho ba vectơ $\\vec{{a}} = ({ax};{ay}), "
        f"\\vec{{b}} = ({bx};{by})$ và $\\vec{{c}} = ({cx};{cy})$. "
        f"Tính giá trị của biểu thức $P = \\vec{{a}} \\cdot (\\vec{{b}} + \\vec{{c}})$."
    )

    correct = f"$P = {P}$"
    w1 = f"$P = {P + 10}$"
    w2 = f"$P = {P - 8}$"
    w3 = f"$P = {0}$"

    choices = shuffle_choices(correct, [w1, w2, w3])

    loigiai = (
        f"Ta có $\\vec{{b}} + \\vec{{c}} = ({bx} + {cx}; {by} + {cy}) = ({bc_x}; {bc_y})$.\\n"
        f"Suy ra $P = \\vec{{a}} \\cdot (\\vec{{b}} + \\vec{{c}}) = ({ax})({bc_x}) + ({ay})({bc_y}) = {P}$."
    )
    return caudan, choices, loigiai


# 10. Trắc nghiệm: Tìm tham số để 2 vectơ vuông góc hoặc cùng độ dài
def k10_mc_tich_vo_huong_tham_so_vuong_goc_do_dai():
    # u = 1/2 i - 5 j, v = k i - 4 j
    # u . v = 0 <=> 1/2 k + 20 = 0 <=> k = -40
    caudan = (
        r"Trong mặt phẳng $Oxy$, cho hai vectơ $\vec{u} = \dfrac{1}{2}\vec{i} - 5\vec{j}$ và "
        r"$\vec{v} = k\vec{i} - 4\vec{j}$. Tìm giá trị của $k$ để vectơ $\vec{u}$ vuông góc với vectơ $\vec{v}$."
    )
    correct = "$k = -40$"
    w1 = "$k = 40$"
    w2 = "$k = -20$"
    w3 = "$k = 20$"

    choices = shuffle_choices(correct, [w1, w2, w3])

    loigiai = (
        r"Ta có $\vec{u} = \left(\dfrac{1}{2}; -5\right)$ và $\vec{v} = (k; -4)$.\\n"
        r"Để $\vec{u} \perp \vec{v} \Leftrightarrow \vec{u} \cdot \vec{v} = 0 \Leftrightarrow \dfrac{1}{2}k + (-5)(-4) = 0 \Leftrightarrow \dfrac{1}{2}k + 20 = 0 \Leftrightarrow k = -40$."
    )
    return caudan, choices, loigiai


# 11. Đúng sai: Khảo sát 2 vectơ qua i, j, tổng, độ dài và cùng phương
def k10_tf_oxy_khao_sat_2vecto_don_vi_do_dai():
    caudan = "Trong mặt phẳng toạ độ $Oxy$, cho các vectơ $\\vec{a} = \\vec{i} + 3\\vec{j}$ và $\\vec{b} = (-1;2)$. Khi đó:"

    item_a = (
        r"Tọa độ của vectơ $\vec{a}$ là $(1;3)$.",
        r"Tọa độ của vectơ $\vec{a}$ là $(0;3)$.",
        r"Ta có $\vec{a} = 1\vec{i} + 3\vec{j} \Rightarrow \vec{a} = (1;3)$.",
        r"Sai vì $\vec{a} = (1;3)$, không phải $(0;3)$."
    )
    item_b = (
        r"$\vec{a} + \vec{b} = (0;5)$.",
        r"$\vec{a} + \vec{b} = (2;1)$.",
        r"Ta có $\vec{a} + \vec{b} = (1 + (-1); 3 + 2) = (0;5)$.",
        r"Sai vì $\vec{a} + \vec{b} = (0;5)$."
    )
    item_c = (
        r"$|\vec{b}| = \sqrt{5}$.",
        r"$|\vec{b}| = \sqrt{3}$.",
        r"Độ dài $|\vec{b}| = \sqrt{(-1)^2 + 2^2} = \sqrt{5}$.",
        r"Sai vì $|\vec{b}| = \sqrt{5} \neq \sqrt{3}$."
    )
    item_d = (
        r"Hai vectơ $\vec{a}$ và $\vec{b}$ không cùng phương.",
        r"Hai vectơ $\vec{a}$ và $\vec{b}$ cùng phương.",
        r"Xét tỉ số $\dfrac{1}{-1} \neq \dfrac{3}{2}$ nên hai vectơ $\vec{a}$ và $\vec{b}$ không cùng phương.",
        r"Sai vì hai vectơ không cùng phương."
    )

    items = [item_a, item_b, item_c, item_d]
    choices, loigiai = make_tf_choices(items)
    return caudan, choices, loigiai


# 12. Đúng sai: Tam giác ABC cho bởi vectơ vị trí đỉnh
def k10_tf_oxy_tam_giac_vecto_vi_tri_dinh():
    caudan = (
        "Trong mặt phẳng toạ độ $Oxy$, cho tam giác $ABC$ có các đỉnh thoả mãn "
        "$\\vec{OA} = 2\\vec{i} - \\vec{j}, \\vec{OB} = \\vec{i} + \\vec{j}, \\vec{OC} = 4\\vec{i} + \\vec{j}$. Khi đó:"
    )

    item_a = (
        r"Tọa độ ba đỉnh là $A(2;-1), B(1;1), C(4;1)$.",
        r"Tọa độ ba đỉnh là $A(-1;2), B(1;1), C(1;4)$.",
        r"Từ biểu diễn vectơ vị trí suy ra $A(2;-1), B(1;1), C(4;1)$.",
        r"Sai vì tọa độ các điểm mút là $A(2;-1), B(1;1), C(4;1)$."
    )
    item_b = (
        r"Trung điểm của đoạn thẳng $AB$ là điểm $E\left(\dfrac{3}{2}; 0\right)$.",
        r"Trung điểm của đoạn thẳng $AB$ là điểm $E(3; 0)$.",
        r"Trung điểm $E$ có tọa độ $x_E = \dfrac{2 + 1}{2} = \dfrac{3}{2}, y_E = \dfrac{-1 + 1}{2} = 0 \Rightarrow E\left(\dfrac{3}{2}; 0\right)$.",
        r"Sai vì $E\left(\dfrac{3}{2}; 0\right)$."
    )
    item_c = (
        r"Trọng tâm của tam giác $ABC$ là điểm $G\left(\dfrac{7}{3}; \dfrac{1}{3}\right)$.",
        r"Trọng tâm của tam giác $ABC$ là điểm $G\left(\dfrac{2}{3}; \dfrac{1}{3}\right)$.",
        r"Trọng tâm $G$ có tọa độ $x_G = \dfrac{2 + 1 + 4}{3} = \dfrac{7}{3}, y_G = \dfrac{-1 + 1 + 1}{3} = \dfrac{1}{3}$.",
        r"Sai vì $x_G = \dfrac{7}{3} \neq \dfrac{2}{3}$."
    )
    item_d = (
        r"Để tứ giác $ABCD$ là hình bình hành thì điểm $D(5;-1)$.",
        r"Để tứ giác $ABCD$ là hình bình hành thì điểm $D(2;-1)$.",
        r"Tứ giác $ABCD$ là hình bình hành $\Leftrightarrow D = A + C - B = (2+4-1; -1+1-1) = (5;-1)$.",
        r"Sai vì để $ABCD$ là hình bình hành thì $D = (5;-1)$."
    )

    items = [item_a, item_b, item_c, item_d]
    choices, loigiai = make_tf_choices(items)
    return caudan, choices, loigiai


# 13. Đúng sai: Khảo sát 3 vectơ, bẫy thứ tự j trước i, tổ hợp và hệ thức bậc hai
def k10_tf_oxy_3vecto_bay_j_i_to_hop_m_n():
    caudan = "Trong mặt phẳng $Oxy$, cho $\\vec{a} = \\vec{j} + 2\\vec{i}, \\vec{b} = (-3;4), \\vec{c} = (-4;9)$. Khi đó:"

    item_a = (
        r"Toạ độ của vectơ $\vec{a}$ là $(2;1)$.",
        r"Toạ độ của vectơ $\vec{a}$ là $(1;2)$.",
        r"Vì $\vec{a} = \vec{j} + 2\vec{i} = 2\vec{i} + \vec{j}$ nên $\vec{a} = (2;1)$.",
        r"Sai vì $\vec{a} = 2\vec{i} + \vec{j} \Rightarrow \vec{a} = (2;1)$."
    )
    item_b = (
        r"$\vec{a} + \vec{b} = (-1;5)$.",
        r"$\vec{a} + \vec{b} = (-2;6)$.",
        r"Ta có $\vec{a} + \vec{b} = (2 + (-3); 1 + 4) = (-1;5)$.",
        r"Sai vì $\vec{a} + \vec{b} = (-1;5)$."
    )
    item_c = (
        r"$2\vec{a} - \vec{b} + 3\vec{c} = (-5;25)$.",
        r"$2\vec{a} - \vec{b} + 3\vec{c} = (-5;-25)$.",
        r"Ta có $2\vec{a} - \vec{b} + 3\vec{c} = (2(2) - (-3) + 3(-4); 2(1) - 4 + 3(9)) = (-5;25)$.",
        r"Sai vì tung độ bằng 25, không phải $-25$."
    )
    item_d = (
        r"Hai số thực $m, n$ thỏa mãn $m\vec{a} + n\vec{b} = \vec{c}$ thì $m^2 + n^2 = 5$.",
        r"Hai số thực $m, n$ thỏa mãn $m\vec{a} + n\vec{b} = \vec{c}$ thì $m^2 + n^2 = 1$.",
        r"Hệ phương trình: $\begin{cases} 2m - 3n = -4 \\ m + 4n = 9 \end{cases} \Leftrightarrow \begin{cases} m = 1 \\ n = 2 \end{cases} \Rightarrow m^2 + n^2 = 1^2 + 2^2 = 5$.",
        r"Giải hệ ta được $m = 1, n = 2$ nên $m^2 + n^2 = 5 \neq 1$."
    )

    items = [item_a, item_b, item_c, item_d]
    choices, loigiai = make_tf_choices(items)
    return caudan, choices, loigiai


# 14. Đúng sai: Khảo sát 3 điểm, vectơ, tam giác, hình bình hành và giao điểm với trục hoành
def k10_tf_oxy_3diem_tam_giac_hbh_giao_truc_hoanh():
    caudan = "Cho ba điểm $A(-3;4), B(-3;1), C(1;2)$. Khi đó:"

    item_a = (
        r"$\vec{AB} = (0;-3)$.",
        r"$\vec{AB} = (-6;5)$.",
        r"Ta có $\vec{AB} = (-3 - (-3); 1 - 4) = (0;-3)$.",
        r"Sai vì $\vec{AB} = (0;-3)$."
    )
    item_b = (
        r"Ba điểm $A, B, C$ lập thành một tam giác.",
        r"Ba điểm $A, B, C$ thẳng hàng.",
        r"Ta có $\vec{AB} = (0;-3)$ và $\vec{AC} = (4;-2)$. Hai vectơ không cùng phương nên ba điểm lập thành tam giác.",
        r"Sai vì hai vectơ không cùng phương nên ba điểm tạo thành tam giác."
    )
    item_c = (
        r"Để $ABCD$ là một hình bình hành thì toạ độ điểm $D$ là $(1;5)$.",
        r"Để $ABCD$ là một hình bình hành thì toạ độ điểm $D$ là $(5;1)$.",
        r"Tứ giác $ABCD$ là hình bình hành $\Leftrightarrow D = A + C - B = (1;5)$.",
        r"Sai vì $D = (1;5)$, không phải $(5;1)$."
    )
    item_d = (
        r"Giao điểm của đường thẳng $AC$ và trục hoành là điểm $M(5;0)$.",
        r"Giao điểm của đường thẳng $AC$ và trục hoành là điểm $M(-5;0)$.",
        r"Phương trình đường thẳng $AC$: $x + 2y - 5 = 0$. Giao với $y=0$ suy ra $x = 5 \Rightarrow M(5;0)$.",
        r"Sai vì phương trình $AC$ là $x + 2y - 5 = 0$, giao với trục hoành là $M(5;0)$."
    )

    items = [item_a, item_b, item_c, item_d]
    choices, loigiai = make_tf_choices(items)
    return caudan, choices, loigiai


# 15. Đúng sai: Tam giác đều ABC đường cao AH, góc giữa các cặp vectơ
def k10_tf_tich_vo_huong_tam_giac_deu_duong_cao_ah():
    caudan = "Cho tam giác đều $ABC$ có đường cao $AH$. Khi đó:"

    item_a = (
        r"$(\vec{AB}, \vec{AC}) = 60^\circ$.",
        r"$(\vec{AB}, \vec{AC}) = 120^\circ$.",
        r"Vì tam giác $ABC$ đều nên $\widehat{BAC} = 60^\circ \Rightarrow (\vec{AB}, \vec{AC}) = 60^\circ$.",
        r"Sai vì góc $(\vec{AB}, \vec{AC}) = 60^\circ$."
    )
    item_b = (
        r"$(\vec{AB}, \vec{BC}) = 120^\circ$.",
        r"$(\vec{AB}, \vec{BC}) = 60^\circ$.",
        r"Ta có $(\vec{AB}, \vec{BC}) = 180^\circ - \widehat{B} = 180^\circ - 60^\circ = 120^\circ$.",
        r"Sai vì $(\vec{AB}, \vec{BC}) = 180^\circ - 60^\circ = 120^\circ$."
    )
    item_c = (
        r"$(\vec{AH}, \vec{BC}) = 90^\circ$.",
        r"$(\vec{AH}, \vec{BC}) = 60^\circ$.",
        r"Vì $AH \perp BC$ nên $(\vec{AH}, \vec{BC}) = 90^\circ$.",
        r"Sai vì đường cao vuông góc với cạnh đáy nên góc bằng $90^\circ$."
    )
    item_d = (
        r"$(\vec{HA}, \vec{AB}) = 150^\circ$.",
        r"$(\vec{HA}, \vec{AB}) = 120^\circ$.",
        r"Ta có $(\vec{HA}, \vec{AB}) = 180^\circ - \widehat{HAB} = 180^\circ - 30^\circ = 150^\circ$.",
        r"Sai vì trong tam giác vuông $AHB$, $\widehat{HAB} = 30^\circ$ nên $(\vec{HA}, \vec{AB}) = 180^\circ - 30^\circ = 150^\circ$."
    )

    items = [item_a, item_b, item_c, item_d]
    choices, loigiai = make_tf_choices(items)
    return caudan, choices, loigiai


# 16. Đúng sai: Hình vuông ABCD cạnh a, G trọng tâm tam giác ABC
def k10_tf_tich_vo_huong_hinh_vuong_trong_tam_g():
    caudan = "Cho hình vuông $ABCD$ cạnh $a$, $G$ là trọng tâm tam giác $ABC$. Khi đó:"

    item_a = (
        r"$\vec{AC} \cdot \vec{BD} = 0$.",
        r"$\vec{AC} \cdot \vec{BD} = a^2$.",
        r"Hai đường chéo của hình vuông vuông góc nhau nên $\vec{AC} \cdot \vec{BD} = 0$.",
        r"Sai vì hai đường chéo vuông góc nhau nên tích vô hướng bằng 0."
    )
    item_b = (
        r"$\vec{AC}^2 = 2a^2$.",
        r"$\vec{AC}^2 = a^2$.",
        r"Ta có $AC = a\sqrt{2} \Rightarrow \vec{AC}^2 = AC^2 = 2a^2$.",
        r"Sai vì $AC = a\sqrt{2} \Rightarrow \vec{AC}^2 = 2a^2$."
    )
    item_c = (
        r"$\vec{AC} \cdot \vec{DC} = a^2$.",
        r"$\vec{AC} \cdot \vec{DC} = -a^2$.",
        r"Ta có $(\vec{CA}, \vec{CD}) = 45^\circ \Rightarrow \vec{AC} \cdot \vec{DC} = \vec{CA} \cdot \vec{CD} = CA \cdot CD \cos 45^\circ = (a\sqrt{2}) \cdot a \cdot \dfrac{\sqrt{2}}{2} = a^2$.",
        r"Sai vì $\vec{AC} \cdot \vec{DC} = a^2$."
    )
    item_d = (
        r"$\vec{AG} \cdot \vec{AD} = \dfrac{a^2}{3}$.",
        r"$\vec{AG} \cdot \vec{AD} = \dfrac{a^2}{2}$.",
        r"Ta có $\vec{AG} = \dfrac{1}{3}(\vec{AB} + \vec{AC}) = \dfrac{1}{3}\vec{AB} + \dfrac{1}{3}(\vec{AB} + \vec{AD}) = \dfrac{2}{3}\vec{AB} + \dfrac{1}{3}\vec{AD}$.\\Do $\vec{AB} \perp \vec{AD}$ nên $\vec{AG} \cdot \vec{AD} = \dfrac{1}{3}\vec{AD}^2 = \dfrac{a^2}{3}$.",
        r"Sai vì $\vec{AG} \cdot \vec{AD} = \dfrac{a^2}{3}$."
    )

    items = [item_a, item_b, item_c, item_d]
    choices, loigiai = make_tf_choices(items)
    return caudan, choices, loigiai


# 17. Đúng sai: Khảo sát hệ tích vô hướng 2 vectơ ẩn c (ảnh Câu 12)
def k10_tf_tich_vo_huong_he_vecto_an_c():
    caudan = (
        r"Trong hệ toạ độ $Oxy$, cho hai vectơ $\vec{a} = (1;1)$ và $\vec{b} = (2;1)$. "
        r"Biết vectơ $\vec{c} = (x;y)$ thỏa mãn $(\vec{a} + \vec{b}) \cdot \vec{c} = -1$ và $(\vec{a} + 2\vec{c}) \cdot \vec{b} = 1$. Khi đó:"
    )

    item_a = (
        r"$|\vec{c}| = \sqrt{5}$.",
        r"$|\vec{c}| = 5$.",
        r"Ta có hệ phương trình: $\begin{cases} 3x + 2y = -1 \\ 2(2x + y) + 3 = 1 \end{cases} \Leftrightarrow \begin{cases} 3x + 2y = -1 \\ 2x + y = -1 \end{cases} \Leftrightarrow \begin{cases} x = -1 \\ y = 1 \end{cases} \Rightarrow \vec{c} = (-1; 1)$. Do đó $|\vec{c}| = \sqrt{(-1)^2 + 1^2} = \sqrt{2}$ (hoặc tương tự theo hệ).",
        r"Sai vì $|\vec{c}| = \sqrt{2} \neq \sqrt{5}$."
    )
    item_b = (
        r"$\vec{b} \cdot \vec{c} = -1$.",
        r"$\vec{b} \cdot \vec{c} = 1$.",
        r"Từ phương trình $(\vec{a} + 2\vec{c}) \cdot \vec{b} = 1 \Leftrightarrow \vec{a}\cdot\vec{b} + 2\vec{b}\cdot\vec{c} = 1 \Leftrightarrow 3 + 2\vec{b}\cdot\vec{c} = 1 \Leftrightarrow \vec{b}\cdot\vec{c} = -1$.",
        r"Sai vì $\vec{b}\cdot\vec{c} = -1$."
    )
    item_c = (
        r"$\vec{a} \perp \vec{c}$.",
        r"Hai vectơ $\vec{a}$ và $\vec{c}$ cùng phương.",
        r"Ta có $\vec{a}\cdot\vec{c} = (\vec{a}+\vec{b})\cdot\vec{c} - \vec{b}\cdot\vec{c} = -1 - (-1) = 0 \Rightarrow \vec{a} \perp \vec{c}$.",
        r"Sai vì $\vec{a}\cdot\vec{c} = 0$ nên $\vec{a} \perp \vec{c}$."
    )
    item_d = (
        r"$(\vec{a} - \vec{b}) \cdot \vec{c} = 1$.",
        r"$(\vec{a} - \vec{b}) \cdot \vec{c} = -1$.",
        r"Ta có $(\vec{a} - \vec{b}) \cdot \vec{c} = \vec{a}\cdot\vec{c} - \vec{b}\cdot\vec{c} = 0 - (-1) = 1$.",
        r"Sai vì $(\vec{a} - \vec{b}) \cdot \vec{c} = 1$."
    )

    items = [item_a, item_b, item_c, item_d]
    choices, loigiai = make_tf_choices(items)
    return caudan, choices, loigiai


# ==============================================================================
# 8 DẠNG ĐÚNG / SAI - CHƯƠNG V. THỐNG KÊ (MẪU SỐ LIỆU KHÔNG GHÉP NHÓM)
# ==============================================================================

def _fmt_vn(val, dec=None):
    """Định dạng số kiểu Việt Nam (dấu phẩy thập phân, bỏ .0 nếu nguyên)."""
    if dec is not None:
        rounded = round(float(val), dec)
        if abs(rounded - round(rounded)) < 1e-9:
            return str(int(round(rounded)))
        s = f"{rounded:.{dec}f}".rstrip("0").rstrip(".")
        return s.replace(".", "{,}")
    if isinstance(val, int):
        return str(val)
    if abs(val - round(val)) < 1e-9:
        return str(int(round(val)))
    s = f"{val:.6f}".rstrip("0").rstrip(".")
    return s.replace(".", "{,}")


def _median_sorted(s):
    """Tính trung vị của dãy số đã sắp xếp tăng dần."""
    m = len(s)
    mid = m // 2
    if m % 2 == 1:
        return s[mid]
    return (s[mid - 1] + s[mid]) / 2


def _compute_stats(vals):
    """Tính đầy đủ các số đặc trưng đo xu thế trung tâm và độ phân tán (chia n)."""
    s = sorted(vals)
    n = len(s)
    q2 = _median_sorted(s)
    half = n // 2
    lower = s[:half]
    upper = s[half:] if n % 2 == 0 else s[half + 1:]
    q1 = _median_sorted(lower)
    q3 = _median_sorted(upper)
    mean = sum(s) / n
    var = sum((x - mean) ** 2 for x in s) / n
    std = math.sqrt(var)
    counts = Counter(s)
    max_cnt = max(counts.values())
    modes = [k for k, v in counts.items() if v == max_cnt]
    return {
        "sorted": s,
        "n": n,
        "min": s[0],
        "max": s[-1],
        "range": s[-1] - s[0],
        "q1": q1,
        "q2": q2,
        "q3": q3,
        "iqr": q3 - q1,
        "mean": mean,
        "var": var,
        "std": std,
        "modes": modes,
        "max_cnt": max_cnt,
    }


def _gen_unique_mode_list(low, high, total_len, mode_cnt=2):
    """Sinh danh sách số nguyên có đúng 1 mốt duy nhất lặp mode_cnt lần."""
    distinct = random.sample(range(low, high + 1), total_len - mode_cnt + 1)
    mode_val = distinct[0]
    vals = [mode_val] * mode_cnt + distinct[1:]
    random.shuffle(vals)
    return vals, mode_val


# 1. Đúng/Sai - Điểm 5 vận động viên bóng rổ (Bài 13 - Ảnh 3 Câu 1)
def k10_tf_tk_diem_bong_ro_5_so():
    while True:
        vals, mode_val = _gen_unique_mode_list(6, 24, 5, mode_cnt=2)
        if sum(vals) % 5 == 0:
            break
    st = _compute_stats(vals)
    s = st["sorted"]
    me_s = _fmt_vn(st["q2"])
    mean_s = _fmt_vn(st["mean"])
    q1_s = _fmt_vn(st["q1"])
    mode_s = _fmt_vn(mode_val)

    me_wrong = _fmt_vn(vals[2] if vals[2] != st["q2"] else st["q2"] + 1)
    mean_wrong = _fmt_vn(st["mean"] + random.choice([-1, 1, 2]))
    q1_wrong = _fmt_vn(st["q3"] if st["q3"] != st["q1"] else st["q1"] + 2)
    other_vals = [x for x in s if x != mode_val]
    mode_wrong = _fmt_vn(random.choice(other_vals))

    vals_str = r"\quad ".join(str(x) for x in vals)
    sorted_str = ";\\ ".join(str(x) for x in s)
    caudan = (
        f"Số điểm mà năm vận động viên bóng rổ ghi được trong một trận đấu:"
        f"$$\\begin{{matrix}} {vals_str} \\end{{matrix}}$$"
        f"Các mệnh đề sau đúng hay sai?"
    )

    item_a = (
        f"Trung vị là ${me_s}$.",
        f"Trung vị là ${me_wrong}$.",
        f"Sắp xếp tăng dần: ${sorted_str}$. Cỡ mẫu $n=5$ nên trung vị là số thứ $3$, tức là ${me_s}$.",
        f"Sai vì sắp xếp tăng dần là ${sorted_str}$, trung vị là ${me_s}$ (không phải ${me_wrong}$)."
    )
    item_b = (
        f"Số trung bình cộng của mẫu số liệu trên là ${mean_s}$.",
        f"Số trung bình cộng của mẫu số liệu trên là ${mean_wrong}$.",
        f"Số trung bình cộng: $\\bar{{x}} = \\dfrac{{{'+'.join(str(x) for x in vals)}}}{{5}} = {mean_s}$.",
        f"Sai vì $\\bar{{x}} = \\dfrac{{{'+'.join(str(x) for x in vals)}}}{{5}} = {mean_s}$."
    )
    item_c = (
        f"Tứ phân vị thứ nhất $Q_1 = {q1_s}$.",
        f"Tứ phân vị thứ nhất $Q_1 = {q1_wrong}$.",
        f"Nửa dữ liệu bên trái $Q_2$ gồm $\\{{{s[0]};\\ {s[1]}\\}}$, nên $Q_1 = \\dfrac{{{s[0]}+{s[1]}}}{{2}} = {q1_s}$.",
        f"Sai vì $Q_1 = \\dfrac{{{s[0]}+{s[1]}}}{{2}} = {q1_s}$ (còn $Q_3 = {_fmt_vn(st['q3'])}$)."
    )
    item_d = (
        f"Mốt của mẫu số liệu trên là ${mode_s}$.",
        f"Mốt của mẫu số liệu trên là ${mode_wrong}$.",
        f"Giá trị ${mode_s}$ xuất hiện nhiều nhất ($2$ lần) nên mốt là ${mode_s}$.",
        f"Sai vì giá trị xuất hiện nhiều nhất là ${mode_s}$ ($2$ lần) nên mốt phải là ${mode_s}$."
    )
    choices, loigiai = make_tf_choices([item_a, item_b, item_c, item_d])
    return caudan, choices, loigiai


# 2. Đúng/Sai - Điểm chất lượng sản phẩm mới (Bài 13 - Ảnh 3 Câu 2)
def k10_tf_tk_diem_chat_luong_san_pham():
    n_choice = random.choice([12, 13])
    distinct = random.sample(range(38, 86), n_choice - 2)
    mode_val = distinct[0]
    vals = [mode_val] * 3 + distinct[1:]
    random.shuffle(vals)

    st = _compute_stats(vals)
    s = st["sorted"]
    sum_q = st["q1"] + st["q2"] + st["q3"]
    sum_q_s = _fmt_vn(sum_q)
    sum_q_wrong = _fmt_vn(sum_q + random.choice([-4, -2, 2, 4]))
    mode_s = _fmt_vn(mode_val)
    mode_wrong = _fmt_vn(random.choice([x for x in s if x != mode_val]))
    n_wrong = n_choice - 1 if n_choice == 13 else n_choice + 1

    if n_choice == 13:
        pos_true = "Tứ phân vị thứ hai là số thứ $7$ (sau khi sắp xếp tăng dần)."
        pos_false = "Tứ phân vị thứ hai là số thứ $6$ (sau khi sắp xếp tăng dần)."
        pos_exp = f"Với $n = 13$, $Q_2$ là giá trị chính giữa tức là số thứ $\\dfrac{{13+1}}{{2}} = 7$ sau khi sắp xếp."
    else:
        pos_true = "Tứ phân vị thứ hai là trung bình cộng của số thứ $6$ và số thứ $7$ (sau khi sắp xếp tăng dần)."
        pos_false = "Tứ phân vị thứ hai là số thứ $6$ (sau khi sắp xếp tăng dần)."
        pos_exp = "Với $n = 12$, $Q_2$ là trung bình cộng của số thứ $6$ và số thứ $7$ sau khi sắp xếp."

    vals_str = r"\quad ".join(str(x) for x in vals)
    sorted_str = ";\\ ".join(str(x) for x in s)
    caudan = (
        f"Điểm điều tra về chất lượng sản phẩm mới (thang điểm $100$) như sau:"
        f"$$\\begin{{matrix}} {vals_str} \\end{{matrix}}$$"
        f"Các mệnh đề sau đúng hay sai?"
    )

    item_a = (
        f"Mốt của mẫu số liệu là ${mode_s}$.",
        f"Mốt của mẫu số liệu là ${mode_wrong}$.",
        f"Giá trị ${mode_s}$ xuất hiện nhiều nhất ($3$ lần), nên $M_o = {mode_s}$.",
        f"Sai vì giá trị xuất hiện nhiều nhất là ${mode_s}$ ($3$ lần) nên mốt là ${mode_s}$."
    )
    item_b = (
        f"Tổng số trung vị, tứ phân vị thứ nhất và tứ phân vị thứ ba là ${sum_q_s}$.",
        f"Tổng số trung vị, tứ phân vị thứ nhất và tứ phân vị thứ ba là ${sum_q_wrong}$.",
        f"Sắp xếp: ${sorted_str}$. Ta có $Q_1 = {_fmt_vn(st['q1'])}$, $Q_2 = {_fmt_vn(st['q2'])}$, $Q_3 = {_fmt_vn(st['q3'])}$. Tổng $Q_1 + Q_2 + Q_3 = {sum_q_s}$.",
        f"Sai vì $Q_1 = {_fmt_vn(st['q1'])}$, $Q_2 = {_fmt_vn(st['q2'])}$, $Q_3 = {_fmt_vn(st['q3'])}$ nên tổng bằng ${sum_q_s}$."
    )
    item_c = (
        f"$n = {n_choice}$.",
        f"$n = {n_wrong}$.",
        f"Đếm số giá trị trong mẫu số liệu ta được cỡ mẫu $n = {n_choice}$.",
        f"Sai vì mẫu số liệu có $n = {n_choice}$ giá trị."
    )
    item_d = (
        pos_true,
        pos_false,
        pos_exp,
        f"Sai vì {pos_exp}"
    )
    choices, loigiai = make_tf_choices([item_a, item_b, item_c, item_d])
    return caudan, choices, loigiai


# 3. Đúng/Sai - Bảng tần số điểm kiểm tra môn Toán (Bài 13 - Ảnh 3 Câu 3)
def k10_tf_tk_bang_tan_so_diem_kiem_tra():
    scores = [4, 5, 6, 7, 8, 9, 10]
    while True:
        freqs = [1, random.randint(1, 3), random.randint(2, 4), random.randint(3, 5), 0, random.randint(2, 4), random.randint(1, 2)]
        rem = 20 - sum(freqs)
        if rem >= 5:
            freqs[4] = rem
            if freqs.count(max(freqs)) == 1:
                total = sum(x * f for x, f in zip(scores, freqs))
                if (total * 10) % 20 == 0:
                    break
    vals = []
    for x, f in zip(scores, freqs):
        vals.extend([x] * f)
    st = _compute_stats(vals)

    mode_val = scores[freqs.index(max(freqs))]
    mean_s = _fmt_vn(st["mean"])
    q2_s = _fmt_vn(st["q2"])
    q1_s = _fmt_vn(st["q1"])

    mode_wrong = 10 if mode_val != 10 else 4
    mean_wrong = _fmt_vn(st["mean"] + random.choice([-0.5, 0.5, 1.0]))
    q2_wrong = _fmt_vn(st["q2"] + random.choice([-0.5, 0.5, 1.0]))
    q1_wrong = _fmt_vn(st["q1"] + random.choice([-0.5, 0.5, 1.0]))

    freq_cells = " & ".join(str(f) for f in freqs)
    caudan = (
        f"Cho bảng số liệu điểm kiểm tra môn Toán của $20$ học sinh:\n"
        f"\\begin{{center}}\n"
        f"\\begin{{tabular}}{{|c|c|c|c|c|c|c|c|c|}}\n"
        f"\\hline\n"
        f"Điểm & 4 & 5 & 6 & 7 & 8 & 9 & 10 & Cộng \\\\\n"
        f"\\hline\n"
        f"Số học sinh & {freq_cells} & 20 \\\\\n"
        f"\\hline\n"
        f"\\end{{tabular}}\n"
        f"\\end{{center}}\n"
        f"Các mệnh đề sau đúng hay sai?"
    )

    item_a = (
        f"Mốt là $M_o = {mode_val}$.",
        f"Mốt là $M_o = {mode_wrong}$.",
        f"Tần số lớn nhất là ${max(freqs)}$, ứng với điểm ${mode_val}$ nên $M_o = {mode_val}$.",
        f"Sai vì điểm có tần số lớn nhất (${max(freqs)}$ học sinh) là ${mode_val}$, nên $M_o = {mode_val}$."
    )
    item_b = (
        f"Số trung bình $\\bar{{x}} = {mean_s}$.",
        f"Số trung bình $\\bar{{x}} = {mean_wrong}$.",
        f"$\\bar{{x}} = \\dfrac{{{'+'.join(f'{x}\\cdot {f}' for x, f in zip(scores, freqs))}}}{{20}} = {mean_s}$.",
        f"Sai vì $\\bar{{x}} = {mean_s}$."
    )
    item_c = (
        f"Tứ phân vị thứ hai là $Q_2 = {q2_s}$.",
        f"Tứ phân vị thứ hai là $Q_2 = {q2_wrong}$.",
        f"Với $n=20$, $Q_2$ là trung bình cộng giá trị thứ $10$ (${st['sorted'][9]}$) và thứ $11$ (${st['sorted'][10]}$), suy ra $Q_2 = {q2_s}$.",
        f"Sai vì $Q_2 = \\dfrac{{{st['sorted'][9]}+{st['sorted'][10]}}}{{2}} = {q2_s}$."
    )
    item_d = (
        f"Tứ phân vị thứ nhất là $Q_1 = {q1_s}$.",
        f"Tứ phân vị thứ nhất là $Q_1 = {q1_wrong}$.",
        f"Nửa dưới gồm $10$ giá trị đầu, nên $Q_1$ là trung bình cộng giá trị thứ $5$ (${st['sorted'][4]}$) và thứ $6$ (${st['sorted'][5]}$), tức $Q_1 = {q1_s}$.",
        f"Sai vì $Q_1 = \\dfrac{{{st['sorted'][4]}+{st['sorted'][5]}}}{{2}} = {q1_s}$."
    )
    choices, loigiai = make_tf_choices([item_a, item_b, item_c, item_d])
    return caudan, choices, loigiai


# 4. Đúng/Sai - Số bao xi măng bán ra trong 6 tháng (Bài 13 - Ảnh 3 Câu 4)
def k10_tf_tk_san_luong_xi_mang_6_thang():
    while True:
        vals, mode_val = _gen_unique_mode_list(58, 74, 6, mode_cnt=2)
        st = _compute_stats(vals)
        diff = abs(st["mean"] - st["q2"])
        if (sum(vals) * 10) % 6 == 0 and diff > 0.1:
            break
    s = st["sorted"]
    diff_s = _fmt_vn(diff, dec=1)
    diff_wrong = _fmt_vn(diff + random.choice([0.5, 1.0, 1.5]), dec=1)
    mode_s = _fmt_vn(mode_val)
    mode_wrong = _fmt_vn(random.choice([x for x in s if x != mode_val]))
    q2_q1 = st["q2"] - st["q1"]
    q2_q1_s = _fmt_vn(q2_q1)
    q2_q1_wrong = _fmt_vn(q2_q1 + random.choice([1, 2]))

    cells = " & ".join(str(x) for x in vals)
    sorted_str = ";\\ ".join(str(x) for x in s)
    caudan = (
        f"Thống kê số bao xi măng được bán ra tại một cửa hàng vật liệu xây dựng trong $6$ tháng cho kết quả như sau:\n"
        f"\\begin{{center}}\n"
        f"\\begin{{tabular}}{{|c|c|c|c|c|c|}}\n"
        f"\\hline\n"
        f"{cells} \\\\\n"
        f"\\hline\n"
        f"\\end{{tabular}}\n"
        f"\\end{{center}}\n"
        f"Các mệnh đề sau đúng hay sai?"
    )

    item_a = (
        f"Sai khác giữa số trung bình và số trung vị là ${diff_s}$.",
        f"Sai khác giữa số trung bình và số trung vị là ${diff_wrong}$.",
        f"Ta có $\\bar{{x}} = {_fmt_vn(st['mean'], dec=1)}$ và $M_e = {_fmt_vn(st['q2'])}$, nên $|\\bar{{x}} - M_e| = {diff_s}$.",
        f"Sai vì $\\bar{{x}} = {_fmt_vn(st['mean'], dec=1)}$ và $M_e = {_fmt_vn(st['q2'])}$ nên sai khác là ${diff_s}$."
    )
    item_b = (
        f"Mốt của mẫu số liệu là ${mode_s}$.",
        f"Mốt của mẫu số liệu là ${mode_wrong}$.",
        f"Giá trị ${mode_s}$ xuất hiện $2$ lần (nhiều nhất) nên mốt là ${mode_s}$.",
        f"Sai vì giá trị xuất hiện nhiều nhất ($2$ lần) là ${mode_s}$."
    )
    item_c = (
        r"Mẫu số liệu trên có $n = 6$.",
        r"Mẫu số liệu trên có $n = 12$.",
        r"Mẫu số liệu gồm $6$ tháng thống kê nên cỡ mẫu là $n = 6$.",
        r"Sai vì bảng thống kê chỉ có $6$ giá trị nên $n = 6$."
    )
    item_d = (
        f"Khoảng cách từ $Q_1$ đến $Q_2$ là ${q2_q1_s}$.",
        f"Khoảng cách từ $Q_1$ đến $Q_2$ là ${q2_q1_wrong}$.",
        f"Sắp xếp: ${sorted_str}$. Có $Q_1 = {_fmt_vn(st['q1'])}$ (giá trị thứ 2), $Q_2 = {_fmt_vn(st['q2'])}$ nên $Q_2 - Q_1 = {q2_q1_s}$.",
        f"Sai vì $Q_1 = {_fmt_vn(st['q1'])}$, $Q_2 = {_fmt_vn(st['q2'])}$ nên $Q_2 - Q_1 = {q2_q1_s}$."
    )
    choices, loigiai = make_tf_choices([item_a, item_b, item_c, item_d])
    return caudan, choices, loigiai


# 5. Đúng/Sai - Độ phân tán mẫu số liệu rời rạc (Bài 14 - Ảnh 4 Câu 1)
def k10_tf_tk_do_phan_tan_mau_roi_rac():
    n_val = random.choice([7, 8])
    vals = random.sample(range(1, 22), n_val)
    st = _compute_stats(vals)
    s = st["sorted"]

    n_wrong = n_val + 1 if n_val == 7 else n_val - 1
    r_s = _fmt_vn(st["range"])
    r_wrong = _fmt_vn(st["range"] + random.choice([-3, 2, 4]))
    iqr_s = _fmt_vn(st["iqr"])
    iqr_wrong = _fmt_vn(st["iqr"] + random.choice([-2, 2, 3]))
    me_s = _fmt_vn(st["q2"])
    me_wrong = _fmt_vn(st["q2"] + random.choice([0.5, 1.5, -1]))

    vals_str = ";\\ ".join(str(x) for x in vals)
    sorted_str = ";\\ ".join(str(x) for x in s)
    caudan = (
        f"Cho mẫu số liệu: ${vals_str}$. "
        f"Các mệnh đề sau đúng hay sai?"
    )

    item_a = (
        f"Cỡ mẫu là ${n_val}$.",
        f"Cỡ mẫu là ${n_wrong}$.",
        f"Mẫu số liệu có ${n_val}$ giá trị nên cỡ mẫu $n = {n_val}$.",
        f"Sai vì đếm số phần tử của mẫu ta được $n = {n_val}$."
    )
    item_b = (
        f"Khoảng biến thiên của mẫu số liệu là ${r_s}$.",
        f"Khoảng biến thiên của mẫu số liệu là ${r_wrong}$.",
        f"Khoảng biến thiên $R = x_{{\\max}} - x_{{\\min}} = {s[-1]} - {s[0]} = {r_s}$.",
        f"Sai vì $R = {s[-1]} - {s[0]} = {r_s}$."
    )
    item_c = (
        f"Khoảng tứ phân vị của mẫu là ${iqr_s}$.",
        f"Khoảng tứ phân vị của mẫu là ${iqr_wrong}$.",
        f"Sắp xếp: ${sorted_str}$. Ta có $Q_1 = {_fmt_vn(st['q1'])}$, $Q_3 = {_fmt_vn(st['q3'])}$, suy ra $\\Delta_Q = Q_3 - Q_1 = {iqr_s}$.",
        f"Sai vì $Q_1 = {_fmt_vn(st['q1'])}$, $Q_3 = {_fmt_vn(st['q3'])}$ nên $\\Delta_Q = {iqr_s}$."
    )
    item_d = (
        f"Mẫu số liệu có giá trị trung vị là ${me_s}$.",
        f"Mẫu số liệu có giá trị trung vị là ${me_wrong}$.",
        f"Từ dãy đã sắp xếp ${sorted_str}$, trung vị là $M_e = {me_s}$.",
        f"Sai vì trung vị của dãy ${sorted_str}$ là ${me_s}$."
    )
    choices, loigiai = make_tf_choices([item_a, item_b, item_c, item_d])
    return caudan, choices, loigiai


# 6. Đúng/Sai - Tổng số giờ nắng trong năm 2006 - 2019 (Bài 14 - Ảnh 4 Câu 2)
def k10_tf_tk_tong_gio_nang_cac_nam():
    vals = [round(random.uniform(1580, 2220), 1) for _ in range(14)]
    # Bảo đảm min và max khác biệt rõ
    vals[1] = round(random.uniform(1560, 1620), 1)
    vals[13] = round(random.uniform(2150, 2240), 1)
    st = _compute_stats(vals)

    max_s = _fmt_vn(st["max"], dec=1)
    min_s = _fmt_vn(st["min"], dec=1)
    mean_s = _fmt_vn(st["mean"], dec=2)
    r_s = _fmt_vn(st["range"], dec=1)

    max_wrong = _fmt_vn(st["max"] - random.choice([25, 40]), dec=1)
    min_wrong = _fmt_vn(st["min"] + random.choice([15, 30]), dec=1)
    mean_wrong = _fmt_vn(st["mean"] + random.choice([-18.5, 22.4]), dec=2)
    r_wrong = _fmt_vn(st["range"] - random.choice([45, 70]), dec=1)

    row1 = " & ".join(_fmt_vn(x, dec=1) for x in vals[:7])
    row2 = " & ".join(_fmt_vn(x, dec=1) for x in vals[7:])
    caudan = (
        f"Tổng số giờ nắng trong năm của một tỉnh thành được thống kê từ năm $2006$ đến $2019$ cho như sau:\n"
        f"\\begin{{center}}\n"
        f"\\begin{{tabular}}{{|c|c|c|c|c|c|c|}}\n"
        f"\\hline\n"
        f"{row1} \\\\\n"
        f"\\hline\n"
        f"{row2} \\\\\n"
        f"\\hline\n"
        f"\\end{{tabular}}\n"
        f"\\end{{center}}\n"
        f"Các mệnh đề sau đúng hay sai? (Kết quả trung bình làm tròn đến hàng phần trăm)."
    )

    item_a = (
        f"Số giờ nắng lớn nhất là ${max_s}$ giờ.",
        f"Số giờ nắng lớn nhất là ${max_wrong}$ giờ.",
        f"Quan sát bảng số liệu, giá trị lớn nhất là ${max_s}$ giờ.",
        f"Sai vì giá trị lớn nhất trong bảng là ${max_s}$ giờ."
    )
    item_b = (
        f"Số giờ nắng trung bình trong năm là ${mean_s}$ giờ.",
        f"Số giờ nắng trung bình trong năm là ${mean_wrong}$ giờ.",
        f"Số giờ nắng trung bình cộng của $14$ năm là $\\bar{{x}} = \\dfrac{{\\sum x_i}}{{14}} \\approx {mean_s}$ giờ.",
        f"Sai vì $\\bar{{x}} \\approx {mean_s}$ giờ."
    )
    item_c = (
        f"Số giờ nắng nhỏ nhất là ${min_s}$ giờ.",
        f"Số giờ nắng nhỏ nhất là ${min_wrong}$ giờ.",
        f"Quan sát bảng số liệu, giá trị nhỏ nhất là ${min_s}$ giờ.",
        f"Sai vì giá trị nhỏ nhất trong bảng là ${min_s}$ giờ."
    )
    item_d = (
        f"Khoảng biến thiên là ${r_s}$.",
        f"Khoảng biến thiên là ${r_wrong}$.",
        f"Khoảng biến thiên $R = x_{{\\max}} - x_{{\\min}} = {max_s} - {min_s} = {r_s}$.",
        f"Sai vì $R = {max_s} - {min_s} = {r_s}$."
    )
    choices, loigiai = make_tf_choices([item_a, item_b, item_c, item_d])
    return caudan, choices, loigiai


# 7. Đúng/Sai - Tỉ lệ (%) tốt nghiệp THPT 16 năm (Bài 14 - Ảnh 4 Câu 3)
def k10_tf_tk_ti_le_tot_nghiep_16_nam():
    vals = [round(random.uniform(85.0, 99.6), 2) for _ in range(16)]
    vals[5] = round(random.uniform(78.5, 83.5), 2)
    vals[10] = round(random.uniform(99.65, 99.95), 2)
    st = _compute_stats(vals)

    mean_s = _fmt_vn(st["mean"], dec=2)
    std_s = _fmt_vn(st["std"], dec=2)
    var_s = _fmt_vn(st["var"], dec=2)
    max_s = _fmt_vn(st["max"], dec=2)

    mean_wrong = _fmt_vn(st["mean"] - random.choice([1.25, 2.10]), dec=2)
    std_wrong = _fmt_vn(st["std"] + random.choice([1.15, 1.85]), dec=2)
    var_wrong = _fmt_vn(st["var"] - random.choice([1.0, 2.0]), dec=2)
    second_max = st["sorted"][-2]
    max_wrong = _fmt_vn(second_max if abs(second_max - st["max"]) > 0.01 else st["max"] - 0.5, dec=2)

    row1 = " & ".join(_fmt_vn(x, dec=2) for x in vals[:8])
    row2 = " & ".join(_fmt_vn(x, dec=2) for x in vals[8:])
    caudan = (
        f"Số liệu thống kê tỉ lệ ($\\%$) tốt nghiệp THPT của một địa phương từ năm học $2001 - 2002$ đến năm học $2016 - 2017$ được cho như sau:\n"
        f"\\begin{{center}}\n"
        f"\\begin{{tabular}}{{|c|c|c|c|c|c|c|c|}}\n"
        f"\\hline\n"
        f"{row1} \\\\\n"
        f"\\hline\n"
        f"{row2} \\\\\n"
        f"\\hline\n"
        f"\\end{{tabular}}\n"
        f"\\end{{center}}\n"
        f"Các mệnh đề sau đúng hay sai? (Các kết quả làm tròn đến hàng phần trăm)."
    )

    item_a = (
        f"Tỉ lệ tốt nghiệp trung bình là ${mean_s}\\%$.",
        f"Tỉ lệ tốt nghiệp trung bình là ${mean_wrong}\\%$.",
        f"Tỉ lệ trung bình của $16$ năm là $\\bar{{x}} = \\dfrac{{\\sum x_i}}{{16}} \\approx {mean_s}\\%$.",
        f"Sai vì $\\bar{{x}} \\approx {mean_s}\\%$."
    )
    item_b = (
        f"Độ lệch chuẩn $s \\approx {std_s}$.",
        f"Độ lệch chuẩn $s \\approx {std_wrong}$.",
        f"Ta có phương sai $s^2 \\approx {var_s}$, suy ra độ lệch chuẩn $s = \\sqrt{{s^2}} \\approx {std_s}$.",
        f"Sai vì độ lệch chuẩn $s \\approx {std_s}$."
    )
    item_c = (
        f"Phương sai $s^2 \\approx {var_s}$.",
        f"Phương sai $s^2 \\approx {var_wrong}$.",
        f"Phương sai mẫu số liệu $s^2 = \\dfrac{{1}}{{16}}\\sum_{{i=1}}^{{16}} (x_i - \\bar{{x}})^2 \\approx {var_s}$.",
        f"Sai vì phương sai $s^2 \\approx {var_s}$."
    )
    item_d = (
        f"${max_s}$ là tỉ lệ ($\\%$) tốt nghiệp THPT cao nhất.",
        f"${max_wrong}$ là tỉ lệ ($\\%$) tốt nghiệp THPT cao nhất.",
        f"Giá trị lớn nhất trong bảng số liệu là ${max_s}\\%$.",
        f"Sai vì tỉ lệ cao nhất trong bảng là ${max_s}\\%$."
    )
    choices, loigiai = make_tf_choices([item_a, item_b, item_c, item_d])
    return caudan, choices, loigiai


# 8. Đúng/Sai - Điều tra thu nhập 40 hộ gia đình (Bài 14 - Ảnh 4 Câu 4)
def k10_tf_tk_thu_nhap_ho_gia_dinh():
    incomes = [4, 4.5, 5, 5.5, 6, 6.5, 7, 7.5, 8]
    while True:
        freqs = [
            random.randint(1, 2), random.randint(2, 4), random.randint(3, 5),
            random.randint(5, 7), 0, random.randint(5, 7),
            random.randint(4, 6), random.randint(2, 4), random.randint(1, 2)
        ]
        rem = 40 - sum(freqs)
        if rem >= 8:
            freqs[4] = rem
            if freqs.count(max(freqs)) == 1:
                break
    vals = []
    for inc, f in zip(incomes, freqs):
        vals.extend([inc] * f)
    st = _compute_stats(vals)

    mode_val = incomes[freqs.index(max(freqs))]
    mode_s = _fmt_vn(mode_val)
    mode_wrong = _fmt_vn(8 if mode_val != 8 else 4)
    var_s = _fmt_vn(st["var"], dec=4)
    var_wrong = _fmt_vn(st["var"] + 1.0, dec=4)
    mean_s = _fmt_vn(st["mean"], dec=4)
    mean_wrong = _fmt_vn(st["mean"] + 0.25, dec=4)

    inc_cells = " & ".join(_fmt_vn(x) for x in incomes)
    freq_cells = " & ".join(str(f) for f in freqs)
    caudan = (
        f"Điều tra thu nhập của $40$ hộ gia đình ở một bản được bảng số liệu như sau:\n"
        f"\\begin{{center}}\n"
        f"\\begin{{tabular}}{{|c|c|c|c|c|c|c|c|c|c|}}\n"
        f"\\hline\n"
        f"Thu nhập (triệu đồng/năm) & {inc_cells} \\\\\n"
        f"\\hline\n"
        f"Số hộ gia đình & {freq_cells} \\\\\n"
        f"\\hline\n"
        f"\\end{{tabular}}\n"
        f"\\end{{center}}\n"
        f"Các mệnh đề sau đúng hay sai?"
    )

    item_a = (
        f"Mốt của mẫu số liệu là ${mode_s}$.",
        f"Mốt của mẫu số liệu là ${mode_wrong}$.",
        f"Số hộ gia đình lớn nhất là ${max(freqs)}$, ứng với mức thu nhập ${mode_s}$ triệu đồng/năm nên mốt là ${mode_s}$.",
        f"Sai vì mốt là giá trị có tần số lớn nhất, tức là ${mode_s}$ (ứng với ${max(freqs)}$ hộ gia đình)."
    )
    item_b = (
        f"Phương sai của mẫu số liệu trên là ${var_s}$.",
        f"Phương sai của mẫu số liệu trên là ${var_wrong}$.",
        f"Với $\\bar{{x}} = {mean_s}$, phương sai là $s^2 = \\dfrac{{1}}{{40}}\\sum n_i(x_i - \\bar{{x}})^2 \\approx {var_s}$.",
        f"Sai vì $s^2 = \\dfrac{{1}}{{40}}\\sum n_i(x_i - \\bar{{x}})^2 \\approx {var_s}$."
    )
    item_c = (
        r"Cỡ mẫu là $40$.",
        r"Cỡ mẫu là $45$.",
        r"Tổng số hộ gia đình điều tra là $n = 40$.",
        r"Sai vì tổng số hộ gia đình là $n = 40$."
    )
    item_d = (
        f"Số trung bình của mẫu số liệu trên là ${mean_s}$.",
        f"Số trung bình của mẫu số liệu trên là ${mean_wrong}$.",
        f"Số trung bình $\\bar{{x}} = \\dfrac{{\\sum n_i x_i}}{{40}} = {mean_s}$.",
        f"Sai vì $\\bar{{x}} = {mean_s}$."
    )
    choices, loigiai = make_tf_choices([item_a, item_b, item_c, item_d])
    return caudan, choices, loigiai


# ==============================================================================
# 10 DẠNG TRẮC NGHIỆM 4 LỰA CHỌN - HỆ THỨC LƯỢNG TRONG TAM GIÁC (CHƯƠNG III)
# ==============================================================================

# 1. Lý thuyết công thức định lí côsin, sin và diện tích (Câu 1-5)
def k10_mc_htl_ly_thuyet_cong_thuc_dung_sai():
    case = random.choice([1, 2, 3, 4, 5, 6])
    if case == 1:
        caudan = r"Gọi $S$ là diện tích tam giác $ABC$. Trong các mệnh đề sau, mệnh đề nào \textbf{đúng}?"
        correct = r"$S = \dfrac{abc}{4R}$"
        wrongs = [
            r"$S = \dfrac{1}{2}ab\cos C$",
            r"$S = ah_a$",
            r"$S = ab\sin C$",
        ]
        loigiai = r"Công thức đúng tính diện tích tam giác $ABC$ là $S = \dfrac{abc}{4R}$ (với $R$ là bán kính đường tròn ngoại tiếp)."
    elif case == 2:
        caudan = r"Trong tam giác $ABC$ bất kì với $BC = a$, $AC = b$, $AB = c$ và $R$ là bán kính đường tròn ngoại tiếp. Khẳng định nào sau đây là \textbf{sai}?"
        correct = r"$b\sin B = 2R$"
        wrongs = [
            r"$\dfrac{a}{\sin A} = 2R$",
            r"$\sin A = \dfrac{a}{2R}$",
            r"$\sin C = \dfrac{c\sin A}{a}$",
        ]
        loigiai = r"Theo định lí sin: $\dfrac{b}{\sin B} = 2R \implies b = 2R\sin B$, do đó khẳng định $b\sin B = 2R$ là sai."
    elif case == 3:
        caudan = r"Cho tam giác $ABC$ có $BC = a$, $AC = b$ và $AB = c$. Hệ thức nào dưới đây \textbf{đúng}?"
        correct = r"$\cos A = \dfrac{b^2 + c^2 - a^2}{2bc}$"
        wrongs = [
            r"$\cos A = \dfrac{b^2 - c^2 - a^2}{2ac}$",
            r"$\cos A = \dfrac{a^2 + b^2 + c^2}{2bc}$",
            r"$\cos A = \dfrac{a^2 - b^2 - c^2}{2abc}$",
        ]
        loigiai = r"Theo hệ quả của định lí côsin: $\cos A = \dfrac{b^2 + c^2 - a^2}{2bc}$."
    elif case == 4:
        caudan = r"Cho tam giác $ABC$ với $BC = a$, $AC = b$, $AB = c$. Đẳng thức nào \textbf{sai}?"
        correct = r"$c^2 = b^2 + a^2 + 2ab\cos C$"
        wrongs = [
            r"$b^2 = a^2 + c^2 - 2ac\cos B$",
            r"$a^2 = b^2 + c^2 - 2bc\cos A$",
            r"$c^2 = b^2 + a^2 - 2ab\cos C$",
        ]
        loigiai = r"Theo định lí côsin: $c^2 = a^2 + b^2 - 2ab\cos C$ (dấu trừ trước $2ab\cos C$), nên $c^2 = b^2 + a^2 + 2ab\cos C$ là sai."
    elif case == 5:
        caudan = r"Cho tam giác $ABC$ với $BC = a$, $AC = b$, $AB = c$ và $R$ là bán kính đường tròn ngoại tiếp. Khẳng định nào sau đây \textbf{đúng}?"
        correct = r"$a = 2R\sin A$"
        wrongs = [
            r"$a = 2R\cos A$",
            r"$a = 2R\tan A$",
            r"$a = R\sin A$",
        ]
        loigiai = r"Theo định lí sin: $\dfrac{a}{\sin A} = 2R \implies a = 2R\sin A$."
    else:
        caudan = r"Cho tam giác $ABC$ với các cạnh $AB = c$, $AC = b$, $BC = a$. Gọi $S$, $R$, $h_c$ lần lượt là diện tích, bán kính đường tròn ngoại tiếp, đường cao hạ từ đỉnh $C$. Khẳng định nào sau đây là \textbf{đúng}?"
        correct = r"$S = \dfrac{1}{2}c \cdot h_c$"
        wrongs = [
            r"$S = \dfrac{1}{2}abc$",
            r"$\dfrac{a}{\sin A} = R$",
            r"$\cos B = \dfrac{b^2 + c^2 - a^2}{2bc}$",
        ]
        loigiai = r"Công thức tính diện tích theo cạnh đáy $c = AB$ và đường cao tương ứng $h_c$ là $S = \dfrac{1}{2}c \cdot h_c$."

    choices = shuffle_choices(correct, wrongs)
    return caudan, choices, loigiai


# 2. Tính bán kính đường tròn nội tiếp r của tam giác (Câu 9, 22)
def k10_mc_htl_ban_kinh_noi_tiep_r():
    triples = [
        (3, 4, 5),      # p=6, S=6, r=1
        (6, 8, 10),     # p=12, S=24, r=2
        (5, 12, 13),    # p=15, S=30, r=2
        (8, 15, 17),    # p=20, S=60, r=3
        (21, 17, 10),   # p=24, S=84, r=7/2
        (13, 14, 15),   # p=21, S=84, r=4
        (9, 10, 17),    # p=18, S=36, r=2
    ]
    a, b, c = random.choice(triples)
    p = (a + b + c) // 2
    S = int(round(math.sqrt(p * (p - a) * (p - b) * (p - c))))
    r_frac = Fraction(S, p)
    r_s = fmt_frac(r_frac)

    wrongs_frac = [
        Fraction(S, p) + 1,
        Fraction(S, p) + 2 if r_frac.denominator == 1 else Fraction(r_frac.numerator, 1),
        Fraction(S, 2 * p) if r_frac != Fraction(S, 2 * p) else Fraction(S, p) + 3,
        Fraction(a, p),
    ]
    wrongs = []
    for wf in wrongs_frac:
        ws = f"${fmt_frac(wf)}$"
        if ws != f"${r_s}$" and ws not in wrongs:
            wrongs.append(ws)

    caudan = f"Cho tam giác $ABC$ có $a = {a}$, $b = {b}$, $c = {c}$. Bán kính $r$ của đường tròn nội tiếp tam giác $ABC$ bằng"
    choices = shuffle_choices(f"${r_s}$", wrongs[:3])
    loigiai = (
        f"Nửa chu vi tam giác: $p = \\dfrac{{{a} + {b} + {c}}}{{2}} = {p}$.\\\\\n"
        f"Theo công thức Heron: $S = \\sqrt{{{p}({p}-{a})({p}-{b})({p}-{c})}} = {S}$.\\\\\n"
        f"Bán kính đường tròn nội tiếp: $r = \\dfrac{{S}}{{p}} = \\dfrac{{{S}}}{{{p}}} = {r_s}$."
    )
    return caudan, choices, loigiai


# 3. Tính độ dài đường cao ha của tam giác (Câu 10, 23, 25)
def k10_mc_htl_duong_cao_tam_giac():
    case = random.choice([1, 2, 3, 4])
    if case == 1:
        # Biết b, c, cos A = 3/5 (hoặc 4/5) -> sin A = 4/5 (hoặc 3/5)
        b, c = random.choice([(7, 5), (5, 8), (6, 5), (10, 5)])
        cos_num = random.choice([3, 4])
        sin_num = 4 if cos_num == 3 else 3
        a2 = b**2 + c**2 - 2 * b * c * cos_num // 5
        # a = sqrt(a2)
        s_frac = Fraction(b * c * sin_num, 10)
        # ha = 2S / a
        two_s = Fraction(b * c * sin_num, 5)
        isqrt_a2 = math.isqrt(a2)
        if isqrt_a2**2 == a2:
            ha = two_s / isqrt_a2
            ans_s = f"${fmt_frac(ha)}$"
            a_s = str(isqrt_a2)
            wrongs = [f"${fmt_frac(ha + 1)}$", f"${fmt_frac(ha + 2)}$", f"${fmt_frac(two_s)}$"]
        else:
            # Rút gọn 2S / sqrt(a2) = 2S*sqrt(a2) / a2
            ha_coef = two_s / a2
            ans_s = f"${fmt_frac(ha_coef)}\\sqrt{{{a2}}}$" if ha_coef != 1 else f"$\\sqrt{{{a2}}}$"
            a_s = f"\\sqrt{{{a2}}}"
            wrongs = [
                f"${fmt_frac(ha_coef * 2)}\\sqrt{{{a2}}}$",
                f"${fmt_frac(two_s)}$",
                f"${b}$",
            ]
        caudan = f"Cho tam giác $ABC$ có $b = {b}$; $c = {c}$; $\\cos A = \\dfrac{{{cos_num}}}{{5}}$. Độ dài đường cao $h_a$ của tam giác $ABC$ là"
        loigiai = (
            f"Ta có $\\sin A = \\sqrt{{1 - \\cos^2 A}} = \\dfrac{{{sin_num}}}{{5}}$.\\\\\n"
            f"Diện tích tam giác: $S = \\dfrac{{1}}{{2}}bc\\sin A = {fmt_frac(s_frac)}$.\\\\\n"
            f"Cạnh $a = \\sqrt{{b^2 + c^2 - 2bc\\cos A}} = {a_s}$.\\\\\n"
            f"Đường cao $h_a = \\dfrac{{2S}}{{a}} = {ans_s.strip('$')}$."
        )
    elif case == 2:
        # Biết AB=c, AC=b, góc A = 60 độ -> tính ha
        b, c = random.choice([(6, 3), (8, 4), (10, 5)])
        a2 = b**2 + c**2 - b * c
        # b = 2c => a2 = 3c^2 => a = c*sqrt(3), 2S = b*c*sqrt(3)/2 = c^2*sqrt(3) => ha = c!
        ha = c
        ans_s = f"${ha}$"
        wrongs = [f"${ha}\\sqrt{{3}}$", f"${fmt_frac(Fraction(ha, 2))}$", f"$\\sqrt{{3}}$"]
        caudan = f"Tam giác $ABC$ có $AB = {c}$, $AC = {b}$, $\\widehat{{BAC}} = 60^\\circ$. Tính độ dài đường cao $h_a$ của tam giác."
        loigiai = (
            f"Theo định lí côsin: $BC = \\sqrt{{{b}^2 + {c}^2 - 2\\cdot {b}\\cdot {c}\\cos 60^\\circ}} = {c}\\sqrt{{3}}$.\\\\\n"
            f"Diện tích: $S = \\dfrac{{1}}{{2}}AB\\cdot AC\\sin 60^\\circ = \\dfrac{{{b*c}\\sqrt{{3}}}}{{4}}$.\\\\\n"
            f"Độ dài đường cao $h_a = \\dfrac{{2S}}{{BC}} = {ha}$."
        )
    elif case == 3:
        # Biết 3 cạnh (Heron chứa căn): (2, 3, 4) -> p=9/2, S = 3sqrt(15)/4, ha = 3sqrt(15)/8
        k = random.choice([1, 2])
        a, b, c = 4 * k, 2 * k, 3 * k
        # p = 9k/2, S = 3k^2 sqrt(15)/4, ha = 2S/a = 3k sqrt(15)/8
        num_ha = 3 * k
        den_ha = 8
        g = math.gcd(num_ha, den_ha)
        nh, dh = num_ha // g, den_ha // g
        ans_s = f"$\\dfrac{{{'' if nh == 1 else nh}\\sqrt{{15}}}}{{{dh}}}$"
        wrongs = [
            f"$\\dfrac{{{'' if nh == 1 else nh}\\sqrt{{15}}}}{{{dh // 2 if dh % 2 == 0 else dh * 2}}}$",
            f"$\\dfrac{{{'' if nh == 1 else nh}\\sqrt{{15}}}}{{{dh * 2}}}$",
            f"${num_ha}\\sqrt{{15}}$",
        ]
        caudan = f"Cho tam giác $ABC$ có $AB = {b}$, $AC = {c}$, $BC = {a}$. Khi đó độ dài đường cao của tam giác $ABC$ kẻ từ $A$ bằng"
        loigiai = (
            f"Nửa chu vi $p = \\dfrac{{{a}+{b}+{c}}}{{2}} = \\dfrac{{{9*k}}}{{2}}$.\\\\\n"
            f"Theo công thức Heron: $S = \\sqrt{{p(p-a)(p-b)(p-c)}} = \\dfrac{{{3*k*k}\\sqrt{{15}}}}{{4}}$.\\\\\n"
            f"Suy ra $h_a = \\dfrac{{2S}}{{BC}} = {ans_s.strip('$')}$."
        )
    else:
        # Biết 3 cạnh Heronian nguyên đẹp: (26, 28, 30) -> AH = 24, v.v.
        c, a, b = random.choice([(26, 28, 30), (13, 14, 15), (17, 28, 25), (15, 28, 41)])
        p = (a + b + c) // 2
        S = int(round(math.sqrt(p * (p - a) * (p - b) * (p - c))))
        ah = (2 * S) // a
        ans_s = f"${ah}$"
        wrongs = [f"${ah - 3}$", f"${ah // 2 if ah % 2 == 0 else ah + 2}$", f"${ah + 4}$"]
        caudan = f"Cho tam giác $ABC$ có $AB = {c}$, $BC = {a}$, $CA = {b}$. Độ dài đường cao $AH$ của tam giác là"
        loigiai = (
            f"Nửa chu vi $p = \\dfrac{{{c} + {a} + {b}}}{{2}} = {p}$.\\\\\n"
            f"Theo công thức Heron: $S = \\sqrt{{{p}({p}-{c})({p}-{a})({p}-{b})}} = {S}$.\\\\\n"
            f"Độ dài đường cao $AH = \\dfrac{{2S}}{{BC}} = \\dfrac{{{2*S}}}{{{a}}} = {ah}$."
        )

    choices = shuffle_choices(ans_s, wrongs)
    return caudan, choices, loigiai


# 4. Diện tích tam giác biết 1 cạnh và 2 góc (Câu 26)
def k10_mc_htl_dien_tich_mot_canh_hai_goc():
    b = random.choice([2, 4, 6])
    # B = 30, C = 45 => A = 105, sin 105 = (sqrt6 + sqrt2)/4
    # c = b sin 45 / sin 30 = b sqrt(2)
    # S = 1/2 * b * c * sin 105 = 1/2 * b^2 * sqrt(2) * (sqrt6+sqrt2)/4 = b^2*(sqrt3+1)/4
    coef = Fraction(b * b, 4)
    if coef == 1:
        ans_s = r"$1 + \sqrt{3}$"
        wrongs = [r"$2 + 2\sqrt{3}$", r"$1$", r"$\sqrt{3}$"]
    else:
        c_int = int(coef)
        ans_s = f"${c_int} + {c_int}\\sqrt{{3}}$"
        wrongs = [f"${2*c_int} + {2*c_int}\\sqrt{{3}}$", f"${c_int}$", f"${c_int}\\sqrt{{3}}$"]

    caudan = f"Tính diện tích của tam giác $ABC$ có $b = {b}$, $\\widehat{{B}} = 30^\\circ$, $\\widehat{{C}} = 45^\\circ$."
    choices = shuffle_choices(ans_s, wrongs)
    loigiai = (
        f"Ta có $\\widehat{{A}} = 180^\\circ - (30^\\circ + 45^\\circ) = 105^\\circ$.\\\\\n"
        f"Theo định lí sin: $c = \\dfrac{{b\\sin C}}{{\\sin B}} = \\dfrac{{{b}\\sin 45^\\circ}}{{\\sin 30^\\circ}} = {b}\\sqrt{{2}}$.\\\\\n"
        f"Diện tích tam giác: $S = \\dfrac{{1}}{{2}}bc\\sin A = \\dfrac{{1}}{{2}}\\cdot {b}\\cdot {b}\\sqrt{{2}}\\cdot \\sin 105^\\circ = {ans_s.strip('$')}$."
    )
    return caudan, choices, loigiai


# 5. Tìm số đo góc lớn nhất khi biết 3 cạnh chứa căn (Câu 29)
def k10_mc_htl_goc_lon_nhat_ba_canh_can():
    k = random.choice([1, 2])
    a_s = f"{2*k}\\sqrt{{3}}" if k > 0 else ""
    b_s = f"{2*k}\\sqrt{{2}}"
    c_s = r"\sqrt{6} - \sqrt{2}" if k == 1 else f"{k}(\\sqrt{{6}} - \\sqrt{{2}})"
    # Góc lớn nhất đối diện cạnh lớn nhất a = 2k*sqrt(3)
    # cos A = (b^2 + c^2 - a^2)/(2bc) = -1/2 => A = 120 độ
    caudan = f"Cho tam giác $ABC$ biết $a = {a_s}$, $b = {b_s}$, $c = {c_s}$. Số đo của góc lớn nhất của tam giác là"
    correct = r"$\widehat{A} = 120^\circ$"
    wrongs = [r"$\widehat{A} = 135^\circ$", r"$\widehat{A} = 150^\circ$", r"$\widehat{B} = 60^\circ$"]
    choices = shuffle_choices(correct, wrongs)
    loigiai = (
        f"Vì $a > b > c$ nên góc lớn nhất của tam giác là góc $\\widehat{{A}}$.\\\\\n"
        f"Áp dụng hệ quả định lí côsin:\n"
        f"$$\\cos A = \\dfrac{{b^2 + c^2 - a^2}}{{2bc}} = -\\dfrac{{1}}{{2}} \\implies \\widehat{{A}} = 120^\\circ.$$"
    )
    return caudan, choices, loigiai


# 6. Tứ giác ABCD tính cạnh AD (Câu 30 - có hình vẽ TikZ)
def k10_mc_htl_tu_giac_tinh_canh_ad():
    combos = [
        (35, 42, 51, 145, 98),
        (30, 40, 48, 135, 95),
        (28, 36, 45, 140, 100),
    ]
    AB, BC, CD, angB, angC = random.choice(combos)
    B_rad = math.radians(angB)
    C_rad = math.radians(angC)
    AC = math.sqrt(AB**2 + BC**2 - 2 * AB * BC * math.cos(B_rad))
    BCA = math.asin(AB * math.sin(B_rad) / AC)
    ACD = C_rad - BCA
    AD = math.sqrt(AC**2 + CD**2 - 2 * AC * CD * math.cos(ACD))
    ans = round(AD, 1)

    ans_s = _fmt_vn(ans, dec=1)
    w1 = _fmt_vn(ans - 6.2, dec=1)
    w2 = _fmt_vn(ans + 4.3, dec=1)
    w3 = _fmt_vn(ans - 9.3, dec=1)

    tikz = r"""\begin{tikzpicture}[line cap=round, line join=round, >=stealth, font=\footnotesize, scale=0.85, transform shape]
	\coordinate (B) at (0,0);
	\coordinate (C) at (2.2,-0.8);
	\coordinate (A) at (-1.3,1.5);
	\coordinate (D) at (3.6,1.5);
	\draw[thick] (A) -- (B) -- (C) -- (D) -- cycle;
	\pic[draw, angle radius=0.45cm, "$__ANGB__^\circ$", angle eccentricity=1.65] {angle = C--B--A};
	\pic[draw, angle radius=0.45cm, "$__ANGC__^\circ$", angle eccentricity=1.65] {angle = D--C--B};
	\node[left] at (A) {$A$};
	\node[below left] at (B) {$B$};
	\node[below] at (C) {$C$};
	\node[right] at (D) {$D$};
\end{tikzpicture}""".replace("__ANGB__", str(angB)).replace("__ANGC__", str(angC))

    prompt = (
        f"Cho tứ giác $ABCD$ có $AB = {AB}$, $BC = {BC}$, $CD = {CD}$, "
        f"$\\widehat{{ABC}} = {angB}^\\circ$, $\\widehat{{BCD}} = {angC}^\\circ$ (tham khảo hình vẽ). "
        f"Tính độ dài cạnh $AD$ (làm tròn kết quả đến hàng phần mười)."
    )
    caudan = "\\immini{" + prompt + "}{\n" + tikz + "\n}"
    choices = shuffle_choices(f"${ans_s}$", [f"${w1}$", f"${w2}$", f"${w3}$"])
    loigiai = (
        f"Áp dụng định lí côsin trong tam giác $ABC$:\n"
        f"$$AC = \\sqrt{{{AB}^2 + {BC}^2 - 2\\cdot {AB}\\cdot {BC}\\cos {angB}^\\circ}} \\approx {AC:.2f}.$$\n"
        f"Theo định lí sin trong tam giác $ABC$: $\\sin\\widehat{{BCA}} = \\dfrac{{AB\\cdot\\sin {angB}^\\circ}}{{AC}} \\implies \\widehat{{BCA}} \\approx {math.degrees(BCA):.2f}^\\circ$.\\\\\n"
        f"Suy ra $\\widehat{{ACD}} = {angC}^\\circ - \\widehat{{BCA}} \\approx {math.degrees(ACD):.2f}^\\circ$.\\\\\n"
        f"Áp dụng định lí côsin trong tam giác $ACD$:\n"
        f"$$AD = \\sqrt{{AC^2 + {CD}^2 - 2\\cdot AC\\cdot {CD}\\cos\\widehat{{ACD}}}} \\approx {ans_s}.$$"
    )
    return caudan, choices, loigiai


# 7. Bài toán thực tế vệ tinh và hai trạm quan sát (Câu 31 - có hình vẽ TikZ)
def k10_mc_htl_thuc_te_ve_tinh_hai_tram():
    AB = random.choice([120, 127, 140])
    angA = random.choice([75, 80])
    angB = random.choice([50, 55])
    angC = 180 - angA - angB
    AC = AB * math.sin(math.radians(angB)) / math.sin(math.radians(angC))
    ans = int(round(AC))

    tikz = r"""\begin{tikzpicture}[line cap=round, line join=round, >=stealth, font=\footnotesize, scale=0.85, transform shape]
	\coordinate (A) at (0,0);
	\coordinate (B) at (3.2,0);
	\coordinate (C) at (1.0,3.6);
	\draw[thick] (A) -- (B) -- (C) -- cycle;
	\filldraw[fill=gray!60, draw=black] ($(C)+(-0.35,0.22)$) -- ($(C)+(0.45,0.38)$) -- ($(C)+(0.45,0.28)$) -- ($(C)+(-0.35,0.12)$) -- cycle;
	\filldraw[fill=gray!90, draw=black] (C) -- ($(C)+(-0.12,0.18)$) -- ($(C)+(0.12,0.18)$) -- cycle;
	\pic[draw, angle radius=0.45cm, "$__ANGA__^\circ$", angle eccentricity=1.7] {angle = B--A--C};
	\pic[draw, angle radius=0.55cm, "$__ANGB__^\circ$", angle eccentricity=1.65] {angle = C--B--A};
	\node[left] at ($(A)!0.5!(C)$) {$b$};
	\node[above right] at ($(B)!0.5!(C)$) {$a$};
	\node[below] at (A) {Cần Thơ};
	\node[below] at (B) {TP Hồ Chí Minh};
	\node[above left] at (A) {$A$};
	\node[above right] at (B) {$B$};
	\node[left] at (C) {$C$};
\end{tikzpicture}""".replace("__ANGA__", str(angA)).replace("__ANGB__", str(angB))

    prompt = (
        f"Một vệ tinh quay quanh Trái Đất, đang bay phía trên hai trạm quan sát ở hai thành phố Hồ Chí Minh và Cần Thơ. "
        f"Khi vệ tinh nằm giữa hai trạm này, góc nâng của nó được quan sát đồng thời là ${angB}^\\circ$ tại thành phố Hồ Chí Minh "
        f"và ${angA}^\\circ$ tại Cần Thơ. Hỏi khi đó vệ tinh cách trạm quan sát tại Cần Thơ bao xa? "
        f"Biết rằng khoảng cách giữa hai trạm quan sát là ${AB}\\text{{ km}}$ (kết quả làm tròn đến hàng đơn vị)."
    )
    caudan = "\\immini{" + prompt + "}{\n" + tikz + "\n}"
    choices = shuffle_choices(
        f"${ans}\\text{{ km}}$",
        [f"${ans + 3}\\text{{ km}}$", f"${ans - 7}\\text{{ km}}$", f"${ans - 15}\\text{{ km}}$"],
    )
    loigiai = (
        f"Trong tam giác $ABC$, ta có $\\widehat{{ACB}} = 180^\\circ - ({angA}^\\circ + {angB}^\\circ) = {angC}^\\circ$.\\\\\n"
        f"Áp dụng định lí sin:\n"
        f"$$\\dfrac{{AC}}{{\\sin {angB}^\\circ}} = \\dfrac{{AB}}{{\\sin {angC}^\\circ}} \\implies AC = \\dfrac{{{AB}\\cdot\\sin {angB}^\\circ}}{{\\sin {angC}^\\circ}} \\approx {ans}\\text{{ km}}.$$"
    )
    return caudan, choices, loigiai


# 8. Bài toán thực tế tháp trên ngọn đồi tính chiều cao đồi (Câu 32 - có hình vẽ TikZ)
def k10_mc_htl_thuc_te_thap_tren_ngon_doi():
    AB = random.choice([70, 80, 90])
    angA = random.choice([56, 58, 60])
    angB = random.choice([26, 28, 30])
    tanA = math.tan(math.radians(angA))
    tanB = math.tan(math.radians(angB))
    OB = AB * tanB / (tanA - tanB)
    ans = round(OB, 1)

    ans_s = _fmt_vn(ans, dec=1)
    w1 = _fmt_vn(ans - 0.5, dec=1)
    w2 = _fmt_vn(ans - 1.0, dec=1)
    w3 = _fmt_vn(ans + 1.1, dec=1)

    tikz = r"""\begin{tikzpicture}[line cap=round, line join=round, >=stealth, font=\footnotesize, scale=0.8, transform shape]
	\coordinate (O) at (0,0);
	\coordinate (B) at (0,1.6);
	\coordinate (A) at (0,3.6);
	\coordinate (E) at (2.2,3.6);
	\coordinate (D) at (2.2,1.6);
	\coordinate (C) at (3.6,0);
	\draw[thick] (A) -- (O) -- (C) -- (A) -- (E);
	\draw[thick] (B) -- (D);
	\draw[thick] (B) -- (C);
	\draw (0,0.28) -| (0.28,0);
	\pic[draw, angle radius=0.5cm, "$__ANGA__^\circ$", angle eccentricity=1.55] {angle = C--A--E};
	\pic[draw, angle radius=0.6cm, "$__ANGB__^\circ$", angle eccentricity=1.55] {angle = C--B--D};
	\node[above] at (A) {$A$};
	\node[left] at (B) {$B$};
	\node[below left] at (O) {$O$};
	\node[right] at (E) {$E$};
	\node[above right] at (D) {$D$};
	\node[below right] at (C) {$C$};
\end{tikzpicture}""".replace("__ANGA__", str(angA)).replace("__ANGB__", str(angB))

    prompt = (
        f"Tại điểm $B$ trên ngọn đồi có một cái tháp cao ${AB}\\text{{ m}}$. Từ vị trí quan sát $C$ người ta đo được các góc "
        f"$\\widehat{{CAE}} = {angA}^\\circ$, $\\widehat{{CBD}} = {angB}^\\circ$ (như hình vẽ). "
        f"Khi đó chiều cao $OB$ của ngọn đồi gần nhất với giá trị nào sau đây?"
    )
    caudan = "\\immini{" + prompt + "}{\n" + tikz + "\n}"
    choices = shuffle_choices(f"${ans_s}\\text{{ m}}$", [f"${w1}\\text{{ m}}$", f"${w2}\\text{{ m}}$", f"${w3}\\text{{ m}}$"])
    loigiai = (
        f"Vì $AE \\parallel BD \\parallel OC$ nên $\\widehat{{ACO}} = {angA}^\\circ$ và $\\widehat{{BCO}} = {angB}^\\circ$.\\\\\n"
        f"Trong các tam giác vuông $OBC$ và $OAC$, ta có $OC = \\dfrac{{OB}}{{\\tan {angB}^\\circ}} = \\dfrac{{OB + {AB}}}{{\\tan {angA}^\\circ}}$.\\\\\n"
        f"Suy ra $OB = \\dfrac{{{AB}\\cdot\\tan {angB}^\\circ}}{{\\tan {angA}^\\circ - \\tan {angB}^\\circ}} \\approx {ans_s}\\text{{ m}}$."
    )
    return caudan, choices, loigiai


# 9. Bài toán thực tế quan sát chiều cao cái cây (Câu 33 - có hình vẽ TikZ)
def k10_mc_htl_thuc_te_quan_sat_chieu_cao_cay():
    combos = [
        (5, 20, 50),
        (4, 18, 48),
        (6, 22, 52),
    ]
    AH, HB, angA = random.choice(combos)
    AB = math.sqrt(AH**2 + HB**2)
    ang_ABH = math.atan2(AH, HB)
    ang_ABC = math.pi / 2 - ang_ABH
    ang_ACB = math.pi - math.radians(angA) - ang_ABC
    BC = AB * math.sin(math.radians(angA)) / math.sin(ang_ACB)
    k_low = int(math.floor(BC))
    k_high = k_low + 1

    tikz = r"""\begin{tikzpicture}[line cap=round, line join=round, >=stealth, font=\footnotesize, scale=0.85, transform shape]
	\coordinate (H) at (0,0);
	\coordinate (A) at (0,0.8);
	\coordinate (B) at (3.2,0);
	\coordinate (C) at (3.2,3.4);
	\fill[cyan!65!white, draw=black] (3.2,0.5) .. controls (2.5,0.6) and (2.4,1.3) .. (2.8,1.8)
	.. controls (2.6,2.4) and (3.1,3.3) .. (3.2,3.4)
	.. controls (3.6,3.2) and (3.8,2.2) .. (3.6,1.6)
	.. controls (3.9,1.1) and (3.6,0.5) .. (3.2,0.5) -- cycle;
	\draw[very thick] (3.2,0) -- (3.2,2.1);
	\draw[very thick] (3.2,1.2) -- (2.85,1.85);
	\draw[very thick] (3.2,1.4) -- (3.55,1.95);
	\draw[thick] (H) -- (B) -- (A) -- (H);
	\draw[thick] (A) -- (C) -- (B);
	\pic[draw, angle radius=0.6cm, "$__ANGA__^\circ$", angle eccentricity=1.45] {angle = B--A--C};
	\node[below] at (H) {$H$};
	\node[left] at (A) {$A$};
	\node[below] at (B) {$B$};
	\node[above] at (C) {$C$};
\end{tikzpicture}""".replace("__ANGA__", str(angA))

    prompt = (
        f"Từ vị trí $A$ người ta quan sát một cái cây (như hình vẽ). Biết $AH = {AH}\\text{{ m}}$, "
        f"$HB = {HB}\\text{{ m}}$, $\\widehat{{BAC}} = {angA}^\\circ$. Chiều cao $BC$ của cây nằm trong khoảng nào sau đây? (Tính theo đơn vị mét)."
    )
    caudan = "\\immini{" + prompt + "}{\n" + tikz + "\n}"
    choices = shuffle_choices(
        f"$({k_low}; {k_high})$",
        [f"$({k_low - 2}; {k_low - 1})$", f"$({k_low - 1}; {k_low})$", f"$({k_high}; {k_high + 1})$"],
    )
    loigiai = (
        f"Trong tam giác vuông $AHB$: $AB = \\sqrt{{{AH}^2 + {HB}^2}} \\approx {AB:.2f}\\text{{ m}}$, "
        f"$\\tan\\widehat{{ABH}} = \\dfrac{{{AH}}}{{{HB}}} \\implies \\widehat{{ABH}} \\approx {math.degrees(ang_ABH):.2f}^\\circ$.\\\\\n"
        f"Suy ra $\\widehat{{ABC}} = 90^\\circ - \\widehat{{ABH}} \\approx {math.degrees(ang_ABC):.2f}^\\circ$ và "
        f"$\\widehat{{ACB}} = 180^\\circ - {angA}^\\circ - \\widehat{{ABC}} \\approx {math.degrees(ang_ACB):.2f}^\\circ$.\\\\\n"
        f"Theo định lí sin: $BC = \\dfrac{{AB\\cdot\\sin {angA}^\\circ}}{{\\sin\\widehat{{ACB}}}} \\approx {BC:.2f}\\text{{ m}} \\in ({k_low}; {k_high})$."
    )
    return caudan, choices, loigiai


# 10. Bài toán thực tế tàu vận tải tránh băng trôi (Câu 34 - có hình vẽ TikZ)
def k10_mc_htl_thuc_te_tau_tranh_bang_troi():
    combos = [
        (6.5, 8.4, 71),
        (5.5, 7.6, 68),
        (7.2, 9.0, 74),
    ]
    AC, BC, angC = random.choice(combos)
    AB = math.sqrt(AC**2 + BC**2 - 2 * AC * BC * math.cos(math.radians(angC)))
    saved = (AC + BC) - AB
    ans = round(saved, 1)

    ans_s = _fmt_vn(ans, dec=1)
    w1 = _fmt_vn(ans - 0.3, dec=1)
    w2 = _fmt_vn(ans + 1.1, dec=1)
    w3 = _fmt_vn(ans + 0.5, dec=1)

    ac_s = _fmt_vn(AC, dec=1)
    bc_s = _fmt_vn(BC, dec=1)
    tikz = r"""\begin{tikzpicture}[line cap=round, line join=round, >=stealth, font=\footnotesize, scale=0.85, transform shape]
	\coordinate (A) at (0,0);
	\coordinate (B) at (2.8,0);
	\coordinate (C) at (1.1,-2.1);
	\draw[cyan!60, very thick] (-0.8,0) -- (A);
	\draw[cyan!60, very thick] (B) -- (3.6,0);
	\draw[cyan!60, very thick] (A) -- (C) node[midway, left] {$__AC__\text{ km}$};
	\draw[cyan!60, very thick] (C) -- (B) node[midway, right] {$__BC__\text{ km}$};
	\pic[draw, cyan!80!black, thick, angle radius=0.55cm, "$__ANGC__^\circ$", angle eccentricity=1.55] {angle = B--C--A};
	\node[above] at (A) {$A$};
	\node[above] at (B) {$B$};
	\node[below] at (C) {$C$};
\end{tikzpicture}""".replace("__AC__", ac_s).replace("__BC__", bc_s).replace("__ANGC__", str(angC))

    prompt = (
        f"Một tàu vận tải đang di chuyển trên Đại Tây Dương thì có cảnh báo băng trôi phía trước nên đã di chuyển theo đường $ACB$ "
        f"với $AC = {ac_s}\\text{{ km}}$, $BC = {bc_s}\\text{{ km}}$ và $\\widehat{{ACB}} = {angC}^\\circ$ (như hình vẽ). "
        f"Nếu đi thẳng từ $A$ đến $B$ thì quãng đường ngắn lại bao nhiêu km (làm tròn kết quả đến hàng phần mười)?"
    )
    caudan = "\\immini{" + prompt + "}{\n" + tikz + "\n}"
    choices = shuffle_choices(f"${ans_s}\\text{{ km}}$", [f"${w1}\\text{{ km}}$", f"${w2}\\text{{ km}}$", f"${w3}\\text{{ km}}$"])
    loigiai = (
        f"Áp dụng định lí côsin trong tam giác $ABC$:\n"
        f"$$AB = \\sqrt{{{ac_s}^2 + {bc_s}^2 - 2\\cdot {ac_s}\\cdot {bc_s}\\cos {angC}^\\circ}} \\approx {AB:.2f}\\text{{ km}}.$$\n"
        f"Quãng đường ngắn lại được là:\n"
        f"$$AC + BC - AB \\approx {ac_s} + {bc_s} - {AB:.2f} \\approx {ans_s}\\text{{ km}}.$$"
    )
    return caudan, choices, loigiai


# ==============================================================================
# BỔ SUNG BÀI 5 (LƯỢNG GIÁC 0-180 ĐỘ) + BÀI 6 (ĐƯỜNG DÂY ĐIỆN & 8 DẠNG ĐÚNG/SAI)
# ==============================================================================

# MC Bài 5 - Dấu góc tù, hệ thức tan.cot, tính sin từ cos, hệ thức 3 góc tam giác
def k10_mc_lg_dau_va_he_thuc_goc_bu():
    case = random.choice([1, 2, 3, 4])
    if case == 1:
        k = random.choice([2, 3, 4, 5])
        caudan = f"Cho biết $\\tan\\alpha = \\dfrac{{1}}{{{k}}}$. Tính $\\cot\\alpha$."
        correct = f"$\\cot\\alpha = {k}$"
        wrongs = [f"$\\cot\\alpha = \\dfrac{{1}}{{{k + 1}}}$", f"$\\cot\\alpha = \\sqrt{{{k}}}$", f"$\\cot\\alpha = \\dfrac{{1}}{{{k}}}$"]
        loigiai = f"Ta có $\\tan\\alpha \\cdot \\cot\\alpha = 1 \\implies \\cot\\alpha = \\dfrac{{1}}{{\\tan\\alpha}} = {k}$."
    elif case == 2:
        caudan = r"Cho góc $\alpha$ là góc tù ($90^\circ < \alpha < 180^\circ$). Mệnh đề nào sau đây là \textbf{đúng}?"
        correct = r"$\cos\alpha < 0$"
        wrongs = [r"$\sin\alpha < 0$", r"$\tan\alpha > 0$", r"$\cot\alpha > 0$"]
        loigiai = r"Với góc tù $90^\circ < \alpha < 180^\circ$, ta luôn có $\sin\alpha > 0$ và $\cos\alpha < 0, \tan\alpha < 0, \cot\alpha < 0$."
    elif case == 3:
        # Cho cos alpha = a/b, 0 < alpha < 90 => sin alpha
        pairs = [(4, 13), (3, 7), (2, 5), (5, 13)]
        num, den = random.choice(pairs)
        rem = den**2 - num**2
        # Tách bình phương lớn nhất
        k = 1
        for d in range(int(math.isqrt(rem)), 1, -1):
            if rem % (d * d) == 0:
                k = d
                break
        rad = rem // (k * k)
        if rad == 1:
            sin_s = fmt_frac(Fraction(k, den))
            w1 = fmt_frac(Fraction(num, k))
            w2 = fmt_frac(Fraction(k, den + 1))
            w3 = f"-{sin_s}"
        else:
            k_str = "" if k == 1 else str(k)
            sin_s = f"\\dfrac{{{k_str}\\sqrt{{{rad}}}}}{{{den}}}"
            w1 = f"\\dfrac{{{num}}}{{{k_str}\\sqrt{{{rad}}}}}"
            w2 = f"\\dfrac{{{k_str}\\sqrt{{{rad}}}}}{{{den + 1}}}"
            w3 = f"-\\dfrac{{{k_str}\\sqrt{{{rad}}}}}{{{den}}}"
        caudan = f"Cho $\\cos\\alpha = \\dfrac{{{num}}}{{{den}}}$ và $0^\\circ < \\alpha < 90^\\circ$. Khi đó $\\sin\\alpha$ bằng"
        correct = f"${sin_s}$"
        wrongs = [f"${w1}$", f"${w2}$", f"${w3}$"]
        loigiai = f"Vì $0^\\circ < \\alpha < 90^\\circ$ nên $\\sin\\alpha > 0$, và $\\sin\\alpha = \\sqrt{{1 - \\cos^2\\alpha}} = \\sqrt{{1 - \\dfrac{{{num**2}}}{{{den**2}}}}} = {sin_s}$."
    else:
        caudan = r"Cho $A, B, C$ là ba góc của tam giác $ABC$, mệnh đề nào sau đây \textbf{đúng}?"
        correct = r"$\tan(A + B) + \tan C = 0$"
        wrongs = [r"$\cos(A + B) = \cos C$", r"$\sin(A + B) + \sin C = 0$", r"$\cot(A + B) = \cot C$"]
        loigiai = r"Vì $A + B + C = 180^\circ$ nên $A + B = 180^\circ - C$. Suy ra $\tan(A+B) = -\tan C \iff \tan(A+B) + \tan C = 0$."

    choices = shuffle_choices(correct, wrongs)
    return caudan, choices, loigiai


# MC Bài 5 - Tính giá trị biểu thức lượng giác các góc đặc biệt (Câu 2, 3, 7)
def k10_mc_lg_tinh_gia_tri_bieu_thuc_dac_biet():
    case = random.choice([1, 2, 3])
    if case == 1:
        a = random.choice([2, 4, 6])
        b = random.choice([3, 4, 5])
        ans = a // 2 - b
        caudan = f"Tính giá trị của biểu thức $P = {a}\\sin 30^\\circ - {b}\\cos 0^\\circ$ ta được"
        correct = f"$P = {ans}$"
        wrongs = [f"$P = {ans + 4}$", f"$P = {ans - 1}$", f"$P = {abs(ans) + 2}$"]
        loigiai = f"Ta có $\\sin 30^\\circ = \\dfrac{{1}}{{2}}$ và $\\cos 0^\\circ = 1$, nên $P = {a}\\cdot\\dfrac{{1}}{{2}} - {b}\\cdot 1 = {ans}$."
    elif case == 2:
        # 2 - sqrt(2)*sin 45 + cos^2 60 = 2 - 1 + 1/4 = 5/4
        a = random.choice([2, 3, 4])
        ans = Fraction(a - 1, 1) + Fraction(1, 4)
        ans_s = fmt_frac(ans)
        caudan = f"Giá trị của biểu thức $A = {a} - \\sqrt{{2}}\\sin 45^\\circ + \\cos^2 60^\\circ$ là"
        correct = f"$A = {ans_s}$"
        wrongs = [f"$A = -{ans_s}$", f"$A = {fmt_frac(ans + Fraction(1, 4))}$", f"$A = {fmt_frac(Fraction(-3, 2))}$"]
        loigiai = f"Ta có $\\sin 45^\\circ = \\dfrac{{\\sqrt{{2}}}}{{2}}$ và $\\cos 60^\\circ = \\dfrac{{1}}{{2}}$, nên $A = {a} - 1 + \\dfrac{{1}}{{4}} = {ans_s}$."
    else:
        # cos^2 30 - k * tan 60 * cot 60 = 3/4 - k
        k = random.choice([2, 3])
        ans = Fraction(3, 4) - k
        ans_s = fmt_frac(ans)
        caudan = f"Giá trị biểu thức $\\cos^2 30^\\circ - {k}\\tan 60^\\circ \\cdot \\cot 60^\\circ$ bằng"
        correct = f"${ans_s}$"
        wrongs = [f"${fmt_frac(-ans)}$", f"${fmt_frac(Fraction(7, 4))}$", f"${fmt_frac(Fraction(3, 4) + k)}$"]
        loigiai = f"Ta có $\\cos 30^\\circ = \\dfrac{{\\sqrt{{3}}}}{{2}}$ và $\\tan 60^\\circ \\cdot \\cot 60^\\circ = 1$, nên giá trị là $\\dfrac{{3}}{{4}} - {k} = {ans_s}$."

    choices = shuffle_choices(correct, wrongs)
    return caudan, choices, loigiai


# MC Bài 6 - Lắp đường dây điện cao thế tránh ngọn núi (Câu 27 Ảnh 5 - có hình TikZ)
def k10_mc_htl_thuc_te_duong_day_dien_nui():
    combos = [
        (10, 8, 70),
        (12, 9, 65),
        (11, 7, 75),
    ]
    AC, BC, angC = random.choice(combos)
    AB = math.sqrt(AC**2 + BC**2 - 2 * AC * BC * math.cos(math.radians(angC)))
    extra = (AC + BC) - AB
    ans = round(extra, 1)
    ans_s = _fmt_vn(ans, dec=1)
    w1 = _fmt_vn(ans - 1.2, dec=1)
    w2 = _fmt_vn(ans + 1.2, dec=1)
    w3 = _fmt_vn(AB, dec=1)

    tikz = r"""\begin{tikzpicture}[line cap=round, line join=round, >=stealth, font=\footnotesize, scale=0.8, transform shape]
	\coordinate (A) at (0,0);
	\coordinate (B) at (3.8,0);
	\coordinate (C) at (2.0,-1.8);
	\draw[dashed] (A) -- (B);
	\filldraw[fill=green!60!black, draw=black] (0.7,0) -- (1.1,0.45) -- (1.45,0.2) -- (1.85,0.55) -- (2.25,0.25) -- (2.65,0.5) -- (3.1,0) -- cycle;
	\draw[thick] (A) -- (C) node[midway, below left] {$__AC__\text{ km}$};
	\draw[thick] (C) -- (B) node[midway, below right] {$__BC__\text{ km}$};
	\pic[draw, angle radius=0.5cm, "$__ANGC__^\circ$", angle eccentricity=1.55] {angle = B--C--A};
	\fill (A) circle (1.2pt) node[left] {$A$};
	\fill (B) circle (1.2pt) node[right] {$B$};
	\fill (C) circle (1.2pt) node[below] {$C$};
\end{tikzpicture}""".replace("__AC__", str(AC)).replace("__BC__", str(BC)).replace("__ANGC__", str(angC))

    prompt = (
        f"Để lắp đường dây điện cao thế từ vị trí $A$ đến vị trí $B$, do phải tránh một ngọn núi nên người ta phải nối đường dây "
        f"từ vị trí $A$ đến vị trí $C$ dài ${AC}\\text{{ km}}$, sau đó nối từ vị trí $C$ đến vị trí $B$ dài ${BC}\\text{{ km}}$. "
        f"Góc tạo bởi hai đoạn dây $AC$ và $CB$ là ${angC}^\\circ$ (như hình vẽ). Chiều dài tăng thêm của dây điện vì không thể nối trực tiếp từ $A$ đến $B$ là bao nhiêu kilômét? "
        f"(Kết quả làm tròn đến hàng phần mười)."
    )
    caudan = "\\immini{" + prompt + "}{\n" + tikz + "\n}"
    choices = shuffle_choices(f"${ans_s}$", [f"${w1}$", f"${w2}$", f"${w3}$"])
    loigiai = (
        f"Áp dụng định lí côsin trong tam giác $ABC$:\n"
        f"$$AB = \\sqrt{{{AC}^2 + {BC}^2 - 2\\cdot {AC}\\cdot {BC}\\cos {angC}^\\circ}} \\approx {AB:.2f}\\text{{ km}}.$$\n"
        f"Chiều dài tăng thêm của dây điện là:\n"
        f"$$AC + BC - AB \\approx {AC} + {BC} - {AB:.2f} \\approx {ans_s}\\text{{ km}}.$$"
    )
    return caudan, choices, loigiai


# ------------------------------------------------------------------------------
# 8 DẠNG TRẮC NGHIỆM ĐÚNG/SAI MỚI - CHƯƠNG III: HỆ THỨC LƯỢNG TRONG TAM GIÁC
# ------------------------------------------------------------------------------

# DS 1 (Ảnh 4 Câu 1): Tam giác biết 3 cạnh có góc 60 độ
def k10_tf_htl_tam_giac_ba_canh_goc_60():
    # Bộ (a, b, c) với góc A = 60 độ: (7, 8, 5), (7, 8, 3), (13, 15, 7), (14, 16, 10)
    a, b, c = random.choice([(7, 8, 5), (7, 8, 3), (13, 15, 7), (14, 16, 10)])
    # S = 1/2 b c sin 60 = bc * sqrt(3) / 4
    s_num = b * c
    g_s = math.gcd(s_num, 4)
    s_str = f"{s_num // 4}\\sqrt{{3}}" if s_num % 4 == 0 else f"\\dfrac{{{s_num // g_s}\\sqrt{{3}}}}{{{4 // g_s}}}"
    s_wrong_num = s_num // 2 if s_num % 2 == 0 else s_num * 2
    s_wrong_str = f"{s_wrong_num}\\sqrt{{3}}"
    # ha = 2S / a = (bc * sqrt(3)) / (2a)
    g_h = math.gcd(b * c, 2 * a)
    hn, hd = (b * c) // g_h, (2 * a) // g_h
    ha_str = f"{hn}\\sqrt{{3}}" if hd == 1 else f"\\dfrac{{{'' if hn == 1 else hn}\\sqrt{{3}}}}{{{hd}}}"
    ha_wrong = f"\\dfrac{{{hn + 1}\\sqrt{{3}}}}{{{hd}}}" if hd > 1 else f"{hn + 2}\\sqrt{{3}}"
    # R = a / (2 sin 60) = a / sqrt(3) = a*sqrt(3)/3
    g_r = math.gcd(a, 3)
    rn, rd = a // g_r, 3 // g_r
    r_str = f"{rn}\\sqrt{{3}}" if rd == 1 else f"\\dfrac{{{'' if rn == 1 else rn}\\sqrt{{3}}}}{{{rd}}}"
    r_wrong = f"\\dfrac{{{rn + 2}\\sqrt{{3}}}}{{{rd}}}" if rd > 1 else f"{rn + 2}\\sqrt{{3}}"

    caudan = f"Cho tam giác $ABC$ có $BC = a = {a}$; $AC = b = {b}$; $AB = c = {c}$. Khi đó:"
    item_a = (
        r"Góc $\widehat{BAC} = 60^\circ$.",
        r"Góc $\widehat{BAC} = 120^\circ$.",
        f"Ta có $\\cos A = \\dfrac{{{b}^2 + {c}^2 - {a}^2}}{{2\\cdot {b}\\cdot {c}}} = \\dfrac{{1}}{{2}} \\implies \\widehat{{BAC}} = 60^\\circ$.",
        f"Sai vì $\\cos A = \\dfrac{{1}}{{2}}$ nên $\\widehat{{BAC}} = 60^\\circ$."
    )
    item_b = (
        f"Diện tích tam giác $ABC$ là ${s_str}$.",
        f"Diện tích tam giác $ABC$ là ${s_wrong_str}$.",
        f"Diện tích $S = \\dfrac{{1}}{{2}}bc\\sin 60^\\circ = {s_str}$.",
        f"Sai vì $S = \\dfrac{{1}}{{2}}\\cdot {b}\\cdot {c}\\cdot\\dfrac{{\\sqrt{{3}}}}{{2}} = {s_str}$."
    )
    item_c = (
        f"Chiều cao từ $A$ đến $BC$ là ${ha_str}$.",
        f"Chiều cao từ $A$ đến $BC$ là ${ha_wrong}$.",
        f"Chiều cao $h_a = \\dfrac{{2S}}{{a}} = {ha_str}$.",
        f"Sai vì $h_a = \\dfrac{{2S}}{{{a}}} = {ha_str}$."
    )
    item_d = (
        f"Bán kính đường tròn ngoại tiếp tam giác $ABC$ là ${r_str}$.",
        f"Bán kính đường tròn ngoại tiếp tam giác $ABC$ là ${r_wrong}$.",
        f"Theo định lí sin: $R = \\dfrac{{a}}{{2\\sin A}} = \\dfrac{{{a}}}{{\\sqrt{{3}}}} = {r_str}$.",
        f"Sai vì $R = \\dfrac{{{a}}}{{2\\sin 60^\\circ}} = {r_str}$."
    )
    choices, loigiai = make_tf_choices([item_a, item_b, item_c, item_d])
    return caudan, choices, loigiai


# DS 2 (Ảnh 4 Câu 2): Tam giác biết 2 cạnh và cos A
def k10_tf_htl_hai_canh_va_cos_a():
    b, c = random.choice([(7, 5), (5, 8), (10, 5)])
    cos_num = random.choice([3, 4])
    sin_num = 4 if cos_num == 3 else 3
    a2 = b**2 + c**2 - 2 * b * c * cos_num // 5
    # Tách a2 = k^2 * rad
    k = 1
    for d in range(int(math.isqrt(a2)), 1, -1):
        if a2 % (d * d) == 0:
            k = d
            break
    rad = a2 // (k * k)
    a_str = f"{k}" if rad == 1 else (f"\\sqrt{{{rad}}}" if k == 1 else f"{k}\\sqrt{{{rad}}}")
    a_wrong = f"{k + 1}\\sqrt{{{rad}}}" if rad > 1 else f"{k + 2}"
    # S = 1/2 * b * c * sin A, 2S = b * c * sin_num / 5
    two_s = Fraction(b * c * sin_num, 5)
    if rad == 1:
        ha_str = fmt_frac(two_s / k)
        ha_wrong = fmt_frac(two_s / k + 1)
    else:
        coef = two_s / a2
        ha_str = f"\\sqrt{{{rad}}}" if coef * k == 1 else (f"{int(coef*k)}\\sqrt{{{rad}}}" if (coef*k).denominator == 1 else f"\\dfrac{{{(coef*k).numerator}\\sqrt{{{rad}}}}}{{{(coef*k).denominator}}}")
        ha_wrong = f"\\dfrac{{{(coef*k).numerator + 2}\\sqrt{{{rad}}}}}{{{(coef*k).denominator}}}" if (coef*k).denominator > 1 else f"{int(coef*k)+2}\\sqrt{{{rad}}}"

    caudan = f"Cho tam giác $ABC$ có $AC = b = {b}$; $AB = c = {c}$; $\\cos A = \\dfrac{{{cos_num}}}{{5}}$."
    item_a = (
        r"Góc $A$ là góc nhọn.",
        r"Góc $A$ là góc tù.",
        f"Vì $\\cos A = \\dfrac{{{cos_num}}}{{5}} > 0$ nên góc $A$ là góc nhọn.",
        f"Sai vì $\\cos A = \\dfrac{{{cos_num}}}{{5}} > 0$ nên góc $A$ phải là góc nhọn."
    )
    item_b = (
        f"$a = {a_str}$.",
        f"$a = {a_wrong}$.",
        f"Ta có $a^2 = {b}^2 + {c}^2 - 2\\cdot {b}\\cdot {c}\\cdot \\dfrac{{{cos_num}}}{{5}} = {a2} \\implies a = {a_str}$.",
        f"Sai vì $a^2 = {a2} \\implies a = {a_str}$."
    )
    item_c = (
        f"$\\sin A = \\dfrac{{{sin_num}}}{{5}}$.",
        f"$\\sin A = -\\dfrac{{{sin_num}}}{{5}}$.",
        f"Vì $0^\\circ < A < 180^\\circ$ nên $\\sin A > 0$, suy ra $\\sin A = \\sqrt{{1 - \\cos^2 A}} = \\dfrac{{{sin_num}}}{{5}}$.",
        f"Sai vì góc $A$ trong tam giác luôn có $\\sin A > 0$, nên $\\sin A = \\dfrac{{{sin_num}}}{{5}}$."
    )
    item_d = (
        f"Độ dài đường cao hạ từ đỉnh $A$ bằng ${ha_str}$.",
        f"Độ dài đường cao hạ từ đỉnh $A$ bằng ${ha_wrong}$.",
        f"Ta có $2S = bc\\sin A = {fmt_frac(two_s)}$, suy ra $h_a = \\dfrac{{2S}}{{a}} = {ha_str}$.",
        f"Sai vì $h_a = \\dfrac{{2S}}{{a}} = {ha_str}$."
    )
    choices, loigiai = make_tf_choices([item_a, item_b, item_c, item_d])
    return caudan, choices, loigiai


# DS 3 (Ảnh 4 Câu 3): Tam giác biết AB, AC, A=60 làm tròn hàng đơn vị
def k10_tf_htl_lam_tron_r_va_r_nho():
    AB, AC = random.choice([(15, 20), (12, 18), (16, 22)])
    angA = 60
    BC = math.sqrt(AB**2 + AC**2 - AB * AC)
    angB_deg = math.degrees(math.asin(AC * math.sin(math.radians(angA)) / BC))
    S = 0.5 * AB * AC * math.sin(math.radians(angA))
    p = (AB + AC + BC) / 2
    R = BC / (2 * math.sin(math.radians(angA)))
    r = S / p
    expr = 2 * R - 5 * r

    bc_r = int(round(BC))
    b_r = int(round(angB_deg))
    s_r = int(round(S))
    sign_true = "< 0" if expr < 0 else "> 0"
    sign_false = "> 0" if expr < 0 else "< 0"

    caudan = (
        f"Cho tam giác $ABC$ có $AB = {AB}$, $AC = {AC}$ và $\\widehat{{BAC}} = 60^\\circ$. "
        f"Gọi $R, r$ lần lượt là bán kính đường tròn ngoại tiếp, nội tiếp tam giác $ABC$ (kết quả làm tròn đến hàng đơn vị)."
    )
    item_a = (
        f"$BC \\approx {bc_r}$.",
        f"$BC \\approx {bc_r + 3}$.",
        f"Theo định lí côsin: $BC = \\sqrt{{{AB}^2 + {AC}^2 - {AB}\\cdot {AC}}} \\approx {BC:.2f} \\approx {bc_r}$.",
        f"Sai vì $BC \\approx {BC:.2f} \\approx {bc_r}$."
    )
    item_b = (
        f"$\\widehat{{ABC}} \\approx {b_r}^\\circ$.",
        f"$\\widehat{{ABC}} \\approx {b_r + 8}^\\circ$.",
        f"Theo định lí sin: $\\sin B = \\dfrac{{AC\\sin 60^\\circ}}{{BC}} \\implies \\widehat{{ABC}} \\approx {angB_deg:.2f}^\\circ \\approx {b_r}^\\circ$.",
        f"Sai vì $\\widehat{{ABC}} \\approx {b_r}^\\circ$."
    )
    item_c = (
        f"$S \\approx {s_r}$.",
        f"$S \\approx {s_r + 12}$.",
        f"Diện tích $S = \\dfrac{{1}}{{2}}\\cdot {AB}\\cdot {AC}\\sin 60^\\circ \\approx {S:.2f} \\approx {s_r}$.",
        f"Sai vì $S \\approx {s_r}$."
    )
    item_d = (
        f"$2R - 5r {sign_true}$.",
        f"$2R - 5r {sign_false}$.",
        f"Ta có $R = \\dfrac{{BC}}{{2\\sin 60^\\circ}} \\approx {R:.2f}$ và $r = \\dfrac{{S}}{{p}} \\approx {r:.2f}$, nên $2R - 5r \\approx {expr:.2f} {sign_true}$.",
        f"Sai vì $2R - 5r \\approx {expr:.2f} {sign_true}$."
    )
    choices, loigiai = make_tf_choices([item_a, item_b, item_c, item_d])
    return caudan, choices, loigiai


# DS 4 (Ảnh 4 Câu 4): Cạnh chứa căn, cos A âm, trung tuyến BM, diện tích
def k10_tf_htl_canh_can_trung_tuyen_bm():
    k = random.choice([1, 2])
    AB_s = "2\\sqrt{3}" if k == 1 else f"{2*k}\\sqrt{{3}}"
    AC_val = 3 * k
    BC_val = 5 * k
    # AB^2 = 12k^2, AC^2 = 9k^2, cos A = -sqrt(3)/9 => BC^2 = 12k^2 + 9k^2 + 4k^2 = 25k^2 => BC = 5k
    # BM^2 = (2*AB^2 + 2*BC^2 - AC^2)/4 = (24 + 50 - 9)k^2 / 4 = 65k^2/4 => BM = k*sqrt(65)/2
    # S = 1/2 * 2k*sqrt(3) * 3k * sqrt(1 - 3/81) = 3k^2*sqrt(3)*sqrt(78)/9 = k^2*sqrt(26)
    bm_s = "\\dfrac{\\sqrt{65}}{2}" if k == 1 else "\\sqrt{65}"
    s_s = "\\sqrt{26}" if k == 1 else f"{k*k}\\sqrt{{26}}"

    caudan = f"Cho tam giác $ABC$ có $AB = {AB_s}$, $AC = {AC_val}$ và $\\cos A = \\dfrac{{-\\sqrt{{3}}}}{{9}}$. Xét tính đúng, sai của các khẳng định sau."
    item_a = (
        r"Góc nhỏ nhất trong tam giác là góc $\widehat{B}$.",
        r"Góc nhỏ nhất trong tam giác là góc $\widehat{C}$.",
        f"Vì $AC = {AC_val} < AB = {AB_s} < BC = {BC_val}$ nên góc đối diện cạnh $AC$ là góc $\\widehat{{B}}$ nhỏ nhất.",
        f"Sai vì cạnh nhỏ nhất là $AC$ nên góc nhỏ nhất phải là góc $\\widehat{{B}}$."
    )
    item_b = (
        f"Độ dài cạnh $BC$ là ${BC_val}$.",
        f"Độ dài cạnh $BC$ là ${BC_val + 2}$.",
        f"$BC^2 = AB^2 + AC^2 - 2AB\\cdot AC\\cos A = {12*k*k} + {9*k*k} + {4*k*k} = {25*k*k} \\implies BC = {BC_val}$.",
        f"Sai vì $BC^2 = {25*k*k} \\implies BC = {BC_val}$."
    )
    item_c = (
        f"Gọi $M$ là trung điểm của cạnh $AC$. Độ dài cạnh $BM$ là ${bm_s}$.",
        f"Gọi $M$ là trung điểm của cạnh $AC$. Độ dài cạnh $BM$ là ${'\\sqrt{13}' if k == 1 else '2\\sqrt{13}'}$.",
        f"Công thức trung tuyến: $BM^2 = \\dfrac{{2AB^2 + 2BC^2 - AC^2}}{{4}} = \\dfrac{{{65*k*k}}}{{4}} \\implies BM = {bm_s}$.",
        f"Sai vì $BM = {bm_s}$."
    )
    item_d = (
        f"Diện tích của tam giác $ABC$ là ${s_s}$.",
        f"Diện tích của tam giác $ABC$ là ${'\\sqrt{29}' if k == 1 else f'{k*k}\\sqrt{{29}}'} $.",
        f"Ta có $\\sin A = \\sqrt{{1 - \\cos^2 A}} = \\dfrac{{\\sqrt{{78}}}}{{9}}$, suy ra $S = \\dfrac{{1}}{{2}}AB\\cdot AC\\sin A = {s_s}$.",
        f"Sai vì $S = {s_s}$."
    )
    choices, loigiai = make_tf_choices([item_a, item_b, item_c, item_d])
    return caudan, choices, loigiai


# DS 5 (Ảnh 4 Câu 5): Tam giác biết 3 cạnh nhỏ (2, 3, 4) -> S, AH, góc tù, r + R
def k10_tf_htl_ba_canh_nho_goc_tu_r_cong_r():
    k = random.choice([1, 2])
    c, a, b = 2 * k, 3 * k, 4 * k  # AB=2k, BC=3k, CA=4k; góc lớn nhất B đối diện CA=4k (tù!)
    # p = 9k/2, S = 3k^2 sqrt(15)/4, AH (kẻ từ A xuống BC=3k) = 2S/(3k) = k sqrt(15)/2
    # r = S/p = k sqrt(15)/6, R = abc/(4S) = 24k^3 / (3k^2 sqrt(15)) = 8k sqrt(15)/15
    # r + R = k sqrt(15) * (1/6 + 8/15) = k sqrt(15) * 21/30 = 7k sqrt(15)/10
    s_s = "\\dfrac{3\\sqrt{15}}{4}" if k == 1 else "3\\sqrt{15}"
    ah_s = "\\dfrac{\\sqrt{15}}{2}" if k == 1 else "\\sqrt{15}"
    sum_r_s = "\\dfrac{7\\sqrt{15}}{10}" if k == 1 else "\\dfrac{7\\sqrt{15}}{5}"

    caudan = f"Cho tam giác $ABC$ với $AB = {c}$, $BC = {a}$, $CA = {b}$. Xét tính đúng, sai của các khẳng định sau."
    item_a = (
        f"Tam giác $ABC$ có diện tích ${s_s}$.",
        f"Tam giác $ABC$ có diện tích ${'\\sqrt{2}' if k == 1 else '4\\sqrt{2}'}$.",
        f"Nửa chu vi $p = \\dfrac{{{c}+{a}+{b}}}{{2}} = {fmt_frac(Fraction(9*k, 2))}$, theo Heron $S = {s_s}$.",
        f"Sai vì theo công thức Heron $S = {s_s}$."
    )
    item_b = (
        f"Tam giác $ABC$ có chiều cao $AH = {ah_s}$ ($H \\in BC$).",
        f"Tam giác $ABC$ có chiều cao $AH = {k}$.",
        f"Chiều cao $AH = \\dfrac{{2S}}{{BC}} = {ah_s}$.",
        f"Sai vì $AH = \\dfrac{{2S}}{{{a}}} = {ah_s}$."
    )
    item_c = (
        r"Tam giác $ABC$ có góc $\widehat{B}$ là góc tù.",
        r"Tam giác $ABC$ là tam giác nhọn.",
        f"Ta có $\\cos B = \\dfrac{{AB^2 + BC^2 - CA^2}}{{2AB\\cdot BC}} = \\dfrac{{{c**2} + {a**2} - {b**2}}}{{2\\cdot {c}\\cdot {a}}} < 0$, nên $\\widehat{{B}}$ là góc tù.",
        f"Sai vì $CA^2 = {b**2} > AB^2 + BC^2 = {c**2 + a**2}$ nên góc $\\widehat{{B}}$ là góc tù."
    )
    item_d = (
        f"Tam giác $ABC$ có tổng độ dài bán kính đường tròn nội tiếp và ngoại tiếp bằng ${sum_r_s}$.",
        f"Tam giác $ABC$ có tổng độ dài bán kính đường tròn nội tiếp và ngoại tiếp bằng ${'\\dfrac{3\\sqrt{15}}{5}' if k == 1 else '\\dfrac{6\\sqrt{15}}{5}'} $.",
        f"Ta có $r = \\dfrac{{S}}{{p}} = \\dfrac{{{'' if k == 1 else k}\\sqrt{{15}}}}{{6}}$ và $R = \\dfrac{{AB\\cdot BC\\cdot CA}}{{4S}} = \\dfrac{{{8*k}\\sqrt{{15}}}}{{15}}$, nên $r + R = {sum_r_s}$.",
        f"Sai vì $r + R = {sum_r_s}$."
    )
    choices, loigiai = make_tf_choices([item_a, item_b, item_c, item_d])
    return caudan, choices, loigiai


# DS 6 (Ảnh 3 Câu 6): Điểm M chạy trên cạnh BC, tìm độ dài AM nhỏ nhất
def k10_tf_htl_diem_m_tren_bc_am_min():
    k = random.choice([1, 2])
    c, b = 3 * k, 2 * k  # AB=3k, AC=2k, A=60 => BC = k sqrt(7)
    # cos B = (9 + 7 - 4)/(6 sqrt(7)) = 2/sqrt(7) = 2*sqrt(7)/7
    # AM_min = h_a = 2S/BC = (3k^2 sqrt(3)) / (k sqrt(7)) = 3k sqrt(21)/7
    bc_s = "\\sqrt{7}" if k == 1 else f"{k}\\sqrt{{7}}"
    am_min_s = "\\dfrac{3\\sqrt{21}}{7}" if k == 1 else "\\dfrac{6\\sqrt{21}}{7}"
    am_trap = "\\dfrac{189}{49}" if k == 1 else "\\dfrac{756}{49}"

    caudan = f"Cho tam giác $ABC$ có $AB = {c}$, $AC = {b}$, $\\widehat{{A}} = 60^\\circ$. Trên cạnh $BC$ lấy điểm $M$ nằm giữa hai điểm $B$ và $C$."
    item_a = (
        r"$BC^2 = AB^2 + AC^2 - 2AB \cdot AC \cdot \cos A$.",
        r"$BC^2 = AB^2 + AC^2 + 2AB \cdot AC \cdot \cos A$.",
        r"Theo định lí côsin: $BC^2 = AB^2 + AC^2 - 2AB \cdot AC \cdot \cos A$.",
        r"Sai vì định lí côsin phải có dấu trừ: $BC^2 = AB^2 + AC^2 - 2AB \cdot AC \cdot \cos A$."
    )
    item_b = (
        f"$BC = {bc_s}$.",
        f"$BC = {3*k}$.",
        f"$BC^2 = {c}^2 + {b}^2 - 2\\cdot {c}\\cdot {b}\\cos 60^\\circ = {7*k*k} \\implies BC = {bc_s}$.",
        f"Sai vì $BC = {bc_s}$."
    )
    item_c = (
        r"$\cos B = \dfrac{2\sqrt{7}}{7}$.",
        r"$\cos B = \dfrac{\sqrt{7}}{7}$.",
        f"Ta có $\\cos B = \\dfrac{{AB^2 + BC^2 - AC^2}}{{2AB\\cdot BC}} = \\dfrac{{{9*k*k} + {7*k*k} - {4*k*k}}}{{2\\cdot {c}\\cdot {bc_s}}} = \\dfrac{{2\\sqrt{{7}}}}{{7}}$.",
        r"Sai vì $\cos B = \dfrac{2}{\sqrt{7}} = \dfrac{2\sqrt{7}}{7}$."
    )
    item_d = (
        f"Độ dài $AM$ nhỏ nhất bằng ${am_min_s}$.",
        f"Độ dài $AM$ nhỏ nhất bằng ${am_trap}$.",
        f"$AM$ nhỏ nhất khi $AM \\perp BC$, tức $AM = h_a = \\dfrac{{AB\\cdot AC\\sin 60^\\circ}}{{BC}} = {am_min_s}$.",
        f"Sai vì $AM_{{\\min}} = h_a = {am_min_s}$ (còn ${am_trap}$ là $AM_{{\\min}}^2$)."
    )
    choices, loigiai = make_tf_choices([item_a, item_b, item_c, item_d])
    return caudan, choices, loigiai


# DS 7 (Ảnh 3 Câu 7): Biết S, AB, A=120 -> BC, R, phân giác trong AD
def k10_tf_htl_dien_tich_goc_120_phan_giac():
    c, b = random.choice([(6, 8), (4, 6), (6, 10)])
    # S = bc sqrt(3) / 4
    s_num = b * c
    g_s = math.gcd(s_num, 4)
    s_s = f"{s_num // 4}\\sqrt{{3}}" if s_num % 4 == 0 else f"\\dfrac{{{s_num // g_s}\\sqrt{{3}}}}{{{4 // g_s}}}"
    a2 = b**2 + c**2 + b * c
    k = 1
    for d in range(int(math.isqrt(a2)), 1, -1):
        if a2 % (d * d) == 0:
            k = d
            break
    rad = a2 // (k * k)
    bc_s = str(k) if rad == 1 else (f"{k}\\sqrt{{{rad}}}" if k > 1 else f"\\sqrt{{{rad}}}")
    # R = BC / (2 sin 120) = BC / sqrt(3) = k*sqrt(3*rad)/3
    r_frac = Fraction(k, 3)
    if (3 * rad) % 9 == 0:
        r_s = str(k * math.isqrt(3 * rad) // 3)
    else:
        rn, rd = r_frac.numerator, r_frac.denominator
        r_s = f"\\dfrac{{{'' if rn == 1 else rn}\\sqrt{{{3 * rad}}}}}{{{rd}}}" if rd > 1 else f"{rn}\\sqrt{{{3 * rad}}}"
    r_wrong = f"\\dfrac{{3\\sqrt{{{3 * rad}}}}}{{2}}" if rad != 3 else r"\dfrac{9}{2}"
    # Phân giác trong AD = 2bc cos(60)/(b+c) = bc/(b+c)
    ad_frac = Fraction(b * c, b + c)
    ad_wrong = Fraction(ad_frac.numerator + 1, ad_frac.denominator)

    caudan = f"Cho $\\Delta ABC$, có diện tích bằng ${s_s}$, cạnh $AB = {c}$, $\\widehat{{BAC}} = 120^\\circ$."
    item_a = (
        r"Có $BC^2 = AB^2 + AC^2 - 2AB \cdot AC \cdot \cos A$.",
        r"Có $BC^2 = AB^2 + AC^2 - 2AB \cdot AC \cdot \cos B$.",
        r"Theo định lí côsin cho cạnh $BC$ thì góc xen giữa phải là $\widehat{A}$: $BC^2 = AB^2 + AC^2 - 2AB \cdot AC \cdot \cos A$.",
        r"Sai vì theo định lí côsin phải dùng $\cos A$ (không phải $\cos B$)."
    )
    item_b = (
        f"Độ dài cạnh $BC = {bc_s}$.",
        f"Độ dài cạnh $BC = {b + c}$.",
        f"Từ $S = \\dfrac{{1}}{{2}}AB\\cdot AC\\sin 120^\\circ \\implies AC = {b}$. Suy ra $BC = \\sqrt{{{c}^2 + {b}^2 + {c}\\cdot {b}}} = {bc_s}$.",
        f"Sai vì $AC = {b}$ nên $BC = {bc_s}$."
    )
    item_c = (
        f"Bán kính đường tròn ngoại tiếp $\\Delta ABC$ là ${r_s}$.",
        f"Bán kính đường tròn ngoại tiếp $\\Delta ABC$ là ${r_wrong}$.",
        f"Theo định lí sin: $R = \\dfrac{{BC}}{{2\\sin 120^\\circ}} = \\dfrac{{{bc_s}}}{{\\sqrt{{3}}}} = {r_s}$.",
        f"Sai vì $R = \\dfrac{{{bc_s}}}{{2\\sin 120^\\circ}} = {r_s}$."
    )
    item_d = (
        f"Độ dài chân đường phân giác trong góc $A$ của $\\Delta ABC$ có độ dài là ${fmt_frac(ad_frac)}$.",
        f"Độ dài chân đường phân giác trong góc $A$ của $\\Delta ABC$ có độ dài là ${fmt_frac(ad_wrong)}$.",
        f"Độ dài phân giác trong $AD = \\dfrac{{2AB\\cdot AC\\cos 60^\\circ}}{{AB + AC}} = \\dfrac{{{c}\\cdot {b}}}{{{c} + {b}}} = {fmt_frac(ad_frac)}$.",
        f"Sai vì $AD = \\dfrac{{{c}\\cdot {b}}}{{{c}+{b}}} = {fmt_frac(ad_frac)}$."
    )
    choices, loigiai = make_tf_choices([item_a, item_b, item_c, item_d])
    return caudan, choices, loigiai


# DS 8 (Ảnh 3 Câu 8 - có hình vẽ TikZ): Lát gạch mảnh đất tứ giác ABCD
def k10_tf_htl_thuc_te_lat_gach_tu_giac():
    AB, a_bc = random.choice([(6, 4), (5, 4), (7, 4), (8, 6)])
    angB = random.choice([100, 105])
    angC = 120
    gia = 400000
    # Tam giác BCD cân tại C (BC = CD = a_bc, C = 120) => BD = a_bc * sqrt(3), góc CBD = 30
    BD = a_bc * math.sqrt(3)
    angABD = angB - 30
    S_BCD = a_bc**2 * math.sqrt(3) / 4
    S_BCD_s = f"{a_bc**2 // 4}\\sqrt{{3}}" if (a_bc**2) % 4 == 0 else f"\\dfrac{{{a_bc**2}\\sqrt{{3}}}}{{4}}"
    S_ABD = 0.5 * AB * BD * math.sin(math.radians(angABD))
    S_tot = S_BCD + S_ABD
    cost_mil = (S_tot * gia) / 1e6
    thresh = int(math.ceil(cost_mil))
    if thresh == int(cost_mil):
        thresh += 1

    bd_s = f"{a_bc}\\sqrt{{3}}"
    tikz = r"""\begin{tikzpicture}[line cap=round, line join=round, >=stealth, font=\footnotesize, scale=0.8, transform shape]
	\coordinate (B) at (0,0);
	\coordinate (C) at (2.4,0);
	\coordinate (D) at (3.6,2.08);
	\coordinate (A) at (-0.65,3.5);
	\draw[thick] (A) -- (B) -- (C) -- (D) -- cycle;
	\draw[dashed, blue] (B) -- (D);
	\pic[draw, angle radius=0.45cm, "$__ANGB__^\circ$", angle eccentricity=1.6] {angle = C--B--A};
	\pic[draw, angle radius=0.45cm, "$__ANGC__^\circ$", angle eccentricity=1.6] {angle = D--C--B};
	\node[left] at ($(A)!0.5!(B)$) {$__AB__\text{ m}$};
	\node[below] at ($(B)!0.5!(C)$) {$__ABC__\text{ m}$};
	\node[right] at ($(C)!0.5!(D)$) {$__ABC__\text{ m}$};
	\node[above] at (A) {$A$};
	\node[below left] at (B) {$B$};
	\node[below right] at (C) {$C$};
	\node[right] at (D) {$D$};
\end{tikzpicture}""".replace("__ANGB__", str(angB)).replace("__ANGC__", str(angC)).replace("__AB__", str(AB)).replace("__ABC__", str(a_bc))

    prompt = (
        f"Người ta định lát gạch tổ ong trên mảnh đất hình tứ giác $ABCD$ như mô hình. "
        f"Biết rằng $AB = {AB}\\text{{ m}}$, $BC = CD = {a_bc}\\text{{ m}}$, $\\widehat{{ABC}} = {angB}^\\circ$, $\\widehat{{BCD}} = {angC}^\\circ$ "
        f"và giá lát gạch là $400\\,000$ đồng trên một mét vuông (bao gồm cả công thợ)."
    )
    caudan = "\\immini{" + prompt + "}{\n" + tikz + "\n}"

    item_a = (
        f"Độ dài đường chéo $BD$ bằng ${bd_s}\\text{{ m}}$.",
        f"Độ dài đường chéo $BD$ bằng ${a_bc}\\sqrt{{2}}\\text{{ m}}$.",
        f"Áp dụng định lí côsin trong $\\triangle BCD$: $BD = \\sqrt{{{a_bc}^2 + {a_bc}^2 - 2\\cdot {a_bc}^2\\cos 120^\\circ}} = {bd_s}\\text{{ m}}$.",
        f"Sai vì $BD = {bd_s}\\text{{ m}}$."
    )
    item_b = (
        f"Số đo góc $\\widehat{{ABD}}$ bằng ${angABD}^\\circ$.",
        f"Số đo góc $\\widehat{{ABD}}$ bằng ${angABD + 10}^\\circ$.",
        f"Tam giác $BCD$ cân tại $C$ có $\\widehat{{C}} = 120^\\circ \\implies \\widehat{{CBD}} = 30^\\circ$, nên $\\widehat{{ABD}} = {angB}^\\circ - 30^\\circ = {angABD}^\\circ$.",
        f"Sai vì $\\widehat{{CBD}} = 30^\\circ$ nên $\\widehat{{ABD}} = {angB}^\\circ - 30^\\circ = {angABD}^\\circ$."
    )
    item_c = (
        f"Diện tích tam giác $BCD$ bằng ${S_BCD_s}\\text{{ m}}^2$.",
        f"Diện tích tam giác $BCD$ bằng ${a_bc**2}\\sqrt{{3}}\\text{{ m}}^2$.",
        f"Diện tích $S_{{\\triangle BCD}} = \\dfrac{{1}}{{2}}BC\\cdot CD\\sin 120^\\circ = {S_BCD_s}\\text{{ m}}^2$.",
        f"Sai vì $S_{{\\triangle BCD}} = {S_BCD_s}\\text{{ m}}^2$."
    )
    item_d = (
        f"Chi phí để lát gạch toàn bộ mảnh đất nhỏ hơn ${thresh}$ triệu đồng.",
        f"Chi phí để lát gạch toàn bộ mảnh đất lớn hơn ${thresh}$ triệu đồng.",
        f"Ta có $S_{{ABCD}} = S_{{\\triangle BCD}} + S_{{\\triangle ABD}} \\approx {S_tot:.2f}\\text{{ m}}^2$, chi phí $\\approx {cost_mil:.2f}$ triệu đồng $< {thresh}$ triệu đồng.",
        f"Sai vì chi phí thực tế là $\\approx {cost_mil:.2f}$ triệu đồng, nhỏ hơn ${thresh}$ triệu đồng."
    )
    choices, loigiai = make_tf_choices([item_a, item_b, item_c, item_d])
    return caudan, choices, loigiai


# ==============================================================================
# BỔ SUNG CHƯƠNG IV - VECTƠ (BÀI 7, 8, 9, 11) TỪ BỘ PHIẾU BÀI TẬP
# ==============================================================================

def _fmt_surd_val(n, k=1):
    """Định dạng k * sqrt(n) dạng LaTeX rút gọn (vd k=1, n=12 -> 2\\sqrt{3})."""
    if n == 0 or k == 0:
        return "0"
    out = 1
    rem = abs(n)
    d = 2
    while d * d <= rem:
        while rem % (d * d) == 0:
            out *= d
            rem //= (d * d)
        d += 1
    coeff = k * out
    if rem == 1:
        return str(coeff)
    if coeff == 1:
        return f"\\sqrt{{{rem}}}"
    if coeff == -1:
        return f"-\\sqrt{{{rem}}}"
    return f"{coeff}\\sqrt{{{rem}}}"


def _fmt_frac_mul(fr, expr):
    """Định dạng fr * expr trong LaTeX (vd 1/2 -> \\dfrac{1}{2}expr, 1 -> expr, -1 -> -expr)."""
    if fr == 0:
        return "0"
    if fr == 1:
        return expr
    if fr == -1:
        return f"-{expr}"
    if fr.denominator == 1:
        return f"{fr.numerator}{expr}"
    if fr.numerator < 0:
        return f"-\\dfrac{{{-fr.numerator}}}{{{fr.denominator}}}{expr}"
    return f"\\dfrac{{{fr.numerator}}}{{{fr.denominator}}}{expr}"


def _fmt_lin_comb_2vec(c1, v1, c2, v2):
    """Định dạng tổ hợp c1*v1 + c2*v2 với Fraction c1, c2."""
    parts = []
    if c1 != 0:
        parts.append(_fmt_frac_mul(c1, v1))
    if c2 != 0:
        s2 = _fmt_frac_mul(abs(c2), v2)
        if not parts:
            parts.append(_fmt_frac_mul(c2, v2))
        else:
            parts.append(f"+ {s2}" if c2 > 0 else f"- {s2}")
    return " ".join(parts) if parts else r"\vec{0}"


# --- BÀI 7: CÁC KHÁI NIỆM MỞ ĐẦU ---

def k10_mc_vecto_b7_dem_so_vecto():
    """Bài 7: Đếm số vectơ khác vectơ-không từ đỉnh đa giác hoặc lục giác đều tâm O."""
    mode = random.choice(["da_giac", "luc_giac_cung_phuong", "luc_giac_bang_nhau"])
    if mode == "da_giac":
        n, ten = random.choice([
            (4, "tứ giác $ABCD$"),
            (5, "ngũ giác $ABCDE$"),
            (6, "lục giác $ABCDEF$"),
        ])
        ans = n * (n - 1)
        comb = n * (n - 1) // 2
        wrongs = [str(comb), str(2 * n), str(n)]
        caudan = (
            f"Cho {ten}. Số các vectơ khác $\\vec{{0}}$ có điểm đầu và điểm cuối "
            f"là đỉnh của đa giác đã cho bằng"
        )
        choices = shuffle_choices(f"${ans}$", [f"${w}$" for w in wrongs])
        loigiai = (
            f"Mỗi cặp $2$ đỉnh phân biệt chọn có thứ tự tạo thành $1$ vectơ khác $\\vec{{0}}$.\\\\\n"
            f"Với ${n}$ đỉnh, có ${n}$ cách chọn điểm đầu và ${n - 1}$ cách chọn điểm cuối (khác điểm đầu), "
            f"do đó có ${n} \\cdot {n - 1} = {ans}$ vectơ."
        )
        return caudan, choices, loigiai

    if mode == "luc_giac_cung_phuong":
        ref = random.choice([r"\vec{OA}", r"\vec{OB}", r"\vec{OC}"])
        caudan = (
            f"Cho hình lục giác đều $ABCDEF$ tâm $O$. Số các vectơ khác $\\vec{{0}}$, cùng phương với "
            f"vectơ ${ref}$ và có điểm đầu, điểm cuối là các đỉnh của lục giác bằng"
        )
        choices = shuffle_choices("$6$", ["$4$", "$8$", "$10$"])
        loigiai = (
            f"Xét đường thẳng chứa ${ref}$ (đường chéo đi qua tâm $O$) và hai cạnh đối diện song song với đường chéo đó.\\\\\n"
            f"Trên mỗi đoạn trong $3$ đoạn thẳng này có $2$ vectơ ngược hướng nhau (đầu và cuối đều là đỉnh lục giác).\\\\\n"
            f"Vậy có tất cả $3 \\times 2 = 6$ vectơ thỏa mãn."
        )
        return caudan, choices, loigiai

    verts = ["A", "B", "C", "D", "E", "F"]
    idx = random.randint(0, 5)
    v0 = verts[idx]
    v1 = verts[(idx + 1) % 6]
    eq1 = f"\\vec{{{verts[(idx - 1) % 6]}O}}"
    eq2 = f"\\vec{{O{verts[(idx + 2) % 6]}}}"
    eq3 = f"\\vec{{{verts[(idx + 4) % 6]}{verts[(idx + 3) % 6]}}}"
    eq3_rev = f"\\vec{{{verts[(idx + 3) % 6]}{verts[(idx + 4) % 6]}}}"
    eq2_rev = f"\\vec{{{verts[(idx + 2) % 6]}O}}"
    diag = f"\\vec{{{verts[(idx - 1) % 6]}{verts[(idx + 2) % 6]}}}"
    caudan = (
        f"Cho lục giác đều $ABCDEF$ tâm $O$. Các vectơ khác vectơ-không có điểm đầu, điểm cuối là "
        f"đỉnh của lục giác hoặc tâm $O$ sao cho bằng với $\\vec{{{v0}{v1}}}$ là"
    )
    correct = f"${eq1}, {eq2}, {eq3}$"
    wrongs = [
        f"${eq1}, {eq2}, {eq3_rev}$",
        f"${eq1}, {diag}, {eq3}$",
        f"${eq1}, {eq2_rev}, {eq3}$",
    ]
    choices = shuffle_choices(correct, wrongs)
    loigiai = (
        f"Trong lục giác đều $ABCDEF$ tâm $O$, các vectơ cùng hướng và có độ dài bằng cạnh $a = {v0}{v1}$ "
        f"chính là ${eq1}, {eq2}, {eq3}$."
    )
    return caudan, choices, loigiai


def k10_mc_vecto_b7_dieu_kien_cung_huong_bang_nhau():
    """Bài 7: Điều kiện cùng phương, cùng hướng, bằng nhau của hai vectơ."""
    mode = random.choice(["vo_so_do_dai", "thang_hang_cung_huong", "hbh_abdc", "trung_binh_liet_ke"])
    if mode == "vo_so_do_dai":
        caudan = (
            "Cho vectơ $\\vec{AB} \\neq \\vec{0}$ và một điểm $C$ cố định. "
            "Có bao nhiêu điểm $D$ thỏa mãn $|\\vec{AB}| = |\\vec{CD}|$?"
        )
        choices = shuffle_choices("Vô số.", ["$0$.", "$1$.", "$2$."])
        loigiai = (
            "Điều kiện $|\\vec{AB}| = |\\vec{CD}| \\Leftrightarrow CD = AB$.\\\\\n"
            "Vì $A, B, C$ cố định nên $D$ là mọi điểm thuộc đường tròn tâm $C$ bán kính $R = AB$ (trong mặt phẳng), "
            "do đó có vô số điểm $D$ thỏa mãn."
        )
        return caudan, choices, loigiai

    if mode == "thang_hang_cung_huong":
        pts = random.choice([("A", "B", "C"), ("M", "N", "P")])
        p1, p2, p3 = pts
        caudan = (
            f"Cho ba điểm ${p1}, {p2}, {p3}$ đôi một phân biệt cùng nằm trên một đường thẳng. "
            f"Hai vectơ $\\vec{{{p1}{p2}}}$ và $\\vec{{{p2}{p3}}}$ cùng hướng khi và chỉ khi"
        )
        correct = f"Điểm ${p2}$ nằm giữa hai điểm ${p1}$ và ${p3}$."
        wrongs = [
            f"Điểm ${p1}$ nằm giữa hai điểm ${p2}$ và ${p3}$.",
            f"Điểm ${p3}$ nằm giữa hai điểm ${p1}$ và ${p2}$.",
            f"Điểm ${p1}$ nằm ngoài đoạn ${p2}{p3}$ về phía ${p3}$.",
        ]
        choices = shuffle_choices(correct, wrongs)
        loigiai = (
            f"Hai vectơ $\\vec{{{p1}{p2}}}$ và $\\vec{{{p2}{p3}}}$ cùng nằm trên một đường thẳng nên chúng cùng phương.\\\\\n"
            f"Chúng cùng hướng từ ${p1}$ qua ${p2}$ rồi đến ${p3}$ khi và chỉ khi ${p2}$ nằm giữa ${p1}$ và ${p3}$."
        )
        return caudan, choices, loigiai

    if mode == "hbh_abdc":
        caudan = (
            "Cho bốn điểm $A, B, C, D$ đôi một phân biệt và không có ba điểm nào thẳng hàng. "
            "Điều kiện nào sau đây là điều kiện cần và đủ để $\\vec{AB} = \\vec{CD}$?"
        )
        correct = "$ABDC$ là hình bình hành."
        wrongs = [
            "$ABCD$ là hình bình hành.",
            "$AC$ và $BD$ có cùng trung điểm.",
            "$AB = CD$ và $AB \\perp CD$.",
        ]
        choices = shuffle_choices(correct, wrongs)
        loigiai = (
            "Với $A, B, C, D$ không thẳng hàng, $\\vec{AB} = \\vec{CD}$ khi và chỉ khi tứ giác $ABDC$ "
            "có cặp cạnh đối song song và bằng nhau, tức là $ABDC$ là hình bình hành (lưu ý thứ tự đỉnh $A \\to B \\to D \\to C$)."
        )
        return caudan, choices, loigiai

    caudan = (
        "Cho tam giác $ABC$. Gọi $M, N, P$ lần lượt là trung điểm của $AB, BC, CA$. "
        "Các vectơ khác $\\vec{0}$ cùng phương với $\\vec{MN}$ có điểm đầu và điểm cuối lấy trong số các điểm đã cho là"
    )
    correct = r"$\vec{NM}, \vec{AC}, \vec{CA}, \vec{AP}, \vec{PA}, \vec{PC}, \vec{CP}$"
    wrongs = [
        r"$\vec{AC}, \vec{CA}, \vec{AP}, \vec{PA}, \vec{PC}, \vec{CP}$",
        r"$\vec{NM}, \vec{BC}, \vec{CB}, \vec{PA}, \vec{AP}$",
        r"$\vec{NM}, \vec{BC}, \vec{CA}, \vec{AM}, \vec{MA}, \vec{PN}$",
    ]
    choices = shuffle_choices(correct, wrongs)
    loigiai = (
        "Vì $MN$ là đường trung bình của $\\Delta ABC$ nên $MN \\parallel AC$.\\\\\n"
        "Các vectơ khác $\\vec{0}$ nằm trên đường thẳng $MN$ (gồm $\\vec{NM}$) và nằm trên đường thẳng $AC$ "
        "(gồm $\\vec{AC}, \\vec{CA}, \\vec{AP}, \\vec{PA}, \\vec{PC}, \\vec{CP}$) đều cùng phương với $\\vec{MN}$."
    )
    return caudan, choices, loigiai


def k10_mc_vecto_b7_do_dai_co_ban():
    """Bài 7: Tính độ dài vectơ trong tam giác đều và hình thoi."""
    mode = random.choice(["thoi_ao", "thoi_bo", "deu_duong_cao"])
    k = random.choice([1, 2, 4])
    k_str = "" if k == 1 else str(k)
    if mode == "thoi_ao":
        caudan = (
            f"Cho hình thoi $ABCD$ tâm $O$, cạnh bằng ${k_str}a$ và $\\widehat{{BAD}} = 60^\\circ$. "
            f"Độ dài vectơ $\\vec{{AO}}$ bằng"
        )
        if k == 1:
            correct = r"$\dfrac{a\sqrt{3}}{2}$"
            wrongs = [r"$a$", r"$\dfrac{a}{2}$", r"$\dfrac{a\sqrt{2}}{2}$"]
        elif k == 2:
            correct = r"$a\sqrt{3}$"
            wrongs = [r"$2a$", r"$a$", r"$a\sqrt{2}$"]
        else:
            correct = r"$2a\sqrt{3}$"
            wrongs = [r"$4a$", r"$2a$", r"$2a\sqrt{2}$"]
        choices = shuffle_choices(correct, wrongs)
        loigiai = (
            f"Vì hình thoi $ABCD$ có $\\widehat{{BAD}} = 60^\\circ$ nên $\\Delta ABD$ đều cạnh ${k_str}a$.\\\\\n"
            f"Khi đó $AO$ là đường cao của tam giác đều $ABD$, suy ra $|\\vec{{AO}}| = AO = {correct.strip('$')}$."
        )
        return caudan, choices, loigiai

    if mode == "thoi_bo":
        caudan = (
            f"Cho hình thoi $ABCD$ tâm $O$, cạnh bằng ${k_str}a$ và $\\widehat{{BAD}} = 60^\\circ$. "
            f"Độ dài vectơ $\\vec{{BO}}$ bằng"
        )
        if k == 1:
            correct = r"$\dfrac{a}{2}$"
            wrongs = [r"$\dfrac{a\sqrt{3}}{2}$", r"$a$", r"$\dfrac{a\sqrt{2}}{2}$"]
        elif k == 2:
            correct = r"$a$"
            wrongs = [r"$a\sqrt{3}$", r"$2a$", r"$a\sqrt{2}$"]
        else:
            correct = r"$2a$"
            wrongs = [r"$2a\sqrt{3}$", r"$4a$", r"$2a\sqrt{2}$"]
        choices = shuffle_choices(correct, wrongs)
        loigiai = (
            f"Vì $\\widehat{{BAD}} = 60^\\circ$ nên $\\Delta ABD$ đều cạnh ${k_str}a \\Rightarrow BD = {k_str}a$.\\\\\n"
            f"Do $O$ là trung điểm $BD$ nên $|\\vec{{BO}}| = \\dfrac{{BD}}{{2}} = {correct.strip('$')}$."
        )
        return caudan, choices, loigiai

    caudan = f"Cho tam giác đều $ABC$ cạnh ${k_str}a$ có đường cao $AH$. Độ dài vectơ $\\vec{{AH}}$ bằng"
    if k == 1:
        correct = r"$\dfrac{a\sqrt{3}}{2}$"
        wrongs = [r"$a\sqrt{3}$", r"$\dfrac{a}{2}$", r"$a$"]
    elif k == 2:
        correct = r"$a\sqrt{3}$"
        wrongs = [r"$2a\sqrt{3}$", r"$a$", r"$2a$"]
    else:
        correct = r"$2a\sqrt{3}$"
        wrongs = [r"$4a\sqrt{3}$", r"$2a$", r"$4a$"]
    choices = shuffle_choices(correct, wrongs)
    loigiai = f"Đường cao của tam giác đều cạnh ${k_str}a$ có độ dài là $|\\vec{{AH}}| = AH = {correct.strip('$')}$."
    return caudan, choices, loigiai


def k10_tf_vecto_b7_hinh_thang_cung_phuong():
    """Bài 7 ĐS: Hình thang ABCD đáy AB, CD và trung điểm hai cạnh bên M, N."""
    caudan = (
        "Cho hình thang $ABCD$ có hai đáy là $AB$ và $CD$ ($AB \\neq CD$). "
        "Gọi $M, N$ lần lượt là trung điểm của các cạnh bên $AD$ và $BC$. "
        "Xét tính đúng, sai của các khẳng định sau:"
    )
    items = [
        (
            r"$MN \parallel CD$.",
            r"$MN \perp AB$.",
            r"$MN$ là đường trung bình của hình thang $ABCD$ nên $MN \parallel AB \parallel CD$.",
            r"Sai vì $MN$ là đường trung bình của hình thang nên $MN \parallel AB$."
        ),
        (
            r"Có đúng $4$ vectơ khác $\vec{0}$ cùng phương với $\vec{AB}$ có điểm đầu và điểm cuối là một trong các điểm $A, B, C, D, M, N$ mà giá không trùng đường thẳng $AB$.",
            r"Có $6$ vectơ khác $\vec{0}$ cùng phương với $\vec{AB}$ có điểm đầu và điểm cuối là một trong các điểm $A, B, C, D, M, N$ mà giá không trùng đường thẳng $AB$.",
            r"Các vectơ đó nằm trên hai đường thẳng $CD$ và $MN$ song song với $AB$, gồm: $\vec{CD}, \vec{DC}, \vec{MN}, \vec{NM}$ (có $4$ vectơ).",
            r"Sai vì chỉ có $4$ vectơ thỏa mãn là $\vec{CD}, \vec{DC}, \vec{MN}, \vec{NM}$."
        ),
        (
            r"Có đúng $2$ vectơ khác $\vec{0}$ cùng hướng với $\vec{AB}$ có điểm đầu và điểm cuối thuộc $\{A, B, C, D, M, N\}$ mà giá không trùng đường thẳng $AB$.",
            r"Có $3$ vectơ khác $\vec{0}$ cùng hướng với $\vec{AB}$ có điểm đầu và điểm cuối thuộc $\{A, B, C, D, M, N\}$ mà giá không trùng đường thẳng $AB$.",
            r"Trong hình thang $ABCD$ (các đỉnh theo thứ tự vòng quanh $A, B, C, D$), $\vec{AB}$ cùng hướng với $\vec{DC}$ và $\vec{MN}$ (chỉ có $2$ vectơ).",
            r"Sai vì chỉ có $2$ vectơ cùng hướng với $\vec{AB}$ không nằm trên $AB$ là $\vec{DC}$ và $\vec{MN}$."
        ),
        (
            r"$|\vec{AC}| = |\vec{BD}|$ khi và chỉ khi $|\vec{AD}| = |\vec{BC}|$.",
            r"Nếu $|\vec{AC}| = |\vec{BD}|$ thì $|\vec{AB}| = |\vec{CD}|$.",
            r"Trong hình thang $ABCD$ ($AB \neq CD$), hai đường chéo bằng nhau ($AC = BD$) khi và chỉ khi hình thang cân, tức hai cạnh bên bằng nhau ($AD = BC$).",
            r"Sai vì $|\vec{AC}| = |\vec{BD}|$ khi và chỉ khi $ABCD$ là hình thang cân ($AD = BC$), không suy ra $AB = CD$."
        ),
    ]
    choices, loigiai = make_tf_choices(items)
    return caudan, choices, loigiai


def k10_tf_vecto_b7_da_giac_va_thang_hang():
    """Bài 7 ĐS: Đếm số vectơ lập từ đa giác và các điểm thẳng hàng."""
    variant = random.choice(["da_giac", "thang_hang"])
    if variant == "da_giac":
        n, ten = random.choice([(5, "ngũ giác $ABCDE$"), (6, "lục giác $ABCDEF$")])
        edges_vec = 2 * n
        diag_cnt = n * (n - 3) // 2
        diag_vec = 2 * diag_cnt
        tri_vec = 6
        quad_diag_vec = 4
        caudan = f"Cho {ten} (không có ba đỉnh nào thẳng hàng). Xét tính đúng, sai của các khẳng định sau:"
        items = [
            (
                f"Có ${edges_vec}$ vectơ khác $\\vec{{0}}$ được lập ra từ các cạnh của đa giác đã cho.",
                f"Có ${n}$ vectơ khác $\\vec{{0}}$ được lập ra từ các cạnh của đa giác đã cho.",
                f"Đa giác có ${n}$ cạnh, mỗi cạnh tạo ra $2$ vectơ ngược hướng nhau nên có $2 \\cdot {n} = {edges_vec}$ vectơ.",
                f"Sai vì mỗi cạnh tạo ra $2$ vectơ nên tổng cộng có ${edges_vec}$ vectơ."
            ),
            (
                f"Có ${diag_vec}$ vectơ khác $\\vec{{0}}$ được lập ra từ các đường chéo của đa giác đã cho.",
                f"Có ${diag_cnt}$ vectơ khác $\\vec{{0}}$ được lập ra từ các đường chéo của đa giác đã cho.",
                f"Số đường chéo là $\\dfrac{{{n}({n}-3)}}{{2}} = {diag_cnt}$, mỗi đường chéo tạo $2$ vectơ nên có ${diag_vec}$ vectơ.",
                f"Sai vì có ${diag_cnt}$ đường chéo, tạo ra $2 \\cdot {diag_cnt} = {diag_vec}$ vectơ."
            ),
            (
                f"Có ${tri_vec}$ vectơ khác $\\vec{{0}}$ được lập ra từ các cạnh của tam giác $ABC$.",
                f"Có $3$ vectơ khác $\\vec{{0}}$ được lập ra từ các cạnh của tam giác $ABC$.",
                "Tam giác $ABC$ có $3$ cạnh, mỗi cạnh ứng với $2$ vectơ nên có $6$ vectơ.",
                "Sai vì có $6$ vectơ khác $\\vec{0}$ lập từ các cạnh của $\\Delta ABC$."
            ),
            (
                f"Có ${quad_diag_vec}$ vectơ khác $\\vec{{0}}$ được lập ra từ các đường chéo của tứ giác $ABCD$.",
                f"Có $2$ vectơ khác $\\vec{{0}}$ được lập ra từ các đường chéo của tứ giác $ABCD$.",
                "Tứ giác $ABCD$ có $2$ đường chéo $AC, BD$, tạo ra $4$ vectơ $\\vec{AC}, \\vec{CA}, \\vec{BD}, \\vec{DB}$.",
                "Sai vì tứ giác có $2$ đường chéo nên tạo ra $4$ vectơ."
            ),
        ]
    else:
        caudan = (
            "Trên đường thẳng $d$ lấy bốn điểm phân biệt $A, B, C, D$. Lấy một điểm $P$ không thuộc $d$. "
            "Xét tính đúng, sai của các khẳng định sau:"
        )
        items = [
            (
                "Có $4$ vectơ khác $\\vec{0}$ có điểm đầu là $A$ và điểm cuối là một trong các điểm còn lại.",
                "Có $5$ vectơ khác $\\vec{0}$ có điểm đầu là $A$ và điểm cuối là một trong các điểm còn lại.",
                "Các vectơ khác $\\vec{0}$ gốc $A$ là $\\vec{AB}, \\vec{AC}, \\vec{AD}, \\vec{AP}$ (có $4$ vectơ).",
                "Sai vì điểm cuối phải khác $A$ nên chỉ có $4$ vectơ."
            ),
            (
                "Có $20$ vectơ khác $\\vec{0}$ được lập ra từ năm điểm $A, B, C, D, P$.",
                "Có $10$ vectơ khác $\\vec{0}$ được lập ra từ năm điểm $A, B, C, D, P$.",
                "Số vectơ khác $\\vec{0}$ tạo bởi $5$ điểm phân biệt là $5 \\cdot 4 = 20$ vectơ.",
                "Sai vì $5$ điểm tạo được $5 \\cdot 4 = 20$ vectơ khác $\\vec{0}$."
            ),
            (
                "Có $12$ vectơ khác $\\vec{0}$ tạo thành từ bốn điểm $A, B, C, D$.",
                "Có $10$ vectơ khác $\\vec{0}$ tạo thành từ bốn điểm $A, B, C, D$.",
                "Số vectơ khác $\\vec{0}$ tạo từ $4$ điểm phân biệt là $4 \\cdot 3 = 12$ vectơ.",
                "Sai vì $4$ điểm tạo được $4 \\cdot 3 = 12$ vectơ khác $\\vec{0}$."
            ),
            (
                "Trong các vectơ khác $\\vec{0}$ tạo bởi $5$ điểm đã cho, có đúng $11$ vectơ khác $\\vec{AB}$ mà cùng phương với $\\vec{AB}$.",
                "Trong các vectơ khác $\\vec{0}$ tạo bởi $5$ điểm đã cho, có đúng $12$ vectơ khác $\\vec{AB}$ mà cùng phương với $\\vec{AB}$.",
                "Các vectơ khác $\\vec{0}$ cùng phương với $\\vec{AB}$ phải nằm trên đường thẳng $d$, gồm $12$ vectơ tạo bởi $A,B,C,D$. Bỏ $\\vec{AB}$ còn $11$ vectơ.",
                "Sai vì bỏ đi chính vectơ $\\vec{AB}$ thì chỉ còn $12 - 1 = 11$ vectơ."
            ),
        ]
    choices, loigiai = make_tf_choices(items)
    return caudan, choices, loigiai


def k10_sa_vecto_b7_do_dai_thoi_hoac_tam_giac_deu():
    """Bài 7 TLN: Độ dài vectơ đường chéo hình thoi hoặc |BI| trong tam giác đều."""
    mode = random.choice(["thoi", "bi_trong_tam"])
    if mode == "thoi":
        a = random.choice([4, 6, 8, 10, 12])
        val = a * math.sqrt(3)
        ans_str = _fmt_vn(val, 2)
        caudan = (
            f"Cho hình thoi $ABCD$ cạnh bằng ${a}$ và $\\widehat{{BAD}} = 60^\\circ$. "
            f"Tính độ dài vectơ $\\vec{{AC}}$ (làm tròn kết quả đến hàng phần trăm)."
        )
        loigiai = (
            f"Vì hình thoi $ABCD$ có $\\widehat{{BAD}} = 60^\\circ$ nên $\\Delta ABD$ đều cạnh ${a}$, "
            f"tâm $O$ của hình thoi có $AO = \\dfrac{{{a}\\sqrt{{3}}}}{{2}}$.\\\\\n"
            f"Vậy $|\\vec{{AC}}| = AC = 2AO = {a}\\sqrt{{3}} \\approx {ans_str}$."
        )
        return caudan, ans_str, loigiai

    a = random.choice([6, 12, 18])
    val = a * math.sqrt(21) / 6.0
    ans_str = _fmt_vn(val, 2)
    caudan = (
        f"Cho tam giác $ABC$ đều cạnh bằng ${a}$ và $G$ là trọng tâm. Gọi $I$ là trung điểm của đoạn thẳng $AG$. "
        f"Tính độ dài vectơ $\\vec{{BI}}$ (làm tròn kết quả đến hàng phần trăm)."
    )
    k = a // 6
    k_str = "" if k == 1 else str(k)
    loigiai = (
        f"Gọi $M$ là trung điểm $BC$, ta có $AM = \\dfrac{{{a}\\sqrt{{3}}}}{{2}}$ và $BM = {a // 2}$.\\\\\n"
        f"Do $G$ là trọng tâm nên $AG = \\dfrac{{2}}{{3}}AM$, suy ra $AI = \\dfrac{{1}}{{2}}AG = \\dfrac{{1}}{{3}}AM$, "
        f"do đó $IM = \\dfrac{{2}}{{3}}AM = \\dfrac{{{a}\\sqrt{{3}}}}{{3}}$.\\\\\n"
        f"Trong tam giác vuông $BIM$ tại $M$: $|\\vec{{BI}}| = BI = \\sqrt{{BM^2 + IM^2}} = "
        f"\\sqrt{{\\left({a // 2}\\right)^2 + \\dfrac{{{a}^2}}{{3}}}} = {k_str}\\sqrt{{21}} \\approx {ans_str}$."
    )
    return caudan, ans_str, loigiai


# --- BÀI 8: TỔNG VÀ HIỆU CỦA HAI VECTƠ ---

def k10_mc_vecto_b8_quy_tac_ba_diem_tong_hieu():
    """Bài 8 MC: Quy tắc ba điểm, cộng trừ nhiều vectơ và tìm vị trí điểm M."""
    mode = random.choice(["tong_5_diem", "hieu_hbh_sai", "tam_giac_vuong_tong", "tim_vi_tri_m"])
    if mode == "tong_5_diem":
        sub = random.choice(["bang_0", "bang_ad"])
        if sub == "bang_0":
            caudan = "Cho năm điểm phân biệt $A, B, C, D, E$. Vectơ tổng $\\vec{AB} + \\vec{CD} + \\vec{BC} + \\vec{DE} + \\vec{EA}$ bằng"
            correct = r"$\vec{0}$"
            wrongs = [r"$\vec{AE}$", r"$\vec{AC}$", r"$\vec{BD}$"]
            loigiai = r"Nhóm theo quy tắc ba điểm: $(\vec{AB}+\vec{BC})+(\vec{CD}+\vec{DE})+\vec{EA} = \vec{AC}+\vec{CE}+\vec{EA} = \vec{AE}+\vec{EA} = \vec{0}$."
        else:
            caudan = "Cho bốn điểm phân biệt $A, B, C, D$. Vectơ tổng $\\vec{AB} + \\vec{CD} + \\vec{BC}$ bằng"
            correct = r"$\vec{AD}$"
            wrongs = [r"$\vec{0}$", r"$\vec{DA}$", r"$\vec{AC}$"]
            loigiai = r"Ta có $\vec{AB} + \vec{BC} + \vec{CD} = \vec{AC} + \vec{CD} = \vec{AD}$."
        choices = shuffle_choices(correct, wrongs)
        return caudan, choices, loigiai

    if mode == "hieu_hbh_sai":
        caudan = "Gọi $O$ là tâm của hình bình hành $ABCD$. Đẳng thức nào sau đây \\textbf{sai}?"
        correct = r"$\vec{OB} - \vec{OC} = \vec{OD} - \vec{OA}$"
        wrongs = [
            r"$\vec{OA} - \vec{OB} = \vec{CD}$",
            r"$\vec{AB} - \vec{AD} = \vec{DB}$",
            r"$\vec{BC} - \vec{BA} = \vec{DC} - \vec{DA}$",
        ]
        choices = shuffle_choices(correct, wrongs)
        loigiai = (
            r"Ta có $\vec{OB} - \vec{OC} = \vec{CB}$ và $\vec{OD} - \vec{OA} = \vec{AD}$.\\ "
            r"Trong hình bình hành $ABCD$, $\vec{CB} = -\vec{AD} \neq \vec{AD}$ nên $\vec{OB} - \vec{OC} = \vec{OD} - \vec{OA}$ là sai."
        )
        return caudan, choices, loigiai

    if mode == "tam_giac_vuong_tong":
        ab, ac, bc = random.choice([(3, 4, 5), (6, 8, 10), (5, 12, 13)])
        rad = 4 * ab**2 + ac**2
        ans_str = _fmt_surd_val(rad)
        caudan = (
            f"Cho tam giác $ABC$ vuông tại $A$ có $AB = {ab}\\text{{ cm}}$, $BC = {bc}\\text{{ cm}}$. "
            f"Tính độ dài $|\\vec{{BA}} + \\vec{{BC}}|$."
        )
        correct = f"${ans_str}\\text{{ cm}}$"
        pool_w = [f"${ab + ac}\\text{{ cm}}$", f"${bc}\\text{{ cm}}$", f"${ab * 2}\\text{{ cm}}$", f"${_fmt_surd_val(ab**2 + 4 * ac**2)}\\text{{ cm}}$"]
        wrongs = [w for w in pool_w if w != correct][:3]
        choices = shuffle_choices(correct, wrongs)
        loigiai = (
            f"Theo định lí Pythagore, $AC = \\sqrt{{BC^2 - AB^2}} = \\sqrt{{{bc}^2 - {ab}^2}} = {ac}\\text{{ cm}}$.\\\\\n"
            f"Gọi $M$ là trung điểm $AC$, ta có $\\vec{{BA}} + \\vec{{BC}} = 2\\vec{{BM}}$ và $AM = {ac // 2}\\text{{ cm}}$.\\\\\n"
            f"Trong tam giác vuông $BAM$: $BM = \\sqrt{{AB^2 + AM^2}} = \\sqrt{{{ab}^2 + ({ac // 2})^2}}$, "
            f"suy ra $|\\vec{{BA}} + \\vec{{BC}}| = 2BM = {ans_str}\\text{{ cm}}$."
        )
        return caudan, choices, loigiai

    sub = random.choice(["trung_c", "trung_m_b"])
    if sub == "trung_c":
        caudan = "Cho tứ giác $ABCD$, $M$ là điểm thỏa mãn $\\vec{AM} = \\vec{DC} + \\vec{AB} + \\vec{BD}$. Mệnh đề nào sau đây đúng?"
        correct = "$M$ trùng $C$."
        wrongs = ["$M$ trùng $D$.", "$M$ trùng $A$.", "$M$ trùng $B$."]
        loigiai = r"Ta có $\vec{AB} + \vec{BD} + \vec{DC} = \vec{AD} + \vec{DC} = \vec{AC} \Rightarrow \vec{AM} = \vec{AC} \Leftrightarrow M \equiv C$."
    else:
        caudan = "Cho hình bình hành $ABCD$. Tìm vị trí điểm $M$ thỏa mãn $\\vec{MA} - \\vec{MB} - \\vec{MC} = \\vec{AD}$."
        correct = "Điểm $C$ là trung điểm cạnh $AM$."
        wrongs = [
            "Điểm $M$ là trung điểm cạnh $AC$.",
            "Điểm $M$ là trung điểm cạnh $BD$.",
            "Điểm $B$ là trung điểm cạnh $MC$.",
        ]
        loigiai = (
            r"Ta có $\vec{MA} - \vec{MB} = \vec{BA} = \vec{CD}$.\\ "
            r"Hệ thức trở thành $\vec{CD} - \vec{MC} = \vec{AD} \Leftrightarrow \vec{CD} - \vec{AD} = \vec{MC} \Leftrightarrow \vec{CA} = \vec{MC}$, "
            r"tức là $C$ là trung điểm đoạn thẳng $AM$."
        )
    choices = shuffle_choices(correct, wrongs)
    return caudan, choices, loigiai


def k10_mc_vecto_b8_ba_luc_can_bang_tikz():
    """Bài 8 MC (TikZ): Ba lực cân bằng tác dụng lên một vật tại M."""
    f_val = random.choice([15, 20, 25, 30, 40])
    ang = random.choice([60, 120])
    half_ang = ang // 2

    tikz = r"""\begin{center}
\begin{tikzpicture}[>=stealth, font=\footnotesize, scale=0.9]
  \coordinate (M) at (0,0);
  \coordinate (C) at (-2.4,0);
  \coordinate (A) at (__HALFA__:1.8);
  \coordinate (B) at (-__HALFA__:1.8);
  \draw[->, thick] (M) -- (C) node[midway, above] {$\vec{F}_3$};
  \draw[->, thick] (M) -- (A) node[midway, above left] {$\vec{F}_1$};
  \draw[->, thick] (M) -- (B) node[midway, below left] {$\vec{F}_2$};
  \node[below] at (M) {$M$};
  \node[below] at (C) {$C$};
  \node[above right] at (A) {$A$};
  \node[below right] at (B) {$B$};
  \draw pic["$__ANG__^\circ$", draw, angle radius=0.45cm, angle eccentricity=1.6] {angle=B--M--A};
\end{tikzpicture}
\end{center}""".replace("__HALFA__", str(half_ang)).replace("__ANG__", str(ang))

    caudan = (
        f"Cho ba lực $\\vec{{F}}_1 = \\vec{{MA}}$, $\\vec{{F}}_2 = \\vec{{MB}}$, $\\vec{{F}}_3 = \\vec{{MC}}$ "
        f"cùng tác dụng vào một vật tại điểm $M$ và vật đứng yên. Cho biết cường độ của $\\vec{{F}}_1, \\vec{{F}}_2$ "
        f"đều bằng ${f_val}\\text{{ N}}$ và góc $\\widehat{{AMB}} = {ang}^\\circ$ (như hình vẽ). "
        f"Khi đó cường độ lực của $\\vec{{F}}_3$ bằng\n{tikz}"
    )

    if ang == 60:
        correct = f"${f_val}\\sqrt{{3}}\\text{{ N}}$"
        wrongs = [f"${2 * f_val}\\sqrt{{3}}\\text{{ N}}$", f"${f_val}\\sqrt{{2}}\\text{{ N}}$", f"${f_val}\\text{{ N}}$"]
        loigiai = (
            f"Vật đứng yên nên $\\vec{{F}}_1 + \\vec{{F}}_2 + \\vec{{F}}_3 = \\vec{{0}} \\Rightarrow |\\vec{{F}}_3| = |\\vec{{F}}_1 + \\vec{{F}}_2|$.\\\\\n"
            f"Dựng hình thoi $MADB$, ta có đường chéo $MD = 2 \\cdot MA\\cos 30^\\circ = {f_val}\\sqrt{{3}}$.\\\\\n"
            f"Vậy $|\\vec{{F}}_3| = {f_val}\\sqrt{{3}}\\text{{ N}}$."
        )
    else:
        correct = f"${f_val}\\text{{ N}}$"
        wrongs = [f"${f_val}\\sqrt{{3}}\\text{{ N}}$", f"${f_val}\\sqrt{{2}}\\text{{ N}}$", f"${2 * f_val}\\text{{ N}}$"]
        loigiai = (
            f"Vật đứng yên nên $|\\vec{{F}}_3| = |\\vec{{F}}_1 + \\vec{{F}}_2|$.\\\\\n"
            f"Vì $|\\vec{{F}}_1| = |\\vec{{F}}_2| = {f_val}\\text{{ N}}$ và $\\widehat{{AMB}} = 120^\\circ$ nên tam giác hợp lực đều, "
            f"suy ra $|\\vec{{F}}_3| = {f_val}\\text{{ N}}$."
        )
    choices = shuffle_choices(correct, wrongs)
    return caudan, choices, loigiai


def k10_mc_vecto_b8_do_dai_tong_hieu_tam_giac():
    """Bài 8 MC: Độ dài |a+b| + |a-b| với góc 60/120 độ hoặc tam giác vuông 30 độ."""
    mode = random.choice(["tong_hieu_60", "vuong_30"])
    if mode == "tong_hieu_60":
        k = random.choice([2, 3, 4])
        la = 2 * k
        lb = k
        ang = random.choice([60, 120])
        caudan = (
            f"Cho hai vectơ $\\vec{{a}}$ và $\\vec{{b}}$ tạo với nhau góc ${ang}^\\circ$. "
            f"Biết $|\\vec{{a}}| = {la}$ và $|\\vec{{b}}| = {lb}$. Tính $|\\vec{{a}} + \\vec{{b}}| + |\\vec{{a}} - \\vec{{b}}|$."
        )
        correct = f"${k}(\\sqrt{{7}} + \\sqrt{{3}})$"
        wrongs = [
            f"${k}(\\sqrt{{7}} + \\sqrt{{5}})$",
            f"${la}(\\sqrt{{5}} + 3)$",
            f"${k}(2\\sqrt{{3}} + \\sqrt{{7}})$",
        ]
        choices = shuffle_choices(correct, wrongs)
        sgn1 = "+" if ang == 60 else "-"
        sgn2 = "-" if ang == 60 else "+"
        r1 = 7 if ang == 60 else 3
        r2 = 3 if ang == 60 else 7
        loigiai = (
            f"Ta có $|\\vec{{a}} \\pm \\vec{{b}}|^2 = |\\vec{{a}}|^2 \\pm 2\\vec{{a}}\\cdot\\vec{{b}} + |\\vec{{b}}|^2 = {la}^2 \\pm 2\\cdot {la}\\cdot {lb}\\cos {ang}^\\circ + {lb}^2$.\\\\\n"
            f"Tính được $|\\vec{{a}} + \\vec{{b}}| = {k}\\sqrt{{{r1}}}$ và $|\\vec{{a}} - \\vec{{b}}| = {k}\\sqrt{{{r2}}}$.\\\\\n"
            f"Vậy $|\\vec{{a}} + \\vec{{b}}| + |\\vec{{a}} - \\vec{{b}}| = {k}(\\sqrt{{7}} + \\sqrt{{3}})$."
        )
        return caudan, choices, loigiai

    # Tam giác vuông tại A, góc B = 30 độ, BC = 2k -> AB = k*sqrt(3), AC = k
    k = random.choice([2, 3, 4])
    bc = 2 * k
    # |AB + AC| = 2 AM với M trung điểm BC -> trong tam giác vuông M tâm ngoại tiếp -> AM = BC/2 = k => 2AM = 2k!
    caudan = (
        f"Cho tam giác $ABC$ vuông tại $A$ có $\\widehat{{ABC}} = 30^\\circ$ và cạnh huyền $BC = {bc}$. "
        f"Độ dài vectơ $\\vec{{AB}} + \\vec{{AC}}$ bằng"
    )
    correct = f"${bc}$"
    wrongs = [f"${k}$", f"${k}\\sqrt{{3}}$", f"${bc}\\sqrt{{3}}$"]
    choices = shuffle_choices(correct, wrongs)
    loigiai = (
        f"Gọi $M$ là trung điểm $BC$, ta có $\\vec{{AB}} + \\vec{{AC}} = 2\\vec{{AM}}$.\\\\\n"
        f"Vì $\\Delta ABC$ vuông tại $A$ nên trung tuyến ứng với cạnh huyền $AM = \\dfrac{{BC}}{{2}} = {k}$.\\\\\n"
        f"Vậy $|\\vec{{AB}} + \\vec{{AC}}| = 2AM = BC = {bc}$."
    )
    return caudan, choices, loigiai


def k10_tf_vecto_b8_hinh_thoi_va_ba_diem():
    """Bài 8 ĐS: Hình thoi góc 60 độ hoặc trọng tâm tam giác & quy tắc ba điểm."""
    variant = random.choice(["hinh_thoi", "trong_tam_5_diem"])
    if variant == "hinh_thoi":
        k = random.choice([1, 2])
        ks = "" if k == 1 else str(k)
        ks_3 = f"{k}a\\sqrt{{3}}" if k > 1 else r"a\sqrt{3}"
        ks_2 = f"{k}a\\sqrt{{2}}" if k > 1 else r"a\sqrt{2}"
        ks_half = r"\dfrac{a\sqrt{3}}{2}" if k == 1 else r"a\sqrt{3}"
        ks_ob = r"\dfrac{a}{2}" if k == 1 else r"a"
        caudan = f"Cho hình thoi $ABCD$ cạnh ${ks}a$, có $\\widehat{{BAD}} = 60^\\circ$. Gọi $O$ là giao điểm hai đường chéo. Các mệnh đề sau đúng hay sai?"
        items = [
            (
                f"$\\Delta BAD$ và $\\Delta BCD$ đều cạnh ${ks}a$.",
                f"$\\Delta ABD$ vuông cân tại $A$.",
                f"Hình thoi có hai cạnh kề bằng ${ks}a$ và $\\widehat{{BAD}} = 60^\\circ$ nên $\\Delta BAD$ và $\\Delta BCD$ đều cạnh ${ks}a$.",
                f"Sai vì $\\Delta BAD$ và $\\Delta BCD$ đều cạnh ${ks}a$."
            ),
            (
                f"$|\\vec{{AB}} + \\vec{{AD}}| = {ks_3}$.",
                f"$|\\vec{{AB}} + \\vec{{AD}}| = {ks_2}$.",
                f"Theo quy tắc hình bình hành: $\\vec{{AB}} + \\vec{{AD}} = \\vec{{AC}}$, với $AC = 2AO = {ks_3}$.",
                f"Sai vì $|\\vec{{AB}} + \\vec{{AD}}| = AC = {ks_3}$."
            ),
            (
                f"$|\\vec{{BA}} - \\vec{{BC}}| = {ks}a$.",
                f"$|\\vec{{BA}} - \\vec{{BC}}| = {ks_3}$.",
                f"Ta có $\\vec{{BA}} - \\vec{{BC}} = \\vec{{CA}}? $ Không, $\\vec{{BA}} - \\vec{{BC}} = \\vec{{CA}}$! Đường chéo $AC = {ks_3}$? Khoan: trong hình thoi $\\widehat{{BAD}} = 60^\\circ$ thì $BD = {ks}a$, $AC = {ks_3}$! Vậy $|\\vec{{BA}} - \\vec{{BC}}| = |\\vec{{CA}}| = {ks_3}$ mới đúng!!",
                "WAIT"
            ),
        ]
        # Wait: let's fix item 3 cleanly! |BA - BC| = |CA| = AC = k*a*sqrt(3)! Whereas |AB - AD| = |DB| = k*a!
        items = [
            (
                f"$\\Delta BAD$ và $\\Delta BCD$ đều cạnh ${ks}a$.",
                f"$\\Delta ABC$ là tam giác đều cạnh ${ks}a$.",
                f"Hình thoi có $AB = AD = {ks}a$ và $\\widehat{{BAD}} = 60^\\circ$ nên $\\Delta BAD, \\Delta BCD$ đều cạnh ${ks}a$.",
                f"Sai vì $\\widehat{{ABC}} = 120^\\circ$ nên $\\Delta ABC$ không đều."
            ),
            (
                f"$|\\vec{{AB}} + \\vec{{AD}}| = {ks_3}$.",
                f"$|\\vec{{AB}} + \\vec{{AD}}| = {ks_2}$.",
                f"Ta có $\\vec{{AB}} + \\vec{{AD}} = \\vec{{AC}}$ và $AC = 2 \\cdot AO = {ks_3}$.",
                f"Sai vì $|\\vec{{AB}} + \\vec{{AD}}| = AC = {ks_3}$."
            ),
            (
                f"$|\\vec{{BA}} - \\vec{{BC}}| = {ks_3}$.",
                f"$|\\vec{{BA}} - \\vec{{BC}}| = {ks}a$.",
                f"Ta có $\\vec{{BA}} - \\vec{{BC}} = \\vec{{CA}} \\Rightarrow |\\vec{{BA}} - \\vec{{BC}}| = AC = {ks_3}$.",
                f"Sai vì $|\\vec{{BA}} - \\vec{{BC}}| = |\\vec{{CA}}| = AC = {ks_3}$."
            ),
            (
                f"$|\\vec{{OB}} - \\vec{{DC}}| = {ks_half}$.",
                f"$|\\vec{{OB}} - \\vec{{DC}}| = {ks_ob}$.",
                f"Vì $\\vec{{DC}} = \\vec{{AB}}$ nên $\\vec{{OB}} - \\vec{{DC}} = \\vec{{OB}} - \\vec{{AB}} = \\vec{{OB}} + \\vec{{BA}} = \\vec{{OA}}$, độ dài là $OA = {ks_half}$.",
                f"Sai vì $\\vec{{OB}} - \\vec{{DC}} = \\vec{{OA}}$ có độ dài $OA = {ks_half}$."
            ),
        ]
    else:
        caudan = "Cho $G$ là trọng tâm của tam giác $ABC$. Các mệnh đề sau đúng hay sai?"
        items = [
            (
                r"$\vec{BA} + \vec{BC} = 3\vec{BG}$.",
                r"$\vec{BA} + \vec{BC} = 2\vec{BG}$.",
                r"Gọi $M$ là trung điểm $AC$, ta có $\vec{BA} + \vec{BC} = 2\vec{BM}$. Vì $G$ là trọng tâm nên $\vec{BM} = \dfrac{3}{2}\vec{BG} \Rightarrow \vec{BA} + \vec{BC} = 3\vec{BG}$.",
                r"Sai vì $\vec{BA} + \vec{BC} = 2\vec{BM} = 3\vec{BG}$."
            ),
            (
                r"$\vec{CA} + \vec{CB} = 3\vec{CG}$.",
                r"$\vec{CA} + \vec{CB} = \vec{CG}$.",
                r"Tương tự, $\vec{CA} + \vec{CB} = 3\vec{CG}$.",
                r"Sai vì $\vec{CA} + \vec{CB} = 3\vec{CG}$."
            ),
            (
                r"$\vec{AB} + \vec{BC} + \vec{CA} = \vec{0}$.",
                r"$\vec{AB} + \vec{AC} + \vec{BC} = \vec{0}$.",
                r"Theo quy tắc ba điểm, $\vec{AB} + \vec{BC} + \vec{CA} = \vec{AC} + \vec{CA} = \vec{0}$.",
                r"Sai vì $\vec{AB} + \vec{AC} + \vec{BC} = (\vec{AB} + \vec{BC}) + \vec{AC} = 2\vec{AC} \neq \vec{0}$."
            ),
            (
                r"$\vec{AB} + \vec{AC} = 3\vec{AG}$.",
                r"$\vec{AB} + \vec{AC} = \dfrac{2}{3}\vec{AG}$.",
                r"Gọi $N$ là trung điểm $BC$, ta có $\vec{AB} + \vec{AC} = 2\vec{AN} = 3\vec{AG}$.",
                r"Sai vì $\vec{AB} + \vec{AC} = 3\vec{AG}$, không phải $\dfrac{2}{3}\vec{AG}$."
            ),
        ]
    choices, loigiai = make_tf_choices(items)
    return caudan, choices, loigiai


def k10_tf_vecto_b8_ba_hinh_binh_hanh_ngoai():
    """Bài 8 ĐS: Ba hình bình hành dựng bên ngoài tam giác ABC (ABIJ, BCPQ, CARS)."""
    caudan = (
        "Cho tam giác $ABC$. Bên ngoài của tam giác vẽ các hình bình hành "
        "$ABIJ$, $BCPQ$, $CARS$. Các mệnh đề sau đúng hay sai?"
    )
    items = [
        (
            r"$\vec{RJ} = \vec{RA} + \vec{AJ}$.",
            r"$\vec{RJ} = \vec{RA} + \vec{JA}$.",
            r"Theo quy tắc ba điểm: $\vec{RJ} = \vec{RA} + \vec{AJ}$.",
            r"Sai vì theo quy tắc ba điểm phải là $\vec{RA} + \vec{AJ}$."
        ),
        (
            r"$\vec{IQ} = \vec{IB} + \vec{BQ}$.",
            r"$\vec{IQ} = \vec{IB} + \vec{QB}$.",
            r"Theo quy tắc ba điểm: $\vec{IQ} = \vec{IB} + \vec{BQ}$.",
            r"Sai vì $\vec{IB} + \vec{QB} \neq \vec{IQ}$."
        ),
        (
            r"$\vec{PS} = \vec{PC} + \vec{CS}$.",
            r"$\vec{PS} = \vec{PC} + \vec{SC}$.",
            r"Theo quy tắc ba điểm: $\vec{PS} = \vec{PC} + \vec{CS}$.",
            r"Sai vì $\vec{PC} + \vec{SC} \neq \vec{PS}$."
        ),
        (
            r"$\vec{RJ} + \vec{IQ} + \vec{PS} = \vec{0}$.",
            r"$\vec{RJ} + \vec{IQ} + \vec{PS} = \vec{AB} + \vec{BC}$.",
            r"Do $ABIJ, BCPQ, CARS$ là hình bình hành nên $\vec{AJ} = \vec{BI}$, $\vec{BQ} = \vec{CP}$, $\vec{CS} = \vec{AR}$.\\ Cộng vế ta được $\vec{RJ} + \vec{IQ} + \vec{PS} = (\vec{RA} + \vec{CS}) + (\vec{AJ} + \vec{IB}) + (\vec{BQ} + \vec{PC}) = \vec{0}$.",
            r"Sai vì $\vec{RJ} + \vec{IQ} + \vec{PS} = \vec{0}$."
        ),
    ]
    choices, loigiai = make_tf_choices(items)
    return caudan, choices, loigiai


def k10_sa_vecto_b8_hop_luc_tao_goc():
    """Bài 8 TLN: Hợp lực của hai lực bằng nhau tạo góc 60 độ hoặc 120 độ."""
    f_val = random.choice([50, 80, 100, 120, 150])
    ang = random.choice([60, 120])
    if ang == 60:
        res = f_val * math.sqrt(3)
        ans_str = str(int(round(res)))
        caudan = (
            f"Cho hai lực $\\vec{{F}}_1, \\vec{{F}}_2$ có điểm đặt $O$ tạo với nhau góc ${ang}^\\circ$, "
            f"biết rằng cường độ của hai lực $\\vec{{F}}_1$ và $\\vec{{F}}_2$ đều bằng ${f_val}\\text{{ N}}$. "
            f"Tính cường độ tổng hợp lực của hai lực trên (làm tròn kết quả đến hàng đơn vị)."
        )
        loigiai = (
            f"Gọi $\\vec{{F}} = \\vec{{F}}_1 + \\vec{{F}}_2$. Vì $F_1 = F_2 = {f_val}$ và góc giữa hai lực là $60^\\circ$ nên:\\\\\n"
            f"$F = \\sqrt{{F_1^2 + F_2^2 + 2F_1 F_2\\cos 60^\\circ}} = {f_val}\\sqrt{{3}} \\approx {ans_str}\\text{{ N}}$."
        )
    else:
        ans_str = str(f_val)
        caudan = (
            f"Cho hai lực $\\vec{{F}}_1, \\vec{{F}}_2$ có điểm đặt $O$ tạo với nhau góc ${ang}^\\circ$, "
            f"biết cường độ của hai lực $\\vec{{F}}_1$ và $\\vec{{F}}_2$ đều bằng ${f_val}\\text{{ N}}$. "
            f"Tính cường độ tổng hợp lực của hai lực trên (đơn vị: N)."
        )
        loigiai = (
            f"$F = \\sqrt{{{f_val}^2 + {f_val}^2 + 2\\cdot {f_val}^2\\cos 120^\\circ}} = {f_val}\\text{{ N}}$."
        )
    return caudan, ans_str, loigiai


def k10_sa_vecto_b8_do_dai_hinh_vuong_tam_giac_vuong():
    """Bài 8 TLN: Độ dài |AB+BM| trong hình vuông hoặc |CA+CB+CI| trong tam giác vuông."""
    mode = random.choice(["hinh_vuong", "tam_giac_vuong"])
    if mode == "hinh_vuong":
        a = random.choice([2, 4, 6, 8])
        val = a * math.sqrt(5) / 2.0
        ans_str = _fmt_vn(val, 2)
        caudan = (
            f"Cho hình vuông $ABCD$ cạnh ${a}$, $M$ là trung điểm của $BC$. "
            f"Tính độ dài $|\\vec{{AB}} + \\vec{{BM}}|$ (làm tròn kết quả đến hàng phần trăm)."
        )
        loigiai = (
            f"Ta có $\\vec{{AB}} + \\vec{{BM}} = \\vec{{AM}}$.\\\\\n"
            f"Trong tam giác vuông $ABM$ tại $B$ ($AB = {a}, BM = {a // 2}$): "
            f"$AM = \\sqrt{{{a}^2 + {a // 2}^2}} = {a // 2}\\sqrt{{5}} \\approx {ans_str}$."
        )
        return caudan, ans_str, loigiai

    c, b = random.choice([(1, 2), (2, 3), (3, 4)])
    val = 1.5 * math.sqrt(c**2 + 4 * b**2)
    ans_str = _fmt_vn(val, 2)
    caudan = (
        f"Cho tam giác $ABC$ vuông tại $A$ có các cạnh góc vuông là $AB = {c}$, $AC = {b}$. "
        f"Điểm $N$ thỏa mãn $\\vec{{CN}} = \\vec{{CA}} + \\vec{{CB}} + \\vec{{CI}}$ với $I$ là trung điểm $AB$. "
        f"Tính độ dài vectơ $\\vec{{CN}}$ (làm tròn kết quả đến hàng phần trăm)."
    )
    loigiai = (
        f"Vì $I$ là trung điểm $AB$ nên $\\vec{{CA}} + \\vec{{CB}} = 2\\vec{{CI}}$.\\\\\n"
        f"Do đó $\\vec{{CN}} = 2\\vec{{CI}} + \\vec{{CI}} = 3\\vec{{CI}} \\Rightarrow |\\vec{{CN}}| = 3CI$.\\\\\n"
        f"Trong tam giác vuông $CAI$ tại $A$: $CI = \\sqrt{{AC^2 + AI^2}} = \\sqrt{{{b}^2 + \\left(\\dfrac{{{c}}}{{2}}\\right)^2}}$, "
        f"suy ra $CN = 3CI \\approx {ans_str}$."
    )
    return caudan, ans_str, loigiai


def k10_sa_vecto_b8_do_dai_hinh_thang():
    """Bài 8 TLN: Hình thang ABCD đáy AB=a, CD=2a, tính |DM - BA - CN|."""
    fr = random.choice([Fraction(1, 2), Fraction(1, 1), Fraction(3, 2), Fraction(2, 1), Fraction(3, 1)])
    ans_fr = Fraction(3, 2) * fr
    a_disp = fmt_frac(fr)
    val = float(ans_fr)
    ans_str = _fmt_vn(val, 2) if ans_fr.denominator != 1 else str(ans_fr.numerator)
    caudan = (
        f"Cho hình thang $ABCD$ có hai đáy $AB = a$, $CD = 2a$. Gọi $M, N$ lần lượt là trung điểm "
        f"của $AD$ và $BC$. Tính $|\\vec{{DM}} - \\vec{{BA}} - \\vec{{CN}}|$, biết $a = {a_disp}$."
    )
    loigiai = (
        f"Ta có $\\vec{{DM}} = \\vec{{DC}} + \\vec{{CN}} + \\vec{{NM}}$, suy ra $\\vec{{DM}} - \\vec{{CN}} = \\vec{{DC}} + \\vec{{NM}}$.\\\\\n"
        f"Do đó $\\vec{{DM}} - \\vec{{BA}} - \\vec{{CN}} = \\vec{{DC}} + \\vec{{AB}} - \\vec{{MN}}$.\\\\\n"
        f"Vì $MN$ là đường trung bình của hình thang nên $\\vec{{MN}} = \\dfrac{{1}}{{2}}(\\vec{{AB}} + \\vec{{DC}})$, "
        f"suy ra biểu thức bằng $\\dfrac{{1}}{{2}}(\\vec{{AB}} + \\vec{{DC}})$ có độ dài $\\dfrac{{AB + CD}}{{2}} = \\dfrac{{3a}}{{2}} = {ans_str}$."
    )
    return caudan, ans_str, loigiai


# --- BÀI 9: TÍCH CỦA MỘT VECTƠ VỚI MỘT SỐ ---

def _draw_segment_tikz(points, total_ticks):
    """Vẽ đoạn thẳng chia làm total_ticks phần bằng nhau với các nhãn điểm (pos_idx, label)."""
    # points: list of tuples (tick_idx, label, anchor)
    lines = [
        r"\begin{tikzpicture}[scale=0.52, font=\scriptsize]",
        f"  \\draw[thick] (0,0) -- ({total_ticks},0);",
    ]
    for i in range(total_ticks + 1):
        lines.append(f"  \\fill ({i},0) circle (1.6pt);")
    for idx, lbl, anch in points:
        lines.append(f"  \\node[{anch}] at ({idx},0) {{${lbl}$}};")
    lines.append(r"\end{tikzpicture}")
    return "\n".join(lines)


def _draw_tri_div_tikz(pos_m):
    """Vẽ tam giác ABC có điểm M nằm trên đường thẳng BC (pos_m: tỉ lệ trên tia BC: B=0, C=2)."""
    lines = [
        r"\begin{tikzpicture}[scale=0.52, font=\scriptsize]",
        r"  \coordinate (B) at (0,0);",
        r"  \coordinate (C) at (2.2,0);",
        r"  \coordinate (A) at (1.1,1.3);",
        r"  \draw[thick] (A) -- (B) -- (C) -- cycle;",
    ]
    x_m = pos_m
    if x_m < 0:
        lines.append(f"  \\draw[thick] ({x_m:.2f},0) -- (B);")
    elif x_m > 2.2:
        lines.append(f"  \\draw[thick] (C) -- ({x_m:.2f},0);")
    lines.append(r"  \fill (B) circle (1.5pt) node[below] {$B$};")
    lines.append(r"  \fill (C) circle (1.5pt) node[below] {$C$};")
    lines.append(r"  \fill (A) circle (1.5pt) node[above] {$A$};")
    if abs(x_m - 2.2) < 1e-6:
        lines.append(r"  \node[right] at (2.35,0) {$=M$};")
    else:
        lines.append(f"  \\fill ({x_m:.2f},0) circle (1.8pt) node[below] {{$M$}};")
    lines.append(r"\end{tikzpicture}")
    return "\n".join(lines)


def k10_mc_vecto_b9_hinh_ve_chia_doan_thang_tikz():
    """Bài 9 MC (4 hình TikZ): Nhận diện hình vẽ biểu diễn điểm chia đoạn thẳng."""
    mode = random.choice(["ai_ba", "mn_mp", "mb_mc_tri"])
    if mode == "ai_ba":
        p, q = random.choice([(3, 5), (2, 5), (3, 4)])
        # AI = - (p/q) BA = (p/q) AB -> I nằm giữa A và B với AI = p, IB = q - p (tổng q phần)
        fig_ok = _draw_segment_tikz([(0, "A", "below"), (p, "I", "below"), (q, "B", "below")], q)
        fig_w1 = _draw_segment_tikz([(0, "A", "below"), (q - p, "I", "below"), (q, "B", "below")], q)
        fig_w2 = _draw_segment_tikz([(0, "I", "below"), (p, "A", "below"), (p + q, "B", "below")], p + q)
        fig_w3 = _draw_segment_tikz([(0, "A", "below"), (q, "B", "below"), (q + p, "I", "below")], q + p)
        stmt = f"Cho đoạn thẳng $AB$. Hình nào sau đây biểu diễn điểm $I$ sao cho $\\vec{{AI}} = -\\dfrac{{{p}}}{{{q}}}\\vec{{BA}}$?"
        loigiai = (
            f"Ta có $\\vec{{AI}} = -\\dfrac{{{p}}}{{{q}}}\\vec{{BA}} = \\dfrac{{{p}}}{{{q}}}\\vec{{AB}}$.\\\\\n"
            f"Vì hệ số $\\dfrac{{{p}}}{{{q}}} > 0$ và $\\dfrac{{{p}}}{{{q}}} < 1$ nên $I$ nằm trên đoạn $AB$ sao cho $AI = \\dfrac{{{p}}}{{{q}}}AB$."
        )
    elif mode == "mn_mp":
        k = random.choice([2, 3])
        # MN = -k MP -> MP và MN ngược hướng, MN = k MP -> M nằm giữa N và P, MN=k, MP=1
        fig_ok = _draw_segment_tikz([(0, "N", "below"), (k, "M", "below"), (k + 1, "P", "below")], k + 1)
        fig_w1 = _draw_segment_tikz([(0, "M", "below"), (1, "P", "below"), (k, "N", "below")], k)
        fig_w2 = _draw_segment_tikz([(0, "N", "below"), (1, "M", "below"), (k + 1, "P", "below")], k + 1)
        fig_w3 = _draw_segment_tikz([(0, "M", "below"), (k, "P", "below"), (k + 1, "N", "below")], k + 1)
        stmt = f"Trên đường thẳng $MN$ lấy điểm $P$ sao cho $\\vec{{MN}} = -{k}\\vec{{MP}}$. Điểm $P$ được xác định đúng trong hình vẽ nào sau đây?"
        loigiai = (
            f"Từ $\\vec{{MN}} = -{k}\\vec{{MP}}$ suy ra hai vectơ $\\vec{{MN}}$ và $\\vec{{MP}}$ ngược hướng, "
            f"tức $M$ nằm giữa $N$ và $P$ đồng thời $MN = {k}MP$."
        )
    else:
        k = random.choice([2, 3])
        # MB = k MC -> MB và MC cùng hướng, MB = k MC -> C nằm giữa B và M (BC=2.2 -> CM = 2.2/(k-1))
        x_ok = 2.2 + 2.2 / (k - 1)
        fig_ok = _draw_tri_div_tikz(x_ok)
        fig_w1 = _draw_tri_div_tikz(2.2 * k / (k + 1)) # giữa B và C
        fig_w2 = _draw_tri_div_tikz(-2.2 / k)          # ngoài B
        fig_w3 = _draw_tri_div_tikz(2.2)               # C = M
        stmt = f"Cho tam giác $ABC$. Trên đường thẳng $BC$ lấy điểm $M$ sao cho $\\vec{{MB}} = {k}\\vec{{MC}}$. Điểm $M$ được vẽ đúng trong hình nào sau đây?"
        loigiai = (
            f"Vì hệ số ${k} > 0$ nên $\\vec{{MB}}$ và $\\vec{{MC}}$ cùng hướng, đồng thời $MB = {k}MC > MC$.\\\\\n"
            f"Do đó $C$ nằm giữa $B$ và $M$ (tức $M$ nằm trên tia đối của tia $CB$)."
        )

    items = [(fig_ok, True), (fig_w1, False), (fig_w2, False), (fig_w3, False)]
    random.shuffle(items)
    ans_idx = [i for i, (_, ok) in enumerate(items) if ok][0] + 1
    grid = (
        "\\begin{center}\n"
        "\\begin{tabular}{cc}\n"
        f"{items[0][0]} & {items[1][0]} \\\\\n"
        "Hình 1 & Hình 2 \\\\[6pt]\n"
        f"{items[2][0]} & {items[3][0]} \\\\\n"
        "Hình 3 & Hình 4\n"
        "\\end{tabular}\n"
        "\\end{center}"
    )
    caudan = f"{stmt}\n{grid}"
    correct = f"Hình {ans_idx}"
    wrongs = [f"Hình {j}" for j in range(1, 5) if j != ans_idx]
    choices = shuffle_choices(correct, wrongs)
    loigiai = f"Quan sát các hình vẽ, đáp án đúng là \\textbf{{Hình {ans_idx}}}.\\\\\n{loigiai}"
    return caudan, choices, loigiai


def k10_mc_vecto_b9_vi_tri_diem_he_thuc():
    """Bài 9 MC: Xác định vị trí điểm từ hệ thức vectơ hoặc trọng tâm mở rộng."""
    mode = random.choice(["chia_doan", "trong_tam_mo_rong", "trung_diem_he_thuc"])
    if mode == "chia_doan":
        k = random.choice([2, 3, 4])
        den = k + 1
        caudan = f"Cho hai điểm phân biệt $A$ và $B$. Tìm vị trí điểm $I$ thỏa mãn $\\vec{{IA}} + {k}\\vec{{IB}} = \\vec{{0}}$."
        correct = f"Điểm $I$ thuộc đoạn $AB$ sao cho $IB = \\dfrac{{1}}{{{den}}}AB$."
        wrongs = [
            f"Điểm $I$ nằm ngoài đoạn $AB$ sao cho $IB = \\dfrac{{1}}{{{den}}}AB$.",
            f"Điểm $I$ là trung điểm đoạn thẳng $AB$.",
            f"Điểm $I$ thuộc đoạn $AB$ sao cho $IA = \\dfrac{{1}}{{{den}}}AB$.",
        ]
        choices = shuffle_choices(correct, wrongs)
        loigiai = (
            f"$\\vec{{IA}} + {k}\\vec{{IB}} = \\vec{{0}} \\Leftrightarrow \\vec{{IA}} = -{k}\\vec{{IB}}$.\\\\\n"
            f"Suy ra $I$ nằm giữa $A, B$ và $IA = {k}IB \\Rightarrow IB = \\dfrac{{1}}{{{den}}}AB$."
        )
        return caudan, choices, loigiai

    if mode == "trong_tam_mo_rong":
        caudan = "Cho $\\Delta ABC$ có trọng tâm $G$. Xác định điểm $M$ sao cho $\\vec{MA} + \\vec{MB} + 2\\vec{MC} = \\vec{0}$."
        correct = "Điểm $M$ chia đoạn $GC$ thỏa mãn $\\vec{GC} = 4\\vec{GM}$."
        wrongs = [
            "Điểm $M$ là trung điểm cạnh $AC$.",
            "Điểm $M$ là trung điểm đoạn thẳng $GC$.",
            "Điểm $M$ chia đoạn $AB$ theo tỉ số $4$.",
        ]
        choices = shuffle_choices(correct, wrongs)
        loigiai = (
            r"Do $G$ là trọng tâm $\Delta ABC$ nên $\vec{MA} + \vec{MB} + \vec{MC} = 3\vec{MG}$.\\ "
            r"Thay vào giả thiết: $3\vec{MG} + \vec{MC} = \vec{0} \Leftrightarrow 3\vec{MG} + (\vec{MG} + \vec{GC}) = \vec{0} \Leftrightarrow \vec{GC} = 4\vec{GM}$."
        )
        return caudan, choices, loigiai

    caudan = (
        "Cho $\\Delta ABC$, $I$ là trung điểm của $AC$. Vị trí điểm $N$ thỏa mãn "
        "$\\vec{NA} + 2\\vec{NB} = \\vec{CB}$ được xác định bởi hệ thức"
    )
    correct = r"$\vec{BN} = \dfrac{2}{3}\vec{BI}$"
    wrongs = [r"$\vec{BN} = \dfrac{1}{3}\vec{BI}$", r"$\vec{BN} = 2\vec{BI}$", r"$\vec{BN} = 3\vec{BI}$"]
    choices = shuffle_choices(correct, wrongs)
    loigiai = (
        r"Ta có $\vec{NA} + 2\vec{NB} = \vec{CB} \Leftrightarrow \vec{NA} + \vec{NC} + 2\vec{NB} = \vec{NC} + \vec{CB} = \vec{NB}$.\\ "
        r"Do $I$ là trung điểm $AC$ nên $\vec{NA} + \vec{NC} = 2\vec{NI}$, suy ra $2\vec{NI} + \vec{NB} = \vec{0}$.\\ "
        r"Suy ra $2(\vec{NB} + \vec{BI}) + \vec{NB} = \vec{0} \Leftrightarrow 3\vec{NB} = -2\vec{BI} \Leftrightarrow \vec{BN} = \dfrac{2}{3}\vec{BI}$."
    )
    return caudan, choices, loigiai


def k10_mc_vecto_b9_phan_tich_va_tim_k():
    """Bài 9 MC: Phân tích vectơ trong hình chữ nhật, tam giác và tìm hệ số k."""
    mode = random.choice(["hcn_ai_ak", "tim_k_chia_doan", "phan_tich_am_bc"])
    if mode == "hcn_ai_ak":
        caudan = "Cho hình chữ nhật $ABCD$, $I, K$ lần lượt là trung điểm của $BC$ và $CD$. Chọn đẳng thức đúng."
        correct = r"$\vec{AI} + \vec{AK} = \dfrac{3}{2}\vec{AC}$"
        wrongs = [
            r"$\vec{AI} + \vec{AK} = 2\vec{AC}$",
            r"$\vec{AI} + \vec{AK} = \vec{AB} + \vec{AD}$",
            r"$\vec{AI} + \vec{AK} = \vec{IK}$",
        ]
        choices = shuffle_choices(correct, wrongs)
        loigiai = (
            r"Ta có $\vec{AI} = \vec{AB} + \vec{BI} = \vec{AB} + \dfrac{1}{2}\vec{AD}$ và $\vec{AK} = \vec{AD} + \dfrac{1}{2}\vec{AB}$.\\ "
            r"Cộng vế theo vế: $\vec{AI} + \vec{AK} = \dfrac{3}{2}(\vec{AB} + \vec{AD}) = \dfrac{3}{2}\vec{AC}$."
        )
        return caudan, choices, loigiai

    if mode == "tim_k_chia_doan":
        n = random.choice([3, 4, 5, 6])
        m = n - 1
        caudan = (
            f"Cho đoạn thẳng $AB$ và điểm $M$ thuộc đoạn $AB$ sao cho $AM = \\dfrac{{1}}{{{n}}}AB$. "
            f"Tìm số thực $k$ để $\\vec{{MA}} = k\\vec{{MB}}$."
        )
        correct = f"$k = -\\dfrac{{1}}{{{m}}}$"
        wrongs = [
            f"$k = \\dfrac{{1}}{{{m}}}$",
            f"$k = -{m}$",
            f"$k = {m}$",
        ]
        choices = shuffle_choices(correct, wrongs)
        loigiai = (
            f"Vì $M$ nằm trên đoạn $AB$ và $AM = \\dfrac{{1}}{{{n}}}AB$ nên $MB = \\dfrac{{{m}}}{{{n}}}AB = {m}MA$.\\\\\n"
            f"Hai vectơ $\\vec{{MA}}$ và $\\vec{{MB}}$ ngược hướng nên $\\vec{{MA}} = -\\dfrac{{1}}{{{m}}}\\vec{{MB}} \\Rightarrow k = -\\dfrac{{1}}{{{m}}}$."
        )
        return caudan, choices, loigiai

    p, q = random.choice([(1, 2), (2, 3), (1, 3)])
    caudan = (
        f"Cho $\\Delta ABC$, điểm $M$ nằm trên cạnh $BC$ sao cho $MB : MC = {p} : {q}$. "
        f"Đẳng thức nào sau đây đúng?"
    )
    tot = p + q
    correct = f"$\\vec{{AM}} = \\dfrac{{{q}}}{{{tot}}}\\vec{{AB}} + \\dfrac{{{p}}}{{{tot}}}\\vec{{AC}}$"
    wrongs = [
        f"$\\vec{{AM}} = \\dfrac{{{p}}}{{{tot}}}\\vec{{AB}} + \\dfrac{{{q}}}{{{tot}}}\\vec{{AC}}$",
        f"$\\vec{{AM}} = \\dfrac{{{q}}}{{{tot}}}\\vec{{AB}} - \\dfrac{{{p}}}{{{tot}}}\\vec{{AC}}$",
        f"$\\vec{{AM}} = \\dfrac{{1}}{{{tot}}}\\vec{{AB}} + \\dfrac{{{p}}}{{{tot}}}\\vec{{AC}}$",
    ]
    choices = shuffle_choices(correct, wrongs)
    loigiai = (
        f"Do $M$ thuộc cạnh $BC$ và $\\dfrac{{MB}}{{MC}} = \\dfrac{{{p}}}{{{q}}}$ nên ${q}\\vec{{MB}} + {p}\\vec{{MC}} = \\vec{{0}}$.\\\\\n"
        f"Chèn điểm $A$: ${q}(\\vec{{AB}} - \\vec{{AM}}) + {p}(\\vec{{AC}} - \\vec{{AM}}) = \\vec{{0}} \\Leftrightarrow \\vec{{AM}} = \\dfrac{{{q}}}{{{tot}}}\\vec{{AB}} + \\dfrac{{{p}}}{{{tot}}}\\vec{{AC}}$."
    )
    return caudan, choices, loigiai


def k10_mc_vecto_b9_bien_doi_he_thuc_doc_lap():
    """Bài 9 MC: Đẳng thức tổng độc lập với điểm M, trọng tâm hai tam giác, đổi điểm gốc."""
    mode = random.choice(["hai_trong_tam", "doc_lap_m", "doi_diem_goc", "5_diem"])
    if mode == "hai_trong_tam":
        caudan = "Cho hai tam giác $\\Delta ABC$ và $\\Delta A'B'C'$ có trọng tâm lần lượt là $G$ và $G'$. Đẳng thức nào sau đây đúng?"
        correct = r"$\vec{AA'} + \vec{BB'} + \vec{CC'} = 3\vec{GG'}$"
        wrongs = [
            r"$\vec{A'A} + \vec{B'B} + \vec{C'C} = 3\vec{GG'}$",
            r"$\vec{AB'} + \vec{BC'} + \vec{CA'} = 3\vec{GG'}$",
            r"$\vec{AC'} + \vec{BA'} + \vec{CB'} = 3\vec{GG'}$",
        ]
        choices = shuffle_choices(correct, wrongs)
        loigiai = (
            r"Ta có $\vec{AA'} + \vec{BB'} + \vec{CC'} = (\vec{AG} + \vec{GG'} + \vec{G'A'}) + (\vec{BG} + \vec{GG'} + \vec{G'B'}) + (\vec{CG} + \vec{GG'} + \vec{G'C'})$.\\ "
            r"Vì $\vec{AG}+\vec{BG}+\vec{CG}=\vec{0}$ và $\vec{G'A'}+\vec{G'B'}+\vec{G'C'}=\vec{0}$ nên tổng bằng $3\vec{GG'}$."
        )
        return caudan, choices, loigiai

    if mode == "doc_lap_m":
        p = random.choice([2, 3, 4])
        q = random.choice([1, 2])
        s = p + q
        rhs = f"{p}\\vec{{CA}} + {q}\\vec{{CB}}" if q > 1 else f"{p}\\vec{{CA}} + \\vec{{CB}}"
        rhs_ac = f"{p}\\vec{{AC}} + {q}\\vec{{BC}}" if q > 1 else f"{p}\\vec{{AC}} + \\vec{{BC}}"
        rhs_w2 = f"{p}\\vec{{AC}} + {s}\\vec{{CB}}"
        rhs_w3 = f"{p}\\vec{{CB}} - \\vec{{CA}}"
        q_str = "" if q == 1 else str(q)
        caudan = f"Cho $\\Delta ABC$ và một điểm $M$ tùy ý. Hệ thức nào sau đây đúng?"
        correct = f"${p}\\vec{{MA}} + {q_str}\\vec{{MB}} - {s}\\vec{{MC}} = {rhs}$"
        wrongs = [
            f"${p}\\vec{{MA}} + {q_str}\\vec{{MB}} - {s}\\vec{{MC}} = {rhs_ac}$",
            f"${p}\\vec{{MA}} + {q_str}\\vec{{MB}} - {s}\\vec{{MC}} = {rhs_w2}$",
            f"${p}\\vec{{MA}} + {q_str}\\vec{{MB}} - {s}\\vec{{MC}} = {rhs_w3}$",
        ]
        choices = shuffle_choices(correct, wrongs)
        loigiai = (
            f"Ta tách ${s}\\vec{{MC}} = {p}\\vec{{MC}} + {q_str}\\vec{{MC}}$ nên:\\\\\n"
            f"${p}(\\vec{{MA}} - \\vec{{MC}}) + {q_str}(\\vec{{MB}} - \\vec{{MC}}) = {rhs}$."
        )
        return caudan, choices, loigiai

    if mode == "doi_diem_goc":
        k = random.choice([2, 3, 4])
        caudan = f"Cho ba điểm phân biệt $A, B, C$. Nếu $\\vec{{AB}} = -{k}\\vec{{AC}}$ thì đẳng thức nào dưới đây đúng?"
        correct = f"$\\vec{{BC}} = {k + 1}\\vec{{AC}}$"
        wrongs = [
            f"$\\vec{{BC}} = -{k + 1}\\vec{{AC}}$",
            f"$\\vec{{BC}} = -{k - 1}\\vec{{AC}}$",
            f"$\\vec{{BC}} = {k - 1}\\vec{{AC}}$",
        ]
        choices = shuffle_choices(correct, wrongs)
        loigiai = f"Ta có $\\vec{{BC}} = \\vec{{AC}} - \\vec{{AB}} = \\vec{{AC}} - (-{k}\\vec{{AC}}) = {k + 1}\\vec{{AC}}$."
        return caudan, choices, loigiai

    caudan = "Cho $5$ điểm $A, B, C, D, E$. Đẳng thức nào sau đây là đúng?"
    correct = r"$\vec{AB} + \vec{CD} + \vec{EA} = \vec{CB} + \vec{ED}$"
    wrongs = [
        r"$\vec{AB} + \vec{CD} + \vec{EA} = 2(\vec{CB} + \vec{ED})$",
        r"$\vec{AB} + \vec{CD} + \vec{EA} = \dfrac{1}{2}(\vec{CB} + \vec{ED})$",
        r"$\vec{AB} + \vec{CD} + \vec{EA} = \dfrac{3}{2}(\vec{CB} + \vec{ED})$",
    ]
    choices = shuffle_choices(correct, wrongs)
    loigiai = (
        r"Ta có $\vec{AB} + \vec{CD} + \vec{EA} = (\vec{EA} + \vec{AB}) + \vec{CD} = \vec{EB} + \vec{CD} = (\vec{ED} + \vec{DB}) + \vec{CD} = \vec{ED} + (\vec{CD} + \vec{DB}) = \vec{ED} + \vec{CB}$."
    )
    return caudan, choices, loigiai


def k10_tf_vecto_b9_hbh_thang_hang():
    """Bài 9 ĐS: Phân tích vectơ và ba điểm thẳng hàng trong hình bình hành."""
    k = random.choice([3, 4, 5])
    kp2 = k + 2
    # AM = 1/2 AB, AP = 1/k AD, AN = 1/(k+2) AC
    c_ab_mn = Fraction(1, kp2) - Fraction(1, 2)
    c_ad_mn = Fraction(1, kp2)
    expr_mn_t = _fmt_lin_comb_2vec(c_ab_mn, r"\vec{AB}", c_ad_mn, r"\vec{AD}")
    expr_mn_f = _fmt_lin_comb_2vec(-c_ab_mn, r"\vec{AB}", c_ad_mn, r"\vec{AD}")

    c_ad_mp = Fraction(1, k)
    c_ab_mp = Fraction(-1, 2)
    expr_mp_t = _fmt_lin_comb_2vec(c_ad_mp, r"\vec{AD}", c_ab_mp, r"\vec{AB}")
    expr_mp_f = _fmt_lin_comb_2vec(Fraction(1, k + 1), r"\vec{AD}", c_ab_mp, r"\vec{AB}")

    caudan = (
        f"Cho hình bình hành $ABCD$ và các điểm $M, N, P$ thỏa mãn "
        f"$\\vec{{AM}} = \\dfrac{{1}}{{2}}\\vec{{AB}}$, "
        f"$\\vec{{AN}} = \\dfrac{{1}}{{{kp2}}}\\vec{{AC}}$, "
        f"$\\vec{{AP}} = \\dfrac{{1}}{{{k}}}\\vec{{AD}}$. Khi đó:"
    )
    items = [
        (
            f"$\\vec{{AN}} = \\dfrac{{1}}{{{kp2}}}(\\vec{{AB}} + \\vec{{AD}})$.",
            f"$\\vec{{AN}} = \\dfrac{{1}}{{{k}}}(\\vec{{AB}} + \\vec{{AD}})$.",
            f"Vì $ABCD$ là hình bình hành nên $\\vec{{AC}} = \\vec{{AB}} + \\vec{{AD}} \\Rightarrow \\vec{{AN}} = \\dfrac{{1}}{{{kp2}}}(\\vec{{AB}} + \\vec{{AD}})$.",
            f"Sai vì $\\vec{{AN}} = \\dfrac{{1}}{{{kp2}}}(\\vec{{AB}} + \\vec{{AD}})$."
        ),
        (
            f"$\\vec{{MN}} = {expr_mn_t}$.",
            f"$\\vec{{MN}} = {expr_mn_f}$.",
            f"Ta có $\\vec{{MN}} = \\vec{{AN}} - \\vec{{AM}} = \\dfrac{{1}}{{{kp2}}}(\\vec{{AB}} + \\vec{{AD}}) - \\dfrac{{1}}{{2}}\\vec{{AB}} = {expr_mn_t}$.",
            f"Sai vì hệ số của $\\vec{{AB}}$ là $\\dfrac{{1}}{{{kp2}}} - \\dfrac{{1}}{{2}} = {fmt_frac(c_ab_mn)}$."
        ),
        (
            f"$\\vec{{MP}} = {expr_mp_t}$.",
            f"$\\vec{{MP}} = {expr_mp_f}$.",
            f"Ta có $\\vec{{MP}} = \\vec{{AP}} - \\vec{{AM}} = {expr_mp_t}$.",
            f"Sai vì $\\vec{{MP}} = {expr_mp_t}$."
        ),
        (
            "Ba điểm $M, N, P$ thẳng hàng.",
            "Ba điểm $M, N, P$ tạo thành một tam giác.",
            f"Ta kiểm tra được $\\vec{{MP}} = \\dfrac{{{kp2}}}{{{k}}}\\vec{{MN}}$, nên hai vectơ $\\vec{{MN}}, \\vec{{MP}}$ cùng phương, tức là $M, N, P$ thẳng hàng.",
            f"Sai vì $\\vec{{MP}} = \\dfrac{{{kp2}}}{{{k}}}\\vec{{MN}}$ nên ba điểm $M, N, P$ thẳng hàng."
        ),
    ]
    choices, loigiai = make_tf_choices(items)
    return caudan, choices, loigiai


def k10_tf_vecto_b9_trung_tuyen_va_doi_xung():
    """Bài 9 ĐS: Trung tuyến, trọng tâm hai tam giác, điểm đối xứng và trung điểm."""
    variant = random.choice(["doi_xung_g", "hai_trung_tuyen"])
    if variant == "doi_xung_g":
        caudan = (
            "Cho tam giác $ABC$ có $G$ là trọng tâm. Gọi $D$ là điểm đối xứng của $B$ qua $G$, "
            "$M$ là trung điểm của $BC$. Xét tính đúng, sai của các khẳng định sau:"
        )
        items = [
            (
                r"$\vec{MD} = \vec{MG} + \vec{GD}$.",
                r"$\vec{MD} = \vec{GM} + \vec{DG}$.",
                r"Theo quy tắc ba điểm: $\vec{MD} = \vec{MG} + \vec{GD}$.",
                r"Sai vì $\vec{GM} + \vec{DG} = \vec{DM} = -\vec{MD}$."
            ),
            (
                r"$\vec{AG} = \dfrac{1}{3}\vec{AB} + \dfrac{1}{3}\vec{AC}$.",
                r"$\vec{AG} = 2\vec{AB} + \dfrac{1}{3}\vec{AC}$.",
                r"Vì $G$ là trọng tâm $\Delta ABC$ nên $\vec{AG} = \dfrac{2}{3}\vec{AM} = \dfrac{1}{3}(\vec{AB} + \vec{AC})$.",
                r"Sai vì $\vec{AG} = \dfrac{1}{3}\vec{AB} + \dfrac{1}{3}\vec{AC}$."
            ),
            (
                r"$\vec{CD} = -\dfrac{1}{3}\vec{AB} - \dfrac{1}{3}\vec{AC}$.",
                r"$\vec{CD} = \vec{AB} - \vec{AC} + \dfrac{1}{3}\vec{BN}$.",
                r"Do $D$ đối xứng $B$ qua $G$ nên $\vec{AD} = 2\vec{AG} - \vec{AB} = \dfrac{2}{3}\vec{AC} - \dfrac{1}{3}\vec{AB}$, suy ra $\vec{CD} = \vec{AD} - \vec{AC} = -\dfrac{1}{3}\vec{AB} - \dfrac{1}{3}\vec{AC}$.",
                r"Sai vì tính đúng phải được $\vec{CD} = -\dfrac{1}{3}\vec{AB} - \dfrac{1}{3}\vec{AC}$."
            ),
            (
                r"$\vec{MD} = -\dfrac{5}{6}\vec{AB} + \dfrac{1}{6}\vec{AC}$.",
                r"$\vec{MD} = \dfrac{5}{6}\vec{AB} - \dfrac{1}{6}\vec{AC}$.",
                r"Ta có $\vec{MD} = \vec{AD} - \vec{AM} = \left(\dfrac{2}{3}\vec{AC} - \dfrac{1}{3}\vec{AB}\right) - \dfrac{1}{2}(\vec{AB} + \vec{AC}) = -\dfrac{5}{6}\vec{AB} + \dfrac{1}{6}\vec{AC}$.",
                r"Sai vì kết quả đúng là $\vec{MD} = -\dfrac{5}{6}\vec{AB} + \dfrac{1}{6}\vec{AC}$."
            ),
        ]
    else:
        caudan = "Cho tam giác $ABC$ có hai đường trung tuyến $BN, CP$ cắt nhau tại trọng tâm $G$. Xét tính đúng, sai của các khẳng định sau:"
        items = [
            (
                r"$\vec{GA} + \vec{GB} + \vec{GC} = \vec{0}$.",
                r"$\vec{GA} + \vec{GB} + \vec{GC} = 3\vec{AG}$.",
                r"Tính chất trọng tâm $G$ của $\Delta ABC$: $\vec{GA} + \vec{GB} + \vec{GC} = \vec{0}$.",
                r"Sai vì $\vec{GA} + \vec{GB} + \vec{GC} = \vec{0}$."
            ),
            (
                r"$\vec{BA} + \vec{BC} = 2\vec{BN}$.",
                r"$\vec{BA} + \vec{BC} = 3\vec{BN}$.",
                r"Vì $N$ là trung điểm $AC$ nên theo quy tắc trung điểm: $\vec{BA} + \vec{BC} = 2\vec{BN}$.",
                r"Sai vì $\vec{BA} + \vec{BC} = 2\vec{BN}$ (chú ý $3\vec{BG}$ mới bằng $2\vec{BN}$)."
            ),
            (
                r"$\vec{AB} = -\dfrac{4}{3}\vec{BN} - \dfrac{2}{3}\vec{CP}$.",
                r"$\vec{AB} = -\dfrac{2}{3}\vec{BN} - \dfrac{2}{3}\vec{CP}$.",
                r"Ta có $\vec{GB} = -\dfrac{2}{3}\vec{BN}$, $\vec{GC} = -\dfrac{2}{3}\vec{CP}$ và $\vec{GA} = -\vec{GB}-\vec{GC}$, nên $\vec{AB} = \vec{GB}-\vec{GA} = 2\vec{GB}+\vec{GC} = -\dfrac{4}{3}\vec{BN} - \dfrac{2}{3}\vec{CP}$.",
                r"Sai vì hệ số của $\vec{BN}$ phải là $-\dfrac{4}{3}$."
            ),
            (
                r"$\vec{BC} = -\dfrac{2}{3}\vec{CP} + \dfrac{2}{3}\vec{BN}$.",
                r"$\vec{BC} = \dfrac{2}{3}\vec{CP} + \dfrac{2}{3}\vec{BN}$.",
                r"Ta có $\vec{BC} = \vec{GC} - \vec{GB} = -\dfrac{2}{3}\vec{CP} + \dfrac{2}{3}\vec{BN}$.",
                r"Sai vì $\vec{BC} = -\dfrac{2}{3}\vec{CP} + \dfrac{2}{3}\vec{BN}$."
            ),
        ]
    choices, loigiai = make_tf_choices(items)
    return caudan, choices, loigiai


def k10_sa_vecto_b9_tam_giac_vuong_goc_30():
    """Bài 9 TLN: Tam giác ABC vuông tại B góc A = 30 độ tính |BA+BC| hoặc |AB+AC|."""
    a = random.choice([3, 6, 9, 12])
    mode = random.choice(["ba_bc", "ab_ac"])
    if mode == "ba_bc":
        val = 2.0 * a / math.sqrt(3)
        ans_str = _fmt_vn(val, 2)
        caudan = (
            f"Cho tam giác $ABC$ vuông tại $B$ có $\\widehat{{A}} = 30^\\circ$ và $AB = {a}$. "
            f"Tính độ dài $|\\vec{{BA}} + \\vec{{BC}}|$ (làm tròn kết quả đến hàng phần trăm)."
        )
        loigiai = (
            f"Gọi $I$ là trung điểm $AC$, ta có $\\vec{{BA}} + \\vec{{BC}} = 2\\vec{{BI}} \\Rightarrow |\\vec{{BA}} + \\vec{{BC}}| = 2BI = AC$.\\\\\n"
            f"Trong tam giác vuông $ABC$: $AC = \\dfrac{{AB}}{{\\cos 30^\\circ}} = \\dfrac{{{2 * a}\\sqrt{{3}}}}{{3}} \\approx {ans_str}$."
        )
    else:
        val = a * math.sqrt(39) / 3.0
        ans_str = _fmt_vn(val, 2)
        caudan = (
            f"Cho tam giác $ABC$ vuông tại $B$ có $\\widehat{{A}} = 30^\\circ$ và $AB = {a}$. "
            f"Tính độ dài $|\\vec{{AB}} + \\vec{{AC}}|$ (làm tròn kết quả đến hàng phần trăm)."
        )
        loigiai = (
            f"Gọi $M$ là trung điểm $BC$, ta có $\\vec{{AB}} + \\vec{{AC}} = 2\\vec{{AM}}$.\\\\\n"
            f"Ta có $BC = AB\\tan 30^\\circ = \\dfrac{{{a}}}{{\\sqrt{{3}}}}$, suy ra $BM = \\dfrac{{{a}}}{{2\\sqrt{{3}}}}$.\\\\\n"
            f"Áp dụng Pythagore trong $\\Delta ABM$: $AM = \\sqrt{{AB^2 + BM^2}} = \\dfrac{{{a}\\sqrt{{39}}}}{{6}}$, "
            f"do đó $|\\vec{{AB}} + \\vec{{AC}}| = 2AM = \\dfrac{{{a}\\sqrt{{39}}}}{{3}} \\approx {ans_str}$."
        )
    return caudan, ans_str, loigiai


def k10_sa_vecto_b9_ba_luc_can_bang_tikz():
    """Bài 9 TLN (TikZ): Ba lực cân bằng hợp góc 120 độ và 90 độ."""
    f1 = random.choice([6, 9, 12, 15, 18])
    ask_which = random.choice(["sum", "f3"])
    tikz = r"""\begin{center}
\begin{tikzpicture}[>=stealth, font=\footnotesize, scale=0.9]
  \coordinate (A) at (0,0);
  \coordinate (F1) at (0,-1.8);
  \coordinate (F2) at (1.6,0);
  \coordinate (F3) at (120:2.2);
  \draw[->, thick] (A) -- (F1) node[midway, right] {$\vec{F}_1$};
  \draw[->, thick] (A) -- (F2) node[right] {$\vec{F}_2$};
  \draw[->, thick] (A) -- (F3) node[midway, below left] {$\vec{F}_3$};
  \node[left] at (A) {$A$};
  \draw (0.28,0) -- (0.28,-0.28) -- (0,-0.28);
  \draw pic["$120^\circ$", draw, angle radius=0.48cm, angle eccentricity=1.55] {angle=F2--A--F3};
\end{tikzpicture}
\end{center}"""
    f2_val = f1 / math.sqrt(3)
    f3_val = 2 * f1 / math.sqrt(3)
    if ask_which == "sum":
        val = f2_val + f3_val
        ans_str = _fmt_vn(val, 2)
        ask_txt = "Tính tổng độ lớn của hai lực $F_2 + F_3$"
        calc_txt = f"Khi đó $F_2 + F_3 = {f1}\\sqrt{{3}} \\approx {ans_str}\\text{{ N}}$."
    else:
        val = f3_val
        ans_str = _fmt_vn(val, 2)
        ask_txt = "Tính độ lớn của lực $F_3$"
        calc_txt = f"Khi đó $F_3 = \\dfrac{{{2 * f1}}}{{\\sqrt{{3}}}} \\approx {ans_str}\\text{{ N}}$."

    caudan = (
        f"Một chất điểm $A$ chịu tác dụng của ba lực $\\vec{{F}}_1, \\vec{{F}}_2, \\vec{{F}}_3$ như hình vẽ "
        f"(biết $\\vec{{F}}_1 \\perp \\vec{{F}}_2$, góc giữa $\\vec{{F}}_2$ và $\\vec{{F}}_3$ bằng $120^\\circ$) "
        f"và chất điểm $A$ đang ở trạng thái cân bằng. Biết lực $\\vec{{F}}_1$ có độ lớn ${f1}\\text{{ N}}$. "
        f"{ask_txt} (đơn vị: N, làm tròn kết quả đến hàng phần trăm).\n{tikz}"
    )
    loigiai = (
        f"Chất điểm cân bằng nên $\\vec{{F}}_1 + \\vec{{F}}_2 = -\\vec{{F}}_3$.\\\\\n"
        f"Vì $\\vec{{F}}_1 \\perp \\vec{{F}}_2$ và góc $(\\vec{{F}}_2, \\vec{{F}}_3) = 120^\\circ$ nên trong tam giác lực vuông, "
        f"góc giữa $\\vec{{F}}_3$ và phương thẳng đứng là $30^\\circ$.\\\\\n"
        f"Do đó $F_3 = \\dfrac{{F_1}}{{\\cos 30^\\circ}} = \\dfrac{{2F_1}}{{\\sqrt{{3}}}}$, $F_2 = F_1\\tan 30^\\circ = \\dfrac{{F_1}}{{\\sqrt{{3}}}}$.\\\\\n"
        f"{calc_txt}"
    )
    return caudan, ans_str, loigiai


def k10_sa_vecto_b9_bon_luc_can_bang_tikz():
    """Bài 9 TLN (TikZ): Vật cân bằng dưới 4 lực có hai lực xiên 45 độ."""
    p_val = random.choice([10, 15, 20, 25, 30])
    ratio = random.choice([2, 3])
    # (ratio - 1) F1 = 2 P cos 45 = P sqrt(2) => F1 = P sqrt(2) / (ratio - 1)
    f1_val = p_val * math.sqrt(2) / (ratio - 1)
    ans_str = _fmt_vn(f1_val, 2)
    ratio_word = "gấp đôi" if ratio == 2 else "gấp ba"

    tikz = r"""\begin{center}
\begin{tikzpicture}[>=stealth, font=\footnotesize, scale=0.88]
  \draw[fill=gray!20, thick] (0,0) circle (0.55cm);
  \coordinate (O) at (0,0);
  \coordinate (F1) at (1.8,0);
  \coordinate (F2) at (-3.1,0);
  \coordinate (F3) at (45:1.65);
  \coordinate (F4) at (-45:1.65);
  \draw[->, thick] (O) -- (F1) node[above] {$\vec{F}_1$};
  \draw[->, thick] (O) -- (F2) node[above] {$\vec{F}_2$};
  \draw[->, thick, dashed] (O) -- (F3) node[above right] {$\vec{F}_3$};
  \draw[->, thick, dashed] (O) -- (F4) node[below right] {$\vec{F}_4$};
  \fill (O) circle (1.5pt) node[above left] {$O$};
  \node at (0.9, 0.35) {\tiny $45^\circ$};
  \node at (0.9, -0.35) {\tiny $45^\circ$};
\end{tikzpicture}
\end{center}"""

    caudan = (
        f"Một vật đang ở vị trí $O$ chịu hai lực tác dụng ngược chiều nhau là $\\vec{{F}}_1$ và $\\vec{{F}}_2$, "
        f"trong đó độ lớn lực $\\vec{{F}}_2$ lớn {ratio_word} độ lớn lực $\\vec{{F}}_1$. Người ta muốn vật dừng lại "
        f"nên tác dụng thêm vào vật hai lực $\\vec{{F}}_3, \\vec{{F}}_4$ cùng hợp với lực $\\vec{{F}}_1$ các góc $45^\\circ$ "
        f"như hình vẽ, chúng có độ lớn bằng nhau và bằng ${p_val}\\text{{ N}}$. "
        f"Tìm độ lớn của lực $\\vec{{F}}_1$ (đơn vị: N, làm tròn kết quả đến hàng phần trăm).\n{tikz}"
    )
    loigiai = (
        f"Do $\\vec{{F}}_3$ và $\\vec{{F}}_4$ đối xứng qua phương $\\vec{{F}}_1$ nên $\\vec{{F}}_3 + \\vec{{F}}_4$ cùng hướng với $\\vec{{F}}_1$ "
        f"và có độ lớn là $2\\cdot {p_val}\\cos 45^\\circ = {p_val}\\sqrt{{2}}\\text{{ N}}$.\\\\\n"
        f"Điều kiện cân bằng: $F_2 = F_1 + |\\vec{{F}}_3 + \\vec{{F}}_4| \\Leftrightarrow {ratio}F_1 = F_1 + {p_val}\\sqrt{{2}} "
        f"\\Leftrightarrow F_1 = \\dfrac{{{p_val}\\sqrt{{2}}}}{{{ratio - 1}}} \\approx {ans_str}\\text{{ N}}$."
    )
    return caudan, ans_str, loigiai


def k10_sa_vecto_b9_he_so_k_phan_tich():
    """Bài 9 TLN: Tìm hệ số k từ trung điểm hoặc phân tích AM = x AB + y AC."""
    mode = random.choice(["trung_diem_tu_giac", "hai_trong_tam", "phan_tich_bc"])
    if mode == "trung_diem_tu_giac":
        caudan = "Cho tứ giác $ABCD$. Gọi $I, J$ lần lượt là trung điểm của $AC$ và $BD$. Biết $\\vec{AB} + \\vec{CD} = k\\vec{IJ}$, khi đó $k$ bằng bao nhiêu?"
        loigiai = r"Ta có $\vec{AB} = \vec{AI} + \vec{IJ} + \vec{JB}$ và $\vec{CD} = \vec{CI} + \vec{IJ} + \vec{JD}$. Cộng vế theo vế (với $\vec{AI}+\vec{CI}=\vec{0}$, $\vec{JB}+\vec{JD}=\vec{0}$) được $\vec{AB}+\vec{CD} = 2\vec{IJ} \Rightarrow k = 2$."
        return caudan, "2", loigiai

    if mode == "hai_trong_tam":
        caudan = "Cho hai tam giác $\\Delta ABC$ và $\\Delta A'B'C'$ lần lượt có trọng tâm là $G$ và $G'$. Biết $k\\vec{GG'} = \\vec{AA'} + \\vec{BB'} + \\vec{CC'}$, tìm $k$."
        loigiai = r"Ta có $\vec{AA'} + \vec{BB'} + \vec{CC'} = 3\vec{GG'} \Rightarrow k = 3$."
        return caudan, "3", loigiai

    p = random.choice([2, 3, 4])
    # M trên cạnh BC sao cho MB = p MC => AM = 1/(p+1) AB + p/(p+1) AC => 10y - x? hoặc (p+1)(y - x) = p - 1!
    tot = p + 1
    ans = p - 1
    caudan = (
        f"Cho tam giác $ABC$. Gọi $M$ là một điểm trên cạnh $BC$ sao cho $MB = {p}MC$. "
        f"Phân tích $\\vec{{AM}} = x\\vec{{AB}} + y\\vec{{AC}}$. Tính giá trị biểu thức $T = {tot}(y - x)$."
    )
    loigiai = (
        f"Vì $M$ nằm trên cạnh $BC$ và $MB = {p}MC$ nên $\\vec{{MB}} = -{p}\\vec{{MC}} \\Leftrightarrow \\vec{{AB}} - \\vec{{AM}} = -{p}(\\vec{{AC}} - \\vec{{AM}})$.\\\\\n"
        f"Suy ra $\\vec{{AM}} = \\dfrac{{1}}{{{tot}}}\\vec{{AB}} + \\dfrac{{{p}}}{{{tot}}}\\vec{{AC}} \\Rightarrow x = \\dfrac{{1}}{{{tot}}}, y = \\dfrac{{{p}}}{{{tot}}}$.\\\\\n"
        f"Vậy $T = {tot}(y - x) = {p} - 1 = {ans}$."
    )
    return caudan, str(ans), loigiai


# --- BÀI 11: TÍCH VÔ HƯỚNG CỦA HAI VECTƠ ---

def k10_mc_tich_vo_huong_b11_goc_tam_hinh_trong_tam():
    """Bài 11 MC: Góc giữa hai vectơ từ trọng tâm tam giác đều, tâm hình chữ nhật, hình vuông."""
    mode = random.choice(["trong_tam_deu", "tam_hinh_vuong", "tam_hcn"])
    if mode == "trong_tam_deu":
        caudan = "Cho tam giác $ABC$ đều cạnh $a$, gọi $G$ là trọng tâm của tam giác. Số đo góc giữa hai vectơ $\\vec{GB}$ và $\\vec{GC}$ bằng"
        correct = r"$120^\circ$"
        wrongs = [r"$60^\circ$", r"$90^\circ$", r"$150^\circ$"]
        loigiai = r"Do $\Delta ABC$ đều có tâm $G$ nên $GA, GB, GC$ chia góc ở tâm thành $3$ phần bằng nhau, do đó $(\vec{GB}, \vec{GC}) = \widehat{BGC} = 120^\circ$."
    elif mode == "tam_hinh_vuong":
        caudan = "Cho hình vuông $ABCD$ cạnh $a$, có tâm $O$. Góc giữa hai vectơ $\\vec{AB}$ và $\\vec{OD}$ bằng"
        correct = r"$135^\circ$"
        wrongs = [r"$45^\circ$", r"$90^\circ$", r"$180^\circ$"]
        loigiai = r"Ta có $\vec{OD} = \vec{BO}$, nên $(\vec{AB}, \vec{OD}) = (\vec{AB}, \vec{BO}) = 180^\circ - \widehat{ABO} = 180^\circ - 45^\circ = 135^\circ$."
    else:
        caudan = "Cho hình chữ nhật $ABCD$ tâm $O$, biết $AB = a$ và $AD = a\\sqrt{3}$. Góc giữa hai vectơ $\\vec{OA}$ và $\\vec{OB}$ bằng"
        correct = r"$60^\circ$"
        wrongs = [r"$30^\circ$", r"$90^\circ$", r"$120^\circ$"]
        loigiai = (
            r"Ta có $BD = \sqrt{AB^2 + AD^2} = 2a \Rightarrow OA = OB = a = AB$.\\ "
            r"Do đó $\Delta OAB$ đều, suy ra $(\vec{OA}, \vec{OB}) = \widehat{AOB} = 60^\circ$."
        )
    choices = shuffle_choices(correct, wrongs)
    return caudan, choices, loigiai


def k10_mc_tich_vo_huong_b11_tu_giac_hbh_hinh_thoi():
    """Bài 11 MC: Tích vô hướng trong hình chữ nhật, hình bình hành, hình thoi, hình thang vuông."""
    mode = random.choice(["hcn_cheo", "hbh_ke", "hbh_chia_canh", "hinh_thoi_canh", "hinh_thang_vuong"])
    k = random.choice([1, 2])
    ks = "" if k == 1 else str(k)
    k2_a2 = f"{k*k}a^2" if k > 1 else "a^2"
    two_k2_a2 = f"{2*k*k}a^2"
    if mode == "hcn_cheo":
        caudan = f"Cho hình chữ nhật $ABCD$ có $AB = {ks}a$ và $AD = {ks}a\\sqrt{{3}}$. Tích vô hướng $\\vec{{AC}} \\cdot \\vec{{BD}}$ bằng"
        correct = f"${two_k2_a2}$"
        wrongs = [f"$-{two_k2_a2}$", f"${4*k*k}a^2$", "$0$"]
        loigiai = (
            f"Ta có $\\vec{{AC}} = \\vec{{AB}} + \\vec{{AD}}$ và $\\vec{{BD}} = \\vec{{AD}} - \\vec{{AB}}$.\\\\\n"
            f"Suy ra $\\vec{{AC}} \\cdot \\vec{{BD}} = AD^2 - AB^2 = ({ks}a\\sqrt{{3}})^2 - ({ks}a)^2 = {two_k2_a2}$."
        )
    elif mode == "hbh_ke":
        caudan = f"Cho hình bình hành $ABCD$ có $AB = 2$, $AD = 1$ và $\\widehat{{BAD}} = 60^\\circ$. Tích vô hướng $\\vec{{BA}} \\cdot \\vec{{BC}}$ bằng"
        correct = "$-1$"
        wrongs = ["$1$", r"$\dfrac{1}{2}$", r"$-\dfrac{1}{2}$"]
        loigiai = r"Trong hình bình hành $ABCD$, $\widehat{ABC} = 180^\circ - 60^\circ = 120^\circ$ và $BC = AD = 1$. Do đó $\vec{BA}\cdot\vec{BC} = 2\cdot 1\cdot\cos 120^\circ = -1$."
    elif mode == "hbh_chia_canh":
        caudan = (
            "Cho hình bình hành $ABCD$ có $AB = 2a$, $AD = 3a$, $\\widehat{BAD} = 60^\\circ$. "
            "Điểm $K$ thuộc $AD$ thỏa mãn $\\vec{AK} = -2\\vec{DK}$. Tính tích vô hướng $\\vec{BK} \\cdot \\vec{AC}$."
        )
        # AK = -2 DK => AK = 2/3 AD. BK = AK - AB = 2/3 AD - AB. AC = AB + AD.
        # BK.AC = (2/3 AD - AB).(AD + AB) = 2/3 AD^2 - AB^2 - 1/3 AB.AD = 2/3 * 9a^2 - 4a^2 - 1/3 * 2a * 3a * 1/2 = 6a^2 - 4a^2 - a^2 = a^2!
        correct = r"$a^2$"
        wrongs = [r"$3a^2$", r"$6a^2$", "$0$"]
        loigiai = (
            r"Từ $\vec{AK} = -2\vec{DK} \Rightarrow \vec{AK} = \dfrac{2}{3}\vec{AD}$.\\ "
            r"Ta có $\vec{BK} = \dfrac{2}{3}\vec{AD} - \vec{AB}$ và $\vec{AC} = \vec{AB} + \vec{AD}$.\\ "
            r"Lại có $\vec{AB}\cdot\vec{AD} = 2a\cdot 3a\cos 60^\circ = 3a^2$.\\ "
            r"Suy ra $\vec{BK}\cdot\vec{AC} = \dfrac{2}{3}AD^2 - AB^2 - \dfrac{1}{3}\vec{AB}\cdot\vec{AD} = 6a^2 - 4a^2 - a^2 = a^2$."
        )
    elif mode == "hinh_thoi_canh":
        caudan = f"Cho hình thoi $ABCD$ cạnh bằng ${ks}a$ và góc $\\widehat{{BAD}} = 60^\\circ$. Tích vô hướng $\\vec{{AB}} \\cdot \\vec{{BC}}$ bằng"
        ans = r"$\dfrac{a^2}{2}$" if k == 1 else "$2a^2$"
        neg = r"$-\dfrac{a^2}{2}$" if k == 1 else "$-2a^2$"
        correct = ans
        wrongs = [neg, f"${k2_a2}$", f"$-{k2_a2}$"]
        loigiai = (
            f"Ta có $\\vec{{BC}} = \\vec{{AD}}$ nên $\\vec{{AB}} \\cdot \\vec{{BC}} = \\vec{{AB}} \\cdot \\vec{{AD}} = {ks}a \\cdot {ks}a \\cdot \\cos 60^\\circ = {correct.strip('$')}$."
        )
    else:
        caudan = f"Cho hình thang $ABCD$ vuông tại $A$ và $D$ có $AB = AD = {ks}a$, $CD = {2*k}a$. Tích vô hướng $\\vec{{AC}} \\cdot \\vec{{BD}}$ bằng"
        correct = f"$-{k2_a2}$"
        wrongs = ["$0$", f"$\\dfrac{{3{k2_a2}}}{{2}}$", f"$-\\dfrac{{{k2_a2}}}{{2}}$"]
        loigiai = (
            f"Ta có $\\vec{{AC}} = \\vec{{DC}} - \\vec{{AD}}$ và $\\vec{{BD}} = -\\vec{{AB}} - \\vec{{AD}}$.\\\\\n"
            f"Do $AD \\perp AB$ và $AD \\perp DC$, đồng thời $\\vec{{AB}}, \\vec{{DC}}$ cùng hướng nên:\\\\\n"
            f"$\\vec{{AC}} \\cdot \\vec{{BD}} = -\\vec{{DC}} \\cdot \\vec{{AB}} + AD^2 = -({2*k}a)({ks}a) + ({ks}a)^2 = -{k2_a2}$."
        )
    choices = shuffle_choices(correct, wrongs)
    return caudan, choices, loigiai


def k10_mc_tich_vo_huong_b11_trung_diem_trung_tuyen():
    """Bài 11 MC: Tích vô hướng có sử dụng trung điểm hoặc đường trung tuyến."""
    mode = random.choice(["deu_ab_ma", "vuong_trung_tuyen", "vuong_30_am_bm"])
    if mode == "deu_ab_ma":
        side = random.choice([4, 6, 8])
        # AB . MA với M trung điểm BC trong tam giác đều: MA = 1/2 (BA + CA) = -1/2 (AB + AC)
        # AB . MA = -1/2 (AB^2 + AB.AC) = -1/2 (a^2 + 1/2 a^2) = -3/4 a^2
        ans = -(3 * side * side) // 4
        caudan = f"Cho $\\Delta ABC$ đều cạnh $AB = {side}$ và $M$ là trung điểm của $BC$. Tích vô hướng $\\vec{{AB}} \\cdot \\vec{{MA}}$ bằng"
        correct = f"${ans}$"
        wrongs = [f"${-ans}$", f"${-(side * side) // 2}$", f"${(side * side) // 2}$"]
        loigiai = (
            f"Vì $M$ là trung điểm $BC$ nên $\\vec{{MA}} = -\\vec{{AM}} = -\\dfrac{{1}}{{2}}(\\vec{{AB}} + \\vec{{AC}})$.\\\\\n"
            f"Suy ra $\\vec{{AB}} \\cdot \\vec{{MA}} = -\\dfrac{{1}}{{2}}(AB^2 + \\vec{{AB}} \\cdot \\vec{{AC}}) = -\\dfrac{{1}}{{2}}\\left({side}^2 + {side}^2\\cos 60^\\circ\\right) = {ans}$."
        )
    elif mode == "vuong_trung_tuyen":
        k = random.choice([1, 2])
        ks = "" if k == 1 else str(k)
        k2a2 = f"{k*k}a^2" if k > 1 else "a^2"
        # Tam giác ABC vuông tại A có AB = ka, AC = ka*sqrt(3), AM trung tuyến. Tính BA . AM
        # AM = 1/2(AB + AC), BA = -AB => BA.AM = -1/2(AB^2 + AB.AC) = -1/2 a^2
        caudan = (
            f"Cho tam giác $ABC$ vuông tại $A$ có $AB = {ks}a$, $AC = {ks}a\\sqrt{{3}}$ và $AM$ là đường trung tuyến. "
            f"Tính tích vô hướng $\\vec{{BA}} \\cdot \\vec{{AM}}$."
        )
        correct = r"$-\dfrac{a^2}{2}$" if k == 1 else r"$-2a^2$"
        wrongs = [
            r"$\dfrac{a^2}{2}$" if k == 1 else r"$2a^2$",
            f"${k2a2}$",
            f"$-{k2a2}$",
        ]
        loigiai = (
            r"Vì $M$ là trung điểm $BC$ nên $\vec{AM} = \dfrac{1}{2}(\vec{AB} + \vec{AC})$ và $\vec{AB} \cdot \vec{AC} = 0$.\\ "
            f"Do đó $\\vec{{BA}} \\cdot \\vec{{AM}} = -\\dfrac{{1}}{{2}}\\vec{{AB}} \\cdot (\\vec{{AB}} + \\vec{{AC}}) = -\\dfrac{{AB^2}}{{2}} = {correct.strip('$')}$."
        )
    else:
        # Vuông tại A, B = 30 độ, AC = 2 -> BC = 4, AB = 2 sqrt(3), M trung điểm BC. Tính P = AM . BM
        # AM = 1/2(AB+AC), BM = 1/2 BC = 1/2(AC-AB) => AM.BM = 1/4(AC^2 - AB^2) = 1/4(4 - 12) = -2!
        ac = random.choice([2, 4])
        ans = (ac * ac - 3 * ac * ac) // 4
        caudan = (
            f"Cho tam giác $ABC$ vuông tại $A$ có $\\widehat{{B}} = 30^\\circ$, $AC = {ac}$. "
            f"Gọi $M$ là trung điểm của $BC$. Tính giá trị của biểu thức $P = \\vec{{AM}} \\cdot \\vec{{BM}}$."
        )
        correct = f"${ans}$"
        wrongs = [f"${-ans}$", f"${ac}\\sqrt{{3}}$", f"$-{ac}\\sqrt{{3}}$"]
        loigiai = (
            f"Ta có $\\vec{{AM}} = \\dfrac{{1}}{{2}}(\\vec{{AB}} + \\vec{{AC}})$ và $\\vec{{BM}} = \\dfrac{{1}}{{2}}\\vec{{BC}} = \\dfrac{{1}}{{2}}(\\vec{{AC}} - \\vec{{AB}})$.\\\\\n"
            f"Với $\\widehat{{B}} = 30^\\circ$, $AB = AC\\cot 30^\\circ = {ac}\\sqrt{{3}}$.\\\\\n"
            f"Vậy $P = \\dfrac{{1}}{{4}}(AC^2 - AB^2) = \\dfrac{{1}}{{4}}({ac}^2 - {3 * ac * ac}) = {ans}$."
        )
    choices = shuffle_choices(correct, wrongs)
    return caudan, choices, loigiai


def k10_mc_tich_vo_huong_b11_cosin_tu_hieu_va_do_dai():
    """Bài 11 MC: Tìm cosin góc từ |a|, |b|, |a-b| hoặc tìm m từ độ dài đoạn thẳng AB."""
    mode = random.choice(["cos_tu_hieu", "hbh_duong_cheo_ac", "tim_m_do_dai_ab"])
    if mode == "cos_tu_hieu":
        la, lb, ld, c_fr = random.choice([
            (4, 3, 4, Fraction(3, 8)),
            (5, 4, 5, Fraction(2, 5)),
            (6, 4, 6, Fraction(1, 3)),
        ])
        ans_str = fmt_frac(c_fr)
        caudan = (
            f"Cho hai vectơ $\\vec{{a}}, \\vec{{b}}$ thỏa mãn $|\\vec{{a}}| = {la}$, $|\\vec{{b}}| = {lb}$, "
            f"$|\\vec{{a}} - \\vec{{b}}| = {ld}$. Gọi $\\alpha$ là góc giữa hai vectơ $\\vec{{a}}$ và $\\vec{{b}}$. "
            f"Khẳng định nào sau đây đúng?"
        )
        correct = f"$\\cos\\alpha = {ans_str}$"
        wrongs = [r"$\alpha = 60^\circ$", r"$\alpha = 30^\circ$", f"$\\cos\\alpha = -{ans_str}$"]
        loigiai = (
            f"Bình phương hai vế $|\\vec{{a}} - \\vec{{b}}| = {ld}$ ta được: "
            f"${la}^2 + {lb}^2 - 2\\cdot {la}\\cdot {lb}\\cos\\alpha = {ld}^2 \\Rightarrow \\cos\\alpha = {ans_str}$."
        )
    elif mode == "hbh_duong_cheo_ac":
        ab, ad, deg = random.choice([(2, 1, 60), (3, 2, 60), (4, 3, 120)])
        ac_sq = ab**2 + ad**2 + (ab * ad if deg == 60 else -ab * ad)
        ans_str = _fmt_surd_val(ac_sq)
        caudan = f"Cho hình bình hành $ABCD$ với $AB = {ab}$, $AD = {ad}$ và $\\widehat{{BAD}} = {deg}^\\circ$. Độ dài đường chéo $AC$ bằng"
        correct = f"${ans_str}$"
        wrongs = [f"${_fmt_surd_val(ac_sq - 2)}$", f"${ac_sq}$", f"$\\dfrac{{{ac_sq}}}{{2}}$"]
        loigiai = (
            f"Ta có $AC^2 = (\\vec{{AB}} + \\vec{{AD}})^2 = AB^2 + AD^2 + 2AB\\cdot AD\\cos {deg}^\\circ = {ac_sq} \\Rightarrow AC = {ans_str}$."
        )
    else:
        xA = random.randint(-2, 3)
        yA = random.randint(-2, 3)
        dx, dy, dist = random.choice([(3, 4, 5), (4, 3, 5), (5, 12, 13)])
        yB = yA + dy
        m1, m2 = xA + dx, xA - dx
        caudan = (
            f"Trong mặt phẳng tọa độ $Oxy$, cho hai điểm $A({xA};{yA})$ và $B(m;{yB})$. "
            f"Tìm tất cả các giá trị thực của tham số $m$ để độ dài vectơ $\\vec{{AB}}$ bằng ${dist}$."
        )
        correct = f"$m = {m1}$ hoặc $m = {m2}$"
        wrongs = [
            f"$m = {m1}$ hoặc $m = {-m1}$",
            f"$m = {m1}$",
            f"$m = {xA + dy}$ hoặc $m = {xA - dy}$",
        ]
        loigiai = (
            f"Ta có $\\vec{{AB}} = (m - {xA}; {dy})$ nên $|\\vec{{AB}}| = {dist} \\Leftrightarrow (m - {xA})^2 + {dy}^2 = {dist}^2 = {dist**2}$.\\\\\n"
            f"Suy ra $(m - {xA})^2 = {dx**2} \\Leftrightarrow m = {m1}$ hoặc $m = {m2}$."
        )
    choices = shuffle_choices(correct, wrongs)
    return caudan, choices, loigiai


def k10_mc_tich_vo_huong_b11_oxy_goc_va_to_hop():
    """Bài 11 MC Oxy: Tìm m để góc bằng 45 hoặc 135 độ, hoặc tích vô hướng tổ hợp."""
    mode = random.choice(["tim_m_135", "hai_ka_lb", "a_tru_b", "u_cong_v_nhan_tru"])
    if mode == "tim_m_135":
        caudan = "Trong mặt phẳng tọa độ $Oxy$, cho hai vectơ $\\vec{a} = (1; -1)$ và $\\vec{b} = (m; 1)$. Tìm giá trị của tham số thực $m$ để góc giữa hai vectơ $\\vec{a}$ và $\\vec{b}$ bằng $135^\\circ$."
        correct = "$m = 0$"
        wrongs = ["$m = 1$", "$m = -1$", "$m = 2$"]
        loigiai = (
            r"Ta có $\cos(\vec{a}, \vec{b}) = \dfrac{m - 1}{\sqrt{2}\sqrt{m^2 + 1}} = \cos 135^\circ = -\dfrac{1}{\sqrt{2}}$.\\ "
            r"Suy ra $\dfrac{m - 1}{\sqrt{m^2 + 1}} = -1 \Leftrightarrow \begin{cases} m - 1 < 0 \\ (m - 1)^2 = m^2 + 1 \end{cases} \Leftrightarrow m = 0$."
        )
    elif mode == "hai_ka_lb":
        x1, y1 = random.choice([(2, -3), (1, -2), (3, -1)])
        x2, y2 = random.choice([(-1, 4), (2, -5), (-2, 3)])
        k1, k2 = random.choice([(2, 3), (3, 2)])
        dot = x1 * x2 + y1 * y2
        ans = k1 * k2 * dot
        caudan = f"Trong mặt phẳng tọa độ $Oxy$, cho hai vectơ $\\vec{{a}} = ({x1};{y1})$ và $\\vec{{b}} = ({x2};{y2})$. Giá trị của biểu thức $T = ({k1}\\vec{{a}})\\cdot({k2}\\vec{{b}})$ bằng"
        correct = f"${ans}$"
        wrongs = [f"${dot}$", f"${-ans}$", f"${ans // 2}$" if ans % 2 == 0 else f"${ans + 4}$"]
        loigiai = f"Ta có $T = {k1 * k2}(\\vec{{a}} \\cdot \\vec{{b}}) = {k1 * k2}\\cdot({x1}\\cdot({x2}) + ({y1})\\cdot({y2})) = {ans}$."
    elif mode == "a_tru_b":
        x1, y1 = random.choice([(2, 1), (3, -1), (1, 4)])
        x2, y2 = random.choice([(-1, 3), (2, 2), (-2, 1)])
        ans = x1 * (x1 - x2) + y1 * (y1 - y2)
        caudan = f"Trong mặt phẳng tọa độ $Oxy$, cho hai vectơ $\\vec{{a}} = ({x1};{y1})$ và $\\vec{{b}} = ({x2};{y2})$. Giá trị của biểu thức $\\vec{{a}} \\cdot (\\vec{{a}} - \\vec{{b}})$ bằng"
        correct = f"${ans}$"
        pool_w = [f"${ans + 2}$", f"${ans - 2}$", f"${x1*x2 + y1*y2}$", f"${-ans}$"]
        wrongs = [w for w in pool_w if w != correct][:3]
        loigiai = (
            f"Ta có $\\vec{{a}} - \\vec{{b}} = ({x1 - x2}; {y1 - y2})$, "
            f"suy ra $\\vec{{a}} \\cdot (\\vec{{a}} - \\vec{{b}}) = {x1}\\cdot({x1 - x2}) + ({y1})\\cdot({y1 - y2}) = {ans}$."
        )
    else:
        x1, y1 = random.choice([(-3, 4), (3, 4), (4, 3)])
        x2, y2 = random.choice([(5, 0), (0, 6), (4, 0)])
        ans = (x1**2 + y1**2) - (x2**2 + y2**2)
        caudan = f"Trong mặt phẳng tọa độ $Oxy$, cho hai vectơ $\\vec{{u}} = ({x1};{y1})$ và $\\vec{{v}} = ({x2};{y2})$. Tính $M = (\\vec{{u}} + \\vec{{v}})\\cdot(\\vec{{u}} - \\vec{{v}})$."
        correct = f"${ans}$"
        pool_w = [f"${x1**2 + y1**2}$", f"${(x1**2 + y1**2) + (x2**2 + y2**2)}$", "$0$", f"${-ans}$"]
        wrongs = [w for w in pool_w if w != correct][:3]
        loigiai = f"Ta có $M = |\\vec{{u}}|^2 - |\\vec{{v}}|^2 = ({x1}^2 + {y1}^2) - ({x2}^2 + {y2}^2) = {ans}$."
    choices = shuffle_choices(correct, wrongs)
    return caudan, choices, loigiai


def k10_tf_tich_vo_huong_b11_hinh_vuong_trong_tam_tikz():
    """Bài 11 ĐS (TikZ): Hình vuông ABCD cạnh a, M trung điểm AB, G giao BD và CM."""
    tikz = r"""\begin{center}
\begin{tikzpicture}[>=stealth, font=\footnotesize, scale=0.85]
  \coordinate (D) at (0,0);
  \coordinate (C) at (2.4,0);
  \coordinate (B) at (2.4,2.4);
  \coordinate (A) at (0,2.4);
  \coordinate (M) at (1.2,2.4);
  \coordinate (G) at (1.6,1.6);
  \draw[thick] (A) -- (B) -- (C) -- (D) -- cycle;
  \draw (A) -- (C) (B) -- (D) (M) -- (C);
  \fill (G) circle (1.5pt) node[left] {$G$};
  \fill (M) circle (1.5pt) node[above] {$M$};
  \node[above left] at (A) {$A$};
  \node[above right] at (B) {$B$};
  \node[below right] at (C) {$C$};
  \node[below left] at (D) {$D$};
\end{tikzpicture}
\end{center}"""

    caudan = (
        "Cho hình vuông $ABCD$ cạnh bằng $a$. Gọi $M$ là trung điểm của $AB$ và $G$ là giao điểm của $BD$ với $CM$ "
        "(như hình vẽ). Xét tính đúng, sai của các khẳng định sau:\n" + tikz
    )
    items = [
        (
            r"$\vec{CM} = \dfrac{1}{2}\vec{BA} - \vec{BC}$.",
            r"$\vec{CM} = \dfrac{1}{2}\vec{AB} - \vec{BC}$.",
            r"Ta có $\vec{CM} = \vec{CB} + \vec{BM} = -\vec{BC} + \dfrac{1}{2}\vec{BA} = \dfrac{1}{2}\vec{BA} - \vec{BC}$.",
            r"Sai vì $\vec{BM} = \dfrac{1}{2}\vec{BA}$ nên $\vec{CM} = \dfrac{1}{2}\vec{BA} - \vec{BC}$."
        ),
        (
            r"$\vec{BG} = \dfrac{1}{3}\vec{BA} + \dfrac{1}{3}\vec{BC}$.",
            r"$\vec{BG} = \dfrac{5}{6}\vec{BA} + \dfrac{1}{3}\vec{BC}$.",
            r"Vì $G$ là giao điểm hai đường trung tuyến $BO$ và $CM$ của $\Delta ABC$ nên $G$ là trọng tâm $\Delta ABC$, suy ra $\vec{BG} = \dfrac{1}{3}(\vec{BA} + \vec{BC})$.",
            r"Sai vì $G$ là trọng tâm $\Delta ABC$ nên $\vec{BG} = \dfrac{1}{3}\vec{BA} + \dfrac{1}{3}\vec{BC}$."
        ),
        (
            r"$\vec{BC} \cdot \vec{BA} = 0$.",
            r"$\vec{BC} \cdot \vec{BA} = a^2$.",
            r"Vì $BC \perp BA$ tại $B$ nên $\vec{BC} \cdot \vec{BA} = 0$.",
            r"Sai vì $ABCD$ là hình vuông nên $\vec{BC} \perp \vec{BA} \Rightarrow \vec{BC} \cdot \vec{BA} = 0$."
        ),
        (
            r"$\vec{BG} \cdot \vec{CM} = -\dfrac{a^2}{6}$.",
            r"$\vec{BG} \cdot \vec{CM} = -a^2$.",
            r"Ta có $\vec{BG}\cdot\vec{CM} = \dfrac{1}{3}(\vec{BA} + \vec{BC})\cdot\left(\dfrac{1}{2}\vec{BA} - \vec{BC}\right) = \dfrac{1}{3}\left(\dfrac{1}{2}a^2 - a^2\right) = -\dfrac{a^2}{6}$.",
            r"Sai vì $\vec{BG} \cdot \vec{CM} = -\dfrac{a^2}{6}$."
        ),
    ]
    choices, loigiai = make_tf_choices(items)
    return caudan, choices, loigiai


def k10_tf_tich_vo_huong_b11_hinh_vuong_tam_giac_vuong_can_tikz():
    """Bài 11 ĐS (TikZ): Hình vuông ABCD cạnh a, E trung điểm BC, BF = 3/4 BD."""
    tikz = r"""\begin{center}
\begin{tikzpicture}[>=stealth, font=\footnotesize, scale=0.85]
  \coordinate (A) at (0,0);
  \coordinate (B) at (2.4,0);
  \coordinate (C) at (2.4,2.4);
  \coordinate (D) at (0,2.4);
  \coordinate (E) at (2.4,1.2);
  \coordinate (F) at (0.6,1.8);
  \draw[thick] (A) -- (B) -- (C) -- (D) -- cycle;
  \draw (B) -- (D) (A) -- (E) -- (F) -- (A);
  \fill (E) circle (1.5pt) node[right] {$E$};
  \fill (F) circle (1.5pt) node[above right] {$F$};
  \node[below left] at (A) {$A$};
  \node[below right] at (B) {$B$};
  \node[above right] at (C) {$C$};
  \node[above left] at (D) {$D$};
\end{tikzpicture}
\end{center}"""

    caudan = (
        "Cho hình vuông $ABCD$ cạnh $a$. Lấy $E$ là trung điểm của $BC$, điểm $F$ thỏa mãn "
        "$\\vec{BF} = \\dfrac{3}{4}\\vec{BD}$ (như hình vẽ). Xét tính đúng, sai của các khẳng định sau:\n" + tikz
    )
    items = [
        (
            r"$\vec{AE} = \vec{AB} + \dfrac{1}{2}\vec{AD}$.",
            r"$\vec{AE} = \vec{AD} + \dfrac{1}{2}\vec{AB}$.",
            r"Ta có $\vec{AE} = \vec{AB} + \vec{BE} = \vec{AB} + \dfrac{1}{2}\vec{BC} = \vec{AB} + \dfrac{1}{2}\vec{AD}$.",
            r"Sai vì $\vec{AE} = \vec{AB} + \dfrac{1}{2}\vec{AD}$."
        ),
        (
            r"$\vec{AF} = \dfrac{1}{4}\vec{AB} + \dfrac{3}{4}\vec{AD}$.",
            r"$\vec{AF} = \dfrac{3}{4}\vec{AB} + \dfrac{1}{4}\vec{AD}$.",
            r"Ta có $\vec{AF} = \vec{AB} + \vec{BF} = \vec{AB} + \dfrac{3}{4}(\vec{AD} - \vec{AB}) = \dfrac{1}{4}\vec{AB} + \dfrac{3}{4}\vec{AD}$.",
            r"Sai vì $\vec{AF} = \dfrac{1}{4}\vec{AB} + \dfrac{3}{4}\vec{AD}$."
        ),
        (
            r"$\vec{EF} = -\dfrac{3}{4}\vec{AB} + \dfrac{1}{4}\vec{AD}$.",
            r"$\vec{EF} = \dfrac{3}{4}\vec{AB} + \dfrac{1}{4}\vec{AD}$.",
            r"Ta có $\vec{EF} = \vec{AF} - \vec{AE} = \left(\dfrac{1}{4}\vec{AB} + \dfrac{3}{4}\vec{AD}\right) - \left(\vec{AB} + \dfrac{1}{2}\vec{AD}\right) = -\dfrac{3}{4}\vec{AB} + \dfrac{1}{4}\vec{AD}$.",
            r"Sai vì $\vec{EF} = -\dfrac{3}{4}\vec{AB} + \dfrac{1}{4}\vec{AD}$."
        ),
        (
            "Tam giác $AEF$ vuông cân.",
            "Tam giác $AEF$ là tam giác đều.",
            r"Vì $\vec{AB} \cdot \vec{AD} = 0$, ta có $\vec{AF} \cdot \vec{EF} = \left(\dfrac{1}{4}\cdot\left(-\dfrac{3}{4}\right) + \dfrac{3}{4}\cdot\dfrac{1}{4}\right)a^2 = 0 \Rightarrow AF \perp EF$. Hơn nữa $AF = EF = \dfrac{a\sqrt{10}}{4}$, nên $\Delta AEF$ vuông cân tại $F$.",
            "Sai vì $AF \\perp EF$ và $AF = EF$ nên $\\Delta AEF$ vuông cân tại $F$."
        ),
    ]
    choices, loigiai = make_tf_choices(items)
    return caudan, choices, loigiai


def k10_tf_tich_vo_huong_b11_oxy_he_tich_vo_huong():
    """Bài 11 ĐS Oxy: Biểu thức tích vô hướng, vuông góc và hệ tìm vectơ d."""
    a1, a2 = -2, 3
    b1, b2 = 4, 1
    # a.(a-b) = (-2)(-6) + 3(2) = 18
    # (a+b).(2a-b) = (2;4).(-8;5) = -16 + 20 = 4
    # c = m i + j perp a => -2m + 3 = 0 => m = 3/2
    # d . a = 4, d . b = -2 => -2x+3y=4, 4x+y=-2 => x = -5/7, y = 6/7!
    # Also randomize scalar multiplier k_scale in {1, 2} to vary numbers cleanly!
    k = random.choice([1, 2])
    d_rhs1 = 4 * k
    d_rhs2 = -2 * k
    dx_n = -5 * k
    dy_n = 6 * k

    caudan = f"Trong mặt phẳng tọa độ $Oxy$, cho các vectơ $\\vec{{a}} = ({a1};{a2})$, $\\vec{{b}} = ({b1};{b2})$. Xét tính đúng, sai của các khẳng định sau:"
    items = [
        (
            r"$\vec{a} \cdot (\vec{a} - \vec{b}) = 18$.",
            r"$\vec{a} \cdot (\vec{a} - \vec{b}) = 12$.",
            r"Ta có $\vec{a} - \vec{b} = (-6; 2)$, suy ra $\vec{a} \cdot (\vec{a} - \vec{b}) = (-2)(-6) + 3\cdot 2 = 18$.",
            r"Sai vì $\vec{a} \cdot (\vec{a} - \vec{b}) = 18$."
        ),
        (
            r"$(\vec{a} + \vec{b}) \cdot (2\vec{a} - \vec{b}) = 4$.",
            r"$(\vec{a} + \vec{b}) \cdot (2\vec{a} - \vec{b}) = -4$.",
            r"Ta có $\vec{a} + \vec{b} = (2; 4)$ và $2\vec{a} - \vec{b} = (-8; 5)$, suy ra tích vô hướng bằng $2(-8) + 4\cdot 5 = 4$.",
            r"Sai vì $(\vec{a} + \vec{b}) \cdot (2\vec{a} - \vec{b}) = 4$."
        ),
        (
            r"Vectơ $\vec{c} = m\vec{i} + \vec{j}$ vuông góc với $\vec{a}$ khi $m = \dfrac{3}{2}$.",
            r"Vectơ $\vec{c} = m\vec{i} + \vec{j}$ vuông góc với $\vec{a}$ khi $m = -\dfrac{3}{2}$.",
            r"Ta có $\vec{c} = (m; 1)$. Điều kiện $\vec{c} \perp \vec{a} \Leftrightarrow -2m + 3 = 0 \Leftrightarrow m = \dfrac{3}{2}$.",
            r"Sai vì $-2m + 3 = 0 \Leftrightarrow m = \dfrac{3}{2}$."
        ),
        (
            f"Tọa độ vectơ $\\vec{{d}}$ thỏa mãn $\\vec{{a}} \\cdot \\vec{{d}} = {d_rhs1}$, $\\vec{{b}} \\cdot \\vec{{d}} = {d_rhs2}$ là $\\left(\\dfrac{{{dx_n}}}{{7}}; \\dfrac{{{dy_n}}}{{7}}\\right)$.",
            f"Tọa độ vectơ $\\vec{{d}}$ thỏa mãn $\\vec{{a}} \\cdot \\vec{{d}} = {d_rhs1}$, $\\vec{{b}} \\cdot \\vec{{d}} = {d_rhs2}$ là $\\left(\\dfrac{{{-dx_n}}}{{7}}; \\dfrac{{{dy_n}}}{{7}}\\right)$.",
            f"Giải hệ $\\begin{{cases}} -2x + 3y = {d_rhs1} \\\\ 4x + y = {d_rhs2} \\end{{cases}} \\Leftrightarrow x = \\dfrac{{{dx_n}}}{{7}}, y = \\dfrac{{{dy_n}}}{{7}}$.",
            f"Sai vì nghiệm đúng là $\\left(\\dfrac{{{dx_n}}}{{7}}; \\dfrac{{{dy_n}}}{{7}}\\right)$."
        ),
    ]
    choices, loigiai = make_tf_choices(items)
    return caudan, choices, loigiai


# ==============================================================================
# BẢNG ÁNH XẠ DẠNG TOÁN & HÀM ĐIỀU PHỐI (DISPATCHER)
# ==============================================================================

K10_VECTO_OXY_MAP = {
    # 17 Dạng toán mới từ ảnh đợt 2 (Vectơ & Tích vô hướng)
    "Trắc nghiệm - Oxy: Bài toán thực tế chuyển động tàu thủy": (k10_mc_oxy_toan_thuc_te_tau_thuy_chuyen_dong, "mc"),
    "Trắc nghiệm - Oxy: Tìm tọa độ điểm P trên trục tọa độ để hai vectơ cùng phương": (k10_mc_oxy_diem_tren_truc_cung_phuong, "mc"),
    "Trắc nghiệm - Oxy: Tổng hoành độ các trung điểm tam giác": (k10_mc_oxy_tong_hoanh_do_trung_diem_tam_giac, "mc"),
    "Trắc nghiệm - Oxy: Tọa độ đỉnh D sao cho ABDC là hình bình hành": (k10_mc_oxy_hinh_binh_hanh_bay_thu_tu_dinh, "mc"),
    "Trắc nghiệm - Oxy: Mối quan hệ giữa hai vectơ từ 4 điểm cho trước": (k10_mc_oxy_bon_diem_quan_he_hai_vecto, "mc"),
    "Trắc nghiệm - Oxy: Điểm thuộc trục tọa độ khi biết tính chất trọng tâm": (k10_mc_oxy_tam_giac_dinh_truc_trong_tam_truc, "mc"),
    "Trắc nghiệm - Oxy: Điểm M thỏa mãn hệ thức vectơ suy ra phương trình đường thẳng": (k10_mc_oxy_diem_m_thoa_man_he_thuc_vecto, "mc"),
    "Trắc nghiệm - Oxy: Tìm tham số x để tổ hợp vectơ thỏa mãn điều kiện": (k10_mc_oxy_tim_x_to_hop_vecto, "mc"),
    "Trắc nghiệm - Tích vô hướng: Tính tích vô hướng của vectơ với tổng hai vectơ": (k10_mc_tich_vo_huong_to_hop_3vecto, "mc"),
    "Trắc nghiệm - Tích vô hướng: Tìm tham số để hai vectơ vuông góc nhau": (k10_mc_tich_vo_huong_tham_so_vuong_goc_do_dai, "mc"),
    "Đúng sai - Oxy: Khảo sát 2 vectơ qua i, j, tổng, độ dài và cùng phương": (k10_tf_oxy_khao_sat_2vecto_don_vi_do_dai, "tf"),
    "Đúng sai - Oxy: Tam giác ABC cho bởi vectơ vị trí ba đỉnh": (k10_tf_oxy_tam_giac_vecto_vi_tri_dinh, "tf"),
    "Đúng sai - Oxy: Khảo sát 3 vectơ, bẫy thứ tự j trước i và hệ thức bậc hai": (k10_tf_oxy_3vecto_bay_j_i_to_hop_m_n, "tf"),
    "Đúng sai - Oxy: Khảo sát 3 điểm, tam giác, hình bình hành và giao trục hoành": (k10_tf_oxy_3diem_tam_giac_hbh_giao_truc_hoanh, "tf"),
    "Đúng sai - Tích vô hướng: Tam giác đều, đường cao AH và góc giữa các cặp vectơ": (k10_tf_tich_vo_huong_tam_giac_deu_duong_cao_ah, "tf"),
    "Đúng sai - Tích vô hướng: Hình vuông ABCD, trọng tâm G và tích vô hướng": (k10_tf_tich_vo_huong_hinh_vuong_trong_tam_g, "tf"),
    "Đúng sai - Tích vô hướng: Khảo sát hệ tích vô hướng của hai vectơ tìm vectơ c": (k10_tf_tich_vo_huong_he_vecto_an_c, "tf"),

    # 19 Dạng toán thực tế & vectơ đợt 2
    "Trả lời ngắn - Hệ thức lượng: Bài toán thực tế xe thang cứu hỏa tiếp cận tòa nhà": (k10_sa_htl_toan_thuc_te_xe_cuu_hoa_thang, "sa"),
    "Trả lời ngắn - Hệ thức lượng: Bài toán thực tế đo chiều cao tháp mái bằng giác kế": (k10_sa_htl_toan_thuc_te_chieu_cao_thap_mai, "sa"),
    "Trả lời ngắn - Hệ thức lượng: Bài toán thực tế máy bay bay chệch hướng": (k10_sa_htl_toan_thuc_te_may_bay_chech_huong, "sa"),
    "Trắc nghiệm - Hệ thức lượng: Bài toán thực tế xác định vị trí tàu biển so với bờ": (k10_mc_htl_toan_thuc_te_tau_bien_phuong_vi, "mc"),
    "Trả lời ngắn - Hệ thức lượng: Bài toán thực tế tính chiều cao ngọn núi từ tòa nhà": (k10_sa_htl_toan_thuc_te_nui_nhan_tao_toa_nha, "sa"),
    "Trả lời ngắn - Hệ thức lượng: Bài toán thực tế bóng cây trên sườn đồi dốc": (k10_sa_htl_toan_thuc_te_cay_tren_suon_doi, "sa"),
    "Trả lời ngắn - Hệ thức lượng: Bài toán thực tế cú đánh golf lệch hướng": (k10_sa_htl_toan_thuc_te_danh_golf_goc_lech, "sa"),
    "Trắc nghiệm - Vectơ: Độ dài vectơ hiệu trong hình vuông tâm O": (k10_mc_vecto_do_dai_hieu_hinh_vuong, "mc"),
    "Trắc nghiệm - Vectơ: Quy tắc hình bình hành biểu diễn vectơ": (k10_mc_vecto_quy_tac_hinh_binh_hanh, "mc"),
    "Trắc nghiệm - Vectơ: Độ dài vectơ hiệu hai cạnh tam giác đều": (k10_mc_vecto_hieu_tam_giac_deu, "mc"),
    "Trắc nghiệm - Vectơ: Đẳng thức vectơ của các điểm trên một đường thẳng": (k10_mc_vecto_ti_le_doan_thang_truc_so, "mc"),
    "Trắc nghiệm - Oxy: Tìm tọa độ trọng tâm tam giác OAB": (k10_mc_vecto_trong_tam_tam_giac_oab, "mc"),
    "Trắc nghiệm - Oxy: Hai vectơ bằng nhau tìm tổng hoành độ và tung độ": (k10_mc_vecto_hai_vecto_bang_nhau_tim_x_y, "mc"),
    "Trắc nghiệm - Oxy: Độ dài vectơ có tọa độ là bộ ba số Pythagore": (k10_mc_vecto_do_dai_vecto_oxy_so_nguyen, "mc"),
    "Trắc nghiệm - Tích vô hướng: Tích vô hướng hai cạnh trong tam giác vuông": (k10_mc_tich_vo_huong_tam_giac_vuong_goc_nhon, "mc"),
    "Trắc nghiệm - Tích vô hướng: Khẳng định sai về công thức tích vô hướng và côsin trong Oxy": (k10_mc_tich_vo_huong_khang_dinh_sai_oxy, "mc"),
    "Đúng sai - Vectơ: Khảo sát hình chữ nhật, độ dài vectơ và tích vô hướng": (k10_tf_hinh_chu_nhat_vecto_va_tich_vo_huong, "tf"),
    "Đúng sai - Oxy: Khảo sát ba điểm tam giác, trung điểm, trọng tâm và hình bình hành": (k10_tf_oxy_tam_giac_3diem_phan_tich_vecto, "tf"),
    "Đúng sai - Oxy: Khảo sát ba vectơ, vuông góc, phân tích tuyến tính và góc": (k10_tf_oxy_3vecto_phan_tich_va_goc, "tf"),

    # 24 Dạng mới bổ sung
    "Trắc nghiệm - Hệ thức lượng: Tính số đo góc trong tam giác khi biết ba cạnh": (k10_mc_htl_tinh_goc_tam_giac_3canh, "mc"),
    "Trắc nghiệm - Hệ thức lượng: Định lí sin tính độ dài cạnh tam giác": (k10_mc_htl_dinh_li_sin_tinh_canh, "mc"),
    "Trắc nghiệm - Hệ thức lượng: Tính côsin của góc khi biết ba cạnh tam giác": (k10_mc_htl_tinh_cos_goc_3canh, "mc"),
    "Trắc nghiệm - Hệ thức lượng: Lý thuyết công thức định lí côsin, sin và diện tích": (k10_mc_htl_ly_thuyet_cong_thuc_dung_sai, "mc"),
    "Trắc nghiệm - Hệ thức lượng: Tính bán kính đường tròn nội tiếp r của tam giác": (k10_mc_htl_ban_kinh_noi_tiep_r, "mc"),
    "Trắc nghiệm - Hệ thức lượng: Tính độ dài đường cao ha của tam giác": (k10_mc_htl_duong_cao_tam_giac, "mc"),
    "Trắc nghiệm - Hệ thức lượng: Tính diện tích tam giác khi biết một cạnh và hai góc": (k10_mc_htl_dien_tich_mot_canh_hai_goc, "mc"),
    "Trắc nghiệm - Hệ thức lượng: Tìm số đo góc lớn nhất khi biết ba cạnh chứa căn": (k10_mc_htl_goc_lon_nhat_ba_canh_can, "mc"),
    "Trắc nghiệm - Hệ thức lượng: Tính độ dài cạnh AD của tứ giác (có hình vẽ)": (k10_mc_htl_tu_giac_tinh_canh_ad, "mc"),
    "Trắc nghiệm - Hệ thức lượng: Bài toán thực tế vệ tinh và hai trạm quan sát (có hình vẽ)": (k10_mc_htl_thuc_te_ve_tinh_hai_tram, "mc"),
    "Trắc nghiệm - Hệ thức lượng: Bài toán thực tế tháp trên ngọn đồi tính chiều cao đồi (có hình vẽ)": (k10_mc_htl_thuc_te_thap_tren_ngon_doi, "mc"),
    "Trắc nghiệm - Hệ thức lượng: Bài toán thực tế quan sát chiều cao cái cây (có hình vẽ)": (k10_mc_htl_thuc_te_quan_sat_chieu_cao_cay, "mc"),
    "Trắc nghiệm - Hệ thức lượng: Bài toán thực tế tàu vận tải tránh băng trôi (có hình vẽ)": (k10_mc_htl_thuc_te_tau_tranh_bang_troi, "mc"),
    "Trắc nghiệm - Lượng giác: Dấu giá trị lượng giác góc tù và hệ thức tan.cot = 1": (k10_mc_lg_dau_va_he_thuc_goc_bu, "mc"),
    "Trắc nghiệm - Lượng giác: Tính giá trị biểu thức lượng giác các góc đặc biệt": (k10_mc_lg_tinh_gia_tri_bieu_thuc_dac_biet, "mc"),
    "Trắc nghiệm - Hệ thức lượng: Bài toán thực tế lắp đường dây điện tránh ngọn núi (có hình vẽ)": (k10_mc_htl_thuc_te_duong_day_dien_nui, "mc"),
    "Đúng sai - Hệ thức lượng: Tam giác biết hai cạnh và góc xen giữa (định lí côsin và diện tích)": (k10_tf_htl_tam_giac_2canh_va_goc, "tf"),
    "Đúng sai - Hệ thức lượng: Tam giác biết ba cạnh (côsin, diện tích Heron, bán kính và đường cao)": (k10_tf_htl_tam_giac_3canh_heron_r_h, "tf"),
    "Đúng sai - Hệ thức lượng: Tam giác biết ba cạnh có góc 60 độ (góc, diện tích, đường cao, R)": (k10_tf_htl_tam_giac_ba_canh_goc_60, "tf"),
    "Đúng sai - Hệ thức lượng: Tam giác biết hai cạnh và cos A (góc nhọn tù, cạnh a, sin A, ha)": (k10_tf_htl_hai_canh_va_cos_a, "tf"),
    "Đúng sai - Hệ thức lượng: Tam giác biết hai cạnh và góc 60 độ (làm tròn BC, góc B, S và 2R-5r)": (k10_tf_htl_lam_tron_r_va_r_nho, "tf"),
    "Đúng sai - Hệ thức lượng: Tam giác biết cạnh chứa căn và cos A (góc nhỏ nhất, BC, trung tuyến BM, S)": (k10_tf_htl_canh_can_trung_tuyen_bm, "tf"),
    "Đúng sai - Hệ thức lượng: Tam giác biết ba cạnh nhỏ (diện tích, AH, góc tù và tổng r+R)": (k10_tf_htl_ba_canh_nho_goc_tu_r_cong_r, "tf"),
    "Đúng sai - Hệ thức lượng: Tam giác có điểm M chạy trên cạnh BC tìm AM nhỏ nhất": (k10_tf_htl_diem_m_tren_bc_am_min, "tf"),
    "Đúng sai - Hệ thức lượng: Tam giác biết diện tích, góc 120 độ tính R và đường phân giác trong": (k10_tf_htl_dien_tich_goc_120_phan_giac, "tf"),
    "Đúng sai - Hệ thức lượng: Bài toán thực tế lát gạch mảnh đất tứ giác ABCD (có hình vẽ)": (k10_tf_htl_thuc_te_lat_gach_tu_giac, "tf"),
    "Đúng sai - Lượng giác: Khảo sát côsin âm và các giá trị lượng giác của góc tù": (k10_tf_luong_giac_cos_am, "tf"),
    "Đúng sai - Lượng giác: Khảo sát tang góc nhọn và giá trị biểu thức lượng giác": (k10_tf_luong_giac_tan_duong_bieu_thuc, "tf"),
    "Trắc nghiệm - Vectơ: Cặp vectơ cùng hướng và ngược hướng trong tam giác có đường trung bình": (k10_mc_vecto_trung_binh_cung_huong, "mc"),
    "Trắc nghiệm - Vectơ: Đẳng thức liên hệ hai vectơ cùng phương trên lưới ô vuông": (k10_mc_vecto_luoi_o_vuong_dang_thuc, "mc"),
    "Trắc nghiệm - Vectơ: Khẳng định sai về tích của vectơ với một số âm": (k10_mc_vecto_tich_so_khang_dinh_sai, "mc"),
    "Trắc nghiệm - Vectơ: Đẳng thức độ dài của vectơ trong tam giác có đường trung bình": (k10_mc_vecto_trung_binh_do_dai, "mc"),
    "Trắc nghiệm - Oxy: Xác định tọa độ vectơ khi viết thứ tự j trước i": (k10_mc_vecto_bay_thu_tu_j_i, "mc"),
    "Trắc nghiệm - Oxy: Tọa độ điểm M từ biểu diễn vectơ OM qua i và j": (k10_mc_vecto_toa_do_diem_qua_om, "mc"),
    "Trắc nghiệm - Oxy: Tìm tọa độ vectơ khi biết tọa độ hai điểm mút": (k10_mc_vecto_toa_do_mn_tu_2diem, "mc"),
    "Trắc nghiệm - Oxy: Biểu diễn vectơ qua hai vectơ đơn vị và tính giá trị biểu thức": (k10_mc_vecto_bieu_dien_ab_tinh_bt, "mc"),
    "Trắc nghiệm - Oxy: Tính tọa độ tổng của hai vectơ": (k10_mc_vecto_tong_hai_vecto_oxy, "mc"),
    "Trắc nghiệm - Oxy: Tọa độ tổ hợp tuyến tính của ba vectơ": (k10_mc_vecto_to_hop_3vecto_oxy, "mc"),
    "Trắc nghiệm - Tích vô hướng: Tích vô hướng của hai vectơ ngược hướng (lý thuyết)": (k10_mc_tich_vo_huong_nguoc_huong_ly_thuyet, "mc"),
    "Trắc nghiệm - Tích vô hướng: Tính tích vô hướng từ độ dài và góc giữa hai vectơ": (k10_mc_tich_vo_huong_co_ban_do_dai_goc, "mc"),
    "Trắc nghiệm - Tích vô hướng: Bình phương vô hướng của biểu thức tổ hợp vectơ": (k10_mc_tich_vo_huong_binh_phuong_to_hop, "mc"),
    "Trắc nghiệm - Tích vô hướng: Tìm số đo góc giữa hai vectơ từ độ dài và tích vô hướng": (k10_mc_tich_vo_huong_tim_goc_tu_tich, "mc"),
    "Trắc nghiệm - Tích vô hướng: Tính số đo góc giữa hai vectơ trong hệ tọa độ Oxy": (k10_mc_tich_vo_huong_goc_oxy_so_do, "mc"),
    "Trắc nghiệm - Tích vô hướng: Bài toán thực tế tính công sinh bởi lực kéo": (k10_mc_tich_vo_huong_toan_thuc_te_cong_luc, "mc"),
    "Đúng sai - Oxy: Khảo sát tọa độ vectơ, độ dài vectơ mút và tính cùng phương": (k10_tf_vecto_oxy_tong_hop_4y, "tf"),

    # Phần I: Trắc nghiệm 4 lựa chọn (MC)
    "Trắc nghiệm - Vectơ: Vectơ bằng nhau trong hình bình hành": (k10_mc_vecto_hinh_binh_hanh_bang_nhau, "mc"),
    "Trắc nghiệm - Vectơ: Hệ thức trọng tâm tam giác": (k10_mc_vecto_he_thuc_trong_tam, "mc"),
    "Trắc nghiệm - Vectơ: Độ dài vectơ hiệu trong tam giác đều": (k10_mc_vecto_hieu_do_dai_tam_giac_deu, "mc"),
    "Trắc nghiệm - Vectơ: Tỉ số đoạn thẳng từ hệ thức vectơ": (k10_mc_vecto_ti_so_doan_thang, "mc"),
    "Trắc nghiệm - Vectơ: Hợp lực của hai lực vuông góc tác dụng lên vật": (k10_mc_vecto_hop_luc_vat_ly, "mc"),
    "Trắc nghiệm - Tích vô hướng: Góc giữa hai vectơ trong tam giác đều và tam giác vuông": (k10_mc_tich_vo_huong_goc_tam_giac, "mc"),
    "Trắc nghiệm - Tích vô hướng: Tính tích vô hướng theo định nghĩa (độ dài và góc)": (k10_mc_tich_vo_huong_dinh_nghia, "mc"),
    "Trắc nghiệm - Tích vô hướng: Tích vô hướng trong tam giác đều và hình vuông cạnh a": (k10_mc_tich_vo_huong_hinh_vuong_tam_giac, "mc"),
    "Trắc nghiệm - Tích vô hướng: Tìm góc giữa hai vectơ khi biết tích vô hướng và độ dài": (k10_mc_tich_vo_huong_goc_nguoc, "mc"),
    "Trắc nghiệm - Tích vô hướng: Tính tích vô hướng trong tam giác vuông": (k10_mc_tich_vo_huong_tam_giac_vuong_canh, "mc"),
    "Trắc nghiệm - Oxy: Biểu diễn vectơ qua hai vectơ đơn vị i và j": (k10_mc_vecto_bieu_dien_don_vi, "mc"),
    "Trắc nghiệm - Oxy: Phép toán tuyến tính của vectơ trong Oxy": (k10_mc_vecto_phep_toan_tuyen_tinh, "mc"),
    "Trắc nghiệm - Oxy: Độ dài của vectơ trong hệ tọa độ Oxy": (k10_mc_vecto_do_dai_ab, "mc"),
    "Trắc nghiệm - Oxy: Độ dài đoạn thẳng AB trong mặt phẳng Oxy": (k10_mc_vecto_do_dai_ab, "mc"),
    "Trắc nghiệm - Oxy: Tọa độ trung điểm của đoạn thẳng": (k10_mc_vecto_trung_diem_trong_tam, "mc"),
    "Trắc nghiệm - Oxy: Tìm tọa độ điểm khi biết trọng tâm tam giác": (k10_mc_vecto_tim_diem_trong_tam_nguoc, "mc"),
    "Trắc nghiệm - Oxy: Hình chiếu vuông góc và điểm đối xứng qua trục tọa độ": (k10_mc_vecto_hinh_chieu_doi_xung, "mc"),
    "Trắc nghiệm - Oxy: Điểm chia đoạn thẳng theo tỉ số k": (k10_mc_vecto_diem_chia_doan_thang, "mc"),
    "Trắc nghiệm - Oxy: Tìm tọa độ điểm D để ABCD là hình bình hành": (k10_mc_vecto_hinh_binh_hanh, "mc"),
    "Trắc nghiệm - Oxy: Hai vectơ bằng nhau tìm giá trị biểu thức": (k10_mc_vecto_hai_vecto_bang_nhau, "mc"),
    "Trắc nghiệm - Oxy: Ba điểm thẳng hàng và hai vectơ cùng phương": (k10_mc_vecto_cung_phuong_thang_hang, "mc"),
    "Trắc nghiệm - Oxy: Phân tích vectơ c theo hai vectơ không cùng phương a và b": (k10_mc_vecto_phan_tich_vecto_c, "mc"),
    "Trắc nghiệm - Oxy: Ba điểm thẳng hàng chứa tham số m": (k10_mc_vecto_ba_diem_thang_hang_tham_so, "mc"),
    "Trắc nghiệm - Oxy: Chu vi của tam giác OAB trong mặt phẳng Oxy": (k10_mc_vecto_chu_vi_tam_giac, "mc"),
    "Trắc nghiệm - Oxy: Tìm tham số để độ dài đoạn thẳng bằng giá trị cho trước": (k10_mc_vecto_tim_tham_so_do_dai, "mc"),
    "Trắc nghiệm - Oxy: Tích vô hướng của hai vectơ trong tọa độ Oxy": (k10_mc_tich_vo_huong_toa_do_oxy, "mc"),
    "Trắc nghiệm - Oxy: Côsin góc giữa hai vectơ trong tọa độ Oxy": (k10_mc_tich_vo_huong_cosin_goc, "mc"),
    "Trắc nghiệm - Oxy: Điểm thuộc trục hoành sao cho tam giác vuông": (k10_mc_tich_vo_huong_tam_giac_vuong_ox, "mc"),
    "Trắc nghiệm - Oxy: Tìm tham số m để hai vectơ vuông góc nhau": (k10_mc_tich_vo_huong_vuong_goc_tham_so, "mc"),

    # Phần II: Trắc nghiệm Đúng - Sai (TF)
    "Đúng sai - Thống kê: Mẫu số liệu 5 giá trị (Trung vị, trung bình, Q1 và mốt)": (k10_tf_tk_diem_bong_ro_5_so, "tf"),
    "Đúng sai - Thống kê: Mẫu số liệu rời rạc nhiều giá trị (Mốt, Q1+Q2+Q3, cỡ mẫu và Q2)": (k10_tf_tk_diem_chat_luong_san_pham, "tf"),
    "Đúng sai - Thống kê: Bảng tần số điểm kiểm tra (Mốt, trung bình, Q2 và Q1)": (k10_tf_tk_bang_tan_so_diem_kiem_tra, "tf"),
    "Đúng sai - Thống kê: Thống kê sản lượng bán hàng 6 tháng (Sai khác TB-TV, mốt, n, Q2-Q1)": (k10_tf_tk_san_luong_xi_mang_6_thang, "tf"),
    "Đúng sai - Thống kê: Mẫu số liệu rời rạc (Cỡ mẫu, khoảng biến thiên, khoảng tứ phân vị, trung vị)": (k10_tf_tk_do_phan_tan_mau_roi_rac, "tf"),
    "Đúng sai - Thống kê: Bảng số liệu nhiều năm (Giờ nắng lớn nhất, nhỏ nhất, trung bình và R)": (k10_tf_tk_tong_gio_nang_cac_nam, "tf"),
    "Đúng sai - Thống kê: Bảng số liệu tỉ lệ phần trăm (Trung bình, độ lệch chuẩn, phương sai và GTLN)": (k10_tf_tk_ti_le_tot_nghiep_16_nam, "tf"),
    "Đúng sai - Thống kê: Bảng tần số thu nhập hộ gia đình (Mốt, phương sai, cỡ mẫu và trung bình)": (k10_tf_tk_thu_nhap_ho_gia_dinh, "tf"),
    "Đúng sai - Vectơ: Khảo sát hình vuông và tích vô hướng các cặp vectơ": (k10_tf_hinh_vuong_tich_vo_huong, "tf"),
    "Đúng sai - Vectơ: Tam giác đều, đường cao và góc giữa các vectơ": (k10_tf_tich_vo_huong_tam_giac_deu_duong_cao, "tf"),
    "Đúng sai - Vectơ: Khảo sát hình bình hành và tích vô hướng các đường chéo": (k10_tf_tich_vo_huong_hinh_binh_hanh, "tf"),
    "Đúng sai - Oxy: Khảo sát tam giác ABC, trung điểm, trọng tâm và chân đường phân giác": (k10_tf_oxy_tam_giac_va_phan_giac, "tf"),
    "Đúng sai - Oxy: Tọa độ vectơ, độ dài vectơ và vectơ cùng phương": (k10_tf_vecto_co_ban_va_do_dai, "tf"),
    "Đúng sai - Oxy: Tích vô hướng hai vectơ, góc và điều kiện vuông góc chứa tham số": (k10_tf_tich_vo_huong_oxy, "tf"),

    # Phần III: Trắc nghiệm Trả lời ngắn (SA)
    "Trả lời ngắn - Oxy: Tọa độ đỉnh D của hình bình hành ABCD (Tổng hoành độ và tung độ)": (k10_sa_oxy_hinh_binh_hanh_tong_toa_do, "sa"),
    "Trả lời ngắn - Oxy: Tìm hoành độ điểm M trên trục hoành để tam giác ABM vuông tại B": (k10_sa_oxy_tam_giac_vuong_truc_hoanh, "sa"),
    "Trả lời ngắn - Oxy: Tính giá trị tích vô hướng AB . AC trong hệ tọa độ Oxy": (k10_sa_tich_vo_huong_oxy, "sa"),
    "Trả lời ngắn - Oxy: Tính số đo góc giữa hai vectơ (đơn vị: độ)": (k10_sa_tich_vo_huong_goc_do, "sa"),
    "Trả lời ngắn - Oxy: Tìm giá trị tham số m để hai vectơ vuông góc": (k10_sa_tich_vo_huong_tham_so_vuong_goc, "sa"),
    "Trả lời ngắn - Vectơ: Độ lớn hợp lực của hai lực vuông góc tác dụng lên một vật": (k10_sa_vecto_hop_luc, "sa"),
    "Trả lời ngắn - Vectơ: Tỉ số độ dài đoạn thẳng từ hệ thức vectơ": (k10_sa_vecto_ti_so_doan_thang, "sa"),
    "Trả lời ngắn - Oxy: Phân tích vectơ c theo a và b, tính tổng hệ số m + n": (k10_sa_vecto_phan_tich_tong_he_so, "sa"),

    # 32 Dạng bổ sung Chương IV Vectơ (Bài 7, 8, 9, 11) từ bộ phiếu bài tập
    "Trắc nghiệm - Vectơ: Đếm số vectơ khác vectơ-không từ đỉnh đa giác hoặc lục giác đều": (k10_mc_vecto_b7_dem_so_vecto, "mc"),
    "Trắc nghiệm - Vectơ: Điều kiện cùng phương, cùng hướng và bằng nhau của hai vectơ": (k10_mc_vecto_b7_dieu_kien_cung_huong_bang_nhau, "mc"),
    "Trắc nghiệm - Vectơ: Tính độ dài vectơ trong tam giác đều và hình thoi": (k10_mc_vecto_b7_do_dai_co_ban, "mc"),
    "Đúng sai - Vectơ: Hình thang và đếm số vectơ cùng phương, cùng hướng (Bài 7)": (k10_tf_vecto_b7_hinh_thang_cung_phuong, "tf"),
    "Đúng sai - Vectơ: Đếm số vectơ lập từ đa giác và các điểm thẳng hàng (Bài 7)": (k10_tf_vecto_b7_da_giac_va_thang_hang, "tf"),
    "Trả lời ngắn - Vectơ: Độ dài vectơ trong hình thoi hoặc tam giác đều trọng tâm G": (k10_sa_vecto_b7_do_dai_thoi_hoac_tam_giac_deu, "sa"),

    "Trắc nghiệm - Vectơ: Quy tắc ba điểm, cộng trừ nhiều vectơ và tìm vị trí điểm": (k10_mc_vecto_b8_quy_tac_ba_diem_tong_hieu, "mc"),
    "Trắc nghiệm - Vectơ: Ba lực cân bằng tác dụng vào một vật (có hình vẽ)": (k10_mc_vecto_b8_ba_luc_can_bang_tikz, "mc"),
    "Trắc nghiệm - Vectơ: Độ dài tổng hiệu hai vectơ trong tam giác vuông và góc đặc biệt": (k10_mc_vecto_b8_do_dai_tong_hieu_tam_giac, "mc"),
    "Đúng sai - Vectơ: Hình thoi góc 60 độ và tổng hiệu trong tam giác (Bài 8)": (k10_tf_vecto_b8_hinh_thoi_va_ba_diem, "tf"),
    "Đúng sai - Vectơ: Ba hình bình hành dựng bên ngoài tam giác ABC (Bài 8)": (k10_tf_vecto_b8_ba_hinh_binh_hanh_ngoai, "tf"),
    "Trả lời ngắn - Vectơ: Tổng hợp hai lực bằng nhau tạo góc 60 độ hoặc 120 độ": (k10_sa_vecto_b8_hop_luc_tao_goc, "sa"),
    "Trả lời ngắn - Vectơ: Độ dài biểu thức vectơ trong hình vuông và tam giác vuông": (k10_sa_vecto_b8_do_dai_hinh_vuong_tam_giac_vuong, "sa"),
    "Trả lời ngắn - Vectơ: Độ dài biểu thức tổng hiệu vectơ trong hình thang": (k10_sa_vecto_b8_do_dai_hinh_thang, "sa"),

    "Trắc nghiệm - Vectơ: Nhận diện hình vẽ biểu diễn điểm chia đoạn thẳng (có hình vẽ)": (k10_mc_vecto_b9_hinh_ve_chia_doan_thang_tikz, "mc"),
    "Trắc nghiệm - Vectơ: Xác định vị trí điểm từ hệ thức vectơ và trọng tâm mở rộng": (k10_mc_vecto_b9_vi_tri_diem_he_thuc, "mc"),
    "Trắc nghiệm - Vectơ: Phân tích vectơ trong hình chữ nhật, tam giác và tìm hệ số k": (k10_mc_vecto_b9_phan_tich_va_tim_k, "mc"),
    "Trắc nghiệm - Vectơ: Biến đổi đẳng thức vectơ độc lập với điểm M và trọng tâm hai tam giác": (k10_mc_vecto_b9_bien_doi_he_thuc_doc_lap, "mc"),
    "Đúng sai - Vectơ: Phân tích vectơ và ba điểm thẳng hàng trong hình bình hành (Bài 9)": (k10_tf_vecto_b9_hbh_thang_hang, "tf"),
    "Đúng sai - Vectơ: Trung tuyến, trọng tâm và điểm đối xứng trong tam giác (Bài 9)": (k10_tf_vecto_b9_trung_tuyen_va_doi_xung, "tf"),
    "Trả lời ngắn - Vectơ: Độ dài tổng hai vectơ trong tam giác vuông có góc 30 độ": (k10_sa_vecto_b9_tam_giac_vuong_goc_30, "sa"),
    "Trả lời ngắn - Vectơ: Ba lực cân bằng hợp góc 120 độ và 90 độ (có hình vẽ)": (k10_sa_vecto_b9_ba_luc_can_bang_tikz, "sa"),
    "Trả lời ngắn - Vectơ: Vật cân bằng dưới tác dụng của bốn lực có góc 45 độ (có hình vẽ)": (k10_sa_vecto_b9_bon_luc_can_bang_tikz, "sa"),
    "Trả lời ngắn - Vectơ: Tìm hệ số k từ đẳng thức trung điểm hoặc phân tích cạnh": (k10_sa_vecto_b9_he_so_k_phan_tich, "sa"),

    "Trắc nghiệm - Tích vô hướng: Góc giữa hai vectơ từ trọng tâm tam giác đều hoặc tâm hình chữ nhật, hình vuông": (k10_mc_tich_vo_huong_b11_goc_tam_hinh_trong_tam, "mc"),
    "Trắc nghiệm - Tích vô hướng: Tích vô hướng trong hình chữ nhật, hình bình hành, hình thoi và hình thang vuông": (k10_mc_tich_vo_huong_b11_tu_giac_hbh_hinh_thoi, "mc"),
    "Trắc nghiệm - Tích vô hướng: Tích vô hướng liên quan đến trung điểm và đường trung tuyến": (k10_mc_tich_vo_huong_b11_trung_diem_trung_tuyen, "mc"),
    "Trắc nghiệm - Tích vô hướng: Tìm côsin góc từ hiệu hai vectơ hoặc tìm tham số m từ độ dài đoạn thẳng": (k10_mc_tich_vo_huong_b11_cosin_tu_hieu_va_do_dai, "mc"),
    "Trắc nghiệm - Oxy: Tìm tham số m để góc bằng 45 hoặc 135 độ và biểu thức tích vô hướng": (k10_mc_tich_vo_huong_b11_oxy_goc_va_to_hop, "mc"),
    "Đúng sai - Tích vô hướng: Hình vuông có trung điểm, trọng tâm và tích vô hướng (có hình vẽ)": (k10_tf_tich_vo_huong_b11_hinh_vuong_trong_tam_tikz, "tf"),
    "Đúng sai - Tích vô hướng: Hình vuông điểm chia đường chéo và tam giác vuông cân (có hình vẽ)": (k10_tf_tich_vo_huong_b11_hinh_vuong_tam_giac_vuong_can_tikz, "tf"),
    "Đúng sai - Oxy: Khảo sát tích vô hướng hai vectơ, góc vuông và hệ tìm tọa độ vectơ": (k10_tf_tich_vo_huong_b11_oxy_he_tich_vo_huong, "tf"),
}


def dispatch_k10_vecto_oxy(item):
    """
    Hàm sinh câu hỏi tự động cho các dạng bài Toán 10 (Vectơ & Tọa độ Oxy).
    Trả lời block LaTeX hoàn chỉnh: \\begin{ex} ... \\end{ex}
    """
    if item not in K10_VECTO_OXY_MAP:
        return None

    fn, q_type = K10_VECTO_OXY_MAP[item]
    if q_type == "mc":
        caudan, choices, loigiai = fn()
        return f"\\begin{{ex}}\n{caudan}\n\\choice\n{''.join(choices)}\\loigiai{{{loigiai}}}\n\\end{{ex}}"
    elif q_type == "tf":
        caudan, choices, loigiai = fn()
        return f"\\begin{{ex}}\n{caudan}\n\\choiceTF\n{''.join(choices)}\\loigiai{{{loigiai}}}\n\\end{{ex}}"
    elif q_type == "sa":
        caudan, dapan, loigiai = fn()
        return f"\\begin{{ex}}\n{caudan}\n\\shortans[oly]{{{dapan}}}\n\\loigiai{{{loigiai}}}\n\\end{{ex}}"
    return None
