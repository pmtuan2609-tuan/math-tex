# -*- coding: utf-8 -*-
"""
Module Ngân hàng Bài tập cuối chương mở rộng (Trắc nghiệm nhiều phương án)
Chứa các dạng câu hỏi được phân loại theo từng Chương và chuyên đề ôn tập.
Tất cả các hàm đều tự động ngẫu nhiên hóa tham số và xáo trộn phương án.
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


# ==============================================================================
# CHƯƠNG I: ỨNG DỤNG ĐẠO HÀM ĐỂ KHẢO SÁT HÀM SỐ (16 DẠNG)
# ==============================================================================

def CuoiChuong1_MC_Cau65():
    # Điểm cực đại hàm bậc ba từ đồ thị ngẫu nhiên hóa
    pool = [
        {"x_cd": 0, "y_cd": 2, "x_ct": 2, "y_ct": -2, "formula": r"(\x)^3 - 3*(\x)^2 + 2", "dom": "-0.8:2.8"},
        {"x_cd": -1, "y_cd": 2, "x_ct": 1, "y_ct": -2, "formula": r"(\x)^3 - 3*(\x)", "dom": "-2.1:2.1"},
        {"x_cd": 2, "y_cd": 3, "x_ct": 0, "y_ct": -1, "formula": r"-(\x)^3 + 3*(\x)^2 - 1", "dom": "-0.8:2.8"},
    ]
    p = random.choice(pool)
    x_cd, y_cd, x_ct, y_ct = p["x_cd"], p["y_cd"], p["x_ct"], p["y_ct"]

    caudan = fr'''Cho hàm số bậc ba $y = f(x)$ có đồ thị như hình vẽ dưới đây.
\begin{{center}}
\begin{{tikzpicture}}[>=stealth, scale=0.8,font=\footnotesize]
\draw[->] (-2.5,0) -- (3.5,0) node[above] {{$x$}};
\draw[->] (0,-3) -- (0,3.5) node[left] {{$y$}};
\fill (0,0) circle (1.5pt) node[below left] {{$O$}};
\draw[dashed] ({x_ct},0) node[above] {{${x_ct}$}} -- ({x_ct},{y_ct}) -- (0,{y_ct}) node[left] {{${y_ct}$}};
\draw ({x_cd},{y_cd}) node[above left] {{${y_cd}$}};
\draw[thick, smooth, samples=100, domain={p["dom"]}] plot(\x, {{{p["formula"]}}});
\end{{tikzpicture}}
\end{{center}}
Điểm cực đại của hàm số đã cho là'''
    choices = shuffle_choices(fr"${x_cd}$", [fr"${x_ct}$", fr"${y_cd}$", fr"${y_ct}$"])
    loi_giai = fr'''Dựa vào đồ thị, hàm số đạt cực đại tại điểm $x = {x_cd}$ (với giá trị cực đại tương ứng là $y = {y_cd}$).'''
    return caudan, choices, loi_giai


def CuoiChuong1_MC_Cau66():
    # Tiệm cận ngang từ bảng biến thiên
    y0 = random.choice([1, 2, -1, -2])
    x0 = random.choice([-2, -1, 1, 2])
    caudan = fr'''Cho hàm số $y = \dfrac{{ax+b}}{{cx+d}}$ ($ac \ne 0, ad-bc \ne 0$) có bảng biến thiên như dưới đây.
\begin{{center}}
\begin{{tikzpicture}}
\tkzTabInit[nocadre,lgt=1.2,espcl=3]{{$x$ / 0.6, $y'$ / 0.6, $y$ / 2}}{{$-\infty$, ${x0}$, $+\infty$}}
\tkzTabLine{{ , -, d, -, }}
\tkzTabVar{{+/ ${y0}$, -D+/ $-\infty$ / $+\infty$, -/ ${y0}$}}
\end{{tikzpicture}}
\end{{center}}
Đường tiệm cận ngang của đồ thị hàm số đã cho có phương trình là'''
    choices = shuffle_choices(fr"$y = {y0}$", [fr"$x = {x0}$", fr"$x = {y0}$", fr"$y = {x0}$"])
    loi_giai = fr'''Từ bảng biến thiên, ta có $\lim\limits_{{x \to -\infty}} y = {y0}$ và $\lim\limits_{{x \to +\infty}} y = {y0}$ nên đường thẳng $y = {y0}$ là đường tiệm cận ngang của đồ thị hàm số.'''
    return caudan, choices, loi_giai


def CuoiChuong1_MC_Cau67():
    # Giá trị cực tiểu hàm bậc ba y = x^3 - (3k/2) x^2 + d ngẫu nhiên hóa
    k = random.choice([1, 2, 3])
    d = random.choice([-2, -1, 0, 1, 2])
    # f'(x) = 3x^2 - 3kx = 3x(x - k) => ct at x = k
    # f(k) = k^3 - 3/2 k^3 + d = -1/2 k^3 + d
    y_ct = Fraction(-k**3, 2) + d
    frac_str = f"{y_ct.numerator}/{y_ct.denominator}" if y_ct.denominator != 1 else str(y_ct.numerator)
    tex_ans = fr"\dfrac{{{y_ct.numerator}}}{{{y_ct.denominator}}}" if y_ct.denominator != 1 else str(y_ct.numerator)

    k32_str = fr"\dfrac{{{3*k}x^2}}{{2}}" if (3*k)%2 != 0 else fr"{3*k//2}x^2"
    d_str = f"+ {d}" if d > 0 else (f"- {abs(d)}" if d < 0 else "")

    caudan = fr'''Cho hàm số $y = f(x) = x^3 - {k32_str} {d_str}$. Giá trị cực tiểu của hàm số đã cho là'''
    choices = shuffle_choices(fr"${tex_ans}$", [fr"${d}$", fr"${k}$", fr"${-k}$"])
    loi_giai = fr'''Ta có $f'(x) = 3x^2 - {3*k}x = 3x(x - {k})$. \\
$f'(x) = 0 \iff x = 0$ hoặc $x = {k}$. \\
Bảng biến thiên cho thấy hàm số đạt cực tiểu tại $x = {k}$, giá trị cực tiểu là $f({k}) = {tex_ans}$.'''
    return caudan, choices, loi_giai


def CuoiChuong1_MC_Cau68():
    # Tiệm cận ngang hàm phân thức bậc nhất trên bậc nhất ngẫu nhiên hóa
    a = random.choice([2, 4, 6, 8])
    c = random.choice([3, 5, 7, 9])
    b = random.choice([1, 3, 5])
    d = random.choice([1, 2, 4])
    g = math.gcd(a, c)
    num, den = a // g, c // g

    caudan = fr'''Đồ thị hàm số $y = \dfrac{{{a}x+{b}}}{{{c}x+{d}}}$ có đường tiệm cận ngang là'''
    choices = shuffle_choices(fr"$y = \dfrac{{{num}}}{{{den}}}$", [fr"$x = \dfrac{{{num}}}{{{den}}}$", fr"$x = -\dfrac{{{d}}}{{{c}}}$", fr"$y = {b}$"])
    loi_giai = fr'''Ta có $\lim\limits_{{x \to \pm\infty}} \dfrac{{{a}x+{b}}}{{{c}x+{d}}} = \dfrac{{{a}}}{{{c}}} = \dfrac{{{num}}}{{{den}}}$. Vậy đường tiệm cận ngang của đồ thị hàm số là $y = \dfrac{{{num}}}{{{den}}}$.'''
    return caudan, choices, loi_giai


def CuoiChuong1_MC_Cau69():
    # Tổng số đường tiệm cận đứng và ngang từ bảng biến thiên ngẫu nhiên hóa
    y1 = random.choice([1, 2, 3])
    y2 = random.choice([-1, -2, -3])
    x0 = random.choice([1, 2, -1])

    caudan = fr'''Cho hàm số $y = f(x)$ liên tục trên $\mathbb{{R}} \setminus \{{{x0}\}}$ có bảng biến thiên như hình vẽ.
\begin{{center}}
\begin{{tikzpicture}}
\tkzTabInit[nocadre=false,lgt=1.2,espcl=2.5]{{$x$ / 0.6, $y'$ / 0.6, $y$ / 2}}{{$-\infty$, $-2$, ${x0}$, $+\infty$}}
\tkzTabLine{{ , -, 0, +, d, +, }}
\tkzTabVar{{+/ ${y1}$, -/ $-\sqrt{{2}}$, +D-/ $+\infty$ / $-\infty$, -/ ${y2}$}}
\end{{tikzpicture}}
\end{{center}}
Tổng số đường tiệm cận đứng và đường tiệm cận ngang của đồ thị hàm số $y = f(x)$ là:'''
    choices = shuffle_choices("$3$", ["$4$", "$2$", "$1$"])
    loi_giai = fr'''Từ bảng biến thiên:
- $\lim\limits_{{x \to -\infty}} y = {y1} \implies y = {y1}$ là tiệm cận ngang.
- $\lim\limits_{{x \to +\infty}} y = {y2} \implies y = {y2}$ là tiệm cận ngang.
- Tại $x = {x0}$: $\lim\limits_{{x \to {x0}^-}} y = +\infty \implies x = {x0}$ là tiệm cận đứng.
Vậy đồ thị hàm số có tổng cộng $2 + 1 = 3$ đường tiệm cận.'''
    return caudan, choices, loi_giai


def CuoiChuong1_MC_Cau70():
    # Điểm cực tiểu của hàm số trên [-1; 3] từ đồ thị ngẫu nhiên hóa
    x_ct = random.choice([1, 2])
    y_ct = random.choice([-2, -3])

    caudan = fr'''Cho hàm số $y = f(x)$ liên tục trên đoạn $[-1;3]$ và có đồ thị như hình vẽ.
\begin{{center}}
\begin{{tikzpicture}}[>=stealth, scale=0.8]
\draw[->] (-1.5,0) -- (3.5,0) node[below] {{$x$}};
\draw[->] (0,-3.5) -- (0,3.5) node[right] {{$y$}};
\fill (0,0) circle (1.5pt) node[below left] {{$O$}};
\draw[dashed] (-1,0) node[below] {{$-1$}} -- (-1,1) -- (0,1) node[right] {{$1$}};
\draw[dashed] ({x_ct},0) node[above] {{${x_ct}$}} -- ({x_ct},{y_ct}) -- (0,{y_ct}) node[left] {{${y_ct}$}};
\draw[dashed] (3,0) node[above right] {{$3$}} -- (3,3) -- (0,3) node[left] {{$3$}};
\draw (0,2) node[above left] {{$2$}};
\draw[thick] (-1,1) .. controls (-0.5,2) and (-0.2,2) .. (0,2);
\draw[thick] (0,2) .. controls (0.5,2) and ({x_ct-0.5},{y_ct}) .. ({x_ct},{y_ct});
\draw[thick] ({x_ct},{y_ct}) -- (3,3);
\fill (-1,1) circle (1pt);
\fill (0,2) circle (1pt);
\fill ({x_ct},{y_ct}) circle (1pt);
\fill (3,3) circle (1pt);
\end{{tikzpicture}}
\end{{center}}
Điểm cực tiểu của hàm số trên $[-1;3]$ là:'''
    choices = shuffle_choices(fr"$x = {x_ct}$", ["$x = 3$", "$y = 1$", fr"$y = {y_ct}$"])
    loi_giai = fr'''Quan sát đồ thị, tại lân cận điểm $x = {x_ct}$, đồ thị đổi hướng từ giảm sang tăng và đạt điểm thấp nhất tại $({x_ct}; {y_ct})$. Do đó điểm cực tiểu của hàm số là $x = {x_ct}$.'''
    return caudan, choices, loi_giai


def CuoiChuong1_MC_Cau71():
    # Giá trị cực đại hàm bậc 2 trên bậc 1 ngẫu nhiên hóa
    # y = (x^2 + a)/(x) hoặc y = (x^2 + 2x + 2)/(x + 1)
    k = random.choice([2, 3, 4])
    k2 = k**2
    caudan = fr'''Cho hàm số $y = \dfrac{{x^2 + {k2}}}{{x}}$. Giá trị cực tiểu của hàm số đã cho trên khoảng $(0; +\infty)$ là'''
    ans = 2 * k
    choices = shuffle_choices(fr"${ans}$", [fr"${k}$", fr"${k2}$", fr"${ans + 2}$"])
    loi_giai = fr'''Với $x > 0$, ta có $y = x + \dfrac{{{k2}}}{{x}} \ge 2\sqrt{{x \cdot \dfrac{{{k2}}}{{x}}}} = {ans}$. Dấu bằng xảy ra khi $x = {k} > 0$. Vậy giá trị cực tiểu là ${ans}$.'''
    return caudan, choices, loi_giai


def CuoiChuong1_MC_Cau72():
    # Số đường tiệm cận của y = (x^2+bx+c)/(m x^2 + n) ngẫu nhiên hóa
    m = random.choice([2, 3, 4])
    n = random.choice([2, 3, 5])
    caudan = fr'''Số đường tiệm cận của đồ thị hàm số $y = \dfrac{{x^2 + 3x - 4}}{{{m}x^2 + {n}}}$ là'''
    choices = shuffle_choices("$1$", ["$0$", "$2$", "$3$"])
    loi_giai = fr'''Mẫu số ${m}x^2 + {n} > 0, \forall x \in \mathbb{{R}}$ nên đồ thị hàm số không có đường tiệm cận đứng.
$\lim\limits_{{x \to \pm\infty}} y = \lim\limits_{{x \to \pm\infty}} \dfrac{{x^2 + 3x - 4}}{{{m}x^2 + {n}}} = \dfrac{{1}}{{{m}}}$, do đó đường thẳng $y = \dfrac{{1}}{{{m}}}$ là đường tiệm cận ngang duy nhất.
Vậy đồ thị hàm số có đúng $1$ đường tiệm cận.'''
    return caudan, choices, loi_giai


def CuoiChuong1_MC_Cau73():
    # Hàm y = (x^2 - sx + p)e^x nghịch biến ngẫu nhiên hóa
    x1, x2 = random.choice([(1, 2), (2, 3), (1, 3), (2, 4)])
    s = x1 + x2
    p = x1 * x2
    # y' = (x^2 - sx + p + 2x - s) e^x = (x^2 - (s-2)x + (p-s)) e^x
    # Để y' có nghiệm x1, x2:
    # y = (x^2 - (s+2)x + p + s + 2) e^x => y' = (x^2 - sx + p) e^x
    s_poly = s + 2
    p_poly = p + s + 2

    caudan = fr'''Hàm số $y = (x^2 - {s_poly}x + {p_poly})e^x$ nghịch biến trong khoảng nào sau đây?'''
    correct = fr"$({x1}; {x2})$"
    wrongs = [
        fr"$({x1 - 1}; {x1})$",
        fr"$({x2}; {x2 + 1})$",
        fr"$(0; {x1})$"
    ]
    choices = shuffle_choices(correct, wrongs)
    loi_giai = fr'''Ta có: $y' = (2x - {s_poly})e^x + (x^2 - {s_poly}x + {p_poly})e^x = (x^2 - {s}x + {p})e^x$. \\
Vì $e^x > 0, \forall x$ nên $y' < 0 \iff x^2 - {s}x + {p} < 0 \iff {x1} < x < {x2}$. \\
Vậy hàm số nghịch biến trên khoảng $({x1}; {x2})$.'''
    return caudan, choices, loi_giai


def CuoiChuong1_MC_Cau74():
    # Giá trị cực tiểu hàm bậc ba từ đồ thị ngẫu nhiên hóa
    y_ct = random.choice([-1, -2, -3])
    x_ct = random.choice([2, 3])

    caudan = fr'''Cho hàm số $f(x) = ax^3 + bx^2 + cx + d$ có đồ thị đạt cực tiểu tại điểm $({x_ct}; {y_ct})$.
Giá trị cực tiểu của hàm số $y = f(x)$ là'''
    choices = shuffle_choices(fr"$y = {y_ct}$", [fr"$x = {x_ct}$", fr"$x = {y_ct}$", fr"$y = {x_ct}$"])
    loi_giai = fr'''Dựa vào dữ kiện cực tiểu tại $({x_ct}; {y_ct})$, giá trị cực tiểu của hàm số là $y = {y_ct}$.'''
    return caudan, choices, loi_giai


def CuoiChuong1_MC_Cau75():
    # Tổng số đường tiệm cận từ bảng biến thiên ngẫu nhiên hóa
    y_left = random.choice([1, 2])
    y_right = random.choice([3, 4])
    x0 = random.choice([0, 1])

    caudan = fr'''Cho hàm số $y = f(x)$ có bảng biến thiên như sau.
\begin{{center}}
\begin{{tikzpicture}}
\tkzTabInit[nocadre,lgt=1.2,espcl=2.5]{{$x$ / 0.6, $y'$ / 0.6, $y$ / 2}}{{$-\infty$, ${x0}$, $3$, $+\infty$}}
\tkzTabLine{{ , -, d, -, 0, +, }}
\tkzTabVar{{+/ ${y_left}$, -D+/ $-\infty$ / $2$, -/ $-3$, +/ ${y_right}$}}
\end{{tikzpicture}}
\end{{center}}
Tổng số đường tiệm cận đứng và tiệm cận ngang của đồ thị hàm số đã cho là'''
    choices = shuffle_choices("$3$", ["$0$", "$1$", "$2$"])
    loi_giai = fr'''Từ bảng biến thiên:
- $\lim\limits_{{x \to -\infty}} y = ${y_left}$ \implies y = ${y_left}$ là tiệm cận ngang.
- $\lim\limits_{{x \to +\infty}} y = ${y_right}$ \implies y = ${y_right}$ là tiệm cận ngang.
- Tại $x = ${x0}$: $\lim\limits_{{x \to {x0}^-}} y = -\infty \implies x = ${x0}$ là tiệm cận đứng.
Tổng số đường tiệm cận đứng và ngang là $2 + 1 = 3$.'''
    return caudan, choices, loi_giai


def CuoiChuong1_MC_Cau76():
    # Số điểm cực đại của f'(x) = x^2(x-a)(x-b)^3 ngẫu nhiên hóa
    a = random.choice([1, 2])
    b = a + random.choice([1, 2])

    caudan = fr'''Hàm số $f(x)$ có đạo hàm $f'(x) = x^2(x - {a})(x - {b})^3, \forall x \in \mathbb{{R}}$. Hàm số $f(x)$ có bao nhiêu điểm cực đại?'''
    choices = shuffle_choices("$1$", ["$0$", "$2$", "$3$"])
    loi_giai = fr'''$f'(x) = 0 \iff x = 0$ (bội chẵn), $x = {a}$ (bội lẻ), $x = {b}$ (bội lẻ). \\
- Qua $x = 0$, $f'(x)$ không đổi dấu. \\
- Bảng xét dấu: \\
  + Khi $x \in ({a}; {b})$: $f'(x) < 0$. \\
  + Khi $x > {b}$: $f'(x) > 0$. \\
  + Khi $x < {a}$: $f'(x) > 0$. \\
Qua $x = {a}$, $f'(x)$ đổi dấu từ dương sang âm nên $x = {a}$ là điểm cực đại duy nhất. Vậy hàm số có đúng $1$ điểm cực đại.'''
    return caudan, choices, loi_giai


def CuoiChuong1_MC_Cau77():
    # Tiệm cận hàm y = (x-a)/(x^2-a^2) ngẫu nhiên hóa
    a = random.choice([2, 3, 4, 5])
    a2 = a**2

    caudan = fr'''Đồ thị của hàm số $y = \dfrac{{x - {a}}}{{x^2 - {a2}}}$ có tất cả bao nhiêu đường tiệm cận đứng và tiệm cận ngang?'''
    choices = shuffle_choices("$2$", ["$1$", "$0$", "$3$"])
    loi_giai = fr'''Với $x \ne {a}$, ta có $y = \dfrac{{x - {a}}}{{(x - {a})(x + {a})}} = \dfrac{{1}}{{x + {a}}}$. \\
- $\lim\limits_{{x \to \pm\infty}} y = 0 \implies y = 0$ là tiệm cận ngang. \\
- $\lim\limits_{{x \to -{a}}} y = \infty \implies x = -{a}$ là tiệm cận đứng. \\
- Tại $x = {a}$: $\lim\limits_{{x \to {a}}} y = \dfrac{{1}}{{{2*a}}} \ne \infty$ nên $x = {a}$ không là tiệm cận đứng. \\
Vậy đồ thị có tất cả $1 + 1 = 2$ đường tiệm cận.'''
    return caudan, choices, loi_giai


def CuoiChuong1_MC_Cau78():
    # Gia tốc tại thời điểm vận tốc triệt tiêu ngẫu nhiên hóa
    k = random.choice([2, 3, 4])
    # S(t) = t^3 - 3k t^2 ... v(t) = 3t^2 - 6k t = 0 => t = 2k
    # a(t) = 6t - 6k => a(2k) = 6k
    # Let S(t) = t^3 - 3 t^2 - 9 t + 5 with t=3, a=12
    cases = [
        {"k": 1, "t0": 3, "a_ans": 12, "expr": "t^3 - 3t^2 - 9t + 5"},
        {"k": 2, "t0": 4, "a_ans": 18, "expr": "t^3 - 3t^2 - 24t + 8"},
        {"k": 3, "t0": 2, "a_ans": 6,  "expr": "t^3 - 3t^2 + 1"},
    ]
    c = random.choice(cases)
    t0, a_ans, expr = c["t0"], c["a_ans"], c["expr"]

    caudan = fr'''Một chất điểm chuyển động có phương trình $S = {expr}$, trong đó $t$ được tính bằng giây và $S$ được tính bằng mét. Gia tốc tại thời điểm vận tốc bị triệt tiêu ($v=0$) là'''
    choices = shuffle_choices(fr"${a_ans}\text{{ m/s}}^2$", [fr"${-a_ans}\text{{ m/s}}^2$", fr"${a_ans // 2}\text{{ m/s}}^2$", fr"${a_ans + 6}\text{{ m/s}}^2$"])
    loi_giai = fr'''Vận tốc là $v(t) = S'(t)$. Khi vận tốc triệt tiêu ta tìm được thời điểm $t = {t0}\text{{ s}}$. \\
Gia tốc là $a(t) = v'(t)$. Thay $t = {t0}$ ta được $a({t0}) = {a_ans}\text{{ m/s}}^2$.'''
    return caudan, choices, loi_giai


def CuoiChuong1_MC_Cau79():
    # Số cực trị của hàm số nhất biến ngẫu nhiên hóa
    a = random.choice([2, 3, 4])
    b = random.choice([-5, -3, 3, 5])
    c = random.choice([1, 2])
    d = random.choice([2024, 2025, 2026])

    caudan = fr'''Hàm số $y = \dfrac{{{a}x {f'+ {b}' if b>0 else f'- {abs(b)}'}}}{{{c if c>1 else ''}x + {d}}}$ có mấy cực trị?'''
    choices = shuffle_choices("$0$", ["$1$", "$2$", "$3$"])
    loi_giai = fr'''Đạo hàm của hàm phân thức bậc nhất trên bậc nhất luôn cùng dấu trên từng khoảng xác định, do đó hàm số không có cực trị (có $0$ cực trị).'''
    return caudan, choices, loi_giai


def CuoiChuong1_MC_Cau80():
    # Tiệm cận từ BBT ngẫu nhiên hóa
    y1 = random.choice([2, 3, 4])
    y2 = random.choice([-2, -3, -4])
    caudan = fr'''Cho bảng biến thiên của hàm số $y = f(x)$ có $\lim\limits_{{x \to -\infty}} f(x) = {y1}$, $\lim\limits_{{x \to +\infty}} f(x) = {y2}$, và $\lim\limits_{{x \to 0^+}} f(x) = -\infty$.
Tổng số đường tiệm cận của đồ thị hàm số $y = f(x)$ là'''
    choices = shuffle_choices("$3$", ["$0$", "$2$", "$1$"])
    loi_giai = fr'''Đồ thị có $2$ tiệm cận ngang $y = {y1}, y = {y2}$ và $1$ tiệm cận đứng $x = 0$. Tổng cộng có $3$ đường tiệm cận.'''
    return caudan, choices, loi_giai



# ==============================================================================
# CHƯƠNG III: CÁC SỐ ĐẶC TRƯNG ĐO ĐỘ PHÂN TÁN CHO MẪU GHÉP NHÓM (7 DẠNG)
# ==============================================================================

def CuoiChuong3_MC_Cau7():
    # Phương sai điểm trung bình môn Toán ngẫu nhiên hóa
    datasets = [
        {"freqs": [8, 10, 16, 24, 13, 7, 4], "ans": "0,616", "wrongs": ["0,785", "0,609", "0,780"], "mean": "8,079", "n": 82},
        {"freqs": [6, 12, 18, 22, 14, 8, 5], "ans": "0,634", "wrongs": ["0,712", "0,580", "0,795"], "mean": "8,065", "n": 85},
        {"freqs": [10, 14, 15, 20, 15, 6, 3], "ans": "0,598", "wrongs": ["0,675", "0,520", "0,730"], "mean": "7,964", "n": 83},
    ]
    d = random.choice(datasets)
    freqs = d["freqs"]

    caudan = fr'''Thống kê điểm trung bình môn Toán của một số học sinh lớp 12 được mẫu số liệu sau:
\begin{{center}}
\begin{{tabular}}{{|l|c|c|c|c|c|c|c|}}
\hline
Khoảng điểm & $[6,5; 7)$ & $[7; 7,5)$ & $[7,5; 8)$ & $[8; 8,5)$ & $[8,5; 9)$ & $[9; 9,5)$ & $[9,5; 10)$ \\
\hline
Tần số & ${freqs[0]}$ & ${freqs[1]}$ & ${freqs[2]}$ & ${freqs[3]}$ & ${freqs[4]}$ & ${freqs[5]}$ & ${freqs[6]}$ \\
\hline
\end{{tabular}}
\end{{center}}
Phương sai của mẫu số liệu về điểm trung bình môn Toán của các học sinh đó là (làm tròn đến hàng phần nghìn)'''
    choices = shuffle_choices(f"${d['ans']}$", [f"${w}$" for w in d["wrongs"]])
    loi_giai = fr'''Các giá trị đại diện là: $6,75; 7,25; 7,75; 8,25; 8,75; 9,25; 9,75$. \\
Tổng số học sinh: $n = {d["n"]}$. \\
Số trung bình: $\bar{{x}} \approx {d["mean"]}$. \\
Phương sai mẫu: $s^2 = \dfrac{{1}}{{n}}\sum n_i x_i^2 - \bar{{x}}^2 \approx {d["ans"]}$.'''
    return caudan, choices, loi_giai


def CuoiChuong3_MC_Cau8():
    # Phương sai mẫu số liệu điểm thi ngẫu nhiên hóa
    datasets = [
        {"freqs": [8, 14, 2, 9, 9], "ans": "8,65", "wrongs": ["3,13", "2,42", "9,11"], "mean": "5,86", "n": 42},
        {"freqs": [6, 12, 4, 10, 8], "ans": "8,15", "wrongs": ["3,25", "2,85", "9,40"], "mean": "5,80", "n": 40},
        {"freqs": [10, 10, 5, 8, 7], "ans": "8,44", "wrongs": ["3,05", "2,60", "9,25"], "mean": "5,40", "n": 40},
    ]
    d = random.choice(datasets)
    freqs = d["freqs"]

    caudan = fr'''Cho mẫu số liệu ghép nhóm về điểm thi và số người dự thi như sau:
\begin{{center}}
\begin{{tabular}}{{|c|c|c|c|c|c|}}
\hline
Điểm thi & $[1; 3)$ & $[3; 5)$ & $[5; 7)$ & $[7; 9)$ & $[9; 11)$ \\
\hline
Số người dự thi & ${freqs[0]}$ & ${freqs[1]}$ & ${freqs[2]}$ & ${freqs[3]}$ & ${freqs[4]}$ \\
\hline
\end{{tabular}}
\end{{center}}
Tính phương sai của mẫu số liệu ghép nhóm trên (kết quả làm tròn đến hàng phần trăm).'''
    choices = shuffle_choices(f"${d['ans']}$", [f"${w}$" for w in d["wrongs"]])
    loi_giai = fr'''Giá trị đại diện lần lượt là: $2, 4, 6, 8, 10$. \\
Tổng số người: $n = {d["n"]}$. \\
Số trung bình: $\bar{{x}} \approx {d["mean"]}$. \\
Phương sai: $s^2 \approx {d["ans"]}$.'''
    return caudan, choices, loi_giai


def CuoiChuong3_MC_Cau9():
    # Tứ phân vị thứ nhất Q1 thời gian chờ khám ngẫu nhiên hóa
    datasets = [
        {"freqs": [3, 12, 15, 8], "ans": "7,71", "wrongs": ["6,70", "14,50", "6,79"], "n": 38},
        {"freqs": [4, 10, 16, 10], "ans": "8,00", "wrongs": ["7,25", "13,50", "6,50"], "n": 40},
        {"freqs": [2, 14, 14, 10], "ans": "7,86", "wrongs": ["6,90", "14,00", "7,15"], "n": 40},
    ]
    d = random.choice(datasets)
    freqs = d["freqs"]

    caudan = fr'''Thời gian chờ khám của các bệnh nhân tại một phòng khám được cho trong bảng sau:
\begin{{center}}
\begin{{tabular}}{{|c|c|c|c|c|}}
\hline
Thời gian (phút) & $[0; 5)$ & $[5; 10)$ & $[10; 15)$ & $[15; 20)$ \\
\hline
Số bệnh nhân & ${freqs[0]}$ & ${freqs[1]}$ & ${freqs[2]}$ & ${freqs[3]}$ \\
\hline
\end{{tabular}}
\end{{center}}
Tứ phân vị thứ nhất của mẫu số liệu ghép nhóm này là:'''
    choices = shuffle_choices(f"${d['ans']}$", [f"${w}$" for w in d["wrongs"]])
    loi_giai = fr'''Cỡ mẫu: $n = {d["n"]}$. Áp dụng công thức tứ phân vị thứ nhất cho mẫu số liệu ghép nhóm ta tính được $Q_1 \approx {d["ans"]}$.'''
    return caudan, choices, loi_giai


def CuoiChuong3_MC_Cau10():
    # Khoảng biến thiên lương nhân viên ngẫu nhiên hóa
    h = random.choice([4, 5, 6, 7])
    start = random.choice([6, 8, 10])
    groups = [(start + i*h, start + (i+1)*h) for i in range(6)]
    ans = groups[-1][1] - groups[0][0]
    freqs = [random.randint(1, 10) for _ in range(6)]

    caudan = fr'''Cho mẫu số liệu ghép nhóm về lương (triệu đồng) và số nhân viên như bảng sau. Tìm khoảng biến thiên của mẫu số liệu ghép nhóm đã cho.
\begin{{center}}
\begin{{tabular}}{{|c|c|c|c|c|c|c|}}
\hline
Lương (triệu đồng) & $[{groups[0][0]}; {groups[0][1]})$ & $[{groups[1][0]}; {groups[1][1]})$ & $[{groups[2][0]}; {groups[2][1]})$ & $[{groups[3][0]}; {groups[3][1]})$ & $[{groups[4][0]}; {groups[4][1]})$ & $[{groups[5][0]}; {groups[5][1]})$ \\
\hline
Số nhân viên & ${freqs[0]}$ & ${freqs[1]}$ & ${freqs[2]}$ & ${freqs[3]}$ & ${freqs[4]}$ & ${freqs[5]}$ \\
\hline
\end{{tabular}}
\end{{center}}'''
    choices = shuffle_choices(fr"${ans}$", [fr"${ans + h}$", fr"${ans - h}$", fr"${groups[-1][1]}$"])
    loi_giai = fr'''Khoảng biến thiên của mẫu số liệu ghép nhóm là hiệu giữa đầu mút phải của nhóm cuối cùng và đầu mút trái của nhóm đầu tiên:
$R = {groups[-1][1]} - {groups[0][0]} = {ans}\text{{ (triệu đồng)}}$.'''
    return caudan, choices, loi_giai


def CuoiChuong3_MC_Cau11():
    # Độ lệch chuẩn chiều cao học sinh ngẫu nhiên hóa
    datasets = [
        {"freqs": [25, 50, 200, 175, 50], "s": "3,85", "mean": "161,4", "wrongs": ["s = 161,4", "s = 8,20", "s = 14,48"]},
        {"freqs": [30, 60, 180, 160, 70], "s": "4,12", "mean": "161,2", "wrongs": ["s = 161,2", "s = 7,85", "s = 16,97"]},
        {"freqs": [20, 45, 210, 180, 45], "s": "3,68", "mean": "161,5", "wrongs": ["s = 161,5", "s = 8,50", "s = 13,54"]},
    ]
    d = random.choice(datasets)
    freqs = d["freqs"]

    caudan = fr'''Một trường học thực hiện đo chiều cao (tính bằng cm) của 500 học sinh trong trường. Kết quả thu được như sau:
\begin{{center}}
\begin{{tabular}}{{|c|c|c|c|c|c|}}
\hline
Chiều cao & $[150; 154)$ & $[154; 158)$ & $[158; 162)$ & $[162; 166)$ & $[166; 170)$ \\
\hline
Tần số & ${freqs[0]}$ & ${freqs[1]}$ & ${freqs[2]}$ & ${freqs[3]}$ & ${freqs[4]}$ \\
\hline
\end{{tabular}}
\end{{center}}
Độ lệch chuẩn của mẫu số liệu trên là:'''
    choices = shuffle_choices(fr"$s = {d['s']}$", [fr"${w}$" for w in d["wrongs"]])
    loi_giai = fr'''Tính số trung bình $\bar{{x}} \approx {d["mean"]}$ và phương sai $s^2$, ta suy ra độ lệch chuẩn $s = \sqrt{{s^2}} \approx {d['s']}\text{{ cm}}$.'''
    return caudan, choices, loi_giai


def CuoiChuong3_MC_Cau12():
    # Khoảng biến thiên chiều cao nữ sinh ngẫu nhiên hóa
    h = random.choice([4, 5, 6])
    min_val = random.choice([150, 155, 158])
    max_val = min_val + 6 * h
    ans = max_val - min_val
    freqs = [random.randint(2, 10) for _ in range(6)]

    caudan = fr'''Thống kê chiều cao của học sinh một lớp được cho ở bảng sau:
\begin{{center}}
\begin{{tabular}}{{|c|c|c|c|c|c|c|}}
\hline
Chiều cao (cm) & $[{min_val}; {min_val+h})$ & $[{min_val+h}; {min_val+2*h})$ & $[{min_val+2*h}; {min_val+3*h})$ & $[{min_val+3*h}; {min_val+4*h})$ & $[{min_val+4*h}; {min_val+5*h})$ & $[{min_val+5*h}; {max_val})$ \\
\hline
Số học sinh & ${freqs[0]}$ & ${freqs[1]}$ & ${freqs[2]}$ & ${freqs[3]}$ & ${freqs[4]}$ & ${freqs[5]}$ \\
\hline
\end{{tabular}}
\end{{center}}
Khoảng biến thiên của mẫu số liệu là'''
    choices = shuffle_choices(fr"${ans}$", [fr"${h}$", fr"${ans - h}$", fr"${ans + h}$"])
    loi_giai = fr'''Khoảng biến thiên của mẫu số liệu ghép nhóm là $R = {max_val} - {min_val} = {ans}\text{{ (cm)}}$.'''
    return caudan, choices, loi_giai


def CuoiChuong3_MC_Cau13():
    # Khoảng biến thiên chiều cao đơn vị mét ngẫu nhiên hóa
    step = random.choice([0.05, 0.06])
    start = random.choice([1.45, 1.50])
    end = round(start + 5 * step, 2)
    ans = round(end - start, 2)
    ans_str = str(ans).replace(".", ",")

    caudan = fr'''Thống kê lại chiều cao của học sinh theo đơn vị mét, với nhóm đầu tiên là $[{str(start).replace(".", ",")}; {str(round(start+step, 2)).replace(".", ",")})$ và nhóm cuối cùng là $[{str(round(end-step, 2)).replace(".", ",")}; {str(end).replace(".", ",")})$.
Khoảng biến thiên của mẫu số liệu ghép nhóm trên là?'''
    choices = shuffle_choices(fr"${ans_str}\text{{ (m)}}$", [r"$1\text{ (m)}$", r"$0,76\text{ (m)}$", r"$0,50\text{ (m)}$"])
    loi_giai = fr'''Khoảng biến thiên là $R = {str(end).replace(".", ",")} - {str(start).replace(".", ",")} = {ans_str}\text{{ (m)}}$.'''
    return caudan, choices, loi_giai


# ==============================================================================
# CHƯƠNG IV: NGUYÊN HÀM VÀ TÍCH PHÂN (7 DẠNG)
# ==============================================================================

def CuoiChuong4_MC_Cau4():
    # Tích phân cộng khoảng ngẫu nhiên hóa
    a = random.choice([1, 2])
    b = a + random.choice([2, 3])
    c = b + random.choice([2, 3])
    I1 = random.randint(3, 10)
    I_total = I1 + random.randint(5, 15)
    ans = I_total - I1

    caudan = fr'''Nếu hàm số $f(x)$ thỏa mãn $\int\limits_{{{a}}}^{{{b}}} f(x)\,\mathrm{{d}}x = {I1}$ và $\int\limits_{{{a}}}^{{{c}}} f(x)\,\mathrm{{d}}x = {I_total}$ thì giá trị của $\int\limits_{{{b}}}^{{{c}}} f(x)\,\mathrm{{d}}x$ bằng'''
    choices = shuffle_choices(fr"${ans}$", [fr"${-ans}$", fr"${I_total + I1}$", fr"${ans + 2}$"])
    loi_giai = fr'''Theo tính chất của tích phân: $\int\limits_{{{a}}}^{{{c}}} f(x)\,\mathrm{{d}}x = \int\limits_{{{a}}}^{{{b}}} f(x)\,\mathrm{{d}}x + \int\limits_{{{b}}}^{{{c}}} f(x)\,\mathrm{{d}}x$. \\
Suy ra $\int\limits_{{{b}}}^{{{c}}} f(x)\,\mathrm{{d}}x = {I_total} - {I1} = {ans}$.'''
    return caudan, choices, loi_giai


def CuoiChuong4_MC_Cau5():
    # Tuyến tính tích phân \int [k f(x) + c] ngẫu nhiên hóa
    a = random.randint(1, 5)
    b = a + random.randint(3, 7)
    k = random.choice([-3, -4, -5, -6, -7])
    c = random.choice([-3, -2, 2, 3])
    I_val = random.choice([-10, -5, 5, 8, 10])
    ans = k * I_val + c * (b - a)

    diff_ba = b - a
    term_c = c * diff_ba
    caudan = fr'''Cho tích phân $\int\limits_{{{a}}}^{{{b}}} f(x)\,\mathrm{{d}}x = {I_val}$. Tính tích phân $\int\limits_{{{a}}}^{{{b}}} [{k}f(x) {f'+ {c}' if c>0 else f'- {abs(c)}'}]\,\mathrm{{d}}x$.'''
    choices = shuffle_choices(fr"${ans}$", [fr"${ans + 12}$", fr"${ans - 15}$", fr"${ans // 2}$"])
    loi_giai = fr'''Ta có: $\int\limits_{{{a}}}^{{{b}}} [{k}f(x) {f'+ {c}' if c>0 else f'- {abs(c)}'}]\,\mathrm{{d}}x = {k} \int\limits_{{{a}}}^{{{b}}} f(x)\,\mathrm{{d}}x + {c}({b} - {a}) = {k}({I_val}) + {term_c} = {ans}$.'''
    return caudan, choices, loi_giai


def CuoiChuong4_MC_Cau6():
    # \int_a^c = \int_a^b + \int_b^c ngẫu nhiên hóa
    a = 0
    b = random.randint(2, 4)
    c = b + random.randint(2, 4)
    u = random.randint(3, 12)
    v = random.randint(3, 12)
    ans = u + v

    caudan = fr'''Cho hàm số $f(x)$ liên tục trên $\mathbb{{R}}$ và có $\int\limits_{{{a}}}^{{{b}}} f(x)\,\mathrm{{d}}x = {u}, \int\limits_{{{b}}}^{{{c}}} f(x)\,\mathrm{{d}}x = {v}$. Tính $I = \int\limits_{{{a}}}^{{{c}}} f(x)\,\mathrm{{d}}x$.'''
    choices = shuffle_choices(fr"${ans}$", [fr"${u * v}$", fr"${abs(u - v)}$", fr"${ans + 3}$"])
    loi_giai = fr'''Ta có: $I = \int\limits_{{{a}}}^{{{c}}} f(x)\,\mathrm{{d}}x = \int\limits_{{{a}}}^{{{b}}} f(x)\,\mathrm{{d}}x + \int\limits_{{{b}}}^{{{c}}} f(x)\,\mathrm{{d}}x = {u} + {v} = {ans}$.'''
    return caudan, choices, loi_giai


def CuoiChuong4_MC_Cau7():
    # \int [m g(x) + p] = K ngẫu nhiên hóa
    a = random.randint(1, 3)
    b = a + random.randint(2, 4)
    m = random.choice([2, 3, 4])
    I_g = random.randint(2, 8)
    p = random.choice([2, 3, 4, 5])
    diff_ba = b - a
    term_p = p * diff_ba
    K = m * I_g + term_p

    caudan = fr'''Biết $\int\limits_{{{a}}}^{{{b}}} [{m}g(x) + {p}]\,\mathrm{{d}}x = {K}$. Tính tích phân $\int\limits_{{{a}}}^{{{b}}} g(x)\,\mathrm{{d}}x$.'''
    choices = shuffle_choices(fr"${I_g}$", [fr"${I_g + 2}$", fr"${K}$", fr"${I_g - 1}$"])
    loi_giai = fr'''Ta có $\int\limits_{{{a}}}^{{{b}}} [{m}g(x) + {p}]\,\mathrm{{d}}x = {m} \int\limits_{{{a}}}^{{{b}}} g(x)\,\mathrm{{d}}x + {p}({b} - {a}) = {m}I + {term_p} = {K}$. \\
Suy ra $I = \dfrac{{{K} - {term_p}}}{{{m}}} = {I_g}$.'''
    return caudan, choices, loi_giai


def CuoiChuong4_MC_Cau8():
    # \int [f(x) - g(x)] ngẫu nhiên hóa
    a = random.randint(1, 3)
    b = a + random.randint(2, 4)
    u = random.randint(6, 15)
    v = random.randint(-8, -2)
    ans = u - v

    caudan = fr'''Cho $\int\limits_{{{a}}}^{{{b}}} f(x)\,\mathrm{{d}}x = {u}$ và $\int\limits_{{{a}}}^{{{b}}} g(x)\,\mathrm{{d}}x = {v}$. Giá trị $\int\limits_{{{a}}}^{{{b}}} [f(x) - g(x)]\,\mathrm{{d}}x$ bằng:'''
    choices = shuffle_choices(fr"${ans}$", [fr"${u + v}$", fr"${u}$", fr"${v}$"])
    loi_giai = fr'''Ta có: $\int\limits_{{{a}}}^{{{b}}} [f(x) - g(x)]\,\mathrm{{d}}x = \int\limits_{{{a}}}^{{{b}}} f(x)\,\mathrm{{d}}x - \int\limits_{{{a}}}^{{{b}}} g(x)\,\mathrm{{d}}x = {u} - ({v}) = {ans}$.'''
    return caudan, choices, loi_giai


def CuoiChuong4_MC_Cau9():
    # \int k f(x) ngẫu nhiên hóa
    a = -1
    b = random.choice([3, 4, 5])
    k = random.choice([2, 3, 4, 5])
    u = random.randint(2, 6)
    ans = k * u

    caudan = fr'''Nếu $\int\limits_{{{a}}}^{{{b}}} f(x)\,\mathrm{{d}}x = {u}$ thì $\int\limits_{{{a}}}^{{{b}}} {k}f(x)\,\mathrm{{d}}x$ bằng?'''
    choices = shuffle_choices(fr"${ans}$", [fr"${u}$", fr"${-ans}$", fr"${ans + k}$"])
    loi_giai = fr'''Ta có $\int\limits_{{{a}}}^{{{b}}} {k}f(x)\,\mathrm{{d}}x = {k} \int\limits_{{{a}}}^{{{b}}} f(x)\,\mathrm{{d}}x = {k} \times {u} = {ans}$.'''
    return caudan, choices, loi_giai


def CuoiChuong4_MC_Cau10():
    # \int f'(x) dx = f(b) - f(a) ngẫu nhiên hóa
    m = random.choice([1, 2, 3])
    n = random.choice([-4, -2, 2, 4])
    p = random.choice([2024, 2025, 2026])
    a = random.choice([-3, -2, -1])
    b = random.choice([1, 2, 3])
    f_b = m * (b**2) + n * b + p
    f_a = m * (a**2) + n * a + p
    ans = f_b - f_a

    n_str = f"+ {n}x" if n > 0 else f"- {abs(n)}x"
    caudan = fr'''Cho hàm số $f(x) = {m if m>1 else ''}x^2 {n_str} - {p}$. Tính $I = \int\limits_{{{a}}}^{{{b}}} f'(x)\,\mathrm{{d}}x$'''
    choices = shuffle_choices(fr"${ans}$", [fr"${ans - 2}$", fr"${ans + 2}$", fr"${-ans}$"])
    loi_giai = fr'''Theo công thức Newton - Leibniz:
$I = \int\limits_{{{a}}}^{{{b}}} f'(x)\,\mathrm{{d}}x = f({b}) - f({a}) = [{m}({b})^2 {n_str} - {p}] - [{m}({a})^2 {n_str} - {p}] = {ans}$.'''
    return caudan, choices, loi_giai


# ==============================================================================
# CHƯƠNG II: VECTƠ VÀ HỆ TRỤC TOẠ ĐỘ TRONG KHÔNG GIAN (8 DẠNG)
# ==============================================================================

def CuoiChuong2_MC_Cau21():
    # Mặt phẳng song song trong hình hộp ngẫu nhiên hóa
    pairs = [
        {"plane": "(DA'C')", "parallel": "(B'AC)", "wrongs": ["(BDA')", "(D'AC)", "(ABC)"]},
        {"plane": "(BDC')",  "parallel": "(B'A'D)", "wrongs": ["(BAC)", "(A'B'C')", "(ABD)"]},
        {"plane": "(BDA')",  "parallel": "(B'C'D)", "wrongs": ["(ABC)", "(CDA')", "(A'B'C)"]},
    ]
    p = random.choice(pairs)
    caudan = fr'''Cho hình hộp $ABCD.A'B'C'D'$. Mặt phẳng ${p["plane"]}$ song song với mặt phẳng nào sau đây?
\begin{{center}}
\begin{{tikzpicture}}[font=\footnotesize, scale=0.8]
\coordinate (A') at (1, 0.5);
\coordinate (B') at (0, -1);
\coordinate (C') at (4, -1);
\coordinate (D') at (5, 0.5);
\coordinate (A) at (1, 3.5);
\coordinate (B) at (0, 2);
\coordinate (C) at (4, 2);
\coordinate (D) at (5, 3.5);

\draw[dashed] (A) -- (A') (A') -- (B') (A') -- (D');
\draw (A) -- (B) -- (C) -- (D) -- cycle;
\draw (B') -- (C') -- (D');
\draw (B) -- (B') (C) -- (C') (D) -- (D');

\fill (A) circle (1.5pt) node[above] {{$A$}};
\fill (B) circle (1.5pt) node[left] {{$B$}};
\fill (C) circle (1.5pt) node[above] {{$C$}};
\fill (D) circle (1.5pt) node[right] {{$D$}};
\fill (A') circle (1.5pt) node[below right] {{$A'$}};
\fill (B') circle (1.5pt) node[left] {{$B'$}};
\fill (C') circle (1.5pt) node[below] {{$C'$}};
\fill (D') circle (1.5pt) node[right] {{$D'$}};
\end{{tikzpicture}}
\end{{center}}'''
    choices = shuffle_choices(fr"${p['parallel']}$", [fr"${w}$" for w in p["wrongs"]])
    loi_giai = fr'''Trong hình hộp $ABCD.A'B'C'D'$, hai mặt phẳng ${p["plane"]}$ và ${p["parallel"]}$ chứa các cặp đường thẳng tương ứng song song nên song song với nhau.'''
    return caudan, choices, loi_giai


def CuoiChuong2_MC_Cau22():
    # Quy tắc hình hộp vectơ ngẫu nhiên hóa
    cfgs = [
        {"correct": r"\overrightarrow{AA'} + \overrightarrow{AC} = \overrightarrow{AC'}",
         "wrongs": [r"\overrightarrow{AA'} + \overrightarrow{AB} + \overrightarrow{AD} = \overrightarrow{AC}",
                    r"\overrightarrow{AB} + \overrightarrow{AD} = \overrightarrow{AC'}",
                    r"\overrightarrow{AB} + \overrightarrow{AC} = \overrightarrow{AD}"],
         "exp": r"Xét hình bình hành $ACC'A'$, ta có $\overrightarrow{AA'} + \overrightarrow{AC} = \overrightarrow{AC'}$."},
        {"correct": r"\overrightarrow{BB'} + \overrightarrow{BD} = \overrightarrow{BD'}",
         "wrongs": [r"\overrightarrow{BB'} + \overrightarrow{BA} + \overrightarrow{BC} = \overrightarrow{BD}",
                    r"\overrightarrow{BA} + \overrightarrow{BC} = \overrightarrow{BD'}",
                    r"\overrightarrow{BA} + \overrightarrow{BD} = \overrightarrow{BC}"],
         "exp": r"Xét hình bình hành $BDD'B'$, ta có $\overrightarrow{BB'} + \overrightarrow{BD} = \overrightarrow{BD'}$."},
    ]
    c = random.choice(cfgs)
    caudan = r'''Cho hình hộp $ABCD.A'B'C'D'$. Phát biểu nào sau đây là đúng?'''
    choices = shuffle_choices(fr"${c['correct']}$", [fr"${w}$" for w in c["wrongs"]])
    loi_giai = c["exp"]
    return caudan, choices, loi_giai


def CuoiChuong2_MC_Cau23():
    # Hiệu hai vectơ ngẫu nhiên hóa tên điểm
    letters = random.choice([("M", "B", "L"), ("S", "A", "C"), ("P", "Q", "R"), ("K", "E", "F")])
    O, A, B = letters
    caudan = fr'''Trong không gian, cho ba điểm phân biệt ${O}, {A}, {B}$. Tìm khẳng định đúng.'''
    correct = fr"\overrightarrow{{{O}{A}}} - \overrightarrow{{{O}{B}}} = \overrightarrow{{{B}{A}}}"
    wrongs = [
        fr"\overrightarrow{{{O}{B}}} - \overrightarrow{{{A}{B}}} = \overrightarrow{{{A}{O}}}",
        fr"\overrightarrow{{{O}{A}}} + \overrightarrow{{{O}{B}}} = \overrightarrow{{{B}{A}}}",
        fr"\overrightarrow{{{O}{B}}} + \overrightarrow{{{A}{B}}} = \overrightarrow{{{O}{A}}}"
    ]
    choices = shuffle_choices(fr"${correct}$", [fr"${w}$" for w in wrongs])
    loi_giai = fr'''Theo quy tắc trừ hai vectơ chung gốc: $\overrightarrow{{{O}{A}}} - \overrightarrow{{{O}{B}}} = \overrightarrow{{{B}{A}}}$.'''
    return caudan, choices, loi_giai


def CuoiChuong2_MC_Cau24():
    # Mệnh đề sai vectơ trong hình lập phương ngẫu nhiên hóa
    caudan = r'''Cho hình lập phương $ABCD.A'B'C'D'$. Phát biểu nào sau đây là \textbf{\underline{Sai}}?'''
    wrong_stmt = r"\overrightarrow{AB} + \overrightarrow{BC'} + \overrightarrow{C'D'} = \overrightarrow{AC'}"
    correct_stmts = [
        r"\overrightarrow{AB} + \overrightarrow{BB'} = \overrightarrow{AB'}",
        r"\overrightarrow{AB} + \overrightarrow{AA'} + \overrightarrow{AD} = \overrightarrow{AC'}",
        r"\overrightarrow{CC'} + \overrightarrow{CD} = \overrightarrow{CD'}"
    ]
    choices = shuffle_choices(fr"${wrong_stmt}$", [fr"${c}$" for c in correct_stmts])
    loi_giai = r'''Ta có $\overrightarrow{AB} + \overrightarrow{BC'} + \overrightarrow{C'D'} = \overrightarrow{AC'} + \overrightarrow{C'D'} = \overrightarrow{AD'} \ne \overrightarrow{AC'}$. Do đó khẳng định này là sai.'''
    return caudan, choices, loi_giai


def CuoiChuong2_MC_Cau25():
    # Vectơ trong tứ diện ngẫu nhiên hóa
    midpoints = [
        {"mid": "G", "seg": "SC", "ans": r"\overrightarrow{AS} + \overrightarrow{AC} = 2\overrightarrow{AG}"},
        {"mid": "E", "seg": "SA", "ans": r"\overrightarrow{BS} + \overrightarrow{BA} = 2\overrightarrow{BE}"},
        {"mid": "F", "seg": "SB", "ans": r"\overrightarrow{CS} + \overrightarrow{CB} = 2\overrightarrow{CF}"},
    ]
    m = random.choice(midpoints)
    caudan = fr'''Cho tứ diện $SABC$. Gọi $E, F, G$ lần lượt là trung điểm của các đoạn $SA, SB, SC$. Khẳng định nào sau đây là đúng?'''
    choices = shuffle_choices(fr"${m['ans']}$",
                             [r"$\overrightarrow{AS} - \overrightarrow{BA} = 2\overrightarrow{FA}$",
                              r"$\overrightarrow{BA} - \overrightarrow{SB} = 2\overrightarrow{BE}$",
                              r"$\overrightarrow{CS} + \overrightarrow{CB} = \overrightarrow{FC}$"])
    loi_giai = fr'''Vì ${m["mid"]}$ là trung điểm của đoạn thẳng ${m["seg"]}$ nên ${m["ans"]}$.'''
    return caudan, choices, loi_giai


def CuoiChuong2_MC_Cau26():
    # Vectơ hình hộp AC' = AB + AA' + AD ngẫu nhiên hóa
    caudan = r'''Cho hình hộp $ABCD.A'B'C'D'$. Phát biểu nào sau đây là đúng?'''
    choices = shuffle_choices(r"$\overrightarrow{AB} + \overrightarrow{AA'} + \overrightarrow{AD} = \overrightarrow{AC'}$",
                             [r"$\overrightarrow{AB} + \overrightarrow{AC} + \overrightarrow{AA'} = \overrightarrow{AC'}$",
                              r"$\overrightarrow{AB} + \overrightarrow{BB'} + \overrightarrow{B'A'} = \overrightarrow{AC'}$",
                              r"$\overrightarrow{AB} + \overrightarrow{BC'} + \overrightarrow{C'D'} = \overrightarrow{AC'}$"])
    loi_giai = r'''Theo quy tắc hình hộp: $\overrightarrow{AB} + \overrightarrow{AD} + \overrightarrow{AA'} = \overrightarrow{AC'}$.'''
    return caudan, choices, loi_giai


def CuoiChuong2_MC_Cau27():
    # Vectơ lập phương AC1 = AA1 + AD + AB ngẫu nhiên hóa
    caudan = r'''Cho hình lập phương $ABCD.A_1B_1C_1D_1$. Mệnh đề nào sau đây đúng?'''
    choices = shuffle_choices(r"$\overrightarrow{AC_1} = \overrightarrow{AA_1} + \overrightarrow{AD} + \overrightarrow{AB}$",
                             [r"$\overrightarrow{AC_1} = \overrightarrow{AB} + \overrightarrow{AD}$",
                              r"$\overrightarrow{AC_1} = \overrightarrow{AA_1} + \overrightarrow{AD}$",
                              r"$\overrightarrow{AC_1} = \overrightarrow{AA_1} + \overrightarrow{AB}$"])
    loi_giai = r'''Theo quy tắc hình hộp áp dụng cho hình lập phương: $\overrightarrow{AC_1} = \overrightarrow{AB} + \overrightarrow{AD} + \overrightarrow{AA_1}$.'''
    return caudan, choices, loi_giai


def CuoiChuong2_MC_Cau28():
    # Hình hộp chữ nhật khẳng định sai ngẫu nhiên hóa
    caudan = r'''Cho hình hộp chữ nhật $ABCD.A'B'C'D'$. Khẳng định nào sau đây \textbf{sai}?'''
    choices = shuffle_choices(r"$\overrightarrow{AB} = \overrightarrow{C'D'}$",
                             [r"$\overrightarrow{AB} + \overrightarrow{AD} = \overrightarrow{AC}$",
                              r"$\overrightarrow{BA} + \overrightarrow{BC} + \overrightarrow{BB'} = \overrightarrow{BD'}$",
                              r"$\overrightarrow{A'C'} = \overrightarrow{AC}$"])
    loi_giai = r'''Ta có $\overrightarrow{AB} = \overrightarrow{DC} = \overrightarrow{D'C'}$, do đó $\overrightarrow{AB} = \overrightarrow{C'D'}$ là sai vì ngược hướng.'''
    return caudan, choices, loi_giai


# ==============================================================================
# CHƯƠNG V: PHƯƠNG PHÁP TOẠ ĐỘ TRONG KHÔNG GIAN OXYZ (9 DẠNG)
# ==============================================================================

def CuoiChuong5_MC_Cau2():
    # VTCP của d: (x - x0)/a = -y/b = (z - z0)/c ngẫu nhiên hóa
    k = random.choice([2, 3])
    u1 = random.choice([-2, 2, -1, 1])
    u2 = random.choice([-1, 1, -2, 2])
    u3 = random.choice([3, -3, 2, -2])
    a = k * u1
    b = -k * u2
    c = k * u3
    x0 = random.randint(1, 4)
    z0 = random.randint(-4, -1)

    caudan = fr'''Trong không gian $Oxyz$, cho đường thẳng $d: \dfrac{{x - {x0}}}{{{a}}} = \dfrac{{-y}}{{{b}}} = \dfrac{{z {f'- {z0}' if z0>0 else f'+ {abs(z0)}'}}}{{{c}}}$. Vectơ nào dưới đây là một vectơ chỉ phương của $d$?'''
    correct = fr"\vec{{u}}_1 = ({u1}; {u2}; {u3})"
    wrongs = [
        fr"\vec{{u}}_2 = ({-u1}; {u2}; {u3})",
        fr"\vec{{u}}_3 = ({x0}; 0; {z0})",
        fr"\vec{{u}}_4 = ({a}; {b}; {c})"
    ]
    choices = shuffle_choices(fr"${correct}$", [fr"${w}$" for w in wrongs])
    loi_giai = fr'''Đưa phương trình về dạng chính tắc: $\dfrac{{x - {x0}}}{{{a}}} = \dfrac{{y}}{{{-b}}} = \dfrac{{z {f'- {z0}' if z0>0 else f'+ {abs(z0)}'}}}{{{c}}}$. \\
Vectơ chỉ phương của $d$ là $\vec{{v}} = ({a}; {-b}; {c}) = {k}({u1}; {u2}; {u3})$. \\
Do đó $\vec{{u}}_1 = ({u1}; {u2}; {u3})$ là một vectơ chỉ phương của $d$.'''
    return caudan, choices, loi_giai


def CuoiChuong5_MC_Cau3():
    # Đường thẳng qua B song song Delta_1 ngẫu nhiên hóa
    xB = random.choice([1, 2, 3])
    yB = random.choice([4, 5, 6])
    zB = random.choice([-3, -2, -1])
    u1, u2, u3 = random.choice([(4, 9, 3), (2, 3, 5), (3, 4, 1), (1, 2, 4)])

    caudan = fr'''Trong không gian $Oxyz$, đường thẳng $d$ đi qua điểm $B({xB}; {yB}; {zB})$ và song song với đường thẳng $\Delta_1 \colon \dfrac{{x+2}}{{-{u1}}} = \dfrac{{y-2}}{{-{u2}}} = \dfrac{{z+5}}{{-{u3}}}$ có phương trình là'''
    correct = fr"\begin{{cases}} x = {xB} + {u1}t \\ y = {yB} + {u2}t \\ z = {zB} + {u3}t \end{{cases}}"
    wrongs = [
        fr"\begin{{cases}} x = {xB} + {u1}t \\ y = {yB} - {u2}t \\ z = {zB} + {u3}t \end{{cases}}",
        fr"\begin{{cases}} x = {u1} + {xB}t \\ y = {u2} + {yB}t \\ z = {u3} + {zB}t \end{{cases}}",
        fr"\begin{{cases}} x = -{xB} + {u1}t \\ y = -{yB} + {u2}t \\ z = -{zB} + {u3}t \end{{cases}}"
    ]
    choices = shuffle_choices(fr"${correct}$", [fr"${w}$" for w in wrongs])
    loi_giai = fr'''Đường thẳng $\Delta_1$ có VTCP $\vec{{u}} = (-{u1}; -{u2}; -{u3}) = -({u1}; {u2}; {u3})$. \\
Vì $d \parallel \Delta_1$ và $d$ qua $B({xB}; {yB}; {zB})$ nên phương trình tham số của $d$ là $\begin{{cases}} x = {xB} + {u1}t \\ y = {yB} + {u2}t \\ z = {zB} + {u3}t \end{{cases}}$.'''
    return caudan, choices, loi_giai


def CuoiChuong5_MC_Cau4():
    # m d - n w ngẫu nhiên hóa
    dx, dy, dz = random.choice([(-5, -4, 7), (-3, 2, 4), (1, -2, 3), (-4, 1, 5)])
    wx, wy, wz = random.choice([(-3, -6, 10), (-2, 1, 3), (2, -1, 4), (-1, -3, 2)])
    m, n = 3, 2
    ans_x = m * dx - n * wx
    ans_y = m * dy - n * wy
    ans_z = m * dz - n * wz

    caudan = fr'''Trong hệ trục tọa độ $Oxyz$, cho hai vectơ $\vec{{d}}=({dx}; {dy}; {dz})$ và $\vec{{w}}=({wx}; {wy}; {wz})$. Tọa độ vectơ $3\vec{{d}} - 2\vec{{w}}$ là'''
    correct = fr"({ans_x}; {ans_y}; {ans_z})"
    wrongs = [
        fr"({ans_x + 1}; {ans_y - 2}; {ans_z + 3})",
        fr"({ans_x - 3}; {ans_y + 1}; {ans_z - 2})",
        fr"({-ans_x}; {ans_y}; {ans_z})"
    ]
    choices = shuffle_choices(fr"${correct}$", [fr"${w}$" for w in wrongs])
    loi_giai = fr'''$3\vec{{d}} = ({m*dx}; {m*dy}; {m*dz})$, $2\vec{{w}} = ({n*wx}; {n*wy}; {n*wz})$. \\
Suy ra $3\vec{{d}} - 2\vec{{w}} = ({m*dx} - ({n*wx}); {m*dy} - ({n*wy}); {m*dz} - ({n*wz})) = ({ans_x}; {ans_y}; {ans_z})$.'''
    return caudan, choices, loi_giai


def CuoiChuong5_MC_Cau5():
    # Điểm thuộc đường thẳng Delta ngẫu nhiên hóa
    x0, y0, z0 = random.choice([(-6, 2, -1), (1, -3, 2), (-2, 4, 1), (3, -1, -2)])
    a, b, c = random.choice([(1, 7, 4), (2, 3, -1), (1, -2, 3), (3, 1, 2)])
    t_val = random.choice([-2, -1, 1, 2])
    px, py, pz = x0 + a*t_val, y0 + b*t_val, z0 + c*t_val

    caudan = fr'''Trong không gian $Oxyz$, cho đường thẳng $\Delta \colon \begin{{cases}} x = {x0} + {f'{a}' if a!=1 else ''}t \\ y = {y0} + {f'{b}' if b!=1 else ''}t \\ z = {z0} + {f'{c}' if c!=1 else ''}t \end{{cases}}$. Đường thẳng $\Delta$ đi qua điểm nào trong các điểm sau?'''
    correct = fr"A({px}; {py}; {pz})"
    wrongs = [
        fr"B({px+2}; {py}; {pz-1})",
        fr"C({-px}; {py}; {pz})",
        fr"D({a}; {b}; {c})"
    ]
    choices = shuffle_choices(fr"${correct}$", [fr"${w}$" for w in wrongs])
    loi_giai = fr'''Thay $t = {t_val}$ vào phương trình tham số:
$x = {x0} + ({a})({t_val}) = {px}$, $y = {y0} + ({b})({t_val}) = {py}$, $z = {z0} + ({c})({t_val}) = {pz}$.
Vậy điểm $A({px}; {py}; {pz}) \in \Delta$.'''
    return caudan, choices, loi_giai


def CuoiChuong5_MC_Cau6():
    # u = 2a + 3b - 2c ngẫu nhiên hóa
    ax, ay, az = random.choice([(2, -3, 3), (1, 2, -1), (-1, 3, 2)])
    bx, by, bz = random.choice([(0, 2, -1), (2, 0, 1), (-2, 1, 0)])
    cx, cy, cz = random.choice([(3, -1, 4), (1, 1, 2), (0, -2, 3)])
    ux = 2*ax + 3*bx - 2*cx
    uy = 2*ay + 3*by - 2*cy
    uz = 2*az + 3*bz - 2*cz

    caudan = fr'''Trong không gian với hệ tọa độ $Oxyz$, cho $\vec{{a}} = ({ax}; {ay}; {az})$, $\vec{{b}} = ({bx}; {by}; {bz})$, $\vec{{c}} = ({cx}; {cy}; {cz})$. Tìm tọa độ của vectơ $\vec{{u}} = 2\vec{{a}} + 3\vec{{b}} - 2\vec{{c}}$.'''
    correct = fr"({ux}; {uy}; {uz})"
    wrongs = [
        fr"({ux + 2}; {uy - 1}; {uz + 3})",
        fr"({ux}; {uy}; {-uz})",
        fr"({-ux}; {uy}; {uz})"
    ]
    choices = shuffle_choices(fr"${correct}$", [fr"${w}$" for w in wrongs])
    loi_giai = fr'''Tọa độ của $\vec{{u}}$ là: \\
$x_u = 2({ax}) + 3({bx}) - 2({cx}) = {ux}$. \\
$y_u = 2({ay}) + 3({by}) - 2({cy}) = {uy}$. \\
$z_u = 2({az}) + 3({bz}) - 2({cz}) = {uz}$. \\
Vậy $\vec{{u}} = ({ux}; {uy}; {uz})$.'''
    return caudan, choices, loi_giai


def CuoiChuong5_MC_Cau7():
    # Pt chính tắc qua A, VTCP u ngẫu nhiên hóa
    x0, y0, z0 = random.choice([(1, 0, -2), (2, -1, 3), (-1, 2, 0), (0, 3, -1)])
    a, b, c = random.choice([(2, -1, 3), (1, 2, -2), (3, -2, 1), (-2, 1, 4)])

    caudan = fr'''Trong không gian $Oxyz$, đường thẳng đi qua điểm $A({x0}; {y0}; {z0})$ và có vectơ chỉ phương $\vec{{u}} = ({a}; {b}; {c})$ có phương trình chính tắc là:'''
    x_part = fr"\dfrac{{x - {x0}}}{{{a}}}" if x0 != 0 else fr"\dfrac{{x}}{{{a}}}"
    y_part = fr"\dfrac{{y - {y0}}}{{{b}}}" if y0 > 0 else (fr"\dfrac{{y + {abs(y0)}}}{{{b}}}" if y0 < 0 else fr"\dfrac{{y}}{{{b}}}")
    z_part = fr"\dfrac{{z - {z0}}}{{{c}}}" if z0 > 0 else (fr"\dfrac{{z + {abs(z0)}}}{{{c}}}" if z0 < 0 else fr"\dfrac{{z}}{{{c}}}")
    correct = fr"{x_part} = {y_part} = {z_part}"

    wrongs = [
        fr"\dfrac{{x + {abs(x0)+1}}}{{{a}}} = {y_part} = {z_part}",
        fr"\dfrac{{x}}{{{a}}} = \dfrac{{y - 1}}{{{b}}} = {z_part}",
        fr"{x_part} = {y_part} = \dfrac{{z - 1}}{{{c}}}"
    ]
    choices = shuffle_choices(fr"${correct}$", [fr"${w}$" for w in wrongs])
    loi_giai = fr'''Phương trình chính tắc của đường thẳng đi qua $A(x_0; y_0; z_0)$ có VTCP $\vec{{u}}(a; b; c)$ là $\dfrac{{x-x_0}}{{a}} = \dfrac{{y-y_0}}{{b}} = \dfrac{{z-z_0}}{{c}}$. \\
Thay tọa độ điểm $A({x0}; {y0}; {z0})$ và $\vec{{u}}({a}; {b}; {c})$ ta được phương trình đúng: ${correct}$.'''
    return caudan, choices, loi_giai


def CuoiChuong5_MC_Cau8():
    # d = a - b + 2c ngẫu nhiên hóa
    ax, ay, az = random.choice([(1, 2, 3), (2, -1, 1), (-1, 0, 2)])
    bx, by, bz = random.choice([(2, 2, -1), (1, 1, 0), (0, -2, 1)])
    cx, cy, cz = random.choice([(4, 0, -4), (3, -1, 2), (1, 2, -1)])
    dx = ax - bx + 2*cx
    dy = ay - by + 2*cy
    dz = az - bz + 2*cz

    caudan = fr'''Trong không gian với hệ trục toạ độ $Oxyz$, cho ba vectơ $\vec{{a}}({ax}; {ay}; {az}), \vec{{b}}({bx}; {by}; {bz}), \vec{{c}}({cx}; {cy}; {cz})$. Toạ độ của vectơ $\vec{{d}} = \vec{{a}} - \vec{{b}} + 2\vec{{c}}$ là'''
    correct = fr"\vec{{d}}({dx}; {dy}; {dz})"
    wrongs = [
        fr"\vec{{d}}({dx}; {dy}; {-dz})",
        fr"\vec{{d}}({-dx}; {dy}; {dz})",
        fr"\vec{{d}}({-dx}; {-dy}; {-dz})"
    ]
    choices = shuffle_choices(fr"${correct}$", [fr"${w}$" for w in wrongs])
    loi_giai = fr'''Tọa độ vectơ $\vec{{d}}$ là: \\
$x = {ax} - ({bx}) + 2({cx}) = {dx}$. \\
$y = {ay} - ({by}) + 2({cy}) = {dy}$. \\
$z = {az} - ({bz}) + 2({cz}) = {dz}$. \\
Vậy $\vec{{d}}({dx}; {dy}; {dz})$.'''
    return caudan, choices, loi_giai


def CuoiChuong5_MC_Cau9():
    # Pt đường thẳng song song d ngẫu nhiên hóa
    xA, yA, zA = random.choice([(1, 2, 3), (2, -1, 4), (-1, 3, 2), (3, 1, -2)])
    u1, u2, u3 = random.choice([(-1, 1, -4), (2, -3, 1), (1, 2, -2), (-2, 1, 3)])

    caudan = fr'''Trong không gian $, phương trình đường thẳng đi qua điểm ({xA}; {yA}; {zA})$ và song song với đường thẳng  \colon egin{{cases}} x = 1 + {u1}t \ y = {u2}t \ z = -1 + {u3}t \end{{cases}}$ là'''
    correct = fr"\dfrac{{x - {xA}}}{{{u1}}} = \dfrac{{y - {yA}}}{{{u2}}} = \dfrac{{z - {zA}}}{{{u3}}}"
    wrongs = [
        fr"\dfrac{{x + {xA}}}{{{u1}}} = \dfrac{{y + {yA}}}{{{u2}}} = \dfrac{{z + {zA}}}{{{u3}}}",
        fr"\dfrac{{x - {xA}}}{{{u2}}} = \dfrac{{y - {yA}}}{{{u1}}} = \dfrac{{z - {zA}}}{{{u3}}}",
        fr"\dfrac{{x - 1}}{{{u1}}} = \dfrac{{y}}{{{u2}}} = \dfrac{{z + 1}}{{{u3}}}"
    ]
    choices = shuffle_choices(fr"$", [fr"$" for w in wrongs])
    loi_giai = fr'''Đường thẳng $ có VTCP $ec{{u}} = ({u1}; {u2}; {u3})$. \
Đường thẳng cần tìm đi qua ({xA}; {yA}; {zA})$ và nhận $ec{{u}}$ làm VTCP nên có phương trình: $.'''
    return caudan, choices, loi_giai


def CuoiChuong5_MC_Cau10():
    # Pt tham số qua M, N ngẫu nhiên hóa
    xM, yM, zM = random.choice([(1, 1, 1), (2, -1, 0), (0, 3, 1), (-1, 2, 2)])
    xN, yN, zN = random.choice([(-2, 3, 1), (4, 1, -2), (1, -1, 3), (2, 0, 1)])
    u1 = xN - xM
    u2 = yN - yM
    u3 = zN - zM

    caudan = fr'''Phương trình tham số đường thẳng $ đi qua điểm ({xM}; {yM}; {zM})$ và ({xN}; {yN}; {zN})$ là'''
    u1_str = f"+ {u1}t" if u1 > 0 else (f"- {abs(u1)}t" if u1 < 0 else "")
    u2_str = f"+ {u2}t" if u2 > 0 else (f"- {abs(u2)}t" if u2 < 0 else "")
    u3_str = f"+ {u3}t" if u3 > 0 else (f"- {abs(u3)}t" if u3 < 0 else "")

    correct = fr"egin{{cases}} x = {xM} {u1_str} \ y = {yM} {u2_str} \ z = {zM} {u3_str} \end{{cases}}"
    wrongs = [
        fr"egin{{cases}} x = {xM} {u1_str} \ y = {yM} {u2_str} \ z = {zM} + t \end{{cases}}",
        fr"egin{{cases}} x = {xN} + t \ y = {yN} + t \ z = {zN} + t \end{{cases}}",
        fr"egin{{cases}} x = {xM + 2} {u1_str} \ y = {yM} {u2_str} \ z = {zM - 1} \end{{cases}}"
    ]
    choices = shuffle_choices(fr"$", [fr"$" for w in wrongs])
    loi_giai = fr'''Vectơ chỉ phương $\overrightarrow{{MN}} = ({u1}; {u2}; {u3})$. \
Phương trình tham số của đường thẳng đi qua ({xM}; {yM}; {zM})$ và nhận $\overrightarrow{{MN}}$ làm VTCP là: $.'''
    return caudan, choices, loi_giai


# ==============================================================================
# CHUYÊN ĐỀ ÔN TẬP TOÁN 11 (35 DẠNG) NGẪU NHIÊN HÓA TOÀN DIỆN
# ==============================================================================

# --- Khối đa diện & Quan hệ không gian 11 ---

def OnTap11_MC_Cau1():
    # Thể tích chóp S.ABC đáy đều, SA vuông góc đáy, SC cạnh bên
    pythago = [
        {"a": 3, "sc": 5, "sa": 4, "v": r"3\sqrt{3}"},
        {"a": 6, "sc": 10, "sa": 8, "v": r"24\sqrt{3}"},
        {"a": 8, "sc": 10, "sa": 6, "v": r"32\sqrt{3}"},
        {"a": 5, "sc": 13, "sa": 12, "v": r"25\sqrt{3}"},
        {"a": 12, "sc": 15, "sa": 9, "v": r"108\sqrt{3}"},
    ]
    cfg = random.choice(pythago)
    a, sc, sa, v_ans = cfg["a"], cfg["sc"], cfg["sa"], cfg["v"]
    s_base = Fraction(a**2, 4)
    
    caudan = fr'''Cho khối chóp $S.ABC$ có $SA$ vuông góc với mặt phẳng $(ABC)$, tam giác $ABC$ là tam giác đều có cạnh $AB = {a}$, cạnh bên $SC = {sc}$. Thể tích của khối chóp $S.ABC$ bằng'''
    correct = fr"${v_ans}$"
    wrongs = [
        fr"${sa}\sqrt{{3}}$",
        fr"${a * sa}$",
        fr"${a * sc}$"
    ]
    choices = shuffle_choices(correct, wrongs)
    loi_giai = fr'''Tam giác $ABC$ đều cạnh ${a}$ nên $S_{{ABC}} = \dfrac{{{a}^2\sqrt{{3}}}}{{4}} = \dfrac{{{a**2}\sqrt{{3}}}}{{4}}$. \\
Vì $SA \perp (ABC)$ nên tam giác $SAC$ vuông tại $A$. Ta có $SA = \sqrt{{SC^2 - AC^2}} = \sqrt{{{sc}^2 - {a}^2}} = {sa}$. \\
Thể tích khối chóp là: $V = \dfrac{{1}}{{3}} S_{{ABC}} \cdot SA = {v_ans}$.'''
    return caudan, choices, loi_giai


def OnTap11_MC_Cau2():
    # Thể tích hộp chữ nhật CD=a, A'D'=b, DD'=c
    a = random.choice([4, 6, 8, 10])
    b = random.choice([3, 5, 7, 9])
    c = random.choice([2, 4, 5, 6])
    v_val = a * b * c

    caudan = fr'''Cho khối hộp chữ nhật $ABCD.A'B'C'D'$ có $CD = {a}a, A'D' = {b}a, DD' = {c}a$. Thể tích $V$ của khối hộp chữ nhật đã cho bằng'''
    correct = fr"$V = {v_val}a^3$"
    wrongs = [
        fr"$V = {v_val // 2}a^3$",
        fr"$V = \dfrac{{{v_val}}}{{3}}a^3$",
        fr"$V = {v_val * 2}a^3$"
    ]
    choices = shuffle_choices(correct, wrongs)
    loi_giai = fr'''Ba kích thước của hình hộp chữ nhật lần lượt là ${a}a, {b}a, {c}a$. \\
Thể tích $V = {a}a \cdot {b}a \cdot {c}a = {v_val}a^3$.'''
    return caudan, choices, loi_giai


def OnTap11_MC_Cau3():
    # Thể tích lăng trụ đứng ABC.A'B'C' có AB = AC = a, AA' = h, góc BAC
    cases = [
        {"angle": r"45^\circ", "h": r"a\sqrt{2}", "ans": r"\dfrac{a^3}{2}"},
        {"angle": r"30^\circ", "h": r"4a", "ans": r"a^3"},
        {"angle": r"60^\circ", "h": r"a\sqrt{3}", "ans": r"\dfrac{3a^3}{4}"},
        {"angle": r"90^\circ", "h": r"2a", "ans": r"a^3"},
    ]
    c = random.choice(cases)
    caudan = fr'''Cho khối lăng trụ đứng $ABC.A'B'C'$ có $AB = AC = a, AA' = {c["h"]}, \widehat{{BAC}} = {c["angle"]}$. Tính thể tích $V$ của khối lăng trụ đã cho.'''
    correct = fr"${c['ans']}$"
    wrongs = [
        r"$\dfrac{a^3}{4}$",
        r"$\dfrac{a^3}{6}$",
        r"$\dfrac{a^3\sqrt{2}}{3}$"
    ]
    if correct in wrongs: wrongs.remove(correct)
    while len(wrongs) < 3: wrongs.append(r"$\dfrac{2a^3}{3}$")
    choices = shuffle_choices(correct, wrongs[:3])
    loi_giai = fr'''Diện tích đáy tam giác $ABC$ là: $S_{{ABC}} = \dfrac{{1}}{{2}} AB \cdot AC \cdot \sin \widehat{{BAC}}$. \\
Thể tích: $V = S_{{ABC}} \cdot AA' = {c['ans']}$.'''
    return caudan, choices, loi_giai


def OnTap11_MC_Cau4():
    # SA vuông góc đáy => SA vuông góc đường thẳng trong đáy
    edges = ["AB", "BC", "AC"]
    e = random.choice(edges)
    caudan = fr'''Cho hình chóp $S.ABC$ có $SA$ vuông góc với mặt đáy $(ABC)$. Mệnh đề nào sau đây là \textbf{{\underline{{đúng}}}}?'''
    correct = fr"$SA \perp {e}$"
    wrongs = [r"$SA \perp SC$", r"$SB \perp SC$", r"$SA \perp SB$"]
    choices = shuffle_choices(correct, wrongs)
    loi_giai = fr'''Vì $SA \perp (ABC)$ mà ${e} \subset (ABC)$ nên $SA \perp {e}$.'''
    return caudan, choices, loi_giai


def OnTap11_MC_Cau5():
    # Thể tích chóp đáy hình thang vuông
    cases = [
        {"ang": r"60^\circ", "tan": r"\sqrt{3}", "sa": r"a\sqrt{6}", "v": r"\dfrac{a^3\sqrt{6}}{2}"},
        {"ang": r"45^\circ", "tan": r"1", "sa": r"a\sqrt{2}", "v": r"\dfrac{a^3\sqrt{2}}{2}"},
        {"ang": r"30^\circ", "tan": r"\dfrac{\sqrt{3}}{3}", "sa": r"\dfrac{a\sqrt{6}}{3}", "v": r"\dfrac{a^3\sqrt{6}}{6}"},
    ]
    c = random.choice(cases)
    caudan = fr'''Cho hình chóp $S.ABCD$ có $SA \perp (ABCD)$, đáy $ABCD$ là hình thang vuông tại $A$ và $D$. Biết $AD = DC = a, AB = 2a$, góc giữa cạnh $SC$ và mặt phẳng $(ABCD)$ bằng ${c["ang"]}$. Thể tích khối chóp $S.ABCD$ là:'''
    correct = fr"$V = {c['v']}$"
    wrongs = [
        r"$V = \dfrac{a^3\sqrt{6}}{12}$",
        r"$V = \dfrac{a^3\sqrt{6}}{4}$",
        r"$V = \dfrac{a^3\sqrt{2}}{4}$"
    ]
    if correct in wrongs: wrongs.remove(correct)
    choices = shuffle_choices(correct, wrongs[:3])
    loi_giai = fr'''Diện tích đáy $ABCD$: $S = \dfrac{{(AB + CD) \cdot AD}}{{2}} = \dfrac{{(2a + a) \cdot a}}{{2}} = \dfrac{{3a^2}}{{2}}$. \\
Ta có $AC = \sqrt{{AD^2 + CD^2}} = a\sqrt{{2}}$. \\
$SA = AC \tan {c['ang']} = {c['sa']}$. \\
Thể tích: $V = \dfrac{{1}}{{3}} S \cdot SA = {c['v']}$.'''
    return caudan, choices, loi_giai


def OnTap11_MC_Cau6():
    # Góc giữa đường chéo đáy và mặt bên hình chóp S.ABCD ngẫu nhiên hóa
    cfgs = [
        {"line": "AC", "plane": "(SAD)", "proj": "AD", "perp": "CD", "ang": r"\widehat{CAD}", "deg": "45^\\circ", "wrongs": [r"\widehat{SCD}", r"\widehat{CSA}", r"\widehat{SCA}"]},
        {"line": "AC", "plane": "(SAB)", "proj": "AB", "perp": "CB", "ang": r"\widehat{CAB}", "deg": "45^\\circ", "wrongs": [r"\widehat{SCB}", r"\widehat{CSA}", r"\widehat{SCA}"]},
        {"line": "BD", "plane": "(SAB)", "proj": "AB", "perp": "DA", "ang": r"\widehat{DBA}", "deg": "45^\\circ", "wrongs": [r"\widehat{SDA}", r"\widehat{DSB}", r"\widehat{SBA}"]},
    ]
    c = random.choice(cfgs)
    caudan = fr'''Cho hình chóp $S.ABCD$ có đáy là hình vuông, $SA \perp (ABCD)$. Góc giữa đường thẳng ${c["line"]}$ và mặt phẳng ${c["plane"]}$ là'''
    choices = shuffle_choices(fr"${c['ang']}$", [fr"${w}$" for w in c["wrongs"]])
    loi_giai = fr'''Ta có ${c["perp"]} \perp {c["proj"]}$ và ${c["perp"]} \perp SA \implies {c["perp"]} \perp {c["plane"]}$. \\
Hình chiếu của ${c["line"]}$ lên ${c["plane"]}$ là ${c["proj"]}$. Do đó góc cần tìm là ${c["ang"]} = {c["deg"]}$.'''
    return caudan, choices, loi_giai


def OnTap11_MC_Cau7():
    # Chóp đáy chữ nhật AB = m*a, BC = n*a, SA = k*a
    m = random.choice([1, 2])
    n = random.choice([2, 3])
    k = random.choice([1, 3])
    num = m * n * k
    frac_str = f"\\dfrac{{{num}a^3}}{{3}}" if num % 3 != 0 else f"{num // 3}a^3"

    caudan = fr'''Cho hình chóp $S.ABCD$ có đáy $ABCD$ là hình chữ nhật, cạnh $AB = {m}a, BC = {n}a$, $SA$ vuông góc với mặt phẳng $(ABCD)$ và cạnh $SA = {k}a$. Tính theo $a$ thể tích $V$ của khối chóp $S.ABCD$.'''
    correct = fr"$V = {frac_str}$"
    wrongs = [
        fr"$V = {num}a^3$",
        fr"$V = \dfrac{{{num + 1}a^3}}{{3}}$",
        fr"$V = \dfrac{{{max(1, num - 1)}a^3}}{{3}}$"
    ]
    choices = shuffle_choices(correct, wrongs)
    loi_giai = fr'''Diện tích đáy: $S_{{ABCD}} = AB \cdot BC = {m*n}a^2$. \\
Thể tích: $V = \dfrac{{1}}{{3}} S_{{ABCD}} \cdot SA = \dfrac{{1}}{{3}} \cdot {m*n}a^2 \cdot {k}a = {frac_str}$.'''
    return caudan, choices, loi_giai


def OnTap11_MC_Cau8():
    # Chóp tam giác đều cạnh a, SA = h*a\sqrt{3}
    h = random.choice([1, 2, 3])
    num = h * 3
    frac_str = f"\\dfrac{{{h}a^3}}{{4}}"
    
    caudan = fr'''Cho hình chóp $S.ABC$ có đáy $ABC$ là tam giác đều cạnh $a$. Biết $SA \perp (ABC)$ và $SA = {f'{h}' if h > 1 else ''}a\sqrt{{3}}$. Tính thể tích khối chóp $S.ABC$.'''
    correct = fr"${frac_str}$"
    wrongs = [
        fr"$\dfrac{{{h}a^3}}{{2}}$",
        fr"$\dfrac{{{h+1}a^3}}{{4}}$",
        fr"$\dfrac{{{h}a^3}}{{6}}$"
    ]
    choices = shuffle_choices(correct, wrongs)
    loi_giai = fr'''Diện tích tam giác đều $ABC$: $S_{{ABC}} = \dfrac{{a^2\sqrt{{3}}}}{{4}}$. \\
Thể tích: $V = \dfrac{{1}}{{3}} S_{{ABC}} \cdot SA = \dfrac{{1}}{{3}} \cdot \dfrac{{a^2\sqrt{{3}}}}{{4}} \cdot {f'{h}' if h > 1 else ''}a\sqrt{{3}} = {frac_str}$.'''
    return caudan, choices, loi_giai


def OnTap11_MC_Cau9():
    # Chóp S.ABC đáy vuông tại B, AB=u, BC=v, SB=w
    u = random.choice([2, 4])
    v = random.choice([3, 6])
    w = random.choice([2, 5])
    v_val = (u * v * w) // 6

    caudan = fr'''Cho hình chóp $S.ABC$ có đáy là tam giác vuông tại $B$, $AB={u}, BC={v}$. Cạnh bên $SB$ vuông góc với đáy và $SB={w}$. Tính thể tích khối chóp $S.ABC$?'''
    correct = fr"${v_val}$"
    wrongs = [fr"${v_val + 2}$", fr"${v_val - 1}$", fr"${v_val * 2}$"]
    choices = shuffle_choices(correct, wrongs)
    loi_giai = fr'''Diện tích đáy: $S = \dfrac{{1}}{{2}} AB \cdot BC = \dfrac{{1}}{{2}} \cdot {u} \cdot {v} = {(u*v)//2}$. \\
Thể tích: $V = \dfrac{{1}}{{3}} S \cdot SB = \dfrac{{1}}{{3}} \cdot {(u*v)//2} \cdot {w} = {v_val}$.'''
    return caudan, choices, loi_giai


def OnTap11_MC_Cau10():
    # Góc giữa đường chéo mặt bên và mặt phẳng đáy lăng trụ ngẫu nhiên hóa
    cfgs = [
        {"rel": r"AA' = A'C'",            "ans": r"45^\circ", "wrongs": [r"30^\circ", r"60^\circ", r"90^\circ"], "exp": r"\tan \varphi = \dfrac{BB'}{B'C'} = 1 \implies \varphi = 45^\circ"},
        {"rel": r"AA' = A'C'\sqrt{3}",     "ans": r"60^\circ", "wrongs": [r"30^\circ", r"45^\circ", r"90^\circ"], "exp": r"\tan \varphi = \dfrac{BB'}{B'C'} = \sqrt{3} \implies \varphi = 60^\circ"},
        {"rel": r"AA' = \dfrac{A'C'}{\sqrt{3}}", "ans": r"30^\circ", "wrongs": [r"45^\circ", r"60^\circ", r"90^\circ"], "exp": r"\tan \varphi = \dfrac{BB'}{B'C'} = \dfrac{1}{\sqrt{3}} \implies \varphi = 30^\circ"},
    ]
    c = random.choice(cfgs)
    caudan = fr'''Cho lăng trụ đứng $ABC.A'B'C'$ có đáy là tam giác đều và ${c["rel"]}$. Tìm góc giữa đường thẳng $BC'$ và mặt phẳng $(A'B'C')$?'''
    choices = shuffle_choices(fr"${c['ans']}$", [fr"${w}$" for w in c["wrongs"]])
    loi_giai = fr'''Vì lăng trụ đứng nên $BB' \perp (A'B'C')$. Hình chiếu của $BC'$ lên $(A'B'C')$ là $B'C'$. \\
Tam giác $BB'C'$ vuông tại $B'$. Ta có ${c["exp"]}$. \\
Suy ra góc giữa $BC'$ và $(A'B'C')$ bằng ${c["ans"]}$.'''
    return caudan, choices, loi_giai


# --- Phương trình Lượng giác 11 ---

def OnTap11_MC_Cau11():
    # cos x = m hoặc sin x = m
    mode = random.choice(["cos1", "cos0", "sin0", "cos_m1"])
    if mode == "cos1":
        caudan = r'''Tập nghiệm của phương trình $\cos x = 1$ là'''
        correct = r"$S = \{ k2\pi \mid k \in \mathbb{Z} \}$"
        wrongs = [r"$S = \left\{ \dfrac{\pi}{2} + k2\pi \mid k \in \mathbb{Z} \right\}$",
                  r"$S = \{ \pi + k2\pi \mid k \in \mathbb{Z} \}$",
                  r"$S = \left\{ \dfrac{\pi}{2} + k\pi \mid k \in \mathbb{Z} \right\}$"]
        loi_giai = r'''Ta có $\cos x = 1 \iff x = k2\pi \ (k \in \mathbb{Z})$.'''
    elif mode == "cos0":
        caudan = r'''Tập nghiệm của phương trình $\cos x = 0$ là'''
        correct = r"$S = \left\{ \dfrac{\pi}{2} + k\pi \mid k \in \mathbb{Z} \right\}$"
        wrongs = [r"$S = \{ k2\pi \mid k \in \mathbb{Z} \}$",
                  r"$S = \left\{ \dfrac{\pi}{2} + k2\pi \mid k \in \mathbb{Z} \right\}$",
                  r"$S = \{ \pi + k\pi \mid k \in \mathbb{Z} \}$"]
        loi_giai = r'''Ta có $\cos x = 0 \iff x = \dfrac{\pi}{2} + k\pi \ (k \in \mathbb{Z})$.'''
    elif mode == "sin0":
        caudan = r'''Tập nghiệm của phương trình $\sin x = 0$ là'''
        correct = r"$S = \{ k\pi \mid k \in \mathbb{Z} \}$"
        wrongs = [r"$S = \{ k2\pi \mid k \in \mathbb{Z} \}$",
                  r"$S = \left\{ \dfrac{\pi}{2} + k\pi \mid k \in \mathbb{Z} \right\}$",
                  r"$S = \{ \pi + k2\pi \mid k \in \mathbb{Z} \}$"]
        loi_giai = r'''Ta có $\sin x = 0 \iff x = k\pi \ (k \in \mathbb{Z})$.'''
    else:
        caudan = r'''Tập nghiệm của phương trình $\cos x = -1$ là'''
        correct = r"$S = \{ \pi + k2\pi \mid k \in \mathbb{Z} \}$"
        wrongs = [r"$S = \{ k2\pi \mid k \in \mathbb{Z} \}$",
                  r"$S = \left\{ -\dfrac{\pi}{2} + k2\pi \mid k \in \mathbb{Z} \right\}$",
                  r"$S = \{ k\pi \mid k \in \mathbb{Z} \}$"]
        loi_giai = r'''Ta có $\cos x = -1 \iff x = \pi + k2\pi \ (k \in \mathbb{Z})$.'''
    choices = shuffle_choices(correct, wrongs)
    return caudan, choices, loi_giai


def OnTap11_MC_Cau12():
    # tan(k x) = \sqrt{3}
    k = random.choice([2, 3, 4])
    caudan = fr'''Giải phương trình $\tan {k}x = \sqrt{{3}}$.'''
    correct = fr"$x = \dfrac{{\pi}}{{{3*k}}} + k\dfrac{{\pi}}{{{k}}}, k \in \mathbb{{Z}}$"
    wrongs = [
        fr"$x = \dfrac{{\pi}}{{3}} + k\pi, k \in \mathbb{{Z}}$",
        fr"$x = \pm\dfrac{{\pi}}{{{3*k}}} + k\dfrac{{\pi}}{{{k}}}, k \in \mathbb{{Z}}$",
        fr"$x = \dfrac{{\pi}}{{{3*k}}} + k\pi, k \in \mathbb{{Z}}$"
    ]
    choices = shuffle_choices(correct, wrongs)
    loi_giai = fr'''$\tan {k}x = \sqrt{{3}} \iff {k}x = \dfrac{{\pi}}{{3}} + k\pi \iff x = \dfrac{{\pi}}{{{3*k}}} + k\dfrac{{\pi}}{{{k}}} \ (k \in \mathbb{{Z}})$.'''
    return caudan, choices, loi_giai


def OnTap11_MC_Cau13():
    # 2 sin x - \sqrt{3} = 0 hoặc 2 sin x - 1 = 0
    mode = random.choice(["sqrt3", "1"])
    if mode == "sqrt3":
        caudan = r'''Nghiệm của phương trình $2\sin x - \sqrt{3} = 0$ là'''
        correct = r"$\left[ \begin{array}{l} x = \dfrac{\pi}{3} + k2\pi \\ x = \dfrac{2\pi}{3} + k2\pi \end{array} \right., k \in \mathbb{Z}$"
        wrongs = [
            r"$x = \pm\dfrac{\pi}{3} + k2\pi, k \in \mathbb{Z}$",
            r"$\left[ \begin{array}{l} x = \dfrac{\pi}{6} + k2\pi \\ x = \dfrac{5\pi}{6} + k2\pi \end{array} \right., k \in \mathbb{Z}$",
            r"$x = \pm\dfrac{\pi}{6} + k2\pi, k \in \mathbb{Z}$"
        ]
        loi_giai = r'''$2\sin x - \sqrt{3} = 0 \iff \sin x = \dfrac{\sqrt{3}}{2} = \sin \dfrac{\pi}{3} \iff x = \dfrac{\pi}{3} + k2\pi$ hoặc $x = \dfrac{2\pi}{3} + k2\pi$.'''
    else:
        caudan = r'''Nghiệm của phương trình $2\sin x - 1 = 0$ là'''
        correct = r"$\left[ \begin{array}{l} x = \dfrac{\pi}{6} + k2\pi \\ x = \dfrac{5\pi}{6} + k2\pi \end{array} \right., k \in \mathbb{Z}$"
        wrongs = [
            r"$x = \pm\dfrac{\pi}{6} + k2\pi, k \in \mathbb{Z}$",
            r"$\left[ \begin{array}{l} x = \dfrac{\pi}{3} + k2\pi \\ x = \dfrac{2\pi}{3} + k2\pi \end{array} \right., k \in \mathbb{Z}$",
            r"$x = \pm\dfrac{\pi}{3} + k2\pi, k \in \mathbb{Z}$"
        ]
        loi_giai = r'''$2\sin x - 1 = 0 \iff \sin x = \dfrac{1}{2} = \sin \dfrac{\pi}{6} \iff x = \dfrac{\pi}{6} + k2\pi$ hoặc $x = \dfrac{5\pi}{6} + k2\pi$.'''
    choices = shuffle_choices(correct, wrongs)
    return caudan, choices, loi_giai


def OnTap11_MC_Cau14():
    # cos(a x) = cos(b x)
    a, b = random.choice([(3, 1), (4, 2), (5, 1)])
    s1, s2 = a - b, a + b
    caudan = fr'''Nghiệm của phương trình $\cos({a}x) = \cos({b}x)$ là'''
    correct = fr"$\left[ \begin{{array}}{{l}} x = k\dfrac{{2\pi}}{{{s1}}} \\ x = k\dfrac{{2\pi}}{{{s2}}} \end{{array}} \right., k \in \mathbb{{Z}}$"
    wrongs = [
        fr"$\left[ \begin{{array}}{{l}} x = k\dfrac{{\pi}}{{{s1}}} \\ x = k\dfrac{{\pi}}{{{s2}}} \end{{array}} \right., k \in \mathbb{{Z}}$",
        fr"$x = k2\pi, k \in \mathbb{{Z}}$",
        fr"$x = k\pi, k \in \mathbb{{Z}}$"
    ]
    choices = shuffle_choices(correct, wrongs)
    loi_giai = fr'''$\cos({a}x) = \cos({b}x) \iff {a}x = \pm {b}x + k2\pi \iff x = k\dfrac{{2\pi}}{{{s1}}}$ hoặc $x = k\dfrac{{2\pi}}{{{s2}}} \ (k \in \mathbb{{Z}})$.'''
    return caudan, choices, loi_giai


def OnTap11_MC_Cau15():
    # tan x = m
    vals = [
        (r"\sqrt{3}", r"\dfrac{\pi}{3}"),
        (r"1", r"\dfrac{\pi}{4}"),
        (r"-\sqrt{3}", r"-\dfrac{\pi}{3}"),
        (r"-1", r"-\dfrac{\pi}{4}"),
    ]
    m_str, alpha = random.choice(vals)
    caudan = fr'''Phương trình $\tan x = {m_str}$ có tập nghiệm là'''
    correct = fr"$S = \left\{{ {alpha} + k\pi \mid k \in \mathbb{{Z}} \right\}}$"
    wrongs = [
        fr"$S = \left\{{ {alpha} + k2\pi \mid k \in \mathbb{{Z}} \right\}}$",
        fr"$S = \left\{{ \pm {alpha} + k\pi \mid k \in \mathbb{{Z}} \right\}}$",
        fr"$S = \left\{{ \pm {alpha} + k2\pi \mid k \in \mathbb{{Z}} \right\}}$"
    ]
    choices = shuffle_choices(correct, wrongs)
    loi_giai = fr'''$\tan x = {m_str} \iff x = {alpha} + k\pi \ (k \in \mathbb{{Z}})$.'''
    return caudan, choices, loi_giai


def OnTap11_MC_Cau16():
    # cos x = m
    vals = [
        (r"\dfrac{1}{2}", r"\dfrac{\pi}{3}"),
        (r"\dfrac{\sqrt{2}}{2}", r"\dfrac{\pi}{4}"),
        (r"\dfrac{\sqrt{3}}{2}", r"\dfrac{\pi}{6}"),
        (r"-\dfrac{1}{2}", r"\dfrac{2\pi}{3}"),
    ]
    m_str, alpha = random.choice(vals)
    caudan = fr'''Nghiệm của phương trình $\cos x = {m_str}$ là'''
    correct = fr"$x = \pm {alpha} + k2\pi \quad (k \in \mathbb{{Z}})$"
    wrongs = [
        fr"$x = {alpha} + k\pi \quad (k \in \mathbb{{Z}})$",
        fr"$x = \pm {alpha} + k\pi \quad (k \in \mathbb{{Z}})$",
        r"$x = \dfrac{\pi}{2} + k2\pi \quad (k \in \mathbb{Z})$"
    ]
    choices = shuffle_choices(correct, wrongs)
    loi_giai = fr'''$\cos x = {m_str} = \cos\left({alpha}\right) \iff x = \pm {alpha} + k2\pi \ (k \in \mathbb{{Z}})$.'''
    return caudan, choices, loi_giai


# --- Đạo hàm 11 ---

def OnTap11_MC_Cau17():
    # Đạo hàm a sin x + b cos x
    a = random.choice([1, 2, 3])
    b = random.choice([1, 2, 3])
    caudan = fr'''Đạo hàm của hàm số $f(x) = {a if a > 1 else ''}\sin x + {b if b > 1 else ''}\cos x$ là'''
    correct = fr"${a if a > 1 else ''}\cos x - {b if b > 1 else ''}\sin x$"
    wrongs = [
        fr"${a if a > 1 else ''}\cos x + {b if b > 1 else ''}\sin x$",
        fr"$-{a if a > 1 else ''}\cos x - {b if b > 1 else ''}\sin x$",
        fr"${b if b > 1 else ''}\cos x - {a if a > 1 else ''}\sin x$"
    ]
    choices = shuffle_choices(correct, wrongs)
    loi_giai = fr'''$f'(x) = {a if a > 1 else ''}(\sin x)' + {b if b > 1 else ''}(\cos x)' = {a if a > 1 else ''}\cos x - {b if b > 1 else ''}\sin x$.'''
    return caudan, choices, loi_giai


def OnTap11_MC_Cau18():
    # Đạo hàm a^x
    a = random.choice([2, 3, 5, 7, 8, 9, 10])
    caudan = fr'''Tính đạo hàm của hàm số $y = {a}^x$.'''
    correct = fr"$y' = {a}^x \ln {a}$"
    wrongs = [
        fr"$y' = {a}^x \log {a}$",
        fr"$y' = {a}^x$",
        fr"$y' = \dfrac{{{a}^x}}{{\ln {a}}}$"
    ]
    choices = shuffle_choices(correct, wrongs)
    loi_giai = fr'''Áp dụng công thức $(a^x)' = a^x \ln a$, ta có $({a}^x)' = {a}^x \ln {a}$.'''
    return caudan, choices, loi_giai


def OnTap11_MC_Cau19():
    # Đạo hàm a x + b cos x
    a = random.choice([1, 2, 3, 5])
    caudan = fr'''Cho hàm số $y = {a if a > 1 else ''}x + \cos x$. Đạo hàm của hàm số là:'''
    correct = fr"$y' = {a} - \sin x$"
    wrongs = [
        fr"$y' = {a} + \sin x$",
        fr"$y' = 1 - \sin x$",
        fr"$y' = {a}x - \sin x$"
    ]
    choices = shuffle_choices(correct, wrongs)
    loi_giai = fr'''$y' = ({a if a > 1 else ''}x)' + (\cos x)' = {a} - \sin x$.'''
    return caudan, choices, loi_giai


def OnTap11_MC_Cau20():
    # Đạo hàm m sin x + n cos x
    m = random.choice([3, 4, 5, 6])
    n = random.choice([2, 7, 8, 9])
    caudan = fr'''Tính đạo hàm của hàm số $y = {m}\sin x + {n}\cos x$.'''
    correct = fr"$y' = {m}\cos x - {n}\sin x$"
    wrongs = [
        fr"$y' = {n}\sin x + {m}\cos x$",
        fr"$y' = -{n}\sin x - {m}\cos x$",
        fr"$y' = {m}\cos x + {n}\sin x$"
    ]
    choices = shuffle_choices(correct, wrongs)
    loi_giai = fr'''$y' = {m}(\sin x)' + {n}(\cos x)' = {m}\cos x - {n}\sin x$.'''
    return caudan, choices, loi_giai


def OnTap11_MC_Cau21():
    # Đạo hàm a^{x^2 - b x - c}
    a = random.choice([2, 3, 5])
    b = random.choice([2, 3, 4])
    c = random.choice([1, 2, 5])
    caudan = fr'''Tính đạo hàm của hàm số $y = {a}^{{x^2 - {b}x - {c}}}$?'''
    correct = fr"$y' = (2x - {b}) {a}^{{x^2 - {b}x - {c}}} \ln {a}$"
    wrongs = [
        fr"$y' = {a}^{{x^2 - {b}x - {c}}} \ln {a}$",
        fr"$y' = \dfrac{{{a}^{{x^2 - {b}x - {c}}}}}{{\ln {a}}}$",
        fr"$y' = (2x - {b}) {a}^{{x^2 - {b}x - {c}}}$"
    ]
    choices = shuffle_choices(correct, wrongs)
    loi_giai = fr'''$(a^u)' = u' \cdot a^u \ln a \implies y' = (x^2 - {b}x - {c})' \cdot {a}^{{x^2 - {b}x - {c}}} \ln {a} = (2x - {b}) {a}^{{x^2 - {b}x - {c}}} \ln {a}$.'''
    return caudan, choices, loi_giai


# --- Cấp số cộng & Cấp số nhân 11 ---

def OnTap11_MC_Cau22():
    # CSN u1, u2 => u4
    u1 = random.choice([2, 3, 4])
    q = random.choice([2, 3])
    u2 = u1 * q
    u4 = u1 * (q**3)

    caudan = fr'''Cho cấp số nhân $(u_n)$ có $u_1 = {u1}$ và $u_2 = {u2}$. Số hạng $u_4$ của cấp số nhân là'''
    correct = fr"${u4}$"
    wrongs = [fr"${u4 * q}$", fr"${u1 * q + 5}$", fr"${u4 // q}$"]
    choices = shuffle_choices(correct, wrongs)
    loi_giai = fr'''Công bội: $q = \dfrac{{u_2}}{{u_1}} = \dfrac{{{u2}}}{{{u1}}} = {q}$. \\
Số hạng $u_4 = u_1 \cdot q^3 = {u1} \cdot {q}^3 = {u4}$.'''
    return caudan, choices, loi_giai


def OnTap11_MC_Cau23():
    # CSC u1, d => uk
    u1 = random.choice([5, 8, 10, 12, 15])
    d = random.choice([-5, -4, -3, -2, 2, 3, 4])
    k = random.choice([15, 20, 25, 30])
    uk = u1 + (k - 1) * d

    caudan = fr'''Cho cấp số cộng $(u_n)$ có số hạng đầu $u_1 = {u1}$ và công sai $d = {d}$. Tìm số hạng thứ ${k}$ của cấp số cộng đã cho.'''
    correct = fr"$u_{{{k}}} = {uk}$"
    wrongs = [
        fr"$u_{{{k}}} = {uk - 4}$",
        fr"$u_{{{k}}} = {uk + 8}$",
        fr"$u_{{{k}}} = {uk - d}$"
    ]
    choices = shuffle_choices(correct, wrongs)
    loi_giai = fr'''Ta có: $u_{{{k}}} = u_1 + ({k} - 1)d = {u1} + {k - 1}({d}) = {uk}$.'''
    return caudan, choices, loi_giai


def OnTap11_MC_Cau24():
    # CSC u1, u2 => d
    u1 = random.choice([-5, -2, 2, 3, 5])
    d = random.choice([3, 4, 5, 6, 7])
    u2 = u1 + d

    caudan = fr'''Cho cấp số cộng $(u_n)$ với $u_1 = {u1}$ và $u_2 = {u2}$. Công sai của cấp số cộng đã cho bằng'''
    correct = fr"${d}$"
    wrongs = [fr"${d - 2}$", fr"${-d}$", fr"${d + 4}$"]
    choices = shuffle_choices(correct, wrongs)
    loi_giai = fr'''Công sai $d = u_2 - u_1 = {u2} - ({u1}) = {d}$.'''
    return caudan, choices, loi_giai


def OnTap11_MC_Cau25():
    # CSN u10, u11 => q
    q = random.choice([-2, -1, 2, 3])
    u10 = random.choice([-5, -3, 2, 4])
    u11 = u10 * q

    caudan = fr'''Cho cấp số nhân $(u_n)$ có $u_{{10}} = {u10}$ và $u_{{11}} = {u11}$. Tìm công bội $q$ cấp số nhân đã cho.'''
    correct = fr"$q = {q}$"
    wrongs = [fr"$q = {-q}$", fr"$q = {q + 3}$", fr"$q = {u11 - u10}$"]
    choices = shuffle_choices(correct, wrongs)
    loi_giai = fr'''Công bội $q = \dfrac{{u_{{11}}}}{{u_{{10}}}} = \dfrac{{{u11}}}{{{u10}}} = {q}$.'''
    return caudan, choices, loi_giai


def OnTap11_MC_Cau26():
    # CSN u1, q => u3
    u1 = random.choice([2024, 2025, 2026, 100, 200])
    q = random.choice([2, 3, 4])
    u3 = u1 * (q**2)

    caudan = fr'''Cho cấp số nhân $(u_n)$ với $u_1 = {u1}$ và công bội $q = {q}$. Giá trị $u_3$ bằng'''
    correct = fr"${u3}$"
    wrongs = [fr"${u1 * q}$", fr"${u1 + 2*q}$", fr"${u3 // q}$"]
    choices = shuffle_choices(correct, wrongs)
    loi_giai = fr'''$u_3 = u_1 \cdot q^2 = {u1} \cdot {q}^2 = {u3}$.'''
    return caudan, choices, loi_giai


def OnTap11_MC_Cau27():
    # CSN u2, q => u5
    u2 = random.choice([3, 4, 5, 6])
    q = random.choice([2, 3])
    u5 = u2 * (q**3)

    caudan = fr'''Cho cấp số nhân $(u_n)$ có $u_2 = {u2}$ và công bội $q = {q}$. Số hạng $u_5$ của cấp số nhân là'''
    correct = fr"${u5}$"
    wrongs = [fr"${u5 * q}$", fr"${u5 // q}$", fr"${u2 * q}$"]
    choices = shuffle_choices(correct, wrongs)
    loi_giai = fr'''$u_5 = u_2 \cdot q^3 = {u2} \cdot {q}^3 = {u5}$.'''
    return caudan, choices, loi_giai


def OnTap11_MC_Cau28():
    # Dãy số nào là cấp số cộng
    a0 = random.choice([-3, -2, 1, 2])
    d = random.choice([2, 3, 4, 5])
    seq = [a0 + i*d for i in range(5)]
    seq_str = "; ".join(str(x) for x in seq)

    caudan = r'''Dãy số nào là cấp số cộng trong các dãy sau?'''
    correct = fr"${seq_str}$"
    wrongs = [
        r"Dãy số $(u_n)$ có số hạng tổng quát $u_n = n^2$",
        r"$0; 2; 6; 8; 12$",
        r"$1; 2; 4; 8; 16$"
    ]
    choices = shuffle_choices(correct, wrongs)
    loi_giai = fr'''Xét dãy ${seq_str}$, hiệu giữa hai số hạng liên tiếp luôn bằng ${d}$ nên đây là cấp số cộng với công sai $d = {d}$.'''
    return caudan, choices, loi_giai


# --- Mũ và Lôgarit 11 ---

def OnTap11_MC_Cau29():
    # log_a x = b
    a = random.choice([2, 3, 5])
    b = random.choice([2, 3, 4])
    ans = a**b

    caudan = fr'''Nghiệm của phương trình $\log_{{{a}}} x = {b}$ là'''
    correct = fr"$x = {ans}$"
    wrongs = [fr"$x = {ans + 1}$", fr"$x = {a * b}$", fr"$x = {a + b}$"]
    choices = shuffle_choices(correct, wrongs)
    loi_giai = fr'''$\log_{{{a}}} x = {b} \iff x = {a}^{{{b}}} = {ans}$.'''
    return caudan, choices, loi_giai


def OnTap11_MC_Cau30():
    # a^{x - b} = a^{-c}
    a = random.choice([2, 3, 4, 5])
    b = random.choice([2, 3, 4])
    c = random.choice([3, 4, 5])
    ans = b - c
    pow_val = a**c

    caudan = fr'''Tìm nghiệm của phương trình ${a}^{{x - {b}}} = \dfrac{{1}}{{{pow_val}}}$.'''
    correct = fr"$x = {ans}$"
    wrongs = [fr"$x = {b + c}$", fr"$x = {-ans}$", fr"$x = 0$"]
    choices = shuffle_choices(correct, wrongs)
    loi_giai = fr'''Ta có $\dfrac{{1}}{{{pow_val}}} = {a}^{{-{c}}}$. Do đó ${a}^{{x - {b}}} = {a}^{{-{c}}} \iff x - {b} = -{c} \iff x = {ans}$.'''
    return caudan, choices, loi_giai


def OnTap11_MC_Cau31():
    # log2(b*x - c) > d
    b = random.choice([2, 3, 4])
    c = random.choice([1, 2, 4])
    d = random.choice([2, 3])
    pow_d = 2**d
    # b*x > pow_d + c
    num = pow_d + c
    if num % b == 0:
        ans_str = str(num // b)
    else:
        ans_str = fr"\dfrac{{{num}}}{{{b}}}"

    caudan = fr'''Giải bất phương trình $\log_2({b}x - {c}) > {d}$.'''
    correct = fr"$x > {ans_str}$"
    wrongs = [
        fr"$x < {ans_str}$",
        fr"$x > {pow_d}$",
        fr"$\dfrac{{{c}}}{{{b}}} < x < {ans_str}$"
    ]
    choices = shuffle_choices(correct, wrongs)
    loi_giai = fr'''$\log_2({b}x - {c}) > {d} \iff {b}x - {c} > 2^{{{d}}} = {pow_d} \iff {b}x > {num} \iff x > {ans_str}$.'''
    return caudan, choices, loi_giai


def OnTap11_MC_Cau32():
    # log2(x - b) > c
    b = random.choice([10, 15, 20, 25])
    c = random.choice([4, 5, 6])
    pow_c = 2**c
    ans = b + pow_c

    caudan = fr'''Tập nghiệm của bất phương trình $\log_2(x - {b}) > {c}$ là'''
    correct = fr"$S = ({ans}; +\infty)$"
    wrongs = [
        fr"$S = ({pow_c}; +\infty)$",
        fr"$S = (-\infty; {ans})$",
        fr"$S = [{ans}; +\infty)$"
    ]
    choices = shuffle_choices(correct, wrongs)
    loi_giai = fr'''$\log_2(x - {b}) > {c} \iff x - {b} > 2^{{{c}}} = {pow_c} \iff x > {ans}$. Vậy $S = ({ans}; +\infty)$.'''
    return caudan, choices, loi_giai


def OnTap11_MC_Cau33():
    # a^x <= a^b
    a = random.choice([2, 3, 5])
    b = random.choice([3, 4, 5])
    val = a**b

    caudan = fr'''Tập nghiệm của bất phương trình ${a}^x \le {val}$ là'''
    correct = fr"$(-\infty; {b}]$"
    wrongs = [
        fr"$({b}; +\infty)$",
        fr"$(-\infty; {b})$",
        fr"$[{b}; +\infty)$"
    ]
    choices = shuffle_choices(correct, wrongs)
    loi_giai = fr'''${a}^x \le {val} = {a}^{{{b}}} \iff x \le {b}$. Vậy tập nghiệm là $(-\infty; {b}]$.'''
    return caudan, choices, loi_giai


def OnTap11_MC_Cau34():
    # log_{1/2} x > -b
    b = random.choice([3, 4, 5])
    val = 2**b

    caudan = fr'''Tập nghiệm của bất phương trình $\log_{{\frac{{1}}{{2}}}} x > -{b}$ là'''
    correct = fr"$(0; {val})$"
    wrongs = [
        fr"$({val}; +\infty)$",
        fr"$(-\infty; {val})$",
        fr"$\left(-\infty; \dfrac{{1}}{{{val}}}\right)$"
    ]
    choices = shuffle_choices(correct, wrongs)
    loi_giai = fr'''Điều kiện: $x > 0$. \\
Vì cơ số $0 < \dfrac{{1}}{{2}} < 1$ nên bất phương trình đổi chiều: \\
$\log_{{\frac{{1}}{{2}}}} x > -{b} \iff x < \left(\dfrac{{1}}{{2}}\right)^{{-{b}}} = {val}$. \\
Kết hợp điều kiện ta được tập nghiệm $(0; {val})$.'''
    return caudan, choices, loi_giai


def OnTap11_MC_Cau35():
    # log2(x - b) > c
    b = random.choice([1, 2, 3, 4])
    c = random.choice([1, 2, 3])
    ans = b + 2**c

    caudan = fr'''Tìm tập nghiệm của bất phương trình $\log_2(x - {b}) > {c}$?'''
    correct = fr"$({ans}; +\infty)$"
    wrongs = [
        fr"$({b}; +\infty)$",
        fr"$[{ans}; +\infty)$",
        fr"$({b}; {ans})$"
    ]
    choices = shuffle_choices(correct, wrongs)
    loi_giai = fr'''$\log_2(x - {b}) > {c} \iff x - {b} > 2^{{{c}}} = {2**c} \iff x > {ans}$. Vậy tập nghiệm là $({ans}; +\infty)$.'''
    return caudan, choices, loi_giai


