# -*- coding: utf-8 -*-
import random
import math
from fractions import Fraction
from cuoi_chuong_tf import make_tf_choices

# ==============================================================================
# PHẦN I: 12 CÂU TRẮC NGHIỆM NHIỀU LỰA CHỌN (MC)
# ==============================================================================

def CuoiChuong_DeTongHop_MC_Cau1():
    # Câu 1: Phương trình sin x = 0 (hoặc cos x = 0, sin x = 1, cos x = 1...)
    mode = random.choice(["sin0", "cos0", "sin1", "cos1"])
    if mode == "sin0":
        caudan = r'''Phương trình $\sin x = 0$ có tập nghiệm là'''
        correct = r'''{\True $S=\{k\pi \mid k\in\mathbb{Z}\}$}'''
        w1 = r'''{$S=\left\{-\dfrac{\pi}{2}+k2\pi \mid k\in\mathbb{Z}\right\}$}'''
        w2 = r'''{$S=\{k2\pi \mid k\in\mathbb{Z}\}$}'''
        w3 = r'''{$S=\left\{\dfrac{\pi}{2}+k2\pi \mid k\in\mathbb{Z}\right\}$}'''
        loi_giai = r'''Ta có phương trình lượng giác cơ bản:
$$\sin x = 0 \Leftrightarrow x = k\pi \quad (k\in\mathbb{Z})$$
Vậy tập nghiệm của phương trình là $S=\{k\pi \mid k\in\mathbb{Z}\}$.'''
    elif mode == "cos0":
        caudan = r'''Phương trình $\cos x = 0$ có tập nghiệm là'''
        correct = r'''{\True $S=\left\{\dfrac{\pi}{2}+k\pi \mid k\in\mathbb{Z}\right\}$}'''
        w1 = r'''{$S=\{k\pi \mid k\in\mathbb{Z}\}$}'''
        w2 = r'''{$S=\{k2\pi \mid k\in\mathbb{Z}\}$}'''
        w3 = r'''{$S=\left\{\dfrac{\pi}{2}+k2\pi \mid k\in\mathbb{Z}\right\}$}'''
        loi_giai = r'''Ta có phương trình lượng giác cơ bản:
$$\cos x = 0 \Leftrightarrow x = \dfrac{\pi}{2} + k\pi \quad (k\in\mathbb{Z})$$
Vậy tập nghiệm của phương trình là $S=\left\{\dfrac{\pi}{2}+k\pi \mid k\in\mathbb{Z}\right\}$.'''
    elif mode == "sin1":
        caudan = r'''Phương trình $\sin x = 1$ có tập nghiệm là'''
        correct = r'''{\True $S=\left\{\dfrac{\pi}{2}+k2\pi \mid k\in\mathbb{Z}\right\}$}'''
        w1 = r'''{$S=\{k\pi \mid k\in\mathbb{Z}\}$}'''
        w2 = r'''{$S=\left\{\dfrac{\pi}{2}+k\pi \mid k\in\mathbb{Z}\right\}$}'''
        w3 = r'''{$S=\{k2\pi \mid k\in\mathbb{Z}\}$}'''
        loi_giai = r'''Ta có phương trình lượng giác cơ bản:
$$\sin x = 1 \Leftrightarrow x = \dfrac{\pi}{2} + k2\pi \quad (k\in\mathbb{Z})$$
Vậy tập nghiệm của phương trình là $S=\left\{\dfrac{\pi}{2}+k2\pi \mid k\in\mathbb{Z}\right\}$.'''
    else:
        caudan = r'''Phương trình $\cos x = 1$ có tập nghiệm là'''
        correct = r'''{\True $S=\{k2\pi \mid k\in\mathbb{Z}\}$}'''
        w1 = r'''{$S=\{k\pi \mid k\in\mathbb{Z}\}$}'''
        w2 = r'''{$S=\left\{\dfrac{\pi}{2}+k2\pi \mid k\in\mathbb{Z}\right\}$}'''
        w3 = r'''{$S=\left\{\pi+k2\pi \mid k\in\mathbb{Z}\right\}$}'''
        loi_giai = r'''Ta có phương trình lượng giác cơ bản:
$$\cos x = 1 \Leftrightarrow x = k2\pi \quad (k\in\mathbb{Z})$$
Vậy tập nghiệm của phương trình là $S=\{k2\pi \mid k\in\mathbb{Z}\}$.'''

    choices = [correct, w1, w2, w3]
    random.shuffle(choices)
    choices = [f"{c}\n" for c in choices]
    return caudan, choices, loi_giai


def CuoiChuong_DeTongHop_MC_Cau2():
    # Câu 2: Thống kê: Bảng số liệu ghép nhóm mức lương, khoảng biến thiên R
    a0 = random.choice([4, 5, 6, 7])
    step = random.choice([1, 2])
    k_groups = random.choice([5, 6])
    ak = a0 + k_groups * step
    R = ak - a0

    # Sinh các tần số
    n_list = [random.randint(2, 6) for _ in range(k_groups)]
    total_n = sum(n_list)

    headers = [f"[{a0 + i*step};{a0 + (i+1)*step})" for i in range(k_groups)]
    table_cols = "c|" * (k_groups + 1)
    header_str = " & ".join(headers)
    freq_str = " & ".join(str(x) for x in n_list)

    caudan = fr'''Sau khi khảo sát về mức lương khởi điểm (đơn vị: triệu đồng) của ${total_n}$ công nhân, người ta thu được mẫu số liệu ghép nhóm như sau.
\begin{{center}}
\begin{{tabular}}{{|c|{table_cols[:-1]}}}
\hline
\textbf{{Mức lương}} & {header_str} \\
\hline
\textbf{{Tần số}} & {freq_str} \\
\hline
\end{{tabular}}
\end{{center}}
Khoảng biến thiên của mẫu số liệu ghép nhóm đó bằng'''

    correct = fr'''{{\True ${R}$}}'''
    w1 = fr'''{{${step}$}}'''
    w2 = fr'''{{${round(R + random.choice([1.2, 1.5, -1.3]), 2)}$}}'''
    w3 = fr'''{{${round(R / 2 + 0.5, 2)}$}}'''

    choices = [correct, w1, w2, w3]
    random.shuffle(choices)
    choices = [f"{c}\n" for c in choices]

    loi_giai = fr'''Dựa vào bảng số liệu ghép nhóm, ta thấy:
\begin{{itemize}}
    \item Đầu mút trái của nhóm chứa giá trị nhỏ nhất (nhóm đầu tiên) là $a_1 = {a0}$.
    \item Đầu mút phải của nhóm chứa giá trị lớn nhất (nhóm cuối cùng) là $a_{{{k_groups}}} = {ak}$.
\end{{itemize}}
Vậy khoảng biến thiên của mẫu số liệu ghép nhóm trên là:
$$R = {ak} - {a0} = {R}.$$'''
    return caudan, choices, loi_giai


def CuoiChuong_DeTongHop_MC_Cau3():
    # Câu 3: PT đường thẳng qua A(x0, y0, z0) có VTCP u = (a, b, c)
    x0 = random.randint(-4, 4)
    y0 = random.randint(-4, 4)
    z0 = random.randint(-5, 5)
    while x0 == 0: x0 = 1
    while y0 == 0: y0 = 3
    while z0 == 0: z0 = -5

    a = random.choice([-3, -2, -1, 1, 2, 3])
    b = random.choice([-3, -2, -1, 1, 2, 3])
    c = random.choice([-3, -2, -1, 1, 2, 3])
    while b == a: b = random.choice([-4, 4])

    def fmt_num(val):
        if val > 0: return f"-{val}"
        elif val < 0: return f"+{abs(val)}"
        else: return ""

    correct = fr'''{{\True $\dfrac{{x{fmt_num(x0)}}}{{{a}}} = \dfrac{{y{fmt_num(y0)}}}{{{b}}} = \dfrac{{z{fmt_num(z0)}}}{{{c}}}$}}'''
    w1 = fr'''{{$\dfrac{{x{fmt_num(-x0)}}}{{{a}}} = \dfrac{{y{fmt_num(y0)}}}{{{b}}} = \dfrac{{z{fmt_num(z0)}}}{{{c}}}$}}'''
    w2 = fr'''{{$\dfrac{{x{fmt_num(x0)}}}{{{a}}} = \dfrac{{y{fmt_num(-y0)}}}{{{b}}} = \dfrac{{z{fmt_num(z0)}}}{{{c}}}$}}'''
    w3 = fr'''{{$\dfrac{{x{fmt_num(x0)}}}{{{a}}} = \dfrac{{y{fmt_num(y0)}}}{{{b}}} = \dfrac{{z{fmt_num(-z0)}}}{{{c}}}$}}'''

    caudan = fr'''Trong không gian với hệ tọa độ $Oxyz$, phương trình của đường thẳng đi qua điểm $A({x0};{y0};{z0})$ và có một vectơ chỉ phương $\overrightarrow{{u}} = ({a};{b};{c})$ là'''

    choices = [correct, w1, w2, w3]
    random.shuffle(choices)
    choices = [f"{c}\n" for c in choices]

    loi_giai = fr'''Phương trình chính tắc của đường thẳng đi qua điểm $M(x_0;y_0;z_0)$ và có vectơ chỉ phương $\overrightarrow{{u}}=(a;b;c)$ (với $a,b,c \neq 0$) là:
$$\dfrac{{x-x_0}}{{a}} = \dfrac{{y-y_0}}{{b}} = \dfrac{{z-z_0}}{{c}}$$
Áp dụng với điểm $A({x0};{y0};{z0})$ và vectơ chỉ phương $\overrightarrow{{u}} = ({a};{b};{c})$, ta được phương trình đường thẳng là:
$$\dfrac{{x{fmt_num(x0)}}}{{{a}}} = \dfrac{{y{fmt_num(y0)}}}{{{b}}} = \dfrac{{z{fmt_num(z0)}}}{{{c}}}$$'''
    return caudan, choices, loi_giai


def CuoiChuong_DeTongHop_MC_Cau4():
    # Câu 4: Tích phân Newton-Leibniz: F(b) - F(a)
    a = random.choice([0, 1, 2])
    b = a + random.choice([1, 2])
    Fa = random.randint(1, 5)
    Fb = Fa + random.choice([3, 4, 5, 6, 7])
    ans = Fb - Fa

    caudan = fr'''Cho hàm số $f(x)$ liên tục trên $\mathbb{{R}}$ có một nguyên hàm là $F(x)$ thỏa mãn $F({a})={Fa}, F({b})={Fb}$. Phát biểu nào sau đây là đúng?'''

    correct = fr'''{{\True $\displaystyle\int\limits_{{{a}}}^{{{b}}} f(x)\mathrm{{d}}x = {ans}$}}'''
    w1 = fr'''{{$\displaystyle\int\limits_{{{a}}}^{{{b}}} f(x)\mathrm{{d}}x = {Fa + Fb}$}}'''
    w2 = fr'''{{$\displaystyle\int\limits_{{{a}}}^{{{b}}} f(x)\mathrm{{d}}x = {ans + random.choice([-2, 2])}$}}'''
    w3 = fr'''{{$\displaystyle\int\limits_{{{a}}}^{{{b}}} f(x)\mathrm{{d}}x = {Fa * Fb}$}}'''

    choices = [correct, w1, w2, w3]
    random.shuffle(choices)
    choices = [f"{c}\n" for c in choices]

    loi_giai = fr'''Theo công thức Newton - Leibniz, ta có:
$$\displaystyle\int\limits_{{{a}}}^{{{b}}} f(x)\mathrm{{d}}x = F({b}) - F({a}) = {Fb} - {Fa} = {ans}.$$
Vậy phát biểu đúng là $\displaystyle\int\limits_{{{a}}}^{{{b}}} f(x)\mathrm{{d}}x = {ans}$.'''
    return caudan, choices, loi_giai


def CuoiChuong_DeTongHop_MC_Cau5():
    # Câu 5: Đạo hàm hàm phân thức y = (ax + b)/(cx + d)
    c = random.choice([2, 3, 4])
    d = random.choice([1, 2])
    b = random.choice([3, 4, 5])
    bc = b * c

    caudan = fr'''Cho hàm số $y = f(x) = \dfrac{{ax+{b}}}{{{c}x+{d}}}$ (với $a > {bc // d}$). Đạo hàm của hàm số đã cho là'''

    d_str = f"{d}a" if d != 1 else "a"
    correct = fr'''{{\True $y' = \dfrac{{{d_str}-{bc}}}{{({c}x+{d})^2}}$}}'''
    w1 = fr'''{{$y' = \dfrac{{-{d_str}-{bc}}}{{({c}x+{d})^2}}$}}'''
    w2 = fr'''{{$y' = \dfrac{{{d_str}+{bc}}}{{({c}x+{d})^2}}$}}'''
    w3 = fr'''{{$y' = \dfrac{{{bc}-{d_str}}}{{({c}x+{d})^2}}$}}'''

    choices = [correct, w1, w2, w3]
    random.shuffle(choices)
    choices = [f"{c}\n" for c in choices]

    loi_giai = fr'''Ta có hàm số $y = \dfrac{{ax+{b}}}{{{c}x+{d}}}$.
Đạo hàm của hàm số là:
$$y' = \dfrac{{a \cdot {d} - {b} \cdot {c}}}{{({c}x+{d})^2}} = \dfrac{{{d_str}-{bc}}}{{({c}x+{d})^2}}.$$'''
    return caudan, choices, loi_giai


def CuoiChuong_DeTongHop_MC_Cau6():
    # Câu 6: Tính chất nguyên hàm int k f(x)dx = k int f(x)dx ngẫu nhiên hóa
    k = random.choice([2, 3, 5, 7, 8])
    caudan = fr'''Cho hàm số $f(x)$ liên tục trên $\mathbb{{R}}$ và hằng số $k = {k}$ ($k \neq 0$). Phát biểu nào sau đây là đúng?'''

    correct = fr'''{{\True $\displaystyle\int {k}f(x)\mathrm{{d}}x = {k} \displaystyle\int f(x)\mathrm{{d}}x$}}'''
    w1 = fr'''{{$\displaystyle\int {k}f(x)\mathrm{{d}}x = {k} + \displaystyle\int f(x)\mathrm{{d}}x$}}'''
    w2 = fr'''{{$\displaystyle\int {k}f(x)\mathrm{{d}}x = {k} - \displaystyle\int f(x)\mathrm{{d}}x$}}'''
    w3 = fr'''{{$\displaystyle\int {k}f(x)\mathrm{{d}}x = -{k} \displaystyle\int f(x)\mathrm{{d}}x$}}'''

    choices = [correct, w1, w2, w3]
    random.shuffle(choices)
    choices = [f"{c}\n" for c in choices]

    loi_giai = fr'''Theo tính chất cơ bản của nguyên hàm, với hằng số $k \neq 0$, ta có:
$$\displaystyle\int k f(x)\mathrm{{d}}x = k \displaystyle\int f(x)\mathrm{{d}}x$$
Áp dụng với hằng số bằng ${k}$, ta được:
$$\displaystyle\int {k}f(x)\mathrm{{d}}x = {k} \displaystyle\int f(x)\mathrm{{d}}x.$$
Vậy phát biểu đúng là $\displaystyle\int {k}f(x)\mathrm{{d}}x = {k} \displaystyle\int f(x)\mathrm{{d}}x$.'''
    return caudan, choices, loi_giai


def CuoiChuong_DeTongHop_MC_Cau7():
    # Câu 7: Bảng biến thiên hàm bậc ba trên [-1; 2]
    y_left = random.choice([-5, -4, -3])
    y_cd = random.choice([1, 2, 3])
    y_ct = random.choice([-1, 0])
    y_right = random.choice([4, 5, 6, 7])
    max_val = max(y_cd, y_right)

    caudan = fr'''\immini{{Cho hàm số bậc ba $y = f(x)$ có bảng biến thiên trên đoạn $[-1; 2]$ như sau. Giá trị lớn nhất của hàm số đã cho trên đoạn $[-1; 2]$ bằng}}
{{\begin{{tikzpicture}}
\tkzTabInit[lgt=1.5, espcl=2.5]
{{$x$ /0.7, $f'(x)$ / 0.7, $f(x)$ / 2}}
{{$-1$, $0$, $1$, $2$}}
\tkzTabLine{{, +, 0, -, 0, +, }}
\tkzTabVar{{-/ ${y_left}$, +/ ${y_cd}$, -/ ${y_ct}$, +/ ${y_right}$}}
\end{{tikzpicture}}}}'''

    correct = fr'''{{\True ${max_val}$}}'''
    w1 = fr'''{{${y_cd if max_val == y_right else y_right}$}}'''
    w2 = fr'''{{${y_ct}$}}'''
    w3 = fr'''{{${y_left}$}}'''

    choices = [correct, w1, w2, w3]
    random.shuffle(choices)
    choices = [f"{c}\n" for c in choices]

    loi_giai = fr'''Dựa vào bảng biến thiên của hàm số $y=f(x)$ trên đoạn $[-1;2]$, ta thấy:
Giá trị lớn nhất của hàm số trên đoạn $[-1; 2]$ là ${max_val}$ (đạt tại $x = 2$).'''
    return caudan, choices, loi_giai


def CuoiChuong_DeTongHop_MC_Cau8():
    # Câu 8: Mẫu số liệu ghép nhóm số giờ xem TV, tính số trung bình
    n1 = random.choice([15, 20, 25])
    n2 = random.choice([30, 35, 40])
    n3 = random.choice([25, 30, 35])
    n4 = random.choice([10, 12, 15])
    n5 = random.choice([5, 8, 10])
    total_n = n1 + n2 + n3 + n4 + n5

    c1, c2, c3, c4, c5 = 1, 3, 5, 7, 9
    sum_val = c1*n1 + c2*n2 + c3*n3 + c4*n4 + c5*n5
    mean_val = round(sum_val / total_n, 1)

    caudan = fr'''Sau khi khảo sát tổng số giờ xem truyền hình (đơn vị: giờ) của ${total_n}$ gia đình trong hai ngày nghỉ cuối tuần, người ta thu được mẫu số liệu ghép nhóm như sau.
\begin{{center}}
\begin{{tabular}}{{|c|c|c|c|c|c|}}
\hline
\textbf{{Số giờ xem truyền hình}} & $[0;2)$ & $[2;4)$ & $[4;6)$ & $[6;8)$ & $[8;10)$ \\
\hline
\textbf{{Tần số}} & ${n1}$ & ${n2}$ & ${n3}$ & ${n4}$ & ${n5}$ \\
\hline
\end{{tabular}}
\end{{center}}
Giá trị trung bình của mẫu số liệu ghép nhóm đó bằng (làm tròn kết quả đến hàng phần mười)'''

    correct = fr'''{{\True ${str(mean_val).replace(".", ",")}$}}'''
    w1 = fr'''{{${str(round(mean_val + 0.7, 1)).replace(".", ",")}$}}'''
    w2 = fr'''{{${str(round(mean_val - 1.2, 1)).replace(".", ",")}$}}'''
    w3 = fr'''{{${total_n // 10}$}}'''

    choices = [correct, w1, w2, w3]
    random.shuffle(choices)
    choices = [f"{c}\n" for c in choices]

    loi_giai = fr'''Giá trị đại diện cho các nhóm lần lượt là $c_1 = 1, c_2 = 3, c_3 = 5, c_4 = 7, c_5 = 9$.
Giá trị trung bình của mẫu số liệu ghép nhóm là:
$$\bar{{x}} = \dfrac{{1 \cdot {n1} + 3 \cdot {n2} + 5 \cdot {n3} + 7 \cdot {n4} + 9 \cdot {n5}}}{{{total_n}}} = \dfrac{{{sum_val}}}{{{total_n}}} \approx {str(mean_val).replace(".", ",")}.$$'''
    return caudan, choices, loi_giai


def CuoiChuong_DeTongHop_MC_Cau9():
    # Câu 9: Hình hộp ABCD.A'B'C'D', vectơ cùng phương với A'D'
    target_vec = random.choice([r"\overrightarrow{A'D'}", r"\overrightarrow{A'B'}", r"\overrightarrow{AA'}"])
    if target_vec == r"\overrightarrow{A'D'}":
        ans_vec = r"\overrightarrow{AD}"
        opp_side = "ADD'A'"
        par_edge = "A'D' \\parallel AD"
        w_vecs = [r"\overrightarrow{BD}", r"\overrightarrow{AB}", r"\overrightarrow{AC}"]
    elif target_vec == r"\overrightarrow{A'B'}":
        ans_vec = r"\overrightarrow{AB}"
        opp_side = "ABB'A'"
        par_edge = "A'B' \\parallel AB"
        w_vecs = [r"\overrightarrow{AD}", r"\overrightarrow{AC}", r"\overrightarrow{BD}"]
    else:
        ans_vec = r"\overrightarrow{CC'}"
        opp_side = "ACC'A'"
        par_edge = "AA' \\parallel CC'"
        w_vecs = [r"\overrightarrow{AB}", r"\overrightarrow{AD}", r"\overrightarrow{BD}"]

    caudan = fr'''\immini{{Cho hình hộp $ABCD.A'B'C'D'$ (xem hình minh họa bên). Vectơ nào sau đây cùng phương với vectơ ${target_vec}$?}}
{{\begin{{tikzpicture}}[line cap=round, line join=round, thick, scale=0.55]
\coordinate (B) at (0,0);
\coordinate (C) at (4,0);
\coordinate (A) at (1.2,1.2);
\coordinate (D) at ($(A)+(C)-(B)$);
\coordinate (shift) at (0.6,4);
\coordinate (A') at ($(A)+(shift)$);
\coordinate (B') at ($(B)+(shift)$);
\coordinate (C') at ($(C)+(shift)$);
\coordinate (D') at ($(D)+(shift)$);
\draw[dashed] (B) -- (A) -- (D);
\draw[dashed] (A) -- (A');
\draw (B) -- (C) -- (D) -- (D') -- (C') -- (B') -- cycle;
\draw (C) -- (C');
\draw (B') -- (A') -- (D');
\node[left] at (A) {{$A$}};
\node[below left] at (B) {{$B$}};
\node[below right] at (C) {{$C$}};
\node[right] at (D) {{$D$}};
\node[above] at (A') {{$A'$}};
\node[left] at (B') {{$B'$}};
\node[right] at (C') {{$C'$}};
\node[above right] at (D') {{$D'$}};
\end{{tikzpicture}}}}'''

    correct = fr'''{{\True ${ans_vec}$}}'''
    w1 = fr'''{{${w_vecs[0]}$}}'''
    w2 = fr'''{{${w_vecs[1]}$}}'''
    w3 = fr'''{{${w_vecs[2]}$}}'''

    choices = [correct, w1, w2, w3]
    random.shuffle(choices)
    choices = [f"{c}\n" for c in choices]

    loi_giai = fr'''Vì $ABCD.A'B'C'D'$ là hình hộp nên mặt bên ${opp_side}$ là hình bình hành.
Suy ra ${par_edge}$.
Do đó, vectơ ${target_vec}$ cùng phương với vectơ ${ans_vec}$.'''
    return caudan, choices, loi_giai


def CuoiChuong_DeTongHop_MC_Cau10():
    # Câu 10: Cấp số nhân u2 = u1 * q ngẫu nhiên hóa
    m = random.choice([2, 3, 4, 5, 6])
    q_val = random.choice([2, 3, 4])
    n = m * q_val

    caudan = fr'''Cho cấp số nhân $(u_n)$ có công bội $q$ với số hạng đầu $u_1 = {m}$ và số hạng thứ hai $u_2 = {n}$. Mối liên hệ nào sau đây là đúng?'''
    correct = fr'''{{\True ${n} = {m} \cdot q$}}'''
    w1 = fr'''{{${m} = {n} + q$}}'''
    w2 = fr'''{{${m} = {n} \cdot q$}}'''
    w3 = fr'''{{${n} = {m} + q$}}'''

    choices = [correct, w1, w2, w3]
    random.shuffle(choices)
    choices = [f"{c}\n" for c in choices]

    loi_giai = fr'''Theo định nghĩa của cấp số nhân:
$$u_2 = u_1 \cdot q \iff {n} = {m} \cdot q$$
Vậy phát biểu đúng là ${n} = {m} \cdot q$.'''
    return caudan, choices, loi_giai


def CuoiChuong_DeTongHop_MC_Cau11():
    # Câu 11: Hình chóp S.ABCD, SA vuông góc (ABCD) ngẫu nhiên hóa đường thẳng vuông góc mặt phẳng
    mode = random.choice(["BC", "CD"])
    if mode == "BC":
        target_line = "BC"
        ans_plane = "(SAB)"
        wrong_planes = ["(SCD)", "(SBC)", "(SBD)"]
        perp_edge = "AB"
    else:
        target_line = "CD"
        ans_plane = "(SAD)"
        wrong_planes = ["(SBC)", "(SCD)", "(SBD)"]
        perp_edge = "AD"

    caudan = fr'''\immini{{Cho hình chóp $S.ABCD$ có đáy $ABCD$ là hình vuông và $SA$ vuông góc với $(ABCD)$ (xem hình minh họa bên). Đường thẳng ${target_line}$ vuông góc với mặt phẳng nào trong các mặt phẳng sau đây?}}
{{\begin{{tikzpicture}}[line cap=round, line join=round, thick, scale=0.55]
\coordinate (B) at (0,0);
\coordinate (C) at (4.5,0);
\coordinate (A) at (2,1.2);
\coordinate (D) at ($(A)+(C)-(B)$);
\coordinate (S) at (2,4.5);
\draw[dashed] (S) -- (A);
\draw[dashed] (A) -- (B);
\draw[dashed] (A) -- (D);
\draw[dashed] (A) -- (C);
\draw[dashed] (B) -- (D);
\draw (S) -- (B);
\draw (S) -- (C);
\draw (S) -- (D);
\draw (B) -- (C);
\draw (C) -- (D);
\node[above] at (S) {{$S$}};
\node[left] at (A) {{$A$}};
\node[left] at (B) {{$B$}};
\node[right] at (C) {{$C$}};
\node[right] at (D) {{$D$}};
\end{{tikzpicture}}}}'''

    correct = fr'''{{\True ${ans_plane}$}}'''
    w1 = fr'''{{{wrong_planes[0]}}}'''
    w2 = fr'''{{{wrong_planes[1]}}}'''
    w3 = fr'''{{{wrong_planes[2]}}}'''

    choices = [correct, w1, w2, w3]
    random.shuffle(choices)
    choices = [f"{c}\n" for c in choices]

    loi_giai = fr'''Ta có đáy $ABCD$ là hình vuông nên ${target_line} \perp {perp_edge}$. Mặt khác, vì $SA \perp (ABCD)$ nên $SA \perp {target_line}$.
Do $SA$ và ${perp_edge}$ cắt nhau trong mặt phẳng ${ans_plane}$ nên ${target_line} \perp ${ans_plane}$.'''
    return caudan, choices, loi_giai


def CuoiChuong_DeTongHop_MC_Cau12():
    # Câu 12: Nguyên hàm int (a x^2 - cos x) dx = (a/3) x^3 - sin x + C
    coeff = random.choice([3, 6, 9])
    coeff3 = coeff // 3
    caudan = fr'''Nguyên hàm của hàm số $f(x) = {coeff}x^2 - \cos x$ là'''

    c3_str = f"{coeff3}x^3" if coeff3 != 1 else "x^3"
    c2_str = f"{coeff * 2}x"

    correct = fr'''{{\True ${c3_str} - \sin x + C$}}'''
    w1 = fr'''{{${c3_str} + \sin x + C$}}'''
    w2 = fr'''{{${c2_str} + \sin x + C$}}'''
    w3 = fr'''{{${c2_str} - \sin x + C$}}'''

    choices = [correct, w1, w2, w3]
    random.shuffle(choices)
    choices = [f"{c}\n" for c in choices]

    loi_giai = fr'''Ta có:
$$ \displaystyle\int ({coeff}x^2 - \cos x)\,\mathrm{{d}}x = {c3_str} - \sin x + C. $$
Vậy nguyên hàm của hàm số đã cho là ${c3_str} - \sin x + C$.'''
    return caudan, choices, loi_giai


# ==============================================================================
# PHẦN II: 4 CÂU TRẮC NGHIỆM ĐÚNG - SAI (TF)
# ==============================================================================

def CuoiChuong_DeTongHop_TF_Cau1():
    # TF 1: Hàm bậc ba y = a x^3 + b x^2 + c x + d nâng cấp mạnh mẽ với số nguyên cực đẹp
    pairs_even = [
        (-3, -1), (-3, 1), (-2, 0), (-2, 2), (-1, 1), (-1, 3), (0, 2), (0, 4),
        (1, 3), (1, 5), (2, 4), (2, 6), (3, 5), (-4, -2), (-4, 0), (-4, 2)
    ]
    pairs_odd = [
        (-3, 0), (-2, 1), (-1, 0), (-1, 2), (0, 1), (0, 3), (1, 2), (1, 4),
        (2, 3), (2, 5), (3, 4), (-4, -1), (-3, 2), (-2, 3)
    ]
    if random.choice([True, False]):
        x1, x2 = random.choice(pairs_even)
        a = random.choice([1, -1])
    else:
        x1, x2 = random.choice(pairs_odd)
        a = random.choice([2, -2])
        
    d = random.randint(-6, 8)
    
    s = x1 + x2
    p = x1 * x2
    b_coef = -3 * a * s // 2  # Luôn là số nguyên
    c_coef = 3 * a * p
    
    def f(x):
        return a * x**3 + b_coef * x**2 + c_coef * x + d
    
    # Định dạng biểu thức f(x)
    def fmt_poly(a1, b1, c1, d1):
        parts = []
        if a1 == 1: parts.append("x^3")
        elif a1 == -1: parts.append("-x^3")
        else: parts.append(f"{a1}x^3")
        
        if b1 > 0: parts.append(f"+ {b1}x^2" if b1 != 1 else "+ x^2")
        elif b1 < 0: parts.append(f"- {abs(b1)}x^2" if abs(b1) != 1 else "- x^2")
        
        if c1 > 0: parts.append(f"+ {c1}x" if c1 != 1 else "+ x")
        elif c1 < 0: parts.append(f"- {abs(c1)}x" if abs(c1) != 1 else "- x")
        
        if d1 > 0: parts.append(f"+ {d1}")
        elif d1 < 0: parts.append(f"- {abs(d1)}")
        return " ".join(parts)
    
    def fmt_quad(A1, B1, C1):
        parts = []
        if A1 == 1: parts.append("x^2")
        elif A1 == -1: parts.append("-x^2")
        else: parts.append(f"{A1}x^2")
        
        if B1 > 0: parts.append(f"+ {B1}x" if B1 != 1 else "+ x")
        elif B1 < 0: parts.append(f"- {abs(B1)}x" if abs(B1) != 1 else "- x")
        
        if C1 > 0: parts.append(f"+ {C1}")
        elif C1 < 0: parts.append(f"- {abs(C1)}")
        return " ".join(parts)

    poly_str = fmt_poly(a, b_coef, c_coef, d)
    fprime_str = fmt_quad(3 * a, 2 * b_coef, c_coef)
    fprime_wrong = fmt_quad(3 * a, b_coef, c_coef)
    
    caudan = fr'''Cho hàm số $y = f(x) = {poly_str}$.'''
    
    # Cực trị (hoàn toàn là số nguyên)
    y1 = f(x1)
    y2 = f(x2)
    
    # Đường thẳng qua 2 cực trị y = m x + k (hoàn toàn nguyên)
    m = -a * (x2 - x1)**2 // 2
    k = y1 - m * x1
    
    def fmt_line(m1, k1):
        if m1 == 1: res = "x"
        elif m1 == -1: res = "-x"
        else: res = f"{m1}x"
        if k1 > 0: res += f" + {k1}"
        elif k1 < 0: res += f" - {abs(k1)}"
        return res
        
    line_str = fmt_line(m, k)
    line_wrong = fmt_line(m, k - random.choice([3, 4, 5]))
    
    # Đoạn [alpha, beta]
    alpha = x1 + 1
    beta = x2 + 1
    val_alpha = f(alpha)
    val_x2 = f(x2)
    val_beta = f(beta)
    
    vals = [(val_alpha, alpha), (val_x2, x2), (val_beta, beta)]
    if a > 0:
        max_val, max_x = max(vals, key=lambda t: t[0])
        wrong_x = alpha if max_x == beta else beta
    else:
        max_val, max_x = min(vals, key=lambda t: t[0])
        wrong_x = beta if max_x == alpha else alpha

    items = [
        (
            fr'''Đạo hàm của hàm số đã cho là $f'(x) = {fprime_str}$.''',
            fr'''Đạo hàm của hàm số đã cho là $f'(x) = {fprime_wrong}$.''',
            fr'''Ta có $f'(x) = ({poly_str})' = {fprime_str}$.''',
            fr'''Đạo hàm đúng là $f'(x) = {fprime_str} \ne {fprime_wrong}$.'''
        ),
        (
            fr'''Phương trình $f'(x) = 0$ có tập nghiệm là $S = \{{{x1}; {x2}\}}$.''',
            fr'''Phương trình $f'(x) = 0$ có tập nghiệm là $S = \{{{-x1}; {-x2}\}}$.''',
            fr'''$f'(x) = 0 \iff 3a(x - {x1})(x - {x2}) = 0 \iff x = {x1}$ hoặc $x = {x2} \implies S = \{{{x1}; {x2}\}}$.''',
            fr'''Phương trình $f'(x) = 0$ có các nghiệm là $x = {x1}, x = {x2}$.'''
        ),
        (
            fr'''Hàm số đã cho đạt giá trị lớn nhất trên đoạn $[{alpha}; {beta}]$ tại $x = {max_x}$.''',
            fr'''Hàm số đã cho đạt giá trị lớn nhất trên đoạn $[{alpha}; {beta}]$ tại $x = {wrong_x}$.''',
            fr'''Trên đoạn $[{alpha}; {beta}]$, ta có $f({alpha}) = {val_alpha}, f({x2}) = {val_x2}, f({beta}) = {val_beta}$. So sánh các giá trị ta thấy giá trị lớn nhất đạt tại $x = {max_x}$ (với giá trị $f({max_x}) = {max_val}$).''',
            fr'''So sánh các giá trị trên đoạn $[{alpha}; {beta}]$, ta thấy giá trị lớn nhất đạt tại $x = {max_x} \ne {wrong_x}$.'''
        ),
        (
            fr'''Phương trình đường thẳng đi qua hai điểm cực trị của đồ thị hàm số là $y = {line_str}$.''',
            fr'''Phương trình đường thẳng đi qua hai điểm cực trị của đồ thị hàm số là $y = {line_wrong}$.''',
            fr'''Hai điểm cực trị là $M_1({x1}; {y1})$ và $M_2({x2}; {y2})$. Phương trình đường thẳng đi qua hai điểm cực trị là $y = {line_str}$.''',
            fr'''Phương trình đường thẳng qua hai cực trị đúng là $y = {line_str} \ne {line_wrong}$.'''
        )
    ]
    choices, loi_giai = make_tf_choices(items)
    return caudan, choices, loi_giai


def CuoiChuong_DeTongHop_TF_Cau2():
    # TF 2: Bơm nước vào bể theo parabol với số liệu tuyệt đẹp
    scenarios = [
        {"t_max": 3, "k": 1, "a_inv": 2, "h": 4, "t_end": 6, "v_max": 9},     # V(3) = 9 m³ nguyên!
        {"t_max": 3, "k": 1, "a_inv": 1, "h": 8, "t_end": 6, "v_max": 18},    # V(3) = 18 m³ nguyên!
        {"t_max": 3, "k": 2, "a_inv": 1, "h": 5, "t_end": 6, "v_max": 18},    # V(3) = 18 m³ nguyên!
        {"t_max": 4, "k": 2, "a_inv": 4, "h": 3, "t_end": 8, "v_max": 10.7},  # Chuẩn SGK
        {"t_max": 4, "k": 2, "a_inv": 2, "h": 6, "t_end": 8, "v_max": 21.3},  
        {"t_max": 5, "k": 3, "a_inv": 4, "h": 4, "t_end": 10, "v_max": 20.8}, 
        {"t_max": 5, "k": 1, "a_inv": 4, "h": 6, "t_end": 10, "v_max": 20.8}, 
        {"t_max": 6, "k": 2, "a_inv": 6, "h": 5, "t_end": 12, "v_max": 24},   # V(6) = 24 m³ nguyên!
        {"t_max": 6, "k": 4, "a_inv": 4, "h": 5, "t_end": 12, "v_max": 36},   # V(6) = 36 m³ nguyên!
        {"t_max": 6, "k": 3, "a_inv": 3, "h": 9, "t_end": 12, "v_max": 48},   # V(6) = 48 m³ nguyên!
    ]
    sc = random.choice(scenarios)
    t_max = sc["t_max"]
    k = sc["k"]
    t1 = t_max - k
    t2 = t_max + k
    h = sc["h"]
    a_inv = sc["a_inv"]
    t_end = sc["t_end"]
    b_coef = 2 * t_max // a_inv
    
    denom_v = 3 * a_inv
    b_half = b_coef // 2
    v_max = sc["v_max"]

    f_str = f"-\\dfrac{{1}}{{{a_inv}}}t^2 + {b_coef}t" if a_inv != 1 else f"-t^2 + {b_coef}t"
    v_str = f"{b_half}t^2 - \\dfrac{{t^3}}{{{denom_v}}}" if b_half != 1 else f"t^2 - \\dfrac{{t^3}}{{{denom_v}}}"

    caudan = fr'''\immini{{Người ta dùng một thiết bị bơm nước vào một bể không có nước. Tính từ lúc thiết bị bắt đầu hoạt động, tại thời điểm $t$ giờ với $0 \le t \le {t_end}$, thiết bị đó có tốc độ bơm nước vào bể là $f(t)$ ($m^3$/giờ). Biết rằng đồ thị của hàm số $y = f(t)$ là một phần đường parabol đi qua gốc tọa độ $O$ và hai điểm $A({t1};{h}), B({t2};{h})$ (hình bên).}}
{{\begin{{tikzpicture}}[line cap=round, line join=round, >=stealth, font=\footnotesize, scale=0.5]
\draw[->] (-0.8,0) -- ({t_end + 1.2},0) node[above] {{$t$ (giờ)}};
\draw[->] (0,-0.8) -- (0,{h + 2.5}) node[right] {{$y$ ($m^3$/giờ)}};
\node[below left] at (0,0) {{$O$}};
\draw ({t1},2pt) -- ({t1},-2pt) node[below] {{${t1}$}};
\draw ({t2},2pt) -- ({t2},-2pt) node[below] {{${t2}$}};
\draw (2pt,{h}) -- (-2pt,{h}) node[left] {{${h}$}};
\draw[dashed, thin] (0,{h}) -- ({t2},{h});
\draw[dashed, thin] ({t1},0) -- ({t1},{h});
\draw[dashed, thin] ({t2},0) -- ({t2},{h});
\draw[thick, smooth, samples=200, domain=0:{t_end}] plot(\x, {{-\x*\x/{a_inv} + {b_coef}*\x}});
\node[above left=-2pt] at ({t1},{h}) {{$A$}};
\node[above right=-2pt] at ({t2},{h}) {{$B$}};
\node[right] at ({t_end - 0.5}, 1.5) {{$y=f(t)$}};
\end{{tikzpicture}}}}'''

    items = [
        (
            fr'''Với $0 \le t \le {t_end}$ thì tốc độ bơm là $f(t) = {f_str}$ ($m^3$/giờ).''',
            fr'''Với $0 \le t \le {t_end}$ thì tốc độ bơm là $f(t) = {h}t - \dfrac{{t^2}}{{{a_inv + 2}}}$ ($m^3$/giờ).''',
            fr'''$f(t) = at^2 + bt$. Do đi qua $A({t1}; {h})$ và $B({t2}; {h})$, giải hệ phương trình ta được $a = -\dfrac{{1}}{{{a_inv}}}, b = {b_coef}$. Vậy $f(t) = {f_str}$.''',
            fr'''Hàm parabol đúng là $f(t) = {f_str}$.'''
        ),
        (
            fr'''Tại thời điểm $t$ giờ ($0 \le t \le {t_end}$) tính từ lúc bắt đầu hoạt động, lượng nước trong bể là $V(t) = {v_str}$ ($m^3$).''',
            fr'''Tại thời điểm $t$ giờ ($0 \le t \le {t_end}$) tính từ lúc bắt đầu hoạt động, lượng nước trong bể là $V(t) = {b_coef}t - \dfrac{{t^2}}{{{a_inv}}}$ ($m^3$).''',
            fr'''$V(t) = \displaystyle\int\limits_0^t f(x)\,\mathrm{{d}}x = \left.\left(-\dfrac{{x^3}}{{{denom_v}}} + {b_half}x^2\right)\right|_0^t = {v_str}$ ($m^3$).''',
            fr'''Lượng nước là tích phân của tốc độ bơm, biểu thức đúng là $V(t) = {v_str}$.'''
        ),
        (
            fr'''Tại thời điểm thiết bị có tốc độ bơm nước lớn nhất, lượng nước trong bể xấp xỉ ${v_max}$ mét khối.''',
            fr'''Tại thời điểm thiết bị có tốc độ bơm nước lớn nhất, lượng nước trong bể lớn hơn ${v_max + 10}$ mét khối.''',
            fr'''Tốc độ bơm lớn nhất tại đỉnh parabol $t = {t_max}$. Khi đó $V({t_max}) \approx {v_max}\text{{ m}}^3$.''',
            fr'''Tại $t = {t_max}$, lượng nước trong bể là $V({t_max}) \approx {v_max}\text{{ m}}^3 \ne {v_max + 10}\text{{ m}}^3$.'''
        ),
        (
            fr'''Thời điểm thiết bị bơm đạt tốc độ lớn nhất là sau ${t_max}$ giờ kể từ lúc bắt đầu.''',
            fr'''Thời điểm thiết bị bơm đạt tốc độ lớn nhất là sau ${t_end}$ giờ kể từ lúc bắt đầu.''',
            fr'''Hàm số $f(t) = {f_str}$ đạt cực đại tại đỉnh $t = -\dfrac{{b}}{{2a}} = {t_max}$ (giờ).''',
            fr'''Đỉnh parabol có hoành độ $t = {t_max}$ giờ, không phải ${t_end}$ giờ.'''
        )
    ]
    choices, loi_giai = make_tf_choices(items)
    return caudan, choices, loi_giai


def CuoiChuong_DeTongHop_TF_Cau3():
    # TF 3: Không gian Oxyz: Trạm phát sóng mở rộng nhiều bộ số Pytago nguyên đẹp
    pythago = [
        {"z0": 12, "R0": 13, "r": 5},
        {"z0": 5,  "R0": 13, "r": 12},
        {"z0": 8,  "R0": 10, "r": 6},
        {"z0": 6,  "R0": 10, "r": 8},
        {"z0": 15, "R0": 17, "r": 8},
        {"z0": 8,  "R0": 17, "r": 15},
        {"z0": 12, "R0": 15, "r": 9},
        {"z0": 9,  "R0": 15, "r": 12},
        {"z0": 16, "R0": 20, "r": 12},
        {"z0": 20, "R0": 25, "r": 15},
        {"z0": 24, "R0": 26, "r": 10},
    ]
    cfg = random.choice(pythago)
    z0 = cfg["z0"]
    R0 = cfg["R0"]
    r_val = cfg["r"]
    
    x0 = random.choice([-4, -3, -2, -1, 1, 2, 3, 4])
    y0 = random.choice([-4, -3, -2, -1, 1, 2, 3, 4])
    
    R_m = R0 * 10
    r_m = r_val * 10
    h_m = z0 * 10
    R2 = R0**2
    
    caudan = fr'''\immini{{Trong không gian với hệ tọa độ $Oxyz$, một trạm thu phát sóng điện thoại di động được đặt ở vị trí $I({x0};{y0};{z0})$, trong đó một đơn vị độ dài trên mỗi trục tương ứng với $10$ mét trên thực tế. Trạm thu phát sóng đó có bán kính phủ sóng là ${R_m}$ mét. Vùng phủ sóng của trạm thu phát được quy ước là tập hợp tất cả các điểm $P$ trên mặt đất và trong không gian sao cho khoảng cách $IP$ không vượt quá ${R_m}$ mét. Mặt đất được coi là mặt phẳng $(Oxy)$ và mỗi người trên mặt đất được coi như một chất điểm (hình bên).}}
{{\begin{{tikzpicture}}[line cap=round, line join=round, >=stealth, font=\footnotesize,scale=0.5]
\coordinate (H) at (0,0);
\coordinate (I) at (0,4.5);
\coordinate (P) at (2.2,0);
\coordinate (P1) at (-6.5,-1.5);
\coordinate (P2) at (5.5,-1.5);
\coordinate (P3) at (7.5, 2.5);
\coordinate (P4) at (-4.5, 2.5);
\filldraw[fill=green!5, draw=green!50!black, thick] (P1) -- (P2) -- (P3) -- (P4) -- cycle;
\node[below left, green!30!black] at (P3) {{Mặt phẳng $(Oxy)$}};
\draw[dashed, thick, blue] (2.2,0) arc (0:180:2.2cm and 0.6cm);
\draw[thick, blue] (-2.2,0) arc (180:360:2.2cm and 0.6cm);
\draw (0,0.25) -- (0.25,0.25) -- (0.25,0);
\draw[dashed, thick] (H) -- (I) node[midway, left] {{${h_m}\text{{ m}}$}};
\draw[dashed, thick, blue] (H) -- (P) node[midway, below] {{$r={r_m}\text{{ m}}$}};
\draw[dashed, thick, red] (I) -- (P) node[midway, right] {{${R_m}\text{{ m}}$}};
\fill (H) circle (1.5pt) node[below] {{$H$}};
\fill (I) circle (1.5pt) node[right] {{$I({x0};{y0};{z0})$}};
\fill (P) circle (1.5pt) node[right] {{$P$}};
\end{{tikzpicture}}}}'''

    def fmt_sq(val, var):
        if val > 0: return f"({var} - {val})^2"
        elif val < 0: return f"({var} + {abs(val)})^2"
        else: return f"{var}^2"

    sph_str = f"{fmt_sq(x0, 'x')} + {fmt_sq(y0, 'y')} + {fmt_sq(z0, 'z')} = {R2}"

    items = [
        (
            fr'''Vùng phủ sóng của trạm thu phát là một phần của hình cầu giới hạn bởi mặt cầu $(S)$ có phương trình ${sph_str}$.''',
            fr'''Vùng phủ sóng của trạm thu phát là một phần của hình cầu giới hạn bởi mặt cầu $(S)$ có phương trình $(x-1)^2 + (y-1)^2 + z^2 = {R_m}$.''',
            fr'''Tâm $I({x0}; {y0}; {z0})$, bán kính $R = {R_m}\text{{ m}} = {R0}$ đv $\implies R^2 = {R2}$. Phương trình mặt cầu là ${sph_str}$.''',
            fr'''Bán kính theo đơn vị trục tọa độ là $R = {R0}$ nên $R^2 = {R2} \ne {R_m}$.'''
        ),
        (
            fr'''Bán kính vùng phủ sóng trên mặt phẳng $(Oxy)$ bằng ${r_m}\text{{ m}}$.''',
            fr'''Bán kính vùng phủ sóng trên mặt phẳng $(Oxy)$ bằng ${R_m}\text{{ m}}$.''',
            fr'''Hình chiếu tâm lên $(Oxy)$ là $H({x0}; {y0}; 0)$. Bán kính đường tròn trên $(Oxy)$ là $r = \sqrt{{R^2 - d(I, (Oxy))^2}} = \sqrt{{{R0}^2 - {z0}^2}} = {r_val}$ đv $= {r_m}\text{{ m}}$.''',
            fr'''Bán kính trên mặt đất là $r = \sqrt{{R^2 - h^2}} = {r_m}\text{{ m}} \ne {R_m}\text{{ m}}$.'''
        ),
        (
            fr'''Vị trí điểm tâm vùng phủ sóng trên mặt đất là $H({x0}; {y0}; 0)$.''',
            fr'''Vị trí điểm tâm vùng phủ sóng trên mặt đất là $H(0; 0; 0)$.''',
            fr'''Hình chiếu vuông góc của trạm $I({x0}; {y0}; {z0})$ lên mặt phẳng $(Oxy)$ là điểm $H({x0}; {y0}; 0)$.''',
            fr'''Tâm vùng phủ sóng trên mặt đất là hình chiếu của $I$ lên $(Oxy)$, tức $H({x0}; {y0}; 0) \ne (0; 0; 0)$.'''
        ),
        (
            fr'''Khoảng cách từ trạm thu phát $I$ đến mặt đất bằng ${h_m}\text{{ m}}$.''',
            fr'''Khoảng cách từ trạm thu phát $I$ đến mặt đất bằng ${R_m}\text{{ m}}$.''',
            fr'''Khoảng cách từ $I$ đến $(Oxy)$ bằng $|z_I| = {z0}$ đv $= {h_m}\text{{ m}}$.''',
            fr'''Khoảng cách đến mặt phẳng $(Oxy)$ bằng cao độ $z_I = {z0}$ đv $= {h_m}\text{{ m}} \ne {R_m}\text{{ m}}$.'''
        )
    ]
    choices, loi_giai = make_tf_choices(items)
    return caudan, choices, loi_giai


def CuoiChuong_DeTongHop_TF_Cau4():
    # TF 4: Xác suất học bổng với tỉ lệ phần trăm số cực đẹp
    configs = [
        {"pA": 0.20, "pB_A": 0.30, "pB_notA": 0.10},  # P(B) = 14%
        {"pA": 0.25, "pB_A": 0.20, "pB_notA": 0.08},  # P(B) = 11%
        {"pA": 0.10, "pB_A": 0.40, "pB_notA": 0.10},  # P(B) = 13%
        {"pA": 0.30, "pB_A": 0.20, "pB_notA": 0.10},  # P(B) = 13%
        {"pA": 0.40, "pB_A": 0.20, "pB_notA": 0.10},  # P(B) = 14%
        {"pA": 0.50, "pB_A": 0.30, "pB_notA": 0.10},  # P(B) = 20%
        {"pA": 0.20, "pB_A": 0.40, "pB_notA": 0.15},  # P(B) = 20%
        {"pA": 0.30, "pB_A": 0.50, "pB_notA": 0.10},  # P(B) = 22%
        {"pA": 0.15, "pB_A": 0.30, "pB_notA": 0.10},  # P(B) = 13%
        {"pA": 0.20, "pB_A": 0.25, "pB_notA": 0.05},  # P(B) = 9%
    ]
    cfg = random.choice(configs)
    pA = cfg["pA"]
    pB_given_A = cfg["pB_A"]
    pB_given_notA = cfg["pB_notA"]
    
    pNotA = round(1 - pA, 2)
    pB = round(pA * pB_given_A + pNotA * pB_given_notA, 4)
    pNotB = round(1 - pB, 4)
    pNotB_given_notA = round(1 - pB_given_notA, 2)
    pNotA_given_notB = round((pNotB_given_notA * pNotA) / pNotB, 3)

    caudan = fr'''Một trường đại học trao hai loại học bổng $A$ và $B$ cho sinh viên trong trường, một sinh viên có thể được nhận cả hai loại học bổng $A$ và $B$. Trong số các sinh viên được trao học bổng loại $A$ có ${int(pB_given_A*100)}\%$ số bạn được trao học bổng loại $B$ và trong số các sinh viên không được trao học bổng loại $A$ có ${int(pB_given_notA*100)}\%$ số bạn được trao học bổng loại $B$. Có ${pB*100:.1f}\%$ số sinh viên toàn trường được trao học bổng loại $B$. Chọn ngẫu nhiên một sinh viên trong trường.'''

    items = [
        (
            fr'''Xác suất để sinh viên đó không được trao học bổng loại $B$ là ${pNotB}$.''',
            fr'''Xác suất để sinh viên đó không được trao học bổng loại $B$ là ${round(pNotB - 0.02, 4)}$.''',
            fr'''$P(\overline{{B}}) = 1 - P(B) = 1 - {pB} = {pNotB}$.''',
            fr'''$P(\overline{{B}}) = 1 - {pB} = {pNotB} \ne {round(pNotB - 0.02, 4)}$.'''
        ),
        (
            fr'''Xác suất để sinh viên đó không được trao học bổng loại $B$, biết sinh viên đó không được trao học bổng loại $A$, là ${pNotB_given_notA}$.''',
            fr'''Xác suất để sinh viên đó không được trao học bổng loại $B$, biết sinh viên đó không được trao học bổng loại $A$, là ${round(pNotB_given_notA - 0.05, 2)}$.''',
            fr'''$P(\overline{{B}}|\overline{{A}}) = 1 - P(B|\overline{{A}}) = 1 - {pB_given_notA} = {pNotB_given_notA}$.''',
            fr'''$P(\overline{{B}}|\overline{{A}}) = 1 - {pB_given_notA} = {pNotB_given_notA}$.'''
        ),
        (
            fr'''Xác suất để sinh viên đó không được trao học bổng loại $A$ là ${pNotA}$.''',
            fr'''Xác suất để sinh viên đó không được trao học bổng loại $A$ là ${round(pNotA - 0.05, 2)}$.''',
            fr'''Theo công thức xác suất toàn phần: $P(B) = P(B|A)P(A) + P(B|\overline{{A}})P(\overline{{A}}) \implies {pB} = {pB_given_A} P(A) + {pB_given_notA}(1 - P(A)) \implies P(A) = {pA} \implies P(\overline{{A}}) = {pNotA}$.''',
            fr'''Từ công thức xác suất toàn phần ta tính được $P(A) = {pA} \implies P(\overline{{A}}) = {pNotA}$.'''
        ),
        (
            fr'''Xác suất để sinh viên đó không được trao học bổng loại $A$, biết sinh viên đó không được trao học bổng loại $B$, xấp xỉ ${pNotA_given_notB}$.''',
            fr'''Xác suất để sinh viên đó không được trao học bổng loại $A$, biết sinh viên đó không được trao học bổng loại $B$, nhỏ hơn $0,5$.''',
            fr'''$P(\overline{{A}}|\overline{{B}}) = \dfrac{{P(\overline{{B}}|\overline{{A}}) P(\overline{{A}})}}{{P(\overline{{B}})}} = \dfrac{{{pNotB_given_notA} \times {pNotA}}}{{{pNotB}}} \approx {pNotA_given_notB}$.''',
            fr'''$P(\overline{{A}}|\overline{{B}}) \approx {pNotA_given_notB} > 0,5$, khẳng định nhỏ hơn $0,5$ là sai.'''
        )
    ]
    choices, loi_giai = make_tf_choices(items)
    return caudan, choices, loi_giai


# ==============================================================================
# PHẦN III: 6 CÂU TRẢ LỜI NGẮN (SA)
# ==============================================================================

def CuoiChuong_DeTongHop_SA_Cau1():
    # SA 1: Tối ưu hóa lợi nhuận L(x) = B(x) - C(x) ngẫu nhiên hóa số đẹp
    configs = [
        {"x0": 8,  "c0": 56, "p": 200, "d0": 332, "ans": "0,5", "L_val": 500},
        {"x0": 9,  "c0": 61, "p": 250, "d0": 415, "ans": "0,8", "L_val": 800},
        {"x0": 10, "c0": 80, "p": 320, "d0": 500, "ans": "1,2", "L_val": 1200},
        {"x0": 11, "c0": 83, "p": 380, "d0": 499, "ans": "1,8", "L_val": 1800},
        {"x0": 12, "c0": 90, "p": 450, "d0": 524, "ans": "2,5", "L_val": 2500},
        {"x0": 10, "c0": 60, "p": 300, "d0": 300, "ans": "1,4", "L_val": 1400},
        {"x0": 9,  "c0": 71, "p": 260, "d0": 315, "ans": "0,9", "L_val": 900},
    ]
    cfg = random.choice(configs)
    x0 = cfg["x0"]
    c0 = cfg["c0"]
    p = cfg["p"]
    d0 = cfg["d0"]
    ans = cfg["ans"]
    L_val = cfg["L_val"]
    
    x_max = x0 + random.randint(5, 8)
    lin_coef = p - c0

    caudan = fr'''Một công ty sản xuất mỗi ngày được $x$ sản phẩm ($1 \le x \le {x_max}$). Tổng chi phí sản xuất $x$ sản phẩm tính bằng nghìn đồng cho bởi hàm chi phí $C(x) = x^3 - 3x^2 + {c0}x + {d0}$. Giả sử công ty này bán hết sản phẩm mỗi ngày với giá ${p}$ nghìn đồng/sản phẩm. Gọi $B(x)$ là số tiền bán được và $L(x)$ là lợi nhuận thu được khi bán $x$ sản phẩm. Lợi nhuận (đơn vị triệu đồng) tối đa mà công ty có được là bao nhiêu?'''
    dapan = ans
    loi_giai = fr'''Doanh thu $B(x) = {p}x$ (nghìn đồng). \\
Lợi nhuận $L(x) = B(x) - C(x) = -x^3 + 3x^2 + {lin_coef}x - {d0}$ (nghìn đồng). \\
$L'(x) = -3x^2 + 6x + {lin_coef} = -3(x - {x0})(x + {x0 - 2}) = 0 \iff x = {x0} \in [1; {x_max}]$. \\
Lợi nhuận tối đa đạt tại $x = {x0}$ với $L({x0}) = {L_val}$ nghìn đồng $= {ans}$ triệu đồng.'''
    return caudan, dapan, loi_giai


def CuoiChuong_DeTongHop_SA_Cau2():
    # SA 2: Trọng tâm tam giác trong hình hộp chữ nhật Oxyz ngẫu nhiên hóa số đẹp
    boxes = [
        {"a": 10, "b": 16, "c": 8,  "m": 1, "n": 2, "p": 3, "T": 22},
        {"a": 12, "b": 15, "c": 9,  "m": 1, "n": 1, "p": 1, "T": 12},
        {"a": 9,  "b": 12, "c": 6,  "m": 2, "n": 1, "p": 3, "T": 16},
        {"a": 15, "b": 9,  "c": 12, "m": 1, "n": 2, "p": 1, "T": 15},
        {"a": 6,  "b": 12, "c": 15, "m": 3, "n": 1, "p": 2, "T": 20},
        {"a": 12, "b": 18, "c": 6,  "m": 1, "n": 2, "p": 2, "T": 20},
        {"a": 9,  "b": 15, "c": 12, "m": 2, "n": 2, "p": 1, "T": 20},
    ]
    b = random.choice(boxes)
    a, bb, c = b["a"], b["b"], b["c"]
    m, n, p = b["m"], b["n"], b["p"]
    T_ans = b["T"]
    
    m_str = f"{m}x" if m != 1 else "x"
    n_str = f"+ {n}y" if n != 1 else "+ y"
    p_str = f"+ {p}z" if p != 1 else "+ z"
    expr_str = f"{m_str} {n_str} {p_str}"

    caudan = fr'''Cho hình hộp chữ nhật $ABCD.A'B'C'D'$ có $AB = {a}, AD = {bb}, AA' = {c}$. Chọn hệ trục tọa độ $Oxyz$ có gốc $O$ trùng với $A$, các vectơ $\vec{{AB}}, \vec{{AD}}, \vec{{AA'}}$ lần lượt cùng hướng với $\vec{{i}}, \vec{{j}}, \vec{{k}}$. Gọi $G(x; y; z)$ là trọng tâm của tam giác $A'BD$. Tính $T = {expr_str}$.'''
    dapan = str(T_ans)
    loi_giai = fr'''Tọa độ các đỉnh: $A'(0; 0; {c}), B({a}; 0; 0), D(0; {bb}; 0)$. \\
Trọng tâm $G$ của tam giác $A'BD$ có tọa độ: \\
$x = \dfrac{{{a}}}{{3}}, y = \dfrac{{{bb}}}{{3}}, z = \dfrac{{{c}}}{{3}}$. \\
Suy ra: $T = {expr_str} = \dfrac{{{m} \cdot {a} + {n} \cdot {bb} + {p} \cdot {c}}}{{3}} = \dfrac{{{m*a + n*bb + p*c}}}{{3}} = {T_ans}$.'''
    return caudan, dapan, loi_giai


def CuoiChuong_DeTongHop_SA_Cau3():
    # SA 3: Khoảng biến thiên của mẫu số liệu ghép nhóm ngẫu nhiên hóa
    start = random.choice([10, 15, 20, 25, 30, 40, 50])
    w = random.choice([4, 5, 6, 10])
    k_grps = random.choice([4, 5, 6])
    end = start + k_grps * w
    R = end - start
    
    freqs = [random.randint(4, 15) for _ in range(k_grps)]
    headers = [f"[{start + i*w}; {start + (i+1)*w})" for i in range(k_grps)]
    
    caudan = fr'''Bảng số liệu ghép nhóm sau đây cho biết kết quả thống kê của một nghiên cứu:
\begin{{center}}
\begin{{tabular}}{{|c|{'c|'*k_grps}}}
\hline
Nhóm & {' & '.join(headers)} \\
\hline
Tần số & {' & '.join(str(f) for f in freqs)} \\
\hline
\end{{tabular}}
\end{{center}}
Khoảng biến thiên của mẫu số liệu ghép nhóm trên bằng bao nhiêu?'''
    dapan = str(R)
    loi_giai = fr'''Dựa vào bảng số liệu ghép nhóm, ta có: \\
Đầu mút trái của nhóm thứ nhất là $a_1 = {start}$. \\
Đầu mút phải của nhóm cuối cùng là $a_{{{k_grps + 1}}} = {end}$. \\
Khoảng biến thiên của mẫu số liệu ghép nhóm là: \\
$R = a_{{{k_grps + 1}}} - a_1 = {end} - {start} = {R}$.'''
    return caudan, dapan, loi_giai


def CuoiChuong_DeTongHop_SA_Cau4():
    # SA 4: Ứng dụng tích phân tính quãng đường ô tô phanh ngẫu nhiên hóa
    k = random.choice([2, 3, 4, 5, 6])
    t_stop = random.choice([4, 5, 6, 8, 10, 12])
    v0 = k * t_stop
    s = (v0 * t_stop) // 2
    
    caudan = fr'''Một ô tô đang chạy với vận tốc ${v0}\text{{ m/s}}$ thì người lái xe đạp phanh. Từ thời điểm đó, ô tô chuyển động chậm dần đều với gia tốc $a(t) = -{k}\text{{ m/s}}^2$ (tức vận tốc $v(t) = {v0} - {k}t\text{{ m/s}}$). Hỏi từ lúc đạp phanh đến khi dừng hẳn, ô tô di chuyển được quãng đường bao nhiêu mét?'''
    dapan = str(s)
    loi_giai = fr'''Ô tô dừng hẳn khi $v(t) = 0 \iff {v0} - {k}t = 0 \iff t = {t_stop}\text{{ (s)}}$. \\
Quãng đường ô tô di chuyển từ lúc đạp phanh đến khi dừng hẳn là: \\
$s = \displaystyle\int_{{0}}^{{{t_stop}}} ({v0} - {k}t)\,\mathrm{{d}}t = \left.\left({v0}t - \dfrac{{{k}t^2}}{{2}}\right)\right|_{{0}}^{{{t_stop}}} = {v0} \cdot {t_stop} - \dfrac{{{k} \cdot {t_stop}^2}}{{2}} = {s}\text{{ (m)}}$.'''
    return caudan, dapan, loi_giai


def CuoiChuong_DeTongHop_SA_Cau5():
    # SA 5: Trạm kiểm soát không lưu ra đa Oxyz ngẫu nhiên hóa số đẹp
    triplets = [
        (3, 4, 12, 13),
        (2, 3, 6, 7),
        (1, 4, 8, 9),
        (6, 6, 7, 11),
        (2, 6, 9, 11),
        (6, 10, 15, 19),
        (4, 12, 3, 13),
        (8, 9, 12, 17),
        (2, 10, 11, 15),
    ]
    dx, dy, dz, d = random.choice(triplets)
    sx, sy, sz = random.choice([1, -1]), random.choice([1, -1]), random.choice([1, -1])
    dx *= sx; dy *= sy; dz *= sz
    
    xA = random.randint(-5, 5)
    yA = random.randint(-5, 5)
    zA = random.randint(0, 4)
    
    xM = xA + dx
    yM = yA + dy
    zM = zA + dz
    
    caudan = fr'''Trong không gian $Oxyz$ (với đơn vị trên mỗi trục toạ độ là $1\text{{ km}}$), một trạm kiểm soát không lưu đặt tại vị trí $A({xA}; {yA}; {zA})$. Một máy bay đang ở vị trí $M({xM}; {yM}; {zM})$. Tính khoảng cách từ máy bay đến trạm kiểm soát không lưu theo đơn vị kilômét.'''
    dapan = str(d)
    loi_giai = fr'''Khoảng cách từ trạm kiểm soát không lưu $A$ đến máy bay $M$ là: \\
$AM = \sqrt{{({xM} - {xA})^2 + ({yM} - {yA})^2 + ({zM} - {zA})^2}} = \sqrt{{({dx})^2 + ({dy})^2 + ({dz})^2}} = \sqrt{{{d**2}}} = {d}\text{{ (km)}}$.'''
    return caudan, dapan, loi_giai


def CuoiChuong_DeTongHop_SA_Cau6():
    # SA 6: Chẩn đoán bệnh - Xác suất toàn phần và Bayes ngẫu nhiên hóa
    p_b = random.choice([0.01, 0.02, 0.04, 0.05])
    p_tb = random.choice([0.90, 0.95, 0.96, 0.98])
    p_t_not_b = random.choice([0.02, 0.03, 0.05])
    
    p_not_b = 1 - p_b
    p_t = p_b * p_tb + p_not_b * p_t_not_b
    p_b_given_t = (p_b * p_tb) / p_t
    
    ans_val = round(p_b_given_t, 2)
    ans_str = f"{ans_val:.2f}".replace('.', ',')
    
    p_b_pct = f"{p_b*100:g}".replace('.', ',')
    p_tb_pct = f"{p_tb*100:g}".replace('.', ',')
    p_t_not_b_pct = f"{p_t_not_b*100:g}".replace('.', ',')
    
    caudan = fr'''Tỉ lệ người mắc một căn bệnh trong cộng đồng là ${p_b_pct}\%$. Một xét nghiệm y tế có độ chính xác: người thực sự bị bệnh thì xét nghiệm cho kết quả dương tính với xác suất ${p_tb_pct}\%$; người không bị bệnh thì xét nghiệm cho kết quả dương tính giả với xác suất ${p_t_not_b_pct}\%$. Chọn ngẫu nhiên một người trong cộng đồng đem đi xét nghiệm và người đó nhận kết quả dương tính. Tính xác suất để người đó thực sự mắc bệnh (làm tròn kết quả đến hàng phần trăm).'''
    dapan = ans_str
    
    loi_giai = fr'''Gọi $B$ là biến cố "Người được chọn thực sự mắc bệnh" và $T$ là biến cố "Người được chọn có kết quả xét nghiệm dương tính". \\
Theo đề bài: $P(B) = {p_b}$, $P(\overline{{B}}) = 1 - {p_b} = {p_not_b:.2f}$. \\
$P(T|B) = {p_tb}$, $P(T|\overline{{B}}) = {p_t_not_b}$. \\
Theo công thức xác suất toàn phần: \\
$P(T) = P(B)P(T|B) + P(\overline{{B}})P(T|\overline{{B}}) = {p_b} \times {p_tb} + {p_not_b:.2f} \times {p_t_not_b} = {p_t:.4f}$. \\
Áp dụng công thức Bayes, xác suất người đó thực sự mắc bệnh khi có kết quả dương tính là: \\
$P(B|T) = \dfrac{{P(B)P(T|B)}}{{P(T)}} = \dfrac{{{p_b} \times {p_tb}}}{{{p_t:.4f}}} = \dfrac{{{p_b * p_tb:.4f}}}{{{p_t:.4f}}} \approx {dapan}$.'''
    return caudan, dapan, loi_giai



