# -*- coding: utf-8 -*-
import random
import math
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


def make_tf_choices(items_data):
    """
    items_data: danh sách 4 tuple (true_text, false_text, true_expl, false_expl)
    Sinh ngẫu nhiên tính Đúng/Sai cho từng ý.
    Đảm bảo không phải tất cả đều Đúng hoặc tất cả đều Sai.
    """
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
# CHƯƠNG I: ĐÚNG / SAI (2 CÂU BỔ SUNG)
# ==============================================================================

def CuoiChuong1_TF_Cau17():
    # BBT hàm số ngẫu nhiên hóa phong phú với số nguyên đẹp
    x_tc = random.choice([-5, -4, -3, -2, -1, 1, 2, 3, 4, 5])
    k = random.choice([2, 3, 4, 5, 6])
    x_ct = x_tc + k
    y_ct = random.choice([-8, -7, -6, -5, -4, -3, -2])
    lim_trai = random.choice([1, 2, 3, 4, 5, 6])
    nam = random.choice([2024, 2025, 2026, 2027, 2028, 2029, 2030])
    
    val_min = y_ct + nam * x_ct

    caudan = fr'''\immini{{Cho hàm số $y = f(x)$ có bảng biến thiên như sau:
Khi đó:}}{{
\begin{{tikzpicture}}
\tkzTabInit[nocadre,lgt=1.2,espcl=2]{{$x$ / 0.6, $y'$ / 0.6, $y$ /1.8}}{{$-\infty$, ${x_tc}$, ${x_ct}$, $+\infty$}}
\tkzTabLine{{ , +, d, -, 0, +, }}
\tkzTabVar{{-/ $-\infty$, +D+/ ${lim_trai}$ / $+\infty$, -/ ${y_ct}$, +/ $+\infty$}}
\end{{tikzpicture}}}}'''

    items = [
        (
            r'''Hàm số $y = f(x)$ có đúng một điểm cực trị.''',
            r'''Hàm số $y = f(x)$ có hai điểm cực trị.''',
            fr'''Dựa vào bảng biến thiên, đạo hàm đổi dấu từ âm sang dương khi qua $x = {x_ct}$ và $f(x)$ xác định tại đó, do đó hàm số có đúng $1$ điểm cực tiểu tại $x = {x_ct}$. Tại $x = {x_tc}$ hàm số không xác định nên không phải cực trị.''',
            fr'''Tại $x = {x_tc}$ hàm số không xác định nên không phải điểm cực trị, do đó hàm số chỉ có đúng $1$ điểm cực trị là $x = {x_ct}$.'''
        ),
        (
            fr'''Giá trị nhỏ nhất của $h(x) = f(x) + {nam}x$ trên đoạn $[{x_ct}; {nam}]$ bằng ${val_min}$.''',
            fr'''Giá trị nhỏ nhất của $h(x) = f(x) + {nam}x$ trên đoạn $[{x_ct}; {nam}]$ bằng ${val_min + 10}$.''',
            fr'''Trên $[{x_ct}; {nam}]$, $f(x)$ đồng biến và hàm số $g(x) = {nam}x$ đồng biến, do đó $h(x) = f(x) + {nam}x$ đồng biến trên $[{x_ct}; {nam}]$. Suy ra $\min\limits_{{[{x_ct}; {nam}]}} h(x) = h({x_ct}) = f({x_ct}) + {nam} \cdot {x_ct} = {y_ct} + {nam * x_ct} = {val_min}$.''',
            fr'''Ta có $h(x)$ đồng biến trên $[{x_ct}; {nam}]$ nên $\min h(x) = h({x_ct}) = {val_min} \ne {val_min + 10}$.'''
        ),
        (
            fr'''Hàm số $y = f(x)$ đồng biến trên khoảng $({x_ct}; +\infty)$.''',
            fr'''Hàm số $y = f(x)$ nghịch biến trên khoảng $({x_ct}; +\infty)$.''',
            fr'''Trên khoảng $({x_ct}; +\infty)$, $y' > 0$ nên hàm số đồng biến.''',
            fr'''Trên khoảng $({x_ct}; +\infty)$, đạo hàm $y' > 0$ nên hàm số đồng biến chứ không nghịch biến.'''
        ),
        (
            r'''Đồ thị hàm số $y = f(x)$ có đúng một đường tiệm cận đứng là $x = ''' + str(x_tc) + r'''$.''',
            r'''Đồ thị hàm số $y = f(x)$ có đúng hai đường tiệm cận.''',
            fr'''Ta có $\lim\limits_{{x \to {x_tc}^+}} f(x) = +\infty$ nên $x = {x_tc}$ là tiệm cận đứng duy nhất. Vì $\lim\limits_{{x \to \pm\infty}} f(x) = \pm\infty$ nên đồ thị không có tiệm cận ngang.''',
            fr'''Đồ thị hàm số chỉ có duy nhất một đường tiệm cận đứng $x = {x_tc}$, không có tiệm cận ngang vì $\lim\limits_{{x \to \pm\infty}} f(x) = \pm\infty$. Khẳng định có 2 đường tiệm cận là sai.'''
        )
    ]
    choices, loi_giai = make_tf_choices(items)
    return caudan, choices, loi_giai


def CuoiChuong1_TF_Cau18():
    # Hàm số f(x) = (x^2 + bx + c)/x với c là số chính phương => nghiệm cực trị nguyên đẹp!
    c_root = random.choice([1, 2, 3, 4, 5])
    c = c_root ** 2
    b = random.choice([-6, -5, -4, -3, -2, 2, 3, 4, 5, 6])
    
    b_str = f"+ {b}x" if b > 0 else f"- {abs(b)}x"
    b_tx = f"+ {b}" if b > 0 else f"- {abs(b)}"
    
    y_cd = -2 * c_root + b
    y_ct = 2 * c_root + b
    
    caudan = fr'''Cho hàm số $y = f(x) = \dfrac{{x^2 {b_str} + {c}}}{{x}}$.'''
    
    items = [
        (
            fr'''Họ nguyên hàm của hàm số $f(x)$ là $F(x) = \dfrac{{x^2}}{{2}} {b_tx}x + {c}\ln|x| + C$.''',
            fr'''Họ nguyên hàm của hàm số $f(x)$ là $F(x) = x^2 {b_tx}x + {c}\ln|x| + C$.''',
            fr'''Ta có $f(x) = x {b_tx} + \dfrac{{{c}}}{{x}} \implies \displaystyle\int f(x)\,\mathrm{{d}}x = \dfrac{{x^2}}{{2}} {b_tx}x + {c}\ln|x| + C$.''',
            fr'''Nguyên hàm của $x$ là $\dfrac{{x^2}}{{2}}$ chứ không phải $x^2$.'''
        ),
        (
            fr'''Đường thẳng đi qua hai điểm cực trị của đồ thị hàm số có phương trình $y = 2x {b_tx}$.''',
            fr'''Đường thẳng đi qua hai điểm cực trị của đồ thị hàm số có phương trình $y = x {b_tx}$.''',
            fr'''Ta có $y = \dfrac{{u(x)}}{{v(x)}} \implies$ đường thẳng qua hai cực trị là $y = \dfrac{{u'(x)}}{{v'(x)}} = \dfrac{{2x {b_tx}}}{{1}} = 2x {b_tx}$. Hai điểm cực trị có tọa độ nguyên là $({c_root}; {y_ct})$ và $({-c_root}; {y_cd})$.''',
            fr'''Đường thẳng $y = x {b_tx}$ là tiệm cận xiên, đường thẳng đi qua hai cực trị là $y = 2x {b_tx}$.'''
        ),
        (
            fr'''Đồ thị hàm số đã cho có tiệm cận xiên là đường thẳng $y = x {b_tx}$.''',
            fr'''Đồ thị hàm số đã cho có tiệm cận xiên là đường thẳng $y = x + {b + 1}$.''',
            fr'''Vì $f(x) = x {b_tx} + \dfrac{{{c}}}{{x}}$ và $\lim\limits_{{x \to \infty}} \dfrac{{{c}}}{{x}} = 0$ nên tiệm cận xiên là $y = x {b_tx}$.''',
            fr'''Phương trình tiệm cận xiên đúng là $y = x {b_tx}$.'''
        ),
        (
            fr'''Đạo hàm của hàm số là $y' = \dfrac{{x^2 - {c}}}{{x^2}}$.''',
            fr'''Đạo hàm của hàm số là $y' = \dfrac{{x^2 + {c}}}{{x^2}}$.''',
            fr'''$y' = \left(x {b_tx} + \dfrac{{{c}}}{{x}}\right)' = 1 - \dfrac{{{c}}}{{x^2}} = \dfrac{{x^2 - {c}}}{{x^2}}$.''',
            fr'''Đạo hàm đúng là $y' = \dfrac{{x^2 - {c}}}{{x^2}} \ne \dfrac{{x^2 + {c}}}{{x^2}}$.'''
        )
    ]
    choices, loi_giai = make_tf_choices(items)
    return caudan, choices, loi_giai


# ==============================================================================
# CHƯƠNG II: ĐÚNG / SAI (2 CÂU BỔ SUNG)
# ==============================================================================

def CuoiChuong2_TF_Cau5():
    # Điểm cực trị khoảng cách: thiết kế trọng tâm G NGUYÊN HOÀN TOÀN
    xG = random.randint(-2, 3)
    yG = random.randint(-2, 3)
    zG = random.choice([1, 2, 3, 4])
    
    # Offsets sao cho tổng bằng 0 => G là trọng tâm nguyên
    dx1, dy1, dz1 = random.choice([(-2, 1, 1), (1, -2, 1), (2, -1, -1), (1, 1, -2), (-1, 2, -1)])
    dx2, dy2, dz2 = random.choice([(1, -1, 0), (-1, 0, 1), (0, 1, -1), (2, 0, -2), (-2, 2, 0)])
    while (dx1, dy1, dz1) == (dx2, dy2, dz2):
        dx2, dy2, dz2 = (-dx1, dz1, dy1)
        
    dx3 = -(dx1 + dx2)
    dy3 = -(dy1 + dy2)
    dz3 = -(dz1 + dz2)
    
    xA, yA, zA = xG + dx1, yG + dy1, zG + dz1
    xB, yB, zB = xG + dx2, yG + dy2, zG + dz2
    xC, yC, zC = xG + dx3, yG + dy3, zG + dz3
    
    u1, u2, u3 = xB - xA, yB - yA, zB - zA
    v1, v2, v3 = xC - xA, yC - yA, zC - zA
    dot_prod = u1*v1 + u2*v2 + u3*v3
    len_AB2 = u1**2 + u2**2 + u3**2
    len_AC2 = v1**2 + v2**2 + v3**2
    len_AB_AC = len_AB2 * len_AC2

    caudan = fr'''Trong không gian $Oxyz$ cho ba điểm $A({xA}; {yA}; {zA})$, $B({xB}; {yB}; {zB})$, $C({xC}; {yC}; {zC})$. Khi đó:'''

    items = [
        (
            fr'''Điểm $M$ trên mặt phẳng $(Oxy)$ sao cho biểu thức $MA^2 + MB^2 + MC^2$ đạt giá trị nhỏ nhất có tọa độ là $M({xG}; {yG}; 0)$.''',
            fr'''Điểm $M$ trên mặt phẳng $(Oxy)$ sao cho biểu thức $MA^2 + MB^2 + MC^2$ đạt giá trị nhỏ nhất có tọa độ là $M({xG}; {yG}; {zG})$.''',
            fr'''Gọi $G$ là trọng tâm $\Delta ABC \implies G({xG}; {yG}; {zG})$. Ta có $MA^2+MB^2+MC^2 = 3MG^2 + GA^2+GB^2+GC^2$. Biểu thức nhỏ nhất khi $M$ là hình chiếu vuông góc của $G$ lên $(Oxy)$, do đó $M({xG}; {yG}; 0)$.''',
            fr'''Vì $M$ thuộc $(Oxy)$ nên cao độ của $M$ phải bằng $0$. Tọa độ đúng là $M({xG}; {yG}; 0)$.'''
        ),
        (
            fr'''Côsin của góc giữa hai vectơ $\overrightarrow{{AB}}, \overrightarrow{{AC}}$ bằng $\dfrac{{{dot_prod}}}{{\sqrt{{{len_AB_AC}}}}}$.''',
            fr'''Côsin của góc giữa hai vectơ $\overrightarrow{{AB}}, \overrightarrow{{AC}}$ bằng $-\dfrac{{{dot_prod}}}{{\sqrt{{{len_AB_AC}}}}}$.''',
            fr'''$\overrightarrow{{AB}} = ({u1}; {u2}; {u3}), \overrightarrow{{AC}} = ({v1}; {v2}; {v3})$. Khi đó $\cos(\overrightarrow{{AB}}, \overrightarrow{{AC}}) = \dfrac{{{dot_prod}}}{{\sqrt{{{len_AB2}}} \cdot \sqrt{{{len_AC2}}}}} = \dfrac{{{dot_prod}}}{{\sqrt{{{len_AB_AC}}}}}$.''',
            fr'''Công thức đúng là $\cos(\overrightarrow{{AB}}, \overrightarrow{{AC}}) = \dfrac{{{dot_prod}}}{{\sqrt{{{len_AB_AC}}}}}$.'''
        ),
        (
            (r'''Góc $\widehat{BAC}$ là góc tù.''' if dot_prod < 0 else r'''Góc $\widehat{BAC}$ là góc nhọn.'''),
            (r'''Góc $\widehat{BAC}$ là góc nhọn.''' if dot_prod < 0 else r'''Góc $\widehat{BAC}$ là góc tù.'''),
            fr'''Vì $\cos\widehat{{BAC}} = \dfrac{{{dot_prod}}}{{\sqrt{{{len_AB_AC}}}}}$ mang dấu {'âm' if dot_prod < 0 else 'dương'} nên $\widehat{{BAC}}$ là góc {'tù' if dot_prod < 0 else 'nhọn'}.''',
            fr'''Do tích vô hướng {'âm' if dot_prod < 0 else 'dương'} nên góc $\widehat{{BAC}}$ là góc {'tù' if dot_prod < 0 else 'nhọn'}.'''
        ),
        (
            fr'''Tích vô hướng của hai vectơ $\overrightarrow{{AB}}$ và $\overrightarrow{{AC}}$ bằng ${dot_prod}$.''',
            fr'''Tích vô hướng của hai vectơ $\overrightarrow{{AB}}$ và $\overrightarrow{{AC}}$ bằng ${-dot_prod if dot_prod != 0 else 5}$.''',
            fr'''$\overrightarrow{{AB}} \cdot \overrightarrow{{AC}} = ({u1})({v1}) + ({u2})({v2}) + ({u3})({v3}) = {dot_prod}$.''',
            fr'''Tích vô hướng đúng bằng ${dot_prod}$.'''
        )
    ]
    choices, loi_giai = make_tf_choices(items)
    return caudan, choices, loi_giai


def CuoiChuong2_TF_Cau6():
    # Hình hộp chữ nhật với đường chéo AC' NGUYÊN ĐẸP
    pythago_boxes = [
        {"a": 2, "b": 3, "c": 6, "diag": 7},
        {"a": 1, "b": 4, "c": 8, "diag": 9},
        {"a": 4, "b": 4, "c": 7, "diag": 9},
        {"a": 2, "b": 6, "c": 9, "diag": 11},
        {"a": 6, "b": 6, "c": 7, "diag": 11},
        {"a": 3, "b": 4, "c": 12, "diag": 13},
        {"a": 2, "b": 10, "c": 11, "diag": 15},
        {"a": 6, "b": 3, "c": 2, "diag": 7},
        {"a": 4, "b": 12, "c": 3, "diag": 13},
    ]
    box = random.choice(pythago_boxes)
    a, b, c, diag = box["a"], box["b"], box["c"], box["diag"]

    caudan = fr'''\immini{{Trong không gian $Oxyz$ cho hình hộp chữ nhật $ABCD.A'B'C'D'$ có $A$ trùng với gốc tọa độ và gắn hệ trục tọa độ với $AB = {a}$ (nằm trên tia $Ox$), $AD = {b}$ (nằm trên tia $Oy$), $AA' = {c}$ (nằm trên tia $Oz$).}}{{
\begin{{tikzpicture}}[font=\footnotesize, scale=0.8]
    \coordinate (A) at (0,0);
    \coordinate (D) at (2.5,0);
    \coordinate (B) at (-1,-1);
    \coordinate (C) at (1.5,-1);
    \coordinate (A') at (0,2);
    \coordinate (D') at (2.5,2);
    \coordinate (B') at (-1,1);
    \coordinate (C') at (1.5,1);
    
    \draw[->, dashed] (A) -- (-1.5,-1.5) node[left] {{$x$}};
    \draw[->, dashed] (A) -- (3,0) node[below] {{$y$}};
    \draw[->, dashed] (A) -- (0,2.5) node[right] {{$z$}};
    
    \draw[dashed] (A) -- (B) (A) -- (D) (A) -- (A');
    \draw (B) -- (C) -- (D);
    \draw (A') -- (B') -- (C') -- (D') -- cycle;
    \draw (B) -- (B') (C) -- (C') (D) -- (D');
    
    \node[below right] at (A) {{$A$}};
    \node[left] at (B) {{$B$}};
    \node[below right] at (C) {{$C$}};
    \node[below] at (D) {{$D$}};
    \node[above right] at (A') {{$A'$}};
    \node[left] at (B') {{$B'$}};
    \node[below right] at (C') {{$C'$}};
    \node[above] at (D') {{$D'$}};
\end{{tikzpicture}}}}'''

    items = [
        (
            fr'''Tọa độ đỉnh $C'$ là $C'({a}; {b}; {c})$.''',
            fr'''Tọa độ đỉnh $C'$ là $C'({b}; {a}; {c})$.''',
            fr'''Vì $A(0;0;0)$, $B({a};0;0)$, $D(0;{b};0)$, $A'(0;0;{c})$ nên $C'({a}; {b}; {c})$.''',
            fr'''Do $AB = {a}$ trên tia $Ox$ và $AD = {b}$ trên tia $Oy$ nên $C'({a}; {b}; {c})$.'''
        ),
        (
            fr'''Vectơ $\overrightarrow{{AC'}}$ có độ dài đúng bằng ${diag}$.''',
            fr'''Vectơ $\overrightarrow{{AC'}}$ có độ dài bằng ${a + b + c}$.''',
            fr'''$AC' = \sqrt{{{a}^2 + {b}^2 + {c}^2}} = \sqrt{{{a**2 + b**2 + c**2}}} = {diag}$.''',
            fr'''Độ dài đường chéo hình hộp chữ nhật là $\sqrt{{{a}^2+{b}^2+{c}^2}} = {diag} \ne {a+b+c}$.'''
        ),
        (
            fr'''Phương trình mặt phẳng $(A'B'C'D')$ là $z - {c} = 0$.''',
            fr'''Phương trình mặt phẳng $(A'B'C'D')$ là $x + y + z - {c} = 0$.''',
            fr'''Mặt phẳng $(A'B'C'D')$ song song với mặt phẳng $(Oxy)$ và đi qua $A'(0; 0; {c})$ nên có phương trình $z = {c} \iff z - {c} = 0$.''',
            fr'''Mặt phẳng đáy trên song song với $(Oxy)$ nên có phương trình dạng $z = \text{{const}}$, tức $z - {c} = 0$.'''
        ),
        (
            fr'''Mặt phẳng $(ABCD)$ trùng với mặt phẳng tọa độ $(Oxy)$ và có phương trình $z = 0$.''',
            r'''Mặt phẳng $(ABCD)$ có phương trình $x + y = 0$.''',
            r'''Đáy $ABCD$ nằm hoàn toàn trong mặt phẳng tọa độ $(Oxy)$ nên có phương trình là $z = 0$.''',
            r'''Mặt phẳng đáy $ABCD$ là mặt phẳng $(Oxy)$, có phương trình $z = 0$.'''
        )
    ]
    choices, loi_giai = make_tf_choices(items)
    return caudan, choices, loi_giai


# ==============================================================================
# CHƯƠNG III: THỐNG KÊ (8 CÂU)
# ==============================================================================

def CuoiChuong3_TF_Cau1():
    # Thời gian tập thể dục Bình và An ngẫu nhiên hóa
    t0 = random.choice([10, 15, 20, 25])
    w = 5
    t1, t2, t3, t4, t5 = t0, t0+w, t0+2*w, t0+3*w, t0+4*w
    t_end = t0 + 5*w
    R = t_end - t0

    caudan = fr'''Cho bảng số liệu dưới đây về thời gian (phút) tập thể dục buổi sáng của hai bạn Bình và An trong $30$ ngày:
\begin{{center}}
\begin{{tabular}}{{|l|c|c|c|c|c|}}
\hline
\textbf{{Thời gian}} & $[{t1};{t2})$ & $[{t2};{t3})$ & $[{t3};{t4})$ & $[{t4};{t5})$ & $[{t5};{t_end})$ \\
\hline
\textbf{{Bạn Bình}} & $5$ & $8$ & $10$ & $4$ & $3$ \\
\hline
\textbf{{Bạn An}} & $10$ & $10$ & $5$ & $3$ & $2$ \\
\hline
\end{{tabular}}
\end{{center}}'''

    q1_binh = t2 + (7.5 - 5) / 8 * w
    q1_an = t1 + (7.5 - 0) / 10 * w
    q3_an = t3 + (22.5 - 20) / 5 * w
    iqr_an = q3_an - q1_an

    items = [
        (
            fr'''Khoảng biến thiên của mẫu số liệu ghép nhóm về thời gian tập thể dục của An là ${R}$ (phút).''',
            fr'''Khoảng biến thiên của mẫu số liệu ghép nhóm về thời gian tập thể dục của An là ${R - 5}$ (phút).''',
            fr'''Khoảng biến thiên của mẫu ghép nhóm là $R = {t_end} - {t1} = {R}$ (phút).''',
            fr'''Khoảng biến thiên là $R = {t_end} - {t1} = {R}$ (phút) chứ không phải ${R - 5}$.'''
        ),
        (
            fr'''Tứ phân vị thứ nhất của mẫu số liệu ghép nhóm về thời gian tập thể dục buổi sáng của bạn Bình là $Q_1 \approx {q1_binh:.2f}$ (phút).''',
            fr'''Tứ phân vị thứ nhất của mẫu số liệu ghép nhóm về thời gian tập thể dục buổi sáng của bạn Bình là $Q_1 \approx {q1_binh + 1:.2f}$ (phút).''',
            fr'''Cỡ mẫu $n = 30$. $\dfrac{{n}}{{4}} = 7,5$. Nhóm chứa $Q_1$ là $[{t2}; {t3})$. $Q_1 = {t2} + \dfrac{{7,5 - 5}}{{8}} \cdot {w} = {q1_binh:.2f}$.''',
            fr'''Áp dụng công thức tính $Q_1$ ta được $Q_1 \approx {q1_binh:.2f}$.'''
        ),
        (
            fr'''Khoảng tứ phân vị của mẫu số liệu ghép nhóm về thời gian tập thể dục của bạn An bằng ${iqr_an:.2f}$ (phút).''',
            fr'''Khoảng tứ phân vị của mẫu số liệu ghép nhóm về thời gian tập thể dục của bạn An là ${iqr_an + 15:.2f}$ (phút).''',
            fr'''Với bạn An: $Q_1 = {q1_an:.2f}, Q_3 = {q3_an:.2f} \implies \Delta_Q = {q3_an:.2f} - {q1_an:.2f} = {iqr_an:.2f}$.''',
            fr'''Khoảng tứ phân vị $\Delta_Q = {iqr_an:.2f} \ne {iqr_an + 15:.2f}$.'''
        ),
        (
            r'''Phương sai của mẫu số liệu ghép nhóm về thời gian tập thể dục buổi sáng của bạn Bình xấp xỉ $38,5$.''',
            r'''Phương sai của mẫu số liệu ghép nhóm về thời gian tập thể dục buổi sáng của bạn Bình bằng $12,5$.''',
            r'''Tính toán theo công thức phương sai mẫu ghép nhóm với các giá trị đại diện cho kết quả $s^2 \approx 38,5$.''',
            r'''Phương sai tính được là $s^2 \approx 38,5 \ne 12,5$.'''
        )
    ]
    choices, loi_giai = make_tf_choices(items)
    return caudan, choices, loi_giai


def CuoiChuong3_TF_Cau2():
    # Bảng lương nhân viên ngẫu nhiên hóa
    L0 = random.choice([6, 8, 10, 12])
    step = 3
    intervals = [(L0 + i*step, L0 + (i+1)*step) for i in range(6)]
    R = intervals[-1][1] - intervals[0][0]

    caudan = fr'''Cho bảng số liệu ghép nhóm về lương (triệu đồng) và số nhân viên như sau:
\begin{{center}}
\begin{{tabular}}{{|c|c|c|c|c|c|c|}}
\hline
Lương (triệu đồng) & $[{intervals[0][0]}; {intervals[0][1]})$ & $[{intervals[1][0]}; {intervals[1][1]})$ & $[{intervals[2][0]}; {intervals[2][1]})$ & $[{intervals[3][0]}; {intervals[3][1]})$ & $[{intervals[4][0]}; {intervals[4][1]})$ & $[{intervals[5][0]}; {intervals[5][1]})$ \\
\hline
Số nhân viên & $13$ & $12$ & $14$ & $4$ & $1$ & $1$ \\
\hline
\end{{tabular}}
\end{{center}}'''

    q1 = intervals[0][0] + (11.25 / 13) * step
    q3 = intervals[2][0] + ((33.75 - 25) / 14) * step
    delta_q = q3 - q1
    outlier_thresh = q3 + 1.5 * delta_q

    items = [
        (
            fr'''Khoảng biến thiên của mẫu số liệu là ${R}$ (triệu đồng).''',
            fr'''Khoảng biến thiên của mẫu số liệu là ${R + 2}$ (triệu đồng).''',
            fr'''Khoảng biến thiên $R = {intervals[-1][1]} - {intervals[0][0]} = {R}$ (triệu đồng).''',
            fr'''Khoảng biến thiên $R = {R} \ne {R + 2}$.'''
        ),
        (
            fr'''Tứ phân vị thứ nhất xấp xỉ bằng ${q1:.2f}$ (triệu đồng).''',
            fr'''Tứ phân vị thứ nhất xấp xỉ bằng ${q1 + 1.6:.2f}$ (triệu đồng).''',
            fr'''$n = 45$, $\dfrac{{n}}{{4}} = 11,25$. Nhóm chứa $Q_1$ là $[{intervals[0][0]}; {intervals[0][1]})$. $Q_1 = {intervals[0][0]} + \dfrac{{11,25}}{{13}} \cdot {step} \approx {q1:.2f}$.''',
            fr'''$Q_1 \approx {q1:.2f} \ne {q1 + 1.6:.2f}$.'''
        ),
        (
            fr'''Tứ phân vị thứ ba xấp xỉ bằng ${q3:.2f}$ (triệu đồng).''',
            fr'''Tứ phân vị thứ ba xấp xỉ bằng ${q3 + 2.0:.2f}$ (triệu đồng).''',
            fr'''$\dfrac{{3n}}{{4}} = 33,75$. Nhóm chứa $Q_3$ là $[{intervals[2][0]}; {intervals[2][1]})$. $Q_3 = {intervals[2][0]} + \dfrac{{33,75 - 25}}{{14}} \cdot {step} \approx {q3:.2f}$.''',
            fr'''$Q_3 \approx {q3:.2f} \ne {q3 + 2.0:.2f}$.'''
        ),
        (
            fr'''Mức lương ${outlier_thresh + 0.7:.1f}$ triệu đồng là một giá trị ngoại lệ của mẫu số liệu.''',
            fr'''Mức lương ${outlier_thresh + 0.7:.1f}$ triệu đồng không phải là giá trị ngoại lệ của mẫu số liệu.''',
            fr'''$\Delta_Q \approx {delta_q:.2f}$. Ngưỡng trên $Q_3 + 1,5\Delta_Q \approx {outlier_thresh:.2f}$. Vì ${outlier_thresh + 0.7:.1f} > {outlier_thresh:.2f}$ nên nó là giá trị ngoại lệ.''',
            fr'''Khoảng không ngoại lệ là $[Q_1 - 1,5\Delta_Q; Q_3 + 1,5\Delta_Q]$. Do ${outlier_thresh + 0.7:.1f} > {outlier_thresh:.2f}$ nên nó là giá trị ngoại lệ.'''
        )
    ]
    choices, loi_giai = make_tf_choices(items)
    return caudan, choices, loi_giai


def CuoiChuong3_TF_Cau3():
    # CLB Toán Tin 100 hs
    d0 = random.choice([20, 30, 40, 50])
    w = 10
    d_end = d0 + 60
    caudan = fr'''Để tuyển chọn thành viên cho Câu lạc bộ Toán - Tin, nhà trường tổ chức bài thi đánh giá năng lực cho $100$ học sinh với kết quả điểm thi ghép nhóm như sau:
\begin{{center}}
\begin{{tabular}}{{|c|c|c|c|c|c|c|}}
\hline
Điểm số & $[{d0};{d0+10})$ & $[{d0+10};{d0+20})$ & $[{d0+20};{d0+30})$ & $[{d0+30};{d0+40})$ & $[{d0+40};{d0+50})$ & $[{d0+50};{d_end})$ \\
\hline
Số học sinh & $10$ & $15$ & $25$ & $30$ & $15$ & $5$ \\
\hline
\end{{tabular}}
\end{{center}}
An và Bình là hai học sinh đạt số điểm lần lượt là ${d0+42}$ điểm và ${d0+29,5}$ điểm. Quy định phân loại: Xuất sắc ($\ge Q_3$), Tiềm năng ($[M_e; Q_3)$), Chưa đạt ($< M_e$).'''

    me = d0 + 30
    q3 = d0 + 30 + (75 - 50)/30 * 10
    tb = d0 + 29.0

    items = [
        (
            r'''Khoảng biến thiên của mẫu số liệu ghép nhóm này là $60$.''',
            r'''Khoảng biến thiên của mẫu số liệu ghép nhóm này là $50$.''',
            fr'''Khoảng biến thiên $R = {d_end} - {d0} = 60$.''',
            r'''$R = 60 \ne 50$.'''
        ),
        (
            fr'''Điểm trung vị của $100$ học sinh tham gia kỳ thi là ${me}$ điểm.''',
            fr'''Điểm trung vị của $100$ học sinh tham gia kỳ thi là ${me + 1}$ điểm.''',
            fr'''$\dfrac{{n}}{{2}} = 50$. Điểm trung vị $M_e = {me}$ điểm.''',
            fr'''Điểm trung vị là ${me}$ điểm chứ không phải ${me + 1}$ điểm.'''
        ),
        (
            fr'''Mặc dù Bình xếp loại chưa đạt, nhưng điểm số của Bình (${d0+29,5}$) vẫn cao hơn mức điểm trung bình của toàn bộ học sinh (${tb}$).''',
            r'''Điểm số của Bình thấp hơn điểm số trung bình của toàn bộ học sinh.''',
            fr'''Điểm trung bình $\bar{{x}} = {tb}$. Điểm của Bình là ${d0+29,5} > {tb}$ nên cao hơn điểm trung bình.''',
            fr'''Điểm trung bình là ${tb}$, điểm của Bình là ${d0+29,5} > {tb}$.'''
        ),
        (
            fr'''Tứ phân vị thứ ba của mẫu số liệu bằng ${q3:.2f}$ điểm.''',
            fr'''Tứ phân vị thứ ba của mẫu số liệu bằng ${q3 + 7:.2f}$ điểm.''',
            fr'''$\dfrac{{3n}}{{4}} = 75$. Nhóm chứa $Q_3$ là $[{d0+30}; {d0+40})$. $Q_3 = {d0+30} + \dfrac{{75 - 50}}{{30}} \cdot 10 \approx {q3:.2f}$.''',
            fr'''$Q_3 \approx {q3:.2f} \ne {q3 + 7:.2f}$.'''
        )
    ]
    choices, loi_giai = make_tf_choices(items)
    return caudan, choices, loi_giai


def CuoiChuong3_TF_Cau4():
    # Cổ phiếu A và B 50 ngày
    p0 = random.choice([80, 90, 100, 110, 120])
    w = 2
    p_end = p0 + 10
    caudan = fr'''Bảng sau thống kê giá đóng cửa (nghìn đồng) của hai mã cổ phiếu A và B trong 50 ngày giao dịch liên tiếp:
\begin{{center}}
\begin{{tabular}}{{|c|c|c|c|c|c|}}
\hline
Giá đóng cửa & $[{p0}; {p0+2})$ & $[{p0+2}; {p0+4})$ & $[{p0+4}; {p0+6})$ & $[{p0+6}; {p0+8})$ & $[{p0+8}; {p_end})$ \\
\hline
Số ngày CP A & $8$ & $9$ & $12$ & $10$ & $11$ \\
\hline
Số ngày CP B & $16$ & $4$ & $3$ & $6$ & $21$ \\
\hline
\end{{tabular}}
\end{{center}}'''

    items = [
        (
            r'''Khoảng biến thiên về giá đóng cửa của cả hai cổ phiếu đều bằng $10$ (nghìn đồng).''',
            r'''Khoảng biến thiên về giá đóng cửa của cổ phiếu A lớn hơn cổ phiếu B.''',
            fr'''Cả hai đều có giá đóng cửa từ nhóm $[{p0}; {p0+2})$ đến $[{p0+8}; {p_end})$, do đó $R_A = R_B = {p_end} - {p0} = 10$.''',
            r'''Khoảng biến thiên của cả hai mã cổ phiếu đều là $10$.'''
        ),
        (
            r'''Phương sai của mẫu số liệu về giá đóng cửa của cổ phiếu B xấp xỉ $14,9$.''',
            r'''Phương sai của mẫu số liệu về giá đóng cửa của cổ phiếu B là khoảng $12,4$.''',
            r'''Tính toán cho cổ phiếu B cho phương sai $s_B^2 \approx 14,9$.''',
            r'''Phương sai thực tế của cổ phiếu B là $s_B^2 \approx 14,9 \ne 12,4$.'''
        ),
        (
            r'''Đầu tư vào cổ phiếu B có độ rủi ro cao hơn đầu tư vào cổ phiếu A vì độ lệch chuẩn lớn hơn.''',
            r'''Nếu dựa vào độ lệch chuẩn thì đầu tư vào cổ phiếu A có độ rủi ro cao hơn đầu tư vào cổ phiếu B.''',
            r'''Ta có $s_A \approx 2,85$ và $s_B \approx 3,86$. Vì $s_B > s_A$ nên cổ phiếu B có mức độ biến động và rủi ro cao hơn.''',
            r'''Độ lệch chuẩn của B lớn hơn của A ($s_B > s_A$) nên cổ phiếu B có mức độ rủi ro cao hơn.'''
        ),
        (
            fr'''Giá đóng cửa trung bình của cổ phiếu A xấp xỉ ${p0 + 5.3:.1f}$ nghìn đồng.''',
            r'''Giá đóng cửa trung bình của cổ phiếu A và cổ phiếu B trong 50 ngày là bằng nhau.''',
            fr'''$\bar{{x}}_A \approx {p0 + 5.32:.2f}$, $\bar{{x}}_B \approx {p0 + 5.48:.2f} \ne \bar{{x}}_A$.''',
            r'''Giá đóng cửa trung bình của hai cổ phiếu khác nhau.'''
        )
    ]
    choices, loi_giai = make_tf_choices(items)
    return caudan, choices, loi_giai


def CuoiChuong3_TF_Cau5():
    # Bảng lượng khách hàng tháng 8 ngẫu nhiên hóa độ dời
    base_shift = random.choice([0, 100, 200])
    raw_vals = [
        143, 273, 543, 343, 423,
        584, 296, 477, 403, 202,
        638, 339, 413, 530, 252,
        303, 243, 524, 614, 414,
        188, 389, 557, 434, 289
    ]
    vals = [v + base_shift for v in raw_vals]
    g1 = 140 + base_shift
    g2 = 240 + base_shift
    g3 = 340 + base_shift
    g4 = 440 + base_shift
    g5 = 540 + base_shift
    g6 = 640 + base_shift
    R_val = g6 - g1

    caudan = fr'''Bảng thống kê lượng khách hàng đến cửa hàng tiện lợi vào tháng 8 trong $25$ năm:
\begin{{center}}
\begin{{tabular}}{{|c|c|c|c|c|}}
\hline	${vals[0]}$ & ${vals[1]}$ & ${vals[2]}$ & ${vals[3]}$ & ${vals[4]}$ \\
\hline	${vals[5]}$ & ${vals[6]}$ & ${vals[7]}$ & ${vals[8]}$ & ${vals[9]}$ \\
\hline	${vals[10]}$ & ${vals[11]}$ & ${vals[12]}$ & ${vals[13]}$ & ${vals[14]}$ \\
\hline	${vals[15]}$ & ${vals[16]}$ & ${vals[17]}$ & ${vals[18]}$ & ${vals[19]}$ \\
\hline	${vals[20]}$ & ${vals[21]}$ & ${vals[22]}$ & ${vals[23]}$ & ${vals[24]}$\\
\hline
\end{{tabular}}
\end{{center}}'''

    items = [
        (
            fr'''Nếu chia thành các nhóm với nhóm đầu tiên là $[{g1}; {g2})$ và độ dài mỗi nhóm là $100$ thì có tất cả $5$ nhóm: $[{g1}; {g2})$, $[{g2}; {g3})$, $[{g3}; {g4})$, $[{g4}; {g5})$, $[{g5}; {g6})$.''',
            fr'''Nếu nhóm đầu tiên là $[{g1}; {g2})$ với độ dài mỗi nhóm là $100$ thì mẫu số liệu trên được chia thành $4$ nhóm.''',
            fr'''Giá trị nhỏ nhất là ${min(vals)}$ và lớn nhất là ${max(vals)}$, nên cần $5$ nhóm từ $[{g1}; {g2})$ đến $[{g5}; {g6})$. Khẳng định $4$ nhóm là sai.''',
            fr'''Vì giá trị lớn nhất là ${max(vals)}$ nên nhóm cuối cùng phải là $[{g5}; {g6})$, tổng cộng có $5$ nhóm chứ không phải $4$ nhóm.'''
        ),
        (
            fr'''Khoảng biến thiên của mẫu số liệu ghép nhóm là ${R_val}$ (người).''',
            fr'''Khoảng biến thiên của mẫu số liệu ghép nhóm trên là ${R_val - 50}$ mm.''',
            fr'''Khoảng biến thiên của mẫu ghép nhóm là $R = {g6} - {g1} = {R_val}$ (người). Đơn vị là người chứ không phải mm.''',
            fr'''Khoảng biến thiên $R = {g6} - {g1} = {R_val}$ (người).'''
        ),
        (
            fr'''Tần số của nhóm $[{g2}; {g3})$ trong mẫu ghép nhóm bằng $7$.''',
            fr'''Tần số của nhóm $[{g2}; {g3})$ trong mẫu ghép nhóm bằng $4$.''',
            fr'''Có đúng $7$ giá trị thuộc nhóm $[{g2}; {g3})$.''',
            fr'''Đếm trực tiếp ta có $7$ giá trị thuộc $[{g2}; {g3})$.'''
        ),
        (
            r'''Độ lệch chuẩn của mẫu số liệu ghép nhóm trên khoảng $135$ (người).''',
            r'''Độ lệch chuẩn của mẫu số liệu ghép nhóm trên khoảng $130$.''',
            r'''Tính toán các giá trị đại diện với các tần số tương ứng cho độ lệch chuẩn $s \approx 135$.''',
            r'''Độ lệch chuẩn thực tế xấp xỉ $135 \ne 130$.'''
        )
    ]
    choices, loi_giai = make_tf_choices(items)
    return caudan, choices, loi_giai


def CuoiChuong3_TF_Cau6():
    # Thời gian thi thử ngẫu nhiên hóa thời gian bắt đầu và phân phối tần số
    t0 = random.choice([55, 60, 65, 70])
    data_presets = [
        {"freqs": [5, 13, 18, 35, 31], "n": 102, "q1": 77.08, "q3": 85.89, "dq": 8.8, "mo": 84.0, "var": 34.2, "t_base": 65},
        {"freqs": [6, 14, 20, 32, 28], "n": 100, "q1": 76.25, "q3": 85.31, "dq": 9.1, "mo": 83.8, "var": 35.1, "t_base": 65},
        {"freqs": [4, 12, 16, 36, 32], "n": 100, "q1": 77.50, "q3": 86.11, "dq": 8.6, "mo": 84.2, "var": 33.8, "t_base": 65},
    ]
    preset = random.choice(data_presets)
    shift = t0 - preset["t_base"]
    f = preset["freqs"]
    n_tot = preset["n"]
    dq_val = preset["dq"]
    mo_val = round(preset["mo"] + shift, 1)
    var_val = preset["var"]
    
    headers = [f"[{t0 + i*5}; {t0 + (i+1)*5})" for i in range(5)]
    R_val = 25

    caudan = fr'''Thời gian (phút) hoàn thành bài thi thử của ${n_tot}$ học sinh lớp 12 được ghi lại ở bảng sau:
\begin{{center}}
\begin{{tabular}}{{|c|c|c|c|c|c|}}
\hline
Thời gian (phút) & {headers[0]} & {headers[1]} & {headers[2]} & {headers[3]} & {headers[4]} \\
\hline
Số học sinh & ${f[0]}$ & ${f[1]}$ & ${f[2]}$ & ${f[3]}$ & ${f[4]}$ \\
\hline
\end{{tabular}}
\end{{center}}'''

    mo_str = str(mo_val).replace('.', ',')
    dq_str = str(dq_val).replace('.', ',')
    var_str = str(var_val).replace('.', ',')

    items = [
        (
            fr'''Khoảng biến thiên của mẫu số liệu trên bằng ${R_val}$ (phút).''',
            fr'''Khoảng biến thiên của mẫu số liệu trên bằng ${R_val - 5}$.''',
            fr'''Khoảng biến thiên của mẫu ghép nhóm là $R = {t0 + 25} - {t0} = ${R_val}$ (phút).''',
            fr'''$R = {t0 + 25} - {t0} = ${R_val}$ \ne ${R_val - 5}$.'''
        ),
        (
            fr'''Khoảng tứ phân vị của mẫu số liệu ghép nhóm trên xấp xỉ ${dq_str}$ (phút).''',
            fr'''Khoảng tứ phân vị của mẫu số liệu ghép nhóm trên xấp xỉ ${round(dq_val + 3.7, 1)}$.''',
            fr'''Tính toán $Q_1, Q_3$ ta được khoảng tứ phân vị $\Delta_Q = Q_3 - Q_1 \approx ${dq_str}$.''',
            fr'''$\Delta_Q \approx ${dq_str}$ \ne ${round(dq_val + 3.7, 1)}$.'''
        ),
        (
            fr'''Mốt của mẫu số liệu ghép nhóm xấp xỉ ${mo_str}$ phút.''',
            fr'''Mốt của mẫu số liệu ghép nhóm xấp xỉ ${t0 + 13}$ phút.''',
            fr'''Nhóm chứa mốt là $[{t0+15}; {t0+20})$ với tần số lớn nhất là ${f[3]}$. Mốt tính được là $M_o \approx ${mo_str}$ phút.''',
            fr'''Nhóm chứa mốt có tần số lớn nhất là ${f[3]}$, mốt xấp xỉ ${mo_str}$ phút.'''
        ),
        (
            fr'''Phương sai của mẫu số liệu trên xấp xỉ ${var_str}$.''',
            fr'''Phương sai của mẫu số liệu trên xấp xỉ ${round(var_val + 10.8, 1)}$.''',
            fr'''Tính toán phương sai ghép nhóm cho kết quả $s^2 \approx ${var_str}$.''',
            fr'''Phương sai tính được là $s^2 \approx ${var_str}$ \ne ${round(var_val + 10.8, 1)}$.'''
        )
    ]
    choices, loi_giai = make_tf_choices(items)
    return caudan, choices, loi_giai


def CuoiChuong3_TF_Cau7():
    # Thống kê độ cận thị ngẫu nhiên hóa
    presets = [
        {"d0": 0.25, "freqs": [25, 32, 14, 12, 4], "n": 87, "s": 0.57, "s2": 0.33, "dq": 0.82},
        {"d0": 0.50, "freqs": [20, 30, 20, 15, 5], "n": 90, "s": 0.59, "s2": 0.35, "dq": 0.85},
        {"d0": 0.25, "freqs": [24, 28, 18, 10, 6], "n": 86, "s": 0.58, "s2": 0.34, "dq": 0.84},
    ]
    p = random.choice(presets)
    d0 = p["d0"]
    f = p["freqs"]
    n_tot = p["n"]
    s_val = p["s"]
    s2_val = p["s2"]
    dq_val = p["dq"]

    def fmt_d(val):
        return f"{val:.2f}".replace('.', ',')

    headers = [f"[{fmt_d(d0 + i*0.5)}; {fmt_d(d0 + (i+1)*0.5)})" for i in range(5)]

    caudan = fr'''Thống kê độ cận thị của ${n_tot}$ học sinh bị cận ở một trường THPT:
\begin{{center}}
\begin{{tabular}}{{|c|c|c|c|c|c|}}
\hline
Độ cận (diop) & {headers[0]} & {headers[1]} & {headers[2]} & {headers[3]} & {headers[4]} \\
\hline
Số học sinh & ${f[0]}$ & ${f[1]}$ & ${f[2]}$ & ${f[3]}$ & ${f[4]}$ \\
\hline
\end{{tabular}}
\end{{center}}'''

    items = [
        (
            r'''Khoảng biến thiên của mẫu số liệu ghép nhóm trên là $2,5$ (diop).''',
            r'''Khoảng biến thiên của mẫu số liệu ghép nhóm trên là $2,0$ (diop).''',
            r'''Khoảng biến thiên $R = 2,5$ diop.''',
            r'''$R = 2,5 \ne 2,0$.'''
        ),
        (
            fr'''Độ lệch chuẩn của mẫu số liệu trên lớn hơn $0,5$.''',
            fr'''Độ lệch chuẩn của mẫu số liệu trên bé hơn $0,5$.''',
            fr'''Tính toán ta có phương sai $s^2 \approx {s2_val} \implies s \approx {s_val} > 0,5$.''',
            fr'''Độ lệch chuẩn $s \approx {s_val} > 0,5$, khẳng định bé hơn $0,5$ là sai.'''
        ),
        (
            fr'''Phương sai của mẫu số liệu trên bé hơn $0,4$.''',
            fr'''Phương sai của mẫu số liệu trên lớn hơn $0,4$.''',
            fr'''Giá trị phương sai $s^2 \approx {s2_val} < 0,4$.''',
            fr'''Phương sai $s^2 \approx {s2_val} < 0,4$, khẳng định lớn hơn $0,4$ là sai.'''
        ),
        (
            fr'''Khoảng tứ phân vị của mẫu số liệu ghép nhóm trên bé hơn $1$.''',
            fr'''Khoảng tứ phân vị của mẫu số liệu ghép nhóm trên lớn hơn $1$.''',
            fr'''$\Delta_Q = Q_3 - Q_1 \approx {dq_val} < 1$.''',
            fr'''Khoảng tứ phân vị $\Delta_Q \approx {dq_val} < 1$, khẳng định lớn hơn $1$ là sai.'''
        )
    ]
    choices, loi_giai = make_tf_choices(items)
    return caudan, choices, loi_giai


def CuoiChuong3_TF_Cau8():
    # Điểm thi cuối HK2 ngẫu nhiên hóa
    presets = [
        {"freqs": [2, 5, 10, 12, 11], "n": 40, "me_grp": "[6; 8)", "q3": 8.18, "var": 5.04},
        {"freqs": [3, 6, 9, 13, 9],   "n": 40, "me_grp": "[6; 8)", "q3": 8.00, "var": 4.95},
        {"freqs": [2, 4, 12, 14, 8],  "n": 40, "me_grp": "[6; 8)", "q3": 7.71, "var": 4.82},
    ]
    p = random.choice(presets)
    f = p["freqs"]
    n_tot = p["n"]
    me_grp = p["me_grp"]
    q3_val = p["q3"]
    var_val = p["var"]
    var_str = str(round(var_val, 1)).replace('.', ',')
    q3_str = str(q3_val).replace('.', ',')

    caudan = fr'''Điểm thi của một lớp học gồm ${n_tot}$ học sinh cuối học kỳ 2 được thống kê bởi bảng sau:
\begin{{center}}
\begin{{tabular}}{{|c|c|c|c|c|c|}}
\hline
Điểm số & $[0; 2)$ & $[2; 4)$ & $[4; 6)$ & $[6; 8)$ & $[8; 10)$ \\
\hline
Số học sinh & ${f[0]}$ & ${f[1]}$ & ${f[2]}$ & ${f[3]}$ & ${f[4]}$ \\
\hline
\end{{tabular}}
\end{{center}}'''

    items = [
        (
            r'''Khoảng biến thiên của mẫu số liệu bằng $10$.''',
            r'''Khoảng biến thiên của mẫu số liệu bằng $8$.''',
            r'''Khoảng biến thiên $R = 10 - 0 = 10$.''',
            r'''$R = 10 - 0 = 10 \ne 8$.'''
        ),
        (
            fr'''Nhóm chứa trung vị là nhóm ${me_grp}$.''',
            r'''Nhóm chứa trung vị là nhóm $[4; 6)$.''',
            fr'''$n = {n_tot}$. $\dfrac{{n}}{{2}} = {n_tot // 2}$. Vị trí trung vị rơi vào nhóm ${me_grp}$.''',
            fr'''Vị trí trung vị rơi vào nhóm ${me_grp}$ chứ không phải $[4; 6)$.'''
        ),
        (
            fr'''Tứ phân vị thứ ba của mẫu số liệu ghép nhóm xấp xỉ ${q3_str}$.''',
            r'''Tứ phân vị thứ ba là $5$.''',
            fr'''Nhóm chứa $Q_3$ cho kết quả $Q_3 \approx ${q3_str}$.''',
            fr'''$Q_3 \approx ${q3_str}$ \ne 5$.'''
        ),
        (
            fr'''Phương sai của mẫu số liệu trên xấp xỉ ${var_str}$.''',
            r'''Phương sai bằng $3,2$.''',
            fr'''Tính toán cho kết quả phương sai $s^2 \approx ${var_str}$ \ne 3,2$.''',
            fr'''Phương sai thực tế là $s^2 \approx ${var_str}$ \ne 3,2$.'''
        )
    ]
    choices, loi_giai = make_tf_choices(items)
    return caudan, choices, loi_giai



# ==============================================================================
# CHƯƠNG IV: NGUYÊN HÀM - TÍCH PHÂN (6 CÂU)
# ==============================================================================

def CuoiChuong4_TF_Cau1():
    # f(x) = a x^2 + b x + c với a chia hết cho 3, b chẵn => Nguyên hàm nguyên đẹp!
    a = random.choice([-6, -3, 3, 6, 9])
    b = random.choice([-6, -4, -2, 2, 4, 6])
    c = random.choice([-8, -6, -4, -2, 2, 4, 6, 8])
    
    a_coef = a // 3
    b_coef = b // 2
    
    def fmt_quad(A, B, C):
        parts = []
        parts.append(f"{A}x^2" if A != 1 else "x^2")
        if B > 0: parts.append(f"+ {B}x")
        else: parts.append(f"- {abs(B)}x")
        if C > 0: parts.append(f"+ {C}")
        else: parts.append(f"- {abs(C)}")
        return " ".join(parts)
        
    poly_f = fmt_quad(a, b, c)
    caudan = fr'''Cho $F(x)$ là một nguyên hàm của hàm số $f(x) = {poly_f}$. Xét tính đúng-sai của các khẳng định sau:'''

    # F(x) = (a/3)x^3 + (b/2)x^2 + cx (tất cả hệ số là số nguyên)
    def F_val(x):
        return a_coef * x**3 + b_coef * x**2 + c * x
        
    x_low = random.choice([-4, -3, -2])
    x_high = random.choice([1, 2, 3])
    int_val = F_val(x_high) - F_val(x_low)
    
    # \int_1^3 f'(x)dx = f(3) - f(1)
    def f_val(x):
        return a * x**2 + b * x + c
    f_diff = f_val(3) - f_val(1)

    items = [
        (
            fr'''$F'(x) = {poly_f}$.''',
            fr'''$F'(x) = {2*a}x + {b}$.''',
            fr'''Theo định nghĩa nguyên hàm, $F'(x) = f(x) = {poly_f}$.''',
            fr'''$F'(x) = f(x) = {poly_f}$, khẳng định $F'(x) = {2*a}x + {b}$ là đạo hàm của $f(x)$ chứ không phải của $F(x)$.'''
        ),
        (
            fr'''$\displaystyle\int\limits_{{1}}^{{3}} ({poly_f})\,\mathrm{{d}}x = F(3) - F(1)$.''',
            fr'''$\displaystyle\int\limits_{{1}}^{{3}} ({poly_f})\,\mathrm{{d}}x = F(3) + F(1)$.''',
            r'''Theo định lý cơ bản của giải tích Newton-Leibniz, $\displaystyle\int\limits_{a}^{b} f(x)\,\mathrm{d}x = F(b) - F(a) = F(3) - F(1)$.''',
            r'''Công thức đúng là hiệu $F(3) - F(1)$, không phải tổng $F(3) + F(1)$.'''
        ),
        (
            fr'''$\displaystyle\int\limits_{{1}}^{{3}} f'(x)\,\mathrm{{d}}x = {f_diff}$.''',
            fr'''$\displaystyle\int\limits_{{1}}^{{3}} f'(x)\,\mathrm{{d}}x = {-f_diff}$.''',
            fr'''$\displaystyle\int\limits_{{1}}^{{3}} f'(x)\,\mathrm{{d}}x = f(3) - f(1) = {f_diff}$.''',
            fr'''$f(3) - f(1) = {f_diff} \ne {-f_diff}$.'''
        ),
        (
            fr'''$\displaystyle\int\limits_{{{x_low}}}^{{{x_high}}} f(x)\,\mathrm{{d}}x = {int_val}$.''',
            fr'''$\displaystyle\int\limits_{{{x_low}}}^{{{x_high}}} f(x)\,\mathrm{{d}}x = {-int_val}$.''',
            fr'''$\displaystyle\int\limits_{{{x_low}}}^{{{x_high}}} ({poly_f})\,\mathrm{{d}}x = F({x_high}) - F({x_low}) = {int_val}$.''',
            fr'''Giá trị tích phân đúng là ${int_val} \ne {-int_val}$.'''
        )
    ]
    choices, loi_giai = make_tf_choices(items)
    return caudan, choices, loi_giai


def CuoiChuong4_TF_Cau2():
    # f(x) = a x^2 + b x + c với a chia hết cho 3, b chẵn => Hằng số C nguyên đẹp!
    a = random.choice([-6, -3, 3, 6])
    b = random.choice([-6, -4, -2, 2, 4, 6])
    c = random.choice([-5, -3, -1, 1, 3, 5])
    
    a_coef = a // 3
    b_coef = b // 2
    
    caudan = fr'''Cho hàm số $f(x) = {a}x^2 + {b}x + {c}$. Xét tính đúng-sai của các khẳng định sau:'''
    
    # F(1) = y0
    y0 = random.choice([5, 6, 7, 8, 10])
    # F(1) = a_coef + b_coef + c + C => C nguyên hoàn toàn
    C_const = y0 - (a_coef + b_coef + c)

    items = [
        (
            fr'''$\displaystyle\int f(x)\,\mathrm{{d}}x = {a_coef}x^3 + {b_coef}x^2 + {c}x + C$.''',
            fr'''$\displaystyle\int f(x)\,\mathrm{{d}}x = {a}x^3 + {b_coef}x^2 + {c}x + C$.''',
            fr'''$\displaystyle\int ({a}x^2+{b}x+{c})\,\mathrm{{d}}x = {a_coef}x^3 + {b_coef}x^2 + {c}x + C$.''',
            fr'''Hệ số của $x^3$ phải là ${a_coef}$, không phải ${a}$.'''
        ),
        (
            fr'''Nếu $F(x)$ là một nguyên hàm của $f(x)$ thỏa mãn $F(1) = {y0}$ thì hằng số $C = {C_const}$.''',
            fr'''Nếu $F(x)$ là một nguyên hàm của $f(x)$ thỏa mãn $F(1) = {y0}$ thì hằng số $C = {y0}$.''',
            fr'''$F(1) = {a_coef} + {b_coef} + {c} + C = {y0} \implies C = {y0} - ({a_coef + b_coef + c}) = {C_const}$.''',
            fr'''Khi $F(1) = {y0}$ thì hằng số $C = {C_const} \ne {y0}$.'''
        ),
        (
            fr'''Hàm số $g(x) = {a_coef}x^3 + {b}x^2 + {c}x$ không phải là một nguyên hàm của $f(x)$.''',
            fr'''$g(x) = {a_coef}x^3 + {b}x^2 + {c}x$ là một nguyên hàm của $f(x)$.''',
            fr'''Ta có $g'(x) = {a}x^2 + {2*b}x + {c} \ne f(x)$ nên $g(x)$ không là nguyên hàm của $f(x)$.''',
            r'''$g'(x) \ne f(x)$, khẳng định $g(x)$ là nguyên hàm là sai.'''
        ),
        (
            r'''Thể tích khối tròn xoay tạo thành khi quay hình phẳng giới hạn bởi đồ thị $y = f(x)$, trục hoành và hai đường thẳng $x = 0, x = 1$ quanh trục $Ox$ được tính theo công thức $V = \pi \displaystyle\int\limits_{0}^{1} [f(x)]^2\,\mathrm{d}x$.''',
            r'''Thể tích khối tròn xoay tạo thành khi quay quanh trục $Ox$ được tính theo công thức $V = \displaystyle\int\limits_{0}^{1} f(x)\,\mathrm{d}x$.''',
            r'''Công thức tính thể tích khối tròn xoay quanh trục $Ox$ là $V = \pi \displaystyle\int\limits_{a}^{b} [f(x)]^2\,\mathrm{d}x$.''',
            r'''Công thức đúng phải có bình phương và nhân với hệ số $\pi$.'''
        )
    ]
    choices, loi_giai = make_tf_choices(items)
    return caudan, choices, loi_giai


def CuoiChuong4_TF_Cau3():
    # f(x) = x^3 - 3*k^2*x + d với k nguyên => diện tích nguyên đẹp!
    k = random.choice([1, 2, 3, 4])
    d = random.choice([-8, -6, -4, -2, 2, 4, 6, 8])
    b = 3 * k**2
    caudan = fr'''Cho hàm số $f(x) = x^3 - {b}x {f"+ {d}" if d > 0 else f"- {abs(d)}"}$. Khi đó:'''

    area = 4 * k**3

    items = [
        (
            fr'''Hàm số đã cho có đạo hàm là $f'(x) = 3x^2 - {b}$.''',
            fr'''Hàm số đã cho có đạo hàm là $f'(x) = 3x^2 - {b}x$.''',
            fr'''Ta có $f'(x) = (x^3)' - ({b}x)' + ({d})' = 3x^2 - {b}$.''',
            fr'''$({b}x)' = {b}$, do đó đạo hàm đúng là $3x^2 - {b}$.'''
        ),
        (
            fr'''Diện tích hình phẳng giới hạn bởi đồ thị hàm số $y = f'(x)$ và trục hoành bằng ${area}$ (đvdt).''',
            fr'''Diện tích hình phẳng giới hạn bởi đồ thị hàm số $y = f'(x)$ và trục hoành bằng ${area // 2}$ (đvdt).''',
            fr'''Phương trình hoành độ giao điểm: $3x^2 - {b} = 0 \iff x = \pm {k}$. $S = \displaystyle\int\limits_{{-{k}}}^{{{k}}} |3x^2 - {b}|\,\mathrm{{d}}x = {area}$.''',
            fr'''$S = {area} \ne {area // 2}$.'''
        ),
        (
            fr'''Giá trị $f({k}) = {-2*k**3 + d}$.''',
            fr'''Giá trị $f({k}) = {2*k**3 + d}$.''',
            fr'''$f({k}) = {k}^3 - {b}({k}) + ({d}) = {-2*k**3 + d}$.''',
            fr'''$f({k}) = {-2*k**3 + d} \ne {2*k**3 + d}$.'''
        ),
        (
            fr'''Phương trình $f'(x) = 0$ có hai nghiệm phân biệt là $x = {k}$ và $x = {-k}$.''',
            fr'''Phương trình $f'(x) = 0$ có nghiệm kép.''',
            fr'''$3x^2 - {b} = 0 \iff x^2 = {k**2} \iff x = \pm {k}$.''',
            fr'''Phương trình có hai nghiệm phân biệt $x = \pm {k}$.'''
        )
    ]
    choices, loi_giai = make_tf_choices(items)
    return caudan, choices, loi_giai


def CuoiChuong4_TF_Cau4():
    # f(x) = -x^3 + 3*k*x^2 + d với k chẵn => diện tích nguyên đẹp!
    k = random.choice([2, 4])
    d = random.choice([2, 4, 6, 8])
    b = 3 * k
    caudan = fr'''Cho hàm số $f(x) = -x^3 + {b}x^2 + {d}$ có đồ thị $(C)$.'''

    # Area between (C) and y = d: S = 27 * k^4 / 4 (luôn là số nguyên khi k chẵn)
    s_val = 27 * (k**4) // 4
    x_max = 2 * k
    y_max = 4 * k**3 + d

    items = [
        (
            fr'''Một nguyên hàm của hàm số này là $F(x) = -\dfrac{{x^4}}{{4}} + {k}x^3 + {d}x$.''',
            fr'''Một nguyên hàm của hàm số này là $F(x) = -x^4 + {k}x^3 + {d}x$.''',
            fr'''$\displaystyle\int (-x^3 + {b}x^2 + {d})\,\mathrm{{d}}x = -\dfrac{{x^4}}{{4}} + {k}x^3 + {d}x + C$. Chọn $C = 0$.''',
            r'''Nguyên hàm đúng có hệ số bậc 4 là $-\dfrac{1}{4}$.'''
        ),
        (
            fr'''Diện tích hình phẳng giới hạn bởi đồ thị $(C)$, trục tung và đường thẳng $y = {d}$ bằng ${s_val}$ (đvdt).''',
            fr'''Diện tích hình phẳng giới hạn bởi đồ thị $(C)$, trục tung và đường thẳng $y = {d}$ là ${s_val + 50}$ (đvdt).''',
            fr'''Phương trình hoành độ giao điểm: $-x^3 + {b}x^2 + {d} = {d} \iff x^2({b} - x) = 0 \iff x = 0$ hoặc $x = {b}$. $S = \displaystyle\int\limits_{{0}}^{{{b}}} (-x^3 + {b}x^2)\,\mathrm{{d}}x = \left.\left(-\dfrac{{x^4}}{{4}} + {k}x^3\right)\right|_0^{{{b}}} = {s_val}$.''',
            fr'''$S = {s_val} \ne {s_val + 50}$.'''
        ),
        (
            fr'''Hàm số $f(x)$ đạt cực đại tại điểm $x = {x_max}$.''',
            fr'''Hàm số $f(x)$ đạt cực đại tại điểm $x = 0$.''',
            fr'''$f'(x) = -3x^2 + {2*b}x = 0 \iff x = 0$ hoặc $x = {x_max}$. Vì $a = -1 < 0$ nên đạt cực đại tại $x = {x_max}$.''',
            fr'''Điểm cực đại là $x = {x_max}$, tại $x = 0$ là điểm cực tiểu.'''
        ),
        (
            fr'''Giá trị cực đại của hàm số bằng ${y_max}$.''',
            fr'''Giá trị cực đại của hàm số bằng ${d}$.''',
            fr'''$y_{{CĐ}} = f({x_max}) = -({x_max})^3 + {b}({x_max})^2 + {d} = {y_max}$.''',
            fr'''$y_{{CĐ}} = {y_max} \ne {d}$.'''
        )
    ]
    choices, loi_giai = make_tf_choices(items)
    return caudan, choices, loi_giai


def CuoiChuong4_TF_Cau5():
    # f(x) = x^3 - 3*k*x^2 + 2*k^3 với k chẵn => diện tích nguyên đẹp!
    k = random.choice([2, 4])
    b = 3 * k
    c = 2 * k**3
    caudan = fr'''Cho hàm số $f(x) = x^3 - {b}x^2 + {c}$ có đồ thị $(C)$.'''

    # Area S = 5 * k^4 / 2 (luôn nguyên khi k chẵn)
    s_val = 5 * (k**4) // 2

    items = [
        (
            fr'''Một nguyên hàm của hàm số này là $F(x) = \dfrac{{x^4}}{{4}} - {k}x^3 + {c}x$.''',
            fr'''Một nguyên hàm của hàm số này là $F(x) = x^4 - {k}x^3 + {c}x$.''',
            fr'''$\displaystyle\int (x^3 - {b}x^2 + {c})\,\mathrm{{d}}x = \dfrac{{x^4}}{{4}} - {k}x^3 + {c}x + C$. Chọn $C = 0$.''',
            r'''Nguyên hàm của $x^3$ là $\dfrac{x^4}{4}$.'''
        ),
        (
            fr'''Giá trị lớn nhất của hàm số này trên $[0; {2*k}]$ bằng ${c}$.''',
            fr'''Giá trị lớn nhất của hàm số này trên $[0; {2*k}]$ bằng ${c + 10}$.''',
            fr'''$f'(x) = 3x^2 - {2*b}x = 0 \iff x = 0, x = {2*k}$. Ta có $f(0) = {c}, f({2*k}) = -{2*k**3} \implies \max\limits_{{[0; {2*k}]}} f(x) = {c}$.''',
            fr'''GTLN trên đoạn $[0; {2*k}]$ là $f(0) = {c} \ne {c + 10}$.'''
        ),
        (
            fr'''Diện tích hình phẳng giới hạn bởi đồ thị $(C)$, trục hoành và hai đường thẳng $x = 0, x = {2*k}$ bằng ${s_val}$ (đvdt).''',
            fr'''Diện tích hình phẳng giới hạn bởi đồ thị $(C)$, trục hoành và hai đường thẳng $x = 0, x = {2*k}$ là ${s_val + 20}$ (đvdt).''',
            fr'''Nghiệm của $f(x) = 0$ trên $[0; {2*k}]$ là $x = {k}$. $S = \displaystyle\int\limits_{{0}}^{{{k}}} f(x)\,\mathrm{{d}}x - \displaystyle\int\limits_{{{k}}}^{{{2*k}}} f(x)\,\mathrm{{d}}x = {s_val}$.''',
            fr'''$S = {s_val} \ne {s_val + 20}$.'''
        ),
        (
            fr'''Điểm cực tiểu của hàm số là $x = {2*k}$.''',
            fr'''Điểm cực tiểu của hàm số là $x = 0$.''',
            fr'''Đạo hàm đổi dấu từ âm sang dương khi qua $x = {2*k}$ nên $x = {2*k}$ là điểm cực tiểu.''',
            fr'''Tại $x = 0$ là điểm cực đại, điểm cực tiểu là $x = {2*k}$.'''
        )
    ]
    choices, loi_giai = make_tf_choices(items)
    return caudan, choices, loi_giai


def CuoiChuong4_TF_Cau6():
    # f(x) = 3x^2 - 2(a+b)x + ab với nghiệm nguyên đẹp
    roots = [(1, 2), (1, 3), (2, 3), (1, 4), (2, 4)]
    r1, r2 = random.choice(roots)
    s = r1 + r2
    p = r1 * r2
    b_coef = 2 * s
    caudan = fr'''Cho hàm số $f(x) = 3x^2 - {b_coef}x + {p}$ có một nguyên hàm là $F(x)$ thỏa mãn $F(0) = 0$.'''

    items = [
        (
            fr'''Biểu thức của nguyên hàm là $F(x) = x^3 - {s}x^2 + {p}x$.''',
            fr'''Biểu thức của nguyên hàm là $F(x) = x^3 - {b_coef}x^2 + {p}x$.''',
            fr'''$F(x) = \displaystyle\int (3x^2 - {b_coef}x + {p})\,\mathrm{{d}}x = x^3 - {s}x^2 + {p}x + C$. Do $F(0) = 0 \implies C = 0 \implies F(x) = x^3 - {s}x^2 + {p}x$.''',
            fr'''Hệ số của $x^2$ là $-{s}$ chứ không phải $-{b_coef}$.'''
        ),
        (
            r'''Nếu $G(x)$ là một nguyên hàm bất kỳ của $f(x)$ thì $F(5) - F(4) + G(4) = G(5)$.''',
            r'''Nếu $G(x)$ là một nguyên hàm bất kỳ của $f(x)$ thì $F(5) - F(4) = G(4) - G(5)$.''',
            r'''Hai nguyên hàm của cùng một hàm số sai khác nhau một hằng số: $G(x) = F(x) + C_0$. Khi đó $G(5) - G(4) = F(5) - F(4) \implies F(5) - F(4) + G(4) = G(5)$.''',
            r'''Theo tính chất tích phân: $G(5) - G(4) = \displaystyle\int\limits_{4}^{5} f(x)\,\mathrm{d}x = F(5) - F(4)$, khẳng định bằng đối số là sai.'''
        ),
        (
            fr'''Phương trình $f(x) = 0$ có hai nghiệm phân biệt là $x = {r1}$ và $x = {r2}$.''',
            fr'''Phương trình $f(x) = 0$ vô nghiệm trên $\mathbb{{R}}$.''',
            fr'''Ta có $\Delta' = {s}^2 - 3({p}) = ({r1-r2})^2 + {r1*r2} > 0$. Phương trình có hai nghiệm $x = {r1}$ và $x = {r2}$.''',
            fr'''Phương trình $f(x) = 0$ có hai nghiệm phân biệt là $x = {r1}, x = {r2}$.'''
        ),
        (
            fr'''Giá trị của $F({r1}) = {r1**3 - s*r1**2 + p*r1}$.''',
            fr'''Giá trị của $F({r1}) = {r1**3 + s*r1**2 + p*r1 + 10}$.''',
            fr'''Thay $x = {r1}$ vào $F(x)$ ta được $F({r1}) = {r1**3 - s*r1**2 + p*r1}$.''',
            fr'''$F({r1}) = {r1**3 - s*r1**2 + p*r1}$.'''
        )
    ]
    choices, loi_giai = make_tf_choices(items)
    return caudan, choices, loi_giai


# ==============================================================================
# CHƯƠNG V: TỌA ĐỘ TRONG KHÔNG GIAN (6 CÂU)
# ==============================================================================

def CuoiChuong5_TF_Cau1():
    # Đường thẳng d và giao điểm với mặt phẳng (Q) ngẫu nhiên hóa phong phú
    x0 = random.choice([-8, -6, -5, -4, -3, -2, -1, 1, 2, 3, 4, 5, 6, 8])
    y0 = random.choice([-5, -4, -3, -2, -1, 1, 2, 3, 4, 5])
    z0 = random.choice([2, 3, 4, 5, 6, 7])
    
    u1, u2, u3 = random.choice([(-4, -3, 2), (-3, 2, 1), (2, -1, 3), (1, 4, -2), (-2, 3, -1)])
    
    caudan = fr'''Trong không gian $Oxyz$, cho đường thẳng $d \colon \dfrac{{x{'+' if x0 < 0 else '-'}{abs(x0)}}}{{{u1}}} = \dfrac{{y{'+' if y0 < 0 else '-'}{abs(y0)}}}{{{u2}}} = \dfrac{{z - {z0}}}{{{u3}}}$. Xét tính đúng-sai của các khẳng định sau:'''

    items = [
        (
            fr'''Một vectơ chỉ phương của đường thẳng $d$ là $\vec{{u}} = ({-u1}; {-u2}; {-u3})$.''',
            fr'''Một vectơ chỉ phương của đường thẳng $d$ là $\vec{{u}} = ({-u1}; {-u2}; {u3})$.''',
            fr'''Vectơ dưới mẫu là $({u1}; {u2}; {u3}) = -({-u1}; {-u2}; {-u3})$, do đó $\vec{{u}} = ({-u1}; {-u2}; {-u3})$ là một VTCP của $d$.''',
            fr'''Vectơ chỉ phương của $d$ là $k({u1}; {u2}; {u3})$. Khẳng định $({-u1}; {-u2}; {u3})$ sai dấu ở cao độ.'''
        ),
        (
            fr'''Điểm $A({-x0}; {-y0}; {z0})$ thuộc đường thẳng $d$.''',
            fr'''Điểm $A({x0}; {y0}; {z0})$ thuộc đường thẳng $d$.''',
            fr'''Từ phương trình chính tắc của $d$, điểm đi qua là $A({-x0}; {-y0}; {z0})$.''',
            fr'''Điểm thuộc đường thẳng là $A({-x0}; {-y0}; {z0})$, không phải $({x0}; {y0}; {z0})$.'''
        ),
        (
            fr'''Đường thẳng $d_1 \colon \begin{{cases}} x = {-x0 + 1} + {u1}t \\ y = {-y0} + {u2}t \\ z = {z0 + 1} + {u3}t \end{{cases}}$ song song với đường thẳng $d$.''',
            fr'''Đường thẳng $d_1$ trùng với đường thẳng $d$.''',
            fr'''$d_1$ có VTCP cùng phương với $d$. Điểm $M_1({-x0 + 1}; {-y0}; {z0 + 1}) \in d_1$ không thuộc $d$ nên $d_1 \parallel d$.''',
            fr'''$M_1 \notin d$ nên hai đường thẳng song song chứ không trùng nhau.'''
        ),
        (
            r'''Mặt phẳng $(Oxy)$ có phương trình $z = 0$, cắt đường thẳng $d$ tại đúng $1$ điểm.''',
            r'''Đường thẳng $d$ song song với mặt phẳng $(Oxy)$.''',
            fr'''Vì vectơ chỉ phương của $d$ có cao độ $u_3 = {u3} \ne 0$ nên $d$ cắt $(Oxy)$ tại đúng $1$ điểm.''',
            fr'''$u_3 = {u3} \ne 0$ nên $d$ không song song với $(Oxy)$.'''
        )
    ]
    choices, loi_giai = make_tf_choices(items)
    return caudan, choices, loi_giai


def CuoiChuong5_TF_Cau2():
    # Cabin cáp treo với vận tốc nguyên đẹp
    cable_configs = [
        {"u": (2, -2, 1), "len_u": 3, "k_v": 2, "speed": 6.0},      # v = (4, -4, 2)
        {"u": (1, 2, 2),  "len_u": 3, "k_v": 3, "speed": 9.0},      # v = (3, 6, 6)
        {"u": (2, 3, 6),  "len_u": 7, "k_v": 1, "speed": 7.0},      # v = (2, 3, 6)
        {"u": (4, 4, 7),  "len_u": 9, "k_v": 1, "speed": 9.0},      # v = (4, 4, 7)
        {"u": (1, 4, 8),  "len_u": 9, "k_v": 1, "speed": 9.0},      # v = (1, 4, 8)
    ]
    cfg = random.choice(cable_configs)
    u1, u2, u3 = cfg["u"]
    speed = cfg["speed"]
    k_v = cfg["k_v"]
    vx, vy, vz = k_v * u1, k_v * u2, k_v * u3
    
    x0 = random.choice([5, 10, 15, 20])
    y0 = random.choice([2, 4, 6, 8])
    t_stop = random.choice([60, 120, 180])
    dist_AB = int(speed * t_stop)

    caudan = fr'''Trong không gian với hệ tọa độ $Oxyz$, một cabin cáp treo xuất phát từ điểm $A({x0}; {y0}; 0)$ và chuyển động đều theo đường cáp có vectơ chỉ phương là $\vec{{u}} = ({u1}; {u2}; {u3})$ với tốc độ ${speed:.1f}\text{{ m/s}}$ (đơn vị trên mỗi trục tọa độ là mét).'''

    items = [
        (
            fr'''Phương trình tham số của đường cáp là $\begin{{cases}} x = {x0} + {u1}s \\ y = {y0} + {u2}s \\ z = {u3}s \end{{cases}} (s \in \mathbb{{R}})$.''',
            fr'''Phương trình tham số của đường cáp là $\begin{{cases}} x = {u1} + {x0}s \\ y = {u2} + {y0}s \\ z = {u3} \end{{cases}}$.''',
            fr'''Đường thẳng đi qua $A({x0}; {y0}; 0)$ có VTCP $\vec{{u}} = ({u1}; {u2}; {u3})$ có phương trình: $x = {x0}+{u1}s, y = {y0}+{u2}s, z = {u3}s$.''',
            fr'''Điểm đi qua là $({x0}; {y0}; 0)$ và VTCP là $({u1}; {u2}; {u3})$.'''
        ),
        (
            fr'''Sau thời gian $t\text{{ (s)}}$ kể từ lúc xuất phát ($t \ge 0$), cabin đến điểm $M({vx}t+{x0}; {vy}t+{y0}; {vz}t)$.''',
            fr'''Sau thời gian $t\text{{ (s)}}$ kể từ lúc xuất phát, cabin đến điểm $M({u1}t+{x0}; {u2}t+{y0}; {u3}t)$.''',
            fr'''$|\vec{{u}}| = {cfg["len_u"]}$. Vectơ vận tốc $\vec{{v}} = \dfrac{{{speed}}}{{{cfg["len_u"]}}}\vec{{u}} = ({vx}; {vy}; {vz})$. Do đó $M = A + t\vec{{v}} = ({vx}t+{x0}; {vy}t+{y0}; {vz}t)$.''',
            fr'''Vận tốc là ${speed}\text{{ m/s}}$, do đó vectơ vận tốc là $({vx}; {vy}; {vz})$.'''
        ),
        (
            fr'''Cabin dừng ở điểm $B$ sau ${t_stop}\text{{ s}}$, khi đó quãng đường $AB$ dài ${dist_AB}\text{{ m}}$.''',
            fr'''Cabin dừng ở điểm $B$ sau ${t_stop}\text{{ s}}$, khi đó quãng đường $AB$ dài ${dist_AB - 50}\text{{ m}}$.''',
            fr'''Quãng đường $AB = v \cdot t = {speed} \times {t_stop} = {dist_AB}\text{{ m}}$.''',
            fr'''Quãng đường $AB = {speed} \times {t_stop} = {dist_AB}\text{{ m}} \ne {dist_AB - 50}\text{{ m}}$.'''
        ),
        (
            r'''Đường cáp $AB$ tạo với mặt phẳng $(Oxy)$ một góc có $\sin\varphi = \dfrac{''' + str(abs(u3)) + r'''}{''' + str(cfg["len_u"]) + r'''}$.''',
            r'''Đường cáp $AB$ song song với mặt phẳng $(Oxy)$.''',
            fr'''Mặt phẳng $(Oxy)$ có VTPT $\vec{{k}} = (0; 0; 1)$. $\sin\varphi = \dfrac{{|\vec{{u}} \cdot \vec{{k}}|}}{{|\vec{{u}}| \cdot |\vec{{k}}|}} = \dfrac{{{abs(u3)}}}{{{cfg["len_u"]}}}$.''',
            fr'''$\sin\varphi = \dfrac{{{abs(u3)}}}{{{cfg["len_u"]}}} \ne 0$ nên cáp không song song với $(Oxy)$.'''
        )
    ]
    choices, loi_giai = make_tf_choices(items)
    return caudan, choices, loi_giai


def CuoiChuong5_TF_Cau3():
    # Trạm thu phát sóng với bộ ba số Pytago nguyên đẹp
    pythago = [
        {"z0": 3,  "R": 5,  "r": 4},
        {"z0": 4,  "R": 5,  "r": 3},
        {"z0": 6,  "R": 10, "r": 8},
        {"z0": 8,  "R": 10, "r": 6},
        {"z0": 5,  "R": 13, "r": 12},
        {"z0": 12, "R": 13, "r": 5},
        {"z0": 8,  "R": 17, "r": 15},
        {"z0": 15, "R": 17, "r": 8},
        {"z0": 9,  "R": 15, "r": 12},
        {"z0": 12, "R": 15, "r": 9},
    ]
    cfg = random.choice(pythago)
    z0 = cfg["z0"]
    R = cfg["R"]
    r = cfg["r"]
    R2 = R**2
    
    x0 = random.choice([-5, -4, -3, -2, -1, 1, 2, 3, 4, 5])
    y0 = random.choice([-5, -4, -3, -2, -1, 1, 2, 3, 4, 5])
    
    y_sgn = '+' if y0 < 0 else '-'
    x_sgn = '+' if x0 < 0 else '-'

    caudan = fr'''Trong không gian với hệ trục tọa độ $Oxyz$ (đơn vị: km), một trạm thu phát sóng đặt tại $I({x0}; {y0}; {z0})$ với bán kính phủ sóng ${R}\text{{ km}}$. Xét tính đúng-sai của các khẳng định sau:'''

    items = [
        (
            fr'''Phương trình mặt cầu mô tả ranh giới vùng phủ sóng là $(x {x_sgn} {abs(x0)})^2 + (y {y_sgn} {abs(y0)})^2 + (z - {z0})^2 = {R2}$.''',
            fr'''Phương trình mặt cầu mô tả ranh giới vùng phủ sóng là $(x {x_sgn} {abs(x0)})^2 + (y {y_sgn} {abs(y0)})^2 + (z + {z0})^2 = {R2}$.''',
            fr'''Tâm $I({x0}; {y0}; {z0})$ và bán kính $R = {R} \implies (x {x_sgn} {abs(x0)})^2 + (y {y_sgn} {abs(y0)})^2 + (z - {z0})^2 = {R2}$.''',
            r'''Phương trình mặt cầu tâm $I(a; b; c)$ là $(x - a)^2 + (y - b)^2 + (z - c)^2 = R^2$.'''
        ),
        (
            fr'''Vị trí trạm $I$ cách mặt đất (mặt phẳng $Oxy$) một khoảng đúng bằng ${z0}\text{{ km}}$.''',
            fr'''Vị trí trạm $I$ cách mặt đất một khoảng bằng ${R}\text{{ km}}$.''',
            fr'''Khoảng cách từ $I({x0}; {y0}; {z0})$ đến mặt phẳng $(Oxy)$ là $d = |{z0}| = {z0}\text{{ km}}$.''',
            fr'''Khoảng cách đến $(Oxy)$ là cao độ $z_I = {z0}\text{{ km}} \ne {R}\text{{ km}}$.'''
        ),
        (
            fr'''Vùng phủ sóng trên mặt đất $(Oxy)$ là một hình tròn có bán kính $r = {r}\text{{ km}}$.''',
            fr'''Vùng phủ sóng trên mặt đất $(Oxy)$ là một hình tròn có bán kính $r = {R}\text{{ km}}$.''',
            fr'''Đường tròn giao tuyến trên $(Oxy)$ có bán kính $r = \sqrt{{R^2 - d^2}} = \sqrt{{{R2} - {z0**2}}} = {r}\text{{ km}}$.''',
            fr'''Bán kính giao tuyến trên mặt đất là $r = \sqrt{{R^2 - d^2}} = {r}\text{{ km}} \ne {R}\text{{ km}}$.'''
        ),
        (
            fr'''Tâm vùng phủ sóng trên mặt đất là điểm $H({x0}; {y0}; 0)$.''',
            fr'''Tâm vùng phủ sóng trên mặt đất là gốc tọa độ $O(0; 0; 0)$.''',
            fr'''Tâm vùng phủ sóng trên mặt đất là hình chiếu vuông góc của $I({x0}; {y0}; {z0})$ lên $(Oxy)$, tức $H({x0}; {y0}; 0)$.''',
            fr'''Tâm vùng phủ sóng trên mặt đất là $H({x0}; {y0}; 0) \ne (0; 0; 0)$.'''
        )
    ]
    choices, loi_giai = make_tf_choices(items)
    return caudan, choices, loi_giai


def CuoiChuong5_TF_Cau4():
    # Tấm đan bê tông ngẫu nhiên hóa kích thước
    presets = [
        {"w": 9,  "l": 12, "mc": 15, "am": 9,  "alpha": 30},
        {"w": 6,  "l": 8,  "mc": 10, "am": 6,  "alpha": 30},
        {"w": 12, "l": 16, "mc": 20, "am": 12, "alpha": 30},
        {"w": 15, "l": 20, "mc": 25, "am": 15, "alpha": 30},
    ]
    cfg = random.choice(presets)
    w_val, l_val, mc_val, am_val, alpha_val = cfg["w"], cfg["l"], cfg["mc"], cfg["am"], cfg["alpha"]

    caudan = fr'''\immini{{Một tấm đan bê tông hình chữ nhật $ABCD$ kích thước ${w_val}\,\text{{dm}} \times {l_val}\,\text{{dm}}$ nằm cạnh bờ tường vuông góc với sàn. Tấm đan được kéo lên tạo với sàn góc $\alpha$, giữ lại bởi sợi dây xích $MC = {mc_val}\,\text{{dm}}$ nối từ $C$ đến $M$ trên tường, $AM \perp$ sàn và $AM = {am_val}\,\text{{dm}}$. Chọn hệ trục $Oxyz$ với $A$ là gốc, $B$ thuộc tia $Ox$, $D$ thuộc tia $Oy$, tia $Oz$ hướng lên theo $AM$.}}{{
\begin{{tikzpicture}}[scale=0.6,>=stealth, font=\footnotesize, line join=round, line cap=round] 
    \coordinate (T) at (-.56,-.22);
    \coordinate (A) at (0,0); 
    \coordinate (B) at (0,3);
    \coordinate (P) at (6,5.4);
    \coordinate (O) at (6,2.4);
    \coordinate (E) at (3,-1);
    \coordinate (Q) at (9,1.4);
    \coordinate (G) at (4,1.6);
    \coordinate (H) at (4,5);
    \coordinate (J) at (1.27,0.51);
    \coordinate (K) at (2.8,0);
    \coordinate (L) at (5.52,1.09);
    \coordinate (M) at (2.8,0.7);
    \coordinate (N) at (5.52,1.79);
    \coordinate (S) at (4.57,1.41);
    \coordinate (I) at (7.72,0.36);
    \coordinate (R) at (4,4);
    \fill[black!30] (G)--(J)--(M)--(N);
    \draw[->] (A)--(T)node[below]{{$y$}};
    \draw[->] (G)node[above left]{{$A$}}--(H)node[right]{{$z$}};
    \draw[->] (S)--(I)node[above right]{{$x$}};
    \draw (A)--(B)--(P)--(O)--cycle (A)--(E)--(Q)--(O)--cycle;
    \draw[dashed] (G)--(S) (M)node[below right]{{$C$}} (N)--(L);
    \draw[thick] (G)--(J)node[above]{{$D$}}--(M)--(N)node[right]{{$B$}}--cycle;
    \draw (R)node[right]{{$M$}}--(M);
\end{{tikzpicture}}}}'''

    items = [
        (
            fr'''Góc giữa tấm đan và mặt sàn là $\alpha = {alpha_val}^\circ$.''',
            r'''Góc giữa tấm đan và mặt sàn là $\alpha = 45^\circ$.''',
            fr'''Dựa vào tam giác vuông và độ dài dây xích $MC = {mc_val}\text{{ dm}}$, giải phương trình ta tìm được $\alpha = {alpha_val}^\circ$.''',
            fr'''Góc tìm được là $\alpha = {alpha_val}^\circ \ne 45^\circ$.'''
        ),
        (
            r'''Phương trình mặt phẳng chứa tấm đan sau khi kéo lên là $x - \sqrt{3}z = 0$.''',
            r'''Phương trình mặt phẳng chứa tấm đan sau khi kéo lên là $\sqrt{3}x - z = 0$.''',
            r'''Tấm đan quay quanh trục $AD$ tạo góc $30^\circ$ với sàn, phương trình mặt phẳng là $x - \sqrt{3}z = 0$.''',
            r'''Phương trình đúng là $x - \sqrt{3}z = 0$.'''
        ),
        (
            r'''Điểm $M$ thuộc trục $Oz$ có tọa độ $M(0; 0; 9)$.''',
            r'''Điểm $M$ thuộc mặt phẳng có phương trình $z = 0$.''',
            r'''Vì $AM$ vuông góc với mặt sàn và $AM = 9\text{ dm}$ nên $M(0; 0; 9)$ thuộc trục $Oz$. Mặt phẳng $z = 0$ là mặt sàn, $M$ không thuộc mặt sàn.''',
            r'''$M$ nằm trên bờ tường có cao độ $z = 9 \ne 0$.'''
        ),
        (
            r'''Hình chiếu vuông góc của tấm đan lên mặt sàn có diện tích $S' = S \cos 30^\circ$.''',
            r'''Hình chiếu vuông góc của tấm đan lên mặt sàn có diện tích không đổi.''',
            r'''Vì tấm đan nghiêng một góc $\alpha = 30^\circ$ nên diện tích hình chiếu là $S' = S \cos 30^\circ = \dfrac{\sqrt{3}}{2}S \ne S$.''',
            r'''Khi nghiêng một góc $\alpha > 0$, diện tích hình chiếu thu hẹp theo công thức $S' = S\cos\alpha$.'''
        )
    ]
    choices, loi_giai = make_tf_choices(items)
    return caudan, choices, loi_giai


def CuoiChuong5_TF_Cau5():
    # Kho chứa hàng lăng trụ đứng
    caudan = r'''Một kho chứa hàng hình lăng trụ đứng $ABFPE.DCGQH$ có đáy là hình chữ nhật và mái $EFP, HQG$ là tam giác cân. Kích thước kho: $AB = 6\text{ m}, AE = 5\text{ m}, AD = 8\text{ m}$, chiều cao nóc nhà $QT = 7\text{ m}$ (với $T$ là trung điểm $DC$). Chọn hệ trục tọa độ với $O \in AD$ sao cho $OA = 2\text{ m}$. Khi đó:'''

    items = [
        (
            r'''Vectơ $\overrightarrow{OC}$ có tọa độ là $(-6; 6; 0)$.''',
            r'''Vectơ $\overrightarrow{OC}$ có tọa độ là $(6; 6; 0)$.''',
            r'''Điểm $O$ cách $A$ một đoạn $2\text{ m}$, $AD = 8\text{ m} \implies D(-6; 0; 0)$. $C = D + \vec{DC} = (-6; 6; 0) \implies \overrightarrow{OC} = (-6; 6; 0)$.''',
            r'''$D$ nằm trên tia âm của trục $Ox$ nên hoành độ là $-6$, do đó $\overrightarrow{OC} = (-6; 6; 0)$.'''
        ),
        (
            r'''Tọa độ điểm nóc nhà $Q$ là $(-6; 3; 7)$.''',
            r'''Tọa độ điểm nóc nhà $Q$ là $(-6; 3; 5)$.''',
            r'''$T$ là trung điểm $DC \implies T(-6; 3; 0)$. Đỉnh nóc $Q$ nằm thẳng đứng trên $T$ ở độ cao $7\text{ m} \implies Q(-6; 3; 7)$.''',
            r'''Chiều cao nóc nhà là $QT = 7\text{ m}$ nên cao độ $z_Q = 7$, không phải $5$.'''
        ),
        (
            r'''Khoảng cách từ điểm $T$ đến mặt phẳng mái $(EPQH)$ xấp xỉ $1,66\text{ m}$.''',
            r'''Khoảng cách từ điểm $T$ đến mặt phẳng $(EPQH)$ là $2\sqrt{13}\text{ m}$.''',
            r'''Tính toán khoảng cách từ điểm đến mặt phẳng mái nghiêng ta được $d \approx 1,66\text{ m} \ne 2\sqrt{13} \approx 7,21\text{ m}$.''',
            r'''Khoảng cách $d(T, (EPQH)) \approx 1,66\text{ m} \ne 2\sqrt{13}\text{ m}$.'''
        ),
        (
            r'''Độ dài đoạn cáp nối tối thiểu từ $O$ qua điểm $K$ trên trục $Oz$ đến camera tại trung điểm $FG$ bằng $5 + 2\sqrt{10}\text{ m}$.''',
            r'''Độ dài đoạn cáp nối tối thiểu từ $O$ đến camera là $15\text{ m}$.''',
            r'''Sử dụng bài toán trải mặt phẳng tìm đường đi ngắn nhất, độ dài tối thiểu là $5 + 2\sqrt{10}\text{ m}$.''',
            r'''Độ dài đoạn cáp tối thiểu chính xác là $5 + 2\sqrt{10}\text{ m}$.'''
        )
    ]
    choices, loi_giai = make_tf_choices(items)
    return caudan, choices, loi_giai


def CuoiChuong5_TF_Cau6():
    # Mặt cầu (S) với số liệu nguyên đẹp phong phú
    x0 = random.choice([-4, -3, -2, -1, 1, 2, 3, 4])
    y0 = random.choice([-4, -3, -2, -1, 1, 2, 3, 4])
    z0 = random.choice([-4, -3, -2, -1, 1, 2, 3, 4])
    R = random.choice([3, 4, 5, 6, 7])
    R2 = R**2
    
    caudan = fr'''Trong không gian $Oxyz$, cho mặt cầu $(S) \colon (x {'+' if x0 < 0 else '-'} {abs(x0)})^2 + (y {'+' if y0 < 0 else '-'} {abs(y0)})^2 + (z {'+' if z0 < 0 else '-'} {abs(z0)})^2 = {R2}$. Xét tính đúng-sai của các khẳng định sau:'''

    items = [
        (
            fr'''Mặt cầu $(S)$ có tâm $I({x0}; {y0}; {z0})$ và bán kính $R = {R}$.''',
            fr'''Mặt cầu $(S)$ có tâm $I({-x0}; {-y0}; {-z0})$ và bán kính $R = {R2}$.''',
            fr'''Từ phương trình chính tắc suy ra $I({x0}; {y0}; {z0})$ và $R = \sqrt{{{R2}}} = {R}$.''',
            fr'''Tâm $I({x0}; {y0}; {z0})$ và $R = {R}$, khẳng định $R = {R2}$ là sai.'''
        ),
        (
            fr'''Khoảng cách từ tâm $I$ đến gốc tọa độ $O$ bằng $\sqrt{{{x0**2 + y0**2 + z0**2}}}$.''',
            fr'''Khoảng cách từ tâm $I$ đến gốc tọa độ $O$ bằng ${abs(x0) + abs(y0) + abs(z0)}$.''',
            fr'''$OI = \sqrt{{{x0}^2 + {y0}^2 + ({z0})^2}} = \sqrt{{{x0**2 + y0**2 + z0**2}}}$.''',
            fr'''Khoảng cách đúng là $\sqrt{{{x0**2 + y0**2 + z0**2}}} \ne {abs(x0) + abs(y0) + abs(z0)}$.'''
        ),
        (
            fr'''Mặt phẳng tiếp xúc với mặt cầu $(S)$ tại điểm $B({x0}; {y0}; {z0 + R})$ có phương trình $z = {z0 + R}$.''',
            fr'''Mặt phẳng tiếp xúc với mặt cầu $(S)$ tại điểm $B({x0}; {y0}; {z0 + R})$ có phương trình $x + y = {x0 + y0}$.''',
            fr'''VTPT tại $B$ là $\overrightarrow{{IB}} = (0; 0; {R}) \parallel (0; 0; 1)$. Phương trình tiếp diện là $z - ({z0 + R}) = 0 \iff z = {z0 + R}$.''',
            fr'''VTPT cùng phương với trục $Oz$ nên phương trình tiếp diện là $z = {z0 + R}$.'''
        ),
        (
            fr'''Điểm $A({x0 + R + 1}; {y0}; {z0})$ nằm bên ngoài mặt cầu $(S)$.''',
            fr'''Điểm $A({x0 + R + 1}; {y0}; {z0})$ nằm bên trong mặt cầu $(S)$.''',
            fr'''$IA = {R + 1} > {R} = R_{{(S)}} \implies A$ nằm ngoài mặt cầu $(S)$.''',
            fr'''Khoảng cách $IA = {R + 1} > R$ nên điểm $A$ nằm ngoài mặt cầu.'''
        )
    ]
    choices, loi_giai = make_tf_choices(items)
    return caudan, choices, loi_giai


# ==============================================================================
# CHƯƠNG VI: XÁC SUẤT CÓ ĐIỀU KIỆN (8 CÂU)
# ==============================================================================

def CuoiChuong6_TF_Cau1():
    # Hai hộp bi với phân số tối giản cực đẹp
    boxes_configs = [
        {"b1": 2, "w1": 6, "b2": 2, "w2": 5},   # n1=8, n2=8
        {"b1": 3, "w1": 9, "b2": 3, "w2": 8},   # n1=12, n2=12
        {"b1": 4, "w1": 8, "b2": 3, "w2": 5},   # n1=12, n2=9
        {"b1": 2, "w1": 4, "b2": 3, "w2": 5},   # n1=6, n2=9
        {"b1": 3, "w1": 6, "b2": 2, "w2": 3},   # n1=9, n2=6
    ]
    cfg = random.choice(boxes_configs)
    b1, w1 = cfg["b1"], cfg["w1"]
    b2, w2 = cfg["b2"], cfg["w2"]
    
    n1 = b1 + w1
    n2 = b2 + w2 + 1
    
    p_D1 = Fraction(b1, n1)
    p_T1 = Fraction(w1, n1)
    
    p_D2_given_D1 = Fraction(b2 + 1, n2)
    p_D2_given_T1 = Fraction(b2, n2)
    
    p_D2 = p_D1 * p_D2_given_D1 + p_T1 * p_D2_given_T1
    p_T1_given_D2 = (p_T1 * p_D2_given_T1) / p_D2

    caudan = fr'''Có hai hộp: hộp I có ${b1}$ viên bi đen và ${w1}$ viên bi trắng; hộp II có ${b2}$ viên bi đen và ${w2}$ viên bi trắng. Bạn An chọn ngẫu nhiên một viên bi từ hộp I thả vào hộp II, sau đó, bạn Bình chọn ngẫu nhiên một viên bi từ hộp II. Khi đó:'''

    items = [
        (
            fr'''Xác suất để bạn Bình chọn được viên bi màu đen là $\dfrac{{{p_D2.numerator}}}{{{p_D2.denominator}}}$.''',
            r'''Xác suất để bạn Bình chọn được viên bi màu đen là $\dfrac{1}{2}$.''',
            fr'''Theo công thức xác suất toàn phần: $P(D_2) = P(D_1)P(D_2|D_1) + P(T_1)P(D_2|T_1) = \dfrac{{{b1}}}{{{n1}}} \cdot \dfrac{{{b2+1}}}{{{n2}}} + \dfrac{{{w1}}}{{{n1}}} \cdot \dfrac{{{b2}}}{{{n2}}} = \dfrac{{{p_D2.numerator}}}{{{p_D2.denominator}}}$.''',
            fr'''$P(D_2) = \dfrac{{{p_D2.numerator}}}{{{p_D2.denominator}}} \ne \dfrac{{1}}{{2}}$.'''
        ),
        (
            fr'''Giả sử bạn Bình chọn được viên bi màu đen. Xác suất để bạn An đã chọn viên bi màu trắng là $\dfrac{{{p_T1_given_D2.numerator}}}{{{p_T1_given_D2.denominator}}}$.''',
            r'''Giả sử bạn Bình chọn được viên bi màu đen. Xác suất để bạn An chọn được viên bi màu trắng là $\dfrac{1}{3}$.''',
            fr'''Theo công thức Bayes: $P(T_1|D_2) = \dfrac{{P(T_1) P(D_2|T_1)}}{{P(D_2)}} = \dfrac{{{p_T1_given_D2.numerator}}}{{{p_T1_given_D2.denominator}}}$.''',
            fr'''$P(T_1|D_2) = \dfrac{{{p_T1_given_D2.numerator}}}{{{p_T1_given_D2.denominator}}} \ne \dfrac{{1}}{{3}}$.'''
        ),
        (
            fr'''Giả sử bạn An chọn được viên bi màu trắng. Xác suất để bạn Bình chọn được viên bi màu đen là $\dfrac{{{b2}}}{{{n2}}}$.''',
            fr'''Giả sử bạn An chọn được viên bi màu trắng. Xác suất để bạn Bình chọn được viên bi màu đen là $\dfrac{{{b2}}}{{{n2 - 1}}}$.''',
            fr'''Khi An chuyển $1$ bi trắng sang hộp II thì hộp II có tổng cộng ${n2}$ viên, trong đó có ${b2}$ viên đen. Xác suất là $\dfrac{{{b2}}}{{{n2}}}$.''',
            fr'''Hộp II lúc này có tổng cộng ${n2}$ viên nên xác suất là $\dfrac{{{b2}}}{{{n2}}}$.'''
        ),
        (
            fr'''Xác suất bạn An chọn được viên bi màu đen từ hộp I là $\dfrac{{{p_D1.numerator}}}{{{p_D1.denominator}}}$.''',
            r'''Xác suất bạn An chọn được viên bi màu đen từ hộp I là $\dfrac{1}{5}$.''',
            fr'''Hộp I có ${b1}$ viên đen trong tổng số ${n1}$ viên $\implies P(D_1) = \dfrac{{{b1}}}{{{n1}}} = \dfrac{{{p_D1.numerator}}}{{{p_D1.denominator}}}$.''',
            fr'''$P(D_1) = \dfrac{{{p_D1.numerator}}}{{{p_D1.denominator}}} \ne \dfrac{{1}}{{5}}$.'''
        )
    ]
    choices, loi_giai = make_tf_choices(items)
    return caudan, choices, loi_giai


def CuoiChuong6_TF_Cau2():
    # Hai người kiểm tra tiền giả với xác suất số thập phân 2 chữ số tròn đẹp
    cases = [
        {"pV": 0.70, "pQ_V": 0.60, "pQ_notV": 0.40},   # P(both_not) = 0.30 * 0.40 = 0.12 => at_least_one = 0.88
        {"pV": 0.60, "pQ_V": 0.70, "pQ_notV": 0.30},   # P(both_not) = 0.40 * 0.30 = 0.12 => at_least_one = 0.88
        {"pV": 0.80, "pQ_V": 0.75, "pQ_notV": 0.25},   # P(both_not) = 0.20 * 0.25 = 0.05 => at_least_one = 0.95
        {"pV": 0.75, "pQ_V": 0.80, "pQ_notV": 0.40},   # P(both_not) = 0.25 * 0.40 = 0.10 => at_least_one = 0.90
        {"pV": 0.80, "pQ_V": 0.70, "pQ_notV": 0.20},   # P(both_not) = 0.20 * 0.20 = 0.04 => at_least_one = 0.96
    ]
    c = random.choice(cases)
    pV = c["pV"]
    pQ_given_V = c["pQ_V"]
    pQ_given_notV = c["pQ_notV"]
    
    pNotV = round(1 - pV, 2)
    pBothNot = round(pNotV * pQ_given_notV, 3)
    pAtLeastOne = round(1 - pBothNot, 3)
    pV_given_atLeastOne = round(pV / pAtLeastOne, 2)

    caudan = fr'''Một tờ tiền giả lần lượt bị hai bạn Vương và Quân kiểm tra. Xác suất để bạn Vương phát hiện ra tờ này giả là ${pV}$. Nếu bạn Vương cho rằng đây là tiền giả, thì xác suất để bạn Quân cũng nhận định như thế là ${pQ_given_V}$. Ngược lại, nếu bạn Vương cho rằng tờ này là tiền thật thì xác suất để bạn Quân cũng nhận định như thế là ${pQ_given_notV}$. Xét tính đúng-sai của các khẳng định sau:'''

    items = [
        (
            fr'''Xác suất để bạn Vương không phát hiện ra tờ tiền đó giả là ${pNotV}$.''',
            fr'''Xác suất để bạn Vương không phát hiện ra tờ tiền đó giả là ${round(pNotV + 0.1, 2)}$.''',
            fr'''$P(\overline{{V}}) = 1 - P(V) = 1 - {pV} = {pNotV}$.''',
            fr'''$1 - {pV} = {pNotV} \ne {round(pNotV + 0.1, 2)}$.'''
        ),
        (
            fr'''Xác suất để hai người này đều không phát hiện đây là tờ tiền giả bằng ${pBothNot:.2f}$.''',
            fr'''Xác suất để hai người này đều không phát hiện đây là tờ tiền giả là $0,25$.''',
            fr'''$P(\overline{{V}} \cap \overline{{Q}}) = P(\overline{{V}}) \cdot P(\overline{{Q}}|\overline{{V}}) = {pNotV} \times {pQ_given_notV} = {pBothNot:.2f}$.''',
            fr'''Xác suất đúng là ${pBothNot:.2f} \ne 0,25$.'''
        ),
        (
            fr'''Xác suất để ít nhất một trong hai người phát hiện ra tờ tiền giả là ${pAtLeastOne:.2f}$.''',
            fr'''Xác suất để ít nhất một trong hai người này phát hiện ra tờ tiền đó là giả là $0,50$.''',
            fr'''$P(\text{{ít nhất 1 người}}) = 1 - P(\overline{{V}} \cap \overline{{Q}}) = 1 - {pBothNot} = {pAtLeastOne:.2f}$.''',
            fr'''$1 - {pBothNot} = {pAtLeastOne:.2f} \ne 0,50$.'''
        ),
        (
            fr'''Biết tờ tiền đã bị ít nhất một trong hai người phát hiện là giả, xác suất để bạn Vương phát hiện ra nó giả xấp xỉ ${pV_given_atLeastOne:.2f}$.''',
            fr'''Biết tờ tiền đó đã bị ít nhất một trong hai người này phát hiện là giả, xác suất để Bạn Vương phát hiện ra nó giả là $0,40$.''',
            fr'''$P(V|\text{{ít nhất 1}}) = \dfrac{{P(V)}}{{P(\text{{ít nhất 1}})}} = \dfrac{{{pV}}}{{{pAtLeastOne}}} \approx {pV_given_atLeastOne:.2f}$.''',
            fr'''$\dfrac{{{pV}}}{{{pAtLeastOne}}} \approx {pV_given_atLeastOne:.2f} \ne 0,40$.'''
        )
    ]
    choices, loi_giai = make_tf_choices(items)
    return caudan, choices, loi_giai


def CuoiChuong6_TF_Cau3():
    # Hai phác đồ điều trị với phần trăm tròn đẹp
    cases = [
        {"cure_A": 0.60, "side_A": 0.04, "cure_B": 0.80, "side_B": 0.08},  # side_total = 6%
        {"cure_A": 0.70, "side_A": 0.06, "cure_B": 0.80, "side_B": 0.10},  # side_total = 8%
        {"cure_A": 0.65, "side_A": 0.05, "cure_B": 0.75, "side_B": 0.09},  # side_total = 7%
        {"cure_A": 0.60, "side_A": 0.05, "cure_B": 0.70, "side_B": 0.15},  # side_total = 10%
    ]
    c = random.choice(cases)
    p_cure_A = c["cure_A"]
    p_side_A = c["side_A"]
    p_cure_B = c["cure_B"]
    p_side_B = c["side_B"]
    
    p_side_total = round(0.5 * p_side_A + 0.5 * p_side_B, 3)
    p_B_given_side = round((0.5 * p_side_B) / p_side_total, 2)

    caudan = fr'''Có hai phác đồ điều trị A và B cho một loại bệnh. Phác đồ A có xác suất chữa khỏi là ${int(p_cure_A*100)}\%$ và xác suất gây tác dụng phụ nghiêm trọng là ${int(p_side_A*100)}\%$. Phác đồ B có xác suất chữa khỏi là ${int(p_cure_B*100)}\%$ và xác suất gây tác dụng phụ nghiêm trọng là ${int(p_side_B*100)}\%$. Một bệnh nhân được chỉ định ngẫu nhiên một trong hai phác đồ với xác suất như nhau ($50\%$).'''

    items = [
        (
            fr'''Xác suất để bệnh nhân bị tác dụng phụ nghiêm trọng là ${p_side_total*100:.1f}\%$.''',
            fr'''Xác suất để bệnh nhân bị tác dụng phụ nghiêm trọng là $20\%$.''',
            fr'''$P(TP) = 0,5 \times {p_side_A} + 0,5 \times {p_side_B} = {p_side_total} = {p_side_total*100:.1f}\%$.''',
            fr'''$P(TP) = {p_side_total*100:.1f}\% \ne 20\%$.'''
        ),
        (
            fr'''Nếu biết bệnh nhân gặp tác dụng phụ nghiêm trọng thì xác suất bệnh nhân đã điều trị bằng phác đồ B xấp xỉ ${p_B_given_side:.2f}$.''',
            fr'''Nếu biết bệnh nhân gặp tác dụng phụ nghiêm trọng thì xác suất bệnh nhân đã điều trị bằng phác đồ B nhỏ hơn $0,3$.''',
            fr'''$P(B|TP) = \dfrac{{0,5 \times {p_side_B}}}{{{p_side_total}}} \approx {p_B_given_side:.2f} > 0,50$.''',
            fr'''$P(B|TP) \approx {p_B_given_side:.2f}$, khẳng định nhỏ hơn $0,3$ là sai.'''
        ),
        (
            fr'''Xác suất bệnh nhân điều trị bằng phác đồ A và được chữa khỏi bệnh là ${0.5 * p_cure_A:.2f}$.''',
            fr'''Xác suất bệnh nhân điều trị bằng phác đồ A và được chữa khỏi bệnh là ${p_cure_A}$.''',
            fr'''$P(A \cap K) = P(A) \cdot P(K|A) = 0,5 \times {p_cure_A} = {0.5 * p_cure_A:.2f}$.''',
            fr'''$P(A \cap K) = 0,5 \times {p_cure_A} = {0.5 * p_cure_A:.2f} \ne {p_cure_A}$.'''
        ),
        (
            fr'''Xác suất bệnh nhân điều trị bằng phác đồ B và được chữa khỏi bệnh là ${0.5 * p_cure_B:.2f}$.''',
            fr'''Xác suất bệnh nhân điều trị bằng phác đồ B và được chữa khỏi bệnh là ${p_cure_B}$.''',
            fr'''$P(B \cap K) = P(B) \cdot P(K|B) = 0,5 \times {p_cure_B} = {0.5 * p_cure_B:.2f}$.''',
            fr'''$P(B \cap K) = 0,5 \times {p_cure_B} = {0.5 * p_cure_B:.2f} \ne {p_cure_B}$.'''
        )
    ]
    choices, loi_giai = make_tf_choices(items)
    return caudan, choices, loi_giai


def CuoiChuong6_TF_Cau4():
    # Khảo sát BHYT ngẫu nhiên hóa
    p_ins = random.choice([0.60, 0.70, 0.80])
    p_sup_given_ins = random.choice([0.80, 0.85, 0.90])
    p_sup_given_notIns = random.choice([0.50, 0.60])
    
    p_notIns = round(1 - p_ins, 2)
    p_sup = round(p_ins * p_sup_given_ins + p_notIns * p_sup_given_notIns, 4)
    p_notSup = round(1 - p_sup, 4)

    caudan = fr'''Trong một cuộc khảo sát, có ${int(p_ins*100)}\%$ người tham gia có bảo hiểm y tế. Biết rằng ${int(p_sup_given_ins*100)}\%$ người có bảo hiểm và ${int(p_sup_given_notIns*100)}\%$ người không có bảo hiểm được hỗ trợ chi phí khám chữa bệnh. Chọn ngẫu nhiên một người từ cuộc khảo sát.'''

    items = [
        (
            fr'''Xác suất chọn được người có bảo hiểm và được hỗ trợ chi phí là ${p_ins * p_sup_given_ins:.2f}$.''',
            fr'''Xác suất chọn được người có bảo hiểm và được hỗ trợ chi phí là ${p_sup_given_ins}$.''',
            fr'''$P(B \cap HT) = P(B) \cdot P(HT|B) = {p_ins} \times {p_sup_given_ins} = {p_ins * p_sup_given_ins:.2f}$.''',
            fr'''$P(B \cap HT) = {p_ins * p_sup_given_ins:.2f} \ne {p_sup_given_ins}$.'''
        ),
        (
            fr'''Xác suất chọn được người không được hỗ trợ chi phí khám chữa bệnh là ${p_notSup:.2f}$.''',
            fr'''Xác suất chọn được người không được hỗ trợ chi phí khám chữa bệnh là $0,45$.''',
            fr'''$P(HT) = {p_sup} \implies P(\overline{{HT}}) = 1 - {p_sup} = {p_notSup:.2f}$.''',
            fr'''$P(\overline{{HT}}) = {p_notSup:.2f} \ne 0,45$.'''
        ),
        (
            fr'''Tỉ lệ người không có bảo hiểm y tế trong cuộc khảo sát là ${int(p_notIns*100)}\%$.''',
            fr'''Tỉ lệ người không có bảo hiểm y tế là $40\%$.''',
            fr'''$100\% - {int(p_ins*100)}\% = {int(p_notIns*100)}\%$.''',
            fr'''$100\% - {int(p_ins*100)}\% = {int(p_notIns*100)}\%$.'''
        ),
        (
            fr'''Xác suất chọn được người có bảo hiểm y tế lớn hơn xác suất chọn được người không có bảo hiểm y tế.''',
            r'''Xác suất chọn được người không có bảo hiểm y tế lớn hơn người có bảo hiểm y tế.''',
            fr'''Vì ${int(p_ins*100)}\% > {int(p_notIns*100)}\%$ nên khẳng định là đúng.''',
            fr'''Vì ${int(p_ins*100)}\% > {int(p_notIns*100)}\%$ nên tỉ lệ có BHYT cao hơn.'''
        )
    ]
    choices, loi_giai = make_tf_choices(items)
    return caudan, choices, loi_giai


def CuoiChuong6_TF_Cau5():
    # Chuông báo siêu thị ngẫu nhiên hóa
    p_alarm_unpaid = 0.99
    p_alarm_paid = 0.001
    p_unpaid = 0.001
    p_paid = round(1 - p_unpaid, 3)

    caudan = fr'''Ở cửa siêu thị có thiết bị cảnh báo hàng chưa thanh toán. Thiết bị phát chuông với $99\%$ hàng qua cửa mà \textbf{{chưa thanh toán}} và $0,1\%$ hàng \textbf{{đã thanh toán}}. Tỷ lệ hàng qua cửa chưa thanh toán là $0,1\%$. Chọn ngẫu nhiên một hàng hóa qua cửa:'''

    items = [
        (
            fr'''Xác suất để hàng hóa qua cửa đã thanh toán là ${p_paid}$.''',
            r'''Xác suất để hàng hóa qua cửa đã thanh toán là $0,99$.''',
            fr'''$1 - {p_unpaid} = {p_paid}$.''',
            fr'''$1 - {p_unpaid} = {p_paid} \ne 0,99$.'''
        ),
        (
            r'''Biết rằng hàng hóa đã thanh toán, xác suất để thiết bị phát chuông cảnh báo là $0,001$.''',
            r'''Biết rằng hàng hóa đã thanh toán, xác suất để thiết bị phát chuông cảnh báo là $0,01$.''',
            r'''Theo giả thiết: thiết bị phát chuông với $0,1\% = 0,001$ các hàng hóa đã thanh toán.''',
            r'''Xác suất theo giả thiết là $0,1\% = 0,001$.'''
        ),
        (
            r'''Xác suất để hàng hóa qua cửa chưa thanh toán và thiết bị phát chuông cảnh báo là $0,00099$.''',
            r'''Xác suất để hàng hóa qua cửa chưa thanh toán và thiết bị phát chuông cảnh báo là $0,01$.''',
            r'''$P(\text{chưa thanh toán} \cap \text{chuông}) = 0,001 \times 0,99 = 0,00099$.''',
            r'''$0,001 \times 0,99 = 0,00099 \ne 0,01$.'''
        ),
        (
            r'''Xác suất hàng hóa qua cửa chưa thanh toán và thiết bị không phát chuông cảnh báo là $10^{-5}$.''',
            r'''Xác suất hàng hóa qua cửa chưa thanh toán và thiết bị không phát chuông cảnh báo là $10^{-3}$.''',
            r'''$P(\text{chưa thanh toán} \cap \text{không chuông}) = 0,001 \times (1 - 0,99) = 0,001 \times 0,01 = 10^{-5}$.''',
            r'''$0,001 \times 0,01 = 10^{-5} \ne 10^{-3}$.'''
        )
    ]
    choices, loi_giai = make_tf_choices(items)
    return caudan, choices, loi_giai


def CuoiChuong6_TF_Cau6():
    # RT-PCR Covid-19 với số liệu phần trăm đẹp
    cases = [
        {"p_dis": 0.05, "fp": 0.05, "fn": 0.10},  # pos = 0.05*0.90 + 0.95*0.05 = 0.045 + 0.0475 = 0.0925
        {"p_dis": 0.04, "fp": 0.04, "fn": 0.10},  # pos = 0.04*0.90 + 0.96*0.04 = 0.036 + 0.0384 = 0.0744
        {"p_dis": 0.05, "fp": 0.02, "fn": 0.10},  # pos = 0.05*0.90 + 0.95*0.02 = 0.045 + 0.019 = 0.064
        {"p_dis": 0.10, "fp": 0.05, "fn": 0.10},  # pos = 0.10*0.90 + 0.90*0.05 = 0.090 + 0.045 = 0.135
    ]
    c = random.choice(cases)
    p_dis = c["p_dis"]
    fp = c["fp"]
    fn = c["fn"]
    
    tp = round(1 - fn, 2)
    p_pos = round(p_dis * tp + (1 - p_dis) * fp, 4)
    p_pos_pct = p_pos * 100
    p_real_given_pos = round((p_dis * tp) / p_pos * 100, 1)

    caudan = fr'''Trong xét nghiệm RT-PCR xác định nhiễm virus: tỉ lệ dương tính giả là ${int(fp*100)}\%$, tỉ lệ âm tính giả là ${int(fn*100)}\%$, và tỉ lệ mắc bệnh trong cộng đồng là ${int(p_dis*100)}\%$. Xét tính đúng-sai của các khẳng định sau:'''

    items = [
        (
            fr'''Xác suất xét nghiệm RT-PCR có kết quả dương tính là ${p_pos_pct:.2f}\%$.''',
            fr'''Xác suất xét nghiệm RT-PCR có kết quả dương tính là ${p_pos_pct + 10:.2f}\%$.''',
            fr'''Theo xác suất toàn phần: $P(+) = {p_dis}({tp}) + {1 - p_dis:.2f}({fp}) = {p_pos} = ${p_pos_pct:.2f}\%$.''',
            fr'''$P(+) = ${p_pos_pct:.2f}\% \ne ${p_pos_pct + 10:.2f}\%$.'''
        ),
        (
            fr'''Xác suất dương tính thật bằng ${int(tp*100)}\%$.''',
            r'''Xác suất dương tính thật bằng $99\%$.''',
            fr'''Vì tỉ lệ âm tính giả là ${int(fn*100)}\%$ nên tỉ lệ dương tính thật là $100\% - ${int(fn*100)}\% = ${int(tp*100)}\%$.''',
            fr'''Tỉ lệ dương tính thật bằng $1 - {fn} = ${int(tp*100)}\% \ne 99\%$.'''
        ),
        (
            fr'''Trong những người có kết quả xét nghiệm dương tính, xác suất người đó thực sự nhiễm virus xấp xỉ ${p_real_given_pos}\%$.''',
            r'''Xác suất người nhiễm virus trong những người có kết quả dương tính lớn hơn $90\%$.''',
            fr'''Theo Bayes: $P(B|+) = \dfrac{{{p_dis} \times {tp}}}{{{p_pos}}} \approx ${p_real_given_pos}\% < 90\%$.''',
            fr'''$P(B|+) \approx ${p_real_given_pos}\% < 90\%$.'''
        ),
        (
            r'''Xác suất một người không nhiễm virus khi có kết quả âm tính lớn hơn $95\%$.''',
            r'''Xác suất một người không nhiễm virus khi có kết quả âm tính nhỏ hơn $50\%$.''',
            r'''Hầu hết các xét nghiệm âm tính đều thuộc về người không nhiễm bệnh, xác suất này luôn $> 95\%$.''',
            r'''Xác suất này xấp xỉ trên $99\%$, khẳng định nhỏ hơn $50\%$ là sai.'''
        )
    ]
    choices, loi_giai = make_tf_choices(items)
    return caudan, choices, loi_giai


def CuoiChuong6_TF_Cau7():
    # Bảng 2x2 hút thuốc lá và ung thư phổi ngẫu nhiên hóa
    pool = [
        {"smoke_cancer": 1200, "smoke_nocancer": 1300, "nosmoke_cancer": 300},
        {"smoke_cancer": 1000, "smoke_nocancer": 1500, "nosmoke_cancer": 200},
        {"smoke_cancer": 1500, "smoke_nocancer": 1500, "nosmoke_cancer": 400},
        {"smoke_cancer": 1124, "smoke_nocancer": 1126, "nosmoke_cancer": 276},
    ]
    cfg = random.choice(pool)
    n_smoke_cancer = cfg["smoke_cancer"]
    n_smoke_nocancer = cfg["smoke_nocancer"]
    n_nosmoke_cancer = cfg["nosmoke_cancer"]
    n_nosmoke_nocancer = 10000 - (n_smoke_cancer + n_smoke_nocancer + n_nosmoke_cancer)
    
    total_cancer = n_smoke_cancer + n_nosmoke_cancer
    total_smoke = n_smoke_cancer + n_smoke_nocancer

    caudan = fr'''Khảo sát $10000$ người về mối liên hệ giữa hút thuốc lá và ung thư phổi được trình bày trong bảng sau:
\begin{{center}}
\begin{{tabular}}{{|c|c|c|}}
\hline
& Mắc ung thư phổi & Không mắc ung thư phổi \\
\hline
Hút thuốc lá & ${n_smoke_cancer}$ người & ${n_smoke_nocancer}$ người \\
\hline
Không hút thuốc lá & ${n_nosmoke_cancer}$ người & ${n_nosmoke_nocancer}$ người \\
\hline
\end{{tabular}}
\end{{center}}
Chọn ngẫu nhiên một người trong số $10000$ người được khảo sát.'''

    pct_cancer = total_cancer / 10000 * 100
    pct_smoke = total_smoke / 10000 * 100
    p_smoke_given_cancer = n_smoke_cancer / total_cancer * 100

    items = [
        (
            fr'''Xác suất để người đó bị ung thư phổi là ${pct_cancer:.1f}\%$.''',
            fr'''Xác suất để người đó bị ung thư phổi là ${pct_cancer * 2:.1f}\%$.''',
            fr'''Tổng số người ung thư phổi là ${total_cancer}$. Xác suất $P = \dfrac{{{total_cancer}}}{{10000}} = ${pct_cancer:.1f}\%$.''',
            fr'''$P = \dfrac{{{total_cancer}}}{{10000}} = ${pct_cancer:.1f}\% \ne ${pct_cancer * 2:.1f}\%$.'''
        ),
        (
            r'''Người hút thuốc lá có nguy cơ mắc ung thư phổi cao hơn người không hút thuốc lá.''',
            r'''Người hút thuốc lá có nguy cơ mắc ung thư phổi bằng người không hút thuốc lá.''',
            r'''Tỉ lệ ung thư ở nhóm hút thuốc cao vượt trội so với nhóm không hút thuốc.''',
            r'''Nguy cơ mắc bệnh ở nhóm hút thuốc cao gấp nhiều lần so với nhóm không hút thuốc.'''
        ),
        (
            fr'''Nếu người đó bị ung thư phổi thì xác suất người đó có hút thuốc lá lớn hơn $70\%$.''',
            r'''Nếu người đó bị ung thư phổi thì xác suất người đó hút thuốc lá nhỏ hơn $40\%$.''',
            fr'''$P(\text{{hút thuốc}}|\text{{ung thư}}) = \dfrac{{{n_smoke_cancer}}}{{{total_cancer}}} \approx {p_smoke_given_cancer:.1f}\% > 70\%$.''',
            fr'''$P(\text{{hút thuốc}}|\text{{ung thư}}) \approx {p_smoke_given_cancer:.1f}\% > 70\%$.'''
        ),
        (
            fr'''Xác suất để người đó là người hút thuốc lá bằng ${pct_smoke:.1f}\%$.''',
            fr'''Xác suất để người đó hút thuốc lá là ${pct_cancer:.1f}\%$.''',
            fr'''Tổng số người hút thuốc là ${total_smoke}$. Xác suất là $\dfrac{{{total_smoke}}}{{10000}} = ${pct_smoke:.1f}\%$.''',
            fr'''Tỉ lệ hút thuốc là ${pct_smoke:.1f}\%$, khẳng định ${pct_cancer:.1f}\%$ là sai.'''
        )
    ]
    choices, loi_giai = make_tf_choices(items)
    return caudan, choices, loi_giai


def CuoiChuong6_TF_Cau8():
    # Điểm môn Toán và đậu tốt nghiệp với phần trăm tròn đẹp
    cases = [
        {"p_above": 0.80, "p_pass_above": 0.90, "p_pass_below": 0.10},  # pass = 72% + 2% = 74%
        {"p_above": 0.70, "p_pass_above": 0.90, "p_pass_below": 0.10},  # pass = 63% + 3% = 66%
        {"p_above": 0.80, "p_pass_above": 0.95, "p_pass_below": 0.05},  # pass = 76% + 1% = 77%
        {"p_above": 0.75, "p_pass_above": 0.92, "p_pass_below": 0.08},  # pass = 69% + 2% = 71%
        {"p_above": 0.70, "p_pass_above": 0.90, "p_pass_below": 0.05},  # pass = 63% + 1.5% = 64.5%
    ]
    cfg = random.choice(cases)
    p_above = cfg["p_above"]
    p_pass_above = cfg["p_pass_above"]
    p_pass_below = cfg["p_pass_below"]
    
    p_below = round(1 - p_above, 2)
    p_both = round(p_above * p_pass_above, 3)
    p_pass_total = round(p_above * p_pass_above + p_below * p_pass_below, 4)
    p_above_given_pass = round(p_both / p_pass_total, 2)

    caudan = fr'''Thống kê ở một trường THPT cho thấy tỉ lệ học sinh đạt điểm trên trung bình môn Toán cả năm lớp 12 là ${int(p_above*100)}\%$. Xác suất đậu tốt nghiệp khi biết điểm trên trung bình là ${int(p_pass_above*100)}\%$ và khi biết điểm dưới trung bình là ${int(p_pass_below*100)}\%$. Chọn ngẫu nhiên một học sinh:'''

    items = [
        (
            fr'''Có ${int(p_below*100)}\%$ học sinh có điểm dưới trung bình môn Toán cả năm lớp 12.''',
            fr'''Có ${int(p_below*100 // 2)}\%$ học sinh có điểm dưới trung bình môn Toán cả năm lớp 12.''',
            fr'''Tỉ lệ học sinh điểm dưới trung bình là $100\% - ${int(p_above*100)}\% = ${int(p_below*100)}\%$.''',
            fr'''$100\% - ${int(p_above*100)}\% = ${int(p_below*100)}\%$.'''
        ),
        (
            fr'''Xác suất học sinh đó thi đậu tốt nghiệp và có điểm môn Toán trên trung bình là ${p_both}$.''',
            fr'''Xác suất học sinh đó thi đậu tốt nghiệp và có điểm môn Toán trên trung bình là $0,25$.''',
            fr'''$P(\text{{đậu}} \cap \text{{trên TB}}) = {p_above} \times {p_pass_above} = ${p_both}$.''',
            fr'''${p_above} \times {p_pass_above} = ${p_both} \ne 0,25$.'''
        ),
        (
            fr'''Xác suất đậu tốt nghiệp của học sinh đó bằng ${p_pass_total*100:.1f}\%$.''',
            r'''Xác suất đậu tốt nghiệp của học sinh đó là $95\%$.''',
            fr'''$P(\text{{đậu}}) = {p_above} \times {p_pass_above} + {p_below} \times {p_pass_below} = {p_pass_total} = ${p_pass_total*100:.1f}\%$.''',
            fr'''$P(\text{{đậu}}) = ${p_pass_total*100:.1f}\% \ne 95\%$.'''
        ),
        (
            fr'''Biết rằng học sinh đó đậu tốt nghiệp, xác suất học sinh đó có điểm trên trung bình môn Toán xấp xỉ ${p_above_given_pass:.2f}$.''',
            r'''Biết rằng học sinh đó đậu tốt nghiệp thì xác suất học sinh đó có điểm trên trung bình môn Toán là $0,30$.''',
            fr'''$P(\text{{trên TB}}|\text{{đậu}}) = \dfrac{{{p_both}}}{{{p_pass_total}}} \approx ${p_above_given_pass:.2f}$.''',
            fr'''$P(\text{{trên TB}}|\text{{đậu}}) \approx ${p_above_given_pass:.2f} \ne 0,30$.'''
        )
    ]
    choices, loi_giai = make_tf_choices(items)
    return caudan, choices, loi_giai
