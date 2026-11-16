# -*- coding: utf-8 -*-
"""
Module nâng cấp ngân hàng câu hỏi trắc nghiệm Chương 1 (CuoiChuong1_MC_*)
Toàn bộ câu hỏi được lập trình sinh số ngẫu nhiên thuật toán (Algorithmic Generation),
không sử dụng các bộ preset tĩnh 2-3 câu, đảm bảo mỗi lần bấm sinh đề đều ra một bài toán mới với số liệu khác nhau.
Áp dụng clean_option để loại bỏ triệt để dấu chấm thừa cho gói ex_test.
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


def fmt_linear(a, b):
    terms = []
    if a == 1:
        terms.append("x")
    elif a == -1:
        terms.append("-x")
    elif a != 0:
        terms.append(f"{a}x")
    if b > 0:
        terms.append(f"+ {b}")
    elif b < 0:
        terms.append(f"- {abs(b)}")
    elif not terms:
        terms.append("0")
    return " ".join(terms)


# ==============================================================================
# CÁC CÂU HỎI TRẮC NGHIỆM CHƯƠNG 1 THUẬT TOÁN HÓA ĐA DẠNG BIẾN THỂ
# ==============================================================================

def CuoiChuong1_MC_Cau4():
    # Tiệm cận ngang từ bảng biến thiên ngẫu nhiên số
    y1 = random.choice([-5, -4, -3, -2, -1, 1, 2, 3, 4, 5])
    diff = random.choice([1, 2, 3, 4, 5])
    y2 = y1 + diff
    x0 = random.choice([-2, -1, 0, 1, 2])

    caudan = fr'''\immini{{Cho hàm số $y=f(x)$ có bảng biến thiên sau. Đồ thị hàm số $y=f(x)$ có mấy đường tiệm cận ngang?}}
{{\begin{{tikzpicture}}
    \tkzTabInit[nocadre,espcl=2.2,lgt=1.2]
    {{$x$/0.6, $y'$/0.6, $y$/1.2}}
    {{$-\infty$, ${x0}$, $+\infty$}}
    \tkzTabLine{{,-,d,+,}}
    \tkzTabVar{{+/ ${y1}$, -D+/ $-\infty$ / $+\infty$, +/ ${y2}$}}
\end{{tikzpicture}}
}}'''
    correct = r'''$2$'''
    wrongs = [r'''$0$''', r'''$1$''', r'''$3$''']
    choices = shuffle_choices(correct, wrongs)
    loi_giai = fr'''Ta có $\lim\limits_{{x \to -\infty}} f(x) = {y1} \implies y = {y1}$ là tiệm cận ngang. \\
Ta có $\lim\limits_{{x \to +\infty}} f(x) = {y2} \implies y = {y2}$ là tiệm cận ngang. \\
Vì ${y1} \ne {y2}$ nên đồ thị hàm số có đúng $2$ đường tiệm cận ngang.'''
    return caudan, choices, loi_giai


def CuoiChuong1_MC_Cau16():
    # Số điểm cực tiểu từ dấu đạo hàm f'(x)
    x1 = random.randint(-4, -2)
    x2 = random.randint(x1 + 2, 0)
    x3 = random.randint(x2 + 2, 3)
    x4 = random.randint(x3 + 2, 5)

    caudan = fr'''Cho hàm số $y=f(x)$ có đạo hàm $f'(x) = (x - {x1})^2(x - {x2})(x - {x3})^3(x - {x4})$. Số điểm cực tiểu của hàm số đã cho là'''
    correct = r'''$2$'''
    wrongs = [r'''$1$''', r'''$3$''', r'''$0$''']
    choices = shuffle_choices(correct, wrongs)
    loi_giai = fr'''Nghiệm $x = {x1}$ là nghiệm bội chẵn nên $f'(x)$ không đổi dấu khi qua $x = {x1}$. \\
Các nghiệm $x = {x2}, x = {x3}, x = {x4}$ là các nghiệm bội lẻ. \\
Khi qua các nghiệm bội lẻ theo thứ tự từ trái sang phải, dấu của $f'(x)$ đổi lần lượt: dương sang âm (cực đại), âm sang dương (cực tiểu), dương sang âm (cực đại) hoặc ngược lại. \\
Qua bảng xét dấu, hàm số có đúng $1$ điểm cực đại và $2$ điểm cực tiểu (hoặc $1$ điểm cực tiểu tùy vào hệ số bậc cao nhất). \\
Với hệ số cao nhất dương: khoảng ngoài cùng mang dấu dương, suy ra tại $x = {x2}$ (đổi từ $+$ sang $-$: cực đại), tại $x = {x3}$ (đổi từ $-$ sang $+$: cực tiểu), tại $x = {x4}$ (đổi từ $+$ sang $-$: cực đại). Do đó số điểm cực tiểu là $1$.'''
    return caudan, choices, loi_giai


def CuoiChuong1_MC_Cau18():
    # Biện luận số nghiệm f(x) = m từ đồ thị hàm bậc ba ngẫu nhiên hóa hoàn toàn
    k = random.choice([1, 2])
    y_shift = random.choice([-2, -1, 0, 1, 2])
    # y = k*x^3 - 3*k*x + y_shift => cực đại tại x = -1, y_cd = 2k + y_shift
    # cực tiểu tại x = 1, y_ct = -2k + y_shift
    y_cd = 2 * k + y_shift
    y_ct = -2 * k + y_shift

    # Chọn m sao cho số nghiệm thay đổi: 1, 2, hoặc 3
    case = random.choice(["1_above", "3_between", "1_below"])
    if case == "1_above":
        m = y_cd + random.choice([1, 2])
        ans = 1
    elif case == "3_between":
        m = y_shift
        ans = 3
    else:
        m = y_ct - random.choice([1, 2])
        ans = 1

    caudan = fr'''\immini{{Cho hàm số $y = f(x)$ có đồ thị như hình vẽ bên với giá trị cực đại $y_{{cd}} = {y_cd}$ và giá trị cực tiểu $y_{{ct}} = {y_ct}$. Số nghiệm thực của phương trình $f(x) = {m}$ là}}
{{\begin{{tikzpicture}}[scale=0.55, line join=round, line cap=round, >=stealth,font=\footnotesize]
	\def\xmin{{-2.5}}\def\xmax{{2.5}}\def\ymin{{{y_ct - 2}}}\def\ymax{{{y_cd + 2}}}
	\draw[->] (\xmin-0.2,0)--(\xmax+0.2,0) node[below]{{$x$}};
	\draw[->] (0,\ymin-0.2)--(0,\ymax+0.2) node[right]{{$y$}};
	\draw (0,0) node[below left]{{$O$}};
	\clip (\xmin,\ymin) rectangle (\xmax,\ymax);
	\draw[thick,smooth,samples=200,domain=\xmin:\xmax] plot (\x,{{{k}*((\x)^3) - {3*k}*(\x) + {y_shift}}});
	\draw[dashed] (-2,{y_cd})--(2,{y_cd}); \fill (-1,{y_cd}) circle(1.5pt) node[above]{{\tiny $({-1};{y_cd})$}};
	\draw[dashed] (-2,{y_ct})--(2,{y_ct}); \fill (1,{y_ct}) circle(1.5pt) node[below]{{\tiny $({1};{y_ct})$}};
\end{{tikzpicture}}}}'''
    correct = fr"${ans}$"
    wrongs = [str(x) for x in [0, 1, 2, 3, 4] if x != ans][:3]
    choices = shuffle_choices(correct, [fr"${w}$" for w in wrongs])
    loi_giai = fr'''Dựa vào đồ thị, giá trị cực đại là $y_{{cd}} = {y_cd}$ và giá trị cực tiểu là $y_{{ct}} = {y_ct}$. \\
Đường thẳng $y = {m}$ cắt đồ thị hàm số tại đúng ${ans}$ điểm. \\
Vậy phương trình $f(x) = {m}$ có đúng ${ans}$ nghiệm thực.'''
    return caudan, choices, loi_giai


def CuoiChuong1_MC_Cau19():
    # Số tiệm cận từ bảng biến thiên ngẫu nhiên hóa
    x0 = random.choice([-3, -2, -1, 1, 2, 3])
    y_left = random.choice([-4, -3, -2, -1, 1, 2, 3])
    y_right = y_left + random.choice([2, 3, 4])

    caudan = fr'''\immini{{Cho hàm số $y=f(x)$ có bảng biến thiên như hình bên. Đồ thị hàm số $y=f(x)$ có bao nhiêu đường tiệm cận (gồm cả tiệm cận đứng và tiệm cận ngang)?}}
{{\begin{{tikzpicture}} 
	\tkzTabInit[nocadre,lgt=1.2,espcl=2,deltacl=0.6]
	{{$x$ /0.6,$y'$ /0.6,$y$ /1.5}}
	{{$-\infty$,${x0}$,$+\infty$}}
	\tkzTabLine{{,+,d,+,}}
	\tkzTabVar{{-/${y_left}$,+D-/$+\infty$/$-\infty$,+/${y_right}$}}
\end{{tikzpicture}}}}'''
    correct = r'''$3$'''
    wrongs = [r'''$1$''', r'''$2$''', r'''$4$''']
    choices = shuffle_choices(correct, wrongs)
    loi_giai = fr'''Ta có: \\
- $\lim\limits_{{x \to -\infty}} f(x) = {y_left} \implies y = {y_left}$ là một tiệm cận ngang. \\
- $\lim\limits_{{x \to +\infty}} f(x) = {y_right} \implies y = {y_right}$ là một tiệm cận ngang. \\
- Tại $x = {x0}$, các giới hạn một bên đều ra vô cực $\implies x = {x0}$ là một tiệm cận đứng. \\
Vậy đồ thị hàm số có tổng cộng $2 + 1 = 3$ đường tiệm cận.'''
    return caudan, choices, loi_giai


def CuoiChuong1_MC_Cau21():
    # Khoảng nghịch biến của hàm trùng phương từ BBT ngẫu nhiên số
    x0 = random.choice([1, 2, 3, 4])
    y0 = random.choice([-3, -2, -1, 0, 1])
    y_max = y0 + random.choice([2, 3, 4, 5])

    caudan = fr'''\immini{{Cho hàm số $y = f(x)$ có bảng biến thiên như sau. Hàm số đã cho nghịch biến trên khoảng nào sau đây?}}
{{\begin{{tikzpicture}}
  \tkzTabInit[nocadre,lgt=1.2,espcl=1.3,deltacl=0.4]
  {{$x$ /0.6, $y'$ /0.6, $y$ /1.5}}
  {{$-\infty$, ${-x0}$, $0$, ${x0}$, $+\infty$}}
  \tkzTabLine{{, -, 0, +, 0, -, 0, +, }}
  \tkzTabVar{{+/$+\infty$, -/${y0}$, +/${y_max}$, -/${y0}$, +/$+\infty$}}
\end{{tikzpicture}}}}'''
    correct = fr"$(0; {x0})$"
    wrongs = [
        fr"$(0; +\infty)$",
        fr"$({-x0}; 0)$",
        fr"$({x0}; +\infty)$"
    ]
    choices = shuffle_choices(correct, wrongs)
    loi_giai = fr'''Dựa vào bảng biến thiên, ta thấy $y' < 0$ trên các khoảng $(-\infty; {-x0})$ và $(0; {x0})$. \\
Do đó hàm số nghịch biến trên khoảng $(0; {x0})$.'''
    return caudan, choices, loi_giai


def CuoiChuong1_MC_Cau22():
    # GTLN của hàm bậc ba f(x) = x^3 - 3*a^2*x + d trên [-m; m] với m > a
    a = random.choice([1, 2])
    d = random.choice([-5, -3, -1, 2, 4, 6, 8, 10])
    m = a + 1
    coeff = 3 * (a**2)

    # f(-m) = -m^3 + 3a^2 m + d
    # f(-a) = -a^3 + 3a^3 + d = 2a^3 + d (cực đại)
    # f(a) = -2a^3 + d (cực tiểu)
    # f(m) = m^3 - 3a^2 m + d
    val_neg_a = 2 * (a**3) + d
    val_pos_m = m**3 - coeff * m + d
    max_val = max(val_neg_a, val_pos_m)

    caudan = fr'''Giá trị lớn nhất của hàm số $f(x) = x^3 - {coeff}x + {d}$ trên đoạn $[{-m}; {m}]$ bằng'''
    correct = fr"${max_val}$"
    wrongs = [fr"${max_val - 4}$", fr"${d}$", fr"${-2*(a**3) + d}$"]
    choices = shuffle_choices(correct, wrongs)
    loi_giai = fr'''Ta có $f'(x) = 3x^2 - {coeff} = 0 \iff x = \pm {a} \in [{-m}; {m}]$. \\
Tính các giá trị tại các điểm tới hạn và đầu mút, ta tìm được giá trị lớn nhất là ${max_val}$.'''
    return caudan, choices, loi_giai


def CuoiChuong1_MC_Cau24():
    # Giá trị cực đại của hàm bậc ba từ đồ thị ngẫu nhiên hóa
    x_cd = random.choice([-2, -1, 0, 1])
    x_ct = x_cd + 2
    y_shift = random.choice([-3, -2, -1, 0, 1, 2])
    # f(x) = (x - x_cd)^2 (x - x_cd - 3) + y_cd => cực đại tại x_cd, y_cd = y_shift + 4
    y_cd = y_shift + 4
    y_ct = y_shift

    caudan = fr'''\immini{{Cho hàm số $y = ax^3 + bx^2 + cx + d \; (a \neq 0)$ có đồ thị là đường cong như hình bên. Giá trị cực đại của hàm số đã cho bằng}}
{{\begin{{tikzpicture}}[scale=0.55, line join=round, line cap=round, >=stealth,font=\footnotesize]
	\def\xmin{{-3.5}}\def\xmax{{3.5}}\def\ymin{{{y_ct - 2}}}\def\ymax{{{y_cd + 2}}}
	\draw[->] (\xmin-0.2,0)--(\xmax+0.2,0) node[below]{{$x$}};
	\draw[->] (0,\ymin-0.2)--(0,\ymax+0.2) node[right]{{$y$}};
	\draw (0,0) node[below left]{{$O$}};
	\clip (\xmin,\ymin) rectangle (\xmax,\ymax);
	\draw[thick,smooth,samples=200,domain=\xmin:\xmax] plot (\x,{{(\x - {x_cd})*(\x - {x_cd})*(-\x + {x_ct} + 1) + {y_cd}}});
	\draw[dashed] ({x_cd},0)--({x_cd},{y_cd})--(0,{y_cd});\fill ({x_cd},{y_cd}) circle(1.5pt);
	\draw[dashed] ({x_ct},0)--({x_ct},{y_ct})--(0,{y_ct});\fill ({x_ct},{y_ct}) circle(1.5pt);
\end{{tikzpicture}}}}'''
    correct = fr"${y_cd}$"
    wrongs = [fr"${x_cd}$", fr"${y_ct}$", fr"${y_cd + 2}$"]
    choices = shuffle_choices(correct, wrongs)
    loi_giai = fr'''Từ đồ thị hàm số, điểm cực đại của đồ thị là $({x_cd}; {y_cd})$. \\
Do đó giá trị cực đại của hàm số đã cho bằng $y = {y_cd}$.'''
    return caudan, choices, loi_giai


def CuoiChuong1_MC_Cau26():
    # Số điểm cực trị từ công thức đạo hàm
    x1 = random.choice([-3, -2, -1])
    x2 = random.choice([1, 2, 3])
    x3 = x2 + random.choice([1, 2])
    k_even = random.choice([2, 4])

    caudan = fr'''Cho hàm số $y=f(x)$ có đạo hàm $f'(x) = x^{{{k_even}}}(x {"+" if -x1 > 0 else "-"} {abs(x1)})(x - {x2})(x - {x3})^3, \; \forall x \in \mathbb{{R}}$. Số điểm cực trị của hàm số đã cho là'''
    correct = r'''$3$'''
    wrongs = [r'''$1$''', r'''$2$''', r'''$4$''']
    choices = shuffle_choices(correct, wrongs)
    loi_giai = fr'''Nghiệm $x = 0$ là nghiệm bội chẵn (bội ${k_even}$) nên $f'(x)$ không đổi dấu khi qua $x = 0$. \\
Các nghiệm $x = {x1}$, $x = {x2}$ (nghiệm đơn) và $x = {x3}$ (nghiệm bội $3$) là các nghiệm bội lẻ nên $f'(x)$ đổi dấu khi qua chúng. \\
Vậy hàm số có đúng $3$ điểm cực trị.'''
    return caudan, choices, loi_giai


def CuoiChuong1_MC_Cau27():
    # So sánh giá trị hàm số từ đạo hàm f'(x) = (x - a)(x - b)
    a = random.choice([-2, -1, 0, 1])
    k = random.choice([3, 4, 5])
    b = a + k
    mid = a + 2

    caudan = fr'''Cho hàm số $y = f(x)$ có đạo hàm $f'(x) = (x {"+" if -a > 0 else "-"} {abs(a)})(x - {b}), \; \forall x \in \mathbb{{R}}$. Mệnh đề nào sau đây đúng?'''
    correct = fr"$f({a}) > f({mid})$"
    wrongs = [
        fr"$f({a}) = f({b})$",
        fr"$f({b}) > f({a})$",
        fr"$f({b}) > f({mid})$"
    ]
    choices = shuffle_choices(correct, wrongs)
    loi_giai = fr'''Ta có $f'(x) < 0 \iff {a} < x < {b}$, do đó hàm số $y = f(x)$ nghịch biến trên đoạn $[{a}; {b}]$. \\
Vì ${a} < {mid} < {b}$ nên $f({a}) > f({mid}) > f({b})$. \\
Do đó mệnh đề $f({a}) > f({mid})$ là đúng.'''
    return caudan, choices, loi_giai


def CuoiChuong1_MC_Cau28():
    # Nhận dạng đồ thị hàm phân thức 2 trên 1
    x0 = random.choice([-2, -1, 1, 2])
    b_lin = random.choice([-2, -1, 1, 2])
    # y = x + b_lin + 1/(x - x0) = ( (x + b_lin)(x - x0) + 1 ) / (x - x0)
    # Tử = x^2 + (b_lin - x0)x + (-b_lin*x0 + 1)
    k_lin = b_lin - x0
    c_lin = -b_lin * x0 + 1
    
    def fmt_t(coef, var="x", is_lead=False):
        if coef == 0:
            return ""
        sign = "+" if coef > 0 else "-"
        abs_c = abs(coef)
        c_str = "" if (abs_c == 1 and var != "") else str(abs_c)
        if is_lead:
            return f"{'-' if coef < 0 else ''}{c_str}{var}"
        return f"{sign} {c_str}{var}"

    term_k = fmt_t(k_lin, "x")
    term_c = fmt_t(c_lin, "")
    num_str = f"x^2 {term_k} {term_c}".replace("  ", " ").strip()
    den_str = f"x - {x0}" if x0 > 0 else f"x + {abs(x0)}"
    den_opp = f"x + {x0}" if x0 > 0 else f"x - {abs(x0)}"
    func_tex = fr"y = \dfrac{{{num_str}}}{{{den_str}}}"
    b_str = f"+ {b_lin}" if b_lin > 0 else f"- {abs(b_lin)}"

    # Cực trị
    x_cd = x0 - 1
    y_cd = x0 + b_lin - 2
    x_ct = x0 + 1
    y_ct = x0 + b_lin + 2

    xmin = min(-3.5, x0 - 2.5)
    xmax = max(3.5, x0 + 2.5)
    ymin = min(-4.5, y_cd - 2)
    ymax = max(5.5, y_ct + 2)

    tikz = fr'''\begin{{tikzpicture}}[scale=0.55, line join=round, line cap=round, >=stealth, font=\footnotesize]
	\def\xmin{{{xmin}}}\def\xmax{{{xmax}}}\def\ymin{{{ymin}}}\def\ymax{{{ymax}}}
	\draw[->] (\xmin-0.2,0)--(\xmax+0.2,0) node[below]{{$x$}};
	\draw[->] (0,\ymin-0.2)--(0,\ymax+0.2) node[right]{{$y$}};
	\draw (0,0) node[below left]{{$O$}};
	\begin{{scope}}
	\clip (\xmin,\ymin) rectangle (\xmax,\ymax);
	\draw[dashed, red!80!black, thick] ({x0},\ymin)--({x0},\ymax);
	\draw[dashed, blue!80!black, thick] (\xmin,{{\xmin + {b_lin}}})--(\xmax,{{\xmax + {b_lin}}});
	\draw[thick, smooth, samples=150, domain=\xmin:{x0 - 0.22}] plot (\x,{{((\x)^2 + ({k_lin})*(\x) + ({c_lin}))/((\x) - ({x0}))}});
	\draw[thick, smooth, samples=150, domain={x0 + 0.22}:\xmax] plot (\x,{{((\x)^2 + ({k_lin})*(\x) + ({c_lin}))/((\x) - ({x0}))}});
	\end{{scope}}
	\fill ({x_cd},{y_cd}) circle (1.5pt);
	\draw[dashed] ({x_cd},0) node[below]{{${x_cd}$}} -- ({x_cd},{y_cd}) -- (0,{y_cd}) node[left]{{${y_cd}$}};
	\fill ({x_ct},{y_ct}) circle (1.5pt);
	\draw[dashed] ({x_ct},0) node[below]{{${x_ct}$}} -- ({x_ct},{y_ct}) -- (0,{y_ct}) node[left]{{${y_ct}$}};
	\draw ({x0},0.1) -- ({x0},-0.1) node[{'below right' if x0 > 0 else 'below left'}]{{${x0}$}};
\end{{tikzpicture}}'''

    caudan = fr'''\immini{{Đồ thị ở hình bên có tiệm cận đứng $x = {x0}$ và tiệm cận xiên $y = x {b_str}$. Đây là đồ thị của hàm số nào sau đây?}}
{{{tikz}}}'''
    correct = fr"${func_tex}$"
    
    # 3 phương án sai hoàn toàn phân biệt, không chứa 1x
    wrong_num1 = f"-x^2 {term_k} {term_c}".replace("  ", " ").strip()
    w1 = fr"$y = \dfrac{{{wrong_num1}}}{{{den_str}}}$"
    w2 = fr"$y = \dfrac{{{num_str}}}{{{den_opp}}}$"
    
    k_alt = -k_lin if k_lin != 0 else 2
    term_k_alt = fmt_t(k_alt, "x")
    wrong_num3 = f"x^2 {term_k_alt} {term_c}".replace("  ", " ").strip()
    w3 = fr"$y = \dfrac{{{wrong_num3}}}{{{den_str}}}$"

    choices = shuffle_choices(correct, [w1, w2, w3])
    loi_giai = fr'''Đồ thị hàm số có tiệm cận đứng $x = {x0}$ và tiệm cận xiên $y = x {b_str}$. \\
Xét hàm số ${func_tex} = x {b_str} + \dfrac{{1}}{{{den_str}}}$ hoàn toàn phù hợp.'''
    return caudan, choices, loi_giai


def CuoiChuong1_MC_Cau29():
    # Số điểm cực trị của hàm phân thức bậc nhất trên bậc nhất
    a = random.choice([2, 3, 4, 5])
    b = random.choice([-5, -3, -1, 1, 3, 5])
    d = random.choice([-4, -3, -2, 2, 3, 4])
    num_str = fmt_linear(a, b)
    den_str = fmt_linear(1, d)

    caudan = fr'''Số điểm cực trị của hàm số $y = \dfrac{{{num_str}}}{{{den_str}}}$ là'''
    correct = r'''$0$'''
    wrongs = [r'''$1$''', r'''$2$''', r'''$3$''']
    choices = shuffle_choices(correct, wrongs)
    loi_giai = fr'''Hàm số phân thức bậc nhất trên bậc nhất có đạo hàm $y' = \dfrac{{{a*d - b}}}{{({den_str})^2}} \ne 0$ luôn cùng một dấu trên từng khoảng xác định. \\
Do đó đạo hàm không bao giờ đổi dấu, hàm số không có điểm cực trị.'''
    return caudan, choices, loi_giai


def CuoiChuong1_MC_Cau30():
    # Tổng M + m từ đồ thị
    M_val = random.choice([3, 4, 5, 6])
    m_val = random.choice([-4, -3, -2, -1])
    ans = M_val + m_val

    caudan = fr'''\immini{{Cho hàm số $y=f(x)$ liên tục trên đoạn $[-1; 5]$ có đồ thị như hình bên với giá trị lớn nhất $M = {M_val}$ và giá trị nhỏ nhất $m = {m_val}$. Giá trị của $M + m$ bằng}}
{{\begin{{tikzpicture}}[scale=0.5, line join=round, line cap=round, >=stealth,font=\footnotesize]
	\draw[->] (-1.5,0)--(5.5,0) node[below]{{$x$}};
	\draw[->] (0,-4.5)--(0,6.5) node[right]{{$y$}};
	\draw (0,0) node[below left]{{$O$}};
	\draw[thick] (-1,{M_val}) -- (1,{m_val}) -- (3,1) -- (5,0);
	\draw[dashed] (-1,0)--(-1,{M_val})--(0,{M_val});
	\draw[dashed] (1,0)--(1,{m_val})--(0,{m_val});
\end{{tikzpicture}}}}'''
    correct = fr"${ans}$"
    wrongs = [fr"${M_val - m_val}$", fr"${ans + 2}$", fr"${ans - 3}$"]
    choices = shuffle_choices(correct, wrongs)
    loi_giai = fr'''Dựa vào đồ thị trên đoạn $[-1; 5]$, giá trị lớn nhất là $M = {M_val}$ và giá trị nhỏ nhất là $m = {m_val}$. \\
Vậy $M + m = {M_val} + ({m_val}) = {ans}$.'''
    return caudan, choices, loi_giai


def CuoiChuong1_MC_Cau34():
    # Bảng xét dấu f'(x) có nghiệm bội chẵn
    x1 = random.choice([-3, -2, -1])
    x2 = 0
    x3 = random.choice([1, 2, 3])

    caudan = fr'''\immini{{Cho hàm số $f(x)$ có bảng xét dấu của $f'(x)$ như sau. Số điểm cực trị của hàm số đã cho là}}
{{\begin{{tikzpicture}}
	\tkzTabInit[lgt=1.2,espcl=1.5,nocadre]
	{{$x$/0.6, $f'(x)$/0.6}}
	{{$-\infty$, ${x1}$, ${x2}$, ${x3}$, $+\infty$}}
	\tkzTabLine{{,+,0,-,0,-,0,+,}}
\end{{tikzpicture}}}}'''
    correct = r'''$2$'''
    wrongs = [r'''$0$''', r'''$1$''', r'''$3$''']
    choices = shuffle_choices(correct, wrongs)
    loi_giai = fr'''Đạo hàm $f'(x)$ đổi dấu khi qua $x = {x1}$ và $x = {x3}$. \\
Tại $x = {x2}$, $f'(x)$ không đổi dấu. \\
Do đó hàm số có đúng $2$ điểm cực trị.'''
    return caudan, choices, loi_giai


def CuoiChuong1_MC_Cau35():
    # GTNN của f(x) = x^3 - 3*k^2*x + c trên [0; m] với m > k
    k = random.choice([1, 2, 3])
    c_shift = random.randint(-5, 5)
    coeff = 3 * (k**2)
    m = k + random.choice([1, 2])
    f_k = -2 * (k**3) + c_shift
    f_0 = c_shift
    f_m = m**3 - coeff * m + c_shift
    min_val = min(f_k, f_0, f_m)

    caudan = fr'''Giá trị nhỏ nhất của hàm số $f(x) = x^3 - {coeff}x {"+" if c_shift > 0 else "-"} {abs(c_shift)}$ trên đoạn $[0; {m}]$ là'''
    correct = fr"${min_val}$"
    wrongs = [fr"${f_0}$", fr"${f_m}$", fr"${min_val - 4}$"]
    if correct in wrongs:
        wrongs.remove(correct)
        wrongs.append(fr"${min_val + 3}$")
    choices = shuffle_choices(correct, wrongs[:3])
    loi_giai = fr'''Ta có $f'(x) = 3x^2 - {coeff} = 0 \iff x = \pm {k}$. \\
Trên đoạn $[0; {m}]$, nhận điểm tới hạn $x = {k}$. \\
Tính các giá trị: $f(0) = {f_0}$, $f({k}) = {f_k}$, $f({m}) = {f_m}$. \\
Vậy giá trị nhỏ nhất của hàm số trên đoạn $[0; {m}]$ là ${min_val}$.'''
    return caudan, choices, loi_giai


def CuoiChuong1_MC_Cau36():
    # Tiệm cận đứng của y = (ax+b)/(x - x0)
    x0 = random.choice([-6, -5, -4, -3, -2, -1, 1, 2, 3, 4, 5, 6])
    a = random.choice([1, 2, 3, -1, -2])
    b = random.choice([1, 3, 5, 7, -1, -3, -5])
    sign_x0 = f"- {x0}" if x0 > 0 else f"+ {abs(x0)}"
    num_str = fmt_linear(a, b)
    caudan = fr'''Đường tiệm cận đứng của đồ thị hàm số $y = \dfrac{{{num_str}}}{{x {sign_x0}}}$ là'''
    correct = fr"$x = {x0}$"
    wrongs = [
        fr"$y = {x0}$",
        fr"$x = {-x0}$",
        fr"$y = {a}$"
    ]
    choices = shuffle_choices(correct, wrongs)
    loi_giai = fr'''Nghiệm của mẫu số là $x {sign_x0} = 0 \iff x = {x0}$ (và tử số khác $0$). \\
Do đó đường tiệm cận đứng của đồ thị hàm số là $x = {x0}$.'''
    return caudan, choices, loi_giai


def CuoiChuong1_MC_Cau37():
    # Nhận dạng hàm phân thức y = (ax+b)/(cx+d) từ BBT
    x0 = random.choice([-2, -1, 1, 2])
    y0 = random.choice([-2, -1, 1, 2])
    # y = (y0*x + b)/(x - x0) với y0*(-x0) - b < 0 để hàm đồng biến
    b = -y0 * x0 + random.choice([1, 2, 3])

    num_str = fmt_linear(y0, b)
    den_str = fmt_linear(1, -x0)

    caudan = fr'''\immini{{Cho hàm số $y=f(x)$ có bảng biến thiên sau với tiệm cận đứng $x = {x0}$ và tiệm cận ngang $y = {y0}$. Công thức của $f(x)$ là}}
{{\begin{{tikzpicture}} 
	\tkzTabInit[nocadre,lgt=1.2,espcl=2,deltacl=0.6]
	{{$x$ /0.8,$y'$ /0.6,$y$ /1.8}}
	{{$-\infty$,${x0}$,$+\infty$}}
	\tkzTabLine{{,+,d,+,}}
	\tkzTabVar{{-/${y0}$,+D-/$+\infty$/$-\infty$,+/${y0}$}}
\end{{tikzpicture}}}}'''
    correct = fr"$y = \dfrac{{{num_str}}}{{{den_str}}}$"
    wrongs = [
        fr"$y = \dfrac{{{fmt_linear(y0, -b)}}}{{{den_str}}}$",
        fr"$y = \dfrac{{{fmt_linear(-y0, b)}}}{{{den_str}}}$",
        fr"$y = \dfrac{{{num_str}}}{{{fmt_linear(1, x0)}}}$"
    ]
    choices = shuffle_choices(correct, wrongs)
    loi_giai = fr'''Dựa vào bảng biến thiên, đồ thị có tiệm cận đứng $x = {x0}$, tiệm cận ngang $y = {y0}$ và hàm số đồng biến ($y' > 0$). \\
Hàm số ${correct}$ thỏa mãn các điều kiện trên.'''
    return caudan, choices, loi_giai


def CuoiChuong1_MC_Cau39():
    # Số đường tiệm cận từ BBT
    x0 = random.choice([-3, -2, -1, 1, 2, 3])
    y1 = random.choice([-5, -4, -3, -2, -1, 1, 2, 3, 4])
    y2 = y1 + random.choice([1, 2, 3, 4])

    caudan = fr'''Cho hàm số $y=f(x)$ có $\lim\limits_{{x \to -\infty}} f(x) = {y1}$, $\lim\limits_{{x \to +\infty}} f(x) = {y2}$ và $\lim\limits_{{x \to {x0}^+}} f(x) = +\infty$. Đồ thị hàm số có bao nhiêu đường tiệm cận (đứng và ngang)?'''
    correct = r'''$3$'''
    wrongs = [r'''$1$''', r'''$2$''', r'''$4$''']
    choices = shuffle_choices(correct, wrongs)
    loi_giai = fr'''Ta có $2$ tiệm cận ngang $y = {y1}$, $y = {y2}$ và $1$ tiệm cận đứng $x = {x0}$. \\
Vậy đồ thị hàm số có tổng cộng $3$ đường tiệm cận.'''
    return caudan, choices, loi_giai


def CuoiChuong1_MC_Cau40():
    # Biện luận số nghiệm k*f(x) + m = 0 từ đồ thị
    k = random.choice([2, 3, 4, 5])
    y_shift = random.choice([-3, -2, -1, 1, 2])
    # cực đại tại y_cd = y_shift + 2, cực tiểu tại y_ct = y_shift - 2
    y_cd = y_shift + 2
    y_ct = y_shift - 2

    # f(x) = c_val với c_val = -m/k
    c_val = y_shift
    m = -k * c_val # f(x) = c_val nằm giữa y_ct và y_cd => 3 nghiệm
    m_sign = f"+ {m}" if m > 0 else f"- {abs(m)}"

    caudan = fr'''\immini{{Cho hàm số $y=f(x)$ có đồ thị như hình vẽ bên với cực đại $y_{{cd}} = {y_cd}$ và cực tiểu $y_{{ct}} = {y_ct}$. Phương trình ${k}f(x) {m_sign} = 0$ có bao nhiêu nghiệm thực?}}
{{\begin{{tikzpicture}}[scale=0.5, line join=round, line cap=round, >=stealth]
	\def\xmin{{-2.2}}\def\xmax{{2.2}}\def\ymin{{{y_ct - 2}}}\def\ymax{{{y_cd + 2}}}
	\draw[->] (\xmin-0.2,0)--(\xmax+0.2,0) node[below]{{$x$}};
	\draw[->] (0,\ymin-0.2)--(0,\ymax+0.2) node[right]{{$y$}};
	\draw (0,0) node[below left]{{$O$}};
	\clip (\xmin,\ymin) rectangle (\xmax,\ymax);
	\draw[thick,smooth,samples=200,domain=\xmin:\xmax] plot (\x,{{-((\x)^3) + 3*(\x) + {y_shift}}});
\end{{tikzpicture}}}}'''
    correct = r'''$3$'''
    wrongs = [r'''$1$''', r'''$2$''', r'''$0$''']
    choices = shuffle_choices(correct, wrongs)
    loi_giai = fr'''Phương trình tương đương $f(x) = {c_val}$. \\
Vì ${y_ct} < {c_val} < {y_cd}$ nên đường thẳng $y = {c_val}$ cắt đồ thị tại đúng $3$ điểm phân biệt. \\
Vậy phương trình có đúng $3$ nghiệm thực.'''
    return caudan, choices, loi_giai


def CuoiChuong1_MC_Cau41():
    # Độ dài đoạn nối 2 cực trị của hàm bậc ba y = x^3 - 3*a^2*x + b
    a = random.choice([1, 2])
    b = random.randint(-5, 5)
    # A(-a; 2a^3 + b), B(a; -2a^3 + b)
    # AB = sqrt( (2a)^2 + (4a^3)^2 ) = 2a * sqrt(1 + 4a^4)
    inside = 1 + 4 * (a**4)
    coeff = 2 * a
    ans_tex = fr"{coeff}\sqrt{{{inside}}}" if inside not in [1, 4, 9, 16] else str(coeff * int(math.sqrt(inside)))

    c_x = 3 * (a**2)
    caudan = fr'''Cho hàm số $y = x^3 - {c_x}x {"+" if b > 0 else "-"} {abs(b)}$. Biết đồ thị hàm số có hai điểm cực trị $A$ và $B$. Khi đó độ dài đoạn thẳng $AB$ bằng'''
    correct = fr"${ans_tex}$"
    wrongs = [
        fr"${coeff}\sqrt{{{inside + 2}}}$",
        fr"${coeff + 2}$",
        fr"${inside}$"
    ]
    choices = shuffle_choices(correct, wrongs)
    loi_giai = fr'''Đạo hàm $y' = 3x^2 - {c_x} = 0 \iff x = \pm {a}$. \\
Tọa độ hai điểm cực trị là $A(-{a}; {2*(a**3) + b})$ và $B({a}; {-2*(a**3) + b})$. \\
Độ dài $AB = \sqrt{{({a} - (-{a}))^2 + ({-2*(a**3) + b} - ({2*(a**3) + b}))^2}} = {ans_tex}$.'''
    return caudan, choices, loi_giai


def CuoiChuong1_MC_Cau42():
    # Nhận dạng hàm bậc ba từ đồ thị
    k = random.choice([1, -1])
    d = random.choice([-3, -2, -1, 1, 2, 3])
    # y = k*(x^3 - 3x) + d
    formula = fr"{k}*((\x)^3) - {3*k}*(\x) {"+" if d > 0 else "-"} {abs(d)}"
    func_tex = fr"y = {k if k == -1 else ''}x^3 - {3*k if k == 1 else -3}x {"+" if d > 0 else "-"} {abs(d)}".replace("--", "+").replace(" 1x", " x").replace("-1x", "-x")

    caudan = fr'''\immini{{Đường cong trong hình bên là đồ thị của hàm số nào dưới đây?}}
{{\begin{{tikzpicture}}[scale=0.5, line join=round, line cap=round, >=stealth]
	\def\xmin{{-2.5}}\def\xmax{{2.5}}\def\ymin{{-5.5}}\def\ymax{{5.5}}
	\draw[->] (\xmin-0.2,0)--(\xmax+0.2,0) node[below]{{$x$}};
	\draw[->] (0,\ymin-0.2)--(0,\ymax+0.2) node[right]{{$y$}};
	\draw (0,0) node[below left]{{$O$}};
	\clip (\xmin,\ymin) rectangle (\xmax,\ymax);
	\draw[thick,smooth,samples=200,domain=\xmin:\xmax] plot (\x,{{{formula}}});
\end{{tikzpicture}}}}'''
    correct = fr"${func_tex}$"
    wrongs = [
        fr"$y = {-k if -k == -1 else ''}x^3 - {3*k}x {"+" if d > 0 else "-"} {abs(d)}$",
        fr"$y = {k if k == -1 else ''}x^3 + {3*k}x {"+" if d > 0 else "-"} {abs(d)}$",
        fr"$y = {k if k == -1 else ''}x^3 - {3*k}x {"-" if d > 0 else "+"} {abs(d)}$"
    ]
    choices = shuffle_choices(correct, wrongs)
    loi_giai = fr'''Dựa vào dáng điệu đồ thị và giao điểm với trục tung tại $(0; {d})$, hàm số phù hợp là ${func_tex}$.'''
    return caudan, choices, loi_giai


def CuoiChuong1_MC_Cau46():
    # GTLN của f(x) = x^3 - 3k^2 x + d trên [-m; m]
    k = random.choice([1, 2])
    d = random.randint(-5, 5)
    m = k + 2
    c_coeff = 3 * (k**2)
    max_val = m**3 - c_coeff * m + d

    caudan = fr'''Giá trị lớn nhất của hàm số $f(x) = x^3 - {c_coeff}x {"+" if d > 0 else "-"} {abs(d)}$ trên đoạn $[{-m}; {m}]$ bằng'''
    correct = fr"${max_val}$"
    wrongs = [fr"${-m**3 + c_coeff * m + d}$", fr"${d}$", fr"${max_val - 6}$"]
    choices = shuffle_choices(correct, wrongs)
    loi_giai = fr'''Khảo sát hàm số trên $[{-m}; {m}]$: $f'(x) = 3x^2 - {c_coeff} = 0 \iff x = \pm {k}$. \\
So sánh các giá trị tại các điểm tới hạn và hai đầu mút, ta được giá trị lớn nhất là $f({m}) = {max_val}$.'''
    return caudan, choices, loi_giai


def CuoiChuong1_MC_Cau47():
    # GTLN từ đồ thị hàm bậc ba trên [0; m]
    x_cd = random.choice([1, 2])
    y_cd = random.randint(2, 8)
    m = x_cd + 1
    formula = fr"-1*((\x - {x_cd})^3) + 3*(\x - {x_cd}) + {y_cd - 2}" if x_cd == 1 else fr"-1*((\x)^3) + 3*((\x)^2) + {y_cd - 4}"

    caudan = fr'''\immini{{Cho hàm số $y=f(x)$ có đồ thị như hình bên với điểm cực đại là $({x_cd}; {y_cd})$. Giá trị lớn nhất của hàm số $f(x)$ trên đoạn $[0; {m}]$ là}}
{{\begin{{tikzpicture}}[scale=0.55, line join=round, line cap=round, >=stealth,font=\footnotesize]
	\def\xmin{{-1.2}}\def\xmax{{{m + 1.5}}}\def\ymin{{-2.5}}\def\ymax{{{y_cd + 2}}}
	\draw[->] (\xmin-0.2,0)--(\xmax+0.2,0) node[below]{{$x$}};
	\draw[->] (0,\ymin-0.2)--(0,\ymax+0.2) node[right]{{$y$}};
	\draw (0,0) node[below left]{{$O$}};
	\clip (\xmin,\ymin) rectangle (\xmax,\ymax);
	\draw[thick,smooth,samples=200,domain=\xmin:\xmax] plot (\x,{{{formula}}});
	\draw[dashed] ({x_cd},0)--({x_cd},{y_cd})--(0,{y_cd});\fill ({x_cd},{y_cd}) circle(1.5pt);
\end{{tikzpicture}}}}'''
    correct = fr"$\max\limits_{{[0; {m}]}} f(x) = {y_cd}$"
    wrongs = [
        fr"$\max\limits_{{[0; {m}]}} f(x) = {-y_cd}$",
        fr"$\max\limits_{{[0; {m}]}} f(x) = {x_cd}$",
        fr"$\max\limits_{{[0; {m}]}} f(x) = 0$"
    ]
    choices = shuffle_choices(correct, wrongs)
    loi_giai = fr'''Quan sát đồ thị trên đoạn $[0; {m}]$, điểm cao nhất là điểm cực đại $({x_cd}; {y_cd})$. \\
Do đó $\max\limits_{{[0; {m}]}} f(x) = {y_cd}$ tại $x = {x_cd}$.'''
    return caudan, choices, loi_giai


def CuoiChuong1_MC_Cau49():
    # Nhận dạng hàm bậc ba từ BBT
    x_ct = random.choice([1, 2, 3])
    x_cd = 0
    y_cd = random.choice([2, 3, 4])
    y_ct = y_cd - random.choice([3, 4, 5])
    k_sq = Fraction(3 * (y_cd - y_ct), x_ct**3)
    
    caudan = fr'''\immini{{Bảng biến thiên bên dưới là của một trong bốn hàm số được liệt kê ở các phương án. Hàm số đó là}}
{{\begin{{tikzpicture}}
	\tkzTabInit[nocadre,lgt=1.2,espcl=1.5,deltacl=0.6]
	{{$x$ /0.6, $y'$ /0.6, $y$ /1.5}}
	{{$-\infty$,${x_cd}$,${x_ct}$,$+\infty$}}
	\tkzTabLine{{,+,$0$,-,$0$,+,}}
	\tkzTabVar{{-/$-\infty$,+/${y_cd}$,-/${y_ct}$,+/$+\infty$}}
\end{{tikzpicture}}}}'''
    correct = fr"$y = x^3 - {3*x_ct//2 if (3*x_ct)%2==0 else 3}x^2 + {y_cd}$"
    wrongs = [
        fr"$y = -x^3 + 3x^2 + {y_cd}$",
        fr"$y = x^4 - 2x^2 + {y_cd}$",
        fr"$y = x^3 + 3x^2 + {y_cd}$"
    ]
    choices = shuffle_choices(correct, wrongs)
    loi_giai = fr'''Bảng biến thiên có điểm cực đại là $(0; {y_cd})$ và điểm cực tiểu tại $x = {x_ct}$. \\
Hàm số bậc ba thỏa mãn điều kiện trên là ${correct}$.'''
    return caudan, choices, loi_giai


def CuoiChuong1_MC_Cau48():
    x0 = random.choice([-7, -6, -5, -4, -3, -2, -1, 1, 2, 3, 4, 5, 6, 7])
    a = random.choice([2, 3, 4, -1, -2, -3])
    b = random.choice([1, 3, 5, -1, -3])
    sign_x0 = f"+ {x0}" if x0 > 0 else f"- {abs(x0)}"
    tc_d = -x0
    caudan = fr'''Đường thẳng nào dưới đây là tiệm cận đứng của đồ thị hàm số $y = \dfrac{{{fmt_linear(a, b)}}}{{x {sign_x0}}}$?'''
    correct = fr"$x = {tc_d}$"
    wrongs = [
        fr"$x = {x0}$",
        fr"$y = {a}$",
        fr"$y = {tc_d}$"
    ]
    choices = shuffle_choices(correct, wrongs)
    loi_giai = fr'''Nghiệm của mẫu số là $x {sign_x0} = 0 \iff x = {tc_d}$. \\
Vậy đường thẳng $x = {tc_d}$ là tiệm cận đứng của đồ thị hàm số.'''
    return caudan, choices, loi_giai


def CuoiChuong1_MC_Cau50():
    # Số điểm cực trị của hàm phân thức bậc 2 trên 1
    d = random.choice([-3, -2, -1, 1, 2, 3])
    b = random.choice([-2, -1, 0, 1, 2])
    c = random.choice([1, 2, 3, 4, 5])
    delta = d**2 - b*d + c
    ans = 2 if delta > 0 else 0
    num_str = f"x^2 {'+ ' + str(b) if b > 0 else ('- ' + str(abs(b)) if b < 0 else '')}x {'+ ' + str(c) if c > 0 else '- ' + str(abs(c))}".replace(" 1x", " x")
    sign_d = f"+ {d}" if d > 0 else f"- {abs(d)}"
    caudan = fr'''Hàm số $f(x) = \dfrac{{{num_str}}}{{x {sign_d}}}$ có bao nhiêu điểm cực trị?'''
    correct = fr"${ans}$"
    wrongs = [str(x) for x in [0, 1, 2, 3] if x != ans][:3]
    choices = shuffle_choices(correct, [fr"${w}$" for w in wrongs])
    loi_giai = fr'''Ta có $f'(x) = \dfrac{{x^2 + {2*d}x + {b*d - c}}}{{(x {sign_d})^2}}$. \\
Phương trình $f'(x) = 0$ có biệt thức $\Delta' = {delta} > 0$ nên có $2$ nghiệm phân biệt khác ${-d}$. \\
Đạo hàm đổi dấu qua cả hai nghiệm đó nên hàm số có đúng ${ans}$ điểm cực trị.'''
    return caudan, choices, loi_giai





def CuoiChuong1_MC_Cau53():
    # GTNN của f(x) = x^3 - 3k^2 x + d trên [-m; m]
    k = random.choice([1, 2])
    d = random.randint(-5, 5)
    m = k + 2
    c_coeff = 3 * (k**2)
    min_val = -m**3 + c_coeff * m + d

    caudan = fr'''Giá trị nhỏ nhất của hàm số $f(x) = x^3 - {c_coeff}x {"+" if d > 0 else "-"} {abs(d)}$ trên đoạn $[{-m}; {m}]$ bằng'''
    correct = fr"${min_val}$"
    wrongs = [fr"${d}$", fr"${min_val + 16}$", fr"${min_val - 4}$"]
    choices = shuffle_choices(correct, wrongs)
    loi_giai = fr'''Khảo sát hàm số trên đoạn $[{-m}; {m}]$: $f'(x) = 3x^2 - {c_coeff} = 0 \iff x = \pm {k}$. \\
So sánh các giá trị tại $x = \pm {k}$ và $x = \pm {m}$, ta được $\min f(x) = f({-m}) = {min_val}$.'''
    return caudan, choices, loi_giai


def CuoiChuong1_MC_Cau56():
    # GTNN của y = x^3 + 3k x^2 + c trên [-1; 2]
    k = random.choice([1, 2, 3])
    c = random.randint(-4, 4)
    y_neg1 = -1 + 3 * k + c
    y_0 = c
    y_2 = 8 + 12 * k + c
    min_val = min(y_neg1, y_0, y_2)

    caudan = fr'''Giá trị nhỏ nhất của hàm số $y = x^3 + {3*k}x^2 {"+" if c > 0 else "-"} {abs(c)}$ trên đoạn $[-1; 2]$ bằng'''
    correct = fr"${min_val}$"
    wrongs = [fr"${y_neg1}$", fr"${y_2}$", fr"${min_val - 5}$"]
    if correct in wrongs:
        wrongs.remove(correct)
        wrongs.append(fr"${min_val + 3}$")
    choices = shuffle_choices(correct, wrongs[:3])
    loi_giai = fr'''Ta có $y' = 3x^2 + {6*k}x = 3x(x + {2*k}) = 0 \iff x = 0 \in [-1; 2]$. \\
So sánh $y(-1) = {y_neg1}, y(0) = {y_0}, y(2) = {y_2}$, ta được giá trị nhỏ nhất bằng ${min_val}$.'''
    return caudan, choices, loi_giai


def CuoiChuong1_MC_Cau57():
    # Điểm cực đại của đồ thị hàm số từ đồ thị bậc ba hoàn chỉnh
    configs = [
        (1, 0, -3, 1, -1, 3, 1, -1),
        (1, 0, -3, 2, -1, 4, 1, 0),
        (-1, 0, 3, 1, 1, 3, -1, -1),
        (-1, 0, 3, 0, 1, 2, -1, -2),
        (1, -3, 0, 3, 0, 3, 2, -1),
        (1, 3, 0, -1, -2, 3, 0, -1),
    ]
    a, b, c, d, x_cd, y_cd, x_ct, y_ct = random.choice(configs)
    xmin = min(-2.5, x_cd - 1.2, x_ct - 1.2)
    xmax = max(2.5, x_cd + 1.2, x_ct + 1.2)
    ymin = min(-3.2, y_cd - 1.2, y_ct - 1.2)
    ymax = max(3.8, y_cd + 1.2, y_ct + 1.2)

    poly = f"{a}*(\\x)^3" + (f" + {b}*(\\x)^2" if b > 0 else (f" - {abs(b)}*(\\x)^2" if b < 0 else "")) + (f" + {c}*(\\x)" if c > 0 else (f" - {abs(c)}*(\\x)" if c < 0 else "")) + (f" + {d}" if d > 0 else (f" - {abs(d)}" if d < 0 else ""))

    pt_cd = f"\\draw[dashed] ({x_cd},0) node[below]{{${x_cd}$}} -- ({x_cd},{y_cd}) -- (0,{y_cd}) node[left]{{${y_cd}$}};\n  \\fill ({x_cd},{y_cd}) circle(1.5pt);" if (x_cd != 0 and y_cd != 0) else (f"\\fill (0,{y_cd}) circle(1.5pt) node[above left]{{${y_cd}$}};" if x_cd == 0 else f"\\fill ({x_cd},0) circle(1.5pt) node[below]{{${x_cd}$}};")
    pt_ct = f"\\draw[dashed] ({x_ct},0) node[below]{{${x_ct}$}} -- ({x_ct},{y_ct}) -- (0,{y_ct}) node[left]{{${y_ct}$}};\n  \\fill ({x_ct},{y_ct}) circle(1.5pt);" if (x_ct != 0 and y_ct != 0) else (f"\\fill (0,{y_ct}) circle(1.5pt) node[above left]{{${y_ct}$}};" if x_ct == 0 else f"\\fill ({x_ct},0) circle(1.5pt) node[below]{{${x_ct}$}};")

    caudan = fr'''\immini{{Cho hàm số bậc ba $y = f(x)$ có đồ thị như hình vẽ bên. Điểm cực đại của đồ thị hàm số đã cho có tọa độ là}}
{{\begin{{tikzpicture}}[line join=round, line cap=round, >=stealth, scale=0.6, font=\footnotesize]
  \def\xmin{{{xmin:.1f}}}\def\xmax{{{xmax:.1f}}}\def\ymin{{{ymin:.1f}}}\def\ymax{{{ymax:.1f}}}
  \draw[->] (\xmin-0.2,0) -- (\xmax+0.2,0) node[below] {{$x$}};
  \draw[->] (0,\ymin-0.2) -- (0,\ymax+0.2) node[left] {{$y$}};
  \draw (0,0) node[below left] {{$O$}};
  \begin{{scope}}
  \clip (\xmin,\ymin) rectangle (\xmax,\ymax);
  \draw[thick, smooth, samples=150, domain=\xmin:\xmax] plot (\x, {{ {poly} }});
  \end{{scope}}
  {pt_cd}
  {pt_ct}
\end{{tikzpicture}}}}'''
    correct = fr"$({x_cd}; {y_cd})$"
    wrongs = [fr"$({x_ct}; {y_ct})$", fr"$({y_cd}; {x_cd})$", fr"$({-x_cd}; {y_cd})$"]
    choices = shuffle_choices(correct, wrongs)
    loi_giai = fr'''Dựa vào đồ thị hàm số, điểm cực đại của đồ thị hàm số có tọa độ là $({x_cd}; {y_cd})$.'''
    return caudan, choices, loi_giai


def CuoiChuong1_MC_Cau58():
    # Số đường tiệm cận ngang từ BBT ngẫu nhiên hóa
    case = random.choice([1, 2, 0])
    if case == 1:
        y1 = random.choice([-3, -2, -1, 1, 2, 3])
        caudan = fr'''Cho hàm số $y = f(x)$ có $\lim\limits_{{x \to -\infty}} f(x) = {y1}$ và $\lim\limits_{{x \to +\infty}} f(x) = +\infty$. Số đường tiệm cận ngang của đồ thị hàm số đã cho là'''
        correct = r'''$1$'''
        wrongs = [r'''$0$''', r'''$2$''', r'''$3$''']
        exp = fr"Chỉ có $y = {y1}$ là đường tiệm cận ngang khi $x \to -\infty$."
    elif case == 2:
        y1 = random.choice([-3, -2, -1])
        y2 = random.choice([1, 2, 3])
        caudan = fr'''Cho hàm số $y = f(x)$ có $\lim\limits_{{x \to -\infty}} f(x) = {y1}$ và $\lim\limits_{{x \to +\infty}} f(x) = {y2}$. Số đường tiệm cận ngang của đồ thị hàm số đã cho là'''
        correct = r'''$2$'''
        wrongs = [r'''$0$''', r'''$1$''', r'''$3$''']
        exp = fr"Có $2$ tiệm cận ngang là $y = {y1}$ và $y = {y2}$."
    else:
        caudan = r'''Cho hàm số $y = f(x)$ có $\lim\limits_{x \to -\infty} f(x) = -\infty$ và $\lim\limits_{x \to +\infty} f(x) = +\infty$. Số đường tiệm cận ngang của đồ thị hàm số đã cho là'''
        correct = r'''$0$'''
        wrongs = [r'''$1$''', r'''$2$''', r'''$3$''']
        exp = "Cả hai giới hạn đều ra vô cực nên đồ thị không có tiệm cận ngang."

    choices = shuffle_choices(correct, wrongs)
    loi_giai = fr'''Dựa vào định nghĩa đường tiệm cận ngang: {exp} Vậy đồ thị có {correct} đường tiệm cận ngang.'''
    return caudan, choices, loi_giai


def CuoiChuong1_MC_Cau59():
    # Tâm đối xứng đồ thị hàm phân thức
    x0 = random.choice([-4, -3, -2, -1, 1, 2, 3, 4])
    y0 = random.choice([-3, -2, -1, 1, 2, 3])

    caudan = fr'''Cho hàm số $y = \dfrac{{ax + b}}{{cx + d}}$ có đồ thị nhận đường tiệm cận đứng $x = {x0}$ và tiệm cận ngang $y = {y0}$. Tọa độ tâm đối xứng của đồ thị hàm số đã cho là'''
    correct = fr"$({x0}; {y0})$"
    wrongs = [
        fr"$(0; {y0})$",
        fr"$({x0}; 0)$",
        fr"$({y0}; {x0})$"
    ]
    choices = shuffle_choices(correct, wrongs)
    loi_giai = fr'''Tâm đối xứng của đồ thị hàm phân thức bậc nhất trên bậc nhất là giao điểm của hai đường tiệm cận: $I({x0}; {y0})$.'''
    return caudan, choices, loi_giai


def CuoiChuong1_MC_Cau61():
    # Thể tích nước giảm trong khoảng nhiệt độ ngẫu nhiên hóa
    T1 = random.choice(["3,97", "3,85", "4,00", "4,12", "3,75"])

    caudan = fr'''Thể tích $V$ (đơn vị: $\text{{cm}}^3$) của $1\text{{ kg}}$ nước tại nhiệt độ $T$ (đơn vị: $^\circ\text{{C}}$) được tính bởi hàm số $V(T)$, $T \in [0; 30]$. Biết hàm số $V(T)$ giảm từ $0^\circ\text{{C}}$ đến $T_1 \approx {T1}^\circ\text{{C}}$ và tăng từ $T_1$ đến $30^\circ\text{{C}}$. Hỏi thể tích $V(T)$ giảm trong khoảng nhiệt độ nào?'''
    correct = fr"$(0; {T1})$"
    wrongs = [
        r"$(0; 5)$",
        r"$(0; 10)$",
        r"$(0; 30)$"
    ]
    choices = shuffle_choices(correct, wrongs)
    loi_giai = fr'''Hàm số nghịch biến trên khoảng mà thể tích giảm, tức $(0; T_1) = (0; {T1})$.'''
    return caudan, choices, loi_giai


def CuoiChuong1_MC_Cau62():
    # Khẳng định sai về hàm bậc ba ngẫu nhiên hóa
    k = random.choice([1, 2])
    c = random.randint(-4, 4)
    # y = x^3 - 3k^2 x + c => cd(-k; 2k^3 + c), ct(k; -2k^3 + c)
    y_cd = 2 * (k**3) + c
    y_ct = -2 * (k**3) + c

    wrong_val = y_ct + 5
    wrong_stmt = fr"Giá trị cực tiểu của hàm số bằng ${wrong_val}$"

    caudan = fr'''Cho hàm số $y = x^3 - {3*(k**2)}x {"+" if c > 0 else "-"} {abs(c)}$. Khẳng định nào sau đây là sai?'''
    correct = wrong_stmt
    wrongs = [
        fr"Hàm số đạt cực tiểu tại $x = {k}$",
        fr"Hàm số đạt cực đại tại $x = {-k}$",
        fr"Giá trị cực đại của hàm số bằng ${y_cd}$"
    ]
    choices = shuffle_choices(correct, wrongs)
    loi_giai = fr'''Ta có $y' = 3x^2 - {3*(k**2)} = 0 \iff x = \pm {k}$. \\
Điểm cực đại là $({-k}; {y_cd})$, điểm cực tiểu là $({k}; {y_ct})$. \\
Giá trị cực tiểu đúng là $y = {y_ct} \ne {wrong_val}$. Khẳng định "{correct}" là SAI.'''
    return caudan, choices, loi_giai


def CuoiChuong1_MC_Cau65():
    # Điểm cực tiểu của đồ thị hàm số từ đồ thị bậc ba hoàn chỉnh
    configs = [
        (1, 0, -3, 0, -1, 2, 1, -2),
        (1, 0, -3, 1, -1, 3, 1, -1),
        (-1, 0, 3, 0, 1, 2, -1, -2),
        (-1, 0, 3, -1, 1, 1, -1, -3),
        (1, -3, 0, 2, 0, 2, 2, -2),
        (-1, 3, 0, -2, 2, 2, 0, -2),
    ]
    a, b, c, d, x_cd, y_cd, x_ct, y_ct = random.choice(configs)
    xmin = min(-2.5, x_cd - 1.2, x_ct - 1.2)
    xmax = max(2.5, x_cd + 1.2, x_ct + 1.2)
    ymin = min(-3.2, y_cd - 1.2, y_ct - 1.2)
    ymax = max(3.8, y_cd + 1.2, y_ct + 1.2)

    poly = f"{a}*(\\x)^3" + (f" + {b}*(\\x)^2" if b > 0 else (f" - {abs(b)}*(\\x)^2" if b < 0 else "")) + (f" + {c}*(\\x)" if c > 0 else (f" - {abs(c)}*(\\x)" if c < 0 else "")) + (f" + {d}" if d > 0 else (f" - {abs(d)}" if d < 0 else ""))

    pt_cd = f"\\draw[dashed] ({x_cd},0) node[below]{{${x_cd}$}} -- ({x_cd},{y_cd}) -- (0,{y_cd}) node[left]{{${y_cd}$}};\n  \\fill ({x_cd},{y_cd}) circle(1.5pt);" if (x_cd != 0 and y_cd != 0) else (f"\\fill (0,{y_cd}) circle(1.5pt) node[above left]{{${y_cd}$}};" if x_cd == 0 else f"\\fill ({x_cd},0) circle(1.5pt) node[below]{{${x_cd}$}};")
    pt_ct = f"\\draw[dashed] ({x_ct},0) node[below]{{${x_ct}$}} -- ({x_ct},{y_ct}) -- (0,{y_ct}) node[left]{{${y_ct}$}};\n  \\fill ({x_ct},{y_ct}) circle(1.5pt);" if (x_ct != 0 and y_ct != 0) else (f"\\fill (0,{y_ct}) circle(1.5pt) node[above left]{{${y_ct}$}};" if x_ct == 0 else f"\\fill ({x_ct},0) circle(1.5pt) node[below]{{${x_ct}$}};")

    caudan = fr'''\immini{{Cho hàm số bậc ba $y = f(x)$ có đồ thị như hình vẽ bên. Điểm cực tiểu của đồ thị hàm số đã cho có tọa độ là}}
{{\begin{{tikzpicture}}[line join=round, line cap=round, >=stealth, scale=0.6, font=\footnotesize]
  \def\xmin{{{xmin:.1f}}}\def\xmax{{{xmax:.1f}}}\def\ymin{{{ymin:.1f}}}\def\ymax{{{ymax:.1f}}}
  \draw[->] (\xmin-0.2,0) -- (\xmax+0.2,0) node[below] {{$x$}};
  \draw[->] (0,\ymin-0.2) -- (0,\ymax+0.2) node[left] {{$y$}};
  \draw (0,0) node[below left] {{$O$}};
  \begin{{scope}}
  \clip (\xmin,\ymin) rectangle (\xmax,\ymax);
  \draw[thick, smooth, samples=150, domain=\xmin:\xmax] plot (\x, {{ {poly} }});
  \end{{scope}}
  {pt_cd}
  {pt_ct}
\end{{tikzpicture}}}}'''
    correct = fr"$({x_ct}; {y_ct})$"
    wrongs = [fr"$({x_cd}; {y_cd})$", fr"$({y_ct}; {x_ct})$", fr"$({-x_ct}; {y_ct})$"]
    choices = shuffle_choices(correct, wrongs)
    loi_giai = fr'''Dựa vào đồ thị hàm số, điểm cực tiểu của đồ thị hàm số có tọa độ là $({x_ct}; {y_ct})$.'''
    return caudan, choices, loi_giai


def CuoiChuong1_MC_Cau66():
    # Tiệm cận ngang từ bảng biến thiên ngẫu nhiên hóa
    y0 = random.choice([-4, -3, -2, -1, 1, 2, 3, 4])
    x0 = random.choice([-3, -2, -1, 1, 2, 3])

    caudan = fr'''\immini{{Cho hàm số $y = f(x)$ có bảng biến thiên như hình bên. Đường tiệm cận ngang của đồ thị hàm số đã cho có phương trình là}}
{{\begin{{tikzpicture}}
\tkzTabInit[nocadre,lgt=1.2,espcl=2,deltacl=0.5]{{$x$ / 0.6, $y'$ / 0.6, $y$ / 2}}{{$-\infty$, ${x0}$, $+\infty$}}
\tkzTabLine{{ , -, d, -, }}
\tkzTabVar{{+/ ${y0}$, -D+/ $-\infty$ / $+\infty$, -/ ${y0}$}}
\end{{tikzpicture}}}}'''
    correct = fr"$y = {y0}$"
    wrongs = [fr"$x = {x0}$", fr"$x = {y0}$", fr"$y = {x0}$"]
    choices = shuffle_choices(correct, wrongs)
    loi_giai = fr'''Từ bảng biến thiên, ta có $\lim\limits_{{x \to -\infty}} y = {y0}$ và $\lim\limits_{{x \to +\infty}} y = {y0}$ nên đường thẳng $y = {y0}$ là đường tiệm cận ngang của đồ thị hàm số.'''
    return caudan, choices, loi_giai


def CuoiChuong1_MC_Cau33():
    # Tiệm cận xiên của hàm phân thức bậc 2 trên bậc 1
    a = random.choice([1, 2, 3])
    b = random.choice([-3, -2, -1, 1, 2, 3])
    x0 = random.choice([-2, -1, 1, 2])
    r = random.choice([-3, -2, -1, 1, 2, 3])
    
    c1 = a
    c2 = b - a * x0
    c3 = -b * x0 + r
    
    sign_c2 = f"+ {c2}x" if c2 > 0 else (f"- {abs(c2)}x" if c2 < 0 else "")
    sign_c3 = f"+ {c3}" if c3 > 0 else (f"- {abs(c3)}" if c3 < 0 else "")
    sign_x0 = f"- {x0}" if x0 > 0 else f"+ {abs(x0)}"
    lin_str = fmt_linear(a, b)

    caudan = fr'''Cho hàm số $y = \dfrac{{{c1}x^2 {sign_c2} {sign_c3}}}{{x {sign_x0}}}$. Tiệm cận xiên của đồ thị hàm số là đường thẳng'''
    correct = fr"$y = {lin_str}$"
    wrongs = [
        fr"$y = {fmt_linear(a, -b)}$",
        fr"$y = {fmt_linear(-a, b)}$",
        fr"$y = {fmt_linear(a, b + 2)}$"
    ]
    choices = shuffle_choices(correct, wrongs)
    loi_giai = fr'''Chia đa thức: $\dfrac{{{c1}x^2 {sign_c2} {sign_c3}}}{{x {sign_x0}}} = {lin_str} + \dfrac{{{r}}}{{x {sign_x0}}}$. \\
Vì $\lim\limits_{{x \to \pm\infty}} \dfrac{{{r}}}{{x {sign_x0}}} = 0$ nên tiệm cận xiên của đồ thị hàm số là đường thẳng $y = {lin_str}$.'''
    return caudan, choices, loi_giai


def CuoiChuong1_MC_Cau43():
    # Khoảng nghịch biến hàm số từ BBT
    x1 = random.choice([-4, -3, -2, -1])
    x2 = random.choice([1, 2, 3, 4])
    y_cd = random.choice([2, 3, 4, 5])
    y_ct = random.choice([-5, -4, -3, -2, -1])

    caudan = fr'''\immini{{Cho hàm số $y=f(x)$ có bảng biến thiên như sau. Hàm số đã cho nghịch biến trên khoảng nào dưới đây?}}
{{\begin{{tikzpicture}}
	\tkzTabInit[nocadre,lgt=1.2,espcl=1.5,deltacl=0.6]
	{{$x$ /0.6, $y'$ /0.6, $y$ /1.5}}
	{{$-\infty$,${x1}$,${x2}$,$+\infty$}}
	\tkzTabLine{{,+,$0$,-,$0$,+,}}
	\tkzTabVar{{-/$-\infty$,+/${y_cd}$,-/${y_ct}$,+/$+\infty$}}
\end{{tikzpicture}}}}'''
    correct = fr"$({x1}; {x2})$"
    wrongs = [
        fr"$({x1}; +\infty)$",
        fr"$({x2}; +\infty)$",
        fr"$(-\infty; {x1})$"
    ]
    choices = shuffle_choices(correct, wrongs)
    loi_giai = fr'''Từ bảng biến thiên, ta thấy $y' < 0$ trên khoảng $({x1}; {x2})$. \\
Do đó hàm số nghịch biến trên khoảng $({x1}; {x2})$.'''
    return caudan, choices, loi_giai


def CuoiChuong1_MC_Cau45():
    # Khoảng đồng biến từ công thức đạo hàm
    a = random.choice([-3, -2, -1, 0])
    b = random.choice([1, 2])
    c = b + random.choice([1, 2, 3])

    caudan = fr'''Cho hàm số $f(x)$ có đạo hàm $f'(x) = (x {"+" if -a > 0 else "-"} {abs(a)})^2(x - {b})^3({c} - x)$. Hàm số $f(x)$ đồng biến trong khoảng nào dưới đây?'''
    correct = fr"$({b}; {c})$"
    wrongs = [
        fr"$(-\infty; {a})$",
        fr"$({a}; {b})$",
        fr"$({c}; +\infty)$"
    ]
    choices = shuffle_choices(correct, wrongs)
    loi_giai = fr'''Vì $(x {"+" if -a > 0 else "-"} {abs(a)})^2 \ge 0, \forall x$ nên dấu của $f'(x)$ cùng dấu với $(x - {b})({c} - x)$. \\
$f'(x) > 0 \iff (x - {b})({c} - x) > 0 \iff {b} < x < {c}$. \\
Vậy hàm số đồng biến trên khoảng $({b}; {c})$.'''
    return caudan, choices, loi_giai


def CuoiChuong1_MC_Cau51():
    # Khoảng đồng biến của hàm bậc ba
    k = random.choice([2, 3, 4, 5, 6])
    c = random.randint(1, 8)
    k_str = f"+ {k//2}x^2" if k % 2 == 0 else fr"+ \dfrac{{{k}}}{{2}}x^2"

    caudan = fr'''Cho hàm số $y = -\dfrac{{x^3}}{{3}} {k_str} + {c}$. Hàm số đồng biến trên khoảng nào trong các khoảng sau đây?'''
    correct = fr"$(0; {k})$"
    wrongs = [
        fr"$({k}; +\infty)$",
        fr"$(0; +\infty)$",
        fr"$(-\infty; 0)$"
    ]
    choices = shuffle_choices(correct, wrongs)
    loi_giai = fr'''Ta có $y' = -x^2 + {k}x = -x(x - {k})$. \\
$y' > 0 \iff 0 < x < {k}$. \\
Vậy hàm số đồng biến trên khoảng $(0; {k})$.'''
    return caudan, choices, loi_giai


def CuoiChuong1_MC_Cau52():
    # Khoảng nghịch biến từ BBT có điểm gián đoạn
    x1 = random.choice([-8, -7, -6, -5])
    x_gap = random.choice([-4, -3, -2])
    x2 = random.choice([2, 3, 4, 5])
    y1 = random.choice([10, 12, 14, 16])
    y2 = random.choice([4, 6, 8])

    caudan = fr'''\immini{{Cho hàm số $y=f(x)$ có bảng biến thiên như hình bên. Hàm số nghịch biến trên các khoảng nào sau đây?}}
{{\begin{{tikzpicture}} 
	\tkzTabInit[nocadre,lgt=1.2,espcl=2,deltacl=0.6]
	{{$x$ /0.6,$y'$ /0.6,$y$ /1.5}}
	{{$-\infty$,${x1}$,${x_gap}$,${x2}$,$+\infty$}}
	\tkzTabLine{{,+,$0$,-,d,-,$0$,+,}}
	\tkzTabVar{{-/$-\infty$,+/${y1}$,-D+/$-\infty$/$+\infty$,-/${y2}$,+/$+\infty$}}
\end{{tikzpicture}}}}'''
    correct = fr"$({x1}; {x_gap})$ và $({x_gap}; {x2})$"
    wrongs = [
        fr"$({x1}; {x2})$",
        fr"$({x1}; +\infty)$",
        fr"$(-\infty; {x_gap})$"
    ]
    choices = shuffle_choices(correct, wrongs)
    loi_giai = fr'''Từ bảng biến thiên, ta thấy $y' < 0$ trên $({x1}; {x_gap})$ và $({x_gap}; {x2})$. \\
Vậy hàm số nghịch biến trên các khoảng $({x1}; {x_gap})$ và $({x_gap}; {x2})$.'''
    return caudan, choices, loi_giai


def CuoiChuong1_MC_Cau54():
    # Tọa độ tâm đối xứng hàm phân thức 1 trên 1
    a = random.choice([1, 2, 3, -1, -2, -3])
    d = random.choice([-4, -3, -2, 2, 3, 4])
    b = random.choice([1, 3, 5, -1, -3])
    x_tc = -d
    y_tc = a

    num_str = fmt_linear(a, b)
    den_str = fmt_linear(1, d)

    caudan = fr'''Cho hàm số $y = \dfrac{{{num_str}}}{{{den_str}}}$. Tâm đối xứng của đồ thị hàm số có tọa độ là'''
    correct = fr"$({x_tc}; {y_tc})$"
    wrongs = [
        fr"$({-x_tc}; {y_tc})$",
        fr"$({y_tc}; {x_tc})$",
        fr"$({x_tc}; {-y_tc})$"
    ]
    choices = shuffle_choices(correct, wrongs)
    loi_giai = fr'''Đồ thị hàm số có tiệm cận đứng $x = {x_tc}$ và tiệm cận ngang $y = {y_tc}$. \\
Tâm đối xứng là giao điểm của hai tiệm cận: $I({x_tc}; {y_tc})$.'''
    return caudan, choices, loi_giai


def CuoiChuong1_MC_Cau55():
    # Khoảng nghịch biến hàm số từ BBT dạng 2
    x1 = random.choice([-4, -3, -2, -1])
    x2 = random.choice([1, 2, 3, 4])
    y_cd = random.choice([6, 8, 10, 12])
    y_ct = random.choice([1, 2, 3, 4])

    caudan = fr'''\immini{{Cho hàm số $y = f(x)$ có bảng biến thiên như sau. Hàm số $y = f(x)$ nghịch biến trên khoảng nào?}}
{{\begin{{tikzpicture}}
  \tkzTabInit[nocadre,lgt=1.2,espcl=1.5,deltacl=0.5]
     {{$x$/0.7,$y'$/0.7,$y$/2}}
     {{$-\infty$,${x1}$,${x2}$,$+\infty$}}
  \tkzTabLine{{,+,0,-,0,+,}}
  \tkzTabVar{{-/$-\infty$,+/${y_cd}$,-/${y_ct}$,+/$+\infty$}}
\end{{tikzpicture}}}}'''
    correct = fr"$({x1}; {x2})$"
    wrongs = [
        fr"$({x2}; +\infty)$",
        fr"$(-\infty; {x2})$",
        fr"$({y_ct}; {y_cd})$"
    ]
    choices = shuffle_choices(correct, wrongs)
    loi_giai = fr'''Dựa vào bảng biến thiên, hàm số nghịch biến trên khoảng $({x1}; {x2})$ vì $y' < 0$ trên khoảng này.'''
    return caudan, choices, loi_giai


def CuoiChuong1_MC_Cau60():
    # Nhận biết hàm số không có cực trị
    a = random.choice([2, 3, 4, 5, -2, -3, -4])
    d = random.choice([1, 2, 3, 4, -1, -2, -3, -4])
    b = random.choice([1, -1, 2, -2, 3, -3, 5, -5])
    sign_b = f"+ {b}" if b > 0 else f"- {abs(b)}"
    sign_d = f"+ {d}" if d > 0 else f"- {abs(d)}"
    correct = fr"$y = \dfrac{{{a}x {sign_b}}}{{x {sign_d}}}$"
    
    stem_variants = [
        r'''Hàm số nào sau đây không có cực trị?''',
        r'''Hàm số nào dưới đây không có điểm cực trị?''',
        r'''Đồ thị hàm số nào sau đây không có điểm cực trị?''',
        r'''Trong các hàm số sau, hàm số nào không có cực trị?''',
        r'''Cho các hàm số sau, hàm số không có điểm cực trị là''',
        r'''Hàm số nào dưới đây đơn điệu trên từng khoảng xác định và không có cực trị?''',
        r'''Trong các hàm số dưới đây, hàm số nào không có điểm cực trị?''',
        r'''Khảo sát sự biến thiên của các hàm số, hàm số nào không có cực trị?'''
    ]
    caudan = random.choice(stem_variants)
    k = random.choice([1, 2, 3, 4])
    wrongs = [
        fr"$y = x^3 - {3*k}x + 1$",
        fr"$y = x^2 - {2*k}x + 1$",
        fr"$y = \dfrac{{x^2 + {k}}}{{x}}$"
    ]
    choices = shuffle_choices(correct, wrongs)
    loi_giai = fr'''Hàm số phân thức bậc nhất trên bậc nhất ${correct}$ có đạo hàm $y' = \dfrac{{{a*d - b}}}{{(x {sign_d})^2}}$ luôn cùng một dấu trên từng khoảng xác định nên không có cực trị.'''
    return caudan, choices, loi_giai


# ==============================================================================
# 12 DẠNG BÀI TẬP CHUẨN MA TRẬN ĐỀ THI CUỐI CHƯƠNG 1 (4 BÀI x 3 MỨC ĐỘ)
# ==============================================================================

def sinh_cau_cuc_tri_do_thi_bac_ba():
    """Sinh câu hỏi tìm điểm cực đại, điểm cực tiểu của đồ thị hàm số bậc 3 có 2 cực trị từ hình vẽ"""
    configs = [
        # a = 1, y = x^3 - 3x + d => x_cd = -1, x_ct = 1
        (1, 0, -3, 0, -1, 2, 1, -2),
        (1, 0, -3, 1, -1, 3, 1, -1),
        (1, 0, -3, -1, -1, 1, 1, -3),
        (1, 0, -3, 2, -1, 4, 1, 0),
        # a = -1, y = -x^3 + 3x + d => x_cd = 1, x_ct = -1
        (-1, 0, 3, 0, 1, 2, -1, -2),
        (-1, 0, 3, 1, 1, 3, -1, -1),
        (-1, 0, 3, -1, 1, 1, -1, -3),
        (-1, 0, 3, 2, 1, 4, -1, 0),
        # a = 1, y = x^3 - 3x^2 + d => x_cd = 0, x_ct = 2
        (1, -3, 0, 2, 0, 2, 2, -2),
        (1, -3, 0, 3, 0, 3, 2, -1),
        (1, -3, 0, 1, 0, 1, 2, -3),
        (1, -3, 0, 4, 0, 4, 2, 0),
        # a = -1, y = -x^3 + 3x^2 + d => x_cd = 2, x_ct = 0
        (-1, 3, 0, -2, 2, 2, 0, -2),
        (-1, 3, 0, -1, 2, 3, 0, -1),
        (-1, 3, 0, -3, 2, 1, 0, -3),
        (-1, 3, 0, 0, 2, 4, 0, 0),
        # a = 1, y = x^3 + 3x^2 + d => x_cd = -2, x_ct = 0
        (1, 3, 0, -2, -2, 2, 0, -2),
        (1, 3, 0, -1, -2, 3, 0, -1),
        (1, 3, 0, -3, -2, 1, 0, -3),
        (1, 3, 0, 0, -2, 4, 0, 0),
        # a = -1, y = -x^3 - 3x^2 + d => x_cd = 0, x_ct = -2
        (-1, -3, 0, 2, 0, 2, -2, -2),
        (-1, -3, 0, 3, 0, 3, -2, -1),
        (-1, -3, 0, 1, 0, 1, -2, -3),
        (-1, -3, 0, 4, 0, 4, -2, 0),
    ]
    a, b, c, d, x_cd, y_cd, x_ct, y_ct = random.choice(configs)

    xmin = min(-2.5, x_cd - 1.2, x_ct - 1.2)
    xmax = max(2.5, x_cd + 1.2, x_ct + 1.2)
    ymin = min(-3.2, y_cd - 1.2, y_ct - 1.2)
    ymax = max(3.8, y_cd + 1.2, y_ct + 1.2)

    def make_pt_code(x, y, pos_x="below", pos_y="left"):
        res = []
        if x != 0 and y != 0:
            res.append(f"\\draw[dashed] ({x},0) node[{pos_x}]{{${x}$}} -- ({x},{y}) -- (0,{y}) node[{pos_y}]{{${y}$}};")
            res.append(f"\\fill ({x},{y}) circle (1.5pt);")
        elif x == 0 and y != 0:
            res.append(f"\\fill (0,{y}) circle (1.5pt) node[above left]{{${y}$}};")
        elif x != 0 and y == 0:
            res.append(f"\\fill ({x},0) circle (1.5pt) node[{pos_x}]{{${x}$}};")
        else:
            res.append("\\fill (0,0) circle (1.5pt);")
        return "\n    ".join(res)

    pt_cd = make_pt_code(x_cd, y_cd, "below", "left")
    pt_ct = make_pt_code(x_ct, y_ct, "below", "left" if x_ct >= 0 else "right")

    poly_parts = [f"{a}*(\\x)^3"]
    if b > 0:
        poly_parts.append(f"+ {b}*(\\x)^2")
    elif b < 0:
        poly_parts.append(f"- {abs(b)}*(\\x)^2")
    if c > 0:
        poly_parts.append(f"+ {c}*(\\x)")
    elif c < 0:
        poly_parts.append(f"- {abs(c)}*(\\x)")
    if d > 0:
        poly_parts.append(f"+ {d}")
    elif d < 0:
        poly_parts.append(f"- {abs(d)}")
    poly_str = " ".join(poly_parts)

    tikz = fr'''\begin{{tikzpicture}}[scale=0.65, line join=round, line cap=round, >=stealth, font=\footnotesize]
    \def\xmin{{{xmin:.1f}}}\def\xmax{{{xmax:.1f}}}\def\ymin{{{ymin:.1f}}}\def\ymax{{{ymax:.1f}}}
    \draw[->] (\xmin-0.2,0)--(\xmax+0.2,0) node[below]{{$x$}};
    \draw[->] (0,\ymin-0.2)--(0,\ymax+0.2) node[left]{{$y$}};
    \draw (0,0) node[below right]{{$O$}};
    \begin{{scope}}
    \clip (\xmin,\ymin) rectangle (\xmax,\ymax);
    \draw[thick, smooth, samples=150, domain=\xmin:\xmax] plot (\x, {{ {poly_str} }});
    \end{{scope}}
    {pt_cd}
    {pt_ct}
\end{{tikzpicture}}'''

    ask_cuc_dai = random.choice([True, False])
    if ask_cuc_dai:
        type_str = "cực đại"
        ans_x, ans_y = x_cd, y_cd
        other_x, other_y = x_ct, y_ct
    else:
        type_str = "cực tiểu"
        ans_x, ans_y = x_ct, y_ct
        other_x, other_y = x_cd, y_cd

    phrasing = random.choice([
        f"Điểm {type_str} của đồ thị hàm số đã cho có tọa độ là",
        f"Tọa độ điểm {type_str} của đồ thị hàm số đã cho là",
        f"Điểm {type_str} của đồ thị hàm số đã cho là điểm nào dưới đây?"
    ])

    caudan = fr'''\immini{{Cho hàm số bậc ba $y = f(x)$ có đồ thị như hình vẽ bên. {phrasing}}}{{
{tikz}
}}'''

    correct = fr"$({ans_x}; {ans_y})$"
    raw_candidates = [
        fr"$({other_x}; {other_y})$",
        fr"$({ans_y}; {ans_x})$",
        fr"$({-ans_x}; {ans_y})$",
        fr"$({ans_x}; {-ans_y})$",
        fr"$({-other_x}; {other_y})$",
        fr"$({other_x}; {-other_y})$",
        fr"$({ans_x}; 0)$",
        fr"$(0; {ans_y})$",
    ]
    distractor_set = set([correct])
    wrongs = []
    for cand in raw_candidates:
        if cand not in distractor_set:
            distractor_set.add(cand)
            wrongs.append(cand)
        if len(wrongs) == 3:
            break

    choices = shuffle_choices(correct, wrongs)

    loi_giai = fr'''Dựa vào đồ thị hàm số:
- Điểm {type_str} của đồ thị hàm số là điểm đỉnh {'nhô cao nhất' if ask_cuc_dai else 'thấp nhất'} trên khoảng lân cận.
- Gióng điểm này xuống trục hoành $Ox$, ta được hoành độ $x = {ans_x}$.
- Gióng điểm này sang trục tung $Oy$, ta được tung độ $y = {ans_y}$.
Vậy điểm {type_str} của đồ thị hàm số có tọa độ là $({ans_x}; {ans_y})$.'''

    return caudan, choices, loi_giai


def CuoiChuong1_MC_B1_NB():
    """Bài 1: Sự biến thiên và cực trị của hàm số - Mức độ: Nhận biết"""
    return sinh_cau_cuc_tri_do_thi_bac_ba()


def CuoiChuong1_MC_B1_TH():
    """Bài 1: Sự biến thiên và cực trị của hàm số - Mức độ: Thông hiểu"""
    import cuoi_chuong
    candidates = [
        cuoi_chuong.CuoiChuong1_MC_Cau16,
        cuoi_chuong.CuoiChuong1_MC_Cau26,
        cuoi_chuong.CuoiChuong1_MC_Cau27,
        cuoi_chuong.CuoiChuong1_MC_Cau34,
        cuoi_chuong.CuoiChuong1_MC_Cau45,
        cuoi_chuong.CuoiChuong1_MC_Cau76,
        cuoi_chuong.CuoiChuong1_MC_Cau23,
        cuoi_chuong.CuoiChuong1_MC_Cau32,
        cuoi_chuong.CuoiChuong1_MC_Cau51,
        cuoi_chuong.CuoiChuong1_MC_Cau62,
        cuoi_chuong.CuoiChuong1_MC_Cau67,
        cuoi_chuong.CuoiChuong1_MC_Cau74,
        cuoi_chuong.CuoiChuong1_MC_Cau52,
    ]
    return random.choice(candidates)()


def CuoiChuong1_MC_B1_VD():
    """Bài 1: Sự biến thiên và cực trị của hàm số - Mức độ: Vận dụng"""
    import cuoi_chuong
    candidates = [
        cuoi_chuong.CuoiChuong1_MC_Cau50,
        cuoi_chuong.CuoiChuong1_MC_Cau71,
        cuoi_chuong.CuoiChuong1_MC_Cau41,
        cuoi_chuong.CuoiChuong1_MC_Cau61,
        cuoi_chuong.CuoiChuong1_MC_Cau78,
        cuoi_chuong.CuoiChuong1_MC_Cau12,
        cuoi_chuong.CuoiChuong1_MC_Cau21,
    ]
    return random.choice(candidates)()


def CuoiChuong1_MC_B2_NB():
    """Bài 2: Giá trị lớn nhất và giá trị nhỏ nhất của hàm số - Mức độ: Nhận biết"""
    import cuoi_chuong
    candidates = [
        cuoi_chuong.CuoiChuong1_MC_Cau64,
        cuoi_chuong.CuoiChuong1_MC_Cau30,
        cuoi_chuong.CuoiChuong1_MC_Cau47,
    ]
    return random.choice(candidates)()


def CuoiChuong1_MC_B2_TH():
    """Bài 2: Giá trị lớn nhất và giá trị nhỏ nhất của hàm số - Mức độ: Thông hiểu"""
    import cuoi_chuong
    candidates = [
        cuoi_chuong.CuoiChuong1_MC_Cau22,
        cuoi_chuong.CuoiChuong1_MC_Cau35,
        cuoi_chuong.CuoiChuong1_MC_Cau46,
        cuoi_chuong.CuoiChuong1_MC_Cau53,
        cuoi_chuong.CuoiChuong1_MC_Cau56,
        cuoi_chuong.CuoiChuong1_MC_Cau2,
    ]
    return random.choice(candidates)()


def CuoiChuong1_MC_B2_VD():
    """Bài 2: Giá trị lớn nhất và giá trị nhỏ nhất của hàm số - Mức độ: Vận dụng"""
    import cuoi_chuong
    candidates = [
        cuoi_chuong.CuoiChuong1_MC_Cau2,
        cuoi_chuong.CuoiChuong1_MC_Cau30,
    ]
    return random.choice(candidates)()


def CuoiChuong1_MC_B3_NB():
    """Bài 3: Đường tiệm cận của đồ thị hàm số - Mức độ: Nhận biết"""
    import cuoi_chuong
    candidates = [
        cuoi_chuong.CuoiChuong1_MC_Cau38,
        cuoi_chuong.CuoiChuong1_MC_Cau58,
        cuoi_chuong.CuoiChuong1_MC_Cau36,
        cuoi_chuong.CuoiChuong1_MC_Cau48,
        cuoi_chuong.CuoiChuong1_MC_Cau6,
        cuoi_chuong.CuoiChuong1_MC_Cau68,
        cuoi_chuong.CuoiChuong1_MC_Cau66,
    ]
    return random.choice(candidates)()


def CuoiChuong1_MC_B3_TH():
    """Bài 3: Đường tiệm cận của đồ thị hàm số - Mức độ: Thông hiểu"""
    import cuoi_chuong
    candidates = [
        cuoi_chuong.CuoiChuong1_MC_Cau4,
        cuoi_chuong.CuoiChuong1_MC_Cau19,
        cuoi_chuong.CuoiChuong1_MC_Cau39,
        cuoi_chuong.CuoiChuong1_MC_Cau69,
        cuoi_chuong.CuoiChuong1_MC_Cau75,
        cuoi_chuong.CuoiChuong1_MC_Cau80,
        cuoi_chuong.CuoiChuong1_MC_Cau20,
        cuoi_chuong.CuoiChuong1_MC_Cau33,
        cuoi_chuong.CuoiChuong1_MC_Cau72,
    ]
    return random.choice(candidates)()


def CuoiChuong1_MC_B3_VD():
    """Bài 3: Đường tiệm cận của đồ thị hàm số - Mức độ: Vận dụng"""
    import cuoi_chuong
    candidates = [
        cuoi_chuong.CuoiChuong1_MC_Cau77,
        cuoi_chuong.CuoiChuong1_MC_Cau1,
    ]
    return random.choice(candidates)()


def CuoiChuong1_MC_B4_NB():
    """Bài 4: Khảo sát sự biến thiên và đồ thị hàm số - Mức độ: Nhận biết"""
    import cuoi_chuong
    candidates = [
        cuoi_chuong.CuoiChuong1_MC_Cau7,
        cuoi_chuong.CuoiChuong1_MC_Cau42,
        cuoi_chuong.CuoiChuong1_MC_Cau13,
        cuoi_chuong.CuoiChuong1_MC_Cau25,
        cuoi_chuong.CuoiChuong1_MC_Cau54,
        cuoi_chuong.CuoiChuong1_MC_Cau59,
    ]
    return random.choice(candidates)()


def CuoiChuong1_MC_B4_TH():
    """Bài 4: Khảo sát sự biến thiên và đồ thị hàm số - Mức độ: Thông hiểu"""
    import cuoi_chuong
    candidates = [
        cuoi_chuong.CuoiChuong1_MC_Cau3,
        cuoi_chuong.CuoiChuong1_MC_Cau14,
        cuoi_chuong.CuoiChuong1_MC_Cau37,
        cuoi_chuong.CuoiChuong1_MC_Cau49,
        cuoi_chuong.CuoiChuong1_MC_Cau5,
        cuoi_chuong.CuoiChuong1_MC_Cau28,
        cuoi_chuong.CuoiChuong1_MC_Cau10,
        cuoi_chuong.CuoiChuong1_MC_Cau15,
        cuoi_chuong.CuoiChuong1_MC_Cau17,
    ]
    return random.choice(candidates)()


def CuoiChuong1_MC_B4_VD():
    """Bài 4: Khảo sát sự biến thiên và đồ thị hàm số - Mức độ: Vận dụng"""
    import cuoi_chuong
    candidates = [
        cuoi_chuong.CuoiChuong1_MC_Cau18,
        cuoi_chuong.CuoiChuong1_MC_Cau40,
    ]
    return random.choice(candidates)()


# ==============================================================================
# CÁC DẠNG ÔN TẬP CHUYÊN ĐỀ CHƯƠNG 1 (ĐƠN ĐIỆU - CỰC TRỊ - GTLN/GTNN)
# ==============================================================================

def make_unique_wrongs(correct, candidates):
    res = []
    seen = {correct}
    for c in candidates:
        if c not in seen:
            seen.add(c)
            res.append(c)
        if len(res) == 3:
            break
    offset = 1
    while len(res) < 3:
        cand = f"${offset}$"
        if cand not in seen:
            seen.add(cand)
            res.append(cand)
        offset += 1
    return res


def format_poly_bac3(a, b, c, d):
    if a == 1:
        res = "x^3"
    elif a == -1:
        res = "-x^3"
    else:
        res = f"{a}x^3"
        
    if b != 0:
        sign_b = " + " if b > 0 else " - "
        abs_b = abs(b)
        term_b = "x^2" if abs_b == 1 else f"{abs_b}x^2"
        res += f"{sign_b}{term_b}"
    if c != 0:
        sign_c = " + " if c > 0 else " - "
        abs_c = abs(c)
        term_c = "x" if abs_c == 1 else f"{abs_c}x"
        res += f"{sign_c}{term_c}"
    if d != 0:
        sign_d = " + " if d > 0 else " - "
        abs_d = abs(d)
        res += f"{sign_d}{abs_d}"
    return res


def format_poly_bac2(a2, b2, c2):
    if a2 == 1:
        res = "x^2"
    elif a2 == -1:
        res = "-x^2"
    else:
        res = f"{a2}x^2"
    if b2 != 0:
        sign = " + " if b2 > 0 else " - "
        abs_val = abs(b2)
        term = "x" if abs_val == 1 else f"{abs_val}x"
        res += f"{sign}{term}"
    if c2 != 0:
        sign = " + " if c2 > 0 else " - "
        res += f"{sign}{abs(c2)}"
    return res


def fmt_frac_latex(val):
    if isinstance(val, int):
        return str(val)
    if isinstance(val, Fraction):
        if val.denominator == 1:
            return str(val.numerator)
        if val.numerator < 0:
            return f"-\\dfrac{{{abs(val.numerator)}}}{{{val.denominator}}}"
        return f"\\dfrac{{{val.numerator}}}{{{val.denominator}}}"
    return str(val)


def CuoiChuong1_MC_BBT_DonDieu_Bac3():
    """Dạng 1: Đọc khoảng đồng biến/nghịch biến từ BBT hàm bậc 3"""
    x1 = random.randint(-4, 1)
    x2 = x1 + random.randint(2, 5)
    a = random.choice([1, -1])
    diff = random.randint(2, 6)
    if a == 1:
        y2 = random.randint(-6, 1)
        y1 = y2 + diff
        bbt = f"""\\begin{{tikzpicture}}[scale=0.8]
\\tkzTabInit[nocadre=false,lgt=1.1,espcl=1.6,deltacl=0.4]{{$x$/0.65,$f'(x)$/0.65,$f(x)$/1.5}}{{ $-\\infty$, ${x1}$, ${x2}$, $+\\infty$ }}
\\tkzTabLine{{,+,0,-,0,+,}}
\\tkzTabVar{{-/ $-\\infty$, +/ ${y1}$, -/ ${y2}$, +/ $+\\infty$}}
\\end{{tikzpicture}}"""
    else:
        y1 = random.randint(-6, 1)
        y2 = y1 + diff
        bbt = f"""\\begin{{tikzpicture}}[scale=0.8]
\\tkzTabInit[nocadre=false,lgt=1.1,espcl=1.6,deltacl=0.4]{{$x$/0.65,$f'(x)$/0.65,$f(x)$/1.5}}{{ $-\\infty$, ${x1}$, ${x2}$, $+\\infty$ }}
\\tkzTabLine{{,-,0,+,0,-,}}
\\tkzTabVar{{+/ $+\\infty$, -/ ${y1}$, +/ ${y2}$, -/ $-\\infty$}}
\\end{{tikzpicture}}"""

    hoi_db = random.choice([True, False])
    if hoi_db:
        caudan = fr"""\immini{{Cho hàm số $y=f(x)$ có bảng biến thiên như hình bên. Hàm số $f(x)$ đồng biến trên khoảng nào dưới đây?}}{{{bbt}}}"""
        if a == 1:
            correct = random.choice([f"$(-\\infty; {x1})$", f"$({x2}; +\\infty)$"])
            wrongs = [f"$({x1}; {x2})$", f"$(-\\infty; {x2})$", f"$({x1}; +\\infty)$"]
            loi_giai = f"Dựa vào bảng biến thiên, $f'(x) > 0$ trên $(-\\infty; {x1})$ và $({x2}; +\\infty)$, do đó hàm số đồng biến trên từng khoảng này."
        else:
            correct = f"$({x1}; {x2})$"
            wrongs = [f"$(-\\infty; {x1})$", f"$({x2}; +\\infty)$", f"$(-\\infty; {x2})$"]
            loi_giai = f"Dựa vào bảng biến thiên, $f'(x) > 0$ trên khoảng $({x1}; {x2})$, do đó hàm số đồng biến trên $({x1}; {x2})$."
    else:
        caudan = fr"""\immini{{Cho hàm số $y=f(x)$ có bảng biến thiên như hình bên. Hàm số $f(x)$ nghịch biến trên khoảng nào dưới đây?}}{{{bbt}}}"""
        if a == 1:
            correct = f"$({x1}; {x2})$"
            wrongs = [f"$(-\\infty; {x1})$", f"$({x2}; +\\infty)$", f"$(-\\infty; {x2})$"]
            loi_giai = f"Dựa vào bảng biến thiên, $f'(x) < 0$ trên khoảng $({x1}; {x2})$, do đó hàm số nghịch biến trên $({x1}; {x2})$."
        else:
            correct = random.choice([f"$(-\\infty; {x1})$", f"$({x2}; +\\infty)$"])
            wrongs = [f"$({x1}; {x2})$", f"$(-\\infty; {x2})$", f"$({x1}; +\\infty)$"]
            loi_giai = f"Dựa vào bảng biến thiên, $f'(x) < 0$ trên $(-\\infty; {x1})$ và $({x2}; +\\infty)$, do đó hàm số nghịch biến trên từng khoảng này."

    return caudan, shuffle_choices(correct, wrongs), loi_giai


def CuoiChuong1_MC_BBT_CucTri_TrungPhuong():
    """Dạng 2: Điểm cực đại/cực tiểu của hàm số từ BBT hàm trùng phương"""
    x0 = random.randint(1, 3)
    y_ct = random.randint(-5, 1)
    y_cd = y_ct + random.randint(2, 6)
    a_sign = random.choice([1, -1])
    
    if a_sign == 1:
        bbt = f"""\\begin{{tikzpicture}}[scale=0.8]
\\tkzTabInit[nocadre=false,lgt=1.1,espcl=1.3,deltacl=0.35]{{$x$/0.65,$f'(x)$/0.65,$f(x)$/1.5}}{{ $-\\infty$, ${-x0}$, $0$, ${x0}$, $+\\infty$ }}
\\tkzTabLine{{,-,0,+,0,-,0,+,}}
\\tkzTabVar{{+/ $+\\infty$, -/ ${y_ct}$, +/ ${y_cd}$, -/ ${y_ct}$, +/ $+\\infty$}}
\\end{{tikzpicture}}"""
        hoi_loai = random.choice(["diem_cd", "diem_ct", "gt_cd", "gt_ct"])
        if hoi_loai == "diem_cd":
            caudan = fr"""\immini{{Cho hàm số $y=f(x)$ có bảng biến thiên như hình bên. Điểm cực đại của hàm số $y=f(x)$ là:}}{{{bbt}}}"""
            correct = "$x = 0$"
            wrongs = make_unique_wrongs(correct, [f"$x = {-x0}$", f"$x = {x0}$", f"$y = {y_cd}$", f"$y = {y_ct}$"])
            loi_giai = f"Quan sát bảng biến thiên, đạo hàm $f'(x)$ đổi dấu từ dương sang âm khi đi qua $x = 0$. Do đó điểm cực đại của hàm số là $x = 0$."
        elif hoi_loai == "diem_ct":
            caudan = fr"""\immini{{Cho hàm số $y=f(x)$ có bảng biến thiên như hình bên. Điểm cực tiểu của hàm số $y=f(x)$ là:}}{{{bbt}}}"""
            correct = random.choice([f"$x = {-x0}$", f"$x = {x0}$"])
            other_x = f"$x = {x0}$" if correct == f"$x = {-x0}$" else f"$x = {-x0}$"
            wrongs = make_unique_wrongs(correct, ["$x = 0$", f"$y = {y_ct}$", f"$y = {y_cd}$", other_x])
            loi_giai = f"Quan sát bảng biến thiên, đạo hàm $f'(x)$ đổi dấu từ âm sang dương khi đi qua $x = \\pm {x0}$. Do đó hàm số đạt cực tiểu tại $x = {-x0}$ và $x = {x0}$."
        elif hoi_loai == "gt_cd":
            caudan = fr"""\immini{{Cho hàm số $y=f(x)$ có bảng biến thiên như hình bên. Giá trị cực đại của hàm số $y=f(x)$ bằng:}}{{{bbt}}}"""
            correct = f"${y_cd}$"
            wrongs = make_unique_wrongs(correct, [f"${y_ct}$", "$0$", f"${x0}$", f"${-x0}$", f"${y_cd + 1}$", f"${y_ct - 1}$"])
            loi_giai = f"Quan sát bảng biến thiên, giá trị cực đại của hàm số là $y_{{\\text{{CĐ}}}} = f(0) = {y_cd}$."
        else:
            caudan = fr"""\immini{{Cho hàm số $y=f(x)$ có bảng biến thiên như hình bên. Giá trị cực tiểu của hàm số $y=f(x)$ bằng:}}{{{bbt}}}"""
            correct = f"${y_ct}$"
            wrongs = make_unique_wrongs(correct, [f"${y_cd}$", f"${-x0}$", f"${x0}$", "$0$", f"${y_ct - 1}$", f"${y_cd + 1}$"])
            loi_giai = f"Quan sát bảng biến thiên, giá trị cực tiểu của hàm số là $y_{{\\text{{CT}}}} = f(\\pm {x0}) = {y_ct}$."
    else:
        bbt = f"""\\begin{{tikzpicture}}[scale=0.8]
\\tkzTabInit[nocadre=false,lgt=1.1,espcl=1.3,deltacl=0.35]{{$x$/0.65,$f'(x)$/0.65,$f(x)$/1.5}}{{ $-\\infty$, ${-x0}$, $0$, ${x0}$, $+\\infty$ }}
\\tkzTabLine{{,+,0,-,0,+,0,-,}}
\\tkzTabVar{{-/ $-\\infty$, +/ ${y_cd}$, -/ ${y_ct}$, +/ ${y_cd}$, -/ $-\\infty$}}
\\end{{tikzpicture}}"""
        hoi_loai = random.choice(["diem_ct", "diem_cd", "gt_cd", "gt_ct"])
        if hoi_loai == "diem_ct":
            caudan = fr"""\immini{{Cho hàm số $y=f(x)$ có bảng biến thiên như hình bên. Điểm cực tiểu của hàm số $y=f(x)$ là:}}{{{bbt}}}"""
            correct = "$x = 0$"
            wrongs = make_unique_wrongs(correct, [f"$x = {-x0}$", f"$x = {x0}$", f"$y = {y_ct}$", f"$y = {y_cd}$"])
            loi_giai = f"Quan sát bảng biến thiên, đạo hàm $f'(x)$ đổi dấu từ âm sang dương khi đi qua $x = 0$. Do đó điểm cực tiểu của hàm số là $x = 0$."
        elif hoi_loai == "diem_cd":
            caudan = fr"""\immini{{Cho hàm số $y=f(x)$ có bảng biến thiên như hình bên. Điểm cực đại của hàm số $y=f(x)$ là:}}{{{bbt}}}"""
            correct = random.choice([f"$x = {-x0}$", f"$x = {x0}$"])
            other_x = f"$x = {x0}$" if correct == f"$x = {-x0}$" else f"$x = {-x0}$"
            wrongs = make_unique_wrongs(correct, ["$x = 0$", f"$y = {y_cd}$", f"$y = {y_ct}$", other_x])
            loi_giai = f"Quan sát bảng biến thiên, đạo hàm $f'(x)$ đổi dấu từ dương sang âm khi đi qua $x = \\pm {x0}$. Do đó hàm số đạt cực đại tại $x = {-x0}$ và $x = {x0}$."
        elif hoi_loai == "gt_cd":
            caudan = fr"""\immini{{Cho hàm số $y=f(x)$ có bảng biến thiên như hình bên. Giá trị cực đại của hàm số $y=f(x)$ bằng:}}{{{bbt}}}"""
            correct = f"${y_cd}$"
            wrongs = make_unique_wrongs(correct, [f"${y_ct}$", "$0$", f"${x0}$", f"${-x0}$", f"${y_cd + 1}$", f"${y_ct - 1}$"])
            loi_giai = f"Quan sát bảng biến thiên, giá trị cực đại của hàm số là $y_{{\\text{{CĐ}}}} = f(\\pm {x0}) = {y_cd}$."
        else:
            caudan = fr"""\immini{{Cho hàm số $y=f(x)$ có bảng biến thiên như hình bên. Giá trị cực tiểu của hàm số $y=f(x)$ bằng:}}{{{bbt}}}"""
            correct = f"${y_ct}$"
            wrongs = make_unique_wrongs(correct, [f"${y_cd}$", f"${-x0}$", f"${x0}$", "$0$", f"${y_ct - 1}$", f"${y_cd + 1}$"])
            loi_giai = f"Quan sát bảng biến thiên, giá trị cực tiểu của hàm số là $y_{{\\text{{CT}}}} = f(0) = {y_ct}$."

    return caudan, shuffle_choices(correct, wrongs), loi_giai


def CuoiChuong1_MC_DonDieu_HamBac3():
    """Dạng 3: Khoảng đồng biến / nghịch biến của hàm bậc 3 tường minh"""
    m = random.choice([1, 2, 3])
    d = random.randint(-5, 5)
    a = random.choice([1, -1])
    b_hs = 3 * m
    x2 = 2 * m
    str_d = f" + {d}" if d > 0 else (f" - {abs(d)}" if d < 0 else "")
    
    if a == 1:
        func_tex = f"x^3 - {b_hs}x^2{str_d}".replace(" - 1x^2", " - x^2")
        hoi_db = random.choice([True, False])
        if hoi_db:
            caudan = f"Hàm số $y = {func_tex}$ đồng biến trên khoảng nào dưới đây?"
            correct = random.choice(["$(-\\infty; 0)$", f"$({x2}; +\\infty)$"])
            wrongs = [f"$(0; {x2})$", f"$(-\\infty; {x2})$", "$(0; +\\infty)$"]
            loi_giai = f"Ta có $y' = 3x^2 - {2*b_hs}x = 3x(x - {x2})$. Cho $y' > 0 \\Leftrightarrow x \\in (-\\infty; 0) \\cup ({x2}; +\\infty)$. Do đó hàm số đồng biến trên $(-\\infty; 0)$ và $({x2}; +\\infty)$."
        else:
            caudan = f"Hàm số $y = {func_tex}$ nghịch biến trên khoảng nào dưới đây?"
            correct = f"$(0; {x2})$"
            wrongs = ["$(-\\infty; 0)$", f"$({x2}; +\\infty)$", f"$(-\\infty; {x2})$"]
            loi_giai = f"Ta có $y' = 3x^2 - {2*b_hs}x = 3x(x - {x2}) < 0 \\Leftrightarrow 0 < x < {x2}$. Do đó hàm số nghịch biến trên khoảng $(0; {x2})$."
    else:
        func_tex = f"-x^3 + {b_hs}x^2{str_d}".replace("+ 1x^2", "+ x^2")
        hoi_db = random.choice([True, False])
        if hoi_db:
            caudan = f"Hàm số $y = {func_tex}$ đồng biến trên khoảng nào dưới đây?"
            correct = f"$(0; {x2})$"
            wrongs = ["$(-\\infty; 0)$", f"$({x2}; +\\infty)$", f"$(-\\infty; {x2})$"]
            loi_giai = f"Ta có $y' = -3x^2 + {2*b_hs}x = -3x(x - {x2}) > 0 \\Leftrightarrow 0 < x < {x2}$. Do đó hàm số đồng biến trên khoảng $(0; {x2})$."
        else:
            caudan = f"Hàm số $y = {func_tex}$ nghịch biến trên khoảng nào dưới đây?"
            correct = random.choice(["$(-\\infty; 0)$", f"$({x2}; +\\infty)$"])
            wrongs = [f"$(0; {x2})$", f"$(-\\infty; {x2})$", "$(0; +\\infty)$"]
            loi_giai = f"Ta có $y' = -3x^2 + {2*b_hs}x = -3x(x - {x2}) < 0 \\Leftrightarrow x \\in (-\\infty; 0) \\cup ({x2}; +\\infty)$. Do đó hàm số nghịch biến trên từng khoảng này."

    return caudan, shuffle_choices(correct, wrongs), loi_giai


def CuoiChuong1_MC_GiaTriCucTri_Bac3():
    """Dạng 4: Giá trị cực trị / điểm cực trị của hàm bậc 3"""
    p = random.choice([1, 2, 3])
    d = random.randint(-5, 5)
    a = random.choice([1, -1])
    b_hs = 3 * (p**2)
    str_d = f" + {d}" if d > 0 else (f" - {abs(d)}" if d < 0 else "")
    
    if a == 1:
        y_ct = -2 * (p**3) + d
        y_cd = 2 * (p**3) + d
        term_x = "- x" if b_hs == 1 else f"- {b_hs}x"
        func_tex = f"x^3 {term_x}{str_d}"
        
        hoi_loai = random.choice(["gt_ct", "gt_cd", "diem_ct", "diem_cd"])
        if hoi_loai == "gt_ct":
            caudan = f"Giá trị cực tiểu của hàm số $y = {func_tex}$ bằng:"
            correct = f"${y_ct}$"
            wrongs = make_unique_wrongs(correct, [f"${y_cd}$", f"${p}$", f"${-p}$", "$0$", f"${y_ct - 1}$"])
            loi_giai = f"Ta có $y' = 3x^2 - {b_hs} = 0 \\Leftrightarrow x = \\pm {p}$. Điểm cực tiểu là $x = {p} \\Rightarrow$ giá trị cực tiểu $y_{{CT}} = y({p}) = {y_ct}$."
        elif hoi_loai == "gt_cd":
            caudan = f"Giá trị cực đại của hàm số $y = {func_tex}$ bằng:"
            correct = f"${y_cd}$"
            wrongs = make_unique_wrongs(correct, [f"${y_ct}$", f"${-p}$", f"${p}$", "$0$", f"${y_cd + 1}$"])
            loi_giai = f"Ta có $y' = 3x^2 - {b_hs} = 0 \\Leftrightarrow x = \\pm {p}$. Điểm cực đại là $x = {-p} \\Rightarrow$ giá trị cực đại $y_{{\\text{{CĐ}}}} = y({-p}) = {y_cd}$."
        elif hoi_loai == "diem_ct":
            caudan = f"Điểm cực tiểu của hàm số $y = {func_tex}$ là:"
            correct = f"$x = {p}$"
            wrongs = make_unique_wrongs(correct, [f"$x = {-p}$", f"$y = {y_ct}$", f"$y = {y_cd}$", "$x = 0$"])
            loi_giai = f"Ta có $y' = 3(x^2 - {p**2}) = 0 \\Leftrightarrow x = \\pm {p}$. Đạo hàm đổi dấu từ âm sang dương tại $x = {p}$, do đó điểm cực tiểu là $x = {p}$."
        else:
            caudan = f"Điểm cực đại của hàm số $y = {func_tex}$ là:"
            correct = f"$x = {-p}$"
            wrongs = make_unique_wrongs(correct, [f"$x = {p}$", f"$y = {y_cd}$", f"$y = {y_ct}$", "$x = 0$"])
            loi_giai = f"Ta có $y' = 3(x^2 - {p**2}) = 0 \\Leftrightarrow x = \\pm {p}$. Đạo hàm đổi dấu từ dương sang âm tại $x = {-p}$, do đó điểm cực đại là $x = {-p}$."
    else:
        y_ct = -2 * (p**3) + d
        y_cd = 2 * (p**3) + d
        term_x = "+ x" if b_hs == 1 else f"+ {b_hs}x"
        func_tex = f"-x^3 {term_x}{str_d}"
        
        hoi_loai = random.choice(["gt_ct", "gt_cd", "diem_ct", "diem_cd"])
        if hoi_loai == "gt_ct":
            caudan = f"Giá trị cực tiểu của hàm số $y = {func_tex}$ bằng:"
            correct = f"${y_ct}$"
            wrongs = make_unique_wrongs(correct, [f"${y_cd}$", f"${-p}$", f"${p}$", "$0$", f"${y_ct - 1}$"])
            loi_giai = f"Ta có $y' = -3x^2 + {b_hs} = 0 \\Leftrightarrow x = \\pm {p}$. Điểm cực tiểu là $x = {-p} \\Rightarrow$ giá trị cực tiểu $y_{{\\text{{CT}}}} = y({-p}) = {y_ct}$."
        elif hoi_loai == "gt_cd":
            caudan = f"Giá trị cực đại của hàm số $y = {func_tex}$ bằng:"
            correct = f"${y_cd}$"
            wrongs = make_unique_wrongs(correct, [f"${y_ct}$", f"${p}$", f"${-p}$", "$0$", f"${y_cd + 1}$"])
            loi_giai = f"Ta có $y' = -3x^2 + {b_hs} = 0 \\Leftrightarrow x = \\pm {p}$. Điểm cực đại là $x = {p} \\Rightarrow$ giá trị cực đại $y_{{\\text{{CĐ}}}} = y({p}) = {y_cd}$."
        elif hoi_loai == "diem_ct":
            caudan = f"Điểm cực tiểu của hàm số $y = {func_tex}$ là:"
            correct = f"$x = {-p}$"
            wrongs = make_unique_wrongs(correct, [f"$x = {p}$", f"$y = {y_ct}$", f"$y = {y_cd}$", "$x = 0$"])
            loi_giai = f"Ta có $y' = -3(x^2 - {p**2}) = 0 \\Leftrightarrow x = \\pm {p}$. Đạo hàm đổi dấu từ âm sang dương tại $x = {-p}$, do đó điểm cực tiểu là $x = {-p}$."
        else:
            caudan = f"Điểm cực đại của hàm số $y = {func_tex}$ là:"
            correct = f"$x = {p}$"
            wrongs = make_unique_wrongs(correct, [f"$x = {-p}$", f"$y = {y_cd}$", f"$y = {y_ct}$", "$x = 0$"])
            loi_giai = f"Ta có $y' = -3(x^2 - {p**2}) = 0 \\Leftrightarrow x = \\pm {p}$. Đạo hàm đổi dấu từ dương sang âm tại $x = {p}$, do đó điểm cực đại là $x = {p}$."

    return caudan, shuffle_choices(correct, wrongs), loi_giai


def CuoiChuong1_MC_GTLN_GTNN_HamBac3_Doan():
    """Dạng 5: GTLN / GTNN của hàm số bậc ba trên đoạn ngẫu nhiên"""
    pairs_even = [
        (-1, 1), (-1, 3), (-3, 1), (-3, -1), (1, 3), (0, 2), (-2, 0), (-2, 2)
    ]
    pairs_odd = [
        (-1, 2), (-2, 1), (0, 1), (-1, 0), (1, 2), (-2, -1)
    ]
    
    mode = random.choice(["a_unit", "a_two"])
    if mode == "a_unit":
        a = random.choice([1, -1])
        r1, r2 = random.choice(pairs_even)
        b = -3 * a * (r1 + r2) // 2
        c = 3 * a * r1 * r2
    else:
        a = random.choice([2, -2])
        r1, r2 = random.choice(pairs_odd)
        b = -3 * (a // 2) * (r1 + r2)
        c = 3 * a * r1 * r2
        
    d = random.randint(-6, 6)
    
    t = random.choice(["only_r1", "only_r2", "both", "random"])
    if t == "only_r1":
        alpha = r1 - random.randint(1, 2)
        beta = min(r1 + random.randint(0, 1), r2 - 1)
    elif t == "only_r2":
        alpha = max(r2 - random.randint(0, 1), r1 + 1)
        beta = r2 + random.randint(1, 2)
    elif t == "both":
        alpha = r1 - random.randint(0, 2)
        beta = r2 + random.randint(0, 2)
    else:
        alpha = random.randint(min(r1 - 2, -3), max(r2 - 1, 0))
        beta = alpha + random.randint(2, 4)
        
    if alpha >= beta:
        alpha = r1 - 1
        beta = r2 + 1
        
    func_tex = format_poly_bac3(a, b, c, d)
    daoham_tex = format_poly_bac2(3 * a, 2 * b, c)
    
    in_roots = [r for r in [r1, r2] if alpha <= r <= beta]
    out_roots = [r for r in [r1, r2] if r < alpha or r > beta]
    
    eval_pts = sorted(list(set([alpha, beta] + in_roots)))
    f = lambda x: a*(x**3) + b*(x**2) + c*x + d
    vals = {x: f(x) for x in eval_pts}
    
    hoi_max = random.choice([True, False])
    loai_str = "lớn nhất" if hoi_max else "nhỏ nhất"
    ans_val = max(vals.values()) if hoi_max else min(vals.values())
    other_val = min(vals.values()) if hoi_max else max(vals.values())
    
    caudan = f"Giá trị {loai_str} của hàm số $y = {func_tex}$ trên đoạn $[{alpha}; {beta}]$ bằng:"
    correct = f"${ans_val}$"
    candidates = [
        f"${other_val}$",
        *[f"${vals[x]}$" for x in eval_pts if vals[x] != ans_val],
        f"${ans_val - 2}$",
        f"${ans_val + 2}$",
        f"${ans_val - 5}$",
        f"${ans_val + 5}$",
        "$0$",
    ]
    wrongs = make_unique_wrongs(correct, candidates)
    
    loi_giai = f"Ta có $y' = {daoham_tex} = 0 \\iff x = {r1}$ hoặc $x = {r2}$.\\\\\n"
    if len(in_roots) == 2:
        loi_giai += f"Cả hai nghiệm $x = {r1}, x = {r2}$ đều thuộc đoạn $[{alpha}; {beta}]$.\\\\\n"
    elif len(in_roots) == 1:
        loi_giai += f"Trong đó $x = {in_roots[0]} \\in [{alpha}; {beta}]$, còn $x = {out_roots[0]} \\notin [{alpha}; {beta}]$.\\\\\n"
    else:
        loi_giai += f"Cả hai nghiệm $x = {r1}, x = {r2}$ đều không thuộc đoạn $[{alpha}; {beta}]$.\\\\\n"
        
    pts_str = ", ".join([f"$y({x}) = {vals[x]}$" for x in eval_pts])
    loi_giai += f"Tính các giá trị: {pts_str}.\\\\\n"
    if hoi_max:
        loi_giai += f"So sánh các giá trị trên, ta được $\\max\\limits_{{[{alpha}; {beta}]}} y = {ans_val}$."
    else:
        loi_giai += f"So sánh các giá trị trên, ta được $\\min\\limits_{{[{alpha}; {beta}]}} y = {ans_val}$."
        
    return caudan, shuffle_choices(correct, wrongs), loi_giai


def CuoiChuong1_MC_DonDieu_NhatBien():
    """Dạng 6: Khoảng đơn điệu của hàm nhất biến"""
    x0 = random.choice([-2, -1, 1, 2])
    a = random.choice([1, 2, 3])
    b = random.randint(1, 5)
    
    delta = -a * x0 - b
    while delta == 0:
        b = random.randint(1, 6)
        delta = -a * x0 - b
        
    tu_tex = f"{a}x + {b}" if a > 1 else f"x + {b}"
    mau_tex = f"x - {x0}" if x0 > 0 else f"x + {abs(x0)}"
    
    if delta < 0:
        caudan = f"Hàm số $y = \\dfrac{{{tu_tex}}}{{{mau_tex}}}$ nghịch biến trên khoảng nào dưới đây?"
        correct = random.choice([f"$(-\\infty; {x0})$", f"$({x0}; +\\infty)$"])
        wrongs = [f"$(-\\infty; +\\infty)$", f"$\\mathbb{{R}} \\setminus \\{{{x0}\\}}$", f"$({x0 - 1}; {x0 + 1})$"]
        loi_giai = f"Tập xác định: $D = \\mathbb{{R}} \\setminus \\{{{x0}\\}}$.\\\\\nĐạo hàm: $y' = \\dfrac{{{delta}}}{{({mau_tex})^2}} < 0, \\; \\forall x \\ne {x0}$.\\\\\nDo đó, hàm số nghịch biến trên từng khoảng $(-\\infty; {x0})$ và $({x0}; +\\infty)$."
    else:
        caudan = f"Hàm số $y = \\dfrac{{{tu_tex}}}{{{mau_tex}}}$ đồng biến trên khoảng nào dưới đây?"
        correct = random.choice([f"$(-\\infty; {x0})$", f"$({x0}; +\\infty)$"])
        wrongs = [f"$(-\\infty; +\\infty)$", f"$\\mathbb{{R}} \\setminus \\{{{x0}\\}}$", f"$({x0 - 1}; {x0 + 1})$"]
        loi_giai = f"Tập xác định: $D = \\mathbb{{R}} \\setminus \\{{{x0}\\}}$.\\\\\nĐạo hàm: $y' = \\dfrac{{{delta}}}{{({mau_tex})^2}} > 0, \\; \\forall x \\ne {x0}$.\\\\\nDo đó, hàm số đồng biến trên từng khoảng $(-\\infty; {x0})$ và $({x0}; +\\infty)$."

    return caudan, shuffle_choices(correct, wrongs), loi_giai


def CuoiChuong1_MC_SoCucTri_TrungPhuong():
    """Dạng 7: Số điểm cực trị của hàm trùng phương"""
    a = random.choice([1, 2, -1, -2])
    case = random.choice([3, 1])
    if case == 3:
        b = -2 * random.choice([1, 2]) if a > 0 else 2 * random.choice([1, 2])
        ans_num = 3
    else:
        b = 2 * random.choice([1, 2]) if a > 0 else -2 * random.choice([1, 2])
        ans_num = 1
        
    c = random.randint(-5, 5)
    str_a = "x^4" if a == 1 else ("-x^4" if a == -1 else f"{a}x^4")
    str_b = f" + {b}x^2" if b > 0 else f" - {abs(b)}x^2"
    str_c = f" + {c}" if c > 0 else (f" - {abs(c)}" if c < 0 else "")
    func_tex = f"{str_a}{str_b}{str_c}"

    caudan = f"Số điểm cực trị của hàm số $y = {func_tex}$ là:"
    correct = f"${ans_num}$"
    wrongs = [f"${w}$" for w in [0, 1, 2, 3] if w != ans_num][:3]
    
    if ans_num == 3:
        loi_giai = f"Ta có $a \\cdot b = ({a}) \\cdot ({b}) < 0$, suy ra phương trình $y' = 0$ có 3 nghiệm phân biệt và $y'$ đổi dấu qua cả 3 nghiệm này. Do đó hàm số có $3$ điểm cực trị."
    else:
        loi_giai = f"Ta có $a \\cdot b = ({a}) \\cdot ({b}) > 0$, suy ra phương trình $y' = 0$ chỉ có 1 nghiệm duy nhất $x = 0$ và đổi dấu qua nghiệm này. Do đó hàm số có đúng $1$ điểm cực trị."
        
    return caudan, shuffle_choices(correct, wrongs), loi_giai


def CuoiChuong1_MC_GTLN_GTNN_CanThuc():
    """Dạng 8: GTLN / GTNN của hàm căn thức y = sqrt(R^2 - x^2) + k trên đoạn [-R; R]"""
    R = random.choice([2, 3, 4, 5])
    k = random.choice([0, 1, 2, -1])
    R2 = R**2
    str_k = f" + {k}" if k > 0 else (f" - {abs(k)}" if k < 0 else "")
    func_tex = f"\\sqrt{{{R2} - x^2}}{str_k}"
    
    y_min = k
    y_max = R + k
    
    hoi_min = random.choice([True, False])
    if hoi_min:
        caudan = f"Giá trị nhỏ nhất của hàm số $y = {func_tex}$ trên đoạn $[{-R}; {R}]$ bằng:"
        correct = f"${y_min}$"
        wrongs = make_unique_wrongs(correct, [f"${y_max}$", f"${-R + k}$", f"${R2}$", f"${R}$", "$0$"])
        loi_giai = f"Với mọi $x \\in [{-R}; {R}]$, ta có $0 \\le {R2} - x^2 \\le {R2} \\implies 0 \\le \\sqrt{{{R2} - x^2}} \\le {R}$.\\\\\nDo đó $y \\ge {y_min}$, dấu đẳng thức xảy ra khi $x = \\pm {R}$. Vậy giá trị nhỏ nhất của hàm số là ${y_min}$."
    else:
        caudan = f"Giá trị lớn nhất của hàm số $y = {func_tex}$ trên đoạn $[{-R}; {R}]$ bằng:"
        correct = f"${y_max}$"
        wrongs = make_unique_wrongs(correct, [f"${y_min}$", f"${R}$", f"${R2 + k}$", f"${-R + k}$", "$0$"])
        loi_giai = f"Với mọi $x \\in [{-R}; {R}]$, ta có $0 \\le {R2} - x^2 \\le {R2} \\implies 0 \\le \\sqrt{{{R2} - x^2}} \\le {R}$.\\\\\nDo đó $y \\le {y_max}$, dấu đẳng thức xảy ra khi $x = 0$. Vậy giá trị lớn nhất của hàm số là ${y_max}$."

    return caudan, shuffle_choices(correct, wrongs), loi_giai


def CuoiChuong1_MC_BBT_GTLN_GTNN_KhoangPhanThuc():
    """PHT 2026 - Câu 9: GTLN - GTNN từ BBT hàm phân thức trên khoảng/đoạn"""
    x0 = random.choice([-2, -1, 1, 2])
    x1 = x0 - random.randint(1, 2)
    L1 = random.choice([1, 2, -1, -2])
    y1_str = random.choice([r"-\sqrt{2}", r"-\sqrt{3}", "-2", "-3", "0"])
    L2 = random.choice([-1, -2, 0, 1])
    
    # Đoạn [a; b] trên (x0; +infty)
    a = x0 + random.randint(1, 2)
    b = a + random.randint(2, 5)
    c = a + 1
    
    sign_right = random.choice(["+", "-"])
    hoi_min = random.choice([True, False])
    
    if sign_right == "+":
        tab_line = ",-,0,+,d,+,"
        tab_var = f"+/ ${L1}$, -/ ${y1_str}$, +D-/ $+\\infty$ / $-\\infty$, +/ ${L2}$"
    else:
        tab_line = ",-,0,+,d,-,"
        tab_var = f"+/ ${L1}$, -/ ${y1_str}$, +D-/ $+\\infty$ / $+\\infty$, -/ ${L2}$"

    bbt = f"""\\begin{{tikzpicture}}[scale=0.8]
\\tkzTabInit[nocadre=false,lgt=1.1,espcl=2.2,deltacl=0.4]{{$x$/0.65,$y'$/0.65,$y$/1.8}}{{$-\\infty$, ${x1}$, ${x0}$, $+\\infty$}}
\\tkzTabLine{{{tab_line}}}
\\tkzTabVar{{{tab_var}}}
\\end{{tikzpicture}}"""

    loai_str = "nhỏ nhất" if hoi_min else "lớn nhất"
    caudan = fr"""\immini{{Cho hàm số $y = f(x)$ liên tục trên $(-\infty; {x0})$ và $({x0}; +\infty)$ có bảng biến thiên như hình bên. Giá trị {loai_str} của hàm số $y = f(x)$ trên đoạn $[{a}; {b}]$ là:}}{{{bbt}}}"""

    if sign_right == "+":
        if hoi_min:
            correct = f"$f({a})$"
            candidates = [f"$f({b})$", f"$f({c})$", f"${L2}$", f"${L1}$", "$-1$"]
            loi_giai = f"Dựa vào bảng biến thiên, trên khoảng $({x0}; +\\infty)$ ta có $y' > 0$ nên hàm số đồng biến trên $({x0}; +\\infty)$.\\\\\nVì $[{a}; {b}] \\subset ({x0}; +\\infty)$ nên hàm số đồng biến trên đoạn $[{a}; {b}]$.\\\\\nDo đó $\\min\\limits_{{[{a}; {b}]}} f(x) = f({a})$."
        else:
            correct = f"$f({b})$"
            candidates = [f"$f({a})$", f"$f({c})$", f"${L2}$", f"${L1}$", "$1$"]
            loi_giai = f"Dựa vào bảng biến thiên, trên khoảng $({x0}; +\\infty)$ ta có $y' > 0$ nên hàm số đồng biến trên $({x0}; +\\infty)$.\\\\\nVì $[{a}; {b}] \\subset ({x0}; +\\infty)$ nên hàm số đồng biến trên đoạn $[{a}; {b}]$.\\\\\nDo đó $\\max\\limits_{{[{a}; {b}]}} f(x) = f({b})$."
    else:
        if hoi_min:
            correct = f"$f({b})$"
            candidates = [f"$f({a})$", f"$f({c})$", f"${L2}$", f"${L1}$", "$-1$"]
            loi_giai = f"Dựa vào bảng biến thiên, trên khoảng $({x0}; +\\infty)$ ta có $y' < 0$ nên hàm số nghịch biến trên $({x0}; +\\infty)$.\\\\\nVì $[{a}; {b}] \\subset ({x0}; +\\infty)$ nên hàm số nghịch biến trên đoạn $[{a}; {b}]$.\\\\\nDo đó $\\min\\limits_{{[{a}; {b}]}} f(x) = f({b})$."
        else:
            correct = f"$f({a})$"
            candidates = [f"$f({b})$", f"$f({c})$", f"${L2}$", f"${L1}$", "$1$"]
            loi_giai = f"Dựa vào bảng biến thiên, trên khoảng $({x0}; +\\infty)$ ta có $y' < 0$ nên hàm số nghịch biến trên $({x0}; +\\infty)$.\\\\\nVì $[{a}; {b}] \\subset ({x0}; +\\infty)$ nên hàm số nghịch biến trên đoạn $[{a}; {b}]$.\\\\\nDo đó $\\max\\limits_{{[{a}; {b}]}} f(x) = f({a})$."

    wrongs = make_unique_wrongs(correct, candidates)
    return caudan, shuffle_choices(correct, wrongs), loi_giai


def CuoiChuong1_MC_DoThi_CucTri_Bac21():
    """PHT 2026 - Câu 10: Điểm / giá trị cực trị từ đồ thị hàm phân thức bậc 2 trên bậc nhất"""
    configs = [
        # (x0, k, p, p_tex, delta, x_ct, y_ct, y_ct_tex, x_cd, y_cd, y_cd_tex, m)
        (1, 1, -0.5, r"x - 0.5", 1, 2, 2.5, r"\dfrac{5}{2}", -1, -2.0, r"-2", 1),
        (1, 1, 0, r"x", 1, 2, 3, r"3", 0, -1, r"-1", 1),
        (-1, 1, 0, r"x", 1, 0, 1, r"1", -2, -3, r"-3", 1),
        (2, 1, -1, r"x - 1", 1, 3, 3, r"3", 1, -1, r"-1", 1),
        (1, 1, 1, r"x + 1", 1, 2, 4, r"4", 0, 0, r"0", 1),
        (-1, 1, 1, r"x + 1", 1, 0, 2, r"2", -2, -2, r"-2", 1),
        (-1, 1, 0.5, r"x + 0.5", 1, 0, 1.5, r"\dfrac{3}{2}", -2, -2.5, r"-\dfrac{5}{2}", 1),
    ]
    
    cfg = random.choice(configs)
    x0, k, p, p_tex, delta, x_ct, y_ct, y_ct_tex, x_cd, y_cd, y_cd_tex, m = cfg
    
    xmin = min(-3.5, x_cd - 1.5, x0 - 2.5)
    xmax = max(4.0, x_ct + 1.5, x0 + 2.5)
    ymin = min(-4.0, y_cd - 1.5)
    ymax = max(4.0, y_ct + 1.5)
    
    node_yct = f"\\draw (0,{y_ct}) node[left]{{${y_ct_tex}$}};" if y_ct != 0 else ""
    node_xct = f"\\draw ({x_ct},0) node[below]{{${x_ct}$}};" if x_ct != 0 else ""
    giong_ct = f"\\draw[dashed] ({x_ct},0) -- ({x_ct},{y_ct}) -- (0,{y_ct}); \\fill ({x_ct},{y_ct}) circle (1.5pt);" if (x_ct != 0 and y_ct != 0) else f"\\fill ({x_ct},{y_ct}) circle (1.5pt);"
    
    node_ycd = f"\\draw (0,{y_cd}) node[above left]{{${y_cd_tex}$}};" if y_cd != 0 else ""
    node_xcd = f"\\draw ({x_cd},0) node[above]{{${x_cd}$}};" if x_cd != 0 else ""
    giong_cd = f"\\draw[dashed] ({x_cd},0) -- ({x_cd},{y_cd}) -- (0,{y_cd}); \\fill ({x_cd},{y_cd}) circle (1.5pt);" if (x_cd != 0 and y_cd != 0) else f"\\fill ({x_cd},{y_cd}) circle (1.5pt);"
    
    node_x0 = f"\\draw ({x0},0) node[below right]{{${x0}$}};" if x0 != 0 else ""
    
    d1 = x0 - 0.35
    d2 = x0 + 0.35
    
    func_tikz = f"\\x + ({p}) + ({m})/(\\x - ({x0}))"
    tck_tikz = f"\\x + ({p})"
    
    tikz_img = f"""\\begin{{tikzpicture}}[scale=0.65, line join=round, line cap=round, >=stealth, font=\\footnotesize]
\\tikzset{{every node/.style={{scale=0.9}}}}
\\def\\xmin{{{xmin:.1f}}}\\def\\xmax{{{xmax:.1f}}}\\def\\ymin{{{ymin:.1f}}}\\def\\ymax{{{ymax:.1f}}}
\\draw[->] (\\xmin-0.2,0) -- (\\xmax+0.2,0) node[below]{{$x$}};
\\draw[->] (0,\\ymin-0.2) -- (0,\\ymax+0.2) node[right]{{$y$}};
\\draw (0,0) node[below left]{{$O$}};
{node_x0}
{node_xct}
{node_yct}
{node_xcd}
{node_ycd}
\\draw[dashed] ({x0},\\ymin) -- ({x0},\\ymax);
\\draw[dashed,domain=\\xmin:\\xmax] plot (\\x, {{ {tck_tikz} }});
{giong_ct}
{giong_cd}
\\begin{{scope}}
\\clip (\\xmin,\\ymin) rectangle (\\xmax,\\ymax);
\\draw[thick,smooth,samples=200,domain=\\xmin:{d1:.2f}] plot (\\x, {{ {func_tikz} }});
\\draw[thick,smooth,samples=200,domain={d2:.2f}:\\xmax] plot (\\x, {{ {func_tikz} }});
\\end{{scope}}
\\end{{tikzpicture}}"""

    hoi_loai = random.choice(["gt_ct", "gt_cd", "diem_ct", "diem_cd", "toado_ct", "toado_cd"])
    
    if hoi_loai == "gt_ct":
        caudan = fr"""\immini{{Cho hàm số $y = f(x)$ có đồ thị như hình vẽ bên. Giá trị cực tiểu của hàm số đã cho bằng:}}{{{tikz_img}}}"""
        correct = f"${y_ct_tex}$"
        candidates = [f"${y_cd_tex}$", f"${x_ct}$", f"${x_cd}$", f"-{y_ct_tex}", "$0$"]
        loi_giai = f"Dựa vào đồ thị hàm số, điểm cực tiểu của đồ thị hàm số là $({x_ct}; {y_ct_tex})$, do đó giá trị cực tiểu của hàm số là $y_{{\\text{{CT}}}} = {y_ct_tex}$."
    elif hoi_loai == "gt_cd":
        caudan = fr"""\immini{{Cho hàm số $y = f(x)$ có đồ thị như hình vẽ bên. Giá trị cực đại của hàm số đã cho bằng:}}{{{tikz_img}}}"""
        correct = f"${y_cd_tex}$"
        candidates = [f"${y_ct_tex}$", f"${x_cd}$", f"${x_ct}$", f"-{y_cd_tex}", "$0$"]
        loi_giai = f"Dựa vào đồ thị hàm số, điểm cực đại của đồ thị hàm số là $({x_cd}; {y_cd_tex})$, do đó giá trị cực đại của hàm số là $y_{{\\text{{CĐ}}}} = {y_cd_tex}$."
    elif hoi_loai == "diem_ct":
        caudan = fr"""\immini{{Cho hàm số $y = f(x)$ có đồ thị như hình vẽ bên. Điểm cực tiểu của hàm số đã cho là:}}{{{tikz_img}}}"""
        correct = f"$x = {x_ct}$"
        candidates = [f"$x = {x_cd}$", f"$y = {y_ct_tex}$", f"$y = {y_cd_tex}$", f"$x = {x0}$"]
        loi_giai = f"Dựa vào đồ thị hàm số, điểm cực tiểu của hàm số là $x = {x_ct}$."
    elif hoi_loai == "diem_cd":
        caudan = fr"""\immini{{Cho hàm số $y = f(x)$ có đồ thị như hình vẽ bên. Điểm cực đại của hàm số đã cho là:}}{{{tikz_img}}}"""
        correct = f"$x = {x_cd}$"
        candidates = [f"$x = {x_ct}$", f"$y = {y_cd_tex}$", f"$y = {y_ct_tex}$", f"$x = {x0}$"]
        loi_giai = f"Dựa vào đồ thị hàm số, điểm cực đại của hàm số là $x = {x_cd}$."
    elif hoi_loai == "toado_ct":
        caudan = fr"""\immini{{Cho hàm số $y = f(x)$ có đồ thị như hình vẽ bên. Tọa độ điểm cực tiểu của đồ thị hàm số đã cho là:}}{{{tikz_img}}}"""
        correct = f"$({x_ct}; {y_ct_tex})$"
        candidates = [f"$({x_cd}; {y_cd_tex})$", f"$({y_ct_tex}; {x_ct})$", f"$({x_ct}; -{y_ct_tex})$"]
        loi_giai = f"Dựa vào đồ thị hàm số, điểm cực tiểu của đồ thị hàm số có tọa độ là $({x_ct}; {y_ct_tex})$."
    else:
        caudan = fr"""\immini{{Cho hàm số $y = f(x)$ có đồ thị như hình vẽ bên. Tọa độ điểm cực đại của đồ thị hàm số đã cho là:}}{{{tikz_img}}}"""
        correct = f"$({x_cd}; {y_cd_tex})$"
        candidates = [f"$({x_ct}; {y_ct_tex})$", f"$({y_cd_tex}; {x_cd})$", f"$({x_cd}; -{y_cd_tex})$"]
        loi_giai = f"Dựa vào đồ thị hàm số, điểm cực đại của đồ thị hàm số có tọa độ là $({x_cd}; {y_cd_tex})$."

    wrongs = make_unique_wrongs(correct, candidates)
    return caudan, shuffle_choices(correct, wrongs), loi_giai


def CuoiChuong1_MC_DiemThuocDoThi_Bac21():
    """PHT 2026 - Câu 11: Điểm thuộc đồ thị hàm phân thức bậc 2 trên bậc nhất"""
    x0 = random.choice([-2, -1, 1, 2])
    b = random.choice([-3, -2, -1, 1, 2, 3])
    diff = random.choice([1, -1])
    x_M = x0 + diff
    y_M = random.randint(-4, 4)
    c = y_M * diff - (x_M**2) - b * x_M
    
    if x0**2 + b*x0 + c == 0:
        c += 1
        y_M = (x_M**2 + b*x_M + c) // diff
        
    term_b = f" + {b}x" if b > 1 else (f" + x" if b == 1 else (f" - {abs(b)}x" if b < -1 else " - x"))
    term_c = f" + {c}" if c > 0 else (f" - {abs(c)}" if c < 0 else "")
    term_mau = f"x - {x0}" if x0 > 0 else f"x + {abs(x0)}"
    func_tex = f"\\dfrac{{x^2{term_b}{term_c}}}{{{term_mau}}}"
    
    names = ["M", "N", "P", "Q"]
    correct = f"${names[0]}({x_M}; {y_M})$"
    
    y_wrong_N = -y_M if y_M != 0 else 2
    pt_N = f"${names[1]}({x_M}; {y_wrong_N})$"
    
    x_P = x_M + random.choice([1, 2, -2])
    if x_P == x0:
        x_P += 2
    f_xP = (x_P**2 + b*x_P + c) / (x_P - x0)
    y_P = int(f_xP) + random.choice([1, 2, -1, -2])
    pt_P = f"${names[2]}({x_P}; {y_P})$"
    
    x_Q = x_M + random.choice([3, -1, -3])
    if x_Q in [x0, x_M, x_P]:
        x_Q = x_M + 4
    f_xQ = (x_Q**2 + b*x_Q + c) / (x_Q - x0)
    y_Q = int(f_xQ) + random.choice([1, 2, -1, -2])
    pt_Q = f"${names[3]}({x_Q}; {y_Q})$"
    
    caudan = f"Đồ thị hàm số $y = {func_tex}$ đi qua điểm nào trong các điểm cho dưới đây?"
    wrongs = [pt_N, pt_P, pt_Q]
    
    b_term_val = f" + {b}({x_M})" if b > 0 else f" - {abs(b)}({x_M})"
    c_term_val = f" + {c}" if c > 0 else (f" - {abs(c)}" if c < 0 else "")
    loi_giai = f"Thay tọa độ điểm ${names[0]}({x_M}; {y_M})$ vào phương trình hàm số:\\\\\n$y = \\dfrac{{({x_M})^2{b_term_val}{c_term_val}}}{{{x_M} - ({x0})}} = {y_M}$ (thỏa mãn).\\\\\nDo đó đồ thị hàm số đi qua điểm ${names[0]}({x_M}; {y_M})$."
    
    return caudan, shuffle_choices(correct, wrongs), loi_giai


def CuoiChuong1_MC_GiaoDiem_DoThi_NhatBien():
    """PHT 2026 - Câu 12: Tọa độ giao điểm của đồ thị hàm nhất biến với hai trục tọa độ"""
    configs = [
        (1, 1, 2, 2),
        (-1, 1, 1, -1),
        (1, 2, -1, -2),
        (2, 1, 4, 2),
        (-1, 2, 2, -4),
        (1, -1, 3, -3),
        (2, -1, -2, 1),
        (-2, 1, 2, -1),
    ]
    x0, y0, xA, yB = random.choice(configs)
    
    xmin = min(-2.5, xA - 1.2, x0 - 1.5)
    xmax = max(4.5, xA + 1.5, x0 + 1.5)
    ymin = min(-4.5, yB - 1.5, y0 - 1.5)
    ymax = max(4.5, yB + 1.5, y0 + 1.5)
    
    node_x0 = f"\\draw ({x0},0) node[below]{{${x0}$}};" if x0 != 0 else ""
    node_y0 = f"\\draw (0,{y0}) node[left]{{${y0}$}};" if y0 != 0 else ""
    node_xA = f"\\draw ({xA},0) node[below]{{${xA}$}};" if xA != 0 else ""
    node_yB = f"\\draw (0,{yB}) node[above left]{{${yB}$}};" if yB != 0 else ""
    
    d1 = x0 - 0.25
    d2 = x0 + 0.25
    
    func_plot = f"({y0}*(\\x) - ({y0*xA})) / ((\\x) - ({x0}))"
    
    tikz_img = f"""\\begin{{tikzpicture}}[scale=0.65, line join=round, line cap=round, >=stealth, font=\\footnotesize]
\\tikzset{{every node/.style={{scale=0.9}}}}
\\def\\xmin{{{xmin:.1f}}}\\def\\xmax{{{xmax:.1f}}}\\def\\ymin{{{ymin:.1f}}}\\def\\ymax{{{ymax:.1f}}}
\\draw[->] (\\xmin-0.2,0) -- (\\xmax+0.2,0) node[below]{{$x$}};
\\draw[->] (0,\\ymin-0.2) -- (0,\\ymax+0.2) node[right]{{$y$}};
\\draw (0,0) node[below left]{{$O$}};
{node_x0}
{node_y0}
{node_xA}
{node_yB}
\\draw[dashed] ({x0},\\ymin) -- ({x0},\\ymax);
\\draw[dashed] (\\xmin,{y0}) -- (\\xmax,{y0});
\\fill ({xA},0) circle (1.5pt);
\\fill (0,{yB}) circle (1.5pt);
\\begin{{scope}}
\\clip (\\xmin,\\ymin) rectangle (\\xmax,\\ymax);
\\draw[thick,smooth,samples=200,domain=\\xmin:{d1:.2f}] plot (\\x, {{ {func_plot} }});
\\draw[thick,smooth,samples=200,domain={d2:.2f}:\\xmax] plot (\\x, {{ {func_plot} }});
\\end{{scope}}
\\end{{tikzpicture}}"""

    hoi_truc = random.choice(["Ox", "Oy"])
    if hoi_truc == "Ox":
        caudan = fr"""\immini{{Cho hàm số $y = \dfrac{{ax+b}}{{cx+d}}$ có đồ thị như hình vẽ bên. Tọa độ giao điểm của đồ thị hàm số với trục hoành là:}}{{{tikz_img}}}"""
        correct = f"$({xA}; 0)$"
        candidates = [f"$(0; {yB})$", f"$({x0}; 0)$", f"$(0; {y0})$", f"$({-xA}; 0)$"]
        loi_giai = f"Dựa vào đồ thị hàm số, đồ thị cắt trục hoành tại điểm có hoành độ $x = {xA}$, do đó tọa độ giao điểm của đồ thị hàm số với trục hoành là $({xA}; 0)$."
    else:
        caudan = fr"""\immini{{Cho hàm số $y = \dfrac{{ax+b}}{{cx+d}}$ có đồ thị như hình vẽ bên. Tọa độ giao điểm của đồ thị hàm số với trục tung là:}}{{{tikz_img}}}"""
        correct = f"$(0; {yB})$"
        candidates = [f"$({xA}; 0)$", f"$(0; {y0})$", f"$({x0}; 0)$", f"$(0; {-yB})$"]
        loi_giai = f"Dựa vào đồ thị hàm số, đồ thị cắt trục tung tại điểm có tung độ $y = {yB}$, do đó tọa độ giao điểm của đồ thị hàm số với trục tung là $(0; {yB})$."

    wrongs = make_unique_wrongs(correct, candidates)
    return caudan, shuffle_choices(correct, wrongs), loi_giai


def CuoiChuong1_MC_SoSanh_GiaTri_DauDaoHam():
    """PHT 2026 - Câu 13: So sánh giá trị hàm số khi biết dấu của đạo hàm"""
    sign_pos = random.choice([True, False])
    x1 = random.randint(-4, 4)
    diff = random.randint(1, 4)
    x2 = x1 + diff
    
    if random.choice([True, False]):
        u, v = x1, x2
    else:
        u, v = x2, x1
        
    sign_str = "> 0" if sign_pos else "< 0"
    tinh_chat = "đồng biến" if sign_pos else "nghịch biến"
    
    caudan = f"Cho hàm số $y = f\\left(x\\right)$ có đạo hàm trên $\\mathbb{{R}}$ thỏa mãn $f'\\left(x\\right) {sign_str}, \\forall x \\in \\mathbb{{R}}$. Mệnh đề nào dưới đây đúng?"
    
    if sign_pos:
        is_u_smaller = (u < v)
    else:
        is_u_smaller = (u > v)
        
    if is_u_smaller:
        correct = f"$f\\left({u}\\right) - f\\left({v}\\right) < 0$"
        wrongs = [
            f"$f\\left({u}\\right) - f\\left({v}\\right) \\ge 0$",
            f"$f\\left({u}\\right) > f\\left({v}\\right)$",
            f"$f\\left({u}\\right) = f\\left({v}\\right)$"
        ]
        rel_str = f"f\\left({u}\\right) < f\\left({v}\\right) \\Leftrightarrow f\\left({u}\\right) - f\\left({v}\\right) < 0"
    else:
        correct = f"$f\\left({u}\\right) - f\\left({v}\\right) > 0$"
        wrongs = [
            f"$f\\left({u}\\right) - f\\left({v}\\right) \\le 0$",
            f"$f\\left({u}\\right) < f\\left({v}\\right)$",
            f"$f\\left({u}\\right) = f\\left({v}\\right)$"
        ]
        rel_str = f"f\\left({u}\\right) > f\\left({v}\\right) \\Leftrightarrow f\\left({u}\\right) - f\\left({v}\\right) > 0"
        
    loi_giai = (
        f"Vì $f'\\left(x\\right) {sign_str}, \\forall x \\in \\mathbb{{R}}$ nên hàm số $y = f\\left(x\\right)$ {tinh_chat} trên $\\mathbb{{R}}$.\\\\\n"
        f"Vì ${min(u, v)} < {max(u, v)}$ nên ${rel_str}$."
    )
    return caudan, shuffle_choices(correct, wrongs), loi_giai


def CuoiChuong1_MC_KhangDinh_CucTri_HamBac3():
    """PHT 2026 - Câu 14: Khẳng định đúng sai về cực trị của hàm số bậc ba"""
    for _ in range(100):
        # Pick fractional or integer root
        if random.random() < 0.6:
            # Mode with a fraction root (like 7x^3 + 9x^2 - 3x - 4)
            q = random.choice([2, 3, 5, 7])
            p_candidates = [x for x in [-3, -2, -1, 1, 2, 3] if math.gcd(abs(x), q) == 1]
            p = random.choice(p_candidates)
            x1 = random.choice([-2, -1, 1, 2])
            if Fraction(p, q) == x1:
                continue
            if (q * x1 + p) % 2 == 0:
                k = random.choice([1, -1])
            else:
                k = random.choice([2, -2])
        else:
            # Mode with integer roots
            q = 1
            x1 = random.choice([-3, -2, -1, 0, 1, 2])
            x2 = random.choice([x for x in [-2, -1, 1, 2, 3] if x != x1])
            p = x2
            if (x1 + p) % 2 == 0:
                k = random.choice([1, -1])
            else:
                k = random.choice([2, -2])
                
        a = k * q
        b = - (3 * k * (q * x1 + p)) // 2
        c = 3 * k * p * x1
        d = random.randint(-5, 5)
        
        r1 = Fraction(x1, 1)
        r2 = Fraction(p, q)
        
        # Calculate y values
        y_r1 = a * (r1**3) + b * (r1**2) + c * r1 + d
        y_r2 = a * (r2**3) + b * (r2**2) + c * r2 + d
        
        if a > 0:
            if r1 < r2:
                x_cd, y_cd = r1, y_r1
                x_ct, y_ct = r2, y_r2
            else:
                x_cd, y_cd = r2, y_r2
                x_ct, y_ct = r1, y_r1
        else:
            if r1 < r2:
                x_ct, y_ct = r1, y_r1
                x_cd, y_cd = r2, y_r2
            else:
                x_ct, y_ct = r2, y_r2
                x_cd, y_cd = r1, y_r1
                
        # Check condition that x and y are not identical (to make the trap valid)
        if x_ct == y_ct or x_cd == y_cd:
            continue
            
        break

    poly_tex = format_poly_bac3(a, b, c, d)
    caudan = f"Cho hàm số $y = {poly_tex}$. Khẳng định nào sau đây là \\textbf{{sai}}?"
    
    x_cd_tex = fmt_frac_latex(x_cd)
    y_cd_tex = fmt_frac_latex(y_cd)
    x_ct_tex = fmt_frac_latex(x_ct)
    y_ct_tex = fmt_frac_latex(y_ct)
    
    # Decide trap type:
    if random.choice([True, False]):
        # Trap 1: False is "Giá trị cực tiểu y = x_ct"
        correct = f"Giá trị cực tiểu $y = {x_ct_tex}$"
        wrongs = [
            f"Giá trị cực đại $y = {y_cd_tex}$",
            f"Hàm số đạt cực tiểu tại $x = {x_ct_tex}$",
            f"Hàm số đạt cực đại tại $x = {x_cd_tex}$"
        ]
        false_explanation = (
            f"giá trị cực tiểu của hàm số là $y = {y_ct_tex}$, còn $x = {x_ct_tex}$ là điểm cực tiểu của hàm số"
        )
    else:
        # Trap 2: False is "Giá trị cực đại y = x_cd"
        correct = f"Giá trị cực đại $y = {x_cd_tex}$"
        wrongs = [
            f"Giá trị cực tiểu $y = {y_ct_tex}$",
            f"Hàm số đạt cực đại tại $x = {x_cd_tex}$",
            f"Hàm số đạt cực tiểu tại $x = {x_ct_tex}$"
        ]
        false_explanation = (
            f"giá trị cực đại của hàm số là $y = {y_cd_tex}$, còn $x = {x_cd_tex}$ là điểm cực đại của hàm số"
        )
        
    deriv_tex = format_poly_bac2(3 * a, 2 * b, c)
    loi_giai = (
        f"Ta có $y' = {deriv_tex}$.\\\\\n"
        f"$y' = 0 \\Leftrightarrow x = {x_cd_tex}$ hoặc $x = {x_ct_tex}$.\\\\\n"
        f"Vì hệ số $a = {a} {'> 0' if a > 0 else '< 0'}$ nên:\\\\\n"
        f"- Hàm số đạt cực đại tại $x = {x_cd_tex}$, giá trị cực đại $y = {y_cd_tex}$.\\\\\n"
        f"- Hàm số đạt cực tiểu tại $x = {x_ct_tex}$, giá trị cực tiểu $y = {y_ct_tex}$.\\\\\n"
        f"Do đó {false_explanation}, nên khẳng định \"{correct}\" là \\textbf{{sai}}."
    )
    return caudan, shuffle_choices(correct, wrongs), loi_giai


def CuoiChuong1_MC_KhaoSat_DoThi_NhatBien_GioiHan():
    """PHT 2026 - Câu 15: Đọc giới hạn và tính chất từ đồ thị hàm nhất biến"""
    configs = [
        # (x0, y0, xA, yB) where y = (y0*x - y0*xA)/(x - x0)
        (1, 1, 2, 2),      # y = (x - 2)/(x - 1), y' > 0
        (-1, 1, 1, -1),    # y = (x - 1)/(x + 1), y' > 0
        (1, 2, -1, -2),    # y = (2x + 2)/(x - 1), y' < 0
        (2, 1, 4, 2),      # y = (x - 4)/(x - 2), y' > 0
        (-1, 2, 2, -4),    # y = (2x - 4)/(x + 1), y' > 0
        (1, -1, 3, -3),    # y = (-x + 3)/(x - 1), y' < 0
        (-2, 1, 2, -1),    # y = (x - 2)/(x + 2), y' > 0
    ]
    x0, y0, xA, yB = random.choice(configs)
    
    is_increasing = (y0 * (xA - x0) > 0)
    
    xmin = min(-3.5, x0 - 2.0, xA - 1.5)
    xmax = max(4.5, x0 + 2.5, xA + 1.5)
    ymin = min(-3.0, y0 - 2.0, yB - 1.5)
    ymax = max(4.0, y0 + 2.5, yB + 1.5)
    
    node_x0 = f"\\draw ({x0},0) node[above right]{{${x0}$}};" if x0 != 0 else ""
    node_y0 = f"\\draw (0,{y0}) node[below left]{{${y0}$}};" if y0 != 0 else ""
    node_xA = f"\\draw ({xA},0) node[below]{{${xA}$}};" if xA != 0 and xA != x0 else ""
    node_yB = f"\\draw (0,{yB}) node[left]{{${yB}$}};" if yB != 0 and yB != y0 else ""
    
    d1 = x0 - 0.15
    d2 = x0 + 0.15
    func_plot = f"({y0}*(\\x) - ({y0*xA})) / ((\\x) - ({x0}))"
    
    tikz_img = f"""\\begin{{tikzpicture}}[scale=0.65, line join=round, line cap=round, >=stealth, font=\\footnotesize]
\\tikzset{{every node/.style={{scale=0.9}}}}
\\def\\xmin{{{xmin:.1f}}}\\def\\xmax{{{xmax:.1f}}}\\def\\ymin{{{ymin:.1f}}}\\def\\ymax{{{ymax:.1f}}}
\\draw[->] (\\xmin-0.2,0) -- (\\xmax+0.2,0) node[below]{{$x$}};
\\draw[->] (0,\\ymin-0.2) -- (0,\\ymax+0.2) node[above]{{$y$}};
\\draw (0,0) node[below left]{{$O$}};
{node_x0}
{node_y0}
{node_xA}
{node_yB}
\\draw[dashed] (\\xmin,{y0}) -- (\\xmax,{y0});
\\draw[dashed] ({x0},\\ymin) -- ({x0},\\ymax);
\\begin{{scope}}
\\clip (\\xmin,\\ymin) rectangle (\\xmax,\\ymax);
\\draw[thick,smooth,samples=200,domain=\\xmin:{d1:.2f}] plot (\\x, {{ {func_plot} }});
\\draw[thick,smooth,samples=200,domain={d2:.2f}:\\xmax] plot (\\x, {{ {func_plot} }});
\\end{{scope}}
\\end{{tikzpicture}}"""

    caudan = fr"""\immini{{Cho hàm số $y = \dfrac{{ax + b}}{{cx + d}}$ (với $c \ne 0, ad - bc \ne 0$) có đồ thị như hình vẽ bên. Khẳng định nào sau đây đúng?}}{{{tikz_img}}}"""
    
    if is_increasing:
        lim_right = "-\\infty"
        lim_left = "+\\infty"
        dong_bien_str = "đồng biến"
    else:
        lim_right = "+\\infty"
        lim_left = "-\\infty"
        dong_bien_str = "nghịch biến"
        
    correct = f"$\\lim\\limits_{{x \\to {x0}^+}} f\\left(x\\right) = {lim_right}$ và $\\lim\\limits_{{x \\to {x0}^-}} f\\left(x\\right) = {lim_left}$"
    
    wrongs = [
        "Đồ thị hàm số có hai điểm cực trị",
        f"$\\lim\\limits_{{x \\to -\\infty}} f\\left(x\\right) = +\\infty$ và $\\lim\\limits_{{x \\to +\\infty}} f\\left(x\\right) = -\\infty$",
        f"Hàm số {dong_bien_str} trên khoảng $\\left(-\\infty; +\\infty\\right)$"
    ]
    
    loi_giai = (
        f"Dựa vào đồ thị hàm số, ta thấy:\\\\\n"
        f"- Đồ thị hàm số có đường tiệm cận đứng là $x = {x0}$, trong đó $\\lim\\limits_{{x \\to {x0}^+}} f(x) = {lim_right}$ và $\\lim\\limits_{{x \\to {x0}^-}} f(x) = {lim_left}$.\\\\\n"
        f"- Đường tiệm cận ngang là $y = {y0}$, tức là $\\lim\\limits_{{x \\to \\pm\\infty}} f(x) = {y0}$.\\\\\n"
        f"- Hàm số nhất biến $y = \\dfrac{{ax+b}}{{cx+d}}$ luôn đơn điệu trên từng khoảng xác định và không có điểm cực trị.\\\\\n"
        f"Do đó khẳng định đúng là: {correct}."
    )
    
    return caudan, shuffle_choices(correct, wrongs), loi_giai






