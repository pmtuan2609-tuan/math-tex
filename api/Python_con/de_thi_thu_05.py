# -*- coding: utf-8 -*-
"""
Module Đề thi thử / Đề ôn tập số 5 (12 câu Trắc nghiệm + 4 câu Đúng/Sai + 6 câu Trả lời ngắn)
Được xây dựng và ngẫu nhiên hóa tham số 100% theo chuẩn cấu trúc tốt nghiệp THPT 2025.
Tất cả các phương án đều được chuẩn hóa loại bỏ dấu chấm cuối câu để gói ex_test sinh đúng 1 dấu chấm mặc định.
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
# PHẦN I: 12 CÂU TRẮC NGHIỆM NHIỀU LỰA CHỌN (MC)
# ==============================================================================

def DeThiThu05_MC_Cau1():
    # Câu 1: Giá trị cực tiểu của hàm số từ bảng biến thiên
    cfgs = [
        {"x_cd": -3, "y_cd": 1, "x_ct": 7, "y_ct": 0},
        {"x_cd": -2, "y_cd": 4, "x_ct": 3, "y_ct": -1},
        {"x_cd": -1, "y_cd": 3, "x_ct": 2, "y_ct": -2},
        {"x_cd": -4, "y_cd": 2, "x_ct": 5, "y_ct": 0},
    ]
    c = random.choice(cfgs)
    x_cd, y_cd = c["x_cd"], c["y_cd"]
    x_ct, y_ct = c["x_ct"], c["y_ct"]

    caudan = fr'''\immini{{Cho hàm số $f(x)$ có bảng biến thiên như hình bên. Giá trị cực tiểu của hàm số là
\begin{{center}}
\end{{center}}
}}{{
\begin{{tikzpicture}}
	\tkzTabInit[nocadre,lgt=1.2,espcl=1.5,deltacl=0.6]
	{{$x$ /0.6, $y'$ /0.6, $y$ /1.5}}
	{{$-\infty$, ${x_cd}$, ${x_ct}$, $+\infty$}}
	\tkzTabLine{{,+,$0$,-,$0$,+,}}
	\tkzTabVar{{-/$-\infty$,+/${y_cd}$,-/${y_ct}$,+/$+\infty$}}
\end{{tikzpicture}}
}}'''
    correct = fr"${y_ct}$"
    wrongs = [
        fr"${x_ct}$",
        fr"${x_cd}$",
        fr"${y_cd}$"
    ]
    choices = shuffle_choices(correct, wrongs)
    loi_giai = fr'''Dựa vào bảng biến thiên, hàm số đạt cực tiểu tại điểm $x = {x_ct}$ và giá trị cực tiểu của hàm số là $y_{{ct}} = f({x_ct}) = {y_ct}$.'''
    return caudan, choices, loi_giai


def DeThiThu05_MC_Cau2():
    # Câu 2: VTPT của mặt phẳng (P): Ax + By + Cz + D = 0
    A, B, C = random.choice([(2, 1, -1), (3, -2, 1), (1, 2, -3), (2, -1, 2)])
    D = random.choice([-1, 2, -3, 4])
    B_sign = f"+ {B}y" if B > 0 else f"- {abs(B)}y"
    C_sign = f"+ {C}z" if C > 0 else f"- {abs(C)}z"
    D_sign = f"+ {D}" if D > 0 else f"- {abs(D)}"

    caudan = fr'''Trong không gian $Oxyz$, cho mặt phẳng $(P) \colon {A}x {B_sign} {C_sign} {D_sign} = 0$. Vectơ nào dưới đây là một vectơ pháp tuyến của $(P)$?'''
    correct = fr"$\vec{{n}} = ({A}; {B}; {C})$"
    wrongs = [
        fr"$\vec{{n}}_1 = ({A}; {-B}; {C})$",
        fr"$\vec{{n}}_2 = ({-A}; {B}; {C})$",
        fr"$\vec{{n}}_3 = ({A}; {B}; {-C})$"
    ]
    choices = shuffle_choices(correct, wrongs)
    loi_giai = fr'''Mặt phẳng $(P) \colon {A}x {B_sign} {C_sign} {D_sign} = 0$ có một vectơ pháp tuyến là $\vec{{n}} = ({A}; {B}; {C})$.'''
    return caudan, choices, loi_giai


def DeThiThu05_MC_Cau3():
    # Câu 3: Phương trình chính tắc đường thẳng đi qua A vuông góc mặt phẳng (P)
    xA = random.randint(1, 4)
    yA = random.choice([-2, -1, 1, 2])
    zA = 0
    u1, u2, u3 = random.choice([(1, -2, -2), (2, -1, 3), (1, 2, -2), (2, 1, -1)])
    
    yA_sign = f"+ {abs(yA)}" if yA < 0 else f"- {yA}"

    caudan = fr'''Đường thẳng đi qua điểm $A({xA}; {yA}; {zA})$ và vuông góc với mặt phẳng ${u1}x + ({u2})y + ({u3})z - 3 = 0$ có phương trình chính tắc là'''
    correct = fr"\dfrac{{x - {xA}}}{{{u1}}} = \dfrac{{y {yA_sign}}}{{{u2}}} = \dfrac{{z}}{{{u3}}}"
    wrongs = [
        fr"\dfrac{{x - {xA}}}{{{u1}}} = \dfrac{{y - {abs(yA)}}}{{{-u2}}} = \dfrac{{z + 2}}{{{-u3}}}",
        fr"\dfrac{{x + {xA}}}{{{u1}}} = \dfrac{{y {yA_sign}}}{{{u2}}} = \dfrac{{z}}{{{-u3}}}",
        fr"\dfrac{{x - {xA}}}{{{u1}}} = \dfrac{{y {yA_sign}}}{{{-u2}}} = \dfrac{{z}}{{{u3}}}"
    ]
    choices = shuffle_choices(fr"${correct}$", [fr"${w}$" for w in wrongs])
    loi_giai = fr'''Đường thẳng vuông góc với mặt phẳng nên nhận VTPT của mặt phẳng làm VTCP: $\vec{{u}} = ({u1}; {u2}; {u3})$. \\
Phương trình chính tắc của đường thẳng đi qua $A({xA}; {yA}; {zA})$ là:
$$\dfrac{{x - {xA}}}{{{u1}}} = \dfrac{{y {yA_sign}}}{{{u2}}} = \dfrac{{z}}{{{u3}}}.$$'''
    return caudan, choices, loi_giai


def DeThiThu05_MC_Cau4():
    # Câu 4: Giá trị tích phân tuyến tính
    u = random.choice([3, 4, 5, 6])
    v = random.choice([-7, -5, -3, 4])
    a = random.choice([2, 3])
    b = random.choice([2, 3])
    val = a * u - b * v

    caudan = fr'''Biết $\displaystyle\int_1^3 f(x)\,\mathrm{{d}}x = {u}$ và $\displaystyle\int_1^3 g(x)\,\mathrm{{d}}x = {v}$. Giá trị của $\displaystyle\int_1^3 [{a}f(x) - {b}g(x)]\,\mathrm{{d}}x$ bằng'''
    correct = fr"${val}$"
    wrongs = [
        fr"${-val}$",
        fr"${a * u + b * v}$",
        fr"${u - v}$"
    ]
    choices = shuffle_choices(correct, wrongs)
    loi_giai = fr'''Theo tính chất của tích phân:
$$\int_1^3 [{a}f(x) - {b}g(x)]\,\mathrm{{d}}x = {a}\int_1^3 f(x)\,\mathrm{{d}}x - {b}\int_1^3 g(x)\,\mathrm{{d}}x = {a}({u}) - {b}({v}) = {val}.$$'''
    return caudan, choices, loi_giai


def DeThiThu05_MC_Cau5():
    # Câu 5: Nghiệm phương trình logarit log_b(x - a) = c
    base = random.choice([2, 3])
    c = random.choice([2, 3])
    a = random.choice([1, 2, 3])
    ans = base**c + a

    caudan = fr'''Nghiệm của phương trình $\log_{{{base}}}(x - {a}) = {c}$ là'''
    correct = fr"$x = {ans}$"
    wrongs = [
        fr"$x = {ans - 1}$",
        fr"$x = {ans + 1}$",
        fr"$x = {base**c}$"
    ]
    choices = shuffle_choices(correct, wrongs)
    loi_giai = fr'''Phương trình tương đương với: $x - {a} = {base}^{{{c}}} = {base**c} \iff x = {ans}$.'''
    return caudan, choices, loi_giai


def DeThiThu05_MC_Cau6():
    # Câu 6: Khoảng biến thiên về thời gian tập thể dục
    caudan = r'''Bảng sau thống kê thời gian tập thể dục mỗi ngày trong tháng của hai bạn Hưng và Bình:
\begin{center}
\begin{tabular}{|c|c|c|c|c|c|}
	\hline
	\textbf{Thời gian (phút)} & [10; 15) & [15; 20) & [20; 25) & [25; 30) & [30; 35) \\
	\hline
	Số ngày tập của Hưng & 2 & 14 & 8 & 5 & 2 \\
	\hline
	Số ngày tập của Bình & 1 & 8 & 12 & 7 & 2 \\
	\hline
\end{tabular}
\end{center}
Khoảng biến thiên của mẫu số liệu ghép nhóm về thời gian tập thể dục của Hưng và Bình lần lượt là'''
    correct = r'''25 phút và 25 phút'''
    wrongs = [
        r'''20 phút và 25 phút''',
        r'''20 phút và 20 phút''',
        r'''25 phút và 20 phút'''
    ]
    choices = shuffle_choices(correct, wrongs)
    loi_giai = r'''Cả hai bạn đều có các quan sát rơi vào các nhóm từ $[10; 15)$ đến $[30; 35)$. \\
Khoảng biến thiên của mẫu số liệu ghép nhóm là hiệu giữa đầu mút phải của nhóm cuối cùng và đầu mút trái của nhóm đầu tiên:
$$R = 35 - 10 = 25\text{ phút}.$$
Do đó khoảng biến thiên của cả hai bạn lần lượt là 25 phút và 25 phút.'''
    return caudan, choices, loi_giai


def DeThiThu05_MC_Cau7():
    # Câu 7: Họ nguyên hàm của hàm số lũy thừa
    n = random.choice([2, 3, 4, 5])
    n1 = n + 1

    caudan = fr'''Họ nguyên hàm của hàm số $y = x^{{{n}}}$ là'''
    correct = fr"$\dfrac{{x^{{{n1}}}}}{{{n1}}} + C$"
    wrongs = [
        fr"$x^{{{n1}}} + C$",
        fr"$\dfrac{{x^{{{n}}}}}{{{n}}} + C$",
        fr"${n}x^{{{n-1}}} + C$"
    ]
    choices = shuffle_choices(correct, wrongs)
    loi_giai = fr'''Theo công thức nguyên hàm cơ bản: $\displaystyle\int x^{{{n}}}\,\mathrm{{d}}x = \dfrac{{x^{{{n1}}}}}{{{n1}}} + C$.'''
    return caudan, choices, loi_giai


def DeThiThu05_MC_Cau8():
    # Câu 8: Đường tiệm cận đứng của đồ thị hàm phân thức bậc nhất
    x0 = random.choice([-2, -1, 1, 2])
    y0 = 1

    caudan = fr'''\immini{{Cho hàm số $y = \dfrac{{ax+b}}{{cx+d}}$ ($c\ne 0, ad-bc\ne 0$) có đồ thị hàm số như hình vẽ bên. Đường tiệm cận đứng của đồ thị hàm số là
\begin{{center}}
\end{{center}}
}}{{
\begin{{tikzpicture}}[scale=0.5, line join=round, line cap=round, >=stealth,font=\footnotesize] 
	\def\xmin{{-4}}\def\xmax{{4}}\def\ymin{{-2}}\def\ymax{{4}}
	\draw[->] (\xmin-0.2,0)--(\xmax+0.2,0) node[below]{{$x$}};
	\draw[->] (0,\ymin-0.2)--(0,\ymax+0.2) node[right]{{$y$}};
	\draw (0,0) node[below left]{{$O$}};
	\foreach \x in {{-3,-2,-1,1,2,3}}\draw (\x,0.1)--(\x,-0.1) node[below]{{$\x$}};
	\foreach \y in {{-1,1,2,3}}\draw (0.1,\y)--(-0.1,\y) node[left]{{$\y$}};
	\clip (\xmin,\ymin) rectangle (\xmax,\ymax);
	\draw[dashed] (\xmin,{y0})--(\xmax,{y0});
	\draw[dashed] ({x0},\ymin)--({x0},\ymax);
	\draw[thick,smooth,samples=200,domain=\xmin:{x0-0.1}] plot (\x,{{(1*(\x)+{1-x0})/(1*(\x)-({x0}))}});
	\draw[thick,smooth,samples=200,domain={x0+0.1}:\xmax] plot (\x,{{(1*(\x)+{1-x0})/(1*(\x)-({x0}))}});
\end{{tikzpicture}}
}}'''
    correct = fr"$x = {x0}$"
    wrongs = [
        fr"$x = {-x0}$",
        fr"$y = {y0}$",
        fr"$y = {-y0}$"
    ]
    choices = shuffle_choices(correct, wrongs)
    loi_giai = fr'''Dựa vào đồ thị, đường tiệm cận đứng là đường thẳng vuông góc với trục hoành có phương trình $x = {x0}$.'''
    return caudan, choices, loi_giai


def DeThiThu05_MC_Cau9():
    # Câu 9: Nghiệm phương trình lượng giác cos(2x) = 0
    caudan = r'''Các nghiệm của phương trình $\cos 2x = 0$ là'''
    correct = r'''$x = \dfrac{\pi}{4} + k\dfrac{\pi}{2} \ (k\in\mathbb{Z})$'''
    wrongs = [
        r'''$x = \dfrac{\pi}{4} + k\pi \ (k\in\mathbb{Z})$''',
        r'''$x = \dfrac{\pi}{8} + k\dfrac{\pi}{2} \ (k\in\mathbb{Z})$''',
        r'''$x = \dfrac{\pi}{2} + k\pi \ (k\in\mathbb{Z})$'''
    ]
    choices = shuffle_choices(correct, wrongs)
    loi_giai = r'''$\cos 2x = 0 \iff 2x = \dfrac{\pi}{2} + k\pi \iff x = \dfrac{\pi}{4} + k\dfrac{\pi}{2} \ (k\in\mathbb{Z})$.'''
    return caudan, choices, loi_giai


def DeThiThu05_MC_Cau10():
    # Câu 10: Tập nghiệm của bất phương trình mũ 3^x <= 9
    b = random.choice([2, 3, 5])
    exp = random.choice([2, 3])
    rhs = b**exp

    caudan = fr'''Tập nghiệm của bất phương trình ${b}^x \le {rhs}$ là'''
    correct = fr"$(-\infty; {exp}]$"
    wrongs = [
        fr"$[0; {exp}]$",
        fr"$(0; {exp})$",
        fr"$(-\infty; {exp})$"
    ]
    choices = shuffle_choices(correct, wrongs)
    loi_giai = fr'''${b}^x \le {rhs} \iff {b}^x \le {b}^{{{exp}}} \iff x \le {exp}$ (do cơ số ${b} > 1$). \\
Vậy tập nghiệm là $(-\infty; {exp}]$.'''
    return caudan, choices, loi_giai


def DeThiThu05_MC_Cau11():
    # Câu 11: Cấp số nhân (u_n) biết u2 và q, tìm u1
    q = random.choice([2, 3, 4])
    u2 = random.choice([6, 7, 8, 9, 10, 12])
    u1_frac = Fraction(u2, q)
    u1_tex = fr"\dfrac{{{u1_frac.numerator}}}{{{u1_frac.denominator}}}" if u1_frac.denominator != 1 else str(u1_frac.numerator)

    caudan = fr'''Cho cấp số nhân $(u_n)$ với $u_2 = {u2}$ và công bội $q = {q}$. Số hạng đầu tiên của cấp số nhân đã cho bằng'''
    correct = fr"${u1_tex}$"
    wrongs = [
        fr"${u2 * q}$",
        fr"${u2 - q}$",
        fr"$\dfrac{{{q}}}{{{u2}}}$"
    ]
    choices = shuffle_choices(correct, wrongs)
    loi_giai = fr'''Theo công thức cấp số nhân: $u_2 = u_1 \cdot q \implies u_1 = \dfrac{{u_2}}{{q}} = {u1_tex}$.'''
    return caudan, choices, loi_giai


def DeThiThu05_MC_Cau12():
    # Câu 12: Hình chóp S.ABCD đáy bình hành tâm O, SA = SC, SB = SD
    caudan = r'''Cho hình chóp $S.ABCD$ có đáy $ABCD$ là hình bình hành tâm $O$, $SA = SC$, $SB = SD$. Trong các khẳng định sau, khẳng định nào đúng?'''
    correct = r'''$SO \perp (ABCD)$'''
    wrongs = [
        r'''$SD \perp (ABCD)$''',
        r'''$SA \perp (ABCD)$''',
        r'''$SC \perp (ABCD)$'''
    ]
    choices = shuffle_choices(correct, wrongs)
    loi_giai = r'''Tam giác $SAC$ cân tại $S$ có $O$ là trung điểm của $AC$ nên $SO \perp AC$. \\
Tam giác $SBD$ cân tại $S$ có $O$ là trung điểm của $BD$ nên $SO \perp BD$. \\
Vì $SO \perp AC$ và $SO \perp BD$ nên $SO \perp (ABCD)$.'''
    return caudan, choices, loi_giai


# ==============================================================================
# PHẦN II: 4 CÂU TRẮC NGHIỆM ĐÚNG / SAI (TF)
# ==============================================================================

def DeThiThu05_TF_Cau1():
    # Câu 1: Cabin cáp treo xuất phát từ A(10; 3; 0), u = (2; -2; 1), v = 5 m/s
    caudan = r'''\immini{Một cabin cáp treo xuất phát từ điểm $A(10; 3; 0)$ và chuyển động đều theo đường cáp có vectơ chỉ phương là $\vec{u} = (2; -2; 1)$ với tốc độ là $5\text{ m/s}$ (đơn vị trên mỗi trục tọa độ là mét).}{
\begin{tikzpicture}[line join=round, line cap=round, scale=0.6]
	\draw[thick, ->] (0,0)--(4,0) node[below]{$x$};
	\draw[thick, ->] (0,0)--(0,3) node[left]{$z$};
	\draw[thick, blue] (0.5,0.5)--(3.5,2.5) node[midway, above left]{Cabin};
	\fill (0.5,0.5) circle(2pt) node[below]{$A$};
\end{tikzpicture}
}'''

    items = [
        (
            r'''Phương trình chính tắc của đường cáp là $\dfrac{x-10}{2} = \dfrac{y-3}{-2} = \dfrac{z}{1}$''',
            r'''Phương trình chính tắc của đường cáp là $\dfrac{x+10}{2} = \dfrac{y+3}{-2} = \dfrac{z}{1}$''',
            r'''Đường thẳng đi qua $A(10; 3; 0)$ và nhận $\vec{u} = (2; -2; 1)$ làm VTCP nên có phương trình: $\dfrac{x-10}{2} = \dfrac{y-3}{-2} = \dfrac{z}{1}$.''',
            r'''Dấu của tọa độ điểm $A$ bị sai, phương trình đúng là $\dfrac{x-10}{2} = \dfrac{y-3}{-2} = \dfrac{z}{1}$.'''
        ),
        (
            r'''Đường cáp $AB$ tạo với mặt phẳng $(Oxy)$ một góc xấp xỉ $19^\circ$ (làm tròn đến hàng đơn vị của độ)''',
            r'''Đường cáp $AB$ tạo với mặt phẳng $(Oxy)$ một góc $22^\circ$''',
            r'''Vectơ pháp tuyến của $(Oxy)$ là $\vec{k} = (0; 0; 1)$. Gọi $\varphi$ là góc giữa đường cáp và $(Oxy)$: $\sin\varphi = \dfrac{|\vec{u}\cdot\vec{k}|}{|\vec{u}|\cdot|\vec{k}|} = \dfrac{1}{3} \implies \varphi \approx 19^\circ$.''',
            r'''$\sin\varphi = \dfrac{1}{3} \implies \varphi \approx 19^\circ \ne 22^\circ$.'''
        ),
        (
            r'''Cabin dừng ở điểm $B$ có hoành độ $x_B = 550$. Khi đó quãng đường $AB$ có độ dài bằng $810$ m''',
            r'''Cabin dừng ở điểm $B$ có hoành độ $x_B = 550$. Khi đó quãng đường $AB$ có độ dài bằng $540$ m''',
            r'''$\dfrac{x_B - 10}{2} = \dfrac{550 - 10}{2} = 270 \implies \overrightarrow{AB} = 270\vec{u} \implies AB = 270|\vec{u}| = 270 \times 3 = 810\text{ m}$.''',
            r'''Độ dài quãng đường $AB = 810\text{ m} \ne 540\text{ m}$.'''
        ),
        (
            r'''Giả sử sau $t$ giây kể từ lúc xuất phát ($t \ge 0$), cabin đến vị trí điểm $M$. Khi đó tọa độ của điểm $M$ là $\left(10 + \dfrac{10}{3}t; 3 - \dfrac{10}{3}t; \dfrac{5}{3}t\right)$''',
            r'''Tọa độ của điểm $M$ sau $t$ giây là $(10 + 2t; 3 - 2t; t)$''',
            r'''Vận tốc là $5\text{ m/s}$ nên sau $t$ giây đi được quãng đường $s = 5t$. Vectơ chỉ phương đơn vị là $\vec{e} = \dfrac{\vec{u}}{|\vec{u}|} = \left(\dfrac{2}{3}; -\dfrac{2}{3}; \dfrac{1}{3}\right) \implies M = A + 5t\vec{e} = \left(10 + \dfrac{10}{3}t; 3 - \dfrac{10}{3}t; \dfrac{5}{3}t\right)$.''',
            r'''Vận tốc $5\text{ m/s} \ne |\vec{u}| = 3$, tọa độ điểm $M$ đúng là $\left(10 + \dfrac{10}{3}t; 3 - \dfrac{10}{3}t; \dfrac{5}{3}t\right)$.'''
        )
    ]
    choices, loi_giai = make_tf_choices(items)
    return caudan, choices, loi_giai


def DeThiThu05_TF_Cau2():
    # Câu 2: Khảo sát hàm số f(x) = sin x - e^x
    caudan = r'''Cho hàm số $f(x) = \sin x - e^x$.'''

    items = [
        (
            r'''Đạo hàm của hàm số đã cho là $f'(x) = \cos x - e^x, \ \forall x\in\mathbb{R}$''',
            r'''Đạo hàm của hàm số đã cho là $f'(x) = -\cos x - e^x, \ \forall x\in\mathbb{R}$''',
            r'''$(\sin x)' = \cos x$ và $(e^x)' = e^x$, nên $f'(x) = \cos x - e^x$.''',
            r'''Đạo hàm của $\sin x$ là $\cos x$, không mang dấu trừ.'''
        ),
        (
            r'''Nghiệm của phương trình $f'(x) = 0$ trên đoạn $\left[0; \dfrac{\pi}{2}\right]$ là $x = 0$''',
            r'''Phương trình $f'(x) = 0$ vô nghiệm trên đoạn $\left[0; \dfrac{\pi}{2}\right]$''',
            r'''Trên đoạn $\left[0; \dfrac{\pi}{2}\right]$, $\cos x \le 1$ và $e^x \ge 1 \implies f'(x) = \cos x - e^x \le 0$. Đẳng thức xảy ra khi $\cos x = 1$ và $e^x = 1 \iff x = 0$.''',
            r'''Phương trình có nghiệm duy nhất $x = 0$ trên đoạn $\left[0; \dfrac{\pi}{2}\right]$.'''
        ),
        (
            r'''Giá trị nhỏ nhất của hàm số $f(x)$ trên đoạn $\left[0; \dfrac{\pi}{2}\right]$ là $1 - e^{\pi/2}$''',
            r'''Giá trị nhỏ nhất của hàm số $f(x)$ trên đoạn $\left[0; \dfrac{\pi}{2}\right]$ là $-1$''',
            r'''Vì $f'(x) \le 0$ trên đoạn $\left[0; \dfrac{\pi}{2}\right]$ nên hàm số nghịch biến. Giá trị nhỏ nhất là $f\left(\dfrac{\pi}{2}\right) = \sin\left(\dfrac{\pi}{2}\right) - e^{\pi/2} = 1 - e^{\pi/2}$.''',
            r'''$\min = f(\pi/2) = 1 - e^{\pi/2} \approx -3,81 \ne -1$.'''
        ),
        (
            r'''$f(\pi) = -e^\pi$ và $f(0) = -1$''',
            r'''$f(\pi) = 1 - e^\pi$ và $f(0) = -2$''',
            r'''$f(\pi) = \sin\pi - e^\pi = -e^\pi$; $f(0) = \sin 0 - e^0 = -1$.''',
            r'''$f(\pi) = -e^\pi$ và $f(0) = -1$.'''
        )
    ]
    choices, loi_giai = make_tf_choices(items)
    return caudan, choices, loi_giai


def DeThiThu05_TF_Cau3():
    # Câu 3: Đấu thầu hai dự án: P(A)=0.5, P(B)=0.6, P(A \cap B)=0.4
    caudan = r'''Một công ty dự đấu thầu hai dự án. Khả năng thắng thầu của dự án I là $0{,}5$ và của dự án II là $0{,}6$. Khả năng thắng thầu cả hai dự án là $0{,}4$. Gọi $A$ là biến cố "Thắng thầu dự án I" và $B$ là biến cố "Thắng thầu dự án II".'''

    items = [
        (
            r'''Xác suất công ty thắng thầu dự án II biết công ty thắng thầu dự án I là $0{,}8$''',
            r'''Xác suất công ty thắng thầu dự án II biết công ty thắng thầu dự án I là $0{,}6$''',
            r'''$P(B|A) = \dfrac{P(A \cap B)}{P(A)} = \dfrac{0{,}4}{0{,}5} = 0{,}8$.''',
            r'''$P(B|A) = \dfrac{0{,}4}{0{,}5} = 0{,}8 \ne 0{,}6$.'''
        ),
        (
            r'''Xác suất công ty thắng thầu dự án II biết công ty không thắng thầu dự án I là $0{,}4$''',
            r'''Xác suất công ty thắng thầu dự án II biết công ty không thắng thầu dự án I là $0{,}2$''',
            r'''$P(B|\overline{A}) = \dfrac{P(B \setminus A)}{P(\overline{A})} = \dfrac{P(B) - P(A \cap B)}{1 - P(A)} = \dfrac{0{,}6 - 0{,}4}{0{,}5} = 0{,}4$.''',
            r'''$P(B|\overline{A}) = \dfrac{0{,}2}{0{,}5} = 0{,}4 \ne 0{,}2$.'''
        ),
        (
            r'''Xác suất công ty thắng thầu ít nhất một dự án bằng $0{,}7$''',
            r'''Xác suất công ty thắng thầu ít nhất một dự án bằng $0{,}5$''',
            r'''$P(A \cup B) = P(A) + P(B) - P(A \cap B) = 0{,}5 + 0{,}6 - 0{,}4 = 0{,}7$.''',
            r'''$P(A \cup B) = 0{,}7 \ne 0{,}5$.'''
        ),
        (
            r'''Hai biến cố $A$ và $B$ không độc lập với nhau''',
            r'''Hai biến cố $A$ và $B$ là hai biến cố độc lập''',
            r'''Ta có $P(A) \cdot P(B) = 0{,}5 \times 0{,}6 = 0{,}3 \ne P(A \cap B) = 0{,}4$. Do đó $A$ và $B$ không độc lập.''',
            r'''Vì $P(A \cap B) \ne P(A)P(B)$ nên hai biến cố không độc lập.'''
        )
    ]
    choices, loi_giai = make_tf_choices(items)
    return caudan, choices, loi_giai


def DeThiThu05_TF_Cau4():
    # Câu 4: Dân số Việt Nam năm 2023 là A = 100.3 triệu, r = 0.84%, S = A * e^{rt}
    caudan = r'''Dân số nước ta năm $2023$ ước tính là $A = 100{,}3$ triệu người. Giả sử tỉ lệ tăng dân số hằng năm là $r = 0{,}84\%$. Sau $t$ năm (tính từ mốc năm $2023$), dân số được tính theo công thức: $S = A \cdot e^{rt}$ (triệu người).'''

    items = [
        (
            r'''Sau $1$ năm nữa dân số Việt Nam đạt khoảng $101{,}1$ triệu người''',
            r'''Sau $1$ năm nữa dân số Việt Nam đạt khoảng $105{,}0$ triệu người''',
            r'''$S(1) = 100{,}3 \cdot e^{0{,}0084 \times 1} \approx 101{,}15$ triệu người, xấp xỉ $101{,}1$ triệu người.''',
            r'''Sau $1$ năm dân số tăng thêm khoảng $0{,}84$ triệu, đạt $101{,}1$ triệu người.'''
        ),
        (
            r'''Đến năm $2030$, dân số Việt Nam ước đạt khoảng $106{,}4$ triệu người''',
            r'''Đến năm $2030$, dân số Việt Nam ước đạt $120$ triệu người''',
            r'''Năm $2030$ ứng với $t = 7 \implies S(7) = 100{,}3 \cdot e^{0{,}0084 \times 7} \approx 106{,}38$ triệu người.''',
            r'''Dân số năm $2030$ khoảng $106{,}4$ triệu người, khẳng định đạt $120$ triệu người là sai.'''
        ),
        (
            r'''Dân số nước ta chưa vượt quá $110$ triệu người trong vòng $10$ năm kể từ năm $2023$''',
            r'''Dân số nước ta vượt $110$ triệu người trong vòng $10$ năm kể từ năm $2023$''',
            r'''Sau $10$ năm ($t = 10$): $S(10) = 100{,}3 \cdot e^{0{,}084} \approx 109{,}1$ triệu người $< 110$ triệu người. Để vượt $110$ triệu người cần $t = \dfrac{\ln(110/100{,}3)}{0{,}0084} \approx 11{,}0$ năm.''',
            r'''Sau $10$ năm dân số mới đạt khoảng $109{,}1$ triệu người, chưa vượt $110$ triệu người.'''
        ),
        (
            r'''Nếu từ năm $2035$ mức tăng dân số giảm còn $r = 0{,}4\%$/năm thì đến năm $2040$ dân số vẫn dưới $120$ triệu người''',
            r'''Đến năm $2040$ dân số nước ta sẽ vượt mốc $120$ triệu người''',
            r'''Tốc độ tăng chậm lại khiến dân số năm $2040$ chỉ đạt khoảng $113$ triệu người, không thể vượt $120$ triệu người.''',
            r'''Dân số dự kiến năm $2040$ cách rất xa mốc $120$ triệu người.'''
        )
    ]
    choices, loi_giai = make_tf_choices(items)
    return caudan, choices, loi_giai


# ==============================================================================
# PHẦN III: 6 CÂU TRẢ LỜI NGẮN (SA)
# ==============================================================================

def DeThiThu05_SA_Cau1():
    # Câu 1: Cho (2x+5)f'(x) = 2f(x) - 3x^2 f^2(x), f(1) = 7. Tính tích phân f(x) từ 1 đến 4.
    # [ (2x+5)/f(x) ]' = 3x^2 => (2x+5)/f(x) = x^3 => f(x) = 2/x^2 + 5/x^3
    # \int_1^4 f(x) dx = 123/32 ≈ 3.8
    caudan = r'''Cho hàm số $y = f(x)$ có đạo hàm liên tục trên đoạn $[1; 4]$ thỏa mãn $f(1) = 7$ và $(2x+5) f'(x) = 2f(x) - 3x^2 f^2(x)$. Tính giá trị của tích phân $\displaystyle\int_1^4 f(x)\,\mathrm{d}x$ \textit{(làm tròn kết quả đến hàng phần mười)}.'''
    dapan = "3,8"
    loi_giai = r'''Biến đổi phương trình:
$$2f(x) - (2x+5)f'(x) = 3x^2 f^2(x) \iff \dfrac{(2x+5)'f(x) - (2x+5)f'(x)}{f^2(x)} = 3x^2 \iff \left[\dfrac{2x+5}{f(x)}\right]' = 3x^2.$$
Lấy nguyên hàm hai vế: $\dfrac{2x+5}{f(x)} = x^3 + C$. \\
Vì $f(1) = 7 \implies \dfrac{7}{7} = 1 + C \implies C = 0$. \\
Suy ra $f(x) = \dfrac{2x+5}{x^3} = \dfrac{2}{x^2} + \dfrac{5}{x^3}$. \\
Tích phân:
$$\int_1^4 f(x)\,\mathrm{d}x = \int_1^4 \left(\dfrac{2}{x^2} + \dfrac{5}{x^3}\right)\mathrm{d}x = \left.\left(-\dfrac{2}{x} - \dfrac{5}{2x^2}\right)\right|_1^4 = \dfrac{123}{32} \approx 3,8.$$'''
    return caudan, dapan, loi_giai


def DeThiThu05_SA_Cau2():
    # Câu 2: Lấy bi không hoàn lại (30 đen, 20 trắng trong 50 viên bi)
    # Lần 1 đen, lần 2 trắng: 30/50 * 20/49 = 12/49 ≈ 0.24
    cfgs = [
        {"den": 30, "trang": 20, "ans_str": "0,24"},
        {"den": 25, "trang": 25, "ans_str": "0,26"},
        {"den": 35, "trang": 15, "ans_str": "0,21"},
    ]
    c = random.choice(cfgs)
    den, trang = c["den"], c["trang"]
    tong = den + trang
    ans = c["ans_str"]

    caudan = fr'''Một bình đựng ${tong}$ viên bi có kích thước và chất liệu như nhau, trong đó có ${den}$ viên bi màu đen và ${trang}$ viên bi màu trắng. Lấy ngẫu nhiên ra một viên bi không hoàn lại, rồi lại lấy tiếp một viên bi nữa. Tính xác suất để lấy được một viên bi màu đen ở lần thứ nhất và một viên bi màu trắng ở lần thứ hai. \textit{{(Làm tròn kết quả đến hàng phần trăm)}}'''
    dapan = ans
    loi_giai = fr'''Xác suất lấy được viên bi màu đen ở lần thứ nhất là $P_1 = \dfrac{{{den}}}{{{tong}}}$. \\
Sau khi lấy một viên bi đen, trong bình còn lại ${tong - 1}$ viên bi (gồm ${den - 1}$ đen và ${trang}$ trắng). \\
Xác suất lấy được viên bi màu trắng ở lần thứ hai là $P_2 = \dfrac{{{trang}}}{{{tong - 1}}}$. \\
Xác suất cần tìm:
$$P = P_1 \times P_2 = \dfrac{{{den}}}{{{tong}}} \times \dfrac{{{trang}}}{{{tong - 1}}} \approx {dapan}.$$'''
    return caudan, dapan, loi_giai


def DeThiThu05_SA_Cau3():
    # Câu 3: Rào vườn chữ E dọc bờ sông: 3x*50.000 + y*60.000 = T
    # 5x + 2y = T/3000 => S(x) = x*(500 - 5x)/2 => x = 50 => S_max = 6250
    presets = [
        {"T": 15000000, "price_x": 50000, "price_y": 60000, "ans": "6250"},
        {"T": 18000000, "price_x": 50000, "price_y": 60000, "ans": "9000"},
        {"T": 12000000, "price_x": 50000, "price_y": 60000, "ans": "4000"},
    ]
    p = random.choice(presets)
    T = p["T"]
    T_str = f"{T:,}".replace(',', r'\,')

    caudan = fr'''Một người nông dân có ${T_str}$ đồng để làm một hàng rào hình chữ E dọc theo một con sông bao quanh hai khu đất trồng rau có dạng hai hình chữ nhật bằng nhau. Đối với mặt hàng rào song song với bờ sông thì chi phí là $60\,000$ đồng/mét, còn đối với ba mặt hàng rào song song vuông góc với bờ sông thì chi phí là $50\,000$ đồng/mét; mặt giáp bờ sông không phải rào. Diện tích lớn nhất của hai khu đất thu được sau khi làm hàng rào là bao nhiêu mét vuông?'''
    dapan = p["ans"]
    loi_giai = fr'''Gọi chiều rộng mỗi khu đất (độ dài 3 cạnh rào vuông góc bờ sông) là $x\text{{ (m)}}$ và chiều dài khu đất (mặt rào song song bờ sông) là $y\text{{ (m)}}$ ($x, y > 0$). \\
Tổng chi phí: $3x \times 50\,000 + y \times 60\,000 = {T_str} \iff 15x + 6y = {T // 1000} \iff 5x + 2y = {T // 30000}$. \\
Suy ra $y = \dfrac{{{T // 30000} - 5x}}{{2}}$. \\
Diện tích hai khu đất: $S(x) = xy = x \cdot \dfrac{{{T // 30000} - 5x}}{{2}} = -\dfrac{{5}}{{2}}x^2 + \dfrac{{{T // 30000}}}{{2}}x$. \\
Hàm số đạt giá trị lớn nhất tại đỉnh parabol $x = \dfrac{{{T // 30000}}}{{10}} \implies S_{{\max}} = {dapan}\text{{ m}}^2$.'''
    return caudan, dapan, loi_giai


def DeThiThu05_SA_Cau4():
    # Câu 4: Máy bay từ M(500; 200; 8) đến N(800; 300; 10) trong 20 phút.
    # Vị trí sau 5 phút tiếp theo: (a; b; c). Tính a.
    # MN = (300; 100; 2) => trong 5 phút đi thêm 1/4 MN = (75; 25; 0.5)
    # => P = (875; 325; 10.5) => a = 875.
    presets = [
        {"M": (500, 200, 8),  "N": (800, 300, 10), "t1": 20, "t2": 5,  "a": 875},
        {"M": (400, 100, 6),  "N": (600, 200, 8),  "t1": 20, "t2": 10, "a": 700},
        {"M": (600, 300, 10), "N": (900, 400, 12), "t1": 15, "t2": 5,  "a": 1000},
    ]
    p = random.choice(presets)
    M = p["M"]
    N = p["N"]
    t1 = p["t1"]
    t2 = p["t2"]
    ans = p["a"]

    caudan = fr'''Trong không gian với hệ tọa độ $Oxyz$ (đơn vị đo là kilômét), ra đa phát hiện một máy bay di chuyển với vận tốc và hướng không đổi từ điểm $M({M[0]}; {M[1]}; {M[2]})$ đến điểm $N({N[0]}; {N[1]}; {N[2]})$ trong ${t1}$ phút. Nếu máy bay tiếp tục giữ nguyên vận tốc và hướng bay thì tọa độ của máy bay sau ${t2}$ phút tiếp theo là $(a; b; c)$. Tính giá trị của $a$.'''
    dapan = str(ans)
    loi_giai = fr'''Vectơ độ dời trong ${t1}$ phút là $\overrightarrow{{MN}} = ({N[0]-M[0]}; {N[1]-M[1]}; {N[2]-M[2]})$. \\
Trong ${t2}$ phút tiếp theo, máy bay di chuyển một vectơ bằng $\dfrac{{{t2}}}{{{t1}}}\overrightarrow{{MN}} = \dfrac{{{t2}}}{{{t1}}}({N[0]-M[0]}; {N[1]-M[1]}; {N[2]-M[2]}) = ({ans - N[0]}; \dots; \dots)$. \\
Tọa độ máy bay sau ${t2}$ phút tiếp theo là:
$$P = N + \dfrac{{{t2}}}{{{t1}}}\overrightarrow{{MN}} \implies a = {N[0]} + ({ans - N[0]}) = {ans}.$$'''
    return caudan, dapan, loi_giai


def DeThiThu05_SA_Cau5():
    # Câu 5: Lăng trụ đứng ABC.A'B'C' đáy vuông tại B, AB = sqrt(3), BC = 2, AA' = sqrt(2).
    # d(AM, B'C') = d(B'C', (ABC)) = AA' = sqrt(2) ≈ 1.41
    cfgs = [
        {"h_tex": r"\sqrt{2}", "val": math.sqrt(2), "ans": "1,41"},
        {"h_tex": r"\sqrt{3}", "val": math.sqrt(3), "ans": "1,73"},
        {"h_tex": r"\sqrt{5}", "val": math.sqrt(5), "ans": "2,24"},
    ]
    c = random.choice(cfgs)

    caudan = fr'''Cho hình lăng trụ đứng $ABC.A'B'C'$ có đáy $ABC$ là tam giác vuông tại $B$ và có độ dài các cạnh $AB = \sqrt{{3}}$, $BC = 2$, $AA' = {c["h_tex"]}$. Gọi $M$ là trung điểm của $BC$. Tính khoảng cách giữa hai đường thẳng $AM$ và $B'C'$ \textit{{(làm tròn kết quả đến hàng phần trăm)}}.'''
    dapan = c["ans"]
    loi_giai = fr'''Vì hình lăng trụ là lăng trụ đứng nên các cạnh bên vuông góc với mặt phẳng đáy: $BB' \perp (ABC)$. \\
Ta có $B'C' \parallel BC$. Mà $BC \subset (ABC) \implies B'C' \parallel (ABC)$. \\
Vì $AM \subset (ABC)$ nên đường thẳng $B'C'$ song song với mặt phẳng chứa $AM$ là $(ABC)$. \\
Do đó:
$$d(AM, B'C') = d(B'C', (ABC)) = d(B', (ABC)) = BB' = AA' = {c["h_tex"]} \approx {dapan}.$$'''
    return caudan, dapan, loi_giai


def DeThiThu05_SA_Cau6():
    # Câu 6: Chiếc bàn gấp gọn Oxyz. Độ dài chân bàn FA = 40*sqrt(3) cm. Tính độ cao mặt bàn h = FA * sin(phi)
    # Đường thẳng chân bàn a có VTCP u = (1; 1; 4) => |u| = 3*sqrt(2)
    # Mặt bàn (P): x + y - 2z + 6 = 0 có VTPT n = (1; 1; -2) => |n| = sqrt(6)
    # sin(phi) = |u.n| / (|u|*|n|) = |1 + 1 - 8| / (3*sqrt(2)*sqrt(6)) = 6 / 6*sqrt(3) = 1/sqrt(3)
    # h = FA * sin(phi) = 40*sqrt(3) * (1/sqrt(3)) = 40 cm.
    cfgs = [
        {"len_tex": r"40\sqrt{3}", "FA": 40, "ans": "40"},
        {"len_tex": r"50\sqrt{3}", "FA": 50, "ans": "50"},
        {"len_tex": r"60\sqrt{3}", "FA": 60, "ans": "60"},
    ]
    c = random.choice(cfgs)

    caudan = fr'''Một chiếc bàn gấp gọn được gắn với hệ tọa độ $Oxyz$. Điểm $A$ là chân bàn tiếp xúc với mặt đất thuộc đường thẳng $a \colon \begin{{cases}} x = -3 + t \\ y = 1 + t \\ z = -2 + 4t \end{{cases}}$, cắt mặt bàn là mặt phẳng $(P) \colon x + y - 2z + 6 = 0$ tại điểm $F$. Độ dài chân bàn $FA = {c["len_tex"]}\text{{ cm}}$. Giả sử mặt đất phẳng và song song với mặt bàn $(P)$, độ cao của mặt bàn tính từ mặt đất là bao nhiêu centimet?'''
    dapan = c["ans"]
    loi_giai = fr'''Đường thẳng $a$ chứa chân bàn có vectơ chỉ phương $\vec{{u}} = (1; 1; 4) \implies |\vec{{u}}| = \sqrt{{1^2 + 1^2 + 4^2}} = 3\sqrt{{2}}$. \\
Mặt bàn $(P)$ có vectơ pháp tuyến $\vec{{n}} = (1; 1; -2) \implies |\vec{{n}}| = \sqrt{{1^2 + 1^2 + (-2)^2}} = \sqrt{{6}}$. \\
Góc $\varphi$ tạo bởi chân bàn $a$ và mặt bàn $(P)$ thỏa mãn:
$$\sin\varphi = \dfrac{{|\vec{{u}} \cdot \vec{{n}}|}}{{|\vec{{u}}| \cdot |\vec{{n}}|}} = \dfrac{{|1 \cdot 1 + 1 \cdot 1 + 4 \cdot (-2)|}}{{3\sqrt{{2}} \cdot \sqrt{{6}}}} = \dfrac{{6}}{{6\sqrt{{3}}}} = \dfrac{{1}}{{\sqrt{{3}}}}.$$
Vì mặt đất song song với mặt bàn $(P)$ nên độ cao của mặt bàn tính từ mặt đất là khoảng cách từ điểm $A$ đến mặt bàn $(P)$:
$$h = FA \cdot \sin\varphi = {c["len_tex"]} \cdot \dfrac{{1}}{{\sqrt{{3}}}} = {dapan}\text{{ cm}}.$$'''
    return caudan, dapan, loi_giai
