# -*- coding: utf-8 -*-
"""
Module Đề thi thử / Đề ôn tập số 2 (12 câu Trắc nghiệm + 4 câu Đúng/Sai)
Được chuẩn hóa và ngẫu nhiên hóa tham số dựa trên cấu trúc đề tốt nghiệp THPT 2025.
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
    for i, item in enumerate(items):
        stmt_t, stmt_f, exp_t, exp_f = item
        is_true = random.choice([True, False])
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


# ==============================================================================
# PHẦN I: 12 CÂU TRẮC NGHIỆM NHIỀU PHƯƠNG ÁN (MC)
# ==============================================================================

def DeThiThu02_MC_Cau1():
    # Câu 1: Vectơ trong hình lập phương ABCD.A'B'C'
    groups = [
        ("AD", r"\overrightarrow{AD}", [r"\overrightarrow{B'C'}", r"\overrightarrow{BC}", r"\overrightarrow{A'D'}"], 
               [r"\overrightarrow{CD}", r"\overrightarrow{AA'}", r"\overrightarrow{AB}", r"\overrightarrow{D'A'}"]),
        ("AB", r"\overrightarrow{AB}", [r"\overrightarrow{DC}", r"\overrightarrow{A'B'}", r"\overrightarrow{D'C'}"],
               [r"\overrightarrow{AD}", r"\overrightarrow{BC}", r"\overrightarrow{AA'}", r"\overrightarrow{B'A'}"]),
        ("AA'", r"\overrightarrow{AA'}", [r"\overrightarrow{BB'}", r"\overrightarrow{CC'}", r"\overrightarrow{DD'}"],
               [r"\overrightarrow{AB}", r"\overrightarrow{AD}", r"\overrightarrow{A'A}", r"\overrightarrow{B'C}"]),
        ("BC", r"\overrightarrow{BC}", [r"\overrightarrow{AD}", r"\overrightarrow{B'C'}", r"\overrightarrow{A'D'}"],
               [r"\overrightarrow{BA}", r"\overrightarrow{CD}", r"\overrightarrow{BB'}", r"\overrightarrow{CB}"]),
    ]
    name, target_vec, equal_vecs, diff_vecs = random.choice(groups)
    correct_vec = random.choice(equal_vecs)
    wrong_vecs = random.sample(diff_vecs, 3)

    caudan = fr'''Cho hình lập phương $ABCD.A'B'C'$ (xem hình dưới). Vectơ nào sau đây bằng vectơ ${target_vec}$?
\begin{{center}}
\begin{{tikzpicture}}[scale=1, line join=round, line cap=round]
\coordinate (D) at (0,0);
\coordinate (C) at (2,0);
\coordinate (B) at (2.7,0.7);
\coordinate (A) at (0.7,0.7);
\coordinate (D') at (0,2);
\coordinate (C') at (2,2);
\coordinate (B') at (2.7,2.7);
\coordinate (A') at (0.7,2.7);

\draw (D) node[below] {{$D$}} -- (C) node[below] {{$C$}} -- (C') node[above left] {{$C'$}} -- (D') node[above left] {{$D'$}} -- cycle;
\draw (C) -- (B) node[right] {{$B$}} -- (B') node[above right] {{$B'$}} -- (C');
\draw (D') -- (A') node[above left] {{$A'$}} -- (B');
\draw[dashed] (D) -- (A) node[above left] {{$A$}} -- (B);
\draw[dashed] (A) -- (A');
\end{{tikzpicture}}
\end{{center}}'''

    choices = shuffle_choices(f"${correct_vec}$", [f"${w}$" for w in wrong_vecs])
    loi_giai = fr'''Dựa vào tính chất của hình lập phương $ABCD.A'B'C'$, các đoạn thẳng tương ứng song song, bằng nhau và cùng hướng.
Do đó ta có ${target_vec} = {correct_vec}$.'''
    return caudan, choices, loi_giai


def DeThiThu02_MC_Cau2():
    # Câu 2: Đường tiệm cận đứng của hàm số nhất biến từ bảng biến thiên
    x0 = random.choice([-3, -2, -1, 1, 2, 3])
    y0 = random.choice([-3, -2, -1, 1, 2, 3])
    while y0 == x0:
        y0 = random.choice([-3, -2, -1, 1, 2, 3])
    
    is_increasing = random.choice([True, False])
    if is_increasing:
        sign = "+"
        left_lim = fr"+\infty"
        right_lim = fr"-\infty"
        tab_var = fr"-/ ${y0}$, +D- / ${left_lim}$ / ${right_lim}$, +/ ${y0}$"
    else:
        sign = "-"
        left_lim = fr"-\infty"
        right_lim = fr"+\infty"
        tab_var = fr"+/ ${y0}$, -D+ / ${left_lim}$ / ${right_lim}$, -/ ${y0}$"

    caudan = fr'''Cho hàm số $y=\dfrac{{ax+b}}{{cx+d}}$ ($c \ne 0, ad-bc \ne 0$) có bảng biến thiên như hình dưới đây:
\begin{{center}}
\begin{{tikzpicture}}
\tkzTabInit[lgt=1.2,espcl=3,deltacl=0.6]
{{$x$ / 0.6, $y'$ / 0.6, $y$ / 2}}
{{$-\infty$, ${x0}$, $+\infty$}}
\tkzTabLine{{ , {sign}, d, {sign}, }}
\tkzTabVar{{{tab_var}}}
\end{{tikzpicture}}
\end{{center}}
Đường tiệm cận đứng của đồ thị hàm số đã cho có phương trình là'''

    correct = fr"$x={x0}$"
    wrongs = [
        fr"$x={y0}$",
        fr"$y={y0}$",
        fr"$y={x0}$"
    ]
    choices = shuffle_choices(correct, wrongs)
    loi_giai = fr'''Từ bảng biến thiên, ta thấy $\lim\limits_{{x \to {x0}^-}} y = {left_lim}$ và $\lim\limits_{{x \to {x0}^+}} y = {right_lim}$ nên đường thẳng $x = {x0}$ là đường tiệm cận đứng của đồ thị hàm số.'''
    return caudan, choices, loi_giai


def DeThiThu02_MC_Cau3():
    # Câu 3: Phương trình log_a(b*x) = c
    a = random.choice([2, 3, 5])
    c = random.choice([2, 3])
    val = a**c
    divs = [d for d in [2, 3, 4, 5] if val % d == 0]
    if divs:
        b = random.choice(divs)
    else:
        b = random.choice([2, 3])
    
    ans_num = val
    ans_den = b
    g = math.gcd(ans_num, ans_den)
    num_simp = ans_num // g
    den_simp = ans_den // g

    def fmt_frac(n, d):
        if d == 1:
            return str(n)
        return fr"\dfrac{{{n}}}{{{d}}}"

    correct = fmt_frac(num_simp, den_simp)
    wrongs = set()
    w1 = fmt_frac(c, b)
    if w1 != correct: wrongs.add(w1)
    w2 = fmt_frac(a * c, b)
    if w2 != correct: wrongs.add(w2)
    w3 = fmt_frac(val - 1, b)
    if w3 != correct: wrongs.add(w3)
    w4 = fmt_frac(val + 1, b)
    if w4 != correct: wrongs.add(w4)
    w_list = list(wrongs)[:3]
    while len(w_list) < 3:
        w_list.append(str(random.randint(1, 10)))

    caudan = fr'''Nghiệm của phương trình $\log_{{{a}}}({b}x) = {c}$ là'''
    choices = shuffle_choices(fr"$x = {correct}$", [fr"$x = {w}$" for w in w_list])
    loi_giai = fr'''Ta có: $\log_{{{a}}}({b}x) = {c} \iff {b}x = {a}^{{{c}}} \iff {b}x = {val} \iff x = {correct}$.'''
    return caudan, choices, loi_giai


def DeThiThu02_MC_Cau4():
    # Câu 4: F(x) = k*x^n là nguyên hàm của f(x) = k*n*x^{n-1}
    k = random.randint(2, 7)
    n = random.randint(3, 5)
    f_coef = k * n
    f_pow = n - 1

    caudan = fr'''Hàm số $F(x) = {k}x^{{{n}}}$ là một nguyên hàm của hàm số nào sau đây?'''
    correct = fr'''f_3(x) = {f_coef}x^{{{f_pow}}}'''
    w1 = fr'''f_1(x) = \dfrac{{{k}x^{{{n+1}}}}}{{{n+1}}}'''
    w2 = fr'''f_2(x) = {k}x^{{{f_pow}}}'''
    w3 = fr'''f_4(x) = {k}x^{{{n+1}}}'''

    choices = shuffle_choices(f"${correct}$", [f"${w1}$", f"${w2}$", f"${w3}$"])
    loi_giai = fr'''Hàm số $F(x)$ là nguyên hàm của hàm số $f(x)$ nên ta có:
$f(x) = F'(x) = ({k}x^{{{n}}})' = {k} \cdot {n}x^{{{f_pow}}} = {f_coef}x^{{{f_pow}}}$.
Vậy $F(x) = {k}x^{{{n}}}$ là một nguyên hàm của hàm số $f_3(x) = {f_coef}x^{{{f_pow}}}$.'''
    return caudan, choices, loi_giai


def DeThiThu02_MC_Cau5():
    # Câu 5: Hai biến cố độc lập P(AB) = P(A)*P(B)
    p1 = random.choice([0.2, 0.3, 0.4, 0.5])
    p2 = random.choice([0.4, 0.5, 0.6, 0.7])
    p_ab = round(p1 * p2, 4)
    
    p1_str = str(p1).replace('.', ',')
    p2_str = str(p2).replace('.', ',')
    p_ab_str = str(p_ab).replace('.', ',')

    caudan = fr'''Cho hai biến cố độc lập $A$ và $B$ có xác suất thỏa mãn $P(A) = {p1_str}$ và $P(B) = {p2_str}$. Giá trị của $P(AB)$ bằng'''
    
    correct = p_ab_str
    w1 = str(round(p1 + p2, 2)).replace('.', ',')
    w2 = str(round(abs(p1 - p2), 2)).replace('.', ',')
    w3 = p1_str if p1_str != p_ab_str else p2_str

    choices = shuffle_choices(f"${correct}$", [f"${w1}$", f"${w2}$", f"${w3}$"])
    loi_giai = fr'''Vì $A$ và $B$ là hai biến cố độc lập nên ta có:
$P(AB) = P(A) \cdot P(B) = {p1_str} \cdot {p2_str} = {p_ab_str}$.'''
    return caudan, choices, loi_giai


def DeThiThu02_MC_Cau6():
    # Câu 6: Nghiệm của hệ bất phương trình bậc nhất 2 ẩn
    c1 = random.choice([2, 3, 4])
    c2 = random.choice([1, 2, 3])

    x0, y0 = 1, 0
    while not (x0 + y0 - c1 < 0 and x0 - y0 + c2 > 0):
        x0 = random.randint(-1, 2)
        y0 = random.randint(-1, 2)

    correct_pt = (x0, y0)
    wrong_pt1 = (c1 + 1, 1)
    wrong_pt2 = (-c2 - 1, 2)
    wrong_pt3 = (c1, c1 + c2 + 2)

    caudan = fr'''Cặp số nào sau đây là nghiệm của hệ bất phương trình $\begin{{cases}} x+y-{c1} < 0 \\ x-y+{c2} > 0 \end{{cases}}$?'''
    
    correct = fr"({correct_pt[0]}; {correct_pt[1]})"
    w1 = fr"({wrong_pt1[0]}; {wrong_pt1[1]})"
    w2 = fr"({wrong_pt2[0]}; {wrong_pt2[1]})"
    w3 = fr"({wrong_pt3[0]}; {wrong_pt3[1]})"

    choices = shuffle_choices(f"${correct}$", [f"${w1}$", f"${w2}$", f"${w3}$"])
    v1 = x0 + y0 - c1
    v2 = x0 - y0 + c2
    loi_giai = fr'''Thay $(x; y) = ({correct_pt[0]}; {correct_pt[1]})$ vào hệ ta được:
$\begin{{cases}} {x0} + {y0} - {c1} = {v1} < 0 \text{{ (đúng)}} \\ {x0} - {y0} + {c2} = {v2} > 0 \text{{ (đúng)}} \end{{cases}}$.
Vậy $({correct_pt[0]}; {correct_pt[1]})$ là một nghiệm của hệ bất phương trình.'''
    return caudan, choices, loi_giai


def DeThiThu02_MC_Cau7():
    # Câu 7: Cấp số cộng u_1, d tính u_2 = u_1 + d
    u1 = random.choice([-5, -4, -3, -2, 2, 3, 4])
    d = random.choice([-3, -2, 2, 3, 4, 5])
    u2 = u1 + d

    caudan = fr'''Cho cấp số cộng $(u_n)$ có $u_1 = {u1}$ và công sai $d = {d}$. Giá trị của $u_2$ bằng'''
    
    correct = str(u2)
    w1 = str(u1 * d)
    w2 = str(u1 - d)
    w3 = str(u1 + 2 * d)
    if w1 == correct: w1 = str(u2 + 1)
    if w2 == correct: w2 = str(u2 - 1)
    if w3 == correct: w3 = str(u2 + 2)

    choices = shuffle_choices(f"${correct}$", [f"${w1}$", f"${w2}$", f"${w3}$"])
    loi_giai = fr'''Ta có $u_2 = u_1 + d = {u1} + ({d}) = {u2}$.'''
    return caudan, choices, loi_giai


def DeThiThu02_MC_Cau8():
    # Câu 8: Tìm nhóm chứa trung vị của mẫu số liệu ghép nhóm
    groups = ["[10;20)", "[20;30)", "[30;40)", "[40;50)", "[50;60)", "[60;70)"]
    f1 = random.randint(4, 7)
    f2 = random.randint(6, 9)
    f3 = random.randint(14, 18)
    f4 = random.randint(5, 8)
    f5 = random.randint(4, 7)
    f6 = random.randint(3, 5)
    freqs = [f1, f2, f3, f4, f5, f6]
    N = sum(freqs)
    
    cfs = []
    curr = 0
    for f in freqs:
        curr += f
        cfs.append(curr)

    median_idx = 0
    half = N / 2
    for i, cf in enumerate(cfs):
        if cf >= half:
            median_idx = i
            break

    correct_group = groups[median_idx]
    other_groups = [g for i, g in enumerate(groups) if i != median_idx]
    wrong_groups = random.sample(other_groups, 3)

    caudan = fr'''Khảo sát thời gian (đơn vị: phút) học trực tuyến trong một ngày của ${N}$ học sinh, người ta thu được mẫu số liệu ghép nhóm như sau:
\begin{{center}}
\begin{{tabular}}{{|l|c|c|c|c|c|c|}}
\hline
Thời gian học trực tuyến & $[10;20)$ & $[20;30)$ & $[30;40)$ & $[40;50)$ & $[50;60)$ & $[60;70)$ \\ \hline
Số học sinh & ${f1}$ & ${f2}$ & ${f3}$ & ${f4}$ & ${f5}$ & ${f6}$ \\ \hline
\end{{tabular}}
\end{{center}}
Trung vị của mẫu số liệu trên thuộc nhóm nào sau đây?'''

    choices = shuffle_choices(f"${correct_group}$", [f"${w}$" for w in wrong_groups])
    loi_giai = fr'''Cỡ mẫu là $N = {N}$. Trung vị của mẫu số liệu là trung bình cộng của giá trị thứ ${N // 2}$ và ${N // 2 + 1}$. \\
Tần số tích lũy của các nhóm lần lượt là: ${'; '.join(str(c) for c in cfs)}$. \\
Do các giá trị thứ ${N // 2}$ và ${N // 2 + 1}$ đều nằm trong nhóm có tần số tích lũy là ${cfs[median_idx]}$, nên trung vị thuộc nhóm ${correct_group}$.'''
    return caudan, choices, loi_giai


def DeThiThu02_MC_Cau9():
    # Câu 9: Đạo hàm của hàm tổng f(x) + g(x)
    a = random.choice([2, 3, 4, 5])
    b = random.choice([1, 2, 3])
    b_str = f"{b}x^2" if b > 1 else "x^2"

    caudan = fr'''Cho các hàm số $y=f(x)$ và $y=g(x)$ có đạo hàm trên tập số thực $\mathbb{{R}}$ thỏa mãn $f'(x) = {a}x$ và $g'(x) = {b_str}$. Đạo hàm của hàm số $y=f(x)+g(x)$ là'''
    
    correct = fr"{a}x + {b_str}"
    w1 = fr"{a} + {b_str}"
    w2 = fr"{a + 2}x"
    w3 = fr"{a} + {2*b}x"

    choices = shuffle_choices(f"${correct}$", [f"${w1}$", f"${w2}$", f"${w3}$"])
    loi_giai = fr'''Ta có: $y' = [f(x) + g(x)]' = f'(x) + g'(x) = {a}x + {b_str}$.'''
    return caudan, choices, loi_giai


def DeThiThu02_MC_Cau10():
    # Câu 10: \int [k + f(x)] dx = kx + \int f(x) dx
    k = random.randint(2, 5)
    trig_func, trig_int = random.choice([
        (r"\cos x", r"\sin x"),
        (r"\sin x", r"-\cos x"),
    ])

    caudan = fr'''Cho $\displaystyle\int f(x)\,\mathrm{{d}}x = {trig_int} + C$. Phát biểu nào sau đây là đúng?'''
    
    correct = fr"\displaystyle\int [{k} + f(x)]\,\mathrm{{d}}x = {k}x + {trig_int} + C"
    w1 = fr"\displaystyle\int [{k} + f(x)]\,\mathrm{{d}}x = {k}x - {trig_int} + C"
    w2 = fr"\displaystyle\int [{k} + f(x)]\,\mathrm{{d}}x = {k}x + {trig_func} + C"
    w3 = fr"\displaystyle\int [{k} + f(x)]\,\mathrm{{d}}x = {k}x - {trig_func} + C"

    choices = shuffle_choices(f"${correct}$", [f"${w1}$", f"${w2}$", f"${w3}$"])
    loi_giai = fr'''Theo tính chất của nguyên hàm, ta có:
$\displaystyle\int [{k} + f(x)]\,\mathrm{{d}}x = \displaystyle\int {k}\,\mathrm{{d}}x + \displaystyle\int f(x)\,\mathrm{{d}}x = {k}x + {trig_int} + C$.'''
    return caudan, choices, loi_giai


def DeThiThu02_MC_Cau11():
    # Câu 11: Vectơ AB trong không gian Oxyz
    xA, yA, zA = random.randint(-3, 4), random.randint(-3, 4), random.randint(-3, 4)
    xB, yB, zB = random.randint(-3, 4), random.randint(-3, 4), random.randint(-3, 4)
    while (xA, yA, zA) == (xB, yB, zB):
        xB = random.randint(-3, 4)

    dx = xB - xA
    dy = yB - yA
    dz = zB - zA

    caudan = fr'''Trong không gian với hệ tọa độ $Oxyz$, cho hai điểm $A({xA}; {yA}; {zA})$ và $B({xB}; {yB}; {zB})$. Vectơ $\overrightarrow{{AB}}$ có tọa độ là'''
    
    correct = fr"({dx}; {dy}; {dz})"
    w1 = fr"({-dx}; {-dy}; {-dz})"
    w2 = fr"({xA + xB}; {yA + yB}; {zA + zB})"
    w3 = fr"({dx}; {dy}; {dz + 1})"

    choices = shuffle_choices(f"${correct}$", [f"${w1}$", f"${w2}$", f"${w3}$"])
    loi_giai = fr'''Ta có: $\overrightarrow{{AB}} = (x_B - x_A; y_B - y_A; z_B - z_A) = ({xB} - ({xA}); {yB} - ({yA}); {zB} - ({zA})) = ({dx}; {dy}; {dz})$.'''
    return caudan, choices, loi_giai


def DeThiThu02_MC_Cau12():
    # Câu 12: Cấp số nhân u_k = u_1 * q^(k-1)
    k = random.choice([3, 4, 5])
    pow_q = k - 1

    caudan = fr'''Cho cấp số nhân $(u_n)$ có số hạng đầu $u_1$ và công bội $q$ với $u_1 \ne 0, q > 1$. Số hạng $u_{{{k}}}$ là'''
    
    correct = fr"u_{{{k}}} = u_1 q^{{{pow_q}}}"
    w1 = fr"u_{{{k}}} = u_1 q^{{{k}}}"
    w2 = fr"u_{{{k}}} = u_1 + {pow_q}q"
    w3 = fr"u_{{{k}}} = u_1 + {k}q"

    choices = shuffle_choices(f"${correct}$", [f"${w1}$", f"${w2}$", f"${w3}$"])
    loi_giai = fr'''Theo công thức số hạng tổng quát của cấp số nhân, ta có: $u_n = u_1 q^{{n-1}}$.
Do đó $u_{{{k}}} = u_1 q^{{{pow_q}}}$.'''
    return caudan, choices, loi_giai


# ==============================================================================
# PHẦN II: 4 CÂU ĐÚNG / SAI (TF)
# ==============================================================================

# ==============================================================================
# PHẦN II: 4 CÂU ĐÚNG / SAI (TF)
# ==============================================================================

def DeThiThu02_TF_Cau1():
    # TF 1: Oxyz - Vành đai bảo vệ bán kính R và drone bay thẳng từ M đến N ngẫu nhiên hóa số đẹp
    triples = [
        # (xP, yP, d0, R_unit, h_unit, d_circ, d_min_unit)
        (6, 8, 10, 6, 3, 4, 5),     # d_circ=4, h=3 => d_min=5 => 50m
        (8, 6, 10, 6, 3, 4, 5),
        (-6, 8, 10, 6, 3, 4, 5),
        (8, 6, 10, 7, 4, 3, 5),     # d_circ=3, h=4 => d_min=5 => 50m
        (6, 8, 10, 7, 4, 3, 5),
        (12, 5, 13, 7, 8, 6, 10),   # d_circ=6, h=8 => d_min=10 => 100m
        (5, 12, 13, 7, 8, 6, 10),
        (9, 12, 15, 9, 8, 6, 10),   # d_circ=6, h=8 => d_min=10 => 100m
        (12, 9, 15, 9, 8, 6, 10),
        (8, 15, 17, 12, 12, 5, 13), # d_circ=5, h=12 => d_min=13 => 130m
        (15, 8, 17, 12, 12, 5, 13),
    ]
    cfg = random.choice(triples)
    xP, yP, d0, R_unit, h_unit, d_circ_min, d_min_unit = cfg
    zP = h_unit
    
    g = math.gcd(abs(xP), abs(yP))
    ux = -yP // g
    uy = xP // g
    uz = 0
    
    t_min = random.choice([1, 2])
    t_span = random.choice([2, 3])
    t_end = t_min + t_span
    
    xM = xP - t_min * ux
    yM = yP - t_min * uy
    zM = h_unit
    
    xN = xP + (t_end - t_min) * ux
    yN = yP + (t_end - t_min) * uy
    zN = h_unit
    
    vec_MN = (xN - xM, yN - yM, zN - zM)
    R_meter = R_unit * 10
    d_min_meter = d_min_unit * 10

    caudan = fr'''Trong không gian xét hệ tọa độ $Oxyz$ có một đơn vị dài trên các trục tương ứng với $10\text{{ mét}}$ trên thực tế. Một mục tiêu cần được bảo vệ có vị trí ở gốc tọa độ $O$. Người ta thiết lập một vành đai bảo vệ quanh mục tiêu theo một đường tròn tâm $O$ có bán kính bằng ${R_unit}$ đơn vị (tương ứng ${R_meter}\text{{ mét}}$ trên thực tế) nằm trong mặt phẳng $(Oxy)$. Một máy bay không người lái (được coi như một hạt) bay theo một đường thẳng từ vị trí $M({xM}; {yM}; {zM})$ đến vị trí $N({xN}; {yN}; {zN})$. Tại mỗi vị trí của máy bay, khoảng cách từ máy bay đến vành đai bảo vệ là độ dài ngắn nhất của các đoạn thẳng nối từ vị trí đó đến một điểm bất kì trên vành đai.'''

    items = [
        (
            fr'''$\overrightarrow{{MN}} = ({vec_MN[0]}; {vec_MN[1]}; {vec_MN[2]})$.''',
            fr'''$\overrightarrow{{MN}} = ({-vec_MN[0]}; {vec_MN[1]}; {vec_MN[2]})$.''',
            fr'''$\overrightarrow{{MN}} = ({xN} - {xM}; {yN} - {yM}; {zN} - {zM}) = ({vec_MN[0]}; {vec_MN[1]}; {vec_MN[2]})$.''',
            fr'''$\overrightarrow{{MN}} = ({vec_MN[0]}; {vec_MN[1]}; {vec_MN[2]}) \ne ({-vec_MN[0]}; {vec_MN[1]}; {vec_MN[2]})$.'''
        ),
        (
            fr'''Phương trình tham số của đường thẳng $MN$ là $\begin{{cases}} x = {xM} {f'+ {ux}' if ux > 0 else f'- {abs(ux)}'}t \\ y = {yM} {f'+ {uy}' if uy > 0 else f'- {abs(uy)}'}t \\ z = {zM} \end{{cases}}$ với $t \in \mathbb{{R}}$.''',
            fr'''Phương trình tham số của đường thẳng $MN$ là $\begin{{cases}} x = {xM} {f'+ {ux}' if ux > 0 else f'- {abs(ux)}'}t \\ y = {yM} {f'+ {uy}' if uy > 0 else f'- {abs(uy)}'}t \\ z = 0 \end{{cases}}$ với $t \in \mathbb{{R}}$.''',
            fr'''Đường thẳng $MN$ đi qua điểm $M({xM}; {yM}; {zM})$ và nhận vectơ $\vec{{u}} = ({ux}; {uy}; {uz})$ làm vectơ chỉ phương nên có phương trình tham số $\begin{{cases}} x = {xM} {f'+ {ux}' if ux > 0 else f'- {abs(ux)}'}t \\ y = {yM} {f'+ {uy}' if uy > 0 else f'- {abs(uy)}'}t \\ z = {zM} \end{{cases}}$.''',
            fr'''Phương trình tham số của $MN$ phải có $z = {zM}$ (cao độ không đổi), phương trình đưa ra có $z = 0$ là sai.'''
        ),
        (
            fr'''Trong quá trình bay từ $M$ đến $N$, khoảng cách ngắn nhất từ máy bay đến vành đai bảo vệ là ${d_min_meter}\text{{ mét}}$.''',
            fr'''Trong quá trình bay từ $M$ đến $N$, khoảng cách ngắn nhất từ máy bay đến vành đai bảo vệ là ${d_min_meter + 50}\text{{ mét}}$.''',
            fr'''Vành đai bảo vệ là đường tròn $(C)$ trong $(Oxy)$ có bán kính $R = {R_unit}$. Với điểm trên quỹ đạo bay $MN$, khoảng cách hình chiếu xuống $(Oxy)$ đến gốc $O$ ngắn nhất là $OP' = {d0}$ (đạt được tại $t={t_min}$). Khoảng cách ngắn nhất từ $P'$ đến đường tròn là ${d0} - {R_unit} = {d_circ_min}$ đơn vị. Khi đó khoảng cách trong không gian là $d = 10 \cdot \sqrt{{{d_circ_min}^2 + {h_unit}^2}} = {d_min_meter}\text{{ mét}}$.''',
            fr'''Khoảng cách ngắn nhất tính được là ${d_min_meter}\text{{ mét}} \ne {d_min_meter + 50}\text{{ mét}}$.'''
        ),
        (
            fr'''Trong quá trình bay từ $M$ đến $N$, khoảng cách từ máy bay đến vành đai bảo vệ là ngắn nhất khi máy bay ở vị trí có tọa độ là $({xP}; {yP}; {zP})$.''',
            fr'''Trong quá trình bay từ $M$ đến $N$, khoảng cách từ máy bay đến vành đai bảo vệ là ngắn nhất khi máy bay ở vị trí có tọa độ là $({xM}; {yM}; {zM})$.''',
            fr'''Khoảng cách ngắn nhất đạt được khi $t = {t_min}$. Thay $t = {t_min}$ vào phương trình tham số ta được tọa độ của máy bay là $({xP}; {yP}; {zP})$.''',
            fr'''Khoảng cách ngắn nhất đạt được tại $t = {t_min}$ tương ứng vị trí $({xP}; {yP}; {zP})$, không phải tại điểm xuất phát $({xM}; {yM}; {zM})$.'''
        )
    ]
    choices, loi_giai = make_tf_choices(items)
    return caudan, choices, loi_giai


def DeThiThu02_TF_Cau2():
    # TF 2: Khảo sát hàm số bậc ba ngẫu nhiên hóa phong phú với số cực đẹp
    pairs = [
        (1, 3), (-1, 3), (3, 5), (0, 6), (2, 4), (1, 5), (-3, 3)
    ]
    x1, x2 = random.choice(pairs)
    s = x1 + x2
    p = x1 * x2
    s_half = s // 2
    
    d = random.randint(4, 10)
    
    # f'(x) = x^2 - s*x + p
    # f(x) = 1/3 x^3 - (s/2) x^2 + p*x + d
    def f_val(x):
        return Fraction(x**3, 3) - Fraction(s_half * x**2, 1) + Fraction(p * x, 1) + Fraction(d, 1)
        
    y1 = f_val(x1)
    y2 = f_val(x2)
    
    def fmt_frac(frac):
        if frac.denominator == 1:
            return str(frac.numerator)
        return fr"\dfrac{{{frac.numerator}}}{{{frac.denominator}}}"

    s_str = f"- {s}x" if s > 0 else (f"+ {abs(s)}x" if s < 0 else "")
    p_str = f"+ {p}" if p > 0 else (f"- {abs(p)}" if p < 0 else "")
    s2_str = f"- {s_half}x^2" if s_half > 0 else (f"+ {abs(s_half)}x^2" if s_half < 0 else "")
    px_str = f"+ {p}x" if p > 0 else (f"- {abs(p)}x" if p < 0 else "")

    caudan = fr'''Cho hàm số $f(x) = \dfrac{{1}}{{3}}x^3 {s2_str} {px_str} + {d}$.'''

    items = [
        (
            fr'''Đạo hàm của hàm số đã cho là $f'(x) = x^2 {s_str} {p_str}$.''',
            fr'''Đạo hàm của hàm số đã cho là $f'(x) = x^2 {s2_str} {p_str}$.''',
            fr'''Ta có $f'(x) = 3 \cdot \dfrac{{1}}{{3}}x^2 - 2 \cdot {s_half}x + {p} = x^2 {s_str} {p_str}$.''',
            fr'''Đạo hàm đúng là $f'(x) = x^2 {s_str} {p_str}$.'''
        ),
        (
            fr'''Phương trình $f'(x) = 0$ có tập nghiệm là $S = \{{{x1}; {x2}\}}$.''',
            fr'''Phương trình $f'(x) = 0$ có tập nghiệm là $S = \{{{-x1}; {-x2}\}}$.''',
            fr'''$f'(x) = 0 \iff (x - {x1})(x - {x2}) = 0 \iff x = {x1}$ hoặc $x = {x2}$. Vậy $S = \{{{x1}; {x2}\}}$.''',
            fr'''Phương trình có hai nghiệm là $x = {x1}, x = {x2}$, do đó $S = \{{{x1}; {x2}\}}$.'''
        ),
        (
            fr'''Hàm số đã cho nghịch biến trên khoảng $({x1}; {x2})$.''',
            fr'''Hàm số đã cho đồng biến trên khoảng $({x1}; {x2})$.''',
            fr'''Ta có hệ số $a = \dfrac{{1}}{{3}} > 0$ nên trong khoảng hai nghiệm $({x1}; {x2})$ thì $f'(x) < 0$, suy ra hàm số nghịch biến trên khoảng $({x1}; {x2})$.''',
            fr'''Trên khoảng $({x1}; {x2})$, $f'(x) < 0$ nên hàm số nghịch biến chứ không đồng biến.'''
        ),
        (
            fr'''Giá trị cực tiểu của hàm số đã cho bằng ${fmt_frac(y2)}$.''',
            fr'''Giá trị cực tiểu của hàm số đã cho bằng ${fmt_frac(y1)}$.''',
            fr'''Đạo hàm đổi dấu từ âm sang dương khi qua $x = {x2}$ nên hàm số đạt cực tiểu tại $x = {x2}$ với giá trị cực tiểu $f({x2}) = {fmt_frac(y2)}$.''',
            fr'''Hàm số đạt cực tiểu tại $x = {x2}$ với $f({x2}) = {fmt_frac(y2)} \ne {fmt_frac(y1)}$ (đây là giá trị cực đại tại $x = {x1}$).'''
        )
    ]
    choices, loi_giai = make_tf_choices(items)
    return caudan, choices, loi_giai


def DeThiThu02_TF_Cau3():
    # TF 3: Pin năng lượng mặt trời ngẫu nhiên hóa tham số
    # a_pool = [0.12, 0.15, 0.18, 0.21, 0.24, 0.30]
    cases = [
        {"a": 0.12, "b": 1.44, "a3": 0.04, "b2": 0.72},
        {"a": 0.15, "b": 1.80, "a3": 0.05, "b2": 0.90},
        {"a": 0.18, "b": 2.16, "a3": 0.06, "b2": 1.08},
        {"a": 0.21, "b": 2.52, "a3": 0.07, "b2": 1.26},
        {"a": 0.24, "b": 2.88, "a3": 0.08, "b2": 1.44},
        {"a": 0.30, "b": 3.60, "a3": 0.10, "b2": 1.80},
    ]
    c = random.choice(cases)
    a_val = c["a"]
    b_val = c["b"]
    a3 = c["a3"]
    b2 = c["b2"]
    
    def F_t(t):
        return -a3 * (t**3) + b2 * (t**2)
        
    dW1 = round(F_t(5) - F_t(1), 2)
    dW2 = round(F_t(9) - F_t(1), 2)

    a_str = str(a_val).replace('.', ',')
    b_str = str(b_val).replace('.', ',')
    a3_str = str(a3).replace('.', ',')
    b2_str = str(b2).replace('.', ',')
    dW1_str = str(dW1).replace('.', ',')
    dW2_str = str(dW2).replace('.', ',')

    caudan = fr'''Một hệ thống pin năng lượng mặt trời gồm các tấm pin được kết nối với một bộ lưu trữ điện. Trong thời gian mặt trời chiếu sáng của một ngày, năng lượng điện thu được từ các tấm pin được lưu trong bộ lưu trữ điện. Gọi $F(t)$ là năng lượng điện (kWh) lưu trữ được kể từ thời điểm hệ thống bắt đầu hoạt động đến thời điểm $t$, trong đó $t$ là thời gian tính theo giờ ($0 \le t \le 12$) và thời điểm hệ thống bắt đầu hoạt động ứng với $t=0$. Biết rằng $F(0)=0$.
Tốc độ lưu trữ năng lượng điện (kW) của hệ thống này là hàm số $f(t) = F'(t)$ với $0 \le t \le 12$. Số liệu ghi nhận được ở một ngày cụ thể trong năm cho thấy $f(t) = -{a_str}t^2 + {b_str}t$ với $0 \le t \le 12$.'''

    items = [
        (
            fr'''$F(t) = -{a3_str}t^3 + {b2_str}t^2$ với $0 \le t \le 12$.''',
            fr'''$F(t) = -{a_str}t^3 + {b_str}t^2$ với $0 \le t \le 12$.''',
            fr'''$F(t) = \displaystyle\int f(t)\,\mathrm{{d}}t = \displaystyle\int (-{a_str}t^2 + {b_str}t)\,\mathrm{{d}}t = -{a3_str}t^3 + {b2_str}t^2 + C$. Do $F(0) = 0 \implies C = 0$, vậy $F(t) = -{a3_str}t^3 + {b2_str}t^2$.''',
            fr'''Nguyên hàm của $-{a_str}t^2$ là $-\dfrac{{{a_str}}}{{3}}t^3 = -{a3_str}t^3$, do đó biểu thức đúng là $F(t) = -{a3_str}t^3 + {b2_str}t^2$.'''
        ),
        (
            r'''Năng lượng điện (kWh) lưu trữ được kể từ thời điểm $t=a$ đến thời điểm $t=b$ ($0 \le a < b \le 12$) là $\displaystyle\int\limits_{a}^{b} f(t)\,\mathrm{d}t$.''',
            r'''Năng lượng điện (kWh) lưu trữ được kể từ thời điểm $t=a$ đến thời điểm $t=b$ ($0 \le a < b \le 12$) là $f(b) - f(a)$.''',
            r'''Theo định nghĩa tích phân, năng lượng tích lũy từ thời điểm $a$ đến $b$ là phần diện tích dưới đồ thị hàm tốc độ $f(t)$, tức bằng $F(b) - F(a) = \displaystyle\int\limits_{a}^{b} f(t)\,\mathrm{d}t$.''',
            r'''Năng lượng lưu trữ được tính bằng tích phân của hàm tốc độ $\displaystyle\int\limits_{a}^{b} f(t)\,\mathrm{d}t$, không phải hiệu vận tốc $f(b) - f(a)$.'''
        ),
        (
            fr'''Năng lượng điện lưu trữ được kể từ thời điểm $t=1$ đến thời điểm $t=5$ bằng ${dW1_str}\text{{ kWh}}$.''',
            fr'''Năng lượng điện lưu trữ được kể từ thời điểm $t=1$ đến thời điểm $t=5$ lớn hơn ${round(dW1 + 10, 1)}\text{{ kWh}}$.''',
            fr'''$\Delta W_1 = F(5) - F(1) = [-{a3_str}(5)^3 + {b2_str}(5)^2] - [-{a3_str}(1)^3 + {b2_str}(1)^2] = {dW1_str}\text{{ kWh}}$.''',
            fr'''Ta tính được $\Delta W_1 = {dW1_str}\text{{ kWh}} \ne {round(dW1 + 10, 1)}\text{{ kWh}}$.'''
        ),
        (
            fr'''Năng lượng điện lưu trữ được kể từ thời điểm $t=1$ đến thời điểm $t=9$ lớn hơn hai lần năng lượng điện lưu trữ được kể từ thời điểm $t=1$ đến thời điểm $t=5$.''',
            fr'''Năng lượng điện lưu trữ được kể từ thời điểm $t=1$ đến thời điểm $t=9$ gấp hai lần năng lượng điện lưu trữ được kể từ thời điểm $t=1$ đến thời điểm $t=5$.''',
            fr'''$\Delta W_2 = F(9) - F(1) = {dW2_str}\text{{ kWh}}$. Vì ${dW2_str} > 2 \times {dW1_str} = {round(2*dW1, 2)}$ nên $\Delta W_2 > 2\Delta W_1$.''',
            fr'''$\Delta W_2 = {dW2_str}\text{{ kWh}} \ne 2 \times {dW1_str}\text{{ kWh}}$, khẳng định gấp hai lần là sai.'''
        )
    ]
    choices, loi_giai = make_tf_choices(items)
    return caudan, choices, loi_giai


def DeThiThu02_TF_Cau4():
    # TF 4: AI sàng lọc bệnh y tế ngẫu nhiên hóa
    datasets = [
        {"total": 10000, "warn": 1000, "warn_sick": 600, "warn_nosick": 400, "nowarn_sick": 200, "nowarn_nosick": 8800},
        {"total": 10000, "warn": 1000, "warn_sick": 700, "warn_nosick": 300, "nowarn_sick": 100, "nowarn_nosick": 8900},
        {"total": 10000, "warn": 1200, "warn_sick": 800, "warn_nosick": 400, "nowarn_sick": 200, "nowarn_nosick": 8600},
        {"total": 10000, "warn": 1500, "warn_sick": 900, "warn_nosick": 600, "nowarn_sick": 170, "nowarn_nosick": 8330},
        {"total": 10000, "warn": 800,  "warn_sick": 600, "warn_nosick": 200, "nowarn_sick": 200, "nowarn_nosick": 9000},
    ]
    ds = random.choice(datasets)
    n_tot = ds["total"]
    n_w = ds["warn"]
    n_nw = n_tot - n_w
    n_w_s = ds["warn_sick"]
    n_w_ns = ds["warn_nosick"]
    n_nw_s = ds["nowarn_sick"]
    n_nw_ns = ds["nowarn_nosick"]
    
    total_nosick = n_w_ns + n_nw_ns
    p_nw = n_nw / n_tot
    p_nosick_given_nw = round(n_nw_ns / n_nw, 3)
    p_nosick = round(total_nosick / n_tot, 2)
    p_nw_given_nosick = round(n_nw_ns / total_nosick, 3)

    caudan = fr'''Nhằm đưa ra cảnh báo sớm về tình trạng sức khỏe của cư dân, người ta sử dụng một ứng dụng trí tuệ nhân tạo để sàng lọc nguy cơ mắc bệnh dựa trên hồ sơ y tế được lưu trữ. Khi phát hiện nguy cơ mắc bệnh, ứng dụng này sẽ gửi cảnh báo để giúp người dân đi khám bệnh kịp thời. Người ta dùng ứng dụng này để tầm soát nguy cơ mắc một loại bệnh.
Kết quả thu được khi quét thử nghiệm hồ sơ y tế của ${n_tot}$ người như sau: Có ${n_w}$ người nhận được cảnh báo và ${n_nw}$ người còn lại không nhận được cảnh báo từ ứng dụng. Trong số ${n_w}$ người nhận được cảnh báo thì có ${n_w_s}$ người có bệnh và ${n_w_ns}$ người không có bệnh. Trong số ${n_nw}$ người không nhận được cảnh báo thì có ${n_nw_s}$ người có bệnh và ${n_nw_ns}$ người không có bệnh.
Chọn ngẫu nhiên một người trong số ${n_tot}$ người nói trên.'''

    items = [
        (
            fr'''Xác suất để người đó không nhận được cảnh báo từ ứng dụng bằng ${p_nw:.2f}$.''',
            fr'''Xác suất để người đó không nhận được cảnh báo từ ứng dụng bằng ${round(p_nw - 0.05, 2)}$.''',
            fr'''Số người không nhận cảnh báo là ${n_nw}$ trên tổng số ${n_tot}$ người. Vậy $P(\text{{không cảnh báo}}) = \dfrac{{{n_nw}}}{{{n_tot}}} = {p_nw:.2f}$.''',
            fr'''$P(\text{{không cảnh báo}}) = \dfrac{{{n_nw}}}{{{n_tot}}} = {p_nw:.2f} \ne {round(p_nw - 0.05, 2)}$.'''
        ),
        (
            fr'''Xác suất để người đó không có bệnh, biết rằng người đó không nhận được cảnh báo từ ứng dụng, lớn hơn $0,95$.''',
            fr'''Xác suất để người đó không có bệnh, biết rằng người đó không nhận được cảnh báo từ ứng dụng, nhỏ hơn $0,80$.''',
            fr'''Trong số ${n_nw}$ người không nhận cảnh báo có ${n_nw_ns}$ người không có bệnh. Vậy $P(\text{{không bệnh}} \mid \text{{không cảnh báo}}) = \dfrac{{{n_nw_ns}}}{{{n_nw}}} \approx {p_nosick_given_nw} > 0,95$.''',
            fr'''$P(\text{{không bệnh}} \mid \text{{không cảnh báo}}) = \dfrac{{{n_nw_ns}}}{{{n_nw}}} \approx {p_nosick_given_nw} > 0,95$, khẳng định nhỏ hơn $0,80$ là sai.'''
        ),
        (
            fr'''Xác suất để người đó không có bệnh bằng ${p_nosick:.2f}$.''',
            fr'''Xác suất để người đó không có bệnh bằng ${round(p_nosick - 0.08, 2)}$.''',
            fr'''Tổng số người không có bệnh là ${n_w_ns} + {n_nw_ns} = ${total_nosick}$. Vậy xác suất một người không có bệnh là $P(\text{{không bệnh}}) = \dfrac{{{total_nosick}}}{{{n_tot}}} = ${p_nosick:.2f}$.''',
            fr'''Tổng số người không có bệnh là ${total_nosick}$ người, xác suất là $\dfrac{{{total_nosick}}}{{{n_tot}}} = ${p_nosick:.2f} \ne ${round(p_nosick - 0.08, 2)}$.'''
        ),
        (
            fr'''Xác suất để người đó không nhận được cảnh báo từ ứng dụng, biết rằng người đó không có bệnh, lớn hơn $0,90$.''',
            fr'''Xác suất để người đó không nhận được cảnh báo từ ứng dụng, biết rằng người đó không có bệnh, nhỏ hơn $0,70$.''',
            fr'''Trong tổng số ${total_nosick}$ người không có bệnh có ${n_nw_ns}$ người không nhận cảnh báo. Vậy $P(\text{{không cảnh báo}} \mid \text{{không bệnh}}) = \dfrac{{{n_nw_ns}}}{{{total_nosick}}} \approx {p_nw_given_nosick} > 0,90$.''',
            fr'''$P(\text{{không cảnh báo}} \mid \text{{không bệnh}}) = \dfrac{{{n_nw_ns}}}{{{total_nosick}}} \approx {p_nw_given_nosick} > 0,90$, khẳng định nhỏ hơn $0,70$ là sai.'''
        )
    ]
    choices, loi_giai = make_tf_choices(items)
    return caudan, choices, loi_giai

