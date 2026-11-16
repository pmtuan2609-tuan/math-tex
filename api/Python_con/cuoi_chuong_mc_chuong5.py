# -*- coding: utf-8 -*-
"""
Module sinh đề trắc nghiệm chuẩn ma trận Bài tập Cuối Chương 5 (Toán 12)
Chương V: PHƯƠNG PHÁP TOẠ ĐỘ TRONG KHÔNG GIAN
Gồm 3 bài chuẩn ma trận:
- Bài 1: Phương trình mặt phẳng (Đa dạng hóa toàn diện theo ngân hàng đề thi 2025)
- Bài 2: Phương trình đường thẳng trong không gian
- Bài 3: Phương trình mặt cầu
Tất cả đều sinh ngẫu nhiên số liệu, tự động tính toán đáp án và lời giải chi tiết theo chuẩn ex_test.
"""

import random
import math
from fractions import Fraction

def clean_option(opt):
    if not isinstance(opt, str):
        opt = str(opt)
    opt = opt.strip()
    for pfx in ['A.', 'B.', 'C.', 'D.', 'a.', 'b.', 'c.', 'd.', 'a)', 'b)', 'c)', 'd)']:
        if opt.startswith(pfx):
            opt = opt[len(pfx):].strip()
    while opt.endswith('.'):
        opt = opt[:-1].strip()
    return opt

def shuffle_choices(correct, wrongs):
    c_clean = clean_option(correct)
    distinct_wrongs = []
    seen = {c_clean}
    for w in wrongs:
        wc = clean_option(w)
        if wc not in seen:
            distinct_wrongs.append(wc)
            seen.add(wc)
    idx = 1
    while len(distinct_wrongs) < 3:
        cand = f"{c_clean} + {idx}"
        if cand not in seen:
            distinct_wrongs.append(cand)
            seen.add(cand)
        idx += 1
    
    distinct_wrongs = distinct_wrongs[:3]
    choices = [f"{{\\True {c_clean}}}"] + [f"{{{w}}}" for w in distinct_wrongs]
    random.shuffle(choices)
    return choices

def gcd3(a, b, c):
    return math.gcd(math.gcd(abs(a), abs(b)), abs(c))

def fmt_eq(A, B, C, D):
    terms = []
    if A != 0:
        if A == 1: terms.append("x")
        elif A == -1: terms.append("-x")
        else: terms.append(f"{A}x")
    if B != 0:
        if not terms:
            if B == 1: terms.append("y")
            elif B == -1: terms.append("-y")
            else: terms.append(f"{B}y")
        else:
            if B == 1: terms.append("+ y")
            elif B == -1: terms.append("- y")
            elif B > 0: terms.append(f"+ {B}y")
            else: terms.append(f"- {abs(B)}y")
    if C != 0:
        if not terms:
            if C == 1: terms.append("z")
            elif C == -1: terms.append("-z")
            else: terms.append(f"{C}z")
        else:
            if C == 1: terms.append("+ z")
            elif C == -1: terms.append("- z")
            elif C > 0: terms.append(f"+ {C}z")
            else: terms.append(f"- {abs(C)}z")
    if D != 0:
        if not terms:
            terms.append(f"{D}")
        else:
            if D > 0: terms.append(f"+ {D}")
            else: terms.append(f"- {abs(D)}")
    if not terms:
        return "0 = 0"
    return " ".join(terms) + " = 0"

def make_tf_choices(items_data):
    flags = [random.choice([True, False]) for _ in range(4)]
    if all(flags):
        flags[random.randint(0, 3)] = False
    elif not any(flags):
        flags[random.randint(0, 3)] = True

    labels = ['a', 'b', 'c', 'd']
    choices = []
    expl_lines = []

    for i in range(4):
        t_text, f_text, t_expl, f_expl = items_data[i]
        lbl = labels[i]
        t_clean = clean_option(t_text)
        f_clean = clean_option(f_text)
        if flags[i]:
            choices.append(f"{{\\True {t_clean}}}\n")
            expl_lines.append(f"\\itemch {t_expl.strip()} (Ý {lbl}) \\textbf{{Đúng}}")
        else:
            choices.append(f"{{{f_clean}}}\n")
            expl_lines.append(f"\\itemch {f_expl.strip()} (Ý {lbl}) \\textbf{{Sai}}")

    loi_giai = "\\begin{itemchoice}\n" + "\n".join(expl_lines) + "\n\\end{itemchoice}"
    return choices, loi_giai

# ==============================================================================
# BÀI 1: PHƯƠNG TRÌNH MẶT PHẲNG - NHẬN BIẾT 1
# ==============================================================================
def CuoiChuong5_MC_B1_NB1():
    sub = random.choice([1, 2, 3, 4, 5, 6, 7])
    
    if sub == 1:
        a1, a2, a3 = [random.randint(-4, 4) for _ in range(3)]
        b1, b2, b3 = [random.randint(-4, 4) for _ in range(3)]
        c1 = a2 * b3 - a3 * b2
        c2 = a3 * b1 - a1 * b3
        c3 = a1 * b2 - a2 * b1
        caudan = fr'''Trong không gian $Oxyz$, cho $\vec{{a}} = ({a1}; {a2}; {a3})$ và $\vec{{b}} = ({b1}; {b2}; {b3})$. Tọa độ của tích có hướng $[\vec{{a}}, \vec{{b}}]$ là'''
        correct = fr'''$({c1}; {c2}; {c3})$'''
        wrongs = [
            fr'''$({-c1}; {c2}; {c3})$''',
            fr'''$({c1}; {-c2}; {c3})$''',
            fr'''$({c2}; {c1}; {c3})$'''
        ]
        loi_giai = fr'''Áp dụng công thức tính tích có hướng của hai vectơ:
\[
[\vec{{a}}, \vec{{b}}] = \left( \begin{{vmatrix}} {a2} & {a3} \\ {b2} & {b3} \end{{vmatrix}}; \begin{{vmatrix}} {a3} & {a1} \\ {b3} & {b1} \end{{vmatrix}}; \begin{{vmatrix}} {a1} & {a2} \\ {b1} & {b2} \end{{vmatrix}} \right) = ({c1}; {c2}; {c3}).
\]'''
        return caudan, shuffle_choices(correct, wrongs), loi_giai

    elif sub == 2:
        A = random.choice([2, 3, 4, 5])
        B = random.choice([-3, -2, -1, 1, 2, 3])
        C = random.choice([-3, -2, -1, 1, 2, 3])
        D = random.choice([-7, -5, 2, 4, 6])
        eq = fmt_eq(A, B, C, D)
        caudan = fr'''Trong không gian với hệ tọa độ $Oxyz$, cho mặt phẳng $(P)\colon {eq}$. Vectơ nào dưới đây là một vectơ pháp tuyến của $(P)$?'''
        correct = fr'''$\vec{{n}} = ({A}; {B}; {C})$'''
        wrongs = [
            fr'''$\vec{{n}} = ({A}; {-B}; {C})$''',
            fr'''$\vec{{n}} = ({B}; {A}; {C})$''',
            fr'''$\vec{{n}} = ({A}; {C}; {D})$'''
        ]
        loi_giai = fr'''Mặt phẳng $(P)\colon Ax + By + Cz + D = 0$ có một vectơ pháp tuyến là $\vec{{n}} = (A; B; C)$.\\
Do đó, một VTPT của $(P)$ là $\vec{{n}} = ({A}; {B}; {C})$.'''
        return caudan, shuffle_choices(correct, wrongs), loi_giai

    elif sub == 3:
        A = random.choice([1, 2, 3])
        B = random.choice([-2, -1, 1, 2])
        C = random.choice([-2, 1, 2])
        x0, y0, z0 = random.randint(-3, 3), random.randint(-3, 3), random.randint(-3, 3)
        D = - (A * x0 + B * y0 + C * z0)
        eq = fmt_eq(A, B, C, D)
        caudan = fr'''Trong không gian với hệ tọa độ $Oxyz$, cho mặt phẳng $(P)\colon {eq}$. Điểm nào dưới đây thuộc $(P)$?'''
        correct = fr'''$M({x0}; {y0}; {z0})$'''
        wrongs = [
            fr'''$P({x0 + 1}; {y0}; {z0})$''',
            fr'''$Q({x0}; {y0 - 1}; {z0})$''',
            fr'''$N({x0}; {y0}; {z0 + 2})$'''
        ]
        loi_giai = fr'''Thay tọa độ điểm $M({x0}; {y0}; {z0})$ vào phương trình mặt phẳng $(P)$, ta có:
\[
{A} \cdot ({x0}) {B:+d} \cdot ({y0}) {C:+d} \cdot ({z0}) {D:+d} = 0 \quad (\text{{đúng}}).
\]
Vậy điểm $M({x0}; {y0}; {z0}) \in (P)$.'''
        return caudan, shuffle_choices(correct, wrongs), loi_giai

    elif sub == 4:
        A, B, C = random.choice([(1, 3, -5), (2, -1, 3), (1, -2, 2), (2, 4, -6)])
        D = random.randint(-9, 9)
        eq = fmt_eq(A, B, C, D)
        caudan = fr'''Trong không gian $Oxyz$, vectơ nào sau đây \textbf{{không}} phải là vectơ pháp tuyến của mặt phẳng $(P)\colon {eq}$?'''
        k1, k2 = -1, 2
        vtpt1 = f"({k1*A}; {k1*B}; {k1*C})"
        vtpt2 = f"({k2*A}; {k2*B}; {k2*C})"
        vtpt3 = f"({A}; {B}; {C})"
        correct = fr'''$\vec{{n}} = ({k2*A}; {k2*B}; {-k2*C})$'''
        wrongs = [
            fr'''$\vec{{n}}_1 = {vtpt1}$''',
            fr'''$\vec{{n}}_2 = {vtpt2}$''',
            fr'''$\vec{{n}}_3 = {vtpt3}$'''
        ]
        loi_giai = fr'''Mặt phẳng $(P)$ có một VTPT là $\vec{{n}} = ({A}; {B}; {C})$. Mọi vectơ cùng phương với $\vec{{n}}$ (dạng $k\vec{{n}}, k \ne 0$) đều là VTPT của $(P)$.\\
Vectơ $({k2*A}; {k2*B}; {-k2*C})$ không cùng phương với $\vec{{n}}$ nên không phải là VTPT của $(P)$.'''
        return caudan, shuffle_choices(correct, wrongs), loi_giai

    elif sub == 5:
        plane = random.choice(["(Oxy)", "(Oyz)", "(Oxz)"])
        if plane == "(Oxy)":
            eq = "z = 0"
            vtpt = "(0; 0; 1)"
        elif plane == "(Oyz)":
            eq = "x = 0"
            vtpt = "(1; 0; 0)"
        else:
            eq = "y = 0"
            vtpt = "(0; 1; 0)"
        
        caudan = fr'''Trong không gian $Oxyz$, mặt phẳng tọa độ ${plane}$ có một vectơ pháp tuyến là'''
        correct = fr'''$\vec{{n}} = {vtpt}$'''
        wrongs = [
            fr'''$\vec{{n}} = (1; 1; 0)$''',
            fr'''$\vec{{n}} = (1; 1; 1)$''',
            fr'''$\vec{{n}} = (0; 1; 1)$'''
        ]
        loi_giai = fr'''Mặt phẳng tọa độ ${plane}$ có phương trình là ${eq}$, do đó nhận vectơ $\vec{{n}} = {vtpt}$ làm một vectơ pháp tuyến.'''
        return caudan, shuffle_choices(correct, wrongs), loi_giai

    elif sub == 6:
        caudan = fr'''Trong không gian với hệ tọa độ $Oxyz$, phương trình nào sau đây là phương trình tổng quát của một mặt phẳng?'''
        correct = r'''$2x + y + z + 3 = 0$'''
        wrongs = [
            r'''$x^2 + y + z + 2 = 0$''',
            r'''$2x + y^2 + z + 1 = 0$''',
            r'''$2x + y + z^2 + 4 = 0$'''
        ]
        loi_giai = r'''Phương trình tổng quát của mặt phẳng trong không gian $Oxyz$ luôn có dạng bậc nhất $Ax + By + Cz + D = 0$ với $A^2 + B^2 + C^2 > 0$. Do đó phương trình $2x + y + z + 3 = 0$ là phương trình tổng quát của mặt phẳng.'''
        return caudan, shuffle_choices(correct, wrongs), loi_giai

    else:
        caudan = r'''Trong không gian với hệ tọa độ $Oxyz$, cho hình hộp chữ nhật $ABCD.A'B'C'D'$. Vectơ nào dưới đây là một vectơ pháp tuyến của mặt phẳng $(ABCD)$?'''
        correct = r'''$\vec{AA'}$'''
        wrongs = [
            r'''$\vec{AB}$''',
            r'''$\vec{AC}$''',
            r'''$\vec{AD}$'''
        ]
        loi_giai = r'''Vì $ABCD.A'B'C'D'$ là hình hộp chữ nhật nên cạnh bên $AA' \perp (ABCD)$.\\
Do đó, vectơ $\vec{AA'}$ là một vectơ pháp tuyến của mặt phẳng $(ABCD)$.'''
        return caudan, shuffle_choices(correct, wrongs), loi_giai


# ==============================================================================
# BÀI 1: PHƯƠNG TRÌNH MẶT PHẲNG - NHẬN BIẾT 2
# ==============================================================================
def CuoiChuong5_MC_B1_NB2():
    sub = random.choice([1, 2, 3, 4, 5])
    
    if sub == 1:
        x0, y0, z0 = random.randint(-3, 3), random.randint(-3, 3), random.randint(-3, 3)
        A, B, C = random.choice([1, 2, -1, -2]), random.choice([2, 3, -1, -3]), random.choice([1, -2, 3])
        D = - (A * x0 + B * y0 + C * z0)
        eq = fmt_eq(A, B, C, D)
        caudan = fr'''Trong không gian $Oxyz$, phương trình mặt phẳng đi qua điểm $A({x0}; {y0}; {z0})$ và có một vectơ pháp tuyến $\vec{{n}} = ({A}; {B}; {C})$ là'''
        correct = fr'''${eq}$'''
        wrongs = [
            fr'''${fmt_eq(A, B, C, -D)}$''',
            fr'''${fmt_eq(A, -B, C, D)}$''',
            fr'''${fmt_eq(x0, y0, z0, D)}$'''
        ]
        loi_giai = fr'''Phương trình mặt phẳng đi qua $A({x0}; {y0}; {z0})$ và có VTPT $\vec{{n}} = ({A}; {B}; {C})$ là:
\[
{A}(x {-x0:+d}) {B:+d}(y {-y0:+d}) {C:+d}(z {-z0:+d}) = 0 \iff {eq}.
\]'''
        return caudan, shuffle_choices(correct, wrongs), loi_giai

    elif sub == 2:
        a, b, c = random.choice([(-2, -1, 3), (2, -3, 6), (3, -2, 1), (-1, 2, -3)])
        lcm = math.lcm(math.lcm(abs(a), abs(b)), abs(c))
        A = lcm // a
        B = lcm // b
        C = lcm // c
        g = gcd3(A, B, C)
        A, B, C = A // g, B // g, C // g
        if A < 0:
            A, B, C = -A, -B, -C
        
        caudan = fr'''Trong không gian với hệ tọa độ $Oxyz$, một vectơ pháp tuyến của mặt phẳng $(P)\colon \dfrac{{x}}{{{a}}} + \dfrac{{y}}{{{b}}} + \dfrac{{z}}{{{c}}} = 1$ là'''
        correct = fr'''$\vec{{n}} = ({A}; {B}; {C})$'''
        wrongs = [
            fr'''$\vec{{n}} = ({a}; {b}; {c})$''',
            fr'''$\vec{{n}} = ({-a}; {b}; {-c})$''',
            fr'''$\vec{{n}} = ({A}; {-B}; {C})$'''
        ]
        loi_giai = fr'''Quy đồng mẫu số phương trình mặt phẳng $(P)$:
\[
\frac{{x}}{{{a}}} + \frac{{y}}{{{b}}} + \frac{{z}}{{{c}}} = 1 \iff {fmt_eq(A, B, C, -lcm // g)}.
\]
Do đó một vectơ pháp tuyến của $(P)$ là $\vec{{n}} = ({A}; {B}; {C})$.'''
        return caudan, shuffle_choices(correct, wrongs), loi_giai

    elif sub == 3:
        a = random.choice([2, 3, 4, 6, 8])
        b = random.choice([-2, -3, -4, 2, 3])
        c = random.choice([2, 4, 6, -3])
        lcm = math.lcm(math.lcm(abs(a), abs(b)), abs(c))
        A, B, C = lcm // a, lcm // b, lcm // c
        g = gcd3(A, B, C)
        A, B, C = A // g, B // g, C // g
        D = - (lcm // g)
        eq = fmt_eq(A, B, C, D)
        
        caudan = fr'''Trong không gian với hệ tọa độ $Oxyz$, mặt phẳng $(\alpha)$ cắt ba trục tọa độ lần lượt tại ba điểm $M({a}; 0; 0), N(0; {b}; 0), P(0; 0; {c})$. Phương trình của mặt phẳng $(\alpha)$ là'''
        correct = fr'''${eq}$'''
        wrongs = [
            fr'''$\dfrac{{x}}{{{a}}} + \dfrac{{y}}{{{b}}} + \dfrac{{z}}{{{c}}} = 0$''',
            fr'''${fmt_eq(A, -B, C, D)}$''',
            fr'''${fmt_eq(A, B, C, -D)}$'''
        ]
        loi_giai = fr'''Áp dụng phương trình mặt phẳng theo đoạn chắn:
\[
(\alpha)\colon \frac{{x}}{{{a}}} + \frac{{y}}{{{b}}} + \frac{{z}}{{{c}}} = 1 \iff {eq}.
\]'''
        return caudan, shuffle_choices(correct, wrongs), loi_giai

    elif sub == 4:
        u1, u2, u3 = random.choice([(1, -2, 0), (2, 1, 0), (1, 0, -1), (0, 2, -1)])
        v1, v2, v3 = random.choice([(0, 2, -1), (1, 1, 2), (-2, 0, 1), (3, -1, 0)])
        n1 = u2 * v3 - u3 * v2
        n2 = u3 * v1 - u1 * v3
        n3 = u1 * v2 - u2 * v1
        g = gcd3(n1, n2, n3)
        if g > 0:
            n1, n2, n3 = n1 // g, n2 // g, n3 // g
        caudan = fr'''Trong không gian $Oxyz$, vectơ nào sau đây là một vectơ pháp tuyến của $(P)$, biết $\vec{{u}} = ({u1}; {u2}; {u3}), \vec{{v}} = ({v1}; {v2}; {v3})$ là một cặp vectơ chỉ phương của $(P)$?'''
        correct = fr'''$\vec{{n}} = ({n1}; {n2}; {n3})$'''
        wrongs = [
            fr'''$\vec{{n}} = ({-n1}; {n2}; {-n3})$''',
            fr'''$\vec{{n}} = ({n2}; {n1}; {n3})$''',
            fr'''$\vec{{n}} = ({u1 + v1}; {u2 + v2}; {u3 + v3})$'''
        ]
        loi_giai = fr'''Một vectơ pháp tuyến của mặt phẳng $(P)$ cùng phương với tích có hướng $[\vec{{u}}, \vec{{v}}]$:
\[
[\vec{{u}}, \vec{{v}}] = \left(\begin{{vmatrix}} {u2}&{u3}\\{v2}&{v3}\end{{vmatrix}}; \begin{{vmatrix}} {u3}&{u1}\\{v3}&{v1}\end{{vmatrix}}; \begin{{vmatrix}} {u1}&{u2}\\{v1}&{v2}\end{{vmatrix}}\right) = ({n1*g}; {n2*g}; {n3*g}).
\]
Do đó một VTPT của $(P)$ là $\vec{{n}} = ({n1}; {n2}; {n3})$.'''
        return caudan, shuffle_choices(correct, wrongs), loi_giai

    else:
        xA, yA, zA = 2, -1, 3
        xB, yB, zB = 4, 0, 1
        xC, yC, zC = -10, 5, 3
        AB = (xB - xA, yB - yA, zB - zA)
        AC = (xC - xA, yC - yA, zC - zA)
        n1 = AB[1]*AC[2] - AB[2]*AC[1]
        n2 = AB[2]*AC[0] - AB[0]*AC[2]
        n3 = AB[0]*AC[1] - AB[1]*AC[0]
        g = gcd3(n1, n2, n3)
        n1, n2, n3 = n1 // g, n2 // g, n3 // g
        caudan = fr'''Trong không gian $Oxyz$, cho ba điểm $A({xA}; {yA}; {zA}), B({xB}; {yB}; {zB})$ và $C({xC}; {yC}; {zC})$. Vectơ nào dưới đây là vectơ pháp tuyến của mặt phẳng $(ABC)$?'''
        correct = fr'''$\vec{{n}} = ({n1}; {n2}; {n3})$'''
        wrongs = [
            fr'''$\vec{{n}} = ({n1}; {-n2}; {n3})$''',
            fr'''$\vec{{n}} = ({n2}; {n1}; {-n3})$''',
            fr'''$\vec{{n}} = (1; 8; 2)$'''
        ]
        loi_giai = fr'''Ta có $\vec{{AB}} = ({AB[0]}; {AB[1]}; {AB[2]})$ và $\vec{{AC}} = ({AC[0]}; {AC[1]}; {AC[2]})$.\\
Tích có hướng:
\[
[\vec{{AB}}, \vec{{AC}}] = ({n1*g}; {n2*g}; {n3*g}) = {g}({n1}; {n2}; {n3}).
\]
Vậy một VTPT của mặt phẳng $(ABC)$ là $\vec{{n}} = ({n1}; {n2}; {n3})$.'''
        return caudan, shuffle_choices(correct, wrongs), loi_giai


# ==============================================================================
# BÀI 1: PHƯƠNG TRÌNH MẶT PHẲNG - THÔNG HIỂU
# ==============================================================================
def CuoiChuong5_MC_B1_TH():
    sub = random.choice([1, 2, 3, 4, 5, 6, 7])
    
    if sub == 1:
        xA, yA, zA = 1, 1, 4
        xB, yB, zB = 2, 7, 9
        xC, yC, zC = 0, 9, 13
        AB = (xB - xA, yB - yA, zB - zA)
        AC = (xC - xA, yC - yA, zC - zA)
        n1 = AB[1]*AC[2] - AB[2]*AC[1]
        n2 = AB[2]*AC[0] - AB[0]*AC[2]
        n3 = AB[0]*AC[1] - AB[1]*AC[0]
        g = gcd3(n1, n2, n3)
        A, B, C = n1 // g, n2 // g, n3 // g
        D = - (A * xA + B * yA + C * zA)
        eq = fmt_eq(A, B, C, D)
        caudan = fr'''Trong không gian với hệ tọa độ $Oxyz$, viết phương trình mặt phẳng đi qua ba điểm $A({xA}; {yA}; {zA}), B({xB}; {yB}; {zB}), C({xC}; {yC}; {zC})$.'''
        correct = fr'''${eq}$'''
        wrongs = [
            fr'''${fmt_eq(2, 1, 1, 1)}$''',
            fr'''${fmt_eq(2, 1, -1, -2)}$''',
            fr'''${fmt_eq(7, -2, 1, -9)}$'''
        ]
        loi_giai = fr'''Ta có $\vec{{AB}} = ({AB[0]}; {AB[1]}; {AB[2]})$ và $\vec{{AC}} = ({AC[0]}; {AC[1]}; {AC[2]})$.\\
VTPT của $(ABC)$ là $\vec{{n}} = \dfrac{{1}}{{{g}}}[\vec{{AB}}, \vec{{AC}}] = ({A}; {B}; {C})$.\\
Phương trình mặt phẳng $(ABC)$ đi qua $A({xA}; {yA}; {zA})$:
\[
{A}(x {-xA:+d}) {B:+d}(y {-yA:+d}) {C:+d}(z {-zA:+d}) = 0 \iff {eq}.
\]'''
        return caudan, shuffle_choices(correct, wrongs), loi_giai

    elif sub == 2:
        xA, yA, zA = -1, 2, 0
        xB, yB, zB = 3, 0, 2
        xI, yI, zI = (xA + xB)//2, (yA + yB)//2, (zA + zB)//2
        AB = (xB - xA, yB - yA, zB - zA)
        g = gcd3(AB[0], AB[1], AB[2])
        A, B, C = AB[0]//g, AB[1]//g, AB[2]//g
        D = - (A * xI + B * yI + C * zI)
        eq = fmt_eq(A, B, C, D)
        caudan = fr'''Trong không gian với hệ tọa độ $Oxyz$, cho hai điểm $A({xA}; {yA}; {zA})$ và $B({xB}; {yB}; {zB})$. Mặt phẳng trung trực của đoạn thẳng $AB$ có phương trình là'''
        correct = fr'''${eq}$'''
        wrongs = [
            fr'''${fmt_eq(1, 1, 1, -3)}$''',
            fr'''${fmt_eq(2, -1, 1, 2)}$''',
            fr'''${fmt_eq(2, 1, 1, -4)}$'''
        ]
        loi_giai = fr'''Trung điểm của đoạn thẳng $AB$ là $I({xI}; {yI}; {zI})$.\\
Vectơ $\vec{{AB}} = ({AB[0]}; {AB[1]}; {AB[2]})$ cùng phương với $\vec{{n}} = ({A}; {B}; {C})$.\\
Phương trình mặt phẳng trung trực của $AB$ là:
\[
{A}(x {-xI:+d}) {B:+d}(y {-yI:+d}) {C:+d}(z {-zI:+d}) = 0 \iff {eq}.
\]'''
        return caudan, shuffle_choices(correct, wrongs), loi_giai

    elif sub == 3:
        xA, yA, zA = -1, 1, 1
        xB, yB, zB = 2, 1, 0
        xC, yC, zC = 1, -1, 2
        BC = (xC - xB, yC - yB, zC - zB)
        A, B, C = 1, 2, -2
        D = - (A * xA + B * yA + C * zA)
        eq = fmt_eq(A, B, C, D)
        caudan = fr'''Trong không gian với hệ tọa độ $Oxyz$, cho ba điểm $A({xA}; {yA}; {zA}), B({xB}; {yB}; {zB}), C({xC}; {yC}; {zC})$. Mặt phẳng đi qua $A$ và vuông góc với đường thẳng $BC$ có phương trình là'''
        correct = fr'''${eq}$'''
        wrongs = [
            fr'''${fmt_eq(3, 0, 2, 1)}$''',
            fr'''${fmt_eq(1, 2, -2, -1)}$''',
            fr'''${fmt_eq(3, 0, 2, -1)}$'''
        ]
        loi_giai = fr'''Đường thẳng $BC$ có VTCP $\vec{{BC}} = ({BC[0]}; {BC[1]}; {BC[2]})$, cùng phương với $\vec{{n}} = ({A}; {B}; {C})$.\\
Mặt phẳng đi qua $A({xA}; {yA}; {zA})$ vuông góc với $BC$ nhận $\vec{{n}}$ làm VTPT:
\[
{A}(x {-xA:+d}) {B:+d}(y {-yA:+d}) {C:+d}(z {-zA:+d}) = 0 \iff {eq}.
\]'''
        return caudan, shuffle_choices(correct, wrongs), loi_giai

    elif sub == 4:
        A, B, C = 3, -2, 1
        D = 1
        xM, yM, zM = 2, -1, 4
        D_prime = - (A * xM + B * yM + C * zM)
        eq = fmt_eq(A, B, C, D_prime)
        caudan = fr'''Trong không gian với hệ tọa độ $Oxyz$, cho điểm $M({xM}; {yM}; {zM})$ và mặt phẳng $(P)\colon {fmt_eq(A, B, C, D)}$. Phương trình của mặt phẳng đi qua $M$ và song song với mặt phẳng $(P)$ là'''
        correct = fr'''${eq}$'''
        wrongs = [
            fr'''${fmt_eq(A, B, C, -D_prime)}$''',
            fr'''${fmt_eq(2, -2, 4, -21)}$''',
            fr'''${fmt_eq(2, -2, 4, 21)}$'''
        ]
        loi_giai = fr'''Mặt phẳng song song với $(P)$ có dạng $(Q)\colon {A}x {B:+d}y {C:+d}z + D' = 0$ ($D' \ne {D}$).\\
Vì $M({xM}; {yM}; {zM}) \in (Q)$ nên:
\[
{A} \cdot ({xM}) {B:+d} \cdot ({yM}) {C:+d} \cdot ({zM}) + D' = 0 \iff D' = {D_prime}.
\]
Vậy phương trình mặt phẳng là ${eq}$.'''
        return caudan, shuffle_choices(correct, wrongs), loi_giai

    elif sub == 5:
        x0, y0, z0 = 1, 1, 0
        A, B, C = 2, 2, 1
        D = -1
        eq = fmt_eq(A, B, C, D)
        d_val = abs(A*x0 + B*y0 + C*z0 + D)
        denom = int(math.isqrt(A**2 + B**2 + C**2))
        res_frac = Fraction(d_val, denom)
        ans_str = f"{res_frac}" if res_frac.denominator == 1 else fr"\frac{{{res_frac.numerator}}}{{{res_frac.denominator}}}"
        caudan = fr'''Trong không gian với hệ tọa độ $Oxyz$, khoảng cách từ điểm $A({x0}; {y0}; {z0})$ đến mặt phẳng $(\alpha)\colon {eq}$ bằng'''
        correct = fr'''${ans_str}$'''
        wrongs = [
            fr'''$\frac{{4}}{{3}}$''',
            fr'''$\frac{{3\sqrt{{2}}}}{{2}}$''',
            fr'''$2\sqrt{{2}}$'''
        ]
        loi_giai = fr'''Áp dụng công thức tính khoảng cách từ điểm $A$ đến mặt phẳng $(\alpha)$:
\[
d(A, (\alpha)) = \frac{{|{A} \cdot ({x0}) {B:+d} \cdot ({y0}) {C:+d} \cdot ({z0}) {D:+d}|}}{{\sqrt{{{A}^2 + {B}^2 + {C}^2}}}} = \frac{{|{A*x0 + B*y0 + C*z0 + D}|}}{{{denom}}} = {ans_str}.
\]'''
        return caudan, shuffle_choices(correct, wrongs), loi_giai

    elif sub == 6:
        A1, B1, C1 = 2, 1, -3
        A2, C2 = 1, 1
        m_val = - (A1*A2 + C1*C2)
        caudan = fr'''Trong không gian $Oxyz$, cho hai mặt phẳng $(P)\colon 2x + y - 3z - 2024 = 0$ và $(Q)\colon x + my + z + 2025 = 0$ với $m$ là tham số. Mặt phẳng $(P)$ vuông góc với mặt phẳng $(Q)$ khi và chỉ khi'''
        correct = fr'''$m = {m_val}$'''
        wrongs = [
            fr'''$m = {-m_val}$''',
            fr'''$m = 5$''',
            fr'''$m = -5$'''
        ]
        loi_giai = fr'''Vectơ pháp tuyến của $(P)$ là $\vec{{n}}_1 = ({A1}; {B1}; {C1})$.\\
Vectơ pháp tuyến của $(Q)$ là $\vec{{n}}_2 = ({A2}; m; {C2})$.\\
Hai mặt phẳng vuông góc khi và chỉ khi tích vô hướng của hai VTPT bằng $0$:
\[
\vec{{n}}_1 \cdot \vec{{n}}_2 = 0 \iff {A1} \cdot {A2} + {B1} \cdot m {C1:+d} \cdot {C2} = 0 \iff m {A1*A2 + C1*C2:+d} = 0 \iff m = {m_val}.
\]'''
        return caudan, shuffle_choices(correct, wrongs), loi_giai

    else:
        A, B, C = 1, 2, 3
        D1, D2 = -1, 6
        denom_sq = A**2 + B**2 + C**2
        diff = abs(D1 - D2)
        caudan = fr'''Trong không gian $Oxyz$, khoảng cách giữa hai mặt phẳng song song $(P)\colon {fmt_eq(A, B, C, D1)}$ và $(Q)\colon {fmt_eq(A, B, C, D2)}$ là'''
        from sympy import S, sqrt as sp_sqrt, simplify as sp_simplify, latex as sp_latex
        ans_tex = sp_latex(sp_simplify(S(diff) / sp_sqrt(denom_sq))).replace(r"\frac", r"\dfrac")
        correct = fr'''${ans_tex}$'''
        w1_tex = sp_latex(sp_simplify(S(diff + 1) / sp_sqrt(denom_sq))).replace(r"\frac", r"\dfrac")
        w2_tex = sp_latex(sp_simplify(S(abs(diff - 2)) / sp_sqrt(denom_sq))).replace(r"\frac", r"\dfrac")
        wrongs = [
            fr'''${w1_tex}$''',
            fr'''${diff * 2}$''',
            fr'''${w2_tex}$'''
        ]
        loi_giai = fr'''Khoảng cách giữa hai mặt phẳng song song $(P)\colon Ax+By+Cz+D_1=0$ và $(Q)\colon Ax+By+Cz+D_2=0$ là:
\[
d((P), (Q)) = \frac{{|D_1 - D_2|}}{{\sqrt{{A^2 + B^2 + C^2}}}} = \frac{{|{D1} - ({D2})|}}{{\sqrt{{{A}^2 + {B}^2 + {C}^2}}}} = \frac{{{diff}}}{{\sqrt{{{denom_sq}}}}} = {ans_tex}.
\]'''
        return caudan, shuffle_choices(correct, wrongs), loi_giai


# ==============================================================================
# BÀI 1: PHƯƠNG TRÌNH MẶT PHẲNG - VẬN DỤNG
# ==============================================================================
def CuoiChuong5_MC_B1_VD():
    sub = random.choice([1, 2, 3, 4, 5])
    
    if sub == 1:
        xA, yA, zA = 2, -1, 0
        xB, yB, zB = 1, 1, 2
        AB = (xB - xA, yB - yA, zB - zA)
        nQ = (1, 1, 2)
        n1 = AB[1]*nQ[2] - AB[2]*nQ[1]
        n2 = AB[2]*nQ[0] - AB[0]*nQ[2]
        n3 = AB[0]*nQ[1] - AB[1]*nQ[0]
        g = gcd3(n1, n2, n3)
        A, B, C = n1 // g, n2 // g, n3 // g
        D = - (A * xA + B * yA + C * zA)
        eq = fmt_eq(A, B, C, D)
        caudan = fr'''Trong không gian $Oxyz$, phương trình mặt phẳng $(P)$ đi qua hai điểm $A({xA}; {yA}; {zA}), B({xB}; {yB}; {zB})$ và vuông góc với mặt phẳng $(Q)\colon {fmt_eq(nQ[0], nQ[1], nQ[2], -3)}$ là'''
        correct = fr'''${eq}$'''
        wrongs = [
            fr'''${fmt_eq(A, B, C, -8)}$''',
            fr'''${fmt_eq(A, B, C, 8)}$''',
            fr'''${fmt_eq(A, -B, C, 0)}$'''
        ]
        loi_giai = fr'''Ta có $\vec{{AB}} = ({AB[0]}; {AB[1]}; {AB[2]})$ và VTPT của $(Q)$ là $\vec{{n}}_Q = ({nQ[0]}; {nQ[1]}; {nQ[2]})$.\\
Vì $(P)$ chứa $AB$ và $(P) \perp (Q)$ nên VTPT của $(P)$ là:
\[
\vec{{n}}_P = [\vec{{AB}}, \vec{{n}}_Q] = ({A}; {B}; {C}).
\]
Phương trình mặt phẳng $(P)$ đi qua $A({xA}; {yA}; {zA})$:
\[
{A}(x {-xA:+d}) {B:+d}(y {-yA:+d}) {C:+d}(z {-zA:+d}) = 0 \iff {eq}.
\]'''
        return caudan, shuffle_choices(correct, wrongs), loi_giai

    elif sub == 2:
        xM, yM, zM = 2, 1, -2
        nQ = (1, 1, 2)
        nR = (1, -1, -1)
        n1 = nQ[1]*nR[2] - nQ[2]*nR[1]
        n2 = nQ[2]*nR[0] - nQ[0]*nR[2]
        n3 = nQ[0]*nR[1] - nQ[1]*nR[0]
        g = gcd3(n1, n2, n3)
        A, B, C = n1 // g, n2 // g, n3 // g
        D = - (A * xM + B * yM + C * zM)
        eq = fmt_eq(A, B, C, D)
        caudan = fr'''Trong không gian $Oxyz$, phương trình mặt phẳng $(P)$ đi qua điểm $M({xM}; {yM}; {zM})$ và vuông góc với hai mặt phẳng $(Q)\colon {fmt_eq(nQ[0], nQ[1], nQ[2], -3)}$ và $(R)\colon {fmt_eq(nR[0], nR[1], nR[2], 4)}$ là'''
        correct = fr'''${eq}$'''
        wrongs = [
            fr'''${fmt_eq(A, B, C, -D)}$''',
            fr'''${fmt_eq(2, 1, -2, -9)}$''',
            fr'''${fmt_eq(2, 1, -2, 9)}$'''
        ]
        loi_giai = fr'''VTPT của $(Q)$ và $(R)$ lần lượt là $\vec{{n}}_Q = ({nQ[0]}; {nQ[1]}; {nQ[2]})$ và $\vec{{n}}_R = ({nR[0]}; {nR[1]}; {nR[2]})$.\\
Vì $(P)$ vuông góc với cả hai mặt phẳng $(Q)$ và $(R)$ nên VTPT của $(P)$ là:
\[
\vec{{n}}_P = [\vec{{n}}_Q, \vec{{n}}_R] = ({A}; {B}; {C}).
\]
Phương trình mặt phẳng $(P)$ đi qua $M({xM}; {yM}; {zM})$:
\[
{A}(x {-xM:+d}) {B:+d}(y {-yM:+d}) {C:+d}(z {-zM:+d}) = 0 \iff {eq}.
\]'''
        return caudan, shuffle_choices(correct, wrongs), loi_giai

    elif sub == 3:
        xA, yA, zA = 5, 1, 3
        xB, yB, zB = 1, 6, 2
        xC, yC, zC = 5, 0, 4
        xD, yD, zD = 4, 0, 6
        AB = (xB - xA, yB - yA, zB - zA)
        CD = (xD - xC, yD - yC, zD - zC)
        n1 = AB[1]*CD[2] - AB[2]*CD[1]
        n2 = AB[2]*CD[0] - AB[0]*CD[2]
        n3 = AB[0]*CD[1] - AB[1]*CD[0]
        g = gcd3(n1, n2, n3)
        A, B, C = n1 // g, n2 // g, n3 // g
        D = - (A * xA + B * yA + C * zA)
        eq = fmt_eq(A, B, C, D)
        caudan = fr'''Trong không gian $Oxyz$, cho các điểm $A({xA}; {yA}; {zA}), B({xB}; {yB}; {zB}), C({xC}; {yC}; {zC}), D({xD}; {yD}; {zD})$. Viết phương trình mặt phẳng $(P)$ đi qua hai điểm $A, B$ và song song với đường thẳng $CD$.'''
        correct = fr'''${eq}$'''
        wrongs = [
            fr'''${fmt_eq(A, B, C, -D)}$''',
            fr'''${fmt_eq(4, -5, 1, 24)}$''',
            fr'''$x - 2z + 1 = 0$'''
        ]
        loi_giai = fr'''Ta có $\vec{{AB}} = ({AB[0]}; {AB[1]}; {AB[2]})$ và $\vec{{CD}} = ({CD[0]}; {CD[1]}; {CD[2]})$.\\
VTPT của mặt phẳng $(P)$ là:
\[
\vec{{n}}_P = [\vec{{AB}}, \vec{{CD}}] = ({A}; {B}; {C}).
\]
Phương trình $(P)$ đi qua $A({xA}; {yA}; {zA})$:
\[
{A}(x {-xA:+d}) {B:+d}(y {-yA:+d}) {C:+d}(z {-zA:+d}) = 0 \iff {eq}.
\]
Kiểm tra thấy $C \notin (P)$ nên $(P) \parallel CD$.'''
        return caudan, shuffle_choices(correct, wrongs), loi_giai

    elif sub == 4:
        xA, yA, zA = 1, 2, 3
        caudan = fr'''Trong không gian $Oxyz$, cho điểm $A({xA}; {yA}; {zA})$. Mặt phẳng chứa điểm $A$ và chứa trục $Oz$ có phương trình là'''
        correct = r'''$2x - y = 0$'''
        wrongs = [
            r'''$x + y - z = 0$''',
            r'''$3y - 2z = 0$''',
            r'''$3x - z = 0$'''
        ]
        loi_giai = r'''Mặt phẳng $(\alpha)$ chứa trục $Oz$ nên đi qua gốc tọa độ $O(0; 0; 0)$ và có một VTCP là $\vec{k} = (0; 0; 1)$.\\
Mặt khác $(\alpha)$ chứa điểm $A(1; 2; 3)$ nên nhận $\vec{OA} = (1; 2; 3)$ làm VTCP thứ hai.\\
VTPT của $(\alpha)$ là $\vec{n} = [\vec{OA}, \vec{k}] = (2; -1; 0)$.\\
Phương trình mặt phẳng $(\alpha)$ là $2(x - 0) - 1(y - 0) + 0(z - 0) = 0 \iff 2x - y = 0$.'''
        return caudan, shuffle_choices(correct, wrongs), loi_giai

    else:
        a = random.choice([4, 6])
        b = random.choice([6, 8])
        h = random.choice([2, 3])
        D = - a * h
        caudan = fr'''Một mái hiên của tòa nhà trong không gian $Oxyz$ (đơn vị mét) có dạng một phần của mặt phẳng $(\alpha)$ đi qua điểm trên tường $A(0; 0; {h})$, điểm mép ngoài $B({a}; 0; 0)$ và điểm $C(0; {b}; {h})$. Phương trình tổng quát của mặt phẳng $(\alpha)$ chứa mái hiên đó là'''
        correct = fr'''${h}x + {a}z {D:+d} = 0$'''
        wrongs = [
            fr'''${h}x - {a}z {D:+d} = 0$''',
            fr'''${a}x + {h}z {D:+d} = 0$''',
            fr'''${h}x + {b}y + {a}z = 0$'''
        ]
        loi_giai = fr'''Ta có $\vec{{AB}} = ({a}; 0; {-h})$ và $\vec{{AC}} = (0; {b}; 0)$.\\
Tích có hướng $[\vec{{AB}}, \vec{{AC}}] = ({h*b}; 0; {a*b}) = {b}({h}; 0; {a})$.\\
Chọn VTPT $\vec{{n}} = ({h}; 0; {a})$.\\
Phương trình mặt phẳng $(\alpha)$ đi qua $A(0; 0; {h})$:
\[
{h}(x - 0) + 0(y - 0) + {a}(z - {h}) = 0 \iff {h}x + {a}z {D:+d} = 0.
\]'''
        return caudan, shuffle_choices(correct, wrongs), loi_giai


# ==============================================================================
# BÀI 1: PHƯƠNG TRÌNH MẶT PHẲNG - ĐÚNG / SAI (ẢNH 4)
# ==============================================================================

def CuoiChuong5_TF_B1_Cau1():
    xA, yA, zA = 4, 0, -3
    xB, yB, zB = 3, 2, 3
    xC, yC, zC = 4, -1, -5
    AB = (xB - xA, yB - yA, zB - zA)
    AC = (xC - xA, yC - yA, zC - zA)
    caudan = fr'''Trong không gian $Oxyz$, cho mặt phẳng $(P)$ đi qua ba điểm $A({xA}; {yA}; {zA}), B({xB}; {yB}; {zB})$ và $C({xC}; {yC}; {zC})$. Xét tính đúng-sai của các khẳng định sau:'''
    items = [
        (
            fr'''Mặt phẳng $(P)$ có một cặp vectơ chỉ phương là $\vec{{AB}} = ({AB[0]}; {AB[1]}; {AB[2]})$ và $\vec{{AC}} = ({AC[0]}; {AC[1]}; {AC[2]})$.''',
            fr'''Mặt phẳng $(P)$ có một cặp vectơ chỉ phương là $\vec{{AB}} = (1; -2; -6)$ và $\vec{{AC}} = (0; 1; 1)$.''',
            fr'''Vectơ $\vec{{AB}} = ({AB[0]}; {AB[1]}; {AB[2]})$ và $\vec{{AC}} = ({AC[0]}; {AC[1]}; {AC[2]})$ không cùng phương nên là một cặp VTCP của $(P)$.''',
            fr'''Vectơ $(0; 1; 1)$ không cùng phương với $\vec{{AC}} = ({AC[0]}; {AC[1]}; {AC[2]})$.'''
        ),
        (
            fr'''Mặt phẳng $(P)$ có một vectơ pháp tuyến là $\vec{{n}} = (2; -2; 1)$.''',
            fr'''Mặt phẳng $(P)$ có một vectơ pháp tuyến là $\vec{{n}} = (2; 2; 1)$.''',
            fr'''Tích có hướng $[\vec{{AB}}, \vec{{AC}}] = (2; -2; 1)$ nên $\vec{{n}} = (2; -2; 1)$ là một VTPT của $(P)$.''',
            fr'''Tích có hướng $[\vec{{AB}}, \vec{{AC}}] = (2; -2; 1) \ne (2; 2; 1)$.'''
        ),
        (
            fr'''Mặt phẳng $(P)$ có phương trình tổng quát là $2x - 2y + z - 5 = 0$.''',
            fr'''Mặt phẳng $(P)$ có phương trình tổng quát là $2x - 2y + z + 5 = 0$.''',
            fr'''Phương trình $(P)\colon 2(x - 4) - 2(y - 0) + 1(z + 3) = 0 \iff 2x - 2y + z - 5 = 0$.''',
            fr'''Hệ số tự do của phương trình mặt phẳng là $-5$, không phải $+5$.'''
        ),
        (
            fr'''Khoảng cách từ điểm $M(0; 0; 11)$ đến mặt phẳng $(P)$ bằng $2$.''',
            fr'''Khoảng cách từ điểm $M(0; 0; 11)$ đến mặt phẳng $(P)$ bằng $3$.''',
            fr'''Khoảng cách $d(M, (P)) = \frac{{|2 \cdot 0 - 2 \cdot 0 + 11 - 5|}}{{\sqrt{{2^2 + (-2)^2 + 1^2}}}} = \frac{{6}}{{3}} = 2$.''',
            fr'''Khoảng cách $d(M, (P)) = \frac{{|11 - 5|}}{{3}} = 2 \ne 3$.'''
        )
    ]
    choices, loi_giai = make_tf_choices(items)
    return caudan, choices, loi_giai


def CuoiChuong5_TF_B1_Cau2():
    caudan = r'''Trong không gian với hệ tọa độ $Oxyz$, cho điểm $M(1; 1; -2)$ và mặt phẳng $(P)\colon 2x - y + 2z - 3 = 0$. Xét tính đúng-sai của các khẳng định sau:'''
    items = [
        (
            r'''Mặt phẳng $(P)$ vuông góc với mặt phẳng $(Q)\colon x + 2y - 3 = 0$.''',
            r'''Mặt phẳng $(P)$ song song với mặt phẳng $(Q)\colon x + 2y - 3 = 0$.''',
            r'''Ta có $\vec{n}_P = (2; -1; 2)$ và $\vec{n}_Q = (1; 2; 0)$. Tích vô hướng $\vec{n}_P \cdot \vec{n}_Q = 2(1) - 1(2) + 2(0) = 0$ nên $(P) \perp (Q)$.''',
            r'''$\vec{n}_P \cdot \vec{n}_Q = 0$ nên $(P) \perp (Q)$, không song song.'''
        ),
        (
            r'''Khoảng cách từ điểm $M$ đến mặt phẳng $(P)$ bằng $2$.''',
            r'''Khoảng cách từ điểm $M$ đến mặt phẳng $(P)$ bằng $3$.''',
            r'''Khoảng cách $d(M, (P)) = \frac{|2(1) - 1 + 2(-2) - 3|}{\sqrt{2^2 + (-1)^2 + 2^2}} = \frac{|-6|}{3} = 2$.''',
            r'''Khoảng cách tính được bằng $2$, không phải $3$.'''
        ),
        (
            r'''Mặt phẳng $(P)$ có một vectơ pháp tuyến là $\vec{n} = (2; -1; 2)$.''',
            r'''Mặt phẳng $(P)$ có một vectơ pháp tuyến là $\vec{n} = (2; 1; 2)$.''',
            r'''Phương trình $(P)$ có hệ số của $x, y, z$ là $2, -1, 2$ nên VTPT là $\vec{n} = (2; -1; 2)$.''',
            r'''Tung độ của VTPT là $-1$, không phải $1$.'''
        ),
        (
            r'''Mặt phẳng đi qua $M$ và song song với $(P)$ có phương trình là $2x - y + 2z + 3 = 0$.''',
            r'''Mặt phẳng đi qua $M$ và song song với $(P)$ có phương trình là $2x + y + 2z + 1 = 0$.''',
            r'''Mặt phẳng song song với $(P)$ có dạng $2x - y + 2z + D = 0$. Đi qua $M(1; 1; -2) \implies 2(1) - 1 + 2(-2) + D = 0 \iff D = 3$.''',
            r'''Phương trình đúng là $2x - y + 2z + 3 = 0$.'''
        )
    ]
    choices, loi_giai = make_tf_choices(items)
    return caudan, choices, loi_giai


def CuoiChuong5_TF_B1_Cau3():
    caudan = r'''Trong không gian $Oxyz$, cho tam giác $ABC$ có $A(1; 2; 3), B(4; 5; 6), C(1; 0; 2)$ và mặt phẳng $(P)\colon x + 2y - z + 1 = 0$. Xét tính đúng-sai của các khẳng định sau:'''
    items = [
        (
            r'''Mặt phẳng $(P)$ có một vectơ pháp tuyến là $\vec{n} = (1; 2; -1)$.''',
            r'''Mặt phẳng $(P)$ có một vectơ pháp tuyến là $\vec{n} = (1; 2; 1)$.''',
            r'''Từ phương trình $(P)\colon x + 2y - z + 1 = 0$, VTPT là $\vec{n} = (1; 2; -1)$.''',
            r'''Cao độ của VTPT là $-1$, không phải $1$.'''
        ),
        (
            r'''Điểm $A$ không thuộc mặt phẳng $(P)$.''',
            r'''Điểm $A$ thuộc mặt phẳng $(P)$.''',
            r'''Thay tọa độ $A(1; 2; 3)$ vào $(P)$: $1 + 2(2) - 3 + 1 = 3 \ne 0$, do đó $A \notin (P)$.''',
            r'''$1 + 2(2) - 3 + 1 = 3 \ne 0$ nên $A \notin (P)$.'''
        ),
        (
            r'''Mặt phẳng $(ABC)$ có phương trình tổng quát là $x + y - 2z + 3 = 0$.''',
            r'''Mặt phẳng $(ABC)$ có phương trình tổng quát là $x - y - 2z + 3 = 0$.''',
            r'''$\vec{AB} = (3; 3; 3) \parallel (1; 1; 1)$, $\vec{AC} = (0; -2; -1)$. Tích có hướng $[\vec{AB}, \vec{AC}] \parallel (1; 1; -2)$. Phương trình $(ABC)\colon 1(x-1) + 1(y-2) - 2(z-3) = 0 \iff x + y - 2z + 3 = 0$.''',
            r'''Phương trình $(ABC)$ có hệ số của $y$ là $+1$.'''
        ),
        (
            r'''Mặt phẳng $(Q)$ đi qua hai điểm $A, B$ và vuông góc với $(P)$ có phương trình là $3x - 2y - z + 4 = 0$.''',
            r'''Mặt phẳng $(Q)$ đi qua hai điểm $A, B$ và vuông góc với $(P)$ có phương trình là $3x + 2y - z - 4 = 0$.''',
            r'''VTPT của $(Q)$ là $\vec{n}_Q = [\vec{u}_{AB}, \vec{n}_P] = [(1; 1; 1), (1; 2; -1)] = (-3; 2; 1) \parallel (3; -2; -1)$. Phương trình qua $A(1; 2; 3)\colon 3(x-1) - 2(y-2) - (z-3) = 0 \iff 3x - 2y - z + 4 = 0$.''',
            r'''Phương trình đúng là $3x - 2y - z + 4 = 0$.'''
        )
    ]
    choices, loi_giai = make_tf_choices(items)
    return caudan, choices, loi_giai


def CuoiChuong5_TF_B1_Cau4():
    caudan = r'''Trong không gian với hệ tọa độ $Oxyz$, cho ba điểm $A(1; 2; 0), B(1; 0; 2), C(2; 1; 3)$ và mặt phẳng $(P)\colon x - y + 2z + 7 = 0$. Xét tính đúng-sai của các khẳng định sau:'''
    items = [
        (
            r'''Mặt phẳng $(ABC)$ có một vectơ pháp tuyến là $\vec{n} = (2; -1; -1)$.''',
            r'''Mặt phẳng $(ABC)$ có một vectơ pháp tuyến là $\vec{n} = (2; 1; 1)$.''',
            r'''$\vec{AB} = (0; -2; 2), \vec{AC} = (1; -1; 3) \implies [\vec{AB}, \vec{AC}] = (-4; 2; 2) = -2(2; -1; -1)$. Do đó $\vec{n} = (2; -1; -1)$ là một VTPT của $(ABC)$.''',
            r'''Vectơ $(2; 1; 1)$ không cùng phương với $[\vec{AB}, \vec{AC}] = (-4; 2; 2)$.'''
        ),
        (
            r'''Mặt phẳng $(ABC)$ đi qua điểm $M(3; 1; 5)$.''',
            r'''Mặt phẳng $(ABC)$ không đi qua điểm $M(3; 1; 5)$.''',
            r'''Phương trình $(ABC)\colon 2(x-1) - (y-2) - z = 0 \iff 2x - y - z = 0$. Thay $M(3; 1; 5)$: $2(3) - 1 - 5 = 0$ (đúng) nên $M \in (ABC)$.''',
            r'''Thay tọa độ $M(3; 1; 5)$ vào ta được $2(3) - 1 - 5 = 0$ nên $M$ thuộc $(ABC)$.'''
        ),
        (
            r'''Mặt phẳng $(ABC)$ không vuông góc với mặt phẳng $(P)$.''',
            r'''Mặt phẳng $(ABC)$ vuông góc với mặt phẳng $(P)$.''',
            r'''$\vec{n}_{ABC} \cdot \vec{n}_P = 2(1) - 1(-1) - 1(2) = 1 \ne 0$ nên hai mặt phẳng không vuông góc.''',
            r'''Tích vô hướng $\vec{n}_{ABC} \cdot \vec{n}_P = 1 \ne 0$ nên hai mặt phẳng không vuông góc.'''
        ),
        (
            r'''Khoảng cách từ điểm $A$ đến mặt phẳng $(P)$ bằng $\sqrt{6}$.''',
            r'''Khoảng cách từ điểm $A$ đến mặt phẳng $(P)$ bằng $6$.''',
            r'''Khoảng cách $d(A, (P)) = \frac{|1 - 2 + 2(0) + 7|}{\sqrt{1^2 + (-1)^2 + 2^2}} = \frac{6}{\sqrt{6}} = \sqrt{6}$.''',
            r'''Khoảng cách bằng $\frac{6}{\sqrt{6}} = \sqrt{6} \ne 6$.'''
        )
    ]
    choices, loi_giai = make_tf_choices(items)
    return caudan, choices, loi_giai


def CuoiChuong5_TF_B1_Cau5():
    caudan = r'''Trong không gian $Oxyz$, cho mặt phẳng $(P)\colon 10x + 7y - 26z + 2 = 0$. Xét tính đúng-sai của các khẳng định sau:'''
    items = [
        (
            r'''Vectơ $\vec{n} = (10; 7; -26)$ là một vectơ pháp tuyến của mặt phẳng $(P)$.''',
            r'''Vectơ $\vec{n} = (10; -7; -26)$ là một vectơ pháp tuyến của mặt phẳng $(P)$.''',
            r'''Từ phương trình tổng quát của $(P)$, một VTPT là $\vec{n} = (10; 7; -26)$.''',
            r'''Hệ số của $y$ là $+7$, do đó $\vec{n} = (10; -7; -26)$ là sai.'''
        ),
        (
            r'''Khoảng cách từ điểm $M(0; 1; -1)$ đến $(P)$ bằng $\dfrac{7\sqrt{33}}{33}$.''',
            r'''Khoảng cách từ điểm $M(0; 1; -1)$ đến $(P)$ bằng $\dfrac{7\sqrt{33}}{11}$.''',
            r'''$d(M, (P)) = \frac{|10(0) + 7(1) - 26(-1) + 2|}{\sqrt{10^2 + 7^2 + (-26)^2}} = \frac{35}{\sqrt{825}} = \frac{35}{5\sqrt{33}} = \frac{7\sqrt{33}}{33}$.''',
            r'''$d(M, (P)) = \frac{7}{\sqrt{33}} = \frac{7\sqrt{33}}{33} \ne \frac{7\sqrt{33}}{11}$.'''
        ),
        (
            r'''Mặt phẳng $(P)$ không vuông góc với mặt phẳng $(Q)\colon 10x + 7y - 26z + 2 = 0$.''',
            r'''Mặt phẳng $(P)$ vuông góc với mặt phẳng $(Q)\colon 10x + 7y - 26z + 2 = 0$.''',
            r'''Hai mặt phẳng $(P)$ và $(Q)$ trùng nhau nên không vuông góc.''',
            r'''Tích vô hướng $\vec{n}_P \cdot \vec{n}_Q = 10^2 + 7^2 + (-26)^2 = 825 \ne 0$.'''
        ),
        (
            r'''Mặt phẳng $(\alpha)$ đi qua hai điểm $A(-2; -2; -2), B(0; -2; -1)$ và vuông góc với $(P)$ có dạng $ax + by + cz - 138 = 0$. Khi đó $a + b + c = -69$.''',
            r'''Mặt phẳng $(\alpha)$ đi qua hai điểm $A(-2; -2; -2), B(0; -2; -1)$ và vuông góc với $(P)$ có dạng $ax + by + cz - 138 = 0$. Khi đó $a + b + c = 69$.''',
            r'''$\vec{AB} = (2; 0; 1) \implies \vec{n}_\alpha = [\vec{AB}, \vec{n}_P] = (-7; 62; 14) \parallel (7; -62; -14)$. Phương trình qua $B(0; -2; -1)\colon 7(x-0) - 62(y+2) - 14(z+1) = 0 \iff 7x - 62y - 14z - 138 = 0$. Khi đó $a = 7, b = -62, c = -14 \implies a + b + c = -69$.''',
            r'''Ta có $a = 7, b = -62, c = -14 \implies a + b + c = -69 \ne 69$.'''
        )
    ]
    choices, loi_giai = make_tf_choices(items)
    return caudan, choices, loi_giai


def CuoiChuong5_TF_B1_Cau6():
    caudan = r'''Trong không gian với hệ tọa độ $Oxyz$, cho điểm $B(3; -2; 1)$ và ba mặt phẳng $(\alpha)\colon 2x - y + 4z - 5 = 0, (\beta)\colon x + 3y - 2z + 4 = 0, (\gamma)\colon 5x - y + z - 6 = 0$. Xét tính đúng-sai của các khẳng định sau:'''
    items = [
        (
            r'''Mặt phẳng $(\gamma)$ có một vectơ pháp tuyến là $\vec{n} = (5; -1; 1)$.''',
            r'''Mặt phẳng $(\gamma)$ có một vectơ pháp tuyến là $\vec{n} = (5; 1; 1)$.''',
            r'''Từ phương trình $(\gamma)$, VTPT là $\vec{n} = (5; -1; 1)$.''',
            r'''Hệ số của $y$ trong $(\gamma)$ là $-1$, không phải $1$.'''
        ),
        (
            r'''Hai mặt phẳng $(\alpha)$ và $(\beta)$ cắt nhau (không song song).''',
            r'''Mặt phẳng $(\alpha)$ song song với mặt phẳng $(\beta)$.''',
            r'''VTPT của $(\alpha)$ là $(2; -1; 4)$ và $(\beta)$ là $(1; 3; -2)$. Tỉ lệ $\frac{2}{1} \ne \frac{-1}{3}$ nên hai mặt phẳng cắt nhau.''',
            r'''Hai VTPT không cùng phương nên $(\alpha)$ và $(\beta)$ không song song.'''
        ),
        (
            r'''Mặt phẳng $(\beta)$ vuông góc với mặt phẳng $(\gamma)$.''',
            r'''Mặt phẳng $(\beta)$ không vuông góc với mặt phẳng $(\gamma)$.''',
            r'''$\vec{n}_\beta \cdot \vec{n}_\gamma = 1(5) + 3(-1) - 2(1) = 0$ nên $(\beta) \perp (\gamma)$.''',
            r'''$\vec{n}_\beta \cdot \vec{n}_\gamma = 5 - 3 - 2 = 0$ nên $(\beta) \perp (\gamma)$.'''
        ),
        (
            r'''Mặt phẳng $(P)$ đi qua $B$ và vuông góc với $(\alpha), (\gamma)$ có phương trình tổng quát là $x + 6y + z + 8 = 0$.''',
            r'''Mặt phẳng $(P)$ đi qua $B$ và vuông góc với $(\alpha), (\gamma)$ có phương trình tổng quát là $7x + 13y - 2z + 21 = 0$.''',
            r'''VTPT $\vec{n}_P = [\vec{n}_\alpha, \vec{n}_\gamma] = [(2; -1; 4), (5; -1; 1)] = (3; 18; 3) = 3(1; 6; 1)$. Phương trình qua $B(3; -2; 1)\colon 1(x-3) + 6(y+2) + 1(z-1) = 0 \iff x + 6y + z + 8 = 0$.''',
            r'''Phương trình đúng là $x + 6y + z + 8 = 0$, khẳng định $7x + 13y - 2z + 21 = 0$ là sai.'''
        )
    ]
    choices, loi_giai = make_tf_choices(items)
    return caudan, choices, loi_giai

print("All 10 functions defined OK")


# ==============================================================================
# BÀI 2: PHƯƠNG TRÌNH ĐƯỜNG THẲNG TRONG KHÔNG GIAN
# ==============================================================================

def CuoiChuong5_MC_B2_NB1():
    """B2. Phương trình đường thẳng - Mức độ: NB (Dạng 1): Vectơ chỉ phương của đường thẳng"""
    x0, y0, z0 = random.choice([1, 2, -1]), random.choice([3, -2, 0]), random.choice([-3, 4, 1])
    u1, u2, u3 = random.choice([2, 3, -1]), random.choice([-2, 1, 4]), random.choice([3, -4, 5])
    
    caudan = fr'''Trong không gian $Oxyz$, cho đường thẳng $d\colon \begin{{cases}} x = {x0} {u1:+d}t \\ y = {y0} {u2:+d}t \\ z = {z0} {u3:+d}t \end{{cases}}$. Một vectơ chỉ phương của đường thẳng $d$ là'''
    correct = fr'''$\vec{{u}} = ({u1}; {u2}; {u3})$'''
    wrongs = [
        fr'''$\vec{{u}} = ({x0}; {y0}; {z0})$''',
        fr'''$\vec{{u}} = ({-u1}; {u2}; {u3})$''',
        fr'''$\vec{{u}} = ({u1}; {-u2}; {-u3})$'''
    ]
    
    loi_giai = fr'''Hệ số của tham số $t$ trong phương trình tham số của đường thẳng $d$ chính là tọa độ một vectơ chỉ phương của nó: $\vec{{u}} = ({u1}; {u2}; {u3})$.'''

    return caudan, shuffle_choices(correct, wrongs), loi_giai


def CuoiChuong5_MC_B2_NB2():
    """B2. Phương trình đường thẳng - Mức độ: NB (Dạng 2): Phương trình chính tắc của đường thẳng"""
    x0 = random.choice([1, 2, -3])
    y0 = random.choice([-2, 1, 3])
    z0 = random.choice([4, -1, 2])
    
    u1 = random.choice([2, 3, 5])
    u2 = random.choice([-1, -2, 4])
    u3 = random.choice([1, -3, 2])
    
    sign_x0 = f"{-x0:+d}".replace("+", "- ") if x0 > 0 else f"{-x0:+d}".replace("-", "+ ")
    sign_y0 = f"{-y0:+d}".replace("+", "- ") if y0 > 0 else f"{-y0:+d}".replace("-", "+ ")
    sign_z0 = f"{-z0:+d}".replace("+", "- ") if z0 > 0 else f"{-z0:+d}".replace("-", "+ ")
    
    caudan = fr'''Trong không gian $Oxyz$, đường thẳng $d$ đi qua điểm $M({x0}; {y0}; {z0})$ và nhận $\vec{{u}} = ({u1}; {u2}; {u3})$ làm vectơ chỉ phương có phương trình chính tắc là'''
    correct = fr'''$\displaystyle\frac{{x {sign_x0}}}{{{u1}}} = \frac{{y {sign_y0}}}{{{u2}}} = \frac{{z {sign_z0}}}{{{u3}}}$'''
    wrongs = [
        fr'''$\displaystyle\frac{{x {f"{x0:+d}".replace("+", "+ ").replace("-", "- ")}}}{{{u1}}} = \frac{{y {f"{y0:+d}".replace("+", "+ ").replace("-", "- ")}}}{{{u2}}} = \frac{{z {f"{z0:+d}".replace("+", "+ ").replace("-", "- ")}}}{{{u3}}}$''',
        fr'''$\displaystyle\frac{{x {sign_x0}}}{{{x0}}} = \frac{{y {sign_y0}}}{{{y0}}} = \frac{{z {sign_z0}}}{{{z0}}}$''',
        fr'''$\displaystyle\frac{{x {sign_x0}}}{{{u1}}} = \frac{{y {sign_y0}}}{{{-u2}}} = \frac{{z {sign_z0}}}{{{u3}}}$'''
    ]
    
    loi_giai = fr'''Phương trình chính tắc của đường thẳng đi qua điểm $M(x_0; y_0; z_0)$ có VTCP $\vec{{u}} = (u_1; u_2; u_3)$ là:
\[
\frac{{x - x_0}}{{u_1}} = \frac{{y - y_0}}{{u_2}} = \frac{{z - z_0}}{{u_3}} \iff \frac{{x {sign_x0}}}{{{u1}}} = \frac{{y {sign_y0}}}{{{u2}}} = \frac{{z {sign_z0}}}{{{u3}}}.
\]'''

    return caudan, shuffle_choices(correct, wrongs), loi_giai


def CuoiChuong5_MC_B2_TH():
    """B2. Phương trình đường thẳng - Mức độ: TH: Đường thẳng vuông góc với mặt phẳng"""
    # d vuông góc (P) => u_d = n_P
    x0, y0, z0 = random.choice([1, 2, -1]), random.choice([0, -2, 3]), random.choice([2, 1, -3])
    A, B, C = random.choice([2, 3, -1]), random.choice([1, -2, 4]), random.choice([-3, 2, 5])
    D = random.choice([5, -7, 1])
    
    sign_B = f"{B:+d}".replace("+1", "+").replace("-1", "-")
    sign_C = f"{C:+d}".replace("+1", "+").replace("-1", "-")
    
    caudan = fr'''Trong không gian $Oxyz$, đường thẳng $d$ đi qua điểm $A({x0}; {y0}; {z0})$ và vuông góc với mặt phẳng $(P)\colon {A}x {sign_B}y {sign_C}z {D:+d} = 0$ có phương trình tham số là'''
    
    correct = fr'''$\begin{{cases}} x = {x0} {A:+d}t \\ y = {y0} {B:+d}t \\ z = {z0} {C:+d}t \end{{cases}}$'''
    wrongs = [
        fr'''$\begin{{cases}} x = {A} {x0:+d}t \\ y = {B} {y0:+d}t \\ z = {C} {z0:+d}t \end{{cases}}$''',
        fr'''$\begin{{cases}} x = {x0} {-A:+d}t \\ y = {y0} {B:+d}t \\ z = {z0} {-C:+d}t \end{{cases}}$''',
        fr'''$\begin{{cases}} x = {x0} {A:+d}t \\ y = {y0} {-B:+d}t \\ z = {z0} {C:+d}t \end{{cases}}$'''
    ]
    
    loi_giai = fr'''Mặt phẳng $(P)$ có một vectơ pháp tuyến là $\vec{{n}} = ({A}; {B}; {C})$.\\
Vì $d \perp (P)$ nên đường thẳng $d$ nhận $\vec{{n}}$ làm vectơ chỉ phương: $\vec{{u}}_d = \vec{{n}} = ({A}; {B}; {C})$.\\
Phương trình tham số của $d$ qua $A({x0}; {y0}; {z0})$ là:
\[
\begin{{cases}} x = {x0} {A:+d}t \\ y = {y0} {B:+d}t \\ z = {z0} {C:+d}t \end{{cases}} \quad (t \in \mathbb{{R}}).
\]'''

    return caudan, shuffle_choices(correct, wrongs), loi_giai


def CuoiChuong5_MC_B2_VD():
    """B2. Phương trình đường thẳng - Mức độ: VD: Bài toán thực tế đường bay máy bay / drone Oxyz"""
    # Drone cất cánh từ A(0; 0; 0) theo đường thẳng d: x = at, y = bt, z = ct
    # Khi bay đến độ cao z = H (km), hỏi tọa độ vị trí máy bay
    a = random.choice([2, 3, 4])
    b = random.choice([3, 4, 5])
    c = random.choice([1, 2])
    H = c * random.choice([3, 4, 5])
    
    t_val = H // c
    pos_x = a * t_val
    pos_y = b * t_val
    pos_z = H
    
    caudan = fr'''Trong hệ trục toạ độ $Oxyz$ (đơn vị: kilômét), một máy bay không người lái (drone) cất cánh từ vị trí $O(0; 0; 0)$ và bay thẳng đều theo hướng vectơ $\vec{{u}} = ({a}; {b}; {c})$. Khi drone đạt độ cao $z = {H}\text{{ km}}$ so với mặt đất (mặt phẳng $Oxy$), tọa độ vị trí của drone là'''
    
    correct = fr'''$({pos_x}; {pos_y}; {pos_z})$'''
    wrongs = [
        fr'''$({pos_x + a}; {pos_y}; {pos_z})$''',
        fr'''$({pos_x}; {pos_y + b}; {pos_z})$''',
        fr'''$({a}; {b}; {H})$'''
    ]
    
    loi_giai = fr'''Đường bay thẳng của drone xuất phát từ $O(0; 0; 0)$ có phương trình tham số:
\[
\begin{{cases}} x = {a}t \\ y = {b}t \\ z = {c}t \end{{cases}} \quad (t \ge 0).
\]
Khi drone đạt độ cao $z = {H}\text{{ km}}$, ta có ${c}t = {H} \implies t = {t_val}$.\\
Thay $t = {t_val}$ vào phương trình đường bay, ta được tọa độ của drone là:
\[
x = {a} \cdot {t_val} = {pos_x},\quad y = {b} \cdot {t_val} = {pos_y},\quad z = {pos_z}.
\]
Vậy tọa độ vị trí cần tìm là $({pos_x}; {pos_y}; {pos_z})$.'''

    return caudan, shuffle_choices(correct, wrongs), loi_giai


# ==============================================================================
# BÀI 3: PHƯƠNG TRÌNH MẶT CẦU
# ==============================================================================

def CuoiChuong5_MC_B3_NB1():
    """B3. Phương trình mặt cầu - Mức độ: NB (Dạng 1): Xác định tâm và bán kính dạng chính tắc"""
    a = random.choice([1, 2, -3, -4])
    b = random.choice([-2, 3, -1, 5])
    c = random.choice([4, -5, 2, -1])
    R = random.choice([3, 4, 5, 6])
    R2 = R ** 2
    
    sign_a = f"{-a:+d}".replace("+", "- ") if a > 0 else f"{-a:+d}".replace("-", "+ ")
    sign_b = f"{-b:+d}".replace("+", "- ") if b > 0 else f"{-b:+d}".replace("-", "+ ")
    sign_c = f"{-c:+d}".replace("+", "- ") if c > 0 else f"{-c:+d}".replace("-", "+ ")
    
    caudan = fr'''Trong không gian $Oxyz$, cho mặt cầu $(S)\colon (x {sign_a})^2 + (y {sign_b})^2 + (z {sign_c})^2 = {R2}$. Tọa độ tâm $I$ và bán kính $R$ của mặt cầu $(S)$ là'''
    correct = fr'''$I({a}; {b}; {c})$ và $R = {R}$'''
    wrongs = [
        fr'''$I({-a}; {-b}; {-c})$ và $R = {R}$''',
        fr'''$I({a}; {b}; {c})$ và $R = {R2}$''',
        fr'''$I({-a}; {-b}; {-c})$ và $R = {R2}$'''
    ]
    
    loi_giai = fr'''Phương trình mặt cầu dạng $(x - a)^2 + (y - b)^2 + (z - c)^2 = R^2$ có tâm $I(a; b; c)$ và bán kính $R = \sqrt{{{R2}}} = {R}$.\\
Đối chiếu phương trình $(x {sign_a})^2 + (y {sign_b})^2 + (z {sign_c})^2 = {R2}$, ta được $I({a}; {b}; {c})$ và $R = {R}$.'''

    return caudan, shuffle_choices(correct, wrongs), loi_giai


def CuoiChuong5_MC_B3_NB2():
    """B3. Phương trình mặt cầu - Mức độ: NB (Dạng 2): Tâm và bán kính từ dạng khai triển"""
    a = random.choice([1, 2, -1, -2])
    b = random.choice([2, -3, 1])
    c = random.choice([-2, 1, 3])
    R = random.choice([2, 3, 4])
    # a^2 + b^2 + c^2 - d = R^2 => d = a^2 + b^2 + c^2 - R^2
    d = (a ** 2) + (b ** 2) + (c ** 2) - (R ** 2)
    
    coef_x = -2 * a
    coef_y = -2 * b
    coef_z = -2 * c
    
    caudan = fr'''Trong không gian $Oxyz$, mặt cầu $(S)\colon x^2 + y^2 + z^2 {coef_x:+d}x {coef_y:+d}y {coef_z:+d}z {d:+d} = 0$ có bán kính bằng bao nhiêu?'''
    correct = fr'''$R = {R}$'''
    wrongs = [
        fr'''$R = {R ** 2}$''',
        fr'''$R = {R + 1}$''',
        fr'''$R = \sqrt{{{abs(d)}}}$'''
    ]
    
    loi_giai = fr'''Ta có các hệ số: $a = {-coef_x // 2} = {a}$, $b = {-coef_y // 2} = {b}$, $c = {-coef_z // 2} = {c}$ và $d = {d}$.\\
Bán kính của mặt cầu là:
\[
R = \sqrt{{a^2 + b^2 + c^2 - d}} = \sqrt{{{a}^2 + ({b})^2 + ({c})^2 - ({d})}} = \sqrt{{{R**2}}} = {R}.
\]'''

    return caudan, shuffle_choices(correct, wrongs), loi_giai


def CuoiChuong5_MC_B3_TH():
    """B3. Phương trình mặt cầu - Mức độ: TH: Viết phương trình mặt cầu đường kính AB"""
    xA, yA, zA = random.choice([1, 2]), random.choice([0, -1]), random.choice([2, 1])
    # Tạo B sao cho AB có độ dài là 2*R chẵn (AB^2 = 4*R^2)
    dx, dy, dz = 2, 4, 4  # dx^2 + dy^2 + dz^2 = 4 + 16 + 16 = 36 => AB = 6, R = 3, R^2 = 9
    xB = xA + dx * random.choice([1, -1])
    yB = yA + dy * random.choice([1, -1])
    zB = zA + dz * random.choice([1, -1])
    
    xI = (xA + xB) // 2
    yI = (yA + yB) // 2
    zI = (zA + zB) // 2
    R2 = 9
    
    sign_a = f"{-xI:+d}".replace("+", "- ") if xI > 0 else f"{-xI:+d}".replace("-", "+ ")
    sign_b = f"{-yI:+d}".replace("+", "- ") if yI > 0 else f"{-yI:+d}".replace("-", "+ ")
    sign_c = f"{-zI:+d}".replace("+", "- ") if zI > 0 else f"{-zI:+d}".replace("-", "+ ")
    
    caudan = fr'''Trong không gian $Oxyz$, phương trình mặt cầu $(S)$ có đường kính $AB$ với $A({xA}; {yA}; {zA})$ và $B({xB}; {yB}; {zB})$ là'''
    correct = fr'''$(x {sign_a})^2 + (y {sign_b})^2 + (z {sign_c})^2 = {R2}$'''
    wrongs = [
        fr'''$(x {sign_a})^2 + (y {sign_b})^2 + (z {sign_c})^2 = 36$''',
        fr'''$(x {f"{xI:+d}".replace("+", "+ ").replace("-", "- ")})^2 + (y {f"{yI:+d}".replace("+", "+ ").replace("-", "- ")})^2 + (z {f"{zI:+d}".replace("+", "+ ").replace("-", "- ")})^2 = {R2}$''',
        fr'''$(x {sign_a})^2 + (y {sign_b})^2 + (z {sign_c})^2 = 3$'''
    ]
    
    loi_giai = fr'''Tâm $I$ của mặt cầu là trung điểm đoạn thẳng $AB$:
\[
I\left(\frac{{{xA} + ({xB})}}{{2}}; \frac{{{yA} + ({yB})}}{{2}}; \frac{{{zA} + ({zB})}}{{2}}\right) \implies I({xI}; {yI}; {zI}).
\]
Độ dài $AB = \sqrt{{({xB} - {xA})^2 + ({yB} - {yA})^2 + ({zB} - {zA})^2}} = \sqrt{{36}} = 6$.\\
Bán kính mặt cầu là $R = \frac{{AB}}{{2}} = 3 \implies R^2 = 9$.\\
Phương trình mặt cầu là: $(x {sign_a})^2 + (y {sign_b})^2 + (z {sign_c})^2 = 9$.'''

    return caudan, shuffle_choices(correct, wrongs), loi_giai


def CuoiChuong5_MC_B3_VD():
    """B3. Phương trình mặt cầu - Mức độ: VD: Bài toán thực tế trạm radar / vùng phủ sóng dạng mặt cầu"""
    # Trạm phát sóng đặt tại I(x0, y0, z0), bán kính phủ sóng R km
    # Mục tiêu M(xM, yM, zM), tính khoảng cách IM và so sánh với R
    x0, y0, z0 = 1, 2, 3
    R = random.choice([5, 10, 13])
    
    # Tạo điểm M sao cho IM = R - 1 hoặc R + 2
    in_range = random.choice([True, False])
    if in_range:
        # IM < R
        dist = R - 2
        M_str = f"M({x0 + dist}; {y0}; {z0})"
        correct = fr'''Mục tiêu $M$ nằm trong vùng phủ sóng (vì khoảng cách từ trạm đến mục tiêu $d = {dist}\text{{ km}} < R$).'''
        wrongs = [
            fr'''Mục tiêu $M$ nằm ngoài vùng phủ sóng (vì khoảng cách $d = {dist}\text{{ km}} > R$).''',
            fr'''Mục tiêu $M$ nằm chính xác trên ranh giới vùng phủ sóng.''',
            fr'''Không xác định được do thiếu thông tin công suất trạm phát.'''
        ]
        loi_giai = fr'''Khoảng cách từ trạm radar $I({x0}; {y0}; {z0})$ đến mục tiêu $M({x0 + dist}; {y0}; {z0})$ là:
\[
d = IM = \sqrt{{({x0+dist} - {x0})^2 + ({y0} - {y0})^2 + ({z0} - {z0})^2}} = {dist}\text{{ km}}.
\]
Vì $d = {dist}\text{{ km}} < R = {R}\text{{ km}}$, nên mục tiêu $M$ nằm bên trong vùng phát sóng của trạm.'''
    else:
        # IM > R
        dist = R + 2
        M_str = f"M({x0 + dist}; {y0}; {z0})"
        correct = fr'''Mục tiêu $M$ nằm ngoài vùng phủ sóng (vì khoảng cách từ trạm đến mục tiêu $d = {dist}\text{{ km}} > R$).'''
        wrongs = [
            fr'''Mục tiêu $M$ nằm trong vùng phủ sóng (vì khoảng cách $d = {dist}\text{{ km}} < R$).''',
            fr'''Mục tiêu $M$ nằm chính xác trên ranh giới vùng phủ sóng.''',
            fr'''Không xác định được do thiếu thông tin công suất trạm phát.'''
        ]
        loi_giai = fr'''Khoảng cách từ trạm radar $I({x0}; {y0}; {z0})$ đến mục tiêu $M({x0 + dist}; {y0}; {z0})$ là:
\[
d = IM = \sqrt{{({x0+dist} - {x0})^2 + ({y0} - {y0})^2 + ({z0} - {z0})^2}} = {dist}\text{{ km}}.
\]
Vì $d = {dist}\text{{ km}} > R = {R}\text{{ km}}$, nên mục tiêu $M$ nằm ngoài vùng phát sóng của trạm.'''

    caudan = fr'''Trong hệ toạ độ $Oxyz$ (đơn vị: kilômét), một trạm thu phát tín hiệu đặt tại điểm $I({x0}; {y0}; {z0})$ có bán kính phát sóng an toàn là $R = {R}\text{{ km}}$ (tạo thành một vùng không gian dạng hình cầu tâm $I$, bán kính $R$). Một thiết bị bay tại vị trí ${M_str}$. Kết luận nào sau đây là đúng?'''

    return caudan, shuffle_choices(correct, wrongs), loi_giai


# Alias tương thích ngược
CuoiChuong5_MC_Cau1 = CuoiChuong5_MC_B1_NB1
CuoiChuong5_MC_Cau2 = CuoiChuong5_MC_B1_NB2
CuoiChuong5_MC_Cau3 = CuoiChuong5_MC_B1_TH
CuoiChuong5_MC_Cau4 = CuoiChuong5_MC_B1_VD
CuoiChuong5_MC_Cau5 = CuoiChuong5_MC_B2_NB1
CuoiChuong5_MC_Cau6 = CuoiChuong5_MC_B2_NB2
CuoiChuong5_MC_Cau7 = CuoiChuong5_MC_B2_TH
CuoiChuong5_MC_Cau8 = CuoiChuong5_MC_B2_VD
CuoiChuong5_MC_Cau9 = CuoiChuong5_MC_B3_NB1
CuoiChuong5_MC_Cau10 = CuoiChuong5_MC_B3_NB2
CuoiChuong5_MC_Cau11 = CuoiChuong5_MC_B3_TH
CuoiChuong5_MC_Cau12 = CuoiChuong5_MC_B3_VD
