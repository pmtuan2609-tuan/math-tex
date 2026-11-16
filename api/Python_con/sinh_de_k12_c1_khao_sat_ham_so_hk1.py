# -*- coding: utf-8 -*-
"""
Module: sinh_de_k12_c1_khao_sat_ham_so_hk1
Sinh đề trắc nghiệm Toán 12 - Chương I: Khảo sát hàm số (GDPT 2018)
Bao gồm:
- 6 Dạng Trắc nghiệm 4 phương án (MC)
- 4 Dạng Đúng / Sai (TF)
- 3 Dạng Trả lời ngắn (SA)
"""
import random
import math
from fractions import Fraction

def _fmt_frac(n, d):
    if d == 1:
        return str(n)
    if d < 0:
        n, d = -n, -d
    g = math.gcd(abs(n), abs(d))
    n //= g
    d //= g
    if d == 1:
        return str(n)
    return f"\\frac{{{n}}}{{{d}}}"

def _make_mc_choices(correct, wrongs):
    wrongs_clean = [w for w in wrongs if w != correct]
    random.shuffle(wrongs_clean)
    wrongs_clean = wrongs_clean[:3]
    while len(wrongs_clean) < 3:
        wrongs_clean.append(f"${random.randint(10, 99)}$")
    options = [correct] + wrongs_clean
    random.shuffle(options)
    formatted = []
    for opt in options:
        formatted.append(f" {opt}\n")
    return formatted

def _make_tf_choices(items):
    choices = []
    for val, text in items:
        prefix = "\\True " if val else ""
        choices.append(f"{prefix}{text}\n")
    return choices

# ==============================================================================
# PHẦN 1: TRẮC NGHIỆM NHIỀU LỰA CHỌN (MC)
# ==============================================================================

def k12_mc_c1_khoang_nghich_bien_bac_nhat():
    """MC: Cho f'(x) = ax + b, tìm khoảng nghịch biến."""
    a_val = random.choice([2, 3, 4, 5])
    x0 = random.choice([-4, -3, -2, -1, 1, 2, 3, 4])
    b_val = - a_val * x0
    sign_b = f"+ {b_val}" if b_val > 0 else f"- {abs(b_val)}"
    caudan = f"Cho hàm số $y = f(x)$ có đạo hàm $f'(x) = {a_val}x {sign_b}, \\forall x \\in \\mathbb{{R}}$. Hàm số đã cho nghịch biến trên khoảng nào dưới đây?"
    
    correct = f"$(-\\infty; {x0})$"
    wrongs = [
        f"$({x0}; +\\infty)$",
        f"$(-\\infty; {-x0})$",
        f"$({-x0}; +\\infty)$"
    ]
    choices = _make_mc_choices(correct, wrongs)
    loigiai = (
        f"Hàm số nghịch biến khi và chỉ khi $f'(x) < 0$.\n"
        f"Ta có: ${a_val}x {sign_b} < 0 \\Leftrightarrow {a_val}x < {-b_val} \\Leftrightarrow x < {x0}$.\n"
        f"Vậy hàm số nghịch biến trên khoảng $(-\\infty; {x0})$."
    )
    return caudan, choices, loigiai

def k12_mc_c1_so_cuc_tri_nghiem_boi():
    """MC: Cho f'(x) = (x - x1)^k1 * (x - x2)^k2 ..., tìm số điểm cực trị."""
    x1, x2, x3 = random.sample([-3, -2, -1, 1, 2, 3], 3)
    k_even = random.choice([2, 4])
    s1 = f"(x - {x1})" if x1 > 0 else f"(x + {abs(x1)})"
    s2 = f"(x - {x2})^{{{k_even}}}" if x2 > 0 else f"(x + {abs(x2)})^{{{k_even}}}"
    s3 = f"(x - {x3})" if x3 > 0 else f"(x + {abs(x3)})"
    
    caudan = f"Cho hàm số $y = f(x)$ có đạo hàm $f'(x) = {s1}{s2}{s3}$ với mọi $x \\in \\mathbb{{R}}$. Hàm số đã cho có bao nhiêu điểm cực trị?"
    correct = "$2$"
    wrongs = ["$1$", "$3$", "$0$"]
    choices = _make_mc_choices(correct, wrongs)
    loigiai = (
        f"Ta có $f'(x) = 0 \\Leftrightarrow \\left[\\begin{{array}}{{l}} x = {x1} \\\\ x = {x2} \\\\ x = {x3} \\end{{array}}\\right..\n\n"
        f"Trong đó $x = {x2}$ là nghiệm bội chẵn (bậc {k_even}) nên $f'(x)$ không đổi dấu khi đi qua $x = {x2}$.\n"
        f"Các nghiệm $x = {x1}$ và $x = {x3}$ là nghiệm bội lẻ (bậc 1) nên $f'(x)$ đổi dấu khi đi qua hai điểm này.\n"
        f"Vậy hàm số có đúng $2$ điểm cực trị."
    )
    return caudan, choices, loigiai

def k12_mc_c1_gtln_gtnn_trung_phuong_doan():
    """MC: Giá trị nhỏ nhất của hàm trùng phương trên đoạn chứa điểm cực trị."""
    c_val = random.choice([3, 4, 5, 6])
    min_val = c_val - 1
    caudan = f"Giá trị nhỏ nhất $m$ của hàm số $y = x^4 - 2x^2 + {c_val}$ trên đoạn $[0; \\sqrt{{3}}]$ là:"
    correct = f"${min_val}$"
    wrongs = [f"${c_val}$", f"${c_val + 3}$", f"${min_val - 1}$"]
    choices = _make_mc_choices(correct, wrongs)
    loigiai = (
        f"Hàm số liên tục trên $[0; \\sqrt{{3}}]$.\n"
        f"Ta có $y' = 4x^3 - 4x = 4x(x^2 - 1) = 0 \\Leftrightarrow \\left[\\begin{{array}}{{l}} x = 0 \\in [0; \\sqrt{{3}}] \\\\ x = 1 \\in [0; \\sqrt{{3}}] \\\\ x = -1 \\notin [0; \\sqrt{{3}}] \\end{{array}}\\right..\n\n"
        f"Tính các giá trị:\n"
        f"- $y(0) = {c_val}$.\n"
        f"- $y(1) = 1 - 2 + {c_val} = {min_val}$.\n"
        f"- $y(\\sqrt{{3}}) = (\\sqrt{{3}})^4 - 2(\\sqrt{{3}})^2 + {c_val} = 9 - 6 + {c_val} = {c_val + 3}$.\n\n"
        f"Vậy giá trị nhỏ nhất của hàm số trên đoạn $[0; \\sqrt{{3}}]$ là $m = {min_val}$."
    )
    return caudan, choices, loigiai

def k12_mc_c1_tiem_can_xien_tach_phan_nguyen():
    """MC: Tiệm cận xiên của y = ax + b + c/(dx + e)."""
    a_val = random.choice([-3, -2, 2, 3])
    b_val = random.choice([-8, -5, -4, 4, 5, 7])
    d_val = random.choice([2, 4])
    e_val = random.choice([-9, -7, 3, 5])
    c_val = random.choice([1, 3, 5])
    
    line_str = f"{a_val}x {'+' if b_val > 0 else '-'} {abs(b_val)}"
    denom_str = f"{d_val}x {'+' if e_val > 0 else '-'} {abs(e_val)}"
    caudan = f"Tiệm cận xiên của đồ thị hàm số $y = {line_str} + \\frac{{{c_val}}}{{{denom_str}}}$ là đường thẳng:"
    correct = f"$y = {line_str}$"
    wrongs = [
        f"$y = {a_val}x {'-' if b_val > 0 else '+'} {abs(b_val)}$",
        f"$y = {-a_val}x {'+' if b_val > 0 else '-'} {abs(b_val)}$",
        f"$x = {_fmt_frac(-e_val, d_val)}$"
    ]
    choices = _make_mc_choices(correct, wrongs)
    loigiai = (
        f"Ta có $\\lim_{{x \\to \\pm\\infty}} [y - ({line_str})] = \\lim_{{x \\to \\pm\\infty}} \\frac{{{c_val}}}{{{denom_str}}} = 0$.\n"
        f"Do đó, đường thẳng $y = {line_str}$ là tiệm cận xiên của đồ thị hàm số."
    )
    return caudan, choices, loigiai

def k12_mc_c1_tiem_can_ngang_hai_phía():
    """MC: Cho lim x->+inf f(x) = y1 và lim x->-inf f(x) = y2. Khẳng định tiệm cận ngang."""
    y1 = random.choice([1, 2, 3])
    y2 = -y1
    caudan = f"Cho hàm số $y = f(x)$ xác định trên $\\mathbb{{R}}$ thỏa mãn $\\lim_{{x \\to +\\infty}} f(x) = {y1}$ và $\\lim_{{x \\to -\\infty}} f(x) = {y2}$. Khẳng định nào sau đây là đúng?"
    correct = f"Đồ thị hàm số có hai tiệm cận ngang là các đường thẳng $y = {y1}$ và $y = {y2}$."
    wrongs = [
        f"Đồ thị hàm số có đúng một tiệm cận ngang là $y = {y1}$.",
        "Đồ thị hàm số không có tiệm cận ngang.",
        f"Đồ thị hàm số có hai tiệm cận đứng là $x = {y1}$ và $x = {y2}$."
    ]
    choices = _make_mc_choices(correct, wrongs)
    loigiai = (
        f"Theo định nghĩa đường tiệm cận ngang:\n"
        f"- Vì $\\lim_{{x \\to +\\infty}} f(x) = {y1}$ nên đường thẳng $y = {y1}$ là một tiệm cận ngang (khi $x \\to +\\infty$).\n"
        f"- Vì $\\lim_{{x \\to -\\infty}} f(x) = {y2}$ nên đường thẳng $y = {y2}$ là một tiệm cận ngang (khi $x \\to -\\infty$).\n"
        f"Do đó đồ thị hàm số có đúng 2 tiệm cận ngang là $y = {y1}$ và $y = {y2}$."
    )
    return caudan, choices, loigiai

# Alias không dấu phòng ngừa
k12_mc_c1_tiem_can_ngang_hai_phia = k12_mc_c1_tiem_can_ngang_hai_phía

def k12_mc_c1_giao_diem_truc_tung_phan_thuc():
    """MC: Giao điểm của y = (ax^2 + bx + c)/(dx + e) với trục tung."""
    c_val = random.choice([-6, -4, -3, -2, -1, 1, 2, 3, 4, 6])
    e_val = random.choice([1, 2])
    y0_frac = Fraction(c_val, e_val)
    if y0_frac.denominator == 1:
        y0_str = f"{y0_frac.numerator}"
    else:
        y0_str = f"\\frac{{{y0_frac.numerator}}}{{{y0_frac.denominator}}}"
        
    caudan = f"Đồ thị hàm số $y = \\frac{{x^2 - x {'+' if c_val > 0 else '-'} {abs(c_val)}}}{{{e_val if e_val > 1 else ''}x + {e_val}}}$ cắt trục tung tại điểm có tung độ bằng:"
    correct = f"${y0_str}$"
    wrongs = [
        f"${-y0_frac.numerator if y0_frac.denominator == 1 else _fmt_frac(-y0_frac.numerator, y0_frac.denominator)}$",
        f"${y0_frac.numerator + 1}$",
        "$0$"
    ]
    choices = _make_mc_choices(correct, wrongs)
    loigiai = (
        f"Trục tung có phương trình là $x = 0$.\n"
        f"Thay $x = 0$ vào hàm số ta được: $y = \\frac{{0^2 - 0 {'+' if c_val > 0 else '-'} {abs(c_val)}}}{{0 + {e_val}}} = {y0_str}$.\n"
        f"Vậy đồ thị hàm số cắt trục tung tại điểm $(0; {y0_str})$, có tung độ bằng ${y0_str}$."
    )
    return caudan, choices, loigiai


# ==============================================================================
# PHẦN 2: TRẮC NGHIỆM ĐÚNG SAI (TF)
# ==============================================================================

def k12_tf_c1_khao_sat_bac_ba_doan():
    """TF: Cho hàm số f(x) = x^3 - 3x + d trên đoạn [-2; 2]."""
    d_val = random.choice([80, 85, 91, 95])
    caudan = f"Cho hàm số $f(x) = x^3 - 3x + {d_val}$. Xét tính đúng sai của các khẳng định sau:"
    
    min_val = d_val - 2
    f1_val = d_val - 2
    items = [
        (True, "Đạo hàm của hàm số đã cho là $f'(x) = 3x^2 - 3$."),
        (False, "Phương trình $f'(x) = 0$ có tập nghiệm duy nhất là $S = \\{1\\}$."),
        (True, f"Giá trị cực tiểu của hàm số là $f(1) = {f1_val}$."),
        (True, f"Giá trị nhỏ nhất của hàm số trên đoạn $[-2; 2]$ bằng ${min_val}$.")
    ]
    choices = _make_tf_choices(items)
    loigiai = (
        "\\begin{itemchoice}\n"
        f"\\itemch Đúng. Ta có $f'(x) = (x^3 - 3x + {d_val})' = 3x^2 - 3$.\n"
        "\\itemch Sai. $f'(x) = 0 \\Leftrightarrow 3x^2 - 3 = 0 \\Leftrightarrow x^2 = 1 \\Leftrightarrow x = \\pm 1$. Tập nghiệm $S = \\{-1; 1\\}$.\n"
        f"\\itemch Đúng. $f(1) = 1^3 - 3(1) + {d_val} = {f1_val}$.\n"
        f"\\itemch Đúng. Tính các giá trị: $f(-2) = -8 + 6 + {d_val} = {min_val}; f(-1) = -1 + 3 + {d_val} = {d_val + 2}; f(1) = {f1_val}; f(2) = 8 - 6 + {d_val} = {d_val + 2}$. Do đó $\\min_{{[-2; 2]}} f(x) = {min_val}$.\n"
        "\\end{itemchoice}"
    )
    return caudan, choices, loigiai

def k12_tf_c1_khao_sat_phan_thuc_bac_2_tren_1():
    """TF: Cho y = (x^2 - x + 1)/(-x + 1)."""
    caudan = "Cho hàm số $y = \\frac{x^2 - x + 1}{-x + 1}$. Xét tính đúng sai của các khẳng định sau:"
    items = [
        (True, "Đường thẳng $x = 1$ là đường tiệm cận đứng của đồ thị hàm số."),
        (False, "Hàm số đồng biến trên toàn bộ khoảng $(0; 2)$."),
        (True, "Giá trị lớn nhất của hàm số trên khoảng $(1; +\\infty)$ bằng $-3$."),
        (True, "Đường thẳng $y = -x$ là đường tiệm cận xiên của đồ thị hàm số.")
    ]
    choices = _make_tf_choices(items)
    loigiai = (
        "\\begin{itemchoice}\n"
        "\\itemch Đúng. Vì $\\lim_{x \\to 1^+} y = -\\infty$ và $\\lim_{x \\to 1^-} y = +\\infty$ nên $x = 1$ là tiệm cận đứng.\n"
        "\\itemch Sai. Hàm số không xác định tại $x = 1 \\in (0; 2)$ nên không thể liên tục và đồng biến trên cả khoảng $(0; 2)$.\n"
        "\\itemch Đúng. Ta có $y = -x - \\frac{1}{x - 1} = -(x - 1) - \\frac{1}{x - 1} - 1$. Với $x > 1$, theo BĐT Cauchy: $(x - 1) + \\frac{1}{x - 1} \\ge 2 \\Rightarrow y \\le -2 - 1 = -3$. Dấu bằng xảy ra khi $x = 2$. Vậy $\\max_{(1; +\\infty)} y = -3$.\n"
        "\\itemch Đúng. $\\lim_{x \\to \\pm\\infty} [y - (-x)] = \\lim_{x \\to \\pm\\infty} \\frac{1}{-x + 1} = 0$, nên $y = -x$ là tiệm cận xiên.\n"
        "\\end{itemchoice}"
    )
    return caudan, choices, loigiai

def k12_tf_c1_khao_sat_phan_thuc_tam_thuc_bac_hai():
    """TF: Cho f(x) = (2x - 3)/(x^2 + 4)."""
    caudan = "Cho hàm số $f(x) = \\frac{2x - 3}{x^2 + 4}$. Xét tính đúng sai của các mệnh đề sau:"
    items = [
        (True, "Hàm số đạt cực đại tại điểm $x = 4$."),
        (True, "Đồ thị hàm số có tiệm cận ngang là trục hoành $y = 0$."),
        (True, "Giá trị của hàm số tại $x = 24$ là $f(24) = \\frac{9}{116}$."),
        (False, "Hàm số có đúng một điểm cực trị trên $\\mathbb{R}$.")
    ]
    choices = _make_tf_choices(items)
    loigiai = (
        "\\begin{itemchoice}\n"
        "\\itemch Đúng. Ta có $f'(x) = \\frac{2(x^2 + 4) - 2x(2x - 3)}{(x^2 + 4)^2} = \\frac{-2x^2 + 6x + 8}{(x^2 + 4)^2}$. Phương trình $f'(x) = 0 \\Leftrightarrow -2x^2 + 6x + 8 = 0 \\Leftrightarrow x = -1$ hoặc $x = 4$. Đạo hàm đổi dấu từ dương sang âm qua $x = 4$ nên $x = 4$ là điểm cực đại.\n"
        "\\itemch Đúng. Vì bậc tử ($1$) nhỏ hơn bậc mẫu ($2$) nên $\\lim_{x \\to \\pm\\infty} f(x) = 0$, do đó tiệm cận ngang là trục hoành $y = 0$.\n"
        "\\itemch Đúng. $f(24) = \\frac{2(24) - 3}{24^2 + 4} = \\frac{45}{580} = \\frac{9}{116}$.\n"
        "\\itemch Sai. Hàm số có hai nghiệm phân biệt $x = -1$ và $x = 4$ làm đạo hàm đổi dấu nên có đúng $2$ điểm cực trị.\n"
        "\\end{itemchoice}"
    )
    return caudan, choices, loigiai

def k12_tf_c1_toan_thuc_te_loi_nhuan_doanh_nghiep():
    """TF: Bài toán kinh tế doanh nghiệp: C(x) = 20x + 1200, p(x) = 100 - x."""
    caudan = (
        "Một xưởng sản xuất một loại sản phẩm. Phòng kinh doanh nghiên cứu và đưa ra các hàm số sau:\n"
        "- Chi phí sản xuất $x$ sản phẩm: $C(x) = 20x + 1200$.\n"
        "- Giá bán của mỗi sản phẩm: $p(x) = 100 - x$.\n"
        "(Đơn vị: $x$ là sản phẩm, chi phí và giá bán tính theo nghìn đồng).\n"
        "Xét tính đúng sai của các khẳng định sau:"
    )
    items = [
        (True, "Hàm lợi nhuận thu được khi bán $x$ sản phẩm là $P(x) = -x^2 + 80x - 1200$."),
        (True, "Xưởng sản xuất không bị lỗ khi số lượng sản phẩm bán ra thỏa mãn $20 \\le x \\le 60$."),
        (False, "Hàm doanh thu $R(x)$ đồng biến trên toàn bộ khoảng $(0; 60)$."),
        (False, "Nếu mỗi sản phẩm bị áp thuế $4$ nghìn đồng thì lợi nhuận tối đa giảm $80$ nghìn đồng.")
    ]
    choices = _make_tf_choices(items)
    loigiai = (
        "\\begin{itemchoice}\n"
        "\\itemch Đúng. Doanh thu $R(x) = x \\cdot p(x) = 100x - x^2$. Lợi nhuận $P(x) = R(x) - C(x) = -x^2 + 80x - 1200$.\n"
        "\\itemch Đúng. Xưởng không bị lỗ khi $P(x) \\ge 0 \\Leftrightarrow -x^2 + 80x - 1200 \\ge 0 \\Leftrightarrow 20 \\le x \\le 60$.\n"
        "\\itemch Sai. Doanh thu $R(x) = -x^2 + 100x$ có $R'(x) = -2x + 100 > 0 \\Leftrightarrow x < 50$. Do đó chỉ đồng biến trên $(0; 50)$, không đồng biến trên cả $(0; 60)$.\n"
        "\\itemch Sai. Ban đầu $P_{max} = P(40) = 400$. Khi bị áp thuế 4 nghìn/sản phẩm: $P_{mới}(x) = -x^2 + 76x - 1200 = -(x - 38)^2 + 244 \\Rightarrow P_{max} = 244$. Mức giảm lợi nhuận là $400 - 244 = 156$ nghìn đồng, không phải giảm 80 nghìn đồng.\n"
        "\\end{itemchoice}"
    )
    return caudan, choices, loigiai


# ==============================================================================
# PHẦN 3: TRẢ LỜI NGẮN (SA)
# ==============================================================================

def k12_sa_c1_gtnn_trung_phuong_doan():
    """SA: Tìm GTNN của f(x) = x^4 - 10x^2 - 4 trên đoạn [0; 9]."""
    caudan = "Tìm giá trị nhỏ nhất của hàm số $f(x) = x^4 - 10x^2 - 4$ trên đoạn $[0; 9]$."
    dapan = "-29"
    loigiai = (
        "Hàm số liên tục trên $[0; 9]$.\n"
        "Ta có $f'(x) = 4x^3 - 20x = 4x(x^2 - 5) = 0 \\Leftrightarrow x = 0$ hoặc $x = \\sqrt{5}$ (do $x \\in [0; 9]$).\n"
        "Tính giá trị:\n"
        "- $f(0) = -4$.\n"
        "- $f(\\sqrt{5}) = (\\sqrt{5})^4 - 10(\\sqrt{5})^2 - 4 = 25 - 50 - 4 = -29$.\n"
        "- $f(9) = 9^4 - 10(9^2) - 4 = 5747$.\n\n"
        "Vậy giá trị nhỏ nhất của hàm số trên $[0; 9]$ bằng $-29$."
    )
    return caudan, dapan, loigiai

def k12_sa_c1_so_luong_san_pham_loi_nhuan_toi_da():
    """SA: Số lượng sản phẩm x để lợi nhuận P(x) = -x^2 + 80x - 1200 đạt tối đa."""
    caudan = "Một công ty có hàm lợi nhuận khi sản xuất và bán $x$ sản phẩm là $P(x) = -x^2 + 80x - 1200$ (nghìn đồng). Hỏi công ty cần sản xuất bao nhiêu sản phẩm để đạt lợi nhuận tối đa?"
    dapan = "40"
    loigiai = (
        "Hàm lợi nhuận là một tam thức bậc hai $P(x) = -x^2 + 80x - 1200$ có hệ số $a = -1 < 0$.\n"
        "Đỉnh của parabol đạt tại hoành độ $x = -\\frac{b}{2a} = -\\frac{80}{2(-1)} = 40$.\n"
        "Vậy công ty cần sản xuất đúng $40$ sản phẩm để đạt lợi nhuận tối đa."
    )
    return caudan, dapan, loigiai

def k12_sa_c1_loi_nhuan_toi_da_sau_thue():
    """SA: Lợi nhuận tối đa (nghìn đồng) sau khi áp thuế: P(x) = -x^2 + 76x - 1200."""
    caudan = "Cho hàm lợi nhuận sau thuế của một xưởng sản xuất là $P(x) = -x^2 + 76x - 1200$ (đơn vị: nghìn đồng). Tìm lợi nhuận tối đa mà xưởng có thể đạt được."
    dapan = "244"
    loigiai = (
        "Ta có $P'(x) = -2x + 76 = 0 \\Leftrightarrow x = 38$.\n"
        "Lợi nhuận tối đa đạt được là:\n"
        "$$P(38) = -(38)^2 + 76(38) - 1200 = -1444 + 2888 - 1200 = 244 \\text{ (nghìn đồng)}.$$"
    )
    return caudan, dapan, loigiai


# ==============================================================================
# BỔ SUNG: 3 DẠNG TOÁN MỚI (ĐẠO HÀM NGHIỆM BỘI & THỐNG KÊ GHÉP NHÓM)
# ==============================================================================

def k12_mc_c1_diem_cuc_dai_cuc_tieu_nghiem_boi():
    """MC: Tìm điểm cực đại / cực tiểu từ công thức đạo hàm f'(x) có nghiệm bội chẵn và lẻ."""
    sub = random.choice([1, 2, 3])
    if sub == 1:
        x1, x2, x3 = -1, 1, 2
        factor_str = "(x+1)^2(x-1)^3(2-x)"
        cuc_dai = 2
        cuc_tieu = 1
        nghiem_boi_chan = -1
    elif sub == 2:
        x1, x2, x3 = -2, 0, 3
        factor_str = "(x+2)^4 x (3-x)"
        cuc_dai = 3
        cuc_tieu = 0
        nghiem_boi_chan = -2
    else:
        x1, x2, x3 = 1, 3, 5
        factor_str = "(x-1)^2(x-3)^3(5-x)"
        cuc_dai = 5
        cuc_tieu = 3
        nghiem_boi_chan = 1

    caudan = f"Cho hàm số $f(x)$ có đạo hàm $f'(x) = {factor_str}$. Hàm số $f(x)$ có điểm cực đại là:"
    correct = f"x = {cuc_dai}"
    wrongs = [
        f"x = {nghiem_boi_chan}",
        f"x = {cuc_tieu}",
        f"x = {nghiem_boi_chan} \\text{{ và }} x = {cuc_dai}"
    ]
    
    choices = [f"{{\\True ${correct}$}}\n"] + [f"{{${w}$}}\n" for w in wrongs]
    random.shuffle(choices)

    loigiai = (
        f"Ta có $f'(x) = 0 \\Leftrightarrow \\left[\\begin{{aligned}}& x = {x1} \\\\ & x = {x2} \\\\ & x = {x3}.\\end{{aligned}}\\right.\n"
        f"\\begin{{itemize}}\n"
        f"    \\item Vì nghiệm $x = {nghiem_boi_chan}$ là nghiệm bội chẵn nên qua $x = {nghiem_boi_chan}$ đạo hàm $f'(x)$ không đổi dấu.\n"
        f"    \\item Nghiệm $x = {cuc_tieu}$ là nghiệm bội lẻ và $x = {cuc_dai}$ là nghiệm đơn, do đó $f'(x)$ đổi dấu khi qua hai điểm này.\n"
        f"\\end{{itemize}}\n"
        f"Khi đi qua $x = {cuc_dai}$, đạo hàm $f'(x)$ đổi dấu từ dương sang âm nên hàm số đạt cực đại tại $x = {cuc_dai}$."
    )
    return caudan, choices, loigiai


def k12_tf_c3_thong_ke_ghep_nhom_so_sanh_hai_nhom():
    """TF: So sánh các số đặc trưng mẫu số liệu ghép nhóm của học sinh hai nhóm (Trung bình, Mốt, Độ lệch chuẩn, Khoảng tứ phân vị)."""
    sub = random.choice([1, 2])
    if sub == 1:
        nA = [4, 5, 3, 4, 2]
        nB = [2, 5, 4, 3, 1]
        meanA_val = "7{,}22"
        moB_val = "6{,}75"
        sdB_val = "1{,}12"
        items = [
            (True, f"Số trung bình (kết quả làm tròn đến hàng phần trăm) của mẫu số liệu ghép nhóm của học sinh trường A là ${meanA_val}$"),
            (False, "Mốt của mẫu số liệu ghép nhóm của học sinh trường B là $6{,}5$"),
            (False, "Độ lệch chuẩn (kết quả làm tròn đến hàng phần trăm) của mẫu số liệu ghép nhóm của học sinh trường B là $1{,}13$"),
            (True, "Nếu so sánh theo khoảng tứ phân vị của mẫu số liệu ghép nhóm thì học sinh trường B có điểm trung bình đồng đều hơn")
        ]
        loigiai = (
            "\\begin{itemize}\n"
            "    \\item \\textbf{Ý a) Đúng:} Cỡ mẫu nhóm A là $n_A = 18$. Số trung bình $\\overline{x}_A = \\frac{4 \\cdot 5{,}5 + 5 \\cdot 6{,}5 + 3 \\cdot 7{,}5 + 4 \\cdot 8{,}5 + 2 \\cdot 9{,}5}{18} = \\frac{130}{18} \\approx 7{,}22$.\n"
            "    \\item \\textbf{Ý b) Sai:} Nhóm chứa mốt của B là $[6; 7)$ có tần số $5$. Ta có $M_0 = 6 + \\frac{5-2}{(5-2)+(5-4)} \\cdot 1 = 6{,}75 \\neq 6{,}5$.\n"
            "    \\item \\textbf{Ý c) Sai:} $\\overline{x}_B \\approx 7{,}233$. Phương sai $s_B^2 \\approx 1{,}262 \\implies s_B \\approx 1{,}12 \\neq 1{,}13$.\n"
            "    \\item \\textbf{Ý d) Đúng:} Khoảng tứ phân vị nhóm A là $\\Delta_{Q_A} = 8{,}375 - 6{,}1 = 2{,}275$; khoảng tứ phân vị nhóm B là $\\Delta_{Q_B} \\approx 8{,}083 - 6{,}35 = 1{,}733$. Vì $\\Delta_{Q_B} < \\Delta_{Q_A}$ nên học sinh nhóm B có điểm đồng đều hơn.\n"
            "\\end{itemize}"
        )
    else:
        nA = [3, 6, 4, 5, 2]
        nB = [1, 7, 5, 4, 3]
        items = [
            (True, "Số trung bình của mẫu số liệu ghép nhóm của học sinh trường A là $7{,}35$"),
            (True, "Nhóm chứa mốt của cả hai nhóm học sinh A và B đều là nhóm $[6; 7)$"),
            (False, "Độ lệch chuẩn của học sinh trường A bằng $2{,}5$"),
            (True, "Học sinh trường A có độ phân tán theo khoảng tứ phân vị khác biệt so với trường B")
        ]
        loigiai = (
            "\\begin{itemize}\n"
            "    \\item \\textbf{Ý a) Đúng:} $n_A = 20$, $\\overline{x}_A = \\frac{3 \\cdot 5{,}5 + 6 \\cdot 6{,}5 + 4 \\cdot 7{,}5 + 5 \\cdot 8{,}5 + 2 \\cdot 9{,}5}{20} = 7{,}35$.\n"
            "    \\item \\textbf{Ý b) Đúng:} Tần số lớn nhất của cả 2 nhóm đều đạt tại nhóm $[6; 7)$.\n"
            "    \\item \\textbf{Ý c) Sai:} Độ lệch chuẩn thực tế nhỏ hơn 2.\n"
            "    \\item \\textbf{Ý d) Đúng:} Khoảng tứ phân vị của 2 nhóm khác nhau do phân bố tích lũy khác nhau.\n"
            "\\end{itemize}"
        )

    caudan = (
        "Kết quả điều tra về điểm trung bình năm học của học sinh hai nhóm A và B được cho trong bảng tần số ghép nhóm như sau:\n"
        "\\begin{center}\n"
        "\\renewcommand{\\arraystretch}{1.2}\n"
        "\\begin{tabular}{|l|c|c|c|c|c|}\n"
        "\\hline\n"
        "\\textbf{Điểm trung bình} & $[5; 6)$ & $[6; 7)$ & $[7; 8)$ & $[8; 9)$ & $[9; 10)$ \\\\ \\hline\n"
        "\\textbf{Giá trị đại diện} & $5{,}5$ & $6{,}5$ & $7{,}5$ & $8{,}5$ & $9{,}5$ \\\\ \\hline\n"
        f"\\textbf{{Học sinh nhóm A}} & ${nA[0]}$ & ${nA[1]}$ & ${nA[2]}$ & ${nA[3]}$ & ${nA[4]}$ \\\\ \\hline\n"
        f"\\textbf{{Học sinh nhóm B}} & ${nB[0]}$ & ${nB[1]}$ & ${nB[2]}$ & ${nB[3]}$ & ${nB[4]}$ \\\\ \\hline\n"
        "\\end{tabular}\n"
        "\\end{center}\n"
        "Các mệnh đề sau đúng hay sai?"
    )
    
    choices = []
    for val, text in items:
        prefix = "\\True " if val else ""
        choices.append(f"{{{prefix}{text}}}\n")

    return caudan, choices, loigiai


def k12_mc_c3_khoang_tu_phan_vi_bieu_do_histogram():
    """MC: Xác định khoảng tứ phân vị từ biểu đồ cột tần số ghép nhóm (Histogram)."""
    sub = random.choice([1, 2])
    if sub == 1:
        y1, y2, y3, y4, y5 = 14, 30, 25, 18, 5
        total_n = 92
        q1_str = "7{,}5"
        q3_str = "16"
        correct = "8{,}5"
        wrongs = ["9{,}5", "10{,}5", "7{,}5"]
        detail_calc = (
            "Tổng số ngày là $n = 14 + 30 + 25 + 18 + 5 = 92$.\n"
            "\\begin{itemize}\n"
            "    \\item Ta có $\\frac{n}{4} = 23 \\implies Q_1$ thuộc nhóm $[6; 11)$. Áp dụng công thức:\n"
            "    $$Q_1 = 6 + \\frac{23 - 14}{30} \\cdot 5 = 7{,}5.$$\n"
            "    \\item Ta có $\\frac{3n}{4} = 69 \\implies Q_3$ thuộc nhóm $[11; 16)$. Áp dụng công thức:\n"
            "    $$Q_3 = 11 + \\frac{69 - 44}{25} \\cdot 5 = 16.$$\n"
            "    \\item Khoảng tứ phân vị: $\\Delta_Q = Q_3 - Q_1 = 16 - 7{,}5 = 8{,}5$.\n"
            "\\end{itemize}"
        )
    else:
        y1, y2, y3, y4, y5 = 10, 25, 35, 20, 10
        total_n = 100
        q1_str = "9"
        q3_str = "17{,}25"
        correct = "8{,}25"
        wrongs = ["7{,}25", "9{,}25", "10{,}5"]
        detail_calc = (
            "Tổng số ngày là $n = 10 + 25 + 35 + 20 + 10 = 100$.\n"
            "\\begin{itemize}\n"
            "    \\item Ta có $\\frac{n}{4} = 25 \\implies Q_1$ thuộc nhóm $[6; 11)$. Áp dụng công thức:\n"
            "    $$Q_1 = 6 + \\frac{25 - 10}{25} \\cdot 5 = 9.$$\n"
            "    \\item Ta có $\\frac{3n}{4} = 75 \\implies Q_3$ thuộc nhóm $[16; 21)$. Áp dụng công thức:\n"
            "    $$Q_3 = 16 + \\frac{75 - 70}{20} \\cdot 5 = 17{,}25.$$\n"
            "    \\item Khoảng tứ phân vị: $\\Delta_Q = Q_3 - Q_1 = 17{,}25 - 9 = 8{,}25$.\n"
            "\\end{itemize}"
        )

    max_y = max(y1, y2, y3, y4, y5) + 8
    tikz_code = (
        "\\begin{center}\n"
        "\\begin{tikzpicture}[xscale=0.28, yscale=0.12, font=\\small\\sffamily]\n"
        "    \\foreach \\y in {5, 10, 15, 20, 25, 30, 35} {\n"
        "        \\draw[dotted, gray!60] (1, \\y) -- (26.5, \\y);\n"
        "    }\n"
        f"    \\filldraw[fill=cyan!80!blue!50, draw=black!80] (1, 0) rectangle (6, {y1});\n"
        f"    \\node[above, font=\\footnotesize] at (3.5, {y1}) {{${y1}$}};\n"
        f"    \\filldraw[fill=cyan!80!blue!50, draw=black!80] (6, 0) rectangle (11, {y2});\n"
        f"    \\node[above, font=\\footnotesize] at (8.5, {y2}) {{${y2}$}};\n"
        f"    \\filldraw[fill=cyan!80!blue!50, draw=black!80] (11, 0) rectangle (16, {y3});\n"
        f"    \\node[above, font=\\footnotesize] at (13.5, {y3}) {{${y3}$}};\n"
        f"    \\filldraw[fill=cyan!80!blue!50, draw=black!80] (16, 0) rectangle (21, {y4});\n"
        f"    \\node[above, font=\\footnotesize] at (18.5, {y4}) {{${y4}$}};\n"
        f"    \\filldraw[fill=cyan!80!blue!50, draw=black!80] (21, 0) rectangle (26, {y5});\n"
        f"    \\node[above, font=\\footnotesize] at (23.5, {y5}) {{${y5}$}};\n"
        "    \\draw[->, >=stealth] (1, 0) -- (29, 0) node[right, font=\\bfseries\\small] {Số lượt đặt bàn};\n"
        f"    \\draw[->, >=stealth] (1, 0) -- (1, {max_y}) node[above, font=\\bfseries\\small] {{Số ngày}};\n"
        "    \\foreach \\y in {5, 10, 15, 20, 25, 30, 35} {\n"
        "        \\draw (0.7, \\y) -- (1, \\y);\n"
        "        \\node[left] at (0.7, \\y) {$\\y$};\n"
        "    }\n"
        "    \\foreach \\x in {1, 6, 11, 16, 21, 26} {\n"
        "        \\draw (\\x, -0.8) -- (\\x, 0);\n"
        "        \\node[below] at (\\x, -0.8) {$\\x$};\n"
        "    }\n"
        "\\end{tikzpicture}\n"
        "\\end{center}"
    )

    caudan = (
        "Biểu đồ dưới đây biểu diễn số lượng khách hàng đặt bàn qua hình thức trực tuyến mỗi ngày trong quý III năm 2022 của một nhà hàng. "
        "Cột thứ nhất biểu diễn số ngày có từ 1 đến 6 lượt đặt bàn, cột thứ hai biểu diễn số ngày có từ 6 đến 11 lượt đặt bàn;\\dots\n"
        f"{tikz_code}\n"
        "Khoảng tứ phân vị của mẫu số liệu ghép nhóm cho bởi biểu đồ trên là"
    )

    choices = [f"{{\\True ${correct}$}}\n"] + [f"{{${w}$}}\n" for w in wrongs]
    random.shuffle(choices)

    loigiai = (
        f"Từ biểu đồ, ta có:\n"
        f"{detail_calc}\n"
        f"Vậy ta chọn đáp án có khoảng tứ phân vị là ${correct}$."
    )
    return caudan, choices, loigiai


def k12_mc_c3_mot_mau_so_lieu_ghep_nhom():
    """MC: Tìm mốt của mẫu số liệu ghép nhóm từ bảng tần số (Mức thưởng Tết / Doanh thu)."""
    sub = random.choice([1, 2])
    if sub == 1:
        caudan = (
            "Mức thưởng Tết (triệu đồng) mà các công nhân một nhà máy nhận được như sau:\n"
            "\\begin{center}\n"
            "\\begin{tabular}{|l|c|c|c|c|}\n"
            "\\hline\n"
            "\\textbf{Mức thưởng} & $[5; 10)$ & $[10; 15)$ & $[15; 20)$ & $[20; 25)$ \\\\ \\hline\n"
            "\\textbf{Số công nhân} & $13$ & $35$ & $47$ & $25$ \\\\ \\hline\n"
            "\\end{tabular}\n"
            "\\end{center}\n"
            "Mốt của mẫu số liệu ghép nhóm gần nhất với giá trị nào sau đây?"
        )
        correct = "16{,}76"
        wrongs = ["17{,}76", "16{,}67", "17{,}67"]
        loigiai = (
            "Nhóm chứa mốt là nhóm có tần số lớn nhất: $[15; 20)$ với tần số $m_3 = 47$.\\\\\n"
            "Ta có: $u_3 = 15$, độ dài nhóm $g = 20 - 15 = 5$, tần số nhóm trước $m_2 = 35$, tần số nhóm sau $m_4 = 25$.\\\\\n"
            "Áp dụng công thức tính mốt của mẫu số liệu ghép nhóm:\n"
            "$$M_0 = u_3 + \\frac{m_3 - m_2}{(m_3 - m_2) + (m_3 - m_4)} \\cdot g = 15 + \\frac{47 - 35}{(47 - 35) + (47 - 25)} \\cdot 5 = 15 + \\frac{12}{34} \\cdot 5 \\approx 16{,}76.$$\n"
            "Vậy mốt của mẫu số liệu ghép nhóm gần nhất với giá trị $16{,}76$."
        )
    else:
        caudan = (
            "Thời gian hoàn thành một bài kiểm tra trực tuyến (phút) của học sinh được ghi lại như sau:\n"
            "\\begin{center}\n"
            "\\begin{tabular}{|l|c|c|c|c|}\n"
            "\\hline\n"
            "\\textbf{Thời gian (phút)} & $[10; 15)$ & $[15; 20)$ & $[20; 25)$ & $[25; 30)$ \\\\ \\hline\n"
            "\\textbf{Số học sinh} & $10$ & $28$ & $40$ & $22$ \\\\ \\hline\n"
            "\\end{tabular}\n"
            "\\end{center}\n"
            "Mốt của mẫu số liệu ghép nhóm trên bằng:"
        )
        correct = "22"
        wrongs = ["21{,}5", "22{,}5", "20"]
        loigiai = (
            "Nhóm chứa mốt là $[20; 25)$ có tần số lớn nhất là $40$.\\\\\n"
            "Ta có: $u_m = 20, g = 5, m_i = 40, m_{i-1} = 28, m_{i+1} = 22$.\\\\\n"
            "$$M_0 = 20 + \\frac{40 - 28}{(40 - 28) + (40 - 22)} \\cdot 5 = 20 + \\frac{12}{30} \\cdot 5 = 22.$$"
        )

    choices = [f"{{\\True ${correct}$}}\n"] + [f"{{${w}$}}\n" for w in wrongs]
    random.shuffle(choices)
    return caudan, choices, loigiai


def k12_tf_c4_tich_phan_chuyen_dong_hai_van_dong_vien():
    """TF: Ứng dụng tích phân vào bài toán chuyển động của hai vận động viên và diện tích hình phẳng."""
    tikz_fig = (
        "\\begin{center}\n"
        "\\begin{tikzpicture}[xscale=0.22, yscale=0.68, font=\\small\\sffamily]\n"
        "    \\draw[->, >=stealth, line width=0.6pt] (0, 0) -- (35, 0) node[below right] {$t\\text{ (s)}$};\n"
        "    \\draw[->, >=stealth, line width=0.6pt] (0, 0) -- (0, 8.5) node[above right] {$v\\text{ (m/s)}$};\n"
        "    \\node[below left] at (0, 0) {$O$};\n"
        "    \\fill[pattern=north east lines, pattern color=gray!80] \n"
        "        plot[domain=0:10, samples=25] (\\x, {-((\\x)/10)^3/6 + 7*(\\x)/60 + 5}) -- \n"
        "        plot[domain=10:0, samples=25] (\\x, {-((\\x)/10)^2/1.5 + 4*(\\x)/15 + 4}) -- cycle;\n"
        "    \\fill[pattern=north east lines, pattern color=gray!80] \n"
        "        plot[domain=10:30, samples=30] (\\x, {-((\\x)/10)^2/1.5 + 4*(\\x)/15 + 4}) -- \n"
        "        plot[domain=30:10, samples=30] (\\x, {-((\\x)/10)^3/6 + 7*(\\x)/60 + 5}) -- cycle;\n"
        "    \\draw[thick, smooth, domain=0:32, samples=40] plot (\\x, {-((\\x)/10)^3/6 + 7*(\\x)/60 + 5});\n"
        "    \\draw[thick, smooth, domain=0:32, samples=40] plot (\\x, {-((\\x)/10)^2/1.5 + 4*(\\x)/15 + 4});\n"
        "    \\draw[dashed] (10, 0) -- (10, 6);\n"
        "    \\draw[dashed] (30, 0) -- (30, 6);\n"
        "    \\fill (0, 4) circle (1.5pt) node[left] {$4$};\n"
        "    \\fill (0, 5) circle (1.5pt) node[left] {$5$};\n"
        "    \\fill (10, 0) circle (1.5pt) node[below] {$10$};\n"
        "    \\fill (30, 0) circle (1.5pt) node[below] {$30$};\n"
        "\\end{tikzpicture}\n"
        "\\end{center}"
    )

    caudan = (
        "Có 2 vận động viên $A$ và $B$ chạy trên một đường thẳng với vận tốc lần lượt được biểu diễn bởi đồ thị hàm số "
        "$y = v_1(t) = -\\frac{1}{6\\,000}t^3 + \\frac{7}{60}t + 5\\text{ (m/s)}$ và parabol $y = v_2(t)\\text{ (m/s)}$ như hình vẽ. "
        "Biết rằng 2 vận động viên xuất phát cùng một lúc tại cùng một vị trí.\n"
        f"{tikz_fig}\n"
        "Các mệnh đề sau đúng hay sai?"
    )

    items = [
        (True, "Quãng đường vận động viên $A$ đi được sau 30 giây là $\\int_{0}^{30} v_1(t)\\,dt$"),
        (False, "Tổng diện tích phần tô đậm như hình vẽ bằng khoảng cách giữa 2 vận động viên sau 30 giây kể từ lúc xuất phát"),
        (True, "$v_2(t) = -\\frac{1}{150}(t^2 - 40t - 600)\\text{ (m/s)}$"),
        (False, "Tại thời điểm 10 (s), vận động viên $B$ dẫn trước vận động viên $A$ một khoảng bằng $4{,}3\\text{ m}$ (làm tròn đến hàng phần mười)")
    ]

    choices = []
    for val, text in items:
        prefix = "\\True " if val else ""
        choices.append(f"{{{prefix}{text}}}\n")

    loigiai = (
        "\\begin{itemize}\n"
        "    \\item \\textbf{Ý a) Đúng:} Theo ý nghĩa vật lý của tích phân, quãng đường đi được trong khoảng thời gian $[0; 30]$ là $s_1 = \\int_{0}^{30} v_1(t)\\,dt$.\n"
        "    \\item \\textbf{Ý b) Sai:} Khoảng cách giữa 2 vận động viên tại thời điểm $t = 30$ là $d = |s_2(30) - s_1(30)| = |\\int_{0}^{30} (v_2 - v_1)\\,dt| = |S_2 - S_1| = 15{,}56 - 4{,}31 = 11{,}25\\text{ m}$. Trong khi tổng diện tích phần tô đậm là $S = S_1 + S_2 \\approx 19{,}86\\text{ m}^2 \\neq 11{,}25\\text{ m}$.\n"
        "    \\item \\textbf{Ý c) Đúng:} Parabol $y = v_2(t) = at^2 + bt + c$ đi qua $(0; 4) \\implies c = 4$. Đỉnh tại $(20; \\frac{20}{3})$ và đi qua $(10; 6) \\implies a = -\\frac{1}{150}, b = \\frac{4}{15} \\implies v_2(t) = -\\frac{1}{150}(t^2 - 40t - 600)$.\n"
        "    \\item \\textbf{Ý d) Sai:} Tại $t = 10$, ta có $s_1(10) = \\int_{0}^{10} v_1(t)\\,dt \\approx 55{,}42\\text{ m}$; $s_2(10) = \\int_{0}^{10} v_2(t)\\,dt \\approx 51{,}11\\text{ m}$. Vì $s_1(10) > s_2(10)$ nên vận động viên $A$ dẫn trước vận động viên $B$ một khoảng $\\Delta s \\approx 4{,}3\\text{ m}$, không phải vận động viên $B$ dẫn trước.\n"
        "\\end{itemize}"
    )
    return caudan, choices, loigiai


def k12_tf_c4_phan_ra_phong_xa_pt_vi_phan():
    """TF: Bài toán thực tế phân rã chất phóng xạ Iodine-131 theo phương trình vi phân m'(t) = k m(t)."""
    caudan = (
        "Một mẫu đồng vị phóng xạ (ví dụ: Iodine-131 được sử dụng trong y tế) có khối lượng ban đầu là $800\\text{ mg}$. "
        "Sau $5$ ngày, khối lượng của mẫu chất này phân rã và chỉ còn lại $400\\text{ mg}$. "
        "Gọi $m(t)$ là khối lượng của mẫu chất phóng xạ tại thời điểm $t$ (ngày). "
        "Biết rằng tốc độ phân rã của mẫu chất tỉ lệ thuận với khối lượng hiện có của nó, tức là $m'(t) = k \\cdot m(t)$, "
        "với $k$ là hằng số khác 0 và $m(t) > 0$ với $t \\ge 0$.\n"
        "Xét tính đúng sai của các khẳng định sau:"
    )

    items = [
        (True, "Hằng số tốc độ phân rã của mẫu chất là $k = -\\frac{1}{5}\\ln 2$"),
        (True, "Sau 15 ngày kể từ thời điểm ban đầu, khối lượng mẫu chất còn lại là $100\\text{ mg}$"),
        (False, "Khối lượng của mẫu chất phóng xạ được tính bởi công thức $m(t) = 400e^{kt}$ với $t \\ge 0$"),
        (False, "Để khối lượng mẫu chất phân rã chỉ còn $50\\text{ mg}$, cần đúng $10$ ngày kể từ thời điểm ban đầu")
    ]

    choices = []
    for val, text in items:
        prefix = "\\True " if val else ""
        choices.append(f"{{{prefix}{text}}}\n")

    loigiai = (
        "Từ phương trình vi phân $m'(t) = k \\cdot m(t) \\Leftrightarrow \\frac{m'(t)}{m(t)} = k \\implies \\ln m(t) = kt + C \\implies m(t) = m_0 e^{kt}$.\\\\\n"
        "Với $m_0 = m(0) = 800\\text{ mg} \\implies m(t) = 800e^{kt}$.\\\\\n"
        "Tại $t = 5$, ta có $m(5) = 800e^{5k} = 400 \\implies e^{5k} = \\frac{1}{2} = 2^{-1} \\implies 5k = -\\ln 2 \\implies k = -\\frac{1}{5}\\ln 2$.\n"
        "\\begin{itemize}\n"
        "    \\item \\textbf{Ý a) Đúng:} Hằng số tốc độ phân rã $k = -\\frac{1}{5}\\ln 2$.\n"
        "    \\item \\textbf{Ý b) Đúng:} Sau 15 ngày: $m(15) = 800 \\cdot e^{15k} = 800 \\cdot (e^{5k})^3 = 800 \\cdot \\left(\\frac{1}{2}\\right)^3 = 800 \\cdot \\frac{1}{8} = 100\\text{ mg}$.\n"
        "    \\item \\textbf{Ý c) Sai:} Công thức đúng là $m(t) = 800e^{kt}$ (vì khối lượng ban đầu là $800\\text{ mg}$, không phải $400\\text{ mg}$).\n"
        "    \\item \\textbf{Ý d) Sai:} Để còn $50\\text{ mg}$: $800 \\cdot \\left(\\frac{1}{2}\\right)^{t/5} = 50 \\implies \\left(\\frac{1}{2}\\right)^{t/5} = \\frac{1}{16} = \\left(\\frac{1}{2}\\right)^4 \\implies \\frac{t}{5} = 4 \\implies t = 20\\text{ ngày}$ (không phải 10 ngày).\n"
        "\\end{itemize}"
    )
    return caudan, choices, loigiai
