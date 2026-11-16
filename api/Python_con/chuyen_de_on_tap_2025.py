# -*- coding: utf-8 -*-
"""
Module Chuyên đề ôn tập 2025 - Chủ đề Nguyên hàm & Hàm số
Dành cho đề ôn tập theo định dạng GDPT 2018 (Trắc nghiệm nhiều lựa chọn, Đúng/Sai, Trả lời ngắn).
Các tham số được ngẫu nhiên hóa 100%, tự động tính toán lời giải và đáp án tương ứng.
"""

import math
import random
from fractions import Fraction


def clean_option(s):
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
    choices = []
    loi_giai_parts = []
    labels = ["a)", "b)", "c)", "d)"]
    num_items = len(items)
    if num_items == 4:
        # Guarantee realistic mix of True and False
        pattern = random.choice([
            [True, False, True, False],
            [False, True, False, True],
            [True, True, False, False],
            [False, False, True, True],
            [True, False, False, True],
            [False, True, True, False],
            [True, True, True, False],
            [False, True, True, True],
            [True, False, True, True],
            [True, True, False, True],
            [False, False, False, True],
            [True, False, False, False],
        ])
    else:
        pattern = [random.choice([True, False]) for _ in range(num_items)]
        if not any(pattern):
            pattern[random.randint(0, num_items - 1)] = True

    for i, item in enumerate(items):
        stmt_t, stmt_f, exp_t, exp_f = item
        is_true = pattern[i]
        lbl = labels[i]
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


def fmt_poly_deg3(a, b, c, d):
    """Định dạng đa thức bậc 3 đẹp: ax^3 + bx^2 + cx + d"""
    terms = []
    # ax^3
    if a == 1:
        terms.append("x^3")
    elif a == -1:
        terms.append("-x^3")
    elif a != 0:
        terms.append(f"{a}x^3")
    
    # bx^2
    if b == 1:
        terms.append("+ x^2" if terms else "x^2")
    elif b == -1:
        terms.append("- x^2")
    elif b > 0:
        terms.append(f"+ {b}x^2" if terms else f"{b}x^2")
    elif b < 0:
        terms.append(f"- {-b}x^2")
        
    # cx
    if c == 1:
        terms.append("+ x" if terms else "x")
    elif c == -1:
        terms.append("- x")
    elif c > 0:
        terms.append(f"+ {c}x" if terms else f"{c}x")
    elif c < 0:
        terms.append(f"- {-c}x")
        
    # d
    if d > 0:
        terms.append(f"+ {d}" if terms else f"{d}")
    elif d < 0:
        terms.append(f"- {-d}")
    elif not terms:
        terms.append("0")
        
    return " ".join(terms)


def fmt_poly_deg2(a, b, c):
    """Định dạng đa thức bậc 2 đẹp: ax^2 + bx + c"""
    terms = []
    # ax^2
    if a == 1:
        terms.append("x^2")
    elif a == -1:
        terms.append("-x^2")
    elif a != 0:
        terms.append(f"{a}x^2")
        
    # bx
    if b == 1:
        terms.append("+ x" if terms else "x")
    elif b == -1:
        terms.append("- x")
    elif b > 0:
        terms.append(f"+ {b}x" if terms else f"{b}x")
    elif b < 0:
        terms.append(f"- {-b}x")
        
    # c
    if c > 0:
        terms.append(f"+ {c}" if terms else f"{c}")
    elif c < 0:
        terms.append(f"- {-c}")
    elif not terms:
        terms.append("0")
        
    return " ".join(terms)


# ==============================================================================
# PHẦN 1: CHỦ ĐỀ NGUYÊN HÀM - TRẮC NGHIỆM LỰA CHỌN (MC)
# ==============================================================================

def NguyenHam_MC_DoThiParabol():
    """Câu 8 MC: Đồ thị đạo hàm f'(x) là parabol, tìm f(x) biết f(0)=c"""
    x0 = random.choice([1, 2])
    k = random.choice([1, 2, 3])
    # Parabol f'(x) = k * x * (x - 2*x0) = k*x^2 - 2*k*x0*x
    # Đỉnh tại x = x0, y = -k * x0^2
    y_dinh = -k * (x0 ** 2)
    x_right = 2 * x0
    c = random.choice([-3, -2, -1, 1, 2, 3])
    
    # f(x) = \int (k*x^2 - 2*k*x0*x) dx = (k/3)x^3 - k*x0*x^2 + C
    # f(0) = c => C = c
    
    caudan = fr'''Cho hàm số $y=f(x)$ liên tục trên $\mathbb{{R}}$ và có đồ thị đạo hàm $y=f'(x)$ là đường parabol $(P)$ có đỉnh $I({x0}; {y_dinh})$ và đi qua gốc tọa độ $O(0;0)$ như hình vẽ dưới đây. Biết $f(0) = {c}$. Mệnh đề nào sau đây đúng?
\begin{{center}}
\begin{{tikzpicture}}[scale=0.9,>=stealth]
\draw[->] (-1,0) -- ({x_right + 1.2},0) node[below] {{$x$}};
\draw[->] (0,{y_dinh - 1}) -- (0, 2) node[left] {{$y$}};
\fill (0,0) circle (1.5pt) node[above left] {{$O$}};
\draw[dashed] ({x0},0) node[above] {{${x0}$}} -- ({x0},{y_dinh}) -- (0,{y_dinh}) node[left] {{${y_dinh}$}};
\fill ({x0},{y_dinh}) circle (1.5pt) node[below] {{$I$}};
\fill ({x_right},0) circle (1.5pt) node[above right] {{${x_right}$}};
\draw[thick,domain=-0.4:{x_right + 0.4},samples=100] plot (\x, {{{k}*(\x)*(\x - {x_right})}});
\node at ({x_right + 0.5},1.2) {{$y=f'(x)$}};
\end{{tikzpicture}}
\end{{center}}'''

    if k == 3:
        # f(x) = x^3 - 3*x0*x^2 + c
        f_correct = f"$f(x) = {fmt_poly_deg3(1, -3*x0, 0, c)}$"
        f_wrong1 = f"$f(x) = {fmt_poly_deg3(1, 3*x0, 0, c)}$"
        f_wrong2 = f"$f(x) = {fmt_poly_deg3(3, -6*x0, 0, c)}$"
        f_wrong3 = f"$f(x) = {fmt_poly_deg3(1, -3*x0, 0, -c)}$"
    else:
        # k = 1 or 2
        frac_a = f"\\dfrac{{{k}}}{{3}}"
        b_val = -k * x0
        b_str = f"- {abs(b_val)}x^2" if b_val < 0 else f"+ {b_val}x^2"
        c_str = f"+ {c}" if c > 0 else f"- {abs(c)}"
        
        f_correct = f"$f(x) = {frac_a}x^3 {b_str} {c_str}$"
        f_wrong1 = f"$f(x) = {k}x^3 {b_str} {c_str}$"
        f_wrong2 = f"$f(x) = {frac_a}x^3 + {abs(b_val)}x^2 {c_str}$"
        f_wrong3 = f"$f(x) = {frac_a}x^3 {b_str} " + (f"+ {-c}" if -c > 0 else f"- {c}") + "$"

    choices = shuffle_choices(f_correct, [f_wrong1, f_wrong2, f_wrong3])
    
    loi_giai = fr'''Parabol $(P): y = f'(x) = Ax^2 + Bx + C_0$.
Vì $(P)$ đi qua $O(0;0)$ nên $C_0 = 0$.
$(P)$ có đỉnh $I({x0}; {y_dinh})$ và cắt trục hoành tại $x=0, x={x_right}$ nên phương trình $f'(x)$ có dạng:
\[ f'(x) = {k}x(x - {x_right}) = {k}x^2 - {2*k*x0}x. \]
Ta tìm nguyên hàm của $f'(x)$:
\[ f(x) = \int f'(x)\,dx = \int \left({k}x^2 - {2*k*x0}x\right) dx = {r"\dfrac{" + str(k) + r"}{3}" if k!=3 else ""}x^3 - {k*x0}x^2 + C. \]
Theo giả thiết $f(0) = {c} \implies C = {c}$.
Vậy công thức của hàm số là {f_correct}.'''

    return caudan, choices, loi_giai


def NguyenHam_MC_DoiBienSo():
    """Câu 9 MC: Đổi biến số u = ax^2 + b, xác định dạng tích phân/nguyên hàm theo u"""
    a = random.choice([1, 2, 3])
    b = random.choice([1, 2, 3, 4, 5])
    n = random.choice([3, 4, 5, 6, 7])
    
    u_expr = f"{a}x^2 + {b}" if a > 1 else f"x^2 + {b}"
    integrand = f"x({u_expr})^{{{n}}}"
    
    caudan = fr'''Cho nguyên hàm $I = \int {integrand}\,dx$. Nếu đặt $u = {u_expr}$ thì khẳng định nào sau đây là đúng?'''
    
    coeff = 2 * a
    correct_str = fr"$I = \dfrac{{1}}{{{coeff}}} \int u^{{{n}}}\,du$"
    wrong1 = fr"$I = {coeff} \int u^{{{n}}}\,du$"
    wrong2 = fr"$I = \dfrac{{1}}{{{a}}} \int u^{{{n}}}\,du$"
    wrong3 = fr"$I = \int u^{{{n}}}\,du$"
    
    choices = shuffle_choices(correct_str, [wrong1, wrong2, wrong3])
    loi_giai = fr'''Đặt $u = {u_expr} \implies du = {coeff}x\,dx \implies x\,dx = \dfrac{{1}}{{{coeff}}}\,du$.
Thay vào nguyên hàm $I$, ta được:
\[ I = \int ({u_expr})^{{{n}}} \cdot (x\,dx) = \int u^{{{n}}} \cdot \dfrac{{1}}{{{coeff}}}\,du = \dfrac{{1}}{{{coeff}}} \int u^{{{n}}}\,du. \]'''
    
    return caudan, choices, loi_giai


def NguyenHam_MC_TungPhan():
    """Câu 10 MC: Họ tất cả các nguyên hàm của (ax + b)e^x"""
    a = random.choice([1, 2, 3])
    b = random.choice([-5, -3, -1, 1, 3, 5])
    
    # f(x) = (ax + b) e^x
    # \int (ax+b) e^x dx = (ax+b)e^x - \int a e^x dx = (ax + b - a)e^x + C
    k = b - a
    
    linear_orig = f"{a}x + {b}" if b > 0 else f"{a}x - {abs(b)}"
    if a == 1:
        linear_orig = f"x + {b}" if b > 0 else f"x - {abs(b)}"
        
    def fmt_res(val_a, val_k):
        a_part = f"{val_a}x" if val_a != 1 else "x"
        if val_k > 0:
            return f"({a_part} + {val_k})e^x + C"
        elif val_k < 0:
            return f"({a_part} - {abs(val_k)})e^x + C"
        else:
            return f"{a_part}e^x + C"
            
    correct_str = f"${fmt_res(a, k)}$"
    dists = []
    for cand_k in [b + a, b, -k, k + 1, k - 1, b - 2*a]:
        cand_str = f"${fmt_res(a, cand_k)}$"
        if cand_str != correct_str and cand_str not in dists:
            dists.append(cand_str)
    
    caudan = fr'''Họ tất cả các nguyên hàm của hàm số $f(x) = ({linear_orig})e^x$ là'''
    choices = shuffle_choices(correct_str, dists[:3])
    
    loi_giai = fr'''Sử dụng phương pháp nguyên hàm từng phần:
Đặt $\begin{{cases}} u = {linear_orig} \\ dv = e^x\,dx \end{{cases}} \implies \begin{{cases}} du = {a}\,dx \\ v = e^x \end{{cases}}$.
Theo công thức nguyên hàm từng phần:
\[ \int ({linear_orig})e^x\,dx = ({linear_orig})e^x - \int {a}e^x\,dx = ({linear_orig})e^x - {a}e^x + C = {fmt_res(a, k)}. \]'''
    
    return caudan, choices, loi_giai


def NguyenHam_MC_ViPhanLuongGiac():
    """Câu 11 MC: f'(x) = a*cos(x) + 2*b*x, f(0) = c => tìm f(x)"""
    a = random.choice([2, 3, 4, -2, -3])
    b = random.choice([1, 2, 3, -1, -2])
    c = random.choice([1, 2, 3, 4, -1, -2])
    
    # f'(x) = a*cos(x) + 2*b*x
    # f(x) = a*sin(x) + b*x^2 + C
    # f(0) = C => C = c
    
    two_b = 2 * b
    b_term = f"+ {two_b}x" if two_b > 0 else f"- {abs(two_b)}x"
    f_prime_expr = f"{a}\\cos x {b_term}"
    
    def fmt_fx(val_a, val_b, val_c):
        part_a = f"{val_a}\\sin x" if val_a != 1 else "\\sin x"
        if val_b == 1:
            part_b = "+ x^2"
        elif val_b == -1:
            part_b = "- x^2"
        elif val_b > 0:
            part_b = f"+ {val_b}x^2"
        else:
            part_b = f"- {abs(val_b)}x^2"
            
        part_c = f"+ {val_c}" if val_c > 0 else f"- {abs(val_c)}"
        return f"f(x) = {part_a} {part_b} {part_c}"
        
    correct_str = f"${fmt_fx(a, b, c)}$"
    wrong1 = f"${fmt_fx(-a, b, c)}$"
    wrong2 = f"${fmt_fx(a, two_b, c)}$"
    wrong3 = f"${fmt_fx(a, b, -c)}$"
    
    caudan = fr'''Cho hàm số $y=f(x)$ thỏa mãn $f'(x) = {f_prime_expr}$ và $f(0) = {c}$. Mệnh đề nào dưới đây đúng?'''
    choices = shuffle_choices(correct_str, [wrong1, wrong2, wrong3])
    
    loi_giai = fr'''Ta có:
\[ f(x) = \int f'(x)\,dx = \int \left({f_prime_expr}\right)dx = {a}\sin x + {b}x^2 + C. \]
Vì $f(0) = {c}$ nên ${a}\sin 0 + {b}\cdot 0^2 + C = {c} \implies C = {c}$.
Vậy ${fmt_fx(a, b, c)}$.'''
    
    return caudan, choices, loi_giai


# ==============================================================================
# PHẦN 2: CHỦ ĐỀ NGUYÊN HÀM - ĐÚNG / SAI (TF)
# ==============================================================================

def NguyenHam_TF_DaThucBac3():
    """Câu 1 TF: Cho f(x) = 3ax^2 + 2bx + c, khảo sát nguyên hàm F(x)"""
    a = random.choice([1, 2])
    b = random.choice([-3, -2, -1, 1, 2, 3])
    c = random.choice([-4, -2, 1, 2, 3])
    
    # f(x) = 3*a*x^2 + 2*b*x + c
    f_expr = fmt_poly_deg2(3*a, 2*b, c)
    # F(x) = a*x^3 + b*x^2 + c*x + C
    F_no_C = fmt_poly_deg3(a, b, c, 0)
    
    # a) Đạo hàm tại điểm x0
    x0 = 1
    val_f_prime = 6*a*x0 + 2*b
    stmt_a_t = fr'''Đạo hàm của $f(x)$ tại $x={x0}$ là $f'({x0}) = {val_f_prime}$.'''
    stmt_a_f = fr'''Đạo hàm của $f(x)$ tại $x={x0}$ là $f'({x0}) = {val_f_prime + 2}$.'''
    exp_a_t = fr'''Ta có $f'(x) = {6*a}x + {2*b} \implies f'({x0}) = {6*a}\cdot {x0} + {2*b} = {val_f_prime}$.'''
    exp_a_f = fr'''Ta có $f'(x) = {6*a}x + {2*b} \implies f'({x0}) = {val_f_prime} \ne {val_f_prime + 2}$.'''
    
    # b) Họ nguyên hàm
    stmt_b_t = fr'''Họ tất cả các nguyên hàm của $f(x)$ là $\int f(x)\,dx = {F_no_C} + C$.'''
    stmt_b_f = fr'''Họ tất cả các nguyên hàm của $f(x)$ là $\int f(x)\,dx = {fmt_poly_deg3(3*a, 2*b, c, 0)} + C$.'''
    exp_b_t = fr'''Áp dụng công thức nguyên hàm đa thức: $\int ({f_expr})\,dx = {F_no_C} + C$.'''
    exp_b_f = fr'''Công thức đúng là $\int f(x)\,dx = {F_no_C} + C$, khẳng định đã quên chia cho số mũ khi lấy nguyên hàm.'''
    
    # c) Cho F(1) = y1 => tìm F(x)
    y1 = random.choice([2, 3, 5])
    C_val = y1 - (a + b + c)
    F_full_str = fmt_poly_deg3(a, b, c, C_val)
    stmt_c_t = fr'''Nếu $F(x)$ là một nguyên hàm của $f(x)$ thỏa mãn $F(1) = {y1}$ thì $F(x) = {F_full_str}$.'''
    stmt_c_f = fr'''Nếu $F(x)$ là một nguyên hàm của $f(x)$ thỏa mãn $F(1) = {y1}$ thì $F(x) = {fmt_poly_deg3(a, b, c, C_val + 3)}$.'''
    exp_c_t = fr'''Từ $F(1) = {y1} \implies {a}\cdot 1^3 + {b}\cdot 1^2 + {c}\cdot 1 + C = {y1} \implies C = {C_val}$. Do đó $F(x) = {F_full_str}$.'''
    exp_c_f = fr'''Thay $x=1$ vào ta tính được $C = {C_val}$, không phải $C = {C_val + 3}$.'''
    
    # d) Tích phân từ 0 đến 2
    int_val = a*(2**3) + b*(2**2) + c*2
    stmt_d_t = fr'''Giá trị của tích phân $\int_0^2 f(x)\,dx$ bằng ${int_val}$.'''
    stmt_d_f = fr'''Giá trị của tích phân $\int_0^2 f(x)\,dx$ bằng ${int_val + 4}$.'''
    exp_d_t = fr'''$\int_0^2 f(x)\,dx = F(2) - F(0) = \left({F_no_C}\right)\Big|_0^2 = {a}\cdot 8 + {b}\cdot 4 + {c}\cdot 2 = {int_val}$.'''
    exp_d_f = fr'''$\int_0^2 f(x)\,dx = {int_val} \ne {int_val + 4}$.'''
    
    items = [
        (stmt_a_t, stmt_a_f, exp_a_t, exp_a_f),
        (stmt_b_t, stmt_b_f, exp_b_t, exp_b_f),
        (stmt_c_t, stmt_c_f, exp_c_t, exp_c_f),
        (stmt_d_t, stmt_d_f, exp_d_t, exp_d_f)
    ]
    
    caudan = fr'''Cho hàm số $f(x) = {f_expr}$. Các mệnh đề sau đúng hay sai?'''
    choices, loi_giai = make_tf_choices(items)
    return caudan, choices, loi_giai


def NguyenHam_TF_LuongGiacMu():
    """Câu 2 TF: f(x) = sin(kx) + a*e^x"""
    k = random.choice([2, 3, 4])
    a = random.choice([1, 2, -1])
    
    a_str = f"+ {a}e^x" if a > 0 else (f"- e^x" if a == -1 else f"{a}e^x")
    if a == 1:
        a_str = "+ e^x"
        
    f_expr = f"\\sin({k}x) {a_str}"
    
    # a) f'(x)
    stmt_a_t = fr'''Đạo hàm của hàm số đã cho là $f'(x) = {k}\cos({k}x) {a_str}$.'''
    stmt_a_f = fr'''Đạo hàm của hàm số đã cho là $f'(x) = -\cos({k}x) {a_str}$.'''
    exp_a_t = fr'''Áp dụng $(\sin(kx))' = k\cos(kx)$ và $(e^x)' = e^x$, ta có $f'(x) = {k}\cos({k}x) {a_str}$.'''
    exp_a_f = fr'''Đạo hàm của $\sin({k}x)$ là ${k}\cos({k}x)$, không phải $-\cos({k}x)$.'''
    
    # b) Nguyên hàm của sin(kx)
    stmt_b_t = fr'''Một nguyên hàm của hàm số $g(x) = \sin({k}x)$ là $G(x) = -\dfrac{{1}}{{{k}}}\cos({k}x)$.'''
    stmt_b_f = fr'''Một nguyên hàm của hàm số $g(x) = \sin({k}x)$ là $G(x) = \dfrac{{1}}{{{k}}}\cos({k}x)$.'''
    exp_b_t = fr'''Theo bảng nguyên hàm lượng giác: $\int \sin(kx)\,dx = -\dfrac{{1}}{{k}}\cos(kx) + C$.'''
    exp_b_f = fr'''Khẳng định bị sai dấu: $\int \sin(kx)\,dx = -\dfrac{{1}}{{k}}\cos(kx) + C$.'''
    
    # c) Họ nguyên hàm của f(x)
    stmt_c_t = fr'''Họ tất cả các nguyên hàm của $f(x)$ là $\int f(x)\,dx = -\dfrac{{1}}{{{k}}}\cos({k}x) {a_str} + C$.'''
    stmt_c_f = fr'''Họ tất cả các nguyên hàm của $f(x)$ là $\int f(x)\,dx = -{k}\cos({k}x) {a_str} + C$.'''
    exp_c_t = fr'''Ta có $\int \left(\sin({k}x) {a_str}\right)dx = -\dfrac{{1}}{{{k}}}\cos({k}x) {a_str} + C$.'''
    exp_c_f = fr'''Hệ số trước $\cos({k}x)$ phải là $-\dfrac{{1}}{{{k}}}$, không phải $-{k}$.'''
    
    # d) F(0) = y0 => F(pi/k)
    stmt_d_t = fr'''Nếu $F(x)$ là một nguyên hàm của $f(x)$ thỏa mãn $F(0) = 1$ thì $F\left(\dfrac{{\pi}}{{{k}}}\right) = \dfrac{{2}}{{{k}}} + 1 - {a} + {a}e^{{\frac{{\pi}}{{{k}}}}}$.'''
    stmt_d_f = fr'''Nếu $F(x)$ là một nguyên hàm của $f(x)$ thỏa mãn $F(0) = 1$ thì $F\left(\dfrac{{\pi}}{{{k}}}\right) = 1 + {a}e^{{\frac{{\pi}}{{{k}}}}}$.'''
    exp_d_t = fr'''Ta có $F(0) = -\dfrac{{1}}{{{k}}} + {a} + C = 1 \implies C = 1 - {a} + \dfrac{{1}}{{{k}}}$. Khi đó $F\left(\dfrac{{\pi}}{{{k}}}\right) = -\dfrac{{1}}{{{k}}}\cos(\pi) + {a}e^{{\pi/{k}}} + C = \dfrac{{2}}{{{k}}} + 1 - {a} + {a}e^{{\frac{{\pi}}{{{k}}}}}$.'''
    exp_d_f = fr'''Vì $\cos(\pi) = -1$, tính toán cho thấy kết quả đúng chứa $\dfrac{{2}}{{{k}}} + 1 - {a}$, khẳng định thiếu phần số hạng $\dfrac{{2}}{{{k}}}$.'''
    
    items = [
        (stmt_a_t, stmt_a_f, exp_a_t, exp_a_f),
        (stmt_b_t, stmt_b_f, exp_b_t, exp_b_f),
        (stmt_c_t, stmt_c_f, exp_c_t, exp_c_f),
        (stmt_d_t, stmt_d_f, exp_d_t, exp_d_f)
    ]
    caudan = fr'''Cho hàm số $f(x) = {f_expr}$. Các mệnh đề sau đúng hay sai?'''
    choices, loi_giai = make_tf_choices(items)
    return caudan, choices, loi_giai


def NguyenHam_TF_DoThiBac3():
    """Câu 3 TF: Đồ thị hàm bậc 3 f(x), các tính chất của f'(x) và nguyên hàm F(x)"""
    d = random.choice([1, 2, 3])
    y_cd = d
    y_ct = d - 4
    caudan = fr'''Cho hàm số bậc ba $y=f(x)$ liên tục trên $\mathbb{{R}}$ có đồ thị như hình vẽ sau:
\begin{{center}}
\begin{{tikzpicture}}[scale=0.85,>=stealth]
\draw[->] (-1.5,0) -- (3.5,0) node[below] {{$x$}};
\draw[->] (0,{y_ct - 1}) -- (0,{y_cd + 1.5}) node[left] {{$y$}};
\fill (0,0) circle (1.5pt) node[below left] {{$O$}};
\draw[dashed] (2,0) node[above] {{$2$}} -- (2,{y_ct}) -- (0,{y_ct}) node[left] {{${y_ct}$}};
\fill (0,{y_cd}) circle (1.5pt) node[left] {{${y_cd}$}};
\fill (2,{y_ct}) circle (1.5pt);
\draw[thick,domain=-0.8:3.2,samples=100] plot (\x, {{(\x)^3 - 3*(\x)^2 + {d}}});
\node at (3,{y_cd}) {{$y=f(x)$}};
\end{{tikzpicture}}
\end{{center}}'''

    stmt_a_t = fr'''Hàm số $y=f(x)$ nghịch biến trên khoảng $(0; 2)$.'''
    stmt_a_f = fr'''Hàm số $y=f(x)$ đồng biến trên khoảng $(0; 2)$.'''
    exp_a_t = fr'''Từ đồ thị ta thấy trên khoảng $(0; 2)$ đồ thị đi xuống từ trái sang phải nên hàm số nghịch biến trên $(0; 2)$.'''
    exp_a_f = fr'''Đồ thị đi xuống trên khoảng $(0; 2)$ nên hàm số nghịch biến, khẳng định đồng biến là sai.'''

    stmt_b_t = fr'''Phương trình đạo hàm $f'(x) = 0$ có đúng hai nghiệm phân biệt là $x=0$ và $x=2$.'''
    stmt_b_f = fr'''Phương trình đạo hàm $f'(x) = 0$ vô nghiệm trên $\mathbb{{R}}$.'''
    exp_b_t = fr'''Đồ thị hàm số có hai điểm cực trị tại $x=0$ (cực đại) và $x=2$ (cực tiểu), do đó $f'(x) = 0$ có hai nghiệm phân biệt $x=0, x=2$.'''
    exp_b_f = fr'''Hàm số có hai điểm cực trị nên $f'(x) = 0$ có hai nghiệm phân biệt $x=0$ và $x=2$.'''

    diff_val = y_ct - y_cd
    stmt_c_t = fr'''Nếu $F(x)$ là một nguyên hàm của hàm số $f'(x)$ thì $F(2) - F(0) = {diff_val}$.'''
    stmt_c_f = fr'''Nếu $F(x)$ là một nguyên hàm của hàm số $f'(x)$ thì $F(2) - F(0) = {-diff_val}$.'''
    exp_c_t = fr'''Theo định nghĩa nguyên hàm: $F(2) - F(0) = \int_0^2 f'(x)\,dx = f(2) - f(0) = {y_ct} - {y_cd} = {diff_val}$.'''
    exp_c_f = fr'''$F(2) - F(0) = f(2) - f(0) = {y_ct} - {y_cd} = {diff_val} \ne {-diff_val}$.'''

    stmt_d_t = fr'''Giá trị lớn nhất của hàm số $y=f(x)$ trên đoạn $[0; 2]$ bằng ${y_cd}$.'''
    stmt_d_f = fr'''Giá trị lớn nhất của hàm số $y=f(x)$ trên đoạn $[0; 2]$ bằng ${y_ct}$.'''
    exp_d_t = fr'''Trên đoạn $[0; 2]$, hàm số liên tục và nghịch biến, do đó $\max_{{[0; 2]}} f(x) = f(0) = {y_cd}$.'''
    exp_d_f = fr'''Trên đoạn $[0; 2]$, giá trị lớn nhất là $f(0) = {y_cd}$, còn ${y_ct}$ là giá trị nhỏ nhất tại $x=2$.'''

    items = [
        (stmt_a_t, stmt_a_f, exp_a_t, exp_a_f),
        (stmt_b_t, stmt_b_f, exp_b_t, exp_b_f),
        (stmt_c_t, stmt_c_f, exp_c_t, exp_c_f),
        (stmt_d_t, stmt_d_f, exp_d_t, exp_d_f)
    ]
    choices, loi_giai = make_tf_choices(items)
    return caudan, choices, loi_giai


def NguyenHam_TF_TangTruongDanSo():
    """Câu 4 TF: Toán thực tế tốc độ tăng dân số P'(t) = k / (t + t0)"""
    P0 = random.choice([200, 300, 400, 500])  # nghìn người
    k = random.choice([20, 30, 40, 50])
    t0 = random.choice([1, 2, 5])
    
    # a) Họ nguyên hàm
    stmt_a_t = fr'''Họ tất cả các nguyên hàm của hàm tốc độ tăng trưởng là $P(t) = {k}\ln(t + {t0}) + C$ (với $t \ge 0$).'''
    stmt_a_f = fr'''Họ tất cả các nguyên hàm của hàm tốc độ tăng trưởng là $P(t) = -\dfrac{{{k}}}{{(t + {t0})^2}} + C$.'''
    exp_a_t = fr'''Áp dụng công thức $\int \dfrac{{1}}{{x+a}}\,dx = \ln|x+a| + C$, ta có $P(t) = \int \dfrac{{{k}}}{{t + {t0}}}\,dt = {k}\ln(t + {t0}) + C$ (vì $t \ge 0$).'''
    exp_a_f = fr'''Công thức $-\dfrac{{{k}}}{{(t+{t0})^2}}$ là đạo hàm của $P'(t)$, không phải nguyên hàm.'''

    # b) Hằng số C
    c_val_str = f"{P0} - {k}\\ln {t0}" if t0 > 1 else f"{P0}"
    stmt_b_t = fr'''Hằng số $C$ xác định từ điều kiện ban đầu $P(0) = {P0}$ là $C = {c_val_str}$.'''
    stmt_b_f = fr'''Hằng số $C$ xác định từ điều kiện ban đầu $P(0) = {P0}$ là $C = {P0 + 10}$.'''
    exp_b_t = fr'''Tại $t=0$, $P(0) = {k}\ln({t0}) + C = {P0} \implies C = {c_val_str}$.'''
    exp_b_f = fr'''Tính từ điều kiện $P(0) = {P0}$, ta được $C = {c_val_str} \ne {P0 + 10}$.'''

    # c) Dân số sau 10 năm
    t_val = 10
    val_pop = round(P0 + k * math.log((10 + t0) / t0), 1)
    stmt_c_t = fr'''Sau ${t_val}$ năm, quy mô dân số của thành phố xấp xỉ ${val_pop}$ nghìn người.'''
    stmt_c_f = fr'''Sau ${t_val}$ năm, quy mô dân số của thành phố xấp xỉ ${round(val_pop + 25.5, 1)}$ nghìn người.'''
    exp_c_t = fr'''Sau $10$ năm ($t=10$), dân số là $P(10) = {P0} + {k}\ln\left(\dfrac{{{10 + t0}}}{{{t0}}}\right) \approx {val_pop}$ nghìn người.'''
    exp_c_f = fr'''Thay $t=10$ vào công thức ta được $P(10) \approx {val_pop}$ nghìn người, khẳng định trên là sai.'''

    # d) Tốc độ tăng trưởng sau 5 năm
    rate_5 = round(k / (5 + t0), 2)
    stmt_d_t = fr'''Tại thời điểm $t=5$ năm, tốc độ gia tăng dân số của thành phố là ${rate_5}$ nghìn người/năm.'''
    stmt_d_f = fr'''Tại thời điểm $t=5$ năm, tốc độ gia tăng dân số của thành phố là ${round(rate_5 + 3.2, 2)}$ nghìn người/năm.'''
    exp_d_t = fr'''Tốc độ gia tăng tại $t=5$ là $P'(5) = \dfrac{{{k}}}{{5 + {t0}}} = {rate_5}$ nghìn người/năm.'''
    exp_d_f = fr'''Tốc độ gia tăng tại $t=5$ là $P'(5) = \dfrac{{{k}}}{{{5 + t0}}} = {rate_5} \ne {round(rate_5 + 3.2, 2)}$.'''

    items = [
        (stmt_a_t, stmt_a_f, exp_a_t, exp_a_f),
        (stmt_b_t, stmt_b_f, exp_b_t, exp_b_f),
        (stmt_c_t, stmt_c_f, exp_c_t, exp_c_f),
        (stmt_d_t, stmt_d_f, exp_d_t, exp_d_f)
    ]
    caudan = fr'''Tốc độ gia tăng dân số của một đô thị sau $t$ năm (kể từ năm 2020) được mô hình hóa bởi hàm số $P'(t) = \dfrac{{{k}}}{{t + {t0}}}$ (nghìn người/năm). Dân số của đô thị vào năm 2020 là ${P0}$ nghìn người. Các mệnh đề sau đúng hay sai?'''
    choices, loi_giai = make_tf_choices(items)
    return caudan, choices, loi_giai


# ==============================================================================
# PHẦN 3: CHỦ ĐỀ NGUYÊN HÀM - TRẢ LỜI NGẮN (SA)
# ==============================================================================

def NguyenHam_SA_TinhF2():
    """Câu 1 SA: f(x) = 3ax^2 + 2bx + c, biết F(x1)=y1, tính F(x2)"""
    a = random.choice([1, 2])
    b = random.choice([-2, -1, 1, 2])
    c = random.choice([-3, -1, 1, 3])
    
    f_expr = fmt_poly_deg2(3*a, 2*b, c)
    x1 = 1
    y1 = random.choice([2, 3, 4, 5])
    # F(x) = a*x^3 + b*x^2 + c*x + C
    # y1 = a + b + c + C => C = y1 - a - b - c
    C = y1 - (a + b + c)
    
    x2 = 2
    ans = a * (x2 ** 3) + b * (x2 ** 2) + c * x2 + C
    
    caudan = fr'''Cho hàm số $f(x) = {f_expr}$ và $F(x)$ là một nguyên hàm của $f(x)$ thỏa mãn $F({x1}) = {y1}$. Tính giá trị của $F({x2})$.'''
    
    loi_giai = fr'''Họ tất cả các nguyên hàm của $f(x)$ là:
\[ F(x) = \int ({f_expr})\,dx = {fmt_poly_deg3(a, b, c, 0)} + C. \]
Theo giả thiết:
\[ F({x1}) = {y1} \implies {a}\cdot ({x1})^3 + ({b})\cdot ({x1})^2 + ({c})\cdot ({x1}) + C = {y1} \implies C = {C}. \]
Do đó $F(x) = {fmt_poly_deg3(a, b, c, C)}$.
Vậy giá trị của $F({x2})$ là:
\[ F({x2}) = {a}\cdot {x2}^3 + ({b})\cdot {x2}^2 + ({c})\cdot {x2} + ({C}) = {ans}. \]'''

    return caudan, loi_giai, str(ans)


def NguyenHam_SA_DongNhatHeSo():
    r"""Câu 2 SA: Đồng nhất hệ số \int (mx+n)e^x dx = (ax+b)e^x + C, tính S = a + b"""
    m = random.choice([2, 3, 4, 5])
    n = random.choice([-4, -3, -2, -1, 1, 2, 3, 4])
    
    lin_expr = f"{m}x + {n}" if n > 0 else f"{m}x - {abs(n)}"
    target_name = random.choice(["S = a + b", "P = a - b"])
    
    a_val = m
    b_val = n - m
    if target_name == "S = a + b":
        ans = a_val + b_val
    else:
        ans = a_val - b_val
        
    caudan = fr'''Biết $\int ({lin_expr})e^x\,dx = (ax + b)e^x + C$ với $a, b \in \mathbb{{Z}}$. Tính giá trị của biểu thức ${target_name}$.'''
    
    loi_giai = fr'''Áp dụng phương pháp nguyên hàm từng phần:
Đặt $\begin{{cases}} u = {lin_expr} \\ dv = e^x\,dx \end{{cases}} \implies \begin{{cases}} du = {m}\,dx \\ v = e^x \end{{cases}}$.
Ta có:
\[ \int ({lin_expr})e^x\,dx = ({lin_expr})e^x - \int {m}e^x\,dx = ({lin_expr} - {m})e^x + C = ({m}x + {b_val})e^x + C. \]
Đồng nhất hệ số với $(ax + b)e^x + C$, ta được:
\[ a = {a_val}, \quad b = {b_val}. \]
Vậy ${target_name} = {ans}$.'''

    return caudan, loi_giai, str(ans)


def NguyenHam_SA_LuongGiacF0():
    """Câu 3 SA: f(x) = (2k)*cos(kx), F(pi/(2k)) = y0, tính F(0)"""
    k = random.choice([2, 3, 4])
    a = 2 * k
    y0 = random.choice([3, 4, 5, 6])
    
    ans = y0 - 2
    
    caudan = fr'''Cho hàm số $f(x) = {a}\cos({k}x)$. Biết $F(x)$ là một nguyên hàm của $f(x)$ thỏa mãn $F\left(\dfrac{{\pi}}{{{2*k}}}\right) = {y0}$. Tính giá trị của $F(0)$.'''
    
    loi_giai = fr'''Ta có:
\[ F(x) = \int {a}\cos({k}x)\,dx = \dfrac{{{a}}}{{{k}}}\sin({k}x) + C = 2\sin({k}x) + C. \]
Theo giả thiết:
\[ F\left(\dfrac{{\pi}}{{{2*k}}}\right) = {y0} \implies 2\sin\left({k}\cdot \dfrac{{\pi}}{{{2*k}}}\right) + C = {y0} \implies 2\sin\left(\dfrac{{\pi}}{{2}}\right) + C = {y0} \implies 2 + C = {y0} \implies C = {ans}. \]
Do đó $F(0) = 2\sin(0) + C = C = {ans}$.'''

    return caudan, loi_giai, str(ans)


def NguyenHam_SA_OToDapPhanh():
    """Câu 4 SA: Ô tô đạp phanh v(t) = -at + v0. Tính quãng đường đến khi dừng hẳn"""
    pairs = [
        (20, 4),  # s = 400 / 8 = 50 m
        (24, 4),  # s = 576 / 8 = 72 m
        (30, 5),  # s = 900 / 10 = 90 m
        (16, 2),  # s = 256 / 4 = 64 m
        (18, 3),  # s = 324 / 6 = 54 m
        (12, 2),  # s = 144 / 4 = 36 m
    ]
    v0, a = random.choice(pairs)
    t_dung = v0 // a
    s = (v0 ** 2) // (2 * a)
    
    caudan = fr'''Một ô tô đang chạy với vận tốc ${v0}\text{{ m/s}}$ thì người lái xe đạp phanh. Từ thời điểm đó, ô tô chuyển động chậm dần đều với vận tốc $v(t) = -{a}t + {v0}\text{{ (m/s)}}$, trong đó $t$ là khoảng thời gian tính bằng giây kể từ lúc bắt đầu đạp phanh. Hỏi từ lúc đạp phanh đến khi dừng hẳn, ô tô còn di chuyển được bao nhiêu mét?'''
    
    loi_giai = fr'''Khi ô tô dừng hẳn thì vận tốc $v(t) = 0$:
\[ -{a}t + {v0} = 0 \implies t = {t_dung}\text{{ (giây)}}. \]
Quãng đường ô tô di chuyển từ lúc đạp phanh đến khi dừng hẳn là:
\[ s = \int_0^{{{t_dung}}} v(t)\,dt = \int_0^{{{t_dung}}} (-{a}t + {v0})\,dt = \left( -\dfrac{{{a}}}{{2}}t^2 + {v0}t \right)\Bigg|_0^{{{t_dung}}} = -\dfrac{{{a}}}{{2}}\cdot ({t_dung})^2 + {v0}\cdot {t_dung} = {s}\text{{ (m)}}. \]
Vậy ô tô còn di chuyển được ${s}\text{{ m}}$.'''

    return caudan, loi_giai, str(s)


def NguyenHam_SA_CucDaiNguyenHam():
    """Câu 5 SA: Cho f(x) = -3x^2 + b*x, tìm điểm cực đại của F(x)"""
    x2 = random.choice([2, 3, 4])
    a = 3
    b = a * x2
    ans = x2
    
    caudan = fr'''Cho hàm số $y=f(x)$ liên tục trên $\mathbb{{R}}$ có công thức $f(x) = -{a}x^2 + {b}x$. Biết $F(x)$ là một nguyên hàm của $f(x)$. Tìm điểm cực đại của hàm số $F(x)$.'''
    
    loi_giai = fr'''Vì $F(x)$ là một nguyên hàm của $f(x)$ nên $F'(x) = f(x) = -{a}x^2 + {b}x$.
Giải phương trình:
\[ F'(x) = 0 \iff -{a}x(x - {x2}) = 0 \iff \left[\begin{{aligned}} x &= 0 \\ x &= {x2}. \end{{aligned}}\right. \]
Bảng xét dấu của $F'(x)$:
\begin{{itemize}}
\item $F'(x) > 0$ khi $x \in (0; {x2})$;
\item $F'(x) < 0$ khi $x \in (-\infty; 0) \cup ({x2}; +\infty)$.
\end{{itemize}}
Do đó qua điểm $x = {x2}$, đạo hàm $F'(x)$ đổi dấu từ dương sang âm nên hàm số $F(x)$ đạt cực đại tại điểm $x = {x2}$.'''

    return caudan, loi_giai, str(ans)


def NguyenHam_SA_BomNuocVaoBe():
    """Câu 6 SA: Bơm nước vào bể có sẵn V0 lít, tốc độ v(t) = at + b (lít/phút). Tính V sau T phút"""
    V0 = random.choice([100, 150, 200, 250, 300])
    a = random.choice([2, 4, 6])
    b = random.choice([10, 15, 20, 25])
    T = random.choice([5, 10, 15, 20])
    
    water_in = (a // 2) * (T ** 2) + b * T
    total_V = V0 + water_in
    
    caudan = fr'''Một bể chứa nước ban đầu có ${V0}\text{{ lít}}$ nước. Người ta bắt đầu bơm thêm nước vào bể với tốc độ $v(t) = {a}t + {b}\text{{ (lít/phút)}}$, trong đó $t$ là thời gian tính bằng phút kể từ khi bắt đầu bơm. Hỏi sau ${T}\text{{ phút}}$, tổng lượng nước có trong bể là bao nhiêu lít?'''
    
    loi_giai = fr'''Lượng nước được bơm thêm vào bể sau ${T}\text{{ phút}}$ là:
\[ \Delta V = \int_0^{{{T}}} v(t)\,dt = \int_0^{{{T}}} ({a}t + {b})\,dt = \left( \dfrac{{{a}}}{{2}}t^2 + {b}t \right)\Bigg|_0^{{{T}}} = {a//2}\cdot {T}^2 + {b}\cdot {T} = {water_in}\text{{ (lít)}}. \]
Tổng lượng nước trong bể sau ${T}\text{{ phút}}$ là:
\[ V = V_0 + \Delta V = {V0} + {water_in} = {total_V}\text{{ (lít)}}. \]'''

    return caudan, loi_giai, str(total_V)


# ==============================================================================
# PHẦN 4: CHỦ ĐỀ HÀM SỐ - ĐÚNG / SAI (TF) & TRẢ LỜI NGẮN (SA) MỚI
# ==============================================================================

def HamSo_TF_CanThuc():
    r"""Câu 2 TF Hàm số: Khảo sát hàm chứa căn y = x + \sqrt{a^2 - x^2} trên [-a; a]"""
    a = random.choice([2, 3, 4, 5, 6])
    a2 = a ** 2
    
    stmt_a_t = fr'''Tập xác định của hàm số là $D = [-{a}; {a}]$.'''
    stmt_a_f = fr'''Tập xác định của hàm số là $D = (-{a}; {a})$.'''
    exp_a_t = fr'''Điều kiện xác định: ${a2} - x^2 \ge 0 \iff x^2 \le {a2} \iff -{a} \le x \le {a}$. Do đó $D = [-{a}; {a}]$.'''
    exp_a_f = fr'''Biểu thức dưới căn nhận giá trị tại hai đầu mút $x = \pm {a}$ nên $D = [-{a}; {a}]$, không phải khoảng mở $(-{a}; {a})$.'''

    stmt_b_t = fr'''Đạo hàm của hàm số trên khoảng $(-{a}; {a})$ là $y' = 1 - \dfrac{{x}}{{\sqrt{{{a2} - x^2}}}}$.'''
    stmt_b_f = fr'''Đạo hàm của hàm số trên khoảng $(-{a}; {a})$ là $y' = 1 + \dfrac{{x}}{{\sqrt{{{a2} - x^2}}}}$.'''
    exp_b_t = fr'''Ta có $y' = (x)' + \left(\sqrt{{{a2} - x^2}}\right)' = 1 + \dfrac{{-2x}}{{2\sqrt{{{a2} - x^2}}}} = 1 - \dfrac{{x}}{{\sqrt{{{a2} - x^2}}}}$.'''
    exp_b_f = fr'''Đạo hàm của $\sqrt{{{a2}-x^2}}$ có dấu trừ ở tử số: $\dfrac{{-x}}{{\sqrt{{{a2}-x^2}}}}$, khẳng định mang dấu cộng là sai.'''

    max_val_str = f"{a}\\sqrt{{2}}"
    stmt_c_t = fr'''Giá trị lớn nhất của hàm số trên đoạn $[-{a}; {a}]$ bằng ${max_val_str}$.'''
    stmt_c_f = fr'''Giá trị lớn nhất của hàm số trên đoạn $[-{a}; {a}]$ bằng ${a}$.'''
    exp_c_t = fr'''$y' = 0 \iff \sqrt{{{a2} - x^2}} = x \iff \begin{{cases}} x > 0 \\ 2x^2 = {a2} \end{{cases}} \iff x = \dfrac{{{a}\sqrt{{2}}}}{{2}}$.
Khi đó $y\left(\dfrac{{{a}\sqrt{{2}}}}{{2}}\right) = \dfrac{{{a}\sqrt{{2}}}}{{2}} + \dfrac{{{a}\sqrt{{2}}}}{{2}} = {max_val_str}$.
Tại hai đầu mút: $y(-{a}) = -{a}$, $y({a}) = {a}$. Vậy $\max y = {max_val_str}$.'''
    exp_c_f = fr'''Giá trị lớn nhất đạt tại $x = \dfrac{{{a}\sqrt{{2}}}}{{2}}$ bằng ${max_val_str} > {a}$.'''

    stmt_d_t = fr'''Giá trị nhỏ nhất của hàm số trên đoạn $[-{a}; {a}]$ bằng $-{a}$.'''
    stmt_d_f = fr'''Giá trị nhỏ nhất của hàm số trên đoạn $[-{a}; {a}]$ bằng $0$.'''
    exp_d_t = fr'''So sánh các giá trị $y(-{a}) = -{a}$, $y({a}) = {a}$, $y\left(\dfrac{{{a}\sqrt{{2}}}}{{2}}\right) = {max_val_str}$, ta có $\min y = -{a}$ tại $x = -{a}$.'''
    exp_d_f = fr'''Tại $x = -{a}$ thì $y = -{a} + 0 = -{a} < 0$, nên GTNN bằng $-{a}$, khẳng định bằng $0$ là sai.'''

    items = [
        (stmt_a_t, stmt_a_f, exp_a_t, exp_a_f),
        (stmt_b_t, stmt_b_f, exp_b_t, exp_b_f),
        (stmt_c_t, stmt_c_f, exp_c_t, exp_c_f),
        (stmt_d_t, stmt_d_f, exp_d_t, exp_d_f)
    ]
    caudan = fr'''Cho hàm số $y = f(x) = x + \sqrt{{{a2} - x^2}}$ trên đoạn $[-{a}; {a}]$. Các mệnh đề sau đúng hay sai?'''
    choices, loi_giai = make_tf_choices(items)
    return caudan, choices, loi_giai


def HamSo_TF_CatTamTon():
    """Câu 4 TF Hàm số: Cắt 4 góc tấm tôn hình vuông cạnh a gập thành hộp"""
    a = random.choice([12, 18, 24, 30, 36, 60])
    x_opt = a // 6
    v_max = x_opt * ((a - 2 * x_opt) ** 2)
    
    stmt_a_t = fr'''Điều kiện của cạnh hình vuông bị cắt là $0 < x < {a // 2}$.'''
    stmt_a_f = fr'''Điều kiện của cạnh hình vuông bị cắt là $0 < x < {a}$.'''
    exp_a_t = fr'''Do hai góc bị cắt có độ dài $2x$, đáy hộp có kích thước $a - 2x > 0 \implies x < \dfrac{{{a}}}{{2}} = {a // 2}$. Vậy $0 < x < {a // 2}$.'''
    exp_a_f = fr'''Nếu $x \ge {a // 2}$ thì chiều dài đáy $a - 2x \le 0$ không tạo thành hình hộp.'''

    stmt_b_t = fr'''Thể tích của chiếc hộp không nắp được tính theo công thức $V(x) = x({a} - 2x)^2$.'''
    stmt_b_f = fr'''Thể tích của chiếc hộp không nắp được tính theo công thức $V(x) = x^2({a} - 2x)$.'''
    exp_b_t = fr'''Đáy hộp là hình vuông cạnh $({a} - 2x)$, chiều cao hộp là $x$. Thể tích $V(x) = x({a} - 2x)^2$.'''
    exp_b_f = fr'''Diện tích đáy là $({a} - 2x)^2$, chiều cao là $x$, nên $V(x) = x({a}-2x)^2$, khẳng định $x^2({a}-2x)$ là sai.'''

    stmt_c_t = fr'''Đạo hàm của hàm thể tích là $V'(x) = ({a} - 2x)({a} - 6x)$.'''
    stmt_c_f = fr'''Đạo hàm của hàm thể tích là $V'(x) = ({a} - 2x)({a} - 4x)$.'''
    exp_c_t = fr'''$V(x) = 4x^3 - {4*a}x^2 + {a**2}x \implies V'(x) = 12x^2 - {8*a}x + {a**2} = ({a} - 2x)({a} - 6x)$.'''
    exp_c_f = fr'''$V'(x) = 12x^2 - {8*a}x + {a**2} = ({a}-2x)({a}-6x) \ne ({a}-2x)({a}-4x)$.'''

    stmt_d_t = fr'''Thể tích chiếc hộp lớn nhất khi $x = {x_opt}\text{{ cm}}$ và giá trị lớn nhất bằng ${v_max}\text{{ cm}}^3$.'''
    stmt_d_f = fr'''Thể tích chiếc hộp lớn nhất khi $x = {a // 4}\text{{ cm}}$.'''
    exp_d_t = fr'''Cho $V'(x) = 0 \iff x = \dfrac{{{a}}}{{6}} = {x_opt}$ (nhận vì thuộc $(0; {a//2})$). Khi đó $V_{{max}} = {x_opt}({a} - 2\cdot {x_opt})^2 = {v_max}\text{{ cm}}^3$.'''
    exp_d_f = fr'''Điểm cực đại là $x = \dfrac{{{a}}}{{6}} = {x_opt}$, không phải $x = {a // 4}$.'''

    items = [
        (stmt_a_t, stmt_a_f, exp_a_t, exp_a_f),
        (stmt_b_t, stmt_b_f, exp_b_t, exp_b_f),
        (stmt_c_t, stmt_c_f, exp_c_t, exp_c_f),
        (stmt_d_t, stmt_d_f, exp_d_t, exp_d_f)
    ]
    caudan = fr'''Một tấm tôn hình vuông có cạnh bằng ${a}\text{{ cm}}$. Người ta cắt bỏ bốn hình vuông bằng nhau có cạnh bằng $x\text{{ (cm)}}$ ở bốn góc, sau đó gập các mép lại để tạo thành một chiếc hộp chữ nhật không nắp. Các mệnh đề sau đúng hay sai?'''
    choices, loi_giai = make_tf_choices(items)
    return caudan, choices, loi_giai


def HamSo_SA_SoNguyenDuongDongBien():
    """Câu 1 SA: Số giá trị nguyên m để hàm số y = x^3/3 - (m+1)x^2 + (m^2+2m-3)x đồng biến trên (alpha; +inf)"""
    alpha = random.choice([6, 7, 8, 9, 10])
    m_max = alpha - 3
    ans = max(0, m_max)
    
    caudan = fr'''Có bao nhiêu giá trị nguyên dương của tham số $m$ để hàm số $y = \dfrac{{1}}{{3}}x^3 - (m+1)x^2 + (m^2 + 2m - 3)x + 2025$ đồng biến trên khoảng $({alpha}; +\infty)$?'''
    
    loi_giai = fr'''Tập xác định $D = \mathbb{{R}}$.
Ta có đạo hàm:
\[ y' = x^2 - 2(m+1)x + (m^2 + 2m - 3). \]
Phương trình $y' = 0$ có $\Delta' = (m+1)^2 - (m^2 + 2m - 3) = 4 > 0$.
Do đó $y' = 0$ luôn có hai nghiệm phân biệt:
\[ x_1 = (m+1) - 2 = m - 1, \quad x_2 = (m+1) + 2 = m + 3 \quad (x_1 < x_2). \]
Hàm số đồng biến trên khoảng $({alpha}; +\infty)$ khi và chỉ khi:
\[ y' \ge 0, \; \forall x \in ({alpha}; +\infty) \iff x_2 \le {alpha} \iff m + 3 \le {alpha} \iff m \le {m_max}. \]
Vì $m$ là số nguyên dương ($m \in \mathbb{{Z}}^+$) nên $m \in \{{1; 2; \dots; {m_max}\}}$.
Vậy có tất cả ${ans}$ giá trị nguyên dương của $m$ thỏa mãn.'''

    return caudan, loi_giai, str(ans)


def HamSo_SA_TichGiaTriCucTri():
    """Câu 2 SA: Cho hàm số y = (x^2 - 2x + 2) / (x - 1), tính tích các giá trị cực trị"""
    x0 = random.choice([1, 2, 3, -1, -2])
    k = random.choice([1, 2, 3])
    c0 = random.choice([0, 1, 2])
    
    A = c0 - x0
    B = -c0 * x0 + k**2
    
    y1 = (x0 + c0) - 2 * k
    y2 = (x0 + c0) + 2 * k
    prod = y1 * y2
    
    num_str = fmt_poly_deg2(1, A, B)
    den_str = f"x - {x0}" if x0 > 0 else f"x + {abs(x0)}"
    
    caudan = fr'''Cho hàm số $y = \dfrac{{{num_str}}}{{{den_str}}}$. Tính tích các giá trị cực trị của hàm số đã cho.'''
    
    loi_giai = fr'''Tập xác định $D = \mathbb{{R}} \setminus \{{ {x0} \}}$.
Ta viết lại hàm số dưới dạng:
\[ y = x + {c0} + \dfrac{{{k**2}}}{{{den_str}}}. \]
Đạo hàm:
\[ y' = 1 - \dfrac{{{k**2}}}{{({den_str})^2}} = 0 \iff ({den_str})^2 = {k**2} \iff \left[\begin{{aligned}} x &= {x0 + k} \\ x &= {x0 - k}. \end{{aligned}}\right. \]
Các giá trị cực trị của hàm số là:
\[ y_1 = y({x0 + k}) = {y2}, \quad y_2 = y({x0 - k}) = {y1}. \]
Tích các giá trị cực trị là:
\[ P = y_1 \cdot y_2 = ({y2}) \cdot ({y1}) = {prod}. \]'''

    return caudan, loi_giai, str(prod)


def HamSo_SA_TiemCanChuaCan():
    r"""Câu 4 SA: Đồ thị y = \sqrt{x^2 + a} / (x - b). Tính tổng số tiệm cận"""
    a_val = random.choice([1, 2, 3, 4, 5])
    b_val = random.choice([1, 2, 3, 4])
    
    ans = 3
    b_str = f"x - {b_val}"
    
    caudan = fr'''Tìm tổng số đường tiệm cận đứng và tiệm cận ngang của đồ thị hàm số $y = \dfrac{{\sqrt{{x^2 + {a_val}}}}}{{{b_str}}}$.'''
    
    loi_giai = fr'''Tập xác định: $D = \mathbb{{R}} \setminus \{{ {b_val} \}}$ (do $x^2 + {a_val} > 0$ với mọi $x$).
1. Tiệm cận đứng:
\[ \lim_{{x \to {b_val}^+}} y = +\infty, \quad \lim_{{x \to {b_val}^-}} y = -\infty. \]
Do đó đường thẳng $x = {b_val}$ là tiệm cận đứng của đồ thị hàm số (1 tiệm cận đứng).

2. Tiệm cận ngang:
\[ \lim_{{x \to +\infty}} y = \lim_{{x \to +\infty}} \dfrac{{x\sqrt{{1 + \frac{{{a_val}}}{{x^2}}}}}}{{x(1 - \frac{{{b_val}}}{{x}})}} = 1 \implies y = 1\text{{ là tiệm cận ngang}}. \]
\[ \lim_{{x \to -\infty}} y = \lim_{{x \to -\infty}} \dfrac{{-|x|\sqrt{{1 + \frac{{{a_val}}}{{x^2}}}}}}{{x(1 - \frac{{{b_val}}}{{x}})}} = \lim_{{x \to -\infty}} \dfrac{{-x\sqrt{{1 + \frac{{{a_val}}}{{x^2}}}}}}{{x(1 - \frac{{{b_val}}}{{x}})}} = -1 \implies y = -1\text{{ là tiệm cận ngang}}. \]
Vậy đồ thị hàm số có $2$ đường tiệm cận ngang là $y = 1$ và $y = -1$.
Tổng số đường tiệm cận đứng và tiệm cận ngang là $1 + 2 = {ans}$.'''

    return caudan, loi_giai, str(ans)


def HamSo_SA_DoanhThuTour():
    """Câu 5 SA: Tối ưu hóa doanh thu tour du lịch R(x) = (N0 + x)(P0 - d*x)"""
    N0 = random.choice([20, 30, 40])
    d = random.choice([10, 20])
    x_opt = random.choice([10, 15, 20])
    P0 = d * (2 * x_opt + N0)
    
    total_guests = N0 + x_opt
    
    caudan = fr'''Một công ty du lịch tổ chức một chuyến tham quan với quy định: Nếu đoàn có đúng ${N0}$ khách thì giá vé là ${P0}\text{{ nghìn đồng/người}}$. Cứ có thêm $1$ khách tham gia thì giá vé cho mỗi người trong đoàn sẽ giảm đi ${d}\text{{ nghìn đồng}}$. Hỏi đoàn khách cần có bao nhiêu người để doanh thu của công ty du lịch đạt giá trị lớn nhất?'''
    
    loi_giai = fr'''Gọi $x$ là số lượng khách tham gia thêm ($x \ge 0, x \in \mathbb{{N}}$).
Khi đó tổng số người trong đoàn là $N(x) = {N0} + x$ (người).
Giá vé của mỗi người lúc này là:
\[ P(x) = {P0} - {d}x\text{{ (nghìn đồng)}}. \]
Tổng doanh thu của công ty thu được là:
\[ R(x) = N(x) \cdot P(x) = ({N0} + x)({P0} - {d}x) = -{d}x^2 + ({P0} - {d*N0})x + {N0*P0}. \]
Hàm số $R(x)$ là một tam thức bậc hai có bề lõm quay xuống dưới ($a = -{d} < 0$), do đó đạt giá trị lớn nhất tại đỉnh parabol:
\[ x = -\dfrac{{b}}{{2a}} = \dfrac{{{P0} - {d*N0}}}{{2\cdot {d}}} = {x_opt}. \]
Số lượng khách trong đoàn để doanh thu lớn nhất là:
\[ N = {N0} + {x_opt} = {total_guests}\text{{ (người)}}. \]'''

    return caudan, loi_giai, str(total_guests)


def HamSo_SA_TiemCanTrietTieu():
    """Câu 6 SA: Số tiệm cận của phân thức có nghiệm triệt tiêu y = (x - x1)/(x^2 - (x1+x2)x + x1*x2)"""
    x1 = random.choice([1, 2, 3])
    x2 = random.choice([-3, -2, 4, 5])
    
    sum_roots = x1 + x2
    prod_roots = x1 * x2
    
    den_str = fmt_poly_deg2(1, -sum_roots, prod_roots)
    num_str = f"x - {x1}" if x1 > 0 else f"x + {abs(x1)}"
    
    ans = 2
    
    caudan = fr'''Tìm tổng số đường tiệm cận đứng và tiệm cận ngang của đồ thị hàm số $y = \dfrac{{{num_str}}}{{{den_str}}}$.'''
    
    loi_giai = fr'''Tập xác định: $D = \mathbb{{R}} \setminus \{{ {x1}; {x2} \}}$.
Phân tích mẫu số: ${den_str} = ({num_str})(x - {x2})$.
Với mọi $x \in D$, ta rút gọn hàm số:
\[ y = \dfrac{{{num_str}}}{{({num_str})(x - {x2})}} = \dfrac{{1}}{{x - {x2}}}. \]
1. Tiệm cận đứng:
\begin{{itemize}}
\item Tại $x = {x1}$: $\lim_{{x \to {x1}}} y = \lim_{{x \to {x1}}} \dfrac{{1}}{{x - {x2}}} = \dfrac{{1}}{{{x1} - {x2}}} \ne \pm\infty \implies x = {x1}$ không phải là tiệm cận đứng.
\item Tại $x = {x2}$: $\lim_{{x \to {x2}^+}} y = +\infty$ (hoặc $-\infty$) $\implies x = {x2}$ là tiệm cận đứng duy nhất.
\end{{itemize}}
2. Tiệm cận ngang:
\[ \lim_{{x \to \pm\infty}} y = \lim_{{x \to \pm\infty}} \dfrac{{1}}{{x - {x2}}} = 0 \implies y = 0\text{{ là tiệm cận ngang duy nhất}}. \]
Vậy tổng số đường tiệm cận đứng và tiệm cận ngang của đồ thị hàm số là $1 + 1 = {ans}$.'''

    return caudan, loi_giai, str(ans)


# ==============================================================================
# PHẦN 5: CHƯƠNG II - VECTƠ VÀ HỆ TỌA ĐỘ TRONG KHÔNG GIAN (2025)
# ==============================================================================

def VectoKG_MC_TichVoHuongCungHuongNguocHuong():
    """Lý thuyết tích vô hướng: cùng hướng, ngược hướng, góc giữa hai vectơ"""
    variant = random.choice([1, 2, 3, 4, 5])
    if variant == 1:
        caudan = r'''Cho $\vec{a}$ và $\vec{b}$ là hai vectơ cùng hướng và đều khác vectơ $\vec{0}$. Mệnh đề nào sau đây đúng?'''
        correct_text = r"$\vec{a} \cdot \vec{b} = |\vec{a}| \cdot |\vec{b}|$"
        wrong_texts = [
            r"$\vec{a} \cdot \vec{b} = 0$",
            r"$\vec{a} \cdot \vec{b} = -1$",
            r"$\vec{a} \cdot \vec{b} = -|\vec{a}| \cdot |\vec{b}|$"
        ]
        loi_giai = r'''Vì hai vectơ $\vec{a}$ và $\vec{b}$ cùng hướng nên góc giữa chúng bằng $0^\circ$.
Do đó $\vec{a} \cdot \vec{b} = |\vec{a}| \cdot |\vec{b}| \cdot \cos 0^\circ = |\vec{a}| \cdot |\vec{b}|$.'''
    elif variant == 2:
        caudan = r'''Cho $\vec{a}$ và $\vec{b}$ là hai vectơ ngược hướng và đều khác vectơ $\vec{0}$. Mệnh đề nào sau đây đúng?'''
        correct_text = r"$\vec{a} \cdot \vec{b} = -|\vec{a}| \cdot |\vec{b}|$"
        wrong_texts = [
            r"$\vec{a} \cdot \vec{b} = 0$",
            r"$\vec{a} \cdot \vec{b} = |\vec{a}| \cdot |\vec{b}|$",
            r"$\vec{a} \cdot \vec{b} = 1$"
        ]
        loi_giai = r'''Vì hai vectơ $\vec{a}$ và $\vec{b}$ ngược hướng nên góc giữa chúng bằng $180^\circ$.
Do đó $\vec{a} \cdot \vec{b} = |\vec{a}| \cdot |\vec{b}| \cdot \cos 180^\circ = -|\vec{a}| \cdot |\vec{b}|$.'''
    elif variant == 3:
        caudan = r'''Cho hai vectơ $\vec{a}$ và $\vec{b}$ khác $\vec{0}$. Xác định góc $\alpha$ giữa hai vectơ $\vec{a}$ và $\vec{b}$ khi $\vec{a} \cdot \vec{b} = -|\vec{a}| \cdot |\vec{b}|$.'''
        correct_text = r"$\alpha = 180^\circ$"
        wrong_texts = [
            r"$\alpha = 0^\circ$",
            r"$\alpha = 90^\circ$",
            r"$\alpha = 45^\circ$"
        ]
        loi_giai = r'''Ta có $\cos\alpha = \dfrac{\vec{a} \cdot \vec{b}}{|\vec{a}| \cdot |\vec{b}|} = \dfrac{-|\vec{a}| \cdot |\vec{b}|}{|\vec{a}| \cdot |\vec{b}|} = -1 \implies \alpha = 180^\circ$.'''
    elif variant == 4:
        caudan = r'''Cho hai vectơ $\vec{a}$ và $\vec{b}$ khác $\vec{0}$. Xác định góc $\alpha$ giữa hai vectơ $\vec{a}$ và $\vec{b}$ khi $\vec{a} \cdot \vec{b} = |\vec{a}| \cdot |\vec{b}|$.'''
        correct_text = r"$\alpha = 0^\circ$"
        wrong_texts = [
            r"$\alpha = 180^\circ$",
            r"$\alpha = 90^\circ$",
            r"$\alpha = 60^\circ$"
        ]
        loi_giai = r'''Ta có $\cos\alpha = \dfrac{\vec{a} \cdot \vec{b}}{|\vec{a}| \cdot |\vec{b}|} = \dfrac{|\vec{a}| \cdot |\vec{b}|}{|\vec{a}| \cdot |\vec{b}|} = 1 \implies \alpha = 0^\circ$.'''
    else:
        caudan = r'''Cho hai vectơ $\vec{a}$ và $\vec{b}$ khác $\vec{0}$. Xác định góc $\alpha$ giữa hai vectơ $\vec{a}$ và $\vec{b}$ khi $\vec{a} \cdot \vec{b} = 0$.'''
        correct_text = r"$\alpha = 90^\circ$"
        wrong_texts = [
            r"$\alpha = 0^\circ$",
            r"$\alpha = 180^\circ$",
            r"$\alpha = 45^\circ$"
        ]
        loi_giai = r'''Ta có $\cos\alpha = \dfrac{\vec{a} \cdot \vec{b}}{|\vec{a}| \cdot |\vec{b}|} = 0 \implies \alpha = 90^\circ$.'''

    choices = shuffle_choices(correct_text, wrong_texts)
    return caudan, choices, loi_giai


def VectoKG_MC_GocGiuaHaiVecto_DoDai():
    """Góc giữa hai vectơ từ độ dài và tích vô hướng"""
    configs = [
        (8, 2, "8", r"\dfrac{8}{8 \cdot 2} = \dfrac{1}{2}", "60^\\circ"),
        (7, 2, "7\\sqrt{2}", r"\dfrac{7\sqrt{2}}{7 \cdot 2} = \dfrac{\sqrt{2}}{2}", "45^\\circ"),
        (6, 4, "12\\sqrt{3}", r"\dfrac{12\sqrt{3}}{6 \cdot 4} = \dfrac{\sqrt{3}}{2}", "30^\\circ"),
        (5, 6, "0", r"\dfrac{0}{5 \cdot 6} = 0", "90^\\circ"),
        (4, 3, "-6", r"\dfrac{-6}{4 \cdot 3} = -\dfrac{1}{2}", "120^\\circ"),
        (2, 5, "-5\\sqrt{2}", r"\dfrac{-5\sqrt{2}}{2 \cdot 5} = -\dfrac{\sqrt{2}}{2}", "135^\\circ"),
        (6, 2, "-6\\sqrt{3}", r"\dfrac{-6\sqrt{3}}{6 \cdot 2} = -\dfrac{\sqrt{3}}{2}", "150^\\circ"),
    ]
    la, lb, p_str, cos_str, correct_deg = random.choice(configs)
    
    vec_a_name = random.choice([r"\vec{a}", r"\vec{u}"])
    vec_b_name = random.choice([r"\vec{b}", r"\vec{v}"])
    
    caudan = fr'''Cho hai vectơ ${vec_a_name}$ và ${vec_b_name}$ thỏa mãn $|{vec_a_name}| = {la}, |{vec_b_name}| = {lb}$ và ${vec_a_name} \cdot {vec_b_name} = {p_str}$. Góc giữa hai vectơ đã cho là'''
    
    all_angles = ["30^\\circ", "45^\\circ", "60^\\circ", "90^\\circ", "120^\\circ", "135^\\circ", "150^\\circ", "180^\\circ"]
    wrong_degs = [deg for deg in all_angles if deg != correct_deg]
    chosen_wrongs = random.sample(wrong_degs, 3)
    
    choices = shuffle_choices(f"${correct_deg}$", [f"${w}$" for w in chosen_wrongs])
    
    loi_giai = fr'''Áp dụng định nghĩa tích vô hướng:
\[ \cos({vec_a_name}, {vec_b_name}) = \dfrac{{{vec_a_name} \cdot {vec_b_name}}}{{|{vec_a_name}| \cdot |{vec_b_name}|}} = {cos_str}. \]
Suy ra góc giữa hai vectơ là $({vec_a_name}, {vec_b_name}) = {correct_deg}$.'''

    return caudan, choices, loi_giai


def VectoKG_MC_GocHinhLapPhuong():
    """Góc giữa hai vectơ trong hình lập phương kèm hình vẽ TikZ"""
    items = [
        ("B_1C_1", "BD", "BC", "BD", r"45^\circ",
         r"Vì $B_1C_1 \parallel BC$ và $B_1C_1 = BC$ nên $\vec{B_1C_1} = \vec{BC}$. Do đó $(\vec{B_1C_1}, \vec{BD}) = (\vec{BC}, \vec{BD})$. Trong hình vuông $ABCD$, tam giác $BCD$ vuông cân tại $C$ nên $(\vec{BC}, \vec{BD}) = \widehat{CBD} = 45^\circ$."),
        ("B_1C_1", "DB", "BC", "DB", r"135^\circ",
         r"Vì $\vec{B_1C_1} = \vec{BC}$ nên $(\vec{B_1C_1}, \vec{DB}) = (\vec{BC}, \vec{DB}) = 180^\circ - (\vec{BC}, \vec{BD}) = 180^\circ - 45^\circ = 135^\circ$."),
        ("A_1B_1", "BD", "AB", "BD", r"135^\circ",
         r"Vì $\vec{A_1B_1} = \vec{AB}$ nên $(\vec{A_1B_1}, \vec{BD}) = (\vec{AB}, \vec{BD}) = 180^\circ - (\vec{BA}, \vec{BD}) = 180^\circ - 45^\circ = 135^\circ$."),
        ("A_1B_1", "DB", "AB", "DB", r"45^\circ",
         r"Vì $\vec{A_1B_1} = \vec{AB} = \vec{DC}$ nên $(\vec{A_1B_1}, \vec{DB}) = (\vec{DC}, \vec{DB}) = \widehat{BDC} = 45^\circ$."),
        ("A_1C_1", "BD", "AC", "BD", r"90^\circ",
         r"Vì $\vec{A_1C_1} = \vec{AC}$ nên $(\vec{A_1C_1}, \vec{BD}) = (\vec{AC}, \vec{BD})$. Do $ABCD$ là hình vuông nên hai đường chéo $AC \bot BD$, suy ra góc giữa hai vectơ bằng $90^\circ$."),
        ("AA_1", "BD", "AA_1", "BD", r"90^\circ",
         r"Vì $AA_1 \bot (ABCD)$ nên $AA_1 \bot BD$, do đó $(\vec{AA_1}, \vec{BD}) = 90^\circ$."),
    ]
    u_name, v_name, rep_u, rep_v, correct_deg, expl = random.choice(items)
    
    caudan = fr'''Cho hình lập phương $ABCD.A_1B_1C_1D_1$ (xem hình dưới). Góc giữa hai vectơ $\vec{{{u_name}}}$ và $\vec{{{v_name}}}$ bằng
\begin{{center}}
\begin{{tikzpicture}}[scale=0.85,line join=round,line cap=round,>=stealth]
\coordinate (A) at (0,0);
\coordinate (B) at (1,-0.8);
\coordinate (C) at (3.2,-0.8);
\coordinate (D) at (2.2,0);
\coordinate (A1) at (0,2.2);
\coordinate (B1) at (1,1.4);
\coordinate (C1) at (3.2,1.4);
\coordinate (D1) at (2.2,2.2);
\draw[thick] (A1)--(B1)--(C1)--(D1)--cycle;
\draw[thick] (B)--(C)--(C1)--(B1)--cycle;
\draw[thick] (C)--(D)--(D1);
\draw[dashed] (A)--(B);
\draw[dashed] (A)--(D);
\draw[dashed] (A)--(A1);
\node[left] at (A) {{$A$}};
\node[below] at (B) {{$B$}};
\node[below right] at (C) {{$C$}};
\node[right] at (D) {{$D$}};
\node[left] at (A1) {{$A_1$}};
\node[left] at (B1) {{$B_1$}};
\node[right] at (C1) {{$C_1$}};
\node[above] at (D1) {{$D_1$}};
\end{{tikzpicture}}
\end{{center}}'''

    all_angles = [r"45^\circ", r"60^\circ", r"90^\circ", r"120^\circ", r"135^\circ"]
    wrong_degs = [w for w in all_angles if w != correct_deg]
    chosen_wrongs = random.sample(wrong_degs, 3)
    
    choices = shuffle_choices(f"${correct_deg}$", [f"${w}$" for w in chosen_wrongs])
    loi_giai = expl
    return caudan, choices, loi_giai


def VectoKG_MC_DangThucVectoTuDien():
    """Đẳng thức vectơ trong tứ diện kèm hình vẽ TikZ"""
    caudan = r'''Cho tứ diện $ABCD$ (xem hình dưới). Mệnh đề nào dưới đây là mệnh đề đúng?
\begin{center}
\begin{tikzpicture}[scale=0.85,line join=round,line cap=round,>=stealth]
\coordinate (A) at (0,0);
\coordinate (B) at (1.2,-1.2);
\coordinate (C) at (4.5,0);
\coordinate (D) at (2,2.5);
\draw[thick] (D) -- (A) -- (B) -- (C) -- (D);
\draw[thick] (D) -- (B);
\draw[dashed] (A) -- (C);
\fill (A) circle (1.5pt) node[left] {$A$};
\fill (B) circle (1.5pt) node[below] {$B$};
\fill (C) circle (1.5pt) node[right] {$C$};
\fill (D) circle (1.5pt) node[above] {$D$};
\end{tikzpicture}
\end{center}'''

    variant = random.choice([1, 2, 3])
    if variant == 1:
        correct = r"$\vec{AB} - \vec{AC} = \vec{DB} - \vec{DC}$"
        wrongs = [
            r"$\vec{AB} - \vec{AD} = \vec{CD} + \vec{BC}$",
            r"$\vec{AC} - \vec{AD} = \vec{BD} - \vec{BC}$",
            r"$\vec{BC} + \vec{AB} = \vec{DA} - \vec{DC}$"
        ]
        loi_giai = r'''Theo quy tắc phép trừ hai vectơ có cùng điểm đầu:
Ta có $\vec{AB} - \vec{AC} = \vec{CB}$ và $\vec{DB} - \vec{DC} = \vec{CB}$.
Do đó $\vec{AB} - \vec{AC} = \vec{DB} - \vec{DC}$.'''
    elif variant == 2:
        correct = r"$\vec{AC} - \vec{AD} = \vec{BC} - \vec{BD}$"
        wrongs = [
            r"$\vec{AC} - \vec{AD} = \vec{BD} - \vec{BC}$",
            r"$\vec{AB} - \vec{AC} = \vec{CD} - \vec{BD}$",
            r"$\vec{AD} + \vec{DC} = \vec{BA} + \vec{BC}$"
        ]
        loi_giai = r'''Theo quy tắc phép trừ vectơ:
$\vec{AC} - \vec{AD} = \vec{DC}$ và $\vec{BC} - \vec{BD} = \vec{DC}$.
Do đó $\vec{AC} - \vec{AD} = \vec{BC} - \vec{BD}$.'''
    else:
        correct = r"$\vec{AB} + \vec{BC} = \vec{AD} + \vec{DC}$"
        wrongs = [
            r"$\vec{AB} + \vec{BC} = \vec{CD} + \vec{DA}$",
            r"$\vec{AB} - \vec{AD} = \vec{BC} - \vec{DC}$",
            r"$\vec{DA} - \vec{DC} = \vec{BA} - \vec{BC}$"
        ]
        loi_giai = r'''Theo quy tắc ba điểm của phép cộng vectơ:
$\vec{AB} + \vec{BC} = \vec{AC}$ và $\vec{AD} + \vec{DC} = \vec{AC}$.
Do đó $\vec{AB} + \vec{BC} = \vec{AD} + \vec{DC}$.'''

    choices = shuffle_choices(correct, wrongs)
    return caudan, choices, loi_giai


def VectoKG_MC_CongLucKeoTauXaLan():
    """Toán thực tế: Tàu kéo xà lan trên biển sinh công"""
    s_km = random.choice([2, 3, 4, 5])
    F = random.choice([1500, 2000, 2400, 3000, 3500])
    alpha_deg = random.choice([30, 45, 60])
    
    s_m = s_km * 1000
    cos_val = math.cos(math.radians(alpha_deg))
    A_exact = F * s_m * cos_val
    ans = round(A_exact)
    
    def fmt_num(val):
        return f"{val:,}".replace(",", " ")
        
    ans_str = fmt_num(ans)
    w1_str = fmt_num(ans + random.choice([120100, 131000, 115200]))
    w2_str = fmt_num(abs(ans - random.choice([980000, 1020000, 1079000])))
    w3_str = fmt_num(round(F * s_m * math.sin(math.radians(alpha_deg))))
    
    caudan = fr'''Một tàu kéo một xà lan trên biển di chuyển được ${s_km}\text{{ km}}$ với một lực kéo có cường độ ${F}\text{{ N}}$ và có phương hợp với phương dịch chuyển một góc ${alpha_deg}^\circ$ (xem hình minh họa). Tính công thực hiện bởi lực kéo nói trên (kết quả làm tròn đến hàng đơn vị của Jun).
\begin{{center}}
\begin{{tikzpicture}}[scale=0.9,>=stealth]
\draw[fill=gray!40] (0,0) rectangle (1.4,0.35);
\node at (0.7,0.18) {{\footnotesize Xà lan}};
\draw[->,thick] (1.4,0) -- (6.5,0) node[below] {{$\vec{{d}}$}};
\draw[->,thick] (1.4,0) -- ++({alpha_deg}:3.5) node[above] {{$\vec{{F}}$}};
\draw (2.4,0) arc (0:{alpha_deg}:1) node[midway,right=2pt] {{${alpha_deg}^\circ$}};
\draw[thick,fill=gray!20] (4.5,0.2) -- (5.8,0.2) -- (6.2,0.7) -- (4.1,0.7) -- cycle;
\draw[thick] (4.8,0.7) rectangle (5.5,1.1);
\node at (5.1,0.45) {{\footnotesize Tàu}};
\end{{tikzpicture}}
\end{{center}}'''

    choices = shuffle_choices(f"${ans_str}\\text{{ (J)}}$", [
        f"${w1_str}\\text{{ (J)}}$",
        f"${w2_str}\\text{{ (J)}}$",
        f"${w3_str}\\text{{ (J)}}$"
    ])
    
    loi_giai = fr'''Đổi ${s_km}\text{{ km}} = {s_m}\text{{ m}}$.
Công thực hiện bởi lực kéo $\vec{{F}}$ khi vật dịch chuyển vectơ độ dời $\vec{{d}}$ là:
\[ A = \vec{{F}} \cdot \vec{{d}} = |\vec{{F}}| \cdot |\vec{{d}}| \cdot \cos(\vec{{F}}, \vec{{d}}) = {F} \cdot {s_m} \cdot \cos {alpha_deg}^\circ \approx {ans_str}\text{{ (J)}}. \]'''

    return caudan, choices, loi_giai


def ToaDoOxyz_MC_TimM_DoDaiDoanThang():
    """Tìm m để độ dài đoạn thẳng AB = d (nghiệm nguyên đẹp)"""
    quadruples = [
        (6, 3, 2, 7),   # 36 + 9 + 4 = 49 = 7^2
        (2, 3, 6, 7),
        (4, 4, 2, 6),   # 16 + 16 + 4 = 36 = 6^2
        (8, 4, 1, 9),   # 64 + 16 + 1 = 81 = 9^2
        (12, 4, 3, 13), # 144 + 16 + 9 = 169 = 13^2
        (6, 6, 7, 11),  # 36 + 36 + 49 = 121 = 11^2
    ]
    k, dy, dz, d = random.choice(quadruples)
    
    xA = random.choice([1, 2, 3, 4, -1, -2, -3])
    yA = random.choice([-2, -1, 1, 2])
    zA = random.choice([1, 3, 5, -2])
    
    yB = yA + dy
    zB = zA + dz
    
    m1 = xA + k
    m2 = xA - k
    
    caudan = fr'''Trong không gian $Oxyz$, cho hai điểm $A({xA}; {yA}; {zA})$ và $B(m; {yB}; {zB})$. Tìm tất cả các giá trị của $m$ để độ dài đoạn thẳng $AB = {d}$.'''
    
    correct_str = fr"$m = {m1}\text{{ hoặc }} m = {m2}$"
    w1 = fr"$m = {m1}\text{{ hoặc }} m = {-m2}$"
    w2 = fr"$m = {-m1}\text{{ hoặc }} m = {m2}$"
    w3 = fr"$m = {m1 + 2}\text{{ hoặc }} m = {m2 - 2}$"
    
    choices = shuffle_choices(correct_str, [w1, w2, w3])
    
    rem_sq = dy**2 + dz**2
    d_sq = d**2
    k_sq = k**2
    
    loi_giai = fr'''Ta có:
\[ AB = \sqrt{{(m - {xA})^2 + ({yB} - ({yA}))^2 + ({zB} - ({zA}))^2}} = \sqrt{{(m - {xA})^2 + {rem_sq}}}. \]
Theo giả thiết:
\[ AB = {d} \iff (m - {xA})^2 + {rem_sq} = {d_sq} \iff (m - {xA})^2 = {k_sq} \iff \left[\begin{{aligned}} m - {xA} &= {k} \\ m - {xA} &= -{k} \end{{aligned}}\right. \iff \left[\begin{{aligned}} m &= {m1} \\ m &= {m2}. \end{{aligned}}\right. \]
Vậy có hai giá trị thỏa mãn là $m = {m1}$ hoặc $m = {m2}$.'''

    return caudan, choices, loi_giai


def ToaDoOxyz_MC_TimM_TamGiacVuong():
    """Tìm m để tam giác ABC vuông tại B (nghiệm m nguyên đẹp)"""
    m_ans = random.choice([-10, -5, -2, -1, 3, 4, 6, 8])
    
    xB = random.choice([0, 1, 2, -1])
    yB = random.choice([1, 2, 3, -1])
    zB = random.choice([2, 3, 4, -2])
    
    u1 = random.choice([1, 2, 3, -1, -2])
    u2 = random.choice([1, -1])
    u3 = 1
    
    xA = xB + u1
    yA = yB + u2
    zA = zB + u3
    
    v1 = random.choice([1, 2, 3, -1, -2])
    v3 = -u1 * v1 - u2 * (m_ans - yB)
    
    xC = xB + v1
    zC = zB + v3
    
    caudan = fr'''Trong không gian $Oxyz$, cho ba điểm $A({xA}; {yA}; {zA}), B({xB}; {yB}; {zB})$ và $C({xC}; m; {zC})$. Tìm giá trị của tham số $m$ để tam giác $ABC$ vuông tại $B$.'''
    
    correct_str = fr"$m = {m_ans}$"
    w1 = fr"$m = {-m_ans}$"
    w2 = fr"$m = {m_ans + 4}$"
    w3 = fr"$m = {m_ans - 5}$"
    
    choices = shuffle_choices(correct_str, [w1, w2, w3])
    
    c1 = u1 * v1
    c3 = u3 * v3
    sum_c = c1 + c3
    
    loi_giai = fr'''Ta có các vectơ:
\[ \vec{{BA}} = ({u1}; {u2}; {u3}), \quad \vec{{BC}} = ({v1}; m - {yB}; {v3}). \]
Tam giác $ABC$ vuông tại $B$ khi và chỉ khi:
\[ \vec{{BA}} \bot \vec{{BC}} \iff \vec{{BA}} \cdot \vec{{BC}} = 0 \]
\[ \iff {u1} \cdot ({v1}) + ({u2})(m - {yB}) + {u3} \cdot ({v3}) = 0 \]
\[ \iff {c1} + {u2}(m - {yB}) + {c3} = 0 \iff {u2}(m - {yB}) = {-sum_c} \iff m = {m_ans}. \]
Vậy $m = {m_ans}$.'''

    return caudan, choices, loi_giai


# ------------------------------------------------------------------------------
# Mở rộng Chương II: Quy tắc hình hộp, lăng trụ, chóp tứ giác đều & Đúng/Sai Oxyz
# ------------------------------------------------------------------------------

def VectoKG_MC_QuyTacHinhHop():
    """Quy tắc hình hộp: AA1 + AB + AD = AC1 (kèm hình vẽ TikZ)"""
    variant = random.choice([1, 2, 3])
    if variant == 1:
        caudan = r'''Cho hình hộp $ABCD.A_1B_1C_1D_1$ (xem hình dưới). Tìm khẳng định đúng.
\begin{center}
\begin{tikzpicture}[scale=0.85,line join=round,line cap=round,>=stealth]
\coordinate (A) at (0.8,0.8);
\coordinate (B) at (0,0);
\coordinate (C) at (3.2,0);
\coordinate (D) at (4,0.8);
\coordinate (A1) at (0.8,2.2);
\coordinate (B1) at (0,1.4);
\coordinate (C1) at (3.2,1.4);
\coordinate (D1) at (4,2.2);
\draw[thick] (B1)--(C1)--(D1)--(A1)--cycle;
\draw[thick] (B)--(C)--(D);
\draw[thick] (B)--(B1);
\draw[thick] (C)--(C1);
\draw[thick] (D)--(D1);
\draw[dashed] (A)--(B);
\draw[dashed] (A)--(D);
\draw[dashed] (A)--(A1);
\node[left] at (A) {$A$};
\node[below left] at (B) {$B$};
\node[below right] at (C) {$C$};
\node[right] at (D) {$D$};
\node[above left] at (A1) {$A_1$};
\node[left] at (B1) {$B_1$};
\node[right] at (C1) {$C_1$};
\node[above right] at (D1) {$D_1$};
\end{tikzpicture}
\end{center}'''
        correct = r"$\vec{AA_1} + \vec{AB} + \vec{AD} = \vec{AC_1}$"
        wrongs = [
            r"$\vec{AA_1} + \vec{AB} + \vec{AD} = \vec{CA_1}$",
            r"$\vec{AA_1} + \vec{AB} + \vec{AD} = \vec{A_1C_1}$",
            r"$\vec{AA_1} + \vec{AB} + \vec{AD} = \vec{C_1A_1}$"
        ]
        loi_giai = r'''Theo quy tắc hình hộp: Tổng ba vectơ xuất phát từ cùng một đỉnh bằng vectơ đường chéo xuất phát từ đỉnh đó:
\[ \vec{AA_1} + \vec{AB} + \vec{AD} = \vec{AC_1}. \]'''
    elif variant == 2:
        caudan = r'''Cho hình hộp $ABCD.EFGH$ (xem hình dưới). Tìm khẳng định đúng.
\begin{center}
\begin{tikzpicture}[scale=0.85,line join=round,line cap=round,>=stealth]
\coordinate (A) at (0.8,0.8);
\coordinate (B) at (0,0);
\coordinate (C) at (3.2,0);
\coordinate (D) at (4,0.8);
\coordinate (E) at (0.8,2.2);
\coordinate (F) at (0,1.4);
\coordinate (G) at (3.2,1.4);
\coordinate (H) at (4,2.2);
\draw[thick] (F)--(G)--(H)--(E)--cycle;
\draw[thick] (B)--(C)--(D);
\draw[thick] (B)--(F);
\draw[thick] (C)--(G);
\draw[thick] (D)--(H);
\draw[dashed] (A)--(B);
\draw[dashed] (A)--(D);
\draw[dashed] (A)--(E);
\node[left] at (A) {$A$};
\node[below left] at (B) {$B$};
\node[below right] at (C) {$C$};
\node[right] at (D) {$D$};
\node[above left] at (E) {$E$};
\node[left] at (F) {$F$};
\node[right] at (G) {$G$};
\node[above right] at (H) {$H$};
\end{tikzpicture}
\end{center}'''
        correct = r"$\vec{AE} + \vec{AB} + \vec{AD} = \vec{AG}$"
        wrongs = [
            r"$\vec{AE} + \vec{AB} + \vec{AD} = \vec{CE}$",
            r"$\vec{AE} + \vec{AB} + \vec{AD} = \vec{GE}$",
            r"$\vec{AE} + \vec{AB} + \vec{AD} = \vec{EG}$"
        ]
        loi_giai = r'''Theo quy tắc hình hộp: Tổng ba vectơ xuất phát từ đỉnh $A$ có chung điểm đầu bằng vectơ đường chéo xuất phát từ $A$:
\[ \vec{AE} + \vec{AB} + \vec{AD} = \vec{AG}. \]'''
    else:
        caudan = r'''Cho hình hộp $ABCD.A'B'C'D'$. Khẳng định nào sau đây đúng?'''
        correct = r"$\vec{AB} + \vec{AD} + \vec{AA'} = \vec{AC'}$"
        wrongs = [
            r"$\vec{AB} + \vec{AD} + \vec{AA'} = \vec{CA'}$",
            r"$\vec{AB} + \vec{AD} + \vec{AA'} = \vec{BD'}$",
            r"$\vec{AB} + \vec{AD} + \vec{AA'} = \vec{DB'}$"
        ]
        loi_giai = r'''Theo quy tắc hình hộp: $\vec{AB} + \vec{AD} + \vec{AA'} = \vec{AC'}$.'''

    choices = shuffle_choices(correct, wrongs)
    return caudan, choices, loi_giai


def VectoKG_MC_HeThucVectoHinhHop_TimSai():
    """Hệ thức vectơ trong hình hộp: tìm khẳng định sai (kèm hình vẽ TikZ)"""
    caudan = r'''Cho hình hộp $ABCD.A'B'C'D'$ (xem hình dưới). Trong các khẳng định sau, khẳng định nào \textbf{sai}?
\begin{center}
\begin{tikzpicture}[scale=0.85,line join=round,line cap=round,>=stealth]
\coordinate (A) at (0.8,0.8);
\coordinate (B) at (0,0);
\coordinate (C) at (3.2,0);
\coordinate (D) at (4,0.8);
\coordinate (A1) at (0.8,2.2);
\coordinate (B1) at (0,1.4);
\coordinate (C1) at (3.2,1.4);
\coordinate (D1) at (4,2.2);
\draw[thick] (B1)--(C1)--(D1)--(A1)--cycle;
\draw[thick] (B)--(C)--(D);
\draw[thick] (B)--(B1);
\draw[thick] (C)--(C1);
\draw[thick] (D)--(D1);
\draw[dashed] (A)--(B);
\draw[dashed] (A)--(D);
\draw[dashed] (A)--(A1);
\node[left] at (A) {$A$};
\node[below left] at (B) {$B$};
\node[below right] at (C) {$C$};
\node[right] at (D) {$D$};
\node[above left] at (A1) {$A'$};
\node[left] at (B1) {$B'$};
\node[right] at (C1) {$C'$};
\node[above right] at (D1) {$D'$};
\end{tikzpicture}
\end{center}'''

    variant = random.choice([1, 2])
    if variant == 1:
        wrong_stmt = r"$\vec{AC} - \vec{D'D} = \vec{0}$"
        true_stmts = [
            r"$\vec{AB} + \vec{B'D'} = \vec{AD}$",
            r"$\vec{AB} + \vec{CD} = \vec{0}$",
            r"$\vec{AC'} + \vec{A'C} = 2\vec{AC}$"
        ]
        loi_giai = r'''Xét từng khẳng định:
\begin{itemize}
\item Ta có $\vec{B'D'} = \vec{BD}$ nên $\vec{AB} + \vec{B'D'} = \vec{AB} + \vec{BD} = \vec{AD}$ (đúng).
\item Vì $ABCD$ là hình bình hành nên $\vec{CD} = -\vec{AB} \implies \vec{AB} + \vec{CD} = \vec{0}$ (đúng).
\item Ta có $\vec{AC'} = \vec{AC} + \vec{CC'}$ và $\vec{A'C} = \vec{AC} - \vec{AA'} = \vec{AC} - \vec{CC'}$, do đó $\vec{AC'} + \vec{A'C} = 2\vec{AC}$ (đúng).
\item Ta có $\vec{AC} - \vec{D'D} = \vec{AC} + \vec{DD'} = \vec{AC} + \vec{CC'} = \vec{AC'} \ne \vec{0}$. Do đó khẳng định $\vec{AC} - \vec{D'D} = \vec{0}$ là sai.
\end{itemize}'''
    else:
        wrong_stmt = r"$\vec{AA'} + \vec{CC'} = \vec{0}$"
        true_stmts = [
            r"$\vec{AB} + \vec{AD} = \vec{A'C'} $",
            r"$\vec{BC} + \vec{D'A'} = \vec{0}$",
            r"$\vec{BD} + \vec{D'C'} = \vec{BC}$"
        ]
        loi_giai = r'''Xét từng khẳng định:
\begin{itemize}
\item $\vec{AA'} = \vec{CC'}$ (hai vectơ cùng phương, cùng hướng, cùng độ dài) nên $\vec{AA'} + \vec{CC'} = 2\vec{AA'} \ne \vec{0}$. Vậy khẳng định $\vec{AA'} + \vec{CC'} = \vec{0}$ là sai.
\item $\vec{AB} + \vec{AD} = \vec{AC} = \vec{A'C'}$ (đúng).
\item $\vec{D'A'} = -\vec{BC} \implies \vec{BC} + \vec{D'A'} = \vec{0}$ (đúng).
\item $\vec{BD} + \vec{D'C'} = \vec{BD} + \vec{DC} = \vec{BC}$ (đúng).
\end{itemize}'''

    choices = shuffle_choices(wrong_stmt, true_stmts)
    return caudan, choices, loi_giai


def VectoKG_MC_VectoLangTru():
    """Quy tắc cộng vectơ trong lăng trụ tam giác (kèm hình vẽ TikZ)"""
    variant = random.choice([1, 2, 3])
    if variant == 1:
        caudan = r'''Cho hình lăng trụ $ABC.A'B'C'$ (xem hình dưới). Phát biểu nào sau đây là \textbf{đúng}?
\begin{center}
\begin{tikzpicture}[scale=0.85,line join=round,line cap=round,>=stealth]
\coordinate (A) at (0,0);
\coordinate (B) at (1.4,-0.8);
\coordinate (C) at (3.5,0);
\coordinate (A1) at (0.4,2.5);
\coordinate (B1) at (1.8,1.7);
\coordinate (C1) at (3.9,2.5);
\draw[thick] (A1)--(B1)--(C1)--cycle;
\draw[thick] (A)--(B)--(C);
\draw[dashed] (A)--(C);
\draw[thick] (A)--(A1);
\draw[thick] (B)--(B1);
\draw[thick] (C)--(C1);
\node[left] at (A) {$A$};
\node[below] at (B) {$B$};
\node[right] at (C) {$C$};
\node[left] at (A1) {$A'$};
\node[left] at (B1) {$B'$};
\node[right] at (C1) {$C'$};
\end{tikzpicture}
\end{center}'''
        correct = r"$\vec{BA} + \vec{A'C'} = \vec{BC}$"
        wrongs = [
            r"$\vec{BA} + \vec{A'C'} = \vec{A'A}$",
            r"$\vec{BA} + \vec{A'C'} = \vec{BC'}$",
            r"$\vec{BA} + \vec{A'C'} = \vec{C'B'}$"
        ]
        loi_giai = r'''Vì $ABC.A'B'C'$ là hình lăng trụ nên mặt bên $ACC'A'$ là hình bình hành, suy ra $\vec{A'C'} = \vec{AC}$.
Khi đó:
\[ \vec{BA} + \vec{A'C'} = \vec{BA} + \vec{AC} = \vec{BC}. \]
Vậy phát biểu đúng là $\vec{BA} + \vec{A'C'} = \vec{BC}$.'''
    elif variant == 2:
        caudan = r'''Cho hình lăng trụ $ABC.A'B'C'$. Phát biểu nào sau đây là \textbf{đúng}?'''
        correct = r"$\vec{CA} + \vec{A'B'} = \vec{CB}$"
        wrongs = [
            r"$\vec{CA} + \vec{A'B'} = \vec{BC}$",
            r"$\vec{CA} + \vec{A'B'} = \vec{CC'}$",
            r"$\vec{CA} + \vec{A'B'} = \vec{B'C'}$"
        ]
        loi_giai = r'''Vì $\vec{A'B'} = \vec{AB}$ nên:
\[ \vec{CA} + \vec{A'B'} = \vec{CA} + \vec{AB} = \vec{CB}. \]'''
    else:
        caudan = r'''Cho hình lăng trụ $ABC.A'B'C'$. Phát biểu nào sau đây là \textbf{đúng}?'''
        correct = r"$\vec{AB} + \vec{B'C'} = \vec{AC}$"
        wrongs = [
            r"$\vec{AB} + \vec{B'C'} = \vec{CA}$",
            r"$\vec{AB} + \vec{B'C'} = \vec{AA'}$",
            r"$\vec{AB} + \vec{B'C'} = \vec{AC'}$"
        ]
        loi_giai = r'''Vì $\vec{B'C'} = \vec{BC}$ nên:
\[ \vec{AB} + \vec{B'C'} = \vec{AB} + \vec{BC} = \vec{AC}. \]'''

    choices = shuffle_choices(correct, wrongs)
    return caudan, choices, loi_giai


def VectoKG_MC_VectoHinhChopTuGiacDeu():
    """Tổng vectơ trong hình chóp tứ giác đều S.ABCD: SA+SB+SC+SD = 4SO (kèm TikZ)"""
    caudan = r'''Cho hình chóp tứ giác đều $S.ABCD$ (xem hình dưới). Gọi $O$ là giao điểm của $AC$ và $BD$. Phát biểu nào sau đây là \textbf{đúng}?
\begin{center}
\begin{tikzpicture}[scale=0.85,line join=round,line cap=round,>=stealth]
\coordinate (A) at (1,0.8);
\coordinate (B) at (0,-0.6);
\coordinate (C) at (3,-0.6);
\coordinate (D) at (4,0.8);
\coordinate (O) at (2,0.1);
\coordinate (S) at (2,2.8);
\draw[thick] (S)--(B)--(C)--(D)--(S)--(C);
\draw[dashed] (S)--(A)--(B);
\draw[dashed] (A)--(D);
\draw[dashed] (A)--(C);
\draw[dashed] (B)--(D);
\draw[dashed] (S)--(O);
\node[above] at (S) {$S$};
\node[left] at (A) {$A$};
\node[below left] at (B) {$B$};
\node[below right] at (C) {$C$};
\node[right] at (D) {$D$};
\node[below] at (O) {$O$};
\end{tikzpicture}
\end{center}'''

    variant = random.choice([1, 2])
    if variant == 1:
        correct = r"$\vec{SA} + \vec{SB} + \vec{SC} + \vec{SD} = 4\vec{SO}$"
        wrongs = [
            r"$\vec{SA} + \vec{SB} + \vec{SC} + \vec{SD} = 2\vec{SO}$",
            r"$\vec{SA} + \vec{SB} + \vec{SC} + \vec{SD} = \vec{SO}$",
            r"$\vec{SA} + \vec{SB} + \vec{SC} + \vec{SD} = \vec{0}$"
        ]
        loi_giai = r'''Vì đáy $ABCD$ là hình vuông tâm $O$ nên $O$ là trung điểm của $AC$ và $BD$.
Theo tính chất trung điểm của đoạn thẳng:
\[ \vec{SA} + \vec{SC} = 2\vec{SO}, \quad \vec{SB} + \vec{SD} = 2\vec{SO}. \]
Cộng vế với vế hai đẳng thức trên, ta được:
\[ \vec{SA} + \vec{SB} + \vec{SC} + \vec{SD} = 2\vec{SO} + 2\vec{SO} = 4\vec{SO}. \]'''
    else:
        correct = r"$\vec{OA} + \vec{OB} + \vec{OC} + \vec{OD} = \vec{0}$"
        wrongs = [
            r"$\vec{OA} + \vec{OB} + \vec{OC} + \vec{OD} = \vec{SO}$",
            r"$\vec{OA} + \vec{OB} + \vec{OC} + \vec{OD} = 2\vec{SO}$",
            r"$\vec{OA} + \vec{OB} + \vec{OC} + \vec{OD} = 4\vec{SO}$"
        ]
        loi_giai = r'''Vì $O$ là trung điểm của $AC$ và $BD$ nên:
$\vec{OA} + \vec{OC} = \vec{0}$ và $\vec{OB} + \vec{OD} = \vec{0}$.
Do đó $\vec{OA} + \vec{OB} + \vec{OC} + \vec{OD} = \vec{0}$.'''

    choices = shuffle_choices(correct, wrongs)
    return caudan, choices, loi_giai


def ToaDoOxyz_TF_KhaoSat3Vecto():
    """Đúng/Sai: Khảo sát độ dài, cosin góc, tính vuông góc của ba vectơ"""
    a1, a2, a3 = random.choice([(-1, 1, 0), (1, -1, 0), (0, 1, 1), (-1, 0, 1)])
    b1, b2, b3 = random.choice([(1, 1, 0), (1, 0, 1), (0, 1, -1), (1, -1, 0)])
    c1, c2, c3 = random.choice([(1, 1, 1), (1, -1, 1), (-1, 1, 1), (2, 1, 0)])
    
    len_a_sq = a1**2 + a2**2 + a3**2
    len_c_sq = c1**2 + c2**2 + c3**2
    dot_ac = a1*c1 + a2*c2 + a3*c3
    dot_bc = b1*c1 + b2*c2 + b3*c3
    
    caudan = fr'''Cho ba vec-tơ $\vec{{a}} = ({a1}; {a2}; {a3})$, $\vec{{b}} = ({b1}; {b2}; {b3})$ và $\vec{{c}} = ({c1}; {c2}; {c3})$.'''
    
    exact_len_a = math.sqrt(len_a_sq)
    if exact_len_a.is_integer():
        len_a_true_str = str(int(exact_len_a))
    else:
        len_a_true_str = fr"\sqrt{{{len_a_sq}}}"
    len_a_false_str = str(int(exact_len_a) + 1 if exact_len_a.is_integer() else len_a_sq)
    item_a = (
        fr"|\vec{{a}}| = {len_a_true_str}",
        fr"|\vec{{a}}| = {len_a_false_str}",
        fr"Ta có $|\vec{{a}}| = \sqrt{{({a1})^2 + ({a2})^2 + ({a3})^2}} = {len_a_true_str}$.",
        fr"Ta có $|\vec{{a}}| = \sqrt{{({a1})^2 + ({a2})^2 + ({a3})^2}} = {len_a_true_str} \ne {len_a_false_str}$."
    )
    
    exact_len_c = math.sqrt(len_c_sq)
    if exact_len_c.is_integer():
        len_c_true_str = str(int(exact_len_c))
    else:
        len_c_true_str = fr"\sqrt{{{len_c_sq}}}"
    len_c_false_str = fr"\sqrt{{{len_c_sq + 2}}}"
    item_b = (
        fr"|\vec{{c}}| = {len_c_true_str}",
        fr"|\vec{{c}}| = {len_c_false_str}",
        fr"Ta có $|\vec{{c}}| = \sqrt{{({c1})^2 + ({c2})^2 + ({c3})^2}} = {len_c_true_str}$.",
        fr"Ta có $|\vec{{c}}| = \sqrt{{({c1})^2 + ({c2})^2 + ({c3})^2}} = {len_c_true_str} \ne {len_c_false_str}$."
    )
    
    den_prod = len_a_sq * len_c_sq
    cos_true_str = fr"\dfrac{{{dot_ac}}}{{\sqrt{{{den_prod}}}}}" if not math.sqrt(den_prod).is_integer() else fr"\dfrac{{{dot_ac}}}{{{int(math.sqrt(den_prod))}}}"
    cos_false_str = fr"\dfrac{{{dot_ac + 1}}}{{\sqrt{{{den_prod}}}}}"
    item_c = (
        fr"\cos(\vec{{a}}, \vec{{c}}) = {cos_true_str}",
        fr"\cos(\vec{{a}}, \vec{{c}}) = {cos_false_str}",
        fr"Ta có $\vec{{a}} \cdot \vec{{c}} = ({a1})({c1}) + ({a2})({c2}) + ({a3})({c3}) = {dot_ac}$. Suy ra $\cos(\vec{{a}}, \vec{{c}}) = \dfrac{{\vec{{a}} \cdot \vec{{c}}}}{{|\vec{{a}}| \cdot |\vec{{c}}|}} = {cos_true_str}$.",
        fr"Ta có $\cos(\vec{{a}}, \vec{{c}}) = \dfrac{{\vec{{a}} \cdot \vec{{c}}}}{{|\vec{{a}}| \cdot |\vec{{c}}|}} = {cos_true_str} \ne {cos_false_str}$."
    )
    
    is_perp = (dot_bc == 0)
    if is_perp:
        item_d = (
            r"\vec{b} \bot \vec{c}",
            r"\vec{b} \text{ không vuông góc với } \vec{c}",
            fr"Ta có $\vec{{b}} \cdot \vec{{c}} = ({b1})({c1}) + ({b2})({c2}) + ({b3})({c3}) = {dot_bc} = 0 \implies \vec{{b}} \bot \vec{{c}}$.",
            fr"Vì $\vec{{b}} \cdot \vec{{c}} = 0$ nên $\vec{{b}} \bot \vec{{c}}$."
        )
    else:
        item_d = (
            r"\vec{b} \text{ không vuông góc với } \vec{c}",
            r"\vec{b} \bot \vec{c}",
            fr"Ta có $\vec{{b}} \cdot \vec{{c}} = ({b1})({c1}) + ({b2})({c2}) + ({b3})({c3}) = {dot_bc} \ne 0$ nên $\vec{{b}}$ không vuông góc với $\vec{{c}}$.",
            fr"Ta có $\vec{{b}} \cdot \vec{{c}} = {dot_bc} \ne 0$ nên khẳng định $\vec{{b}} \bot \vec{{c}}$ là sai."
        )

    items_data = [item_a, item_b, item_c, item_d]
    choices, loi_giai = make_tf_choices(items_data)
    return caudan, choices, loi_giai


def ToaDoOxyz_TF_HinhBinhHanh_DienTich():
    """Đúng/Sai: Hình bình hành ABCD, cos góc, diện tích tam giác, tọa độ đỉnh D"""
    xA = random.choice([-1, 0, 1])
    yA = random.choice([2, 3, 1])
    zA = random.choice([0, 1, -1])
    
    u1, u2, u3 = random.choice([(2, -1, -1), (1, -2, 1), (2, 1, -1), (1, 1, -2)])
    xB = xA + u1
    yB = yA + u2
    zB = zA + u3
    
    v1, v2, v3 = random.choice([(2, -2, -2), (1, -1, 1), (0, -1, 2), (2, 0, -1)])
    xC = xA + v1
    yC = yA + v2
    zC = zA + v3
    
    xD = xA + xC - xB
    yD = yA + yC - yB
    zD = zA + zC - zB
    
    caudan = fr'''Trong không gian với hệ trục toạ độ $Oxyz$, cho hình bình hành $ABCD$ có $A({xA}; {yA}; {zA}), B({xB}; {yB}; {zB}), C({xC}; {yC}; {zC})$.'''
    
    item_a = (
        fr"\vec{{AB}} = ({u1}; {u2}; {u3})",
        fr"\vec{{AB}} = ({-u1}; {-u2}; {-u3})",
        fr"Tọa độ vectơ $\vec{{AB}} = ({xB} - ({xA}); {yB} - ({yA}); {zB} - ({zA})) = ({u1}; {u2}; {u3})$.",
        fr"Tọa độ vectơ $\vec{{AB}} = ({u1}; {u2}; {u3}) \ne ({-u1}; {-u2}; {-u3})$."
    )
    
    dot_prod = u1*v1 + u2*v2 + u3*v3
    len_ab_sq = u1**2 + u2**2 + u3**2
    len_ac_sq = v1**2 + v2**2 + v3**2
    den_sq = len_ab_sq * len_ac_sq
    
    cos_tex = fr"\dfrac{{{dot_prod}}}{{\sqrt{{{den_sq}}}}}"
    item_b = (
        fr"\cos(\vec{{AB}}, \vec{{AC}}) = {cos_tex}",
        fr"\cos(\vec{{AB}}, \vec{{AC}}) = \dfrac{{{dot_prod + 1}}}{{\sqrt{{{den_sq}}}}}",
        fr"Ta có $\cos(\vec{{AB}}, \vec{{AC}}) = \dfrac{{\vec{{AB}} \cdot \vec{{AC}}}}{{|\vec{{AB}}| \cdot |\vec{{AC}}|}} = \dfrac{{{dot_prod}}}{{\sqrt{{{len_ab_sq}}} \cdot \sqrt{{{len_ac_sq}}}}} = {cos_tex}$.",
        fr"Ta có $\cos(\vec{{AB}}, \vec{{AC}}) = {cos_tex}$."
    )
    
    cx = u2*v3 - u3*v2
    cy = u3*v1 - u1*v3
    cz = u1*v2 - u2*v1
    cross_sq = cx**2 + cy**2 + cz**2
    s_val = 0.5 * math.sqrt(cross_sq)
    s_tex = fr"\dfrac{{\sqrt{{{cross_sq}}}}}{{2}}" if not math.sqrt(cross_sq).is_integer() else (str(int(s_val)) if s_val.is_integer() else fr"\dfrac{{{int(math.sqrt(cross_sq))}}}{{2}}")
    s_wrong_tex = fr"\sqrt{{{cross_sq}}}"
    item_c = (
        fr"\text{{Diện tích của tam giác }} ABC \text{{ bằng }} {s_tex}",
        fr"\text{{Diện tích của tam giác }} ABC \text{{ bằng }} {s_wrong_tex}",
        fr"Diện tích tam giác $ABC$: $S_{{ABC}} = \dfrac{{1}}{{2}} |[\vec{{AB}}, \vec{{AC}}]| = \dfrac{{1}}{{2}} \sqrt{{({cx})^2 + ({cy})^2 + ({cz})^2}} = {s_tex}$.",
        fr"Diện tích tam giác $ABC$ là $S = {s_tex} \ne {s_wrong_tex}$."
    )
    
    item_d = (
        fr"\text{{Toạ độ của điểm }} D \text{{ là }} ({xD}; {yD}; {zD})",
        fr"\text{{Toạ độ của điểm }} D \text{{ là }} ({xD + 1}; {yD}; {zD - 1})",
        fr"Vì $ABCD$ là hình bình hành nên $\vec{{AD}} = \vec{{BC}} \iff (x_D - ({xA}); y_D - ({yA}); z_D - ({zA})) = ({xC} - ({xB}); {yC} - ({yB}); {zC} - ({zB})) \implies D({xD}; {yD}; {zD})$.",
        fr"Tọa độ đỉnh $D$ là $({xD}; {yD}; {zD})$."
    )

    items_data = [item_a, item_b, item_c, item_d]
    choices, loi_giai = make_tf_choices(items_data)
    return caudan, choices, loi_giai


def ToaDoOxyz_TF_BaDiemThangHang():
    """Đúng/Sai: Cho ba điểm A, B, C, xét vectơ AB, AC, tính cùng phương và thẳng hàng"""
    xA = random.choice([1, 2, -1])
    yA = random.choice([-2, 1, 0])
    zA = random.choice([3, 2, -1])
    
    u1, u2, u3 = random.choice([(-3, 3, -1), (2, -1, 3), (-2, 4, -2), (1, -2, 2)])
    xB = xA + u1
    yB = yA + u2
    zB = zA + u3
    
    v1, v2, v3 = random.choice([(2, 1, -1), (-2, -1, 1), (3, 1, 0), (1, 2, -1)])
    while u1*v2 == u2*v1 and u1*v3 == u3*v1:
        v1 += 1
    
    xC = xA + v1
    yC = yA + v2
    zC = zA + v3
    
    caudan = fr'''Cho các điểm $A({xA}; {yA}; {zA}), B({xB}; {yB}; {zB}), C({xC}; {yC}; {zC})$.'''
    
    item_a = (
        fr"\vec{{AB}} = ({u1}; {u2}; {u3})",
        fr"\vec{{AB}} = ({-u1}; {-u2}; {-u3})",
        fr"$\vec{{AB}} = ({xB} - ({xA}); {yB} - ({yA}); {zB} - ({zA})) = ({u1}; {u2}; {u3})$.",
        fr"$\vec{{AB}} = ({u1}; {u2}; {u3}) \ne ({-u1}; {-u2}; {-u3})$."
    )
    
    item_b = (
        fr"\vec{{AC}} = ({v1}; {v2}; {v3})",
        fr"\vec{{AC}} = ({v1 + 1}; {v2}; {v3 - 1})",
        fr"$\vec{{AC}} = ({xC} - ({xA}); {yC} - ({yA}); {zC} - ({zA})) = ({v1}; {v2}; {v3})$.",
        fr"$\vec{{AC}} = ({v1}; {v2}; {v3})$."
    )
    
    k_rand = random.choice([2, 3, -2])
    item_c = (
        fr"\vec{{AB}} \text{{ không cùng phương với }} \vec{{AC}}",
        fr"\vec{{AB}} = {k_rand}\vec{{AC}}",
        fr"Ta thấy các tỉ số tọa độ không bằng nhau nên hai vectơ $\vec{{AB}}$ và $\vec{{AC}}$ không cùng phương.",
        fr"Vì các tỉ số giữa các tọa độ tương ứng của $\vec{{AB}}$ và $\vec{{AC}}$ không bằng nhau nên $\vec{{AB}} \ne {k_rand}\vec{{AC}}$."
    )
    
    item_d = (
        r"\text{Ba điểm } A, B, C \text{ không thẳng hàng}",
        r"\text{Ba điểm } A, B, C \text{ thẳng hàng}",
        r"Vì hai vectơ $\vec{AB}$ và $\vec{AC}$ không cùng phương nên ba điểm $A, B, C$ không thẳng hàng (tạo thành một tam giác).",
        r"Vì hai vectơ $\vec{AB}$ và $\vec{AC}$ không cùng phương nên ba điểm $A, B, C$ không thể thẳng hàng."
    )

    items_data = [item_a, item_b, item_c, item_d]
    choices, loi_giai = make_tf_choices(items_data)
    return caudan, choices, loi_giai


# ==============================================================================
# PHẦN 6: CHUYÊN ĐỀ ÔN TẬP BỔ SUNG (TOÁN THỰC TẾ OXYZ, GTLN-GTNN, CỠ MẪU)
# ==============================================================================

def ToaDoOxyz_SA_ToanThucTe_HaiMayBay():
    """Toán thực tế Oxyz: Khoảng cách giữa hai máy bay MiG sau t giờ (Trả lời ngắn)"""
    d_S1 = random.choice([180, 200, 220, 250])
    d_E1 = random.choice([80, 100, 120, 150])
    h1 = random.choice([40, 50, 60])
    
    d_N2 = random.choice([80, 100, 120, 150])
    d_W2 = random.choice([120, 150, 180, 200])
    h2 = random.choice([70, 80, 90])
    
    x1, y1, z1 = d_S1, d_E1, h1
    x2, y2, z2 = -d_N2, -d_W2, h2
    
    dist_sq = (x2 - x1)**2 + (y2 - y1)**2 + (z2 - z1)**2
    dist = math.sqrt(dist_sq)
    ans = round(dist)
    
    caudan = fr'''Hai máy bay MiG-41 và MiG-31 xuất phát cùng một lúc tại một sân bay $M$. Lúc $t$ giờ, chiếc MiG-41 đến vị trí $N$ cách sân bay ${d_S1}\text{{km}}$ về phía nam và ${d_E1}\text{{km}}$ về phía đông, đồng thời cách mặt đất ${h1}\text{{km}}$; chiếc MiG-31 đến vị trí $P$ cách sân bay ${d_N2}\text{{km}}$ về phía bắc và ${d_W2}\text{{km}}$ về phía tây, đồng thời cách mặt đất ${h2}\text{{km}}$. Chọn hệ trục tọa độ $Oxyz$ với $O$ là vị trí xuất phát, trục $Ox$ hướng về phía nam, trục $Oy$ hướng về phía đông, trục $Oz$ vuông góc và hướng lên trên. Tìm khoảng cách giữa hai máy bay sau $t$ giờ (làm tròn đến chữ số hàng đơn vị của km).'''
    
    dx = x2 - x1
    dy = y2 - y1
    dz = z2 - z1
    
    loi_giai = fr'''Theo đề bài, chọn hệ trục tọa độ $Oxyz$ với:
\begin{{itemize}}
\item Gốc $O(0; 0; 0)$ tại vị trí sân bay $M$.
\item Trục $Ox$ hướng về phía nam $\implies$ vị trí về phía nam có hoành độ dương, phía bắc có hoành độ âm.
\item Trục $Oy$ hướng về phía đông $\implies$ vị trí về phía đông có tung độ dương, phía tây có tung độ âm.
\item Trục $Oz$ hướng thẳng đứng lên trên $\implies$ cao độ là khoảng cách so với mặt đất.
\end{{itemize}}
Tọa độ của hai máy bay lúc $t$ giờ là:
\[ N({x1}; {y1}; {z1}) \quad \text{{và}} \quad P({x2}; {y2}; {z2}). \]
Khoảng cách giữa hai máy bay là độ dài đoạn thẳng $NP$:
\[ NP = \sqrt{{({x2} - {x1})^2 + ({y2} - {y1})^2 + ({z2} - {z1})^2}} = \sqrt{{({dx})^2 + ({dy})^2 + ({dz})^2}} = \sqrt{{{dist_sq}}} \approx {dist:.2f}\text{{ km}}. \]
Làm tròn đến chữ số hàng đơn vị, khoảng cách giữa hai máy bay là ${ans}\text{{ km}}$.'''

    return caudan, loi_giai, str(ans)


def ToaDoOxyz_MC_ToanThucTe_HaiMayBay():
    """Toán thực tế Oxyz: Khoảng cách giữa hai máy bay MiG sau t giờ (Trắc nghiệm)"""
    caudan, loi_giai, ans_str = ToaDoOxyz_SA_ToanThucTe_HaiMayBay()
    ans = int(ans_str)
    
    w1 = ans + random.choice([15, 20, -15])
    w2 = ans - random.choice([25, 30, 40])
    w3 = round(ans * 1.15)
    
    choices = shuffle_choices(f"${ans}\\text{{ km}}$", [
        f"${w1}\\text{{ km}}$",
        f"${w2}\\text{{ km}}$",
        f"${w3}\\text{{ km}}$"
    ])
    return caudan, choices, loi_giai


def HamSo_MC_GTLN_GTNN_DoThiDoan():
    """GTLN và GTNN từ đồ thị hàm số trên đoạn [a; b], tính M - m"""
    m_val = random.choice([-3, -4, -5])
    M_val = random.choice([4, 5, 6])
    
    ans = M_val - m_val
    
    caudan = fr'''Cho hàm số $y = f(x)$ liên tục trên đoạn $[-2; 6]$ và có đồ thị như hình vẽ bên dưới. Gọi $M$ và $m$ lần lượt là giá trị lớn nhất và giá trị nhỏ nhất của hàm số đã cho trên đoạn $[-2; 6]$. Giá trị của $M - m$ bằng
\begin{{center}}
\begin{{tikzpicture}}[scale=0.68,>=stealth]
\draw[->] (-3,0) -- (7.5,0) node[below] {{$x$}};
\draw[->] (0,{m_val - 1.2}) -- (0,{M_val + 1.5}) node[left] {{$y$}};
\node[below left] at (0,0) {{$O$}};
\draw[dashed] (-2,0) node[below] {{$-2$}} -- (-2,{m_val + 3}) -- (0,{m_val + 3}) node[right] {{${m_val + 3}$}};
\draw[dashed] (1,0) node[above] {{$1$}} -- (1,{m_val}) -- (0,{m_val}) node[left] {{${m_val}$}};
\draw[dashed] (4,0) node[below] {{$4$}} -- (4,{M_val}) -- (0,{M_val}) node[left] {{${M_val}$}};
\draw[dashed] (6,0) node[below] {{$6$}} -- (6,{M_val});
\node[below] at (2,0) {{$2$}};
\node[below] at (3,0) {{$3$}};
\draw[thick,domain=-2:4,samples=100] plot (\x, {{({M_val - m_val}/9)*(\x - 1)^2 + {m_val}}});
\draw[thick] (4,{M_val}) -- (6,{M_val});
\fill (-2,{m_val + 3}) circle (1.5pt);
\fill (1,{m_val}) circle (1.5pt);
\fill (4,{M_val}) circle (1.5pt);
\fill (6,{M_val}) circle (1.5pt);
\end{{tikzpicture}}
\end{{center}}'''

    correct = f"${ans}$"
    wrongs = [
        f"${-ans}$",
        f"${ans - 1}$",
        f"${M_val + m_val}$"
    ]
    choices = shuffle_choices(correct, wrongs)
    
    loi_giai = fr'''Dựa vào đồ thị hàm số trên đoạn $[-2; 6]$, ta có:
\begin{{itemize}}
\item Điểm cao nhất của đồ thị có tung độ là $M = {M_val}$ (đạt được trên đoạn $[4; 6]$).
\item Điểm thấp nhất của đồ thị có tung độ là $m = {m_val}$ (đạt được tại $x = 1$).
\end{{itemize}}
Do đó:
\[ M - m = {M_val} - ({m_val}) = {ans}. \]'''

    return caudan, choices, loi_giai


def ThongKe_MC_CoMauGhepNhom():
    """Xác định cỡ mẫu từ bảng tần số ghép nhóm"""
    n1 = random.randint(1, 4)
    n2 = random.randint(6, 12)
    n3 = random.randint(8, 15)
    n4 = random.randint(8, 14)
    n5 = random.randint(2, 9)
    
    total_n = n1 + n2 + n3 + n4 + n5
    
    start_val = random.choice([4.5, 3.0, 5.0, 0])
    step = random.choice([1.0, 0.5, 2.0])
    
    def fmt(val):
        if float(val).is_integer():
            return str(int(val))
        return str(val).replace(".", ",")
        
    g1 = f"[{fmt(start_val)}; {fmt(start_val + step)})"
    g2 = f"[{fmt(start_val + step)}; {fmt(start_val + 2*step)})"
    g3 = f"[{fmt(start_val + 2*step)}; {fmt(start_val + 3*step)})"
    g4 = f"[{fmt(start_val + 3*step)}; {fmt(start_val + 4*step)})"
    g5 = f"[{fmt(start_val + 4*step)}; {fmt(start_val + 5*step)})"
    
    topic = random.choice([
        ("Điểm kiểm tra giữa kì I của một lớp được giáo viên ghi lại theo bảng sau:", "học sinh"),
        ("Thời gian tự học ở nhà mỗi ngày của học sinh một trường được ghi lại theo bảng sau:", "học sinh"),
        ("Khối lượng (tính bằng kg) của một số kiện hàng được thống kê ở bảng sau:", "kiện hàng")
    ])
    
    caudan = fr'''{topic[0]}
\begin{{center}}
\begin{{tabular}}{{|c|c|c|c|c|c|}}
\hline
Nhóm & ${g1}$ & ${g2}$ & ${g3}$ & ${g4}$ & ${g5}$ \\ \hline
Số {topic[1]} & ${n1}$ & ${n2}$ & ${n3}$ & ${n4}$ & ${n5}$ \\ \hline
\end{{tabular}}
\end{{center}}
Cỡ mẫu (tổng số {topic[1]}) của mẫu số liệu ghép nhóm trên là bao nhiêu?'''

    correct = f"${total_n}$"
    wrongs = [
        f"${total_n - n1}$",
        f"${total_n + random.choice([1, 2, -1])}$",
        f"${total_n - n5}$"
    ]
    wrongs = list(set([w for w in wrongs if w != correct]))
    while len(wrongs) < 3:
        wrongs.append(f"${total_n + len(wrongs) + 3}$")
        
    choices = shuffle_choices(correct, wrongs)
    
    loi_giai = fr'''Cỡ mẫu của mẫu số liệu ghép nhóm là tổng tần số của tất cả các nhóm:
\[ n = {n1} + {n2} + {n3} + {n4} + {n5} = {total_n}. \]
Vậy cỡ mẫu là ${total_n}$.'''

    return caudan, choices, loi_giai


def HamSo_TF_DeCuongHK1_Cau1():
    """Đúng sai - Hàm số: Khảo sát bảng biến thiên hàm bậc ba (Câu 1 - Đề cương HK1)"""
    x1 = random.randint(1, 5)
    x2 = x1 + random.randint(1, 3)
    y1 = random.randint(10, 15)
    y2 = y1 + random.randint(2, 6)
    
    caudan = fr'''Cho hàm số $y = f(x)$ xác định trên $\mathbb{{R}}$ và có bảng biến thiên như hình vẽ sau:
\begin{{center}}
\begin{{tabular}}{{|c|ccccccc|}}
\hline
$x$ & $-\infty$ & & ${x1}$ & & ${x2}$ & & $+\infty$ \\ \hline
$y'$ & & $-$ & $0$ & $+$ & $0$ & $-$ & \\ \hline
& $+\infty$ & & & & ${y2}$ & & \\
$y$ & & $\searrow$ & & $\nearrow$ & & $\searrow$ & \\
& & & ${y1}$ & & & & $-\infty$ \\ \hline
\end{{tabular}}
\end{{center}}
Các khẳng định sau đúng hay sai?'''

    item_a = (
        r"\text{Hàm số không có giá trị nhỏ nhất trên } \mathbb{R}",
        fr"\text{{Giá trị nhỏ nhất của hàm số là }} {y1}",
        fr"Vì $\lim_{{x \to +\infty}} f(x) = -\infty$ nên hàm số không có giá trị nhỏ nhất trên $\mathbb{{R}}$. Giá trị ${y1}$ chỉ là giá trị cực tiểu của hàm số.",
        fr"Vì $\lim_{{x \to +\infty}} f(x) = -\infty$ nên hàm số không có giá trị nhỏ nhất trên $\mathbb{{R}}$ (${y1}$ chỉ là giá trị cực tiểu)."
    )
    
    item_b = (
        fr"\text{{Hàm số đồng biến trên khoảng }} ({x1}; {x2})",
        fr"\text{{Hàm số đồng biến trên khoảng }} ({y1}; {y2})",
        fr"Dựa vào bảng biến thiên, $y' > 0$ trên khoảng $({x1}; {x2})$ nên hàm số đồng biến trên khoảng $({x1}; {x2})$.",
        fr"Khoảng $({y1}; {y2})$ là khoảng giá trị của $y$, không phải khoảng của biến số $x$. Hàm số đồng biến trên khoảng $({x1}; {x2})$."
    )
    
    item_c = (
        fr"\text{{Hàm số đạt cực đại tại }} x = {x2}",
        fr"\text{{Hàm số đạt cực đại tại }} x = {x1}",
        fr"Tại $x = {x2}$, đạo hàm $y'$ đổi dấu từ dương sang âm nên hàm số đạt cực đại tại $x = {x2}$.",
        fr"Tại $x = {x1}$, đạo hàm đổi dấu từ âm sang dương nên đây là điểm cực tiểu, không phải cực đại."
    )
    
    item_d = (
        r"\text{Đồ thị hàm số cắt trục hoành tại đúng 1 điểm}",
        r"\text{Đồ thị hàm số cắt trục hoành tại 3 điểm phân biệt}",
        fr"Vì $y_{{ct}} = {y1} > 0$ và $y_{{cd}} = {y2} > 0$ nên $y_{{ct}} \cdot y_{{cd}} > 0$. Hai điểm cực trị đều nằm phía trên trục hoành $Ox$, do đó đồ thị chỉ cắt trục hoành tại duy nhất 1 điểm trên khoảng $({x2}; +\infty)$.",
        fr"Vì $y_{{ct}} = {y1} > 0$ và $y_{{cd}} = {y2} > 0$ nên hai điểm cực trị cùng nằm phía trên trục hoành, đồ thị chỉ cắt trục hoành tại đúng 1 điểm (không thể cắt tại 3 điểm)."
    )
    
    items_data = [item_a, item_b, item_c, item_d]
    choices, loi_giai = make_tf_choices(items_data)
    return caudan, choices, loi_giai


def ToaDoOxyz_TF_DeCuongHK1_Cau2():
    """Đúng sai - Oxyz: Khảo sát ba vectơ n, v, m (Câu 2 - Đề cương HK1)"""
    x1, y1, z1 = 6, -4, -3
    x2, y2, z2 = 7, 1, -8
    k = -2
    x3, y3, z3 = k * x1, k * y1, k * z1
    
    mult = random.choice([1, -1])
    x1 *= mult
    y1 *= mult
    z1 *= mult
    x3 *= mult
    y3 *= mult
    z3 *= mult
    
    caudan = fr'''Trong không gian $Oxyz$, cho các vectơ $\vec{{n}} = ({x1}; {y1}; {z1})$, $\vec{{v}} = ({x2}; {y2}; {z2})$ và $\vec{{m}} = ({x3}; {y3}; {z3})$. Các khẳng định sau đúng hay sai?'''

    item_a = (
        r"\vec{n} \text{ và } \vec{v} \text{ không cùng phương}",
        r"\vec{n} \text{ và } \vec{v} \text{ cùng phương}",
        fr"Ta có $\dfrac{{{x1}}}{{{x2}}} \ne \dfrac{{{y1}}}{{{y2}}}$ (vì $\dfrac{{{x1}}}{{{x2}}} \approx {x1/x2:.2f} \ne \dfrac{{{y1}}}{{{y2}}} = {y1/y2:.2f}$) nên hai vectơ $\vec{{n}}$ và $\vec{{v}}$ không cùng phương.",
        fr"Vì các tỉ số giữa các tọa độ tương ứng $\dfrac{{{x1}}}{{{x2}}} \ne \dfrac{{{y1}}}{{{y2}}}$ nên hai vectơ không cùng phương."
    )
    
    len_v_sq = x2**2 + y2**2 + z2**2
    item_b = (
        fr"|\vec{{v}}| = \sqrt{{{len_v_sq}}}",
        fr"|\vec{{v}}| = {round(math.sqrt(len_v_sq)) + 2}",
        fr"Độ dài $|\vec{{v}}| = \sqrt{{{x2}^2 + {y2}^2 + ({z2})^2}} = \sqrt{{{len_v_sq}}}$.",
        fr"Độ dài $|\vec{{v}}| = \sqrt{{{x2}^2 + {y2}^2 + ({z2})^2}} = \sqrt{{{len_v_sq}}} \ne {round(math.sqrt(len_v_sq)) + 2}$."
    )
    
    c_x = 3*x1 - 4*x2
    c_y = 3*y1 - 4*y2
    c_z = 3*z1 - 4*z2
    
    item_c = (
        fr"3\vec{{n}} - 4\vec{{v}} = ({c_x}; {c_y}; {c_z})",
        fr"3\vec{{n}} - 4\vec{{v}} = ({c_x}; {c_y}; {c_z + 1})",
        fr"Ta có: $3\vec{{n}} - 4\vec{{v}} = (3\cdot({x1}) - 4\cdot({x2}); 3\cdot({y1}) - 4\cdot({y2}); 3\cdot({z1}) - 4\cdot({z2})) = ({c_x}; {c_y}; {c_z})$.",
        fr"Ta tính được $3\vec{{n}} - 4\vec{{v}} = ({c_x}; {c_y}; {c_z}) \ne ({c_x}; {c_y}; {c_z + 1})$."
    )
    
    item_d = (
        r"\vec{n} \text{ và } \vec{m} \text{ cùng phương}",
        r"\vec{n} \text{ và } \vec{m} \text{ không cùng phương}",
        fr"Ta có: $\vec{{m}} = ({x3}; {y3}; {z3}) = {k}\cdot({x1}; {y1}; {z1}) = {k}\vec{{n}}$ nên hai vectơ $\vec{{n}}$ và $\vec{{m}}$ cùng phương (ngược hướng).",
        fr"Vì $\vec{{m}} = {k}\vec{{n}}$ nên hai vectơ $\vec{{n}}$ và $\vec{{m}}$ cùng phương."
    )
    
    items_data = [item_a, item_b, item_c, item_d]
    choices, loi_giai = make_tf_choices(items_data)
    return caudan, choices, loi_giai


def ToaDoOxyz_TF_DeCuongHK1_Cau3():
    """Đúng sai - Oxyz: Hình hộp chữ nhật gắn hệ trục Oxyz (Câu 3 - Đề cương HK1)"""
    a = random.choice([4, 5, 6])
    b = random.choice([3, 4, 5])
    c = random.choice([3, 4, 5])
    
    caudan = fr'''Cho hình hộp chữ nhật $ABCD.A'B'C'D'$ có $AB = {a}, AD = {b}, AA' = {c}$. Xét hệ trục tọa độ $Oxyz$ có gốc $O$ trùng với điểm $A$, các điểm $B, D, A'$ lần lượt nằm trên các tia $Ox, Oy, Oz$.
\begin{{center}}
\begin{{tikzpicture}}[scale=0.75,>=stealth]
\coordinate (A) at (0,0);
\coordinate (B) at (-1.2,-1.4);
\coordinate (D) at (4,0);
\coordinate (C) at ($(B)+(D)-(A)$);
\coordinate (A1) at (0,3.2);
\coordinate (B1) at ($(B)+(0,3.2)$);
\coordinate (D1) at ($(D)+(0,3.2)$);
\coordinate (C1) at ($(C)+(0,3.2)$);

\draw[->,thick] (A) -- ($(B)!1.6!(A)$) node[left] {{$x$}};
\draw[->,thick] (A) -- ($(D)!1.25!(A)$) node[right] {{$y$}};
\draw[->,thick] (A) -- ($(A1)!1.25!(A)$) node[above] {{$z$}};

\draw[dashed] (A) -- (B);
\draw[dashed] (A) -- (D);
\draw[dashed] (A) -- (A1);

\draw (B) -- (C) -- (D);
\draw (A1) -- (B1) -- (C1) -- (D1) -- cycle;
\draw (B) -- (B1);
\draw (C) -- (C1);
\draw (D) -- (D1);

\node[below left] at (A) {{$A$}};
\node[below left] at (B) {{$B$}};
\node[below] at (C) {{$C$}};
\node[right] at (D) {{$D$}};
\node[above left] at (A1) {{$A'$}};
\node[left] at (B1) {{$B'$}};
\node[above right] at (D1) {{$D'$}};
\node[above] at (C1) {{$C'$}};
\end{{tikzpicture}}
\end{{center}}
Các khẳng định sau đúng hay sai?'''

    item_a = (
        fr"\text{{Tọa độ điểm }} D'(0; {b}; {c})",
        fr"\text{{Tọa độ điểm }} D'({b-1}; 1; {c})",
        fr"Điểm $D$ nằm trên tia $Oy$ nên $D(0; {b}; 0)$. Vì $D'$ có cùng hoành độ và tung độ với $D$, đồng thời có cao độ bằng $AA' = {c}$ nên $D'(0; {b}; {c})$.",
        fr"Vì $D$ nằm trên tia $Oy$ nên $D(0; {b}; 0)$, suy ra $D'(0; {b}; {c}) \ne ({b-1}; 1; {c})$."
    )
    
    item_b = (
        fr"\vec{{D'C'}} = {a}\vec{{i}} + 0\vec{{j}} + 0\vec{{k}}",
        fr"\vec{{D'C'}} = 0\vec{{i}} + {b}\vec{{j}} + 0\vec{{k}}",
        fr"Vectơ $\vec{{D'C'}} = \vec{{AB}} = ({a}; 0; 0) = {a}\vec{{i}} + 0\vec{{j}} + 0\vec{{k}}$.",
        fr"Vectơ $\vec{{D'C'}} = \vec{{AB}} = ({a}; 0; 0) = {a}\vec{{i}} \ne {b}\vec{{j}}$."
    )
    
    item_c = (
        fr"\text{{Tọa độ điểm }} B'({a}; 0; {c})",
        fr"\text{{Tọa độ điểm }} B'(0; {a}; {c})",
        fr"Điểm $B$ nằm trên tia $Ox$ với $AB = {a} \implies B({a}; 0; 0)$. Điểm $B'$ có cùng hoành độ và tung độ với $B$ và có cao độ $c = {c}$, do đó $B'({a}; 0; {c})$.",
        fr"Điểm $B$ nằm trên trục $Ox$ nên hoành độ của $B'$ là ${a}$, tung độ bằng $0$, do đó $B'({a}; 0; {c}) \ne (0; {a}; {c})$."
    )
    
    item_d = (
        fr"\text{{Tọa độ điểm }} C'({a}; {b}; {c})",
        fr"\text{{Tọa độ điểm }} C'({b}; {a}; {c})",
        fr"Điểm $C'$ có hình chiếu vuông góc lên $Ox$ là $B({a}; 0; 0)$, lên $Oy$ là $D(0; {b}; 0)$ và lên $Oz$ là $A'(0; 0; {c})$. Do đó $C'({a}; {b}; {c})$.",
        fr"Tọa độ của $C'$ là $({a}; {b}; {c}) \ne ({b}; {a}; {c})$."
    )
    
    items_data = [item_a, item_b, item_c, item_d]
    choices, loi_giai = make_tf_choices(items_data)
    return caudan, choices, loi_giai


def ThongKe_TF_DeCuongHK1_Cau3():
    """Đúng sai - Thống kê: So sánh khoảng biến thiên hai mẫu độ tuổi kết hôn (Câu 3 - Đề cương HK1)"""
    nA1 = random.randint(8, 12)
    nA2 = random.randint(25, 29)
    nA3 = random.randint(23, 27)
    nA4 = random.randint(23, 27)
    nA5 = 100 - (nA1 + nA2 + nA3 + nA4)
    if nA5 <= 5:
        nA5 = 13
        nA4 = 100 - (nA1 + nA2 + nA3 + nA5)
    total_A = nA1 + nA2 + nA3 + nA4 + nA5

    nB1 = random.randint(15, 20)
    nB2 = random.randint(28, 35)
    nB3 = random.randint(45, 55)
    nB4 = random.randint(2, 5)
    nB5 = 0
    
    RA = 15
    RB = 12

    caudan = fr'''Giả sử kết quả khảo sát hai khu vực A và B về độ tuổi kết hôn của một số phụ nữ vừa lập gia đình được cho ở bảng sau:
\begin{{center}}
\begin{{tabular}}{{|l|c|c|c|c|c|}}
\hline
Tuổi kết hôn & $[19; 22)$ & $[22; 25)$ & $[25; 28)$ & $[28; 31)$ & $[31; 34)$ \\ \hline
Số phụ nữ khu vực A & ${nA1}$ & ${nA2}$ & ${nA3}$ & ${nA4}$ & ${nA5}$ \\ \hline
Số phụ nữ khu vực B & ${nB1}$ & ${nB2}$ & ${nB3}$ & ${nB4}$ & ${nB5}$ \\ \hline
\end{{tabular}}
\end{{center}}
Các khẳng định sau đúng hay sai?'''

    item_a = (
        fr"\text{{Khoảng biến thiên của khu vực B, }} R_B = {RB}",
        fr"\text{{Khoảng biến thiên của khu vực B, }} R_B = {RA}",
        fr"Vì nhóm $[31; 34)$ của khu vực B có tần số bằng $0$, nhóm có tần số khác không lớn nhất là $[28; 31)$ và nhỏ nhất là $[19; 22)$ nên khoảng biến thiên của mẫu B là $R_B = 31 - 19 = {RB}$.",
        fr"Vì nhóm $[31; 34)$ có tần số bằng $0$ nên nhóm có dữ liệu lớn nhất là $[28; 31)$. Khoảng biến thiên $R_B = 31 - 19 = {RB} \ne {RA}$."
    )
    
    item_b = (
        r"\text{Nếu so sánh bằng khoảng biến thiên thì khu vực B có độ tuổi kết hôn đồng đều hơn khu vực A}",
        r"\text{Nếu so sánh bằng khoảng biến thiên thì khu vực A có độ tuổi kết hôn đồng đều hơn khu vực B}",
        fr"Ta có $R_A = 34 - 19 = {RA}$ và $R_B = {RB}$. Vì $R_B < R_A$ nên độ tuổi kết hôn của khu vực B ít phân tán hơn, tức là đồng đều hơn khu vực A.",
        fr"Vì khoảng biến thiên của khu vực B ($R_B = {RB}$) nhỏ hơn khu vực A ($R_A = {RA}$) nên khu vực B có độ tuổi kết hôn đồng đều hơn khu vực A."
    )
    
    sum_B_22_28 = nB2 + nB3
    item_c = (
        fr"\text{{Độ tuổi kết hôn từ }} [22; 28) \text{{ của khu vực B là }} {sum_B_22_28}",
        fr"\text{{Độ tuổi kết hôn từ }} [22; 28) \text{{ của khu vực B là }} {sum_B_22_28 - 29}",
        fr"Số phụ nữ có độ tuổi kết hôn từ $[22; 28)$ ở khu vực B là tổng số của hai nhóm $[22; 25)$ và $[25; 28)$: ${nB2} + {nB3} = {sum_B_22_28}$.",
        fr"Số phụ nữ từ $[22; 28)$ của khu vực B là ${nB2} + {nB3} = {sum_B_22_28} \ne {sum_B_22_28 - 29}$."
    )
    
    item_d = (
        fr"\text{{Cỡ mẫu của khu vực A, }} n_A = {total_A}",
        fr"\text{{Cỡ mẫu của khu vực A, }} n_A = {total_A + 10}",
        fr"Cỡ mẫu khu vực A là $n_A = {nA1} + {nA2} + {nA3} + {nA4} + {nA5} = {total_A}$.",
        fr"Cỡ mẫu khu vực A là $n_A = {nA1} + {nA2} + {nA3} + {nA4} + {nA5} = {total_A} \ne {total_A + 10}$."
    )

    items_data = [item_a, item_b, item_c, item_d]
    choices, loi_giai = make_tf_choices(items_data)
    return caudan, choices, loi_giai


def HamSo_TF_DeCuongHK1_Cau4():
    """Đúng sai - Hàm số: Khảo sát hàm đa thức bậc ba y = x^3 + 3ax^2 + d (Câu 4 - Đề cương HK1)"""
    a = random.choice([1, 2])
    d = random.randint(-6, -2)
    x_cd = -2 * a
    x_ct = 0
    y_cd = x_cd**3 + 3 * a * (x_cd**2) + d
    y_ct = d
    sum_y = y_cd + y_ct
    
    he_so_x2 = 3 * a
    sign_d = f"+ {d}" if d > 0 else f"- {abs(d)}"
    caudan = fr'''Cho hàm số $y = x^3 + {he_so_x2}x^2 {sign_d}$. Các khẳng định sau đúng hay sai?'''

    item_a = (
        fr"\text{{Hàm số nghịch biến trên khoảng }} ({x_cd}; {x_ct})",
        fr"\text{{Hàm số đồng biến trên khoảng }} ({x_cd}; {x_ct})",
        fr"Ta có $y' = 3x^2 + {6*a}x = 3x(x + {2*a})$. Cho $y' = 0 \iff x = {x_cd}$ hoặc $x = {x_ct}$. Vì hệ số bậc cao nhất dương nên $y' < 0$ với mọi $x \in ({x_cd}; {x_ct})$, do đó hàm số nghịch biến trên khoảng $({x_cd}; {x_ct})$.",
        fr"Vì $y' < 0$ trên khoảng $({x_cd}; {x_ct})$ nên hàm số nghịch biến trên khoảng $({x_cd}; {x_ct})$, không đồng biến."
    )
    
    x_fake = x_cd - 2
    item_b = (
        fr"\text{{Hàm số đồng biến trên khoảng }} ({x_ct}; +\infty)",
        fr"\text{{Hàm số đồng biến trên khoảng }} ({x_fake}; +\infty)",
        fr"Hàm số có $y' > 0$ trên các khoảng $(-\infty; {x_cd})$ và $({x_ct}; +\infty)$ nên hàm số đồng biến trên khoảng $({x_ct}; +\infty)$.",
        fr"Trên khoảng $({x_fake}; +\infty)$ có chứa khoảng $({x_cd}; {x_ct})$ mà trên đó hàm số nghịch biến, do đó hàm số không đồng biến trên khoảng $({x_fake}; +\infty)$."
    )
    
    item_c = (
        fr"y_{{CĐ}} + y_{{CT}} = {sum_y}",
        fr"y_{{CĐ}} + y_{{CT}} = {sum_y + random.choice([2, -2, 3])}",
        fr"Giá trị cực đại $y_{{CĐ}} = y({x_cd}) = ({x_cd})^3 + {he_so_x2}({x_cd})^2 {sign_d} = {y_cd}$.\\Giá trị cực tiểu $y_{{CT}} = y({x_ct}) = {y_ct}$.\\Suy ra $y_{{CĐ}} + y_{{CT}} = {y_cd} + ({y_ct}) = {sum_y}$.",
        fr"Ta có $y_{{CĐ}} = {y_cd}$ và $y_{{CT}} = {y_ct}$, do đó $y_{{CĐ}} + y_{{CT}} = {sum_y}$."
    )
    
    item_d = (
        fr"\text{{Giá trị cực tiểu }} y = {y_ct}",
        fr"\text{{Giá trị cực tiểu }} y = {x_ct}",
        fr"Hàm số đạt cực tiểu tại điểm $x = {x_ct}$, giá trị cực tiểu tương ứng là $y = y({x_ct}) = {y_ct}$.",
        fr"Giá trị cực tiểu của hàm số là $y = {y_ct}$ (trong khi $x = {x_ct}$ là điểm cực tiểu)."
    )

    items_data = [item_a, item_b, item_c, item_d]
    choices, loi_giai = make_tf_choices(items_data)
    return caudan, choices, loi_giai


def HamSo_SA_DeCuongHK1_Cau1():
    """Trả lời ngắn - Hàm số: Biểu thức cực trị A = k1*M - k2*m của hàm bậc ba (Câu 1 - Đề cương HK1)"""
    c = random.choice([1, 2])
    d = random.randint(-4, 4)
    M = 2 * (c**3) + d
    m = -2 * (c**3) + d
    
    k1 = random.randint(2023, 2026)
    k2 = k1 + random.choice([-1, 1])
    
    ans = k1 * M - k2 * m
    
    sign_3c2 = f"- {3 * (c**2)}x"
    sign_d = f"+ {d}" if d > 0 else (f"- {abs(d)}" if d < 0 else "")
    
    caudan = fr'''Cho hàm số $y = x^3 {sign_3c2} {sign_d}$. Gọi $M$ là giá trị cực đại, $m$ là giá trị cực tiểu của hàm số. Tính giá trị biểu thức:
\[ A = {k1}M - {k2}m. \]'''

    loi_giai = fr'''Ta có đạo hàm: $y' = 3x^2 - {3 * (c**2)} = 3(x^2 - {c**2})$.
$y' = 0 \iff x = \pm {c}$.
Hàm số đạt cực đại tại $x = -{c}$, giá trị cực đại là:
\[ M = y(-{c}) = (-{c})^3 - {3*(c**2)}(-{c}) {sign_d} = {M}. \]
Hàm số đạt cực tiểu tại $x = {c}$, giá trị cực tiểu là:
\[ m = y({c}) = ({c})^3 - {3*(c**2)}({c}) {sign_d} = {m}. \]
Thay vào biểu thức $A$, ta được:
\[ A = {k1}\cdot({M}) - {k2}\cdot({m}) = {k1*M} - ({k2*m}) = {ans}. \]
Vậy đáp án là ${ans}$.'''

    return caudan, loi_giai, str(ans)


def HamSo_SA_DeCuongHK1_Cau2():
    """Trả lời ngắn - Hàm số: Hai số có hiệu d, tích bé nhất, tính 1000a (Câu 2 - Đề cương HK1)"""
    d = random.choice([7, 9, 11, 13, 15, 17])
    ans = 500 * d
    a_val = d / 2

    caudan = fr'''Hai số có hiệu của số lớn với số bé là ${d}$ và tích của chúng là bé nhất. Gọi $a$ là số lớn hơn. Tính $1000a$?'''

    loi_giai = fr'''Gọi số bé hơn là $x$, khi đó số lớn hơn là $a = x + {d}$.
Tích của hai số là:
\[ P(x) = x(x + {d}) = x^2 + {d}x = \left(x + \dfrac{{{d}}}{{2}}\right)^2 - \dfrac{{{d**2}}}{{4}}. \]
Vì $\left(x + \dfrac{{{d}}}{{2}}\right)^2 \ge 0$ với mọi $x \in \mathbb{{R}}$ nên $P(x)$ đạt giá trị nhỏ nhất khi:
\[ x + \dfrac{{{d}}}{{2}} = 0 \iff x = -\dfrac{{{d}}}{{2}} = -{d/2}. \]
Khi đó số lớn hơn là:
\[ a = x + {d} = -{d/2} + {d} = {a_val}. \]
Do đó:
\[ 1000a = 1000 \times {a_val} = {ans}. \]
Vậy giá trị cần tìm là ${ans}$.'''

    return caudan, loi_giai, str(ans)


def HamSo_SA_DeCuongHK1_Cau3():
    """Trả lời ngắn - Hàm số: Tiệm cận xiên hàm phân thức bậc hai trên bậc nhất (Câu 3 - Đề cương HK1)"""
    u = random.choice([2, 3])
    p = random.choice([-11, -9, -7, 7, 9, 11])
    q = random.choice([3, 5, 7, 9])
    v = random.choice([-6, -4, -2, 2, 4, 6])
    w = random.choice([5, 11, 15, 17])
    
    m = random.choice([-5, -3, -2, 2, 3, 5])
    k1 = p * m
    k2 = p**2
    
    ans = m * u + (p * v - u * q)
    
    num_str = f"{u}x^2 " + (f"+ {v}x" if v > 0 else f"- {abs(v)}x") + f" + {w}"
    den_str = f"{p}x + {q}" if q > 0 else f"{p}x - {abs(q)}"
    
    b_num = p * v - u * q
    b_den = p**2
    
    caudan = fr'''Cho hàm số $y = \dfrac{{{num_str}}}{{{den_str}}}$ có đường tiệm cận xiên là $y = ax + b$. Tính giá trị biểu thức:
\[ A = {k1}a + {k2}b. \]'''

    loi_giai = fr'''Thực hiện phép chia đa thức tử cho mẫu:
\[ \dfrac{{{num_str}}}{{{den_str}}} = \dfrac{{{u}}}{{{p}}}x + \dfrac{{{b_num}}}{{{b_den}}} + \dfrac{{R}}{{{den_str}}}. \]
Suy ra phương trình đường tiệm cận xiên của đồ thị hàm số là:
\[ y = ax + b = \dfrac{{{u}}}{{{p}}}x + \dfrac{{{b_num}}}{{{b_den}}}. \]
Do đó:
\[ a = \dfrac{{{u}}}{{{p}}}, \quad b = \dfrac{{{b_num}}}{{{b_den}}}. \]
Thay vào biểu thức $A$, ta có:
\[ A = {k1}a + {k2}b = {k1}\left(\dfrac{{{u}}}{{{p}}}\right) + {k2}\left(\dfrac{{{b_num}}}{{{b_den}}}\right) = {m}\cdot({u}) + ({b_num}) = {ans}. \]
Vậy giá trị của biểu thức $A$ là ${ans}$.'''

    return caudan, loi_giai, str(ans)


def ToaDoOxyz_SA_DeCuongHK1_Cau4():
    """Trả lời ngắn - Oxyz: Biểu thức độ dài vectơ trong không gian Oxyz (Câu 4 - Đề cương HK1)"""
    pyth = random.choice([(-3, 4, 0), (3, -4, 0), (0, 3, 4), (0, -3, 4), (6, -8, 0)])
    xa, ya, za = pyth
    len_a = round(math.sqrt(xa**2 + ya**2 + za**2))
    
    len_b = random.choice([4, 5, 6])
    xb, yb, zb = 0, len_b, 0
    
    len_c = random.choice([1, 2])
    xc, yc, zc = -len_c, 0, 0
    
    c3 = random.choice([2, 3, 4])
    inside = len_a + len_b - c3 * len_c
    
    mult = random.randint(-135, -120)
    ans = mult * inside

    caudan = fr'''Trong không gian $Oxyz$, cho $\vec{{a}} = ({xa}; {ya}; {za})$, $\vec{{b}} = ({xb}; {yb}; {zb})$, $\vec{{c}} = ({xc}; {yc}; {zc})$. Tính giá trị biểu thức:
\[ A = {mult}\cdot\left(|\vec{{a}}| + |\vec{{b}}| - {c3}|\vec{{c}}|\right). \]'''

    loi_giai = fr'''Ta có:
\begin{{itemize}}
\item $|\vec{{a}}| = \sqrt{{({xa})^2 + ({ya})^2 + ({za})^2}} = \sqrt{{{xa**2 + ya**2 + za**2}}} = {len_a}$.
\item $|\vec{{b}}| = \sqrt{{{xb}^2 + {yb}^2 + {zb}^2}} = {len_b}$.
\item $|\vec{{c}}| = \sqrt{{({xc})^2 + {yc}^2 + {zc}^2}} = {len_c}$.
\end{{itemize}}
Suy ra:
\[ |\vec{{a}}| + |\vec{{b}}| - {c3}|\vec{{c}}| = {len_a} + {len_b} - {c3}\cdot({len_c}) = {inside}. \]
Do đó:
\[ A = {mult}\cdot({inside}) = {ans}. \]
Vậy giá trị biểu thức $A$ là ${ans}$.'''

    return caudan, loi_giai, str(ans)


def ThongKe_SA_DeCuongHK1_Cau1():
    """Trả lời ngắn - Thống kê: Tìm khoảng tứ phân vị mẫu số liệu ghép nhóm tốc độ gõ phím (Câu 1)"""
    n1 = random.randint(210, 250)
    n2 = random.randint(180, 210)
    n3 = random.randint(210, 240)
    n4 = random.randint(110, 140)
    n5 = random.randint(65, 85)
    
    intervals = [(50, 60), (60, 70), (70, 80), (80, 90), (90, 100)]
    counts = [n1, n2, n3, n4, n5]
    n = sum(counts)
    
    cum = []
    s = 0
    for c in counts:
        s += c
        cum.append(s)
        
    p1 = n / 4
    idx1 = 0
    while idx1 < len(cum) and cum[idx1] < p1:
        idx1 += 1
    u1, v1 = intervals[idx1]
    cf_prev1 = cum[idx1 - 1] if idx1 > 0 else 0
    n_k1 = counts[idx1]
    h1 = v1 - u1
    q1 = u1 + ((p1 - cf_prev1) / n_k1) * h1
    
    p3 = 3 * n / 4
    idx3 = 0
    while idx3 < len(cum) and cum[idx3] < p3:
        idx3 += 1
    u3, v3 = intervals[idx3]
    cf_prev3 = cum[idx3 - 1] if idx3 > 0 else 0
    n_k3 = counts[idx3]
    h3 = v3 - u3
    q3 = u3 + ((p3 - cf_prev3) / n_k3) * h3
    
    delta_q = q3 - q1
    ans_val = round(delta_q, 1)
    ans_str = f"{ans_val:.1f}".replace('.', ',')

    caudan = fr'''Một trường THPT mở cuộc kiểm tra tốc độ gõ phím (đơn vị: từ/phút) của ${n}$ học sinh toàn trường thu được kết quả sau:
\begin{{center}}
\begin{{tabular}}{{|l|c|c|c|c|c|}}
\hline
Tốc độ gõ (từ/phút) & $[50; 60)$ & $[60; 70)$ & $[70; 80)$ & $[80; 90)$ & $[90; 100)$ \\ \hline
Số học sinh & ${n1}$ & ${n2}$ & ${n3}$ & ${n4}$ & ${n5}$ \\ \hline
\end{{tabular}}
\end{{center}}
Tìm khoảng tứ phân vị của mẫu số liệu ghép nhóm trên (làm tròn kết quả đến hàng phần mười).'''

    loi_giai = fr'''Cỡ mẫu là $n = {n1} + {n2} + {n3} + {n4} + {n5} = {n}$.
\begin{{itemize}}
\item Gọi $Q_1$ là tứ phân vị thứ nhất của mẫu số liệu. Ta có $\dfrac{{n}}{{4}} = \dfrac{{{n}}}{{4}} = {p1}$.
Do đó nhóm chứa tứ phân vị thứ nhất là nhóm $[{u1}; {v1})$.
Áp dụng công thức tính tứ phân vị thứ nhất:
\[ Q_1 = {u1} + \dfrac{{{p1} - {cf_prev1}}}{{{n_k1}}} \cdot {h1} \approx {round(q1, 2)}. \]
\item Gọi $Q_3$ là tứ phân vị thứ ba của mẫu số liệu. Ta có $\dfrac{{3n}}{{4}} = \dfrac{{3 \cdot {n}}}{{4}} = {p3}$.
Do đó nhóm chứa tứ phân vị thứ ba là nhóm $[{u3}; {v3})$.
Áp dụng công thức tính tứ phân vị thứ ba:
\[ Q_3 = {u3} + \dfrac{{{p3} - {cf_prev3}}}{{{n_k3}}} \cdot {h3} \approx {round(q3, 2)}. \]
\item Khoảng tứ phân vị của mẫu số liệu ghép nhóm là:
\[ \Delta_Q = Q_3 - Q_1 \approx {round(q3, 2)} - {round(q1, 2)} \approx {ans_str}. \]
\end{{itemize}}
Vậy khoảng tứ phân vị của mẫu số liệu là ${ans_str}$.'''

    return caudan, loi_giai, ans_str


def ToaDoOxyz_SA_DeCuongHK1_Cau2():
    """Trả lời ngắn - Oxyz: Tính độ dài vectơ tổ hợp tuyến tính 1/2*a - 2*b (Câu 2)"""
    a1 = random.choice([-6, -4, -2, 2, 4, 6])
    a2 = random.choice([-5, -3, 3, 5])
    a3 = random.choice([-7, -5, -3, 3, 5, 7])
    
    b1 = random.choice([-3, -2, -1, 1, 2, 3])
    b2 = random.choice([-2, -1, 1, 2])
    b3 = random.choice([-2, -1, 1, 2])
    
    u1 = 0.5 * a1 - 2 * b1
    u2 = 0.5 * a2 - 2 * b2
    u3 = 0.5 * a3 - 2 * b3
    
    val_len = math.sqrt(u1**2 + u2**2 + u3**2)
    ans_val = round(val_len, 2)
    ans_str = f"{ans_val:.2f}".replace('.', ',')
    
    u1_str = f"{int(u1)}" if u1.is_integer() else f"{u1}"
    u2_str = f"{int(u2)}" if u2.is_integer() else f"{u2}"
    u3_str = f"{int(u3)}" if u3.is_integer() else f"{u3}"

    caudan = fr'''Trong không gian $Oxyz$, cho $\vec{{a}} = ({a1}; {a2}; {a3})$ và $\vec{{b}} = ({b1}; {b2}; {b3})$. Tính độ dài của vectơ $\dfrac{{1}}{{2}}\vec{{a}} - 2\vec{{b}}$ (làm tròn kết quả đến hàng phần trăm).'''

    loi_giai = fr'''Ta có:
\begin{{itemize}}
\item $\dfrac{{1}}{{2}}\vec{{a}} = \left(\dfrac{{{a1}}}{{2}}; \dfrac{{{a2}}}{{2}}; \dfrac{{{a3}}}{{2}}\right) = ({0.5*a1}; {0.5*a2}; {0.5*a3})$.
\item $2\vec{{b}} = ({2*b1}; {2*b2}; {2*b3})$.
\end{{itemize}}
Suy ra tọa độ vectơ:
\[ \vec{{u}} = \dfrac{{1}}{{2}}\vec{{a}} - 2\vec{{b}} = ({u1_str}; {u2_str}; {u3_str}). \]
Độ dài của vectơ $\dfrac{{1}}{{2}}\vec{{a}} - 2\vec{{b}}$ là:
\[ \left|\dfrac{{1}}{{2}}\vec{{a}} - 2\vec{{b}}\right| = \sqrt{{({u1_str})^2 + ({u2_str})^2 + ({u3_str})^2}} = \sqrt{{{round(u1**2 + u2**2 + u3**2, 4)}}} \approx {ans_str}. \]
Vậy độ dài vectơ cần tìm là ${ans_str}$.'''

    return caudan, loi_giai, ans_str


def HamSo_SA_DeCuongHK1_Cau3_CucTri():
    """Trả lời ngắn - Hàm số: Biểu thức cực trị y1^2 - 2*y2 hàm bậc ba y = -x^3 + 3ax^2 + d (Câu 3)"""
    a = random.choice([1, 2])
    d = random.randint(2, 6)
    
    y2 = d
    y1 = 4 * (a**3) + d
    
    P = y1**2 - 2 * y2
    he_so_x2 = 3 * a

    caudan = fr'''Gọi $y_1, y_2$ lần lượt là giá trị cực đại, giá trị cực tiểu của hàm số $y = -x^3 + {he_so_x2}x^2 + {d}$. Khi đó giá trị của biểu thức $y_1^2 - 2y_2$ bằng bao nhiêu?'''

    loi_giai = fr'''Tập xác định: $D = \mathbb{{R}}$.
Đạo hàm: $y' = -3x^2 + {6*a}x = -3x(x - {2*a})$.
$y' = 0 \iff \left[\begin{{aligned}} x &= 0 \\ x &= {2*a} \end{{aligned}}\right.$
Bảng xét dấu $y'$ cho thấy:
\begin{{itemize}}
\item Hàm số đạt cực đại tại $x = {2*a}$, giá trị cực đại là:
\[ y_1 = y({2*a}) = -({2*a})^3 + {he_so_x2}({2*a})^2 + {d} = {y1}. \]
\item Hàm số đạt cực tiểu tại $x = 0$, giá trị cực tiểu là:
\[ y_2 = y(0) = {y2}. \]
\end{{itemize}}
Thay vào biểu thức ta được:
\[ y_1^2 - 2y_2 = ({y1})^2 - 2\cdot({y2}) = {y1**2} - {2*y2} = {P}. \]
Vậy giá trị biểu thức là ${P}$.'''

    return caudan, loi_giai, str(P)


def HamSo_SA_DeCuongHK1_Cau4_TiemCanXien():
    """Trả lời ngắn - Hàm số: Tiệm cận xiên y = ax + b, tính 1000b + a (Câu 4)"""
    c = random.randint(1, 4)
    m = random.randint(1, 5)
    a_val = 1
    b_val = m + c
    P = 1000 * b_val + a_val
    
    caudan = fr'''Biết rằng đồ thị hàm số $y = \dfrac{{x^2 + {m}x}}{{x - {c}}}$ có đường tiệm cận xiên là $y = ax + b$. Tính giá trị của biểu thức $P = 1000b + a$.'''

    loi_giai = fr'''Thực hiện phép chia đa thức tử cho mẫu:
\[ \dfrac{{x^2 + {m}x}}{{x - {c}}} = (x + {b_val}) + \dfrac{{{c * b_val}}}{{x - {c}}}. \]
Vì $\lim_{{x \to \pm\infty}} \left[\dfrac{{x^2 + {m}x}}{{x - {c}}} - (x + {b_val})\right] = \lim_{{x \to \pm\infty}} \dfrac{{{c * b_val}}}{{x - {c}}} = 0$ nên đồ thị hàm số có đường tiệm cận xiên là:
\[ y = ax + b = x + {b_val}. \]
Suy ra:
\[ a = 1, \quad b = {b_val}. \]
Do đó:
\[ P = 1000b + a = 1000 \cdot ({b_val}) + 1 = {P}. \]
Vậy giá trị của biểu thức $P$ là ${P}$.'''

    return caudan, loi_giai, str(P)


def HamSo_SA_Trang75_Cau1_VietCucTri():
    """Trả lời ngắn - Hàm số: Biểu thức Vi-ét (x1 + x2)^2 - x1*x2 của hai điểm cực trị (Trang 75 - Câu 1)"""
    pairs = [(-1, 3), (-3, 1), (-2, 2), (-4, 0), (0, 4), (-3, 3)]
    x1, x2 = random.choice(pairs)
    if random.choice([True, False]):
        x1, x2 = x2, x1
        
    S = (x1 + x2) // 2
    P_val = x1 * x2
    d = random.randint(-5, 5)
    
    k = random.choice([1, 2])
    ans = (x1 + x2)**2 - k * (x1 * x2)
    
    term_x2 = f"- {3 * S}x^2" if S > 0 else (f"+ {abs(3 * S)}x^2" if S < 0 else "")
    term_x = f"- {abs(3 * P_val)}x" if P_val < 0 else (f"+ {3 * P_val}x" if P_val > 0 else "")
    term_d = f"+ {d}" if d > 0 else (f"- {abs(d)}" if d < 0 else "")
    
    expr_k = "(x_1 + x_2)^2 - x_1 x_2" if k == 1 else f"(x_1 + x_2)^2 - {k}x_1 x_2"
    
    caudan = fr'''Hàm số $y = x^3 {term_x2} {term_x} {term_d}$ có hai điểm cực trị là $x_1; x_2$. Giá trị biểu thức $P = {expr_k}$ là?'''

    loi_giai = fr'''Tập xác định: $D = \mathbb{{R}}$.
Ta có đạo hàm: $y' = 3x^2 {f"- {6*S}x" if S > 0 else (f"+ {abs(6*S)}x" if S < 0 else "")} {term_x.replace("x", "")}$.
Vì hàm số có hai điểm cực trị $x_1, x_2$ nên $x_1, x_2$ là hai nghiệm phân biệt của phương trình $y' = 0$.
Theo định lý Vi-ét cho phương trình $y' = 0$:
\[ \begin{{cases}} x_1 + x_2 = {x1 + x2} \\ x_1 x_2 = {x1 * x2} \end{{cases}} \]
Thay vào biểu thức $P$, ta được:
\[ P = {expr_k} = ({x1 + x2})^2 - {k}\cdot({x1 * x2}) = {(x1+x2)**2} - ({k*x1*x2}) = {ans}. \]
Vậy giá trị của biểu thức là ${ans}$.'''

    return caudan, loi_giai, str(ans)


def HamSo_SA_Trang75_Cau2_ThamSoMDongBien():
    """Trả lời ngắn - Hàm số: Số giá trị nguyên của m để hàm bậc ba đồng biến trên R (Trang 75 - Câu 2)"""
    choice = random.choice([(4, -1, 4), (10, -2, 5), (18, -3, 6), (28, -4, 7)])
    u, m_min, m_max = choice
    ans = m_max - m_min + 1

    caudan = fr'''Có bao nhiêu giá trị nguyên của tham số $m$ để hàm số $y = x^3 - mx^2 + \left(m + \dfrac{{{u}}}{{3}}\right)x$ đồng biến trên $\mathbb{{R}}$?'''

    loi_giai = fr'''Tập xác định: $D = \mathbb{{R}}$.
Ta có đạo hàm: $y' = 3x^2 - 2mx + \left(m + \dfrac{{{u}}}{{3}}\right)$.
Để hàm số đồng biến trên $\mathbb{{R}}$ thì $y' \ge 0, \forall x \in \mathbb{{R}}$
\[ \iff \begin{{cases}} a = 3 > 0 \text{{ (luôn đúng)}} \\ \Delta' \le 0 \end{{cases}} \]
Ta có:
\[ \Delta' = (-m)^2 - 3\left(m + \dfrac{{{u}}}{{3}}\right) = m^2 - 3m - {u} \le 0 \iff {m_min} \le m \le {m_max}. \]
Vì $m \in \mathbb{{Z}}$ nên $m \in \{{{", ".join(str(i) for i in range(m_min, m_max + 1))}\}}$.
Vậy có tất cả ${ans}$ giá trị nguyên của tham số $m$ thỏa mãn yêu cầu.'''

    return caudan, loi_giai, str(ans)


def HamSo_SA_Trang75_Cau3_TiemCanXien():
    """Trả lời ngắn - Hàm số: Tiệm cận xiên y = ax + b, tính k1*a - k2*b (Trang 75 - Câu 3)"""
    c = random.choice([2, 3])
    u = random.choice([-4, -3, -1, 1, 3])
    v = random.choice([-3, -1, 1, 3])
    
    a_val = 1
    b_val = u + c
    
    k1 = random.randint(2, 4)
    k2 = random.randint(2, 5)
    ans = k1 * a_val - k2 * b_val
    
    num_str = f"x^2 " + (f"+ {u}x" if u > 0 else f"- {abs(u)}x") + (f" + {v}" if v > 0 else f" - {abs(v)}")

    caudan = fr'''Cho hàm số $y = \dfrac{{{num_str}}}{{x - {c}}}$. Đồ thị hàm số có đường tiệm cận xiên là $y = ax + b$. Khi đó giá trị biểu thức $P = {k1}a - {k2}b$ là:'''

    loi_giai = fr'''Thực hiện phép chia đa thức:
\[ \dfrac{{{num_str}}}{{x - {c}}} = (x {f"+ {b_val}" if b_val >= 0 else f"- {abs(b_val)}"}) + \dfrac{{{c * b_val + v}}}{{x - {c}}}. \]
Suy ra phương trình đường tiệm cận xiên là:
\[ y = ax + b = x {f"+ {b_val}" if b_val >= 0 else f"- {abs(b_val)}"}. \]
Do đó:
\[ a = 1, \quad b = {b_val}. \]
Giá trị của biểu thức $P$ là:
\[ P = {k1}a - {k2}b = {k1}\cdot(1) - {k2}\cdot({b_val}) = {ans}. \]
Vậy giá trị biểu thức là ${ans}$.'''

    return caudan, loi_giai, str(ans)


def HamSo_SA_Trang75_Cau4_VanTocLonNhat():
    """Trả lời ngắn - Hàm số: Vận tốc tức thời lớn nhất của chất điểm v(t) = -t^3 + 3at^2 + v0 (Trang 75 - Câu 4)"""
    a = random.choice([1, 2])
    v0 = random.randint(250, 350)
    T = random.randint(2 * a + 3, 2 * a + 5)
    
    t_max = 2 * a
    v_max = 4 * (a**3) + v0
    he_so_t2 = 3 * a

    caudan = fr'''Một chất điểm chuyển động có vận tốc tức thời $v(t)$ phụ thuộc vào thời gian $t$ theo hàm số $v(t) = -t^3 + {he_so_t2}t^2 + {v0}\text{{ (m/s)}}$. Trong khoảng thời gian từ $t = 0\text{{ (s)}}$ đến $t = {T}\text{{ (s)}}$ chất điểm đạt vận tốc lớn nhất bằng bao nhiêu?'''

    loi_giai = fr'''Xét hàm số $v(t) = -t^3 + {he_so_t2}t^2 + {v0}$ trên đoạn $[0; {T}]$.
Đạo hàm: $v'(t) = -3t^2 + {6*a}t = -3t(t - {2*a})$.
Cho $v'(t) = 0 \iff \left[\begin{{aligned}} t &= 0 \in [0; {T}] \\ t &= {t_max} \in [0; {T}] \end{{aligned}}\right.$
Tính các giá trị tại các điểm đặc biệt:
\begin{{itemize}}
\item $v(0) = {v0}\text{{ (m/s)}}$.
\item $v({t_max}) = -({t_max})^3 + {he_so_t2}({t_max})^2 + {v0} = {v_max}\text{{ (m/s)}}$.
\item $v({T}) = -({T})^3 + {he_so_t2}({T})^2 + {v0} = {-T**3 + he_so_t2*(T**2) + v0}\text{{ (m/s)}}$.
\end{{itemize}}
So sánh các giá trị trên, ta thấy vận tốc lớn nhất của chất điểm là:
\[ v_{{\max}} = v({t_max}) = {v_max}\text{{ (m/s)}}. \]
Vậy vận tốc lớn nhất của chất điểm là ${v_max}$.'''

    return caudan, loi_giai, str(v_max)


def HamSo_SA_Trang75_Cau5_GiaoDiemLoaiNghiem():
    """Trả lời ngắn - Hàm số: Tọa độ giao điểm đồ thị loại nghiệm triệt tiêu mẫu (Trang 75 - Câu 5)"""
    x1 = random.choice([1, 2])
    k = random.choice([1, 2, 3])
    if k + 1 == x1:
        k += 1
        
    x0 = k + 1
    y0 = x0 + k
    
    num_P = x0**2 + y0**2 - 3 * x0 * y0
    den_P = x0 + y0
    b_term = 2 * x1 + 1
    
    caudan = fr'''Đồ thị hai hàm số $y = \dfrac{{2x^2 - {b_term}x + {x1}}}{{x - {x1}}}$ và $y = x + {k}$ cắt nhau tại điểm $M_0(x_0; y_0)$. Khi đó giá trị biểu thức $P = \dfrac{{x_0^2 + y_0^2 - 3x_0 y_0}}{{x_0 + y_0}}$ là:'''

    ans_val = num_P / den_P
    ans_str = f"{int(ans_val)}" if ans_val.is_integer() else f"{round(ans_val, 2)}".replace('.', ',')

    loi_giai = fr'''Điều kiện xác định: $x \ne {x1}$.
Phương trình hoành độ giao điểm của hai đồ thị hàm số:
\[ \dfrac{{2x^2 - {b_term}x + {x1}}}{{x - {x1}}} = x + {k} \]
Vì $2x^2 - {b_term}x + {x1} = (x - {x1})(2x - 1)$ nên với điều kiện $x \ne {x1}$, phương trình tương đương:
\[ 2x - 1 = x + {k} \iff x = {x0}. \]
Giá trị $x_0 = {x0}$ thỏa mãn điều kiện $x \ne {x1}$.
Tung độ giao điểm tương ứng:
\[ y_0 = {x0} + {k} = {y0}. \]
Tọa độ giao điểm là $M_0({x0}; {y0})$.
Thay vào biểu thức $P$, ta được:
\[ P = \dfrac{{{x0}^2 + {y0}^2 - 3 \cdot {x0} \cdot {y0}}}{{{x0} + {y0}}} = \dfrac{{{x0**2} + {y0**2} - {3*x0*y0}}}{{{den_P}}} = \dfrac{{{num_P}}}{{{den_P}}} = {ans_str}. \]
Vậy giá trị của biểu thức $P$ là ${ans_str}$.'''

    return caudan, loi_giai, ans_str


def HamSo_SA_Trang75_Cau6_GTNN_TrenDoan():
    """Trả lời ngắn - Hàm số: Tìm GTNN của hàm bậc ba f(x) = x^3 - 8x^2 + 16x + d trên [1; 3] (Trang 75 - Câu 6)"""
    d = random.randint(-12, -6)
    ans = 3 + d

    sign_d = f"+ {d}" if d > 0 else f"- {abs(d)}"
    caudan = fr'''Cho hàm số $f(x) = x^3 - 8x^2 + 16x {sign_d}$. Tìm giá trị nhỏ nhất của hàm số trên đoạn $[1; 3]$.'''

    loi_giai = fr'''Hàm số liên tục trên đoạn $[1; 3]$.
Đạo hàm: $f'(x) = 3x^2 - 16x + 16 = (3x - 4)(x - 4)$.
Cho $f'(x) = 0 \iff \left[\begin{{aligned}} x &= \dfrac{{4}}{{3}} \in [1; 3] \\ x &= 4 \notin [1; 3] \end{{aligned}}\right.$
Tính các giá trị của hàm số:
\begin{{itemize}}
\item $f(1) = 1^3 - 8\cdot 1^2 + 16\cdot 1 {sign_d} = {9 + d}$.
\item $f(3) = 3^3 - 8\cdot 3^2 + 16\cdot 3 {sign_d} = {3 + d}$.
\item $f\left(\dfrac{{4}}{{3}}\right) = \left(\dfrac{{4}}{{3}}\right)^3 - 8\left(\dfrac{{4}}{{3}}\right)^2 + 16\left(\dfrac{{4}}{{3}}\right) {sign_d} = \dfrac{{256}}{{27}} {sign_d} = \dfrac{{{256 + 27*d}}}{{27}} \approx {round(256/27 + d, 2)}$.
\end{{itemize}}
So sánh các giá trị trên, ta có:
\[ \min_{{[1; 3]}} f(x) = f(3) = {ans}. \]
Vậy giá trị nhỏ nhất của hàm số trên đoạn $[1; 3]$ là ${ans}$.'''

    return caudan, loi_giai, str(ans)


def HamSo_SA_VanTocGiam():
    """Trả lời ngắn - Hàm số: Kể từ giây thứ bao nhiêu thì vận tốc v(t) của vật giảm (Câu 2)"""
    a = random.choice([1, 2])
    t0 = random.choice([1.5, 2.0, 2.5, 3.0, 3.5, 4.0, 4.5, 5.0])
    b = int(2 * a * t0) if (2 * a * t0).is_integer() else round(2 * a * t0, 1)
    
    min_c = int(-a * (t0**2)) + 1
    c = random.randint(min_c, min_c + 8)
    
    poly_terms = []
    if a == 1:
        poly_terms.append("-t^2")
    else:
        poly_terms.append(f"-{a}t^2")
        
    if b > 0:
        poly_terms.append(f"+ {b}t")
    elif b < 0:
        poly_terms.append(f"- {abs(b)}t")
        
    if c > 0:
        poly_terms.append(f"+ {c}")
    elif c < 0:
        poly_terms.append(f"- {abs(c)}")
    elif not poly_terms:
        poly_terms.append("0")
        
    v_str = " ".join(poly_terms)
    
    ans_val = int(t0) if t0.is_integer() else t0
    ans_str = f"{ans_val}".replace(".", ",")
    ans_num = f"{ans_val}"
    
    caudan = fr'''Một chuyển động có vận tốc được xác định bởi phương trình $v(t) = {v_str}$ với $t \ge 0$, trong đó $t$ tính bằng giây và $v$ tính bằng m/s. Kể từ giây thứ bao nhiêu trở đi thì vận tốc của vật giảm?'''
    
    loi_giai = fr'''Gia tốc tức thời của chuyển động tại thời điểm $t$ là:
\[ a(t) = v'(t) = \left({v_str}\right)' = {-2*a}t + {b}. \]
Vận tốc của vật giảm khi và chỉ khi đạo hàm $v'(t) < 0$:
\[ v'(t) < 0 \iff {-2*a}t + {b} < 0 \iff {-2*a}t < -{b} \iff t > \dfrac{{{b}}}{{{2*a}}} = {ans_str}. \]
Vậy kể từ giây thứ ${ans_str}$ trở đi thì vận tốc của vật bắt đầu giảm.'''

    return caudan, loi_giai, ans_num


def HamSo_SA_CucTri_BieuThuc_x1_x2():
    """Trả lời ngắn - Hàm số: Điểm cực đại x1, cực tiểu x2, tính biểu thức A = k1*x1 + k2*3x2 (Câu 3)"""
    valid_pairs = []
    for x1_cand in [-1, 0, 1, 2]:
        for p_cand in range(3 * x1_cand + 1, 3 * x1_cand + 12):
            if p_cand % 3 != 0 and (3 * x1_cand + p_cand) % 2 == 0:
                valid_pairs.append((x1_cand, p_cand))
                
    x1, p = random.choice(valid_pairs)
    b_coef = - (3 * x1 + p) // 2
    c_coef = p * x1
    d = random.randint(-6, 6)
    
    k1 = random.choice([1, 2, 3, -1, -2])
    k2 = random.choice([1, 2, 3])
    ans = k1 * x1 - k2 * p
    
    t1 = "x_1" if k1 == 1 else ("-x_1" if k1 == -1 else f"{k1}x_1")
    t2 = f"- {3*k2}x_2"
    expr_A = f"{t1} {t2}"
    
    poly_y = fmt_poly_deg3(1, b_coef, c_coef, d)
    poly_y_prime = fmt_poly_deg2(3, 2 * b_coef, c_coef)
    
    caudan = fr'''Cho hàm số $y = {poly_y}$. Hàm số có điểm cực đại và điểm cực tiểu lần lượt là $x_1, x_2$. Tính giá trị biểu thức $A = {expr_A}$.'''
    
    loi_giai = fr'''Tập xác định: $D = \mathbb{{R}}$.
Ta có đạo hàm:
\[ y' = {poly_y_prime} = (x - {x1})(3x - {p}). \]
Cho $y' = 0 \iff \left[\begin{{aligned}} x &= {x1} \\ x &= \dfrac{{{p}}}{{3}} \end{{aligned}}\right.$
Vì hệ số bậc ba $a = 1 > 0$ và ${x1} < \dfrac{{{p}}}{{3}}$ nên qua điểm $x = {x1}$ đạo hàm đổi dấu từ dương sang âm, qua điểm $x = \dfrac{{{p}}}{{3}}$ đạo hàm đổi dấu từ âm sang dương.
Do đó, hàm số đạt cực đại tại $x_1 = {x1}$ và đạt cực tiểu tại $x_2 = \dfrac{{{p}}}{{3}}$.
Suy ra:
\[ 3x_2 = {p}. \]
Thay vào biểu thức $A$, ta được:
\[ A = {expr_A} = {k1}\cdot ({x1}) - {k2}\cdot (3x_2) = {k1 * x1} - {k2}\cdot ({p}) = {ans}. \]
Vậy giá trị biểu thức $A$ bằng ${ans}$.'''

    return caudan, loi_giai, str(ans)


def HamSo_SA_GTLN_GTNN_Logarit():
    """Trả lời ngắn - Hàm số: Tích GTLN và GTNN của hàm y = x - ln x + c trên [1/m; e] bằng ae + b, tính Y1*a - Y2*b (Câu 4)"""
    m = random.choice([2, 3, 4])
    c = random.choice([0, 1, 2])
    
    a_val = 1 + c
    b_val = c**2 - 1
    
    Y1 = random.choice([2024, 2025, 2026, 2027])
    Y2 = random.choice([2025, 2026, 2027, 2028])
    if Y1 == Y2:
        Y2 += 1
        
    ans = Y1 * a_val - Y2 * b_val
    
    y_str = "x - \\ln x" + (f" + {c}" if c > 0 else "")
    
    caudan = fr'''Cho hàm số $y = {y_str}$. Tích của giá trị lớn nhất và giá trị nhỏ nhất của hàm số trên đoạn $\left[\dfrac{{1}}{{{m}}}; e\right]$ bằng $ae + b$. Tính ${Y1}a - {Y2}b$.'''
    
    y_1m = fr"\dfrac{{1}}{{{m}}} + \ln {m}" + (f" + {c}" if c > 0 else "")
    min_val = 1 + c
    max_val_str = f"e {f'+ {c-1}' if c-1 > 0 else (f'- {abs(c-1)}' if c-1 < 0 else '')}".strip()
    
    b_sign = f"+ {b_val}" if b_val >= 0 else f"- {abs(b_val)}"
    
    loi_giai = fr'''Hàm số $y = {y_str}$ liên tục trên đoạn $\left[\dfrac{{1}}{{{m}}}; e\right]$.
Ta có: $y' = 1 - \dfrac{{1}}{{x}} = \dfrac{{x - 1}}{{x}}$.
Cho $y' = 0 \iff x = 1 \in \left[\dfrac{{1}}{{{m}}}; e\right]$.
Tính các giá trị tại các điểm đầu mút và điểm tới hạn:
\begin{{itemize}}
\item $y(1) = 1 - \ln 1 {f"+ {c}" if c > 0 else ""} = {min_val}$.
\item $y\left(\dfrac{{1}}{{{m}}}\right) = \dfrac{{1}}{{{m}}} - \ln\left(\dfrac{{1}}{{{m}}}\right) {f"+ {c}" if c > 0 else ""} = {y_1m} \approx {round(1/m + math.log(m) + c, 3)}$.
\item $y(e) = e - \ln e {f"+ {c}" if c > 0 else ""} = e - 1 {f"+ {c}" if c > 0 else ""} = {max_val_str} \approx {round(math.e - 1 + c, 3)}$.
\end{{itemize}}
So sánh các giá trị, ta được:
\[ \min_{{\left[\frac{{1}}{{{m}}}; e\right]}} y = y(1) = {min_val}, \quad \max_{{\left[\frac{{1}}{{{m}}}; e\right]}} y = y(e) = {max_val_str}. \]
Tích của giá trị lớn nhất và giá trị nhỏ nhất là:
\[ P = \min \cdot \max = {min_val}\cdot ({max_val_str}) = {a_val}e {b_sign}. \]
Theo giả thiết $P = ae + b$, suy ra:
\[ a = {a_val}, \quad b = {b_val}. \]
Do đó:
\[ {Y1}a - {Y2}b = {Y1}\cdot ({a_val}) - {Y2}\cdot ({b_val}) = {ans}. \]
Vậy giá trị của biểu thức là ${ans}$.'''

    return caudan, loi_giai, str(ans)


def LuongGiac_MC_NghiemTrenDoan():
    """Trắc nghiệm - Lượng giác: Phương trình cos x = cos(alpha) trên đoạn [0; 2pi] (Ảnh 1 - Câu 1)"""
    alpha_data = [
        (r"\dfrac{\pi}{6}", r"\dfrac{11\pi}{6}", r"\dfrac{5\pi}{6}", r"\dfrac{7\pi}{6}", r"-\dfrac{\pi}{6}"),
        (r"\dfrac{\pi}{4}", r"\dfrac{7\pi}{4}", r"\dfrac{3\pi}{4}", r"\dfrac{5\pi}{4}", r"-\dfrac{\pi}{4}"),
        (r"\dfrac{\pi}{3}", r"\dfrac{5\pi}{3}", r"\dfrac{2\pi}{3}", r"\dfrac{4\pi}{3}", r"-\dfrac{\pi}{3}"),
        (r"\dfrac{2\pi}{3}", r"\dfrac{4\pi}{3}", r"\dfrac{\pi}{3}", r"\dfrac{5\pi}{3}", r"-\dfrac{2\pi}{3}"),
        (r"\dfrac{3\pi}{4}", r"\dfrac{5\pi}{4}", r"\dfrac{\pi}{4}", r"\dfrac{7\pi}{4}", r"-\dfrac{3\pi}{4}"),
        (r"\dfrac{5\pi}{6}", r"\dfrac{7\pi}{6}", r"\dfrac{\pi}{6}", r"\dfrac{11\pi}{6}", r"-\dfrac{5\pi}{6}"),
    ]
    a_tex, a_opp_2pi, a_pi_minus, a_pi_plus, a_neg = random.choice(alpha_data)
    
    caudan = fr'''Phương trình $\cos x = \cos {a_tex}$ có tập nghiệm trên đoạn $[0; 2\pi]$ là'''
    
    opt_correct = fr"$\left\{{{a_tex}; {a_opp_2pi}\right\}}$"
    opt_wrong1 = fr"$\left\{{{a_tex}; {a_pi_minus}\right\}}$"
    opt_wrong2 = fr"$\left\{{{a_tex}; {a_pi_plus}\right\}}$"
    opt_wrong3 = fr"$\left\{{{a_tex}; {a_neg}\right\}}$"
    
    choices = shuffle_choices(opt_correct, [opt_wrong1, opt_wrong2, opt_wrong3])
    
    loi_giai = fr'''Phương trình $\cos x = \cos {a_tex} \iff \left[\begin{{aligned}} x &= {a_tex} + k2\pi \\ x &= -{a_tex} + k2\pi \end{{aligned}}\right. \quad (k \in \mathbb{{Z}})$.
Vì $x \in [0; 2\pi]$ nên:
\begin{{itemize}}
\item Với $x = {a_tex} + k2\pi \implies 0 \le {a_tex} + k2\pi \le 2\pi \implies k = 0 \implies x = {a_tex}$.
\item Với $x = -{a_tex} + k2\pi \implies 0 \le -{a_tex} + k2\pi \le 2\pi \implies k = 1 \implies x = 2\pi - {a_tex} = {a_opp_2pi}$.
\end{{itemize}}
Vậy tập nghiệm của phương trình trên đoạn $[0; 2\pi]$ là {opt_correct}.'''

    return caudan, choices, loi_giai


def Logarit_MC_BatPhuongTrinhCoBan():
    """Trắc nghiệm - Logarit: Tập nghiệm bất phương trình log_a(x) > b cơ số nhỏ hơn 1 (Ảnh 1 - Câu 2)"""
    data = [
        (r"\dfrac{1}{2}", -1, 2),
        (r"\dfrac{1}{2}", -2, 4),
        (r"\dfrac{1}{3}", -1, 3),
        (r"\dfrac{1}{3}", -2, 9),
        (r"\dfrac{1}{4}", -1, 4),
    ]
    a_tex, b_val, val_pow = random.choice(data)
    
    caudan = fr'''Tập nghiệm của bất phương trình $\log_{{{a_tex}}}(x) > {b_val}$ là'''
    
    opt_correct = fr"$(0; {val_pow})$"
    opt_wrong1 = fr"$({val_pow}; +\infty)$"
    opt_wrong2 = fr"$(-\infty; {val_pow})$"
    opt_wrong3 = fr"$(0; +\infty)$"
    
    choices = shuffle_choices(opt_correct, [opt_wrong1, opt_wrong2, opt_wrong3])
    
    loi_giai = fr'''Điều kiện xác định: $x > 0$.
Vì cơ số $0 < {a_tex} < 1$ nên khi bỏ logarit ta phải đổi chiều bất phương trình:
\[ \log_{{{a_tex}}}(x) > {b_val} \iff x < \left({a_tex}\right)^{{{b_val}}} = {val_pow}. \]
Kết hợp với điều kiện $x > 0$, ta được tập nghiệm là:
\[ S = (0; {val_pow}). \]'''

    return caudan, choices, loi_giai


def DaySo_MC_CapSoCong_TongSn():
    """Trắc nghiệm - Cấp số cộng: Cho Sn = an^2 + bn, tính số hạng thứ k uk (Ảnh 1 - Câu 3)"""
    a = random.choice([1, 2, 3])
    b = random.choice([1, 2, 3, -1])
    k = random.choice([4, 5, 6, 7])
    
    uk = 2 * a * k + (b - a)
    
    b_str = f"+ {b}n" if b > 0 else f"- {abs(b)}n"
    a_str = f"{a}n^2" if a > 1 else "n^2"
    
    caudan = fr'''Cho cấp số cộng $(u_n)$ có tổng $n$ số hạng đầu là $S_n = {a_str} {b_str}$. Số hạng $u_{{{k}}}$ bằng'''
    
    correct_str = str(uk)
    wrong1 = str(uk - 2)
    wrong2 = str(uk + 1)
    wrong3 = str(uk + 2)
    
    choices = shuffle_choices(correct_str, [wrong1, wrong2, wrong3])
    
    Sk = a * (k**2) + b * k
    Sk_prev = a * ((k-1)**2) + b * (k-1)
    
    loi_giai = fr'''Ta có mối liên hệ giữa số hạng thứ $k$ và tổng $k$ số hạng đầu của cấp số cộng:
\[ u_{{{k}}} = S_{{{k}}} - S_{{{k-1}}}. \]
Với $k = {k}$:
\begin{{itemize}}
\item $S_{{{k}}} = {a}\cdot {k}^2 {f"+ {b}" if b>0 else f"- {abs(b)}"}\cdot {k} = {Sk}$.
\item $S_{{{k-1}}} = {a}\cdot {k-1}^2 {f"+ {b}" if b>0 else f"- {abs(b)}"}\cdot {k-1} = {Sk_prev}$.
\end{{itemize}}
Do đó:
\[ u_{{{k}}} = {Sk} - {Sk_prev} = {uk}. \]
Vậy $u_{{{k}}} = {uk}$.'''

    return caudan, choices, loi_giai


def Oxyz_MC_DiemThuocDuongThang():
    """Trắc nghiệm - Oxyz: Điểm nào sau đây KHÔNG thuộc đường thẳng tham số d (Ảnh 1 - Câu 6)"""
    x0 = random.randint(-5, 5)
    y0 = random.randint(-5, 5)
    z0 = random.randint(-5, 5)
    
    a = random.choice([-3, -2, -1, 1, 2, 3])
    b = random.choice([-3, -2, -1, 1, 2, 3])
    c = random.choice([-3, -2, -1, 1, 2, 3])
    
    t1, t2, t3 = random.sample([-3, -2, -1, 0, 1, 2, 3], 3)
    p1 = (x0 + a * t1, y0 + b * t1, z0 + c * t1)
    p2 = (x0 + a * t2, y0 + b * t2, z0 + c * t2)
    p3 = (x0 + a * t3, y0 + b * t3, z0 + c * t3)
    
    t_wrong = random.choice([t for t in [-3, -2, -1, 0, 1, 2, 3] if t not in [t1, t2, t3]])
    delta = random.choice([-2, -1, 1, 2])
    p_wrong = (x0 + a * t_wrong, y0 + b * t_wrong, z0 + c * t_wrong + delta)
    
    fx = f"{x0} " + (f"+ {a}t" if a > 0 else f"- {abs(a)}t")
    fy = f"{y0} " + (f"+ {b}t" if b > 0 else f"- {abs(b)}t")
    fz = f"{z0} " + (f"+ {c}t" if c > 0 else f"- {abs(c)}t")
    
    caudan = fr'''Trong không gian $Oxyz$, cho đường thẳng $d: \begin{{cases}} x = {fx} \\ y = {fy} \\ z = {fz} \end{{cases}}$. Điểm nào sau đây KHÔNG thuộc $d$?'''
    
    pt_w_str = f"M({p_wrong[0]}; {p_wrong[1]}; {p_wrong[2]})"
    pt1_str = f"A({p1[0]}; {p1[1]}; {p1[2]})"
    pt2_str = f"B({p2[0]}; {p2[1]}; {p2[2]})"
    pt3_str = f"C({p3[0]}; {p3[1]}; {p3[2]})"
    
    choices = shuffle_choices(pt_w_str, [pt1_str, pt2_str, pt3_str])
    
    loi_giai = fr'''Thay tọa độ điểm ${pt_w_str}$ vào phương trình tham số của $d$:
\[ \begin{{cases}} {p_wrong[0]} = {fx} \\ {p_wrong[1]} = {fy} \\ {p_wrong[2]} = {fz} \end{{cases}} \iff \begin{{cases}} t = {t_wrong} \\ t = {t_wrong} \\ t = \dfrac{{{p_wrong[2] - z0}}}{{{c}}} \ne {t_wrong} \end{{cases}} \]
Hệ phương trình vô nghiệm $t$, do đó điểm ${pt_w_str}$ không thuộc đường thẳng $d$.'''

    return caudan, choices, loi_giai


def HinhHoc_MC_LangTru_HaiMatPhangVuongGoc():
    """Trắc nghiệm - Hình học: Lăng trụ đứng ABC.A'B'C' đáy vuông, tìm hai mặt phẳng vuông góc (Ảnh 2 - Câu 10)"""
    vertex_choices = ['B', 'A', 'C']
    v_right = random.choice(vertex_choices)
    
    if v_right == 'B':
        mp_given = r"(BCC'B')"
        mp_correct = r"(ABB'A')"
        mp_wrong1 = r"(ACC'A')"
        mp_wrong2 = r"(A'BC)"
        mp_wrong3 = r"(AB'C')"
        expl = r"Vì $ABC.A'B'C'$ là lăng trụ đứng nên $BB' \perp (ABC) \implies BB' \perp AB$. Lại có đáy $ABC$ vuông tại $B$ nên $BC \perp AB$. Suy ra $AB \perp (BCC'B')$. Mà $AB \subset (ABB'A')$ nên $(ABB'A') \perp (BCC'B')$."
    elif v_right == 'A':
        mp_given = r"(ACC'A')"
        mp_correct = r"(ABB'A')"
        mp_wrong1 = r"(BCC'B')"
        mp_wrong2 = r"(A'BC)"
        mp_wrong3 = r"(A'B'C)"
        expl = r"Vì lăng trụ đứng nên $AA' \perp (ABC) \implies AA' \perp AB$. Đáy vuông tại $A$ nên $AC \perp AB$. Suy ra $AB \perp (ACC'A')$. Mà $AB \subset (ABB'A')$ nên $(ABB'A') \perp (ACC'A')$."
    else:
        mp_given = r"(ACC'A')"
        mp_correct = r"(BCC'B')"
        mp_wrong1 = r"(ABB'A')"
        mp_wrong2 = r"(AB'C)"
        mp_wrong3 = r"(A'B'C)"
        expl = r"Vì lăng trụ đứng nên $CC' \perp (ABC) \implies CC' \perp BC$. Đáy vuông tại $C$ nên $AC \perp BC$. Suy ra $BC \perp (ACC'A')$. Mà $BC \subset (BCC'B')$ nên $(BCC'B') \perp (ACC'A')$."

    caudan = fr'''Cho lăng trụ đứng $ABC.A'B'C'$ có đáy $ABC$ là tam giác vuông tại ${v_right}$. Mặt phẳng ${mp_given}$ vuông góc với mặt phẳng nào dưới đây?
\begin{{center}}
\begin{{tikzpicture}}[scale=0.9,>=stealth]
\coordinate (A) at (0,0);
\coordinate (B) at (1.2,-1);
\coordinate (C) at (3.5,0);
\coordinate (A1) at (0,2.5);
\coordinate (B1) at (1.2,1.5);
\coordinate (C1) at (3.5,2.5);
\draw (A) -- (B) -- (C) (A1) -- (B1) -- (C1) -- cycle;
\draw (A) -- (A1) (B) -- (B1) (C) -- (C1);
\draw[dashed] (A) -- (C);
\node[left] at (A) {{$A$}};
\node[below] at (B) {{$B$}};
\node[right] at (C) {{$C$}};
\node[left] at (A1) {{$A'$}};
\node[below] at (B1) {{$B'$}};
\node[right] at (C1) {{$C'$}};
\end{{tikzpicture}}
\end{{center}}'''

    choices = shuffle_choices(f"${mp_correct}$", [f"${mp_wrong1}$", f"${mp_wrong2}$", f"${mp_wrong3}$"])
    loi_giai = expl

    return caudan, choices, loi_giai


def XacSuat_MC_CongThucBienCoDoiDieuKien():
    """Trắc nghiệm - Xác suất: Cho P(A) và P(B_ngang|A), tính P(A B_ngang) (Ảnh 2 - Câu 12)"""
    p_A = round(random.uniform(0.12, 0.45), 2)
    p_B_bar_given_A = round(random.choice([0.4, 0.5, 0.6, 0.7, 0.8]), 2)
    
    ans_val = round(p_A * p_B_bar_given_A, 4)
    ans_str = f"{ans_val}".replace(".", ",")
    
    w1_val = round(ans_val * 10, 3)
    w1_str = f"{w1_val}".replace(".", ",")
    
    w2_val = round(p_A * 0.5, 3)
    w2_str = f"{w2_val}".replace(".", ",")
    
    w3_val = round(abs(p_A - p_B_bar_given_A), 2)
    w3_str = f"{w3_val}".replace(".", ",")
    
    p_A_str = f"{p_A}".replace(".", ",")
    p_cond_str = f"{p_B_bar_given_A}".replace(".", ",")
    
    caudan = fr'''Cho hai biến cố $A$ và $B$. Biết $P(A) = {p_A_str}$ và $P(\overline{{B}}|A) = {p_cond_str}$. Giá trị của $P(A\overline{{B}})$ bằng'''
    
    choices = shuffle_choices(ans_str, [w1_str, w2_str, w3_str])
    
    loi_giai = fr'''Theo công thức nhân xác suất (xác suất có điều kiện):
\[ P(A\overline{{B}}) = P(A) \cdot P(\overline{{B}}|A) = {p_A_str} \times {p_cond_str} = {ans_str}. \]
Vậy giá trị của $P(A\overline{{B}})$ là ${ans_str}$.'''

    return caudan, choices, loi_giai


def XacSuat_TF_ToanThucTe_HocSinhTuTin():
    """Đúng/Sai - Xác suất toàn phần & Bayes: Học sinh chăm chỉ ôn tập và tỷ lệ tự tin (Ảnh 3 - Câu 4)"""
    N = 50
    n_cham = random.choice([30, 40])
    n_khong = N - n_cham
    
    pct_khong = int(n_khong / N * 100)
    pct_cham = int(n_cham / N * 100)
    
    if n_cham == 30:
        p_cham_pct = 90
        n_cham_tutin = int(n_cham * 0.90)
        p_khong_pct = 15
        n_khong_tutin = int(n_khong * 0.15)
    else:
        p_cham_pct = 85
        n_cham_tutin = int(n_cham * 0.85)
        p_khong_pct = 20
        n_khong_tutin = int(n_khong * 0.20)
        
    n_tong_tutin = n_cham_tutin + n_khong_tutin
    pct_khong_given_tutin = int(round(n_khong_tutin / n_tong_tutin * 100))
    
    caudan = fr'''Lớp 12A1 có ${N}$ học sinh. Chuẩn bị cho kỳ thi tốt nghiệp THPT sắp tới, có ${n_cham}$ bạn trong lớp chăm chỉ ôn tập. Trước kỳ thi, giáo viên chủ nhiệm khảo sát ngẫu nhiên một bạn trong lớp. Qua khảo sát, tỉ lệ tự tin trong số những bạn chăm chỉ ôn tập là ${p_cham_pct}\%$ và tỉ lệ tự tin trong số những bạn không chăm chỉ ôn tập là ${p_khong_pct}\%$. Xét tính đúng sai của các khẳng định sau:'''
    
    stmt_a_t = fr"Có ${pct_khong}\%$ học sinh trong lớp đã không chăm chỉ ôn tập."
    stmt_a_f = fr"Có ${pct_khong + 10}\%$ học sinh trong lớp đã không chăm chỉ ôn tập."
    exp_a_t = fr"Số học sinh không chăm chỉ ôn tập là ${N} - {n_cham} = {n_khong}$ học sinh, chiếm tỉ lệ $\dfrac{{{n_khong}}}{{{N}}} = {pct_khong}\%$."
    exp_a_f = fr"Tỉ lệ học sinh không chăm chỉ ôn tập là $\dfrac{{{N} - {n_cham}}}{{{N}}} = \dfrac{{{n_khong}}}{{{N}}} = {pct_khong}\% \ne {pct_khong + 10}\%$."
    
    stmt_b_t = fr"Có ${n_cham_tutin}$ học sinh đã chăm chỉ ôn tập và tự tin trước kỳ thi."
    stmt_b_f = fr"Có ${n_cham_tutin - 3}$ học sinh đã chăm chỉ ôn tập và tự tin trước kỳ thi."
    exp_b_t = fr"Số học sinh chăm chỉ ôn tập và tự tin là ${n_cham} \times {p_cham_pct}\% = {n_cham_tutin}$ học sinh."
    exp_b_f = fr"Số học sinh chăm chỉ ôn tập và tự tin là ${n_cham} \times {p_cham_pct}\% = {n_cham_tutin}$ học sinh, không phải ${n_cham_tutin - 3}$."
    
    stmt_c_t = fr"Có ${n_khong_tutin}$ học sinh đã không chăm chỉ ôn tập mà vẫn tự tin trước kỳ thi."
    stmt_c_f = fr"Có ${n_khong_tutin + 2}$ học sinh đã không chăm chỉ ôn tập mà vẫn tự tin trước kỳ thi."
    exp_c_t = fr"Số học sinh không chăm chỉ ôn tập nhưng vẫn tự tin là ${n_khong} \times {p_khong_pct}\% = {n_khong_tutin}$ học sinh."
    exp_c_f = fr"Số học sinh không chăm chỉ ôn tập nhưng vẫn tự tin là ${n_khong} \times {p_khong_pct}\% = {n_khong_tutin}$ học sinh, không phải ${n_khong_tutin + 2}$."
    
    stmt_d_t = fr"Trong số những bạn tự tin trước kỳ thi, xác suất chọn được một bạn không chăm chỉ ôn tập là ${pct_khong_given_tutin}\%$."
    stmt_d_f = fr"Trong số những bạn tự tin trước kỳ thi, xác suất chọn được một bạn không chăm chỉ ôn tập là ${pct_khong_given_tutin + 10}\%$."
    exp_d_t = fr"Tổng số bạn tự tin là ${n_cham_tutin} + {n_khong_tutin} = {n_tong_tutin}$ học sinh. Trong đó có ${n_khong_tutin}$ bạn không chăm chỉ, xác suất là $\dfrac{{{n_khong_tutin}}}{{{n_tong_tutin}}} = {pct_khong_given_tutin}\%$."
    exp_d_f = fr"Tổng số bạn tự tin là ${n_cham_tutin} + {n_khong_tutin} = {n_tong_tutin}$ bạn. Xác suất cần tìm là $\dfrac{{{n_khong_tutin}}}{{{n_tong_tutin}}} = {pct_khong_given_tutin}\% \ne {pct_khong_given_tutin + 10}\%$."
    
    items_data = [
        (stmt_a_t, stmt_a_f, exp_a_t, exp_a_f),
        (stmt_b_t, stmt_b_f, exp_b_t, exp_b_f),
        (stmt_c_t, stmt_c_f, exp_c_t, exp_c_f),
        (stmt_d_t, stmt_d_f, exp_d_t, exp_d_f),
    ]
    
    choices, loi_giai = make_tf_choices(items_data)
    return caudan, choices, loi_giai


def XacSuat_MC_BaXaThuBanBia():
    """
    Ảnh 1 - Câu 2: Ba tuyển thủ cùng bắn súng vào một tấm bia, tính xác suất để có đúng 2 người bắn trúng bia.
    """
    p1 = random.choice([0.4, 0.5, 0.6, 0.7])
    p2 = random.choice([p for p in [0.4, 0.5, 0.6, 0.7, 0.8] if p != p1])
    p3 = random.choice([p for p in [0.5, 0.6, 0.7, 0.8] if p != p2])
    
    q1 = round(1 - p1, 2)
    q2 = round(1 - p2, 2)
    q3 = round(1 - p3, 2)
    
    # Xác suất có đúng 2 người bắn trúng
    # P = p1*p2*q3 + p1*q2*p3 + q1*p2*p3
    term1 = p1 * p2 * q3
    term2 = p1 * q2 * p3
    term3 = q1 * p2 * p3
    P_exact2 = round(term1 + term2 + term3, 4)
    
    p1_s = f"{p1:.1f}".replace('.', ',')
    p2_s = f"{p2:.1f}".replace('.', ',')
    p3_s = f"{p3:.1f}".replace('.', ',')
    
    q1_s = f"{q1:.1f}".replace('.', ',')
    q2_s = f"{q2:.1f}".replace('.', ',')
    q3_s = f"{q3:.1f}".replace('.', ',')
    
    ans_s = f"{P_exact2:.2f}".replace('.', ',')
    
    # Nhiễu
    # Sai 1: Cả 3 cùng trúng p1*p2*p3
    w1 = round(p1 * p2 * p3, 2)
    # Sai 2: Đúng 1 người trúng
    w2 = round(p1 * q2 * q3 + q1 * p2 * q3 + q1 * q2 * p3, 2)
    # Sai 3: Ít nhất 1 người trúng 1 - q1*q2*q3
    w3 = round(1 - q1 * q2 * q3, 2)
    
    candidates = []
    for w in [w1, w2, w3, round(P_exact2 - 0.15, 2), round(P_exact2 + 0.15, 2), round(P_exact2 - 0.23, 2)]:
        if 0 < w < 1:
            ws = f"{w:.2f}".replace('.', ',')
            if ws != ans_s and ws not in candidates:
                candidates.append(ws)
        if len(candidates) == 3:
            break
            
    caudan = fr"Ba tuyển thủ cùng bắn súng vào một tấm bia, xác suất trúng đích lần lượt là ${p1_s};~{p2_s}$ và ${p3_s}$. Xác suất để có đúng 2 người bắn trúng bia là"
    
    loi_giai = fr"""Gọi $A_i$ là biến cố: ``Người thứ $i$ bắn trúng bia'' với $i \in \{{1; 2; 3\}}.$
Theo giả thiết, các biến cố $A_1, A_2, A_3$ độc lập với nhau và:
\[ P(A_1) = {p1_s},~ P(A_2) = {p2_s},~ P(A_3) = {p3_s} \]
Suy ra xác suất không trúng của mỗi người là:
\[ P(\overline{{A}}_1) = 1 - {p1_s} = {q1_s},~ P(\overline{{A}}_2) = 1 - {p2_s} = {q2_s},~ P(\overline{{A}}_3) = 1 - {p3_s} = {q3_s} \]
Gọi biến cố $B$: ``Có đúng 2 người bắn trúng bia''. Ta có:
\[ B = (A_1 A_2 \overline{{A}}_3) \cup (A_1 \overline{{A}}_2 A_3) \cup (\overline{{A}}_1 A_2 A_3) \]
Vì ba biến cố thành phần đôi một xung khắc nên:
\[ P(B) = P(A_1 A_2 \overline{{A}}_3) + P(A_1 \overline{{A}}_2 A_3) + P(\overline{{A}}_1 A_2 A_3) \]
\[ = {p1_s} \times {p2_s} \times {q3_s} + {p1_s} \times {q2_s} \times {p3_s} + {q1_s} \times {p2_s} \times {p3_s} \]
\[ = {term1:.4f} + {term2:.4f} + {term3:.4f} = {P_exact2:.4f} \approx {ans_s}. \]""".replace('.', ',')

    choices = shuffle_choices(f"${ans_s}$", [f"${c}$" for c in candidates[:3]])
    return caudan, choices, loi_giai


def Oxyz_MC_PhanTichVectoTheo3Vecto():
    """
    Ảnh 1 - Câu 3: Trong không gian Oxyz biểu diễn vectơ u theo 3 vectơ a, b, c không đồng phẳng.
    """
    while True:
        a = (random.randint(1, 4), random.randint(-3, 2), random.randint(1, 3))
        b = (random.randint(-3, -1), random.randint(1, 3), random.randint(-3, -1))
        c = (random.randint(1, 3), random.randint(1, 3), random.randint(-3, 1))
        
        det = (a[0] * (b[1] * c[2] - b[2] * c[1])
               - a[1] * (b[0] * c[2] - b[2] * c[0])
               + a[2] * (b[0] * c[1] - b[1] * c[0]))
        if det != 0:
            break
            
    # Chọn nghiệm x, y, z nguyên nhỏ đẹp
    x = random.choice([2, 3, -2, -3])
    y = random.choice([-2, -3, 2, 3])
    z = random.choice([1, -1, 2, -2])
    
    u = (x * a[0] + y * b[0] + z * c[0],
         x * a[1] + y * b[1] + z * c[1],
         x * a[2] + y * b[2] + z * c[2])
         
    def fmt_comb(k1, k2, k3):
        res = ""
        # k1*a
        if k1 == 1: res += r"\vec{a}"
        elif k1 == -1: res += r"-\vec{a}"
        else: res += rf"{k1}\vec{a}"
        # k2*b
        if k2 == 1: res += r" + \vec{b}"
        elif k2 == -1: res += r" - \vec{b}"
        elif k2 > 0: res += rf" + {k2}\vec{b}"
        else: res += rf" - {-k2}\vec{b}"
        # k3*c
        if k3 == 1: res += r" + \vec{c}"
        elif k3 == -1: res += r" - \vec{c}"
        elif k3 > 0: res += rf" + {k3}\vec{c}"
        else: res += rf" - {-k3}\vec{c}"
        return res

    correct_comb = fmt_comb(x, y, z)
    
    wrong_combs = [
        fmt_comb(x, -y, z),
        fmt_comb(x, y, -z),
        fmt_comb(y, x, z),
    ]
    if any(w == correct_comb for w in wrong_combs):
        wrong_combs = [
            fmt_comb(x+1, y, z),
            fmt_comb(x, y-1, z),
            fmt_comb(x, -y, -z)
        ]
        
    caudan = (rf"Trong không gian với hệ tọa độ $Oxyz$ cho các vectơ "
              rf"$\vec{{a}} = ({a[0]};~{a[1]};~{a[2]})$, "
              rf"$\vec{{b}} = ({b[0]};~{b[1]};~{b[2]})$, "
              rf"$\vec{{c}} = ({c[0]};~{c[1]};~{c[2]})$, "
              rf"$\vec{{u}} = ({u[0]};~{u[1]};~{u[2]})$. Mệnh đề nào sau đây đúng?")
              
    loi_giai = rf"""Giả sử $\vec{{u}} = x\vec{{a}} + y\vec{{b}} + z\vec{{c}}$. Khi đó ta có hệ phương trình:
\[ \heva{{& {a[0]}x + ({b[0]})y + ({c[0]})z = {u[0]} \\ & {a[1]}x + ({b[1]})y + ({c[1]})z = {u[1]} \\ & {a[2]}x + ({b[2]})y + ({c[2]})z = {u[2]} }} \Leftrightarrow \heva{{& x = {x} \\ & y = {y} \\ & z = {z} }} \]
Vậy $\vec{{u}} = {correct_comb}$."""

    choices = shuffle_choices(rf"$\vec{{u}} = {correct_comb}$", [rf"$\vec{{u}} = {w}$" for w in wrong_combs])
    return caudan, choices, loi_giai


def DaoHam_MC_ToanThucTe_ViKhuanGiam():
    """
    Ảnh 2 - Câu 11: Sự ảnh hưởng khi sử dụng độc tố với vi khuẩn P(t) = (t+a)/(t^2+bt+c).
    Vào thời điểm nào thì số lượng vi khuẩn bắt đầu giảm?
    """
    t0 = random.choice([1, 2, 3])
    a = random.choice([1, 2])
    b = random.choice([1, 2])
    # c = t0^2 + 2*a*t0 + a*b sao cho tử số P'(t) = -t^2 - 2at + (c - ab) = 0 có nghiệm dương t0
    c = t0**2 + 2 * a * t0 + a * b
    
    # Delta mẫu = b^2 - 4c < 0 luôn đúng vì c > 0 lớn
    caudan = (rf"Sự ảnh hưởng khi sử dụng một loại độc tố với vi khuẩn X được một nhà sinh học mô tả bởi hàm số "
              rf"$P(t) = \dfrac{{t + {a}}}{{t^2 + {b}t + {c}}}$, trong đó $P(t)$ là số lượng vi khuẩn sau thời gian $t$ "
              rf"sử dụng độc tố ($t \ge 0$). Vào thời điểm nào thì số lượng vi khuẩn X bắt đầu giảm?")
              
    correct = rf"Sau ${t0}$ giờ."
    wrong_1 = rf"Sau ${t0 + 1}$ giờ."
    wrong_2 = rf"Sau ${t0 / 2:.1f}$ giờ.".replace('.', ',') if t0 > 1 else r"Sau $0,5$ giờ."
    wrong_3 = r"Ngay từ lúc bắt đầu sử dụng độc tố."
    
    loi_giai = rf"""Ta có đạo hàm của hàm số $P(t)$:
\[ P'(t) = \dfrac{{(t+{a})'(t^2+{b}t+{c}) - (t+{a})(t^2+{b}t+{c})'}}{{(t^2+{b}t+{c})^2}} \]
\[ = \dfrac{{(t^2+{b}t+{c}) - (t+{a})(2t+{b})}}{{(t^2+{b}t+{c})^2}} = \dfrac{{-t^2 - {2*a}t + {c - a*b}}}{{(t^2+{b}t+{c})^2}} \]
Xét $P'(t) = 0 \Leftrightarrow -t^2 - {2*a}t + {c - a*b} = 0 \Leftrightarrow \hoac{{& t = {t0} \quad (\text{{thỏa mãn }} t \ge 0) \\ & t = {-t0 - 2*a} \quad (\text{{loại}})}} $
Bảng biến thiên cho thấy trên khoảng $(0; {t0})$, $P'(t) > 0$ nên số lượng vi khuẩn tăng; trên khoảng $({t0}; +\infty)$, $P'(t) < 0$ nên số lượng vi khuẩn giảm.
Vậy sau ${t0}$ giờ thì số lượng vi khuẩn bắt đầu giảm."""

    choices = shuffle_choices(correct, [wrong_1, wrong_2, wrong_3])
    return caudan, choices, loi_giai


def HamSo_MC_BangXetDauDaoHam_DiemGDT():
    """
    Ảnh 2 - Câu 12: Bảng xét dấu đạo hàm f'(x) có điểm gián đoạn của đạo hàm (dấu ||), hỏi khoảng đồng biến.
    """
    x1 = random.randint(-3, -1)
    x2 = 0
    x3 = random.randint(1, 3)
    x4 = x3 + random.randint(2, 3)
    
    caudan = (rf"Cho hàm số $y=f(x)$ liên tục trên $\mathbb{{R}}$ và có bảng xét dấu của đạo hàm như hình vẽ:"
              r"\begin{center}"
              r"\begin{tabular}{c|ccccccccccc}"
              rf"$x$ & $-\infty$ & & ${x1}$ & & ${x2}$ & & ${x3}$ & & ${x4}$ & & $+\infty$ \\ \hline"
              r"$f'(x)$ & & $+$ & $0$ & $-$ & $||$ & $+$ & $0$ & $-$ & $0$ & $+$ & "
              r"\end{tabular}"
              r"\end{center}"
              r"Hàm số đã cho đồng biến trong khoảng nào dưới đây?")
              
    correct = rf"$({x2};~{x3})$"
    wrong_1 = rf"$({x3};~{x4})$"
    wrong_2 = rf"$({x1};~{x3})$"
    wrong_3 = rf"$(-\infty;~{x2})$"
    
    loi_giai = rf"""Dựa vào bảng xét dấu đạo hàm:
- Trên khoảng $({x2};~{x3})$, ta có $f'(x) > 0$ và hàm số $y=f(x)$ liên tục trên $\mathbb{{R}}$ nên hàm số đồng biến trên khoảng $({x2};~{x3})$.
- Trên các khoảng khác: hàm số nghịch biến trên $({x1};~{x2})$ và $({x3};~{x4})$.
Do đó phương án đúng là $({x2};~{x3})$."""

    choices = shuffle_choices(correct, [wrong_1, wrong_2, wrong_3])
    return caudan, choices, loi_giai


def DaoHam_TF_VatChuyenDong_ViTri_VanToc_GiaToc():
    """
    Ảnh 3 - Câu 3: Một vật chuyển động dọc theo một trục số x(t) = t^3 - a*t^2 + b*t + c.
    4 mệnh đề đúng sai: chiều chuyển động, gia tốc a(t), tốc độ lớn nhất, giảm tốc độ.
    """
    # x(t) = t^3 - 7t^2 + 11t + 5
    a_coef = 7
    b_coef = 11
    c_coef = 5
    
    # v(t) = 3t^2 - 14t + 11
    # v'(t) = a(t) = 6t - 14
    # v(1) = 0, v(11/3) = 0
    # v(3) = 27 - 42 + 11 = -4 < 0
    
    caudan = (rf"Một vật chuyển động dọc theo một trục số nằm ngang, chiều dương từ trái sang phải. "
              rf"Giả sử vị trí của vật $x$ (mét) từ thời điểm $t = 0$ giây đến thời điểm $t = 5$ giây được cho bởi công thức "
              rf"$x(t) = t^3 - {a_coef}t^2 + {b_coef}t + {c_coef}$. Xét tính đúng sai của các khẳng định sau:")
              
    stmt_a_t = r"Trong khoảng thời gian từ thời điểm $1$ giây đến thời điểm $3$ giây vật đang chuyển động sang trái."
    stmt_a_f = r"Trong khoảng thời gian từ thời điểm $1$ giây đến thời điểm $3$ giây vật đang chuyển động sang phải."
    exp_a_t = (r"Vận tốc của vật là $v(t) = x'(t) = 3t^2 - 14t + 11$. "
               r"Với mọi $t \in (1; 3)$, ta có $v(t) < 0$ nên vật đang chuyển động ngược chiều dương, tức là chuyển động sang trái.")
    exp_a_f = (r"Vận tốc $v(t) = 3t^2 - 14t + 11$. Trên $(1; 3)$, $v(t) < 0$ nên vật chuyển động sang trái, không phải sang phải.")
    
    stmt_b_t = r"Gia tốc tức thời của vật tại thời điểm $t$ là $a(t) = 6t - 14$ (m/s$^2$)."
    stmt_b_f = r"Gia tốc tức thời của vật tại thời điểm $t$ là $a(t) = 3t^2 - 14t + 11$ (m/s$^2$)."
    exp_b_t = r"Gia tốc là đạo hàm cấp hai của phương trình vị trí: $a(t) = v'(t) = x''(t) = 6t - 14$."
    exp_b_f = r"Biểu thức $3t^2 - 14t + 11$ là vận tốc tức thời $v(t)$, gia tốc tức thời phải là đạo hàm của vận tốc: $a(t) = 6t - 14$."
    
    stmt_c_t = r"Trong khoảng thời gian từ giây thứ nhất đến giây thứ tư, tốc độ của vật lớn nhất là $\dfrac{16}{3}$ (m/s)."
    stmt_c_f = r"Trong khoảng thời gian từ giây thứ nhất đến giây thứ tư, tốc độ của vật lớn nhất là $4$ (m/s)."
    exp_c_t = (r"Tốc độ của vật là $|v(t)| = |3t^2 - 14t + 11|$. "
               r"Đỉnh parabol của $v(t)$ đạt tại $t = \dfrac{7}{3} \in [1; 4]$ với $v\left(\dfrac{7}{3}\right) = -\dfrac{16}{3}$. "
               r"Tại các mút: $v(1) = 0$, $v(4) = 3$. "
               r"Do đó tốc độ lớn nhất trên $[1; 4]$ là $\left|v\left(\dfrac{7}{3}\right)\right| = \dfrac{16}{3}$ (m/s).")
    exp_c_f = r"Tốc độ đạt cực đại tại đỉnh parabol $t = \dfrac{7}{3}$ với giá trị $\left|-\dfrac{16}{3}\right| = \dfrac{16}{3} \ne 4$."
    
    stmt_d_t = r"Trong khoảng thời gian từ khi vật bắt đầu chuyển động đến thời điểm $1$ giây vật chuyển động giảm tốc độ."
    stmt_d_f = r"Trong khoảng thời gian từ khi vật bắt đầu chuyển động đến thời điểm $3$ giây vật luôn giảm tốc độ."
    exp_d_t = (r"Tại $t=0$, vận tốc $v(0) = 11 > 0$, gia tốc $a(0) = -14 < 0$. "
               r"Trên khoảng $(0; 1)$, $v(t) > 0$ và $a(t) < 0$ nên $v(t) \cdot a(t) < 0$, vật chuyển động chậm dần (giảm tốc độ).")
    exp_d_f = (r"Trên khoảng $\left(\dfrac{7}{3}; 3\right)$, ta có $v(t) < 0$ và $a(t) > 0$ nhưng tốc độ thay đổi; "
               r"cụ thể tại $t=1$, $v(1)=0$, sau đó tốc độ tăng lên $\dfrac{16}{3}$, nên khẳng định luôn giảm tốc độ từ $0$ đến $3$ giây là SAI.")
               
    items_data = [
        (stmt_a_t, stmt_a_f, exp_a_t, exp_a_f),
        (stmt_b_t, stmt_b_f, exp_b_t, exp_b_f),
        (stmt_c_t, stmt_c_f, exp_c_t, exp_c_f),
        (stmt_d_t, stmt_d_f, exp_d_t, exp_d_f),
    ]
    choices, loi_giai = make_tf_choices(items_data)
    return caudan, choices, loi_giai


def HamSo_TF_DoThiBacBa_PhuongTrinhLogarit_HeSo():
    """
    Ảnh 3 - Câu 4: Đồ thị hàm bậc ba y = ax^3 + bx^2 + cx + d.
    4 mệnh đề đúng sai:
    a) Phương trình log_3[f(x)+7] = 2 có 2 nghiệm.
    b) Giá trị cực tiểu của hàm số bằng -1.
    c) Hàm số đồng biến trên khoảng (0; 2).
    d) Giá trị của biểu thức 4a + 2b + c - 5d bằng 10.
    """
    # Hàm mẫu chuẩn: Cực tiểu tại (0; -1), Cực đại tại (2; 3)
    # y = -x^3 + 3x^2 - 1 => a = -1, b = 3, c = 0, d = -1
    # Kiểm tra: y' = -3x^2 + 6x = 0 => x=0, x=2.
    # y(0) = -1 (CT), y(2) = -8 + 12 - 1 = 3 (CD).
    # 4a + 2b + c - 5d = 4(-1) + 2(3) + 0 - 5(-1) = -4 + 6 + 5 = 7 (hoặc tùy hệ số).
    # Trong đề bài: 4a + 2b + c - 5d
    val_expr = 4 * (-1) + 2 * 3 + 0 - 5 * (-1) # = 7
    
    # TikZ code vẽ đồ thị
    tikz_code = r"""\begin{tikzpicture}[scale=0.7, baseline=(current bounding box.north)]
    \draw[->] (-1.5,0) -- (3.5,0) node[below] {$x$};
    \draw[->] (0,-2) -- (0,4.2) node[right] {$y$};
    \node[below left] at (0,0) {$O$};
    \draw[dashed] (2,0) node[below] {$2$} -- (2,3) -- (0,3) node[left] {$3$};
    \node[below left] at (0,-1) {$-1$};
    \draw[thick, smooth, samples=100, domain=-0.8:2.8] plot (\x, {-(\x)^3 + 3*(\x)^2 - 1});
\end{tikzpicture}"""

    caudan = (rf"\immini{{Cho hàm số $f(x) = ax^3 + bx^2 + cx + d$ có đồ thị như hình bên."
              rf" Xét tính đúng sai của các khẳng định sau:}}{{{tikz_code}}}")

    # Mệnh đề a: log_3[f(x)+7] = 2 <=> f(x)+7 = 9 <=> f(x) = 2.
    # Đường thẳng y = 2 cắt đồ thị tại 3 điểm (vì -1 < 2 < 3) => Có 3 nghiệm.
    stmt_a_t = r"Phương trình $\log_3[f(x) + 7] = 2$ có ba nghiệm phân biệt."
    stmt_a_f = r"Phương trình $\log_3[f(x) + 7] = 2$ có hai nghiệm."
    exp_a_t = (r"Ta có $\log_3[f(x) + 7] = 2 \Leftrightarrow f(x) + 7 = 3^2 = 9 \Leftrightarrow f(x) = 2$. "
               r"Vì giá trị cực tiểu $y_{\text{CT}} = -1 < 2 < y_{\text{CĐ}} = 3$ nên đường thẳng $y=2$ cắt đồ thị tại $3$ điểm phân biệt, phương trình có $3$ nghiệm.")
    exp_a_f = (r"Phương trình $\log_3[f(x) + 7] = 2 \Leftrightarrow f(x) = 2$. "
               r"Đường thẳng $y = 2$ nằm giữa cực tiểu $-1$ và cực đại $3$ nên cắt đồ thị tại $3$ điểm phân biệt, phương trình có $3$ nghiệm, không phải $2$ nghiệm.")

    stmt_b_t = r"Giá trị cực tiểu của hàm số $y = f(x)$ bằng $-1$."
    stmt_b_f = r"Giá trị cực tiểu của hàm số $y = f(x)$ bằng $0$."
    exp_b_t = r"Từ đồ thị ta thấy điểm cực tiểu của đồ thị là $(0; -1)$, do đó giá trị cực tiểu của hàm số là $y_{\text{CT}} = -1$."
    exp_b_f = r"Giá trị cực tiểu của hàm số là tung độ của điểm cực tiểu: $y_{\text{CT}} = -1 \ne 0$."

    stmt_c_t = r"Hàm số $y = f(x)$ đồng biến trên khoảng $(0; 2)$."
    stmt_c_f = r"Hàm số $y = f(x)$ đồng biến trên khoảng $(-1; 3)$."
    exp_c_t = r"Đồ thị hàm số đi lên từ trái sang phải trên khoảng $(0; 2)$, do đó hàm số đồng biến trên khoảng $(0; 2)$."
    exp_c_f = r"Trên khoảng $(-1; 3)$, đồ thị có cả khoảng đi xuống và đi lên nên hàm số không thể đồng biến trên cả khoảng $(-1; 3)$."

    stmt_d_t = rf"Giá trị của biểu thức $4a + 2b + c - 5d$ bằng ${val_expr}$."
    stmt_d_f = r"Giá trị của biểu thức $4a + 2b + c - 5d$ bằng $10$."
    exp_d_t = (rf"Đồ thị hàm số đi qua điểm $(0; -1) \Rightarrow d = -1$. "
               rf"Hàm số đạt cực trị tại $x = 0$ và $x = 2$ nên $f'(x) = 3ax^2 + 2bx + c$ có hai nghiệm $0$ và $2 \Rightarrow c = 0$ và $6a + 2b = 0 \Rightarrow b = -3a$. "
               rf"Đồ thị đi qua điểm cực đại $(2; 3) \Rightarrow 8a + 4b + d = 3 \Rightarrow 8a + 4(-3a) - 1 = 3 \Rightarrow -4a = 4 \Rightarrow a = -1 \Rightarrow b = 3$. "
               rf"Vậy $4a + 2b + c - 5d = 4(-1) + 2(3) + 0 - 5(-1) = {val_expr}$.")
    exp_d_f = (rf"Xác định được các hệ số $a = -1, b = 3, c = 0, d = -1$. "
               rf"Suy ra $4a + 2b + c - 5d = {val_expr} \ne 10$.")

    items_data = [
        (stmt_a_t, stmt_a_f, exp_a_t, exp_a_f),
        (stmt_b_t, stmt_b_f, exp_b_t, exp_b_f),
        (stmt_c_t, stmt_c_f, exp_c_t, exp_c_f),
        (stmt_d_t, stmt_d_f, exp_d_t, exp_d_f),
    ]
    choices, loi_giai = make_tf_choices(items_data)
    return caudan, choices, loi_giai


def HamSo_TF_ChuyenDongHatThangDung():
    """
    Câu 5: Giả sử một hạt chuyển động trên một trục thẳng đứng chiều dương hướng lên trên
    sao cho toạ độ của hạt (đơn vị: mét) tại thời điểm t (giây) là y = t^3 - 3*k^2*t + c, t >= 0.
    """
    k = random.randint(2, 4)
    b_coef = 3 * (k ** 2)
    c = random.randint(1, 9)
    t1 = k + 1
    
    # y(t) = t^3 - b_coef*t + c
    # v(t) = y'(t) = 3t^2 - b_coef = 3(t^2 - k^2)
    # a(t) = v'(t) = 6t
    a_at_k = 6 * k
    
    # Quãng đường từ 0 đến t1
    y0 = c
    yk = k**3 - b_coef * k + c
    yt1 = t1**3 - b_coef * t1 + c
    s1 = abs(yk - y0)
    s2 = abs(yt1 - yk)
    s_total = s1 + s2
    d_disp = abs(yt1 - y0)
    
    caudan = (f"Giả sử một hạt chuyển động trên một trục thẳng đứng chiều dương hướng lên trên "
              f"sao cho toạ độ của hạt (đơn vị: mét) tại thời điểm $t$ (giây) là $y = t^3 - {b_coef}t + {c}, t \\ge 0$.\n"
              f"Xét tính đúng, sai của các phát biểu sau:")
              
    stmt_a_t = rf"Gia tốc của hạt tại thời điểm $t = {k}$ là ${a_at_k}\text{{ m/s}}^2$."
    stmt_a_f = rf"Gia tốc của hạt tại thời điểm $t = {k}$ là ${3*k}\text{{ m/s}}^2$."
    exp_a_t = (rf"Ta có vận tốc $v(t) = y'(t) = 3t^2 - {b_coef}$, gia tốc $a(t) = v'(t) = y''(t) = 6t$. "
               rf"Tại thời điểm $t = {k}$, gia tốc của hạt là $a({k}) = 6 \times {k} = {a_at_k}\text{{ m/s}}^2$.")
    exp_a_f = (rf"Ta có $v(t) = 3t^2 - {b_coef}$, do đó $a(t) = 6t$. "
               rf"Tại $t = {k}$ thì $a({k}) = {a_at_k}\text{{ m/s}}^2 \ne {3*k}\text{{ m/s}}^2$.")

    stmt_b_t = rf"Hạt chuyển động xuống dưới trong khoảng thời gian $0 \le t < {k}$."
    stmt_b_f = r"Hạt chuyển động xuống dưới khi $t \le 0$."
    exp_b_t = (rf"Hạt chuyển động xuống dưới (theo chiều âm của trục toạ độ) khi $v(t) < 0 \Leftrightarrow 3t^2 - {b_coef} < 0 \Leftrightarrow 0 \le t < {k}$ (do $t \ge 0$).")
    exp_b_f = (rf"Thời gian chuyển động là $t \ge 0$. Hạt chuyển động xuống dưới khi vận tốc mang dấu âm: "
               rf"$v(t) < 0 \Leftrightarrow 3t^2 - {b_coef} < 0 \Leftrightarrow 0 \le t < {k}$. Mệnh đề $t \le 0$ là sai.")

    stmt_c_t = rf"Trong khoảng thời gian $0 \le t \le {t1}$, hạt đi được quãng đường ${s_total}\text{{ m}}$."
    stmt_c_f = rf"Trong khoảng thời gian $0 \le t \le {t1}$, hạt đi được quãng đường ${d_disp}\text{{ m}}$."
    exp_c_t = (rf"Tại $t = 0$: $y(0) = {y0}$. "
               rf"Tại $t = {k}$: $y({k}) = {yk}$, vận tốc triệt tiêu và hạt đổi chiều chuyển động. "
               rf"Quãng đường hạt đi từ $t = 0$ đến $t = {k}$ là $s_1 = |y({k}) - y(0)| = |{yk} - {y0}| = {s1}\text{{ m}}$. "
               rf"Tại $t = {t1}$: $y({t1}) = {yt1}$. "
               rf"Quãng đường hạt đi từ $t = {k}$ đến $t = {t1}$ là $s_2 = |y({t1}) - y({k})| = |{yt1} - ({yk})| = {s2}\text{{ m}}$. "
               rf"Tổng quãng đường đi được trong khoảng thời gian $0 \le t \le {t1}$ là $s = s_1 + s_2 = {s1} + {s2} = {s_total}\text{{ m}}$.")
    exp_c_f = (rf"Giá trị ${d_disp}\text{{ m}}$ chỉ là độ dịch chuyển $|y({t1}) - y(0)| = |{yt1} - {y0}| = {d_disp}\text{{ m}}$. "
               rf"Vì hạt đổi chiều chuyển động tại $t = {k}$ nên quãng đường thực tế phải bằng tổng hai đoạn: "
               rf"$s = |y({k}) - y(0)| + |y({t1}) - y({k})| = {s1} + {s2} = {s_total}\text{{ m}}$.")

    stmt_d_t = rf"Hạt chuyển động giảm tốc khi $0 < t < {k}$ và tăng tốc khi $t > {k}$."
    stmt_d_f = r"Hạt tăng tốc khi $t \ge 0$, hạt giảm tốc khi $t \le 0$."
    exp_d_t = (rf"Hạt tăng tốc khi tích $v(t) \cdot a(t) > 0$ và giảm tốc khi $v(t) \cdot a(t) < 0$. "
               rf"Vì $a(t) = 6t > 0$ với mọi $t > 0$ nên dấu của tích $v(t) \cdot a(t)$ phụ thuộc vào dấu của $v(t)$. "
               rf"Khi $0 < t < {k}$: $v(t) < 0 \Rightarrow v(t) \cdot a(t) < 0 \Rightarrow$ hạt giảm tốc. "
               rf"Khi $t > {k}$: $v(t) > 0 \Rightarrow v(t) \cdot a(t) > 0 \Rightarrow$ hạt tăng tốc.")
    exp_d_f = (rf"Thời gian chuyển động $t \ge 0$. "
               rf"Hạt giảm tốc khi $0 < t < {k}$ (do $v(t) < 0$ và $a(t) > 0$) "
               rf"và tăng tốc khi $t > {k}$ (do $v(t) > 0$ và $a(t) > 0$). Do đó phát biểu trên là sai.")

    items_data = [
        (stmt_a_t, stmt_a_f, exp_a_t, exp_a_f),
        (stmt_b_t, stmt_b_f, exp_b_t, exp_b_f),
        (stmt_c_t, stmt_c_f, exp_c_t, exp_c_f),
        (stmt_d_t, stmt_d_f, exp_d_t, exp_d_f),
    ]
    choices, loi_giai = make_tf_choices(items_data)
    return caudan, choices, loi_giai


def HamSo_TF_LuuLuongNuocSong():
    """
    Câu 7: Trong 25 phút theo dõi, lưu lượng nước của một con sông được tính theo công thức
    Q(t) = -t^3/10 + b*t^2 + c.
    """
    b = random.randint(4, 6)
    c = random.randint(30, 60)
    t0 = 10
    t2 = 15
    
    q0 = c
    q_t0 = - (t0**3)/10 + b*(t0**2) + c
    q_alert = int(q_t0 + 50)
    
    q_t2 = - (t2**3)/10 + b*(t2**2) + c
    v_avg = round((q_t2 - q_t0) / (t2 - t0), 1)
    v_avg_str = f"{v_avg}".replace('.', ',')
    v_avg_sai = round(v_avg + random.choice([-10, 10, 15]), 1)
    v_avg_sai_str = f"{v_avg_sai}".replace('.', ',')
    
    q_prime_10 = int(-0.3 * 100 + 2 * b * 10)
    v_test = int(round(q_prime_10 * 0.7))
    
    caudan = (f"Trong 25 phút theo dõi, lưu lượng nước của một con sông được tính theo công thức\n"
              f"\\[ Q(t) = -\\frac{{t^3}}{{10}} + {b}t^2 + {c}. \\]\n"
              f"Trong đó $Q$ tính theo $\\text{{m}}^3/\\text{{phút}}$, $t$ tính theo phút, $0 \\le t \\le 25$. "
              f"Khi lưu lượng nước của con sông lên đến ${q_alert}\\text{{ m}}^3/\\text{{phút}}$ thì cảnh báo lũ được đưa ra.\n"
              f"Xét tính đúng, sai của các phát biểu sau:")

    stmt_a_t = rf"Lưu lượng nước sông lúc bắt đầu theo dõi là ${q0}\text{{ m}}^3/\text{{phút}}$."
    stmt_a_f = rf"Lưu lượng nước sông lúc bắt đầu theo dõi là ${q0 + 15}\text{{ m}}^3/\text{{phút}}$."
    exp_a_t = rf"Lúc bắt đầu theo dõi ứng với $t = 0$. Khi đó $Q(0) = -\frac{{0^3}}{{10}} + {b}(0^2) + {c} = {q0}\text{{ m}}^3/\text{{phút}}$."
    exp_a_f = rf"Lúc bắt đầu theo dõi ứng với $t = 0$. Ta có $Q(0) = {q0}\text{{ m}}^3/\text{{phút}} \ne {q0 + 15}\text{{ m}}^3/\text{{phút}}$."

    stmt_b_t = rf"Cảnh báo lũ chưa được đưa ra trước thời điểm $t = {t0}$ phút."
    stmt_b_f = rf"Cảnh báo lũ được đưa ra trước thời điểm $t = {t0}$ phút."
    exp_b_t = (rf"Ta có $Q'(t) = -\frac{{3}}{{10}}t^2 + {2*b}t = t({2*b} - 0,3t) > 0$ với mọi $t \in (0; {t0}]$. "
               rf"Do đó $Q(t)$ đồng biến trên $[0; {t0}]$. "
               rf"Tại $t = {t0}$: $Q({t0}) = -\frac{{{t0}^3}}{{10}} + {b}({t0}^2) + {c} = {int(q_t0)}\text{{ m}}^3/\text{{phút}} < {q_alert}\text{{ m}}^3/\text{{phút}}$. "
               rf"Vì vậy trước thời điểm $t = {t0}$ phút, lưu lượng luôn nhỏ hơn ${q_alert}\text{{ m}}^3/\text{{phút}}$, cảnh báo lũ chưa được đưa ra.")
    exp_b_f = (rf"Tại $t = {t0}$: $Q({t0}) = {int(q_t0)}\text{{ m}}^3/\text{{phút}} < {q_alert}\text{{ m}}^3/\text{{phút}}$ và hàm số đồng biến trên $[0; {t0}]$. "
               rf"Do đó trước thời điểm $t = {t0}$ phút, cảnh báo lũ chưa được đưa ra.")

    stmt_c_t = rf"Trong khoảng thời gian ${t0}$ phút đầu tiên, có thời điểm mà tốc độ tăng của lưu lượng nước sông bằng ${v_test}\text{{ m}}^3/(\text{{phút}})^2$."
    stmt_c_f = rf"Trong khoảng thời gian ${t0}$ phút đầu tiên, không có thời điểm nào mà tốc độ tăng của lưu lượng nước sông bằng ${v_test}\text{{ m}}^3/(\text{{phút}})^2$."
    exp_c_t = (rf"Tốc độ tăng của lưu lượng nước sông tại thời điểm $t$ là đạo hàm $Q'(t) = -0,3t^2 + {2*b}t$. "
               rf"Xét trên đoạn $[0; {t0}]$, ta có $Q'(0) = 0$ và $Q'({t0}) = {q_prime_10}$. "
               rf"Vì hàm số $Q'(t)$ liên tục trên $[0; {t0}]$ và $0 < {v_test} < {q_prime_10}$ nên theo định lí giá trị trung gian, "
               rf"luôn tồn tại thời điểm $t \in (0; {t0})$ sao cho $Q'(t) = {v_test}\text{{ m}}^3/(\text{{phút}})^2$.")
    exp_c_f = (rf"Ta có $Q'(0) = 0$ và $Q'({t0}) = {q_prime_10}$. Do $0 < {v_test} < {q_prime_10}$ nên theo định lí giá trị trung gian, "
               rf"phải tồn tại thời điểm trong ${t0}$ phút đầu tiên có tốc độ tăng bằng ${v_test}\text{{ m}}^3/(\text{{phút}})^2$.")

    stmt_d_t = rf"Trong khoảng thời gian từ phút thứ ${t0}$ đến phút thứ ${t2}$, lưu lượng nước sông trung bình mỗi phút tăng ${v_avg_str}\text{{ m}}^3/\text{{phút}}$."
    stmt_d_f = rf"Trong khoảng thời gian từ phút thứ ${t0}$ đến phút thứ ${t2}$, lưu lượng nước sông trung bình mỗi phút tăng ${v_avg_sai_str}\text{{ m}}^3/\text{{phút}}$."
    exp_d_t = (rf"Tốc độ tăng trung bình mỗi phút trong khoảng thời gian từ $t = {t0}$ đến $t = {t2}$ là: "
               rf"$\frac{{\Delta Q}}{{\Delta t}} = \frac{{Q({t2}) - Q({t0})}}{{{t2} - {t0}}} "
               rf"= \frac{{{q_t2:.1f} - {q_t0:.1f}}}{{{t2 - t0}}} = \frac{{{q_t2 - q_t0:.1f}}}{{{t2 - t0}}} = {v_avg_str}\text{{ m}}^3/\text{{phút}}$.".replace('.', ','))
    exp_d_f = (rf"Tốc độ tăng trung bình được tính bởi $\frac{{Q({t2}) - Q({t0})}}{{{t2} - {t0}}} = {v_avg_str}\text{{ m}}^3/\text{{phút}} \ne {v_avg_sai_str}\text{{ m}}^3/\text{{phút}}$.")

    items_data = [
        (stmt_a_t, stmt_a_f, exp_a_t, exp_a_f),
        (stmt_b_t, stmt_b_f, exp_b_t, exp_b_f),
        (stmt_c_t, stmt_c_f, exp_c_t, exp_c_f),
        (stmt_d_t, stmt_d_f, exp_d_t, exp_d_f),
    ]
    choices, loi_giai = make_tf_choices(items_data)
    return caudan, choices, loi_giai


def HamSo_SA_TheTichNuocTheoNhietDo():
    """
    Câu 11: Thể tích V (cm^3) của 1 kg nước tại nhiệt độ T (0 <= T <= 30) được tính theo công thức
    V(T) = V0 - c1*T + c2*T^2 - c3*T^3.
    Thể tích nước V(T) giảm trong khoảng nhiệt độ (a; b) với b làm tròn đến hàng đơn vị. Tính tổng a + b.
    """
    b_target = random.randint(3, 6)
    delta_t = random.choice([-0.08, -0.04, -0.02, 0.02, 0.04, 0.08])
    t1 = round(b_target + delta_t, 2)
    t2 = random.randint(68, 82)
    
    c3 = 0.0000679
    c1 = round(3 * c3 * t1 * t2, 5)
    c2 = round(3 * c3 * (t1 + t2) / 2, 7)
    v0 = round(random.uniform(999.80, 999.95), 2)
    
    v0_str = f"{v0:.2f}".replace('.', ',')
    c1_str = f"{c1:.5f}".rstrip('0').replace('.', ',')
    c2_str = f"{c2:.7f}".rstrip('0').replace('.', ',')
    c3_str = "0,0000679"
    t1_str = f"{t1:.2f}".replace('.', ',')
    t2_str = f"{t2}"
    
    caudan = (f"Thể tích $V\\text{{ (cm}}^3\\text{{)}}$ của $1\\text{{ kg}}$ nước tại nhiệt độ $T\\ (0 \\le T \\le 30)$ "
              f"đơn vị $^\\circ\\text{{C}}$ được tính theo công thức\n"
              f"\\[ V(T) = {v0_str} - {c1_str}T + {c2_str}T^2 - {c3_str}T^3. \\]\n"
              f"Thể tích nước $V(T)$ giảm trong khoảng nhiệt độ $(a; b)$ với $b$ làm tròn đến hàng đơn vị. Tính tổng $a + b$.")
              
    loi_giai = (f"Đạo hàm của thể tích theo nhiệt độ là:\n"
                f"\\[ V'(T) = -{c1_str} + 2 \\times {c2_str}T - 3 \\times {c3_str}T^2. \\]\n"
                f"Giải phương trình $V'(T) = 0$, ta được hai nghiệm dương:\n"
                f"\\[ T_1 \\approx {t1_str}, \\quad T_2 \\approx {t2_str}. \\]\n"
                f"Vì hệ số của $T^2$ mang dấu âm ($-3 \\times {c3_str} < 0$) nên trên đoạn $[0; 30]$ (chú ý $30 < T_2$):\n"
                f"- $V'(T) < 0$ khi $0 \\le T < {t1_str}$;\n"
                f"- $V'(T) > 0$ khi ${t1_str} < T \\le 30$.\n"
                f"Do đó, thể tích nước $V(T)$ giảm trong khoảng nhiệt độ $(0; {t1_str})$.\n"
                f"Suy ra $a = 0$ và $b \\approx {t1_str}$. Làm tròn $b$ đến hàng đơn vị ta được $b = {b_target}$.\n"
                f"Vậy tổng $a + b = 0 + {b_target} = {b_target}$.")
                
    dapan = str(b_target)
    return caudan, loi_giai, dapan











