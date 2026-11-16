# -*- coding: utf-8 -*-
"""
Module Đề thi thử / Đề ôn tập số 3 (12 câu Trắc nghiệm + 4 câu Đúng/Sai + 6 câu Trả lời ngắn)
Được xây dựng, chuẩn hóa và ngẫu nhiên hóa tham số tự động theo chuẩn đề tốt nghiệp THPT 2025.
Tất cả các phương án đều được loại bỏ dấu chấm cuối câu để tránh lỗi 2 dấu chấm (..) do gói ex_test tự sinh dấu chấm mặc định.
"""

import math
import random
from fractions import Fraction


def clean_option(s):
    if not isinstance(s, str):
        s = str(s)
    s = s.strip()
    # Loại bỏ nhãn trùng nếu có như a), b), c), d), A., B., C., D.
    for pfx in ['a)', 'b)', 'c)', 'd)', 'A.', 'B.', 'C.', 'D.', 'a.', 'b.', 'c.', 'd.']:
        if s.startswith(pfx):
            s = s[len(pfx):].strip()
    # Loại bỏ dấu chấm ở cuối phương án để gói ex_test tự thêm 1 dấu chấm mặc định duy nhất
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

def DeThiThu03_MC_Cau1():
    # Câu 1: Điểm cực tiểu của đồ thị hàm số bậc ba từ đồ thị
    configs = [
        {"x_cd": -1, "y_cd": 0, "x_ct": 1, "y_ct": -4, "formula": r"1*((\x)^3)+0*((\x)^2)+-3*(\x)+-2", "y0": -2},
        {"x_cd": -1, "y_cd": 4, "x_ct": 1, "y_ct": 0,  "formula": r"1*((\x)^3)+0*((\x)^2)+-3*(\x)+2",  "y0": 2},
        {"x_cd": -2, "y_cd": 2, "x_ct": 0, "y_ct": -2, "formula": r"1*((\x)^3)+3*((\x)^2)+0*(\x)+-2",  "y0": -2},
    ]
    c = random.choice(configs)
    x_ct, y_ct = c["x_ct"], c["y_ct"]
    x_cd, y_cd = c["x_cd"], c["y_cd"]

    caudan = fr'''\immini{{Cho hàm số $y = f(x)$ có đồ thị như hình vẽ. Điểm cực tiểu của đồ thị hàm số đã cho là
\begin{{center}}
\end{{center}}
}}{{
\begin{{tikzpicture}}[scale=0.7, line join=round, line cap=round, >=stealth] 
	\def\xmin{{-3}}\def\xmax{{3}}\def\ymin{{-5}}\def\ymax{{4}}
	\draw[->] (\xmin-0.2,0)--(\xmax+0.2,0) node[below]{{$x$}};
	\draw[->] (0,\ymin-0.2)--(0,\ymax+0.2) node[right]{{$y$}};
	\draw (0,0) node[below left]{{$O$}};
	\foreach \x in {{-2,-1,1,2}}\draw (\x,0.1)--(\x,-0.1) node[below]{{$\x$}};
	\foreach \y in {{-4,-2,2}}\draw (0.1,\y)--(-0.1,\y) node[left]{{$\y$}};
	\clip (\xmin,\ymin) rectangle (\xmax,\ymax);
	\draw[thick,smooth,samples=200,domain=\xmin:\xmax] plot (\x,{{{c["formula"]}}});
	\draw[dashed] (0,0)--(0,{c["y0"]})--({x_ct},{c["y0"]});\fill (0,{c["y0"]})circle(1.5pt);
	\draw[dashed] ({x_cd},0)--({x_cd},{y_cd})--(0,{y_cd});\fill ({x_cd},{y_cd})circle(1.5pt);
	\draw[dashed] ({x_ct},0)--({x_ct},{y_ct})--(0,{y_ct});\fill ({x_ct},{y_ct})circle(1.5pt);
\end{{tikzpicture}}
}}'''
    correct = fr"$({x_ct}; {y_ct})$"
    wrongs = [
        fr"$({x_cd}; {y_cd})$",
        fr"$({x_ct}; 0)$",
        fr"$(0; {y_ct})$"
    ]
    choices = shuffle_choices(correct, wrongs)
    loi_giai = fr'''Dựa vào đồ thị, điểm thấp nhất trong lân cận tương ứng với điểm cực tiểu của đồ thị hàm số là $({x_ct}; {y_ct})$.'''
    return caudan, choices, loi_giai


def DeThiThu03_MC_Cau2():
    # Câu 2: Nguyên hàm của hàm lũy thừa y = x^n
    n = random.choice([2, 3, 4, 5, 6, 7])
    n1 = n + 1
    caudan = fr'''Cho hàm số $y = f(x)$ là một nguyên hàm của hàm số $y = x^{n}$. Phát biểu nào sau đây là đúng?'''
    correct = fr"$f(x) = \dfrac{{x^{{{n1}}}}}{{{n1}}}$"
    wrongs = [
        fr"$f(x) = {n}x^{{{n-1}}}$",
        fr"$f(x) = {n1}x^{{{n}}}$",
        fr"$f(x) = \dfrac{{x^{{{n}}}}}{{{n}}}$"
    ]
    choices = shuffle_choices(correct, wrongs)
    loi_giai = fr'''Theo công thức nguyên hàm cơ bản: $\displaystyle\int x^{n}\,\mathrm{{d}}x = \dfrac{{x^{{{n1}}}}}{{{n1}}} + C$. Do đó một nguyên hàm của hàm số là $f(x) = \dfrac{{x^{{{n1}}}}}{{{n1}}}$.'''
    return caudan, choices, loi_giai


def DeThiThu03_MC_Cau3():
    # Câu 3: Phương trình tổng quát của mặt phẳng trong Oxyz
    A, B, C = random.choice([(2, 1, 1), (1, 2, 3), (3, -1, 2), (2, -2, 1), (1, 1, 1)])
    D = random.choice([1, 2, 3, 4, 5])
    
    caudan = r'''Trong không gian với hệ toạ độ $Oxyz$, phương trình nào sau đây là phương trình tổng quát của mặt phẳng?'''
    correct = fr"${A}x + {B}y + {C}z + {D} = 0$"
    wrongs = [
        fr"${A}x + {B}y^2 + {C}z + {D} = 0$",
        fr"${A}x^2 + {B}y + {C}z + {D+1} = 0$",
        fr"${A}x + {B}y + {C}z^2 + {D+2} = 0$"
    ]
    choices = shuffle_choices(correct, wrongs)
    loi_giai = fr'''Phương trình tổng quát của mặt phẳng trong không gian $Oxyz$ là phương trình bậc nhất có dạng $Ax + By + Cz + D = 0$ với $A^2 + B^2 + C^2 > 0$. Vậy phương trình mặt phẳng là ${A}x + {B}y + {C}z + {D} = 0$.'''
    return caudan, choices, loi_giai


def DeThiThu03_MC_Cau4():
    # Câu 4: Tiệm cận ngang của hàm phân thức bậc nhất trên bậc nhất từ đồ thị
    presets = [
        {"a": -1, "b": 2, "c": 1, "d": 1, "tcn": -1, "tcd": -1, "formula": r"(-1*(\x)+2)/(1*(\x)+1)"},
        {"a": 1,  "b": 2, "c": 1, "d": -1, "tcn": 1,  "tcd": 1,  "formula": r"(1*(\x)+2)/(1*(\x)-1)"},
        {"a": 2,  "b": -1, "c": 1, "d": 1, "tcn": 2,  "tcd": -1, "formula": r"(2*(\x)-1)/(1*(\x)+1)"},
        {"a": -2, "b": 1, "c": 1, "d": -1, "tcn": -2, "tcd": 1,  "formula": r"(-2*(\x)+1)/(1*(\x)-1)"},
    ]
    p = random.choice(presets)
    tcn, tcd = p["tcn"], p["tcd"]

    caudan = fr'''\immini{{Cho hàm số $y = f(x)$ có đồ thị như vẽ bên. Đường thẳng nào sau đây là đường tiệm cận ngang của đồ thị hàm số đã cho?
\begin{{center}}
\end{{center}}
}}{{
\begin{{tikzpicture}}[font=\footnotesize,scale=0.5, line join=round, line cap=round, >=stealth]
	\def\xmin{{-4}}\def\xmax{{4}}\def\ymin{{-4}}\def\ymax{{4}}
	\draw[->] (\xmin-0.2,0)--(\xmax+0.2,0) node[below]{{$x$}};
	\draw[->] (0,\ymin-0.2)--(0,\ymax+0.2) node[right]{{$y$}};
	\draw (0,0) node[below left]{{$O$}};
	\foreach \x in {{-3,-2,-1,1,2,3}}\draw (\x,0.1)--(\x,-0.1) node[below]{{$\x$}};
	\foreach \y in {{-3,-2,-1,1,2,3}}\draw (0.1,\y)--(-0.1,\y) node[left]{{$\y$}};
	\clip (\xmin,\ymin) rectangle (\xmax,\ymax);
	\draw[dashed] (\xmin,{tcn})--(\xmax,{tcn});
	\draw[dashed] ({tcd},\ymin)--({tcd},\ymax);
	\draw[thick,smooth,samples=200,domain=\xmin:{tcd-0.1}] plot (\x,{{{p["formula"]}}});
	\draw[thick,smooth,samples=200,domain={tcd+0.1}:\xmax] plot (\x,{{{p["formula"]}}});
\end{{tikzpicture}}
}}'''
    correct = fr"$y = {tcn}$"
    wrongs = [
        fr"$x = {tcd}$",
        fr"$x = {-tcd}$",
        fr"$y = {-tcn}$"
    ]
    choices = shuffle_choices(correct, wrongs)
    loi_giai = fr'''Dựa vào đồ thị, khi $x \to \pm\infty$ thì $y \to {tcn}$. Do đó đường thẳng $y = {tcn}$ là tiệm cận ngang của đồ thị hàm số.'''
    return caudan, choices, loi_giai


def DeThiThu03_MC_Cau5():
    # Câu 5: Phương sai và độ lệch chuẩn của mẫu số liệu ghép nhóm
    s = random.choice([2, 3, 4, 5, 6, 7, 8, 9, 10])
    s2 = s**2

    caudan = fr'''Xét mẫu số liệu ghép nhóm có phương sai bằng ${s2}$. Độ lệch chuẩn của mẫu số liệu đó bằng'''
    correct = fr"${s}$"
    wrongs = [
        fr"${2 * s2}$",
        fr"${s + 2}$",
        fr"${s2**2}$"
    ]
    choices = shuffle_choices(correct, wrongs)
    loi_giai = fr'''Độ lệch chuẩn $s$ là căn bậc hai số học của phương sai: $s = \sqrt{{s^2}} = \sqrt{{{s2}}} = {s}$.'''
    return caudan, choices, loi_giai


def DeThiThu03_MC_Cau6():
    # Câu 6: Tính độ pH của dung dịch
    solutions = [
        {"name": "một loại sữa", "val": "6,8", "exp": 6.8},
        {"name": "nước chanh", "val": "2,4", "exp": 2.4},
        {"name": "cà phê đen", "val": "5,0", "exp": 5.0},
        {"name": "nước biển", "val": "8,1", "exp": 8.1},
        {"name": "nước khoáng", "val": "7,2", "exp": 7.2},
    ]
    sol = random.choice(solutions)
    val = sol["val"]

    caudan = fr'''Chỉ số pH của một dung dịch được tính theo công thức $\mathrm{{pH}} = -\log[H^+]$ với $[H^+]$ là nồng độ ion hydro. Độ pH của {sol["name"]} có $[H^+] = 10^{{-{val}}}$ là bao nhiêu?'''
    correct = fr"${val}$"
    wrongs = [
        fr"${val.replace(',', '')}$",
        fr"${'0,' + val.replace(',', '')}$",
        fr"${val + '0'}$"
    ]
    choices = shuffle_choices(correct, wrongs)
    loi_giai = fr'''Áp dụng công thức: $\mathrm{{pH}} = -\log(10^{{-{val}}}) = -(-{val}) = {val}$.'''
    return caudan, choices, loi_giai


def DeThiThu03_MC_Cau7():
    # Câu 7: Phương trình mặt cầu trong không gian Oxyz
    a = random.choice([1, 2, 3, 5, 9])
    b = random.choice([2, 4, 6, 8, 10])
    c = random.choice([3, 5, 7, 11, 12])
    R = random.choice([4, 5, 7, 12, 13])

    caudan = r'''Trong không gian với hệ toạ độ $Oxyz$, phương trình nào sau đây là phương trình mặt cầu?'''
    correct = fr"$(x - {a})^2 + (y - {b})^2 + (z - {c})^2 = {R}^2$"
    wrongs = [
        fr"$(x^2 - {a})^2 + (y - {b})^2 + (z - {c})^2 = {R}^2$",
        fr"$(x - {a})^2 + (y^2 - {b})^2 + (z - {c})^2 = {R}^2$",
        fr"$(x - {a})^2 + (y - {b})^2 + (z - {c})^2 = -{R}^2$"
    ]
    choices = shuffle_choices(fr"${correct}$", [fr"${w}$" for w in wrongs])
    loi_giai = fr'''Phương trình mặt cầu tâm $I(a; b; c)$, bán kính $R$ có dạng $(x - a)^2 + (y - b)^2 + (z - c)^2 = R^2$. Vậy phương trình đúng là $(x - {a})^2 + (y - {b})^2 + (z - {c})^2 = {R}^2$.'''
    return caudan, choices, loi_giai


def DeThiThu03_MC_Cau8():
    # Câu 8: Phương trình chính tắc của đường thẳng trong Oxyz
    x0 = random.randint(1, 9)
    y0 = random.randint(1, 9)
    z0 = random.randint(1, 9)
    a = random.choice([2, 3, 5, 7])
    b = random.choice([2, 4, 5, 6])
    c = random.choice([3, 4, 7, 8])

    caudan = r'''Trong không gian với hệ toạ độ $Oxyz$, phương trình nào sau đây là phương trình chính tắc của đường thẳng?'''
    correct = fr"\dfrac{{x - {x0}}}{{{a}}} = \dfrac{{y - {y0}}}{{{b}}} = \dfrac{{z - {z0}}}{{{c}}}"
    wrongs = [
        fr"\dfrac{{x - {x0}}}{{{a}}} + \dfrac{{y - {y0}}}{{{b}}} + \dfrac{{z - {z0}}}{{{c}}} = 1",
        fr"\dfrac{{x^2 - {x0}}}{{{a}}} = \dfrac{{y - {y0}}}{{{b}}} = \dfrac{{z - {z0}}}{{{c}}}",
        fr"\dfrac{{x - {x0}}}{{{a}}} = \dfrac{{y - {y0}}}{{{b}}} = {c}"
    ]
    choices = shuffle_choices(fr"${correct}$", [fr"${w}$" for w in wrongs])
    loi_giai = fr'''Phương trình chính tắc của đường thẳng đi qua điểm $(x_0; y_0; z_0)$ có vectơ chỉ phương $(a; b; c)$ ($a, b, c \ne 0$) là: $\dfrac{{x - x_0}}{{a}} = \dfrac{{y - y_0}}{{b}} = \dfrac{{z - z_0}}{{c}}$.'''
    return caudan, choices, loi_giai


def DeThiThu03_MC_Cau9():
    # Câu 9: Định nghĩa xác suất có điều kiện P(A|B)
    caudan = r'''Cho hai biến cố $A$ và $B$. Xác suất của biến cố $A$ với điều kiện biến cố $B$ đã xảy ra được gọi là xác suất của $A$ với điều kiện $B$, kí hiệu là $\mathrm{P}(A|B)$. Phát biểu nào sau đây là đúng?'''
    correct = r'''Nếu $\mathrm{P}(B) > 0$ thì $\mathrm{P}(A|B) = \dfrac{\mathrm{P}(A\cap B)}{\mathrm{P}(B)}$'''
    wrongs = [
        r'''$\mathrm{P}(A|B) = \dfrac{\mathrm{P}(A\cap B)}{\mathrm{P}(A)}$''',
        r'''Nếu $\mathrm{P}(B) > 0$ thì $\mathrm{P}(A|B) = \dfrac{\mathrm{P}(A)}{\mathrm{P}(B)}$''',
        r'''Nếu $\mathrm{P}(A\cap B) > 0$ thì $\mathrm{P}(A|B) = \dfrac{\mathrm{P}(B)}{\mathrm{P}(A\cap B)}$'''
    ]
    choices = shuffle_choices(correct, wrongs)
    loi_giai = r'''Theo định nghĩa xác suất có điều kiện: với $\mathrm{P}(B) > 0$, ta có $\mathrm{P}(A|B) = \dfrac{\mathrm{P}(A\cap B)}{\mathrm{P}(B)}$.'''
    return caudan, choices, loi_giai


def DeThiThu03_MC_Cau10():
    # Câu 10: Khoảng biến thiên của mẫu số liệu ghép nhóm
    caudan = r'''\immini{Xét mẫu số liệu ghép nhóm cho bởi bảng bên. Khoảng biến thiên của mẫu số liệu ghép nhóm đó bằng
\begin{center}
\end{center}
}{
\begin{tabular}{|c|c|}
	\hline
	\textbf{Nhóm} & \textbf{Tần số} \\
	\hline
	$[a_1; a_2)$ & $n_1$ \\
	$[a_2; a_3)$ & $n_2$ \\
	$\cdots$ & $\cdots$ \\
	$[a_m; a_{m+1})$ & $n_m$ \\
	\hline
	& $n$ \\
	\hline
\end{tabular}
}'''
    correct = r'''$a_{m+1} - a_1$'''
    wrongs = [
        r'''$a_{m+1} - a_m$''',
        r'''$n_m - n_1$''',
        r'''$n - n_m$'''
    ]
    choices = shuffle_choices(correct, wrongs)
    loi_giai = r'''Khoảng biến thiên của mẫu số liệu ghép nhóm là hiệu số giữa đầu mút phải của nhóm cuối cùng và đầu mút trái của nhóm đầu tiên: $R = a_{m+1} - a_1$.'''
    return caudan, choices, loi_giai


def DeThiThu03_MC_Cau11():
    # Câu 11: Khoảng tứ phân vị của mẫu số liệu ghép nhóm
    caudan = r'''Xét mẫu số liệu ghép nhóm có tứ phân vị thứ nhất, tứ phân vị thứ hai, tứ phân vị thứ ba lần lượt là $Q_1$, $Q_2$ và $Q_3$. Khoảng tứ phân vị của mẫu số liệu ghép nhóm đó bằng'''
    correct = r'''$Q_3 - Q_1$'''
    wrongs = [
        r'''$Q_2 - Q_1$''',
        r'''$Q_3 - Q_2$''',
        r'''$Q_3 - 2Q_2 + Q_1$'''
    ]
    choices = shuffle_choices(correct, wrongs)
    loi_giai = r'''Khoảng tứ phân vị của mẫu số liệu ghép nhóm là $\Delta_Q = Q_3 - Q_1$.'''
    return caudan, choices, loi_giai


def DeThiThu03_MC_Cau12():
    # Câu 12: Thể tích khối tròn xoay quanh trục Ox
    caudan = r'''Cho hàm số $y = f(x)$ liên tục, không âm trên đoạn $[a; b]$. Hình phẳng $(H)$ giới hạn bởi đồ thị hàm số $y = f(x)$, trục hoành và hai đường thẳng $x = a$, $x = b$ quay quanh trục $Ox$ tạo thành một khối tròn xoay có thể tích bằng'''
    correct = r'''$V = \pi \displaystyle\int\limits_a^b [f(x)]^2\,\mathrm{d}x$'''
    wrongs = [
        r'''$V = \displaystyle\int\limits_a^b [f(x)]^2\,\mathrm{d}x$''',
        r'''$V = \pi \displaystyle\int\limits_b^a [f(x)]^2\,\mathrm{d}x$''',
        r'''$V = \pi \displaystyle\int\limits_a^b f(x)\,\mathrm{d}x$'''
    ]
    choices = shuffle_choices(correct, wrongs)
    loi_giai = r'''Công thức tính thể tích khối tròn xoay khi quay hình phẳng giới hạn bởi đồ thị $y = f(x)$, $y = 0$, $x = a$, $x = b$ quanh trục $Ox$ là $V = \pi \displaystyle\int\limits_a^b [f(x)]^2\,\mathrm{d}x$.'''
    return caudan, choices, loi_giai


# ==============================================================================
# PHẦN II: 4 CÂU TRẮC NGHIỆM ĐÚNG / SAI (TF)
# ==============================================================================

def DeThiThu03_TF_Cau1():
    # Câu 1: Hai đường thẳng trong không gian Oxyz
    line_pairs = [
        {
            "M1": (1, 2, 3), "u1": (2, 1, -2),
            "M2": (4, 5, 6), "u2": (-1, -2, 2),
            "cos_val": "-8/9", "cos_frac": Fraction(-8, 9), "angle_deg": 27
        },
        {
            "M1": (2, 1, -1), "u1": (1, 2, 2),
            "M2": (3, 0, 4),  "u2": (2, -2, 1),
            "cos_val": "0",    "cos_frac": Fraction(0, 1),  "angle_deg": 90
        },
        {
            "M1": (-1, 3, 2), "u1": (3, 0, 4),
            "M2": (1, 1, 0),  "u2": (4, 3, 0),
            "cos_val": "12/25", "cos_frac": Fraction(12, 25), "angle_deg": 61
        },
    ]
    cfg = random.choice(line_pairs)
    x1, y1, z1 = cfg["M1"]
    a1, b1, c1 = cfg["u1"]
    x2, y2, z2 = cfg["M2"]
    a2, b2, c2 = cfg["u2"]
    deg = cfg["angle_deg"]

    caudan = fr'''Trong không gian toạ độ $Oxyz$, cho hai đường thẳng $\Delta_1 \colon \dfrac{{x - {x1}}}{{{a1}}} = \dfrac{{y - {y1}}}{{{b1}}} = \dfrac{{z - {z1}}}{{{c1}}}$ và $\Delta_2 \colon \dfrac{{x - {x2}}}{{{a2}}} = \dfrac{{y - {y2}}}{{{b2}}} = \dfrac{{z - {z2}}}{{{c2}}}$.'''

    items = [
        (
            fr'''Vectơ có toạ độ $({a1}; {b1}; {c1})$ là một vectơ chỉ phương của $\Delta_1''',
            fr'''Vectơ có toạ độ $({x1}; {y1}; {z1})$ là một vectơ chỉ phương của $\Delta_1''',
            fr'''Từ phương trình chính tắc của $\Delta_1$, các hệ số ở mẫu là $({a1}; {b1}; {c1})$ là một VTCP.''',
            fr'''Tọa độ $({x1}; {y1}; {z1})$ là tọa độ một điểm thuộc $\Delta_1$, không phải VTCP.'''
        ),
        (
            fr'''Vectơ có toạ độ $({a2}; {b2}; {c2})$ là một vectơ chỉ phương của $\Delta_2''',
            fr'''Vectơ có toạ độ $({x2}; {y2}; {z2})$ là một vectơ chỉ phương của $\Delta_2''',
            fr'''Từ phương trình chính tắc của $\Delta_2$, các hệ số ở mẫu là $({a2}; {b2}; {c2})$ là một VTCP.''',
            fr'''Tọa độ $({x2}; {y2}; {z2})$ là tọa độ một điểm thuộc $\Delta_2$, không phải VTCP.'''
        ),
        (
            fr'''Côsin của góc giữa hai vectơ $\vec{{u}}_1 = ({a1}; {b1}; {c1})$ và $\vec{{u}}_2 = ({a2}; {b2}; {c2})$ bằng $\dfrac{{{cfg["cos_frac"].numerator}}}{{{cfg["cos_frac"].denominator}}}''',
            fr'''Côsin của góc giữa hai vectơ $\vec{{u}}_1$ và $\vec{{u}}_2$ bằng $\dfrac{{{abs(cfg["cos_frac"].numerator) + 1}}}{{{cfg["cos_frac"].denominator}}}''',
            fr'''$\cos(\vec{{u}}_1, \vec{{u}}_2) = \dfrac{{{a1}({a2}) + {b1}({b2}) + {c1}({c2})}}{{\sqrt{{{a1}^2+{b1}^2+{c1}^2}} \cdot \sqrt{{{a2}^2+{b2}^2+{c2}^2}}}} = \dfrac{{{cfg["cos_frac"].numerator}}}{{{cfg["cos_frac"].denominator}}}$.''',
            fr'''Giá trị tính theo công thức tích vô hướng chia tích độ dài là $\dfrac{{{cfg["cos_frac"].numerator}}}{{{cfg["cos_frac"].denominator}}}$.'''
        ),
        (
            fr'''Góc giữa hai đường thẳng $\Delta_1$ và $\Delta_2$ (làm tròn kết quả đến hàng đơn vị của độ) bằng ${deg}^\circ''',
            fr'''Góc giữa hai đường thẳng $\Delta_1$ và $\Delta_2$ bằng ${180 - deg}^\circ''',
            fr'''Góc giữa hai đường thẳng luôn là góc không tù ($\le 90^\circ$): $\cos \varphi = |\cos(\vec{{u}}_1, \vec{{u}}_2)| = \left|\dfrac{{{cfg["cos_frac"].numerator}}}{{{cfg["cos_frac"].denominator}}}\right| \implies \varphi \approx {deg}^\circ$.''',
            fr'''Góc giữa hai đường thẳng không thể vượt quá $90^\circ$, khẳng định ${180 - deg}^\circ$ là sai.'''
        )
    ]
    choices, loi_giai = make_tf_choices(items)
    return caudan, choices, loi_giai


def DeThiThu03_TF_Cau2():
    # Câu 2: Bể chứa nước lưu lượng bơm và rò rỉ
    presets = [
        {"a": 6, "b": 3, "c": 2, "V_max": 2015, "t_stop": 30, "t_test": 5, "V_in_test": 90, "V_out_test": 25, "V_full": 31, "V_out_full": 961},
        {"a": 8, "b": 4, "c": 2, "V_max": 2500, "t_stop": 25, "t_test": 5, "V_in_test": 120, "V_out_test": 25, "V_full": 28, "V_out_full": 784},
        {"a": 5, "b": 2, "c": 1, "V_max": 1800, "t_stop": 28, "t_test": 5, "V_in_test": 72.5, "V_out_test": 12.5, "V_full": 30, "V_out_full": 900},
    ]
    p = random.choice(presets)
    a, b, c = p["a"], p["b"], p["c"]
    V_max = p["V_max"]
    t_stop = p["t_stop"]
    t_test = p["t_test"]
    V_in_test = int(p["V_in_test"])
    V_out_test = int(p["V_out_test"])
    V_out_full = p["V_out_full"]

    alpha = (a - c) // 2
    V_stop = alpha * (t_stop**2) + b * t_stop

    caudan = fr'''Cho một bể chứa nước ban đầu chưa có nước. Người ta bắt đầu bơm nước vào bể với lưu lượng là $L_1(t) = {a}t + {b}$ (lít/phút). Cùng lúc đó, do bể có một vết nứt dưới đáy nên nước bị chảy ra ngoài với lưu lượng là $L_2(t) = {c}t$ (lít/phút). Dung tích tối đa của bể là ${V_max}$ lít.'''

    items = [
        (
            fr'''Nếu bơm được ${t_stop}$ phút thì dừng, lượng nước trong bể vẫn chưa đầy bể''',
            fr'''Nếu bơm được ${t_stop}$ phút thì dừng, lượng nước trong bể đã làm tràn bể''',
            fr'''Lượng nước sau ${t_stop}$ phút là $V({t_stop}) = \displaystyle\int_0^{{{t_stop}}} ({a - c}t + {b})\,\mathrm{{d}}t = {alpha}({t_stop})^2 + {b}({t_stop}) = {V_stop}\text{{ lít}} < {V_max}\text{{ lít}}$.''',
            fr'''$V({t_stop}) = {V_stop}\text{{ lít}} < {V_max}\text{{ lít}}$ nên bể chưa đầy.'''
        ),
        (
            fr'''Thể tích nước được bơm vào bể trong ${t_test}$ phút đầu tiên là ${V_in_test}$ lít''',
            fr'''Thể tích nước được bơm vào bể trong ${t_test}$ phút đầu tiên là ${V_in_test + 30}$ lít''',
            fr'''$\displaystyle\int_0^{{{t_test}}} ({a}t + {b})\,\mathrm{{d}}t = \left.\left(\dfrac{{{a}t^2}}{{2}} + {b}t\right)\right|_0^{{{t_test}}} = \dfrac{{{a}}}{{2}}({t_test}^2) + {b}({t_test}) = {V_in_test}\text{{ lít}}$.''',
            fr'''Thể tích bơm vào là ${V_in_test}\text{{ lít}} \ne {V_in_test + 30}\text{{ lít}}$.'''
        ),
        (
            fr'''Thể tích nước chảy ra từ bể trong ${t_test}$ phút đầu tiên là ${V_out_test}$ lít''',
            fr'''Thể tích nước chảy ra từ bể trong ${t_test}$ phút đầu tiên là ${V_out_test - 15}$ lít''',
            fr'''$\displaystyle\int_0^{{{t_test}}} {c}t\,\mathrm{{d}}t = \left.\dfrac{{{c}t^2}}{{2}}\right|_0^{{{t_test}}} = {V_out_test}\text{{ lít}}$.''',
            fr'''Thể tích chảy ra là ${V_out_test}\text{{ lít}} \ne ${V_out_test - 15}\text{{ lít}}$.'''
        ),
        (
            fr'''Khi nước chảy vào vừa làm đầy bể, đã có nhiều hơn ${V_out_full - 50}$ lít nước bị chảy ra ngoài''',
            fr'''Khi nước chảy vào vừa làm đầy bể, chỉ có ít hơn $500$ lít nước bị chảy ra ngoài''',
            fr'''Bể đầy khi ${alpha}t^2 + {b}t = {V_max} \implies t \approx {p["V_full"]}$ phút. Lượng nước rò rỉ là $\displaystyle\int_0^{{t}} {c}u\,\mathrm{{d}}u \approx {V_out_full}\text{{ lít}} > {V_out_full - 50}\text{{ lít}}$.''',
            fr'''Lượng nước rò rỉ xấp xỉ ${V_out_full}\text{{ lít}}$, khẳng định ít hơn $500$ lít là sai.'''
        )
    ]
    choices, loi_giai = make_tf_choices(items)
    return caudan, choices, loi_giai


def DeThiThu03_TF_Cau3():
    # Câu 3: Diện tích bề mặt Trái Đất nhìn thấy từ vệ tinh ở độ cao h
    R = 6370
    h_cases = [
        {"h": 280,  "pct_str": "2,1%", "wrong_pct": "2,5%", "k_val": "2/95"},
        {"h": 400,  "pct_str": "3,0%", "wrong_pct": "3,5%", "k_val": "20/677"},
        {"h": 500,  "pct_str": "3,6%", "wrong_pct": "4,2%", "k_val": "25/687"},
    ]
    c = random.choice(h_cases)
    h0 = c["h"]

    caudan = fr'''\immini{{Ta coi Trái Đất là hình cầu hoàn hảo với bán kính $R = {R}\text{{ km}}$ và diện tích toàn phần là $S = 4\pi R^2$. Các phi hành gia từ tàu vũ trụ chỉ có thể nhìn thấy một phần bề mặt Trái Đất. Ở độ cao $h$, phần diện tích Trái Đất các phi hành gia có thể nhìn thấy được tính theo công thức $S_T = 2\pi R^2\left(1 - \dfrac{{R}}{{R + h}}\right)$, trong đó $R$ là bán kính Trái Đất. Gọi $K$ là tỉ số diện tích bề mặt Trái Đất nhìn thấy được ở độ cao $h$ với diện tích toàn phần của Trái Đất.}}{{
\begin{{tikzpicture}}[scale=0.7]
	\draw[ball color=blue!80!black] (1.12,1.34) circle (1.8);
	\draw[red,dashed] (0.5,-1.5) arc (-90:90:1.8cm);
	\fill (3.5, 1.34) circle (2pt) node[right]{{\footnotesize Vệ tinh ($h$)}};
\end{{tikzpicture}}
}}'''

    items = [
        (
            r'''Công thức tính $K$ là $K = \dfrac{1}{2} \cdot \dfrac{h}{R + h}''',
            r'''Công thức tính $K$ là $K = \dfrac{1}{2}\left(1 - \dfrac{h}{R + h}\right)''',
            r'''$K = \dfrac{S_T}{S} = \dfrac{2\pi R^2\left(1 - \dfrac{R}{R+h}\right)}{4\pi R^2} = \dfrac{1}{2} \cdot \dfrac{h}{R + h}$.''',
            r'''$K = \dfrac{1}{2} \cdot \dfrac{h}{R + h} \ne \dfrac{1}{2}\left(1 - \dfrac{h}{R+h}\right)$.'''
        ),
        (
            fr'''Ở độ cao $h = {h0}\text{{ km}}$, có khoảng ${c["pct_str"]}$ (làm tròn kết quả đến hàng phần mười) diện tích bề mặt Trái Đất có thể nhìn thấy''',
            fr'''Ở độ cao $h = {h0}\text{{ km}}$, có khoảng ${c["wrong_pct"]}$ diện tích bề mặt Trái Đất có thể nhìn thấy''',
            fr'''Thay $R = {R}, h = {h0} \implies K = \dfrac{1}{2} \cdot \dfrac{{{h0}}}{{{R + h0}}} \approx {c["pct_str"]}$.''',
            fr'''Tỉ lệ tính được là khoảng ${c["pct_str"]} \ne {c["wrong_pct"]}$.'''
        ),
        (
            fr'''Muốn nhìn thấy $\dfrac{{1}}{{4}}$ diện tích bề mặt Trái Đất, cần đưa tàu vũ trụ đạt đến độ cao đúng bằng ${R}\text{{ km}}''',
            fr'''Muốn nhìn thấy $\dfrac{{1}}{{4}}$ diện tích bề mặt Trái Đất, cần đưa tàu vũ trụ đạt đến độ cao ${R + 100}\text{{ km}}''',
            fr'''$K = \dfrac{{1}}{{4}} \iff \dfrac{{1}}{{2}} \cdot \dfrac{{h}}{{R + h}} = \dfrac{{1}}{{4}} \iff \dfrac{{h}}{{R + h}} = \dfrac{{1}}{{2}} \iff h = R = {R}\text{{ km}}$.''',
            fr'''Độ cao cần thiết chính xác là $h = R = {R}\text{{ km}} \ne {R + 100}\text{{ km}}$.'''
        ),
        (
            r'''Khi độ cao $h$ càng tăng lên thì $K$ càng tăng nhưng không vượt quá $50\%$''',
            r'''Khi độ cao $h$ đủ lớn, phi hành gia có thể nhìn thấy toàn bộ $100\%$ bề mặt Trái Đất''',
            r'''$\lim\limits_{h \to +\infty} K = \lim\limits_{h \to +\infty} \dfrac{1}{2}\cdot\dfrac{h}{R+h} = \dfrac{1}{2} = 50\%$. Do Trái Đất hình cầu nên từ một điểm bên ngoài không thể nhìn thấy quá $50\%$ diện tích.''',
            r'''Góc nhìn từ một điểm ngoài hình cầu luôn bị giới hạn bởi tiếp tuyến nên diện tích nhìn thấy tối đa không vượt quá nửa hình cầu ($50\%$).'''
        )
    ]
    choices, loi_giai = make_tf_choices(items)
    return caudan, choices, loi_giai


def DeThiThu03_TF_Cau4():
    # Câu 4: Hình ảnh laptop đang mở - Góc nhị diện
    laptop_cfgs = [
        {"L": 30, "BC_tex": r"30\sqrt{3}", "cos_val": r"-\dfrac{1}{2}", "deg": 120},
        {"L": 30, "BC_tex": r"30\sqrt{2}", "cos_val": r"0",             "deg": 90},
        {"L": 30, "BC_tex": r"30",         "cos_val": r"\dfrac{1}{2}",  "deg": 60},
        {"L": 25, "BC_tex": r"25\sqrt{3}", "cos_val": r"-\dfrac{1}{2}", "deg": 120},
    ]
    cfg = random.choice(laptop_cfgs)
    L = cfg["L"]
    BC_tex = cfg["BC_tex"]
    cos_val = cfg["cos_val"]
    deg = cfg["deg"]

    caudan = fr'''\immini{{Hình ảnh máy tính xách tay đang mở ở hình vẽ bên gợi nên góc nhị diện và số đo góc $BAC$ được gọi là độ mở của máy tính. Giả sử màn hình và bàn phím có kích thước cạnh tương ứng là $AB = AC = {L}\,\text{{cm}}$.}}{{
\begin{{tikzpicture}}[scale=0.7]
	\coordinate (A) at (0,0);\coordinate (B) at (-1,3.5);\coordinate (D) at (3.5,5);\coordinate (D') at (4.5,1.5);
	\coordinate (C) at (3.5,-1);\coordinate (D'') at (8,0.8);
	\fill[black!60] (A)node[below]{{$B$}}--(B)node[above]{{$A$}}--(D)--(D');
	\draw(A)--(B)--(D)--(D');
	\fill[teal!60] (A)--(C)node[below]{{$C$}}--(D'')--(D');
	\draw (A)--(C)--(D'')--(D');
	\draw[red,thick] (B)--(A)--(C)--cycle;
\end{{tikzpicture}}
}}'''

    items = [
        (
            r'''Hệ thức định lí côsin trong tam giác $ABC$ là $\cos\widehat{BAC} = \dfrac{AB^2 + AC^2 - BC^2}{2AB \cdot AC}$''',
            r'''Hệ thức định lí côsin trong tam giác $ABC$ là $\cos\widehat{BAC} = \dfrac{AB^2 + BC^2 - AC^2}{2AB \cdot BC}$''',
            r'''Theo định lí côsin trong tam giác $ABC$: $BC^2 = AB^2 + AC^2 - 2AB \cdot AC \cos\widehat{BAC} \implies \cos\widehat{BAC} = \dfrac{AB^2 + AC^2 - BC^2}{2AB \cdot AC}$.''',
            r'''Công thức đúng là $\cos\widehat{BAC} = \dfrac{AB^2 + AC^2 - BC^2}{2AB \cdot AC}$.'''
        ),
        (
            fr'''Nếu $BC = {BC_tex}\,\text{{cm}}$ thì $\cos\widehat{{BAC}} = {cos_val}$''',
            fr'''Nếu $BC = {BC_tex}\,\text{{cm}}$ thì $\cos\widehat{{BAC}} = \dfrac{{1}}{{4}}$''',
            fr'''Thay $AB = AC = {L}$ và $BC = {BC_tex}$ vào định lí côsin ta được $\cos\widehat{{BAC}} = {cos_val}$.''',
            fr'''Kết quả tính toán là $\cos\widehat{{BAC}} = {cos_val} \ne \dfrac{{1}}{{4}}$.'''
        ),
        (
            r'''Nếu $\cos\widehat{BAC} = \dfrac{1}{2}$ thì số đo góc $BAC$ bằng $60^\circ$''',
            r'''Nếu $\cos\widehat{BAC} = \dfrac{1}{2}$ thì số đo góc $BAC$ bằng $120^\circ$''',
            r'''Trong tam giác: $\cos\widehat{BAC} = \dfrac{1}{2} \implies \widehat{BAC} = 60^\circ$.''',
            r'''$\arccos(1/2) = 60^\circ \ne 120^\circ$.'''
        ),
        (
            fr'''Độ mở của máy tính là ${deg}^\circ$ khi $BC = {BC_tex}\,\text{{cm}}$''',
            fr'''Độ mở của máy tính là ${180 - deg if deg!=90 else 45}^\circ$ khi $BC = {BC_tex}\,\text{{cm}}$''',
            fr'''Với $\cos\widehat{{BAC}} = {cos_val}$, ta có $\widehat{{BAC}} = {deg}^\circ$, do đó độ mở của máy tính là ${deg}^\circ$.''',
            fr'''Độ mở tương ứng chính xác là ${deg}^\circ$.'''
        )
    ]
    choices, loi_giai = make_tf_choices(items)
    return caudan, choices, loi_giai


# ==============================================================================
# PHẦN III: 6 CÂU TRẢ LỜI NGẮN (SA)
# ==============================================================================

def DeThiThu03_SA_Cau1():
    # Câu 1: Khoảng cách từ vị trí đến nguồn âm trong Oxyz (bộ số Pytago nguyên đẹp)
    triplets = [
        (4, 6, 12, 14),
        (3, 4, 12, 13),
        (2, 3, 6, 7),
        (1, 4, 8, 9),
        (2, 6, 9, 11),
        (6, 6, 7, 11),
        (4, 12, 3, 13),
    ]
    dx, dy, dz, D = random.choice(triplets)
    sx = random.choice([1, -1])
    sy = random.choice([1, -1])
    sz = random.choice([1, -1])
    dx *= sx; dy *= sy; dz *= sz

    xI = random.randint(1, 5)
    yI = random.randint(1, 5)
    zI = random.randint(1, 5)
    xM = xI + dx
    yM = yI + dy
    zM = zI + dz

    caudan = fr'''Một nguồn âm phát ra sóng âm là sóng cầu trong không gian với hệ trục tọa độ $Oxyz$ (đơn vị trên mỗi trục là mét). Nguồn âm đặt tại tâm $I({xI}; {yI}; {zI})$. Để kiểm tra mức độ cảm nhận âm thanh tại vị trí $M({xM}; {yM}; {zM})$, người ta cần tính khoảng cách giữa hai vị trí $I$ và $M$. Khoảng cách giữa hai vị trí $I$ và $M$ là bao nhiêu mét?'''
    dapan = str(D)
    loi_giai = fr'''Khoảng cách giữa hai điểm $I({xI}; {yI}; {zI})$ và $M({xM}; {yM}; {zM})$ là:
$$IM = \sqrt{{({xM} - {xI})^2 + ({yM} - {yI})^2 + ({zM} - {zI})^2}} = \sqrt{{({dx})^2 + ({dy})^2 + ({dz})^2}} = \sqrt{{{D**2}}} = {D}\text{{ (m)}}.$$'''
    return caudan, dapan, loi_giai


def DeThiThu03_SA_Cau2():
    # Câu 2: Phương trình mặt phẳng đi qua 3 nút lưới x + my + nz + p = 0
    presets = [
        {"A": (1, 1, 10), "B": (4, 3, 1), "C": (3, 2, 5), "m": 3,  "n": 1,  "p": -14, "T": -10},
        {"A": (1, 2, 3),  "B": (2, 4, 5), "C": (3, 5, 8), "m": -1, "n": -1, "p": 4,   "T": 2},
        {"A": (2, 1, 3),  "B": (4, 2, 5), "C": (3, 3, 6), "m": -3, "n": 1,  "p": -2,  "T": -4},
        {"A": (1, 3, 2),  "B": (3, 4, 4), "C": (2, 5, 5), "m": 1,  "n": -2, "p": 0,   "T": -1},
    ]
    cfg = random.choice(presets)
    A, B, C = cfg["A"], cfg["B"], cfg["C"]
    m, n, p, T = cfg["m"], cfg["n"], cfg["p"], cfg["T"]

    m_str = f"+ {m}y" if m > 0 else (f"- {abs(m)}y" if m < 0 else "")
    n_str = f"+ {n}z" if n > 0 else (f"- {abs(n)}z" if n < 0 else "")
    p_str = f"+ {p}" if p > 0 else (f"- {abs(p)}" if p < 0 else "")

    caudan = fr'''Trong một khung lưới ô vuông gồm các hình lập phương trong không gian $Oxyz$, ba nút lưới có tọa độ lần lượt là $A({A[0]}; {A[1]}; {A[2]})$, $B({B[0]}; {B[1]}; {B[2]})$, $C({C[0]}; {C[1]}; {C[2]})$. Mặt phẳng $(ABC)$ có phương trình dạng $x {m_str} {n_str} {p_str} = 0$. Giá trị của tổng $m + n + p$ là bao nhiêu?'''
    dapan = str(T)
    loi_giai = fr'''Ta có $\overrightarrow{{AB}} = ({B[0]-A[0]}; {B[1]-A[1]}; {B[2]-A[2]})$ và $\overrightarrow{{AC}} = ({C[0]-A[0]}; {C[1]-A[1]}; {C[2]-A[2]})$. \\
Vectơ pháp tuyến của mặt phẳng $(ABC)$ là $\vec{{n}} = [\overrightarrow{{AB}}, \overrightarrow{{AC}}]$. Chuẩn hóa hệ số của $x$ bằng $1$, ta được phương trình:
$$x {m_str} {n_str} {p_str} = 0.$$
Suy ra $m = {m}, n = {n}, p = {p} \implies m + n + p = {T}$.'''
    return caudan, dapan, loi_giai


def DeThiThu03_SA_Cau3():
    # Câu 3: Tấm nhôm hình vuông cạnh a, cắt 4 góc cạnh x gập hộp thể tích max
    a = random.choice([6, 12, 18, 24, 30, 36])
    x_opt = a // 6

    caudan = fr'''\immini{{Cho một tấm nhôm hình vuông cạnh ${a}\text{{ cm}}$. Người ta cắt ở bốn góc bốn hình vuông bằng nhau, mỗi hình vuông có cạnh bằng $x\text{{ (cm)}}$, rồi gấp tấm nhôm lại để được một cái hộp hình hộp chữ nhật không có nắp. Giá trị của $x$ bằng bao nhiêu xentimét để thể tích của khối hộp đó là lớn nhất?}}{{
\begin{{tikzpicture}}[scale=0.5, font=\footnotesize]
	\coordinate (A) at (0,0); \coordinate (B) at (0,4); \coordinate (C) at (4,4); \coordinate (D) at (4,0);
	\draw (A)--(B)--(C)--(D)--cycle;
	\fill[pattern=north east lines] (0,0) rectangle (1,1);
	\fill[pattern=north east lines] (0,3) rectangle (1,4);
	\fill[pattern=north east lines] (3,0) rectangle (4,1);
	\fill[pattern=north east lines] (3,3) rectangle (4,4);
	\draw[dashed] (1,1) rectangle (3,3);
	\node[left] at (0,2) {{${a}$}};
	\node[below] at (0.5,0) {{$x$}};
\end{{tikzpicture}}
}}'''
    dapan = str(x_opt)
    loi_giai = fr'''Thể tích của chiếc hộp là $V(x) = x({a} - 2x)^2$ với $0 < x < {a // 2}$. \\
Đạo hàm: $V'(x) = ({a} - 2x)^2 - 4x({a} - 2x) = ({a} - 2x)({a} - 6x)$. \\
$V'(x) = 0 \iff x = \dfrac{{{a}}}{{6}} = {x_opt}$ (do $0 < x < {a // 2}$). \\
Lập bảng biến thiên ta thấy thể tích đạt giá trị lớn nhất khi $x = {x_opt}\text{{ cm}}$.'''
    return caudan, dapan, loi_giai


def DeThiThu03_SA_Cau4():
    # Câu 4: Diện tích logo con mắt giới hạn bởi 2 parabol
    cfgs = [
        {"a": Fraction(1, 4), "b": 2, "c": 1, "ans_str": "9,8",  "formula_f": r"-1/4*((\x)^2)+2", "formula_g": r"1/4*((\x)^2)-1"},
        {"a": Fraction(1, 3), "b": 3, "c": 1, "ans_str": "11,0", "formula_f": r"-1/3*((\x)^2)+3", "formula_g": r"1/3*((\x)^2)-1"},
        {"a": Fraction(1, 2), "b": 2, "c": 2, "ans_str": "10,7", "formula_f": r"-1/2*((\x)^2)+2", "formula_g": r"1/2*((\x)^2)-2"},
    ]
    p = random.choice(cfgs)

    caudan = fr'''\immini{{Một logo hình con mắt cho một cơ sở y tế là hình phẳng giới hạn bởi hai parabol $y = f(x)$ và $y = g(x)$ như hình vẽ (đơn vị trên mỗi trục tọa độ là đêximét). Biết $f(x) = -\dfrac{{1}}{{4}}x^2 + 2$ và $g(x) = \dfrac{{1}}{{4}}x^2 - 1$. Diện tích của logo là bao nhiêu đêximét vuông? \textit{{(Làm tròn kết quả đến hàng phần mười)}}}}{{
\begin{{tikzpicture}}[scale=0.6, line join=round, line cap=round, >=stealth]
	\def\xmin{{-3.5}}\def\xmax{{3.5}}\def\ymin{{-1.5}}\def\ymax{{2.5}}
	\draw[->] (\xmin-0.2,0)--(\xmax+0.2,0) node[below]{{$x$}};
	\draw[->] (0,\ymin-0.2)--(0,\ymax+0.2) node[right]{{$y$}};
	\draw (0,0) node[below left]{{$O$}};
	\clip (\xmin,\ymin) rectangle (\xmax,\ymax);
	\draw[thick,smooth,samples=200,domain=-3:3] plot (\x,{{{p["formula_g"]}}});
	\draw[thick,smooth,samples=200,domain=-3:3] plot (\x,{{{p["formula_f"]}}});
	\fill[pattern=north east lines,opacity=0.6] plot[domain=-{math.sqrt(6)}:{math.sqrt(6)}](\x,{{{p["formula_g"]}}})--plot[domain={math.sqrt(6)}:-{math.sqrt(6)}](\x,{{{p["formula_f"]}}})--cycle;
\end{{tikzpicture}}
}}'''
    dapan = p["ans_str"]
    loi_giai = fr'''Phương trình hoành độ giao điểm của hai parabol:
$$-\dfrac{{1}}{{4}}x^2 + 2 = \dfrac{{1}}{{4}}x^2 - 1 \iff \dfrac{{1}}{{2}}x^2 = 3 \iff x = \pm\sqrt{{6}}.$$
Diện tích của logo là:
$$S = \int_{{-\sqrt{{6}}}}^{{\sqrt{{6}}}} \left[\left(-\dfrac{{1}}{{4}}x^2 + 2\right) - \left(\dfrac{{1}}{{4}}x^2 - 1\right)\right]\,\mathrm{{d}}x = \int_{{-\sqrt{{6}}}}^{{\sqrt{{6}}}} \left(3 - \dfrac{{1}}{{2}}x^2\right)\,\mathrm{{d}}x = 4\sqrt{{6}} \approx {dapan}\text{{ dm}}^2.$$'''
    return caudan, dapan, loi_giai


def DeThiThu03_SA_Cau5():
    # Câu 5: Lăng trụ ABC.A'B'C' cạnh 1, góc cạnh bên và đáy 30 độ. Khoảng cách từ B đến (ACC'A')
    caudan = r'''Cho hình lăng trụ $ABC.A'B'C'$ có tất cả các cạnh đều bằng $1$. Góc tạo bởi cạnh bên và mặt phẳng đáy bằng $30^\circ$. Hình chiếu $H$ của $A'$ lên mặt phẳng $(ABC)$ thuộc đường thẳng $BC$. Tính khoảng cách từ $B$ đến mặt phẳng $(ACC'A')$ (làm tròn đến hàng phần trăm).'''
    dapan = "0,65"
    loi_giai = r'''Ta có $\triangle ABC$ đều cạnh $1$. Góc giữa cạnh bên $AA'$ và đáy là $\widehat{A'AH} = 30^\circ$. \\
Trong tam giác vuông $A'HA$, ta có $AH = AA' \cos 30^\circ = \dfrac{\sqrt{3}}{2}$. \\
Do khoảng cách từ $A$ đến đường thẳng $BC$ trong tam giác đều cạnh $1$ đúng bằng $\dfrac{\sqrt{3}}{2}$ nên $AH \perp BC$, suy ra $H$ là trung điểm của $BC$. \\
Chọn hệ trục tọa độ với $H$ là gốc tọa độ, ta xác định tọa độ các đỉnh:
$H(0; 0; 0), B\left(-\dfrac{1}{2}; 0; 0\right), C\left(\dfrac{1}{2}; 0; 0\right), A\left(0; \dfrac{\sqrt{3}}{2}; 0\right), A'\left(0; 0; \dfrac{1}{2}\right)$. \\
Phương trình mặt phẳng $(ACC'A')$ đi qua $A, C, A'$ là: $\sqrt{3}x + y + \sqrt{3}z - \dfrac{\sqrt{3}}{2} = 0$. \\
Khoảng cách từ điểm $B$ đến $(ACC'A')$ là:
$$d(B, (ACC'A')) = \dfrac{\left|\sqrt{3}\left(-\dfrac{1}{2}\right) - \dfrac{\sqrt{3}}{2}\right|}{\sqrt{3 + 1 + 3}} = \dfrac{\sqrt{3}}{\sqrt{7}} = \sqrt{\dfrac{3}{7}} \approx 0,65.$$'''
    return caudan, dapan, loi_giai


def DeThiThu03_SA_Cau6():
    # Câu 6: Xác suất xét nghiệm y tế sốt xuất huyết (Bayes)
    presets = [
        {"N": 8000, "B": 1200, "sens": 0.70, "spec_fp": 0.02, "ans_str": "0,86"},
        {"N": 10000, "B": 1000, "sens": 0.80, "spec_fp": 0.01, "ans_str": "0,90"},
        {"N": 5000,  "B": 500,  "sens": 0.75, "spec_fp": 0.02, "ans_str": "0,81"},
    ]
    cfg = random.choice(presets)
    N, B = cfg["N"], cfg["B"]
    healthy = N - B
    sens_pct = int(cfg["sens"] * 100)
    fp_pct = int(cfg["spec_fp"] * 100)
    ans = cfg["ans_str"]

    caudan = fr'''Một công ty dược phẩm giới thiệu một bộ kit xét nghiệm nhanh bệnh sốt xuất huyết. Trong một đợt thử nghiệm trên ${N}$ người dân, có ${B}$ người thực sự mắc bệnh và ${healthy}$ người không mắc bệnh. Kết quả thử nghiệm cho thấy: trong số những người mắc bệnh có ${sens_pct}\%$ người cho kết quả dương tính; trong số những người không mắc bệnh có ${fp_pct}\%$ người nhận kết quả dương tính giả. Chọn ngẫu nhiên một người trong đợt thử nghiệm đó và người đó có kết quả xét nghiệm dương tính. Xác suất để người này thực sự bị bệnh sốt xuất huyết bằng bao nhiêu? \textit{{(Viết kết quả dưới dạng số thập phân và làm tròn đến hàng phần trăm)}}'''
    dapan = ans
    loi_giai = fr'''Số người bị bệnh và có kết quả dương tính (dương tính thật) là: ${B} \times {cfg["sens"]} = {int(B * cfg["sens"])}$ người. \\
Số người không bị bệnh nhưng có kết quả dương tính (dương tính giả) là: ${healthy} \times {cfg["spec_fp"]} = {int(healthy * cfg["spec_fp"])}$ người. \\
Tổng số người có kết quả xét nghiệm dương tính là: ${int(B * cfg["sens"])} + {int(healthy * cfg["spec_fp"])} = {int(B * cfg["sens"] + healthy * cfg["spec_fp"])}$ người. \\
Xác suất để một người có kết quả dương tính thực sự mắc bệnh là:
$$P = \dfrac{{{int(B * cfg["sens"])}}}{{{int(B * cfg["sens"] + healthy * cfg["spec_fp"])}}} \approx {dapan}.$$'''
    return caudan, dapan, loi_giai
