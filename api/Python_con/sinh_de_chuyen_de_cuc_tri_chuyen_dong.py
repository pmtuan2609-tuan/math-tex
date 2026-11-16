import random
from random import randint, choice, uniform
import math
from fractions import Fraction
import sympy as sp
from sympy import symbols, simplify, latex, Rational, diff, solve, exp, oo

x, t = symbols('x t')

def fmt_p(val):
    """Format float or Fraction to LaTeX string"""
    f = Fraction(val).limit_denominator(1000)
    if f.denominator == 1:
        return str(f.numerator)
    return f"\\dfrac{{{f.numerator}}}{{{f.denominator}}}"

def fmt_signed(val, var=""):
    """Format signed term: + 3x, - 2x, etc."""
    f = Fraction(val).limit_denominator(1000)
    if f == 0:
        return ""
    sgn = "+" if f > 0 else "-"
    abs_f = abs(f)
    if var != "":
        if abs_f == 1:
            coef = ""
        else:
            coef = f"{abs_f.numerator}" if abs_f.denominator == 1 else f"\\dfrac{{{abs_f.numerator}}}{{{abs_f.denominator}}}"
        return f" {sgn} {coef}{var}"
    else:
        num = f"{abs_f.numerator}" if abs_f.denominator == 1 else f"\\dfrac{{{abs_f.numerator}}}{{{abs_f.denominator}}}"
        return f" {sgn} {num}"

def fmt_first_term(val, var=""):
    """Format first term of polynomial"""
    f = Fraction(val).limit_denominator(1000)
    if f == 0:
        return ""
    if var != "":
        if f == 1:
            return var
        if f == -1:
            return f"-{var}"
        if f.denominator == 1:
            return f"{f.numerator}{var}"
        return f"\\dfrac{{{f.numerator}}}{{{f.denominator}}}{var}"
    else:
        if f.denominator == 1:
            return f"{f.numerator}"
        return f"\\dfrac{{{f.numerator}}}{{{f.denominator}}}"

# ==============================================================================
# DẠNG 1 (ẢNH 1 - CÂU 5): Phương trình đường thẳng qua hai điểm cực trị hàm bậc 3
# ==============================================================================
def sinh_cau_ptdt_qua_2_cuc_tri_bac_ba():
    # Chọn hai điểm cực trị x1 < x2 nguyên đẹp
    x1 = randint(-4, 2)
    x2 = randint(x1 + 1, 5)
    # y' = 3a(x - x1)(x - x2) = 3a[x^2 - (x1+x2)x + x1*x2]
    # Để hệ số y nguyên đẹp, chọn a = 1 hoặc -1 (hoặc a = 1/3)
    a_coef = choice([1, -1])
    # y' = 3*a_coef * x^2 - 3*a_coef*(x1+x2)*x + 3*a_coef*x1*x2
    b_coef = -Fraction(3 * a_coef * (x1 + x2), 2)
    # Để b nguyên, cần 3*a_coef*(x1+x2) chẵn => x1+x2 chẵn
    while (x1 + x2) % 2 != 0:
        x1 = randint(-4, 2)
        x2 = randint(x1 + 1, 5)
    
    b_val = -3 * a_coef * (x1 + x2) // 2
    c_val = 3 * a_coef * x1 * x2
    d_val = randint(-6, 6)
    
    # Hàm số: y = a_coef * x^3 + b_val * x^2 + c_val * x + d_val
    # y' = 3*a_coef * x^2 + 2*b_val * x + c_val
    # Chia y cho y':
    # Phần dư R(x) = [c - 2b^2 / (3a)] x + [d - bc / (9a)] ...
    # Tính trực tiếp qua 2 điểm cực trị:
    y1 = a_coef * x1**3 + b_val * x1**2 + c_val * x1 + d_val
    y2 = a_coef * x2**3 + b_val * x2**2 + c_val * x2 + d_val
    
    # Đường thẳng qua (x1, y1) và (x2, y2):
    # k = (y2 - y1) / (x2 - x1)
    k_slope = Fraction(y2 - y1, x2 - x1)
    m_intercept = y1 - k_slope * x1
    
    # Phương trình đường thẳng: y = kx + m
    def fmt_line(k, m):
        k_str = fmt_first_term(k, "x")
        m_str = fmt_signed(m)
        if k_str == "":
            return f"y = {fmt_p(m)}"
        return f"y = {k_str}{m_str}".replace("  ", " ")

    line_true = fmt_line(k_slope, m_intercept)
    
    # Sinh 3 phương án sai
    cand_distractors = [
        fmt_line(-k_slope, m_intercept),
        fmt_line(k_slope, -m_intercept),
        fmt_line(k_slope, m_intercept + 2),
        fmt_line(k_slope, m_intercept - 2),
        fmt_line(-k_slope, -m_intercept),
        fmt_line(k_slope + 1, m_intercept)
    ]
    seen = {line_true}
    wrong_opts = []
    for cand in cand_distractors:
        if cand not in seen:
            seen.add(cand)
            wrong_opts.append(cand)
            if len(wrong_opts) == 3:
                break
                
    # Hiển thị hàm số
    func_str = f"y = {fmt_first_term(a_coef, 'x^3')}{fmt_signed(b_val, 'x^2')}{fmt_signed(c_val, 'x')}{fmt_signed(d_val)}"
    
    caudan = f"Cho hàm số ${func_str}$. Phương trình đường thẳng đi qua hai điểm cực trị của đồ thị hàm số là:"
    
    dapan_a = f"{{\\True ${line_true}$}}\n"
    dapan_b = f"{{${wrong_opts[0]}$}}\n"
    dapan_c = f"{{${wrong_opts[1]}$}}\n"
    dapan_d = f"{{${wrong_opts[2]}$}}\n"
    
    loigiai = f"""Ta có: $y' = {fmt_first_term(3*a_coef, 'x^2')}{fmt_signed(2*b_val, 'x')}{fmt_signed(c_val)}$.\\\\
$y' = 0 \\Leftrightarrow \\hoac{{&x = {x1} \\\\ &x = {x2}}}$.\\\\
Tọa độ hai điểm cực trị của đồ thị hàm số là $A({x1}; {y1})$ và $B({x2}; {y2})$.\\\\
Đường thẳng đi qua hai điểm cực trị $A, B$ có hệ số góc là:
$$k = \\dfrac{{y_B - y_A}}{{x_B - x_A}} = \\dfrac{{{y2} - ({y1})}}{{{x2} - ({x1})}} = {fmt_p(k_slope)}$$
Phương trình đường thẳng $AB$ là:
$$y = {fmt_p(k_slope)}(x - ({x1})) + ({y1}) \\Leftrightarrow {line_true}.$$"""

    phuongan = [dapan_a, dapan_b, dapan_c, dapan_d]
    random.shuffle(phuongan)
    return caudan, phuongan, loigiai

# ==============================================================================
# DẠNG 2 (ẢNH 1 - CÂU 6): Bài toán chuyển động, khoảng thời gian vận tốc giảm
# ==============================================================================
def sinh_cau_chuyen_dong_van_toc_giam():
    # s(t) = (1/3) t^3 - (t0) t^2 + c t
    # v(t) = s'(t) = t^2 - 2*t0 * t + c
    # a(t) = v'(t) = 2t - 2*t0 = 2(t - t0)
    # Vận tốc giảm <=> v'(t) < 0 <=> 0 <= t < t0 => Khoảng (0; t0)
    t0 = randint(3, 8)
    # Để nghiệm v(t) = 0 có nghiệm dương hoặc phân biệt
    # Cho c sao cho v(t) > 0 tại t = 0 và đỉnh có thể > 0 hoặc < 0
    c_val = t0**2 - randint(1, 5) if t0**2 > 5 else t0**2 + randint(1, 10)
    
    s_expr = f"s(t) = \\dfrac{{1}}{{3}}t^3{fmt_signed(-t0, 't^2')}{fmt_signed(c_val, 't')}"
    
    caudan = f"""Một chất điểm chuyển động trên trục tọa độ theo phương trình ${s_expr}$ (trong đó $t$ tính bằng giây, $t \\ge 0$ và $s$ tính bằng mét). Khi đó, $v(t) = s'(t)$ là vận tốc của chất điểm. Trong khoảng thời gian nào (đơn vị giây) tính từ lúc bắt đầu chuyển động, vận tốc của chất điểm giảm?"""
    
    opt_true = f"(0; {t0})"
    # Các khoảng nhiễu:
    cand_distractors = [
        f"({t0}; +\\infty)",
        f"(0; {2*t0})",
        f"({max(1, t0-2)}; {t0+2})",
        f"(0; {t0+1})",
        f"({t0-1}; +\\infty)"
    ]
    seen = {opt_true}
    wrong_opts = []
    for cand in cand_distractors:
        if cand not in seen:
            seen.add(cand)
            wrong_opts.append(cand)
            if len(wrong_opts) == 3:
                break
                
    dapan_a = f"{{\\True ${opt_true}$}}\n"
    dapan_b = f"{{${wrong_opts[0]}$}}\n"
    dapan_c = f"{{${wrong_opts[1]}$}}\n"
    dapan_d = f"{{${wrong_opts[2]}$}}\n"
    
    loigiai = f"""Ta có vận tốc của chất điểm là:
$$v(t) = s'(t) = t^2{fmt_signed(-2*t0, 't')}{fmt_signed(c_val)}.$$
Gia tốc của chất điểm là:
$$a(t) = v'(t) = 2t - {2*t0}.$$
Vận tốc của chất điểm giảm khi và chỉ khi:
$$v'(t) < 0 \\Leftrightarrow 2t - {2*t0} < 0 \\Leftrightarrow t < {t0}.$$
Vì thời gian $t \\ge 0$, do đó trong khoảng thời gian $(0; {t0})$ (giây) tính từ lúc bắt đầu chuyển động, vận tốc của chất điểm giảm."""

    phuongan = [dapan_a, dapan_b, dapan_c, dapan_d]
    random.shuffle(phuongan)
    return caudan, phuongan, loigiai

# ==============================================================================
# DẠNG 3 (ẢNH 2 - CÂU 1): Đúng/Sai hàm số có đạo hàm f'(x) = (ax^2+bx+c)e^x
# ==============================================================================
def sinh_cau_dung_sai_dao_ham_mu():
    # f'(x) = (A x^2 + B x + C) e^x
    # Chọn hai nghiệm x1 < x2 của tam thức bậc 2
    # Thường x1 nguyên âm, x2 là phân số (ví dụ -1 và 1/2) hoặc 2 số nguyên
    # Để nghiệm đẹp: x1 = -1, x2 = 1/2 => (x + 1)(2x - 1) = 2x^2 + x - 1
    pair = choice([(-1, Fraction(1, 2)), (-2, 1), (-1, 2), (-3, 1)])
    x1, x2 = pair
    # Tam thức P(x) = A(x - x1)(x - x2)
    if isinstance(x2, Fraction):
        A = x2.denominator
        B = int(-A * (x1 + x2))
        C = int(A * x1 * x2)
    else:
        A = 1
        B = -(x1 + x2)
        C = x1 * x2
        
    f_prime_poly = f"{fmt_first_term(A, 'x^2')}{fmt_signed(B, 'x')}{fmt_signed(C)}"
    caudan = f"Cho hàm số $y = f(x)$ có đạo hàm $f'(x) = ({f_prime_poly})e^x, \\forall x \\in \\mathbb{{R}}$. Gọi $(C)$ là đồ thị của hàm số $y = f(x)$."
    
    # Ý a: Cực trị của f(x)
    # e^x > 0 => dấu f'(x) cùng dấu với A*x^2 + B*x + C
    # Với A > 0: ngoài cùng dương, trong trái âm:
    # x < x1: f'(x) > 0
    # x1 < x < x2: f'(x) < 0 => x1 là điểm CỰC ĐẠI
    # x > x2: f'(x) > 0 => x2 là điểm CỰC TIỂU
    # Câu khẳng định: đảo lại hoặc giữ đúng
    y_a_dung = choice([True, False])
    if y_a_dung:
        opt_a_str = f"Hàm số $f(x)$ đạt cực đại tại điểm $x = {fmt_p(x1)}$ và đạt cực tiểu tại điểm $x = {fmt_p(x2)}$."
        lg_a = f"Ta có $e^x > 0, \\forall x \\in \\mathbb{{R}}$. Phương trình $f'(x) = 0 \\Leftrightarrow {f_prime_poly} = 0 \\Leftrightarrow \\hoac{{&x = {fmt_p(x1)} \\\\ &x = {fmt_p(x2)}}}$. Vì $A = {A} > 0$ nên qua $x = {fmt_p(x1)}$ đạo hàm đổi dấu từ dương sang âm ($f(x)$ đạt cực đại), qua $x = {fmt_p(x2)}$ đạo hàm đổi dấu từ âm sang dương ($f(x)$ đạt cực tiểu). Mệnh đề này **ĐÚNG**."
    else:
        opt_a_str = f"Hàm số $f(x)$ đạt cực tiểu tại điểm $x = {fmt_p(x1)}$ và đạt cực đại tại điểm $x = {fmt_p(x2)}$."
        lg_a = f"Ta có $e^x > 0, \\forall x$. Dấu của $f'(x)$ phụ thuộc tam thức ${f_prime_poly}$. Vì $A = {A} > 0$ nên $f(x)$ đạt cực đại tại $x = {fmt_p(x1)}$ và đạt cực tiểu tại $x = {fmt_p(x2)}$. Mệnh đề này **SAI**."

    # Ý b: So sánh giá trị hàm số trên một khoảng nghịch biến (x1, x2)
    # Lấy 3 điểm u < v < w nằm trong khoảng (x1, x2)
    # Ví dụ với x1 = -1, x2 = 1/2: lấy 1/6 < 1/5 < 1/4 nằm trong (-1; 1/2)
    # Vì f(x) nghịch biến trên (x1, x2) nên u < v < w => f(u) > f(v) > f(w)
    y_b_dung = choice([True, False])
    if x1 < 0 < x2:
        u_val, v_val, w_val = "1/6", "1/5", "1/4" # 1/6 < 1/5 < 1/4
        u_tex, v_tex, w_tex = "\\dfrac{1}{6}", "\\dfrac{1}{5}", "\\dfrac{1}{4}"
    else:
        u_val, v_val, w_val = "0", "1/2", "1"
        u_tex, v_tex, w_tex = "0", "\\dfrac{1}{2}", "1"
        
    if y_b_dung:
        # Khẳng định đúng: f(1/4) < f(1/5) < f(1/6)
        opt_b_str = f"$f\\left({w_tex}\\right) < f\\left({v_tex}\\right) < f\\left({u_tex}\\right)$."
        lg_b = f"Vì các điểm ${u_tex} < {v_tex} < {w_tex}$ đều thuộc khoảng nghịch biến $({fmt_p(x1)}; {fmt_p(x2)})$ của hàm số $f(x)$ nên $f\\left({w_tex}\\right) < f\\left({v_tex}\\right) < f\\left({u_tex}\\right)$. Mệnh đề này **ĐÚNG**."
    else:
        # Khẳng định sai: f(1/6) < f(1/5) < f(1/4)
        opt_b_str = f"$f\\left({u_tex}\\right) < f\\left({v_tex}\\right) < f\\left({w_tex}\\right)$."
        lg_b = f"Hàm số $f(x)$ nghịch biến trên khoảng $({fmt_p(x1)}; {fmt_p(x2)})$. Do ${u_tex} < {v_tex} < {w_tex}$ nên ta phải có $f\\left({u_tex}\\right) > f\\left({v_tex}\\right) > f\\left({w_tex}\\right)$. Mệnh đề này **SAI**."

    # Ý c: Cực trị của g(x) = f'(x)
    # g'(x) = [2Ax + B + (Ax^2 + Bx + C)] e^x = [Ax^2 + (2A + B)x + (B + C)] e^x
    # Với A = 2, B = 1, C = -1: g'(x) = [2x^2 + 5x + 0]e^x = x(2x + 5)e^x
    # g'(x) = 0 <=> x = 0 hoặc x = -5/2. Tại x = 0: đổi dấu từ âm sang dương => cực tiểu!
    g_A = A
    g_B = 2 * A + B
    g_C = B + C
    # delta của g'
    # Tính điểm x = 0: nếu g_C == 0 thì x = 0 là nghiệm của g'(x) = 0
    # Xét tại x = 0:
    g_prime_0 = g_C
    y_c_dung = choice([True, False])
    if g_C == 0:
        # x = 0 là điểm dừng của g(x)
        # đạo hàm cấp 2 tại 0: g''(0) = g_B
        is_cd = (g_B < 0)
        cuc_str = "cực đại" if is_cd else "cực tiểu"
        say_str = cuc_str if y_c_dung else ("cực tiểu" if is_cd else "cực đại")
        opt_c_str = f"Xét hàm số $g(x) = f'(x)$. Hàm số $g(x)$ đạt {say_str} tại điểm $x = 0$."
        lg_c = f"Ta có $g'(x) = f''(x) = [{fmt_first_term(g_A, 'x^2')}{fmt_signed(g_B, 'x')}{fmt_signed(g_C)}]e^x$. Với $x = 0$ ta thấy $g'(0) = 0$ và qua $x = 0$ đạo hàm đổi dấu nên $x = 0$ là điểm {cuc_str}. Mệnh đề này **{'ĐÚNG' if y_c_dung else 'SAI'}**."
    else:
        opt_c_str = f"Xét hàm số $g(x) = f'(x)$. Hàm số $g(x)$ đạt cực trị tại điểm $x = 0$."
        y_c_dung = False
        lg_c = f"Ta có $g'(0) = {g_C} \\ne 0$ nên $x = 0$ không phải là điểm cực trị của $g(x)$. Mệnh đề này **SAI**."

    # Ý d: Hệ số góc tiếp tuyến k = f'(x)
    # f'(x) = (Ax^2 + Bx + C) e^x
    # Tại x = 0, f'(0) = C
    # Khảo sát g(x) = f'(x), giá trị nhỏ nhất của f'(x) thường đạt tại điểm cực tiểu của g(x)
    y_d_dung = choice([True, False])
    min_val_approx = C
    if y_d_dung:
        opt_d_str = f"Tồn tại tiếp tuyến của đồ thị $(C)$ có hệ số góc bằng ${C}$."
        lg_d = f"Hệ số góc của tiếp tuyến tại điểm có hoành độ $x = 0$ là $k = f'(0) = ({C})e^0 = {C}$. Do đó tồn tại tiếp tuyến thỏa mãn. Mệnh đề này **ĐÚNG**."
    else:
        opt_d_str = f"Không tồn tại tiếp tuyến nào của đồ thị $(C)$ có hệ số góc nhỏ hơn ${C - 2}$."
        lg_d = f"Xét hàm số $g(x) = f'(x)$, giá trị cực tiểu của $g(x)$ nhỏ hơn ${C - 2}$ nên vẫn tồn tại tiếp tuyến có hệ số góc nhỏ hơn. Mệnh đề này **SAI**."

    choice_a = f"{{\\True {opt_a_str}}}" if y_a_dung else f"{{{opt_a_str}}}"
    choice_b = f"{{\\True {opt_b_str}}}" if y_b_dung else f"{{{opt_b_str}}}"
    choice_c = f"{{\\True {opt_c_str}}}" if y_c_dung else f"{{{opt_c_str}}}"
    choice_d = f"{{\\True {opt_d_str}}}" if y_d_dung else f"{{{opt_d_str}}}"

    choices = [choice_a, choice_b, choice_c, choice_d]
    
    loigiai = f"""\\begin{{itemchoice}}
\\itemch {lg_a}
\\itemch {lg_b}
\\itemch {lg_c}
\\itemch {lg_d}
\\end{{itemchoice}}"""

    return caudan, choices, loigiai

# ==============================================================================
# DẠNG 4 (ẢNH 2 - CÂU 2): Đúng/Sai hàm số bậc ba và hình học hai điểm cực trị
# ==============================================================================
def sinh_cau_dung_sai_bac_ba_hinh_hoc():
    # y = a/3 x^3 + b/2 x^2 + c x
    # y' = a x^2 + b x + c
    # Chọn hai điểm cực trị x1, x2 nguyên dương/âm đẹp
    x1 = choice([1, 2])
    x2 = x1 + choice([2, 4]) # ví dụ 1 và 3
    a_lead = -1 # a = -1/3
    # y' = -(x - x1)(x - x2) = -x^2 + (x1+x2)x - x1*x2
    B_coef = x1 + x2
    C_coef = -x1 * x2
    
    # y = -1/3 x^3 + (B_coef/2) x^2 + C_coef x
    # Cần B_coef chẵn để B_coef/2 nguyên
    while (x1 + x2) % 2 != 0:
        x2 += 1
    B_coef = x1 + x2
    C_coef = -x1 * x2
    b_half = B_coef // 2
    d_const = randint(-2, 2)
    
    y1 = Fraction(-1, 3)*x1**3 + b_half*x1**2 + C_coef*x1 + d_const
    y2 = Fraction(-1, 3)*x2**3 + b_half*x2**2 + C_coef*x2 + d_const
    
    # Đường thẳng AB: y = kx + m
    k_AB = Fraction(y2 - y1, x2 - x1)
    m_AB = y1 - k_AB * x1
    
    # Giao điểm M(xM, 0) trên Ox và N(0, yN) trên Oy
    # y = 0 => xM = -m_AB / k_AB
    x_M = -m_AB / k_AB
    y_N = m_AB
    
    # Tam giác OMN vuông tại O => Bán kính đường tròn ngoại tiếp R = MN / 2 = sqrt(xM^2 + yN^2) / 2
    R_binh = (x_M**2 + y_N**2) / 4
    
    func_tex = f"y = -\\dfrac{{1}}{{3}}x^3{fmt_signed(b_half, 'x^2')}{fmt_signed(C_coef, 'x')}{fmt_signed(d_const)}"
    caudan = f"Cho hàm số ${func_tex}$ có đồ thị $(C)$. Gọi $A, B$ là hai điểm cực trị của $(C)$."
    
    # Ý a: Đạo hàm
    y_a_dung = choice([True, False])
    correct_der = f"-x^2{fmt_signed(B_coef, 'x')}{fmt_signed(C_coef)}"
    if y_a_dung:
        opt_a_str = f"Đạo hàm của hàm số đã cho là $y' = {correct_der}$."
        lg_a = f"Ta có $y' = \\left(-\\dfrac{{1}}{{3}}x^3{fmt_signed(b_half, 'x^2')}{fmt_signed(C_coef, 'x')}{fmt_signed(d_const)}\\right)' = {correct_der}$. Mệnh đề này **ĐÚNG**."
    else:
        wrong_der = f"-x^2{fmt_signed(-B_coef, 'x')}{fmt_signed(C_coef)}"
        opt_a_str = f"Đạo hàm của hàm số đã cho là $y' = {wrong_der}$."
        lg_a = f"Đạo hàm chính xác phải là $y' = {correct_der}$. Mệnh đề này **SAI**."

    # Ý b: Đồng biến / nghịch biến
    # a < 0 nên trong khoảng (x1, x2) thì y' > 0 => hàm số ĐỒNG BIẾN trên (x1, x2)
    # Ngoài khoảng: nghịch biến
    y_b_dung = choice([True, False])
    if y_b_dung:
        opt_b_str = f"Hàm số đã cho đồng biến trên khoảng $({x1}; {x2})$."
        lg_b = f"Phương trình $y' = 0 \\Leftrightarrow \\hoac{{&x = {x1} \\\\ &x = {x2}}}$. Với $x \\in ({x1}; {x2})$ thì $y' > 0$ nên hàm số đồng biến trên $({x1}; {x2})$. Mệnh đề này **ĐÚNG**."
    else:
        opt_b_str = f"Hàm số đã cho nghịch biến trên khoảng $({x1}; {x2})$."
        lg_b = f"Vì hệ số của $x^2$ âm nên trong khoảng hai nghiệm $({x1}; {x2})$, $y' > 0$ (hàm số đồng biến). Mệnh đề này **SAI**."

    # Ý c: Diện tích tam giác IAB
    # Chọn I(xI, yI)
    x_I = randint(-2, 4)
    y_I = randint(-4, 4)
    # S_IAB = 1/2 | (xA - xI)(yB - yI) - (xB - xI)(yA - yI) |
    S_IAB = abs((x1 - x_I)*(y2 - y_I) - (x2 - x_I)*(y1 - y_I)) / 2
    y_c_dung = choice([True, False])
    say_S = S_IAB if y_c_dung else S_IAB + 1
    opt_c_str = f"Cho điểm $I({x_I}; {y_I})$. Diện tích tam giác $IAB$ bằng ${fmt_p(say_S)}$."
    lg_c = f"Tọa độ hai điểm cực trị là $A({x1}; {fmt_p(y1)})$ và $B({x2}; {fmt_p(y2)})$. Ta có $\\vec{{IA}} = ({x1 - x_I}; {fmt_p(y1 - y_I)})$, $\\vec{{IB}} = ({x2 - x_I}; {fmt_p(y2 - y_I)})$. Diện tích tam giác $IAB$ là $S = \\dfrac{{1}}{{2}}|x_{{\\vec{{IA}}}}y_{{\\vec{{IB}}}} - x_{{\\vec{{IB}}}}y_{{\\vec{{IA}}}}| = {fmt_p(S_IAB)}$. Mệnh đề này **{'ĐÚNG' if y_c_dung else 'SAI'}**."

    # Ý d: Bán kính đường tròn ngoại tiếp tam giác OMN
    y_d_dung = choice([True, False])
    # R = sqrt(R_binh)
    R_val_str = f"\\dfrac{{\\sqrt{{{fmt_p(4 * R_binh)}}}}}{{2}}" if R_binh.denominator == 1 else f"\\sqrt{{{fmt_p(R_binh)}}}"
    say_R_str = R_val_str if y_d_dung else f"{R_val_str} + 1"
    opt_d_str = f"Gọi $d$ là đường thẳng đi qua hai điểm cực trị $A$ và $B$. Đường thẳng $d$ cắt $Ox$ tại $M$ và cắt $Oy$ tại $N$ (với $O$ là gốc tọa độ). Bán kính đường tròn ngoại tiếp tam giác $OMN$ bằng ${say_R_str}$."
    lg_d = f"Phương trình đường thẳng $AB$ là $y = {fmt_p(k_AB)}x{fmt_signed(m_AB)}$. Giao điểm với các trục tọa độ là $M({fmt_p(x_M)}; 0)$ và $N(0; {fmt_p(y_N)})$. Tam giác $OMN$ vuông tại $O$ nên bán kính đường tròn ngoại tiếp là $R = \\dfrac{{MN}}{{2}} = \\dfrac{{\\sqrt{{OM^2 + ON^2}}}}{{2}} = {R_val_str}$. Mệnh đề này **{'ĐÚNG' if y_d_dung else 'SAI'}**."

    choice_a = f"{{\\True {opt_a_str}}}" if y_a_dung else f"{{{opt_a_str}}}"
    choice_b = f"{{\\True {opt_b_str}}}" if y_b_dung else f"{{{opt_b_str}}}"
    choice_c = f"{{\\True {opt_c_str}}}" if y_c_dung else f"{{{opt_c_str}}}"
    choice_d = f"{{\\True {opt_d_str}}}" if y_d_dung else f"{{{opt_d_str}}}"

    choices = [choice_a, choice_b, choice_c, choice_d]
    
    loigiai = f"""\\begin{{itemchoice}}
\\itemch {lg_a}
\\itemch {lg_b}
\\itemch {lg_c}
\\itemch {lg_d}
\\end{{itemchoice}}"""

    return caudan, choices, loigiai

# ==============================================================================
# DẠNG 5 (ẢNH 3 - CÂU 3): Đúng/Sai hàm phân thức bậc 2/1 và đường thẳng qua cực trị
# ==============================================================================
def sinh_cau_dung_sai_bac_2_1_cuc_tri():
    # y = (a x^2 + b x + c) / (d x + e)
    # Chọn d = 1 hoặc 2 hoặc 3, e nguyên
    d_coef = choice([1, 2, 3])
    e_coef = choice([-1, 1, -2, 2])
    # Để có 2 cực trị, đạo hàm y' có tử số Delta > 0
    # Tử số y' = a*d*x^2 + 2*a*e*x + (b*e - c*d)
    a_coef = choice([-3, -2, -1, 1, 2, 3])
    b_coef = randint(-4, 4)
    c_coef = randint(-5, 5)
    while c_coef == 0:
        c_coef = randint(-5, 5)
        
    # Tử số đạo hàm:
    A_der = a_coef * d_coef
    B_der = 2 * a_coef * e_coef
    C_der = b_coef * e_coef - c_coef * d_coef
    delta = B_der**2 - 4 * A_der * C_der
    while delta <= 0:
        c_coef = randint(-6, 6)
        C_der = b_coef * e_coef - c_coef * d_coef
        delta = B_der**2 - 4 * A_der * C_der

    # Nghiệm tử số đạo hàm
    x1_der = Fraction(-B_der - int(math.isqrt(int(delta))), 2 * A_der) if math.isqrt(int(delta))**2 == delta else (-B_der - delta**0.5) / (2 * A_der)
    x2_der = Fraction(-B_der + int(math.isqrt(int(delta))), 2 * A_der) if math.isqrt(int(delta))**2 == delta else (-B_der + delta**0.5) / (2 * A_der)
    
    # Đường thẳng qua hai điểm cực trị của hàm y = u/v là y = u'/v' = (2ax + b) / d
    # y = (2a/d) x + b/d
    k_ct = Fraction(2 * a_coef, d_coef)
    m_ct = Fraction(b_coef, d_coef)
    
    num_str = f"{fmt_first_term(a_coef, 'x^2')}{fmt_signed(b_coef, 'x')}{fmt_signed(c_coef)}"
    den_str = f"{fmt_first_term(d_coef, 'x')}{fmt_signed(e_coef)}"
    caudan = f"Cho hàm số $y = \\dfrac{{{num_str}}}{{{den_str}}}$ có đồ thị là $(C)$."
    
    # Ý a: Đạo hàm
    der_num_str = f"{fmt_first_term(A_der, 'x^2')}{fmt_signed(B_der, 'x')}{fmt_signed(C_der)}"
    opt_a_str = f"Đạo hàm của hàm số đã cho là $y' = \\dfrac{{{der_num_str}}}{{({den_str})^2}}$."
    y_a_dung = True
    lg_a = f"Áp dụng công thức tính đạo hàm của hàm phân thức $y' = \\dfrac{{u'v - uv'}}{{v^2}}$, ta có tử số là $({fmt_first_term(2*a_coef, 'x')}{fmt_signed(b_coef)})({den_str}) - ({num_str})({d_coef}) = {der_num_str}$. Mệnh đề này **ĐÚNG**."

    # Ý b: Khoảng đồng biến / nghịch biến
    y_b_dung = choice([True, False])
    # Nếu A_der < 0 thì hàm số đồng biến trong khoảng giữa 2 nghiệm (nếu không chứa điểm gián đoạn x = -e/d)
    x_pole = Fraction(-e_coef, d_coef)
    opt_b_str = f"Hàm số đã cho đồng biến trên khoảng $(-\\infty; {fmt_p(x_pole)})$."
    if y_b_dung:
        opt_b_str = f"Hàm số đã cho nghịch biến trên từng khoảng xác định." if delta < 0 else f"Phương trình $y' = 0$ có hai nghiệm phân biệt."
        lg_b = f"Tử số của $y'$ có $\\Delta > 0$ nên $y' = 0$ có hai nghiệm phân biệt. Mệnh đề này **ĐÚNG**."
    else:
        lg_b = f"Dấu của $y'$ thay đổi qua các nghiệm của tử số nên hàm số không đồng biến trên toàn khoảng $(-\\infty; {fmt_p(x_pole)})$. Mệnh đề này **SAI**."

    # Ý c: Đường thẳng qua 2 cực trị vuông góc với d1
    # Đường thẳng qua 2 cực trị là Delta: y = (2a/d) x + b/d <=> (2a/d) x - y + b/d = 0
    # Đường thẳng vuông góc có hệ số góc k' = -1 / k_ct = -d / (2a)
    k_perp = Fraction(-d_coef, 2 * a_coef)
    # d1: k_perp * x - y + const = 0 <=> x - (1/k_perp) y ...
    # Tạo d1 dạng Ax + By + C = 0 sao cho u_d1 . u_AB = 0 <=> 1 + k_ct * k_d1 = 0
    y_c_dung = choice([True, False])
    if y_c_dung:
        # Đường thẳng d1 có hệ số góc -1/k_ct
        opt_c_str = f"Đường thẳng đi qua hai điểm cực trị của $(C)$ có phương trình là $y = {fmt_p(k_ct)}x{fmt_signed(m_ct)}$."
        lg_c = f"Đường thẳng đi qua hai điểm cực trị của đồ thị hàm phân thức bậc hai trên bậc nhất có phương trình $y = \\dfrac{{({num_str})'}}{{({den_str})'}} = \\dfrac{{{2*a_coef}x{fmt_signed(b_coef)}}}{{{d_coef}}} = {fmt_p(k_ct)}x{fmt_signed(m_ct)}$. Mệnh đề này **ĐÚNG**."
    else:
        opt_c_str = f"Đường thẳng đi qua hai điểm cực trị của $(C)$ có phương trình là $y = {fmt_p(-k_ct)}x{fmt_signed(m_ct)}$."
        lg_c = f"Phương trình chính xác của đường thẳng đi qua hai điểm cực trị phải là $y = {fmt_p(k_ct)}x{fmt_signed(m_ct)}$. Mệnh đề này **SAI**."

    # Ý d: Đối xứng nhau qua đường thẳng Delta
    # Hai điểm cực trị đối xứng nhau qua trung trực của AB
    # Trung điểm I của AB: x_I = -B_der / (2 * A_der), y_I = k_ct * x_I + m_ct
    x_I = Fraction(-B_der, 2 * A_der)
    y_I = k_ct * x_I + m_ct
    # Đường trung trực vuông góc với AB và đi qua I:
    # y - y_I = k_perp * (x - x_I) <=> k_perp * x - y + (y_I - k_perp * x_I) = 0
    c_med = y_I - k_perp * x_I
    y_d_dung = choice([True, False])
    med_line_tex = f"y = {fmt_p(k_perp)}x{fmt_signed(c_med)}"
    if y_d_dung:
        opt_d_str = f"Hai điểm cực trị của đồ thị $(C)$ đối xứng nhau qua đường thẳng $\\Delta: {med_line_tex}$."
        lg_d = f"Đường thẳng qua 2 cực trị có hệ số góc $k_1 = {fmt_p(k_ct)}$. Trung trực của đoạn thẳng nối hai điểm cực trị vuông góc với $AB$ nên có hệ số góc $k_2 = -\\dfrac{{1}}{{k_1}} = {fmt_p(k_perp)}$ và đi qua trung điểm $I({fmt_p(x_I)}; {fmt_p(y_I)})$ của $AB$. Phương trình trung trực là ${med_line_tex}$. Mệnh đề này **ĐÚNG**."
    else:
        opt_d_str = f"Hai điểm cực trị của đồ thị $(C)$ đối xứng nhau qua trục tung $Oy$."
        lg_d = f"Trung điểm của đoạn nối hai cực trị có hoành độ $x_I = {fmt_p(x_I)} \\ne 0$ nên hai điểm cực trị không đối xứng qua trục tung. Mệnh đề này **SAI**."

    choice_a = f"{{\\True {opt_a_str}}}" if y_a_dung else f"{{{opt_a_str}}}"
    choice_b = f"{{\\True {opt_b_str}}}" if y_b_dung else f"{{{opt_b_str}}}"
    choice_c = f"{{\\True {opt_c_str}}}" if y_c_dung else f"{{{opt_c_str}}}"
    choice_d = f"{{\\True {opt_d_str}}}" if y_d_dung else f"{{{opt_d_str}}}"

    choices = [choice_a, choice_b, choice_c, choice_d]
    
    loigiai = f"""\\begin{{itemchoice}}
\\itemch {lg_a}
\\itemch {lg_b}
\\itemch {lg_c}
\\itemch {lg_d}
\\end{{itemchoice}}"""

    return caudan, choices, loigiai

# ==============================================================================
# DẠNG OT1: Hàm bậc 3 (Đa dạng hóa câu hỏi: giao điểm, giá trị, cực trị, khoảng đơn điệu, tâm đối xứng, tiếp tuyến, GTLN/GTNN)
# ==============================================================================
def sinh_cau_dung_sai_OT1_bac_ba():
    # Chọn dạng cực trị: có 2 cực trị nguyên đẹp hoặc không có cực trị (hoặc nghiệm đơn)
    has_extrema = choice([True, True, True, False])
    if has_extrema:
        x1 = randint(-3, 1)
        x2 = x1 + choice([1, 2, 3, 4])
        a_coef = choice([-2, -1, 1, 2])
        # y' = 3a(x - x1)(x - x2) = 3a x^2 - 3a(x1+x2)x + 3a x1 x2
        # Để b nguyên: -3*a*(x1+x2) phải chia hết cho 2 hoặc chọn a chẵn / x1+x2 chẵn
        if (x1 + x2) % 2 != 0 and abs(a_coef) % 2 != 0:
            a_coef *= 2  # đảm bảo b_val nguyên
        b_val = -3 * a_coef * (x1 + x2) // 2
        c_val = 3 * a_coef * x1 * x2
    else:
        # y' = 3a(x - x0)^2 + 3a*k^2 với k > 0 (vô nghiệm) hoặc k = 0 (nghiệm kép)
        x_root = randint(-2, 2)
        k_val = choice([1, 2])
        a_coef = choice([-1, 1])
        b_val = -3 * a_coef * x_root
        c_val = 3 * a_coef * (x_root**2 + k_val)
        x1, x2 = None, None

    d_val = randint(-6, 6)

    def f_val(xv):
        return a_coef * xv**3 + b_val * xv**2 + c_val * xv + d_val

    func_str = f"y = {fmt_first_term(a_coef, 'x^3')}{fmt_signed(b_val, 'x^2')}{fmt_signed(c_val, 'x')}{fmt_signed(d_val)}"
    caudan = f"Cho hàm số ${func_str}$ có đồ thị là $(C)$."

    # Xây dựng ngân hàng câu hỏi phong phú cho Dạng OT1
    pool = []

    # 1. Nhóm giá trị hàm số / giao điểm trục tung Oy
    y_giao_Oy = d_val
    dung_1 = choice([True, False])
    loai_1 = choice(["gia_tri", "giao_Oy"])
    if loai_1 == "giao_Oy":
        if dung_1:
            claim = f"Đồ thị $(C)$ cắt trục tung tại điểm $M(0; {y_giao_Oy})$."
            lg = f"Giao điểm của $(C)$ với trục tung có hoành độ $x = 0 \\Rightarrow y(0) = {y_giao_Oy}$, do đó tọa độ giao điểm là $M(0; {y_giao_Oy})$. Mệnh đề này **ĐÚNG**."
        else:
            fake_y = y_giao_Oy + choice([-2, -1, 1, 2])
            claim = f"Đồ thị $(C)$ cắt trục tung tại điểm $M(0; {fake_y})$."
            lg = f"Thay $x = 0$ ta được $y(0) = {y_giao_Oy} \\ne {fake_y}$. Mệnh đề này **SAI**."
    else:
        x_test = choice([-2, -1, 1, 2])
        y_test = f_val(x_test)
        if dung_1:
            claim = f"Giá trị của hàm số tại điểm $x = {x_test}$ bằng ${y_test}$."
            lg = f"Thay $x = {x_test}$ vào hàm số ta được $y({x_test}) = {y_test}$. Mệnh đề này **ĐÚNG**."
        else:
            fake_y = y_test + choice([-3, -1, 1, 3])
            claim = f"Giá trị của hàm số tại điểm $x = {x_test}$ bằng ${fake_y}$."
            lg = f"Thay $x = {x_test}$ vào hàm số ta được $y({x_test}) = {y_test} \\ne {fake_y}$. Mệnh đề này **SAI**."
    pool.append((claim, dung_1, lg))

    # 2. Nhóm đạo hàm: biểu thức đạo hàm hoặc số nghiệm của y' = 0
    der_str = f"y' = {fmt_first_term(3*a_coef, 'x^2')}{fmt_signed(2*b_val, 'x')}{fmt_signed(c_val)}"
    dung_2 = choice([True, False])
    loai_2 = choice(["bieu_thuc_y_prime", "nghiem_y_prime"])
    if loai_2 == "bieu_thuc_y_prime" or not has_extrema:
        if dung_2:
            claim = f"Đạo hàm của hàm số đã cho là ${der_str}$."
            lg = f"Ta có $({func_str})' \\Leftrightarrow {der_str}$. Mệnh đề này **ĐÚNG**."
        else:
            wrong_c = -c_val if c_val != 0 else 3
            der_wrong = f"y' = {fmt_first_term(3*a_coef, 'x^2')}{fmt_signed(2*b_val, 'x')}{fmt_signed(wrong_c)}"
            claim = f"Đạo hàm của hàm số đã cho là ${der_wrong}$."
            lg = f"Đạo hàm đúng phải là ${der_str}$. Mệnh đề này **SAI**."
    else:
        if dung_2:
            claim = f"Phương trình đạo hàm $y' = 0$ có hai nghiệm phân biệt là $x = {x1}$ và $x = {x2}$."
            lg = f"Ta có ${der_str} = 0 \\Leftrightarrow \\hoac{{&x = {x1} \\\\ &x = {x2}}}$. Mệnh đề này **ĐÚNG**."
        else:
            fake_x1, fake_x2 = -x1, -x2
            if fake_x1 == x1 and fake_x2 == x2:
                fake_x1, fake_x2 = x1 + 1, x2 + 1
            claim = f"Phương trình đạo hàm $y' = 0$ có hai nghiệm phân biệt là $x = {fake_x1}$ và $x = {fake_x2}$."
            lg = f"Nghiệm của $y' = 0$ là $x = {x1}$ và $x = {x2}$, không phải $x = {fake_x1}$ và $x = {fake_x2}$. Mệnh đề này **SAI**."
    pool.append((claim, dung_2, lg))

    # 3. Nhóm tính đơn điệu hoặc cực trị
    dung_3 = choice([True, False])
    if has_extrema:
        loai_3 = choice(["cuc_tri", "don_dieu", "gia_tri_cuc_tri"])
        if a_coef > 0:
            x_cd, x_ct = x1, x2
            y_cd, y_ct = f_val(x1), f_val(x2)
        else:
            x_cd, x_ct = x2, x1
            y_cd, y_ct = f_val(x2), f_val(x1)

        if loai_3 == "cuc_tri":
            if dung_3:
                claim = f"Hàm số đạt cực đại tại điểm $x = {x_cd}$ và đạt cực tiểu tại điểm $x = {x_ct}$."
                lg = f"Qua điểm $x = {x_cd}$ đạo hàm đổi dấu từ dương sang âm nên là điểm cực đại; qua $x = {x_ct}$ đạo hàm đổi dấu từ âm sang dương nên là điểm cực tiểu. Mệnh đề này **ĐÚNG**."
            else:
                claim = f"Hàm số đạt cực đại tại điểm $x = {x_ct}$ và đạt cực tiểu tại điểm $x = {x_cd}$."
                lg = f"Điểm cực đại là $x = {x_cd}$ và điểm cực tiểu là $x = {x_ct}$. Mệnh đề này **SAI**."
        elif loai_3 == "gia_tri_cuc_tri":
            hoi_cd = choice([True, False])
            if hoi_cd:
                if dung_3:
                    claim = f"Giá trị cực đại của hàm số bằng ${y_cd}$."
                    lg = f"Giá trị cực đại của hàm số là $y({x_cd}) = {y_cd}$. Mệnh đề này **ĐÚNG**."
                else:
                    fake_ycd = y_ct if y_ct != y_cd else y_cd + 2
                    claim = f"Giá trị cực đại của hàm số bằng ${fake_ycd}$."
                    lg = f"Giá trị cực đại của hàm số là $y({x_cd}) = {y_cd} \\ne {fake_ycd}$. Mệnh đề này **SAI**."
            else:
                if dung_3:
                    claim = f"Giá trị cực tiểu của hàm số bằng ${y_ct}$."
                    lg = f"Giá trị cực tiểu của hàm số là $y({x_ct}) = {y_ct}$. Mệnh đề này **ĐÚNG**."
                else:
                    fake_yct = y_cd if y_cd != y_ct else y_ct - 2
                    claim = f"Giá trị cực tiểu của hàm số bằng ${fake_yct}$."
                    lg = f"Giá trị cực tiểu của hàm số là $y({x_ct}) = {y_ct} \\ne {fake_yct}$. Mệnh đề này **SAI**."
        else:
            # loai_3 == "don_dieu"
            hoi_db = choice([True, False])
            if hoi_db:
                interval_db = f"({x1}; {x2})" if a_coef < 0 else f"({x2}; +\\infty)"
                if dung_3:
                    claim = f"Hàm số đồng biến trên khoảng ${interval_db}$."
                    lg = f"Trên khoảng ${interval_db}$, đạo hàm $y' > 0$ nên hàm số đồng biến. Mệnh đề này **ĐÚNG**."
                else:
                    wrong_interval = f"({x1}; {x2})" if a_coef > 0 else f"({x2}; +\\infty)"
                    claim = f"Hàm số đồng biến trên khoảng ${wrong_interval}$."
                    lg = f"Trên khoảng ${wrong_interval}$, $y' < 0$ nên hàm số nghịch biến. Mệnh đề này **SAI**."
            else:
                interval_nb = f"({x1}; {x2})" if a_coef > 0 else f"({x2}; +\\infty)"
                if dung_3:
                    claim = f"Hàm số nghịch biến trên khoảng ${interval_nb}$."
                    lg = f"Trên khoảng ${interval_nb}$, đạo hàm $y' < 0$ nên hàm số nghịch biến. Mệnh đề này **ĐÚNG**."
                else:
                    wrong_interval = f"({x1}; {x2})" if a_coef < 0 else f"({x2}; +\\infty)"
                    claim = f"Hàm số nghịch biến trên khoảng ${wrong_interval}$."
                    lg = f"Trên khoảng ${wrong_interval}$, $y' > 0$ nên hàm số đồng biến. Mệnh đề này **SAI**."
    else:
        # Không có cực trị
        if dung_3:
            s_tinh_chat = "đồng biến" if a_coef > 0 else "nghịch biến"
            claim = f"Hàm số đã cho {s_tinh_chat} trên $\\mathbb{{R}}$."
            lg = f"Đạo hàm ${der_str} {'>= 0' if a_coef > 0 else '<= 0'}, \\forall x \\in \\mathbb{{R}}$, do đó hàm số {s_tinh_chat} trên $\\mathbb{{R}}$. Mệnh đề này **ĐÚNG**."
        else:
            s_tinh_chat = "nghịch biến" if a_coef > 0 else "đồng biến"
            claim = f"Hàm số đã cho {s_tinh_chat} trên $\\mathbb{{R}}$."
            lg = f"Hệ số $a = {a_coef} {'> 0' if a_coef > 0 else '< 0'}$ nên hàm số không thể {s_tinh_chat} trên $\\mathbb{{R}}$. Mệnh đề này **SAI**."
    pool.append((claim, dung_3, lg))

    # 4. Nhóm tâm đối xứng / tiếp tuyến tại điểm uốn
    # Điểm uốn I: x_u = -b / (3a)
    x_u = Fraction(-b_val, 3 * a_coef)
    y_u = f_val(x_u)
    dung_4 = choice([True, False])
    loai_4 = choice(["tam_doi_xung", "khoang_loi_lom"])
    if loai_4 == "tam_doi_xung":
        pt_I = f"I({fmt_p(x_u)}; {fmt_p(y_u)})"
        if dung_4:
            claim = f"Đồ thị hàm số $(C)$ có tâm đối xứng là điểm ${pt_I}$."
            lg = f"Ta có $y'' = {6*a_coef}x{fmt_signed(2*b_val)}$. Cho $y'' = 0 \\Leftrightarrow x = {fmt_p(x_u)} \\Rightarrow y({fmt_p(x_u)}) = {fmt_p(y_u)}$. Vậy tâm đối xứng là ${pt_I}$. Mệnh đề này **ĐÚNG**."
        else:
            fake_yu = y_u + choice([1, -1, 2])
            pt_fake = f"I({fmt_p(x_u)}; {fmt_p(fake_yu)})"
            claim = f"Đồ thị hàm số $(C)$ có tâm đối xứng là điểm ${pt_fake}$."
            lg = f"Tâm đối xứng của đồ thị là điểm uốn ${pt_I} \\ne {pt_fake}$. Mệnh đề này **SAI**."
    else:
        # Nhóm tính lồi / lõm hoặc hệ số góc tiếp tuyến tại điểm uốn
        # y'(x_u)
        k_u = 3 * a_coef * (x_u**2) + 2 * b_val * x_u + c_val
        if dung_4:
            claim = f"Hệ số góc của tiếp tuyến của $(C)$ tại tâm đối xứng bằng ${fmt_p(k_u)}$."
            lg = f"Hoành độ tâm đối xứng là điểm uốn $x_0 = {fmt_p(x_u)}$. Hệ số góc tiếp tuyến là $k = y'({fmt_p(x_u)}) = {fmt_p(k_u)}$. Mệnh đề này **ĐÚNG**."
        else:
            fake_k = k_u + choice([2, -2, 3])
            claim = f"Hệ số góc của tiếp tuyến của $(C)$ tại tâm đối xứng bằng ${fmt_p(fake_k)}$."
            lg = f"Hệ số góc tiếp tuyến tại điểm uốn là $y'({fmt_p(x_u)}) = {fmt_p(k_u)} \\ne {fmt_p(fake_k)}$. Mệnh đề này **SAI**."
    pool.append((claim, dung_4, lg))

    # Chuẩn bị danh sách phương án, mỗi phương án nằm trên 1 dòng
    choices = []
    lg_items = []
    for claim, is_true, lg in pool:
        ch_str = f"{{\\True {claim}}}" if is_true else f"{{{claim}}}"
        choices.append(ch_str)
        lg_items.append(f"\\itemch {lg}")

    loigiai = "\\begin{itemchoice}\n" + "\n".join(lg_items) + "\n\\end{itemchoice}"
    return caudan, choices, loigiai

# ==============================================================================
# DẠNG OT2: Hàm nhất biến & Phân thức bậc 2 / bậc 1 (Đa dạng hóa câu hỏi)
# Hỗ trợ cả 2 họ hàm phổ biến:
# - Kiểu A: Phân thức bậc 2 trên bậc nhất y = (ax^2+bx+c)/(dx+e)
# - Kiểu B: Phân thức bậc nhất trên bậc nhất (hàm nhất biến chuẩn) y = (ax+b)/(cx+d)
# ==============================================================================
def sinh_cau_dung_sai_OT2_phan_thuc():
    kieu_ham = choice(["bac_2_tren_1", "bac_1_tren_1"])

    pool = []

    if kieu_ham == "bac_2_tren_1":
        x0 = choice([-3, -2, -1, 1, 2, 3])
        a_coef = choice([-1, 1, 2])
        k_val = choice([1, 2])
        B_coef = choice([-3, -2, -1, 0, 1, 2, 3])

        b_val = B_coef - a_coef * x0
        c_val = a_coef * (k_val**2) - B_coef * x0

        num_str = f"{fmt_first_term(a_coef, 'x^2')}{fmt_signed(b_val, 'x')}{fmt_signed(c_val)}"
        den_str = f"x{fmt_signed(-x0)}"
        func_tex = f"y = \\dfrac{{{num_str}}}{{{den_str}}}"
        caudan = f"Cho hàm số ${func_tex}$ có đồ thị là $(C)$."

        # Ý 1: Tập xác định hoặc giao điểm trục tung Oy
        dung_1 = choice([True, False])
        loai_1 = choice(["txd", "giao_Oy"])
        if loai_1 == "txd":
            if dung_1:
                claim = f"Tập xác định của hàm số là $D = \\mathbb{{R}} \\setminus \\{{{x0}\\}}$."
                lg = f"Điều kiện xác định: ${den_str} \\ne 0 \\Leftrightarrow x \\ne {x0}$. Do đó $D = \\mathbb{{R}} \\setminus \\{{{x0}\\}}$. Mệnh đề này **ĐÚNG**."
            else:
                claim = f"Tập xác định của hàm số là $D = \\mathbb{{R}} \\setminus \\{{{-x0}\\}}$."
                lg = f"Mẫu số triệt tiêu khi $x = {x0}$, vậy $D = \\mathbb{{R}} \\setminus \\{{{x0}\\}}$. Mệnh đề này **SAI**."
        else:
            y_giao_Oy = Fraction(c_val, -x0)
            if dung_1:
                claim = f"Đồ thị $(C)$ cắt trục tung tại điểm $M(0; {fmt_p(y_giao_Oy)})$."
                lg = f"Thay $x = 0$ ta được $y(0) = \\dfrac{{{c_val}}}{{{-x0}}} = {fmt_p(y_giao_Oy)}$. Mệnh đề này **ĐÚNG**."
            else:
                fake_y = y_giao_Oy + 1
                claim = f"Đồ thị $(C)$ cắt trục tung tại điểm $M(0; {fmt_p(fake_y)})$."
                lg = f"Tọa độ giao điểm với trục tung là $(0; {fmt_p(y_giao_Oy)}) \\ne (0; {fmt_p(fake_y)})$. Mệnh đề này **SAI**."
        pool.append((claim, dung_1, lg))

        # Ý 2: Đạo hàm y' hoặc số nghiệm của y' = 0
        A_der = a_coef
        B_der = -2 * a_coef * x0
        C_der = a_coef * (x0**2 - k_val**2)
        der_num_true = f"{fmt_first_term(A_der, 'x^2')}{fmt_signed(B_der, 'x')}{fmt_signed(C_der)}"
        der_true_tex = f"y' = \\dfrac{{{der_num_true}}}{{({den_str})^2}}"

        dung_2 = choice([True, False])
        loai_2 = choice(["dao_ham", "so_nghiem"])
        if loai_2 == "dao_ham":
            if dung_2:
                claim = f"Đạo hàm của hàm số đã cho là ${der_true_tex}$."
                lg = f"Áp dụng quy tắc đạo hàm thương ta có ${der_true_tex}$. Mệnh đề này **ĐÚNG**."
            else:
                der_num_wrong = f"{fmt_first_term(A_der, 'x^2')}{fmt_signed(B_der, 'x')}{fmt_signed(-C_der)}"
                claim = f"Đạo hàm của hàm số đã cho là $y' = \\dfrac{{{der_num_wrong}}}{{({den_str})^2}}$."
                lg = f"Đạo hàm chính xác là ${der_true_tex}$. Mệnh đề này **SAI**."
        else:
            # Hai nghiệm của đạo hàm: x = x0 - k_val hoặc x0 + k_val
            x_c1 = x0 - k_val
            x_c2 = x0 + k_val
            if dung_2:
                claim = f"Phương trình $y' = 0$ có hai nghiệm phân biệt là $x = {x_c1}$ và $x = {x_c2}$."
                lg = f"Giải phương trình tử số $y' = 0$ ta được hai nghiệm phân biệt $x = {x_c1}$ và $x = {x_c2}$. Mệnh đề này **ĐÚNG**."
            else:
                claim = f"Phương trình $y' = 0$ vô nghiệm trên tập xác định."
                lg = f"Tử số của $y'$ có hai nghiệm phân biệt $x = {x_c1}$ và $x = {x_c2}$ khác $x0$. Mệnh đề này **SAI**."
        pool.append((claim, dung_2, lg))

        # Ý 3: Tiệm cận đứng hoặc Tiệm cận xiên
        dung_3 = choice([True, False])
        loai_3 = choice(["tcd", "tcx"])
        if loai_3 == "tcd":
            if dung_3:
                claim = f"Đồ thị hàm số $(C)$ có đường tiệm cận đứng là $x = {x0}$."
                lg = f"Ta có $\\lim\\limits_{{x \\to {x0}}} y = \\infty$ nên đường thẳng $x = {x0}$ là tiệm cận đứng. Mệnh đề này **ĐÚNG**."
            else:
                claim = f"Đồ thị hàm số $(C)$ có đường tiệm cận đứng là $x = {-x0}$."
                lg = f"Nghiệm của mẫu số là $x = {x0}$, do đó tiệm cận đứng là $x = {x0}$. Mệnh đề này **SAI**."
        else:
            # Tiệm cận xiên: y = ax + B_coef
            tcx_eq = f"y = {fmt_first_term(a_coef, 'x')}{fmt_signed(B_coef)}"
            if dung_3:
                claim = f"Đồ thị hàm số $(C)$ có đường tiệm cận xiên là ${tcx_eq}$."
                lg = f"Thực hiện phép chia đa thức tử cho mẫu: $y = {fmt_first_term(a_coef, 'x')}{fmt_signed(B_coef)} + \\dfrac{{{a_coef * (k_val**2)}}}{{{den_str}}}$. Vậy tiệm cận xiên là ${tcx_eq}$. Mệnh đề này **ĐÚNG**."
            else:
                fake_tcx = f"y = {fmt_first_term(-a_coef, 'x')}{fmt_signed(B_coef)}"
                claim = f"Đồ thị hàm số $(C)$ có đường tiệm cận xiên là ${fake_tcx}$."
                lg = f"Phương trình tiệm cận xiên của $(C)$ là ${tcx_eq} \\ne {fake_tcx}$. Mệnh đề này **SAI**."
        pool.append((claim, dung_3, lg))

        # Ý 4: Đường thẳng qua 2 cực trị hoặc Tâm đối xứng (giao 2 tiệm cận)
        dung_4 = choice([True, False])
        loai_4 = choice(["duong_qua_cuc_tri", "giao_diem_tiem_can"])
        if loai_4 == "duong_qua_cuc_tri":
            k_line = a_coef
            m_line = B_coef
            line_true = f"y = {fmt_first_term(k_line, 'x')}{fmt_signed(m_line)}"
            if dung_4:
                claim = f"Đường thẳng đi qua hai điểm cực trị của đồ thị hàm số có phương trình là ${line_true}$."
                lg = f"Đường thẳng qua hai điểm cực trị là $y = \\dfrac{{({num_str})'}}{{({den_str})'}} = \\dfrac{{{2*a_coef}x{fmt_signed(b_val)}}}{{1}} \\Leftrightarrow {line_true}$. Mệnh đề này **ĐÚNG**."
            else:
                line_fake = f"y = {fmt_first_term(-k_line, 'x')}{fmt_signed(m_line)}"
                claim = f"Đường thẳng đi qua hai điểm cực trị của đồ thị hàm số có phương trình là ${line_fake}$."
                lg = f"Phương trình đường thẳng qua hai điểm cực trị là ${line_true}$. Mệnh đề này **SAI**."
        else:
            # Giao điểm 2 tiệm cận: I(x0; y_tcx(x0)) với y_tcx = a*x0 + B_coef
            y_I = a_coef * x0 + B_coef
            pt_I = f"I({x0}; {y_I})"
            if dung_4:
                claim = f"Giao điểm của hai đường tiệm cận của $(C)$ là điểm ${pt_I}$."
                lg = f"Tiệm cận đứng là $x = {x0}$, thay vào tiệm cận xiên $y = {fmt_first_term(a_coef, 'x')}{fmt_signed(B_coef)}$ ta được $y = {y_I}$. Vậy giao điểm là ${pt_I}$. Mệnh đề này **ĐÚNG**."
            else:
                pt_fake = f"I({x0}; {y_I + 2})"
                claim = f"Giao điểm của hai đường tiệm cận của $(C)$ là điểm ${pt_fake}$."
                lg = f"Tọa độ giao điểm của hai tiệm cận là ${pt_I} \\ne {pt_fake}$. Mệnh đề này **SAI**."
        pool.append((claim, dung_4, lg))

    else:
        # Kiểu B: Hàm phân thức bậc nhất / bậc nhất y = (ax + b) / (cx + d)
        c_denom = choice([1, 2])
        d_denom = choice([-3, -2, -1, 1, 2, 3])
        # c*x + d = 0 => x = -d/c
        x_pole = Fraction(-d_denom, c_denom)

        a_num = choice([-3, -2, -1, 1, 2, 3])
        # Delta = ad - bc != 0
        ad_val = a_num * d_denom
        b_num = choice([-5, -4, -3, -2, -1, 1, 2, 3, 4, 5])
        while a_num * d_denom - b_num * c_denom == 0:
            b_num = choice([-5, -4, -3, -2, -1, 1, 2, 3, 4, 5])

        det = a_num * d_denom - b_num * c_denom
        num_str = f"{fmt_first_term(a_num, 'x')}{fmt_signed(b_num)}"
        den_str = f"{fmt_first_term(c_denom, 'x')}{fmt_signed(d_denom)}"
        func_tex = f"y = \\dfrac{{{num_str}}}{{{den_str}}}"
        caudan = f"Cho hàm số ${func_tex}$ có đồ thị là $(C)$."

        # 1. Tập xác định
        dung_1 = choice([True, False])
        if dung_1:
            claim = f"Tập xác định của hàm số là $D = \\mathbb{{R}} \\setminus \\{{{fmt_p(x_pole)}\\}}$."
            lg = f"Điều kiện: ${den_str} \\ne 0 \\Leftrightarrow x \\ne {fmt_p(x_pole)}$. Vậy $D = \\mathbb{{R}} \\setminus \\{{{fmt_p(x_pole)}\\}}$. Mệnh đề này **ĐÚNG**."
        else:
            claim = f"Tập xác định của hàm số là $D = \\mathbb{{R}} \\setminus \\{{{fmt_p(-x_pole)}\\}}$."
            lg = f"Mẫu số bằng $0$ khi $x = {fmt_p(x_pole)}$. Mệnh đề này **SAI**."
        pool.append((claim, dung_1, lg))

        # 2. Đạo hàm
        dung_2 = choice([True, False])
        der_true_tex = f"y' = \\dfrac{{{det}}}{{({den_str})^2}}"
        if dung_2:
            claim = f"Đạo hàm của hàm số đã cho là ${der_true_tex}$."
            lg = f"Ta có $y' = \\dfrac{{ad - bc}}{{({den_str})^2}} = \\dfrac{{{a_num}\\cdot({d_denom}) - ({b_num})\\cdot({c_denom})}}{{({den_str})^2}} = {der_true_tex}$. Mệnh đề này **ĐÚNG**."
        else:
            claim = f"Đạo hàm của hàm số đã cho là $y' = \\dfrac{{{-det}}}{{({den_str})^2}}$."
            lg = f"Công thức tính đúng cho kết quả ${der_true_tex}$. Mệnh đề này **SAI**."
        pool.append((claim, dung_2, lg))

        # 3. Tiệm cận ngang & đứng
        dung_3 = choice([True, False])
        y_horiz = Fraction(a_num, c_denom)
        loai_3 = choice(["tcn", "tcd"])
        if loai_3 == "tcn":
            if dung_3:
                claim = f"Đồ thị hàm số $(C)$ có đường tiệm cận ngang là $y = {fmt_p(y_horiz)}$."
                lg = f"Ta có $\\lim\\limits_{{x \\to \\pm\\infty}} y = \\dfrac{{{a_num}}}{{{c_denom}}} = {fmt_p(y_horiz)}$, do đó tiệm cận ngang là $y = {fmt_p(y_horiz)}$. Mệnh đề này **ĐÚNG**."
            else:
                fake_y = fmt_p(y_horiz + 1)
                claim = f"Đồ thị hàm số $(C)$ có đường tiệm cận ngang là $y = {fake_y}$."
                lg = f"Tiệm cận ngang là $y = {fmt_p(y_horiz)} \\ne {fake_y}$. Mệnh đề này **SAI**."
        else:
            if dung_3:
                claim = f"Đồ thị hàm số $(C)$ có đường tiệm cận đứng là $x = {fmt_p(x_pole)}$."
                lg = f"Nghiệm của mẫu số là $x = {fmt_p(x_pole)}$, vậy tiệm cận đứng là $x = {fmt_p(x_pole)}$. Mệnh đề này **ĐÚNG**."
            else:
                claim = f"Đồ thị hàm số $(C)$ có đường tiệm cận đứng là $x = {fmt_p(-x_pole)}$."
                lg = f"Tiệm cận đứng của đồ thị hàm số là $x = {fmt_p(x_pole)}$. Mệnh đề này **SAI**."
        pool.append((claim, dung_3, lg))

        # 4. Đơn điệu / Cực trị (Hàm bậc 1/1 không có cực trị)
        dung_4 = choice([True, False])
        loai_4 = choice(["cuc_tri", "don_dieu"])
        if loai_4 == "cuc_tri":
            if dung_4:
                claim = f"Hàm số đã cho không có cực trị."
                lg = f"Vì $y' = \\dfrac{{{det}}}{{({den_str})^2}} \\ne 0, \\forall x \\ne {fmt_p(x_pole)}$ nên hàm số không có cực trị. Mệnh đề này **ĐÚNG**."
            else:
                claim = f"Hàm số đã cho có một điểm cực trị."
                lg = f"Hàm phân thức bậc nhất trên bậc nhất không có cực trị. Mệnh đề này **SAI**."
        else:
            s_td = "đồng biến" if det > 0 else "nghịch biến"
            if dung_4:
                claim = f"Hàm số đã cho {s_td} trên từng khoảng xác định."
                lg = f"Do $y' {' > 0' if det > 0 else ' < 0'}, \\forall x \\ne {fmt_p(x_pole)}$ nên hàm số {s_td} trên từng khoảng xác định. Mệnh đề này **ĐÚNG**."
            else:
                s_nguoc = "nghịch biến" if det > 0 else "đồng biến"
                claim = f"Hàm số đã cho {s_nguoc} trên từng khoảng xác định."
                lg = f"Đạo hàm mang dấu ${'+' if det > 0 else '-'}$ nên hàm số phải {s_td}. Mệnh đề này **SAI**."
        pool.append((claim, dung_4, lg))

    choices = []
    lg_items = []
    for claim, is_true, lg in pool:
        ch_str = f"{{\\True {claim}}}" if is_true else f"{{{claim}}}"
        choices.append(ch_str)
        lg_items.append(f"\\itemch {lg}")

    loigiai = "\\begin{itemchoice}\n" + "\n".join(lg_items) + "\n\\end{itemchoice}"
    return caudan, choices, loigiai

# ==============================================================================
# DẠNG OT3: Bài toán chuyển động (Đa dạng hóa mô hình và loại câu hỏi)
# Hỗ trợ 2 mô hình chuyển động thực tế:
# - Mô hình A: Chuyển động ném lên / chuyển động biến đổi bậc 3: s(t) = -a t^3 + b t^2 + c t
# - Mô hình B: Chuyển động hãm phanh / ném đứng bậc 2: s(t) = v0 t - 1/2 g t^2
# ==============================================================================
def sinh_cau_dung_sai_OT3_chuyen_dong():
    mo_hinh = choice(["bac_3", "bac_2_ham_phanh"])
    pool = []

    if mo_hinh == "bac_3":
        # s(t) = -t^3 + 3b t^2 + c t hoặc -2t^3 + 3b t^2 + ct
        a_lead = choice([1, 2])
        b_val = randint(2, 6)
        c_val = choice([0, 5, 10, 15, 20])
        t_max_v = Fraction(b_val, a_lead) if a_lead != 1 else b_val

        # s(t) = -a_lead t^3 + 3*b_val*t^2 + c_val*t
        def s_func(tv):
            return -a_lead * (tv**3) + 3 * b_val * (tv**2) + c_val * tv

        def v_func(tv):
            return -3 * a_lead * (tv**2) + 6 * b_val * tv + c_val

        def a_func(tv):
            return -6 * a_lead * tv + 6 * b_val

        s_expr = f"s(t) = {fmt_first_term(-a_lead, 't^3')}{fmt_signed(3*b_val, 't^2')}{fmt_signed(c_val, 't')}"
        caudan = f"Một vật chuyển động thẳng có phương trình quãng đường cho bởi ${s_expr}$, trong đó thời gian $t$ tính bằng giây ($t \\ge 0$) và quãng đường $s$ tính bằng mét."

        # 1. Quãng đường sau thời gian t0
        t0 = choice([1, 2, 3])
        s_t0 = s_func(t0)
        dung_1 = choice([True, False])
        if dung_1:
            claim = f"Quãng đường vật đi được sau ${t0}\\text{{ s}}$ kể từ lúc bắt đầu chuyển động bằng ${s_t0}\\text{{ m}}$."
            lg = f"Thay $t = {t0}$ vào phương trình quãng đường ta có $s({t0}) = {s_t0}\\text{{ m}}$. Mệnh đề này **ĐÚNG**."
        else:
            fake_s = s_t0 + choice([-4, -2, 2, 4])
            claim = f"Quãng đường vật đi được sau ${t0}\\text{{ s}}$ kể từ lúc bắt đầu chuyển động bằng ${fake_s}\\text{{ m}}$."
            lg = f"Quãng đường thực tế sau ${t0}\\text{{ s}}$ là $s({t0}) = {s_t0}\\text{{ m}} \\ne {fake_s}\\text{{ m}}$. Mệnh đề này **SAI**."
        pool.append((claim, dung_1, lg))

        # 2. Vận tốc tại thời điểm t1
        t1 = choice([1, 2])
        v_t1 = v_func(t1)
        dung_2 = choice([True, False])
        if dung_2:
            claim = f"Vận tốc tức thời của vật tại thời điểm $t = {t1}\\text{{ s}}$ bằng ${v_t1}\\text{{ m/s}}$."
            lg = f"Vận tốc tức thời là $v(t) = s'(t) = {-3*a_lead}t^2 + {6*b_val}t{fmt_signed(c_val)}$. Tại $t = {t1}\\text{{ s}}$, $v({t1}) = {v_t1}\\text{{ m/s}}$. Mệnh đề này **ĐÚNG**."
        else:
            fake_v = v_t1 + choice([-5, -3, 3, 5])
            claim = f"Vận tốc tức thời của vật tại thời điểm $t = {t1}\\text{{ s}}$ bằng ${fake_v}\\text{{ m/s}}$."
            lg = f"Vận tốc tức thời tại $t = {t1}\\text{{ s}}$ là $v({t1}) = {v_t1}\\text{{ m/s}} \\ne {fake_v}\\text{{ m/s}}$. Mệnh đề này **SAI**."
        pool.append((claim, dung_2, lg))

        # 3. Gia tốc tại thời điểm hoặc khoảng tăng tốc / giảm tốc
        dung_3 = choice([True, False])
        loai_3 = choice(["khoang_tang_toc", "gia_toc_tai_t"])
        if loai_3 == "khoang_tang_toc":
            say_khoang = f"(0; {b_val})" if a_lead == 1 else f"(0; {fmt_p(t_max_v)})"
            hoi_tang = choice([True, False])
            if hoi_tang:
                if dung_3:
                    claim = f"Trong khoảng thời gian ${say_khoang}\\text{{ s}}$, vật chuyển động tăng tốc (vận tốc tăng dần)."
                    lg = f"Gia tốc $a(t) = v'(t) = {-6*a_lead}t + {6*b_val}$. Vật tăng tốc khi $a(t) > 0 \\Leftrightarrow t < {fmt_p(t_max_v)}$. Do $t \\ge 0$ nên vật tăng tốc trên khoảng ${say_khoang}\\text{{ s}}$. Mệnh đề này **ĐÚNG**."
                else:
                    claim = f"Trong khoảng thời gian $({fmt_p(t_max_v)}; +\\infty)\\text{{ s}}$, vật chuyển động tăng tốc."
                    lg = f"Trên khoảng $({fmt_p(t_max_v)}; +\\infty)\\text{{ s}}$, gia tốc $a(t) < 0$ nên vật chuyển động giảm tốc. Mệnh đề này **SAI**."
            else:
                khoang_giam = f"({fmt_p(t_max_v)}; +\\infty)"
                if dung_3:
                    claim = f"Trong khoảng thời gian ${khoang_giam}\\text{{ s}}$, vật chuyển động giảm tốc (vận tốc giảm dần)."
                    lg = f"Gia tốc $a(t) = v'(t) = {-6*a_lead}t + {6*b_val} < 0 \\Leftrightarrow t > {fmt_p(t_max_v)}$. Vậy vật giảm tốc trên khoảng ${khoang_giam}\\text{{ s}}$. Mệnh đề này **ĐÚNG**."
                else:
                    claim = f"Trong khoảng thời gian ${say_khoang}\\text{{ s}}$, vật chuyển động giảm tốc."
                    lg = f"Trên khoảng ${say_khoang}\\text{{ s}}$, gia tốc dương nên vật tăng tốc. Mệnh đề này **SAI**."
        else:
            t_acc = choice([1, 2])
            val_acc = a_func(t_acc)
            if dung_3:
                claim = f"Gia tốc của vật tại thời điểm $t = {t_acc}\\text{{ s}}$ bằng ${val_acc}\\text{{ m/s}}^2$."
                lg = f"Ta có $a(t) = s''(t) = {-6*a_lead}t + {6*b_val}$. Tại $t = {t_acc}\\text{{ s}}$, $a({t_acc}) = {val_acc}\\text{{ m/s}}^2$. Mệnh đề này **ĐÚNG**."
            else:
                fake_acc = val_acc + choice([-6, 6])
                claim = f"Gia tốc của vật tại thời điểm $t = {t_acc}\\text{{ s}}$ bằng ${fake_acc}\\text{{ m/s}}^2$."
                lg = f"Gia tốc tại $t = {t_acc}\\text{{ s}}$ là $a({t_acc}) = {val_acc}\\text{{ m/s}}^2 \\ne {fake_acc}\\text{{ m/s}}^2$. Mệnh đề này **SAI**."
        pool.append((claim, dung_3, lg))

        # 4. Vận tốc cực đại
        v_max = v_func(t_max_v)
        dung_4 = choice([True, False])
        if dung_4:
            claim = f"Vận tốc lớn nhất của vật đạt được là ${fmt_p(v_max)}\\text{{ m/s}}$ tại thời điểm $t = {fmt_p(t_max_v)}\\text{{ s}}$."
            lg = f"Hàm vận tốc $v(t) = {-3*a_lead}t^2 + {6*b_val}t{fmt_signed(c_val)}$ đạt giá trị lớn nhất tại đỉnh parabol $t = {fmt_p(t_max_v)}\\text{{ s}}$, với $v_{{\\max}} = {fmt_p(v_max)}\\text{{ m/s}}$. Mệnh đề này **ĐÚNG**."
        else:
            fake_vmax = v_max + choice([-10, 10, 5])
            claim = f"Vận tốc lớn nhất của vật đạt được là ${fmt_p(fake_vmax)}\\text{{ m/s}}$."
            lg = f"Vận tốc lớn nhất đạt được là $v({fmt_p(t_max_v)}) = {fmt_p(v_max)}\\text{{ m/s}} \\ne {fmt_p(fake_vmax)}\\text{{ m/s}}$. Mệnh đề này **SAI**."
        pool.append((claim, dung_4, lg))

    else:
        # Mô hình B: Chuyển động hãm phanh (bậc 2): s(t) = -k t^2 + v0 t
        # v(t) = -2k t + v0, dừng hẳn khi v(t) = 0 => t_dung = v0 / (2k)
        k_coef = choice([1, 2, 3])
        t_stop = choice([4, 5, 6, 8, 10])
        v0 = 2 * k_coef * t_stop
        s_expr = f"s(t) = -{k_coef}t^2 + {v0}t"
        caudan = f"Một đoàn tàu đang chạy với tốc độ cao thì người lái tàu hãm phanh. Quãng đường đoàn tàu đi được kể từ thời điểm hãm phanh được cho bởi phương trình ${s_expr}$, trong đó $t$ là thời gian tính bằng giây và $s$ tính bằng mét."

        # 1. Vận tốc ban đầu
        dung_1 = choice([True, False])
        if dung_1:
            claim = f"Vận tốc của đoàn tàu ngay tại thời điểm bắt đầu hãm phanh là ${v0}\\text{{ m/s}}$."
            lg = f"Vận tốc tức thời là $v(t) = s'(t) = -{2*k_coef}t + {v0}$. Tại $t = 0$, $v(0) = {v0}\\text{{ m/s}}$. Mệnh đề này **ĐÚNG**."
        else:
            fake_v0 = v0 - 5
            claim = f"Vận tốc của đoàn tàu ngay tại thời điểm bắt đầu hãm phanh là ${fake_v0}\\text{{ m/s}}$."
            lg = f"Vận tốc ban đầu của tàu là $v(0) = {v0}\\text{{ m/s}} \\ne {fake_v0}\\text{{ m/s}}$. Mệnh đề này **SAI**."
        pool.append((claim, dung_1, lg))

        # 2. Thời điểm đoàn tàu dừng hẳn
        dung_2 = choice([True, False])
        if dung_2:
            claim = f"Kể từ lúc hãm phanh, đoàn tàu dừng hẳn sau thời gian ${t_stop}\\text{{ s}}$."
            lg = f"Tàu dừng hẳn khi vận tốc $v(t) = 0 \\Leftrightarrow -{2*k_coef}t + {v0} = 0 \\Leftrightarrow t = {t_stop}\\text{{ s}}$. Mệnh đề này **ĐÚNG**."
        else:
            fake_t = t_stop + choice([-2, 2])
            claim = f"Kể từ lúc hãm phanh, đoàn tàu dừng hẳn sau thời gian ${fake_t}\\text{{ s}}$."
            lg = f"Thời gian để tàu dừng hẳn là $t = {t_stop}\\text{{ s}} \\ne {fake_t}\\text{{ s}}$. Mệnh đề này **SAI**."
        pool.append((claim, dung_2, lg))

        # 3. Gia tốc của chuyển động
        dung_3 = choice([True, False])
        acc_val = -2 * k_coef
        if dung_3:
            claim = f"Gia tốc của đoàn tàu trong suốt quá trình hãm phanh không đổi và bằng ${acc_val}\\text{{ m/s}}^2$."
            lg = f"Gia tốc $a(t) = v'(t) = -{2*k_coef}\\text{{ m/s}}^2$ (hằng số âm thể hiện chuyển động chậm dần đều). Mệnh đề này **ĐÚNG**."
        else:
            claim = f"Gia tốc của đoàn tàu trong suốt quá trình hãm phanh bằng ${2*k_coef}\\text{{ m/s}}^2$."
            lg = f"Vì tàu chuyển động chậm dần nên gia tốc phải mang dấu âm $a = {acc_val}\\text{{ m/s}}^2$. Mệnh đề này **SAI**."
        pool.append((claim, dung_3, lg))

        # 4. Quãng đường tàu đi được từ khi hãm phanh đến khi dừng hẳn
        s_stop = -k_coef * (t_stop**2) + v0 * t_stop
        dung_4 = choice([True, False])
        if dung_4:
            claim = f"Quãng đường đoàn tàu đi được từ khi hãm phanh đến khi dừng hẳn bằng ${s_stop}\\text{{ m}}$."
            lg = f"Thay $t = {t_stop}\\text{{ s}}$ vào phương trình quãng đường ta được $s({t_stop}) = -{k_coef}\\cdot ({t_stop})^2 + {v0}\\cdot ({t_stop}) = {s_stop}\\text{{ m}}$. Mệnh đề này **ĐÚNG**."
        else:
            fake_s = s_stop + choice([-20, 20])
            claim = f"Quãng đường đoàn tàu đi được từ khi hãm phanh đến khi dừng hẳn bằng ${fake_s}\\text{{ m}}$."
            lg = f"Quãng đường đi được đến khi dừng hẳn là $s({t_stop}) = {s_stop}\\text{{ m}} \\ne {fake_s}\\text{{ m}}$. Mệnh đề này **SAI**."
        pool.append((claim, dung_4, lg))

    choices = []
    lg_items = []
    for claim, is_true, lg in pool:
        ch_str = f"{{\\True {claim}}}" if is_true else f"{{{claim}}}"
        choices.append(ch_str)
        lg_items.append(f"\\itemch {lg}")

    loigiai = "\\begin{itemchoice}\n" + "\n".join(lg_items) + "\n\\end{itemchoice}"
    return caudan, choices, loigiai

# ==============================================================================
# DẠNG OT4: Hàm phân thức bậc 2 trên bậc nhất y = (ax^2+bx+c)/(x - x0)
# (Tập xác định, đạo hàm y', đường tiệm cận, đường thẳng qua 2 điểm cực trị)
# ==============================================================================
def sinh_cau_dung_sai_OT4_bac_2_tren_1():
    # Chọn x0, a, b sao cho hàm số có 2 điểm cực trị
    x0 = choice([-3, -2, -1, 1, 2, 3])
    a_coef = choice([1, 1, -1])  # Thường a = 1, đôi khi a = -1
    b_val = choice([-3, -2, -1, 0, 1, 2, 3])
    
    # Để y' = 0 có hai nghiệm phân biệt nguyên đẹp, ta chọn k_root in {1, 2}
    k_root = choice([1, 2])
    r_val = a_coef * (k_root**2)
    c_val = r_val - a_coef * (x0**2) - b_val * x0
    
    num_str = f"{fmt_first_term(a_coef, 'x^2')}{fmt_signed(b_val, 'x')}{fmt_signed(c_val)}".strip()
    den_str = f"x{fmt_signed(-x0)}".strip()
    func_tex = f"y = \\dfrac{{{num_str}}}{{{den_str}}}"
    caudan = f"Cho hàm số ${func_tex}$ có đồ thị là $(C)$. Các mệnh đề sau đúng hay sai?"

    pool = []

    # -------------------------------------------------------------
    # Mệnh đề a: Tập xác định của hàm số
    # -------------------------------------------------------------
    dung_a = choice([True, False])
    if dung_a:
        claim_a = f"Tập xác định của hàm số là $D = \\mathbb{{R}} \\setminus \\{{{x0}\\}}$."
        lg_a = f"Điều kiện xác định: ${den_str} \\ne 0 \\Leftrightarrow x \\ne {x0}$. Do đó tập xác định của hàm số là $D = \\mathbb{{R}} \\setminus \\{{{x0}\\}}$. Mệnh đề này **ĐÚNG**."
    else:
        fake_x0 = -x0 if x0 != 0 else 1
        claim_a = f"Tập xác định của hàm số là $D = \\mathbb{{R}} \\setminus \\{{{fake_x0}\\}}$."
        lg_a = f"Mẫu thức ${den_str} = 0 \\Leftrightarrow x = {x0}$, do đó tập xác định phải là $D = \\mathbb{{R}} \\setminus \\{{{x0}\\}}$. Mệnh đề này **SAI**."
    pool.append((claim_a, dung_a, lg_a))

    # -------------------------------------------------------------
    # Mệnh đề b: Đạo hàm y'
    # -------------------------------------------------------------
    A_der = a_coef
    B_der = -2 * a_coef * x0
    C_der = a_coef * (x0**2) - r_val
    der_num_true = f"{fmt_first_term(A_der, 'x^2')}{fmt_signed(B_der, 'x')}{fmt_signed(C_der)}".strip()
    der_true_tex = f"y' = \\dfrac{{{der_num_true}}}{{({den_str})^2}}"
    
    dung_b = choice([True, False])
    if dung_b:
        claim_b = f"${der_true_tex}$"
        lg_b = f"Ta có: $y' = \\dfrac{{({num_str})'({den_str}) - ({num_str})({den_str})'}}{{({den_str})^2}} = \\dfrac{{({fmt_first_term(2*a_coef, 'x')}{fmt_signed(b_val)})({den_str}) - ({num_str})}}{{({den_str})^2}} = \\dfrac{{{der_num_true}}}{{({den_str})^2}}$. Mệnh đề này **ĐÚNG**."
    else:
        # Làm sai bằng cách đổi dấu C_der hoặc sai B_der
        fake_C_der = -C_der if C_der != 0 else 2
        der_num_wrong = f"{fmt_first_term(A_der, 'x^2')}{fmt_signed(B_der, 'x')}{fmt_signed(fake_C_der)}".strip()
        der_wrong_tex = f"y' = \\dfrac{{{der_num_wrong}}}{{({den_str})^2}}"
        claim_b = f"${der_wrong_tex}$"
        lg_b = f"Thực hiện đạo hàm thương đúng quy tắc: ${der_true_tex} \\ne {der_wrong_tex}$. Mệnh đề này **SAI**."
    pool.append((claim_b, dung_b, lg_b))

    # -------------------------------------------------------------
    # Mệnh đề c: Đường tiệm cận đứng, tiệm cận xiên hoặc đường thẳng qua cực trị
    # -------------------------------------------------------------
    dung_c = choice([True, False])
    hoi_c = choice(["tcd", "tcx", "line_cuc_tri"])
    line_true = f"y = {fmt_first_term(2 * a_coef, 'x')}{fmt_signed(b_val)}".strip()
    if hoi_c == "tcd":
        if dung_c:
            claim_c = f"Đường thẳng $x = {x0}$ là tiệm cận đứng của đồ thị hàm số $(C)$."
            lg_c = f"Vì $\\lim\\limits_{{x \\to {x0}^+}} y = \\infty$ và $\\lim\\limits_{{x \\to {x0}^-}} y = -\\infty$ (hoặc ngược lại) nên đường thẳng $x = {x0}$ là tiệm cận đứng của đồ thị hàm số $(C)$. Mệnh đề này **ĐÚNG**."
        else:
            fake_tc = -x0 if x0 != 0 else 2
            claim_c = f"Đường thẳng $x = {fake_tc}$ là tiệm cận đứng của đồ thị hàm số $(C)$."
            lg_c = f"Nghiệm của mẫu thức là $x = {x0}$, do đó đường tiệm cận đứng của đồ thị là $x = {x0} \\ne {fake_tc}$. Mệnh đề này **SAI**."
    elif hoi_c == "tcx":
        tcx_b = b_val + a_coef * x0
        tcx_str = f"y = {fmt_first_term(a_coef, 'x')}{fmt_signed(tcx_b)}".strip()
        if dung_c:
            claim_c = f"Đường thẳng ${tcx_str}$ là tiệm cận xiên của đồ thị hàm số $(C)$."
            lg_c = f"Thực hiện phép chia đa thức tử cho mẫu ta có: $y = {fmt_first_term(a_coef, 'x')}{fmt_signed(tcx_b)} + \\dfrac{{{r_val}}}{{{den_str}}}$. Do $\\lim\\limits_{{x \\to \\pm\\infty}} \\dfrac{{{r_val}}}{{{den_str}}} = 0$ nên ${tcx_str}$ là tiệm cận xiên của đồ thị hàm số $(C)$. Mệnh đề này **ĐÚNG**."
        else:
            fake_tcx_b = tcx_b + choice([-1, 1, 2])
            fake_tcx = f"y = {fmt_first_term(a_coef, 'x')}{fmt_signed(fake_tcx_b)}".strip()
            claim_c = f"Đường thẳng ${fake_tcx}$ là tiệm cận xiên của đồ thị hàm số $(C)$."
            lg_c = f"Phương trình đường tiệm cận xiên đúng của $(C)$ là ${tcx_str} \\ne {fake_tcx}$. Mệnh đề này **SAI**."
    else:  # line_cuc_tri
        if dung_c:
            claim_c = f"Đường thẳng đi qua hai điểm cực trị của đồ thị hàm số $(C)$ có phương trình ${line_true}$."
            lg_c = f"Ta biết rằng với hàm phân thức $y = \\dfrac{{u(x)}}{{v(x)}}$, tại các điểm cực trị ta có $y'(x) = 0 \\Leftrightarrow \\dfrac{{u(x)}}{{v(x)}} = \\dfrac{{u'(x)}}{{v'(x)}}$.\\newline Do đó, đường thẳng đi qua hai điểm cực trị của đồ thị hàm số $(C)$ có phương trình là $y = \\dfrac{{({num_str})'}}{{({den_str})'}} = \\dfrac{{{fmt_first_term(2 * a_coef, 'x')}{fmt_signed(b_val)}}}{{1}} \\Leftrightarrow {line_true}$. Mệnh đề này **ĐÚNG**."
        else:
            if b_val != 0:
                fake_line = f"y = {fmt_first_term(2 * a_coef, 'x')}{fmt_signed(-b_val)}".strip()
            else:
                fake_line = f"y = {fmt_first_term(a_coef, 'x')}{fmt_signed(b_val + 1)}".strip()
            claim_c = f"Đường thẳng đi qua hai điểm cực trị của đồ thị hàm số $(C)$ có phương trình ${fake_line}$."
            lg_c = f"Phương trình đường thẳng đi qua hai điểm cực trị có dạng $y = \\dfrac{{u'(x)}}{{v'(x)}} = {line_true} \\ne {fake_line}$. Mệnh đề này **SAI**."
    pool.append((claim_c, dung_c, lg_c))

    # -------------------------------------------------------------
    # Mệnh đề d: Khoảng cách giữa hai điểm cực trị
    # -------------------------------------------------------------
    x_A = x0 - k_root
    x_B = x0 + k_root
    y_A = 2 * a_coef * x_A + b_val
    y_B = 2 * a_coef * x_B + b_val
    dx = x_B - x_A
    dy = y_B - y_A
    d_sq = dx**2 + dy**2
    
    if k_root == 1:
        d_tex = "2\\sqrt{5}"
        d_approx = "4{,}5"
        fake_tex_list = ["2\\sqrt{3}", "3\\sqrt{5}", "\\sqrt{5}", "4\\sqrt{5}", "5", "2\\sqrt{2}"]
        fake_sq_list = [16, 25, 40, 10]
        fake_approx_list = ["3{,}5", "5{,}2", "6{,}0"]
    else:
        d_tex = "4\\sqrt{5}"
        d_approx = "8{,}9"
        fake_tex_list = ["2\\sqrt{5}", "3\\sqrt{5}", "5\\sqrt{5}", "8", "4\\sqrt{3}"]
        fake_sq_list = [64, 100, 40, 50]
        fake_approx_list = ["7{,}8", "9{,}5", "10{,}2"]
        
    kieu_d = choice(["can_thuc", "binh_phuong", "lam_tron"])
    dung_d = choice([True, False])
    
    term_x_diff = f"({x_B} - ({x_A}))^2" if x_A < 0 else f"({x_B} - {x_A})^2"
    term_y_diff = f"({y_B} - ({y_A}))^2" if y_A < 0 else f"({y_B} - {y_A})^2"
    term_dy_sq = f"({dy})^2" if dy < 0 else f"{dy}^2"
    dx_sq = dx**2
    dy_sq = dy**2
    step_sqrt = f"\\sqrt{{{term_x_diff} + {term_y_diff}}} = \\sqrt{{{dx}^2 + {term_dy_sq}}} = \\sqrt{{{dx_sq} + {dy_sq}}} = \\sqrt{{{d_sq}}} = {d_tex}"

    lg_base = (
        f"Tử số của $y'$ bằng $0 \\Leftrightarrow {der_num_true} = 0 \\Leftrightarrow "
        f"\\left[\\begin{{aligned}} x &= {x_A} \\\\ x &= {x_B} \\end{{aligned}}\\right.$.\\newline "
        f"Đường thẳng đi qua hai điểm cực trị có phương trình là $y = \\dfrac{{({num_str})'}}{{({den_str})'}} = {line_true}$.\\newline "
        f"Tọa độ hai điểm cực trị của đồ thị $(C)$ là $A({x_A}; {y_A})$ và $B({x_B}; {y_B})$.\\newline "
        f"Khoảng cách giữa hai điểm cực trị là: "
        f"$AB = {step_sqrt}"
    )
    
    if kieu_d == "can_thuc":
        fake_val = choice(fake_tex_list)
        claim_val = d_tex if dung_d else fake_val
        claim_tpl = choice([
            f"Khoảng cách giữa hai điểm cực trị của đồ thị hàm số $(C)$ bằng ${claim_val}$.",
            f"Độ dài đoạn thẳng nối hai điểm cực trị của đồ thị hàm số $(C)$ bằng ${claim_val}$.",
            f"Gọi $A, B$ là hai điểm cực trị của đồ thị hàm số $(C)$. Khi đó độ dài đoạn thẳng $AB = {claim_val}$."
        ])
        claim_d = claim_tpl
        if dung_d:
            lg_d = f"{lg_base}$. Mệnh đề này **ĐÚNG**."
        else:
            lg_d = f"{lg_base} \\ne {claim_val}$. Mệnh đề này **SAI**."
            
    elif kieu_d == "binh_phuong":
        fake_val = choice(fake_sq_list)
        claim_val = d_sq if dung_d else fake_val
        claim_tpl = choice([
            f"Gọi $A, B$ là hai điểm cực trị của đồ thị $(C)$. Khi đó $AB^2 = {claim_val}$.",
            f"Bình phương khoảng cách giữa hai điểm cực trị của đồ thị hàm số $(C)$ bằng ${claim_val}$."
        ])
        claim_d = claim_tpl
        if dung_d:
            lg_d = f"{lg_base}$. Suy ra $AB^2 = {d_sq}$. Mệnh đề này **ĐÚNG**."
        else:
            lg_d = f"{lg_base}$. Suy ra $AB^2 = {d_sq} \\ne {claim_val}$. Mệnh đề này **SAI**."
            
    else:  # lam_tron
        fake_val = choice(fake_approx_list)
        claim_val = d_approx if dung_d else fake_val
        claim_tpl = choice([
            f"Khoảng cách giữa hai điểm cực trị của đồ thị hàm số $(C)$ làm tròn đến chữ số thập phân thứ nhất bằng ${claim_val}$.",
            f"Độ dài đoạn thẳng nối hai điểm cực trị của đồ thị hàm số $(C)$ xấp xỉ bằng ${claim_val}$."
        ])
        claim_d = claim_tpl
        if dung_d:
            lg_d = f"{lg_base} \\approx {d_approx}$. Mệnh đề này **ĐÚNG**."
        else:
            lg_d = f"{lg_base} \\approx {d_approx} \\ne {claim_val}$. Mệnh đề này **SAI**."
            
    pool.append((claim_d, dung_d, lg_d))

    choices = []
    lg_items = []
    for claim, is_true, lg in pool:
        ch_str = f"{{\\True {claim}}}" if is_true else f"{{{claim}}}"
        choices.append(ch_str)
        lg_items.append(f"\\itemch {lg}")

    loigiai = "\\begin{itemchoice}\n" + "\n".join(lg_items) + "\n\\end{itemchoice}"
    return caudan, choices, loigiai

# ==============================================================================
# CHƯƠNG II: Dạng Đúng/Sai Vectơ trong hình hộp (Hình vẽ sẵn)
# Câu 3: Cho hình hộp (Vẽ sẵn hình). Xác định vectơ bằng nhau, quy tắc ba điểm,
# quy tắc hình bình hành, quy tắc hình hộp, độ dài vectơ (4 nhận biết).
# ==============================================================================
def sinh_cau_dung_sai_hinh_hop_vecto():
    # Danh sách các bộ tên gọi đỉnh cho hình hộp
    naming_schemes = [
        # (Đáy dưới, Đáy trên, Tên gọi LaTeX, label_dict)
        ("A", "B", "C", "D", "A'", "B'", "C'", "D'", "ABCD.A'B'C'D'"),
        ("A", "B", "C", "D", "E", "F", "G", "H", "ABCD.EFGH"),
        ("E", "F", "G", "H", "E'", "F'", "G'", "H'", "EFGH.E'F'G'H'"),
        ("M", "N", "P", "Q", "M'", "N'", "P'", "Q'", "MNPQ.M'N'P'Q'"),
        ("A'", "B'", "C'", "D'", "A", "B", "C", "D", "A'B'C'D'.ABCD"),
        ("A", "B", "C", "D", "A_1", "B_1", "C_1", "D_1", "ABCD.A_1B_1C_1D_1"),
    ]
    A, B, C, D, Ap, Bp, Cp, Dp, name_box = choice(naming_schemes)

    # Đa dạng hóa câu mở đầu
    lead_phrase = choice([
        f"Cho hình hộp ${name_box}$. Xét tính đúng sai của các mệnh đề sau:",
        f"Cho hình hộp ${name_box}$ như hình vẽ bên. Hãy chọn đúng hoặc sai cho mỗi khẳng định sau:",
        f"Cho hình hộp ${name_box}$ (có các mặt đều là hình bình hành). Xét tính đúng sai của mỗi khẳng định:",
        f"Cho hình hộp ${name_box}$ với các vectơ trong không gian. Xét tính đúng sai của các khẳng định sau:"
    ])

    tikz_code = f"""\\begin{{tikzpicture}}[scale=0.75, font=\\footnotesize]
\\coordinate (A) at (0, 2.5);
\\coordinate (B) at (-1.8, 1);
\\coordinate (C) at (1.8, 1);
\\coordinate (D) at (3.6, 2.5);
\\coordinate (A') at (0, 0);
\\coordinate (B') at (-1.8, -1.5);
\\coordinate (C') at (1.8, -1.5);
\\coordinate (D') at (3.6, 0);

\\draw[dashed] (A) -- (A') (A) -- (B) (A) -- (D);
\\draw[dashed] (A') -- (B') (A') -- (D');
\\draw (B) -- (C) -- (D) -- (D') -- (C') -- (B') -- (B);
\\draw (C) -- (C');
\\draw (B') -- (C');

\\fill (A) circle (1.2pt) node[above] {{${A}$}};
\\fill (B) circle (1.2pt) node[left] {{${B}$}};
\\fill (C) circle (1.2pt) node[below right] {{${C}$}};
\\fill (D) circle (1.2pt) node[above right] {{${D}$}};
\\fill (A') circle (1.2pt) node[below left] {{${Ap}$}};
\\fill (B') circle (1.2pt) node[below left] {{${Bp}$}};
\\fill (C') circle (1.2pt) node[below] {{${Cp}$}};
\\fill (D') circle (1.2pt) node[right] {{${Dp}$}};
\\end{{tikzpicture}}"""

    caudan = f"""\\immini{{{lead_phrase}}}
{{{tikz_code}}}"""

    pool = []

    # 1. Nhóm Vectơ bằng nhau
    dung_1 = choice([True, False])
    loai_eq = choice(["canh_day", "canh_ben", "duong_cheo_mat"])
    if loai_eq == "canh_day":
        if dung_1:
            u_vec, v_vec = choice([
                (f"\\vec{{{A}{B}}}", f"\\vec{{{D}{C}}}"),
                (f"\\vec{{{A}{D}}}", f"\\vec{{{B}{C}}}"),
                (f"\\vec{{{Ap}{Bp}}}", f"\\vec{{{Dp}{Cp}}}"),
                (f"\\vec{{{Ap}{Dp}}}", f"\\vec{{{Bp}{Cp}}}"),
                (f"\\vec{{{A}{B}}}", f"\\vec{{{Ap}{Bp}}}"),
                (f"\\vec{{{C}{D}}}", f"\\vec{{{B}{A}}}")
            ])
            claim = f"${u_vec} = {v_vec}$."
            lg = f"Do ${A}{B}{C}{D}$ và ${Ap}{Bp}{Cp}{Dp}$ là các hình bình hành nên các cặp cạnh đối diện song song và cùng độ dài, do đó ${u_vec} = {v_vec}$. Mệnh đề này **ĐÚNG**."
        else:
            u_vec, v_vec = choice([
                (f"\\vec{{{A}{B}}}", f"\\vec{{{C}{D}}}"),
                (f"\\vec{{{A}{D}}}", f"\\vec{{{C}{B}}}"),
                (f"\\vec{{{Ap}{Bp}}}", f"\\vec{{{Cp}{Dp}}}"),
                (f"\\vec{{{A}{B}}}", f"\\vec{{{Bp}{Ap}}}")
            ])
            claim = f"${u_vec} = {v_vec}$."
            lg = f"Hai vectơ ${u_vec}$ và ${v_vec}$ cùng độ dài nhưng ngược hướng nên ${u_vec} = -{v_vec} \\ne {v_vec}$. Mệnh đề này **SAI**."
    elif loai_eq == "canh_ben":
        if dung_1:
            u_vec, v_vec = choice([
                (f"\\vec{{{A}{Ap}}}", f"\\vec{{{B}{Bp}}}"),
                (f"\\vec{{{B}{Bp}}}", f"\\vec{{{C}{Cp}}}"),
                (f"\\vec{{{C}{Cp}}}", f"\\vec{{{D}{Dp}}}"),
                (f"\\vec{{{Ap}{A}}}", f"\\vec{{{Bp}{B}}}")
            ])
            claim = f"${u_vec} = {v_vec}$."
            lg = f"Các cạnh bên của hình hộp đôi một song song, cùng chiều và bằng nhau nên ${u_vec} = {v_vec}$. Mệnh đề này **ĐÚNG**."
        else:
            u_vec, v_vec = choice([
                (f"\\vec{{{A}{Ap}}}", f"\\vec{{{Bp}{B}}}"),
                (f"\\vec{{{C}{Cp}}}", f"\\vec{{{Dp}{D}}}"),
                (f"\\vec{{{B}{Bp}}}", f"\\vec{{{Cp}{C}}}")
            ])
            claim = f"${u_vec} = {v_vec}$."
            lg = f"Hai vectơ này có hướng ngược nhau nên ${u_vec} = -{v_vec} \\ne {v_vec}$. Mệnh đề này **SAI**."
    else:
        # Đường chéo mặt
        if dung_1:
            u_vec, v_vec = choice([
                (f"\\vec{{{A}{C}}}", f"\\vec{{{Ap}{Cp}}}"),
                (f"\\vec{{{B}{D}}}", f"\\vec{{{Bp}{Dp}}}"),
                (f"\\vec{{{C}{A}}}", f"\\vec{{{Cp}{Ap}}}")
            ])
            claim = f"${u_vec} = {v_vec}$."
            lg = f"Tứ giác ${A}{Ap}{Cp}{C}$ là hình bình hành nên ${u_vec} = {v_vec}$. Mệnh đề này **ĐÚNG**."
        else:
            u_vec, v_vec = choice([
                (f"\\vec{{{A}{C}}}", f"\\vec{{{B}{D}}}"),
                (f"\\vec{{{A}{C}}}", f"\\vec{{{Cp}{Ap}}}"),
                (f"\\vec{{{Ap}{Cp}}}", f"\\vec{{{Dp}{Bp}}}")
            ])
            claim = f"${u_vec} = {v_vec}$."
            lg = f"Hai vectơ này không cùng phương hoặc ngược hướng nên không bằng nhau. Mệnh đề này **SAI**."
    pool.append((claim, dung_1, lg))

    # 2. Nhóm Quy tắc ba điểm (phép cộng hoặc phép trừ)
    dung_2 = choice([True, False])
    loai_rule3 = choice(["cong", "tru"])
    if loai_rule3 == "cong":
        X, Y, Z = choice([(A, B, C), (B, C, D), (A, D, Dp), (Ap, Bp, Cp), (A, B, Bp)])
        if dung_2:
            claim = f"$\\vec{{{X}{Y}}} + \\vec{{{Y}{Z}}} = \\vec{{{X}{Z}}}$."
            lg = f"Theo quy tắc ba điểm đối với phép cộng vectơ, ta có $\\vec{{{X}{Y}}} + \\vec{{{Y}{Z}}} = \\vec{{{X}{Z}}}$. Mệnh đề này **ĐÚNG**."
        else:
            claim = f"$\\vec{{{X}{Y}}} + \\vec{{{Y}{Z}}} = \\vec{{{Z}{X}}}$."
            lg = f"Theo quy tắc ba điểm, $\\vec{{{X}{Y}}} + \\vec{{{Y}{Z}}} = \\vec{{{X}{Z}}} = -\\vec{{{Z}{X}}} \\ne \\vec{{{Z}{X}}}$. Mệnh đề này **SAI**."
    else:
        X, Y, Z = choice([(A, C, B), (B, D, A), (Ap, Cp, Bp), (C, A, D)])
        if dung_2:
            claim = f"$\\vec{{{X}{Z}}} - \\vec{{{X}{Y}}} = \\vec{{{Y}{Z}}}$."
            lg = f"Theo quy tắc ba điểm đối với phép trừ vectơ: $\\vec{{{X}{Z}}} - \\vec{{{X}{Y}}} = \\vec{{{Y}{Z}}}$. Mệnh đề này **ĐÚNG**."
        else:
            claim = f"$\\vec{{{X}{Z}}} - \\vec{{{X}{Y}}} = \\vec{{{Z}{Y}}}$."
            lg = f"Theo quy tắc phép trừ, $\\vec{{{X}{Z}}} - \\vec{{{X}{Y}}} = \\vec{{{Y}{Z}}} \\ne \\vec{{{Z}{Y}}}$. Mệnh đề này **SAI**."
    pool.append((claim, dung_2, lg))

    # 3. Nhóm Quy tắc hình bình hành (trên các mặt của hình hộp)
    dung_3 = choice([True, False])
    face = choice(["day_duoi", "day_tren", "mat_ben_1", "mat_ben_2"])
    if face == "day_duoi":
        if dung_3:
            claim = f"$\\vec{{{A}{B}}} + \\vec{{{A}{D}}} = \\vec{{{A}{C}}}$."
            lg = f"Vì ${A}{B}{C}{D}$ là hình bình hành nên theo quy tắc hình bình hành ta có $\\vec{{{A}{B}}} + \\vec{{{A}{D}}} = \\vec{{{A}{C}}}$. Mệnh đề này **ĐÚNG**."
        else:
            claim = f"$\\vec{{{A}{B}}} + \\vec{{{A}{D}}} = \\vec{{{B}{D}}}$."
            lg = f"Theo quy tắc hình bình hành, $\\vec{{{A}{B}}} + \\vec{{{A}{D}}} = \\vec{{{A}{C}}} \\ne \\vec{{{B}{D}}}$. Mệnh đề này **SAI**."
    elif face == "day_tren":
        if dung_3:
            claim = f"$\\vec{{{Ap}{Bp}}} + \\vec{{{Ap}{Dp}}} = \\vec{{{Ap}{Cp}}}$."
            lg = f"Vì ${Ap}{Bp}{Cp}{Dp}$ là hình bình hành nên theo quy tắc hình bình hành ta có $\\vec{{{Ap}{Bp}}} + \\vec{{{Ap}{Dp}}} = \\vec{{{Ap}{Cp}}}$. Mệnh đề này **ĐÚNG**."
        else:
            claim = f"$\\vec{{{Ap}{Bp}}} + \\vec{{{Ap}{Dp}}} = \\vec{{{Cp}{Ap}}}$."
            lg = f"Theo quy tắc hình bình hành, tổng phải bằng vectơ đường chéo xuất phát từ ${Ap}$ là $\\vec{{{Ap}{Cp}}}$. Mệnh đề này **SAI**."
    elif face == "mat_ben_1":
        if dung_3:
            claim = f"$\\vec{{{A}{B}}} + \\vec{{{A}{Ap}}} = \\vec{{{A}{Bp}}}$."
            lg = f"Vì ${A}{B}{Bp}{Ap}$ là hình bình hành nên $\\vec{{{A}{B}}} + \\vec{{{A}{Ap}}} = \\vec{{{A}{Bp}}}$. Mệnh đề này **ĐÚNG**."
        else:
            claim = f"$\\vec{{{A}{B}}} + \\vec{{{A}{Ap}}} = \\vec{{{B}{Ap}}}$."
            lg = f"Tổng hai vectơ có chung gốc ${A}$ là vectơ đường chéo $\\vec{{{A}{Bp}}}$, không phải $\\vec{{{B}{Ap}}}$. Mệnh đề này **SAI**."
    else:
        if dung_3:
            claim = f"$\\vec{{{A}{D}}} + \\vec{{{A}{Ap}}} = \\vec{{{A}{Dp}}}$."
            lg = f"Vì ${A}{D}{Dp}{Ap}$ là hình bình hành nên $\\vec{{{A}{D}}} + \\vec{{{A}{Ap}}} = \\vec{{{A}{Dp}}}$. Mệnh đề này **ĐÚNG**."
        else:
            claim = f"$\\vec{{{A}{D}}} + \\vec{{{A}{Ap}}} = \\vec{{{Ap}{D}}}$."
            lg = f"Tổng hai vectơ cùng xuất phát từ đỉnh ${A}$ là $\\vec{{{A}{Dp}}}$. Mệnh đề này **SAI**."
    pool.append((claim, dung_3, lg))

    # 4. Nhóm Quy tắc hình hộp hoặc Độ dài vectơ
    dung_4 = choice([True, False])
    loai_4 = choice(["quy_tac_hinh_hop", "do_dai_vecto"])
    if loai_4 == "quy_tac_hinh_hop":
        origin_vertex = choice(["A", "Cp", "B", "Dp"])
        if origin_vertex == "A":
            if dung_4:
                claim = f"$\\vec{{{A}{B}}} + \\vec{{{A}{D}}} + \\vec{{{A}{Ap}}} = \\vec{{{A}{Cp}}}$."
                lg = f"Theo quy tắc hình hộp, tổng ba vectơ xuất phát từ đỉnh ${A}$ bằng vectơ đường chéo $\\vec{{{A}{Cp}}}$. Mệnh đề này **ĐÚNG**."
            else:
                wrong_target = choice([f"\\vec{{{Ap}{C}}}", f"\\vec{{{C}{Ap}}}", f"\\vec{{{A}{C}}}"])
                claim = f"$\\vec{{{A}{B}}} + \\vec{{{A}{D}}} + \\vec{{{A}{Ap}}} = {wrong_target}$."
                lg = f"Theo quy tắc hình hộp, $\\vec{{{A}{B}}} + \\vec{{{A}{D}}} + \\vec{{{A}{Ap}}} = \\vec{{{A}{Cp}}} \\ne {wrong_target}$. Mệnh đề này **SAI**."
        elif origin_vertex == "Cp":
            if dung_4:
                claim = f"$\\vec{{{Cp}{Bp}}} + \\vec{{{Cp}{Dp}}} + \\vec{{{Cp}{C}}} = \\vec{{{Cp}{A}}}$."
                lg = f"Theo quy tắc hình hộp, ba vectơ cùng xuất phát từ đỉnh ${Cp}$ có tổng bằng vectơ đường chéo $\\vec{{{Cp}{A}}}$. Mệnh đề này **ĐÚNG**."
            else:
                claim = f"$\\vec{{{Cp}{Bp}}} + \\vec{{{Cp}{Dp}}} + \\vec{{{Cp}{C}}} = \\vec{{{A}{Cp}}}$."
                lg = f"Vectơ tổng phải cùng hướng xuất phát từ ${Cp}$ nên bằng $\\vec{{{Cp}{A}}} = -\\vec{{{A}{Cp}}}$. Mệnh đề này **SAI**."
        elif origin_vertex == "B":
            if dung_4:
                claim = f"$\\vec{{{B}{A}}} + \\vec{{{B}{C}}} + \\vec{{{B}{Bp}}} = \\vec{{{B}{Dp}}}$."
                lg = f"Theo quy tắc hình hộp xuất phát từ đỉnh ${B}$, ta có $\\vec{{{B}{A}}} + \\vec{{{B}{C}}} + \\vec{{{B}{Bp}}} = \\vec{{{B}{Dp}}}$. Mệnh đề này **ĐÚNG**."
            else:
                claim = f"$\\vec{{{B}{A}}} + \\vec{{{B}{C}}} + \\vec{{{B}{Bp}}} = \\vec{{{Bp}{D}}}$."
                lg = f"Tổng ba vectơ xuất phát từ ${B}$ bằng đường chéo $\\vec{{{B}{Dp}}}$. Mệnh đề này **SAI**."
        else:
            if dung_4:
                claim = f"$\\vec{{{Dp}{Ap}}} + \\vec{{{Dp}{Cp}}} + \\vec{{{Dp}{D}}} = \\vec{{{Dp}{B}}}$."
                lg = f"Theo quy tắc hình hộp xuất phát từ đỉnh ${Dp}$, ta có $\\vec{{{Dp}{Ap}}} + \\vec{{{Dp}{Cp}}} + \\vec{{{Dp}{D}}} = \\vec{{{Dp}{B}}}$. Mệnh đề này **ĐÚNG**."
            else:
                claim = f"$\\vec{{{Dp}{Ap}}} + \\vec{{{Dp}{Cp}}} + \\vec{{{Dp}{D}}} = \\vec{{{D}{Bp}}}$."
                lg = f"Quy tắc hình hộp cho kết quả $\\vec{{{Dp}{B}}}$. Mệnh đề này **SAI**."
    else:
        # Độ dài vectơ trong hình hộp
        pair_len = choice([
            (f"\\vec{{{A}{B}}}", f"\\vec{{{Cp}{Dp}}}"),
            (f"\\vec{{{A}{Ap}}}", f"\\vec{{{C}{Cp}}}"),
            (f"\\vec{{{A}{D}}}", f"\\vec{{{Bp}{Cp}}}"),
            (f"\\vec{{{A}{C}}}", f"\\vec{{{Ap}{Cp}}}")
        ])
        if dung_4:
            claim = f"$\\left| {pair_len[0]} \\right| = \\left| {pair_len[1]} \\right|$."
            lg = f"Vì các đoạn thẳng tương ứng có độ dài bằng nhau nên $\\left| {pair_len[0]} \\right| = \\left| {pair_len[1]} \\right|$. Mệnh đề này **ĐÚNG**."
        else:
            claim = f"$\\left| \\vec{{{A}{B}}} \\right| = \\left| \\vec{{{A}{Ap}}} \\right|$ trong mọi hình hộp."
            lg = f"Trong một hình hộp tổng quát, độ dài cạnh đáy ${A}{B}$ và cạnh bên ${A}{Ap}$ không nhất thiết bằng nhau. Mệnh đề này **SAI**."
    pool.append((claim, dung_4, lg))

    choices = []
    lg_items = []
    for claim, is_true, lg in pool:
        ch_str = f"{{\\True {claim}}}" if is_true else f"{{{claim}}}"
        choices.append(ch_str)
        lg_items.append(f"\\itemch {lg}")

    loigiai = "\\begin{itemchoice}\n" + "\n".join(lg_items) + "\n\\end{itemchoice}"
    return caudan, choices, loigiai



# ==============================================================================
# BÀI TOÁN CHUYỂN ĐỘNG - 4 PHƯƠNG ÁN (NHIỀU LỰA CHỌN)
# ==============================================================================

def sinh_cau_chuyen_dong_van_toc_tang():
    """4 Phương án: Khoảng thời gian vận tốc của vật tăng lên"""
    k = choice([1, 2])
    t0 = randint(2, 6)
    b_coeff = 3 * k * t0
    c = randint(5, 25)
    d = randint(-10, 15)
    T = t0 + randint(4, 8)

    poly_s = f"s(t) = {-k}t^3 + {b_coeff}t^2 + {c}t + {d}".replace('+-', '-').replace('1t', 't').replace('-1t^3', '-t^3')
    poly_v = f"v(t) = s'(t) = {-3*k}t^2 + {6*k*t0}t + {c}".replace('+-', '-').replace('1t', 't')
    poly_a = f"a(t) = v'(t) = {-6*k}t + {6*k*t0}".replace('+-', '-')

    caudan = f"""Một vật chuyển động theo quy luật ${poly_s}$ với $t$ (giây) là khoảng thời gian tính từ lúc bắt đầu chuyển động và $s(t)$ (mét) là quãng đường vật đi được trong khoảng thời gian đó. Trong khoảng thời gian ${T}$ giây kể từ lúc bắt đầu chuyển động ($0 \\le t \\le {T}$), vận tốc của vật tăng lên trong khoảng thời gian nào dưới đây?"""

    opt_true = f"(0; {t0})"
    distractors = [
        f"({t0}; {T})",
        f"(0; {T})",
        f"({t0}; +\\infty)"
    ]
    if f"(0; {2*t0})" not in distractors and 2*t0 <= T:
        distractors[2] = f"(0; {2*t0})"

    phuongan = [
        f"{{\\True ${opt_true}$}}\n",
        f"{{${distractors[0]}$}}\n",
        f"{{${distractors[1]}$}}\n",
        f"{{${distractors[2]}$}}\n"
    ]
    random.shuffle(phuongan)

    loigiai = f"""Vận tốc tức thời của vật tại thời điểm $t$ là:
$$v(t) = s'(t) = \\left({poly_s.split('=')[1].strip()}\\right)' = {-3*k}t^2 + {6*k*t0}t + {c}.$$
Gia tốc tức thời của vật là:
$$a(t) = v'(t) = \\left({-3*k}t^2 + {6*k*t0}t + {c}\\right)' = {-6*k}t + {6*k*t0}.$$
Vận tốc của vật tăng lên khi và chỉ khi:
$$v'(t) > 0 \\Leftrightarrow {-6*k}t + {6*k*t0} > 0 \\Leftrightarrow {-6*k}t > {-6*k*t0} \\Leftrightarrow t < {t0}.$$
Kết hợp với điều kiện thời gian xét trong khoảng $0 \\le t \\le {T}$, ta suy ra vận tốc của vật tăng lên trong khoảng thời gian $(0; {t0})$ (giây)."""

    return caudan, phuongan, loigiai


def sinh_cau_chuyen_dong_van_toc_giam_khoang():
    """4 Phương án: Khoảng thời gian vận tốc tức thời của chất điểm giảm"""
    dang_pt = choice([1, 2])
    if dang_pt == 1:
        k = randint(3, 8)
        c = randint(-15, 20)
        d = randint(2, 20)
        T = k + randint(5, 12)
        poly_s = f"s(t) = -\\dfrac{{t^3}}{{3}} + {k}t^2 + {c}t + {d}".replace('+-', '-')
        poly_v = f"v(t) = s'(t) = -t^2 + {2*k}t + {c}".replace('+-', '-')
        poly_a = f"a(t) = v'(t) = -2t + {2*k}".replace('+-', '-')
        t0 = k
    else:
        k = choice([1, 2])
        t0 = randint(3, 7)
        b_coeff = 3 * k * t0
        c = randint(5, 20)
        d = randint(2, 15)
        T = 2 * t0 + randint(2, 5)
        poly_s = f"s(t) = {-k}t^3 + {b_coeff}t^2 + {c}t + {d}".replace('+-', '-').replace('1t', 't').replace('-1t^3', '-t^3')
        poly_v = f"v(t) = s'(t) = {-3*k}t^2 + {6*k*t0}t + {c}".replace('+-', '-').replace('1t', 't')
        poly_a = f"a(t) = v'(t) = {-6*k}t + {6*k*t0}".replace('+-', '-')

    caudan = f"""Một chất điểm chuyển động theo phương trình ${poly_s}$, trong đó $t$ tính bằng giây ($0 \\le t \\le {T}$) và $s$ tính bằng mét. Trong ${T}$ giây đầu tiên, vận tốc tức thời của chất điểm giảm trong khoảng thời gian nào dưới đây?"""

    opt_true = f"({t0}; {T})"
    distractors = [
        f"(0; {t0})",
        f"(0; {T})",
        f"({t0}; +\\infty)"
    ]

    phuongan = [
        f"{{\\True ${opt_true}$}}\n",
        f"{{${distractors[0]}$}}\n",
        f"{{${distractors[1]}$}}\n",
        f"{{${distractors[2]}$}}\n"
    ]
    random.shuffle(phuongan)

    loigiai = f"""Vận tốc tức thời của chất điểm tại thời điểm $t$ là:
$$v(t) = s'(t) = {poly_v.split('=')[2].strip()}.$$
Gia tốc tức thời của chất điểm là:
$$a(t) = v'(t) = {poly_a.split('=')[2].strip()}.$$
Vận tốc tức thời của chất điểm giảm khi và chỉ khi:
$$v'(t) < 0 \\Leftrightarrow {poly_a.split('=')[2].strip()} < 0 \\Leftrightarrow t > {t0}.$$
Trong ${T}$ giây đầu tiên ($0 \\le t \\le {T}$), vận tốc tức thời của chất điểm giảm trong khoảng thời gian $({t0}; {T})$ (giây)."""

    return caudan, phuongan, loigiai


def sinh_cau_chuyen_dong_thoi_diem_van_toc_giam():
    """4 Phương án: Kể từ giây thứ bao nhiêu thì vận tốc bắt đầu giảm / đạt cực đại"""
    a = choice([1, 2])
    t0 = randint(2, 6)
    b = 2 * a * t0
    c = randint(10, 40)

    poly_v = f"v(t) = {-a}t^2 + {b}t + {c}".replace('+-', '-').replace('-1t^2', '-t^2')

    caudan = f"""Một vật chuyển động có vận tốc được xác định bởi hàm số ${poly_v}$ với $t \\ge 0$, trong đó $t$ tính bằng giây và $v$ tính bằng m/s. Kể từ giây thứ bao nhiêu trở đi thì vận tốc của vật bắt đầu giảm?"""

    opt_true = f"t = {t0}\\text{{ s}}"
    distractors = [
        f"t = {2*t0}\\text{{ s}}",
        f"t = {t0 + 2}\\text{{ s}}",
        f"t = {max(1, t0 - 1)}\\text{{ s}}"
    ]

    phuongan = [
        f"{{\\True Giây thứ ${t0}$ (tức ${opt_true}$)}}\n",
        f"{{Giây thứ ${2*t0}$ (tức ${distractors[0]}$)}}\n",
        f"{{Giây thứ ${t0 + 2}$ (tức ${distractors[1]}$)}}\n",
        f"{{Giây thứ ${max(1, t0 - 1)}$ (tức ${distractors[2]}$)}}\n"
    ]
    random.shuffle(phuongan)

    loigiai = f"""Gia tốc tức thời của chuyển động là:
$$a(t) = v'(t) = \\left({poly_v.split('=')[1].strip()}\\right)' = {-2*a}t + {b}.$$
Vận tốc của vật giảm khi và chỉ khi:
$$v'(t) < 0 \\Leftrightarrow {-2*a}t + {b} < 0 \\Leftrightarrow {-2*a}t < {-b} \\Leftrightarrow t > \\dfrac{{{b}}}{{{2*a}}} = {t0}.$$
Như vậy, vận tốc của vật đạt giá trị lớn nhất tại $t = {t0}$ và kể từ giây thứ ${t0}$ trở đi thì vận tốc của vật bắt đầu giảm."""

    return caudan, phuongan, loigiai


def sinh_cau_chuyen_dong_van_toc_lon_nhat():
    """4 Phương án: Vận tốc lớn nhất (tốc độ cực đại) trong quá trình chuyển động"""
    k = choice([1, 2])
    t0 = randint(2, 5)
    b_coeff = 3 * k * t0
    c = randint(5, 20)
    d = randint(2, 15)
    T = t0 + randint(3, 6)

    poly_s = f"s(t) = {-k}t^3 + {b_coeff}t^2 + {c}t + {d}".replace('+-', '-').replace('1t', 't').replace('-1t^3', '-t^3')
    v_max = 3 * k * (t0**2) + c
    v_start = c
    v_end = -3 * k * (T**2) + 6 * k * t0 * T + c

    caudan = f"""Trong khoảng thời gian ${T}$ giây đầu tiên ($0 \\le t \\le {T}$), một chất điểm chuyển động theo phương trình:
$${poly_s},$$
trong đó $t$ tính bằng giây và $s$ tính bằng mét. Vận tốc lớn nhất mà chất điểm đạt được trong khoảng thời gian trên bằng bao nhiêu mét/giây?"""

    opt_true = f"{v_max}\\text{{ m/s}}"
    wrong_1 = f"{v_start}\\text{{ m/s}}"
    wrong_2 = f"{v_max - 2*k*t0}\\text{{ m/s}}"
    wrong_3 = f"{v_max + 3*k*t0}\\text{{ m/s}}"

    phuongan = [
        f"{{\\True ${opt_true}$}}\n",
        f"{{${wrong_1}$}}\n",
        f"{{${wrong_2}$}}\n",
        f"{{${wrong_3}$}}\n"
    ]
    random.shuffle(phuongan)

    loigiai = f"""Vận tốc tức thời của chất điểm tại thời điểm $t$ là:
$$v(t) = s'(t) = {-3*k}t^2 + {6*k*t0}t + {c}.$$
Ta có $v'(t) = {-6*k}t + {6*k*t0}$.
$$v'(t) = 0 \\Leftrightarrow {-6*k}t + {6*k*t0} = 0 \\Leftrightarrow t = {t0} \\in [0; {T}].$$
Bảng biến thiên của hàm số $v(t)$ trên đoạn $[0; {T}]$:
\\begin{{center}}
\\begin{{tikzpicture}}
    \\tkzTabInit[nocadre,lgt=1.2,espcl=2.5,deltacl=0.6]
    {{$t$ /0.6, $v'(t)$ /0.6, $v(t)$ /2}}
    {{$0$, ${t0}$, ${T}$}}
    \\tkzTabLine{{,+,0,-,}}
    \\tkzTabVar{{-/${v_start}$, +/${v_max}$, -/${v_end}$}}
\\end{{tikzpicture}}
\\end{{center}}
Từ bảng biến thiên, vận tốc lớn nhất mà chất điểm đạt được trong khoảng thời gian trên là $v_{{\\max}} = v({t0}) = {v_max}\\text{{ m/s}}$ tại thời điểm $t = {t0}\\text{{ s}}$."""

    return caudan, phuongan, loigiai


def sinh_cau_chuyen_dong_gia_toc_tang():
    """4 Phương án: Khoảng thời gian gia tốc tăng của chuyển động"""
    c1 = choice([1, 2])
    m_val = randint(2, 6)
    c2 = 3 * c1 * m_val
    c3 = randint(10, 30)
    T = m_val + randint(5, 12)

    poly_v = f"v(t) = {c1}t^3 - {c2}t^2 + {c3}".replace('1t^3', 't^3')

    caudan = f"""Vận tốc của một tên lửa đẩy trong khoảng thời gian từ lúc phóng tại thời điểm $t = 0$ (giây) cho đến thời điểm $t = {T}$ (giây) được xác định bởi hàm số:
$$v(t) = {poly_v}\\quad (\\text{{m/s}}).$$
Trong khoảng thời gian nào dưới đây tính từ lúc phóng, gia tốc của tên lửa tăng lên?"""

    opt_true = f"({m_val}; {T})"
    distractors = [
        f"(0; {m_val})",
        f"(0; {T})",
        f"({m_val}; +\\infty)"
    ]

    phuongan = [
        f"{{\\True ${opt_true}$}}\n",
        f"{{${distractors[0]}$}}\n",
        f"{{${distractors[1]}$}}\n",
        f"{{${distractors[2]}$}}\n"
    ]
    random.shuffle(phuongan)

    loigiai = f"""Gia tốc tức thời của tên lửa tại thời điểm $t$ là:
$$a(t) = v'(t) = \\left({poly_v}\\right)' = {3*c1}t^2 - {2*c2}t.$$
Gia tốc của tên lửa tăng khi và chỉ khi đạo hàm cấp hai của vận tốc dương:
$$a'(t) > 0 \\Leftrightarrow {6*c1}t - {2*c2} > 0 \\Leftrightarrow {6*c1}t > {2*c2} \\Leftrightarrow t > \\dfrac{{{2*c2}}}{{{6*c1}}} = {m_val}.$$
Vì xét trong khoảng thời gian từ $t = 0$ đến $t = {T}$ (giây), suy ra gia tốc của tên lửa tăng trong khoảng thời gian $({m_val}; {T})$ (giây)."""

    return caudan, phuongan, loigiai


# ==============================================================================
# BÀI TOÁN THỰC TẾ 5 DẠNG MỚI (MC 4 PHƯƠNG ÁN & TRẢ LỜI NGẮN TLN)
# ==============================================================================

# --- DẠNG 1: LỢI NHUẬN SẢN XUẤT ĐỒNG BIẾN (CÂU 17) ---

def _gen_loi_nhuan_xe_dap():
    items = ["xe đạp", "máy tính bảng", "đồng hồ thông minh", "quạt điện tích điện", "máy lọc không khí"]
    item_name = choice(items)
    currency = choice(["euro", "USD"])
    
    alpha = choice([0.02, 0.015, 0.025])
    x0 = choice([45, 50, 55, 60])
    beta = round(3 * alpha * x0, 2)
    r = choice([35, 38, 40, 42])
    p = choice([110, 120, 130, 140])
    gamma = round(p - 3 * alpha * (r**2 - x0**2) + uniform(-1.5, 1.5), 1)
    d = randint(1800, 3200)
    
    A = -3 * alpha
    B = 2 * beta
    C = p - gamma
    disc = B**2 - 4 * A * C
    r1 = (-B + math.sqrt(disc)) / (2 * A)
    r2 = (-B - math.sqrt(disc)) / (2 * A)
    x_min, x_max = min(r1, r2), max(r1, r2)
    a = math.ceil(x_min)
    b = math.floor(x_max)
    ans_val = a + b
    X_max = b + randint(20, 40)
    
    poly_K = f"K(x) = {alpha}x^3 - {beta}x^2 + {gamma}x + {d}".replace('+-', '-').replace('.', ',')
    
    caudan = f"""Một nhà máy sản xuất {item_name} theo đơn giá ${p}$ {currency}. Chi phí mỗi ngày của nhà máy được cho bởi hàm số ${poly_K}$, trong đó $x$ là số lượng {item_name} sản xuất được trong ngày hôm đó. Mỗi ngày nhà máy có thể sản xuất tối đa ${X_max}$ {item_name}. Giả sử số {item_name} sản xuất được trong mỗi ngày đều được bán hết vào cuối ngày đó. Gọi $G(x)$ là hàm số biểu diễn lợi nhuận hàng ngày của nhà máy. Lợi nhuận hàng ngày là hàm đồng biến theo $x$ khi $x \\in (a; b)$, trong đó $a$ và $b$ là các giá trị nguyên dương. Giá trị lớn nhất của $a + b$ bằng bao nhiêu?"""

    alpha_str = f"{alpha}".replace('.', ',')
    beta_str = f"{beta}".replace('.', ',')
    gamma_str = f"{gamma}".replace('.', ',')
    diff_p_gamma = round(p - gamma, 1)
    diff_str = f"{diff_p_gamma}".replace('.', ',')
    coef_3a = f"{round(3*alpha, 3)}".replace('.', ',')
    coef_2b = f"{round(2*beta, 2)}".replace('.', ',')

    loigiai = f"""Doanh thu mỗi ngày của nhà máy khi bán hết $x$ sản phẩm là:
$$R(x) = {p}x\\quad ({currency}).$$
Hàm lợi nhuận hàng ngày của nhà máy là:
$$G(x) = R(x) - K(x) = {p}x - \\left({alpha_str}x^3 - {beta_str}x^2 + {gamma_str}x + {d}\\right) = -{alpha_str}x^3 + {beta_str}x^2 + {diff_str}x - {d}.$$
Đạo hàm của hàm lợi nhuận là:
$$G'(x) = -{coef_3a}x^2 + {coef_2b}x + {diff_str}.$$
Cho $G'(x) = 0 \\Leftrightarrow -{coef_3a}x^2 + {coef_2b}x + {diff_str} = 0 \\Leftrightarrow \\left[\\begin{{aligned}} x_1 &\\approx {x_min:.2f} \\\\ x_2 &\\approx {x_max:.2f} \\end{{aligned}}\\right.$$
Bảng xét dấu $G'(x)$:
- $G'(x) > 0$ khi và chỉ khi $x \\in ({x_min:.2f}; {x_max:.2f})$.
Do đó, hàm số $G(x)$ đồng biến trên khoảng $({x_min:.2f}; {x_max:.2f})$.
Vì $a, b$ là các số nguyên dương và lợi nhuận là hàm đồng biến khi $x \\in (a; b) \\subset ({x_min:.2f}; {x_max:.2f})$ nên:
$$a \\ge {a}\\quad \\text{{và}}\\quad b \\le {b}.$$
Để tổng $a + b$ lớn nhất thì $a$ lớn nhất và $b$ lớn nhất, tức là $a = {a}$ và $b = {b}$.
Vậy giá trị lớn nhất của $a + b$ là:
$$a + b = {a} + {b} = {ans_val}.$$""".replace('+-', '-').replace('+ -', '- ')

    distractors = [ans_val, ans_val - 10, ans_val + 10, ans_val - 5]
    if len(set(distractors)) < 4:
        distractors = [ans_val, b, a + b - 1, a + b + 2]
    return caudan, loigiai, ans_val, distractors

def sinh_cau_mc_loi_nhuan_xe_dap():
    """MC: Chi phí và khoảng đồng biến lợi nhuận (Câu 17)"""
    caudan, loigiai, ans_val, ans_opts = _gen_loi_nhuan_xe_dap()
    phuongan = [
        f"{{\\True ${ans_opts[0]}$}}\n",
        f"{{${ans_opts[1]}$}}\n",
        f"{{${ans_opts[2]}$}}\n",
        f"{{${ans_opts[3]}$}}\n"
    ]
    random.shuffle(phuongan)
    return caudan, phuongan, loigiai

def sinh_cau_tln_loi_nhuan_xe_dap():
    """TLN: Chi phí và khoảng đồng biến lợi nhuận (Câu 17)"""
    caudan, loigiai, ans_val, _ = _gen_loi_nhuan_xe_dap()
    return caudan, loigiai, str(ans_val)


# --- DẠNG 2: KHAI THÁC GIẾNG DẦU (CÂU 15) ---

def _gen_gieng_dau():
    N0 = randint(15, 22)
    k = choice([7, 8, 9, 10])
    min_q0 = k * N0 + 55
    q0 = randint(min_q0, min_q0 + 110)
    
    diff = q0 - k * N0
    M = diff / k
    a = 1
    b = math.floor(M) if not M.is_integer() else int(M) - 1
    ans_val = 2 * a - b
    
    S0 = N0 * q0
    caudan = f"""Một công ty tiến hành khai thác {N0} giếng dầu trong khu vực được chỉ định. Trung bình mỗi giếng dầu chiết xuất được {q0} thùng dầu mỗi ngày. Công ty có thể khai thác nhiều hơn {N0} giếng dầu nhưng cứ khai thác thêm một giếng thì lượng dầu mỗi giếng chiết xuất được hằng ngày sẽ giảm {k} thùng. Biết số giếng dầu công ty có thể khai thác thêm để sản lượng dầu chiết xuất tăng lên nằm trên đoạn $[a; b]$. Hỏi $2a - b = ?$"""
    
    loigiai = f"""Gọi $x$ ($x \\in \\mathbb{{N}}^*$) là số giếng dầu công ty khai thác thêm.\\\\
Tổng số giếng dầu khai thác mỗi ngày là: $N(x) = {N0} + x$ (giếng).\\\\
Lượng dầu mỗi giếng chiết xuất được mỗi ngày là: $q(x) = {q0} - {k}x$ (thùng).\\\\
Tổng sản lượng dầu chiết xuất mỗi ngày là:
$$S(x) = ({N0} + x)({q0} - {k}x) = {S0} + {diff}x - {k}x^2\\quad (\\text{{thùng}}).$$
Sản lượng dầu ban đầu khi chưa khai thác thêm là $S(0) = {S0}$ thùng.\\\\
Sản lượng dầu chiết xuất tăng lên so với ban đầu khi và chỉ khi:
$$S(x) > S(0) \\Leftrightarrow {diff}x - {k}x^2 > 0 \\Leftrightarrow x({diff} - {k}x) > 0 \\Leftrightarrow 0 < x < \\dfrac{{{diff}}}{{{k}}} \\approx {M:.2f}.$$
Vì $x \\in \\mathbb{{N}}^*$ nên số giếng khai thác thêm thỏa mãn là $x \\in \\{{{a}, {a+1}, \\dots, {b}\\}} = [{a}; {b}]$.\\\\
Do đó $a = {a}$ và $b = {b}$.\\\\
Vậy $2a - b = 2\\cdot {a} - {b} = {ans_val}$."""

    distractors = [ans_val, -ans_val, ans_val - 2, 2*a + b]
    return caudan, loigiai, ans_val, distractors

def sinh_cau_mc_gieng_dau():
    """MC: Khai thác giếng dầu tối ưu sản lượng (Câu 15)"""
    caudan, loigiai, ans_val, ans_opts = _gen_gieng_dau()
    phuongan = [
        f"{{\\True ${ans_opts[0]}$}}\n",
        f"{{${ans_opts[1]}$}}\n",
        f"{{${ans_opts[2]}$}}\n",
        f"{{${ans_opts[3]}$}}\n"
    ]
    random.shuffle(phuongan)
    return caudan, phuongan, loigiai

def sinh_cau_tln_gieng_dau():
    """TLN: Khai thác giếng dầu tối ưu sản lượng (Câu 15)"""
    caudan, loigiai, ans_val, _ = _gen_gieng_dau()
    return caudan, loigiai, str(ans_val)


# --- DẠNG 3: SỐ LƯỢNG SẢN PHẨM ĐỂ LỢI NHUẬN CỰC ĐẠI ---

def _gen_loi_nhuan_cuc_dai():
    items = ["xe đạp", "máy tính bảng", "đồng hồ thông minh", "quạt điện tích điện", "máy lọc không khí"]
    item_name = choice(items)
    currency = choice(["euro", "USD"])
    
    alpha = choice([0.02, 0.015, 0.025])
    x0 = choice([45, 50, 55, 60])
    beta = round(3 * alpha * x0, 2)
    r = choice([35, 38, 40, 42])
    p = choice([110, 120, 130, 140])
    gamma = round(p - 3 * alpha * (r**2 - x0**2) + uniform(-1.5, 1.5), 1)
    d = randint(1800, 3200)
    
    A = -3 * alpha
    B = 2 * beta
    C = p - gamma
    disc = B**2 - 4 * A * C
    r1 = (-B + math.sqrt(disc)) / (2 * A)
    r2 = (-B - math.sqrt(disc)) / (2 * A)
    x_min, x_max = min(r1, r2), max(r1, r2)
    b = math.floor(x_max)
    X_max = b + randint(20, 40)
    
    poly_K = f"K(x) = {alpha}x^3 - {beta}x^2 + {gamma}x + {d}".replace('+-', '-').replace('.', ',')
    
    caudan = f"""Một nhà máy sản xuất {item_name} theo đơn giá ${p}$ {currency}. Chi phí mỗi ngày của nhà máy được cho bởi hàm số ${poly_K}$, trong đó $x$ là số lượng {item_name} sản xuất được trong ngày hôm đó. Mỗi ngày nhà máy có thể sản xuất tối đa ${X_max}$ {item_name}. Giả sử số {item_name} sản xuất được trong mỗi ngày đều được bán hết vào cuối ngày đó. Hỏi để lợi nhuận hàng ngày của nhà máy đạt giá trị lớn nhất thì nhà máy cần sản xuất bao nhiêu {item_name} trong ngày hôm đó?"""

    alpha_str = f"{alpha}".replace('.', ',')
    beta_str = f"{beta}".replace('.', ',')
    gamma_str = f"{gamma}".replace('.', ',')
    diff_p_gamma = round(p - gamma, 1)
    diff_str = f"{diff_p_gamma}".replace('.', ',')
    coef_3a = f"{round(3*alpha, 3)}".replace('.', ',')
    coef_2b = f"{round(2*beta, 2)}".replace('.', ',')

    loigiai = f"""Hàm lợi nhuận hàng ngày của nhà máy khi sản xuất và bán $x$ sản phẩm ($0 \\le x \\le {X_max}$) là:
$$G(x) = {p}x - K(x) = -{alpha_str}x^3 + {beta_str}x^2 + {diff_str}x - {d}.$$
Ta có đạo hàm:
$$G'(x) = -{coef_3a}x^2 + {coef_2b}x + {diff_str}.$$
Cho $G'(x) = 0 \\Leftrightarrow x_1 \\approx {x_min:.2f};\\ x_2 \\approx {x_max:.2f}$.\\\\
Vì hệ số $a = -{coef_3a} < 0$ nên qua điểm $x_2 \\approx {x_max:.2f}$, đạo hàm $G'(x)$ đổi dấu từ dương sang âm, do đó hàm số $G(x)$ đạt cực đại tại $x_2$.\\\\
Vì $x$ là số lượng sản phẩm nguyên dương thuộc đoạn $[0; {X_max}]$, kiểm tra các giá trị nguyên lân cận ta thấy lợi nhuận đạt giá trị lớn nhất tại $x = {b}$.\\\\
Vậy nhà máy cần sản xuất ${b}$ {item_name} mỗi ngày để lợi nhuận đạt giá trị lớn nhất."""

    distractors = [b, b - 5, b + 10, X_max]
    return caudan, loigiai, b, distractors

def sinh_cau_mc_loi_nhuan_cuc_dai():
    """MC: Số lượng sản phẩm để lợi nhuận lớn nhất"""
    caudan, loigiai, ans_val, ans_opts = _gen_loi_nhuan_cuc_dai()
    phuongan = [
        f"{{\\True ${ans_opts[0]}$}}\n",
        f"{{${ans_opts[1]}$}}\n",
        f"{{${ans_opts[2]}$}}\n",
        f"{{${ans_opts[3]}$}}\n"
    ]
    random.shuffle(phuongan)
    return caudan, phuongan, loigiai

def sinh_cau_tln_loi_nhuan_cuc_dai():
    """TLN: Số lượng sản phẩm để lợi nhuận lớn nhất"""
    caudan, loigiai, ans_val, _ = _gen_loi_nhuan_cuc_dai()
    return caudan, loigiai, str(ans_val)


# --- DẠNG 4: TỐC ĐỘ TĂNG DÂN SỐ THEO HÀM MŨ (CÂU 20) ---

def _gen_dan_so_tang_truong():
    Y0 = choice([2024, 2025, 2026])
    N0 = choice([85, 90, 95, 100, 105, 110])
    r = choice([0.011, 0.012, 0.013, 0.014, 0.015])
    v_init = N0 * r
    v0 = round(v_init * uniform(1.25, 1.55), 1)
    t = math.log(v0 / (N0 * r)) / r
    ans_year = Y0 + round(t)
    
    r_str = f'{r}'.replace('.', ',')
    v0_str = f'{v0}'.replace('.', ',')
    v_init_str = f'{v_init:.2f}'.replace('.', ',')
    
    caudan = f"""Dân số của một quốc gia sau $t$ (năm) kể từ năm {Y0} được ước tính bởi công thức $N(t) = {N0}e^{{{r_str}t}}$ ($N(t)$ được tính bằng triệu người, $0 \\le t \\le 50$). Vào năm nào tốc độ tăng dân số của quốc gia đó là {v0_str} triệu người/năm?"""
    
    loigiai = f"""Tốc độ tăng dân số của quốc gia tại thời điểm $t$ là đạo hàm của hàm số $N(t)$:
$$v(t) = N'(t) = \\left({N0}e^{{{r_str}t}}\\right)' = {N0} \\cdot {r_str} \\cdot e^{{{r_str}t}} = {v_init_str}e^{{{r_str}t}}\\quad (\\text{{triệu người/năm}}).$$
Theo giả thiết, tốc độ tăng dân số bằng {v0_str} triệu người/năm nên:
$${v_init_str}e^{{{r_str}t}} = {v0_str} \\Leftrightarrow e^{{{r_str}t}} = \\dfrac{{{v0_str}}}{{{v_init_str}}} \\Leftrightarrow {r_str}t = \\ln\\left(\\dfrac{{{v0_str}}}{{{v_init_str}}}\\right) \\Leftrightarrow t \\approx {t:.2f}\\text{{ (năm)}}.$$
Làm tròn số năm ta được $t \\approx {round(t)}$ năm.\\\\
Vậy vào khoảng năm ${Y0} + {round(t)} = {ans_year}$ thì tốc độ tăng dân số của quốc gia đó đạt {v0_str} triệu người/năm."""

    distractors = [ans_year, ans_year - 3, ans_year + 3, ans_year + 6]
    return caudan, loigiai, ans_year, distractors

def sinh_cau_mc_dan_so_tang_truong():
    """MC: Tốc độ tăng dân số theo hàm mũ (Câu 20)"""
    caudan, loigiai, ans_val, ans_opts = _gen_dan_so_tang_truong()
    phuongan = [
        f"{{\\True Năm ${ans_opts[0]}$}}\n",
        f"{{Năm ${ans_opts[1]}$}}\n",
        f"{{Năm ${ans_opts[2]}$}}\n",
        f"{{Năm ${ans_opts[3]}$}}\n"
    ]
    random.shuffle(phuongan)
    return caudan, phuongan, loigiai

def sinh_cau_tln_dan_so_tang_truong():
    """TLN: Tốc độ tăng dân số theo hàm mũ (Câu 20)"""
    caudan, loigiai, ans_val, _ = _gen_dan_so_tang_truong()
    return caudan, loigiai, str(ans_val)


# --- DẠNG 5: ĐỘ CAO TÀU LƯỢN SIÊU TỐC ĐI LÊN (CÂU 21) ---

def _gen_tau_luon_sieu_toc():
    t1 = choice([5, 6, 7, 8])
    t2_offset = choice([9, 10, 10.5, 11, 11.5])
    t2 = t1 + t2_offset
    
    A = choice([Fraction(4, 85), Fraction(3, 70), Fraction(2, 45), Fraction(3, 80)])
    c3 = Fraction(A, 3)
    sum_t = Fraction(f'{t1 + t2}')
    c2 = Fraction(A * sum_t, 2)
    prod_t = Fraction(f'{t1 * t2}')
    c1 = Fraction(A * prod_t)
    h0 = randint(15, 25)
    T_max = math.ceil(t2 + randint(2, 5))
    
    def fmt_fr(f):
        if f.denominator == 1: return str(f.numerator)
        if f.numerator < 0: return f'-\\dfrac{{{-f.numerator}}}{{{f.denominator}}}'
        return f'\\dfrac{{{f.numerator}}}{{{f.denominator}}}'
        
    poly_h = f'h(t) = -{fmt_fr(c3)}t^3 + {fmt_fr(c2)}t^2 - {fmt_fr(c1)}t + {h0}'
    
    ans_val = round(2 * t1 + t2, 1)
    ans_str = f'{ans_val}'.replace('.', ',')
    
    caudan = f"""Độ cao (tính bằng mét) của tàu lượn siêu tốc so với mặt đất sau $t$ (giây) ($0 \\le t \\le {T_max}$) từ lúc bắt đầu được cho bởi công thức ${poly_h}$. Trong khoảng thời gian $(a; b)$, tàu lượn đi lên. Tính $2a + b$ (kết quả làm tròn đến hàng phần chục)."""
    
    loigiai = f"""Vận tốc theo phương thẳng đứng của tàu lượn tại thời điểm $t$ là:
$$v_y(t) = h'(t) = -{fmt_fr(A)}t^2 + {fmt_fr(A * sum_t)}t - {fmt_fr(c1)} = -{fmt_fr(A)}\\left(t^2 - {sum_t}t + {prod_t}\\right).$$
Cho $h'(t) = 0 \\Leftrightarrow t^2 - {sum_t}t + {prod_t} = 0 \\Leftrightarrow \\left[\\begin{{aligned}} t &= {t1} \\\\ t &= {t2} \\end{{aligned}}\\right.$$
Tàu lượn đi lên khi và chỉ khi độ cao tăng theo thời gian, tức là:
$$h'(t) > 0 \\Leftrightarrow t \\in ({t1}; {t2}).$$
Do đó $a = {t1}$ và $b = {t2}$.\\\\
Vậy $2a + b = 2\\cdot {t1} + {t2} = {ans_str}$."""

    distractors = [ans_str, f'{ans_val - 2}'.replace('.', ','), f'{ans_val + 3}'.replace('.', ','), f'{round(t1 + 2*t2, 1)}'.replace('.', ',')]
    return caudan, loigiai, ans_str, distractors

def sinh_cau_mc_tau_luon_sieu_toc():
    """MC: Độ cao tàu lượn siêu tốc đi lên (Câu 21)"""
    caudan, loigiai, ans_val, ans_opts = _gen_tau_luon_sieu_toc()
    phuongan = [
        f"{{\\True ${ans_opts[0]}$}}\n",
        f"{{${ans_opts[1]}$}}\n",
        f"{{${ans_opts[2]}$}}\n",
        f"{{${ans_opts[3]}$}}\n"
    ]
    random.shuffle(phuongan)
    return caudan, phuongan, loigiai

def sinh_cau_tln_tau_luon_sieu_toc():
    """TLN: Độ cao tàu lượn siêu tốc đi lên (Câu 21)"""
    caudan, loigiai, ans_val, _ = _gen_tau_luon_sieu_toc()
    return caudan, loigiai, str(ans_val)


# --- DẠNG 6: GIÁ THÀNH SẢN PHẨM GIẢM THEO THỜI GIAN (CÂU 24) ---

def _gen_gia_thanh_giam():
    Y0 = choice([2019, 2020, 2021, 2022, 2023])
    N_nam = choice([3, 4, 5])
    T_max = 12 * N_nam
    b = choice([20, 24, 25, 28, 30, 32, 35, 40])
    while b >= T_max - 4:
        b -= 4
    A = choice([20, 25, 30, 35, 40, 50])
    B = 2 * A * b
    C = A * (b**2) + randint(30, 80) * 1000
    
    products = ["sản phẩm", "chiếc xe đạp điện", "chiếc tivi thông minh", "chiếc máy tính xách tay", "chiếc tủ lạnh", "bộ máy lọc nước"]
    prod_name = choice(products)
    
    caudan = f"""Người ta thấy rằng trong vòng {N_nam} năm tính từ đầu năm {Y0}, giá thành $P$ của một {prod_name} vào tháng thứ $t$ thay đổi theo công thức $P(t) = {A}t^2 - {B}t + {C}$ (đồng) với $0 \\le t \\le {T_max}$. Giá thành $P$ của sản phẩm giảm khi $t$ trong khoảng $(a; b)$. Tính $T = b - a$."""
    
    der_2A = 2 * A
    loigiai = f"""Ta có đạo hàm của hàm số giá thành $P(t)$ là:
$$P'(t) = {der_2A}t - {B} = {der_2A}(t - {b}).$$
Giá thành $P$ của sản phẩm giảm khi và chỉ khi $P'(t) < 0$:
$${der_2A}t - {B} < 0 \\Leftrightarrow t < \\dfrac{{{B}}}{{{der_2A}}} = {b}.$$
Kết hợp với điều kiện bài toán $0 \\le t \\le {T_max}$, ta có giá thành sản phẩm giảm khi $t \\in (0; {b})$.\\\\
Do đó $a = 0$ và $b = {b}$.\\\\
Vậy $T = b - a = {b} - 0 = {b}$."""

    ans_val = b
    distractors = [b, b - 4, b + 6, T_max - b]
    d_set = {b}
    cleaned_dist = [b]
    for d in distractors[1:]:
        if d not in d_set and d > 0:
            d_set.add(d)
            cleaned_dist.append(d)
    offset = 2
    while len(cleaned_dist) < 4:
        cand = b + offset
        if cand not in d_set and cand > 0:
            d_set.add(cand)
            cleaned_dist.append(cand)
        offset = -offset if offset > 0 else -offset + 2

    return caudan, loigiai, ans_val, cleaned_dist

def sinh_cau_mc_gia_thanh_giam():
    """MC: Giá thành sản phẩm giảm theo thời gian (Câu 24)"""
    caudan, loigiai, ans_val, ans_opts = _gen_gia_thanh_giam()
    phuongan = [
        f"{{\\True ${ans_opts[0]}$}}\n",
        f"{{${ans_opts[1]}$}}\n",
        f"{{${ans_opts[2]}$}}\n",
        f"{{${ans_opts[3]}$}}\n"
    ]
    random.shuffle(phuongan)
    return caudan, phuongan, loigiai

def sinh_cau_tln_gia_thanh_giam():
    """TLN: Giá thành sản phẩm giảm theo thời gian (Câu 24)"""
    caudan, loigiai, ans_val, _ = _gen_gia_thanh_giam()
    return caudan, loigiai, str(ans_val)


# --- DẠNG 7: KHOẢNG THỜI GIAN SỐ LƯỢNG VI KHUẨN TĂNG (CÂU 22) ---

def _gen_vi_khuan_tang():
    t1 = choice([8, 10, 12, 14])
    t2 = t1 + choice([8, 10, 12, 14])
    
    # 70% trường hợp khoảng sau dài hơn, 30% khoảng trước dài hơn
    c2_longer = choice([True, True, False])
    if c2_longer:
        T_max = t2 + t1 + choice([5, 8, 10, 12])
    else:
        T_max = t2 + max(2, t1 - choice([3, 4, 5]))
        
    alpha = choice([40, 60, 80, 100])
    beta = (3 * alpha * (t1 + t2)) // 2
    gamma = 3 * alpha * t1 * t2
    N0 = choice([50000, 80000, 100000, 120000, 150000])
    
    len1 = t1 - 0
    len2 = T_max - t2
    if len2 > len1:
        a, b_int = t2, T_max
        so_sanh = f"Vì khoảng $({t2}; {T_max})$ có độ dài là ${T_max} - {t2} = {len2}$ lớn hơn độ dài của khoảng $(0; {t1})$ (độ dài là ${t1}$), nên khoảng thời gian dài nhất để số lượng vi khuẩn tăng là $({t2}; {T_max})$."
    else:
        a, b_int = 0, t1
        so_sanh = f"Vì khoảng $(0; {t1})$ có độ dài là ${t1} - 0 = {len1}$ lớn hơn độ dài của khoảng $({t2}; {T_max})$ (độ dài là ${T_max} - {t2} = {len2}$), nên khoảng thời gian dài nhất để số lượng vi khuẩn tăng là $(0; {t1})$."
        
    ans_val = a - b_int
    
    caudan = f"""Trong một thí nghiệm y học, người ta cấy ${N0}$ con vi khuẩn vào môi trường dinh dưỡng. Bằng thực nghiệm người ta xác định được số lượng vi khuẩn $N$ thay đổi theo thời gian bằng công thức $N(t) = {alpha}t^3 - {beta}t^2 + {gamma}t + {N0}$ (thời gian $t$ tính bằng giây, $0 \\le t \\le {T_max}$). Gọi $(a; b)$ là khoảng thời gian dài nhất để vi khuẩn tăng. Hiệu $a - b$ bằng bao nhiêu?"""

    coef_3a = 3 * alpha
    coef_2b = 2 * beta
    sum_t = t1 + t2
    prod_t = t1 * t2
    loigiai = f"""Tốc độ biến thiên số lượng vi khuẩn tại thời điểm $t$ là đạo hàm:
$$N'(t) = {coef_3a}t^2 - {coef_2b}t + {gamma} = {coef_3a}\\left(t^2 - {sum_t}t + {prod_t}\\right) = {coef_3a}(t - {t1})(t - {t2}).$$
Cho $N'(t) = 0 \\Leftrightarrow \\left[\\begin{{aligned}} t &= {t1} \\\\ t &= {t2} \\end{{aligned}}\\right.$$
Số lượng vi khuẩn tăng khi và chỉ khi $N'(t) > 0$.\\\\
Vì hệ số $a = {coef_3a} > 0$ nên $N'(t) > 0 \\Leftrightarrow t \\in (-\\infty; {t1}) \\cup ({t2}; +\\infty)$.\\\\
Kết hợp với điều kiện $0 \\le t \\le {T_max}$, ta có hai khoảng thời gian để vi khuẩn tăng là $(0; {t1})$ và $({t2}; {T_max})$.\\\\
{so_sanh}\\\\
Do đó $a = {a}$ và $b = {b_int}$.\\\\
Vậy hiệu $a - b = {a} - {b_int} = {ans_val}$."""

    distractors = [ans_val, -ans_val, ans_val - 5, ans_val + 5]
    d_set = {ans_val}
    cleaned_dist = [ans_val]
    for d in distractors[1:]:
        if d not in d_set:
            d_set.add(d)
            cleaned_dist.append(d)
    offset = 3
    while len(cleaned_dist) < 4:
        cand = ans_val + offset
        if cand not in d_set:
            d_set.add(cand)
            cleaned_dist.append(cand)
        offset = -offset if offset > 0 else -offset + 3

    return caudan, loigiai, ans_val, cleaned_dist

def sinh_cau_mc_vi_khuan_tang():
    """MC: Khoảng thời gian số lượng vi khuẩn tăng (Câu 22)"""
    caudan, loigiai, ans_val, ans_opts = _gen_vi_khuan_tang()
    phuongan = [
        f"{{\\True ${ans_opts[0]}$}}\n",
        f"{{${ans_opts[1]}$}}\n",
        f"{{${ans_opts[2]}$}}\n",
        f"{{${ans_opts[3]}$}}\n"
    ]
    random.shuffle(phuongan)
    return caudan, phuongan, loigiai

def sinh_cau_tln_vi_khuan_tang():
    """TLN: Khoảng thời gian số lượng vi khuẩn tăng (Câu 22)"""
    caudan, loigiai, ans_val, _ = _gen_vi_khuan_tang()
    return caudan, loigiai, str(ans_val)


# ==============================================================================
# DẠNG MỚI: Mô hình hàm bậc ba lát cắt địa hình: Chiều cao ngọn núi và độ sâu hồ nước
# ==============================================================================
def _gen_lat_cat_vung_dat_nui_ho():
    """Sinh dữ liệu bài toán thực tế lát cắt địa hình hồ nước và ngọn núi bằng hàm bậc ba"""
    scenarios = [
        (2, 3.5, 450),
        (2, 4.0, 500),
        (3, 4.5, 600),
        (1.5, 3.5, 360),
        (2.5, 4.0, 480),
        (3.0, 5.0, 550),
        (2, 3.0, 400),
        (2.5, 3.5, 420),
    ]
    d1, w, h = choice(scenarios)
    xN = d1 + w

    sum_r = d1 + xN
    prod_r = d1 * xN
    delta_p = sum_r**2 - 3 * prod_r
    sqrt_delta = math.sqrt(delta_p)
    x1 = (sum_r - sqrt_delta) / 3.0
    x2 = (sum_r + sqrt_delta) / 3.0

    h_km = h / 1000.0
    denom1 = x1 * (x1 - d1) * (x1 - xN)
    k_val = -h_km / denom1

    val2 = x2 * (x2 - d1) * (x2 - xN)
    H_km = k_val * val2
    H_m = H_km * 1000.0
    ans_val = round(H_m)

    # Định dạng chuỗi số cho LaTeX
    d1_tex = f"{d1}".replace('.', ',') if isinstance(d1, float) and not d1.is_integer() else f"{int(d1)}"
    w_tex = f"{w}".replace('.', ',') if not float(w).is_integer() else f"{int(w)}"
    xN_tex = f"{xN}".replace('.', ',') if not float(xN).is_integer() else f"{int(xN)}"
    h_km_tex = f"{h_km:.3f}".rstrip('0').rstrip('.').replace('.', ',')

    # TikZ scaling
    xscale = round(6.5 / (xN + 0.5), 2)
    yscale = round(1.3 / max(H_km, 1.0), 2)
    k_str = f"{k_val:.6f}"
    d_lake_y = round(h_km + 0.3, 2)
    h_mountain_y = round(H_km + 0.4, 2)
    x_max = round(xN + 0.7, 2)
    x_end = round(xN + 0.3, 2)
    lake_lbl_x = round(d1 / 2.0, 2)
    mtn_lbl_x = round((d1 + xN) / 2.0, 2)

    tikz_code = r"""\begin{center}
\begin{tikzpicture}[>=stealth, xscale=__XSCALE__, yscale=__YSCALE__]
  \begin{scope}
    \clip (0,0) -- plot[domain=0:__D1__, samples=60] (\x, {__K__*\x*(\x-__D1__)*(\x-__XN__)}) -- (__D1__,0) -- cycle;
    \fill[pattern=horizontal lines, pattern color=blue!50] (0,-__DLAKE_Y__) rectangle (__D1__,0.3);
  \end{scope}
  \begin{scope}
    \clip (__D1__,0) -- plot[domain=__D1__:__XN__, samples=60] (\x, {__K__*\x*(\x-__D1__)*(\x-__XN__)}) -- (__XN__,0) -- cycle;
    \fill[pattern=vertical lines, pattern color=brown!50] (__D1__,-0.3) rectangle (__XN__,__HMTN_Y__);
  \end{scope}
  \draw[->] (-0.5,0) -- (__XMAX__,0) node[below] {$x$};
  \draw[->] (0,-__DLAKE_Y__) -- (0,__HMTN_Y__) node[left] {$y$};
  \draw[thick, blue!80!black] plot[domain=-0.2:__XEND__, samples=100] (\x, {__K__*\x*(\x-__D1__)*(\x-__XN__)});
  \draw[dashed] (__X1__,0) -- (__X1__,-__HKM__) -- (0,-__HKM__) node[left] {$-__HKM_TEX__$};
  \node[below left] at (0,0) {$O$};
  \node[above] at (__D1__,0) {$M$};
  \node[above] at (__XN__,0) {$N$};
  \node[blue!80!black] at (__LAKE_LBL_X__,-__LAKE_LBL_Y__) {\small Hồ nước};
  \node[brown!60!black] at (__MTN_LBL_X__,__MTN_LBL_Y__) {\small Núi};
\end{tikzpicture}
\end{center}"""

    tikz_code = (tikz_code
        .replace("__XSCALE__", str(xscale))
        .replace("__YSCALE__", str(yscale))
        .replace("__D1__", str(d1))
        .replace("__XN__", str(xN))
        .replace("__K__", k_str)
        .replace("__DLAKE_Y__", str(d_lake_y))
        .replace("__HMTN_Y__", str(h_mountain_y))
        .replace("__XMAX__", str(x_max))
        .replace("__XEND__", str(x_end))
        .replace("__X1__", f"{x1:.4f}")
        .replace("__HKM__", f"{h_km:.4f}")
        .replace("__HKM_TEX__", h_km_tex)
        .replace("__LAKE_LBL_X__", str(lake_lbl_x))
        .replace("__LAKE_LBL_Y__", str(round(h_km + 0.15, 2)))
        .replace("__MTN_LBL_X__", str(mtn_lbl_x))
        .replace("__MTN_LBL_Y__", str(round(H_km - 0.2, 2)))
    )

    caudan_base = f"Lát cắt của một vùng đất được mô hình hóa bởi hàm bậc ba $y = f(x)$ có đồ thị như hình vẽ bên dưới (đơn vị trên các trục là $\\text{{km}}$). Biết khoảng cách $OM = {d1_tex}\\,\\text{{km}}$; độ rộng của núi $MN = {w_tex}\\,\\text{{km}}$. Độ sâu của hồ nước là ${h}\\,\\text{{m}}$."

    caudan = caudan_base + "\n" + tikz_code

    # Lời giải chi tiết
    sum_r_str = f"{sum_r:.2f}".rstrip('0').rstrip('.').replace('.', ',') if not float(sum_r).is_integer() else f"{int(sum_r)}"
    two_sum_r_str = f"{2*sum_r:.2f}".rstrip('0').rstrip('.').replace('.', ',') if not float(2*sum_r).is_integer() else f"{int(2*sum_r)}"
    prod_r_tex = f"{prod_r:.2f}".rstrip('0').rstrip('.').replace('.', ',') if not float(prod_r).is_integer() else f"{int(prod_r)}"
    x1_round_tex = f"{x1:.4f}".replace('.', ',')
    x2_round_tex = f"{x2:.4f}".replace('.', ',')
    k_round_tex = f"{k_val:.6f}".replace('.', ',')
    H_km_tex = f"{H_km:.4f}".replace('.', ',')

    loigiai = f"""Chọn hệ trục tọa độ $Oxy$ như hình vẽ (gốc tọa độ tại $O$, đơn vị trên các trục là $\\text{{km}}$).
\\begin{{itemize}}
  \\item Đồ thị hàm bậc ba $y = f(x)$ đi qua gốc tọa độ $O(0;0)$, điểm $M({d1_tex};0)$ và điểm $N({xN_tex};0)$ (với $x_N = OM + MN = {d1_tex} + {w_tex} = {xN_tex}$).
  Do đó hàm số có dạng:
  \\[
  f(x) = k \\cdot x(x - {d1_tex})(x - {xN_tex}) = k\\left[x^3 - {sum_r_str}x^2 + {prod_r_tex}x\\right] \\quad (k < 0).
  \\]
  \\item Đạo hàm của hàm số:
  \\[
  f'(x) = k\\left[3x^2 - {two_sum_r_str}x + {prod_r_tex}\\right].
  \\]
  Cho $f'(x) = 0 \\iff 3x^2 - {two_sum_r_str}x + {prod_r_tex} = 0$. Phương trình có hai nghiệm:
  \\[
  x_1 \\approx {x1_round_tex}\\text{{ (hoành độ cực tiểu - đáy hồ)}}, \\quad x_2 \\approx {x2_round_tex}\\text{{ (hoành độ cực đại - đỉnh núi)}}.
  \\]
  \\item Độ sâu của hồ nước là ${h}\\,\\text{{m}} = {h_km_tex}\\,\\text{{km}}$, suy ra tung độ tại đáy hồ là:
  \\[
  f(x_1) = -{h_km_tex}\\,\\text{{km}} \\implies k = \\dfrac{{-{h_km_tex}}}{{x_1(x_1 - {d1_tex})(x_1 - {xN_tex})}} \\approx {k_round_tex}.
  \\]
  \\item Chiều cao của ngọn núi là tung độ cực đại tại $x_2$:
  \\[
  H = f(x_2) = k \\cdot x_2(x_2 - {d1_tex})(x_2 - {xN_tex}) \\approx {H_km_tex}\\,\\text{{km}} = {H_m:.1f}\\,\\text{{m}} \\approx {ans_val}\\,\\text{{m}}.
  \\]
\\end{{itemize}}
Vậy chiều cao của ngọn núi xấp xỉ ${ans_val}\\,\\text{{m}}$."""

    # Chuẩn bị 4 phương án cho MC
    d_set = {ans_val}
    opts = [ans_val]
    for delta_opt in [choice([50, 60, 80]), choice([-50, -60, -80]), choice([120, 150, 200])]:
        cand = ans_val + delta_opt
        if cand > 0 and cand not in d_set:
            d_set.add(cand)
            opts.append(cand)
    offset = 40
    while len(opts) < 4:
        cand = ans_val + offset
        if cand > 0 and cand not in d_set:
            d_set.add(cand)
            opts.append(cand)
        offset = -offset if offset > 0 else -offset + 30

    details = {
        'd1': d1, 'w': w, 'h': h, 'xN': xN, 'x1': x1, 'x2': x2,
        'k_val': k_val, 'H_km': H_km, 'H_m': H_m, 'ans_val': ans_val,
        'd1_tex': d1_tex, 'w_tex': w_tex, 'xN_tex': xN_tex,
        'h_km_tex': h_km_tex, 'caudan_base': caudan_base, 'tikz_code': tikz_code
    }

    return caudan, loigiai, ans_val, opts, details


def sinh_cau_tln_lat_cat_vung_dat_nui_ho():
    """TLN: Chiều cao ngọn núi và độ sâu hồ nước (Mô hình hàm bậc ba lát cắt địa hình)"""
    caudan, loigiai, ans_val, _, _ = _gen_lat_cat_vung_dat_nui_ho()
    prompt = caudan + "\nChiều cao của ngọn núi là bao nhiêu mét? (Không làm tròn kết quả trung gian, kết quả làm tròn đến hàng đơn vị của mét)"
    return prompt, loigiai, str(ans_val)


def sinh_cau_mc_lat_cat_vung_dat_nui_ho():
    """MC: Chiều cao ngọn núi và độ sâu hồ nước (Mô hình hàm bậc ba lát cắt địa hình)"""
    caudan, loigiai, ans_val, opts, _ = _gen_lat_cat_vung_dat_nui_ho()
    prompt = caudan + "\nChiều cao của ngọn núi gần nhất với giá trị nào sau đây?"
    phuongan = [
        f"{{\\True ${opts[0]}\\,\\text{{m}}$}}\n",
        f"{{${opts[1]}\\,\\text{{m}}$}}\n",
        f"{{${opts[2]}\\,\\text{{m}}$}}\n",
        f"{{${opts[3]}\\,\\text{{m}}$}}\n"
    ]
    random.shuffle(phuongan)
    return prompt, phuongan, loigiai


def sinh_cau_ds_lat_cat_vung_dat_nui_ho():
    """Đúng/Sai: Mô hình hàm bậc ba lát cắt địa hình (Chiều cao ngọn núi và độ sâu hồ nước)"""
    caudan, _, ans_val, _, d = _gen_lat_cat_vung_dat_nui_ho()
    prompt = f"Lát cắt của một vùng đất được mô hình hóa bởi hàm bậc ba $y = f(x) = ax^3 + bx^2 + cx + d$ ($a \\ne 0$) có đồ thị như hình vẽ bên dưới (đơn vị trên các trục là $\\text{{km}}$). Biết khoảng cách $OM = {d['d1_tex']}\\,\\text{{km}}$; độ rộng của núi $MN = {d['w_tex']}\\,\\text{{km}}$. Độ sâu của hồ nước là ${d['h']}\\,\\text{{m}}$." + "\n" + d['tikz_code']

    y_a_dung = choice([True, False])
    y_b_dung = choice([True, False])
    y_c_dung = choice([True, False])
    y_d_dung = choice([True, False])

    # Ý a: Giao điểm trục hoành
    if y_a_dung:
        claim_a = f"Đồ thị hàm số $y = f(x)$ cắt trục hoành tại ba điểm phân biệt có hoành độ lần lượt là $x = 0$, $x = {d['d1_tex']}$ và $x = {d['xN_tex']}$."
        lg_a = f"Đồ thị đi qua gốc tọa độ $O(0;0)$, điểm $M({d['d1_tex']};0)$ và $N({d['xN_tex']};0)$ (do $x_N = OM + MN = {d['d1_tex']} + {d['w_tex']} = {d['xN_tex']}$). Mệnh đề này **ĐÚNG**."
    else:
        claim_a = f"Đồ thị hàm số $y = f(x)$ cắt trục hoành tại ba điểm phân biệt có hoành độ lần lượt là $x = 0$, $x = {d['d1_tex']}$ và $x = {d['w_tex']}$."
        lg_a = f"Độ rộng của núi là $MN = {d['w_tex']}\\,\\text{{km}} \\implies x_N = OM + MN = {d['d1_tex']} + {d['w_tex']} = {d['xN_tex']}\\,\\text{{km}} \\ne {d['w_tex']}\\,\\text{{km}}$. Do đó ba giao điểm với trục hoành là $x = 0$, $x = {d['d1_tex']}$, $x = {d['xN_tex']}$. Mệnh đề này **SAI**."

    # Ý b: Hoành độ đáy hồ
    x1_approx = round(d['x1'], 2)
    x1_approx_tex = f"{x1_approx}".replace('.', ',')
    if y_b_dung:
        claim_b = f"Đáy hồ nước nằm tại điểm cực tiểu của hàm số có hoành độ $x_1 \\approx {x1_approx_tex}\\,\\text{{km}}$."
        lg_b = f"Đạo hàm $f'(x) = 0$ có nghiệm cực tiểu nằm trong khoảng $(0; {d['d1_tex']})$ là $x_1 \\approx {d['x1']:.4f}\\,\\text{{km}} \\approx {x1_approx_tex}\\,\\text{{km}}$. Mệnh đề này **ĐÚNG**."
    else:
        fake_x1 = round(d['x1'] + choice([0.35, -0.35, 0.4]), 2)
        fake_x1_tex = f"{fake_x1}".replace('.', ',')
        claim_b = f"Đáy hồ nước nằm tại điểm cực tiểu của hàm số có hoành độ $x_1 \\approx {fake_x1_tex}\\,\\text{{km}}$."
        lg_b = f"Đạo hàm $f'(x) = 0$ có nghiệm cực tiểu nằm trong khoảng $(0; {d['d1_tex']})$ là $x_1 \\approx {d['x1']:.4f}\\,\\text{{km}} \\ne {fake_x1_tex}\\,\\text{{km}}$. Mệnh đề này **SAI**."

    # Ý c: Hệ số a
    k_approx = round(d['k_val'], 4)
    k_approx_tex = f"{k_approx}".replace('.', ',')
    if y_c_dung:
        claim_c = f"Hệ số $a$ của hàm số bậc ba thỏa mãn $a < 0$ và xấp xỉ ${k_approx_tex}$."
        lg_c = f"Tại đáy hồ $f(x_1) = -{d['h_km_tex']}\\,\\text{{km}} \\implies a = k = \\dfrac{{-{d['h_km_tex']}}}{{x_1(x_1 - {d['d1_tex']})(x_1 - {d['xN_tex']})}} \\approx {k_approx_tex} < 0$. Mệnh đề này **ĐÚNG**."
    else:
        pos_k_tex = f"{-k_approx}".replace('.', ',')
        claim_c = f"Hệ số $a$ của hàm số bậc ba thỏa mãn $a > 0$ và xấp xỉ ${pos_k_tex}$."
        lg_c = f"Từ đồ thị ta thấy khi $x \\to +\\infty$ thì $f(x) \\to -\\infty$, do đó hệ số bậc ba phải thỏa mãn $a < 0$ (cụ thể $a \\approx {k_approx_tex}$). Mệnh đề này **SAI**."

    # Ý d: Chiều cao ngọn núi
    if y_d_dung:
        claim_d = f"Chiều cao của ngọn núi (làm tròn đến hàng đơn vị của mét) bằng ${ans_val}\\,\\text{{m}}$."
        lg_d = f"Chiều cao ngọn núi là $H = f(x_2) \\approx {d['H_km']:.4f}\\,\\text{{km}} \\approx {ans_val}\\,\\text{{m}}$. Mệnh đề này **ĐÚNG**."
    else:
        fake_ans = ans_val + choice([100, -100, 150, -150])
        claim_d = f"Chiều cao của ngọn núi (làm tròn đến hàng đơn vị của mét) bằng ${fake_ans}\\,\\text{{m}}$."
        lg_d = f"Chiều cao ngọn núi là $H = f(x_2) \\approx {d['H_km']:.4f}\\,\\text{{km}} \\approx {ans_val}\\,\\text{{m}} \\ne {fake_ans}\\,\\text{{m}}$. Mệnh đề này **SAI**."

    choice_a = f"{{\\True {claim_a}}}" if y_a_dung else f"{{{claim_a}}}"
    choice_b = f"{{\\True {claim_b}}}" if y_b_dung else f"{{{claim_b}}}"
    choice_c = f"{{\\True {claim_c}}}" if y_c_dung else f"{{{claim_c}}}"
    choice_d = f"{{\\True {claim_d}}}" if y_d_dung else f"{{{claim_d}}}"

    choices = [choice_a, choice_b, choice_c, choice_d]
    loigiai = f"""\\begin{{itemchoice}}
\\itemch {lg_a}
\\itemch {lg_b}
\\itemch {lg_c}
\\itemch {lg_d}
\\end{{itemchoice}}"""

    return prompt, choices, loigiai


# Aliases for CuoiChuong1_TF
CuoiChuong1_TF_Cau19 = sinh_cau_dung_sai_bac_ba_hinh_hoc
CuoiChuong1_TF_Cau20 = sinh_cau_dung_sai_bac_2_1_cuc_tri



