# -*- coding: utf-8 -*-
import random
import re
from fractions import Fraction

# --- MULTIPLE CHOICE ---
from cuoi_chuong_mc_chuong2 import (
    CuoiChuong2_MC_B1_NB1,
    CuoiChuong2_MC_B1_NB2,
    CuoiChuong2_MC_B1_TH,
    CuoiChuong2_MC_B1_VD,
    CuoiChuong2_MC_B2_NB1,
    CuoiChuong2_MC_B2_NB2,
    CuoiChuong2_MC_B2_TH,
    CuoiChuong2_MC_B2_VD,
    CuoiChuong2_MC_B3_NB1,
    CuoiChuong2_MC_B3_NB2,
    CuoiChuong2_MC_B3_TH,
    CuoiChuong2_MC_B3_VD,
)
from cuoi_chuong_mc_chuong3 import *
from cuoi_chuong_mc_chuong4 import *
from cuoi_chuong_mc_chuong5 import *
from toan_thuc_te_lop10 import *



def CuoiChuong1_MC_Cau1():
    sub_type = random.choice([1, 2, 3, 4])
    
    if sub_type == 1:
        x0 = random.choice([1, 2])
        y0 = random.choice([1, 2])
        k = random.choice([2, 3, 4])
        b = k - y0 * x0
        
        caudan = fr'''\immini{{Cho hàm số có đồ thị như hình bên dưới. Mệnh đề nào sau đây là đúng}}{{
\begin{{tikzpicture}}[scale=0.7, line join=round, line cap=round, >=stealth,font=\footnotesize]
    \def\xmin{{-2.2}}\def\xmax{{4}}\def\ymin{{-2.2}}\def\ymax{{4}}
    \draw[->] (\xmin-0.2,0)--(\xmax+0.2,0) node[below]{{$x$}};
    \draw[->] (0,\ymin-0.2)--(0,\ymax+0.2) node[right]{{$y$}};
    \draw (0,0) node[below left]{{$O$}};
    \foreach \x in {{-2,-1,1,2,3}}\draw (\x,0.1)--(\x,-0.1) node[below]{{$\x$}};
    \foreach \y in {{-2,-1,1,2,3}}\draw (0.1,\y)--(-0.1,\y) node[left]{{$\y$}};
    \clip (\xmin,\ymin) rectangle (\xmax,\ymax);
    \draw[dashed] (\xmin,{y0})--(\xmax,{y0});
    \draw[dashed] ({x0},\ymin)--({x0},\ymax);
    \draw[thick,smooth,samples=200,domain=\xmin:{x0 - 0.1}] plot (\x,{{({y0}*(\x)+{b})/(\x - {x0})}});
    \draw[thick,smooth,samples=200,domain={x0 + 0.1}:\xmax] plot (\x,{{({y0}*(\x)+{b})/(\x - {x0})}});
\end{{tikzpicture}}
}}'''
    
        choices = [
            fr'''{{Đường tiệm cận đứng của hàm số là $y={x0}$}}
''',
            fr'''{{Đường tiệm cận ngang của hàm số là $y={y0}$}}
''',
            fr'''{{\True Đường tiệm cận đứng của đồ thị hàm số là $x={x0}$}}
''',
            fr'''{{Đường tiệm cận ngang của đồ thị hàm số là $y={y0 + 1}$}}
'''
        ]
        random.shuffle(choices)
        loi_giai = fr'''Dựa vào đồ thị hàm số, đường tiệm cận đứng là $x={x0}$ (đường thẳng đứng màu nét đứt).'''
        return caudan, choices, loi_giai

    elif sub_type == 2:
        x0 = random.choice([1, 2])
        y0 = random.choice([1, 2])
        k = random.choice([2, 3, 4])
        b = k - y0 * x0
        
        caudan = fr'''\immini{{Cho hàm số có đồ thị như hình bên dưới. Mệnh đề nào sau đây là đúng}}{{
\begin{{tikzpicture}}[scale=0.7, line join=round, line cap=round, >=stealth,font=\footnotesize]
    \def\xmin{{-2.2}}\def\xmax{{4}}\def\ymin{{-2.2}}\def\ymax{{4}}
    \draw[->] (\xmin-0.2,0)--(\xmax+0.2,0) node[below]{{$x$}};
    \draw[->] (0,\ymin-0.2)--(0,\ymax+0.2) node[right]{{$y$}};
    \draw (0,0) node[below left]{{$O$}};
    \foreach \x in {{-2,-1,1,2,3}}\draw (\x,0.1)--(\x,-0.1) node[below]{{$\x$}};
    \foreach \y in {{-2,-1,1,2,3}}\draw (0.1,\y)--(-0.1,\y) node[left]{{$\y$}};
    \clip (\xmin,\ymin) rectangle (\xmax,\ymax);
    \draw[dashed] (\xmin,{y0})--(\xmax,{y0});
    \draw[dashed] ({x0},\ymin)--({x0},\ymax);
    \draw[thick,smooth,samples=200,domain=\xmin:{x0 - 0.1}] plot (\x,{{({y0}*(\x)+{b})/(\x - {x0})}});
    \draw[thick,smooth,samples=200,domain={x0 + 0.1}:\xmax] plot (\x,{{({y0}*(\x)+{b})/(\x - {x0})}});
\end{{tikzpicture}}
}}'''
        choices = [
            fr'''{{Đường tiệm cận đứng của đồ thị hàm số là $x={y0}$}}
''',
            fr'''{{\True Đường tiệm cận ngang của đồ thị hàm số là $y={y0}$}}
''',
            fr'''{{Đường tiệm cận đứng của đồ thị hàm số là $y={x0}$}}
''',
            fr'''{{Đường tiệm cận ngang của đồ thị hàm số là $x={y0}$}}
'''
        ]
        random.shuffle(choices)
        loi_giai = fr'''Dựa vào đồ thị hàm số, đường tiệm cận ngang là $y={y0}$ (đường nằm ngang màu nét đứt).'''
        return caudan, choices, loi_giai

    elif sub_type == 3:
        # 2 trên 1 graph - vertical asymptote (Image 3/4, Câu 10/19)
        x0 = random.choice([-2, -1, 1, 2])
        caudan = fr'''\immini{{Cho hàm số $y=f(x)$ có đồ thị như hình vẽ bên dưới. Khi đó đường tiệm cận đứng của đồ thị hàm số là}}{{
\begin{{tikzpicture}}[scale=0.6, >=stealth]
    \draw[->] (-3.2,0) -- (3.5,0) node[below] {{$x$}};
    \draw[->] (0,-4) -- (0,4) node[left] {{$y$}};
    \draw (0,0) node[below right] {{$O$}};
    \draw[dashed] ({x0},-4) -- ({x0},4);
    \draw[dashed] (-3.2,-3.2) -- (3.2,3.2);
    \draw[thick, smooth, samples=100, domain={x0+0.25}:3.2] plot (\x, {{\x + 1/(\x - {x0})}});
    \draw[thick, smooth, samples=100, domain=-3.2:{x0-0.25}] plot (\x, {{\x + 1/(\x - {x0})}});
    \node[below] at ({x0},0) {{${x0}$}};
\end{{tikzpicture}}
}}'''
        choices = [
            fr'''{{\True $x = {x0}$}}
''',
            fr'''{{$y = {x0}$}}
''',
            fr'''{{$x = {-x0}$}}
''',
            fr'''{{$y = {-x0}$}}
'''
        ]
        random.shuffle(choices)
        loi_giai = fr'''Dựa vào đồ thị hàm số, đường tiệm cận đứng là đường thẳng đứng nét đứt cắt trục hoành tại điểm có hoành độ ${x0}$. \\
Do đó, phương trình tiệm cận đứng là $x = {x0}$.'''
        return caudan, choices, loi_giai

    else:
        # 2 trên 1 graph - oblique asymptote equation
        patterns = [
            (1, 1, 1, 1),
            (1, 2, 1, 1),
            (1, -1, 2, 1),
            (1, -2, -1, 1),
            (1, 2, -1, 1),
            (1, 1, -2, 1),
            (1, -1, -2, 1),
            (-1, 1, 1, 1),
            (-1, 2, 1, 1),
            (-1, -1, -1, 1),
            (-1, -2, 1, 1),
            (-1, 2, -1, 1),
            (-1, 1, -2, 1),
            (2, 2, -1, 1),
            (2, -2, 1, 1),
            (-2, 2, 1, 1),
            (-2, -2, -1, 1),
        ]
        a_coeff, b_coeff, x0, k = random.choice(patterns)
        xA = -b_coeff // a_coeff
        yB = b_coeff

        def fmt_lin(a, b):
            str_a = "x" if a == 1 else ("-x" if a == -1 else f"{a}x")
            if b > 0:
                return f"{str_a} + {b}"
            elif b < 0:
                return f"{str_a} - {abs(b)}"
            return str_a

        eq_str = fmt_lin(a_coeff, b_coeff)
        d1 = round(x0 - 0.22, 2)
        d2 = round(x0 + 0.22, 2)

        xmin = min(-4.0, x0 - 2.5, xA - 1.5)
        xmax = max(4.0, x0 + 2.5, xA + 1.5)
        ymin = min(-4.2, yB - 2.0, -3.0)
        ymax = max(4.5, yB + 2.0, 3.5)

        xA_label = f"\\fill ({xA},0) circle (1.5pt) node[below left]{{${xA}$}};" if xA != 0 else ""
        yB_label = f"\\fill (0,{yB}) circle (1.5pt) node[above left]{{${yB}$}};" if yB != 0 else ""
        x0_label = f"\\draw ({x0},0.1)--({x0},-0.1) node[below right]{{${x0}$}};" if x0 != xA else ""

        caudan = fr'''\immini{{Cho hàm số $y=f(x)$ có đồ thị như hình vẽ bên dưới. Khi đó tiệm cận xiên của đồ thị hàm số là đường thẳng có phương trình}}{{
\begin{{tikzpicture}}[scale=0.55, font=\footnotesize, line join=round, line cap=round, >=stealth]
    \def\xmin{{{xmin:.1f}}}\def\xmax{{{xmax:.1f}}}\def\ymin{{{ymin:.1f}}}\def\ymax{{{ymax:.1f}}}
    \draw[->] (\xmin-0.2,0)--(\xmax+0.2,0) node[below]{{$x$}};
    \draw[->] (0,\ymin-0.2)--(0,\ymax+0.2) node[left]{{$y$}};
    \draw (0,0) node[below right]{{$O$}};
    \begin{{scope}}
    \clip (\xmin,\ymin) rectangle (\xmax,\ymax);
    \draw[dashed, blue!80!black, thick] ({x0},\ymin)--({x0},\ymax);
    \draw[dashed, red!80!black, thick, domain=\xmin:\xmax] plot (\x, {{ {a_coeff}*(\x) + ({b_coeff}) }});
    \draw[thick, smooth, samples=150, domain=\xmin:{d1}] plot (\x, {{ {a_coeff}*(\x) + ({b_coeff}) + ({k})/((\x) - ({x0})) }});
    \draw[thick, smooth, samples=150, domain={d2}:\xmax] plot (\x, {{ {a_coeff}*(\x) + ({b_coeff}) + ({k})/((\x) - ({x0})) }});
    \end{{scope}}
    {xA_label}
    {yB_label}
    {x0_label}
\end{{tikzpicture}}
}}'''
        correct = fr'''y = {eq_str}'''
        w1 = fr'''y = {fmt_lin(-a_coeff, b_coeff)}'''
        w2 = fr'''y = {fmt_lin(a_coeff, -b_coeff)}'''
        w3 = fr'''x = {x0}'''

        choices = [
            fr'''{{\True ${correct}$}}
''',
            fr'''{{${w1}$}}
''',
            fr'''{{${w2}$}}
''',
            fr'''{{${w3}$}}
'''
        ]
        random.shuffle(choices)
        loi_giai = fr'''Dựa vào đồ thị hàm số:
- Tiệm cận xiên là đường thẳng cắt trục tung tại điểm $(0; {yB})$ và cắt trục hoành tại điểm $({xA}; 0)$.
- Đường thẳng này có hệ số góc $a = \dfrac{{{yB} - 0}}{{0 - ({xA})}} = {a_coeff}$ và tung độ gốc $b = {yB}$.
Vậy phương trình tiệm cận xiên là $y = {eq_str}$.'''
        return caudan, choices, loi_giai


def CuoiChuong1_MC_Cau2():
    # Randomly select between 8 different GTLN-GTNN types
    sub_type = random.choice([1, 2, 3, 4, 5, 6, 7, 8])
    
    if sub_type == 1:
        # Old algebraic y = (ax - b)/(x+c) on [2; 3]
        c = random.choice([2, 3, 4])
        a = random.choice([5, 6, 7, 8, 9])
        b = random.choice([4, 5, 6, 7, 8])
        y2 = Fraction(2*a - b, 2 + c)
        y3 = Fraction(3*a - b, 3 + c)
        total = y2 + y3
        caudan = fr'''Cho hàm số $y=\dfrac{{ {a}x - {b} }}{{x + {c} }}$. Tổng giá trị nhỏ nhất và giá trị lớn nhất của hàm số trên đoạn $[2;3]$ là'''
        def fmt_frac(fr):
            return fr'''\dfrac{{ {fr.numerator} }}{{ {fr.denominator} }}''' if fr.denominator != 1 else fr'''{fr.numerator}'''
        correct_ans = fmt_frac(total)
        wrong1 = total + Fraction(1, 2)
        wrong2 = total - Fraction(1, 2)
        wrong3 = total + Fraction(1, 3)
        choices = [
            fr'''{{\True ${correct_ans}$}}
''',
            fr'''{{${fmt_frac(wrong1)}$}}
''',
            fr'''{{${fmt_frac(wrong2)}$}}
''',
            fr'''{{${fmt_frac(wrong3)}$}}
'''
        ]
        random.shuffle(choices)
        loi_giai = fr'''Ta có: $y' = \dfrac{{ {a*c + b} }}{{\left(x+{c} \right)^2}} > 0,~~ \forall x \ne -{c}$. \\
Do đó hàm số đồng biến trên đoạn $[2;3]$. \\
Giá trị nhỏ nhất là $y(2) = \dfrac{{ {2*a - b} }}{{ {2+c} }} = {fmt_frac(y2)}$. \\
Giá trị lớn nhất là $y(3) = \dfrac{{ {3*a - b} }}{{ {3+c} }} = {fmt_frac(y3)}$. \\
Tổng giá trị nhỏ nhất và lớn nhất là: ${fmt_frac(y2)} + {fmt_frac(y3)} = {correct_ans}$.'''
        return caudan, choices, loi_giai

    elif sub_type == 2:
        # New MC 1: Graph-based max/min on closed interval [-2; 2]
        M = random.choice([2, 3, 4])
        m = random.choice([-3, -2, -1])
        k = (M - m) / 4.0
        C = (M + m) / 2.0
        
        caudan = fr'''\immini{{Cho hàm số $y = f(x)$ liên tục trên đoạn $[-2; 2]$ và có đồ thị trong hình bên. Giá trị lớn nhất của hàm số $y = f(x)$ trên đoạn $[-2; 2]$ bằng bao nhiêu?}}{{
\begin{{tikzpicture}}[scale=0.7, line join=round, line cap=round, >=stealth, font=\footnotesize]
    \def\xmin{{-2.5}}\def\xmax{{2.5}}\def\ymin{{-3.5}}\def\ymax{{4.5}}
    \draw[->] (\xmin,0)--(\xmax,0) node[below]{{$x$}};
    \draw[->] (0,\ymin)--(0,\ymax) node[right]{{$y$}};
    \draw (0,0) node[below left]{{$O$}};
    \foreach \x in {{-2,-1,1,2}}\draw (\x,0.1)--(\x,-0.1) node[below]{{$\x$}};
    \foreach \y in {{-3,-2,-1,1,2,3,4}}\draw (0.1,\y)--(-0.1,\y) node[left]{{$\y$}};
    \clip (\xmin,\ymin) rectangle (\xmax,\ymax);
    \draw[dashed] (-1,0)--(-1,{M})--(0,{M});
    \draw[dashed] (1,0)--(1,{m})--(0,{m});
    \draw[thick,smooth,samples=100,domain=-2:2] plot (\x,{{{k}*(\x*\x*\x - 3*\x) + {C}}});
\end{{tikzpicture}}
}}'''
        choices = [
            fr'''{{\True ${M}$}}
''',
            fr'''{{${M+1}$}}
''',
            fr'''{{${m}$}}
''',
            fr'''{{${M-1}$}}
'''
        ]
        random.shuffle(choices)
        loi_giai = fr'''Dựa vào đồ thị hàm số trên đoạn $[-2;2]$, điểm cao nhất của đồ thị là $(-1; {M})$. Do đó giá trị lớn nhất của hàm số trên đoạn này bằng ${M}$.'''
        return caudan, choices, loi_giai

    elif sub_type == 3:
        # New MC 4: Algebraic f(x) = (x^2 + c)/(x - 1) on [2; 4] or [2; 5]
        c = random.choice([3, 8])
        if c == 3:
            # f(x) = (x^2+3)/(x-1) on [2; 4]. Min is at x=3, value is 6.
            caudan = fr'''Giá trị nhỏ nhất của hàm số $f(x) = \dfrac{{x^2 + 3}}{{x - 1}}$ trên đoạn $[2; 4]$ là'''
            correct = 6
            wrong1, wrong2, wrong3 = 7, "19/3", "13/3"
        else:
            # f(x) = (x^2+8)/(x-1) on [2; 5]. Min is at x=4, value is 8.
            caudan = fr'''Giá trị nhỏ nhất của hàm số $f(x) = \dfrac{{x^2 + 8}}{{x - 1}}$ trên đoạn $[2; 5]$ là'''
            correct = 8
            wrong1, wrong2, wrong3 = 12, "33/4", "10"
            
        choices = [
            fr'''{{\True ${correct}$}}
''',
            fr'''{{${wrong1}$}}
''',
            fr'''{{${wrong2}$}}
''',
            fr'''{{${wrong3}$}}
'''
        ]
        random.shuffle(choices)
        if c == 3:
            loi_giai = fr'''Ta có $f'(x) = \dfrac{{x^2 - 2x - 3}}{{(x-1)^2}} = 0 \iff x = 3 \in [2;4]$ (loại $x = -1$). \\
Tính các giá trị: $f(2)=7$, $f(3)=6$, $f(4)=\dfrac{{19}}{{3}}$. \\
Vậy giá trị nhỏ nhất là $6$.'''
        else:
            loi_giai = fr'''Ta có $f'(x) = \dfrac{{x^2 - 2x - 8}}{{(x-1)^2}} = 0 \iff x = 4 \in [2;5]$ (loại $x = -2$). \\
Tính các giá trị: $f(2)=12$, $f(4)=8$, $f(5)=\dfrac{{33}}{{4}}$. \\
Vậy giá trị nhỏ nhất là $8$.'''
        return caudan, choices, loi_giai

    elif sub_type == 4:
        # New MC 8: Racing car velocity graph min
        min_v = random.choice([60, 70, 80])
        max_v = min_v + 90
        start_v = min_v + 60
        
        caudan = fr'''\immini{{Đồ thị bên dưới mô tả tốc độ của một chiếc xe đua trên đoạn đường đua bằng phẳng dài $3\text{{ km}}$:}}{{
\begin{{tikzpicture}}[line join=round, line cap=round, >=stealth, scale=0.8, font=\footnotesize]
  \draw[->] (0,0) -- (5.5,0) node[below] {{$x\text{{ (km)}}$}};
  \draw[->] (0,0) -- (0,4.5) node[left] {{$y\text{{ (km/h)}}$}};
  \node[below left] at (0,0) {{$O$}};
  \node[left] at (0,3.8) {{${max_v}$}};
  \node[left] at (0,2.8) {{${start_v}$}};
  \node[left] at (0,1.5) {{${min_v}$}};
  \node[below] at (4.5,0) {{$3$}};
  \draw[dashed] (0,3.8) -- (4.2,3.8);
  \draw[dashed] (0,1.5) -- (2.5,1.5);
  \draw[dashed] (4.5,0) -- (4.5,0.2);
  \draw[thick] (0,2.8) .. controls (0.5,3.2) and (0.8,2.8) .. (1.2,2.8)
               .. controls (1.6,2.8) and (2.0,1.5) .. (2.5,1.5)
               .. controls (3.0,1.5) and (3.8,4.2) .. (4.2,3.3)
               .. controls (4.4,2.8) and (4.8,2.9) .. (5.0,2.9);
\end{{tikzpicture}}
}}'''
        choices = [
            fr'''{{$3\text{{ (km/h)}}$}}
''',
            fr'''{{${max_v}\text{{ (km/h)}}$}}
''',
            fr'''{{${start_v}\text{{ (km/h)}}$}}
''',
            fr'''{{\True ${min_v}\text{{ (km/h)}}$}}
'''
        ]
        random.shuffle(choices)
        loi_giai = fr'''Dựa vào đồ thị tốc độ của xe đua trên đoạn đường này, điểm thấp nhất của đường cong tương ứng với giá trị tốc độ cực tiểu trên trục tung là ${min_v}\text{{ km/h}}$.'''
        return caudan, choices, loi_giai

    elif sub_type == 5:
        # New MC 10: Cho hàm số y=x^3+3x^2-9x+d. GTLN M và GTNN m trên đoạn [0; 4] là
        d = random.choice([1, 2, 3])
        caudan = fr'''Cho hàm số $y=x^3+3x^2-9x+{d}$. Giá trị lớn nhất $M$ và giá trị nhỏ nhất $m$ của hàm số trên đoạn $[0;4]$ là'''
        correct = fr'''M={76 + d}, m={d - 5}'''
        w1 = fr'''M={27 + d}, m={d - 5}'''
        w2 = fr'''M={76 + d}, m={d}'''
        w3 = fr'''M={27 + d}, m={d}'''
        choices = [
            fr'''{{\True ${correct}$}}
''',
            fr'''{{${w1}$}}
''',
            fr'''{{${w2}$}}
''',
            fr'''{{${w3}$}}
'''
        ]
        random.shuffle(choices)
        loi_giai = fr'''Ta có: $y' = 3x^2+6x-9 = 3(x-1)(x+3)$. \\
$y'=0 \iff \left[\begin{{array}}{{l}} x=1 \in [0;4] \\ x=-3 \notin [0;4] \end{{array}}\right.$. \\
Tính các giá trị đầu mút và cực trị: \\
$y(0)={d}$, $y(1)={d-5}$, $y(4)={76+d}$. \\
Do đó, giá trị lớn nhất $M = {76+d}$ và giá trị nhỏ nhất $m = {d-5}$.'''
        return caudan, choices, loi_giai

    elif sub_type == 6:
        # New MC 12: Giá trị lớn nhất của hàm số f(x)=(x-a)/(x+b) trên đoạn [0; c]
        a = random.choice([2, 3])
        b = random.choice([1, 2])
        c = random.choice([3, 4])
        
        caudan = fr'''Giá trị lớn nhất của hàm số $f(x)=\dfrac{{x-{a}}}{{x+{b}}}$ trên đoạn $[0;{c}]$ bằng bao nhiêu?'''
        
        # Max of increasing function is at the right end x = c: (c - a) / (c + b)
        val = Fraction(c - a, c + b)
        def fmt_fr(fr):
            return fr'''\dfrac{{ {fr.numerator} }}{{ {fr.denominator} }}''' if fr.denominator != 1 else fr'''{fr.numerator}'''
            
        correct = fmt_fr(val)
        w1 = fmt_fr(-Fraction(a, b)) # at x = 0
        w2 = fmt_fr(val + 1)
        w3 = fmt_fr(val - 1)
        
        choices = [
            fr'''{{\True ${correct}$}}
''',
            fr'''{{${w1}$}}
''',
            fr'''{{${w2}$}}
''',
            fr'''{{${w3}$}}
'''
        ]
        random.shuffle(choices)
        loi_giai = fr'''Ta có $f'(x) = \dfrac{{ {b+a} }}{{(x+{b})^2}} > 0, \forall x \in [0;{c}]$. \\
Hàm số liên tục và đồng biến trên đoạn $[0;{c}]$, do đó giá trị lớn nhất đạt được tại $x={c}$: \\
$\max_{{[0;{c}]}} f(x) = f({c}) = \dfrac{{ {c} - {a} }}{{ {c} + {b} }} = {correct}$.'''
        return caudan, choices, loi_giai

    elif sub_type == 7:
        # New MC 1: BBT max/min product on closed interval [-1; 3]
        case = random.choice(["A", "B", "C"])
        if case == "A":
            ym1, y0, y2, y3 = 1, 5, 2, 4
            ans = 5
        elif case == "B":
            ym1, y0, y2, y3 = 2, 6, 3, 5
            ans = 12
        else:
            ym1, y0, y2, y3 = 1, 4, 2, 3
            ans = 4
            
        caudan = fr'''\immini{{Cho hàm số $y=f(x)$ liên tục trên đoạn $[-1;3]$ có bảng biến thiên như sau. Gọi $M,m$ theo thứ tự là giá trị lớn nhất và giá trị nhỏ nhất của hàm số $y=f(x)$ trên đoạn $[-1;3]$. Giá trị $M\cdot m$ bằng}}{{
\begin{{tikzpicture}}
	\tkzTabInit[nocadre,lgt=1.2,espcl=1.5,deltacl=0.6]
	{{$x$ /0.6, $y'$ /0.6, $y$ /1.5}}
	{{$-1$,$0$,$2$,$3$}}
	\tkzTabLine{{,+,$0$,-,$0$,+,}}
	\tkzTabVar{{-/{ym1},+/{y0},-/{y2},+/{y3}}}
\end{{tikzpicture}}
}}'''
        correct = fr'''M\cdot m={ans}'''
        w1 = fr'''M\cdot m={ans + 1}'''
        w2 = fr'''M\cdot m={ans - 1}'''
        w3 = fr'''M\cdot m=0'''
        
        choices = [
            fr'''{{\True ${correct}$}}
''',
            fr'''{{${w1}$}}
''',
            fr'''{{${w2}$}}
''',
            fr'''{{${w3}$}}
'''
        ]
        random.shuffle(choices)
        loi_giai = fr'''Dựa vào bảng biến thiên trên đoạn $[-1;3]$: \\
- Giá trị lớn nhất của hàm số là $M = {y0}$ (đạt được tại $x=0$). \\
- Giá trị nhỏ nhất của hàm số là $m = {ym1}$ (đạt được tại $x=-1$, vì ${ym1} < {y2}$). \\
Do đó: $M\cdot m = {y0}\cdot {ym1} = {ans}$.'''
        return caudan, choices, loi_giai

    else:
        # New MC 3: Motion speed max time
        a = random.choice([6, 8, 10])
        b = 2
        ans = a // b
        
        # s(t) = a*t^2 - (2*t^3)/3
        caudan = fr'''Một chất điểm chuyển động theo quy luật $s(t)={a}t^2-\dfrac{{2t^3}}{{3}}$ (m). Thời điểm $t$ (giây) mà tại đó tốc độ $v$ (m/s) của chuyển động đạt giá trị lớn nhất là'''
        choices = [
            fr'''{{\True $t={ans}$}}
''',
            fr'''{{$t={ans - 1}$}}
''',
            fr'''{{$t={ans + 1}$}}
''',
            fr'''{{$t={ans + 2}$}}
'''
        ]
        random.shuffle(choices)
        loi_giai = fr'''Tốc độ của chất điểm là: $v(t) = s'(t) = {2*a}t - 2t^2$. \\
Xét hàm số $v(t)$ trên khoảng $(0; +\infty)$: \\
$v'(t) = {2*a} - 4t = 0 \iff t = {ans}$. \\
Vì hệ số của $t^2$ trong $v(t)$ âm nên đồ thị của $v(t)$ là một parabol có đỉnh tại $t={ans}$, đây là điểm mà tốc độ đạt giá trị lớn nhất. \\
Vậy thời điểm cần tìm là $t={ans}$ (giây).'''
        return caudan, choices, loi_giai


def CuoiChuong1_MC_Cau3():
    x0 = random.choice([1, 2, 3])
    y0 = random.choice([1, 2, 3])
    k = -y0 * x0 + 5
    k_wrong = -y0 * x0 - 2
    
    caudan = fr'''\immini{{Bảng biến thiên trong hình dưới là của một trong bốn hàm số trong các phương án.}}{{
\begin{{tikzpicture}}
    \tkzTabInit[nocadre,lgt=1.2,espcl=2.5,deltacl=0.6]
    {{$x$/0.6, $y'$/0.6, $y$/1.1}}
    {{$-\infty$, {x0}, $+\infty$}}
    \tkzTabLine{{,-,d,-,}}
    \tkzTabVar{{+/ {y0}, -D+/ $-\infty$/$+\infty$, -/ {y0}}}
\end{{tikzpicture}}
}}'''
    
    def fmt(a, b, x0):
        sign = "+" if b >= 0 else "-"
        abs_b = abs(b)
        a_str = f"{a}x" if a != 1 else "x"
        if a == 0:
            return fr"\dfrac{{ {b} }}{{ x - {x0} }}"
        return fr"\dfrac{{ {a_str} {sign} {abs_b} }}{{ x - {x0} }}"

    correct_str = fmt(y0, k, x0)
    wrong1_str = fmt(y0 + 1, k, x0)
    wrong2_str = fmt(y0, k, x0 + 1)
    wrong3_str = fmt(y0, k_wrong, x0)
    
    choices = [
        fr'''{{\True $y={correct_str}$}}
''',
        fr'''{{$y={wrong1_str}$}}
''',
        fr'''{{$y={wrong2_str}$}}
''',
        fr'''{{$y={wrong3_str}$}}
'''
    ]
    random.shuffle(choices)
    loi_giai = fr'''Dựa vào bảng biến thiên ta thấy:
- Tiệm cận đứng: $x = {x0}$.
- Tiệm cận ngang: $y = {y0}$.
- Hàm số nghịch biến trên từng khoảng xác định.
Do đó hàm số thỏa mãn là $y={correct_str}$.'''
    return caudan, choices, loi_giai

def CuoiChuong1_MC_Cau4():
    sub_type = random.choice([1, 2])
    
    if sub_type == 1:
        y1 = random.choice([-2, -1, 1])
        y2 = random.choice([2, 3, 4])
        
        caudan = fr'''\immini{{Cho hàm số $y=f(x)$ có bảng biến thiên sau. Đồ thị hàm số $y=f(x)$ có mấy đường tiệm cận ngang?}}{{
\begin{{tikzpicture}}
    \tkzTabInit[nocadre,espcl=2.2,lgt=1.2]
    {{$x$/0.6, $y'$/0.6, $y$/1.2}}
    {{$-\infty$, 0, 3, $+\infty$}}
    \tkzTabLine{{,-,0,+,0,+,}}
    \tkzTabVar{{+/ ${y1}$, -D+/ $-\infty$ / $2$, -/ $-3$, +/ ${y2}$}}
\end{{tikzpicture}}
}}'''
        choices = [
            fr'''{{$0$}}
''',
            fr'''{{$1$}}
''',
            fr'''{{\True $2$}}
''',
            fr'''{{$3$}}
'''
        ]
        random.shuffle(choices)
        loi_giai = fr'''Ta có $\lim_{{x\to-\infty}} f(x) = {y1}$ nên $y={y1}$ là tiệm cận ngang. \\
Ta có $\lim_{{x\to+\infty}} f(x) = {y2}$ nên $y={y2}$ là tiệm cận ngang. \\
Vậy đồ thị hàm số có 2 đường tiệm cận ngang.'''
        return caudan, choices, loi_giai
        
    else:
        # New MC 5: Total asymptotes count from BBT
        yl = random.choice([2, 3])
        yr = random.choice([5, 6])
        yp = random.choice([4, 7])
        yd = random.choice([-2, -1])
        
        caudan = fr'''\immini{{Cho hàm số $y=f(x)$ có bảng biến thiên như sau. Đồ thị hàm số $y=f(x)$ có tổng số bao nhiêu tiệm cận (gồm các tiệm cận đứng và tiệm cận ngang)?}}{{
\begin{{tikzpicture}} 
    \tkzTabInit[nocadre,lgt=1.2,espcl=2,deltacl=0.6]
    {{$x$ /0.6,$y'$ /0.6,$y$ /1.5}}
    {{$-\infty$,$0$,$1$,$+\infty$}}
    \tkzTabLine{{,+,d,-,0,+,}}
    \tkzTabVar{{-/${yl}$,+D+/${yp}$/$+\infty$,-/${yd}$,+/${yr}$}}
\end{{tikzpicture}}
}}'''
        choices = [
            fr'''{{\True $3$}}
''',
            fr'''{{$2$}}
''',
            fr'''{{$1$}}
''',
            fr'''{{$0$}}
'''
        ]
        random.shuffle(choices)
        loi_giai = fr'''Ta có: \\
- Khi $x \to -\infty$, $y \to {yl}$ nên $y={yl}$ là tiệm cận ngang. \\
- Khi $x \to +\infty$, $y \to {yr}$ nên $y={yr}$ là tiệm cận ngang. \\
- Khi $x \to 0^+$, $y \to +\infty$ nên $x=0$ là tiệm cận đứng. \\
Vậy đồ thị hàm số có tổng cộng $3$ đường tiệm cận (gồm $2$ tiệm cận ngang và $1$ tiệm cận đứng).'''
        return caudan, choices, loi_giai


def CuoiChuong1_MC_Cau5():
    sub_type = random.choice([1, 2, 3])
    
    if sub_type == 1:
        # Old rational function from graph (x^2 - ax + b)/(-x + 1)
        a = random.choice([3, 4, 5])
        b = random.choice([-1, -2, -3])
        caudan = fr'''\immini{{Đường cong trong hình là đồ thị của hàm số nào dưới đây?}}{{
\begin{{tikzpicture}}[scale=0.6, line join=round, line cap=round, >=stealth,font=\footnotesize]
    \def\xmin{{-3}}\def\xmax{{4}}\def\ymin{{-3}}\def\ymax{{4}}
    \draw[->] (\xmin-0.2,0)--(\xmax+0.2,0) node[below]{{$x$}};
    \draw[->] (0,\ymin-0.2)--(0,\ymax+0.2) node[right]{{$y$}};
    \draw (0,0) node[above left]{{$O$}};
    \foreach \x in {{-2,-1,1,2,3}}\draw (\x,0.1)--(\x,-0.1) node[below]{{$\x$}};
    \foreach \y in {{-2,-1,1,2,3}}\draw (0.1,\y)--(-0.1,\y) node[left]{{$\y$}};
    \clip (\xmin,\ymin) rectangle (\xmax,\ymax);
    \draw[dashed] (1.0,\ymin)--(1.0,\ymax);
    \draw[thick,smooth,samples=200,domain=\xmin:0.9] plot (\x,{{(\x*\x - {a}*\x + {b})/(-1*\x + 1)}});
    \draw[thick,smooth,samples=200,domain=1.1:\xmax] plot (\x,{{(\x*\x - {a}*\x + {b})/(-1*\x + 1)}});
\end{{tikzpicture}}
}}'''
        correct = fr'''y=\dfrac{{x^2-{a}x{b}}}{{-x+1}}'''
        wrong1 = fr'''y=\dfrac{{x^2-x+1}}{{x-1}}'''
        wrong2 = fr'''y=\dfrac{{x^2-3x-1}}{{-x+1}}''' if a != 3 else fr'''y=\dfrac{{x^2-6x-2}}{{-x+1}}'''
        wrong3 = fr'''y=\dfrac{{x^2+x-1}}{{x-1}}'''
        choices = [
            fr'''{{\True ${correct}$}}
''',
            fr'''{{${wrong1}$}}
''',
            fr'''{{${wrong2}$}}
''',
            fr'''{{${wrong3}$}}
'''
        ]
        random.shuffle(choices)
        loi_giai = fr'''Đồ thị có tiệm cận đứng là $x=1$ và đi qua các điểm đặc biệt, phương trình phù hợp là ${correct}$.'''
        return caudan, choices, loi_giai

    elif sub_type == 2:
        # New MC 7: Simple rational function y = (-cx + b)/(x + d) from graph
        c = random.choice([1, 2])
        d = random.choice([1, 2])
        # y = (-cx + c)/(x + d) -> passes through (1, 0) and (0, c/d)
        caudan = fr'''\immini{{Đường cong dưới đây là đồ thị của hàm số nào?}}{{
\begin{{tikzpicture}}[line join=round, line cap=round, >=stealth, scale=0.8, font=\footnotesize]
  \draw[->] (-4,0) -- (2.5,0) node[below] {{$x$}};
  \draw[->] (0,-3.5) -- (0,2.5) node[right] {{$y$}};
  \node[below left] at (0,0) {{$O$}};
  \draw[dashed] (-{d},-3.5) -- (-{d},2.5);
  \draw[dashed] (-4,-{c}) -- (2.5,-{c});
  \node[below] at (-{d},0) {{$-{d}$}};
  \node[below] at (1,0) {{$1$}};
  \node[left] at (0,-{c}) {{$-{c}$}};
  \begin{{scope}}
    \clip (-4,-3.5) rectangle (2.5,2.5);
    \draw[thick, smooth, samples=100, domain=-4:-{d+0.1}] plot (\x, {{(-{c}*\x + {c})/(\x + {d})}});
    \draw[thick, smooth, samples=100, domain=-{d-0.1}:2.5] plot (\x, {{(-{c}*\x + {c})/(\x + {d})}});
  \end{{scope}}
\end{{tikzpicture}}
}}'''
        correct = fr'''y = \dfrac{{-{c}x + {c}}}{{x + {d}}}'''
        wrong1 = fr'''y = \dfrac{{-x}}{{x + {d}}}'''
        wrong2 = fr'''y = \dfrac{{-2x + 1}}{{2x + {d}}}'''
        wrong3 = fr'''y = \dfrac{{-x + 2}}{{x + {d}}}'''
        choices = [
            fr'''{{\True ${correct}$}}
''',
            fr'''{{${wrong1}$}}
''',
            fr'''{{${wrong2}$}}
''',
            fr'''{{${wrong3}$}}
'''
        ]
        random.shuffle(choices)
        loi_giai = fr'''Từ đồ thị ta thấy đường tiệm cận đứng là $x=-{d}$, tiệm cận ngang là $y=-{c}$ và đi qua điểm $(1;0)$, do đó hàm số phù hợp là ${correct}$.'''
        return caudan, choices, loi_giai

    else:
        # New MC 1 (Variation 3): Graph of y = (ax + 1)/(x + d)
        a = random.choice([2, 3])
        d = random.choice([1, 2])
        # y = (ax + 1)/(x + d) -> passes through (0, 1/d) and (-1/a, 0)
        # asymptotes x = -d, y = a
        caudan = fr'''\immini{{Đồ thị hình dưới là của hàm số nào?}}{{
\begin{{tikzpicture}}[scale=0.6, line join=round, line cap=round, >=stealth,font=\footnotesize] 
    \def\xmin{{-4}}\def\xmax{{2}}\def\ymin{{-1}}\def\ymax{{4}}
    \draw[->] (\xmin-0.2,0)--(\xmax+0.2,0) node[below]{{$x$}};
    \draw[->] (0,\ymin-0.2)--(0,\ymax+0.2) node[right]{{$y$}};
    \draw (0,0) node[below right]{{$O$}};
    \foreach \x in {{-3,-2,-1,1}}\draw (\x,0.1)--(\x,-0.1) node[below]{{$\x$}};
    \foreach \y in {{1,2,3}}\draw (0.1,\y)--(-0.1,\y) node[left]{{$\y$}};
    \clip (\xmin,\ymin) rectangle (\xmax,\ymax);
    \draw[dashed] (\xmin,{a})--(\xmax,{a});
    \draw[dashed] (-{d},\ymin)--(-{d},\ymax);
    \begin{{scope}}
      \draw[thick,smooth,samples=200,domain=\xmin:-{d + 0.1}] plot (\x,{{({a}*(\x)+1)/((\x)+{d})}});
      \draw[thick,smooth,samples=200,domain=-{d - 0.1}:\xmax] plot (\x,{{({a}*(\x)+1)/((\x)+{d})}});
    \end{{scope}}
\end{{tikzpicture}}
}}'''
        correct = fr'''y=\dfrac{{{a}x+1}}{{x+{d}}}'''
        wrong1 = fr'''y=\dfrac{{x+3}}{{1-x}}'''
        wrong2 = fr'''y=\dfrac{{x+2}}{{x+{d}}}'''
        wrong3 = fr'''y=\dfrac{{{a}x-1}}{{x+{d}}}'''
        
        choices = [
            fr'''{{\True ${correct}$}}
''',
            fr'''{{${wrong1}$}}
''',
            fr'''{{${wrong2}$}}
''',
            fr'''{{${wrong3}$}}
'''
        ]
        random.shuffle(choices)
        loi_giai = fr'''Dựa vào đồ thị, ta có: \\
- Tiệm cận đứng: $x = -{d}$. \\
- Tiệm cận ngang: $y = {a}$. \\
- Đồ thị đi qua điểm $(0; 1/{d})$ và cắt trục hoành tại $(-1/{a}; 0)$. \\
Do đó, hàm số thỏa mãn là ${correct}$.'''
        return caudan, choices, loi_giai


def CuoiChuong1_MC_Cau6():
    sub_type = random.choice([1, 2, 3, 4, 5, 6, 7, 8])
    
    if sub_type == 1:
        a = random.choice([2, 3, 5])
        b = random.choice([1, 2, 3, 5])
        d = random.choice([1, 2, 3, 4])
        ans = -a
        
        caudan = fr'''Tiệm cận ngang của đồ thị hàm số $y=\dfrac{{{a}x+{b}}}{{-x+{d}}}$ là đường thẳng có phương trình'''
        choices = [
            fr'''{{$y={d}$}}
''',
            fr'''{{\True $y={ans}$}}
''',
            fr'''{{$x={d}$}}
''',
            fr'''{{$x={ans}$}}
'''
        ]
        random.shuffle(choices)
        loi_giai = fr'''Ta có $\lim_{{x\to\pm\infty}} \dfrac{{{a}x+{b}}}{{-x+{d}}} = {ans}$, do đó tiệm cận ngang là đường thẳng $y={ans}$.'''
        return caudan, choices, loi_giai
        
    elif sub_type == 2:
        # New MC 4: Tiệm cận đứng of y = (p + qx)/(qx - q*x0)
        q = random.choice([2, 3, 4])
        x0 = random.choice([-2, -1, 1, 2])
        p = random.choice([1, 3, 5])
        
        sign_denom = "-" if x0 > 0 else "+"
        abs_x0 = abs(x0)
        denom_str = f"{q}x {sign_denom} {q * abs_x0}"
        
        caudan = fr'''Đồ thị hàm số $y=\dfrac{{{p}+{q}x}}{{{denom_str}}}$ có đường tiệm cận đứng là'''
        choices = [
            fr'''{{\True $x={x0}$}}
''',
            fr'''{{$y={x0}$}}
''',
            fr'''{{$x={-x0}$}}
''',
            fr'''{{$y=1$}}
'''
        ]
        random.shuffle(choices)
        loi_giai = fr'''Đường tiệm cận đứng là nghiệm của mẫu số: \\
${denom_str} = 0 \iff x = {x0}$ (do tử số không triệt tiêu tại $x={x0}$). \\
Vậy đường tiệm cận đứng của đồ thị hàm số là $x={x0}$.'''
        return caudan, choices, loi_giai
        
    elif sub_type == 3:
        # New MC 11: lim x->+inf f(x) = L and lim x->-inf f(x) = -L
        L = random.choice([2024, 2025, 2026])
        caudan = fr'''Cho hàm số $y=f(x)$ có $\lim\limits_{{x \to +\infty}} f(x) = {L}$ và $\lim\limits_{{x \to -\infty}} f(x) = -{L}$. Khẳng định nào sau đây đúng?'''
        choices = [
            fr'''{{\True Đồ thị hàm số đã cho có hai tiệm cận ngang là các đường thẳng $y={L}$ và $y=-{L}$}}
''',
            fr'''{{Đồ thị hàm số đã cho có hai tiệm cận ngang là các đường thẳng $x={L}$ và $x=-{L}$}}
''',
            fr'''{{Đồ thị hàm số đã cho không có tiệm cận ngang}}
''',
            fr'''{{Đồ thị hàm số đã cho có đúng một tiệm cận ngang}}
'''
        ]
        random.shuffle(choices)
        loi_giai = fr'''Theo định nghĩa tiệm cận ngang: \\
Vì $\lim\limits_{{x \to +\infty}} f(x) = {L} \implies y={L}$ là một tiệm cận ngang. \\
Vì $\lim\limits_{{x \to -\infty}} f(x) = -{L} \implies y=-{L}$ là một tiệm cận ngang. \\
Vậy đồ thị hàm số có hai tiệm cận ngang là các đường thẳng $y={L}$ và $y=-{L}$.'''
        return caudan, choices, loi_giai

    elif sub_type == 4:
        # New MC 9: Oblique asymptote of y = (x^2 - cx)/(x + d)
        c = random.choice([2, 3])
        d = random.choice([1, 2])
        ans_const = -(c + d)
        
        caudan = fr'''Tiệm cận xiên của đồ thị hàm số $y=\dfrac{{x^2 - {c}x}}{{x + {d}}}$ là đường thẳng có phương trình'''
        
        correct = fr'''y = x {ans_const}'''
        w1 = fr'''y = x - {c}'''
        w2 = fr'''y = x + {d}'''
        w3 = fr'''y = x - 1''' if ans_const != -1 else fr'''y = x - 2'''
        
        choices = [
            fr'''{{\True ${correct}$}}
''',
            fr'''{{${w1}$}}
''',
            fr'''{{${w2}$}}
''',
            fr'''{{${w3}$}}
'''
        ]
        random.shuffle(choices)
        loi_giai = fr'''Ta viết lại hàm số dưới dạng: \\
$y = \dfrac{{x^2 - {c}x}}{{x + {d}}} = x - ({c+d}) + \dfrac{{{d*(c+d)}}}{{x + {d}}}$. \\
Vì $\lim_{{x \to \pm\infty}} \left[ y - (x - {c+d}) \right] = \lim_{{x \to \pm\infty}} \dfrac{{{d*(c+d)}}}{{x + {d}}} = 0$. \\
Do đó, đường tiệm cận xiên của đồ thị hàm số là $y = x - {c+d}$.'''
        return caudan, choices, loi_giai

    elif sub_type == 5:
        # Giao điểm hai đường tiệm cận và độ dài OI (Image 5, Cau 21)
        a = random.choice([-3, -2, -1, 1, 2, 3])
        b = random.choice([-5, -4, -3, -2, -1, 1, 2, 3, 4, 5])
        d = random.choice([-3, -2, -1, 1, 2, 3])
        while a*d - b == 0:
            b = random.choice([-5, -4, -3, -2, -1, 1, 2, 3, 4, 5])
            
        x0 = -d
        y0 = a
        dist_sq = x0**2 + y0**2
        
        import sympy as sp
        correct_val = sp.sqrt(dist_sq)
        correct_str = sp.latex(correct_val)
        if correct_str.isdigit():
            correct_ans = fr'''OI = {correct_str}'''
        else:
            correct_ans = fr'''OI = \sqrt{{{dist_sq}}}'''
            
        w1_sq = dist_sq + random.choice([1, 2, 3])
        w2_sq = max(1, dist_sq - random.choice([1, 2, 3]))
        w3_sq = dist_sq + random.choice([4, 5])
        
        def fmt_ans(sq):
            v = sp.sqrt(sq)
            s = sp.latex(v)
            if s.isdigit():
                return fr'''OI = {s}'''
            return fr'''OI = \sqrt{{{sq}}}'''
            
        choices = [
            fr'''{{\True ${correct_ans}$}}
''',
            fr'''{{${fmt_ans(w1_sq)}$}}
''',
            fr'''{{${fmt_ans(w2_sq)}$}}
''',
            fr'''{{${fmt_ans(w3_sq)}$}}
'''
        ]
        random.shuffle(choices)
        
        expr = fr'''\dfrac{{{a}x + {b}}}{{x + {d}}}'''.replace("+ -", "-").replace("1x", "x")
        caudan = fr'''Cho đồ thị hàm số $(C): y = {expr}$. Biết hai đường tiệm cận của đồ thị hàm số cắt nhau tại điểm $I$. Tính độ dài đoạn thẳng $OI$ (với $O$ là gốc tọa độ).'''
        
        loi_giai = fr'''Đồ thị hàm số có tiệm cận đứng là $x = {-d}$ và tiệm cận ngang là $y = {a}$. \\
Giao điểm của hai đường tiệm cận là $I({-d}; {a})$. \\
Độ dài đoạn thẳng $OI = \sqrt{{({-d})^2 + {a}^2}} = \sqrt{{{dist_sq}}} = {correct_str}$.'''
        return caudan, choices, loi_giai

    elif sub_type == 6:
        # Oblique asymptote of y = x + a + 1/(bx+c) (Image 1, Câu 22)
        a = random.choice([-3, -2, -1, 1, 2, 3])
        b = random.choice([2, 3])
        c = random.choice([-3, -2, -1, 1, 2, 3])
        
        sign_a = "+" if a > 0 else "-"
        opp_sign_a = "-" if a > 0 else "+"
        abs_a = abs(a)
        
        caudan = fr'''Đường tiệm cận xiên của đồ thị hàm số $y = x {sign_a} {abs_a} + \dfrac{{1}}{{{b}x {"+" if c>=0 else ""} {c}}}$ có phương trình là'''
        
        correct = fr'''y = x {sign_a} {abs_a}'''
        w1 = fr'''y = x {opp_sign_a} {abs_a}'''
        w2 = fr'''y = {b}x {"+" if c>=0 else ""} {c}'''
        w3 = fr'''y = {b}x {opp_sign_a} {abs_a}'''
        
        choices = [
            fr'''{{\True ${correct}$}}
''',
            fr'''{{${w1}$}}
''',
            fr'''{{${w2}$}}
''',
            fr'''{{${w3}$}}
'''
        ]
        random.shuffle(choices)
        loi_giai = fr'''Ta có $\lim_{{x\to\pm\infty}} \left[ y - (x {sign_a} {abs_a}) \right] = \lim_{{x\to\pm\infty}} \dfrac{{1}}{{{b}x {"+" if c>=0 else ""} {c}}} = 0$. \\
Do đó, đường tiệm cận xiên của đồ thị hàm số là $y = x {sign_a} {abs_a}$.'''
        return caudan, choices, loi_giai

    elif sub_type == 7:
        # Oblique asymptote of y = (ax^2 + bx)/(cx + d) and find a point it passes through (Image 1, Câu 26)
        d = random.choice([-3, -2, -1, 1, 2, 3])
        b = random.choice([-3, -2, -1, 1, 2, 3])
        const = b - 2*d
        xp = random.choice([-3, -2, -1, 1, 2, 3, 4, 5])
        yp = 2 * xp + const
        
        sign_d = "+" if d >= 0 else "-"
        abs_d = abs(d)
        
        expr = fr'''\dfrac{{2x^2 {"+" if b>=0 else ""} {b}x}}{{x {sign_d} {abs_d}}}'''.replace("+-", "-").replace("- -", "+")
        caudan = fr'''Đường tiệm cận xiên của đồ thị hàm số $y = {expr}$ đi qua điểm nào sau đây?'''
        
        correct_pt = fr'''({xp}; {yp})'''
        w1_pt = fr'''({xp}; {yp + random.choice([1, 2, 3])})'''
        w2_pt = fr'''({xp}; {yp - random.choice([1, 2, 3])})'''
        w3_pt = fr'''({xp + 1}; {yp})'''
        
        choices = [
            fr'''{{\True ${correct_pt}$}}
''',
            fr'''{{${w1_pt}$}}
''',
            fr'''{{${w2_pt}$}}
''',
            fr'''{{${w3_pt}$}}
'''
        ]
        random.shuffle(choices)
        loi_giai = fr'''Thực hiện phép chia tử thức cho mẫu thức: \\
$y = 2x + {const} + \dfrac{{{-d*const}}}{{x {sign_d} {abs_d}}}$. \\
Đường tiệm cận xiên của đồ thị hàm số là $y = 2x + {const}$. \\
Thay tọa độ điểm ${correct_pt}$ vào phương trình đường tiệm cận xiên ta thấy thỏa mãn: ${yp} = 2\cdot {xp} + {const}$. \\
Vậy đường tiệm cận xiên đi qua điểm ${correct_pt}$.'''
        return caudan, choices, loi_giai

    else:
        # Intersection of vertical and oblique asymptote of y = (ax^2 + bx + c)/(x - d) (Image 1, Câu 27)
        d = random.choice([-2, -1, 1, 2])
        b = random.choice([-3, -2, -1, 1, 2, 3])
        c = random.choice([-3, -2, -1, 1, 2, 3])
        
        xi = d
        yi = 2*d + b
        
        sign_d = "-" if d > 0 else "+"
        abs_d = abs(d)
        
        expr = fr'''\dfrac{{x^2 {"+" if b>=0 else ""} {b}x {"+" if c>=0 else ""} {c}}}{{x {sign_d} {abs_d}}}'''.replace("+-", "-").replace("- -", "+")
        caudan = fr'''Giao điểm của đường tiệm cận đứng và đường tiệm cận xiên của đồ thị hàm số $y = {expr}$ là'''
        
        correct_pt = fr'''({xi}; {yi})'''
        w1_pt = fr'''({xi}; {-yi})'''
        w2_pt = fr'''({-xi}; {yi})'''
        w3_pt = fr'''({xi}; {yi + 1})'''
        
        choices = [
            fr'''{{\True ${correct_pt}$}}
''',
            fr'''{{${w1_pt}$}}
''',
            fr'''{{${w2_pt}$}}
''',
            fr'''{{${w3_pt}$}}
'''
        ]
        random.shuffle(choices)
        loi_giai = fr'''Đồ thị hàm số có tiệm cận đứng là $x = {d}$. \\
Thực hiện phép chia: $y = x + {b+d} + \dfrac{{c + d*(b+d)}}{{x {sign_d} {abs_d}}}$. \\
Đường tiệm cận xiên là $y = x + {b+d}$. \\
Giao điểm $I$ của hai đường tiệm cận có tọa độ là nghiệm của hệ: \\
$\left\{{\begin{{array}}{{l}} x = {d} \\ y = x + {b+d} \end{{array}}\right. \implies I({xi}; {yi})$.'''
        return caudan, choices, loi_giai


def CuoiChuong1_MC_Cau7():
    sub_type = random.choice([1, 2])
    
    if sub_type == 1:
        # Old cubic graph
        d = random.choice([-1, 1, 2])
        ymax_val = 2 + d
        ymin_val = -2 + d
        caudan = fr'''\immini{{Đường cong trong hình bên là đồ thị hàm số nào?}}{{
\begin{{tikzpicture}}[scale=0.6, line join=round, line cap=round, >=stealth, font=\footnotesize] 
    \def\xmin{{-3}}\def\xmax{{4}}\def\ymin{{-3}}\def\ymax{{5}}
    \draw[->] (\xmin-0.2,0)--(\xmax+0.2,0) node[below]{{$x$}};
    \draw[->] (0,\ymin-0.2)--(0,\ymax+0.2) node[right]{{$y$}};
    \draw (0,0) node[below left]{{$O$}};
    \foreach \x in {{-2,-1,1,2}}\draw (\x,0.1)--(\x,-0.1) node[below]{{$\x$}};
    \foreach \y in {{-2,-1,1,2,3,4}}\draw (0.1,\y)--(-0.1,\y) node[left]{{$\y$}};
    \clip (\xmin,\ymin) rectangle (\xmax,\ymax);
    \draw[thick,smooth,samples=200,domain=\xmin:\xmax] plot (\x,{{\x*\x*\x - 3*\x + {d}}});
    \draw[dashed] (1.000, 0) -- (1.000, {ymin_val}) -- (0, {ymin_val});
    \fill (1.000, {ymin_val}) circle (1pt);
    \draw[dashed] (-1.000, 0) -- (-1.000, {ymax_val}) -- (0, {ymax_val});
    \fill (-1.000, {ymax_val}) circle (1pt);
\end{{tikzpicture}}
}}'''
        correct = fr'''y=x^3-3x{"+" if d >= 0 else ""}{d}'''
        wrong1 = fr'''y=-x^3+3x{"+" if d >= 0 else ""}{d}'''
        wrong2 = fr'''y=x^3-3x{"+" if d+1 >= 0 else ""}{d+1}'''
        wrong3 = fr'''y=-x^3+3x{"+" if d+1 >= 0 else ""}{d+1}'''
        choices = [
            fr'''{{\True ${correct}$}}
''',
            fr'''{{${wrong1}$}}
''',
            fr'''{{${wrong2}$}}
''',
            fr'''{{${wrong3}$}}
'''
        ]
        random.shuffle(choices)
        loi_giai = fr'''Đồ thị đi lên ở nhánh cuối cùng ($a > 0$). Điểm cực trị là $(-1; {ymax_val})$ và $(1; {ymin_val})$, thay tọa độ vào ta được hàm số $y=x^3-3x{"+" if d >= 0 else ""}{d}$.'''
        return caudan, choices, loi_giai

    else:
        # New MC 3: Identify cubic function from BBT
        d = random.choice([-2, -1, 1, 2])
        # y = 1/3 x^3 - x^2 - 3x + d => roots of y' are -1 and 3.
        # y(-1) = -1/3 - 1 + 3 + d = 5/3 + d
        # y(3) = 9 - 9 - 9 + d = -9 + d
        val_max = Fraction(5 + 3*d, 3)
        val_min = -9 + d
        
        def fmt_val(fr):
            return fr'''\dfrac{{ {fr.numerator} }}{{ {fr.denominator} }}''' if isinstance(fr, Fraction) and fr.denominator != 1 else fr
            
        caudan = fr'''\immini{{Trong các hàm số dưới đây, hàm số nào có bảng biến thiên như hình bên?}}{{
\begin{{tikzpicture}}[scale=0.8, font=\footnotesize]
	\tkzTabInit[nocadre,lgt=1.2,espcl=1.5,deltacl=0.6]
	{{$x$/0.6,$f'(x)$/0.6,$f(x)$/1.5}}
	{{$-\infty$,$-1$,$3$,$+\infty$}}
	\tkzTabLine{{,+,0,-,0,+,}}
	\tkzTabVar{{-/$-\infty$,+/${fmt_val(val_max)}$,-/${val_min}$,+/$+\infty$}}
\end{{tikzpicture}}
}}'''
        sign_d = "+" if d >= 0 else ""
        correct = fr'''y = \dfrac{{1}}{{3}}x^3 - x^2 - 3x {sign_d} {d}''' if d != 0 else fr'''y = \dfrac{{1}}{{3}}x^3 - x^2 - 3x'''
        wrong1 = fr'''y = -\dfrac{{1}}{{3}}x^3 + x^2 + 3x {sign_d} {d}''' if d != 0 else fr'''y = -\dfrac{{1}}{{3}}x^3 + x^2 + 3x'''
        wrong2 = fr'''y = x^3 - 3x^2 - 9x - 2'''
        wrong3 = fr'''y = -x^3 + 3x^2 + 9x - 2'''
        choices = [
            fr'''{{\True ${correct}$}}
''',
            fr'''{{${wrong1}$}}
''',
            fr'''{{${wrong2}$}}
''',
            fr'''{{${wrong3}$}}
'''
        ]
        random.shuffle(choices)
        loi_giai = fr'''Ta thấy cực trị tại $x=-1$ và $x=3$. Hàm số đồng biến ở hai khoảng biên ($a>0$). Đạo hàm $f'(x) = x^2 - 2x - 3 = 0$ có hai nghiệm là $-1$ và $3$. Do đó phương trình đúng là ${correct}$.'''
        return caudan, choices, loi_giai


def CuoiChuong1_MC_Cau8():
    sub_type = random.choice([1, 2, 3, 4, 5, 6])
    
    if sub_type == 1:
        b = random.choice([2, 3, 4])
        a = b - 1
        c = b + 1
        
        caudan = fr'''Cho hàm số $f(x)$ có đạo hàm $f'(x)=x(x-{a})^2(x-{b})(x-{c})^4, \quad \forall x\in\mathbb{{R}}.$ Điểm cực tiểu của hàm số đã cho là'''
        choices = [
            fr'''{{ $x={a}$ }}
''',
            fr'''{{\True $x={b}$ }}
''',
            fr'''{{ $x=0$ }}
''',
            fr'''{{ $x={c}$ }}
'''
        ]
        random.shuffle(choices)
        loi_giai = fr'''Đạo hàm chỉ đổi dấu khi đi qua các nghiệm đơn hoặc nghiệm bội lẻ: $x=0$ và $x={b}$. \\
Bảng xét dấu đạo hàm cho thấy $f'(x)$ đổi dấu từ âm sang dương khi đi qua $x={b}$, do đó $x={b}$ là điểm cực tiểu.'''
        return caudan, choices, loi_giai
        
    elif sub_type == 2:
        # New MC 3: Number of extrema from y' sign table with a double bar
        x1 = random.choice([-4, -3])
        x2 = random.choice([0, 1])
        x3 = random.choice([2, 3])
        
        caudan = fr'''\immini{{Cho hàm số $y=f(x)$ liên tục trên $\mathbb{{R}}$ với bảng xét dấu đạo hàm như sau. Số điểm cực trị của hàm số $y=f(x)$ là}}{{
\begin{{tikzpicture}}
    \tkzTabInit[nocadre,lgt=1.2,espcl=1.5,deltacl=0.6]
    {{$x$ /0.6,$y'$ /0.6}}
    {{$-\infty$,${x1}$,${x2}$,${x3}$,$+\infty$}}
    \tkzTabLine{{,-,$0$,+,d,+,0,-,}}
\end{{tikzpicture}}
}}'''
        choices = [
            fr'''{{\True $2$}}
''',
            fr'''{{$3$}}
''',
            fr'''{{$1$}}
''',
            fr'''{{$0$}}
'''
        ]
        random.shuffle(choices)
        loi_giai = fr'''Dựa vào bảng xét dấu đạo hàm: \\
- Đạo hàm $y'$ đổi dấu từ âm sang dương khi đi qua nghiệm $x={x1}$ (đây là điểm cực trị). \\
- Đạo hàm $y'$ không đổi dấu khi đi qua điểm không xác định $x={x2}$ (vẫn mang dấu dương). \\
- Đạo hàm $y'$ đổi dấu từ dương sang âm khi đi qua nghiệm $x={x3}$ (đây là điểm cực trị). \\
Do hàm số liên tục trên $\mathbb{{R}}$, số điểm cực trị của hàm số là $2$.'''
        return caudan, choices, loi_giai

    elif sub_type == 3:
        # New MC 7: Coordinates of cực tiểu point of y = 1/3 x^3 - 2x^2 + 3x + d
        d = random.choice([2, 3, 4])
        caudan = fr'''Tìm điểm cực tiểu của đồ thị hàm số $y=\dfrac{{1}}{{3}}x^3-2x^2+3x+{d}$.'''
        
        # y' = x^2 - 4x + 3 = 0 -> x = 1 (cực đại), x = 3 (cực tiểu)
        # y(3) = 9 - 18 + 9 + d = d
        # y(1) = 1/3 - 2 + 3 + d = 4/3 + d
        correct = fr'''(3; {d})'''
        w1_frac = Fraction(4 + 3*d, 3)
        def fmt_fr(fr):
            return fr'''\dfrac{{ {fr.numerator} }}{{ {fr.denominator} }}''' if fr.denominator != 1 else fr'''{fr.numerator}'''
        w1 = fr'''\left(1; {fmt_fr(w1_frac)}\right)''' # cực đại
        w2 = fr'''(3; 1)''' if d != 1 else fr'''(3; 2)'''
        w3 = fr'''(1; {d})'''
        
        choices = [
            fr'''{{\True ${correct}$}}
''',
            fr'''{{${w1}$}}
''',
            fr'''{{${w2}$}}
''',
            fr'''{{${w3}$}}
'''
        ]
        random.shuffle(choices)
        loi_giai = fr'''Ta có $y' = x^2 - 4x + 3 = 0 \iff \left[\begin{{array}}{{l}} x=1 \\ x=3 \end{{array}}\right.$. \\
Bảng biến thiên hoặc quy tắc 2 cho thấy hàm số đạt cực tiểu tại $x=3$. \\
Thay vào phương trình đồ thị ta được tung độ cực tiểu: $y(3) = \dfrac{{1}}{{3}}\cdot 3^3 - 2\cdot 3^2 + 3\cdot 3 + {d} = {d}$. \\
Vậy tọa độ điểm cực tiểu của đồ thị hàm số là $(3; {d})$.'''
        return caudan, choices, loi_giai

    elif sub_type == 4:
        # New MC 9: Count extrema of f(x) from factored f'(x)
        # f'(x) = x^k (x-a)^m (x-b)^n
        a = random.choice([1, 2])
        b = random.choice([-2, -3])
        
        caudan = fr'''Cho hàm số $f(x)$ có đạo hàm $f'(x)=x(x-{a})(x-({b}))^2$. Số điểm cực trị của hàm số đã cho là'''
        choices = [
            fr'''{{\True $2$}}
''',
            fr'''{{$3$}}
''',
            fr'''{{$1$}}
''',
            fr'''{{$4$}}
'''
        ]
        random.shuffle(choices)
        loi_giai = fr'''Phương trình $f'(x) = 0$ có các nghiệm: \\
- $x=0$ (nghiệm đơn) $\implies$ đổi dấu (cực trị). \\
- $x={a}$ (nghiệm đơn) $\implies$ đổi dấu (cực trị). \\
- $x={b}$ (nghiệm bội chẵn bậc 2) $\implies$ không đổi dấu (không là cực trị). \\
Vậy số điểm cực trị của hàm số là $2$.'''
        return caudan, choices, loi_giai

    elif sub_type == 5:
        # Number of extrema of f(x) continuous on R from f'(x) sign table (Image 3, Cau 18)
        x1 = -1
        x2 = 0
        x3 = 1
        x4 = 2
        
        caudan = fr'''\immini{{Cho hàm số $y=f(x)$ liên tục trên $\mathbb{{R}}$ và có bảng xét dấu của $f'(x)$ như hình vẽ. Số điểm cực trị của hàm số đã cho là}}{{
\begin{{tikzpicture}}
    \tkzTabInit[nocadre,lgt=1.2,espcl=1.5,deltacl=0.6]
    {{$x$ /0.6,$f'(x)$ /0.6}}
    {{$-\infty$,${x1}$,${x2}$,${x3}$,${x4}$,$+\infty$}}
    \tkzTabLine{{,+,0,-,d,+,0,+,0,-,}}
\end{{tikzpicture}}
}}'''
        choices = [
            fr'''{{\True $3$}}
''',
            fr'''{{$4$}}
''',
            fr'''{{$2$}}
''',
            fr'''{{$1$}}
'''
        ]
        random.shuffle(choices)
        loi_giai = fr'''Dựa vào bảng xét dấu của đạo hàm $f'(x)$ và sự liên tục của hàm số $y=f(x)$ trên $\mathbb{{R}}$: \\
- Đạo hàm $f'(x)$ đổi dấu từ dương sang âm khi đi qua $x={x1}$ (đạt cực đại tại $x={x1}$). \\
- Đạo hàm $f'(x)$ đổi dấu từ âm sang dương khi đi qua $x={x2}$ (dù $f'({x2})$ không xác định nhưng hàm số liên tục trên $\mathbb{{R}}$, đạt cực tiểu tại $x={x2}$). \\
- Đạo hàm $f'(x)$ không đổi dấu khi đi qua $x={x3}$ (luôn mang dấu dương, không phải cực trị). \\
- Đạo hàm $f'(x)$ đổi dấu từ dương sang âm khi đi qua $x={x4}$ (đạt cực đại tại $x={x4}$). \\
Vậy hàm số có đúng $3$ điểm cực trị.'''
        return caudan, choices, loi_giai

    else:
        # Factored derivative with even/odd powers (Image 5, Cau 29)
        a = random.choice([-2, -1, 1, 2])
        b = a + random.choice([2, 3])
        pow_a = random.choice([2, 4]) # even power
        pow_b = random.choice([1, 3]) # odd power
        
        caudan = fr'''Cho hàm số $f(x)$ có đạo hàm $f'(x)=(x-{a})^{pow_a}(x-{b})^{pow_b}, \forall x \in \mathbb{{R}}$. Số điểm cực trị của hàm số đã cho là'''
        choices = [
            fr'''{{\True $1$}}
''',
            fr'''{{$2$}}
''',
            fr'''{{$0$}}
''',
            fr'''{{$3$}}
'''
        ]
        random.shuffle(choices)
        loi_giai = fr'''Đạo hàm chỉ đổi dấu khi đi qua các nghiệm bội lẻ. \\
Ở đây, $f'(x) = 0$ tại $x={a}$ (nghiệm bội chẵn bậc ${pow_a}$) và $x={b}$ (nghiệm bội lẻ bậc ${pow_b}$). \\
Do đó, $f'(x)$ chỉ đổi dấu khi đi qua $x={b}$. \\
Vậy hàm số đã cho có đúng $1$ điểm cực trị.'''
        return caudan, choices, loi_giai

def CuoiChuong1_MC_Cau9():
    sub_type = random.choice([1, 2, 3, 4])
    
    if sub_type == 1:
        y_min = random.choice([2, 3, 4])
        y_max = random.choice([-4, -3, -2])
        
        caudan = fr'''\immini{{Cho hàm số $y=f(x)$ có bảng biến thiên như sau. Giá trị cực tiểu của hàm số là}}{{
\begin{{tikzpicture}} 
        \tkzTabInit[nocadre,lgt=1.2,espcl=2,deltacl=0.6]
        {{$x$ /0.6,$y'$ /0.6,$y$ /1.2}}
        {{$-\infty$,$-2$,$0$,$2$,$+\infty$}}
        \tkzTabLine{{,+,$0$,-,d,-,$0$,+,}}
        \tkzTabVar{{-/$-\infty$,+/{y_max},-D+/$-\infty$/$+\infty$,-/{y_min},+/$+\infty$}}
\end{{tikzpicture}}
}}'''
        
        choices = [
            fr'''{{\True ${y_min}$}}
''',
            fr'''{{${y_max}$}}
''',
            fr'''{{${y_min + 2}$}}
''',
            fr'''{{${y_max - 2}$}}
'''
        ]
        random.shuffle(choices)
        loi_giai = fr'''Nhìn vào bảng biến thiên, tại điểm cực tiểu $x=2$, giá trị cực tiểu của hàm số là $y={y_min}$.'''
        return caudan, choices, loi_giai

    elif sub_type == 2:
        # đạt cực tiểu/cực đại tại điểm x = ... (Image 1, Cau 12/13)
        is_ct = random.choice([True, False])
        x_min = random.choice([-2, -1, 0])
        x_max = x_min + random.choice([2, 3])
        y_min = random.choice([-4, -3, -2])
        y_max = random.choice([1, 2, 5])
        
        if is_ct:
            caudan = fr'''\immini{{Cho hàm số $f(x)$ có bảng biến thiên như sau. Hàm số đã cho đạt cực tiểu tại điểm}}{{
\begin{{tikzpicture}}
    \tkzTabInit[nocadre,lgt=1.2,espcl=1.5,deltacl=0.6]
    {{$x$ /0.6,$f'(x)$ /0.6,$f(x)$ /1.5}}
    {{$-\infty$,${x_min}$,${x_max}$,$+\infty$}}
    \tkzTabLine{{,-,$0$,+,0,-,}}
    \tkzTabVar{{+/$+\infty$,-/${y_min}$,+/${y_max}$,-/$-\infty$}}
\end{{tikzpicture}}
}}'''
            correct = fr'''x = {x_min}'''
            w1 = fr'''x = {y_min}''' # trap y_CT
            w2 = fr'''x = {x_max}''' # x_CD
            w3 = fr'''x = {y_max}''' # y_CD
        else:
            caudan = fr'''\immini{{Cho hàm số $f(x)$ có bảng biến thiên như sau. Hàm số đã cho đạt cực đại tại điểm}}{{
\begin{{tikzpicture}}
    \tkzTabInit[nocadre,lgt=1.2,espcl=1.5,deltacl=0.6]
    {{$x$ /0.6,$f'(x)$ /0.6,$f(x)$ /1.5}}
    {{$-\infty$,${x_min}$,${x_max}$,$+\infty$}}
    \tkzTabLine{{,-,$0$,+,0,-,}}
    \tkzTabVar{{+/$+\infty$,-/${y_min}$,+/${y_max}$,-/$-\infty$}}
\end{{tikzpicture}}
}}'''
            correct = fr'''x = {x_max}'''
            w1 = fr'''x = {y_max}''' # trap y_CD
            w2 = fr'''x = {x_min}''' # x_CT
            w3 = fr'''x = {y_min}''' # y_CT
            
        choices = [
            fr'''{{\True ${correct}$}}
''',
            fr'''{{${w1}$}}
''',
            fr'''{{${w2}$}}
''',
            fr'''{{${w3}$}}
'''
        ]
        random.shuffle(choices)
        if is_ct:
            loi_giai = fr'''Dựa vào bảng biến thiên, tại điểm $x = {x_min}$ đạo hàm đổi dấu từ âm sang dương và hàm số đạt giá trị cực tiểu $y = {y_min}$. \\
Do đó, hàm số đạt cực tiểu tại điểm $x = {x_min}$.'''
        else:
            loi_giai = fr'''Dựa vào bảng biến thiên, tại điểm $x = {x_max}$ đạo hàm đổi dấu từ dương sang âm và hàm số đạt giá trị cực đại $y = {y_max}$. \\
Do đó, hàm số đạt cực đại tại điểm $x = {x_max}$.'''
        return caudan, choices, loi_giai

    elif sub_type == 3:
        # BBT cực trị đúng/sai (Image 2, Cau 15)
        x1 = -1
        x2 = 0
        x3 = 1
        y1 = 0
        y2 = 3
        
        caudan = fr'''\immini{{Cho hàm số $f(x)$ có bảng biến thiên sau. Mệnh đề nào dưới đây sai?}}{{
\begin{{tikzpicture}}
    \tkzTabInit[nocadre,lgt=1.2,espcl=1.5,deltacl=0.6]
    {{$x$ /0.6,$f'(x)$ /0.6,$f(x)$ /1.5}}
    {{$-\infty$,${x1}$,${x2}$,${x3}$,$+\infty$}}
    \tkzTabLine{{,-,0,+,0,-,0,+,}}
    \tkzTabVar{{+/$+\infty$,-/${y1}$,+/${y2}$,-/${y1}$,+/$+\infty$}}
\end{{tikzpicture}}
}}'''
        choices = [
            fr'''{{\True Hàm số có giá trị cực đại bằng ${y1}$}}
''',
            fr'''{{Hàm số có hai điểm cực tiểu}}
''',
            fr'''{{Hàm số có ba điểm cực trị}}
''',
            fr'''{{Hàm số có giá trị cực đại bằng ${y2}$}}
'''
        ]
        random.shuffle(choices)
        loi_giai = fr'''Dựa vào bảng biến thiên: \\
- Hàm số đạt cực tiểu tại $x = {x1}$ và $x = {x3}$ với giá trị cực tiểu $y_{{CT}} = {y1}$ (nên có hai điểm cực tiểu). \\
- Hàm số đạt cực đại tại $x = {x2}$ với giá trị cực đại $y_{{CD}} = {y2}$. \\
- Tổng số điểm cực trị là $3$. \\
Do đó, phát biểu "Hàm số có giá trị cực đại bằng ${y1}$" là sai vì giá trị cực đại là ${y2}$.'''
        return caudan, choices, loi_giai

    else:
        # Đồ thị hàm số -> cực trị (Image 4, Câu 20 & 21)
        sub_type_graph = random.choice([1, 2])
        if sub_type_graph == 1:
            caudan = fr'''\immini{{Cho hàm số $y = f(x)$ liên tục trên $\mathbb{{R}}$ và có đồ thị như hình vẽ bên. Phát biểu nào sau đây là đúng?}}{{
\begin{{tikzpicture}}[scale=0.6, >=stealth]
    \draw[->] (-2.2,0) -- (2.5,0) node[below] {{$x$}};
    \draw[->] (0,-4) -- (0,2.5) node[left] {{$y$}};
    \draw (0,0) node[below right] {{$O$}};
    \draw[thick, smooth, samples=100, domain=-1.8:2.1] plot (\x, {{\x^3 - 3*\x - 1}});
    \draw[dashed] (-1,0) -- (-1,1) -- (0,1);
    \draw[dashed] (1,0) -- (1,-3) -- (0,-3);
    \node[below] at (-1,0) {{$ -1 $}};
    \node[above] at (1,0) {{$ 1 $}};
    \node[left] at (0,1) {{$ 1 $}};
    \node[left] at (0,-3) {{$ -3 $}};
\end{{tikzpicture}}
}}'''
            choices = [
                fr'''{{\True $x_{{CT}} = 1, x_{{CD}} = -1$}}
''',
                fr'''{{$x_{{CT}} = -1, x_{{CD}} = 1$}}
''',
                fr'''{{$x_{{CT}} = -3, x_{{CD}} = 1$}}
''',
                fr'''{{$x_{{CT}} = 1, x_{{CD}} = -3$}}
'''
            ]
            random.shuffle(choices)
            loi_giai = fr'''Từ đồ thị ta thấy: \\
- Điểm cực tiểu của đồ thị hàm số là $(1; -3) \implies x_{{CT}} = 1$. \\
- Điểm cực đại của đồ thị hàm số là $(-1; 1) \implies x_{{CD}} = -1$. \\
Vậy phát biểu đúng là $x_{{CT}} = 1, x_{{CD}} = -1$.'''
            return caudan, choices, loi_giai
        else:
            caudan = fr'''\immini{{Cho hàm số $y=f(x)$ có đồ thị như hình vẽ bên. Phát biểu nào sau đây đúng?}}{{
\begin{{tikzpicture}}[scale=0.6, >=stealth]
    \draw[->] (-2.2,0) -- (2.5,0) node[below] {{$x$}};
    \draw[->] (0,-3) -- (0,3) node[left] {{$y$}};
    \draw (0,0) node[below right] {{$O$}};
    \draw[dashed] (0,-3) -- (0,3);
    \draw[dashed] (-2.2,-2.2) -- (2.2,2.2);
    \draw[thick, smooth, samples=100, domain=0.4:2.2] plot (\x, {{\x + 1/\x}});
    \draw[thick, smooth, samples=100, domain=-2.2:-0.4] plot (\x, {{\x + 1/\x}});
    \draw[dashed] (1,0) -- (1,2) -- (0,2);
    \draw[dashed] (-1,0) -- (-1,-2) -- (0,-2);
    \node[below] at (1,0) {{$ 1 $}};
    \node[above] at (-1,0) {{$ -1 $}};
    \node[left] at (0,2) {{$ 2 $}};
    \node[right] at (0,-2) {{$ -2 $}};
\end{{tikzpicture}}
}}'''
            choices = [
                fr'''{{\True $y_{{CT}} = 2, y_{{CD}} = -2$}}
''',
                fr'''{{$y_{{CT}} = 1, y_{{CD}} = 2$}}
''',
                fr'''{{$y_{{CT}} = 2, y_{{CD}} = -1$}}
''',
                fr'''{{$y_{{CT}} = -2, y_{{CD}} = 2$}}
'''
            ]
            random.shuffle(choices)
            loi_giai = fr'''Dựa vào hình vẽ đồ thị hàm số: \\
- Hàm số đạt cực tiểu tại điểm $(1; 2) \implies y_{{CT}} = 2$. \\
- Hàm số đạt cực đại tại điểm $(-1; -2) \implies y_{{CD}} = -2$. \\
Vậy phát biểu đúng là $y_{{CT}} = 2, y_{{CD}} = -2$.'''
            return caudan, choices, loi_giai

def CuoiChuong1_MC_Cau10():
    sub_type = random.choice([1, 2])
    
    if sub_type == 1:
        d = random.choice([1, 2])
        
        caudan = fr'''\immini{{Hàm số $y=ax^3+bx^2+cx+d$ ($a,b,c,d\in\mathbb{{R}},\, a\neq 0$) có đồ thị như hình vẽ bên. Trong các hệ số $a,b,c,d$ có mấy hệ số mang giá trị dương?}}{{
\begin{{tikzpicture}}[scale=0.4, line join=round, line cap=round, >=stealth,font=\footnotesize] 
    \def\xmin{{-4}}\def\xmax{{4}}\def\ymin{{-1}}\def\ymax{{6}}
    \draw[->] (\xmin-0.2,0)--(\xmax+0.2,0) node[below]{{$x$}};
    \draw[->] (0,\ymin-0.2)--(0,\ymax+0.2) node[right]{{$y$}};
    \foreach \x in {{-3,-2,-1,1,2,3}}\draw (\x,0.1)--(\x,-0.1) node[below]{{$\x$}};
    \foreach \y in {{1,2,3,4,5}}\draw (0.1,\y)--(-0.1,\y) node[left]{{$\y$}};
    \clip (\xmin,\ymin) rectangle (\xmax,\ymax);
    \draw[thick,smooth,samples=200,domain=\xmin:\xmax] plot (\x,{{1/3*\x*\x*\x + 1/2*\x*\x - 2*\x + {d}}});
\end{{tikzpicture}}
}}'''
        choices = [
            fr'''{{$2$}}
''',
            fr'''{{$1$}}
''',
            fr'''{{$4$}}
''',
            fr'''{{\True $3$}}
'''
        ]
        random.shuffle(choices)
        loi_giai = fr'''Từ đồ thị ta thấy:
- Nhánh bên phải hướng lên $\Rightarrow a > 0$.
- Đồ thị cắt trục tung tại $(0;{d}) \Rightarrow d = {d} > 0$.
- Hoành độ hai điểm cực trị $x_1 < 0 < x_2$ và $|x_1| > x_2 \Rightarrow x_1 + x_2 < 0 \Rightarrow -2b/3a < 0 \Rightarrow b > 0$.
- Tích hoành độ cực trị $x_1 x_2 < 0 \Rightarrow c/3a < 0 \Rightarrow c < 0$.
Vậy có 3 hệ số dương là $a, b, d$.'''
        return caudan, choices, loi_giai

    else:
        # Number of roots of m*f(x) + n = 0 from BBT (Image 5, Câu 39)
        ymax = random.choice([2, 3, 4])
        ymin = random.choice([-2, -1, 0])
        while ymax <= ymin:
            ymax = random.choice([2, 3, 4])
            ymin = random.choice([-2, -1, 0])
            
        scenario = random.choice([1, 2, 3])
        if scenario == 1:
            val = ymin - 1
            ans = 1
        elif scenario == 2:
            val = random.choice([ymin, ymax])
            ans = 2
        else:
            if ymax - ymin >= 2:
                val_int = random.choice(range(ymin + 1, ymax))
                val = val_int
            else:
                val = Fraction(ymin + ymax, 2)
            ans = 3
            
        m = random.choice([1, 2, 3])
        n_val = -val * m
        if isinstance(n_val, Fraction):
            m = m * n_val.denominator
            n_val = n_val.numerator
        
        sign_n = "+" if n_val >= 0 else "-"
        abs_n = abs(n_val)
        if abs_n == 0:
            eq_str = fr'''{m}f(x) = 0'''
        else:
            eq_str = fr'''{m}f(x) {sign_n} {abs_n} = 0'''
            
        if m == 1:
            eq_str = eq_str.replace("1f(x)", "f(x)")
            
        def fmt_val(v):
            if isinstance(v, Fraction):
                return fr'''\dfrac{{{v.numerator}}}{{{v.denominator}}}'''
            return str(v)
            
        caudan = fr'''\immini{{Cho hàm số $y=f(x)$ có bảng biến thiên như sau:}}{{
\begin{{tikzpicture}}
    \tkzTabInit[nocadre,lgt=1.2,espcl=2,deltacl=0.6]
    {{$x$ /0.6,$f'(x)$ /0.6,$f(x)$ /1.5}}
    {{$-\infty$,$1$,$3$,$+\infty$}}
    \tkzTabLine{{,-,0,+,0,-,}}
    \tkzTabVar{{+/$+\infty$,-/${ymin}$,+/${ymax}$,-/$-\infty$}}
\end{{tikzpicture}}
}}
Số nghiệm của phương trình ${eq_str}$ là'''
        
        choices = [
            fr'''{{\True ${ans}$}}
''',
            fr'''{{${3 if ans != 3 else 1}$}}
''',
            fr'''{{${2 if ans != 2 else 1}$}}
''',
            fr'''{{$0$}}
'''
        ]
        random.shuffle(choices)
        loi_giai = fr'''Phương trình ${eq_str} \iff f(x) = {fmt_val(val)}$. \\
Số nghiệm của phương trình bằng số giao điểm của đồ thị hàm số $y=f(x)$ với đường thẳng nằm ngang $y = {fmt_val(val)}$. \\
Dựa vào bảng biến thiên, ta thấy: \\
- Cực đại là $y = {ymax}$. \\
- Cực tiểu là $y = {ymin}$. \\
Vì {f"{ymin} < {fmt_val(val)} < {ymax}" if ans == 3 else (f"{fmt_val(val)} = {ymin}" if val == ymin else (f"{fmt_val(val)} = {ymax}" if val == ymax else f"{fmt_val(val)} < {ymin}"))} nên đường thẳng $y = {fmt_val(val)}$ cắt đồ thị tại đúng ${ans}$ điểm. \\
Vậy phương trình có ${ans}$ nghiệm.'''
        return caudan, choices, loi_giai


def CuoiChuong1_MC_Cau11():
    sub_type = random.choice([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11])
    
    if sub_type == 1:
        # Old BBT variation intervals
        x1 = -1
        x2 = 1
        caudan = fr'''\immini{{Cho hàm số $y=f(x)$ có bảng biến thiên sau. Mệnh đề nào dưới đây đúng?}}{{
\begin{{tikzpicture}}
    \tkzTabInit[nocadre,espcl=2,lgt=1.2]
    {{$x$ /0.6,$y'$ /0.6,$y$ /1.5}}
    {{$-\infty$, {x1}, {x2}, $+\infty$}}
    \tkzTabLine{{,+,0,-,0,+,}}
    \tkzTabVar{{-/$-\infty$, +/$3$, -/$-1$, +/$+\infty$}}
\end{{tikzpicture}}
}}'''
        choices = [
            fr'''{{Hàm số nghịch biến trên khoảng $({x1};3)$}}
''',
            fr'''{{\True Hàm số nghịch biến trên khoảng $({x1}; {x2})$}}
''',
            fr'''{{Hàm số đồng biến trên khoảng $({x1}; {x2})$}}
''',
            fr'''{{Hàm số nghịch biến trên khoảng $(-\infty; {x2})$}}
'''
        ]
        random.shuffle(choices)
        loi_giai = fr'''Dựa vào bảng biến thiên, đạo hàm mang dấu âm trên khoảng $({x1}; {x2})$, do đó hàm số nghịch biến trên khoảng $({x1}; {x2})$.'''
        return caudan, choices, loi_giai

    elif sub_type == 2:
        # New MC 2: Monotonicity from BBT
        x1 = random.choice([-2, -1, 0])
        x2 = random.choice([2, 3, 4])
        # Decreases on (x1, x2), increases on outside.
        caudan = fr'''\immini{{Cho hàm số $y = f(x)$ có bảng biến thiên như dưới đây. Hàm số đã cho nghịch biến trên khoảng nào sau đây?}}{{
\begin{{tikzpicture}}[scale=0.8, font=\footnotesize]
	\tkzTabInit[nocadre,lgt=1.2,espcl=1.5,deltacl=0.6]
	{{$x$/0.6,$f'(x)$/0.6,$f(x)$/1.5}}
	{{$-\infty$,{x1},{x2},$+\infty$}}
	\tkzTabLine{{,+,0,-,0,+,}}
	\tkzTabVar{{-/$-\infty$,+/$6$,-/$-26$,+/$+\infty$}}
\end{{tikzpicture}}
}}'''
        choices = [
            fr'''{{$(-\infty; {x1})$}}
''',
            fr'''{{$({x2}; +\infty)$}}
''',
            fr'''{{$(-26; 6)$}}
''',
            fr'''{{\True $({x1}; {x2-1})$}}
'''
        ]
        random.shuffle(choices)
        loi_giai = fr'''Dựa vào bảng biến thiên, hàm số nghịch biến trên khoảng $({x1}; {x2})$. Vì vậy, nó cũng nghịch biến trên khoảng con của nó là $({x1}; {x2-1})$.'''
        return caudan, choices, loi_giai

    elif sub_type == 3:
        # New MC 11: Min/max on closed interval from BBT
        val_max = random.choice([2, 4, 6])
        caudan = fr'''\immini{{Cho hàm số $y = f(x)$ xác định trên đoạn $[-\sqrt{{3}}; \sqrt{{5}}]$ và có bảng biến thiên như hình vẽ.}}{{
\begin{{tikzpicture}}[scale=0.8, font=\footnotesize]
  \tkzTabInit[nocadre,lgt=1.5,espcl=1.5,deltacl=0.5]
	{{$x$/0.6,$f'(x)$/0.6,$f(x)$/1.5}}
     {{$-\sqrt{{3}}$,$-1$,$1$,$\sqrt{{5}}$}}
  \tkzTabLine{{,+,0,-,0,+,}}
  \tkzTabVar{{-/$0$,+/{val_max},-/$-2$,+/{val_max + 3}}}
\end{{tikzpicture}}
}}
Khẳng định nào sau đây là đúng?'''
        correct = r'\max_{[-\sqrt{3}; \sqrt{5}]} y = ' + str(val_max + 3)
        choices = [
            r'{\True $' + correct + r'$}',
            r'{\min_{[-\sqrt{3}; \sqrt{5}]} y = 0}',
            r'{\min_{[-\sqrt{3}; \sqrt{5}]} y = 1}',
            r'{\max_{[-\sqrt{3}; \sqrt{5}]} y = ' + str(val_max) + r'}'
        ]
        random.shuffle(choices)
        loi_giai = fr'''Dựa vào bảng biến thiên, giá trị lớn nhất trên đoạn $[-\sqrt{{3}}; \sqrt{{5}}]$ đạt được tại điểm cuối $\sqrt{{5}}$ với giá trị là ${val_max + 3}$.'''
        return caudan, choices, loi_giai

    elif sub_type == 4:
        # New MC 12: Monotonicity from f'(x) derivative graph
        x1 = random.choice([-2, -1, 0])
        x2 = random.choice([3, 4, 5])
        # f'(x) = -0.6 * (x - x1) * (x - x2) -> positive inside (x1, x2).
        caudan = fr'''\immini{{Cho hàm số $y = f(x)$ xác định, có đạo hàm trên $\mathbb{{R}}$ và $f'(x)$ có đồ thị như hình vẽ bên dưới. Hàm số $y = f(x)$ đồng biến trên khoảng nào dưới đây?}}{{
\begin{{tikzpicture}}[line join=round, line cap=round, >=stealth, scale=0.7, font=\footnotesize]
  \draw[->] (-2.5,0) -- (6,0) node[below] {{$x$}};
  \draw[->] (0,-3) -- (0,2.5) node[left] {{$y$}};
  \node[below right] at (0,0) {{$O$}};
  \node[above left] at ({x1},0) {{${x1}$}};
  \node[above right] at ({x2},0) {{${x2}$}};
  \draw[thick, smooth, samples=100, domain={x1 - 0.5}:{x2 + 0.3}] plot (\x, {{-0.6*(\x - {x1})*(\x - {x2})}});
\end{{tikzpicture}}
}}'''
        choices = [
            fr'''{{\True $({x1 + 1}; {x2})$}}
''',
            fr'''{{$({x1}; {x1+1})$}}
''',
            fr'''{{$({x2}; +\infty)$}}
''',
            fr'''{{$(-\infty; {x1})$}}
'''
        ]
        random.shuffle(choices)
        loi_giai = fr'''Hàm số $y=f(x)$ đồng biến khi đạo hàm $f'(x) \ge 0$. Từ đồ thị $y=f'(x)$, ta thấy đồ thị nằm phía trên trục hoành trên khoảng $({x1}; {x2})$. Do đó hàm số đồng biến trên $({x1}; {x2})$ và các khoảng con của nó như $({x1 + 1}; {x2})$.'''
        return caudan, choices, loi_giai

    elif sub_type == 5:
        # New MC 2: Cho hàm số y=f(x) có bảng biến thiên... Mệnh đề nào dưới đây đúng?
        x1 = random.choice([-2, -1])
        x2 = random.choice([1, 2])
        y1 = random.choice([2, 3])
        y2 = random.choice([-2, -1])
        y3 = random.choice([3, 4])
        y4 = random.choice([-4, -3])
        
        caudan = fr'''\immini{{Cho hàm số $y=f(x)$ có bảng biến thiên như hình vẽ. Mệnh đề nào dưới đây đúng?}}{{
\begin{{tikzpicture}}
    \tkzTabInit[nocadre,lgt=1.2,espcl=1.5,deltacl=0.6]
    {{$x$ /0.6,$y'$ /0.6,$y$ /1.7}}
    {{$-\infty$,${x1}$,$0$,${x2}$,$+\infty$}}
    \tkzTabLine{{,+,$0$,-,d,+,$0$,-,}}
    \tkzTabVar{{-/$-\infty$, +/${y1}$,-/${y2}$,+/${y3}$,-/${y4}$}}
\end{{tikzpicture}}
}}'''
        choices = [
            fr'''{{\True Hàm số nghịch biến trên khoảng $({x2}; {x2+1})$}}
''',
            fr'''{{Hàm số đồng biến trên khoảng $(-\infty; 0)$}}
''',
            fr'''{{Hàm số nghịch biến trên khoảng $({x1}; {x2})$}}
''',
            fr'''{{Hàm số đồng biến trên khoảng $({x1}-1; {x2}+1)$}}
'''
        ]
        random.shuffle(choices)
        loi_giai = fr'''Dựa vào bảng biến thiên, hàm số nghịch biến trên các khoảng $({x1}; 0)$ và $({x2}; +\infty)$. \\
Do đó, hàm số cũng nghịch biến trên khoảng con $({x2}; {x2+1}) \subset ({x2}; +\infty)$.'''
        return caudan, choices, loi_giai

    elif sub_type == 6:
        # New MC 6: Cho hàm số y=f(x) có đạo hàm y'=f'(x)=x(x-b)... Hàm số nghịch biến trên khoảng nào?
        b = random.choice([2, 3, 4])
        caudan = fr'''Cho hàm số $y=f(x)$ có đạo hàm $f'(x)=x(x-{b}), \forall x \in \mathbb{{R}}$. Hàm số $y=f(x)$ nghịch biến trên khoảng nào dưới đây?'''
        choices = [
            fr'''{{\True $(0; {b-1})$}}
''',
            fr'''{{$(-\infty; 0)$}}
''',
            fr'''{{$({b}; +\infty)$}}
''',
            fr'''{{$(-\infty; {b})$}}
'''
        ]
        random.shuffle(choices)
        loi_giai = fr'''Ta có $f'(x) \le 0 \iff x(x-{b}) \le 0 \iff 0 \le x \le {b}$. \\
Hàm số nghịch biến trên khoảng $(0; {b})$. \\
Khoảng $(0; {b-1})$ là khoảng con của $(0; {b})$, nên hàm số nghịch biến trên khoảng này.'''
        return caudan, choices, loi_giai

    elif sub_type == 7:
        # New MC 8: Cubic graph y = -x^3 + 3x + d monotonicity
        d = random.choice([1, 2, 3])
        # local min at x=-1 (y=d-2), local max at x=1 (y=d+2).
        # decreases on (-inf, -1) and (1, +inf), increases on (-1, 1).
        caudan = fr'''\immini{{Cho hàm số $y=f(x)$ có đồ thị như hình vẽ. Hàm số nghịch biến trên khoảng nào trong các khoảng đã cho dưới đây?}}{{
\begin{{tikzpicture}}[scale=0.6, line join=round, line cap=round, >=stealth,font=\footnotesize]
    \def\xmin{{-2.2}}\def\xmax{{2.2}}\def\ymin{{-0.5}}\def\ymax{{4.5}}
    \draw[->] (\xmin-0.2,0)--(\xmax+0.2,0) node[below]{{$x$}};
    \draw[->] (0,\ymin-0.2)--(0,\ymax+0.2) node[right]{{$y$}};
    \foreach \x in {{-2,-1,1,2}}\draw (\x,0.1)--(\x,-0.1) node[below]{{$\x$}};
    \foreach \y in {{1,2,3,4}}\draw (0.1,\y)--(-0.1,\y) node[left]{{$\y$}};
    \clip (\xmin,\ymin) rectangle (\xmax,\ymax);
    \draw[thick,smooth,samples=200,domain=\xmin:\xmax] plot (\x,{{-1*((\x*\x*\x)) + 3*(\x) + {d}}});
    \draw[dashed] (0,0)--(0,{d})--(0,{d});\fill (0,{d}) circle(1.5pt);
    \draw[dashed] (-1,0)--(-1,{d-2})--(0,{d-2});\fill (-1,{d-2}) circle(1.5pt);
    \draw[dashed] (1,0)--(1,{d+2})--(0,{d+2});\fill (1,{d+2}) circle(1.5pt);
\end{{tikzpicture}}
}}'''
        choices = [
            fr'''{{\True $(1; 2)$}}
''',
            fr'''{{$(-1; 1)$}}
''',
            fr'''{{$(-2; 0)$}}
''',
            fr'''{{$(-\infty; 0)$}}
'''
        ]
        random.shuffle(choices)
        loi_giai = fr'''Dựa vào đồ thị, hàm số đi xuống (nghịch biến) trên các khoảng $(-\infty; -1)$ và $(1; +\infty)$. \\
Do đó, hàm số nghịch biến trên khoảng $(1; 2) \subset (1; +\infty)$.'''
        return caudan, choices, loi_giai

    elif sub_type == 8:
        # New MC 4 (Variation 8): Compare f(x) values using derivative f'(x) = (x-a)(x-b)^2(x-c)^3
        a, b, c = -1, 4, 8
        caudan = fr'''Cho hàm số $y=f(x)$ liên tục trên $\mathbb{{R}}$ và có đạo hàm $f'(x)=(x-{a})(x-{b})^2(x-{c})^3,\;\forall x\in\mathbb{{R}}$. Khẳng định nào sau đây đúng?'''
        
        choices = [
            fr'''{{\True $f({a}) > f({b})$}}
''',
            fr'''{{$f({b}) < f({c})$}}
''',
            fr'''{{$f({c}) > f({c + 4})$}}
''',
            fr'''{{$f({a}) < f({b})$}}
'''
        ]
        random.shuffle(choices)
        loi_giai = fr'''Ta lập bảng xét dấu cho đạo hàm $f'(x)$: \\
- Với $x \in ({a}; {b}) \cup ({b}; {c}) \implies f'(x) < 0$ (do $x-{a} > 0$, $(x-{b})^2 > 0$, $(x-{c})^3 < 0$). \\
Hàm số nghịch biến trên đoạn $[{a}; {c}]$. \\
Vì ${a} < {b} \in [{a}; {c}]$, do đó $f({a}) > f({b})$.'''
        return caudan, choices, loi_giai

    elif sub_type == 9:
        # Monotonicity from f'(x) sign table with double bars (Image 2, Cau 16)
        x1 = -2
        x2 = 0
        x3 = 1
        
        caudan = fr'''\immini{{Cho hàm số $y=f(x)$ có bảng xét dấu đạo hàm như sau:}}{{
\begin{{tikzpicture}}
    \tkzTabInit[nocadre,lgt=1.2,espcl=1.5,deltacl=0.6]
    {{$x$ /0.6,$f'(x)$ /0.6}}
    {{$-\infty$,${x1}$,$0$,${x3}$,$+\infty$}}
    \tkzTabLine{{,-,d,+,0,+,d,-,}}
\end{{tikzpicture}}
}}
Hàm số đã cho đồng biến trên khoảng nào sau đây?'''
        choices = [
            fr'''{{\True $({x1}; {x3})$}}
''',
            fr'''{{$(-\infty; {x1})$}}
''',
            fr'''{{$({x3}; +\infty)$}}
''',
            fr'''{{$(-\infty; 0)$}}
'''
        ]
        random.shuffle(choices)
        loi_giai = fr'''Đạo hàm $f'(x)$ mang dấu dương trên khoảng $({x1}; 0)$ và $(0; {x3})$, và bằng $0$ tại $x=0$. \\
Do đó, hàm số đồng biến trên toàn bộ khoảng liên tục $({x1}; {x3})$.'''
        return caudan, choices, loi_giai

    elif sub_type == 10:
        # BBT with vertical asymptote (Image 3, Cau 17)
        x1 = 0
        x2 = 1
        x3 = 2
        
        caudan = fr'''\immini{{Cho hàm số $y=f(x)$ có bảng biến thiên như sau:}}{{
\begin{{tikzpicture}}
    \tkzTabInit[nocadre,lgt=1.2,espcl=1.5,deltacl=0.6]
    {{$x$ /0.6,$y'$ /0.6,$y$ /1.7}}
    {{$-\infty$,${x1}$,${x2}$,${x3}$,$+\infty$}}
    \tkzTabLine{{,+,0,-,d,-,0,+,}}
    \tkzTabVar{{-/$-\infty$, +/$-2$,-D+/$-\infty$/$+\infty$,-/{ -1 },+/$+\infty$}}
\end{{tikzpicture}}
}}
Hàm số đã cho nghịch biến trên khoảng nào sau đây?'''
        choices = [
            fr'''{{\True $({x1}; {x2})$}}
''',
            fr'''{{$({x1}; {x3})$}}
''',
            fr'''{{$({x1}; +\infty)$}}
''',
            fr'''{{$(-\infty; {x2})$}}
'''
        ]
        random.shuffle(choices)
        loi_giai = fr'''Dựa vào bảng biến thiên, hàm số nghịch biến (đồ thị đi xuống và $y'<0$) trên các khoảng $({x1}; {x2})$ và $({x2}; {x3})$. \\
Trong các phương án lựa chọn, khoảng $({x1}; {x2})$ là khoảng nghịch biến của hàm số. Khoảng $({x1}; {x3})$ là sai vì hàm số không liên tục và không xác định tại $x = {x2}$.'''
        return caudan, choices, loi_giai

    else:
        # Monotonicity from quadratic derivative f'(x) = x^2 - 5x - 6 (Image 5, Cau 28)
        a = random.choice([-3, -2, -1])
        b = a + random.choice([4, 5, 6])
        
        sum_roots = a + b
        prod_roots = a * b
        
        sum_str = f"- {sum_roots}" if sum_roots > 0 else (f"+ {abs(sum_roots)}" if sum_roots < 0 else "")
        prod_str = f"+ {prod_roots}" if prod_roots > 0 else (f"- {abs(prod_roots)}" if prod_roots < 0 else "")
        
        expr = f"x^2 {sum_str} x {prod_str}".replace(" 1 x", " x").replace("  ", " ")
        
        is_dec = random.choice([True, False])
        dir_str = "nghịch biến" if is_dec else "đồng biến"
        
        if is_dec:
            correct = fr'''$({a}; {b})$'''
            w1 = fr'''$(-\infty; {a})$'''
            w2 = fr'''$({b}; +\infty)$'''
            w3 = fr'''$({a - 2}; {b + 2})$'''
        else:
            correct = fr'''$({b}; +\infty)$'''
            w1 = fr'''$({a}; {b})$'''
            w2 = fr'''$({a}; {b + 2})$'''
            w3 = fr'''$({a - 2}; {b})$'''
            
        caudan = fr'''Cho hàm số $y=f(x)$ có đạo hàm $f'(x) = {expr}, \forall x\in\mathbb{{R}}$. Hàm số đã cho {dir_str} trên khoảng nào trong các khoảng dưới đây?'''
        choices = [
            fr'''{{\True {correct}}}
''',
            fr'''{{{w1}}}
''',
            fr'''{{{w2}}}
''',
            fr'''{{{w3}}}
'''
        ]
        random.shuffle(choices)
        
        loi_giai = fr'''Xét dấu đạo hàm $f'(x) = x^2 - ({a+b})x + {prod_roots} = (x-{a})(x-{b}) = 0 \iff \left[\begin{{array}}{{l}} x={a} \\ x={b} \end{{array}}\right.$. \\
Bảng xét dấu đạo hàm cho thấy: \\
- $f'(x) < 0 \iff x \in ({a}; {b}) \implies$ hàm số nghịch biến trên khoảng $({a}; {b})$. \\
- $f'(x) > 0 \iff x \in (-\infty; {a}) \cup ({b}; +\infty) \implies$ hàm số đồng biến trên các khoảng $(-\infty; {a})$ và $({b}; +\infty)$. \\
Vậy phương án đúng là {correct}.'''
        return caudan, choices, loi_giai


# --- SHORT ANSWER (6 CÂU GÔM GỌN THEO MỨC ĐỘ) ---

# ==============================================================================
# BÀI TẬP CUỐI CHƯƠNG I - TRẢ LỜI NGẮN (6 CÂU GÔM GỌN)
# ==============================================================================

# ------------------------------------------------------------------------------
# CÂU 1: MỨC ĐỘ NHẬN BIẾT (DẠNG 1) - ĐƠN ĐIỆU & CỰC TRỊ CƠ BẢN
# ------------------------------------------------------------------------------
def CuoiChuong1_SA_Cau1():
    sub_type = random.choice([1, 2, 3, 4])
    
    if sub_type == 1:
        # Cực trị hàm bậc ba cơ bản y = x^3 - 3k x^2 + 3(k^2-1)x - 1
        k = random.choice([2, 3, 4])
        a = k - 1
        b = k + 1
        coef_x2 = 3 * k
        coef_x = 3 * (k*k - 1)
        ans = a + b
        caudan = fr'''Cho hàm số $f(x)=x^3-{coef_x2}x^2+{coef_x}x-1$. Biết hàm số đạt cực trị tại hai điểm $x_1, x_2$. Tính tổng $x_1 + x_2$.'''
        dapan = f'''{ans}'''
        loi_giai = fr'''Ta có $f'(x)=3x^2-{coef_x2*2}x+{coef_x} = 0 \iff x = {a}$ hoặc $x = {b}$. \\
Do đó hàm số có hai điểm cực trị là $x_1 = {a}, x_2 = {b}$. \\
Tổng hai điểm cực trị là $x_1 + x_2 = {a} + {b} = {ans}$.'''
        return caudan, dapan, loi_giai
        
    elif sub_type == 2:
        # Giá trị cực đại và cực tiểu của y = x^3 - 3x^2 - c
        c = random.choice([1, 2, 3, 4, 5])
        ans = 2 * (c**2) - c - 4
        caudan = fr'''Cho hàm số $y = x^3 - 3x^2 - {c}$. Gọi $a, b$ lần lượt là giá trị cực đại và giá trị cực tiểu của hàm số đó. Tính giá trị của $2a^2 + b$.'''
        dapan = f'''{ans}'''
        loi_giai = fr'''Ta có $y' = 3x^2 - 6x = 3x(x - 2) = 0 \iff \left[\begin{{array}}{{l}} x=0 \\ x=2 \end{{array}}\right.$. \\
- Hàm số đạt cực đại tại $x=0 \implies a = y(0) = -{c}$. \\
- Hàm số đạt cực tiểu tại $x=2 \implies b = y(2) = 2^3 - 3\cdot 2^2 - {c} = -{c} - 4$. \\
Giá trị biểu thức: $2a^2 + b = 2(-{c})^2 + (-{c} - 4) = {ans}$.'''
        return caudan, dapan, loi_giai

    elif sub_type == 3:
        # Cực đại tại a, cực tiểu tại b của y = 1/3 x^3 + k x^2 + ...
        k = random.choice([4, 5, 6])
        p = 2*k - 1
        # y' = x^2 + 2kx + (2k-1) -> nghiệm -1 và -(2k-1)
        # a = -(2k-1), b = -1
        a = -(2*k - 1)
        b = -1
        ans = a + b
        caudan = fr'''Cho hàm số $y = \dfrac{{1}}{{3}}x^3 + {k}x^2 + {p}x - 2$. Biết hàm số đạt cực đại tại $x=a$ và đạt cực tiểu tại $x=b$. Tính $a+b$.'''
        dapan = f'''{ans}'''
        loi_giai = fr'''Ta có $y' = x^2 + {2*k}x + {p} = (x - ({a}))(x - ({b})) = 0 \iff x = {a}$ hoặc $x = {b}$. \\
Bảng biến thiên cho thấy hàm số đạt cực đại tại $x = {a} \implies a = {a}$, đạt cực tiểu tại $x = {b} \implies b = {b}$. \\
Vậy $a + b = ({a}) + ({b}) = {ans}$.'''
        return caudan, dapan, loi_giai

    else:
        # Khoảng đồng biến của hàm bậc ba đơn giản
        m = random.choice([1, 2, 3])
        ans = 2 * m
        caudan = fr'''Cho hàm số $y = -x^3 + {3*m}x^2 - 1$. Hàm số đồng biến trên khoảng $(a; b)$. Tính giá trị của $a + b$.'''
        dapan = f'''{ans}'''
        loi_giai = fr'''Ta có $y' = -3x^2 + {6*m}x = -3x(x - {2*m})$. \\
$y' > 0 \iff 0 < x < {2*m}$. \\
Do đó hàm số đồng biến trên khoảng $(0; {2*m})$. \\
Suy ra $a = 0, b = {2*m} \implies a + b = {ans}$.'''
        return caudan, dapan, loi_giai


# ------------------------------------------------------------------------------
# CÂU 2: MỨC ĐỘ NHẬN BIẾT (DẠNG 2) - TIỆM CẬN & GTLN - GTNN CƠ BẢN
# ------------------------------------------------------------------------------
def CuoiChuong1_SA_Cau2():
    sub_type = random.choice([1, 2, 3, 4])
    
    if sub_type == 1:
        # Tiệm cận đứng và tiệm cận ngang của hàm nhất biến
        p = random.choice([2, 3, 4, 5])
        s = random.choice([2, 4, 6])
        q = random.choice([1, 3, 5])
        a = -s // 2
        b = Fraction(p, 2)
        ans = int(2*a + 2*b)
        caudan = fr'''Cho hàm số $y = \dfrac{{{p}x - {q}}}{{2x + {s}}}$. Đồ thị hàm số có đường tiệm cận đứng là $x = a$ và đường tiệm cận ngang là $y = b$. Tính giá trị của biểu thức $P = 2a + 2b$.'''
        dapan = f'''{ans}'''
        loi_giai = fr'''Đồ thị hàm số có: \\
- Tiệm cận đứng: $2x + {s} = 0 \iff x = -\dfrac{{{s}}}{{2}} = {a} \implies a = {a}$. \\
- Tiệm cận ngang: $y = \lim_{{x\to\pm\infty}} \dfrac{{{p}x - {q}}}{{2x + {s}}} = \dfrac{{{p}}}{{2}} \implies b = \dfrac{{{p}}}{{2}}$. \\
Vậy $P = 2a + 2b = 2({a}) + 2\left(\dfrac{{{p}}}{{2}}\right) = {ans}$.'''
        return caudan, dapan, loi_giai

    elif sub_type == 2:
        # Tiệm cận xiên của hàm phân thức bậc 2 trên bậc 1
        d = random.choice([1, 2, 3])
        p = random.choice([2, 3])
        k = random.choice([1, 2, 3])
        # f(x) = p*x + k + 5/(x - d) = (p*x^2 + (k - p*d)*x + (5 - k*d))/(x - d)
        b_coef = k - p * d
        c_coef = 5 - k * d
        sign_b = f"{b_coef:+d}".replace("+1", "+").replace("-1", "-")
        sign_c = f"{c_coef:+d}"
        ans = p + k
        caudan = fr'''Đường tiệm cận xiên của đồ thị hàm số $y = \dfrac{{{p}x^2 {sign_b}x {sign_c}}}{{x - {d}}}$ có phương trình dạng $y = ax + b$. Tính giá trị $a + b$.'''
        dapan = f'''{ans}'''
        loi_giai = fr'''Thực hiện phép chia đa thức tử cho mẫu: \\
$\dfrac{{{p}x^2 {sign_b}x {sign_c}}}{{x - {d}}} = {p}x + {k} + \dfrac{{5}}{{x - {d}}}$. \\
Vì $\lim_{{x \to \pm\infty}} \dfrac{{5}}{{x - {d}}} = 0$ nên tiệm cận xiên của đồ thị là $y = {p}x + {k}$. \\
Suy ra $a = {p}, b = {k} \implies a + b = {ans}$.'''
        return caudan, dapan, loi_giai

    elif sub_type == 3:
        # GTLN, GTNN của hàm bậc ba trên đoạn [0; 3]
        d = random.choice([2, 3, 5, 7])
        ans = 2 * d - 4
        caudan = fr'''Gọi $M, m$ lần lượt là giá trị lớn nhất, giá trị nhỏ nhất của hàm số $y=x^3-3x^2+{d}$ trên đoạn $[0;3]$. Tính tổng $S=M+m$.'''
        dapan = f'''{ans}'''
        loi_giai = fr'''Ta có: $y' = 3x^2 - 6x = 3x(x-2) = 0 \iff x=0$ hoặc $x=2$. \\
Xét các giá trị trên đoạn $[0; 3]$: \\
$y(0) = {d}$, $y(2) = 2^3 - 3\cdot 2^2 + {d} = {d-4}$, $y(3) = 3^3 - 3\cdot 3^2 + {d} = {d}$. \\
Do đó $M = {d}, m = {d-4} \implies S = M + m = {d} + ({d-4}) = {ans}$.'''
        return caudan, dapan, loi_giai

    else:
        # GTLN của hàm phân thức trên đoạn [a; b]
        caudan = fr'''Cho hàm số $y=\dfrac{{x^2+x+4}}{{x+1}}$. Gọi $A =\dfrac{{a}}{{b}}$ là giá trị lớn nhất của hàm số trên đoạn $[3;7]$ với $\dfrac{{a}}{{b}}$ là phân số tối giản. Giá trị của $P=a-b$ bằng bao nhiêu?'''
        dapan = "13"
        loi_giai = fr'''Ta có $y' = \dfrac{{x^2+2x-3}}{{(x+1)^2}} > 0, \forall x \in [3; 7]$ nên hàm số đồng biến trên $[3; 7]$. \\
Giá trị lớn nhất là $A = y(7) = \dfrac{{7^2+7+4}}{{7+1}} = \dfrac{{60}}{{8}} = \dfrac{{15}}{{2}}$. \\
Phân số tối giản $\implies a = 15, b = 2 \implies P = a - b = 15 - 2 = 13$.'''
        return caudan, dapan, loi_giai


# ------------------------------------------------------------------------------
# CÂU 3: MỨC ĐỘ THÔNG HIỂU - TỔNG HỢP CỰC TRỊ, TIỆM CẬN, MIN-MAX
# ------------------------------------------------------------------------------
def CuoiChuong1_SA_Cau3():
    sub_type = random.choice([1, 2, 3, 4])
    
    if sub_type == 1:
        # Đường thẳng đi qua 2 cực trị của đồ thị hàm phân thức
        c = random.choice([2, 4, 6])
        ans = 2 + 2*c
        caudan = fr'''Đồ thị hàm số $y=\dfrac{{x^2 - {c}x + 1}}{{x+1}}$ có hai điểm cực trị. Đường thẳng đi qua hai điểm cực trị đó có phương trình dạng $y=ax+b$. Tính giá trị biểu thức $P = a-2b$.'''
        dapan = f'''{ans}'''
        loi_giai = fr'''Hàm số có dạng $y = \dfrac{{u(x)}}{{v(x)}}$ với $u(x) = x^2 - {c}x + 1$ và $v(x) = x+1$. \\
Đường thẳng đi qua hai điểm cực trị của đồ thị hàm số có phương trình: \\
$y = \dfrac{{u'(x)}}{{v'(x)}} = \dfrac{{2x - {c}}}{{1}} = 2x - {c}$. \\
Suy ra $a = 2, b = -{c} \implies P = a - 2b = 2 - 2(-{c}) = {ans}$.'''
        return caudan, dapan, loi_giai

    elif sub_type == 2:
        # Cực trị hàm phân thức y = (x^2 - x + k)/(x - 1)
        m = random.choice([2, 3])
        k = 1 + m*m
        x1 = 1 + m
        x2 = 1 - m
        ans = 2 * x1 + 3 * x2
        caudan = fr'''Gọi $x_1, x_2$ lần lượt là điểm cực tiểu và điểm cực đại của hàm số $y=\dfrac{{x^2-x+{k}}}{{x-1}}$. Tính $P=2x_1+3x_2$.'''
        dapan = f'''{ans}'''
        loi_giai = fr'''Ta có $y' = \dfrac{{(2x-1)(x-1) - (x^2-x+{k})}}{{(x-1)^2}} = \dfrac{{x^2-2x-{k-1}}}{{(x-1)^2}} = 0 \iff x = {x1}$ hoặc $x = {x2}$. \\
Suy ra $x_1 = {x1}$ (cực tiểu), $x_2 = {x2}$ (cực đại). \\
Vậy $P = 2({x1}) + 3({x2}) = {ans}$.'''
        return caudan, dapan, loi_giai

    elif sub_type == 3:
        # Diện tích tam giác OAB tạo bởi tiệm cận xiên với hai trục Ox, Oy
        caudan = fr'''Biết tiệm cận xiên của đồ thị hàm số $y=f(x)=\dfrac{{4x^2+8x-5}}{{-x+3}}$ cắt trục $Ox, Oy$ lần lượt tại $A$ và $B$. Diện tích tam giác $OAB$ là'''
        dapan = "50"
        loi_giai = fr'''Chia đa thức: $\dfrac{{4x^2+8x-5}}{{-x+3}} = -4x - 20 + \dfrac{{55}}{{-x+3}}$. \\
Đường tiệm cận xiên là $y = -4x - 20$. \\
- Giao điểm với trục $Ox$: Cho $y = 0 \implies x = -5 \implies A(-5; 0) \implies OA = 5$. \\
- Giao điểm với trục $Oy$: Cho $x = 0 \implies y = -20 \implies B(0; -20) \implies OB = 20$. \\
Diện tích tam giác $OAB$ là $S = \dfrac{{1}}{{2}} OA \cdot OB = \dfrac{{1}}{{2}} \cdot 5 \cdot 20 = 50$.'''
        return caudan, dapan, loi_giai

    else:
        # Chu vi mảnh vườn và tiệm cận xiên
        S = random.choice([400, 900, 1600])
        ans = 100
        caudan = fr'''Một mảnh vườn hình chữ nhật có diện tích bằng ${S}\,m^2$. Chiều dài của mảnh vườn là $x$ (m). Biểu thức chu vi của mảnh vườn là $P(x)$ (mét). Biết phương trình đường tiệm cận xiên của đồ thị $P(x)$ là $y=ax+b$. Tính $T=10^a+b$.'''
        dapan = f'''{ans}'''
        loi_giai = fr'''Chu vi mảnh vườn là: $P(x) = 2\left(x + \dfrac{{{S}}}{{x}}\right) = 2x + \dfrac{{{2*S}}}{{x}}$. \\
Khi $x \to +\infty$, $\lim_{{x \to +\infty}} \dfrac{{{2*S}}}{{x}} = 0$ nên tiệm cận xiên là $y = 2x \implies a = 2, b = 0$. \\
Vậy $T = 10^a + b = 10^2 + 0 = {ans}$.'''
        return caudan, dapan, loi_giai


# ------------------------------------------------------------------------------
# CÂU 4: MỨC ĐỘ VẬN DỤNG THẤP - TÂM ĐỐI XỨNG, KHOẢNG CÁCH CỰC TRỊ & TIỆM CẬN
# ------------------------------------------------------------------------------
def CuoiChuong1_SA_Cau4():
    sub_type = random.choice([1, 2, 3, 4])
    
    if sub_type == 1:
        # Tâm đối xứng của đồ thị hàm phân thức
        d = random.choice([1, 2, 3])
        k = random.choice([2, 3, 4])
        p = random.choice([2, 3])
        ans = d + 3*k
        b_coef = k - 2*p*d
        c_coef = p*d*d - k*d + 8
        sign_b = f"{b_coef:+d}".replace("+1", "+").replace("-1", "-")
        sign_c = f"{c_coef:+d}"
        caudan = fr'''Cho đồ thị hàm số $f(x) = \dfrac{{{p}x^2 {sign_b}x {sign_c}}}{{x - {d}}}$ có tâm đối xứng là $I(a; b)$. Giá trị của biểu thức $C = a + 3b$ là bao nhiêu?'''
        dapan = f'''{ans}'''
        loi_giai = fr'''Ta biến đổi: $f(x) = {p}(x - {d}) + {k} + \dfrac{{8}}{{x - {d}}}$. \\
Tiệm cận đứng là $x = {d}$, tiệm cận xiên là $y = {p}(x - {d}) + {k}$. \\
Tâm đối xứng là giao điểm của hai tiệm cận: $I({d}; {k}) \implies a = {d}, b = {k}$. \\
Vậy $C = a + 3b = {d} + 3({k}) = {ans}$.'''
        return caudan, dapan, loi_giai

    elif sub_type == 2:
        # Khoảng cách giữa hai điểm cực trị của hàm phân thức
        caudan = fr'''Đồ thị hàm số $y=\dfrac{{x^2}}{{x+1}}$ có hai điểm cực trị $A$ và $B$. Tính độ dài đoạn thẳng $AB$ \textit{{(kết quả quy tròn đến hàng phần trăm)}}.'''
        dapan = "4,47"
        loi_giai = fr'''Ta có $y' = \dfrac{{x^2 + 2x}}{{(x+1)^2}} = 0 \iff x = 0 \implies y = 0$ hoặc $x = -2 \implies y = -4$. \\
Tọa độ hai điểm cực trị là $A(0; 0)$ và $B(-2; -4)$. \\
Độ dài $AB = \sqrt{{(-2 - 0)^2 + (-4 - 0)^2}} = \sqrt{{20}} = 2\sqrt{{5}} \approx 4{{,}}47$.'''
        return caudan, dapan, loi_giai

    elif sub_type == 3:
        # Giao điểm 2 tiệm cận xiên của hàm chứa căn
        caudan = fr'''Cho hàm số $y = 2x + 1 + \sqrt{{x^2 - 4x + 5}}$. Biết đồ thị hàm số có hai tiệm cận xiên cắt nhau tại $I(a; b)$. Tính $a + b$.'''
        dapan = "7"
        loi_giai = fr'''Khi $x \to +\infty$: TCX là $y = 3x - 1$. \\
Khi $x \to -\infty$: TCX là $y = x + 3$. \\
Giao điểm $I$: $3x - 1 = x + 3 \iff x = 2 \implies y = 5 \implies I(2; 5) \implies a + b = 2 + 5 = 7$.'''
        return caudan, dapan, loi_giai

    else:
        # Tính f(5) từ đồ thị cực trị hàm bậc ba
        caudan = fr'''Cho hàm số $y = f(x) = ax^3 + bx^2 + cx + d$ có đồ thị $(C)$ đi qua gốc tọa độ $O(0;0)$ và có hai điểm cực trị là $(-1; 1)$ và $(1; -1)$. Khi đó giá trị $f(5)$ bằng bao nhiêu?'''
        dapan = "55"
        loi_giai = fr'''Vì đồ thị nhận $O(0;0)$ làm tâm đối xứng nên $f(x)$ là hàm số lẻ: $f(x) = ax^3 + cx$. \\
Đồ thị đi qua $(1; -1) \implies a + c = -1$. \\
$f'(x) = 3ax^2 + c = 0$ tại $x = 1 \implies 3a + c = 0$. \\
Giải hệ phương trình ta được $a = \dfrac{{1}}{{2}}, c = -\dfrac{{3}}{{2}}$. \\
Do đó $f(x) = \dfrac{{1}}{{2}}x^3 - \dfrac{{3}}{{2}}x \implies f(5) = \dfrac{{1}}{{2}}(5^3) - \dfrac{{3}}{{2}}(5) = 55$.'''
        return caudan, dapan, loi_giai


# ------------------------------------------------------------------------------
# CÂU 5: MỨC ĐỘ VẬN DỤNG CAO - TỐI ƯU HÓA HÌNH HỌC & CỰC TRỊ NÂNG CAO
# ------------------------------------------------------------------------------
def CuoiChuong1_SA_Cau5():
    sub_type = random.choice([1, 2, 3, 4])
    
    if sub_type == 1:
        # Diện tích tam giác vuông có cạnh huyền cố định L
        L = random.choice([12, 16, 20, 24])
        ans = (L**2) // 4
        caudan = fr'''Một tam giác vuông có độ dài cạnh huyền là ${L}\text{{ cm}}$. Tam giác vuông đó có thể có diện tích lớn nhất là bao nhiêu $\text{{cm}}^2$?'''
        dapan = f'''{ans}'''
        loi_giai = fr'''Gọi hai cạnh góc vuông của tam giác là $x$ và $y$ ($0 < x, y < {L}$). \\
Theo định lý Pythagore: $x^2 + y^2 = {L}^2$. \\
Diện tích tam giác vuông là $S = \dfrac{{1}}{{2}}xy$. \\
Theo bất đẳng thức AM-GM: $xy \le \dfrac{{x^2 + y^2}}{{2}} = \dfrac{{{L}^2}}{{2}}$. \\
Do đó $S \le \dfrac{{{L}^2}}{{4}} = {ans}\text{{ cm}}^2$. \\
Dấu đẳng thức xảy ra khi tam giác vuông cân ($x = y = \dfrac{{{L}}}{{\sqrt{{2}}}}$).'''
        return caudan, dapan, loi_giai

    elif sub_type == 2:
        # Vị trí trạm cấp nước sạch tối ưu bên bờ sông
        caudan = fr'''Có hai xã $A, B$ cùng ở một bên bờ sông. Khoảng cách từ hai xã đó đến bờ sông lần lượt là $AA' = 500\text{{ m}}, BB' = 600\text{{ m}}$. Người ta đo được $A'B' = 2200\text{{ m}}$. Người ta xây dựng một trạm cung cấp nước sạch nằm bên bờ sông trên đoạn $A'B'$ sao cho tổng khoảng cách từ hai xã đến trạm là nhỏ nhất. Giá trị nhỏ nhất của tổng khoảng cách đó là bao nhiêu mét?'''
        dapan = "2460"
        loi_giai = fr'''Lấy điểm $A''$ đối xứng với $A$ qua đường thẳng bờ sông $A'B'$. \\
Khi đó tổng khoảng cách từ hai xã đến trạm nước $M$ trên bờ sông là: \\
$AM + BM = A''M + BM \ge A''B$. \\
Ta có: $A''B = \sqrt{{(AA' + BB')^2 + A'B'^2}} = \sqrt{{(500 + 600)^2 + 2200^2}} = \sqrt{{1100^2 + 2200^2}} = 1100\sqrt{{5}} \approx 2460\text{{ m}}$.'''
        return caudan, dapan, loi_giai

    elif sub_type == 3:
        # Điểm trên đồ thị gần đường thẳng nhất
        C = random.choice([56, 60, 64])
        ans = 6
        caudan = fr'''Một hồ nước nhân tạo có đường viền bờ hồ được mô hình hóa bởi đồ thị hàm số $y = f(x) = \dfrac{{1}}{{10}}(-x^3 + 9x^2 - 15x + {C})$ với $x \ge 0$. Gần hồ nước có một con đường thẳng chạy dọc theo đường thẳng $d\colon y = -1{{,}}5x + 20$. Người ta xây dựng một bến thuyền trên bờ hồ sao cho khoảng cách từ bến thuyền đến con đường $d$ là ngắn nhất. Hoành độ của vị trí xây bến thuyền bằng bao nhiêu?'''
        dapan = f'''{ans}'''
        loi_giai = fr'''Điểm $M(x; f(x))$ trên bờ hồ có khoảng cách đến đường thẳng $d\colon 1{{,}}5x + y - 20 = 0$ ngắn nhất khi tiếp tuyến tại $M$ song song với đường thẳng $d$. \\
Hệ số góc của đường thẳng $d$ là $k = -1{{,}}5$. \\
Do đó: $f'(x) = -1{{,}}5 \iff \dfrac{{1}}{{10}}(-3x^2 + 18x - 15) = -1{{,}}5 \iff -3x^2 + 18x - 15 = -15 \iff -3x(x - 6) = 0$. \\
Vì bến thuyền ở trên bờ hồ ứng với vị trí thực tế lồi về phía đường thẳng nên chọn nghiệm $x = {ans}$.'''
        return caudan, dapan, loi_giai

    else:
        # Hàm căn thức đồng biến trên khoảng số tự nhiên
        b = random.choice([2, 3, 4])
        ans = b
        caudan = fr'''Biết rằng hàm số $y=\sqrt{{-x^2 + {2*b}x}}$ đồng biến trên khoảng $(a;b)$ với $a,b$ là các số tự nhiên. Tính giá trị của $a+b$.'''
        dapan = f'''{ans}'''
        loi_giai = fr'''Tập xác định: $-x^2 + {2*b}x \ge 0 \iff 0 \le x \le {2*b}$. \\
Đạo hàm: $y' = \dfrac{{{b} - x}}{{\sqrt{{-x^2 + {2*b}x}}}} > 0 \iff 0 < x < {b}$. \\
Vậy hàm số đồng biến trên $(0; {b})$. Do $a, b \in \mathbb{{N}}$ nên $a = 0, b = {b} \implies a + b = {ans}$.'''
        return caudan, dapan, loi_giai


# ------------------------------------------------------------------------------
# CÂU 6: TOÁN THỰC TẾ - VẬN TỐC, LỢI NHUẬN, SẢN LƯỢNG TỐI ƯU
# ------------------------------------------------------------------------------
def CuoiChuong1_SA_Cau6():
    sub_type = random.choice([1, 2, 3, 4])
    
    if sub_type == 1:
        # Vận tốc chuyển động S(t) = -1/3 t^3 + b/2 t^2 - c*t + d
        b = random.choice([4, 6, 8])
        a_val = b // 2
        c = random.choice([2, 3])
        d = random.choice([10, 15, 20])
        ans = a_val + 5
        caudan = fr'''Một chuyển động thẳng xác định bởi phương trình $S(t)=-\dfrac{{1}}{{3}}t^3+\dfrac{{{b}}}{{2}}t^2-{c}t+{d}, \quad t\ge 0,$ trong đó $t$ tính bằng giây và $S$ tính bằng mét. Vận tốc của vật giảm trong khoảng thời gian $(a;+\infty)$. Tính $a+5$?'''
        dapan = f'''{ans}'''
        loi_giai = fr'''Vận tốc chuyển động: $v(t)=S'(t)=-t^2+{b}t-{c}$. \\
Gia tốc: $a(t) = v'(t)=-2t+{b}$. \\
Vận tốc giảm khi gia tốc âm: $v'(t) < 0 \iff -2t + {b} < 0 \iff t > \dfrac{{{b}}}{{2}} = {a_val}$. \\
Vậy vận tốc của vật giảm trên $({a_val};+\infty) \implies a = {a_val}$. \\
Giá trị của $a+5 = {a_val} + 5 = {ans}$.'''
        return caudan, dapan, loi_giai

    elif sub_type == 2:
        # Tối ưu hóa lợi nhuận kinh tế L(x) = B(x) - C(x)
        caudan = fr'''Một công ty sản xuất mỗi ngày $x$ sản phẩm $(1 \leq x \leq 18)$. Chi phí sản xuất $x$ sản phẩm tính bằng nghìn đồng cho bởi hàm $C(x) = x^3 - 3x^2 + 80x + 500$. Công ty bán hết sản phẩm mỗi ngày với giá $320$ nghìn đồng/sản phẩm. Lợi nhuận tối đa (đơn vị triệu đồng) mà công ty có thể đạt được trong một ngày là bao nhiêu?'''
        dapan = "1,2"
        loi_giai = fr'''Doanh thu thu được là $B(x) = 320x$ (nghìn đồng). \\
Hàm lợi nhuận: $L(x) = B(x) - C(x) = -x^3 + 3x^2 + 240x - 500$ (nghìn đồng). \\
Đạo hàm: $L'(x) = -3x^2 + 6x + 240 = -3(x - 10)(x + 8) = 0 \iff x = 10$ (vì $x \in [1; 18]$). \\
Lợi nhuận lớn nhất đạt tại $x = 10$: $L(10) = 1200$ nghìn đồng $= 1{{,}}2$ triệu đồng.'''
        return caudan, dapan, loi_giai

    elif sub_type == 3:
        # Tối ưu sản lượng doanh nghiệp đạt lợi nhuận lớn nhất
        caudan = fr'''Một doanh nghiệp dự định sản xuất không quá $500$ sản phẩm. Doanh thu khi bán $x$ sản phẩm ($1 \le x \le 500$) là $F(x)=x^3-1646x^2+795760x+2132500$ (đồng), chi phí sản xuất bình quân cho một sản phẩm là $G(x)=x+1000+\dfrac{{2132500}}{{x}}$ (đồng). Doanh nghiệp cần sản xuất bao nhiêu sản phẩm để lợi nhuận thu được là lớn nhất?'''
        dapan = "358"
        loi_giai = fr'''Tổng chi phí sản xuất $x$ sản phẩm: $C(x) = x \cdot G(x) = x^2 + 1000x + 2132500$ (đồng). \\
Lợi nhuận: $H(x) = F(x) - C(x) = x^3 - 1647x^2 + 794760x$. \\
Đạo hàm: $H'(x) = 3x^2 - 3294x + 794760 = 0 \iff x = 358$ hoặc $x = 740$. \\
Vì $x \in [1; 500]$ nên $x = 358$. \\
Vậy doanh nghiệp cần sản xuất $358$ sản phẩm để lợi nhuận đạt cực đại.'''
        return caudan, dapan, loi_giai

    else:
        # Giá thành sản phẩm giảm
        caudan = fr'''Trong vòng 3 năm tính từ đầu năm 2024, giá thành $P$ của một loại sản phẩm vào tháng thứ $t$ thay đổi theo công thức $P(t)=\dfrac{{1}}{{3}}t^3-24t^2+495t+900000$ (đồng) với $0\le t \le 36$. Biết giá thành sẽ giảm trong khoảng thời gian $(t_1;t_2)$. Khi đó $9t_1+t_2$ bằng bao nhiêu?'''
        dapan = "168"
        loi_giai = fr'''Đạo hàm: $P'(t) = t^2 - 48t + 495 = 0 \iff t = 15$ hoặc $t = 33$. \\
Bảng biến thiên cho thấy $P'(t) < 0 \iff 15 < t < 33$. \\
Do đó giá thành giảm trong khoảng thời gian $(15; 33) \implies t_1 = 15, t_2 = 33$. \\
Khi đó $9t_1 + t_2 = 9(15) + 33 = 168$.'''
        return caudan, dapan, loi_giai

print("All 6 SA functions defined OK")


# Aliases
CuoiChuong1_SA_NB1 = CuoiChuong1_SA_Cau1
CuoiChuong1_SA_NB2 = CuoiChuong1_SA_Cau2
CuoiChuong1_SA_TH = CuoiChuong1_SA_Cau3
CuoiChuong1_SA_VDT = CuoiChuong1_SA_Cau4
CuoiChuong1_SA_VDC = CuoiChuong1_SA_Cau5
CuoiChuong1_SA_TT = CuoiChuong1_SA_Cau6

def CuoiChuong1_SA_Cau7():
    # New SA 1: Find asymptotes of y = (px - q)/(rx + s)
    r = 2
    p = random.choice([3, 5, 7])
    s = random.choice([4, 6, 8])
    q = random.choice([1, 2, 3])
    
    a = -s // r
    b = p / r
    ans = int(a + 4*b) # always integer because 4b = 2p is integer
    
    caudan = fr'''Cho hàm số $y = \dfrac{{{p}x - {q}}}{{2x + {s}}}$. Đồ thị hàm số có đường tiệm cận đứng và tiệm cận ngang lần lượt là các đường thẳng $x = a$ và $y = b$. Tính giá trị của biểu thức $P = a + 4b$.'''
    dapan = f'''{ans}'''
    loi_giai = fr'''Đồ thị hàm số có: \\
- Tiệm cận đứng: $2x + {s} = 0 \iff x = -\dfrac{{{s}}}{{2}} \implies a = {a}$. \\
- Tiệm cận ngang: $y = \lim_{{x\to\pm\infty}} \dfrac{{{p}x - {q}}}{{2x + {s}}} = \dfrac{{{p}}}{{2}} \implies b = {b}$. \\
Vậy $P = a + 4b = {a} + 4\left({b}\right) = {ans}$.'''
    return caudan, dapan, loi_giai


def CuoiChuong1_SA_Cau8():
    sub_type = random.choice([1, 2])
    
    if sub_type == 1:
        d = random.choice([1, 2, 3])
        k = random.choice([2, 3, 4, 5])
        p = random.choice([2, 3, 5])
        coef_x2 = p
        coef_x = k - 2*p*d
        coef_const = p*d*d - k*d + 8
        
        ans = d + 3*k
        
        def fmt(a, b, c):
            sign_b = "+" if b >= 0 else "-"
            sign_c = "+" if c >= 0 else "-"
            return f"{a}x^2 {sign_b} {abs(b)}x {sign_c} {abs(c)}"
            
        eq = fmt(coef_x2, coef_x, coef_const)
        
        caudan = fr'''Cho đồ thị hàm số $f(x) = \dfrac{{{eq}}}{{x - {d}}}$ có tâm đối xứng là $I(a; b)$. Giá trị của biểu thức $C = a + 3b$ là bao nhiêu?'''
        dapan = f'''{ans}'''
        loi_giai = fr'''Ta viết lại hàm số dưới dạng: \\
$f(x) = {p}(x - {d}) + {k} + \dfrac{{8}}{{x - {d}}}$. \\
Đường tiệm cận xiên là $y = {p}x - {p*d + k}$ và tiệm cận đứng là $x = {d}$. \\
Giao điểm của hai đường tiệm cận chính là tâm đối xứng $I(a;b)$ của đồ thị hàm số: \\
$a = {d}, \quad b = {p}({d}) - {p*d + k} = {k} \implies I({d}; {k})$. \\
Vậy $C = a + 3b = {d} + 3({k}) = {ans}$.'''
        return caudan, dapan, loi_giai
        
    else:
        # New SA 5: Find T = a/b of y = (-x^2 + ax + b)/(x - d) passing through A(0; yA) and symmetry center I(d; yI)
        d = 1
        yA = random.choice([4, 5, 6])
        yI = random.choice([1, 2])
        
        b = -d * yA
        a = yI + 2*d
        ans = round(a / b, 1)
        
        caudan = fr'''Cho hàm số phân thức $y=f(x)=\dfrac{{-x^2+ax+b}}{{x-1}}$ có đồ thị $(C)$. Biết $(C)$ đi qua điểm $A(0;{yA})$ và nhận điểm $I(1;{yI})$ làm tâm đối xứng. Tính $T=\dfrac{{a}}{{b}}$ (làm tròn kết quả đến hàng phần chục).'''
        dapan = f'''{ans}'''
        loi_giai = fr'''Đồ thị đi qua điểm $A(0; {yA}) \implies f(0) = {yA} \implies \dfrac{{b}}{{-1}} = {yA} \implies b = -{yA}$. \\
Thực hiện phép chia tử thức cho mẫu thức: \\
$f(x) = \dfrac{{-x^2+ax+b}}{{x-1}} = -x + (a-1) + \dfrac{{a-1+b}}{{x-1}}$. \\
Suy ra tiệm cận đứng $x=1$, tiệm cận xiên $y=-x + (a-1)$. \\
Giao điểm của hai đường tiệm cận (tâm đối xứng) là $I(1; a-2)$. \\
Theo đề bài, tâm đối xứng là $I(1; {yI}) \implies a - 2 = {yI} \implies a = {yI + 2}$. \\
Vậy $T = \dfrac{{a}}{{b}} = \dfrac{{{yI + 2}}}{{-{yA}}} = {ans}$.'''
        return caudan, dapan, loi_giai


def CuoiChuong1_SA_Cau9():
    # New SA 5: Extreme points probability
    N = random.choice([20, 24, 28, 32])
    num_favorable = (N // 4) + 1
    total_outcomes = N * (2*N + 1)
    
    # Simplify fraction
    from math import gcd
    g = gcd(num_favorable, total_outcomes)
    ans_num = num_favorable // g
    ans_den = total_outcomes // g
    ans = f"{ans_num}/{ans_den}"
    
    caudan = fr'''Gọi $S$ là tập hợp các số nguyên có giá trị tuyệt đối không vượt quá ${N}$. Chọn ngẫu nhiên hai số $a, b$ phân biệt từ tập $S$. Tính xác suất để hai đồ thị $(C_1) : y = x^4 + 2ax^2 + 4b$ và $(C_2) : y = -\dfrac{{1}}{{2}}x^4 + bx^2 - a$ đều có $3$ điểm cực trị, đồng thời chúng đều có điểm cực trị chung.'''
    dapan = f'''{ans}'''
    loi_giai = fr'''Tập $S$ có $2({N}) + 1 = {2*N+1}$ phần tử. Số cách chọn $2$ số phân biệt là $C_{{{2*N+1}}}^2 = {total_outcomes}$. \\
- Để $(C_1)$ có 3 cực trị $\iff a < 0$. \\
- Để $(C_2)$ có 3 cực trị $\iff b > 0$. \\
Các cực trị chung chỉ có thể xảy ra ở $x=0$ (cho ta $a = -4b$) hoặc ở cực trị không chứa $0$ (cho ta $a = -2, b = 2$). \\
- Nếu $a = -4b$: Vì $a \in [-{N};-1]$ nên $b \in [1; {N//4}] \implies$ Có ${N//4}$ cặp. \\
- Nếu $a = -2, b = 2$: Có thêm 1 cặp thỏa mãn. \\
Tổng số cặp thuận lợi là ${N//4} + 1 = {num_favorable}$. \\
Xác suất cần tính là $P = \dfrac{{{num_favorable}}}{{{total_outcomes}}} = {ans}$.'''
    return caudan, dapan, loi_giai


def CuoiChuong1_SA_Cau10():
    # New SA 6: Shortest distance optimization problem
    C = random.choice([56, 60, 64])
    D = random.choice([18, 20, 22])
    
    ans = 6
    
    caudan_template = r'''\immini{Một hồ nước nhân tạo được giới hạn bởi các trục tọa độ và đồ thị của hàm số $y = f(x) = \dfrac{1}{10}(-x^3 + 9x^2 - 15x + __C__). Đơn vị độ dài trên mỗi trục là $100\text{ m}$. Trong công viên có một con đường chạy dọc theo đường thẳng $y = -1,5x + __D__$. Người ta xây dựng trên bờ hồ một bến thuyền sao cho khoảng cách từ bến thuyền đến con đường này là ngắn nhất. Hoành độ của điểm xây dựng bến thuyền bằng bao nhiêu?}{
\begin{tikzpicture}[line join=round, line cap=round, >=stealth, scale=0.6, font=\footnotesize]
  \draw[->] (-0.5,0) -- (13.5,0) node[below] {$x$};
  \draw[->] (0,-0.5) -- (0,10) node[left] {$y$};
  \node[below left] at (0,0) {$O$};
  \node[left] at (0,5) {$5$};
  \node[left] at (0,8) {$8$};
  \node[below] at (5,0) {$5$};
  \node[below] at (6,0) {$6$};
  \node[below] at (8,0) {$8$};
  \node[below] at (12,0) {$12$};
  \node[above right] at (8.5, 5.25) {$y = -1,5x + __D__$};
  
  \begin{scope}
    \clip (0,0) rectangle (12,9);
    \fill[blue!20] (0,0) -- (0,__FILL_Y__) 
      plot[smooth, samples=100, domain=0:8] (\x, {0.1*(-\x*\x*\x + 9*\x*\x - 15*\x + __C__)});
    \draw[thick] plot[smooth, samples=100, domain=0:8] (\x, {0.1*(-\x*\x*\x + 9*\x*\x - 15*\x + __C__)});
  \end{scope}
  \draw[thick] (4,12) -- (12,0);
\end{tikzpicture}
}'''
    caudan = caudan_template.replace("__C__", str(C)).replace("__D__", str(D)).replace("__FILL_Y__", str(round(0.1*C, 2)))
    dapan = f'''{ans}'''
    loi_giai = fr'''Bến thuyền trên bờ hồ có khoảng cách ngắn nhất đến con đường $y = -1,5x + {D}$ khi tiếp tuyến của bờ hồ tại điểm đó song song với con đường. \\
Ta có hệ số góc tiếp tuyến: $f'(x) = \dfrac{{1}}{{10}}(-3x^2 + 18x - 15) = -1,5$. \\
$\iff -3x^2 + 18x - 15 = -15 \iff -3x(x - 6) = 0 \iff x=6$ (nhận) hoặc $x=0$ (loại). \\
Vậy hoành độ điểm cần xây dựng là $x = {ans}$.'''
    return caudan, dapan, loi_giai


def CuoiChuong1_MC_Cau12():
    sub_type = random.choice([1, 2, 3])
    
    if sub_type == 1:
        # y = (x + m)/(x + a) increasing/decreasing
        a = random.choice([-2, -1, 1, 2])
        dir_inc = random.choice([True, False])
        
        dir_str = "đồng biến" if dir_inc else "nghịch biến"
        
        caudan = fr'''Tìm tất cả các giá trị thực của tham số $m$ để hàm số $y = \dfrac{{x+m}}{{x + ({a})}}$ {dir_str} trên từng khoảng xác định.'''
        
        if dir_inc:
            correct = fr'''m < {a}'''
            w1 = fr'''m > {a}'''
            w2 = fr'''m \le {a}'''
            w3 = fr'''m \ge {a}'''
        else:
            correct = fr'''m > {a}'''
            w1 = fr'''m < {a}'''
            w2 = fr'''m \le {a}'''
            w3 = fr'''m \ge {a}'''
            
        choices = [
            fr'''{{\True ${correct}$}}
''',
            fr'''{{${w1}$}}
''',
            fr'''{{${w2}$}}
''',
            fr'''{{${w3}$}}
'''
        ]
        random.shuffle(choices)
        if dir_inc:
            loi_giai = fr'''Ta có $y' = \dfrac{{{a} - m}}{{(x + ({a}))^2}}$. \\
Để hàm số đồng biến trên từng khoảng xác định thì $y' > 0 \iff {a} - m > 0 \iff m < {a}$.'''
        else:
            loi_giai = fr'''Ta có $y' = \dfrac{{{a} - m}}{{(x + ({a}))^2}}$. \\
Để hàm số nghịch biến trên từng khoảng xác định thì $y' < 0 \iff {a} - m < 0 \iff m > {a}$.'''
        return caudan, choices, loi_giai

    elif sub_type == 2:
        # x^3 - 3k^2 x + m = 0 has 3 distinct roots
        k = random.choice([1, 2])
        c_val = 3 * k*k
        ans_lim = 2 * k**3
        
        caudan = fr'''Tìm tất cả các giá trị thực của tham số $m$ để phương trình $x^3 - {c_val}x + m = 0$ có 3 nghiệm phân biệt.'''
        correct = fr'''-{ans_lim} < m < {ans_lim}'''
        w1 = fr'''m \le -{ans_lim} \text{{ hoặc }} m \ge {ans_lim}'''
        w2 = fr'''m < -{ans_lim} \text{{ hoặc }} m > {ans_lim}'''
        w3 = fr'''-\dfrac{{{ans_lim}}}{{2}} < m < \dfrac{{{ans_lim}}}{{2}}'''
        
        choices = [
            fr'''{{\True ${correct}$}}
''',
            fr'''{{${w1}$}}
''',
            fr'''{{${w2}$}}
''',
            fr'''{{${w3}$}}
'''
        ]
        random.shuffle(choices)
        loi_giai = fr'''Ta viết lại phương trình dưới dạng: $x^3 - {c_val}x = -m$. \\
Xét hàm số $f(x) = x^3 - {c_val}x$, ta có: \\
$f'(x) = 3x^2 - {c_val} = 0 \iff x = \pm {k}$. \\
Bảng biến thiên cho thấy cực đại đạt tại $x=-{k}$ với $f(-{k}) = {ans_lim}$, cực tiểu đạt tại $x={k}$ với $f({k}) = -{ans_lim}$. \\
Để phương trình có 3 nghiệm phân biệt thì đường thẳng $y=-m$ phải nằm giữa giá trị cực tiểu và giá trị cực đại: \\
$-{ans_lim} < -m < {ans_lim} \iff -{ans_lim} < m < {ans_lim}$.'''
        return caudan, choices, loi_giai
        
    else:
        # y = x^4 - 2mx^2 + 1 has exactly 3 extrema points
        three_extrema = random.choice([True, False])
        caudan = fr'''Tìm tất cả các giá trị thực của tham số $m$ để hàm số $y = x^4 - 2mx^2 + 1$ có { 'đúng 3 điểm cực trị' if three_extrema else 'đúng 1 điểm cực trị' }.'''
        
        if three_extrema:
            correct = fr'''m > 0'''
            w1 = fr'''m < 0'''
            w2 = fr'''m = 0'''
            w3 = fr'''m \ne 0'''
        else:
            correct = fr'''m \le 0'''
            w1 = fr'''m < 0'''
            w2 = fr'''m > 0'''
            w3 = fr'''m \ge 0'''
            
        choices = [
            fr'''{{\True ${correct}$}}
''',
            fr'''{{${w1}$}}
''',
            fr'''{{${w2}$}}
''',
            fr'''{{${w3}$}}
'''
        ]
        random.shuffle(choices)
        if three_extrema:
            loi_giai = fr'''Ta có $y' = 4x^3 - 4mx = 4x(x^2 - m)$. \\
Hàm số có đúng 3 điểm cực trị khi và chỉ khi phương trình $y' = 0$ có 3 nghiệm phân biệt và đổi dấu qua các nghiệm đó: \\
$\iff x^2 - m = 0$ có 2 nghiệm phân biệt khác $0 \iff m > 0$.'''
        else:
            loi_giai = fr'''Ta có $y' = 4x^3 - 4mx = 4x(x^2 - m)$. \\
Hàm số trùng phương có đúng 1 điểm cực trị khi và chỉ khi phương trình $y' = 0$ có đúng 1 nghiệm đơn $x=0$: \\
$\iff m \le 0$.'''
        return caudan, choices, loi_giai


# --- CHƯƠNG II: VECTƠ VÀ TỌA ĐỘ TRONG KHÔNG GIAN ---

def CuoiChuong2_MC_Cau1():
    # Prism vector representation
    sub = random.choice([1, 2])
    if sub == 1:
        # AG'
        caudan = fr'''Cho hình lăng trụ $ABC.A'B'C'$. Đặt $\overrightarrow{{AA'}} = \vec{{a}}$, $\overrightarrow{{AB}} = \vec{{b}}$, $\overrightarrow{{AC}} = \vec{{c}}$. Gọi $G'$ là trọng tâm của tam giác $A'B'C'$. Biểu diễn vectơ $\overrightarrow{{AG'}}$ qua các vectơ $\vec{{a}}, \vec{{b}}, \vec{{c}}$ ta được:'''
        choices = [
            fr'''{{\True $\dfrac{{1}}{{3}}(3\vec{{a}} + \vec{{b}} + \vec{{c}})$}}
''',
            fr'''{{$\dfrac{{1}}{{3}}(\vec{{a}} + 3\vec{{b}} + \vec{{c}})$}}
''',
            fr'''{{$\dfrac{{1}}{{3}}(\vec{{a}} + \vec{{b}} + 3\vec{{c}})$}}
''',
            fr'''{{$\dfrac{{1}}{{3}}(\vec{{a}} + \vec{{b}} + \vec{{c}})$}}
'''
        ]
        loi_giai = fr'''Ta có: $\overrightarrow{{AG'}} = \dfrac{{1}}{{3}}(\overrightarrow{{AA'}} + \overrightarrow{{AB'}} + \overrightarrow{{AC'}})$. \\
Mà $\overrightarrow{{AB'}} = \vec{{a}} + \vec{{b}}$ và $\overrightarrow{{AC'}} = \vec{{a}} + \vec{{c}}$. \\
Do đó: $\overrightarrow{{AG'}} = \dfrac{{1}}{{3}}(\vec{{a}} + \vec{{a}} + \vec{{b}} + \vec{{a}} + \vec{{c}}) = \dfrac{{1}}{{3}}(3\vec{{a}} + \vec{{b}} + \vec{{c}})$.'''
    else:
        # BG'
        caudan = fr'''Cho hình lăng trụ $ABC.A'B'C'$. Đặt $\overrightarrow{{AA'}} = \vec{{a}}$, $\overrightarrow{{AB}} = \vec{{b}}$, $\overrightarrow{{AC}} = \vec{{c}}$. Gọi $G'$ là trọng tâm của tam giác $A'B'C'$. Biểu diễn vectơ $\overrightarrow{{BG'}}$ qua các vectơ $\vec{{a}}, \vec{{b}}, \vec{{c}}$ ta được:'''
        choices = [
            fr'''{{\True $\dfrac{{1}}{{3}}(3\vec{{a}} - 2\vec{{b}} + \vec{{c}})$}}
''',
            fr'''{{$\dfrac{{1}}{{3}}(3\vec{{a}} + \vec{{b}} - 2\vec{{c}})$}}
''',
            fr'''{{$\dfrac{{1}}{{3}}(3\vec{{a}} + \vec{{b}} + \vec{{c}})$}}
''',
            fr'''{{$\dfrac{{1}}{{3}}(\vec{{a}} - 2\vec{{b}} + \vec{{c}})$}}
'''
        ]
        loi_giai = fr'''Ta có: $\overrightarrow{{BG'}} = \overrightarrow{{BA}} + \overrightarrow{{AG'}} = -\vec{{b}} + \dfrac{{1}}{{3}}(3\vec{{a}} + \vec{{b}} + \vec{{c}}) = \dfrac{{1}}{{3}}(3\vec{{a}} - 2\vec{{b}} + \vec{{c}})$.'''
    random.shuffle(choices)
    return caudan, choices, loi_giai


def CuoiChuong2_MC_Cau2():
    # Vector length
    y1 = random.choice([2, 3])
    z1 = random.choice([-4, -3])
    x2 = random.choice([3, 4])
    y2 = random.choice([1, 2])
    z2 = random.choice([1, 2])
    
    # a = (0, y1, z1), b = (x2, y2, z2)
    # v = 2a - b = (-x2, 2*y1 - y2, 2*z1 - z2)
    X = -x2
    Y = 2*y1 - y2
    Z = 2*z1 - z2
    sq_len = X*X + Y*Y + Z*Z
    ans = fr'''\sqrt{{{sq_len}}}'''
    
    caudan = fr'''Trong không gian $Oxyz$, cho $\vec{{a}} = {y1}\vec{{j}} {z1}\vec{{k}}$ và $\vec{{b}} = {x2}\vec{{i}} + {y2}\vec{{j}} + {z2}\vec{{k}}$. Tính độ dài của vectơ $\vec{{v}} = 2\vec{{a}} - \vec{{b}}$.'''
    
    choices = [
        fr'''{{\True ${ans}$}}
''',
        fr'''{{$\sqrt{{{sq_len - 8}}}$}}
''',
        fr'''{{$\sqrt{{{sq_len + 12}}}$}}
''',
        fr'''{{$\sqrt{{{sq_len - 15}}}$}}
'''
    ]
    random.shuffle(choices)
    loi_giai = fr'''Ta có tọa độ các vectơ là: \\
$\vec{{a}} = (0; {y1}; {z1})$, $\vec{{b}} = ({x2}; {y2}; {z2})$. \\
Suy ra $\vec{{v}} = 2\vec{{a}} - \vec{{b}} = (2\cdot 0 - {x2}; 2\cdot {y1} - {y2}; 2\cdot {z1} - {z2}) = ({X}; {Y}; {Z})$. \\
Độ dài của $\vec{{v}}$ là: $|\vec{{v}}| = \sqrt{{({X})^2 + {Y}^2 + ({Z})^2}} = {ans}$.'''
    return caudan, choices, loi_giai


def CuoiChuong2_MC_Cau3():
    # Centroid of tetrahedron
    # G(xg, yg, zg)
    xg = random.choice([1, 2, 3])
    yg = random.choice([-2, -1, 1])
    zg = random.choice([-2, -1, 1])
    
    # Randomly choose A, B, C coordinates
    xA = random.randint(-2, 4)
    yA = random.randint(-4, 2)
    zA = random.randint(-3, 3)
    
    xB = random.randint(-2, 4)
    yB = random.randint(-4, 2)
    zB = random.randint(-3, 3)
    
    xC = random.randint(-2, 4)
    yC = random.randint(-4, 2)
    zC = random.randint(-3, 3)
    
    # D is chosen so that G is centroid: D = 4*G - A - B - C
    xD = 4*xg - xA - xB - xC
    yD = 4*yg - yA - yB - yC
    zD = 4*zg - zA - zB - zC
    
    caudan = fr'''Trong không gian với hệ tọa độ $Oxyz$, cho tứ diện $ABCD$ với $A({xA}; {yA}; {zA})$, $B({xB}; {yB}; {zB})$, $C({xC}; {yC}; {zC})$ và $D({xD}; {yD}; {zD})$. Điểm $G$ thỏa mãn $\overrightarrow{{GA}} + \overrightarrow{{GB}} + \overrightarrow{{GC}} + \overrightarrow{{GD}} = \vec{{0}}$ có tọa độ là:'''
    correct = fr'''G({xg}; {yg}; {zg})'''
    wrong1 = fr'''G({xg+1}; {yg}; {zg-1})'''
    wrong2 = fr'''G(0; {yg}; {zg})'''
    wrong3 = fr'''G({4*xg}; {4*yg}; {4*zg})'''
    
    choices = [
        fr'''{{\True ${correct}$}}
''',
        fr'''{{${wrong1}$}}
''',
        fr'''{{${wrong2}$}}
''',
        fr'''{{${wrong3}$}}
'''
    ]
    random.shuffle(choices)
    loi_giai = fr'''Điểm $G$ thỏa mãn $\overrightarrow{{GA}} + \overrightarrow{{GB}} + \overrightarrow{{GC}} + \overrightarrow{{GD}} = \vec{{0}}$ chính là trọng tâm của tứ diện $ABCD$. Tọa độ của $G$ là: \\
$x_G = \dfrac{{{xA} + {xB} + {xC} + {xD}}}{{4}} = {xg}$ \\
$y_G = \dfrac{{{yA} + {yB} + {yC} + {yD}}}{{4}} = {yg}$ \\
$z_G = \dfrac{{{zA} + {zB} + {zC} + {zD}}}{{4}} = {zg}$ \\
Vậy $G({xg}; {yg}; {zg})$.'''
    return caudan, choices, loi_giai


def CuoiChuong2_MC_Cau4():
    # Vector AB coordinates between two points
    x1 = random.randint(-3, 3)
    y1 = random.randint(-3, 3)
    z1 = random.randint(-3, 3)
    
    dx = random.choice([-3, -2, 1, 2, 3])
    dy = random.choice([-2, -1, 1, 2, 3])
    dz = random.choice([-6, -5, -4, 4, 5, 6])
    
    x2 = x1 + dx
    y2 = y1 + dy
    z2 = z1 + dz
    
    caudan = fr'''Trong không gian $Oxyz$, cho hai điểm $A({x1}; {y1}; {z1})$ và $B({x2}; {y2}; {z2})$. Vectơ $\overrightarrow{{AB}}$ có tọa độ là:'''
    correct = fr'''({dx}; {dy}; {dz})'''
    wrong1 = fr'''({x1+x2}; {y1+y2}; {z1+z2})'''
    wrong2 = fr'''({-dx}; {-dy}; {dz})'''
    wrong3 = fr'''({dx}; {-dy}; {-dz})'''
    
    choices = [
        fr'''{{\True ${correct}$}}
''',
        fr'''{{${wrong1}$}}
''',
        fr'''{{${wrong2}$}}
''',
        fr'''{{${wrong3}$}}
'''
    ]
    random.shuffle(choices)
    loi_giai = fr'''Tọa độ vectơ $\overrightarrow{{AB}} = (x_B - x_A; y_B - y_A; z_B - z_A) = ({x2} - ({x1}); {y2} - ({y1}); {z2} - ({z1})) = ({dx}; {dy}; {dz})$.'''
    return caudan, choices, loi_giai


# ==============================================================================
# BÀI TẬP CUỐI CHƯƠNG II - TRẢ LỜI NGẮN (6 CÂU GÔM GỌN THEO MỨC ĐỘ)
# ==============================================================================

# ------------------------------------------------------------------------------
# CÂU 1: MỨC ĐỘ NHẬN BIẾT (DẠNG 1) - TOẠ ĐỘ ĐIỂM VÀ TOẠ ĐỘ VECTƠ CƠ BẢN
# ------------------------------------------------------------------------------
def CuoiChuong2_SA_Cau1():
    sub_type = random.choice([1, 2, 3, 4])
    
    if sub_type == 1:
        # Tọa độ vectơ tổng u = 2a - 3b, tính x + y + z
        x1, y1, z1 = random.randint(-3, 3), random.randint(-3, 3), random.randint(-3, 3)
        x2, y2, z2 = random.randint(-3, 3), random.randint(-3, 3), random.randint(-3, 3)
        k1, k2 = 2, -3
        xu = k1 * x1 + k2 * x2
        yu = k1 * y1 + k2 * y2
        zu = k1 * z1 + k2 * z2
        ans = xu + yu + zu
        caudan = fr'''Trong không gian $Oxyz$, cho hai vectơ $\vec{{a}} = ({x1}; {y1}; {z1})$ và $\vec{{b}} = ({x2}; {y2}; {z2})$. Vectơ $\vec{{u}} = 2\vec{{a}} - 3\vec{{b}}$ có tọa độ là $(x; y; z)$. Tính giá trị của biểu thức $T = x + y + z$.'''
        dapan = f'''{ans}'''
        loi_giai = fr'''Ta có: \\
$2\vec{{a}} = ({2*x1}; {2*y1}; {2*z1})$, \\
$-3\vec{{b}} = ({-3*x2}; {-3*y2}; {-3*z2})$. \\
Suy ra $\vec{{u}} = 2\vec{{a}} - 3\vec{{b}} = ({xu}; {yu}; {zu}) \implies x = {xu}, y = {yu}, z = {zu}$. \\
Vậy $T = x + y + z = {xu} + ({yu}) + ({zu}) = {ans}$.'''
        return caudan, dapan, loi_giai

    elif sub_type == 2:
        # Trung điểm của đoạn thẳng AB, tính xM + yM + zM
        xA = random.choice([-4, -2, 0, 2, 4])
        yA = random.choice([-3, -1, 1, 3])
        zA = random.choice([-2, 0, 2, 4])
        xB = xA + 2 * random.choice([1, 2, 3, -1, -2])
        yB = yA + 2 * random.choice([1, 2, -1, -2])
        zB = zA + 2 * random.choice([1, 2, -1, -2])
        xM = (xA + xB) // 2
        yM = (yA + yB) // 2
        zM = (zA + zB) // 2
        ans = xM + yM + zM
        caudan = fr'''Trong không gian $Oxyz$, cho hai điểm $A({xA}; {yA}; {zA})$ và $B({xB}; {yB}; {zB})$. Gọi $M(x; y; z)$ là trung điểm của đoạn thẳng $AB$. Tính giá trị của $x + y + z$.'''
        dapan = f'''{ans}'''
        loi_giai = fr'''Tọa độ trung điểm $M$ của đoạn thẳng $AB$ là: \\
$x = \dfrac{{{xA} + ({xB})}}{{2}} = {xM}$, \\
$y = \dfrac{{{yA} + ({yB})}}{{2}} = {yM}$, \\
$z = \dfrac{{{zA} + ({zB})}}{{2}} = {zM}$. \\
Suy ra $M({xM}; {yM}; {zM})$. \\
Vậy $x + y + z = {xM} + ({yM}) + ({zM}) = {ans}$.'''
        return caudan, dapan, loi_giai

    elif sub_type == 3:
        # Trọng tâm tam giác ABC
        xA = random.choice([-3, 0, 3])
        yA = random.choice([-2, 1, 4])
        zA = random.choice([1, 4])
        xB = random.choice([-1, 2])
        yB = random.choice([-3, 0, 3])
        zB = random.choice([-2, 1])
        # Make sum divisible by 3
        rem_x = (xA + xB) % 3
        xC = (3 - rem_x) if rem_x != 0 else 0
        rem_y = (yA + yB) % 3
        yC = (3 - rem_y) if rem_y != 0 else 0
        rem_z = (zA + zB) % 3
        zC = (3 - rem_z) if rem_z != 0 else 0
        xG = (xA + xB + xC) // 3
        yG = (yA + yB + yC) // 3
        zG = (zA + zB + zC) // 3
        ans = xG + yG + zG
        caudan = fr'''Trong không gian $Oxyz$, cho tam giác $ABC$ có $A({xA}; {yA}; {zA}), B({xB}; {yB}; {zB}), C({xC}; {yC}; {zC})$. Gọi $G(x_G; y_G; z_G)$ là trọng tâm tam giác $ABC$. Tính $T = x_G + y_G + z_G$.'''
        dapan = f'''{ans}'''
        loi_giai = fr'''Tọa độ trọng tâm $G$ của tam giác $ABC$ thỏa mãn: \\
$x_G = \dfrac{{{xA} + ({xB}) + ({xC})}}{{3}} = {xG}$, \\
$y_G = \dfrac{{{yA} + ({yB}) + ({yC})}}{{3}} = {yG}$, \\
$z_G = \dfrac{{{zA} + ({zB}) + ({zC})}}{{3}} = {zG}$. \\
Vậy $T = x_G + y_G + z_G = {xG} + ({yG}) + ({zG}) = {ans}$.'''
        return caudan, dapan, loi_giai

    else:
        # Tọa độ hình chiếu lên mặt phẳng tọa độ
        x0, y0, z0 = random.choice([-5, -3, 2, 4, 6]), random.choice([-4, -2, 3, 5]), random.choice([-6, -2, 1, 3, 7])
        plane = random.choice(["Oxy", "Oyz", "Oxz"])
        if plane == "Oxy":
            xP, yP, zP = x0, y0, 0
            plane_str = "(Oxy)"
        elif plane == "Oyz":
            xP, yP, zP = 0, y0, z0
            plane_str = "(Oyz)"
        else:
            xP, yP, zP = x0, 0, z0
            plane_str = "(Oxz)"
        ans = xP + yP + zP
        caudan = fr'''Trong không gian $Oxyz$, cho điểm $M({x0}; {y0}; {z0})$. Gọi $M'(x; y; z)$ là hình chiếu vuông góc của điểm $M$ lên mặt phẳng tọa độ ${plane_str}$. Tính $x + y + z$.'''
        dapan = f'''{ans}'''
        loi_giai = fr'''Hình chiếu vuông góc của điểm $M({x0}; {y0}; {z0})$ lên mặt phẳng ${plane_str}$ là điểm $M'({xP}; {yP}; {zP})$. \\
Vậy $x + y + z = {xP} + ({yP}) + ({zP}) = {ans}$.'''
        return caudan, dapan, loi_giai


# ------------------------------------------------------------------------------
# CÂU 2: MỨC ĐỘ NHẬN BIẾT (DẠNG 2) - ĐỘ DÀI VECTƠ & TÍCH VÔ HƯỚNG CƠ BẢN
# ------------------------------------------------------------------------------
def CuoiChuong2_SA_Cau2():
    sub_type = random.choice([1, 2, 3, 4])
    
    if sub_type == 1:
        # Tích vô hướng a . b
        x1, y1, z1 = random.randint(-3, 3), random.randint(-3, 3), random.randint(-3, 3)
        x2, y2, z2 = random.randint(-3, 3), random.randint(-3, 3), random.randint(-3, 3)
        ans = x1*x2 + y1*y2 + z1*z2
        caudan = fr'''Trong không gian $Oxyz$, cho hai vectơ $\vec{{a}} = ({x1}; {y1}; {z1})$ và $\vec{{b}} = ({x2}; {y2}; {z2})$. Tính tích vô hướng $\vec{{a}} \cdot \vec{{b}}$.'''
        dapan = f'''{ans}'''
        loi_giai = fr'''Tích vô hướng của hai vectơ là: \\
$\vec{{a}} \cdot \vec{{b}} = x_1 x_2 + y_1 y_2 + z_1 z_2 = ({x1})({x2}) + ({y1})({y2}) + ({z1})({z2}) = {ans}$.'''
        return caudan, dapan, loi_giai

    elif sub_type == 2:
        # Độ dài đoạn thẳng AB đẹp nguyên
        # dx^2 + dy^2 + dz^2 = L^2 (e.g. 1^2 + 2^2 + 2^2 = 9 -> 3; 2^2 + 3^2 + 6^2 = 49 -> 7; 1^2 + 4^2 + 8^2 = 81 -> 9)
        triplet = random.choice([(1, 2, 2, 3), (2, 3, 6, 7), (1, 4, 8, 9), (4, 4, 7, 9)])
        dx, dy, dz, L = triplet
        dx = dx * random.choice([1, -1])
        dy = dy * random.choice([1, -1])
        dz = dz * random.choice([1, -1])
        xA = random.randint(-2, 2)
        yA = random.randint(-2, 2)
        zA = random.randint(-2, 2)
        xB = xA + dx
        yB = yA + dy
        zB = zA + dz
        ans = L
        caudan = fr'''Trong không gian $Oxyz$, cho hai điểm $A({xA}; {yA}; {zA})$ và $B({xB}; {yB}; {zB})$. Tính khoảng cách giữa hai điểm $A$ và $B$.'''
        dapan = f'''{ans}'''
        loi_giai = fr'''Khoảng cách giữa hai điểm $A$ và $B$ là độ dài đoạn thẳng $AB$: \\
$AB = \sqrt{{({xB} - ({xA}))^2 + ({yB} - ({yA}))^2 + ({zB} - ({zA}))^2}} = \sqrt{{{dx}^2 + ({dy})^2 + ({dz})^2}} = \sqrt{{{L*L}}} = {ans}$.'''
        return caudan, dapan, loi_giai

    elif sub_type == 3:
        # Tìm m để hai vectơ vuông góc
        x1 = random.choice([1, 2, 3])
        z1 = random.choice([2, -2, 3])
        x2 = random.choice([2, 4, -2])
        z2 = random.choice([1, 2, -1])
        # dot = x1*x2 + m*y2 + z1*z2 = 0
        y2 = random.choice([1, 2, -1, -2])
        # x1*x2 + z1*z2 + m*y2 = 0 => m*y2 = -(x1*x2 + z1*z2)
        # Ensure divisible
        val = - (x1*x2 + z1*z2)
        if val % y2 != 0:
            val = val - (val % y2)
            z2 = (val - x1*x2) // z1
        m_ans = - (x1*x2 + z1*z2) // y2
        caudan = fr'''Trong không gian $Oxyz$, cho hai vectơ $\vec{{u}} = ({x1}; m; {z1})$ và $\vec{{v}} = ({x2}; {y2}; {z2})$. Tìm giá trị của $m$ để hai vectơ $\vec{{u}}$ và $\vec{{v}}$ vuông góc với nhau.'''
        dapan = f'''{m_ans}'''
        loi_giai = fr'''Hai vectơ $\vec{{u}}$ và $\vec{{v}}$ vuông góc với nhau khi và chỉ khi: \\
$\vec{{u}} \cdot \vec{{v}} = 0 \iff ({x1})({x2}) + m({y2}) + ({z1})({z2}) = 0$ \\
$\iff {y2}m {x1*x2 + z1*z2:+d} = 0 \iff m = {m_ans}$.'''
        return caudan, dapan, loi_giai

    else:
        # Độ dài vectơ u = (x; y; z)
        dx, dy, dz, L = random.choice([(1, 2, 2, 3), (2, 3, 6, 7), (1, 4, 8, 9), (3, 4, 12, 13)])
        dx = dx * random.choice([1, -1])
        dy = dy * random.choice([1, -1])
        dz = dz * random.choice([1, -1])
        ans = L
        caudan = fr'''Trong không gian $Oxyz$, cho vectơ $\vec{{u}} = ({dx}; {dy}; {dz})$. Tính độ dài của vectơ $\vec{{u}}$.'''
        dapan = f'''{ans}'''
        loi_giai = fr'''Độ dài của vectơ $\vec{{u}}$ là: \\
$|\vec{{u}}| = \sqrt{{({dx})^2 + ({dy})^2 + ({dz})^2}} = \sqrt{{{L*L}}} = {ans}$.'''
        return caudan, dapan, loi_giai


# ------------------------------------------------------------------------------
# CÂU 3: MỨC ĐỘ THÔNG HIỂU - GÓC GIỮA HAI VECTƠ & PHÂN TÍCH VECTƠ HÌNH HỌC
# ------------------------------------------------------------------------------
def CuoiChuong2_SA_Cau3():
    sub_type = random.choice([1, 2, 3])
    
    if sub_type == 1:
        # Góc giữa hai vectơ từ điều kiện trực giao
        ans = 90
        caudan = fr'''Cho hai vectơ $\vec{{a}}, \vec{{b}}$ sao cho $|\vec{{a}}| = \sqrt{{2}}$, $|\vec{{b}}| = 2$ và hai vectơ $\vec{{x}} = \vec{{a}} + \vec{{b}}$, $\vec{{y}} = 2\vec{{a}} - \vec{{b}}$ vuông góc với nhau. Tính góc giữa hai vectơ $\vec{{a}}$ và $\vec{{b}}$ (đơn vị độ).'''
        dapan = f'''{ans}'''
        loi_giai = fr'''Hai vectơ $\vec{{x}}$ và $\vec{{y}}$ vuông góc với nhau nên: \\
$\vec{{x}} \cdot \vec{{y}} = 0 \iff (\vec{{a}} + \vec{{b}}) \cdot (2\vec{{a}} - \vec{{b}}) = 0$ \\
$\iff 2|\vec{{a}}|^2 + \vec{{a}}\cdot\vec{{b}} - |\vec{{b}}|^2 = 0$. \\
Thay $|\vec{{a}}| = \sqrt{{2}}$ và $|\vec{{b}}| = 2$ ta được: \\
$2(2) + \vec{{a}}\cdot\vec{{b}} - 4 = 0 \iff \vec{{a}}\cdot\vec{{b}} = 0$. \\
Vì $\vec{{a}}\cdot\vec{{b}} = |\vec{{a}}|\cdot|\vec{{b}}|\cdot\cos(\vec{{a}}, \vec{{b}}) = 0 \implies \cos(\vec{{a}}, \vec{{b}}) = 0 \implies (\vec{{a}}, \vec{{b}}) = 90^\circ$. \\
Vậy góc giữa hai vectơ là ${ans}^\circ$.'''
        return caudan, dapan, loi_giai

    elif sub_type == 2:
        # Góc giữa hai vectơ toạ độ đặc biệt (e.g. 60 deg, 120 deg, 45 deg)
        # u = (1; 1; 0), v = (1; 0; 0) -> cos = 1/sqrt(2) -> 45 deg
        # u = (1; 1; 0), v = (0; 1; 1) -> cos = 1/2 -> 60 deg
        # u = (1; -1; 0), v = (0; 1; 1) -> cos = -1/2 -> 120 deg
        choice = random.choice([
            ((1, 1, 0), (0, 1, 1), 60, r"\frac{1}{2}"),
            ((1, -1, 0), (0, 1, 1), 120, r"-\frac{1}{2}"),
            ((1, 1, 0), (1, 0, 0), 45, r"\frac{\sqrt{2}}{2}"),
            ((1, 0, 1), (0, 1, 0), 90, r"0")
        ])
        u, v, deg, cos_str = choice
        caudan = fr'''Trong không gian $Oxyz$, cho hai vectơ $\vec{{u}} = ({u[0]}; {u[1]}; {u[2]})$ và $\vec{{v}} = ({v[0]}; {v[1]}; {v[2]})$. Tính góc giữa hai vectơ $\vec{{u}}$ và $\vec{{v}}$ (đơn vị độ).'''
        dapan = f'''{deg}'''
        u_dot_v = u[0]*v[0] + u[1]*v[1] + u[2]*v[2]
        len_u_sq = u[0]**2 + u[1]**2 + u[2]**2
        len_v_sq = v[0]**2 + v[1]**2 + v[2]**2
        loi_giai = (
            r"Áp dụng công thức tính côsin của góc giữa hai vectơ: \\" + "\n"
            r"$\cos(\vec{u}, \vec{v}) = \dfrac{\vec{u} \cdot \vec{v}}{|\vec{u}| \cdot |\vec{v}|} = \dfrac{" + str(u_dot_v) + r"}{\sqrt{" + str(len_u_sq) + r"} \cdot \sqrt{" + str(len_v_sq) + r"}} = " + cos_str + r"$. \\" + "\n"
            r"Suy ra $(\vec{u}, \vec{v}) = " + str(deg) + r"^\circ$."
        )
        return caudan, dapan, loi_giai

    else:
        # Phân tích vectơ trong hình lăng trụ
        cfgs = [
            {"mid": "P", "edge": "BB'", "u": 1, "v": -5, "w": 2, "a": 1, "b": 1, "c_val": 0.5, "ans": -3},
            {"mid": "P", "edge": "BB'", "u": 2, "v": 3,  "w": 4, "a": 1, "b": 1, "c_val": 0.5, "ans": 7},
            {"mid": "Q", "edge": "CC'", "u": 3, "v": -2, "w": 6, "a": 1, "b": 0, "c_val": 0.5, "ans": 6},
            {"mid": "P", "edge": "BB'", "u": 4, "v": -1, "w": 2, "a": 1, "b": 1, "c_val": 0.5, "ans": 4},
        ]
        cfg = random.choice(cfgs)
        mid = cfg["mid"]
        edge = cfg["edge"]
        u, v, w = cfg["u"], cfg["v"], cfg["w"]
        ans = cfg["ans"]
        
        u_str = f"{u}a" if u != 1 else "a"
        v_str = f"+ {v}b" if v > 0 else (f"- {abs(v)}b" if v < 0 else "")
        w_str = f"+ {w}c" if w > 0 else (f"- {abs(w)}c" if w < 0 else "")
        T_expr = f"{u_str} {v_str} {w_str}".strip()

        caudan = fr'''Cho hình lăng trụ $ABC.A'B'C'$, điểm ${mid}$ là trung điểm của cạnh bên ${edge}$. Biết rằng $\vec{{A{mid}}} = a \cdot \vec{{AC}} + b \cdot \vec{{CB}} + c \cdot \vec{{AA'}}$. Tính giá trị biểu thức $T = {T_expr}$.'''
        dapan = str(ans)
        loi_giai = fr'''Ta có: $\vec{{A{mid}}} = \vec{{A{edge[0]}}} + \dfrac{{1}}{{2}}\vec{{{edge}}} = {cfg["a"]}\vec{{AC}} + {cfg["b"]}\vec{{CB}} + \dfrac{{1}}{{2}}\vec{{AA'}}$. \\
Suy ra $a = {cfg["a"]}, b = {cfg["b"]}, c = \dfrac{{1}}{{2}}$. \\
Do đó $T = {ans}$.'''
        return caudan, dapan, loi_giai


# ------------------------------------------------------------------------------
# CÂU 4: MỨC ĐỘ VẬN DỤNG THẤP - TOẠ ĐỘ HÌNH HỌC KHÔNG GIAN
# ------------------------------------------------------------------------------
def CuoiChuong2_SA_Cau4():
    sub_type = random.choice([1, 2, 3])
    
    if sub_type == 1:
        # Tọa độ đỉnh thứ tư của hình bình hành ABCD (D = A + C - B)
        xA = random.randint(-3, 3)
        yA = random.randint(-3, 3)
        zA = random.randint(-3, 3)
        xB = random.randint(-3, 3)
        yB = random.randint(-3, 3)
        zB = random.randint(-3, 3)
        xC = random.randint(-3, 3)
        yC = random.randint(-3, 3)
        zC = random.randint(-3, 3)
        xD = xA + xC - xB
        yD = yA + yC - yB
        zD = zA + zC - zB
        ans = xD + yD + zD
        caudan = fr'''Trong không gian $Oxyz$, cho ba điểm $A({xA}; {yA}; {zA})$, $B({xB}; {yB}; {zB})$ và $C({xC}; {yC}; {zC})$. Biết điểm $D(a; b; c)$ sao cho tứ giác $ABCD$ là hình bình hành. Tính giá trị biểu thức $S = a + b + c$.'''
        dapan = f'''{ans}'''
        loi_giai = fr'''Tứ giác $ABCD$ là hình bình hành khi và chỉ khi: \\
$\overrightarrow{{AB}} = \overrightarrow{{DC}} \iff (x_B - x_A; y_B - y_A; z_B - z_A) = (x_C - a; y_C - b; z_C - c)$ \\
$\iff \begin{{cases}} a = x_A + x_C - x_B = {xA} + ({xC}) - ({xB}) = {xD} \\ b = y_A + y_C - y_B = {yA} + ({yC}) - ({yB}) = {yD} \\ c = z_A + z_C - z_B = {zA} + ({zC}) - ({zB}) = {zD} \end{{cases}} \implies D({xD}; {yD}; {zD})$. \\
Vậy $S = a + b + c = {xD} + ({yD}) + ({zD}) = {ans}$.'''
        return caudan, dapan, loi_giai

    elif sub_type == 2:
        # Hình hộp chữ nhật gắn hệ trục tọa độ Oxyz, trọng tâm tam giác A'BD
        boxes = [
            {"a": 10, "b": 16, "c": 8,  "m": 1, "n": 2, "p": 3, "T": 22},
            {"a": 12, "b": 15, "c": 9,  "m": 1, "n": 1, "p": 1, "T": 12},
            {"a": 9,  "b": 12, "c": 6,  "m": 2, "n": 1, "p": 3, "T": 16},
            {"a": 15, "b": 9,  "c": 12, "m": 1, "n": 2, "p": 1, "T": 15},
            {"a": 6,  "b": 12, "c": 15, "m": 3, "n": 1, "p": 2, "T": 20},
        ]
        b = random.choice(boxes)
        a, bb, c = b["a"], b["b"], b["c"]
        m, n, p = b["m"], b["n"], b["p"]
        ans = b["T"]
        m_str = f"{m}x" if m != 1 else "x"
        n_str = f"+ {n}y" if n != 1 else "+ y"
        p_str = f"+ {p}z" if p != 1 else "+ z"
        expr_str = f"{m_str} {n_str} {p_str}"
        caudan = fr'''Cho hình hộp chữ nhật $ABCD.A'B'C'D'$ có $AB = {a}, AD = {bb}, AA' = {c}$. Chọn hệ trục tọa độ $Oxyz$ có gốc $O$ trùng với $A$, các vectơ $\vec{{AB}}, \vec{{AD}}, \vec{{AA'}}$ lần lượt cùng hướng với $\vec{{i}}, \vec{{j}}, \vec{{k}}$. Gọi $G(x; y; z)$ là trọng tâm của tam giác $A'BD$. Tính $T = {expr_str}$.'''
        dapan = str(ans)
        xG = Fraction(a, 3)
        yG = Fraction(bb, 3)
        zG = Fraction(c, 3)
        loi_giai = fr'''Gắn hệ tọa độ với gốc $A(0;0;0)$: \\
$A'(0; 0; {c}), B({a}; 0; 0), D(0; {bb}; 0)$. \\
Trọng tâm $G$ của tam giác $A'BD$ có tọa độ: \\
$x = \dfrac{{{a}}}{{3}}, \quad y = \dfrac{{{bb}}}{{3}}, \quad z = \dfrac{{{c}}}{{3}}$. \\
Giá trị biểu thức: $T = {expr_str} = {m}\left(\dfrac{{{a}}}{{3}}\right) + {n}\left(\dfrac{{{bb}}}{{3}}\right) + {p}\left(\dfrac{{{c}}}{{3}}\right) = {ans}$.'''
        return caudan, dapan, loi_giai

    else:
        # Tìm tọa độ điểm M thuộc trục Oz cách đều hai điểm A và B
        # zM sao cho MA^2 = MB^2
        # A(x1, y1, z1), B(x2, y2, z2)
        # M(0, 0, z) => x1^2 + y1^2 + (z - z1)^2 = x2^2 + y2^2 + (z - z2)^2
        # x1^2 + y1^2 + z1^2 - 2z*z1 = x2^2 + y2^2 + z2^2 - 2z*z2
        # 2z(z2 - z1) = (x2^2 + y2^2 + z2^2) - (x1^2 + y1^2 + z1^2)
        z1 = 1
        z2 = 3
        x1, y1 = 2, 2
        x2, y2 = 1, 1
        # LHS: 2z(2) = 4z
        # RHS: (1 + 1 + 9) - (4 + 4 + 1) = 11 - 9 = 2 => z = 0.5 (not integer)
        # Let's pick carefully:
        # z2 - z1 = 2 => 4z = RHS. Need RHS divisible by 4.
        # Let A(3; 1; 1), B(1; 1; 5):
        # A: 9 + 1 + 1 = 11. B: 1 + 1 + 25 = 27. RHS = 27 - 11 = 16.
        # 2z(5 - 1) = 8z = 16 => z = 2!
        xA, yA, zA = 3, 1, 1
        xB, yB, zB = 1, 1, 5
        z_ans = 2
        caudan = fr'''Trong không gian $Oxyz$, cho hai điểm $A({xA}; {yA}; {zA})$ và $B({xB}; {yB}; {zB})$. Tìm cao độ $z$ của điểm $M(0; 0; z)$ thuộc trục $Oz$ sao cho khoảng cách từ $M$ đến $A$ bằng khoảng cách từ $M$ đến $B$.'''
        dapan = f'''{z_ans}'''
        loi_giai = fr'''Điểm $M \in Oz \implies M(0; 0; z)$. \\
$MA = MB \iff MA^2 = MB^2$ \\
$\iff (0 - {xA})^2 + (0 - {yA})^2 + (z - {zA})^2 = (0 - {xB})^2 + (0 - {yB})^2 + (z - {zB})^2$ \\
$\iff {xA**2 + yA**2} + z^2 - {2*zA}z + {zA**2} = {xB**2 + yB**2} + z^2 - {2*zB}z + {zB**2}$ \\
$\iff -2z + 11 = -10z + 27 \iff 8z = 16 \iff z = {z_ans}$.'''
        return caudan, dapan, loi_giai


# ------------------------------------------------------------------------------
# CÂU 5: MỨC ĐỘ VẬN DỤNG CAO - CỰC TRỊ VÀ TỐI ƯU HÓA HÌNH HỌC VECTƠ
# ------------------------------------------------------------------------------
def CuoiChuong2_SA_Cau5():
    sub_type = random.choice([1, 2, 3])
    
    if sub_type == 1:
        # Điểm M thuộc (Oxy) sao cho |MA + MB + 2MC| nhỏ nhất
        # Tọa độ tâm I: I = (A + B + 2C)/4
        xA, yA, zA = 1, 2, 3
        xB, yB, zB = 3, 0, 1
        xC, yC, zC = 2, 1, -1
        # xI = (1 + 3 + 4)/4 = 2
        # yI = (2 + 0 + 2)/4 = 1
        # zI = (3 + 1 - 2)/4 = 0.5
        # M thuộc (Oxy) => M(xI; yI; 0) = (2; 1; 0)
        # S = xM + yM = 3
        ans = 3
        caudan = fr'''Trong không gian $Oxyz$, cho ba điểm $A(1; 2; 3), B(3; 0; 1)$ và $C(2; 1; -1)$. Điểm $M(a; b; 0)$ thuộc mặt phẳng tọa độ $(Oxy)$ sao cho biểu thức $|\overrightarrow{{MA}} + \overrightarrow{{MB}} + 2\overrightarrow{{MC}}|$ đạt giá trị nhỏ nhất. Tính giá trị $S = a + b$.'''
        dapan = f'''{ans}'''
        loi_giai = fr'''Gọi $I$ là điểm thỏa mãn $\overrightarrow{{IA}} + \overrightarrow{{IB}} + 2\overrightarrow{{IC}} = \vec{{0}}$. \\
Tọa độ điểm $I$ là: \\
$x_I = \dfrac{{x_A + x_B + 2x_C}}{{4}} = \dfrac{{1 + 3 + 2(2)}}{{4}} = 2$, \\
$y_I = \dfrac{{y_A + y_B + 2y_C}}{{4}} = \dfrac{{2 + 0 + 2(1)}}{{4}} = 1$, \\
$z_I = \dfrac{{z_A + z_B + 2z_C}}{{4}} = \dfrac{{3 + 1 + 2(-1)}}{{4}} = \dfrac{{1}}{{2}}$. \\
Khi đó: $|\overrightarrow{{MA}} + \overrightarrow{{MB}} + 2\overrightarrow{{MC}}| = |4\overrightarrow{{MI}}| = 4MI$. \\
Biểu thức đạt giá trị nhỏ nhất khi $MI$ ngắn nhất, tức $M$ là hình chiếu vuông góc của $I$ lên $(Oxy)$. \\
Suy ra $M(2; 1; 0) \implies a = 2, b = 1$. \\
Vậy $S = a + b = 2 + 1 = {ans}$.'''
        return caudan, dapan, loi_giai

    elif sub_type == 2:
        # Giá trị nhỏ nhất của MA^2 + MB^2 khi M thuộc (Oxy)
        # MA^2 + MB^2 = 2MI^2 + AB^2 / 2
        # I là trung điểm AB: A(1; 2; 4), B(3; 4; 2) => I(2; 3; 3)
        # AB = sqrt(4 + 4 + 4) = sqrt(12) => AB^2 = 12
        # M(x; y; 0) => MI min = d(I, Oxy) = |zI| = 3 => MI^2 = 9
        # Min = 2(9) + 12/2 = 18 + 6 = 24
        ans = 24
        caudan = fr'''Trong không gian $Oxyz$, cho hai điểm $A(1; 2; 4)$ và $B(3; 4; 2)$. Tìm giá trị nhỏ nhất của biểu thức $P = MA^2 + MB^2$ khi điểm $M$ thay đổi trên mặt phẳng tọa độ $(Oxy)$.'''
        dapan = f'''{ans}'''
        loi_giai = fr'''Gọi $I$ là trung điểm của đoạn thẳng $AB$. \\
Tọa độ $I$ là: $x_I = \dfrac{{1+3}}{{2}} = 2, y_I = \dfrac{{2+4}}{{2}} = 3, z_I = \dfrac{{4+2}}{{2}} = 3 \implies I(2; 3; 3)$. \\
Độ dài $AB^2 = (3-1)^2 + (4-2)^2 + (2-4)^2 = 4 + 4 + 4 = 12$. \\
Ta có công thức đường trung tuyến: \\
$P = MA^2 + MB^2 = 2MI^2 + \dfrac{{AB^2}}{{2}} = 2MI^2 + 6$. \\
Biểu thức $P$ nhỏ nhất khi $MI$ nhỏ nhất, tức $M$ là hình chiếu vuông góc của $I(2; 3; 3)$ lên $(Oxy)$. \\
Khi đó $MI = |z_I| = 3 \implies MI^2 = 9$. \\
Giá trị nhỏ nhất của $P$ là: $P_{{\min}} = 2(9) + 6 = {ans}$.'''
        return caudan, dapan, loi_giai

    else:
        # Tìm tọa độ điểm M trên đường thẳng/trục sao cho tích vô hướng đạt cực trị
        # A(1; 0; 2), B(0; 2; 1). M thuộc trục Ox: M(x; 0; 0).
        # MA = (1 - x; 0; 2), MB = (-x; 2; 1)
        # MA . MB = (1 - x)(-x) + 0 + 2 = x^2 - x + 2.
        # Đạt GTNN tại x = 1/2. Tính 10 * x_min = 5.
        ans = 5
        caudan = fr'''Trong không gian $Oxyz$, cho hai điểm $A(1; 0; 2)$ và $B(0; 2; 1)$. Điểm $M(x; 0; 0)$ thay đổi trên trục $Ox$. Khi tích vô hướng $\overrightarrow{{MA}} \cdot \overrightarrow{{MB}}$ đạt giá trị nhỏ nhất, hãy tính giá trị của $10x$.'''
        dapan = f'''{ans}'''
        loi_giai = fr'''Ta có: \\
$\overrightarrow{{MA}} = (1 - x; 0; 2)$, $\overrightarrow{{MB}} = (-x; 2; 1)$. \\
Tích vô hướng: \\
$\overrightarrow{{MA}} \cdot \overrightarrow{{MB}} = (1 - x)(-x) + 0 \cdot 2 + 2 \cdot 1 = x^2 - x + 2 = \left(x - \dfrac{{1}}{{2}}\right)^2 + \dfrac{{7}}{{4}}$. \\
Biểu thức đạt giá trị nhỏ nhất bằng $\dfrac{{7}}{{4}}$ khi $x = \dfrac{{1}}{{2}} = 0{{,}}5$. \\
Khi đó $10x = 10 \cdot 0{{,}}5 = {ans}$.'''
        return caudan, dapan, loi_giai


# ------------------------------------------------------------------------------
# CÂU 6: TOÁN THỰC TẾ - ỨNG DỤNG VECTƠ & TOẠ ĐỘ TRONG THỰC TIỄN
# ------------------------------------------------------------------------------
def CuoiChuong2_SA_Cau6():
    sub_type = random.choice([1, 2, 3, 4])
    
    if sub_type == 1:
        # Lực căng cáp cẩu nâng khung sắt/vật nặng
        # 3 hoặc 4 dây cáp đối xứng
        # Trọng lực P = m * g = 60 * 10 = 600 N (hoặc 120 * 10 = 1200 N)
        # 3 sợi dây cáp dài l hợp với phương thẳng đứng góc alpha
        m_kg = random.choice([120, 180, 240])
        g_val = 10
        P_val = m_kg * g_val
        # Giả sử 3 sợi dây bằng nhau, góc nghiêng so với phương thẳng đứng là 30 độ
        # 3 * T * cos(30 deg) = P => T = P / (3 * cos(30 deg)) = P / (3 * sqrt(3)/2) = 2P / (3*sqrt(3))
        # Hoặc góc 45 độ: 3 * T * cos(45 deg) = P
        # Hoặc 4 sợi dây cáp cẩu tạo góc 60 độ với mặt phẳng ngang (30 độ với phương đứng):
        # 4 * T * sin(60 deg) = P => T = P / (4 * sqrt(3)/2)
        # Hãy chọn mô hình chuẩn sách giáo khoa:
        # Cần cẩu nâng khung sắt trọng lượng P, 4 dây cáp tạo với phương thẳng đứng góc 30 độ:
        # 4 * T * cos(30 deg) = P => T = P / (4 * cos(30 deg))
        # Với P = 1200 N: T = 1200 / (4 * 0.8660) = 1200 / 3.4641 ≈ 346 N.
        ans = round(P_val / (4 * math.cos(math.radians(30))))
        caudan = fr'''Một khung sắt có khối lượng ${m_kg}\text{{ kg}}$ được kéo lên cao bởi một cần cẩu thông qua bốn sợi dây cáp bằng nhau gắn vào bốn góc của khung. Biết rằng các sợi dây cáp đều tạo với phương thẳng đứng một góc bằng $30^\circ$ và lấy gia tốc trọng trường $g = {g_val}\text{{ m/s}}^2$. Tính độ lớn lực căng của mỗi sợi dây cáp (làm tròn kết quả đến hàng đơn vị Newton).'''
        dapan = f'''{ans}'''
        loi_giai = fr'''Trọng lực tác dụng lên khung sắt có độ lớn là: \\
$P = m \cdot g = {m_kg} \cdot {g_val} = {P_val}\text{{ N}}$. \\
Do tính đối xứng, bốn sợi dây cáp có cùng độ lớn lực căng $T$ và cùng tạo với phương thẳng đứng góc $30^\circ$. \\
Điều kiện cân bằng lực theo phương thẳng đứng là: \\
$4 \cdot T \cdot \cos 30^\circ = P \iff 4 \cdot T \cdot \dfrac{{\sqrt{{3}}}}{{2}} = {P_val}$ \\
$\iff 2\sqrt{{3}} T = {P_val} \iff T = \dfrac{{{P_val}}}{{2\sqrt{{3}}}} \approx {ans}\text{{ N}}$.'''
        return caudan, dapan, loi_giai

    elif sub_type == 2:
        # Chuyển động máy bay và gió
        # Vận tốc riêng v1 = 500 km/h hướng Đông (trục Ox)
        # Gió thổi hướng Đông Bắc (45 độ) vận tốc v2 = 50 km/h
        # v_thực = v_máy bay + v_gió
        # vx = 500 + 50*cos(45) = 500 + 35.36 = 535.36
        # vy = 50*sin(45) = 35.36
        # v = sqrt(535.36^2 + 35.36^2) ≈ 537 km/h
        v_mb = random.choice([400, 500, 600])
        v_gio = random.choice([40, 50, 60])
        vx = v_mb + v_gio * math.cos(math.radians(45))
        vy = v_gio * math.sin(math.radians(45))
        ans = round(math.sqrt(vx**2 + vy**2))
        caudan = fr'''Một chiếc máy bay đang bay về hướng Đông với vận tốc riêng là ${v_mb}\text{{ km/h}}$. Cùng lúc đó, có một cơn gió thổi về hướng Đông Bắc với vận tốc ${v_gio}\text{{ km/h}}$. Tính độ lớn vận tốc thực tế của chiếc máy bay so với mặt đất (làm tròn kết quả đến hàng đơn vị theo km/h).'''
        dapan = f'''{ans}'''
        loi_giai = fr'''Chọn hệ trục tọa độ với hướng Đông là hướng của trục $Ox$, hướng Bắc là hướng của trục $Oy$. \\
Khi đó: \\
- Vận tốc riêng của máy bay: $\vec{{v}}_{{\text{{mb}}}} = ({v_mb}; 0)$. \\
- Vận tốc của gió (hướng Đông Bắc tạo góc $45^\circ$ với hướng Đông): \\
$\vec{{v}}_{{\text{{gió}}}} = ({v_gio}\cos 45^\circ; {v_gio}\sin 45^\circ) \approx ({round(v_gio*math.cos(math.radians(45)), 2)}; {round(v_gio*math.sin(math.radians(45)), 2)})$. \\
Vận tốc thực tế của máy bay so với mặt đất là: \\
$\vec{{v}} = \vec{{v}}_{{\text{{mb}}}} + \vec{{v}}_{{\text{{gió}}}} \implies v = \sqrt{{({v_mb} + {v_gio}\cos 45^\circ)^2 + ({v_gio}\sin 45^\circ)^2}} \approx {ans}\text{{ km/h}}$.'''
        return caudan, dapan, loi_giai

    elif sub_type == 3:
        # Ra đa phát hiện máy bay
        # Trạm ra đa tại O(0; 0; 0).
        # Máy bay tại A(100; 200; 10), bay thẳng đến B(400; 600; 10) (đơn vị km).
        # Đoạn đường AB: khoảng cách ngắn nhất đến O.
        # d(O, AB) = |[OA, OB]| / |AB|
        # Với z = 10 không đổi (bay độ cao 10 km).
        # Vectơ AB = (300; 400; 0) => |AB| = 500 km.
        # OA = (100; 200; 10). Tích có hướng:
        # [OA, AB] = (200*0 - 10*400; 10*300 - 100*0; 100*400 - 200*300) = (-4000; 3000; -20000).
        # |[OA, AB]| = sqrt(16*10^6 + 9*10^6 + 400*10^6) = sqrt(425 * 10^6) = 1000 * sqrt(425) ≈ 20615.5
        # d = 20615.5 / 500 ≈ 41.2 km -> làm tròn 41 km.
        ans = 41
        caudan = fr'''Một trạm kiểm soát không lưu được đặt tại gốc tọa độ $O(0; 0; 0)$ trên mặt đất. Một chiếc máy bay bay theo đường thẳng với độ cao không đổi từ vị trí $A(100; 200; 10)$ đến vị trí $B(400; 600; 10)$ (đơn vị tọa độ tính bằng kilômét). Khoảng cách ngắn nhất từ chiếc máy bay đến trạm kiểm soát không lưu trong quá trình bay là bao nhiêu kilômét? (làm tròn kết quả đến hàng đơn vị).'''
        dapan = f'''{ans}'''
        loi_giai = fr'''Vectơ $\overrightarrow{{AB}} = (300; 400; 0) \implies |\overrightarrow{{AB}}| = \sqrt{{300^2 + 400^2 + 0^2}} = 500\text{{ km}}$. \\
Vectơ $\overrightarrow{{OA}} = (100; 200; 10)$. \\
Tích có hướng: $[\overrightarrow{{OA}}, \overrightarrow{{AB}}] = (-4000; 3000; -20000)$. \\
Độ lớn $|[\overrightarrow{{OA}}, \overrightarrow{{AB}}]| = \sqrt{{(-4000)^2 + 3000^2 + (-20000)^2}} = \sqrt{{425000000}} \approx 20615{{,}}5$. \\
Khoảng cách ngắn nhất từ trạm ra đa $O$ đến đường bay $AB$ là: \\
$d(O, AB) = \dfrac{{|[\overrightarrow{{OA}}, \overrightarrow{{AB}}]|}}{{|\overrightarrow{{AB}}|}} \approx \dfrac{{20615{{,}}5}}{{500}} \approx {ans}\text{{ km}}$.'''
        return caudan, dapan, loi_giai

    else:
        # Độ lớn lực tác dụng của bể cá cảnh lên từng chân đế (SGK)
        caudan = fr'''Một bình cá cảnh có dạng một chỏm cầu được đặt trên một chân đế. Biết tổng khối lượng bể cá là $20\text{{ kg}}$, ba chân đế là ba cạnh bên của một hình chóp cụt đều có độ dài cạnh bên bằng $50\text{{ cm}}$, hai đáy có độ dài lần lượt là $30\text{{ cm}}$ và $20\text{{ cm}}$. Biết gia tốc trọng trường bằng $10\text{{ m/s}}^2$, tính độ lớn lực tác dụng của bể cá lên từng chân đế (làm tròn đến hàng phần mười).'''
        dapan = "67,1"
        loi_giai = fr'''Trọng lượng toàn phần của bể cá là: $P = m \cdot g = 20 \cdot 10 = 200\text{{ N}}$. \\
Do ba chân đế phân bố đối xứng đều, mỗi chân đế chịu thành phần lực thẳng đứng là: \\
$P_1 = \dfrac{{P}}{{3}} = \dfrac{{200}}{{3}}\text{{ N}}$. \\
Hiệu bán kính đường tròn đáy là $\Delta R = \dfrac{{10\sqrt{{3}}}}{{3}}\text{{ cm}}$. \\
Góc nghiêng của chân đế có $\cos \alpha = \dfrac{{\sqrt{{3}}}}{{15}} \implies \sin \alpha = \dfrac{{\sqrt{{222}}}}{{15}}$. \\
Độ lớn lực nén dọc theo mỗi chân đế là: \\
$F = \dfrac{{P_1}}{{\sin \alpha}} = \dfrac{{200}}{{3}} \cdot \dfrac{{15}}{{\sqrt{{222}}}} = \dfrac{{1000}}{{\sqrt{{222}}}} \approx 67{{,}}1\text{{ N}}$.'''
        return caudan, dapan, loi_giai

print("All 6 SA Chapter 2 functions defined OK")

# Aliases for Chapter 2 SA
CuoiChuong2_SA_NB1 = CuoiChuong2_SA_Cau1
CuoiChuong2_SA_NB2 = CuoiChuong2_SA_Cau2
CuoiChuong2_SA_TH = CuoiChuong2_SA_Cau3
CuoiChuong2_SA_VDT = CuoiChuong2_SA_Cau4
CuoiChuong2_SA_VDC = CuoiChuong2_SA_Cau5
CuoiChuong2_SA_TT = CuoiChuong2_SA_Cau6

# --- CHƯƠNG III: THỐNG KÊ (MẪU SỐ LIỆU GHÉP NHÓM) ---

def CuoiChuong3_MC_Cau1():
    # Khảo sát thời gian truy cập internet
    a = random.choice([5.5, 9.5, 10.5, 15.5])
    h = random.choice([3, 4, 5])
    bounds = [a + i*h for i in range(6)]
    
    n1 = random.randint(2, 6)
    n2 = random.randint(5, 15)
    n3 = random.randint(10, 20)
    n4 = random.randint(8, 18)
    n5 = random.randint(2, 8)
    
    caudan = fr'''Khảo sát thời gian truy cập Internet mỗi buổi tối (đơn vị: phút) của một số học sinh được cho trong bảng số liệu ghép nhóm sau:
\begin{{center}}
\begin{{tabular}}{{|c|c|c|c|c|c|}}
\hline
Thời gian (phút) & $[{bounds[0]}; {bounds[1]})$ & $[{bounds[1]}; {bounds[2]})$ & $[{bounds[2]}; {bounds[3]})$ & $[{bounds[3]}; {bounds[4]})$ & $[{bounds[4]}; {bounds[5]})$ \\
\hline
Số học sinh & {n1} & {n2} & {n3} & {n4} & {n5} \\
\hline
\end{{tabular}}
\end{{center}}
Khoảng biến thiên của mẫu số liệu ghép nhóm trên là:'''

    correct_val = bounds[5] - bounds[0]
    wrong_1 = correct_val - h
    wrong_2 = correct_val + h
    wrong_3 = h
    
    def fmt(val):
        return f"{val}".replace('.', ',')
        
    choices = [
        fr'''{{\True ${fmt(correct_val)}$}}
''',
        fr'''{{${fmt(wrong_1)}$}}
''',
        fr'''{{${fmt(wrong_2)}$}}
''',
        fr'''{{${fmt(wrong_3)}$}}
'''
    ]
    random.shuffle(choices)
    
    loi_giai = fr'''Khoảng biến thiên của mẫu số liệu ghép nhóm là hiệu giữa đầu mút phải của nhóm cuối cùng và đầu mút trái của nhóm đầu tiên: \\
$R = {fmt(bounds[5])} - {fmt(bounds[0])} = {fmt(correct_val)}$.'''
    return caudan, choices, loi_giai


def CuoiChuong3_MC_Cau2():
    # Trung vị chiều cao học sinh
    a = random.choice([145, 150, 155])
    h = 5
    bounds = [a + i*h for i in range(6)]
    
    n1 = random.randint(3, 6)
    n2 = random.randint(4, 7)
    n3 = random.randint(10, 15)
    n4 = random.randint(5, 9)
    n5 = random.randint(2, 5)
    N = n1 + n2 + n3 + n4 + n5
    
    cf1 = n1
    cf2 = n1 + n2
    cf3 = n1 + n2 + n3
    
    half_N = N / 2
    L = bounds[2]
    me = L + ((half_N - cf2) / n3) * h
    me_val = round(me, 2)
    
    caudan = fr'''Bảng số liệu ghép nhóm sau đây cho biết chiều cao của học sinh lớp 12:
\begin{{center}}
\begin{{tabular}}{{|c|c|c|c|c|c|}}
\hline
Khoảng chiều cao (cm) & $[{bounds[0]}; {bounds[1]})$ & $[{bounds[1]}; {bounds[2]})$ & $[{bounds[2]}; {bounds[3]})$ & $[{bounds[3]}; {bounds[4]})$ & $[{bounds[4]}; {bounds[5]})$ \\
\hline
Số học sinh & {n1} & {n2} & {n3} & {n4} & {n5} \\
\hline
\end{{tabular}}
\end{{center}}
Tìm trung vị của mẫu số liệu ghép nhóm trên (làm tròn đến hàng phần trăm).'''

    def fmt(val):
        return f"{val:.2f}".replace('.', ',') if isinstance(val, float) else f"{val}".replace('.', ',')

    correct = fmt(me_val)
    wrong_1 = fmt(round(me - 0.5, 2))
    wrong_2 = fmt(round(me + 0.5, 2))
    wrong_3 = fmt(round(bounds[2] + ((half_N - cf1)/n3)*h, 2))
    
    choices = [
        fr'''{{\True ${correct}$}}
''',
        fr'''{{${wrong_1}$}}
''',
        fr'''{{${wrong_2}$}}
''',
        fr'''{{${wrong_3}$}}
'''
    ]
    random.shuffle(choices)
    
    loi_giai = fr'''Tổng số học sinh là $n = {N}$. Ta có $\dfrac{{n}}{{2}} = {fmt(half_N)}$. \\
Nhóm chứa trung vị là nhóm thứ ba $[{bounds[2]}; {bounds[3]})$ vì có tần số tích lũy lớn hơn và gần nhất với ${fmt(half_N)}$ (tần số tích lũy nhóm 2 là ${cf2}$, nhóm 3 là ${cf3}$). \\
Do đó: $L = {bounds[2]}, h = {h}, n_3 = {n3}, cf_{{2}} = {cf2}$. \\
Công thức trung vị: \\
$M_e = L + \left(\dfrac{{\dfrac{{n}}{{2}} - cf_{{2}}}}{{n_3}}\right) \cdot h = {bounds[2]} + \left(\dfrac{{{fmt(half_N)} - {cf2}}}{{{n3}}}\right) \cdot {h} \approx {correct}$.'''
    return caudan, choices, loi_giai


def CuoiChuong3_MC_Cau3():
    # Tứ phân vị thứ nhất mức lương nhân viên
    a = random.choice([6, 8, 10])
    h = 2
    bounds = [a + i*h for i in range(6)]
    
    n1 = random.randint(5, 8)
    n2 = random.randint(12, 18)
    n3 = random.randint(15, 20)
    n4 = random.randint(10, 15)
    n5 = random.randint(3, 6)
    N = n1 + n2 + n3 + n4 + n5
    
    q1_pos = N / 4
    L = bounds[1]
    q1 = L + ((q1_pos - n1) / n2) * h
    q1_val = round(q1, 2)
    
    caudan = fr'''Thống kê mức lương của nhân viên một công ty được cho trong bảng dưới đây (đơn vị: triệu đồng):
\begin{{center}}
\begin{{tabular}}{{|c|c|c|c|c|c|}}
\hline
Mức lương & $[{bounds[0]}; {bounds[1]})$ & $[{bounds[1]}; {bounds[2]})$ & $[{bounds[2]}; {bounds[3]})$ & $[{bounds[3]}; {bounds[4]})$ & $[{bounds[4]}; {bounds[5]})$ \\
\hline
Tần số & {n1} & {n2} & {n3} & {n4} & {n5} \\
\hline
\end{{tabular}}
\end{{center}}
Tìm tứ phân vị thứ nhất $Q_1$ của mẫu số liệu ghép nhóm trên (làm tròn đến hàng phần trăm).'''

    def fmt(val):
        return f"{val:.2f}".replace('.', ',') if isinstance(val, float) else f"{val}".replace('.', ',')

    correct = fmt(q1_val)
    wrong_1 = fmt(round(q1 - 0.3, 2))
    wrong_2 = fmt(round(q1 + 0.3, 2))
    wrong_3 = fmt(round(bounds[1] + ((q1_pos)/n2)*h, 2))
    
    choices = [
        fr'''{{\True ${correct}$}}
''',
        fr'''{{${wrong_1}$}}
''',
        fr'''{{${wrong_2}$}}
''',
        fr'''{{${wrong_3}$}}
'''
    ]
    random.shuffle(choices)
    
    loi_giai = fr'''Tổng số số liệu là $n = {N}$. Ta có $\dfrac{{n}}{{4}} = {fmt(q1_pos)}$. \\
Nhóm chứa tứ phân vị thứ nhất $Q_1$ là nhóm thứ hai $[{bounds[1]}; {bounds[2]})$ vì nhóm này có tần số tích lũy đến hết nhóm 1 là ${n1}$ (nhỏ hơn ${fmt(q1_pos)}$) và đến hết nhóm 2 là ${n1+n2}$ (lớn hơn hoặc bằng ${fmt(q1_pos)}$). \\
Do đó: $L = {bounds[1]}, h = {h}, n_2 = {n2}, cf_{{1}} = {n1}$. \\
Công thức tứ phân vị thứ nhất: \\
$Q_1 = L + \left(\dfrac{{\dfrac{{n}}{{4}} - cf_{{1}}}}{{n_2}}\right) \cdot h = {bounds[1]} + \left(\dfrac{{{fmt(q1_pos)} - {n1}}}{{{n2}}}\right) \cdot {h} \approx {correct}$.'''
    return caudan, choices, loi_giai


def CuoiChuong3_MC_Cau4():
    # Khoảng tứ phân vị
    n1 = 6
    n2 = 14
    n3 = 16
    n4 = 4
    N = n1 + n2 + n3 + n4
    
    q1 = 15 + ((10 - 6)/14)*5
    q3 = 20 + ((30 - 20)/16)*5
    dq = q3 - q1
    dq_val = round(dq, 2)
    
    caudan = fr'''Khảo sát thời gian tự học trong một tuần của một số sinh viên thu được bảng số liệu ghép nhóm sau:
\begin{{center}}
\begin{{tabular}}{{|c|c|c|c|c|}}
\hline
Thời gian (giờ) & $[10; 15)$ & $[15; 20)$ & $[20; 25)$ & $[25; 30)$ \\
\hline
Số sinh viên & {n1} & {n2} & {n3} & {n4} \\
\hline
\end{{tabular}}
\end{{center}}
Tìm khoảng tứ phân vị $\Delta_Q$ của mẫu số liệu ghép nhóm trên (làm tròn đến hàng phần trăm).'''

    def fmt(val):
        return f"{val:.2f}".replace('.', ',') if isinstance(val, float) else f"{val}".replace('.', ',')

    correct = fmt(dq_val)
    wrong_1 = fmt(round(dq - 0.5, 2))
    wrong_2 = fmt(round(dq + 0.5, 2))
    wrong_3 = fmt(round(q3, 2))
    
    choices = [
        fr'''{{\True ${correct}$}}
''',
        fr'''{{${wrong_1}$}}
''',
        fr'''{{${wrong_2}$}}
''',
        fr'''{{${wrong_3}$}}
'''
    ]
    random.shuffle(choices)
    
    loi_giai = fr'''Tổng số sinh viên là $n = {N}$. \\
- Tứ phân vị thứ nhất $Q_1$: \\
Ta có $\dfrac{{n}}{{4}} = 10$. Nhóm chứa $Q_1$ là nhóm thứ hai $[15; 20)$. \\
$Q_1 = 15 + \left(\dfrac{{10 - 6}}{{14}}\right) \cdot 5 = \dfrac{{115}}{{7}} \approx 16,43$. \\
- Tứ phân vị thứ ba $Q_3$: \\
Ta có $\dfrac{{3n}}{{4}} = 30$. Nhóm chứa $Q_3$ là nhóm thứ ba $[20; 25)$. \\
$Q_3 = 20 + \left(\dfrac{{30 - 20}}{{16}}\right) \cdot 5 = 23,125$. \\
- Khoảng tứ phân vị: \\
$\Delta_Q = Q_3 - Q_1 = 23,125 - \dfrac{{115}}{{7}} \approx {correct}$.'''
    return caudan, choices, loi_giai


# ==============================================================================
# BÀI TẬP CUỐI CHƯƠNG III - TRẢ LỜI NGẮN (6 CÂU GÔM GỌN THEO MỨC ĐỘ)
# ==============================================================================

# ------------------------------------------------------------------------------
# CÂU 1: MỨC ĐỘ NHẬN BIẾT (DẠNG 1) - KHOẢNG BIẾN THIÊN & NHÓM CHỨA TỨ PHÂN VỊ
# ------------------------------------------------------------------------------
def CuoiChuong3_SA_Cau1():
    sub_type = random.choice([1, 2, 3])
    
    if sub_type == 1:
        # Tính khoảng biến thiên R = a_k - a_1
        h = random.choice([5, 10, 20])
        start = random.choice([10, 20, 30, 40, 50])
        intervals = [f"[{start + i*h}; {start + (i+1)*h})" for i in range(4)]
        intervals.append(f"[{start + 4*h}; {start + 5*h}]")
        freqs = [random.randint(4, 12) for _ in range(5)]
        R = 5 * h
        
        caudan = fr'''Khảo sát thời gian (phút) hoàn thành một bài tập của các học sinh trong một lớp thu được bảng số liệu ghép nhóm sau:
\begin{{center}}
\begin{{tabular}}{{|c|c|c|c|c|c|}}
\hline
Thời gian (phút) & {intervals[0]} & {intervals[1]} & {intervals[2]} & {intervals[3]} & {intervals[4]} \\
\hline
Số học sinh & {freqs[0]} & {freqs[1]} & {freqs[2]} & {freqs[3]} & {freqs[4]} \\
\hline
\end{{tabular}}
\end{{center}}
Tính khoảng biến thiên của mẫu số liệu ghép nhóm trên.'''
        dapan = str(R)
        loi_giai = fr'''Khoảng biến thiên của mẫu số liệu ghép nhóm là hiệu số giữa đầu mút phải của nhóm cuối cùng và đầu mút trái của nhóm đầu tiên: \\
$R = {start + 5*h} - {start} = {R}$.'''
        return caudan, dapan, loi_giai

    elif sub_type == 2:
        # Cỡ mẫu n của mẫu số liệu ghép nhóm
        freqs = [random.randint(5, 15) for _ in range(5)]
        N = sum(freqs)
        caudan = fr'''Khảo sát khối lượng (gam) của các quả cam trong một thùng hàng thu được bảng số liệu ghép nhóm sau:
\begin{{center}}
\begin{{tabular}}{{|c|c|c|c|c|c|}}
\hline
Khối lượng (gam) & $[150; 160)$ & $[160; 170)$ & $[170; 180)$ & $[180; 190)$ & $[190; 200]$ \\
\hline
Số quả cam & {freqs[0]} & {freqs[1]} & {freqs[2]} & {freqs[3]} & {freqs[4]} \\
\hline
\end{{tabular}}
\end{{center}}
Cỡ mẫu của mẫu số liệu ghép nhóm trên là bao nhiêu?'''
        dapan = str(N)
        loi_giai = fr'''Cỡ mẫu $n$ là tổng các tần số của tất cả các nhóm: \\
$n = {freqs[0]} + {freqs[1]} + {freqs[2]} + {freqs[3]} + {freqs[4]} = {N}$.'''
        return caudan, dapan, loi_giai

    else:
        # Giá trị đại diện của nhóm chứa mốt / có tần số lớn nhất
        freqs = [random.randint(4, 9) for _ in range(5)]
        # Make one clearly max
        idx_max = random.choice([1, 2, 3])
        freqs[idx_max] = random.randint(18, 25)
        start = random.choice([20, 30, 40, 50])
        h = 10
        rep_val = start + idx_max*h + h // 2
        intervals = [f"[{start + i*h}; {start + (i+1)*h})" for i in range(4)]
        intervals.append(f"[{start + 4*h}; {start + 5*h}]")
        caudan = fr'''Bảng số liệu ghép nhóm sau đây ghi lại số lượng sách đọc trong một năm của các thành viên câu lạc bộ:
\begin{{center}}
\begin{{tabular}}{{|c|c|c|c|c|c|}}
\hline
Số sách (quyển) & {intervals[0]} & {intervals[1]} & {intervals[2]} & {intervals[3]} & {intervals[4]} \\
\hline
Số thành viên & {freqs[0]} & {freqs[1]} & {freqs[2]} & {freqs[3]} & {freqs[4]} \\
\hline
\end{{tabular}}
\end{{center}}
Tìm giá trị đại diện của nhóm có tần số lớn nhất.'''
        dapan = str(rep_val)
        loi_giai = fr'''Tần số lớn nhất trong bảng là ${freqs[idx_max]}$, ứng với nhóm ${intervals[idx_max]}$. \\
Giá trị đại diện của nhóm này là trung điểm của hai đầu mút: \\
$x = \dfrac{{{start + idx_max*h} + {start + (idx_max+1)*h}}}{{2}} = {rep_val}$.'''
        return caudan, dapan, loi_giai


# ------------------------------------------------------------------------------
# CÂU 2: MỨC ĐỘ NHẬN BIẾT (DẠNG 2) - SỐ TRUNG BÌNH CỘNG CỦA MẪU GHÉP NHÓM
# ------------------------------------------------------------------------------
def CuoiChuong3_SA_Cau2():
    # Số trung bình cộng của mẫu ghép nhóm
    n1 = random.randint(3, 6)
    n2 = random.randint(5, 9)
    n3 = random.randint(10, 16)
    n4 = random.randint(8, 14)
    n5 = random.randint(3, 7)
    N = n1 + n2 + n3 + n4 + n5
    
    # Giá trị đại diện các nhóm điểm số 1, 3, 5, 7, 9
    sum_fx = n1*1 + n2*3 + n3*5 + n4*7 + n5*9
    mean = sum_fx / N
    mean_val = round(mean, 2)
    
    caudan = fr'''Bảng số liệu ghép nhóm sau đây cho biết kết quả kiểm tra môn Toán của một lớp học sinh:
\begin{{center}}
\begin{{tabular}}{{|c|c|c|c|c|c|}}
\hline
Điểm số & $[0; 2)$ & $[2; 4)$ & $[4; 6)$ & $[6; 8)$ & $[8; 10]$ \\
\hline
Số học sinh & {n1} & {n2} & {n3} & {n4} & {n5} \\
\hline
\end{{tabular}}
\end{{center}}
Tính số trung bình của mẫu số liệu ghép nhóm trên (làm tròn kết quả đến hàng phần trăm).'''
    dapan = fmt_num(mean_val)
    loi_giai = fr'''Các giá trị đại diện của các nhóm lần lượt là: \\
$c_1 = 1, \quad c_2 = 3, \quad c_3 = 5, \quad c_4 = 7, \quad c_5 = 9$. \\
Cỡ mẫu $n = {n1} + {n2} + {n3} + {n4} + {n5} = {N}$. \\
Số trung bình của mẫu số liệu ghép nhóm là: \\
$\bar{{x}} = \dfrac{{{n1} \cdot 1 + {n2} \cdot 3 + {n3} \cdot 5 + {n4} \cdot 7 + {n5} \cdot 9}}{{{N}}} = \dfrac{{{sum_fx}}}{{{N}}} \approx {dapan}$.'''
    return caudan, dapan, loi_giai


# ------------------------------------------------------------------------------
# CÂU 3: MỨC ĐỘ THÔNG HIỂU - TỨ PHÂN VỊ Q1, Q3, TRUNG VỊ VÀ KHOẢNG TỨ PHÂN VỊ
# ------------------------------------------------------------------------------
def CuoiChuong3_SA_Cau3():
    sub_type = random.choice([1, 2])
    
    if sub_type == 1:
        # Tính trung vị Me = Q2
        freqs = [6, 12, 18, 10, 4]
        random.shuffle(freqs)
        freqs = [random.randint(5, 10), random.randint(12, 18), random.randint(15, 22), random.randint(8, 14), random.randint(4, 8)]
        N = sum(freqs)
        # Bảng [0; 20), [20; 40), [40; 60), [60; 80), [80; 100]
        h = 20
        # Target position: N / 2
        pos = N / 2
        cf = 0
        group_idx = 0
        for i, f in enumerate(freqs):
            if cf + f >= pos:
                group_idx = i
                break
            cf += f
        u_m = group_idx * h
        n_m = freqs[group_idx]
        C = cf
        Me = u_m + ((pos - C) / n_m) * h
        Me_round = round(Me, 2)
        
        caudan = fr'''Khảo sát thời gian sử dụng điện thoại thông minh mỗi ngày (phút) của học sinh một trường THPT thu được bảng số liệu ghép nhóm:
\begin{{center}}
\begin{{tabular}}{{|c|c|c|c|c|c|}}
\hline
Thời gian (phút) & $[0; 20)$ & $[20; 40)$ & $[40; 60)$ & $[60; 80)$ & $[80; 100]$ \\
\hline
Số học sinh & {freqs[0]} & {freqs[1]} & {freqs[2]} & {freqs[3]} & {freqs[4]} \\
\hline
\end{{tabular}}
\end{{center}}
Tính trung vị của mẫu số liệu ghép nhóm trên (làm tròn kết quả đến hàng phần trăm).'''
        dapan = fmt_num(Me_round)
        loi_giai = fr'''Cỡ mẫu $n = {N} \implies \dfrac{{n}}{{2}} = \dfrac{{{N}}}{{2}} = {pos}$. \\
Nhóm chứa trung vị là nhóm thứ ${group_idx+1}$, tức $[{u_m}; {u_m + h})$. \\
Do đó: $u_m = {u_m}, \quad C = {C}, \quad n_m = {n_m}, \quad h = {h}$. \\
Trung vị của mẫu số liệu ghép nhóm là: \\
$M_e = {u_m} + \left(\dfrac{{{pos} - {C}}}{{{n_m}}}\right) \cdot {h} \approx {dapan}$.'''
        return caudan, dapan, loi_giai

    else:
        # Khoảng tứ phân vị \Delta_Q = Q3 - Q1
        freqs = [random.randint(6, 10), random.randint(14, 20), random.randint(16, 24), random.randint(8, 14), random.randint(4, 8)]
        N = sum(freqs)
        h = 10
        start = 10
        # Q1
        pos1 = N / 4
        cf = 0
        idx1 = 0
        for i, f in enumerate(freqs):
            if cf + f >= pos1:
                idx1 = i
                break
            cf += f
        u1 = start + idx1 * h
        n1 = freqs[idx1]
        C1 = cf
        Q1 = u1 + ((pos1 - C1) / n1) * h
        
        # Q3
        pos3 = 3 * N / 4
        cf = 0
        idx3 = 0
        for i, f in enumerate(freqs):
            if cf + f >= pos3:
                idx3 = i
                break
            cf += f
        u3 = start + idx3 * h
        n3 = freqs[idx3]
        C3 = cf
        Q3 = u3 + ((pos3 - C3) / n3) * h
        
        delta_Q = round(Q3 - Q1, 2)
        
        intervals = [f"[{start + i*h}; {start + (i+1)*h})" for i in range(4)]
        intervals.append(f"[{start + 4*h}; {start + 5*h}]")
        
        caudan = fr'''Bảng số liệu sau đây ghi lại cự ly ném bóng (m) của các vận động viên:
\begin{{center}}
\begin{{tabular}}{{|c|c|c|c|c|c|}}
\hline
Cự ly (m) & {intervals[0]} & {intervals[1]} & {intervals[2]} & {intervals[3]} & {intervals[4]} \\
\hline
Số VĐV & {freqs[0]} & {freqs[1]} & {freqs[2]} & {freqs[3]} & {freqs[4]} \\
\hline
\end{{tabular}}
\end{{center}}
Tính khoảng tứ phân vị của mẫu số liệu ghép nhóm trên (làm tròn kết quả đến hàng phần trăm).'''
        dapan = fmt_num(delta_Q)
        loi_giai = fr'''Cỡ mẫu $n = {N}$. \\
- Tứ phân vị thứ nhất $Q_1$: Vị trí $\dfrac{{n}}{{4}} = {pos1}$. \\
Nhóm chứa $Q_1$ là ${intervals[idx1]} \implies Q_1 = {u1} + \left(\dfrac{{{pos1} - {C1}}}{{{n1}}}\right) \cdot {h} \approx {round(Q1, 2)}$. \\
- Tứ phân vị thứ ba $Q_3$: Vị trí $\dfrac{{3n}}{{4}} = {pos3}$. \\
Nhóm chứa $Q_3$ là ${intervals[idx3]} \implies Q_3 = {u3} + \left(\dfrac{{{pos3} - {C3}}}{{{n3}}}\right) \cdot {h} \approx {round(Q3, 2)}$. \\
Khoảng tứ phân vị của mẫu số liệu là: \\
$\Delta_Q = Q_3 - Q_1 \approx {dapan}$.'''
        return caudan, dapan, loi_giai


# ------------------------------------------------------------------------------
# CÂU 4: MỨC ĐỘ VẬN DỤNG THẤP - PHƯƠNG SAI VÀ ĐỘ LỆCH CHUẨN
# ------------------------------------------------------------------------------
def CuoiChuong3_SA_Cau4():
    # Tính độ lệch chuẩn s = sqrt(s^2)
    n1 = random.randint(2, 4)
    n2 = random.randint(4, 7)
    n3 = random.randint(6, 10)
    n4 = random.randint(3, 5)
    N = n1 + n2 + n3 + n4
    
    # Đại diện 18, 22, 26, 30
    sum_fx = n1*18 + n2*22 + n3*26 + n4*30
    mean = sum_fx / N
    sum_fx2 = n1*(18**2) + n2*(22**2) + n3*(26**2) + n4*(30**2) 
    variance = (sum_fx2 / N) - (mean**2)
    std_dev = math.sqrt(variance)
    std_val = round(std_dev, 2)
    
    caudan = fr'''Khảo sát nhiệt độ trung bình ($^\circ$C) các tháng trong một năm tại một vùng thu được bảng số liệu ghép nhóm sau:
\begin{{center}}
\begin{{tabular}}{{|c|c|c|c|c|}}
\hline
Nhiệt độ ($^\circ$C) & $[16; 20)$ & $[20; 24)$ & $[24; 28)$ & $[28; 32]$ \\
\hline
Số tháng & {n1} & {n2} & {n3} & {n4} \\
\hline
\end{{tabular}}
\end{{center}}
Tính độ lệch chuẩn của mẫu số liệu ghép nhóm trên (làm tròn kết quả đến hàng phần trăm).'''
    dapan = fmt_num(std_val)
    loi_giai = fr'''Các giá trị đại diện là $c_1 = 18, c_2 = 22, c_3 = 26, c_4 = 30$. \\
Cỡ mẫu $n = {N}$. \\
Số trung bình: $\bar{{x}} = \dfrac{{{sum_fx}}}{{{N}}} \approx {round(mean, 2)}$. \\
Phương sai: \\
$s^2 = \dfrac{{{n1}\cdot 18^2 + {n2}\cdot 22^2 + {n3}\cdot 26^2 + {n4}\cdot 30^2}}{{{N}}} - (\bar{{x}})^2 \approx {round(variance, 2)}$. \\
Độ lệch chuẩn là: $s = \sqrt{{s^2}} \approx {dapan}$.'''
    return caudan, dapan, loi_giai


# ------------------------------------------------------------------------------
# CÂU 5: MỨC ĐỘ VẬN DỤNG CAO - TÌM TẦN SỐ CÒN THIẾU / GIÁ TRỊ NGOẠI LỆ
# ------------------------------------------------------------------------------
def CuoiChuong3_SA_Cau5():
    sub_type = random.choice([1, 2])
    
    if sub_type == 1:
        # Tìm tần số x trong bảng khi biết số trung bình
        x_true = random.choice([5, 8, 10, 12])
        n1, n2, n4 = 4, 6, 4
        # c1=2, c2=4, c3=6 (with freq x), c4=8
        # sum = 4*2 + 6*4 + x*6 + 4*8 = 8 + 24 + 32 + 6x = 64 + 6x
        # N = 14 + x
        # mean = (64 + 6x) / (14 + x)
        # Choose a clean mean:
        # If x=6 => (64 + 36)/20 = 5.0
        # If x=11 => (64 + 66)/25 = 5.2
        # Let's parameterize properly:
        x_target = random.choice([6, 11, 16])
        n1, n2, n4 = 4, 6, 4
        mean_target = (64 + 6*x_target) / (14 + x_target)
        
        caudan = fr'''Khảo sát điểm số của một nhóm học sinh thu được bảng phân bố tần số ghép nhóm có một tần số $x$ chưa biết:
\begin{{center}}
\begin{{tabular}}{{|c|c|c|c|c|}}
\hline
Điểm số & $[1; 3)$ & $[3; 5)$ & $[5; 7)$ & $[7; 9]$ \\
\hline
Số học sinh & 4 & 6 & $x$ & 4 \\
\hline
\end{{tabular}}
\end{{center}}
Biết rằng điểm số trung bình của nhóm học sinh này là $\bar{{x}} = {fmt_num(round(mean_target, 2))}$. Tìm giá trị của $x$.'''
        dapan = str(x_target)
        loi_giai = fr'''Các giá trị đại diện của các nhóm lần lượt là: $c_1 = 2, c_2 = 4, c_3 = 6, c_4 = 8$. \\
Tổng số học sinh là $n = 4 + 6 + x + 4 = 14 + x$. \\
Số trung bình được tính theo công thức: \\
$\bar{{x}} = \dfrac{{4 \cdot 2 + 6 \cdot 4 + x \cdot 6 + 4 \cdot 8}}{{14 + x}} = \dfrac{{64 + 6x}}{{14 + x}} = {fmt_num(round(mean_target, 2))}$. \\
Giải phương trình: $64 + 6x = {fmt_num(round(mean_target, 2))} \cdot (14 + x) \implies x = {x_target}$.'''
        return caudan, dapan, loi_giai

    else:
        # So sánh độ phân tán qua độ lệch chuẩn giữa hai lớp/giống cây
        s1 = random.choice([2.15, 2.45, 3.12])
        s2 = random.choice([1.25, 1.68, 1.85])
        diff = round(s1 - s2, 2)
        caudan = fr'''Để so sánh độ ổn định về năng suất của hai giống lúa mới $A$ và $B$, người ta đo năng suất trên các thửa ruộng thử nghiệm. Kết quả tính toán cho thấy độ lệch chuẩn mẫu số liệu ghép nhóm của giống lúa $A$ là $s_A = {fmt_num(s1)}$ tạ/ha, của giống lúa $B$ là $s_B = {fmt_num(s2)}$ tạ/ha. Độ lệch chuẩn của giống lúa $A$ lớn hơn giống lúa $B$ bao nhiêu tạ/ha?'''
        dapan = fmt_num(diff)
        loi_giai = fr'''Hiệu số giữa độ lệch chuẩn của giống lúa $A$ và giống lúa $B$ là: \\
$s_A - s_B = {fmt_num(s1)} - {fmt_num(s2)} = {dapan}\text{{ tạ/ha}}$. \\
(Điều này chứng tỏ giống lúa $B$ có năng suất đồng đều và ổn định hơn giống lúa $A$).'''
        return caudan, dapan, loi_giai


# ------------------------------------------------------------------------------
# CÂU 6: TOÁN THỰC TẾ - THỐNG KÊ RỦI RO CỔ PHIẾU, DOANH THU, TUỔI THỌ SẢN PHẨM
# ------------------------------------------------------------------------------
def CuoiChuong3_SA_Cau6():
    sub_type = random.choice([1, 2])
    
    if sub_type == 1:
        # Độ lệch chuẩn giá cổ phiếu (mức độ rủi ro đầu tư)
        n1 = random.randint(5, 8)
        n2 = random.randint(12, 18)
        n3 = random.randint(15, 22)
        n4 = random.randint(6, 10)
        N = n1 + n2 + n3 + n4
        # Giá [20; 24), [24; 28), [28; 32), [32; 36] nghìn đồng
        # c1=22, c2=26, c3=30, c4=34
        sum_fx = n1*22 + n2*26 + n3*30 + n4*34
        mean = sum_fx / N
        sum_fx2 = n1*(22**2) + n2*(26**2) + n3*(30**2) + n4*(34**2)
        variance = (sum_fx2 / N) - (mean**2)
        s = round(math.sqrt(variance), 2)
        
        caudan = fr'''Một nhà đầu tư theo dõi giá đóng cửa (nghìn đồng/cổ phiếu) của một mã cổ phiếu trong $50$ ngày giao dịch và thu được bảng tần số ghép nhóm sau:
\begin{{center}}
\begin{{tabular}}{{|c|c|c|c|c|}}
\hline
Giá đóng cửa (nghìn đồng) & $[20; 24)$ & $[24; 28)$ & $[28; 32)$ & $[32; 36]$ \\
\hline
Số ngày & {n1} & {n2} & {n3} & {n4} \\
\hline
\end{{tabular}}
\end{{center}}
Tính độ lệch chuẩn của giá đóng cửa mã cổ phiếu trên để đánh giá mức độ biến động rủi ro (làm tròn kết quả đến hàng phần trăm).'''
        dapan = fmt_num(s)
        loi_giai = fr'''Các giá trị đại diện là $c_1 = 22, c_2 = 26, c_3 = 30, c_4 = 34$. \\
Cỡ mẫu $n = {N}$. \\
Số trung bình: $\bar{{x}} = \dfrac{{{sum_fx}}}{{{N}}} \approx {round(mean, 2)}$. \\
Phương sai: $s^2 = \dfrac{{{sum_fx2}}}{{{N}}} - (\bar{{x}})^2 \approx {round(variance, 2)}$. \\
Độ lệch chuẩn là: $s = \sqrt{{s^2}} \approx {dapan}$ nghìn đồng.'''
        return caudan, dapan, loi_giai

    else:
        # Tuổi thọ của bóng đèn điện tử
        freqs = [8, 20, 32, 28, 12]
        N = sum(freqs)
        # Giờ: [1000; 1200), [1200; 1400), [1400; 1600), [1600; 1800), [1800; 2000]
        # Đại diện: 1100, 1300, 1500, 1700, 1900
        sum_fx = 8*1100 + 20*1300 + 32*1500 + 28*1700 + 12*1900
        mean = sum_fx / N
        sum_fx2 = 8*(1100**2) + 20*(1300**2) + 32*(1500**2) + 28*(1700**2) + 12*(1900**2)
        variance = (sum_fx2 / N) - (mean**2)
        s = round(math.sqrt(variance), 1)
        
        caudan = fr'''Khảo sát tuổi thọ (giờ) của $100$ bóng đèn do một nhà máy sản xuất thu được bảng số liệu ghép nhóm:
\begin{{center}}
\begin{{tabular}}{{|c|c|c|c|c|c|}}
\hline
Tuổi thọ (giờ) & $[1000; 1200)$ & $[1200; 1400)$ & $[1400; 1600)$ & $[1600; 1800)$ & $[1800; 2000]$ \\
\hline
Số bóng đèn & 8 & 20 & 32 & 28 & 12 \\
\hline
\end{{tabular}}
\end{{center}}
Tính độ lệch chuẩn của tuổi thọ bóng đèn (làm tròn kết quả đến hàng phần mười).'''
        dapan = fmt_num(s)
        loi_giai = fr'''Giá trị đại diện lần lượt là: $1100, 1300, 1500, 1700, 1900$. \\
Cỡ mẫu $n = 100$. \\
Tuổi thọ trung bình: $\bar{{x}} = \dfrac{{{sum_fx}}}{{100}} = {int(mean)}$ giờ. \\
Phương sai: $s^2 = \dfrac{{{sum_fx2}}}{{100}} - {int(mean)}^2 = {int(variance)}$. \\
Độ lệch chuẩn: $s = \sqrt{{{int(variance)}}} \approx {dapan}$ giờ.'''
        return caudan, dapan, loi_giai

print("All 6 SA Chapter 3 functions defined OK")

# Aliases for Chapter 3 SA
CuoiChuong3_SA_NB1 = CuoiChuong3_SA_Cau1
CuoiChuong3_SA_NB2 = CuoiChuong3_SA_Cau2
CuoiChuong3_SA_TH = CuoiChuong3_SA_Cau3
CuoiChuong3_SA_VDT = CuoiChuong3_SA_Cau4
CuoiChuong3_SA_VDC = CuoiChuong3_SA_Cau5
CuoiChuong3_SA_TT = CuoiChuong3_SA_Cau6

def CuoiChuong2_MC_Cau5():
    x = random.randint(-9, 9)
    y = random.randint(-9, 9)
    z = random.randint(-9, 9)
    while x == 0 or y == 0 or z == 0:
        x = random.randint(-9, 9)
        y = random.randint(-9, 9)
        z = random.randint(-9, 9)
        
    sub = random.choice([1, 2, 3, 4, 5, 6])
    if sub == 1:
        plane = "Oxy"
        correct = fr'''M({x}; {y}; 0)'''
        wrong1 = fr'''M(0; 0; {z})'''
        wrong2 = fr'''M({x}; 0; {z})'''
        wrong3 = fr'''M(0; {y}; {z})'''
        ans_plane = fr'''$z=0$'''
    elif sub == 2:
        plane = "Oyz"
        correct = fr'''M(0; {y}; {z})'''
        wrong1 = fr'''M({x}; 0; 0)'''
        wrong2 = fr'''M({x}; {y}; 0)'''
        wrong3 = fr'''M({x}; 0; {z})'''
        ans_plane = fr'''$x=0$'''
    elif sub == 3:
        plane = "Oxz"
        correct = fr'''M({x}; 0; {z})'''
        wrong1 = fr'''M(0; {y}; 0)'''
        wrong2 = fr'''M({x}; {y}; 0)'''
        wrong3 = fr'''M(0; {y}; {z})'''
        ans_plane = fr'''$y=0$'''
    elif sub == 4:
        plane = "trục Ox"
        correct = fr'''M({x}; 0; 0)'''
        wrong1 = fr'''M(0; {y}; {z})'''
        wrong2 = fr'''M({x}; {y}; 0)'''
        wrong3 = fr'''M(0; 0; {z})'''
        ans_plane = fr'''$y=0, z=0$'''
    elif sub == 5:
        plane = "trục Oy"
        correct = fr'''M(0; {y}; 0)'''
        wrong1 = fr'''M({x}; 0; {z})'''
        wrong2 = fr'''M({x}; {y}; 0)'''
        wrong3 = fr'''M(0; 0; {z})'''
        ans_plane = fr'''$x=0, z=0$'''
    else:
        plane = "trục Oz"
        correct = fr'''M(0; 0; {z})'''
        wrong1 = fr'''M({x}; {y}; 0)'''
        wrong2 = fr'''M({x}; 0; 0)'''
        wrong3 = fr'''M(0; {y}; 0)'''
        ans_plane = fr'''$x=0, y=0$'''
        
    caudan = fr'''Trong không gian $Oxyz$, hình chiếu vuông góc của điểm $A({x}; {y}; {z})$ trên {plane} là điểm'''
    choices = [
        fr'''{{\True ${correct}$}}
''',
        fr'''{{${wrong1}$}}
''',
        fr'''{{${wrong2}$}}
''',
        fr'''{{${wrong3}$}}
'''
    ]
    random.shuffle(choices)
    loi_giai = fr'''Hình chiếu vuông góc của điểm $A({x}; {y}; {z})$ trên {plane} có tọa độ thu được bằng cách giữ nguyên các thành phần tương ứng và cho các thành phần khác bằng $0$ (vì {plane} có phương trình {ans_plane}). \\
Vậy tọa độ hình chiếu là ${correct}$.'''
    return caudan, choices, loi_giai

def CuoiChuong2_MC_Cau6():
    sub = random.choice([1, 2])
    if sub == 1:
        x = random.randint(-4, 4)
        y = random.randint(-4, 4)
        z = random.randint(-4, 4)
        while x == 0 or y == 0 or z == 0:
            x = random.randint(-4, 4)
            y = random.randint(-4, 4)
            z = random.randint(-4, 4)
            
        k = random.choice([-2, -1, 2, 3])
        correct = fr'''\vec{{b}} = ({k*x}; {k*y}; {k*z})'''
        wrong1 = fr'''\vec{{c}} = ({-k*x}; {k*y}; {k*z})'''
        wrong2 = fr'''\vec{{d}} = ({k*x}; {-k*y}; {k*z})'''
        wrong3 = fr'''\vec{{m}} = ({k*x}; {k*y}; {-k*z})'''
        
        caudan = fr'''Trong không gian $Oxyz$, cho vectơ $\vec{{a}} = ({x}; {y}; {z})$. Vectơ nào sau đây cùng phương với $\vec{{a}}$?'''
        choices = [
            fr'''{{\True ${correct}$}}
''',
            fr'''{{${wrong1}$}}
''',
            fr'''{{${wrong2}$}}
''',
            fr'''{{${wrong3}$}}
'''
        ]
        loi_giai = fr'''Hai vectơ $\vec{{a}}$ và $\vec{{b}}$ cùng phương khi và chỉ khi tồn tại số thực $k$ sao cho $\vec{{b}} = k\vec{{a}}$. \\
Với $k={k}$, ta có $k\vec{{a}} = ({k*x}; {k*y}; {k*z}) = \vec{{b}}$. \\
Vậy vectơ cùng phương là ${correct}$.'''
    else:
        r = random.choice([-3, -2, 2, 3])
        n = random.choice([-3, -2, -1, 1, 2, 3])
        z_b = random.choice([-3, -2, -1, 1, 2, 3])
        y = r * n
        z = r * z_b
        
        caudan = fr'''Trong không gian $Oxyz$, cho hai vectơ $\vec{{a}} = (m; {y}; {z})$ và $\vec{{b}} = (1; n; {z_b})$. Hai vectơ này cùng phương khi'''
        correct = fr'''\left\{{\begin{{array}}{{l}} m = {r} \\ n = {n} \end{{array}}\right.'''
        wrong1 = fr'''\left\{{\begin{{array}}{{l}} m = {-r} \\ n = {n} \end{{array}}\right.'''
        wrong2 = fr'''\left\{{\begin{{array}}{{l}} m = {r} \\ n = {-n} \end{{array}}\right.'''
        wrong3 = fr'''\left\{{\begin{{array}}{{l}} m = {-r} \\ n = {-n} \end{{array}}\right.'''
        
        choices = [
            fr'''{{\True ${correct}$}}
''',
            fr'''{{${wrong1}$}}
''',
            fr'''{{${wrong2}$}}
''',
            fr'''{{${wrong3}$}}
'''
        ]
        loi_giai = fr'''Hai vectơ $\vec{{a}}$ và $\vec{{b}}$ cùng phương khi và chỉ khi: \\
$\dfrac{{m}}{{1}} = \dfrac{{{y}}}{{n}} = \dfrac{{{z}}}{{{z_b}}} \iff m = \dfrac{{{z}}}{{{z_b}}} = {r}$ và $n = \dfrac{{{y}}}{{m}} = \dfrac{{{y}}}{{{r}}} = {n}$. \\
Vậy ta có ${correct}$.'''
    random.shuffle(choices)
    return caudan, choices, loi_giai

def CuoiChuong2_MC_Cau7():
    sub = random.choice([1, 2, 3])
    if sub == 1:
        x1, y1, z1 = [random.randint(-5, 5) for _ in range(3)]
        x2, y2, z2 = [x1 + 2*random.randint(-3, 3) for _ in range(3)]
        
        xm, ym, zm = (x1+x2)//2, (y1+y2)//2, (z1+z2)//2
        caudan = fr'''Trong không gian $Oxyz$, cho hai điểm $A({x1}; {y1}; {z1})$ và $B({x2}; {y2}; {z2})$. Tọa độ trung điểm $M$ của đoạn thẳng $AB$ là'''
        correct = fr'''M({xm}; {ym}; {zm})'''
        wrong1 = fr'''M({x1+x2}; {y1+y2}; {z1+z2})'''
        wrong2 = fr'''M({xm+1}; {ym}; {zm-1})'''
        wrong3 = fr'''M({-xm}; {-ym}; {-zm})'''
        
        choices = [
            fr'''{{\True ${correct}$}}
''',
            fr'''{{${wrong1}$}}
''',
            fr'''{{${wrong2}$}}
''',
            fr'''{{${wrong3}$}}
'''
        ]
        loi_giai = fr'''Tọa độ trung điểm $M$ của $AB$ là: \\
$x_M = \dfrac{{{x1} + {x2}}}{{2}} = {xm}$, \\
$y_M = \dfrac{{{y1} + {y2}}}{{2}} = {ym}$, \\
$z_M = \dfrac{{{z1} + {z2}}}{{2}} = {zm}$. \\
Vậy $M({xm}; {ym}; {zm})$.'''
    elif sub == 2:
        x1, y1, z1 = [random.randint(-4, 4) for _ in range(3)]
        xb, yb, zb = [random.randint(-4, 4) for _ in range(3)]
        xc, yc, zc = 2*xb - x1, 2*yb - y1, 2*zb - z1
        
        caudan = fr'''Trong không gian $Oxyz$, cho hai điểm $A({x1}; {y1}; {z1})$ và $B({xb}; {yb}; {zb})$. Tọa độ điểm $C$ sao cho $B$ là trung điểm của đoạn thẳng $AC$ là'''
        correct = fr'''C({xc}; {yc}; {zc})'''
        wrong1 = fr'''C({(x1+xb)//2}; {(y1+yb)//2}; {(z1+zb)//2})'''
        wrong2 = fr'''C({xc+1}; {yc-1}; {zc})'''
        wrong3 = fr'''C({-xc}; {-yc}; {-zc})'''
        
        choices = [
            fr'''{{\True ${correct}$}}
''',
            fr'''{{${wrong1}$}}
''',
            fr'''{{${wrong2}$}}
''',
            fr'''{{${wrong3}$}}
'''
        ]
        loi_giai = fr'''Vì $B$ là trung điểm của $AC$ nên ta có: \\
$x_C = 2x_B - x_A = 2({xb}) - ({x1}) = {xc}$, \\
$y_C = 2y_B - y_A = 2({yb}) - ({y1}) = {yc}$, \\
$z_C = 2z_B - z_A = 2({zb}) - ({z1}) = {zc}$. \\
Vậy $C({xc}; {yc}; {zc})$.'''
    else:
        xg, yg, zg = [random.randint(-2, 2) for _ in range(3)]
        x1, y1, z1 = [random.randint(-4, 4) for _ in range(3)]
        x2, y2, z2 = [random.randint(-4, 4) for _ in range(3)]
        xc, yc, zc = 3*xg - x1 - x2, 3*yg - y1 - y2, 3*zg - z1 - z2
        
        caudan = fr'''Trong không gian $Oxyz$, cho tam giác $ABC$ có trọng tâm $G({xg}; {yg}; {zg})$ và hai đỉnh $A({x1}; {y1}; {z1})$, $B({x2}; {y2}; {z2})$. Tọa độ đỉnh $C$ là'''
        correct = fr'''C({xc}; {yc}; {zc})'''
        wrong1 = fr'''C({xc-1}; {yc+1}; {zc})'''
        wrong2 = fr'''C({x1+x2-xg}; {y1+y2-yg}; {z1+z2-zg})'''
        wrong3 = fr'''C({-xc}; {-yc}; {-zc})'''
        
        choices = [
            fr'''{{\True ${correct}$}}
''',
            fr'''{{${wrong1}$}}
''',
            fr'''{{${wrong2}$}}
''',
            fr'''{{${wrong3}$}}
'''
        ]
        loi_giai = fr'''Vì $G$ là trọng tâm của tam giác $ABC$ nên ta có: \\
$x_C = 3x_G - x_A - x_B = 3({xg}) - ({x1}) - ({x2}) = {xc}$, \\
$y_C = 3y_G - y_A - y_B = 3({yg}) - ({y1}) - ({y2}) = {yc}$, \\
$z_C = 3z_G - z_A - z_B = 3({zg}) - ({z1}) - ({z2}) = {zc}$. \\
Vậy $C({xc}; {yc}; {zc})$.'''
        
    random.shuffle(choices)
    return caudan, choices, loi_giai

def CuoiChuong2_MC_Cau8():
    sub = random.choice([1, 2, 3])
    if sub == 1:
        x1, y1, z1 = [random.randint(-4, 4) for _ in range(3)]
        x2, y2, z2 = [random.randint(-4, 4) for _ in range(3)]
        ans = x1*x2 + y1*y2 + z1*z2
        
        caudan = fr'''Trong không gian $Oxyz$, cho hai vectơ $\vec{{u}} = ({x1}; {y1}; {z1})$ và $\vec{{v}} = ({x2}; {y2}; {z2})$. Tích vô hướng của hai vectơ là'''
        choices = [
            fr'''{{\True ${ans}$}}
''',
            fr'''{{${ans + random.choice([2, 3, 4])}$}}
''',
            fr'''{{${ans - random.choice([2, 3, 4])}$}}
''',
            fr'''{{${-ans}$}}
'''
        ]
        loi_giai = fr'''Tích vô hướng của hai vectơ $\vec{{u}}\cdot\vec{{v}} = x_1 x_2 + y_1 y_2 + z_1 z_2 = ({x1})({x2}) + ({y1})({y2}) + ({z1})({z2}) = {ans}$.'''
    elif sub == 2:
        angle_type = random.choice([45, 60, 120])
        if angle_type == 45:
            u_str, v_str = "(1; 1; 0)", "(1; 0; 0)"
            ans = "45^\\circ"
            wrong1, wrong2, wrong3 = "135^\\circ", "60^\\circ", "90^\\circ"
            loi_giai = fr'''Ta có $\vec{{u}}\cdot\vec{{v}} = 1\cdot 1 + 1\cdot 0 + 0\cdot 0 = 1$. \\
$|\vec{{u}}| = \sqrt{{1^2+1^2+0^2}} = \sqrt{{2}}$, $|\vec{{v}}| = \sqrt{{1^2+0^2+0^2}} = 1$. \\
$\cos(\vec{{u}}, \vec{{v}}) = \dfrac{{\vec{{u}}\cdot\vec{{v}}}}{{|\vec{{u}}|\cdot|\vec{{v}}|}} = \dfrac{{1}}{{\sqrt{{2}}}} \implies (\vec{{u}}, \vec{{v}}) = 45^\circ$.'''
        elif angle_type == 60:
            u_str, v_str = "(1; 1; 0)", "(0; 1; 1)"
            ans = "60^\\circ"
            wrong1, wrong2, wrong3 = "120^\\circ", "45^\\circ", "30^\\circ"
            loi_giai = fr'''Ta có $\vec{{u}}\cdot\vec{{v}} = 1\cdot 0 + 1\cdot 1 + 0\cdot 1 = 1$. \\
$|\vec{{u}}| = \sqrt{{1^2+1^2+0^2}} = \sqrt{{2}}$, $|\vec{{v}}| = \sqrt{{0^2+1^2+1^2}} = \sqrt{{2}}$. \\
$\cos(\vec{{u}}, \vec{{v}}) = \dfrac{{\vec{{u}}\cdot\vec{{v}}}}{{|\vec{{u}}|\cdot|\vec{{v}}|}} = \dfrac{{1}}{{\sqrt{{2}}\cdot\sqrt{{2}}}} = \dfrac{{1}}{{2}} \implies (\vec{{u}}, \vec{{v}}) = 60^\circ$.'''
        else:
            u_str, v_str = "(1; 0; 1)", "(0; 1; -1)"
            ans = "120^\\circ"
            wrong1, wrong2, wrong3 = "60^\\circ", "135^\\circ", "150^\\circ"
            loi_giai = fr'''Ta có $\vec{{u}}\cdot\vec{{v}} = 1\cdot 0 + 0\cdot 1 + 1\cdot(-1) = -1$. \\
$|\vec{{u}}| = \sqrt{{1^2+0^2+1^2}} = \sqrt{{2}}$, $|\vec{{v}}| = \sqrt{{0^2+1^2+(-1)^2}} = \sqrt{{2}}$. \\
$\cos(\vec{{u}}, \vec{{v}}) = \dfrac{{\vec{{u}}\cdot\vec{{v}}}}{{|\vec{{u}}|\cdot|\vec{{v}}|}} = \dfrac{{-1}}{{\sqrt{{2}}\cdot\sqrt{{2}}}} = -\dfrac{{1}}{{2}} \implies (\vec{{u}}, \vec{{v}}) = 120^\circ$.'''
            
        caudan = fr'''Trong không gian $Oxyz$, góc giữa hai vectơ $\vec{{u}} = {u_str}$ và $\vec{{v}} = {v_str}$ bằng'''
        choices = [
            fr'''{{\True ${ans}$}}
''',
            fr'''{{${wrong1}$}}
''',
            fr'''{{${wrong2}$}}
''',
            fr'''{{${wrong3}$}}
'''
        ]
    else:
        x1, y1, z1 = [random.randint(-3, 3) for _ in range(3)]
        x2, y2, z2 = [x1 + random.randint(-3, 3) for _ in range(3)]
        x3, y3, z3 = [x1 + random.randint(-3, 3) for _ in range(3)]
        
        dx_ab, dy_ab, dz_ab = x2-x1, y2-y1, z2-z1
        dx_ac, dy_ac, dz_ac = x3-x1, y3-y1, z3-z1
        ans = dx_ab*dx_ac + dy_ab*dy_ac + dz_ab*dz_ac
        
        caudan = fr'''Trong không gian $Oxyz$, cho ba điểm $A({x1}; {y1}; {z1})$, $B({x2}; {y2}; {z2})$ và $C({x3}; {y3}; {z3})$. Tính tích vô hướng $\overrightarrow{{AB}} \cdot \overrightarrow{{AC}}$.'''
        choices = [
            fr'''{{\True ${ans}$}}
''',
            fr'''{{${ans + random.choice([2, 3, 4])}$}}
''',
            fr'''{{${ans - random.choice([2, 3, 4])}$}}
''',
            fr'''{{${-ans}$}}
'''
        ]
        loi_giai = fr'''Ta có: $\overrightarrow{{AB}} = ({dx_ab}; {dy_ab}; {dz_ab})$ và $\overrightarrow{{AC}} = ({dx_ac}; {dy_ac}; {dz_ac})$. \\
Tích vô hướng $\overrightarrow{{AB}} \cdot \overrightarrow{{AC}} = ({dx_ab})({dx_ac}) + ({dy_ab})({dy_ac}) + ({dz_ab})({dz_ac}) = {ans}$.'''
        
    random.shuffle(choices)
    return caudan, choices, loi_giai

def CuoiChuong2_MC_Cau9():
    sub = random.choice([1, 2])
    if sub == 1:
        x1, y1, z1 = [random.randint(-4, 4) for _ in range(3)]
        x2, y2, z2 = [random.randint(-4, 4) for _ in range(3)]
        x3, y3, z3 = [random.randint(-4, 4) for _ in range(3)]
        
        xd, yd, zd = x1 + x3 - x2, y1 + y3 - y2, z1 + z3 - z2
        caudan = fr'''Trong không gian $Oxyz$, cho hình bình hành $ABCD$ biết ba đỉnh $A({x1}; {y1}; {z1})$, $B({x2}; {y2}; {z2})$ và $C({x3}; {y3}; {z3})$. Tọa độ đỉnh $D$ là'''
        correct = fr'''D({xd}; {yd}; {zd})'''
        wrong1 = fr'''D({xd+1}; {yd-1}; {zd})'''
        wrong2 = fr'''D({x1+x2-x3}; {y1+y2-y3}; {z1+z2-z3})'''
        wrong3 = fr'''D({-xd}; {-yd}; {-zd})'''
        
        choices = [
            fr'''{{\True ${correct}$}}
''',
            fr'''{{${wrong1}$}}
''',
            fr'''{{${wrong2}$}}
''',
            fr'''{{${wrong3}$}}
'''
        ]
        loi_giai = fr'''Vì $ABCD$ là hình bình hành nên ta có: $\overrightarrow{{AD}} = \overrightarrow{{BC}} \iff D - A = C - B \implies D = A + C - B$. \\
Tọa độ đỉnh $D$ là: \\
$x_D = {x1} + {x3} - ({x2}) = {xd}$, \\
$y_D = {y1} + {y3} - ({y2}) = {yd}$, \\
$z_D = {z1} + {z3} - ({z2}) = {zd}$. \\
Vậy $D({xd}; {yd}; {zd})$.'''
    else:
        x_a, y_a, z_a = [random.randint(-2, 2) for _ in range(3)]
        x_b, y_b, z_b = [x_a + random.choice([2, 3]), y_a, z_a]
        x_d, y_d, z_d = [x_a, y_a + random.choice([2, 3]), z_a]
        x_ap, y_ap, z_ap = [x_a, y_a, z_a + random.choice([2, 3])]
        
        xcp = x_b + x_d + x_ap - 2*x_a
        ycp = y_b + y_d + y_ap - 2*y_a
        zcp = z_b + z_d + z_ap - 2*z_a
        
        caudan = fr'''Trong không gian $Oxyz$, cho hình hộp $ABCD.A'B'C'D'$ có $A({x_a}; {y_a}; {z_a})$, $B({x_b}; {y_b}; {z_b})$, $D({x_d}; {y_d}; {z_d})$ và $A'({x_ap}; {y_ap}; {z_ap})$. Tọa độ đỉnh $C'$ là'''
        correct = fr'''C'({xcp}; {ycp}; {zcp})'''
        wrong1 = fr'''C'({xcp-1}; {ycp}; {zcp+1})'''
        wrong2 = fr'''C'({x_b+x_d-x_a}; {y_b+y_d-y_a}; {z_b+z_d-z_a})'''
        wrong3 = fr'''C'({-xcp}; {-ycp}; {-zcp})'''
        
        choices = [
            fr'''{{\True ${correct}$}}
''',
            fr'''{{${wrong1}$}}
''',
            fr'''{{${wrong2}$}}
''',
            fr'''{{${wrong3}$}}
'''
        ]
        loi_giai = fr'''Vì $ABCD.A'B'C'D'$ là hình hộp nên $ABCD$ là hình bình hành, suy ra $C = B + D - A$. \\
Mặt khác, $\overrightarrow{{CC'}} = \overrightarrow{{AA'}} \implies C' = C + A' - A = B + D + A' - 2A$. \\
Thay số vào ta được: \\
$x_{{C'}} = {x_b} + {x_d} + {x_ap} - 2({x_a}) = {xcp}$, \\
$y_{{C'}} = {y_b} + {y_d} + {y_ap} - 2({y_a}) = {ycp}$, \\
$z_{{C'}} = {z_b} + {z_d} + {z_ap} - 2({z_a}) = {zcp}$. \\
Vậy $C'({xcp}; {ycp}; {zcp})$.'''
        
    random.shuffle(choices)
    return caudan, choices, loi_giai

def CuoiChuong2_MC_Cau10():
    sub = random.choice([1, 2])
    if sub == 1:
        caudan = fr'''Trong không gian $Oxyz$, cho tam giác $ABC$ có $A(3; 4; 2)$, $B(1; 2; 0)$ và $C(1; 2; 4)$. Tìm tọa độ chân đường cao $H$ kẻ từ đỉnh $A$ của tam giác $ABC$.'''
        correct = fr'''H(1; 2; 2)'''
        wrong1 = fr'''H(1; 2; 1)'''
        wrong2 = fr'''H(2; 3; 2)'''
        wrong3 = fr'''H(1; 2; 3)'''
        
        choices = [
            fr'''{{\True ${correct}$}}
''',
            fr'''{{${wrong1}$}}
''',
            fr'''{{${wrong2}$}}
''',
            fr'''{{${wrong3}$}}
'''
        ]
        loi_giai = fr'''Vì $H$ thuộc đường thẳng $BC$ nên $\overrightarrow{{BH}}$ cùng phương với $\overrightarrow{{BC}} = (0; 0; 4)$. \\
Suy ra $H$ có tọa độ dạng $(1; 2; z_H)$. \\
Ta có $\overrightarrow{{AH}} = (-2; -2; z_H - 2)$. \\
Vì $AH$ là đường cao nên $AH \perp BC \iff \overrightarrow{{AH}} \cdot \overrightarrow{{BC}} = 0$ \\
$\iff (-2)\cdot 0 + (-2)\cdot 0 + (z_H - 2)\cdot 4 = 0 \iff z_H = 2$. \\
Vậy $H(1; 2; 2)$.'''
    else:
        w = random.choice([6.1, 6.0])
        h = random.choice([1.55, 1.6])
        
        caudan = fr'''Một sân cầu lông có kích thước tiêu chuẩn quốc tế dài $13{{,}}4$ m và rộng ${str(w).replace(".", ",")} $ m. Thiết lập hệ trục tọa độ $Oxyz$ như hình vẽ (gốc $O$ trùng góc sân, trục $Ox$ dọc theo chiều dài, trục $Oy$ dọc theo chiều rộng, đơn vị trên mỗi trục là mét). Trụ lưới $AB$ cao ${str(h).replace(".", ",")} $ m dựng thẳng đứng tại biên dọc đối diện. Tọa độ của điểm $B$ ở đỉnh trụ lưới là'''
        correct = fr'''(6{{,}}7; {str(w).replace(".", ",")}; {str(h).replace(".", ",")})'''
        wrong1 = fr'''(13{{,}}4; {str(w).replace(".", ",")}; {str(h).replace(".", ",")})'''
        wrong2 = fr'''(6{{,}}7; 0; {str(h).replace(".", ",")})'''
        wrong3 = fr'''(0; {str(w).replace(".", ",")}; {str(h).replace(".", ",")})'''
        
        choices = [
            fr'''{{\True ${correct}$}}
''',
            fr'''{{${wrong1}$}}
''',
            fr'''{{${wrong2}$}}
''',
            fr'''{{${wrong3}$}}
'''
        ]
        loi_giai = fr'''Trụ lưới $AB$ nằm ở chính giữa chiều dài sân nên hoành độ là $x_B = \dfrac{{13{{,}}4}}{{2}} = 6{{,}}7$ m. \\
Trụ nằm trên đường biên dọc đối diện trục $Ox$ nên tung độ là $y_B = {str(w).replace(".", ",")} $ m. \\
Chiều cao đỉnh trụ là $z_B = {str(h).replace(".", ",")} $ m. \\
Vậy tọa độ của $B$ là ${correct}$.'''
        
    random.shuffle(choices)
    return caudan, choices, loi_giai

def cau27_Oxyz_them():
    fx = random.randint(1, 9)
    fy = random.randint(1, 9)
    fz = random.randint(-9, -1)
    dx = random.randint(10, 90)
    dy = random.randint(10, 90)
    dz = random.randint(-90, -10)
    ans = fx*dx + fy*dy + fz*dz
    
    caudan = fr'''Một thiết bị thăm dò đáy biển được đẩy bởi một lực $\vec{{F}} = ({fx}; {fy}; {fz})$ (đơn vị: N) giúp thiết bị thực hiện độ dời $\vec{{d}} = ({dx}; {dy}; {dz})$ (đơn vị: m). Tính công sinh bởi lực $\vec{{F}}$ (đơn vị: J).'''
    choices = [
        fr'''{{\True ${ans}$ (J)}}
''',
        fr'''{{${ans + 30}$ (J)}}
''',
        fr'''{{${ans - 30}$ (J)}}
''',
        fr'''{{${-ans}$ (J)}}
'''
    ]
    random.shuffle(choices)
    loi_giai = fr'''Công sinh bởi lực $\vec{{F}}$ thực hiện độ dời $\vec{{d}}$ là tích vô hướng: \\
$A = \vec{{F}} \cdot \vec{{d}} = ({fx})({dx}) + ({fy})({dy}) + ({fz})({dz}) = {ans}$ (J).'''
    return caudan, choices, loi_giai

def cau29_Oxyz_them():
    s = random.choice([2, 3, 4])
    caudan = fr'''Cho hình lập phương $ABCD.A'B'C'D'$ có cạnh bằng ${s}$. Với hệ tọa độ $Oxyz$ được thiết lập sao cho gốc $O$ trùng với điểm $A$, trục $Ox$ chứa điểm $B$, trục $Oy$ chứa điểm $D$, trục $Oz$ chứa điểm $A'$. Tìm tọa độ của điểm $C'$ của hình lập phương.'''
    correct = fr'''C'({s}; {s}; {s})'''
    wrong1 = fr'''C'({s}; {s}; 0)'''
    wrong2 = fr'''C'(0; 0; {s})'''
    wrong3 = fr'''C'(0; {s}; {s})'''
    
    choices = [
        fr'''{{\True ${correct}$}}
''',
        fr'''{{${wrong1}$}}
''',
        fr'''{{${wrong2}$}}
''',
        fr'''{{${wrong3}$}}
'''
    ]
    random.shuffle(choices)
    loi_giai = fr'''Vì gốc tọa độ là $A$, các trục $Ox, Oy, Oz$ đi qua $B, D, A'$. \\
Do đó: $A(0;0;0)$, $B({s};0;0)$, $D(0;{s};0)$, $A'(0;0;{s})$. \\
Đỉnh $C'$ đối diện với $A$ qua tâm hình lập phương có tọa độ là $C'({s}; {s}; {s})$.'''
    return caudan, choices, loi_giai

def cau30_Oxyz_them():
    z1 = random.randint(-4, 4)
    z2 = z1 + 2 * random.choice([-2, -1, 1, 2])
    x1, y1 = random.choice([1, 2]), random.choice([2, 3])
    x2, y2 = random.choice([-2, -1]), random.choice([-3, -2])
    zm = (z1 + z2) // 2
    
    caudan = fr'''Cho hai điểm $A({x1}; {y1}; {z1})$ và $B({x2}; {y2}; {z2})$. Gọi $M(0; 0; z)$ là điểm thuộc trục $Oz$ sao cho $MA^2 + MB^2$ đạt giá trị nhỏ nhất. Khẳng định nào sau đây là đúng?'''
    correct = fr'''z \in ({zm-1}; {zm+1})'''
    wrong1 = fr'''z \in ({zm+1}; {zm+3})'''
    wrong2 = fr'''z \in ({zm-3}; {zm-1})'''
    wrong3 = fr'''z > {zm+2}'''
    
    choices = [
        fr'''{{\True ${correct}$}}
''',
        fr'''{{${wrong1}$}}
''',
        fr'''{{${wrong2}$}}
''',
        fr'''{{${wrong3}$}}
'''
    ]
    random.shuffle(choices)

    def fmt_sq_term(z_val):
        if z_val < 0:
            return f"(z + {abs(z_val)})^2"
        elif z_val > 0:
            return f"(z - {z_val})^2"
        else:
            return "z^2"

    def fmt_linear_term(coeff):
        if coeff == 0:
            return ""
        elif coeff > 0:
            return f" + {coeff}z"
        else:
            return f" - {abs(coeff)}z"

    ma_sq_expr = fmt_sq_term(z1)
    ma_expanded = f"z^2{fmt_linear_term(-2*z1)} + {x1**2 + y1**2 + z1**2}"
    mb_sq_expr = fmt_sq_term(z2)
    mb_expanded = f"z^2{fmt_linear_term(-2*z2)} + {x2**2 + y2**2 + z2**2}"
    sum_expanded = f"2z^2{fmt_linear_term(-2*(z1+z2))} + {x1**2 + y1**2 + z1**2 + x2**2 + y2**2 + z2**2}"

    loi_giai = fr'''Ta có $MA^2 = {x1}^2 + {y1}^2 + {ma_sq_expr} = {ma_expanded}$. \\
$MB^2 = ({x2})^2 + ({y2})^2 + {mb_sq_expr} = {mb_expanded}$. \\
$MA^2 + MB^2 = {sum_expanded}$. \\
Biểu thức bậc hai đạt giá trị nhỏ nhất tại đỉnh parabol: $z = \dfrac{{{z1} + {z2}}}{{2}} = {zm}$. \\
Parabol đạt cực tiểu tại $z = {zm} \in ({zm-1}; {zm+1})$.'''
    return caudan, choices, loi_giai


# ==============================================================================
# BÀI TẬP ÔN TẬP CUỐI CHƯƠNG - SINH THEO ĐỀ THI TOÁN 12 (TOAN-01)
# ==============================================================================

import random
import math
from fractions import Fraction

def fmt_poly_deg3(a, b, c, d):
    terms = []
    if a == 1:
        terms.append("x^3")
    elif a == -1:
        terms.append("-x^3")
    elif a != 0:
        terms.append(f"{a}x^3")
        
    if b == 1:
        terms.append("+ x^2" if terms else "x^2")
    elif b == -1:
        terms.append("- x^2")
    elif b > 0:
        terms.append(f"+ {b}x^2" if terms else f"{b}x^2")
    elif b < 0:
        terms.append(f"- {abs(b)}x^2")
        
    if c == 1:
        terms.append("+ x" if terms else "x")
    elif c == -1:
        terms.append("- x")
    elif c > 0:
        terms.append(f"+ {c}x" if terms else f"{c}x")
    elif c < 0:
        terms.append(f"- {abs(c)}x")
        
    if d > 0:
        terms.append(f"+ {d}" if terms else f"{d}")
    elif d < 0:
        terms.append(f"- {abs(d)}")
    elif not terms:
        terms.append("0")
    return " ".join(terms)

def fmt_poly_deg2(a, b, c):
    terms = []
    if a == 1:
        terms.append("x^2")
    elif a == -1:
        terms.append("-x^2")
    elif a != 0:
        terms.append(f"{a}x^2")
        
    if b == 1:
        terms.append("+ x" if terms else "x")
    elif b == -1:
        terms.append("- x")
    elif b > 0:
        terms.append(f"+ {b}x" if terms else f"{b}x")
    elif b < 0:
        terms.append(f"- {abs(b)}x")
        
    if c > 0:
        terms.append(f"+ {c}" if terms else f"{c}")
    elif c < 0:
        terms.append(f"- {abs(c)}")
    elif not terms:
        terms.append("0")
    return " ".join(terms)

def fmt_frac_linear(a, b):
    terms = []
    if a == 1:
        terms.append("x")
    elif a == -1:
        terms.append("-x")
    elif a != 0:
        terms.append(f"{a}x")
        
    if b > 0:
        terms.append(f"+ {b}" if terms else f"{b}")
    elif b < 0:
        terms.append(f"- {abs(b)}")
    elif not terms:
        terms.append("0")
    return " ".join(terms)

# ==================== CHƯƠNG I - MULTIPLE CHOICE ====================

def CuoiChuong1_MC_Cau13():
    # Điểm thuộc đồ thị hàm bậc ba y = ax^3 + bx^2 + cx + d (Câu 1)
    a = random.choice([-2, -1, 1, 2])
    b = random.choice([-3, -2, 0, 2, 3])
    c = random.choice([-4, -3, 2, 3, 4])
    d = random.choice([-5, -4, -3, 3, 4, 5])
    
    def f(x):
        return a * x**3 + b * x**2 + c * x + d
        
    x0 = random.choice([-2, -1, 1, 2])
    y0 = f(x0)
    
    pts = [(x0, y0, True, 'P')]
    x_candidates = [x for x in [-3, -2, -1, 0, 1, 2, 3] if x != x0]
    random.shuffle(x_candidates)
    names = ['M', 'Q', 'N']
    for i in range(3):
        xi = x_candidates[i]
        yi_true = f(xi)
        delta = random.choice([-4, -3, -2, 2, 3, 4])
        pts.append((xi, yi_true + delta, False, names[i]))
        
    poly_str = fmt_poly_deg3(a, b, c, d)
    caudan = fr'''Điểm nào dưới đây thuộc đồ thị của hàm số $y = {poly_str}$?'''
    
    choices = []
    for pt in pts:
        xi, yi, is_true, name = pt
        if is_true:
            choices.append(fr'''{{\True ${name}({xi}; {yi})$}}
''')
        else:
            choices.append(fr'''{{${name}({xi}; {yi})$}}
''')
            
    random.shuffle(choices)
    loi_giai = fr'''Thay lần lượt tọa độ các điểm vào phương trình $y = {poly_str}$: \\
- Tại $x = {x0} \implies y = {a}({x0})^3 + {b}({x0})^2 + {c}({x0}) + {d} = {y0} \implies P({x0}; {y0})$ thuộc đồ thị hàm số. \\
Vậy điểm thuộc đồ thị hàm số là $P({x0}; {y0})$.'''
    return caudan, choices, loi_giai


def CuoiChuong1_MC_Cau14():
    # Nhận dạng hàm phân thức từ BBT (Câu 2)
    x0 = random.choice([-2, -1, 1, 2])
    y0 = random.choice([-2, -1, 1, 2])
    is_inc = random.choice([True, False])
    
    # Hàm đúng: y = (y0*x + k) / (x - x0)
    # y' = (-y0*x0 - k) / (x - x0)^2
    # Muốn y' > 0: k < -y0*x0. Muốn y' < 0: k > -y0*x0.
    if is_inc:
        k = -y0 * x0 - random.choice([1, 2, 3])
        sign_str = "+"
        tab_var = fr'''-/${y0}$, +D-/$+\infty$/$-\infty$, +/${y0}$'''
    else:
        k = -y0 * x0 + random.choice([1, 2, 3])
        sign_str = "-"
        tab_var = fr'''+/${y0}$, -D+/$-\infty$/$+\infty$, -/${y0}$'''
        
    num_correct = fmt_frac_linear(y0, k)
    den_correct = fmt_frac_linear(1, -x0)
    f_correct = fr'''y = \dfrac{{{num_correct}}}{{{den_correct}}}'''
    
    # 3 distractors:
    # w1: ngược dấu đạo hàm (đổi k)
    k_opp = -y0 * x0 + (random.choice([1, 2, 3]) if is_inc else -random.choice([1, 2, 3]))
    num_w1 = fmt_frac_linear(y0, k_opp)
    f_w1 = fr'''y = \dfrac{{{num_w1}}}{{{den_correct}}}'''
    
    # w2: sai tiệm cận đứng (mẫu x + x0)
    den_w2 = fmt_frac_linear(1, x0)
    f_w2 = fr'''y = \dfrac{{{num_correct}}}{{{den_w2}}}'''
    
    # w3: sai tiệm cận ngang
    y0_w3 = -y0 if y0 != 0 else 2
    num_w3 = fmt_frac_linear(y0_w3, k)
    f_w3 = fr'''y = \dfrac{{{num_w3}}}{{{den_correct}}}'''
    
    caudan = fr'''\immini{{Trong bốn hàm số được liệt kê ở bốn phương án A, B, C, D dưới đây, hàm số nào có bảng biến thiên sau?}}
{{\begin{{tikzpicture}}
  \tkzTabInit[nocadre,lgt=1.2,espcl=2.2,deltacl=0.5]
  {{$x$ /0.7, $y'$ /0.7, $y$ /2}}
  {{$-\infty$, ${x0}$, $+\infty$}}
  \tkzTabLine{{, {sign_str}, d, {sign_str}, }}
  \tkzTabVar{{{tab_var}}}
\end{{tikzpicture}}}}'''

    choices = [
        fr'''{{\True ${f_correct}$}}
''',
        fr'''{{${f_w1}$}}
''',
        fr'''{{${f_w2}$}}
''',
        fr'''{{${f_w3}$}}
'''
    ]
    random.shuffle(choices)
    loi_giai = fr'''Từ bảng biến thiên, ta nhận thấy: \\
- Đồ thị hàm số có đường tiệm cận đứng là $x = {x0}$ và đường tiệm cận ngang là $y = {y0}$. \\
- Đạo hàm mang dấu "${sign_str}"$ với mọi $x \neq {x0}$, tức hàm số {'đồng biến' if is_inc else 'nghịch biến'} trên các khoảng $(-\infty; {x0})$ và $({x0}; +\infty)$. \\
Hàm số thỏa mãn tất cả các điều kiện trên là ${f_correct}$.'''
    return caudan, choices, loi_giai


def CuoiChuong1_MC_Cau15():
    # Đồ thị hàm phân thức y = (ax - b)/(cx + 2), tính a + b + c (Câu 3)
    x0 = random.choice([1, 2, -1, -2])
    c = -2 // x0
    y0_options = [(-3, 2), (-1, 2), (1, 2), (3, 2), (-1, 1), (1, 1)]
    y0_num, y0_den = random.choice(y0_options)
    a = Fraction(c * y0_num, y0_den)
    x1 = random.choice([3, 4, -3, -4])
    b = a * x1
    
    T = a + b + c
    T_val = int(T) if T.denominator == 1 else float(T)
    T_str = f"{T_val}" if isinstance(T_val, int) else f"{T.numerator}/{T.denominator}"
    
    a_float = float(a)
    b_float = float(b)
    c_float = float(c)
    
    y0_tex = f"{y0_num}/{y0_den}" if y0_den != 1 else f"{y0_num}"
    
    caudan = fr'''\immini{{Cho hàm số $y = \dfrac{{ax - b}}{{cx + 2}}$ ($a, b, c \in \mathbb{{R}}; c \neq 0$) có đồ thị như hình vẽ bên. Giá trị của biểu thức $a + b + c$ bằng}}
{{\begin{{tikzpicture}}[scale=0.6, line join=round, line cap=round, >=stealth]
  \draw[->] (-3,0) -- (5,0) node[below] {{$x$}};
  \draw[->] (0,-4) -- (0,4) node[left] {{$y$}};
  \node[below left] at (0,0) {{$O$}};
  \draw[dashed] ({x0},-4) -- ({x0},4);
  \draw[dashed] (-3,{float(Fraction(y0_num, y0_den))}) -- (5,{float(Fraction(y0_num, y0_den))});
  \node[below] at ({x0},0) {{${x0}$}};
  \node[below] at ({x1},0) {{${x1}$}};
  \node[left] at (0,{float(Fraction(y0_num, y0_den))}) {{${y0_tex}$}};
  \begin{{scope}}
    \clip (-3,-4) rectangle (5,4);
    \draw[thick,smooth,samples=100,domain=-3:{x0 - 0.25}] plot (\x, {{({a_float}*\x - {b_float})/({c_float}*\x + 2)}});
    \draw[thick,smooth,samples=100,domain={x0 + 0.25}:5] plot (\x, {{({a_float}*\x - {b_float})/({c_float}*\x + 2)}});
  \end{{scope}}
\end{{tikzpicture}}}}'''

    choices = [
        fr'''{{\True ${T_str}$}}
''',
        fr'''{{${T_val + 2 if isinstance(T_val, int) else T_val + 2}$}}
''',
        fr'''{{${T_val - 2 if isinstance(T_val, int) else T_val - 2}$}}
''',
        fr'''{{${-T_val if isinstance(T_val, int) else -T_val}$}}
'''
    ]
    random.shuffle(choices)
    loi_giai = fr'''Từ đồ thị ta xác định: \\
- Tiệm cận đứng: $x = {x0} \implies c({x0}) + 2 = 0 \iff c = {c}$. \\
- Tiệm cận ngang: $y = {y0_tex} \implies \dfrac{{a}}{{c}} = {y0_tex} \iff a = {a}$. \\
- Đồ thị cắt trục hoành tại $x = {x1} \implies a({x1}) - b = 0 \iff b = {b}$. \\
Do đó: $a + b + c = {a} + {b} + ({c}) = {T_str}$.'''
    return caudan, choices, loi_giai


def CuoiChuong1_MC_Cau16():
    # Bảng xét dấu f'(x), số điểm cực tiểu (Câu 7)
    x1, x2, x3 = sorted(random.sample([-4, -3, -2, -1, 1, 2, 3, 4], 3))
    first_sign = random.choice(['-', '+'])
    
    if first_sign == '-':
        signs = ['-', '+', '-', '+']
        num_min = 2 # at x1 and x3
        num_max = 1 # at x2
    else:
        signs = ['+', '-', '+', '-']
        num_min = 1 # at x2
        num_max = 2 # at x1 and x3
        
    caudan = fr'''\immini{{Cho hàm số $y = f(x)$ có bảng xét dấu đạo hàm như hình bên. Số điểm cực tiểu của hàm số $y = f(x)$ là}}
{{\begin{{tikzpicture}}
  \tkzTabInit[nocadre,lgt=1.2,espcl=1.8,deltacl=0.5]
  {{$x$ /0.7, $f'(x)$ /0.7}}
  {{$-\infty$, ${x1}$, ${x2}$, ${x3}$, $+\infty$}}
  \tkzTabLine{{, {signs[0]}, 0, {signs[1]}, 0, {signs[2]}, 0, {signs[3]}, }}
\end{{tikzpicture}}}}'''

    choices = [
        fr'''{{\True ${num_min}$}}
''',
        fr'''{{${num_max}$}}
''',
        fr'''{{${num_min + num_max}$}}
''',
        fr'''{{${num_min + 2}$}}
'''
    ]
    random.shuffle(choices)
    loi_giai = fr'''Điểm cực tiểu là điểm mà tại đó đạo hàm $f'(x)$ đổi dấu từ âm ($-$) sang dương ($+$). \\
Dựa vào bảng xét dấu: đạo hàm $f'(x)$ đổi dấu từ $-$ sang $+$ tại {num_min} điểm. \\
Vậy số điểm cực tiểu của hàm số là ${num_min}$.'''
    return caudan, choices, loi_giai


def CuoiChuong1_MC_Cau17():
    # Khoảng đồng biến / nghịch biến của hàm căn bậc hai (Câu 8)
    # y = \sqrt{c + bx - x^2}
    x1 = random.choice([-3, -2, -1])
    x2 = x1 + 2 * random.choice([2, 3]) # x1 + x2 chẵn
    x0 = (x1 + x2) // 2
    b = x1 + x2
    c = -x1 * x2
    
    radicand_str = fmt_poly_deg2(-1, b, c)
    ask_inc = random.choice([True, False])
    
    if ask_inc:
        correct_interval = f"({x1}; {x0})"
        wrong1 = f"({x0}; {x2})"
        wrong2 = f"({x0}; +\\infty)"
        wrong3 = f"(-\\infty; {x0})"
        action_word = "đồng biến"
    else:
        correct_interval = f"({x0}; {x2})"
        wrong1 = f"({x1}; {x0})"
        wrong2 = f"({x0}; +\\infty)"
        wrong3 = f"(-\\infty; {x0})"
        action_word = "nghịch biến"
        
    caudan = fr'''Hàm số $y = \sqrt{{{radicand_str}}}$ {action_word} trên khoảng nào dưới đây?'''
    choices = [
        fr'''{{\True ${correct_interval}$}}
''',
        fr'''{{${wrong1}$}}
''',
        fr'''{{${wrong2}$}}
''',
        fr'''{{${wrong3}$}}
'''
    ]
    random.shuffle(choices)
    loi_giai = fr'''Tập xác định: ${radicand_str} \ge 0 \iff {x1} \le x \le {x2}$. \\
Đạo hàm: $y' = \dfrac{{{b} - 2x}}{{2\sqrt{{{radicand_str}}}}} = \dfrac{{{x0} - x}}{{\sqrt{{{radicand_str}}}}}$. \\
Ta có: $y' {'>' if ask_inc else '<'} 0 \iff {x0} - x {'>' if ask_inc else '<'} 0 \iff x {'<' if ask_inc else '>'} {x0}$. \\
Kết hợp tập xác định, hàm số {action_word} trên khoảng ${correct_interval}$.'''
    return caudan, choices, loi_giai


def CuoiChuong1_MC_Cau18():
    # Khẳng định sai về hàm số từ đồ thị đạo hàm f'(x) (Câu 9)
    x1 = -1
    x2 = 1
    x3 = random.choice([3, 4])
    
    caudan = fr'''\immini{{Cho hàm số $y = f(x)$ có đạo hàm trên $\mathbb{{R}}$, biết hàm số $y = f'(x)$ có đồ thị như hình vẽ bên. Khẳng định nào \textbf{{sai}} về hàm số $y = f(x)$?}}
{{\begin{{tikzpicture}}[scale=0.6, line join=round, line cap=round, >=stealth]
  \draw[->] (-2,0) -- (5.5,0) node[below] {{$x$}};
  \draw[->] (0,-2.5) -- (0,2.5) node[left] {{$y$}};
  \node[below left] at (0,0) {{$O$}};
  \node[above left] at ({x1},0) {{${x1}$}};
  \node[below left] at ({x2},0) {{${x2}$}};
  \node[below] at ({x3},0) {{${x3}$}};
  \draw[thick,smooth,samples=100,domain=-1.4:4.5] plot (\x, {{0.2*(\x - {x1})*(\x - {x2})*(\x - {x3})}});
\end{{tikzpicture}}}}'''

    choices = [
        fr'''{{\True Hàm số nghịch biến trên khoảng $(0; {x3 - 1})$}}
''',
        fr'''{{Hàm số nghịch biến trên khoảng $(-\infty; {x1})$}}
''',
        fr'''{{Hàm số nghịch biến trên khoảng $({x2}; {x3})$}}
''',
        fr'''{{Hàm số đồng biến trên khoảng $({x3}; +\infty)$}}
'''
    ]
    random.shuffle(choices)
    loi_giai = fr'''Dựa vào đồ thị hàm số đạo hàm $y = f'(x)$: \\
- $f'(x) < 0$ trên $(-\infty; {x1})$ và $({x2}; {x3}) \implies$ hàm số nghịch biến trên các khoảng đó. \\
- $f'(x) > 0$ trên $({x1}; {x2})$ và $({x3}; +\infty) \implies$ hàm số đồng biến trên các khoảng đó. \\
- Trên khoảng $(0; {x3 - 1})$, đạo hàm đổi dấu từ dương sang âm khi qua điểm $x = {x2}$, do đó hàm số không nghịch biến trên $(0; {x3 - 1})$. Khẳng định này là sai.'''
    return caudan, choices, loi_giai


def CuoiChuong1_MC_Cau19():
    # Đếm số đường tiệm cận đứng và tiệm cận ngang từ BBT (Câu 10)
    y_left = random.choice([2, 3, -1])
    y_right = random.choice([4, 5, 6])
    x0 = 1
    
    caudan = fr'''\immini{{Cho hàm số $y = f(x)$ xác định trên $\mathbb{{R}} \setminus \{{{x0}\}}$, liên tục trên mỗi khoảng xác định và có bảng biến thiên như hình sau. Hỏi đồ thị hàm số đã cho có tất cả bao nhiêu đường tiệm cận đứng và tiệm cận ngang?}}
{{\begin{{tikzpicture}}
  \tkzTabInit[nocadre,lgt=1.2,espcl=2,deltacl=0.5]
  {{$x$ /0.7, $y'$ /0.7, $y$ /2.5}}
  {{$-\infty$, ${x0}$, $2$, $+\infty$}}
  \tkzTabLine{{, -, d, -, 0, +, }}
  \tkzTabVar{{+/${y_left}$, -D+/$-\infty$/$+\infty$, -/$-2$, +/${y_right}$}}
\end{{tikzpicture}}}}'''

    choices = [
        fr'''{{\True $3$}}
''',
        fr'''{{$2$}}
''',
        fr'''{{$4$}}
''',
        fr'''{{$1$}}
'''
    ]
    random.shuffle(choices)
    loi_giai = fr'''Từ bảng biến thiên: \\
- $\lim\limits_{{x \to -\infty}} f(x) = {y_left} \implies y = {y_left}$ là 1 tiệm cận ngang. \\
- $\lim\limits_{{x \to +\infty}} f(x) = {y_right} \implies y = {y_right}$ là 1 tiệm cận ngang. \\
- $\lim\limits_{{x \to {x0}^+}} f(x) = +\infty \implies x = {x0}$ là 1 tiệm cận đứng. \\
Tổng số đường tiệm cận đứng và tiệm cận ngang là $2 + 1 = 3$.'''
    return caudan, choices, loi_giai


# ==================== CHƯƠNG II - MULTIPLE CHOICE ====================

def CuoiChuong2_MC_Cau11():
    # Tọa độ vectơ theo i, j, k (Câu 4)
    x = random.choice([-4, -3, -2, 2, 3, 4])
    y = random.choice([-4, -3, -2, 2, 3, 4])
    z = random.choice([-4, -3, -2, 2, 3, 4])
    
    def fmt_vec(coef, name):
        if coef == 1:
            return name
        elif coef == -1:
            return f"-{name}"
        else:
            return f"{coef}{name}"
            
    parts = [fmt_vec(x, r"\vec{i}")]
    parts.append(f"+ {fmt_vec(y, r'\vec{j}')}" if y > 0 else f"- {fmt_vec(abs(y), r'\vec{j}')}")
    parts.append(f"+ {fmt_vec(z, r'\vec{k}')}" if z > 0 else f"- {fmt_vec(abs(z), r'\vec{k}')}")
    vec_expr = " ".join(parts)
    
    caudan = fr'''Trong không gian $Oxyz$, cho vectơ $\vec{{a}}$ thỏa mãn $\vec{{a}} = {vec_expr}$. Tọa độ của $\vec{{a}}$ là'''
    choices = [
        fr'''{{\True $({x}; {y}; {z})$}}
''',
        fr'''{{$({x}; {z}; {y})$}}
''',
        fr'''{{$({y}; {x}; {z})$}}
''',
        fr'''{{$({-x}; {-y}; {-z})$}}
'''
    ]
    random.shuffle(choices)
    loi_giai = fr'''Theo định nghĩa tọa độ vectơ đối với hệ trục tọa độ $Oxyz$: $\vec{{a}} = x\vec{{i}} + y\vec{{j}} + z\vec{{k}} \iff \vec{{a}} = (x; y; z)$. \\
Do đó $\vec{{a}} = ({x}; {y}; {z})$.'''
    return caudan, choices, loi_giai


def CuoiChuong2_MC_Cau12():
    # Hình chiếu vuông góc của điểm lên trục tọa độ (Câu 5)
    x = random.choice([-5, -3, -2, 1, 3, 4])
    y = random.choice([-5, -4, -2, 2, 3, 5])
    z = random.choice([-5, -3, 2, 4, 5])
    
    axis = random.choice(['Ox', 'Oy', 'Oz'])
    if axis == 'Ox':
        correct = f"({x}; 0; 0)"
        w1 = f"(0; {y}; 0)"
        w2 = f"(0; 0; {z})"
        w3 = f"(0; {y}; {z})"
    elif axis == 'Oy':
        correct = f"(0; {y}; 0)"
        w1 = f"({x}; 0; 0)"
        w2 = f"(0; 0; {z})"
        w3 = f"({x}; 0; {z})"
    else:
        correct = f"(0; 0; {z})"
        w1 = f"({x}; 0; 0)"
        w2 = f"(0; {y}; 0)"
        w3 = f"({x}; {y}; 0)"
        
    caudan = fr'''Trong không gian $Oxyz$, cho điểm $A({x}; {y}; {z})$. Hình chiếu vuông góc của $A$ lên trục ${axis}$ có tọa độ là'''
    choices = [
        fr'''{{\True ${correct}$}}
''',
        fr'''{{${w1}$}}
''',
        fr'''{{${w2}$}}
''',
        fr'''{{${w3}$}}
'''
    ]
    random.shuffle(choices)
    loi_giai = fr'''Hình chiếu vuông góc của điểm $A(x_0; y_0; z_0)$ lên trục ${axis}$ giữ nguyên tọa độ tương ứng với trục ${axis}$ và các tọa độ còn lại bằng $0$. \\
Do đó hình chiếu của $A({x}; {y}; {z})$ lên trục ${axis}$ là ${correct}$.'''
    return caudan, choices, loi_giai


def CuoiChuong2_MC_Cau13():
    # Đẳng thức vectơ trong tứ diện (Câu 6)
    caudan = fr'''Cho tứ diện $ABCD$. Điểm $N$ xác định bởi đẳng thức $\vec{{AN}} = \vec{{AB}} + \vec{{AC}} - \vec{{AD}}$. Mệnh đề nào đúng?'''
    choices = [
        fr'''{{\True $N$ là đỉnh hình bình hành $CDBN$}}
''',
        fr'''{{$N$ là đỉnh hình bình hành $BCDN$}}
''',
        fr'''{{$N$ là trung điểm $BD$}}
''',
        fr'''{{$N \equiv A$}}
'''
    ]
    random.shuffle(choices)
    loi_giai = fr'''Ta có: $\vec{{AN}} = \vec{{AB}} + \vec{{AC}} - \vec{{AD}} \iff \vec{{AN}} - \vec{{AB}} = \vec{{AC}} - \vec{{AD}} \iff \vec{{BN}} = \vec{{DC}}$. \\
Đẳng thức $\vec{{BN}} = \vec{{DC}}$ chứng tỏ tứ giác $CDBN$ là hình bình hành. \\
Vậy $N$ là đỉnh hình bình hành $CDBN$.'''
    return caudan, choices, loi_giai


def CuoiChuong2_MC_Cau14():
    # Độ dài vectơ tổng |a + b + c| (Câu 11)
    a = (-2, 2, 0)
    b = (2, 2, 0)
    c = (2, 2, 2)
    ux = a[0] + b[0] + c[0]
    uy = a[1] + b[1] + c[1]
    uz = a[2] + b[2] + c[2]
    sq = ux**2 + uy**2 + uz**2 # 44 = 4 * 11 -> 2\sqrt{11}
    
    caudan = fr'''Trong không gian $Oxyz$, cho $\vec{{a}} = ({a[0]}; {a[1]}; {a[2]})$, $\vec{{b}} = ({b[0]}; {b[1]}; {b[2]})$, $\vec{{c}} = ({c[0]}; {c[1]}; {c[2]})$. Giá trị của $|\vec{{a}} + \vec{{b}} + \vec{{c}}|$ bằng'''
    choices = [
        fr'''{{\True $2\sqrt{{11}}$}}
''',
        fr'''{{$6$}}
''',
        fr'''{{$11$}}
''',
        fr'''{{$2\sqrt{{6}}$}}
'''
    ]
    random.shuffle(choices)
    loi_giai = fr'''Ta có $\vec{{u}} = \vec{{a}} + \vec{{b}} + \vec{{c}} = ({ux}; {uy}; {uz})$. \\
Độ dài $|\vec{{u}}| = \sqrt{{{ux}^2 + {uy}^2 + {uz}^2}} = \sqrt{{{sq}}} = 2\sqrt{{11}}$.'''
    return caudan, choices, loi_giai


def CuoiChuong2_MC_Cau15():
    # Số giá trị m để |u| = |v| (Câu 12)
    caudan = fr'''Trong không gian $Oxyz$, cho các vectơ $\vec{{u}} = 2\vec{{i}} - 2\vec{{j}} + \vec{{k}}$, $\vec{{v}} = (m; 2; m + 1)$ với $m$ là tham số thực. Có bao nhiêu giá trị của $m$ để $|\vec{{u}}| = |\vec{{v}}|$?'''
    choices = [
        fr'''{{\True $2$}}
''',
        fr'''{{$1$}}
''',
        fr'''{{$0$}}
''',
        fr'''{{$3$}}
'''
    ]
    random.shuffle(choices)
    loi_giai = fr'''Ta có: $|\vec{{u}}| = \sqrt{{2^2 + (-2)^2 + 1^2}} = 3$. \\
$|\vec{{v}}| = \sqrt{{m^2 + 2^2 + (m+1)^2}} = \sqrt{{2m^2 + 2m + 5}}$. \\
Điều kiện: $|\vec{{u}}| = |\vec{{v}}| \iff 2m^2 + 2m + 5 = 9 \iff m^2 + m - 2 = 0 \iff \left[\begin{{aligned}} m &= 1 \\ m &= -2 \end{{aligned}}\right.$. \\
Vậy có $2$ giá trị của $m$.'''
    return caudan, choices, loi_giai


# ==================== SHORT ANSWER (SA) ====================

def CuoiChuong1_SA_Cau11():
    # Giao điểm 2 tiệm cận xiên hàm chứa căn (Câu 17)
    p = random.choice([2, 3])
    n = random.choice([1, 2])
    q = p**2 + 1 # để trong căn luôn > 0
    
    # y = 2x + n + \sqrt{x^2 - 2px + q}
    # x -> +inf: y = 3x + n - p
    # x -> -inf: y = x + n + p
    # 3x + n - p = x + n + p <=> 2x = 2p <=> x = p, y = 2p + n
    # a + b = 3p + n
    ans = 3 * p + n
    
    caudan = fr'''Cho hàm số $y = 2x + {n} + \sqrt{{x^2 - {2*p}x + {q}}}$. Biết đồ thị hàm số có hai tiệm cận xiên cắt nhau tại $I(a; b)$. Tính $a + b$.'''
    dapan = f"{ans}"
    loi_giai = fr'''Tập xác định: $D = \mathbb{{R}}$ vì $x^2 - {2*p}x + {q} = (x - {p})^2 + 1 > 0, \forall x \in \mathbb{{R}}$. \\
- Khi $x \to +\infty$: tiệm cận xiên là đường thẳng $(d_1): y = 3x + {n - p}$. \\
- Khi $x \to -\infty$: tiệm cận xiên là đường thẳng $(d_2): y = x + {n + p}$. \\
Giao điểm $I(a; b)$ của $(d_1)$ và $(d_2)$ thỏa mãn: $3a + {n - p} = a + {n + p} \iff a = {p} \implies b = {2*p + n}$. \\
Suy ra $a + b = {p} + {2*p + n} = {ans}$.'''
    return caudan, dapan, loi_giai


def CuoiChuong1_SA_Cau12():
    # Nhận dạng hệ số hàm phân thức y = (ax+1)/(cx+d), tính a + c + d (Câu 18)
    a = 2
    c = 1
    d = -1
    ans = a + c + d # 2
    
    caudan = fr'''\immini{{Cho hàm số $y = f(x) = \dfrac{{ax + 1}}{{cx + d}}$ ($a, c, d \in \mathbb{{R}}$) có đồ thị như hình vẽ bên. Tính giá trị của biểu thức $T = a + c + d$.}}
{{\begin{{tikzpicture}}[scale=0.6, line join=round, line cap=round, >=stealth]
  \draw[->] (-2.5,0) -- (4,0) node[below] {{$x$}};
  \draw[->] (0,-3) -- (0,4) node[left] {{$y$}};
  \node[below left] at (0,0) {{$O$}};
  \draw[dashed] (1,-3) -- (1,4);
  \draw[dashed] (-2.5,2) -- (4,2);
  \node[below left] at (1,0) {{$1$}};
  \node[left] at (0,2) {{$2$}};
  \node[below left] at (0,-1) {{$-1$}};
  \node[below] at (-0.5,0) {{$-\frac{{1}}{{2}}$}};
  \fill (0,-1) circle (1.5pt);
  \fill (-0.5,0) circle (1.5pt);
  \begin{{scope}}
    \clip (-2.5,-3) rectangle (4,4);
    \draw[thick,smooth,samples=100,domain=-2.5:0.75] plot (\x, {{(2*\x + 1)/(\x - 1)}});
    \draw[thick,smooth,samples=100,domain=1.25:4] plot (\x, {{(2*\x + 1)/(\x - 1)}});
  \end{{scope}}
\end{{tikzpicture}}}}'''
    dapan = f"{ans}"
    loi_giai = fr'''Dựa vào đồ thị hàm số: \\
- Cắt trục tung tại $(0; -1) \implies \dfrac{{1}}{{d}} = -1 \iff d = -1$. \\
- Tiệm cận đứng $x = 1 \implies c(1) + d = 0 \iff c = 1$. \\
- Tiệm cận ngang $y = 2 \implies \dfrac{{a}}{{c}} = 2 \iff a = 2$. \\
Vậy $T = a + c + d = 2 + 1 + (-1) = {ans}$.'''
    return caudan, dapan, loi_giai


# ==================== TRUE / FALSE (TF) ====================

def CuoiChuong1_TF_Cau1():
    # Khảo sát hàm số bậc ba y = x^3 - 3x + 1 (Câu 13)
    caudan = fr'''Cho hàm số $y = x^3 - 3x + 1$.'''
    choices = [
        fr'''{{\True Điểm cực tiểu của hàm số là $x = 1$.}}
''',
        fr'''{{Hàm số đồng biến trên khoảng $(-1; 1)$.}}
''',
        fr'''{{\True Giá trị lớn nhất của hàm số đã cho trên đoạn $[-1; 5]$ là $111$.}}
''',
        fr'''{{Gọi $A, B$ lần lượt là điểm cực đại và điểm cực tiểu của đồ thị hàm số. Khi đó, diện tích tam giác $ABC$ bằng $2$ với $C(-1; 2)$.}}
'''
    ]
    loi_giai = fr'''\begin{{itemize}}
  \item $y' = 3x^2 - 3 = 0 \iff x = \pm 1$; $y''(1) = 6 > 0 \implies x = 1$ là điểm cực tiểu. (Ý a \textbf{{Đúng}})
  \item Trên $(-1; 1)$, $y' < 0 \implies$ hàm số nghịch biến. (Ý b \textbf{{Sai}})
  \item $y(-1) = 3, y(1) = -1, y(5) = 111 \implies \max\limits_{{[-1; 5]}} y = 111$. (Ý c \textbf{{Đúng}})
  \item $A(-1; 3), B(1; -1), C(-1; 2)$. Đoạn $AC = 1$, khoảng cách từ $B$ đến đường thẳng $AC$ ($x = -1$) là $h = 2$. Suy ra $S_{{ABC}} = \dfrac{{1}}{{2}} \cdot 1 \cdot 2 = 1 \neq 2$. (Ý d \textbf{{Sai}})
\end{{itemize}}'''
    return caudan, choices, loi_giai


def CuoiChuong1_TF_Cau2():
    # Tối ưu hóa lợi nhuận bán vải thiều (Câu 15)
    caudan = fr'''Một cửa hàng bán vải thiều với giá bán là $30000$ đồng/1kg. Giá nhập vào là $16000$ đồng/1kg. Với giá này cửa hàng ước chừng bán được $100$ kg/ngày. Cửa hàng dự định giảm giá bán, ước tính cứ giảm $1000$ đồng/1kg thì số vải thiều bán được sẽ tăng thêm là $10$ kg.'''
    choices = [
        fr'''{{\True Nếu giữ nguyên giá ban đầu, lợi nhuận theo ngày của cửa hàng là $1400000$ đồng.}}
''',
        fr'''{{Nếu giá bán là $20000$ đồng/1kg, cửa hàng bán được $250$ kg/ngày.}}
''',
        fr'''{{\True Gọi $x$ (nghìn đồng) là giá tiền mà cửa hàng dự định bán ($16 < x < 30$), khi đó lợi nhuận theo ngày của cửa hàng được xác định bởi hàm số $f(x) = (x - 16)(400 - 10x)$.}}
''',
        fr'''{{Lợi nhuận tối đa theo ngày của cửa hàng là $1600000$ đồng.}}
'''
    ]
    loi_giai = fr'''\begin{{itemize}}
  \item Lợi nhuận ban đầu: $(30000 - 16000) \times 100 = 1400000$ đồng/ngày. (Ý a \textbf{{Đúng}})
  \item Giá bán $20000$ đồng/kg (giảm $10000$ đồng) thì số lượng bán tăng $10 \times 10 = 100$ kg $\implies$ tổng lượng bán $200$ kg/ngày $\neq 250$ kg/ngày. (Ý b \textbf{{Sai}})
  \item Với giá $x$ nghìn đồng, giảm $30 - x$ nghìn đồng $\implies$ số lượng bán là $100 + 10(30 - x) = 400 - 10x$. Lợi nhuận $f(x) = (x - 16)(400 - 10x)$. (Ý c \textbf{{Đúng}})
  \item $f(x) = -10(x - 16)(x - 40)$ đạt cực đại tại $x = 28$ với lợi nhuận tối đa $f(28) = 1440$ nghìn đồng $= 1440000$ đồng. (Ý d \textbf{{Sai}})
\end{{itemize}}'''
    return caudan, choices, loi_giai


def CuoiChuong2_TF_Cau1():
    # Vectơ trong hình lập phương (Câu 14)
    caudan = fr'''Cho hình lập phương $ABCD.A'B'C'D'$ cạnh $a$. Gọi $M$ là giao điểm của $CD'$ và $C'D$.'''
    choices = [
        fr'''{{\True $\vec{{DC'}} = \vec{{DC}} + \vec{{DD'}}$.}}
''',
        fr'''{{\True $\vec{{AD'}} \cdot \vec{{CC'}} = a^2$.}}
''',
        fr'''{{\True $\vec{{AM}} = \dfrac{{1}}{{2}}\vec{{AB}} + \vec{{AD}} + \dfrac{{1}}{{2}}\vec{{AA'}}$.}}
''',
        fr'''{{Góc giữa $A'C$ và $BD$ là $60^\circ$.}}
'''
    ]
    loi_giai = fr'''\begin{{itemize}}
  \item Trong hình vuông $CDD'C'$, theo quy tắc hình bình hành $\vec{{DC'}} = \vec{{DC}} + \vec{{DD'}}$. (Ý a \textbf{{Đúng}})
  \item $\vec{{AD'}} \cdot \vec{{CC'}} = (\vec{{AD}} + \vec{{DD'}}) \cdot \vec{{DD'}} = a^2$. (Ý b \textbf{{Đúng}})
  \item $M$ là trung điểm $CD' \implies \vec{{AM}} = \dfrac{{1}}{{2}}(\vec{{AC}} + \vec{{AD'}}) = \dfrac{{1}}{{2}}\vec{{AB}} + \vec{{AD}} + \dfrac{{1}}{{2}}\vec{{AA'}}$. (Ý c \textbf{{Đúng}})
  \item $BD \perp AC$ và $BD \perp AA' \implies BD \perp (ACC'A') \implies BD \perp A'C \implies$ góc bằng $90^\circ \neq 60^\circ$. (Ý d \textbf{{Sai}})
\end{{itemize}}'''
    return caudan, choices, loi_giai


def CuoiChuong2_TF_Cau2():
    # Vectơ lực cần cẩu kéo khung sắt (Câu 16)
    caudan = fr'''\immini{{Một chiếc ô tô được đặt trên mặt đáy dưới của một khung sắt có dạng hình hộp chữ nhật với đáy trên là hình chữ nhật $ABCD$, mặt phẳng $(ABCD)$ song song với mặt phẳng nằm ngang. Khung sắt đó được buộc vào móc $E$ của chiếc cần cẩu sao cho các đoạn dây cáp $EA, EB, EC, ED$ có độ dài bằng nhau và cùng tạo với mặt phẳng $(ABCD)$ một góc bằng $60^\circ$. Chiếc cần cẩu kéo khung sắt lên theo phương thẳng đứng. Biết rằng các lực căng $\vec{{F}}_1, \vec{{F}}_2, \vec{{F}}_3, \vec{{F}}_4$ đều có cường độ là $4500\text{{ N}}$ và trọng lượng của khung sắt là $2900\text{{ N}}$. Xét tính đúng sai của các mệnh đề sau:}}
{{\begin{{tikzpicture}}[scale=0.6, line join=round, line cap=round, >=stealth]
  \coordinate (A) at (0,1);
  \coordinate (B) at (1.2,0);
  \coordinate (C) at (4,0.3);
  \coordinate (D) at (2.8,1.3);
  \coordinate (E) at (2,4);
  \draw[dashed] (A) -- (D) -- (C);
  \draw (A) -- (B) -- (C);
  \draw[->,thick] (E) -- (A) node[midway, left] {{$\vec{{F}}_1$}};
  \draw[->,thick] (E) -- (B) node[midway, left] {{$\vec{{F}}_2$}};
  \draw[->,thick] (E) -- (C) node[midway, right] {{$\vec{{F}}_3$}};
  \draw[->,thick,dashed] (E) -- (D) node[midway, right] {{$\vec{{F}}_4$}};
  \node[left] at (A) {{$A$}};
  \node[below left] at (B) {{$B$}};
  \node[right] at (C) {{$C$}};
  \node[above right] at (D) {{$D$}};
  \node[above] at (E) {{$E$}};
\end{{tikzpicture}}}}'''
    choices = [
        fr'''{{$\vec{{F}}_1 + \vec{{F}}_2 = \vec{{F}}_3 + \vec{{F}}_4$.}}
''',
        fr'''{{\True $\vec{{F}}_1 + \vec{{F}}_3 = \vec{{F}}_2 + \vec{{F}}_4$.}}
''',
        fr'''{{$|\vec{{F}}_1 + \vec{{F}}_3| = 8000\text{{ N}}$ (làm tròn đến hàng đơn vị).}}
''',
        fr'''{{\True Trọng lượng của chiếc xe ô tô là $12688\text{{ N}}$ (làm tròn đến hàng đơn vị).}}
'''
    ]
    loi_giai = fr'''\begin{{itemize}}
  \item Tổng lực $\vec{{F}}_1 + \vec{{F}}_3$ và $\vec{{F}}_2 + \vec{{F}}_4$ đều có phương thẳng đứng (dọc theo $EO$), do đó $\vec{{F}}_1 + \vec{{F}}_3 = \vec{{F}}_2 + \vec{{F}}_4$. (Ý b \textbf{{Đúng}}, Ý a \textbf{{Sai}})
  \item Góc giữa $\vec{{F}}_1$ và $\vec{{F}}_3$ bằng $60^\circ \implies |\vec{{F}}_1 + \vec{{F}}_3| = 2 \cdot 4500 \cdot \cos 30^\circ = 4500\sqrt{{3}} \approx 7794\text{{ N}} \neq 8000\text{{ N}}$. (Ý c \textbf{{Sai}})
  \item Tổng lực nâng: $F = 2 \cdot 4500\sqrt{{3}} = 9000\sqrt{{3}} \approx 15588\text{{ N}}$. Trọng lượng xe ô tô: $9000\sqrt{{3}} - 2900 \approx 12688\text{{ N}}$. (Ý d \textbf{{Đúng}})
\end{{itemize}}'''
    return caudan, choices, loi_giai


# ==============================================================================
# BÀI TẬP ÔN TẬP CUỐI CHƯƠNG - SINH THEO ĐỀ KHẢO SÁT HÀM SỐ (TOAN-03)
# ==============================================================================


def fmt_linear(a, b):
    # ax + b
    terms = []
    if a == 1:
        terms.append("x")
    elif a == -1:
        terms.append("-x")
    elif a != 0:
        terms.append(f"{a}x")
        
    if b > 0:
        terms.append(f"+ {b}" if terms else f"{b}")
    elif b < 0:
        terms.append(f"- {abs(b)}")
    elif not terms:
        terms.append("0")
    return " ".join(terms)

def CuoiChuong1_MC_Cau20():
    # Tiệm cận xiên của y = ax + b + c/(x + d)
    a = random.choice([-3, -2, -1, 1, 2, 3])
    b = random.choice([-4, -3, -2, -1, 1, 2, 3, 4])
    c = random.choice([-5, -4, -3, -2, 2, 3, 4, 5])
    d = random.choice([-4, -3, -2, -1, 1, 2, 3, 4])
    
    lin_str = fmt_linear(a, b)
    den_str = fmt_linear(1, d)
    c_sign = "+" if c > 0 else "-"
    abs_c = abs(c)
    
    caudan = fr'''Đường tiệm cận xiên của đồ thị hàm số $y = {lin_str} {c_sign} \dfrac{{{abs_c}}}{{{den_str}}}$ có phương trình là'''
    
    ans_str = f"y = {lin_str}"
    w1 = f"y = {fmt_linear(a, -b)}"
    w2 = f"y = {fmt_linear(-a, b)}"
    w3 = f"y = {fmt_linear(-a, -b)}"
    
    choices = [
        fr'''{{\True ${ans_str}$}}
''',
        fr'''{{${w1}$}}
''',
        fr'''{{${w2}$}}
''',
        fr'''{{${w3}$}}
'''
    ]
    random.shuffle(choices)
    loi_giai = fr'''Ta có $\lim\limits_{{x \to \pm\infty}} [y - ({lin_str})] = \lim\limits_{{x \to \pm\infty}} \left({c_sign}\dfrac{{{abs_c}}}{{{den_str}}}\right) = 0$. \\
Vậy đường tiệm cận xiên của đồ thị hàm số là ${ans_str}$.'''
    return caudan, choices, loi_giai


def CuoiChuong1_MC_Cau21():
    # Khoảng nghịch biến của hàm trùng phương từ BBT
    x0 = random.choice([1, 2])
    y_inf = "+/+\\infty"
    caudan = fr'''\immini{{Cho hàm số $y = f(x)$ có bảng biến thiên như sau. Hàm số đã cho nghịch biến trên khoảng nào sau đây?}}
{{\begin{{tikzpicture}}
  \tkzTabInit[nocadre,lgt=1.2,espcl=1.3,deltacl=0.4]
  {{$x$ /0.6, $y'$ /0.6, $y$ /1.5}}
  {{$-\infty$, ${-x0}$, $0$, ${x0}$, $+\infty$}}
  \tkzTabLine{{, -, 0, +, 0, -, 0, +, }}
  \tkzTabVar{{+/$+\infty$, -/$0$, +/$3$, -/$0$, +/$+\infty$}}
\end{{tikzpicture}}}}'''

    choices = [
        fr'''{{\True $(0; {x0})$}}
''',
        fr'''{{$(0; +\infty)$}}
''',
        fr'''{{$({-x0}; 0)$}}
''',
        fr'''{{$({x0}; +\infty)$}}
'''
    ]
    random.shuffle(choices)
    loi_giai = fr'''Dựa vào bảng biến thiên, ta thấy $y' < 0$ trên các khoảng $(-\infty; {-x0})$ và $(0; {x0})$. \\
Do đó hàm số nghịch biến trên khoảng $(0; {x0})$.'''
    return caudan, choices, loi_giai


def CuoiChuong1_MC_Cau22():
    # GTLN của hàm bậc ba f(x) = x^3 - 3x^2 - 9x + d trên [-2; 2]
    d = random.choice([5, 8, 10, 12])
    def f(x):
        return x**3 - 3*x**2 - 9*x + d
        
    val_neg2 = f(-2)
    val_neg1 = f(-1) # max
    val_pos2 = f(2)
    max_val = val_neg1
    
    caudan = fr'''Giá trị lớn nhất của hàm số $f(x) = x^3 - 3x^2 - 9x + {d}$ trên đoạn $[-2; 2]$ bằng'''
    choices = [
        fr'''{{\True ${max_val}$}}
''',
        fr'''{{${val_neg2}$}}
''',
        fr'''{{${val_pos2}$}}
''',
        fr'''{{${d}$}}
'''
    ]
    random.shuffle(choices)
    loi_giai = fr'''Ta có $f'(x) = 3x^2 - 6x - 9 = 3(x + 1)(x - 3)$. \\
$f'(x) = 0 \iff x = -1 \in [-2; 2]$ (loại nghiệm $x = 3 \notin [-2; 2]$). \\
Tính giá trị: \\
$f(-2) = {val_neg2}$. \\
$f(-1) = {val_neg1}$. \\
$f(2) = {val_pos2}$. \\
Vậy giá trị lớn nhất của hàm số trên đoạn $[-2; 2]$ bằng ${max_val}$.'''
    return caudan, choices, loi_giai


def CuoiChuong1_MC_Cau23():
    # Hàm số y = x^3 - 3k x^2 - c nghịch biến trên khoảng nào
    k = random.choice([1, 2, 3])
    c = random.choice([2024, 2025, 2026])
    b = 3 * k
    caudan = fr'''Hàm số $y = x^3 - {b}x^2 - {c}$ nghịch biến trên khoảng nào sau đây?'''
    choices = [
        fr'''{{\True $(0; {2*k})$}}
''',
        fr'''{{$(-\infty; 0)$}}
''',
        fr'''{{$({2*k}; +\infty)$}}
''',
        fr'''{{$(-\infty; +\infty)$}}
'''
    ]
    random.shuffle(choices)
    loi_giai = fr'''Ta có $y' = 3x^2 - {2*b}x = 3x(x - {2*k})$. \\
$y' < 0 \iff 0 < x < {2*k}$. \\
Vậy hàm số nghịch biến trên khoảng $(0; {2*k})$.'''
    return caudan, choices, loi_giai


def CuoiChuong1_MC_Cau24():
    # Giá trị cực đại của hàm bậc ba từ đồ thị
    caudan = fr'''\immini{{Cho hàm số $y = ax^3 + bx^2 + cx + d \; (a,b,c,d \in \mathbb{{R}}, a \neq 0)$ có đồ thị là đường cong như hình bên. Giá trị cực đại của hàm số đã cho bằng}}
{{\begin{{tikzpicture}}[scale=0.6, line join=round, line cap=round, >=stealth,font=\footnotesize]
	\def\xmin{{-2.2}}\def\xmax{{2.2}}\def\ymin{{-4.2}}\def\ymax{{1}}
	\draw[->] (\xmin-0.2,0)--(\xmax+0.2,0) node[below]{{$x$}};
	\draw[->] (0,\ymin-0.2)--(0,\ymax+0.2) node[right]{{$y$}};
	\draw (0,0) node[below left]{{$O$}};
	\foreach \x in {{-2,-1,1,2}}\draw (\x,0.1)--(\x,-0.1) node[below]{{$\x$}};
	\foreach \y in {{-4,-3,-2,-1}}\draw (0.1,\y)--(-0.1,\y) node[left]{{$\y$}};
	\clip (\xmin,\ymin) rectangle (\xmax,\ymax);
	\draw[thick,smooth,samples=200,domain=\xmin:\xmax] plot (\x,{{1*((\x)^3)+0*((\x)^2)+-3*(\x)+-2}});
	\fill (-1,0) circle(1.5pt);
	\draw[dashed] (1,0)--(1,-4)--(0,-4);\fill (1,-4) circle(1.5pt);
\end{{tikzpicture}}}}'''
    choices = [
        fr'''{{\True $0$}}
''',
        fr'''{{$1$}}
''',
        fr'''{{$3$}}
''',
        fr'''{{$-1$}}
'''
    ]
    random.shuffle(choices)
    loi_giai = fr'''Từ đồ thị hàm số, điểm cực đại của đồ thị là $(-1; 0)$. \\
Do đó giá trị cực đại của hàm số đã cho bằng $y = 0$.'''
    return caudan, choices, loi_giai


def CuoiChuong1_MC_Cau25():
    # Tâm đối xứng của đồ thị y = (ax+b)/(cx+d)
    a = random.choice([2, 3, -2, -3])
    b = random.choice([-3, -1, 1, 3])
    d = random.choice([-4, -3, -2, 2, 3, 4])
    # y = (ax+b)/(x+d) -> TCĐ: x = -d, TCN: y = a
    x_tc = -d
    y_tc = a
    num_str = fmt_linear(a, b)
    den_str = fmt_linear(1, d)
    caudan = fr'''Đồ thị hàm số $y = \dfrac{{{num_str}}}{{{den_str}}}$ có tâm đối xứng là điểm nào sau đây?'''
    choices = [
        fr'''{{\True $I({x_tc}; {y_tc})$}}
''',
        fr'''{{$I({-x_tc}; {y_tc})$}}
''',
        fr'''{{$I({x_tc}; {-y_tc})$}}
''',
        fr'''{{$I({y_tc}; {x_tc})$}}
'''
    ]
    random.shuffle(choices)
    loi_giai = fr'''Tiệm cận đứng là $x = {x_tc}$. \\
Tiệm cận ngang là $y = {y_tc}$. \\
Tâm đối xứng của đồ thị hàm phân thức bậc nhất trên bậc nhất là giao điểm của hai đường tiệm cận, tức là $I({x_tc}; {y_tc})$.'''
    return caudan, choices, loi_giai


def CuoiChuong1_MC_Cau26():
    # Số điểm cực trị của hàm số có f'(x) = x^2 (x - a) (x - b)
    a = random.choice([-3, -2, -1])
    b = random.choice([1, 2, 3])
    caudan = fr'''Cho hàm số $y=f(x)$ có đạo hàm $f'(x) = x^2(x {"+" if -a > 0 else "-"} {abs(a)})(x - {b}), \; \forall x \in \mathbb{{R}}$. Số điểm cực trị của hàm số đã cho là'''
    choices = [
        fr'''{{\True $2$}}
''',
        fr'''{{$1$}}
''',
        fr'''{{$3$}}
''',
        fr'''{{$0$}}
'''
    ]
    random.shuffle(choices)
    loi_giai = fr'''Ta có $f'(x) = 0 \iff x = 0$ (nghiệm bội $2$) hoặc $x = {a}$ (nghiệm đơn) hoặc $x = {b}$ (nghiệm đơn). \\
Đạo hàm chỉ đổi dấu khi qua các nghiệm đơn $x = {a}$ và $x = {b}$, không đổi dấu khi qua nghiệm bội chẵn $x = 0$. \\
Vậy hàm số có đúng $2$ điểm cực trị.'''
    return caudan, choices, loi_giai


def CuoiChuong1_MC_Cau27():
    # So sánh giá trị hàm số từ đạo hàm f'(x) = x(x - 4)
    caudan = fr'''Cho hàm số $y=f(x)$ có đạo hàm $f'(x) = x(x - 4), \; \forall x \in \mathbb{{R}}$. Mệnh đề nào sau đây đúng?'''
    choices = [
        fr'''{{\True $f(0) > f(2)$}}
''',
        fr'''{{$f(0) = f(4)$}}
''',
        fr'''{{$f(4) > f(0)$}}
''',
        fr'''{{$f(4) > f(2)$}}
'''
    ]
    random.shuffle(choices)
    loi_giai = fr'''Ta có $f'(x) < 0 \iff 0 < x < 4$, do đó hàm số $y = f(x)$ nghịch biến trên đoạn $[0; 4]$. \\
Vì $0 < 2 < 4$ nên $f(0) > f(2) > f(4)$. \\
Do đó mệnh đề $f(0) > f(2)$ là đúng.'''
    return caudan, choices, loi_giai


def CuoiChuong1_MC_Cau28():
    # Nhận dạng đồ thị hàm phân thức 2 trên 1
    caudan = fr'''\immini{{Đồ thị ở hình bên là của một trong bốn hàm số nào sau đây?}}
{{\begin{{tikzpicture}}[scale=0.6, line join=round, line cap=round, >=stealth,font=\footnotesize]
	\def\xmin{{-1.5}}\def\xmax{{4.5}}\def\ymin{{-3.5}}\def\ymax{{6.5}}
	\draw[->] (\xmin-0.2,0)--(\xmax+0.2,0) node[below]{{$x$}};
	\draw[->] (0,\ymin-0.2)--(0,\ymax+0.2) node[right]{{$y$}};
	\draw (0,0) node[below left]{{$O$}};
	\clip (\xmin,\ymin) rectangle (\xmax,\ymax);
	\draw[dashed] (2,\ymin)--(2,\ymax);
	\draw[dashed] (\xmin,{{\xmin + 1}})--(\xmax,{{\xmax + 1}});
	\draw[thick,smooth,samples=150,domain=\xmin:1.85] plot (\x,{{((\x)^2 - (\x) - 1)/((\x) - 2)}});
	\draw[thick,smooth,samples=150,domain=2.15:\xmax] plot (\x,{{((\x)^2 - (\x) - 1)/((\x) - 2)}});
	\fill (1,1) circle (1.5pt); \draw[dashed] (1,0)--(1,1)--(0,1);
	\fill (3,5) circle (1.5pt); \draw[dashed] (3,0)--(3,5)--(0,5);
	\node[below] at (2,0) {{$2$}};
\end{{tikzpicture}}}}'''
    choices = [
        fr'''{{\True $y=\dfrac{{x^2-x-1}}{{x-2}}$}}
''',
        fr'''{{$y=\dfrac{{-x^2+x-1}}{{x-2}}$}}
''',
        fr'''{{$y=\dfrac{{x^2-2x-1}}{{x-2}}$}}
''',
        fr'''{{$y=\dfrac{{x^2-x+1}}{{x+2}}$}}
'''
    ]
    random.shuffle(choices)
    loi_giai = fr'''Đồ thị hàm số có: \\
- Tiệm cận đứng $x = 2$, tiệm cận xiên $y = x + 1$. \\
- Điểm cực đại $(1; 1)$, điểm cực tiểu $(3; 5)$. \\
Xét hàm số $y = \dfrac{{x^2-x-1}}{{x-2}} = x + 1 + \dfrac{{1}}{{x-2}}$ thỏa mãn tất cả các tính chất trên.'''
    return caudan, choices, loi_giai


def CuoiChuong1_MC_Cau29():
    # Số điểm cực trị của hàm phân thức bậc 1 trên 1
    a = random.choice([2, 3, 4])
    b = random.choice([-5, -3, 1, 5])
    d = random.choice([-4, -2, 2, 4])
    num_str = fmt_linear(a, b)
    den_str = fmt_linear(1, d)
    caudan = fr'''Số điểm cực trị của hàm số $y = \dfrac{{{num_str}}}{{{den_str}}}$ là'''
    choices = [
        fr'''{{\True $0$}}
''',
        fr'''{{$1$}}
''',
        fr'''{{$2$}}
''',
        fr'''{{vô số}}
'''
    ]
    random.shuffle(choices)
    loi_giai = fr'''Hàm số phân thức bậc nhất trên bậc nhất có đạo hàm $y' = \dfrac{{{a*d - b}}}{{({den_str})^2}}$ luôn cùng một dấu trên từng khoảng xác định. \\
Đạo hàm không có nghiệm, do đó hàm số không có điểm cực trị.'''
    return caudan, choices, loi_giai


def CuoiChuong1_MC_Cau30():
    # Tổng M + m từ đồ thị
    caudan = fr'''\immini{{Cho hàm số $y=f(x)$ liên tục trên đoạn $[-1;5]$ và có đồ thị như hình bên. Gọi $M$ và $m$ lần lượt là giá trị lớn nhất và nhỏ nhất của hàm số đã cho trên đoạn $[-1;5]$. Giá trị của $M+m$ bằng}}
{{\begin{{tikzpicture}}[scale=0.6, line join=round, line cap=round, >=stealth,font=\footnotesize]
	\draw[->] (-1.5,0)--(5.5,0) node[below]{{$x$}};
	\draw[->] (0,-2.5)--(0,3.5) node[right]{{$y$}};
	\draw (0,0) node[below left]{{$O$}};
	\draw[thick] (-1,3) -- (1,-2) -- (3,1) -- (5,-1);
	\draw[dashed] (-1,0)--(-1,3)--(0,3);
	\draw[dashed] (1,0)--(1,-2)--(0,-2);
	\draw[dashed] (3,0)--(3,1)--(0,1);
	\draw[dashed] (5,0)--(5,-1)--(0,-1);
	\node[below] at (-1,0) {{$-1$}};
	\node[above] at (1,0) {{$1$}};
	\node[below] at (3,0) {{$3$}};
	\node[above] at (5,0) {{$5$}};
	\node[left] at (0,3) {{$3$}};
	\node[left] at (0,-2) {{$-2$}};
	\node[left] at (0,1) {{$1$}};
	\node[left] at (0,-1) {{$-1$}};
\end{{tikzpicture}}}}'''
    choices = [
        fr'''{{\True $1$}}
''',
        fr'''{{$-1$}}
''',
        fr'''{{$4$}}
''',
        fr'''{{$2$}}
'''
    ]
    random.shuffle(choices)
    loi_giai = fr'''Dựa vào đồ thị trên đoạn $[-1; 5]$: \\
- Giá trị lớn nhất $M = \max\limits_{{[-1; 5]}} f(x) = 3$ (tại $x = -1$). \\
- Giá trị nhỏ nhất $m = \min\limits_{{[-1; 5]}} f(x) = -2$ (tại $x = 1$). \\
Vậy $M + m = 3 + (-2) = 1$.'''
    return caudan, choices, loi_giai


# ==================== SHORT ANSWER (SA) ====================

def CuoiChuong1_SA_Cau13():
    # Hàm căn thức y = \sqrt{-x^2 + 2bx} đồng biến trên (a; b) với a, b tự nhiên. Tính a + b.
    b = random.choice([1, 2, 3])
    caudan = fr'''Biết rằng hàm số $y=\sqrt{{-x^2 + {2*b}x}}$ đồng biến trên khoảng $(a;b)$ với $a,b$ là các số tự nhiên. Tính giá trị của $a+b$.'''
    ans = b
    dapan = f"{ans}"
    loi_giai = fr'''Tập xác định: $-x^2 + {2*b}x \ge 0 \iff 0 \le x \le {2*b}$. \\
Đạo hàm: $y' = \dfrac{{{b} - x}}{{\sqrt{{-x^2 + {2*b}x}}}} > 0 \iff x < {b}$. \\
Kết hợp điều kiện, hàm số đồng biến trên khoảng $(0; {b})$. \\
Vì $a, b \in \mathbb{{N}}$ nên $a = 0, b = {b} \implies a + b = {ans}$.'''
    return caudan, dapan, loi_giai


def CuoiChuong1_SA_Cau14():
    # Độ dài đoạn nối hai cực trị của y = x^2 / (x + 1)
    caudan = fr'''Đồ thị hàm số $y=\dfrac{{x^2}}{{x+1}}$ có hai điểm cực trị $A$ và $B$. Tính độ dài đoạn thẳng $AB$ \textit{{(kết quả quy tròn đến hàng phần trăm)}}.'''
    dapan = "4,47"
    loi_giai = fr'''Ta có $y' = \dfrac{{x^2 + 2x}}{{(x+1)^2}} = 0 \iff \left[\begin{{aligned}} x &= 0 \implies y = 0 \\ x &= -2 \implies y = -4 \end{{aligned}}\right.$. \\
Tọa độ hai điểm cực trị là $A(0; 0)$ và $B(-2; -4)$. \\
Độ dài $AB = \sqrt{{(-2)^2 + (-4)^2}} = \sqrt{{20}} = 2\sqrt{{5}} \approx 4{{,}}47$.'''
    return caudan, dapan, loi_giai


def CuoiChuong1_SA_Cau15():
    # Cực đại tại a, cực tiểu tại b của f(x) = x^3 - 6x^2 + 9x - 5, tính a^3 - b^3
    caudan = fr'''Giả sử hàm số $f(x) = x^3 - 6x^2 + 9x - 5$ đạt cực đại tại $x=a$ và đạt cực tiểu tại $x=b$. Giá trị của biểu thức $M = a^3 - b^3$ bằng bao nhiêu?'''
    dapan = "-26"
    loi_giai = fr'''Ta có $f'(x) = 3x^2 - 12x + 9 = 3(x - 1)(x - 3) = 0 \iff x = 1$ hoặc $x = 3$. \\
Hàm số đạt cực đại tại $x = 1 \implies a = 1$, đạt cực tiểu tại $x = 3 \implies b = 3$. \\
Vậy $M = a^3 - b^3 = 1^3 - 3^3 = -26$.'''
    return caudan, dapan, loi_giai


def CuoiChuong1_SA_Cau16():
    # Tối ưu hóa lợi nhuận L(x) = B(x) - C(x)
    caudan = fr'''Một công ty sản xuất mỗi ngày được $x$ sản phẩm $(1 \leq x \leq 18)$. Tổng chi phí sản xuất $x$ sản phẩm tính bằng nghìn đồng cho bởi hàm chi phí $C(x) = x^3 - 3x^2 + 80x + 500$. Giả sử công ty này bán hết sản phẩm mỗi ngày với giá $320$ nghìn đồng/sản phẩm. Gọi $B(x)$ là số tiền bán được và $L(x)$ là lợi nhuận thu được khi bán $x$ sản phẩm. Lợi nhuận (đơn vị triệu đồng) tối đa mà công ty có được là bao nhiêu?'''
    dapan = "1,2"
    loi_giai = fr'''Doanh thu $B(x) = 320x$ (nghìn đồng). \\
Lợi nhuận $L(x) = B(x) - C(x) = -x^3 + 3x^2 + 240x - 500$ (nghìn đồng). \\
$L'(x) = -3x^2 + 6x + 240 = -3(x - 10)(x + 8) = 0 \iff x = 10 \in [1; 18]$. \\
Lợi nhuận tối đa đạt tại $x = 10$ với $L(10) = 1200$ nghìn đồng $= 1{{,}}2$ triệu đồng.'''
    return caudan, dapan, loi_giai


def CuoiChuong1_SA_Cau17():
    # GTLN trên đoạn [3; 7] của y = (x^2 + x + 4)/(x + 1)
    caudan = fr'''Cho hàm số $y=\dfrac{{x^2+x+4}}{{x+1}}$. Gọi $A =\dfrac{{a}}{{b}}$ là giá trị lớn nhất của hàm số trên đoạn $[3;7]$ với $\dfrac{{a}}{{b}}$ là phân số tối giản. Giá trị của $P=-2a-7b$ bằng bao nhiêu?'''
    dapan = "-44"
    loi_giai = fr'''Ta có $y' = \dfrac{{x^2+2x-3}}{{(x+1)^2}} > 0, \forall x \in [3; 7]$ nên hàm số đồng biến trên $[3; 7]$. \\
Giá trị lớn nhất là $A = y(7) = \dfrac{{7^2+7+4}}{{7+1}} = \dfrac{{60}}{{8}} = \dfrac{{15}}{{2}}$. \\
Phân số tối giản $\implies a = 15, b = 2$. \\
Vậy $P = -2(15) - 7(2) = -44$.'''
    return caudan, dapan, loi_giai


def CuoiChuong1_SA_Cau18():
    # Diện tích tam giác OAB tạo bởi tiệm cận xiên của y = (4x^2+8x-5)/(-x+3) với Ox, Oy
    caudan = fr'''Biết tiệm cận xiên của đồ thị hàm số $y=f(x)=\dfrac{{4x^2+8x-5}}{{-x+3}}$ cắt trục $Ox, Oy$ lần lượt tại $A$ và $B$. Diện tích tam giác $OAB$ là'''
    dapan = "50"
    loi_giai = fr'''Chia đa thức: $\dfrac{{4x^2+8x-5}}{{-x+3}} = -4x - 20 + \dfrac{{55}}{{-x+3}}$. \\
Tiệm cận xiên: $y = -4x - 20$. \\
- Cắt $Ox$ tại $A(-5; 0) \implies OA = 5$. \\
- Cắt $Oy$ tại $B(0; -20) \implies OB = 20$. \\
Diện tích: $S_{{\triangle OAB}} = \dfrac{{1}}{{2}} \cdot 5 \cdot 20 = 50$.'''
    return caudan, dapan, loi_giai


# ==================== TRUE / FALSE (TF) ====================

def CuoiChuong1_TF_Cau3():
    # BBT hàm phân thức (Câu 13 TF)
    caudan = fr'''\immini{{Cho hàm số $y=f(x)$ có bảng biến thiên như hình bên. Hãy cho biết tính đúng sai của mỗi khẳng định sau:}}
{{\begin{{tikzpicture}}
	\tkzTabInit[nocadre,lgt=1.2,espcl=2.2,deltacl=0.5]
	{{$x$/0.6, $y'$/0.6, $y$/1.4}}
	{{$-\infty$, $2$, $+\infty$}}
	\tkzTabLine{{,+,d,+,}}
	\tkzTabVar{{-/ $-1$, +D-/$+\infty$/$-\infty$, +/$-1$}}
\end{{tikzpicture}}}}'''
    choices = [
        fr'''{{Hàm số đã cho đồng biến trên $\mathbb{{R}}$.}}
''',
        fr'''{{\True $\lim\limits_{{x\to -\infty}} \left[ 2f(x)-3 \right]=-5$.}}
''',
        fr'''{{Đồ thị hàm số đã cho có tiệm cận ngang là đường thẳng $x=-1$.}}
''',
        fr'''{{\True Giá trị lớn nhất của hàm số đã cho trên đoạn $[-3;1]$ là $f(1)$.}}
'''
    ]
    loi_giai = fr'''\begin{{itemize}}
  \item Hàm số gián đoạn tại $x = 2$ nên không đồng biến trên $\mathbb{{R}}$. (Ý a \textbf{{Sai}})
  \item $\lim\limits_{{x \to -\infty}} f(x) = -1 \implies \lim\limits_{{x \to -\infty}} [2f(x) - 3] = 2(-1) - 3 = -5$. (Ý b \textbf{{Đúng}})
  \item Tiệm cận ngang là $y = -1$, không phải $x = -1$. (Ý c \textbf{{Sai}})
  \item Hàm số đồng biến trên $(-\infty; 2)$ nên trên đoạn $[-3; 1]$ giá trị lớn nhất là $f(1)$. (Ý d \textbf{{Đúng}})
\end{{itemize}}'''
    return caudan, choices, loi_giai


def CuoiChuong1_TF_Cau4():
    # Khảo sát hàm số y = x^3 - 3x + 2 (Câu 14 TF)
    caudan = fr'''Cho hàm số $y = x^3 - 3x + 2$.'''
    choices = [
        fr'''{{\True Tập xác định của hàm số là $D = \mathbb{{R}}$.}}
''',
        fr'''{{\True Giá trị lớn nhất của hàm số trên đoạn $[-2;2]$ bằng $4$.}}
''',
        fr'''{{Đạo hàm của hàm số là $y' = 3x^2 - 3x$.}}
''',
        fr'''{{Hàm số đạt cực đại tại $x=1$.}}
'''
    ]
    loi_giai = fr'''\begin{{itemize}}
  \item Hàm đa thức bậc ba xác định trên $\mathbb{{R}}$. (Ý a \textbf{{Đúng}})
  \item $y' = 3x^2 - 3 = 0 \iff x = \pm 1$. Các giá trị: $y(-2)=0, y(-1)=4, y(1)=0, y(2)=4 \implies \max\limits_{{[-2; 2]}} y = 4$. (Ý b \textbf{{Đúng}})
  \item Đạo hàm $y' = 3x^2 - 3 \neq 3x^2 - 3x$. (Ý c \textbf{{Sai}})
  \item $y'' = 6x \implies y''(1) = 6 > 0 \implies x = 1$ là điểm cực tiểu. (Ý d \textbf{{Sai}})
\end{{itemize}}'''
    return caudan, choices, loi_giai


def CuoiChuong1_TF_Cau5():
    # Khảo sát hàm phân thức y = (-x^2 - 3x + 4)/(x - 3) (Câu 15 TF)
    caudan = fr'''Cho hàm số $y = \dfrac{{-x^2 - 3x + 4}}{{x-3}}$ có đồ thị là $(C)$.'''
    choices = [
        fr'''{{\True $(C)$ cắt trục hoành tại hai điểm phân biệt.}}
''',
        fr'''{{\True $(C)$ nhận điểm $I(3;-9)$ là tâm đối xứng.}}
''',
        fr'''{{\True Phương trình đường tiệm cận đứng của $(C)$ là $x=3$.}}
''',
        fr'''{{Phương trình đường tiệm cận xiên của $(C)$ là $y=-x+6$.}}
'''
    ]
    loi_giai = fr'''\begin{{itemize}}
  \item Phương trình $-x^2 - 3x + 4 = 0 \iff x = 1$ hoặc $x = -4$ (khác $3$) $\implies (C)$ cắt $Ox$ tại hai điểm phân biệt. (Ý a \textbf{{Đúng}})
  \item Chia đa thức: $y = -x - 6 - \dfrac{{14}}{{x - 3}}$. Tiệm cận đứng $x = 3$, tiệm cận xiên $y = -x - 6$. Giao điểm là $I(3; -9)$ là tâm đối xứng. (Ý b \textbf{{Đúng}})
  \item Tiệm cận đứng: $x = 3$. (Ý c \textbf{{Đúng}})
  \item Tiệm cận xiên: $y = -x - 6 \neq -x + 6$. (Ý d \textbf{{Sai}})
\end{{itemize}}'''
    return caudan, choices, loi_giai


def CuoiChuong1_TF_Cau6():
    # Chuyển động s(t) = 1/3 t^3 - 64t + 9 (Câu 16 TF)
    caudan = fr'''Một chất điểm chuyển động theo phương trình $s(t) = \dfrac{{1}}{{3}}t^3 - 64t + 9$, trong đó $t$ tính bằng giây, $s(t)$ tính bằng mét ($t \ge 0$). Hãy cho biết tính đúng sai của các khẳng định sau:'''
    choices = [
        fr'''{{Gia tốc tại thời điểm chất điểm đạt vận tốc nhỏ nhất bằng $a=3\text{{ m/s}}^2$.}}
''',
        fr'''{{Vận tốc nhỏ nhất của chất điểm là $v=20\text{{ m/s}}$.}}
''',
        fr'''{{Gia tốc tại thời điểm chất điểm đạt vận tốc bị triệt tiêu bằng $26\text{{ m/s}}^2$.}}
''',
        fr'''{{\True Vận tốc của chất điểm tại thời điểm $t=13\text{{ s}}$ là $105\text{{ m/s}}$.}}
'''
    ]
    loi_giai = fr'''\begin{{itemize}}
  \item $v(t) = t^2 - 64 \ge -64$. Vận tốc nhỏ nhất đạt tại $t = 0$ là $v = -64\text{{ m/s}}$, gia tốc $a(0) = 0\text{{ m/s}}^2$. (Ý a, b \textbf{{Sai}})
  \item Vận tốc bị triệt tiêu khi $v(t) = 0 \iff t = 8\text{{ s}}$. Gia tốc $a(8) = 16\text{{ m/s}}^2 \neq 26$. (Ý c \textbf{{Sai}})
  \item Tại $t = 13\text{{ s}}$: $v(13) = 13^2 - 64 = 105\text{{ m/s}}$. (Ý d \textbf{{Đúng}})
\end{{itemize}}'''
    return caudan, choices, loi_giai


# ==============================================================================
# BÀI TẬP ÔN TẬP CUỐI CHƯƠNG - SINH THEO ĐỀ KHẢO SÁT HÀM SỐ 2 (TOAN-04)
# ==============================================================================


def fmt_linear_de4(a, b):
    terms = []
    if a == 1:
        terms.append("x")
    elif a == -1:
        terms.append("-x")
    elif a != 0:
        terms.append(f"{a}x")
        
    if b > 0:
        terms.append(f"+ {b}" if terms else f"{b}")
    elif b < 0:
        terms.append(f"- {abs(b)}")
    elif not terms:
        terms.append("0")
    return " ".join(terms)

# ==================== MULTIPLE CHOICE (MC) ====================

def CuoiChuong1_MC_Cau31():
    # Giá trị cực tiểu từ BBT
    y_cd = random.choice([2, 3, 4])
    y_ct = random.choice([-4, -3, -2, -5])
    caudan = fr'''\immini{{Cho hàm số $y=f(x)$ có bảng biến thiên sau. Giá trị cực tiểu của hàm số đã cho bằng}}
{{\begin{{tikzpicture}}
	\tkzTabInit[lgt=1.2,espcl=1.5,nocadre]
	{{$x$/0.6, $f'(x)$/0.6, $f(x)$/1.5}}
	{{$-\infty$, $0$, $3$, $+\infty$}}
	\tkzTabLine{{,+,0,-,0,+,}}
	\tkzTabVar{{-/$-\infty$, +/${y_cd}$, -/${y_ct}$, +/$+\infty$}}
\end{{tikzpicture}}}}'''
    choices = [
        fr'''{{\True ${y_ct}$}}
''',
        fr'''{{${y_cd}$}}
''',
        fr'''{{$3$}}
''',
        fr'''{{$0$}}
'''
    ]
    random.shuffle(choices)
    loi_giai = fr'''Từ bảng biến thiên, hàm số đạt cực tiểu tại $x = 3$ và giá trị cực tiểu của hàm số là $y_{{\text{{CT}}}} = {y_ct}$.'''
    return caudan, choices, loi_giai


def CuoiChuong1_MC_Cau32():
    # Hàm bậc ba y = 1/3 x^3 - k x^2 - c x + d nghịch biến trên khoảng nào
    # Nghiệm y' = x^2 - 2k x - c = (x - x1)(x - x2)
    x1 = random.choice([-6, -5, -4, -3])
    x2 = random.choice([4, 5, 6, 7])
    sum_x = x1 + x2
    prod_x = x1 * x2
    # y' = x^2 - sum_x x + prod_x
    k_val = Fraction(sum_x, 2)
    c_val = -prod_x
    # Để hệ số đẹp, chọn x1, x2 sao cho sum_x chẵn
    if sum_x % 2 != 0:
        x2 += 1
        sum_x = x1 + x2
        prod_x = x1 * x2
    k = sum_x // 2
    c = -prod_x
    d = random.choice([1, 6, 9])
    
    caudan = fr'''Cho hàm số $y=\dfrac{{1}}{{3}}x^3 - {k if k != 1 else ""}x^2 - {c}x + {d}$. Hàm số nghịch biến trên khoảng nào sau đây?'''
    choices = [
        fr'''{{\True $({x1}; {x2})$}}
''',
        fr'''{{$({x1}; +\infty)$}}
''',
        fr'''{{$({x2}; +\infty)$}}
''',
        fr'''{{$(-\infty; {x1})$}}
'''
    ]
    random.shuffle(choices)
    loi_giai = fr'''Ta có $y' = x^2 - {2*k}x - {c} = (x {"+" if -x1 > 0 else "-"} {abs(x1)})(x - {x2})$. \\
$y' < 0 \iff {x1} < x < {x2}$. \\
Vậy hàm số nghịch biến trên khoảng $({x1}; {x2})$.'''
    return caudan, choices, loi_giai


def CuoiChuong1_MC_Cau33():
    # Tiệm cận xiên của y = (2x^2 - 3x - 1)/(x - 2)
    # y = ax + b + c/(x + d)
    caudan = fr'''Cho hàm số $y=\dfrac{{2x^2-3x-1}}{{x-2}}$. Tiệm cận xiên của đồ thị hàm số là đường thẳng'''
    choices = [
        fr'''{{\True $y=2x+1$}}
''',
        fr'''{{$y=2x-1$}}
''',
        fr'''{{$y=2x-3$}}
''',
        fr'''{{$y=2x+3$}}
'''
    ]
    random.shuffle(choices)
    loi_giai = fr'''Thực hiện phép chia đa thức: $2x^2 - 3x - 1 = (x - 2)(2x + 1) + 1$. \\
Do đó $y = 2x + 1 + \dfrac{{1}}{{x - 2}}$. \\
Vậy tiệm cận xiên của đồ thị hàm số là đường thẳng $y = 2x + 1$.'''
    return caudan, choices, loi_giai


def CuoiChuong1_MC_Cau34():
    # Bảng xét dấu f'(x) có nghiệm bội chẵn
    caudan = fr'''\immini{{Cho hàm số $f(x)$, bảng xét dấu của $f'(x)$ như sau. Số điểm cực trị của hàm số đã cho là}}
{{\begin{{tikzpicture}}
	\tkzTabInit[lgt=1.2,espcl=1.5,nocadre]
	{{$x$/0.6, $f'(x)$/0.6}}
	{{$-\infty$, $-1$, $0$, $1$, $+\infty$}}
	\tkzTabLine{{,+,0,-,0,-,0,+,}}
\end{{tikzpicture}}}}'''
    choices = [
        fr'''{{\True $2$}}
''',
        fr'''{{$0$}}
''',
        fr'''{{$1$}}
''',
        fr'''{{$3$}}
'''
    ]
    random.shuffle(choices)
    loi_giai = fr'''Đạo hàm $f'(x)$ đổi dấu khi qua $x = -1$ (từ $+$ sang $-$) và khi qua $x = 1$ (từ $-$ sang $+$). \\
Tại $x = 0$, $f'(x)$ không đổi dấu (vẫn mang dấu âm). \\
Vậy hàm số có đúng $2$ điểm cực trị.'''
    return caudan, choices, loi_giai


def CuoiChuong1_MC_Cau35():
    # GTNN của f(x) = x^3 - 6x trên [-1; 4]
    caudan = fr'''Giá trị nhỏ nhất của hàm số $f(x)=x^3-6x$ trên đoạn $[-1;4]$ là'''
    choices = [
        fr'''{{\True $-4\sqrt{{2}}$}}
''',
        fr'''{{$-5$}}
''',
        fr'''{{$5$}}
''',
        fr'''{{$40$}}
'''
    ]
    random.shuffle(choices)
    loi_giai = fr'''Ta có $f'(x) = 3x^2 - 6 = 0 \iff x = \pm\sqrt{{2}}$. \\
Trên đoạn $[-1; 4]$, ta nhận nghiệm $x = \sqrt{{2}}$. \\
Tính các giá trị: \\
$f(-1) = 5$. \\
$f(\sqrt{{2}}) = -4\sqrt{{2}} \approx -5{{,}}66$. \\
$f(4) = 40$. \\
Vậy giá trị nhỏ nhất của hàm số trên đoạn $[-1; 4]$ là $-4\sqrt{{2}}$.'''
    return caudan, choices, loi_giai


def CuoiChuong1_MC_Cau36():
    # Tiệm cận đứng của y = (ax+b)/(cx+d)
    d_val = random.choice([-3, -2, 2, 3, 4])
    sign_str = "+" if -d_val > 0 else "-"
    abs_d = abs(d_val)
    tc_d = d_val
    caudan = fr'''Đường tiệm cận đứng của đồ thị hàm số $y=\dfrac{{x+1}}{{x {sign_str} {abs_d}}}$ là'''
    choices = [
        fr'''{{\True $x={tc_d}$}}
''',
        fr'''{{$y={tc_d}$}}
''',
        fr'''{{$x={-tc_d}$}}
''',
        fr'''{{$y=1$}}
'''
    ]
    random.shuffle(choices)
    loi_giai = fr'''Ta có $\lim\limits_{{x \to {tc_d}^+}} \dfrac{{x+1}}{{x {sign_str} {abs_d}}} = \infty$ nên đường thẳng $x = {tc_d}$ là tiệm cận đứng của đồ thị hàm số.'''
    return caudan, choices, loi_giai


def CuoiChuong1_MC_Cau37():
    # Nhận dạng hàm phân thức từ BBT
    caudan = fr'''\immini{{Cho hàm số $y=f(x)$ có bảng biến thiên sau. Công thức của $f(x)$ là công thức nào sau đây?}}
{{\begin{{tikzpicture}} 
	\tkzTabInit[nocadre,lgt=1.2,espcl=2.5,deltacl=0.6]
	{{$x$ /1,$y'$ /0.6,$y$ /2}}
	{{$-\infty$,$\dfrac{{1}}{{2}}$,$+\infty$}}
	\tkzTabLine{{,+,d,+,}}
	\tkzTabVar{{-/$\dfrac{{1}}{{2}}$,+D-/$+\infty$/$-\infty$,+/$\dfrac{{1}}{{2}}$}}
\end{{tikzpicture}}}}'''
    choices = [
        fr'''{{\True $y=\dfrac{{x-2}}{{2x-1}}$}}
''',
        fr'''{{$y=\dfrac{{x+2}}{{2x-1}}$}}
''',
        fr'''{{$y=\dfrac{{-x+2}}{{2x-1}}$}}
''',
        fr'''{{$y=\dfrac{{-x-2}}{{2x-1}}$}}
'''
    ]
    random.shuffle(choices)
    loi_giai = fr'''Đồ thị hàm số có: \\
- Tiệm cận ngang $y = \dfrac{{1}}{{2}}$ và tiệm cận đứng $x = \dfrac{{1}}{{2}}$. \\
- Hàm số đồng biến trên từng khoảng xác định ($y' > 0$). \\
Xét hàm số $y = \dfrac{{x-2}}{{2x-1}}$ có đạo hàm $y' = \dfrac{{3}}{{(2x-1)^2}} > 0$ và tiệm cận ngang $y = \dfrac{{1}}{{2}}$ phù hợp với bảng biến thiên.'''
    return caudan, choices, loi_giai


def CuoiChuong1_MC_Cau38():
    # Giới hạn và tiệm cận
    y1 = random.choice([2, 3, 4])
    y2 = random.choice([-5, -4, -3])
    x0 = random.choice([1, 2])
    caudan = fr'''Cho hàm số $y=f(x)$ có $\lim\limits_{{x\to {x0}^{{-}}}} f(x)= {y2}$, $\lim\limits_{{x\to +\infty}} f(x)= {y2}$ và $\lim\limits_{{x\to -\infty}} f(x)= {y1}$. Chọn mệnh đề đúng?'''
    choices = [
        fr'''{{\True Đồ thị hàm số có tiệm cận ngang là $y={y1}$ và tiệm cận ngang là $y={y2}$}}
''',
        fr'''{{Đồ thị hàm số có tiệm cận đứng là $x={x0}$}}
''',
        fr'''{{Đồ thị hàm số có tiệm cận ngang là $y={y2}$ và tiệm cận đứng là $x={y1}$}}
''',
        fr'''{{Đồ thị hàm số có tiệm cận đứng là $x={y2}$ và $x={y1}$}}
'''
    ]
    random.shuffle(choices)
    loi_giai = fr'''- Do $\lim\limits_{{x \to -\infty}} f(x) = {y1}$ nên đường thẳng $y = {y1}$ là tiệm cận ngang. \\
- Do $\lim\limits_{{x \to +\infty}} f(x) = {y2}$ nên đường thẳng $y = {y2}$ là tiệm cận ngang. \\
- Giới hạn một bên $\lim\limits_{{x \to {x0}^-}} f(x) = {y2}$ hữu hạn nên không suy ra được tiệm cận đứng tại $x = {x0}$. \\
Vậy đồ thị hàm số có hai đường tiệm cận ngang là $y = {y1}$ và $y = {y2}$.'''
    return caudan, choices, loi_giai


def CuoiChuong1_MC_Cau39():
    # BBT có 2 tiệm cận ngang và 1 tiệm cận đứng
    caudan = fr'''\immini{{Cho hàm số $y=f(x)$ có bảng biến thiên như hình bên. Đồ thị hàm số $y=f(x)$ có bao nhiêu đường tiệm cận?}}
{{\begin{{tikzpicture}} 
	\tkzTabInit[nocadre,lgt=1.2,espcl=2,deltacl=0.6]
	{{$x$ /0.6,$y'$ /0.6,$y$ /1.5}}
	{{$-\infty$,$-9$,$5$,$+\infty$}}
	\tkzTabLine{{,+,d,-,0,+,}}
	\tkzTabVar{{-/$-7$,+D+/$9$/$+\infty$,-/$5$,+/$8$}}
\end{{tikzpicture}}}}'''
    choices = [
        fr'''{{\True $3$}}
''',
        fr'''{{$0$}}
''',
        fr'''{{$1$}}
''',
        fr'''{{$2$}}
'''
    ]
    random.shuffle(choices)
    loi_giai = fr'''- $\lim\limits_{{x \to -\infty}} f(x) = -7 \implies y = -7$ là tiệm cận ngang. \\
- $\lim\limits_{{x \to +\infty}} f(x) = 8 \implies y = 8$ là tiệm cận ngang. \\
- $\lim\limits_{{x \to -9^+}} f(x) = +\infty \implies x = -9$ là tiệm cận đứng. \\
Vậy đồ thị hàm số có tất cả $3$ đường tiệm cận ($2$ tiệm cận ngang và $1$ tiệm cận đứng).'''
    return caudan, choices, loi_giai


def CuoiChuong1_MC_Cau40():
    # Biện luận số nghiệm -7f(x) + 7 = 0 từ đồ thị
    caudan = fr'''\immini{{Cho hàm số $y=f(x)$ có đồ thị như hình vẽ bên. Phương trình $-7f(x)+7= 0$ có bao nhiêu nghiệm?}}
{{\begin{{tikzpicture}}[scale=0.6, line join=round, line cap=round, >=stealth]
	\def\xmin{{-1.2}}\def\xmax{{3.2}}\def\ymin{{-4.2}}\def\ymax{{1}}
	\draw[->] (\xmin-0.2,0)--(\xmax+0.2,0) node[below]{{\footnotesize $x$}};
	\draw[->] (0,\ymin-0.2)--(0,\ymax+0.2) node[right]{{\footnotesize $y$}};
	\draw (0,0) node[below left]{{\footnotesize $O$}};
	\foreach \x in {{-1,1,2,3}}\draw (\x,0.1)--(\x,-0.1) node[below]{{\footnotesize $\x$}};
	\foreach \y in {{-4,-3,-2,-1}}\draw (0.1,\y)--(-0.1,\y) node[left]{{\footnotesize $\y$}};
	\clip (\xmin,\ymin) rectangle (\xmax,\ymax);
	\draw[thick,smooth,samples=200,domain=\xmin:\xmax] plot (\x,{{-1*((\x)^3)+3*((\x)^2)+0*(\x)+-4}});
	\draw[dashed] (1,0)--(1,-2)--(0,-2);\fill (1,-2)circle(1.5pt);
	\draw[dashed] (0,0)--(0,-4)--(0,-4);\fill (0,-4)circle(1.5pt);
	\fill (2,0)circle(1.5pt);
\end{{tikzpicture}}}}'''
    choices = [
        fr'''{{\True $1$}}
''',
        fr'''{{$2$}}
''',
        fr'''{{$0$}}
''',
        fr'''{{$3$}}
'''
    ]
    random.shuffle(choices)
    loi_giai = fr'''Phương trình tương đương $f(x) = 1$. \\
Từ đồ thị, giá trị cực đại của hàm số là $y_{{\text{{CĐ}}}} = 0$. \\
Đường thẳng $y = 1$ nằm phía trên điểm cực đại nên cắt đồ thị tại đúng $1$ điểm. \\
Vậy phương trình có đúng $1$ nghiệm.'''
    return caudan, choices, loi_giai


def CuoiChuong1_MC_Cau41():
    # Độ dài đoạn nối hai điểm cực trị của y = x^3 + 3x^2 - 45x + 9
    caudan = fr'''Cho hàm số $y=f(x)=x^3+3x^2-45x+9$. Biết đồ thị hàm số $y=f(x)$ có hai điểm cực trị $A$ và $B$. Khi đó, độ dài $AB$ là'''
    choices = [
        fr'''{{\True $40\sqrt{{41}}$}}
''',
        fr'''{{$3\sqrt{{7289}}$}}
''',
        fr'''{{$2\sqrt{{16405}}$}}
''',
        fr'''{{$81\sqrt{{10}}$}}
'''
    ]
    random.shuffle(choices)
    loi_giai = fr'''Ta có $y' = 3x^2 + 6x - 45 = 0 \iff x = -5$ hoặc $x = 3$. \\
Tọa độ hai điểm cực trị là $A(-5; 184)$ và $B(3; -72)$. \\
Độ dài $AB = \sqrt{{(3 + 5)^2 + (-72 - 184)^2}} = \sqrt{{8^2 + (-256)^2}} = 40\sqrt{{41}}$.'''
    return caudan, choices, loi_giai


def CuoiChuong1_MC_Cau42():
    # Nhận dạng hàm bậc ba từ đồ thị
    caudan = fr'''\immini{{Cho hàm số $y=f(x)$ có đồ thị như hình vẽ bên. Đồ thị hàm số là của hàm số nào sau đây?}}
{{\begin{{tikzpicture}}[scale=0.6, line join=round, line cap=round, >=stealth]
	\def\xmin{{-1.2}}\def\xmax{{3.2}}\def\ymin{{-4.2}}\def\ymax{{1}}
	\draw[->] (\xmin-0.2,0)--(\xmax+0.2,0) node[below]{{\footnotesize $x$}};
	\draw[->] (0,\ymin-0.2)--(0,\ymax+0.2) node[right]{{\footnotesize $y$}};
	\draw (0,0) node[below left]{{\footnotesize $O$}};
	\foreach \x in {{-1,1,2,3}}\draw (\x,0.1)--(\x,-0.1) node[below]{{\footnotesize $\x$}};
	\foreach \y in {{-4,-3,-2,-1}}\draw (0.1,\y)--(-0.1,\y) node[left]{{\footnotesize $\y$}};
	\clip (\xmin,\ymin) rectangle (\xmax,\ymax);
	\draw[thick,smooth,samples=200,domain=\xmin:\xmax] plot (\x,{{-1*((\x)^3)+3*((\x)^2)+0*(\x)+-4}});
	\draw[dashed] (1,0)--(1,-2)--(0,-2);\fill (1,-2)circle(1.5pt);
	\draw[dashed] (0,0)--(0,-4)--(0,-4);\fill (0,-4)circle(1.5pt);
	\fill (2,0)circle(1.5pt);
\end{{tikzpicture}}}}'''
    choices = [
        fr'''{{\True $y=-x^3+3x^2-4$}}
''',
        fr'''{{$y=-x^3-3x^2-4$}}
''',
        fr'''{{$y=-x^3+2x^2-4$}}
''',
        fr'''{{$y=-x^3+4x^2-4$}}
'''
    ]
    random.shuffle(choices)
    loi_giai = fr'''Đồ thị cắt $Oy$ tại $(0; -4)$ và có hai điểm cực trị $(0; -4)$ và $(2; 0)$. \\
Xét $y = -x^3 + 3x^2 - 4$ có $y' = -3x^2 + 6x = 0 \iff x = 0$ hoặc $x = 2$, hoàn toàn phù hợp với đồ thị đã cho.'''
    return caudan, choices, loi_giai


# ==================== SHORT ANSWER (SA) ====================

def CuoiChuong1_SA_Cau19():
    # Tiệm cận xiên y = ax + b, tính P = -9a + 4b
    caudan = fr'''Cho hàm số $y=f(x)=\dfrac{{-x^2+8x-3}}{{-5x+3}}$ có đồ thị hàm số là $(C)$. Đường tiệm cận xiên của $(C)$ có dạng $y=ax+b$. Tính giá trị biểu thức $P=-9a+4b$ (làm tròn đến hàng phần mười).'''
    dapan = "-7,7"
    loi_giai = fr'''Chia đa thức: $-x^2 + 8x - 3 = (-5x + 3)\left(\dfrac{{1}}{{5}}x - \dfrac{{37}}{{25}}\right) + \dfrac{{36}}{{25}}$. \\
Tiệm cận xiên là $y = \dfrac{{1}}{{5}}x - \dfrac{{37}}{{25}} \implies a = \dfrac{{1}}{{5}}, b = -\dfrac{{37}}{{25}}$. \\
Giá trị $P = -9a + 4b = -9\left(\dfrac{{1}}{{5}}\right) + 4\left(-\dfrac{{37}}{{25}}\right) = -\dfrac{{193}}{{25}} = -7{{,}}72 \approx -7{{,}}7$.'''
    return caudan, dapan, loi_giai


def CuoiChuong1_SA_Cau20():
    # Tối ưu hóa sản xuất: Doanh thu F(x), Chi phí trung bình G(x)
    caudan = fr'''Một doanh nghiệp dự định sản xuất không quá $500$ sản phẩm. Nếu doanh nghiệp sản xuất $x$ sản phẩm $(1 \leq x \leq 500)$ thì doanh thu nhận được khi bán hết số sản phẩm đó là $F(x)=x^3-1646x^2+795760x+2132500$ (đồng), trong khi chi phí sản xuất bình quân cho một sản phẩm là $G(x)=x+1000+\dfrac{{2132500}}{{x}}$ (đồng). Doanh nghiệp cần sản xuất bao nhiêu sản phẩm để lợi nhuận thu được là lớn nhất?'''
    dapan = "358"
    loi_giai = fr'''Chi phí sản xuất $x$ sản phẩm là $C(x) = x \cdot G(x) = x^2 + 1000x + 2132500$ (đồng). \\
Lợi nhuận là $H(x) = F(x) - C(x) = x^3 - 1647x^2 + 794760x$. \\
$H'(x) = 3x^2 - 3294x + 794760 = 0 \iff x = 358 \in [1; 500]$ (loại $x = 740$). \\
Vậy lợi nhuận lớn nhất khi sản xuất $358$ sản phẩm.'''
    return caudan, dapan, loi_giai


def CuoiChuong1_SA_Cau21():
    # GTLN A và GTNN a trên đoạn [3; 4] của y = (x^2 + 2x + 22)/(x + 3)
    caudan = fr'''Ký hiệu $a,A$ lần lượt là giá trị nhỏ nhất và giá trị lớn nhất của hàm số $y=\dfrac{{x^2+2x+22}}{{x+3}}$ trên đoạn $[3;4]$. Giá trị của $P=-3a-4A$ (làm tròn đến hàng phần mười).'''
    dapan = "-44,8"
    loi_giai = fr'''Hàm số đồng biến trên $[3; 4]$ vì $y' = \dfrac{{x^2+6x-16}}{{(x+3)^2}} > 0, \forall x \in [3; 4]$. \\
Giá trị nhỏ nhất $a = y(3) = \dfrac{{37}}{{6}}$. \\
Giá trị lớn nhất $A = y(4) = \dfrac{{46}}{{7}}$. \\
Giá trị $P = -3a - 4A = -3\left(\dfrac{{37}}{{6}}\right) - 4\left(\dfrac{{46}}{{7}}\right) = -\dfrac{{627}}{{14}} \approx -44{{,}}8$.'''
    return caudan, dapan, loi_giai


def CuoiChuong1_SA_Cau22():
    # Đường thẳng qua 2 cực trị của y = (x^2 - 6x + 20)/(x + 2)
    caudan = fr'''Cho hàm số $y=f(x)=\dfrac{{x^2-6x+20}}{{x+2}}$. Biết đồ thị hàm số $y=f(x)$ có hai điểm cực trị lần lượt là $A$ và $B$. Phương trình đường thẳng đi qua hai điểm cực trị $A$ và $B$ có dạng $y=ax+b$. Tính giá trị biểu thức $P = -a-3b$.'''
    dapan = "16"
    loi_giai = fr'''Phương trình đường thẳng qua hai cực trị của đồ thị hàm phân thức bậc 2 trên bậc 1 là: \\
$y = \dfrac{{(x^2 - 6x + 20)'}}{{(x + 2)'}} = \dfrac{{2x - 6}}{{1}} = 2x - 6$. \\
Do đó $a = 2, b = -6$. \\
Vậy $P = -a - 3b = -(2) - 3(-6) = 16$.'''
    return caudan, dapan, loi_giai


def CuoiChuong1_SA_Cau23():
    # Giá thành sản phẩm P(t) = 1/3 t^3 - 24 t^2 + 495 t + 900000 giảm trên (t1; t2)
    caudan = fr'''Người ta thấy rằng trong vòng 3 năm tính từ đầu năm 2024, giá thành $P$ của một loại sản phẩm vào tháng thứ $t$ thay đổi theo công thức $P(t)=\dfrac{{1}}{{3}}t^3-24t^2+495t+900000$ (đồng) với $0\le t \le 36$. Biết giá thành sẽ giảm trong khoảng thời gian $(t_1;t_2)$. Khi đó $9t_1+t_2$ bằng bao nhiêu?'''
    dapan = "168"
    loi_giai = fr'''Ta có $P'(t) = t^2 - 48t + 495 = 0 \iff t = 15$ hoặc $t = 33$. \\
Hàm số nghịch biến trên $(15; 33)$ nên giá thành giảm từ tháng $15$ đến tháng $33$. \\
Suy ra $t_1 = 15, t_2 = 33 \implies 9t_1 + t_2 = 9(15) + 33 = 168$.'''
    return caudan, dapan, loi_giai


def CuoiChuong1_SA_Cau24():
    # Cực đại a, cực tiểu b của y = 1/3 x^3 + 6x^2 + 32x - 3, tính 3a - 3b
    caudan = fr'''Giả sử hàm số $y=\dfrac{{1}}{{3}}x^3+6x^2+32x-3$ có giá trị cực đại là $y=a$ và giá trị cực tiểu là $y=b$. Giá trị của biểu thức $A=3a-3b$ là bao nhiêu?'''
    dapan = "32"
    loi_giai = fr'''Ta có $y' = x^2 + 12x + 32 = 0 \iff x = -8$ hoặc $x = -4$. \\
Giá trị cực đại $a = y(-8) = -\dfrac{{137}}{{3}}$. \\
Giá trị cực tiểu $b = y(-4) = -\dfrac{{169}}{{3}}$. \\
Vậy $A = 3a - 3b = 3\left(-\dfrac{{137}}{{3}}\right) - 3\left(-\dfrac{{169}}{{3}}\right) = -137 - (-169) = 32$.'''
    return caudan, dapan, loi_giai


# ==================== TRUE / FALSE (TF) ====================

def CuoiChuong1_TF_Cau7():
    # Chuyển động s(t) = -t^3 + 9t^2 + 21t + 9
    caudan = fr'''Một chất điểm chuyển động theo phương trình $s(t)=-t^3+9t^2+21t+9$ với $t$ tính bằng giây ($t \ge 0$), $s(t)$ tính bằng mét. Hãy xác định tính đúng sai của các khẳng định sau:'''
    choices = [
        fr'''{{\True Vận tốc của chất điểm tại thời điểm $t$ (giây) là $v(t)=-3t^2+18t+21$.}}
''',
        fr'''{{\True Vận tốc của chất điểm tại giây thứ $2$ là $45\,\text{{m/s}}$.}}
''',
        fr'''{{Quãng đường chất điểm đi được từ lúc bắt đầu đến lúc dừng hẳn là $255\,\text{{m}}$.}}
''',
        fr'''{{\True Vận tốc chuyển động của chất điểm đạt giá trị lớn nhất tại thời điểm $t=3\,\text{{s}}$.}}
'''
    ]
    loi_giai = fr'''\begin{{itemize}}
  \item $v(t) = s'(t) = -3t^2 + 18t + 21$. (Ý a \textbf{{Đúng}})
  \item Tại $t = 2$: $v(2) = 45\,\text{{m/s}}$. (Ý b \textbf{{Đúng}})
  \item Dừng hẳn khi $v(t) = 0 \iff t = 7\,\text{{s}}$. Quãng đường đi được $s(7) - s(0) = 254 - 9 = 245\,\text{{m}} \neq 255\,\text{{m}}$. (Ý c \textbf{{Sai}})
  \item $v(t) = -3(t - 3)^2 + 48 \le 48$, lớn nhất tại $t = 3\,\text{{s}}$. (Ý d \textbf{{Đúng}})
\end{{itemize}}'''
    return caudan, choices, loi_giai


def CuoiChuong1_TF_Cau8():
    # Khảo sát BBT hàm phân thức
    caudan = fr'''\immini{{Cho hàm số $y=f(x)$ có bảng biến thiên như hình bên. Hãy cho biết tính đúng sai của mỗi khẳng định sau:}}
{{\begin{{tikzpicture}}
	\tkzTabInit[nocadre,lgt=1.2,espcl=2.5,deltacl=0.6]
	{{$x$ /0.6,$y'$ /0.6,$y$ /1.5}}
	{{$-\infty$,$-2$,$+\infty$}}
	\tkzTabLine{{,-,d,-,}}
	\tkzTabVar{{+/$-1$,-D+/$-\infty$/$+\infty$,-/$-1$}}
\end{{tikzpicture}}}}'''
    choices = [
        fr'''{{Đồ thị hàm số $y=f(x)$ có tiệm cận ngang là $x=-2$.}}
''',
        fr'''{{Giá trị của $\lim\limits_{{x \to +\infty }} \dfrac{{-2f(x)-1 }}{{-2-4f(x) }} = - \dfrac{{9}}{{2}}$.}}
''',
        fr'''{{Hàm số $y=f(x)$ có tập xác định là $D = \mathbb{{R}} \setminus \\{{-1\\}}$.}}
''',
        fr'''{{Đồ thị hàm số $y=f(x)$ có tiệm cận đứng là $x=-1$.}}
'''
    ]
    loi_giai = fr'''\begin{{itemize}}
  \item Tiệm cận ngang là $y = -1$, không phải $x = -2$. (Ý a \textbf{{Sai}})
  \item $\lim\limits_{{x \to +\infty}} f(x) = -1 \implies \lim\limits_{{x \to +\infty}} \dfrac{{-2f(x) - 1}}{{-2 - 4f(x)}} = \dfrac{{1}}{{2}} \neq -\dfrac{{9}}{{2}}$. (Ý b \textbf{{Sai}})
  \item Hàm số không xác định tại $x = -2 \implies D = \mathbb{{R}} \setminus \\{{-2\\}}$. (Ý c \textbf{{Sai}})
  \item Tiệm cận đứng là $x = -2$, không phải $x = -1$. (Ý d \textbf{{Sai}})
\end{{itemize}}'''
    return caudan, choices, loi_giai


def CuoiChuong1_TF_Cau9():
    # Khảo sát f(x) = 2x^3 - 294x - 1
    caudan = fr'''Cho hàm số $f(x)=2x^3-294x-1$. Hãy cho biết tính đúng sai của mỗi khẳng định sau:'''
    choices = [
        fr'''{{Giá trị cực đại của hàm số là $x=-7$.}}
''',
        fr'''{{\True Hàm số $y =f(x)$ đạt cực tiểu tại $x = 7$.}}
''',
        fr'''{{\True Điểm cực đại của đồ thị hàm số là $\left( -7;1371\right)$.}}
''',
        fr'''{{Hàm số $y =f(x)$ đạt cực đại tại $y=-1373$.}}
'''
    ]
    loi_giai = fr'''\begin{{itemize}}
  \item $f'(x) = 6(x^2 - 49) = 0 \iff x = \pm 7$. Điểm cực đại là $x = -7$, giá trị cực đại là $1371$. (Ý a \textbf{{Sai}})
  \item $f''(7) > 0 \implies x = 7$ là điểm cực tiểu. (Ý b \textbf{{Đúng}})
  \item Điểm cực đại của đồ thị là $(-7; 1371)$. (Ý c \textbf{{Đúng}})
  \item Cực đại tại $x = -7$, giá trị cực đại $1371 \neq -1373$. (Ý d \textbf{{Sai}})
\end{{itemize}}'''
    return caudan, choices, loi_giai


def CuoiChuong1_TF_Cau10():
    # Bảng biến thiên hàm bậc ba
    caudan = fr'''\immini{{Cho hàm số $y=f(x)$ có bảng biến thiên như hình bên. Hãy cho biết tính đúng sai của mỗi khẳng định sau:}}
{{\begin{{tikzpicture}}
	\tkzTabInit[nocadre,lgt=1.2,espcl=2.5,deltacl=0.6]
	{{$x$ /0.6, $y'$ /0.6, $y$ /1.5}}
	{{$-\infty$,$-2$,$4$,$+\infty$}}
	\tkzTabLine{{,-,$0$,+,$0$,-,}}
	\tkzTabVar{{+/$+\infty$,-/$-5$,+/$8$,-/$-\infty$}}
\end{{tikzpicture}}}}'''
    choices = [
        fr'''{{\True Hàm số đạt cực đại tại $x=4$.}}
''',
        fr'''{{Giá trị cực đại của hàm số là $y=4$.}}
''',
        fr'''{{Hàm số đồng biến trên khoảng $\left(-5;+\infty \right)$.}}
''',
        fr'''{{Hàm số nghịch biến trên khoảng $\left(-2;8\right)$.}}
'''
    ]
    loi_giai = fr'''\begin{{itemize}}
  \item Đạo hàm đổi dấu từ $+$ sang $-$ khi qua $x = 4$ nên đạt cực đại tại $x = 4$. (Ý a \textbf{{Đúng}})
  \item Giá trị cực đại là $y = 8$, không phải $4$. (Ý b \textbf{{Sai}})
  \item Hàm số đồng biến trên $(-2; 4)$. (Ý c, d \textbf{{Sai}})
\end{{itemize}}'''
    return caudan, choices, loi_giai


# ==============================================================================
# BÀI TẬP ÔN TẬP CUỐI CHƯƠNG - SINH THEO ĐỀ ÔN 1002 (TOAN-05)
# ==============================================================================


# ==================== MULTIPLE CHOICE (MC) ====================

def CuoiChuong1_MC_Cau43():
    # Đồng biến / nghịch biến từ BBT
    caudan = fr'''\immini{{Cho hàm số $y=f(x)$ có bảng biến thiên như sau. Hàm số đã cho nghịch biến trên khoảng nào dưới đây?}}
{{\begin{{tikzpicture}}
	\tkzTabInit[nocadre,lgt=1.2,espcl=1.5,deltacl=0.6]
	{{$x$ /0.6, $y'$ /0.6, $y$ /1.5}}
	{{$-\infty$,$-1$,$1$,$+\infty$}}
	\tkzTabLine{{,+,$0$,-,$0$,+,}}
	\tkzTabVar{{-/$-\infty$,+/$3$,-/$-2$,+/$+\infty$}}
\end{{tikzpicture}}}}'''
    choices = [
        fr'''{{\True $(-1; 1)$}}
''',
        fr'''{{$(-1; +\infty)$}}
''',
        fr'''{{$(1; +\infty)$}}
''',
        fr'''{{$(-\infty; 1)$}}
'''
    ]
    random.shuffle(choices)
    loi_giai = fr'''Từ bảng biến thiên, ta thấy $y' < 0$ trên khoảng $(-1; 1)$. \\
Do đó hàm số nghịch biến trên khoảng $(-1; 1)$.'''
    return caudan, choices, loi_giai


def CuoiChuong1_MC_Cau44():
    # Giá trị cực tiểu từ BBT
    y_ct = random.choice([-5, -4, -3, -6])
    y_cd = random.choice([2, 3, 4])
    caudan = fr'''\immini{{Cho hàm số $f(x)$ có bảng biến thiên như sau. Giá trị cực tiểu của hàm số đã cho bằng}}
{{\begin{{tikzpicture}}
	\tkzTabInit[nocadre,lgt=1.2,espcl=1.5,deltacl=0.6]
	{{$x$ /0.6, $y'$ /0.6, $y$ /1.5}}
	{{$-\infty$,$0$,$3$,$+\infty$}}
	\tkzTabLine{{,+,$0$,-,$0$,+,}}
	\tkzTabVar{{-/$-\infty$,+/${y_cd}$,-/${y_ct}$,+/$+\infty$}}
\end{{tikzpicture}}}}'''
    choices = [
        fr'''{{\True ${y_ct}$}}
''',
        fr'''{{${y_cd}$}}
''',
        fr'''{{$3$}}
''',
        fr'''{{$0$}}
'''
    ]
    random.shuffle(choices)
    loi_giai = fr'''Từ bảng biến thiên, hàm số đạt cực tiểu tại $x = 3$ và giá trị cực tiểu của hàm số bằng ${y_ct}$.'''
    return caudan, choices, loi_giai


def CuoiChuong1_MC_Cau45():
    # Đồng biến từ f'(x) = (x+1)^2 (x-1)^3 (2-x)
    caudan = fr'''Cho hàm số $f(x)$ có đạo hàm $f'(x)=(x+1)^2(x-1)^3(2-x)$. Hàm số $f(x)$ đồng biến trong khoảng nào dưới đây?'''
    choices = [
        fr'''{{\True $(1; 2)$}}
''',
        fr'''{{$(-\infty; -1)$}}
''',
        fr'''{{$(-1; 1)$}}
''',
        fr'''{{$(2; +\infty)$}}
'''
    ]
    random.shuffle(choices)
    loi_giai = fr'''Ta có $(x+1)^2 \ge 0, \forall x$. Dấu của $f'(x)$ phụ thuộc vào tích $(x-1)(2-x)$. \\
$f'(x) > 0 \iff (x-1)(2-x) > 0 \iff 1 < x < 2$. \\
Vậy hàm số đồng biến trên khoảng $(1; 2)$.'''
    return caudan, choices, loi_giai


def CuoiChuong1_MC_Cau46():
    # GTLN của f(x) = x^3 - 3x + 2 trên [-3; 3]
    caudan = fr'''Giá trị lớn nhất của hàm số $f(x)=x^3-3x+2$ trên đoạn $[-3;3]$ bằng'''
    choices = [
        fr'''{{\True $20$}}
''',
        fr'''{{$-16$}}
''',
        fr'''{{$0$}}
''',
        fr'''{{$4$}}
'''
    ]
    random.shuffle(choices)
    loi_giai = fr'''Ta có $f'(x) = 3x^2 - 3 = 0 \iff x = \pm 1 \in [-3; 3]$. \\
$f(-3) = -16, f(-1) = 4, f(1) = 0, f(3) = 20$. \\
Vậy giá trị lớn nhất của hàm số trên đoạn $[-3; 3]$ là $20$.'''
    return caudan, choices, loi_giai


def CuoiChuong1_MC_Cau47():
    # GTLN từ đồ thị hàm bậc ba trên đoạn [0; 2]
    caudan = fr'''\immini{{Cho hàm số $y=f(x)$ có đồ thị như hình bên. Giá trị lớn nhất của hàm số $f(x)$ trên đoạn $[0;2]$ là}}
{{\begin{{tikzpicture}}[scale=0.6, line join=round, line cap=round, >=stealth,font=\footnotesize]
	\def\xmin{{-2.2}}\def\xmax{{2.2}}\def\ymin{{-2.2}}\def\ymax{{2.2}}
	\draw[->] (\xmin-0.2,0)--(\xmax+0.2,0) node[below]{{$x$}};
	\draw[->] (0,\ymin-0.2)--(0,\ymax+0.2) node[right]{{$y$}};
	\draw (0,0) node[below left]{{$O$}};
	\foreach \x in {{-1,1}}\draw (\x,0.1)--(\x,-0.1) node[below]{{$\x$}};
	\foreach \y in {{-2,-1,1,2}}\draw (0.1,\y)--(-0.1,\y) node[left]{{$\y$}};
	\clip (\xmin,\ymin) rectangle (\xmax,\ymax);
	\draw[thick,smooth,samples=200,domain=\xmin:\xmax] plot (\x,{{-1*((\x)^3)+0*((\x)^2)+3*(\x)+0}});
	\draw[dashed] (-1,0)--(-1,-2)--(0,-2);\fill (-1,-2)circle(1.5pt);
	\draw[dashed] (1,0)--(1,2)--(0,2);\fill (1,2)circle(1.5pt);
\end{{tikzpicture}}}}'''
    choices = [
        fr'''{{\True $\max\limits_{{[0;2]}} f(x) = 2$}}
''',
        fr'''{{$\max\limits_{{[0;2]}} f(x) = -2$}}
''',
        fr'''{{$\max\limits_{{[0;2]}} f(x) = 1$}}
''',
        fr'''{{$\max\limits_{{[0;2]}} f(x) = 0$}}
'''
    ]
    random.shuffle(choices)
    loi_giai = fr'''Quan sát đồ thị trên đoạn $[0; 2]$, điểm cao nhất là cực đại $(1; 2)$. \\
Do đó $\max\limits_{{[0;2]}} f(x) = 2$ tại $x = 1$.'''
    return caudan, choices, loi_giai


def CuoiChuong1_MC_Cau48():
    # Tiệm cận đứng của y = (2x+1)/(x+1)
    a_x = random.choice([1, 2, 3])
    caudan = fr'''Đường thẳng nào dưới đây là tiệm cận đứng của đồ thị hàm số $y=\dfrac{{2x+1}}{{x+{a_x}}}$?'''
    choices = [
        fr'''{{\True $x={-a_x}$}}
''',
        fr'''{{$x={a_x}$}}
''',
        fr'''{{$y=2$}}
''',
        fr'''{{$y={-a_x}$}}
'''
    ]
    random.shuffle(choices)
    loi_giai = fr'''Nghiệm của mẫu số là $x + {a_x} = 0 \iff x = {-a_x}$. \\
Vậy đường thẳng $x = {-a_x}$ là tiệm cận đứng của đồ thị hàm số.'''
    return caudan, choices, loi_giai


def CuoiChuong1_MC_Cau49():
    # Nhận dạng hàm bậc ba từ BBT
    caudan = fr'''\immini{{Bảng biến thiên bên dưới là bảng biến thiên của một trong bốn hàm số được liệt kê ở các phương án A, B, C, D. Hàm số đó là hàm số nào?}}
{{\begin{{tikzpicture}}
	\tkzTabInit[nocadre,lgt=1.2,espcl=1.5,deltacl=0.6]
	{{$x$ /0.6, $y'$ /0.6, $y$ /1.5}}
	{{$-\infty$,$0$,$2$,$+\infty$}}
	\tkzTabLine{{,+,$0$,-,$0$,+,}}
	\tkzTabVar{{-/$-\infty$,+/$3$,-/$-1$,+/$+\infty$}}
\end{{tikzpicture}}}}'''
    choices = [
        fr'''{{\True $y=x^3-3x^2+3$}}
''',
        fr'''{{$y=-x^3+3x^2+3$}}
''',
        fr'''{{$y=x^4-5x^2+3$}}
''',
        fr'''{{$y=x^4-2x^2$}}
'''
    ]
    random.shuffle(choices)
    loi_giai = fr'''Bảng biến thiên là của hàm bậc ba có hệ số $a > 0$, đạt cực đại tại $x = 0$ ($y = 3$) và cực tiểu tại $x = 2$ ($y = -1$). \\
Xét hàm số $y = x^3 - 3x^2 + 3$ có $y' = 3x^2 - 6x = 0 \iff x = 0$ hoặc $x = 2$, hoàn toàn phù hợp.'''
    return caudan, choices, loi_giai


def CuoiChuong1_MC_Cau50():
    # Số điểm cực trị của f(x) = (x^2+x+1)/(x+1)
    caudan = fr'''Hàm số $f(x)=\dfrac{{x^2+x+1}}{{x+1}}$ có bao nhiêu điểm cực trị?'''
    choices = [
        fr'''{{\True $2$}}
''',
        fr'''{{$3$}}
''',
        fr'''{{$1$}}
''',
        fr'''{{$0$}}
'''
    ]
    random.shuffle(choices)
    loi_giai = fr'''Ta có $f'(x) = \dfrac{{(2x+1)(x+1) - (x^2+x+1)}}{{(x+1)^2}} = \dfrac{{x^2+2x}}{{(x+1)^2}} = \dfrac{{x(x+2)}}{{(x+1)^2}}$. \\
$f'(x) = 0 \iff x = 0$ hoặc $x = -2$. \\
Đạo hàm đổi dấu qua $2$ nghiệm đơn này nên hàm số có đúng $2$ điểm cực trị.'''
    return caudan, choices, loi_giai


def CuoiChuong1_MC_Cau51():
    # y = -1/3 x^3 + x^2 + 4 đồng biến trên khoảng nào
    caudan = fr'''Cho hàm số $y = -\dfrac{{x^3}}{{3}} + x^2 + 4$. Hàm số đồng biến trên khoảng nào trong các khoảng sau đây?'''
    choices = [
        fr'''{{\True $(0; 2)$}}
''',
        fr'''{{$(2; +\infty)$}}
''',
        fr'''{{$(0; +\infty)$}}
''',
        fr'''{{$(-\infty; 0)$}}
'''
    ]
    random.shuffle(choices)
    loi_giai = fr'''Ta có $y' = -x^2 + 2x = -x(x-2)$. \\
$y' > 0 \iff 0 < x < 2$. \\
Vậy hàm số đồng biến trên khoảng $(0; 2)$.'''
    return caudan, choices, loi_giai


def CuoiChuong1_MC_Cau52():
    # Bảng biến thiên có điểm gián đoạn, khoảng nghịch biến
    caudan = fr'''\immini{{Cho hàm số $y=f(x)$ có bảng biến thiên như hình bên. Hàm số nghịch biến trên các khoảng nào sau đây?}}
{{\begin{{tikzpicture}} 
	\tkzTabInit[nocadre,lgt=1.2,espcl=2,deltacl=0.6]
	{{$x$ /0.6,$y'$ /0.6,$y$ /1.5}}
	{{$-\infty$,$-7$,$-4$,$4$,$+\infty$}}
	\tkzTabLine{{,+,$0$,-,d,-,$0$,+,}}
	\tkzTabVar{{-/$-\infty$,+/$14$,-D+/$-\infty$/$+\infty$,-/$6$,+/$+\infty$}}
\end{{tikzpicture}}}}'''
    choices = [
        fr'''{{\True $(-7;-4)$ và $(-4;4)$}}
''',
        fr'''{{$(-7; 4)$}}
''',
        fr'''{{$(-7; +\infty)$}}
''',
        fr'''{{$(-\infty; -4)$}}
'''
    ]
    random.shuffle(choices)
    loi_giai = fr'''Từ bảng biến thiên, ta thấy $y' < 0$ trên $(-7; -4)$ và $(-4; 4)$. \\
Vậy hàm số nghịch biến trên các khoảng $(-7; -4)$ và $(-4; 4)$.'''
    return caudan, choices, loi_giai


def CuoiChuong1_MC_Cau53():
    # GTNN của f(x) = x^3 - 3x + 2 trên [-3; 3]
    caudan = fr'''Giá trị nhỏ nhất của hàm số $f(x) = x^3 - 3x + 2$ trên đoạn $[-3;3]$ bằng'''
    choices = [
        fr'''{{\True $-16$}}
''',
        fr'''{{$0$}}
''',
        fr'''{{$4$}}
''',
        fr'''{{$20$}}
'''
    ]
    random.shuffle(choices)
    loi_giai = fr'''Xét trên $[-3; 3]$: $f'(x) = 3x^2 - 3 = 0 \iff x = \pm 1$. \\
$f(-3) = -16, f(-1) = 4, f(1) = 0, f(3) = 20$. \\
Vậy $\min\limits_{{[-3; 3]}} f(x) = -16$ tại $x = -3$.'''
    return caudan, choices, loi_giai


def CuoiChuong1_MC_Cau54():
    # Tâm đối xứng của y = (x+2)/(x-2)
    caudan = fr'''Cho hàm số $y = \dfrac{{x+2}}{{x-2}}$. Tâm đối xứng của đồ thị hàm số có tọa độ là'''
    choices = [
        fr'''{{\True $(2; 1)$}}
''',
        fr'''{{$(2; -1)$}}
''',
        fr'''{{$(1; 2)$}}
''',
        fr'''{{$(2; 2)$}}
'''
    ]
    random.shuffle(choices)
    loi_giai = fr'''Đồ thị hàm số có tiệm cận đứng $x = 2$ và tiệm cận ngang $y = 1$. \\
Tâm đối xứng là giao điểm của hai tiệm cận: $I(2; 1)$.'''
    return caudan, choices, loi_giai


# ==================== SHORT ANSWER (SA) ====================

def CuoiChuong1_SA_Cau25():
    # Bài toán tối ưu lợi nhuận kinh tế
    caudan = fr'''Ông A dự định đầu tư sản xuất một loại sản phẩm với số lượng không quá $200$ sản phẩm. Nếu ông A bán được $x$ sản phẩm thì thu về số tiền tính theo công thức $f(x) = x^3 - 1550x^2 + 128500x + 30000$. Chi phí sản xuất bình quân cho một sản phẩm được tính theo công thức $C(x) = 1000 + x + \dfrac{{25000}}{{x}}$. Hỏi ông A cần sản xuất bao nhiêu sản phẩm thì lợi nhuận thu về là lớn nhất?'''
    dapan = "50"
    loi_giai = fr'''Lợi nhuận thu được khi bán $x$ sản phẩm ($1 \le x \le 200$) là: \\
$L(x) = f(x) - x \cdot C(x) = x^3 - 1551x^2 + 127500x + 5000$. \\
Khảo sát hàm số $L(x)$ trên $[1; 200]$ suy ra lợi nhuận lớn nhất khi sản xuất $50$ sản phẩm.'''
    return caudan, dapan, loi_giai


def CuoiChuong1_SA_Cau26():
    # GTNN của hàm phân thức trên đoạn, biểu thức 3a - b
    caudan = fr'''Cho hàm số $y=\dfrac{{x^2+8x+40}}{{x-1}}$. Gọi $B =\dfrac{{a}}{{b}}$ là giá trị nhỏ nhất của hàm số trên đoạn $[10;14]$ với $\dfrac{{a}}{{b}}$ là phân số tối giản. Giá trị của $P=3a-b$.'''
    dapan = "651"
    loi_giai = fr'''Ta có $y' = \dfrac{{x^2-2x-48}}{{(x-1)^2}} = 0 \iff x = 8$ hoặc $x = -6$ (đều không thuộc $[10; 14]$). \\
Với $x \in [10; 14]$, $y' > 0$ nên hàm đồng biến. \\
Giá trị nhỏ nhất là $B = y(10) = \dfrac{{10^2+8(10)+40}}{{10-1}} = \dfrac{{220}}{{9}}$ (phân số tối giản). \\
Do đó $a = 220, b = 9 \implies P = 3a - b = 3(220) - 9 = 651$. \\
(Lưu ý: Nếu theo phép tính $y(10) = \dfrac{{580}}{{9}}$ của đề thì $P = 1731$).'''
    return caudan, dapan, loi_giai


def CuoiChuong1_SA_Cau27():
    # Cực đại tại a, cực tiểu tại b của hàm bậc ba, tính 5a + 9b
    caudan = fr'''Giả sử hàm số $y=\dfrac{{1}}{{3}}x^3+5x^2+9x-2$ đạt cực đại tại $x=a$ và đạt cực tiểu tại $x=b$. Giá trị của biểu thức $A=5a+9b$ là bao nhiêu?'''
    dapan = "-54"
    loi_giai = fr'''Ta có $y' = x^2 + 10x + 9 = 0 \iff x = -9$ hoặc $x = -1$. \\
Bảng biến thiên cho thấy hàm số đạt cực đại tại $a = -9$ và đạt cực tiểu tại $b = -1$. \\
Vậy $A = 5a + 9b = 5(-9) + 9(-1) = -54$.'''
    return caudan, dapan, loi_giai


def CuoiChuong1_SA_Cau28():
    # Phương trình đường thẳng qua hai cực trị y = ax + b, tính -4a - 9b
    caudan = fr'''Cho hàm số $y=f(x)=\dfrac{{x^2+5x+31}}{{x+2}}$. Biết đồ thị hàm số $y=f(x)$ có hai điểm cực trị lần lượt là $A$ và $B$. Phương trình đường thẳng đi qua hai điểm cực trị $A$ và $B$ có dạng $y=ax+b$. Tính giá trị biểu thức $P = -4a-9b$.'''
    dapan = "-53"
    loi_giai = fr'''Phương trình đường thẳng qua hai cực trị là: \\
$y = \dfrac{{(x^2+5x+31)'}}{{(x+2)'}} = \dfrac{{2x+5}}{{1}} = 2x + 5$. \\
Suy ra $a = 2, b = 5 \implies P = -4a - 9b = -4(2) - 9(5) = -53$.'''
    return caudan, dapan, loi_giai


def CuoiChuong1_SA_Cau29():
    # Tiệm cận xiên y = ax + b, tính (b+2025)/(a-2025)
    caudan = fr'''Cho hàm số $y=f(x)=\dfrac{{x^2+7x-4}}{{-2x-9}}$ có đồ thị hàm số là $(C)$. Đường tiệm cận xiên của $(C)$ có dạng $y=ax+b$. Tính giá trị biểu thức $P=\dfrac{{b+2025}}{{a-2025}}$ (làm tròn đến hàng phần mười).'''
    dapan = "-1,0"
    loi_giai = fr'''Chia đa thức: $x^2 + 7x - 4 = (-2x - 9)\left(-\dfrac{{1}}{{2}}x - \dfrac{{5}}{{4}}\right) - \dfrac{{61}}{{4}}$. \\
Tiệm cận xiên là $y = -0{{,}}5x - 1{{,}}25 \implies a = -0{{,}}5; b = -1{{,}}25$. \\
$P = \dfrac{{-1{{,}}25 + 2025}}{{-0{{,}}5 - 2025}} = \dfrac{{2023{{,}}75}}{{-2025{{,}}5}} \approx -1{{,}}0$.'''
    return caudan, dapan, loi_giai


def CuoiChuong1_SA_Cau30():
    # Chuyển động s(t), vận tốc giảm trên (a; b), tính a - 2b
    caudan = fr'''Trong $18$ giây đầu tiên, một chất điểm chuyển động theo phương trình $s(t) = -t^3+18t^2+2t+9$, trong đó $t$ tính bằng giây và $s$ tính bằng mét. Vận tốc chất điểm giảm trong khoảng thời gian $(a;b)$. Tính giá trị biểu thức $a-2b$.'''
    dapan = "-30"
    loi_giai = fr'''Vận tốc: $v(t) = s'(t) = -3t^2 + 36t + 2$. \\
Gia tốc: $v'(t) = -6t + 36 = 0 \iff t = 6$. \\
Vận tốc giảm khi $v'(t) < 0 \iff t > 6$, tức trong khoảng $(6; 18)$. \\
Suy ra $a = 6, b = 18 \implies a - 2b = 6 - 2(18) = -30$.'''
    return caudan, dapan, loi_giai


# ==================== TRUE / FALSE (TF) ====================

def CuoiChuong1_TF_Cau11():
    # Chuyển động S(t) = -t^3 + 9t^2 + t + 10
    caudan = fr'''Một chất điểm chuyển động được quãng đường $S$ (đơn vị mét) là hàm số phụ thuộc thời gian $t$ (đơn vị giây, $t \ge 0$) theo công thức $S(t) = -t^3 + 9t^2 + t + 10$.'''
    choices = [
        fr'''{{\True Vận tốc trung bình của chuyển động trong $2$ giây đầu tiên bằng $15\,\text{{m/s}}$.}}
''',
        fr'''{{Quãng đường chất điểm đi được sau khi xuất phát $1$ giây bằng $18\,\text{{m}}$.}}
''',
        fr'''{{\True Gia tốc của chuyển động tại thời điểm $t=2$ giây lớn hơn gia tốc của chuyển động tại thời điểm $t=4$ giây.}}
''',
        fr'''{{\True Vận tốc của chuyển động đạt giá trị lớn nhất là $28\,\text{{m/s}}$.}}
'''
    ]
    loi_giai = fr'''\begin{{itemize}}
  \item $v_{{\text{{tb}}}} = \dfrac{{S(2) - S(0)}}{{2}} = \dfrac{{40 - 10}}{{2}} = 15\,\text{{m/s}}$. (Ý a \textbf{{Đúng}})
  \item Quãng đường đi được sau $1$ giây đầu là $S(1) - S(0) = 19 - 10 = 9\,\text{{m}} \neq 18\,\text{{m}}$. (Ý b \textbf{{Sai}})
  \item $a(2) = 6\,\text{{m/s}}^2 > a(4) = -6\,\text{{m/s}}^2$. (Ý c \textbf{{Đúng}})
  \item $v(t) = -3(t - 3)^2 + 28 \le 28\,\text{{m/s}}$. (Ý d \textbf{{Đúng}})
\end{{itemize}}'''
    return caudan, choices, loi_giai


def CuoiChuong1_TF_Cau12():
    # Khảo sát y = x^3 - 3x + 1
    caudan = fr'''Cho hàm số $y = x^3 - 3x + 1$.'''
    choices = [
        fr'''{{\True Điểm cực tiểu của hàm số là $x=1$.}}
''',
        fr'''{{Gọi $A,B$ lần lượt là điểm cực đại và điểm cực tiểu của đồ thị hàm số, điểm $C(-1;2)$. Khi đó diện tích tam giác $ABC$ là $12$.}}
''',
        fr'''{{Hàm số đồng biến trên khoảng $(-1;1)$.}}
''',
        fr'''{{\True Giả sử hàm số đã cho có hai điểm cực trị là $x_1, x_2$. Khi đó giá trị $x_1 \cdot x_2 = -1$.}}
'''
    ]
    loi_giai = fr'''\begin{{itemize}}
  \item $y' = 3x^2 - 3 = 0 \iff x = \pm 1$. Cực tiểu tại $x = 1$. (Ý a \textbf{{Đúng}})
  \item $A(-1; 3), B(1; -1), C(-1; 2) \implies S_{{ABC}} = 1 \neq 12$. (Ý b \textbf{{Sai}})
  \item Trên $(-1; 1)$, $y' < 0$ nên hàm số nghịch biến. (Ý c \textbf{{Sai}})
  \item $x_1 x_2 = (-1)(1) = -1$. (Ý d \textbf{{Đúng}})
\end{{itemize}}'''
    return caudan, choices, loi_giai


def CuoiChuong1_TF_Cau13():
    # Khảo sát hàm phân thức y = (2x^2 - 3x + 6)/(x - 2)
    caudan = fr'''Cho hàm số $y=\dfrac{{2x^2-3x+6}}{{x-2}}$. Các khẳng định sau đúng hay sai?'''
    choices = [
        fr'''{{\True Hàm số đạt cực đại tại điểm $x=0$.}}
''',
        fr'''{{Giá trị nhỏ nhất của hàm số trên $(2;+\infty)$ bằng $12$.}}
''',
        fr'''{{\True Tiệm cận xiên của đồ thị hàm số là đường thẳng có phương trình $y=2x+1$.}}
''',
        fr'''{{Hàm số nghịch biến trên khoảng $(0;4)$.}}
'''
    ]
    loi_giai = fr'''\begin{{itemize}}
  \item Cực đại tại $x = 0$ với $y(0) = -3$. (Ý a \textbf{{Đúng}})
  \item Cực tiểu tại $x = 4$ với $y(4) = 13 \neq 12$. (Ý b \textbf{{Sai}})
  \item $y = 2x + 1 + \dfrac{{8}}{{x - 2}} \implies$ Tiệm cận xiên $y = 2x + 1$. (Ý c \textbf{{Đúng}})
  \item Hàm số gián đoạn tại $x = 2$ nên không nghịch biến trên $(0; 4)$. (Ý d \textbf{{Sai}})
\end{{itemize}}'''
    return caudan, choices, loi_giai


def CuoiChuong1_TF_Cau14():
    # Đồ thị hàm bậc ba y = -x^3 + 6x^2 - 9x + 5
    caudan = fr'''\immini{{Cho hàm số bậc ba $y=f(x)=ax^3+bx^2+cx+d$ có đồ thị như hình vẽ bên. Các khẳng định sau đúng hay sai?}}
{{\begin{{tikzpicture}}[scale=0.6, line join=round, line cap=round, >=stealth,font=\footnotesize]
	\def\xmin{{-0.5}}\def\xmax{{4}}\def\ymin{{-0.5}}\def\ymax{{5.5}}
	\draw[->] (\xmin-0.2,0)--(\xmax+0.2,0) node[below]{{$x$}};
	\draw[->] (0,\ymin-0.2)--(0,\ymax+0.2) node[right]{{$y$}};
	\draw (0,0) node[below left]{{$O$}};
	\foreach \x in {{1,2,3}}\draw (\x,0.1)--(\x,-0.1) node[below]{{$\x$}};
	\foreach \y in {{1,2,3,5}}\draw (0.1,\y)--(-0.1,\y) node[left]{{$\y$}};
	\clip (\xmin,\ymin) rectangle (\xmax,\ymax);
	\draw[thick,smooth,samples=200,domain=\xmin:\xmax] plot (\x,{{-1*((\x)^3)+6*((\x)^2)+-9*(\x)+5}});
	\draw[dashed] (2,0)--(2,3)--(0,3);\fill (2,3)circle(1.5pt);
	\draw[dashed] (1,0)--(1,1)--(0,1);\fill (1,1)circle(1.5pt);
	\draw[dashed] (3,0)--(3,5)--(0,5);\fill (3,5)circle(1.5pt);
\end{{tikzpicture}}}}'''
    choices = [
        fr'''{{Giá trị cực đại của hàm số bằng $3$.}}
''',
        fr'''{{\True Hàm số đồng biến trên khoảng $(1;3)$.}}
''',
        fr'''{{\True Giá trị nhỏ nhất của hàm số trên đoạn $[0;3]$ bằng $1$.}}
''',
        fr'''{{\True $f(0)=5$.}}
'''
    ]
    loi_giai = fr'''\begin{{itemize}}
  \item Cực đại là $(3; 5) \implies$ Giá trị cực đại bằng $5 \neq 3$. (Ý a \textbf{{Sai}})
  \item Đồ thị đi lên từ cực tiểu $(1; 1)$ đến cực đại $(3; 5) \implies$ Đồng biến trên $(1; 3)$. (Ý b \textbf{{Đúng}})
  \item Trên $[0; 3]$, $\min f(x) = f(1) = 1$. (Ý c \textbf{{Đúng}})
  \item Cắt $Oy$ tại $(0; 5) \implies f(0) = 5$. (Ý d \textbf{{Đúng}})
\end{{itemize}}'''
    return caudan, choices, loi_giai


# ==============================================================================
# BÀI TẬP ÔN TẬP CUỐI CHƯƠNG - SINH THEO ĐỀ TOAN-02
# ==============================================================================


# ==================== DE 2: CHUONG I MC ====================

def CuoiChuong1_MC_Cau55():
    # De 2 Cau 1: BBT nghich bien tren (-2; 1)
    caudan = fr'''\immini{{Cho hàm số $y = f(x)$ có bảng biến thiên như sau. Hàm số $y = f(x)$ nghịch biến trên khoảng nào?}}
{{\begin{{tikzpicture}}
  \tkzTabInit[nocadre,lgt=1.2,espcl=1.5,deltacl=0.5]
     {{$x$/0.7,$y'$/0.7,$y$/2}}
     {{$-\infty$,$-2$,$1$,$+\infty$}}
  \tkzTabLine{{,+,0,-,0,+,}}
  \tkzTabVar{{-/$-\infty$,+/$8$,-/$4$,+/$+\infty$}}
\end{{tikzpicture}}}}'''
    choices = [
        fr'''{{\True $(-2; 1)$}}
''',
        fr'''{{$(2; +\infty)$}}
''',
        fr'''{{$(-\infty; 1)$}}
''',
        fr'''{{$(4; 8)$}}
'''
    ]
    random.shuffle(choices)
    loi_giai = fr'''Dựa vào bảng biến thiên, hàm số nghịch biến trên khoảng $(-2; 1)$ vì $y' < 0$ trên khoảng này.'''
    return caudan, choices, loi_giai


def CuoiChuong1_MC_Cau56():
    # De 2 Cau 2: GTNN của y = x^3 + 3x^2 - 1 trên [-1; 2]
    caudan = fr'''Giá trị nhỏ nhất của hàm số $y = x^3 + 3x^2 - 1$ trên đoạn $[-1; 2]$ bằng'''
    choices = [
        fr'''{{\True $-1$}}
''',
        fr'''{{$1$}}
''',
        fr'''{{$3$}}
''',
        fr'''{{$-3$}}
'''
    ]
    random.shuffle(choices)
    loi_giai = fr'''Ta có $y' = 3x^2 + 6x = 3x(x + 2) = 0 \iff x = 0 \in [-1; 2]$ hoặc $x = -2 \notin [-1; 2]$. \\
$y(-1) = 1, y(0) = -1, y(2) = 19 \implies \min\limits_{{[-1; 2]}} y = -1$.'''
    return caudan, choices, loi_giai


def CuoiChuong1_MC_Cau57():
    # De 2 Cau 3: Hàm số đạt cực đại tại điểm từ đồ thị
    caudan = fr'''\immini{{Cho hàm số $y = f(x)$ có đồ thị như hình vẽ bên. Hàm số đạt cực đại tại điểm}}
{{\begin{{tikzpicture}}[line join=round, line cap=round, >=stealth, scale=0.6]
  \draw[->] (-2,0) -- (2,0) node[below] {{$x$}};
  \draw[->] (0,-1.5) -- (0,4) node[left] {{$y$}};
  \draw (0,0) node[below left] {{$O$}};
  \draw (-1,0) node[below] {{$-1$}};
  \draw (0,1) node[above right] {{$1$}};
  \draw (0,3) node[right] {{$3$}};
  \draw (0,-1) node[left] {{$-1$}};
  \draw[dashed] (-1,0) -- (-1,3) -- (0,3);
  \draw[samples=200, domain=-1.5:1.2, smooth, variable=\x] plot (\x, {{2*(\x)^3 + 3*(\x)^2 + 1}});
\end{{tikzpicture}}}}'''
    choices = [
        fr'''{{\True $x = -1$}}
''',
        fr'''{{$x = 0$}}
''',
        fr'''{{$x = 1$}}
''',
        fr'''{{$x = 3$}}
'''
    ]
    random.shuffle(choices)
    loi_giai = fr'''Từ đồ thị hàm số, điểm cực đại của hàm số là $x = -1$.'''
    return caudan, choices, loi_giai


def CuoiChuong1_MC_Cau58():
    # De 2 Cau 4: Bảng biến thiên số tiệm cận ngang
    caudan = fr'''\immini{{Cho hàm số $y = f(x)$ có bảng biến thiên như hình dưới đây. Số đường tiệm cận ngang của đồ thị hàm số đã cho là}}
{{\begin{{tikzpicture}}
  \tkzTabInit[nocadre,lgt=1.2,espcl=1.5,deltacl=0.5]
     {{$x$/0.7,$y'$/0.7,$y$/2}}
     {{$-\infty$,$0$,$1$,$+\infty$}}
  \tkzTabLine{{,-,d,-,0,+,}}
  \tkzTabVar{{+/$2$, -/$-4$, +/$+\infty$ / $-2$, +/$+\infty$}}
\end{{tikzpicture}}}}'''
    choices = [
        fr'''{{\True $1$}}
''',
        fr'''{{$3$}}
''',
        fr'''{{$2$}}
''',
        fr'''{{$0$}}
'''
    ]
    random.shuffle(choices)
    loi_giai = fr'''Ta có $\lim\limits_{{x \to -\infty}} f(x) = 2 \implies y = 2$ là tiệm cận ngang. \\
$\lim\limits_{{x \to +\infty}} f(x) = +\infty$ nên không có TCN khi $x \to +\infty$. \\
Vậy đồ thị hàm số có $1$ đường tiệm cận ngang.'''
    return caudan, choices, loi_giai


def CuoiChuong1_MC_Cau59():
    # De 2 Cau 6: Tâm đối xứng đồ thị hàm phân thức
    caudan = fr'''\immini{{Cho hàm số $y = \dfrac{{ax + b}}{{cx + d}}$ có đồ thị là đường cong như hình vẽ bên. Tọa độ tâm đối xứng của đồ thị hàm số đã cho là}}
{{\begin{{tikzpicture}}[line join=round, line cap=round, >=stealth, scale=0.6]
  \draw[->] (-1.5,0) -- (3,0) node[below] {{$x$}};
  \draw[->] (0,-2) -- (0,2.5) node[left] {{$y$}};
  \draw (0,0) node[below left]{{$O$}};
  \draw[dashed, thick] (1,-2) -- (1,2.5) node[above] {{$x = 1$}};
  \draw[dashed, thick] (-1.5,0.5) -- (3,0.5) node[right] {{$y = \frac{1}{2}$}};
  \draw (0,0.5) node[above left] {{$\frac{1}{2}$}};
  \draw (0.5,0) node[above] {{$\frac{1}{2}$}};
  \draw[samples=200, domain=-1.5:0.7, smooth] plot (\x, {{(0.5*\x - 0.25)/(\x - 1)}});
  \draw[samples=200, domain=1.3:3, smooth] plot (\x, {{(0.5*\x - 0.25)/(\x - 1)}});
\end{{tikzpicture}}}}'''
    choices = [
        fr'''{{\True $(1; \frac{{1}}{{2}})$}}
''',
        fr'''{{$(0; \frac{{1}}{{2}})$}}
''',
        fr'''{{$(1; 0)$}}
''',
        fr'''{{$(\frac{{1}}{{2}}; 1)$}}
'''
    ]
    random.shuffle(choices)
    loi_giai = fr'''Tâm đối xứng là giao điểm của TCĐ $x = 1$ và TCN $y = \frac{{1}}{{2}}$, tức điểm $(1; \frac{{1}}{{2}})$.'''
    return caudan, choices, loi_giai


def CuoiChuong1_MC_Cau60():
    # De 2 Cau 7: Hàm số nào không có cực trị
    caudan = fr'''Hàm số nào sau đây không có cực trị?'''
    choices = [
        fr'''{{\True $y = \dfrac{{2x - 2}}{{x + 1}}$}}
''',
        fr'''{{$y = \dfrac{{x^2 + 1}}{{x}}$}}
''',
        fr'''{{$y = x^2 - 2x + 1$}}
''',
        fr'''{{$y = -x^3 + x + 1$}}
'''
    ]
    random.shuffle(choices)
    loi_giai = fr'''Hàm số nhất biến $y = \dfrac{{2x - 2}}{{x + 1}}$ có đạo hàm $y' = \dfrac{{4}}{{(x+1)^2}} > 0, \forall x \neq -1$ nên không có cực trị.'''
    return caudan, choices, loi_giai


def CuoiChuong1_MC_Cau61():
    # De 2 Cau 11: Thể tích nước giảm trong khoảng nhiệt độ nào
    caudan = fr'''\immini{{Thể tích $V$ (đơn vị: $\text{{cm}}^3$) của $1\text{{ kg}}$ nước tại nhiệt độ $T$ (đơn vị: $^\circ\text{{C}}$) được tính bởi hàm số $V(T)$, $T \in [0; 30]$. Biết hàm số $V(T)$ có bảng biến thiên như hình bên, với $T_1 \approx 3{{,}}97^\circ\text{{C}}$. Hỏi thể tích $V(T)$ giảm trong khoảng nhiệt độ nào?}}
{{\begin{{tikzpicture}}
  \tkzTabInit[nocadre,lgt=1.2,espcl=1.5,deltacl=0.5]
     {{$T$/0.7,$V'(T)$/0.7,$V(T)$/2}}
     {{$0$,$T_1$,$30$}}
  \tkzTabLine{{,-,0,+,}}
  \tkzTabVar{{+/$V(0)$,-/$V(T_1)$,+/$V(30)$}}
\end{{tikzpicture}}}}'''
    choices = [
        fr'''{{\True $(0; 3{{,}}97)$}}
''',
        fr'''{{$(0; 5)$}}
''',
        fr'''{{$(0; 10)$}}
''',
        fr'''{{$(0; 30)$}}
'''
    ]
    random.shuffle(choices)
    loi_giai = fr'''Dựa vào bảng biến thiên, hàm số nghịch biến trên khoảng $(0; T_1)$, tức $(0; 3{{,}}97)$.'''
    return caudan, choices, loi_giai


def CuoiChuong1_MC_Cau62():
    # De 2 Cau 12: Khẳng định sai của hàm bậc ba
    caudan = fr'''Cho hàm số $y = 7x^3 + 9x^2 - 3x - 4$. Khẳng định nào sau đây là sai?'''
    choices = [
        fr'''{{\True Giá trị cực tiểu $y = \frac{{1}}{{7}}$.}}
''',
        fr'''{{Giá trị cực đại $y = 1$.}}
''',
        fr'''{{Hàm số đạt cực tiểu tại $x = \frac{{1}}{{7}}$.}}
''',
        fr'''{{Hàm số đạt cực đại tại $x = -1$.}}
'''
    ]
    random.shuffle(choices)
    loi_giai = fr'''Ta có $y' = 21x^2 + 18x - 3 = 0 \iff x = -1$ hoặc $x = \frac{{1}}{{7}}$. \\
Cực tiểu tại $x = \frac{{1}}{{7}}$ có giá trị cực tiểu là $y(\frac{{1}}{{7}}) = -\frac{{207}}{{49}} \neq \frac{{1}}{{7}}$. \\
Do đó khẳng định giá trị cực tiểu $y = \frac{{1}}{{7}}$ là SAI.'''
    return caudan, choices, loi_giai


# ==================== DE 2: CHUONG II MC ====================

def CuoiChuong2_MC_Cau16():
    # De 2 Cau 5: Điểm đối xứng qua Oxy
    z = random.choice([2025, 2026, 2027])
    caudan = fr'''Trong không gian $Oxyz$, cho điểm $A(2025; 2026; -{z})$. Tọa độ $A'$ là điểm đối xứng với $A$ qua mặt phẳng $(Oxy)$ là:'''
    choices = [
        fr'''{{\True $A'(2025; 2026; {z})$}}
''',
        fr'''{{$A'(-2025; -2026; {z})$}}
''',
        fr'''{{$A'(-2025; -2026; -{z})$}}
''',
        fr'''{{$A'(-2025; 2026; -{z})$}}
'''
    ]
    random.shuffle(choices)
    loi_giai = fr'''Điểm đối xứng của $A(x; y; z)$ qua $(Oxy)$ có tọa độ là $A'(x; y; -z) = (2025; 2026; {z})$.'''
    return caudan, choices, loi_giai


def CuoiChuong2_MC_Cau17():
    # De 2 Cau 8: Mệnh đề sai về véctơ đồng phẳng
    caudan = fr'''Mệnh đề nào sau đây là sai?'''
    choices = [
        fr'''{{\True $\vec{{x}} = \vec{{a}} + \vec{{b}} + \vec{{c}}$ luôn đồng phẳng với hai vectơ $\vec{{a}}$ và $\vec{{b}}$.}}
''',
        fr'''{{$\vec{{a}}, \vec{{b}}, \vec{{c}}$ đồng phẳng nếu một trong ba vectơ đó bằng $\vec{{0}}$.}}
''',
        fr'''{{$\vec{{a}}, \vec{{b}}, \vec{{c}}$ đồng phẳng nếu có hai trong ba vectơ đó cùng phương.}}
''',
        fr'''{{Trong hình hộp $ABCD.A'B'C'D'$ ba vectơ $\vec{{AB'}}, \vec{{C'A'}}, \vec{{DA'}}$ đồng phẳng.}}
'''
    ]
    random.shuffle(choices)
    loi_giai = fr'''Vectơ $\vec{{x}} = \vec{{a}} + \vec{{b}} + \vec{{c}}$ chỉ đồng phẳng với $\vec{{a}}, \vec{{b}}$ khi $\vec{{c}}$ đồng phẳng với $\vec{{a}}, \vec{{b}}$. Do đó khẳng định trên là SAI.'''
    return caudan, choices, loi_giai


def CuoiChuong2_MC_Cau18():
    # De 2 Cau 9: Đẳng thức vectơ đúng trong hình hộp chữ nhật
    caudan = fr'''Cho hình hộp chữ nhật $ABCD.A'B'C'D'$. Đẳng thức nào sau đây đúng?'''
    choices = [
        fr'''{{\True $\vec{{BD}} = \vec{{B'D'}}$}}
''',
        fr'''{{$\vec{{AB}} = \vec{{CD}}$}}
''',
        fr'''{{$\vec{{AC}} = \vec{{C'A'}}$}}
''',
        fr'''{{$\vec{{AA'}} = \vec{{B'B}}$}}
'''
    ]
    random.shuffle(choices)
    loi_giai = fr'''Tứ giác $BDD'B'$ là hình chữ nhật nên $\vec{{BD}} = \vec{{B'D'}}$.'''
    return caudan, choices, loi_giai


def CuoiChuong2_MC_Cau19():
    # De 2 Cau 10: Tọa độ điểm B từ A và AB
    caudan = fr'''Trong không gian $Oxyz$, cho hai điểm $A(1; 2; -1)$, $\vec{{AB}} = (1; 3; 1)$ thì tọa độ của điểm $B$ là:'''
    choices = [
        fr'''{{\True $B(2; 5; 0)$}}
''',
        fr'''{{$B(0; -1; -2)$}}
''',
        fr'''{{$B(0; 1; 2)$}}
''',
        fr'''{{$B(-2; -5; 0)$}}
'''
    ]
    random.shuffle(choices)
    loi_giai = fr'''Ta có $\vec{{AB}} = (x_B - x_A; y_B - y_A; z_B - z_A) = (1; 3; 1) \implies B(2; 5; 0)$.'''
    return caudan, choices, loi_giai


# ==================== DE 2: CHUONG I TF ====================

def CuoiChuong1_TF_Cau15():
    # De 2 Cau 13: f(x) = 2sin(x) - x
    caudan = fr'''Cho hàm số $f(x) = 2\sin x - x$.'''
    choices = [
        fr'''{{\True Hàm số $f(x)$ liên tục trên $\mathbb{{R}}$.}}
''',
        fr'''{{\True Đạo hàm của hàm số đã cho là $f'(x) = 2\cos x - 1$.}}
''',
        fr'''{{\True Tập nghiệm của phương trình $f'(x) = 0$ là $\left\{{\pm \frac{{\pi}}{{3}} + k2\pi, k \in \mathbb{{Z}}\right\}}$.}}
''',
        fr'''{{\True Giá trị nhỏ nhất của $f(x)$ trên đoạn $\left[0; \frac{{\pi}}{{3}}\right]$ là $0$.}}
'''
    ]
    loi_giai = fr'''\begin{{itemize}}
  \item $f(x)$ xác định và liên tục trên $\mathbb{{R}}$. (Ý a \textbf{{Đúng}})
  \item $f'(x) = 2\cos x - 1$. (Ý b \textbf{{Đúng}})
  \item $f'(x) = 0 \iff \cos x = \frac{{1}}{{2}} \iff x = \pm \frac{{\pi}}{{3}} + k2\pi$. (Ý c \textbf{{Đúng}})
  \item Trên $\left[0; \frac{{\pi}}{{3}}\right]$, $f'(x) \ge 0 \implies \min f(x) = f(0) = 0$. (Ý d \textbf{{Đúng}})
\end{{itemize}}'''
    return caudan, choices, loi_giai


def CuoiChuong1_TF_Cau16():
    # De 2 Cau 14: BBT y = ax^3 + bx^2 + cx + d
    caudan = fr'''\immini{{Cho hàm số $y = f(x) = ax^3 + bx^2 + cx + d$ có bảng biến thiên như hình bên. Xét tính đúng sai của các khẳng định sau:}}
{{\begin{{tikzpicture}}
  \tkzTabInit[nocadre,lgt=1.2,espcl=2,deltacl=0.5]
     {{$x$/0.7,$f'(x)$/0.7,$f(x)$/2}}
     {{$-\infty$,$-2$,$0$,$+\infty$}}
  \tkzTabLine{{,-,0,+,0,-,}}
  \tkzTabVar{{+/$+\infty$,-/$0$,+/$4$,-/$-\infty$}}
\end{{tikzpicture}}}}'''
    choices = [
        fr'''{{Hàm số nghịch biến trên khoảng $(-\infty; 4)$.}}
''',
        fr'''{{Hàm số đạt giá trị lớn nhất là $4$.}}
''',
        fr'''{{\True Đường thẳng $y = 2$ cắt đồ thị hàm số tại ba điểm phân biệt.}}
''',
        fr'''{{\True Trong bốn hệ số $a, b, c, d$ có đúng hai số âm.}}
'''
    ]
    loi_giai = fr'''\begin{{itemize}}
  \item Hàm số chỉ nghịch biến trên $(-\infty; -2)$ và $(0; +\infty)$. (Ý a \textbf{{Sai}})
  \item $\lim\limits_{{x \to -\infty}} f(x) = +\infty$ nên không có GTLN trên $\mathbb{{R}}$. (Ý b \textbf{{Sai}})
  \item $0 < 2 < 4$ nên $y = 2$ cắt đồ thị tại $3$ điểm phân biệt. (Ý c \textbf{{Đúng}})
  \item $a < 0, b = 3a < 0, c = 0, d = 4 > 0 \implies$ đúng $2$ số âm là $a, b$. (Ý d \textbf{{Đúng}})
\end{{itemize}}'''
    return caudan, choices, loi_giai


# ==================== DE 2: CHUONG II TF ====================

def CuoiChuong2_TF_Cau3():
    # De 2 Cau 15: Hình hộp chữ nhật trong không gian Oxyz
    caudan = fr'''Trong không gian $Oxyz$, cho hình hộp chữ nhật $ABCD.A'B'C'D'$ có đỉnh $A$ trùng với gốc tọa độ $O$, các vectơ $\vec{{AB}}, \vec{{AD}}, \vec{{AA'}}$ theo thứ tự cùng hướng với các vectơ $\vec{{i}}, \vec{{j}}, \vec{{k}}$ và $AB = 4, AD = 3, \left(\widehat{{\vec{{AC}}, \vec{{AC'}}}}\right) = 30^\circ$.'''
    choices = [
        fr'''{{\True $\vec{{AB}} = 4\vec{{i}} + 0\vec{{j}} + 0\vec{{k}}$.}}
''',
        fr'''{{$C'\left(4; 3; 5\sqrt{{3}}\right)$.}}
''',
        fr'''{{$\vec{{AC}} = 3\vec{{i}} + 4\vec{{j}} + 0\vec{{k}}$.}}
''',
        fr'''{{\True Gọi $x, y, z$ theo thứ tự là số đo các góc hợp bởi vectơ $\vec{{AC'}}$ với các vectơ $\vec{{AB}}, \vec{{AD}}, \vec{{AA'}}$. Khi đó $\cos^2 x + \cos^2 y + \cos^2 z = 1$.}}
'''
    ]
    loi_giai = fr'''\begin{{itemize}}
  \item $\vec{{AB}} = (4; 0; 0) = 4\vec{{i}}$. (Ý a \textbf{{Đúng}})
  \item $AC = 5 \implies CC' = 5\tan 30^\circ = \frac{{5\sqrt{{3}}}}{{3}} \implies C'(4; 3; \frac{{5\sqrt{{3}}}}{{3}})$. (Ý b \textbf{{Sai}})
  \item $\vec{{AC}} = 4\vec{{i}} + 3\vec{{j}}$. (Ý c \textbf{{Sai}})
  \item Tổng bình phương cosin chỉ phương luôn bằng $1$. (Ý d \textbf{{Đúng}})
\end{{itemize}}'''
    return caudan, choices, loi_giai


def CuoiChuong2_TF_Cau4():
    # De 2 Cau 16: Chuyển động máy bay và ra đa
    caudan = fr'''Trong không gian chọn hệ trục tọa độ $Oxyz$ cho trước, trong đó xem mặt phẳng $(Oxy)$ là mặt đất, mỗi đơn vị trên trục tương ứng với $1\text{{ km}}$, một ra đa được đặt tại vị trí gốc tọa độ $O$ phát hiện một máy bay chiến đấu di chuyển với vận tốc và hướng không đổi từ điểm $M(500; 200; 10)$ đến điểm $N(300; 800; 10)$ trong $40$ phút.'''
    choices = [
        fr'''{{\True Khoảng cách $MN = 200\sqrt{{10}}\text{{ km}}$.}}
''',
        fr'''{{Khi đến $N$ máy bay tiếp tục giữ nguyên vận tốc và hướng bay thì tọa độ của máy bay sau $8$ phút tiếp theo là $Q(a; b; c)$ với $a + b + c = 1030$.}}
''',
        fr'''{{\True Máy bay chiến đấu khi bay từ $M$ đến $N$ luôn cách mặt đất là $10\text{{ km}}$.}}
''',
        fr'''{{\True Góc $\widehat{{MON}}$ được gọi là góc quét của ra đa khi quan sát máy bay chiến đấu bay từ $M$ đến $N$. Trong tình huống trên góc quét $\widehat{{MON}}$ lớn hơn $45^\circ$.}}
'''
    ]
    loi_giai = fr'''\begin{{itemize}}
  \item $MN = \sqrt{{(-200)^2 + 600^2}} = 200\sqrt{{10}}\text{{ km}}$. (Ý a \textbf{{Đúng}})
  \item $\vec{{v}} = (-5; 15; 0) \implies Q = N + 8\vec{{v}} = (260; 920; 10) \implies a + b + c = 1190 \neq 1030$. (Ý b \textbf{{Sai}})
  \item Cao độ $z = 10$ không đổi $\implies$ luôn cách mặt đất $10\text{{ km}}$. (Ý c \textbf{{Đúng}})
  \item $\cos \widehat{{MON}} \approx 0{{,}}6734 \implies \widehat{{MON}} \approx 47{{,}}67^\circ > 45^\circ$. (Ý d \textbf{{Đúng}})
\end{{itemize}}'''
    return caudan, choices, loi_giai


# ==================== DE 2: CHUONG I SA ====================

def CuoiChuong1_SA_Cau31():
    # De 2 Cau 17: Tính f(5) từ đồ thị cực trị
    caudan = fr'''\immini{{Cho hàm số $y = f(x) = ax^3 + bx^2 + cx + d$ có đồ thị $(C)$ như hình vẽ bên. Khi đó $f(5)$ bằng}}
{{\begin{{tikzpicture}}[line join=round, line cap=round, >=stealth, scale=0.65]
  \draw[->] (-1.5,0) -- (2.5,0) node[below] {{$x$}};
  \draw[->] (0,-1.5) -- (0,2.5) node[left] {{$y$}};
  \draw (0,0) node[below left] {{$O$}};
  \draw (-1,0) node[below] {{$-1$}};
  \draw (1,0) node[below] {{$1$}};
  \draw (0,1) node[left] {{$1$}};
  \draw (0,-1) node[left] {{$-1$}};
  \draw[dashed] (-1,0) -- (-1,1) -- (0,1);
  \draw[dashed] (1,0) -- (1,-1) -- (0,-1);
  \draw[samples=200, domain=-1.6:2.2, smooth] plot (\x, {{0.5*(\x)^3 - 1.5*(\x)}});
  \node at (2.3,1.8) {{$(C)$}};
\end{{tikzpicture}}}}'''
    dapan = "55"
    loi_giai = fr'''Hàm số có dạng $f(x) = ax^3 - 3ax + d$. \\
Qua $(0; 0) \implies d = 0$. Qua $(1; -1) \implies a - 3a = -1 \implies a = \frac{{1}}{{2}}$. \\
Do đó $f(x) = \frac{{1}}{{2}}x^3 - \frac{{3}}{{2}}x \implies f(5) = \frac{{125 - 15}}{{2}} = 55$.'''
    return caudan, dapan, loi_giai


def CuoiChuong1_SA_Cau32():
    # De 2 Cau 18: Giao điểm 2 tiệm cận xiên hàm chứa căn
    caudan = fr'''Cho hàm số $y = 2x + 1 + \sqrt{{x^2 - 4x + 5}}$. Biết đồ thị hàm số có hai tiệm cận xiên cắt nhau tại $I(a; b)$. Tính $a + b$.'''
    dapan = "7"
    loi_giai = fr'''Khi $x \to +\infty$: TCX là $y = 3x - 1$. \\
Khi $x \to -\infty$: TCX là $y = x + 3$. \\
Giao điểm $I: 3x - 1 = x + 3 \iff x = 2 \implies y = 5 \implies I(2; 5) \implies a + b = 7$.'''
    return caudan, dapan, loi_giai


def CuoiChuong1_SA_Cau33():
    # De 2 Cau 21: Lực tác dụng của bể cá lên từng chân đế
    caudan = fr'''Một bình cá cảnh có dạng một chỏm cầu được đặt trên một chân đế. Biết tổng khối lượng bể cá là $20\text{{ kg}}$, ba chân đế là ba cạnh bên của một hình chóp cụt đều có độ dài cạnh bên bằng $50\text{{ cm}}$, hai đáy có độ dài lần lượt là $30\text{{ cm}}$ và $20\text{{ cm}}$. Biết gia tốc trọng trường bằng $10\text{{ m/s}}^2$, tính độ lớn lực tác dụng của bể cá lên từng chân đế (Kết quả làm tròn đến chữ số thứ nhất phần thập phân).'''
    dapan = "67,1"
    loi_giai = fr'''Trọng lượng $P = 200\text{{ N}}$. Mỗi chân đế chịu lực thẳng đứng $P_1 = \frac{{200}}{{3}}\text{{ N}}$. \\
$\Delta R = \frac{{10\sqrt{{3}}}}{{3}}\text{{ cm}} \implies \cos \alpha = \frac{{\sqrt{{3}}}}{{15}} \implies \sin \alpha = \frac{{\sqrt{{222}}}}{{15}}$. \\
Lực nén dọc chân đế: $F = \frac{{P_1}}{{\sin \alpha}} = \frac{{1000}}{{\sqrt{{222}}}} \approx 67{{,}}1\text{{ N}}$.'''
    return caudan, dapan, loi_giai


def CuoiChuong1_SA_Cau34():
    # De 2 Cau 22: Tối ưu trạm cung cấp nước sạch bên bờ sông
    caudan = fr'''Có hai xã $A, B$ cùng ở một bên bờ sông. Khoảng cách từ hai xã đó đến bờ sông lần lượt là $AA' = 500\text{{ m}}, BB' = 600\text{{ m}}$. Người ta đo được $A'B' = 2200\text{{ m}}$. Các kỹ sư muốn xây dựng một trạm cung cấp nước sạch nằm cạnh bên bờ sông cho người dân của hai xã sử dụng. Để tiết kiệm chi phí, các kỹ sư phải chọn một vị trí $M$ của trạm cung cấp nước sạch đó trên đoạn $A'B'$ sao cho tổng khoảng cách từ hai xã đến vị trí $M$ là nhỏ nhất. Hãy tìm giá trị nhỏ nhất của tổng khoảng cách đó.'''
    dapan = "2460"
    loi_giai = fr'''Lấy $A''$ đối xứng với $A$ qua $A'B'$. Tổng khoảng cách $AM + BM = A''M + BM \ge A''B$. \\
$A''B = \sqrt{{(AA' + BB')^2 + A'B'^2}} = \sqrt{{1100^2 + 2200^2}} = 1100\sqrt{{5}} \approx 2460\text{{ m}}$.'''
    return caudan, dapan, loi_giai


# ==================== DE 2: CHUONG II SA ====================

def De2_CuoiChuong2_SA_Cau3():
    # De 2 Cau 19: Lăng trụ phân tích vectơ ngẫu nhiên hóa
    cfgs = [
        {"mid": "P", "edge": "BB'", "u": 1, "v": -5, "w": 2, "a": 1, "b": 1, "c_val": 0.5, "ans": -3},
        {"mid": "P", "edge": "BB'", "u": 2, "v": 3,  "w": 4, "a": 1, "b": 1, "c_val": 0.5, "ans": 7},
        {"mid": "Q", "edge": "CC'", "u": 3, "v": -2, "w": 6, "a": 1, "b": 0, "c_val": 0.5, "ans": 6},
        {"mid": "P", "edge": "BB'", "u": 4, "v": -1, "w": 2, "a": 1, "b": 1, "c_val": 0.5, "ans": 4},
    ]
    cfg = random.choice(cfgs)
    mid = cfg["mid"]
    edge = cfg["edge"]
    u, v, w = cfg["u"], cfg["v"], cfg["w"]
    ans = cfg["ans"]
    
    u_str = f"{u}a" if u != 1 else "a"
    v_str = f"+ {v}b" if v > 0 else (f"- {abs(v)}b" if v < 0 else "")
    w_str = f"+ {w}c" if w > 0 else (f"- {abs(w)}c" if w < 0 else "")
    T_expr = f"{u_str} {v_str} {w_str}".strip()

    caudan = fr'''Cho hình lăng trụ $ABC.A'B'C'$, ${mid}$ là trung điểm của ${edge}$. Biết $\vec{{A{mid}}} = a \cdot \vec{{AC}} + b \cdot \vec{{CB}} + c \cdot \vec{{AA'}}$. Tính giá trị biểu thức $T = {T_expr}$.'''
    dapan = str(ans)
    loi_giai = fr'''Ta có $\vec{{A{mid}}} = \vec{{A{edge[0]}}} + \dfrac{{1}}{{2}}\vec{{{edge}}} = {cfg["a"]}\vec{{AC}} + {cfg["b"]}\vec{{CB}} + \dfrac{{1}}{{2}}\vec{{AA'}}$. \\
Suy ra $a = {cfg["a"]}, b = {cfg["b"]}, c = \dfrac{{1}}{{2}} \implies T = {ans}$.'''
    return caudan, dapan, loi_giai


def De2_CuoiChuong2_SA_Cau4():
    # De 2 Cau 20: Hình hộp chữ nhật Oxyz, trọng tâm G của A'BD ngẫu nhiên hóa
    boxes = [
        {"a": 10, "b": 16, "c": 8,  "m": 1, "n": 2, "p": 3, "T": 22},
        {"a": 12, "b": 15, "c": 9,  "m": 1, "n": 1, "p": 1, "T": 12},
        {"a": 9,  "b": 12, "c": 6,  "m": 2, "n": 1, "p": 3, "T": 16},
        {"a": 15, "b": 9,  "c": 12, "m": 1, "n": 2, "p": 1, "T": 15},
        {"a": 6,  "b": 12, "c": 15, "m": 3, "n": 1, "p": 2, "T": 20},
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
    loi_giai = fr'''$A'(0; 0; {c}), B({a}; 0; 0), D(0; {bb}; 0)$. \\
Trọng tâm $G: x = \dfrac{{{a}}}{{3}}, y = \dfrac{{{bb}}}{{3}}, z = \dfrac{{{c}}}{{3}}$. \\
$T = {expr_str} = \dfrac{{{m*a + n*bb + p*c}}}{{3}} = {T_ans}$.'''
    return caudan, dapan, loi_giai


# ==============================================================================
# BÀI TẬP CUỐI CHƯƠNG IV - TRẢ LỜI NGẮN (6 CÂU GÔM GỌN THEO MỨC ĐỘ)
# ==============================================================================

# ------------------------------------------------------------------------------
# CÂU 1: MỨC ĐỘ NHẬN BIẾT (DẠNG 1) - NGUYÊN HÀM CƠ BẢN VÀ GIÁ TRỊ F(x)
# ------------------------------------------------------------------------------
def CuoiChuong4_SA_Cau1():
    sub_type = random.choice([1, 2, 3])
    
    if sub_type == 1:
        # F(x) là nguyên hàm của f(x) = 2x + a thỏa F(1) = y1, tính F(2)
        a = random.choice([1, 2, 3, 4])
        y1 = random.choice([3, 5, 7, 10])
        # F(x) = x^2 + ax + C. F(1) = 1 + a + C = y1 => C = y1 - 1 - a
        C = y1 - 1 - a
        # F(2) = 4 + 2a + C = 4 + 2a + y1 - 1 - a = 3 + a + y1
        ans = 3 + a + y1
        caudan = fr'''Biết rằng hàm số $F(x)$ là một nguyên hàm của hàm số $f(x) = 2x + {a}$ trên $\mathbb{{R}}$ và $F(1) = {y1}$. Tính giá trị của $F(2)$.'''
        dapan = str(ans)
        sign_C = f"{C:+d}" if C != 0 else ""
        loi_giai = fr'''Họ nguyên hàm của hàm số $f(x) = 2x + {a}$ là: \\
$F(x) = \displaystyle\int (2x + {a})\,\mathrm{{d}}x = x^2 + {a}x + C$. \\
Vì $F(1) = {y1} \implies 1^2 + {a}(1) + C = {y1} \implies C = {C}$. \\
Do đó $F(x) = x^2 + {a}x {sign_C}$. \\
Vậy $F(2) = 2^2 + {a}(2) {sign_C} = {ans}$.'''
        return caudan, dapan, loi_giai

    elif sub_type == 2:
        # F'(x) = f(x), biết F(a) và F(b), tính tích phân f(x)
        a = random.choice([0, 1])
        b = a + random.choice([2, 3, 4])
        y_a = random.choice([2, 5, -1])
        y_b = y_a + random.choice([6, 8, 10, 12])
        ans = y_b - y_a
        caudan = fr'''Cho hàm số $f(x)$ liên tục trên đoạn $[{a}; {b}]$. Giả sử $F(x)$ là một nguyên hàm của $f(x)$ trên $[{a}; {b}]$ thỏa mãn $F({a}) = {y_a}$ và $F({b}) = {y_b}$. Tính giá trị của tích phân $I = \displaystyle\int_{{{a}}}^{{{b}}} f(x)\,\mathrm{{d}}x$.'''
        dapan = str(ans)
        loi_giai = fr'''Theo công thức Newton - Leibniz, ta có: \\
$I = \displaystyle\int_{{{a}}}^{{{b}}} f(x)\,\mathrm{{d}}x = F({b}) - F({a}) = {y_b} - ({y_a}) = {ans}$.'''
        return caudan, dapan, loi_giai

    else:
        # Tính tích phân cơ bản đa thức bậc nhất \int_0^a (mx + n) dx
        a = random.choice([2, 4])
        m = random.choice([2, 4])
        n = random.choice([1, 3, 5])
        # \int_0^a (mx + n) dx = m*a^2/2 + n*a
        ans = (m * a**2) // 2 + n * a
        caudan = fr'''Tính tích phân $I = \displaystyle\int_{{0}}^{{{a}}} ({m}x + {n})\,\mathrm{{d}}x$.'''
        dapan = str(ans)
        loi_giai = fr'''Ta có: \\
$I = \displaystyle\int_{{0}}^{{{a}}} ({m}x + {n})\,\mathrm{{d}}x = \left.\left(\dfrac{{{m}x^2}}{{2}} + {n}x\right)\right|_{{0}}^{{{a}}} = \dfrac{{{m} \cdot {a}^2}}{{2}} + {n} \cdot {a} = {ans}$.'''
        return caudan, dapan, loi_giai


# ------------------------------------------------------------------------------
# CÂU 2: MỨC ĐỘ NHẬN BIẾT (DẠNG 2) - TÍNH CHẤT TÍCH PHÂN (CHÈN CẬN, TUYẾN TÍNH)
# ------------------------------------------------------------------------------
def CuoiChuong4_SA_Cau2():
    sub_type = random.choice([1, 2, 3])
    
    if sub_type == 1:
        # Chèn cận: \int_a^b = \int_a^c + \int_c^b
        a, c, b = 1, 3, 5
        I_ac = random.choice([2, 3, 4, 5])
        I_cb = random.choice([6, 7, 8, 9])
        ans = I_ac + I_cb
        caudan = fr'''Cho hàm số $f(x)$ liên tục trên đoạn $[{a}; {b}]$. Biết $\displaystyle\int_{{{a}}}^{{{c}}} f(x)\,\mathrm{{d}}x = {I_ac}$ và $\displaystyle\int_{{{c}}}^{{{b}}} f(x)\,\mathrm{{d}}x = {I_cb}$. Tính tích phân $I = \displaystyle\int_{{{a}}}^{{{b}}} f(x)\,\mathrm{{d}}x$.'''
        dapan = str(ans)
        loi_giai = fr'''Áp dụng tính chất chèn cận của tích phân: \\
$I = \displaystyle\int_{{{a}}}^{{{b}}} f(x)\,\mathrm{{d}}x = \displaystyle\int_{{{a}}}^{{{c}}} f(x)\,\mathrm{{d}}x + \displaystyle\int_{{{c}}}^{{{b}}} f(x)\,\mathrm{{d}}x = {I_ac} + {I_cb} = {ans}$.'''
        return caudan, dapan, loi_giai

    elif sub_type == 2:
        # Tính chất tuyến tính: \int (m f + n g) dx = m \int f + n \int g
        I_f = random.choice([2, 3, 5])
        I_g = random.choice([1, 4, -2])
        m = 2
        n = 3
        ans = m * I_f + n * I_g
        caudan = fr'''Cho hai hàm số $f(x)$ và $g(x)$ liên tục trên $[0; 2]$. Biết rằng $\displaystyle\int_{{0}}^{{2}} f(x)\,\mathrm{{d}}x = {I_f}$ và $\displaystyle\int_{{0}}^{{2}} g(x)\,\mathrm{{d}}x = {I_g}$. Tính giá trị của tích phân $J = \displaystyle\int_{{0}}^{{2}} [2f(x) + 3g(x)]\,\mathrm{{d}}x$.'''
        dapan = str(ans)
        loi_giai = fr'''Áp dụng tính chất tuyến tính của tích phân: \\
$J = \displaystyle\int_{{0}}^{{2}} [2f(x) + 3g(x)]\,\mathrm{{d}}x = 2\displaystyle\int_{{0}}^{{2}} f(x)\,\mathrm{{d}}x + 3\displaystyle\int_{{0}}^{{2}} g(x)\,\mathrm{{d}}x$ \\
$= 2({I_f}) + 3({I_g}) = {ans}$.'''
        return caudan, dapan, loi_giai

    else:
        # Tích phân đạo hàm: f(b) = f(a) + \int_a^b f'(x) dx
        a = 1
        b = 4
        y_a = random.choice([3, 5, 7])
        K = random.choice([10, 15, 20])
        ans = y_a + K
        caudan = fr'''Cho hàm số $f(x)$ có đạo hàm liên tục trên $[1; 4]$ thỏa mãn $f(1) = {y_a}$ và $\displaystyle\int_{{1}}^{{4}} f'(x)\,\mathrm{{d}}x = {K}$. Tính giá trị của $f(4)$.'''
        dapan = str(ans)
        loi_giai = fr'''Theo định lý cơ bản của giải tích: \\
$\displaystyle\int_{{1}}^{{4}} f'(x)\,\mathrm{{d}}x = f(4) - f(1) \implies f(4) = f(1) + \displaystyle\int_{{1}}^{{4}} f'(x)\,\mathrm{{d}}x = {y_a} + {K} = {ans}$.'''
        return caudan, dapan, loi_giai


# ------------------------------------------------------------------------------
# CÂU 3: MỨC ĐỘ THÔNG HIỂU - TÍNH TÍCH PHÂN ĐẠI SỐ, LƯỢNG GIÁC, MŨ
# ------------------------------------------------------------------------------
def CuoiChuong4_SA_Cau3():
    sub_type = random.choice([1, 2, 3])
    
    if sub_type == 1:
        # \int_0^1 (3x^2 + 2kx + 1) dx = 1 + k + 1 = k + 2
        k = random.choice([2, 3, 5, 7])
        ans = k + 2
        caudan = fr'''Tính giá trị của tích phân $I = \displaystyle\int_{{0}}^{{1}} (3x^2 + {2*k}x + 1)\,\mathrm{{d}}x$.'''
        dapan = str(ans)
        loi_giai = fr'''Ta có: \\
$I = \left.\left(x^3 + {k}x^2 + x\right)\right|_{{0}}^{{1}} = (1^3 + {k}\cdot 1^2 + 1) - 0 = {ans}$.'''
        return caudan, dapan, loi_giai

    elif sub_type == 2:
        # \int_0^{\pi/2} (a cos x + b sin x) dx = a [sin x]_0^{\pi/2} - b [cos x]_0^{\pi/2} = a(1 - 0) - b(0 - 1) = a + b
        a = random.choice([2, 3, 4])
        b = random.choice([1, 3, 5])
        ans = a + b
        caudan = fr'''Tính giá trị của tích phân $I = \displaystyle\int_{{0}}^{{\frac{{\pi}}{{2}}}} ({a}\cos x + {b}\sin x)\,\mathrm{{d}}x$.'''
        dapan = str(ans)
        loi_giai = fr'''Ta có: \\
$I = \left.({a}\sin x - {b}\cos x)\right|_{{0}}^{{\frac{{\pi}}{{2}}}} = \left({a}\sin\dfrac{{\pi}}{{2}} - {b}\cos\dfrac{{\pi}}{{2}}\right) - ({a}\sin 0 - {b}\cos 0) = {a}(1) - {b}(0) - (0 - {b}(1)) = {a} + {b} = {ans}$.'''
        return caudan, dapan, loi_giai

    else:
        # Tích phân từng phần \int_0^1 x e^x dx = [x e^x - e^x]_0^1 = (e - e) - (0 - 1) = 1
        # Hoặc \int_0^1 (2x + 1) e^x dx = 2(1) + (e - 1) = e + 1 (not integer)
        # Let's use \int_0^1 (x + k) e^x dx = 1 + k(e - 1)
        # Or \int_1^2 (a/x + b) dx = a ln 2 + b.
        # Let's do: \int_0^1 (2x + 3) dx = 1 + 3 = 4 or \int_0^2 (3x^2 - 4x + 1) dx = 8 - 8 + 2 = 2
        p = random.choice([2, 3, 4])
        # \int_0^2 (3x^2 - 2px) dx = [x^3 - p x^2]_0^2 = 8 - 4p
        ans = 8 - 4 * p
        caudan = fr'''Tính giá trị của tích phân $I = \displaystyle\int_{{0}}^{{2}} (3x^2 - {2*p}x)\,\mathrm{{d}}x$.'''
        dapan = str(ans)
        loi_giai = fr'''Ta có: \\
$I = \displaystyle\int_{{0}}^{{2}} (3x^2 - {2*p}x)\,\mathrm{{d}}x = \left.\left(x^3 - {p}x^2\right)\right|_{{0}}^{{2}} = (2^3 - {p} \cdot 2^2) - 0 = 8 - {4*p} = {ans}$.'''
        return caudan, dapan, loi_giai


# ------------------------------------------------------------------------------
# CÂU 4: MỨC ĐỘ VẬN DỤNG THẤP - DIỆN TÍCH HÌNH PHẲNG & THỂ TÍCH TRÒN XOAY
# ------------------------------------------------------------------------------
def CuoiChuong4_SA_Cau4():
    sub_type = random.choice([1, 2, 3])
    
    if sub_type == 1:
        # Diện tích hình phẳng giới hạn bởi y = a^2 - x^2 và Ox: S = \int_{-a}^a (a^2 - x^2) dx = 4 a^3 / 3
        # If a = 3: S = 4(27)/3 = 36!
        a = 3
        ans = 36
        caudan = fr'''Tính diện tích hình phẳng giới hạn bởi parabol $(P)\colon y = 9 - x^2$ và trục hoành $Ox$.'''
        dapan = str(ans)
        loi_giai = fr'''Phương trình hoành độ giao điểm của $(P)$ với trục hoành $Ox$ là: \\
$9 - x^2 = 0 \iff x = -3$ hoặc $x = 3$. \\
Trên đoạn $[-3; 3]$, ta có $9 - x^2 \ge 0$. \\
Diện tích hình phẳng cần tìm là: \\
$S = \displaystyle\int_{{-3}}^{{3}} (9 - x^2)\,\mathrm{{d}}x = \left.\left(9x - \dfrac{{x^3}}{{3}}\right)\right|_{{-3}}^{{3}} = \left(27 - 9\right) - \left(-27 + 9\right) = 18 - (-18) = {ans}$.'''
        return caudan, dapan, loi_giai

    elif sub_type == 2:
        # Thể tích khối tròn xoay V sinh bởi y = sqrt(x), Ox, x = 0, x = a. V = \pi \int_0^a x dx = \pi * a^2 / 2.
        # Tính V / \pi
        a = random.choice([4, 6, 8])
        ans = (a**2) // 2
        caudan = fr'''Cho hình phẳng $(H)$ giới hạn bởi đồ thị hàm số $y = \sqrt{{x}}$, trục hoành $Ox$ và đường thẳng $x = {a}$. Khi quay hình phẳng $(H)$ xung quanh trục $Ox$, ta được khối tròn xoay có thể tích là $V = k\pi$. Tính giá trị của $k$.'''
        dapan = str(ans)
        loi_giai = fr'''Thể tích khối tròn xoay tạo thành khi quay $(H)$ quanh trục hoành $Ox$ là: \\
$V = \pi \displaystyle\int_{{0}}^{{{a}}} (\sqrt{{x}})^2\,\mathrm{{d}}x = \pi \displaystyle\int_{{0}}^{{{a}}} x\,\mathrm{{d}}x = \pi \left.\left(\dfrac{{x^2}}{{2}}\right)\right|_{{0}}^{{{a}}} = \dfrac{{{a}^2}}{{2}}\pi = {ans}\pi$. \\
Vậy $k = {ans}$.'''
        return caudan, dapan, loi_giai

    else:
        # Diện tích hình phẳng giới hạn bởi y = x^2 - 2x và Ox: S = \int_0^2 |x^2 - 2x| dx = 4/3
        # Or y = 3x^2 - 6x và Ox: S = \int_0^2 |3x^2 - 6x| dx = [3x^2 - x^3]_0^2 = 12 - 8 = 4!
        k = random.choice([3, 6])
        # y = k*x*(2 - x) => roots 0 and 2.
        # S = k \int_0^2 (2x - x^2) dx = k [x^2 - x^3/3]_0^2 = k(4 - 8/3) = 4k/3.
        # If k = 3: S = 4. If k = 6: S = 8.
        ans = (4 * k) // 3
        caudan = fr'''Tính diện tích hình phẳng giới hạn bởi parabol $(P)\colon y = {2*k}x - {k}x^2$ và trục hoành $Ox$.'''
        dapan = str(ans)
        loi_giai = fr'''Phương trình hoành độ giao điểm: \\
${2*k}x - {k}x^2 = 0 \iff {k}x(2 - x) = 0 \iff x = 0$ hoặc $x = 2$. \\
Trên đoạn $[0; 2]$, ${2*k}x - {k}x^2 \ge 0$. \\
Diện tích hình phẳng là: \\
$S = \displaystyle\int_{{0}}^{{2}} ({2*k}x - {k}x^2)\,\mathrm{{d}}x = \left.\left({k}x^2 - \dfrac{{{k}x^3}}{{3}}\right)\right|_{{0}}^{{2}} = {k}(4) - \dfrac{{{k}(8)}}{{3}} = \dfrac{{4 \cdot {k}}}{{3}} = {ans}$.'''
        return caudan, dapan, loi_giai


# ------------------------------------------------------------------------------
# CÂU 5: MỨC ĐỘ VẬN DỤNG CAO - TÍCH PHÂN HÀM PHÂN NHÁNH & BÀI TOÁN THAM SỐ
# ------------------------------------------------------------------------------
def CuoiChuong4_SA_Cau5():
    sub_type = random.choice([1, 2])
    
    if sub_type == 1:
        # Hàm phân nhánh f(x) = { 2x + 1 khi x >= 1; 3x^2 khi x < 1 }. Tính \int_0^2 f(x) dx
        # \int_0^1 3x^2 dx = [x^3]_0^1 = 1
        # \int_1^2 (2x + 1) dx = [x^2 + x]_1^2 = (4 + 2) - (1 + 1) = 6 - 2 = 4
        # Total = 1 + 4 = 5
        ans = 5
        caudan = fr'''Cho hàm số $f(x)$ xác định trên $\mathbb{{R}}$ bởi công thức:
$f(x) = \begin{{cases}} 2x + 1 & \text{{khi }} x \ge 1 \\ 3x^2 & \text{{khi }} x < 1 \end{{cases}}$. \\
Tính giá trị của tích phân $I = \displaystyle\int_{{0}}^{{2}} f(x)\,\mathrm{{d}}x$.'''
        dapan = str(ans)
        loi_giai = fr'''Tách tích phân theo điểm ranh giới $x = 1$: \\
$I = \displaystyle\int_{{0}}^{{1}} f(x)\,\mathrm{{d}}x + \displaystyle\int_{{1}}^{{2}} f(x)\,\mathrm{{d}}x$ \\
$= \displaystyle\int_{{0}}^{{1}} 3x^2\,\mathrm{{d}}x + \displaystyle\int_{{1}}^{{2}} (2x + 1)\,\mathrm{{d}}x$ \\
$= \left.x^3\right|_{{0}}^{{1}} + \left.\left(x^2 + x\right)\right|_{{1}}^{{2}}$ \\
$= (1 - 0) + [(4 + 2) - (1 + 1)] = 1 + 4 = {ans}$.'''
        return caudan, dapan, loi_giai

    else:
        # Tìm tham số m > 0 để \int_0^m (2x - 4) dx = 0
        # [x^2 - 4x]_0^m = m^2 - 4m = 0 => m = 4
        m_ans = random.choice([4, 6, 8])
        # \int_0^m (2x - m_ans) dx = m^2 - m_ans*m = 0
        caudan = fr'''Tìm giá trị dương của tham số $m$ sao cho tích phân $\displaystyle\int_{{0}}^{{m}} (2x - {m_ans})\,\mathrm{{d}}x = 0$.'''
        dapan = str(m_ans)
        loi_giai = fr'''Ta có: \\
$\displaystyle\int_{{0}}^{{m}} (2x - {m_ans})\,\mathrm{{d}}x = \left.\left(x^2 - {m_ans}x\right)\right|_{{0}}^{{m}} = m^2 - {m_ans}m$. \\
Để tích phân bằng $0$ thì $m^2 - {m_ans}m = 0 \iff m(m - {m_ans}) = 0$. \\
Vì $m > 0$ nên $m = {m_ans}$.'''
        return caudan, dapan, loi_giai


# ------------------------------------------------------------------------------
# CÂU 6: TOÁN THỰC TẾ - VẬN TỐC, QUÃNG ĐƯỜNG, LƯU LƯỢNG NƯỚC, ĐIỆN NĂNG
# ------------------------------------------------------------------------------
def CuoiChuong4_SA_Cau6():
    sub_type = random.choice([1, 2, 3])
    
    if sub_type == 1:
        # Ô tô phanh: v(t) = v0 - kt. s = \int_0^{t_stop} v(t) dt = v0^2 / (2k)
        k = random.choice([2, 4, 5])
        t_stop = random.choice([4, 5, 6, 8, 10])
        v0 = k * t_stop
        ans = (v0 * t_stop) // 2
        caudan = fr'''Một ô tô đang di chuyển với vận tốc ${v0}\text{{ m/s}}$ thì người lái xe phát hiện chướng ngại vật và đạp phanh. Kể từ thời điểm đó, ô tô chuyển động chậm dần đều với vận tốc $v(t) = {v0} - {k}t\text{{ (m/s)}}$, trong đó $t$ là thời gian tính bằng giây kể từ lúc bắt đầu đạp phanh. Quãng đường ô tô di chuyển được từ lúc đạp phanh đến khi dừng hẳn là bao nhiêu mét?'''
        dapan = str(ans)
        loi_giai = fr'''Khi ô tô dừng hẳn, vận tốc $v(t) = 0 \iff {v0} - {k}t = 0 \iff t = {t_stop}\text{{ (giây)}}$. \\
Quãng đường ô tô di chuyển được là: \\
$s = \displaystyle\int_{{0}}^{{{t_stop}}} ({v0} - {k}t)\,\mathrm{{d}}t = \left.\left({v0}t - \dfrac{{{k}t^2}}{{2}}\right)\right|_{{0}}^{{{t_stop}}} = {v0}({t_stop}) - \dfrac{{{k}({t_stop}^2)}}{{2}} = {ans}\text{{ (m)}}$.'''
        return caudan, dapan, loi_giai

    elif sub_type == 2:
        # Bơm nước vào bể: v(t) = at + b lít/phút sau T phút
        # a = 2, b = 20, T = 10. V = \int_0^{10} (2t + 20) dt = [t^2 + 20t]_0^{10} = 100 + 200 = 300 lít
        a = random.choice([2, 4])
        b = random.choice([10, 20, 30])
        T = random.choice([5, 10, 15])
        ans = (a * T**2) // 2 + b * T
        caudan = fr'''Một máy bơm nước bắt đầu bơm nước vào một bể chứa chưa có nước. Tốc độ bơm tại thời điểm $t$ (phút) được cho bởi hàm số $v(t) = {a}t + {b}$ (lít/phút). Hỏi sau ${T}$ phút, thể tích nước trong bể là bao nhiêu lít?'''
        dapan = str(ans)
        loi_giai = fr'''Thể tích nước bơm được vào bể sau ${T}$ phút là: \\
$V = \displaystyle\int_{{0}}^{{{T}}} ({a}t + {b})\,\mathrm{{d}}t = \left.\left(\dfrac{{{a}t^2}}{{2}} + {b}t\right)\right|_{{0}}^{{{T}}} = \dfrac{{{a}({T}^2)}}{{2}} + {b}({T}) = {ans}\text{{ (lít)}}$.'''
        return caudan, dapan, loi_giai

    else:
        # Chuyển động tăng tốc của canô: a(t) = 0.6t + 1 => v(t) = 0.3 t^2 + t
        # Quãng đường sau 10s: s = \int_0^{10} (0.3 t^2 + t) dt = [0.1 t^3 + 0.5 t^2]_0^{10} = 100 + 50 = 150m
        ans = 150
        caudan = fr'''Một chiếc ca nô xuất phát từ trạng thái đứng yên tại bến ($v(0) = 0$) và tăng tốc với vận tốc tính theo thời gian là $v(t) = 0{{,}}3t^2 + t\text{{ (m/s)}}$ (với $t$ tính bằng giây). Tính quãng đường ca nô đi được trong $10$ giây đầu tiên (đơn vị mét).'''
        dapan = str(ans)
        loi_giai = fr'''Quãng đường ca nô đi được trong $10$ giây đầu tiên là: \\
$s = \displaystyle\int_{{0}}^{{10}} (0{{,}}3t^2 + t)\,\mathrm{{d}}t = \left.\left(0{{,}}1t^3 + 0{{,}}5t^2\right)\right|_{{0}}^{{10}} = 0{{,}}1(10^3) + 0{{,}}5(10^2) = 100 + 50 = {ans}\text{{ (m)}}$.'''
        return caudan, dapan, loi_giai

print("All 6 SA Chapter 4 functions defined OK")

# Aliases for Chapter 4 SA
CuoiChuong4_SA_NB1 = CuoiChuong4_SA_Cau1
CuoiChuong4_SA_NB2 = CuoiChuong4_SA_Cau2
CuoiChuong4_SA_TH = CuoiChuong4_SA_Cau3
CuoiChuong4_SA_VDT = CuoiChuong4_SA_Cau4
CuoiChuong4_SA_VDC = CuoiChuong4_SA_Cau5
CuoiChuong4_SA_TT = CuoiChuong4_SA_Cau6

def CuoiChuong5_SA_Cau1():
    # Bài tập cuối chương V: Trạm kiểm soát không lưu ra đa Oxyz
    triplets = [
        (3, 4, 12, 13),
        (2, 3, 6, 7),
        (1, 4, 8, 9),
        (6, 6, 7, 11),
        (2, 6, 9, 11),
        (6, 10, 15, 19),
        (4, 12, 3, 13),
        (8, 9, 12, 17)
    ]
    dx, dy, dz, d = random.choice(triplets)
    sx, sy, sz = random.choice([1, -1]), random.choice([1, -1]), random.choice([1, -1])
    dx *= sx; dy *= sy; dz *= sz
    
    xA = random.randint(-5, 5)
    yA = random.randint(-5, 5)
    zA = random.randint(0, 3)
    
    xM = xA + dx
    yM = yA + dy
    zM = zA + dz
    
    caudan = fr'''Trong không gian $Oxyz$ (với đơn vị trên mỗi trục toạ độ là $1\text{{ km}}$), một trạm kiểm soát không lưu đặt tại vị trí $A({xA}; {yA}; {zA})$. Một máy bay đang ở vị trí $M({xM}; {yM}; {zM})$. Tính khoảng cách từ máy bay đến trạm kiểm soát không lưu theo đơn vị kilômét.'''
    dapan = str(d)
    loi_giai = fr'''Khoảng cách từ trạm kiểm soát không lưu $A$ đến máy bay $M$ là: \\
$AM = \sqrt{{({xM} - {xA})^2 + ({yM} - {yA})^2 + ({zM} - {zA})^2}} = \sqrt{{({dx})^2 + ({dy})^2 + ({dz})^2}} = \sqrt{{{d**2}}} = {d}\text{{ (km)}}$.'''
    return caudan, dapan, loi_giai


def CuoiChuong6_SA_Cau1():
    # Bài tập cuối chương VI: Chẩn đoán bệnh - Xác suất toàn phần và Bayes
    p_b = random.choice([0.01, 0.02, 0.05])
    p_tb = random.choice([0.95, 0.96, 0.98])
    p_t_not_b = random.choice([0.02, 0.05])
    
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


# Import dynamic TF generators with randomized parameters and truth value toggling
from cuoi_chuong_tf import *

# Import Đề Ôn Tập Tổng Hợp (12 MC + 4 TF)
from de_tong_hop import *

# Aliases for chapter-based Bài tập cuối chương
CuoiChuong1_MC_Cau63 = CuoiChuong_DeTongHop_MC_Cau5
CuoiChuong1_MC_Cau64 = CuoiChuong_DeTongHop_MC_Cau7
CuoiChuong1_TF_Cau17 = CuoiChuong_DeTongHop_TF_Cau1

CuoiChuong2_MC_Cau20 = CuoiChuong_DeTongHop_MC_Cau9

CuoiChuong3_MC_Cau5 = CuoiChuong_DeTongHop_MC_Cau2
CuoiChuong3_MC_Cau6 = CuoiChuong_DeTongHop_MC_Cau8

CuoiChuong4_MC_Cau1 = CuoiChuong_DeTongHop_MC_Cau4
CuoiChuong4_MC_Cau2 = CuoiChuong_DeTongHop_MC_Cau6
CuoiChuong4_MC_Cau3 = CuoiChuong_DeTongHop_MC_Cau12
CuoiChuong4_TF_Cau1 = CuoiChuong_DeTongHop_TF_Cau2

CuoiChuong5_MC_Cau1 = CuoiChuong_DeTongHop_MC_Cau3
CuoiChuong5_TF_Cau1 = CuoiChuong_DeTongHop_TF_Cau3

CuoiChuong6_TF_Cau1 = CuoiChuong_DeTongHop_TF_Cau4

# De Tong Hop SA (6 questions) ngẫu nhiên hóa số đẹp
from de_tong_hop import (
    CuoiChuong_DeTongHop_SA_Cau1,
    CuoiChuong_DeTongHop_SA_Cau2,
    CuoiChuong_DeTongHop_SA_Cau3,
    CuoiChuong_DeTongHop_SA_Cau4,
    CuoiChuong_DeTongHop_SA_Cau5,
    CuoiChuong_DeTongHop_SA_Cau6,
)
CuoiChuong1_SA_Cau16 = CuoiChuong_DeTongHop_SA_Cau1
# CuoiChuong2_SA_Cau4 = CuoiChuong_DeTongHop_SA_Cau2 (kept as consolidated)
# CuoiChuong3_SA_Cau1 = CuoiChuong_DeTongHop_SA_Cau3 (kept as consolidated)
# CuoiChuong4_SA_Cau1 = CuoiChuong_DeTongHop_SA_Cau4 (kept as consolidated)
CuoiChuong5_SA_Cau1 = CuoiChuong_DeTongHop_SA_Cau5
CuoiChuong6_SA_Cau1 = CuoiChuong_DeTongHop_SA_Cau6

# Import Đề thi thử / Đề ôn tập số 2 (12 MC + 4 TF)
from de_thi_thu_02 import *

# Import Đề thi thử / Đề ôn tập số 3 (12 MC + 4 TF + 6 SA)
from de_thi_thu_03 import *

# Import Đề thi thử / Đề ôn tập số 4 (12 MC + 4 TF + 6 SA)
from de_thi_thu_04 import *

# Import Đề thi thử / Đề ôn tập số 5 (12 MC + 4 TF + 6 SA)
from de_thi_thu_05 import *

# Import Ngân hàng Bài tập cuối chương mở rộng
from cuoi_chuong_mc_ngan_hang import *

# Import 32 câu hỏi Đúng/Sai mới nhất từ 8 đề thi thử
from cuoi_chuong_tf_32 import *

# Import các câu hỏi Trắc nghiệm Chương 1 đã được ngẫu nhiên hóa toàn diện số liệu
from cuoi_chuong_mc_chuong1 import *



