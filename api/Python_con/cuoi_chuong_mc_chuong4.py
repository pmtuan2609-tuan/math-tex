# -*- coding: utf-8 -*-
"""
Module sinh đề trắc nghiệm chuẩn ma trận Bài tập Cuối Chương 4 (Toán 12)
Chương IV: NGUYÊN HÀM VÀ TÍCH PHÂN
Gồm 3 bài x 4 câu = 12 câu chuẩn ma trận:
- Bài 1: Nguyên hàm (2 NB, 1 TH, 1 VD)
- Bài 2: Tích phân (2 NB, 1 TH, 1 VD)
- Bài 3: Ứng dụng hình học của tích phân (2 NB, 1 TH, 1 VD)
Tất cả đều sinh ngẫu nhiên số liệu, tự động tính toán đáp án và lời giải chi tiết theo chuẩn ex_test.
"""

import random
import math
from fractions import Fraction


def clean_option(opt):
    """Loại bỏ tiền tố nhãn thừa và dấu chấm kết thúc để tương thích ex_test."""
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
    """Trộn ngẫu nhiên 4 phương án, đảm bảo format chuẩn của ex_test."""
    c_clean = clean_option(correct)
    w_clean = [clean_option(w) for w in wrongs]
    all_ch = [c_clean] + w_clean
    random.shuffle(all_ch)
    res = []
    for ch in all_ch:
        if ch == c_clean:
            res.append(f"{{\\True {ch}}}")
        else:
            res.append(f"{{{ch}}}")
    return res


def fmt_frac(num, den):
    """Định dạng phân số LaTeX gọn gàng."""
    fr = Fraction(num, den)
    if fr.denominator == 1:
        return str(fr.numerator)
    if fr.numerator < 0:
        return f"-\\frac{{{-fr.numerator}}}{{{fr.denominator}}}"
    return f"\\frac{{{fr.numerator}}}{{{fr.denominator}}}"


# ==============================================================================
# BÀI 1: NGUYÊN HÀM
# ==============================================================================

def CuoiChuong4_MC_B1_NB1():
    """B1. Nguyên hàm - Mức độ: NB (Dạng 1): Định nghĩa, nhận biết và tính chất của nguyên hàm"""
    variant = random.choice([1, 2, 3, 4, 5, 6, 7, 8])
    if variant == 1:
        # Định nghĩa nguyên hàm (Câu 2 ảnh batch 1 & Câu 1, 5 Đề 1)
        sub = random.choice([1, 2])
        if sub == 1:
            caudan = r'''Cho hàm số $f(x)$ xác định trên khoảng $K$. Hàm số $F(x)$ được gọi là một nguyên hàm của $f(x)$ trên $K$ nếu khẳng định nào sau đây đúng?'''
            correct = r'''$F'(x) = f(x),\ \forall x \in K$'''
            wrongs = [
                r'''$F(x) = f(x),\ \forall x \in K$''',
                r'''$F(x) = f'(x),\ \forall x \in K$''',
                r'''$F'(x) = f'(x),\ \forall x \in K$'''
            ]
            loi_giai = r'''Theo định nghĩa nguyên hàm: Hàm số $F(x)$ được gọi là một nguyên hàm của $f(x)$ trên $K$ nếu $F'(x) = f(x)$ với mọi $x \in K$.'''
        else:
            caudan = r'''Cho hàm số $f(x)$ có đạo hàm liên tục trên $\mathbb{R}$. Phát biểu nào sau đây là đúng?'''
            correct = r'''$\displaystyle\int f'(x)\,\mathrm{d}x = f(x) + C$'''
            wrongs = [
                r'''$\displaystyle\int f(x)\,\mathrm{d}x = f'(x) + C$''',
                r'''$\displaystyle\int f'(x)\,\mathrm{d}x = f(x)$''',
                r'''$\displaystyle\int f(x)\,\mathrm{d}x = f''(x)$'''
            ]
            loi_giai = r'''Theo tính chất của nguyên hàm: $\displaystyle\int f'(x)\,\mathrm{d}x = f(x) + C$.'''

    elif variant == 2:
        # Tính F'(x0) khi biết F(x) là một nguyên hàm của f(x) (Câu 8 ảnh batch 1 & Câu 8 Đề 1 & Câu 9 Đề 2)
        sub = random.choice([1, 2])
        if sub == 1:
            a = random.choice([1, 2, 3])
            b = random.choice([0, 1, 2, -1])
            x0 = random.choice([3, 4, 5, 25])
            ans = a * (x0 ** 2) + b
            f_expr = fr'''{a}x^2''' if b == 0 else fr'''{a}x^2 {b:+d}'''
            caudan = fr'''Cho hàm số $y = F(x)$ là một nguyên hàm của hàm số $y = {f_expr}$. Tính $F'({x0})$.'''
            correct = fr'''${ans}$'''
            wrongs = [
                fr'''${x0}$''',
                fr'''${ans + 4}$''',
                fr'''${ans - 3}$'''
            ]
            loi_giai = fr'''Vì $F(x)$ là một nguyên hàm của $f(x) = {f_expr}$ nên theo định nghĩa ta có $F'(x) = f(x) = {f_expr}$.\\
Do đó, $F'({x0}) = {f_expr.replace("x", f"({x0})")} = {ans}$.'''
        else:
            f_choice = random.choice([
                (r'''5^x''', r'''5^x''', [r'''5^x \ln 5''', r'''-5^x''', r'''5^x + C''']),
                (r'''\frac{1}{\sin^2 x}''', r'''\frac{1}{\sin^2 x}''', [r'''-\cot x''', r'''-\frac{1}{\sin^2 x}''', r'''\frac{\sin 2x}{\cos^4 x}''']),
                (r'''\cos x''', r'''\cos x''', [r'''-\sin x''', r'''\sin x''', r'''-\cos x'''])
            ])
            fx, ans_fx, wr_fx = f_choice
            caudan = fr'''Cho $\displaystyle\int {fx}\,\mathrm{{d}}x = F(x) + C$. Khẳng định nào dưới đây đúng?'''
            correct = fr'''$F'(x) = {ans_fx}$'''
            wrongs = [fr'''$F'(x) = {w}$''' for w in wr_fx]
            loi_giai = fr'''Theo định nghĩa nguyên hàm, nếu $\displaystyle\int f(x)\,\mathrm{{d}}x = F(x) + C$ thì $F'(x) = f(x) = {ans_fx}$.'''

    elif variant == 3:
        # Nguyên hàm của hằng số vô tỉ (Câu 19 ảnh batch 1)
        k = random.choice([2, 3, 4, 5])
        caudan = fr'''Họ tất cả các nguyên hàm của hàm số $f(x) = \pi^{{{k}}}$ là'''
        correct = fr'''$\pi^{{{k}}}x + C$'''
        wrongs = [
            fr'''$\displaystyle\frac{{\pi^{{{k+1}}}}}{{{k+1}}} + C$''',
            fr'''$\displaystyle\frac{{\pi^{{{k+1}}}x}}{{{k+1}}} + C$''',
            fr'''$\displaystyle\frac{{\pi^{{{k}}}x}}{{{k}}} + C$'''
        ]
        loi_giai = fr'''Vì $\pi^{{{k}}}$ là hằng số nên theo công thức $\displaystyle\int k\,\mathrm{{d}}x = kx + C$, ta có $\displaystyle\int \pi^{{{k}}}\,\mathrm{{d}}x = \pi^{{{k}}}x + C$.'''

    elif variant == 4:
        # Cho int f(x) dx = G(x) + C, xác định f(x) (Câu 24 ảnh batch 1 & Câu 11 Đề 2)
        sub = random.choice([1, 2, 3])
        if sub == 1:
            k = random.choice([2, 3])
            caudan = fr'''Biết $\displaystyle\int f(x)\,\mathrm{{d}}x = x^2 + \cos({k}x) + C$. Khẳng định nào sau đây đúng?'''
            correct = fr'''$f(x) = 2x - {k}\sin({k}x)$'''
            wrongs = [
                fr'''$f(x) = 2x + {k}\sin({k}x)$''',
                fr'''$f(x) = \displaystyle\frac{{x^3}}{{3}} + \sin({k}x)$''',
                fr'''$f(x) = \displaystyle\frac{{x^3}}{{3}} - \frac{{1}}{{{k}}}\sin({k}x)$'''
            ]
            loi_giai = fr'''Đạo hàm cả hai vế: $f(x) = \left(x^2 + \cos({k}x) + C\right)' = 2x - {k}\sin({k}x)$.'''
        elif sub == 2:
            caudan = r'''Nếu $\displaystyle\int f(x)\,\mathrm{d}x = -\cos x + C$ thì khẳng định nào sau đây đúng?'''
            correct = r'''$f(x) = \sin x$'''
            wrongs = [r'''$f(x) = -\sin x$''', r'''$f(x) = -\cos x$''', r'''$f(x) = \cos x$''']
            loi_giai = r'''Ta có $f(x) = (-\cos x + C)' = \sin x$.'''
        else:
            caudan = r'''Nếu $\displaystyle\int f(x)\,\mathrm{d}x = \mathrm{e}^{2x} + C$ thì khẳng định nào sau đây đúng?'''
            correct = r'''$f(x) = 2\mathrm{e}^{2x}$'''
            wrongs = [r'''$f(x) = \mathrm{e}^{2x}$''', r'''$f(x) = \frac{1}{2}\mathrm{e}^{2x}$''', r'''$f(x) = 2x\mathrm{e}^{2x}$''']
            loi_giai = r'''Ta có $f(x) = (\mathrm{e}^{2x} + C)' = 2\mathrm{e}^{2x}$.'''

    elif variant == 5:
        # Khẳng định Sai về công thức nguyên hàm (Câu 26 & 28 ảnh batch 1)
        sub = random.choice([1, 2])
        if sub == 1:
            caudan = r'''Trong các khẳng định sau, khẳng định nào sai?'''
            correct = r'''$\displaystyle\int \mathrm{e}^x\,\mathrm{d}x = \frac{\mathrm{e}^{x+1}}{x+1} + C$'''
            wrongs = [
                r'''$\displaystyle\int \frac{1}{x}\,\mathrm{d}x = \ln|x| + C$ (với $x \ne 0$)''',
                r'''$\displaystyle\int x^{\alpha}\,\mathrm{d}x = \frac{x^{\alpha+1}}{\alpha+1} + C$ (với $\alpha \ne -1$)''',
                r'''$\displaystyle\int \sin x\,\mathrm{d}x = -\cos x + C$'''
            ]
            loi_giai = r'''Công thức đúng là $\displaystyle\int \mathrm{e}^x\,\mathrm{d}x = \mathrm{e}^x + C$. Do đó khẳng định $\displaystyle\int \mathrm{e}^x\,\mathrm{d}x = \frac{\mathrm{e}^{x+1}}{x+1} + C$ là sai.'''
        else:
            caudan = r'''Trong các khẳng định sau, khẳng định nào sai?'''
            correct = r'''$\displaystyle\int x^a\,\mathrm{d}x = \frac{x^{a+1}}{a+1} + C$ (với mọi $a \in \mathbb{R}$)'''
            wrongs = [
                r'''$\displaystyle\int 0\,\mathrm{d}x = C$''',
                r'''$\displaystyle\int \frac{1}{x}\,\mathrm{d}x = \ln|x| + C$ (với $x \ne 0$)''',
                r'''$\displaystyle\int \mathrm{d}x = x + C$'''
            ]
            loi_giai = r'''Công thức $\displaystyle\int x^a\,\mathrm{d}x = \frac{x^{a+1}}{a+1} + C$ chỉ đúng khi $a \ne -1$. Khi $a = -1$, $\displaystyle\int \frac{1}{x}\,\mathrm{d}x = \ln|x| + C$. Do đó khẳng định trên là sai.'''

    elif variant == 6:
        # Cho F(x) = a x^2 + b sin x, tìm f(x) (Câu 27 ảnh batch 1)
        a = random.choice([1, 2, 3])
        b = random.choice([1, 2, -1, -2])
        sign_b = f"{b:+d}".replace("+1", "+").replace("-1", "-")
        sign_opp = f"{-b:+d}".replace("+1", "+").replace("-1", "-")
        f_b = fr'''{2*a}x {sign_b}\cos x'''
        w1 = fr'''{2*a}x {sign_opp}\cos x'''
        w2 = fr'''\frac{{{a}}}{{3}}x^3 {sign_b}\cos x'''
        w3 = fr'''{2*a}x {sign_b}\sin x'''
        caudan = fr'''Hàm số $F(x) = {a}x^2 {sign_b}\sin x$ là một nguyên hàm của hàm số nào sau đây?'''
        correct = fr'''$f(x) = {f_b}$'''
        wrongs = [fr'''$f(x) = {w1}$''', fr'''$f(x) = {w2}$''', fr'''$f(x) = {w3}$''']
        loi_giai = fr'''Vì $F(x)$ là nguyên hàm của $f(x)$ nên $f(x) = F'(x) = ({a}x^2 {sign_b}\sin x)' = {f_b}$.'''

    elif variant == 7:
        # Hàm số nào có một nguyên hàm là y = sin(kx) (Câu 31 ảnh batch 1)
        k = random.choice([2, 3, 4])
        caudan = fr'''Hàm số nào sau đây có một nguyên hàm là hàm số $y = \sin({k}x)$?'''
        correct = fr'''$y = {k}\cos({k}x)$'''
        wrongs = [
            fr'''$y = \cos({k}x)$''',
            fr'''$y = \frac{{\cos({k}x)}}{{{k}}}$''',
            fr'''$y = -{k}\cos({k}x)$'''
        ]
        loi_giai = fr'''Theo định nghĩa, nếu $y$ nhận hàm số $g(x) = \sin({k}x)$ làm nguyên hàm thì $y = g'(x) = (\sin({k}x))' = {k}\cos({k}x)$.'''

    else:
        # Tính chất tuyến tính của nguyên hàm
        k = random.choice([2, 3, 5, -2, -3])
        caudan = fr'''Cho hàm số $f(x)$ liên tục trên khoảng $K$ và số thực $k \ne 0$. Mệnh đề nào sau đây luôn đúng?'''
        correct = fr'''$\displaystyle\int {k}f(x)\,\mathrm{{d}}x = {k}\int f(x)\,\mathrm{{d}}x$'''
        wrongs = [
            fr'''$\displaystyle\int {k}f(x)\,\mathrm{{d}}x = \frac{{1}}{{{k}}}\int f(x)\,\mathrm{{d}}x$''',
            fr'''$\displaystyle\int {k}f(x)\,\mathrm{{d}}x = {k} + \int f(x)\,\mathrm{{d}}x$''',
            fr'''$\displaystyle\int {k}f(x)\,\mathrm{{d}}x = {k}f(x) + C$'''
        ]
        loi_giai = fr'''Theo tính chất cơ bản của nguyên hàm, với hằng số $k \ne 0$, ta có $\displaystyle\int k f(x)\,\mathrm{{d}}x = k \int f(x)\,\mathrm{{d}}x$.'''

    return caudan, shuffle_choices(correct, wrongs), loi_giai


def CuoiChuong4_MC_B1_NB2():
    """B1. Nguyên hàm - Mức độ: NB (Dạng 2): Bảng nguyên hàm hàm số cơ bản"""
    sub = random.choice([1, 2, 3, 4, 5, 6, 7, 8, 9, 10])
    if sub == 1:
        # int x^n dx (Câu 3, 22 batch 1 & Câu 4 Đề 1 & Câu 6 Đề 2)
        n = random.choice([2, 3, 4, 5, 7, 2024, 2025, 2026])
        caudan = fr'''Họ tất cả các nguyên hàm của hàm số $f(x) = x^{{{n}}}$ là'''
        correct = fr'''$\displaystyle\frac{{x^{{{n + 1}}}}}{{{n + 1}}} + C$'''
        wrongs = [
            fr'''$\displaystyle{n} x^{{{n - 1}}} + C$''',
            fr'''$\displaystyle\frac{{x^{{{n}}}}}{{{n}}} + C$''',
            fr'''$\displaystyle x^{{{n + 1}}} + C$'''
        ]
        loi_giai = fr'''Áp dụng công thức nguyên hàm cơ bản: $\displaystyle\int x^{{n}}\,\mathrm{{d}}x = \frac{{x^{{n+1}}}}{{n+1}} + C$ với $n \ne -1$, ta có $\displaystyle\int x^{{{n}}}\,\mathrm{{d}}x = \frac{{x^{{{n+1}}}}}{{{n+1}}} + C$.'''

    elif sub == 2:
        # f(x) = ax + b (Câu 4 batch 1)
        a = random.choice([2, 4, 6])
        b = random.choice([1, 2, 3, 4, 5])
        a2 = a // 2
        term_x2 = fr'''{a2}x^2''' if a2 != 1 else r'''x^2'''
        caudan = fr'''Họ tất cả các nguyên hàm của hàm số $f(x) = {a}x + {b}$ là'''
        correct = fr'''${term_x2} + {b}x + C$'''
        wrongs = [
            fr'''${a}x^2 + {b}x + C$''',
            fr'''${term_x2} + C$''',
            fr'''${a}x^2 + C$'''
        ]
        loi_giai = fr'''Ta có $\displaystyle\int ({a}x + {b})\,\mathrm{{d}}x = {a} \cdot \frac{{x^2}}{{2}} + {b}x + C = {term_x2} + {b}x + C$.'''

    elif sub == 3:
        # f(x) = a x^3 - K (Câu 5 batch 1 & Câu 2 Đề 2)
        a = random.choice([1, 4])
        K = random.choice([2024, 2025, 2026])
        is_minus = random.choice([True, False])
        sign_str = fr'''- {K}''' if is_minus else fr'''+ {K}'''
        sign_prim = fr'''- {K}x''' if is_minus else fr'''+ {K}x'''
        f_expr = fr'''{a if a > 1 else ""}x^3 {sign_str}'''
        if a == 4:
            ans_term = r'''x^4'''
        else:
            ans_term = r'''\frac{x^4}{4}'''
        caudan = fr'''Họ nguyên hàm của hàm số $f(x) = {f_expr}$ là'''
        correct = fr'''${ans_term} {sign_prim} + C$'''
        wrongs = [
            fr'''${4*a}x^2 {sign_str} + C$''',
            fr'''${ans_term} + C$''',
            fr'''${a}x^4 {sign_prim} + C$''' if a != 1 else fr'''4x^4 {sign_prim} + C'''
        ]
        loi_giai = fr'''Ta có $\displaystyle\int ({f_expr})\,\mathrm{{d}}x = \int {a if a > 1 else ""}x^3\,\mathrm{{d}}x {sign_str[0]} \int {K}\,\mathrm{{d}}x = {ans_term} {sign_prim} + C$.'''

    elif sub == 4:
        # f(x) = (x + a)(x + b) (Câu 6 batch 1)
        a = random.choice([1, 2])
        b = random.choice([2, 3])
        s = a + b
        p = a * b
        s_half = fmt_frac(s, 2)
        caudan = fr'''Họ nguyên hàm của hàm số $f(x) = (x + {a})(x + {b})$ là'''
        correct = fr'''$\displaystyle\frac{{x^3}}{{3}} + {s_half}x^2 + {p}x + C$'''
        wrongs = [
            fr'''$2x + {s} + C$''',
            fr'''$\displaystyle\frac{{x^3}}{{3}} - {s_half}x^2 + {p}x + C$''',
            fr'''$\displaystyle\frac{{x^3}}{{3}} + \frac{{{s}}}{{3}}x^2 + {p}x + C$'''
        ]
        loi_giai = fr'''Khai triển hàm số: $f(x) = (x + {a})(x + {b}) = x^2 + {s}x + {p}$.\\
Khi đó: $\displaystyle\int (x^2 + {s}x + {p})\,\mathrm{{d}}x = \frac{{x^3}}{{3}} + {s_half}x^2 + {p}x + C$.'''

    elif sub == 5:
        # f(x) = x^2 + k / x^2 (Câu 7 batch 1 & Câu 2, 3 Đề 1)
        k = random.choice([2, 3, 4])
        caudan = fr'''Tìm nguyên hàm của hàm số $f(x) = x^2 + \frac{{{k}}}{{x^2}}$.'''
        correct = fr'''$\displaystyle\frac{{x^3}}{{3}} - \frac{{{k}}}{{x}} + C$'''
        wrongs = [
            fr'''$\displaystyle\frac{{x^3}}{{3}} + \frac{{{k}}}{{x}} + C$''',
            fr'''$\displaystyle\frac{{x^3}}{{3}} - \frac{{1}}{{x}} + C$''',
            fr'''$\displaystyle 2x - \frac{{{2*k}}}{{x^3}} + C$'''
        ]
        loi_giai = fr'''Ta có $\displaystyle\int \left(x^2 + \frac{{{k}}}{{x^2}}\right)\,\mathrm{{d}}x = \int x^2\,\mathrm{{d}}x + {k}\int x^{{-2}}\,\mathrm{{d}}x = \frac{{x^3}}{{3}} - \frac{{{k}}}{{x}} + C$.'''

    elif sub == 6:
        # f(x) = a x^2 + sin x hoặc sin x + cos x (Câu 10, 11 batch 1 & Câu 10 Đề 1 & Câu 8 Đề 2)
        opt_type = random.choice([1, 2])
        if opt_type == 1:
            a = random.choice([3, 6])
            coef = a // 3
            term_x3 = fr'''{coef}x^3''' if coef > 1 else r'''x^3'''
            caudan = fr'''Họ nguyên hàm của hàm số $f(x) = {a}x^2 + \sin x$ là'''
            correct = fr'''${term_x3} - \cos x + C$'''
            wrongs = [
                fr'''${term_x3} + \cos x + C$''',
                fr'''${2*a}x - \cos x + C$''',
                fr'''${term_x3} + \sin x + C$'''
            ]
            loi_giai = fr'''Ta có $\displaystyle\int ({a}x^2 + \sin x)\,\mathrm{{d}}x = {a} \cdot \frac{{x^3}}{{3}} - \cos x + C = {term_x3} - \cos x + C$.'''
        else:
            caudan = r'''Họ nguyên hàm của hàm số $f(x) = \sin x + \cos x$ là'''
            correct = r'''$-\cos x + \sin x + C$'''
            wrongs = [
                r'''$\cos x - \sin x + C$''',
                r'''$-\cos x - \sin x + C$''',
                r'''$\cos x + \sin x + C$'''
            ]
            loi_giai = r'''Ta có $\displaystyle\int (\sin x + \cos x)\,\mathrm{d}x = -\cos x + \sin x + C$.'''

    elif sub == 7:
        # y = a^x (Câu 12, 13 batch 1 & Câu 9 Đề 1 & Câu 3 Đề 2)
        a = random.choice([2, 5, 6, 2018, 2024])
        caudan = fr'''Nguyên hàm của hàm số $y = {a}^x$ là'''
        correct = fr'''$\displaystyle\frac{{{a}^x}}{{\ln {a}}} + C$'''
        wrongs = [
            fr'''${a}^x \ln {a} + C$''',
            fr'''$\displaystyle\frac{{{a}^{{x+1}}}}{{x + 1}} + C$''',
            fr'''${a}^x + C$'''
        ]
        loi_giai = fr'''Theo công thức nguyên hàm hàm số mũ: $\displaystyle\int a^x\,\mathrm{{d}}x = \frac{{a^x}}{{\ln a}} + C$, ta có $\displaystyle\int {a}^x\,\mathrm{{d}}x = \frac{{{a}^x}}{{\ln {a}}} + C$.'''

    elif sub == 8:
        # f(x) = e^{kx} hoặc e^x + c (Câu 14, 15, 16 batch 1)
        k = random.choice([2, 3, 4])
        caudan = fr'''Tìm nguyên hàm của hàm số $f(x) = \mathrm{{e}}^{{{k}x}}$.'''
        correct = fr'''$\displaystyle\frac{{1}}{{{k}}}\mathrm{{e}}^{{{k}x}} + C$'''
        wrongs = [
            fr'''$\mathrm{{e}}^{{{k}x}} + C$''',
            fr'''${k}\mathrm{{e}}^{{{k}x}} + C$''',
            fr'''$\displaystyle\frac{{\mathrm{{e}}^{{{k}x+1}}}}{{{k}x + 1}} + C$'''
        ]
        loi_giai = fr'''Áp dụng công thức $\displaystyle\int \mathrm{{e}}^{{ax+b}}\,\mathrm{{d}}x = \frac{{1}}{{a}}\mathrm{{e}}^{{ax+b}} + C$, ta có $\displaystyle\int \mathrm{{e}}^{{{k}x}}\,\mathrm{{d}}x = \frac{{1}}{{{k}}}\mathrm{{e}}^{{{k}x}} + C$.'''

    elif sub == 9:
        # f(x) = 2^x + cos x hoặc e^x + x (Câu 17, 21 batch 1 & Câu 7, 10 Đề 1)
        opt_h = random.choice([1, 2])
        if opt_h == 1:
            a = random.choice([2, 6])
            caudan = fr'''Cho hàm số $f(x) = {a}^x + \cos x$. Một nguyên hàm của $f(x)$ trên $\mathbb{{R}}$ là'''
            correct = fr'''$F(x) = \displaystyle\frac{{{a}^x}}{{\ln {a}}} + \sin x$'''
            wrongs = [
                fr'''$F(x) = \displaystyle\frac{{{a}^x}}{{\ln {a}}} - \sin x$''',
                fr'''$F(x) = {a}^x \ln {a} + \sin x$''',
                fr'''$F(x) = {a}^x + \sin x$'''
            ]
            loi_giai = fr'''Ta có $\displaystyle\int ({a}^x + \cos x)\,\mathrm{{d}}x = \frac{{{a}^x}}{{\ln {a}}} + \sin x + C$. Chọn $C = 0$ ta được $F(x) = \frac{{{a}^x}}{{\ln {a}}} + \sin x$.'''
        else:
            caudan = r'''Nguyên hàm của hàm số $f(x) = \mathrm{e}^x + x$ là'''
            correct = r'''$\mathrm{e}^x + \displaystyle\frac{x^2}{2} + C$'''
            wrongs = [
                r'''$\mathrm{e}^x + x^2 + C$''',
                r'''$\displaystyle\frac{\mathrm{e}^x}{\ln 2} + x^2 + C$''',
                r'''$\mathrm{e} + \displaystyle\frac{x^2}{2} + C$'''
            ]
            loi_giai = r'''Ta có $\displaystyle\int (\mathrm{e}^x + x)\,\mathrm{d}x = \mathrm{e}^x + \frac{x^2}{2} + C$.'''

    else:
        # f(x) = x^2 - a^x + 1/x (Câu 20 batch 1)
        a = random.choice([2, 3, 5])
        caudan = fr'''Tìm họ nguyên hàm của hàm số $y = x^2 - {a}^x + \frac{{1}}{{x}}$ trên $(0; +\infty)$.'''
        correct = fr'''$\displaystyle\frac{{x^3}}{{3}} - \frac{{{a}^x}}{{\ln {a}}} + \ln x + C$'''
        wrongs = [
            fr'''$\displaystyle\frac{{x^3}}{{3}} - \frac{{{a}^x}}{{\ln {a}}} - \frac{{1}}{{x^2}} + C$''',
            fr'''$\displaystyle\frac{{x^3}}{{3}} - {a}^x + \frac{{1}}{{x^2}} + C$''',
            fr'''$\displaystyle\frac{{x^3}}{{3}} - \frac{{{a}^x}}{{\ln {a}}} - \ln x + C$'''
        ]
        loi_giai = fr'''Ta có:
\[
\int \left(x^2 - {a}^x + \frac{{1}}{{x}}\right)\,\mathrm{{d}}x = \frac{{x^3}}{{3}} - \frac{{{a}^x}}{{\ln {a}}} + \ln|x| + C = \frac{{x^3}}{{3}} - \frac{{{a}^x}}{{\ln {a}}} + \ln x + C\quad (\text{{do }} x > 0).
\]'''

    return caudan, shuffle_choices(correct, wrongs), loi_giai


def CuoiChuong4_MC_B1_TH():
    """B1. Nguyên hàm - Mức độ: TH: Tìm nguyên hàm thỏa mãn điều kiện F(x0) = y0, nguyên hàm phân thức, căn thức"""
    sub = random.choice([1, 2, 3, 4, 5, 6, 7, 8, 9])
    if sub == 1:
        # f(x) = a/x thỏa F(e) = y0, tính F(x1) (Câu 25 batch 1)
        a = random.choice([1, 2])
        C = random.choice([2, 3, 4])
        y0 = a + C
        x1 = random.choice([2, 3, 5])
        term_a = fr'''{a}''' if a > 1 else ""
        correct = fr'''$F({x1}) = {term_a}\ln {x1} + {C}$'''
        wrongs = [
            fr'''$F({x1}) = {term_a}\ln {x1}$''',
            fr'''$F({x1}) = {term_a}\ln {x1} - {C}$''',
            fr'''$F({x1}) = {term_a}\ln {x1} + {C + 2}$'''
        ]
        caudan = fr'''Biết $F(x)$ là một nguyên hàm của hàm số $f(x) = \frac{{{a}}}{{x}}$ trên $(0; +\infty)$ và $F(\mathrm{{e}}) = {y0}$. Tính $F({x1})$.'''
        loi_giai = fr'''Họ nguyên hàm của $f(x)$ trên $(0; +\infty)$ là $F(x) = \displaystyle\int \frac{{{a}}}{{x}}\,\mathrm{{d}}x = {term_a}\ln x + C$.\\
Theo giả thiết $F(\mathrm{{e}}) = {y0} \implies {term_a}\ln \mathrm{{e}} + C = {y0} \iff {a} + C = {y0} \implies C = {C}$.\\
Do đó $F(x) = {term_a}\ln x + {C}$. Suy ra $F({x1}) = {term_a}\ln {x1} + {C}$.'''

    elif sub == 2:
        # f(x) = a sin x + b / sin^2 x (Câu 30 batch 1)
        a = random.choice([2, 3, 4])
        b = random.choice([2, 3, 5])
        caudan = fr'''Nguyên hàm của hàm số $f(x) = {a}\sin x + \frac{{{b}}}{{\sin^2 x}}$ là'''
        correct = fr'''$-{a}\cos x - {b}\cot x + C$'''
        wrongs = [
            fr'''${a}\cos x - {b}\cot x + C$''',
            fr'''$-{a}\cos x + {b}\cot x + C$''',
            fr'''${a}\cos x - {b}\tan x + C$'''
        ]
        loi_giai = fr'''Ta có: $\displaystyle\int \left({a}\sin x + \frac{{{b}}}{{\sin^2 x}}\right)\,\mathrm{{d}}x = {a}\int \sin x\,\mathrm{{d}}x + {b}\int \frac{{1}}{{\sin^2 x}}\,\mathrm{{d}}x = -{a}\cos x - {b}\cot x + C$.'''

    elif sub == 3:
        # f(x) = (a + b x^4) / x^2 (Câu 32 batch 1 & Câu 5 Đề 2)
        a = random.choice([2, 3, 5])
        b = random.choice([2, 3, 4])
        b_frac = fmt_frac(b, 3)
        caudan = fr'''Tìm họ nguyên hàm của hàm số $f(x) = \frac{{{a} + {b}x^4}}{{x^2}}$ trên khoảng $(0; +\infty)$.'''
        correct = fr'''$\displaystyle {b_frac}x^3 - \frac{{{a}}}{{x}} + C$'''
        wrongs = [
            fr'''$\displaystyle {b_frac}x^3 + \frac{{{a}}}{{x}} + C$''',
            fr'''$\displaystyle {b_frac}x^3 + {a}\ln x^2 + C$''',
            fr'''$\displaystyle {b}x^3 - \frac{{{a}}}{{x}} + C$'''
        ]
        loi_giai = fr'''Biến đổi hàm số: $f(x) = \frac{{{a}}}{{x^2}} + {b}x^2 = {a}x^{{-2}} + {b}x^2$.\\
Khi đó $\displaystyle\int f(x)\,\mathrm{{d}}x = {a}\frac{{x^{{-1}}}}{{-1}} + {b}\frac{{x^3}}{{3}} + C = {b_frac}x^3 - \frac{{{a}}}{{x}} + C$.'''

    elif sub == 4:
        # f(x) = 2x + 3a sqrt(x) thỏa F(1) = 0 (Câu 33 batch 1)
        a = random.choice([1, 2, 3])
        coef_sqrt = 2 * a
        C = -(1 + 2 * a)
        caudan = fr'''Tìm một nguyên hàm $F(x)$ của hàm số $f(x) = 2x + {3*a}\sqrt{{x}}$ trên $(0; +\infty)$ thoả mãn $F(1) = 0$.'''
        correct = fr'''$F(x) = x^2 + {coef_sqrt}\sqrt{{x^3}} {C:+d}$'''
        wrongs = [
            fr'''$F(x) = x^2 + {3*a}\sqrt{{x^3}}$''',
            fr'''$F(x) = x^2 + {coef_sqrt}\sqrt[3]{{x^2}}$''',
            fr'''$F(x) = x^2 + {3*a}\sqrt[3]{{x^2}} {C:+d}$'''
        ]
        loi_giai = fr'''Ta có: $\displaystyle F(x) = \int \left(2x + {3*a}x^{{\frac{{1}}{{2}}}}\right)\,\mathrm{{d}}x = x^2 + {3*a} \cdot \frac{{x^{{\frac{{3}}{{2}}}}}}{{\frac{{3}}{{2}}}} + C = x^2 + {coef_sqrt}\sqrt{{x^3}} + C$.\\
Do $F(1) = 0 \implies 1^2 + {coef_sqrt}\sqrt{{1^3}} + C = 0 \iff 1 + {coef_sqrt} + C = 0 \implies C = {C}$.\\
Vậy $F(x) = x^2 + {coef_sqrt}\sqrt{{x^3}} {C:+d}$.'''

    elif sub == 5:
        # f'(x) = 3a sqrt(x) + 2b / \sqrt[3]{x}, f(1) = y0 (Câu 34 batch 1)
        a = random.choice([1, 2])
        b = random.choice([1, 2])
        y0 = random.choice([1, 2, 3])
        C = y0 - 2 * a - 3 * b
        caudan = fr'''Tìm hàm số $y = f(x)$, biết $f'(x) = {3*a}\sqrt{{x}} + \frac{{{2*b}}}{{\sqrt[3]{{x}}}}$ trên $(0; +\infty)$ và $f(1) = {y0}$.'''
        correct = fr'''$f(x) = {2*a}x\sqrt{{x}} + {3*b}\sqrt[3]{{x^2}} {C:+d}$'''
        wrongs = [
            fr'''$f(x) = {2*a}x\sqrt{{x}} - {3*b}\sqrt[3]{{x^2}} {y0:+d}$''',
            fr'''$f(x) = {a}\sqrt{{x}} + {3*b}\sqrt[3]{{x^2}} {C:+d}$''',
            fr'''$f(x) = {2*a}x\sqrt{{x}} + {3*b}\sqrt[3]{{x}} {C:+d}$'''
        ]
        loi_giai = fr'''Ta có:
\[
f(x) = \int \left({3*a}x^{{\frac{{1}}{{2}}}} + {2*b}x^{{-\frac{{1}}{{3}}}}\right)\,\mathrm{{d}}x = {2*a}x^{{\frac{{3}}{{2}}}} + {3*b}x^{{\frac{{2}}{{3}}}} + C = {2*a}x\sqrt{{x}} + {3*b}\sqrt[3]{{x^2}} + C.
\]
Theo giả thiết $f(1) = {y0} \implies {2*a} \cdot 1 + {3*b} \cdot 1 + C = {y0} \implies C = {C}$.\\
Vậy $f(x) = {2*a}x\sqrt{{x}} + {3*b}\sqrt[3]{{x^2}} {C:+d}$.'''

    elif sub == 6:
        # f(x) = a e^x + b thỏa F(0) = y0 (Câu 35 batch 1)
        a = random.choice([2, 3, 4])
        b = random.choice([1, 2, 3])
        C = random.choice([1, 2, -1, -2])
        y0 = a + C
        caudan = fr'''Biết $F(x)$ là một nguyên hàm của hàm số $f(x) = {a}\mathrm{{e}}^x + {b}$ thoả mãn $F(0) = {y0}$. Khi đó, biểu thức của $F(x)$ là'''
        correct = fr'''$F(x) = {a}\mathrm{{e}}^x + {b}x {C:+d}$'''
        wrongs = [
            fr'''$F(x) = {a}\mathrm{{e}}^x + {b}x {-C:+d}$''',
            fr'''$F(x) = \mathrm{{e}}^x + {b}x$''',
            fr'''$F(x) = {a}\mathrm{{e}}^x + {b}x {C + 3:+d}$'''
        ]
        loi_giai = fr'''Ta có $F(x) = \displaystyle\int ({a}\mathrm{{e}}^x + {b})\,\mathrm{{d}}x = {a}\mathrm{{e}}^x + {b}x + C$.\\
Do $F(0) = {y0} \implies {a}\mathrm{{e}}^0 + {b} \cdot 0 + C = {y0} \iff {a} + C = {y0} \implies C = {C}$.\\
Vậy $F(x) = {a}\mathrm{{e}}^x + {b}x {C:+d}$.'''

    elif sub == 7:
        # f(x) = 6x^5 + 1/x^3 thỏa F(1) = 0 (Câu 11 Đề 1 & Câu 36 batch 1)
        caudan = r'''Cho $F(x)$ là nguyên hàm của hàm số $f(x) = 6x^5 + \frac{1}{x^3}$ trên $(0; +\infty)$ thoả mãn $F(1) = 0$. Tìm $F(x)$.'''
        correct = r'''$F(x) = x^6 - \frac{1}{2x^2} - \frac{1}{2}$'''
        wrongs = [
            r'''$F(x) = x^6 + \frac{1}{2x^2} - \frac{3}{2}$''',
            r'''$F(x) = x^6 - \frac{1}{2x^2} + \frac{1}{2}$''',
            r'''$F(x) = x^6 - \frac{3}{x^2} + 2$'''
        ]
        loi_giai = r'''Ta có: $F(x) = \displaystyle\int \left(6x^5 + x^{-3}\right)\,\mathrm{d}x = x^6 - \frac{1}{2x^2} + C$.\\
Vì $F(1) = 0$ nên $1^6 - \frac{1}{2 \cdot 1^2} + C = 0 \iff \frac{1}{2} + C = 0 \implies C = -\frac{1}{2}$.\\
Vậy $F(x) = x^6 - \frac{1}{2x^2} - \frac{1}{2}$.'''

    elif sub == 8:
        # Biết int (1/(kx) + x^n) dx = a ln|x| + b x^{n+1} + C. Tính a^2 + b (Câu 2 Đề 1)
        k = random.choice([2, 3])
        n = random.choice([3, 5])
        # a = 1/k, b = 1/(n+1)
        a_frac = Fraction(1, k)
        b_frac = Fraction(1, n + 1)
        val = (a_frac ** 2) + b_frac
        caudan = fr'''Biết $\displaystyle\int \left(\frac{{1}}{{{k}x}} + x^{{{n}}}\right)\,\mathrm{{d}}x = a\ln|x| + b x^{{{n+1}}} + C$ với $a, b \in \mathbb{{Q}}, C \in \mathbb{{R}}$. Tính giá trị của biểu thức $P = a^2 + b$.'''
        correct = fr'''${fmt_frac(val.numerator, val.denominator)}$'''
        wrongs = [
            fr'''${fmt_frac(val.numerator + 2, val.denominator)}$''',
            fr'''${fmt_frac(val.numerator, val.denominator + 1)}$''',
            fr'''${val.numerator + val.denominator}$'''
        ]
        loi_giai = fr'''Ta có: $\displaystyle\int \left(\frac{{1}}{{{k}x}} + x^{{{n}}}\right)\,\mathrm{{d}}x = \frac{{1}}{{{k}}}\ln|x| + \frac{{1}}{{{n+1}}}x^{{{n+1}}} + C$.\\
Đồng nhất hệ số, ta được $a = \frac{{1}}{{{k}}}$ và $b = \frac{{1}}{{{n+1}}}$.\\
Suy ra $P = a^2 + b = \left(\frac{{1}}{{{k}}}\right)^2 + \frac{{1}}{{{n+1}}} = {fmt_frac(val.numerator, val.denominator)}$.'''

    else:
        # Tìm một nguyên hàm F(x) của f(x) = -2a x biết F(0) = y0 (Câu 12 Đề 1)
        a = random.choice([1, 2, 3])
        y0 = random.choice([3, 5, 7, 10])
        # F(x) = -a x^2 + y0 = y0 - a x^2
        coef = 2 * a
        caudan = fr'''Tìm một nguyên hàm $F(x)$ của hàm số $f(x) = -{coef}x$ biết $F(0) = {y0}$.'''
        correct = fr'''$F(x) = {y0} - {a if a > 1 else ""}x^2$'''
        wrongs = [
            fr'''$F(x) = {y0} + {a if a > 1 else ""}x^2$''',
            fr'''$F(x) = -{coef}x^2 + {y0}$''',
            fr'''$F(x) = {y0 + 5} - {a if a > 1 else ""}x^2$'''
        ]
        loi_giai = fr'''Ta có $F(x) = \displaystyle\int (-{coef}x)\,\mathrm{{d}}x = -{a if a > 1 else ""}x^2 + C$.\\
Do $F(0) = {y0} \implies -{a if a > 1 else ""}(0)^2 + C = {y0} \implies C = {y0}$.\\
Vậy $F(x) = {y0} - {a if a > 1 else ""}x^2$.'''

    return caudan, shuffle_choices(correct, wrongs), loi_giai


def CuoiChuong4_MC_B1_VD():
    """B1. Nguyên hàm - Mức độ: VD: Toán thực tế chuyển động tìm vận tốc hoặc quãng đường"""
    sub = random.choice([1, 2, 3])
    if sub == 1:
        # Ném bóng từ độ cao h0 với v(t) = -10t + v0 (Câu 37 batch 1)
        h0 = random.choice([15, 20, 25, 30])
        v0 = random.choice([12, 14, 16, 18, 20])
        caudan = fr'''Một quả bóng được ném thẳng đứng lên từ độ cao ${h0}\text{{ m}}$ với vận tốc ban đầu được tính bởi công thức $v(t) = -10t + {v0}\text{{ (m/s)}}$. Công thức nào sau đây tính độ cao $h(t)$ của quả bóng theo thời gian $t$ (giây)?'''
        correct = fr'''$h(t) = -5t^2 + {v0}t + {h0}$'''
        wrongs = [
            fr'''$h(t) = -5t^2 + {v0}t + C$''',
            fr'''$h(t) = 5t^2 - {v0}t + {h0}$''',
            fr'''$h(t) = -10t^2 + {v0}t + {h0}$'''
        ]
        loi_giai = fr'''Độ cao $h(t)$ là một nguyên hàm của vận tốc $v(t)$:
\[
h(t) = \int v(t)\,\mathrm{{d}}t = \int (-10t + {v0})\,\mathrm{{d}}t = -5t^2 + {v0}t + C.
\]
Tại thời điểm ban đầu $t = 0$, bóng ở độ cao $h(0) = {h0}\text{{ m}} \implies -5(0)^2 + {v0}(0) + C = {h0} \implies C = {h0}$.\\
Vậy công thức độ cao là: $h(t) = -5t^2 + {v0}t + {h0}$.'''

    elif sub == 2:
        # Ô tô tăng tốc với a(t) = mt + n
        m = random.choice([2, 4])
        n = random.choice([1, 2, 3])
        v0 = random.choice([5, 10, 15])
        t_calc = random.choice([3, 4, 5])
        v_ans = (m // 2) * (t_calc ** 2) + n * t_calc + v0
        caudan = fr'''Một ô tô đang chuyển động với vận tốc $v_0 = {v0}\text{{ m/s}}$ thì người lái xe đạp ga tăng tốc với gia tốc $a(t) = {m}t + {n}\text{{ (m/s}}^2\text{{)}}$, trong đó $t$ là khoảng thời gian tính bằng giây kể từ thời điểm bắt đầu tăng tốc. Vận tốc của ô tô sau $t = {t_calc}\text{{ giây}}$ bằng bao nhiêu?'''
        correct = fr'''${v_ans}\text{{ m/s}}$'''
        wrongs = [
            fr'''${v_ans + random.choice([4, 6, 8])}\text{{ m/s}}$''',
            fr'''${v_ans - random.choice([3, 5, 7])}\text{{ m/s}}$''',
            fr'''${m * t_calc + n + v0}\text{{ m/s}}$'''
        ]
        loi_giai = fr'''Vận tốc $v(t)$ là một nguyên hàm của gia tốc $a(t)$:
\[
v(t) = \int a(t)\,\mathrm{{d}}t = \int ({m}t + {n})\,\mathrm{{d}}t = {m//2}t^2 + {n}t + C.
\]
Tại thời điểm $t = 0$, xe có vận tốc $v(0) = {v0}$, do đó $C = {v0}$.\\
Suy ra công thức vận tốc là: $v(t) = {m//2}t^2 + {n}t + {v0}$.\\
Vận tốc của xe sau $t = {t_calc}\text{{ s}}$ là:
\[
v({t_calc}) = {m//2} \cdot ({t_calc})^2 + {n} \cdot {t_calc} + {v0} = {v_ans}\text{{ m/s}}.
\]'''

    else:
        # Ô tô hãm phanh (Câu 5 Phần III Đề 1)
        v0 = random.choice([12, 15, 18, 20])
        k = random.choice([2, 3, 4])
        s_frac = Fraction(v0 ** 2, 2 * k)
        s_val = round(float(s_frac), 1)
        if s_val.is_integer():
            s_str = str(int(s_val))
        else:
            s_str = str(s_val).replace(".", ",")
        
        caudan = fr'''Một chiếc ô tô đang chạy với vận tốc ${v0}\text{{ m/s}}$ thì gặp chướng ngại vật, người lái xe hãm phanh khẩn cấp. Sau khi hãm phanh, ô tô chuyển động chậm dần đều với vận tốc $v(t) = -{k}t + {v0}\text{{ (m/s)}}$, trong đó $t$ tính bằng giây. Từ lúc hãm phanh đến khi dừng hẳn, ô tô di chuyển được quãng đường bao nhiêu mét?'''
        correct = fr'''${s_str}\text{{ m}}$'''
        wrongs = [
            fr'''${float(s_val + 5):.1f}\text{{ m}}$'''.replace(".", ",").replace(",0", ""),
            fr'''${float(max(1, s_val - 4)):.1f}\text{{ m}}$'''.replace(".", ",").replace(",0", ""),
            fr'''${v0}\text{{ m}}$'''
        ]
        loi_giai = fr'''Khi ô tô dừng hẳn thì $v(t) = 0 \iff -{k}t + {v0} = 0 \iff t = \frac{{{v0}}}{{{k}}}\text{{ (s)}}$.\\
Quãng đường ô tô di chuyển được từ lúc hãm phanh đến khi dừng hẳn là:
\[
s = \int_0^{{\frac{{{v0}}}{{{k}}}}} (-{k}t + {v0})\,\mathrm{{d}}t = \left(-\frac{{{k}t^2}}{{2}} + {v0}t\right)\Bigg|_0^{{\frac{{{v0}}}{{{k}}}}} = \frac{{{v0}^2}}{{2 \cdot {k}}} = {s_str}\text{{ (m)}}.
\]'''

    return caudan, shuffle_choices(correct, wrongs), loi_giai


# ==============================================================================
# BÀI 2: TÍCH PHÂN
# ==============================================================================

def CuoiChuong4_MC_B2_NB1():
    """B2. Tích phân - Mức độ: NB (Dạng 1): Công thức Newton - Leibniz & Đạo hàm tích phân"""
    variant = random.choice([1, 2, 3, 4, 5, 6])
    if variant == 1:
        # Công thức Newton - Leibniz (Câu 1 ảnh 1)
        caudan = r'''Cho hàm số $y = f(x)$ liên tục trên đoạn $[a; b]$ có một nguyên hàm là $F(x)$. Khẳng định nào sau đây là đúng?'''
        correct = r'''$\displaystyle\int_a^b f(x)\,\mathrm{d}x = F(b) - F(a)$'''
        wrongs = [
            r'''$\displaystyle\int_a^b f(x)\,\mathrm{d}x = f(b) - f(a)$''',
            r'''$\displaystyle\int_a^b f(x)\,\mathrm{d}x = f(b) + f(a)$''',
            r'''$\displaystyle\int_a^b f(x)\,\mathrm{d}x = F(b) + F(a)$'''
        ]
        loi_giai = r'''Theo định nghĩa tích phân và công thức Newton - Leibniz: $\displaystyle\int_a^b f(x)\,\mathrm{d}x = F(b) - F(a)$.'''

    elif variant == 2:
        # F(b) - F(a) có số cụ thể (Câu 15 ảnh 2)
        a = random.choice([1, 2])
        b = a + random.choice([2, 3, 4])
        fa = random.choice([2, 3, 5, -1])
        fb = random.choice([-2, 4, 7, -3])
        ans = fb - fa
        caudan = fr'''Cho hàm số $f(x)$ có một nguyên hàm trên $\mathbb{{R}}$ là $F(x)$. Biết $F({a}) = {fa}$ và $F({b}) = {fb}$, giá trị của $I = \displaystyle\int_{{{a}}}^{{{b}}} f(x)\,\mathrm{{d}}x$ bằng'''
        correct = fr'''${ans}$'''
        wrongs = [fr'''${-ans}$''', fr'''${fa + fb}$''', fr'''${abs(ans) + 2}$''']
        loi_giai = fr'''Áp dụng công thức Newton - Leibniz:
\[
I = \int_{{{a}}}^{{{b}}} f(x)\,\mathrm{{d}}x = F({b}) - F({a}) = {fb} - ({fa}) = {ans}.
\]'''

    elif variant == 3:
        # int_a^b f'(x) dx = f(b) - f(a) (Câu 16 ảnh 2)
        a = random.choice([1, 2])
        b = a + random.choice([1, 2])
        fa = random.randint(1, 4)
        fb = fa + random.choice([1, 2, 3, -2])
        ans = fb - fa
        caudan = fr'''Cho hàm số $f(x)$ có đạo hàm liên tục trên đoạn $[{a}; {b}]$, $f({a}) = {fa}$ và $f({b}) = {fb}$. Khi đó $I = \displaystyle\int_{{{a}}}^{{{b}}} f'(x)\,\mathrm{{d}}x$ bằng'''
        correct = fr'''${ans}$'''
        wrongs = [fr'''${-ans}$''', fr'''${fa + fb}$''', fr'''${ans + 3}$''']
        loi_giai = fr'''Ta có $\displaystyle\int_{{{a}}}^{{{b}}} f'(x)\,\mathrm{{d}}x = f(x)\Big|_{{{a}}}^{{{b}}} = f({b}) - f({a}) = {fb} - {fa} = {ans}$.'''

    elif variant == 4:
        # Cho f(a) = y1, int f'(x) dx = K, tính f(b) (Câu 21 ảnh 3)
        a = 1
        b = random.choice([3, 4, 5])
        fa = random.choice([10, 12, 15])
        K = random.choice([15, 17, 20])
        fb = fa + K
        caudan = fr'''Cho hàm số $f(x)$ thoả mãn $f({a}) = {fa}$, $f'(x)$ liên tục trên đoạn $[{a}; {b}]$ và $\displaystyle\int_{{{a}}}^{{{b}}} f'(x)\,\mathrm{{d}}x = {K}$. Tính $f({b})$.'''
        correct = fr'''${fb}$'''
        wrongs = [fr'''${K - fa}$''', fr'''${fb - 3}$''', fr'''${K}$''']
        loi_giai = fr'''Ta có $\displaystyle\int_{{{a}}}^{{{b}}} f'(x)\,\mathrm{{d}}x = f({b}) - f({a}) \implies {K} = f({b}) - {fa} \implies f({b}) = {fa} + {K} = {fb}$.'''

    elif variant == 5:
        # F(x) = sqrt(x) là nguyên hàm, tính int_1^4 [k + f(x)] dx (Bài 1 Tự luận ảnh 5)
        k = random.choice([2, 3, 4])
        ans = 3 * k + 1
        caudan = fr'''Biết $F(x) = \sqrt{{x}}$ là một nguyên hàm của hàm số $f(x)$ trên $(0; +\infty)$. Tính $I = \displaystyle\int_1^4 [{k} + f(x)]\,\mathrm{{d}}x$.'''
        correct = fr'''${ans}$'''
        wrongs = [fr'''${ans - 1}$''', fr'''${ans + 2}$''', fr'''${3 * k}$''']
        loi_giai = fr'''Ta có:
\[
I = \int_1^4 {k}\,\mathrm{{d}}x + \int_1^4 f(x)\,\mathrm{{d}}x = {k}(4 - 1) + F(4) - F(1) = {3*k} + \sqrt{{4}} - \sqrt{{1}} = {3*k} + 1 = {ans}.
\]'''

    else:
        # Khẳng định SAI về tích phân (Câu 2, 4 ảnh 1)
        sub = random.choice([1, 2])
        if sub == 1:
            caudan = r'''Cho hai hàm số $y = f(x), y = g(x)$ liên tục trên $[a; b]$ và số thực $k$ tuỳ ý. Khẳng định nào sau đây sai?'''
            correct = r'''$\displaystyle\int_a^b f(x) \cdot g(x)\,\mathrm{d}x = \int_a^b f(x)\,\mathrm{d}x \cdot \int_a^b g(x)\,\mathrm{d}x$'''
            wrongs = [
                r'''$\displaystyle\int_a^b k f(x)\,\mathrm{d}x = k \int_a^b f(x)\,\mathrm{d}x$''',
                r'''$\displaystyle\int_a^b [f(x) - g(x)]\,\mathrm{d}x = \int_a^b f(x)\,\mathrm{d}x - \int_a^b g(x)\,\mathrm{d}x$''',
                r'''$\displaystyle\int_a^b [f(x) + g(x)]\,\mathrm{d}x = \int_a^b f(x)\,\mathrm{d}x + \int_a^b g(x)\,\mathrm{d}x$'''
            ]
            loi_giai = r'''Tích phân của một tích không bằng tích các tích phân: $\displaystyle\int_a^b f(x)g(x)\,\mathrm{d}x \ne \int_a^b f(x)\,\mathrm{d}x \cdot \int_a^b g(x)\,\mathrm{d}x$. Do đó khẳng định trên là sai.'''
        else:
            caudan = r'''Cho hàm số $y = f(x)$ liên tục trên đoạn $[a; b]$, $c \in (a; b)$. Mệnh đề nào sau đây sai?'''
            correct = r'''$\displaystyle\int_a^b f(x)\,\mathrm{d}x = \int_b^a f(x)\,\mathrm{d}x$'''
            wrongs = [
                r'''$\displaystyle\int_a^b k\,\mathrm{d}x = k(b - a),\ \forall k \in \mathbb{R}$''',
                r'''$\displaystyle\int_a^b f(x)\,\mathrm{d}x = \int_a^b f(t)\,\mathrm{d}t$''',
                r'''$\displaystyle\int_a^b f(x)\,\mathrm{d}x = \int_a^c f(x)\,\mathrm{d}x + \int_c^b f(x)\,\mathrm{d}x$'''
            ]
            loi_giai = r'''Theo tính chất đổi cận của tích phân: $\displaystyle\int_a^b f(x)\,\mathrm{d}x = -\int_b^a f(x)\,\mathrm{d}x$. Do đó khẳng định $\displaystyle\int_a^b f(x)\,\mathrm{d}x = \int_b^a f(x)\,\mathrm{d}x$ là sai.'''

    return caudan, shuffle_choices(correct, wrongs), loi_giai


def CuoiChuong4_MC_B2_NB2():
    """B2. Tích phân - Mức độ: NB (Dạng 2): Tính chất cộng khoảng & tuyến tính của tích phân"""
    sub = random.choice([1, 2, 3, 4, 5])
    if sub == 1:
        # Đảo cận: int_a^b f = K => int_b^a f = -K (Câu 17 & 19 ảnh 2)
        a = random.choice([1, 3])
        b = a + random.choice([1, 2])
        K = random.choice([2, 5, 10, -3])
        ans = -K
        caudan = fr'''Cho hàm số $y = f(x)$ liên tục trên $\mathbb{{R}}$ và $\displaystyle\int_{{{a}}}^{{{b}}} f(x)\,\mathrm{{d}}x = {K}$. Biểu thức $\displaystyle\int_{{{b}}}^{{{a}}} f(x)\,\mathrm{{d}}x$ bằng'''
        correct = fr'''${ans}$'''
        wrongs = [fr'''${K}$''', fr'''${abs(K) + 1}$''', fr'''${-abs(K) - 2}$''']
        loi_giai = fr'''Theo tính chất đổi cận của tích phân: $\displaystyle\int_{{{b}}}^{{{a}}} f(x)\,\mathrm{{d}}x = -\int_{{{a}}}^{{{b}}} f(x)\,\mathrm{{d}}x = -({K}) = {ans}$.'''

    elif sub == 2:
        # Nối cận liên tiếp: int_0^2 + int_2^4 = int_0^4 (Câu 18 ảnh 2)
        i1 = random.choice([4, 6, 9])
        i2 = random.choice([3, 4, 5])
        ans = i1 + i2
        caudan = fr'''Cho hàm số $f(x)$ liên tục trên $\mathbb{{R}}$ và có $\displaystyle\int_0^2 f(x)\,\mathrm{{d}}x = {i1}$; $\displaystyle\int_2^4 f(x)\,\mathrm{{d}}x = {i2}$. Tính $I = \displaystyle\int_0^4 f(x)\,\mathrm{{d}}x$.'''
        correct = fr'''$I = {ans}$'''
        wrongs = [fr'''$I = {abs(i1 - i2)}$''', fr'''$I = {i1 * i2}$''', fr'''$I = {ans + 3}$''']
        loi_giai = fr'''Theo tính chất chèn cận liên tiếp của tích phân:
\[
I = \int_0^4 f(x)\,\mathrm{{d}}x = \int_0^2 f(x)\,\mathrm{{d}}x + \int_2^4 f(x)\,\mathrm{{d}}x = {i1} + {i2} = {ans}.
\]'''

    elif sub == 3:
        # Chèn cận trừ: int_0^1 = K1, int_0^3 = K2 => int_1^3 = K2 - K1 (Câu 20 ảnh 2)
        K1 = random.choice([-2, -1, 1, 2])
        K2 = random.choice([4, 5, 6])
        ans = K2 - K1
        caudan = fr'''Cho $\displaystyle\int_0^1 f(x)\,\mathrm{{d}}x = {K1}$; $\displaystyle\int_0^3 f(x)\,\mathrm{{d}}x = {K2}$. Giá trị của $\displaystyle\int_1^3 f(x)\,\mathrm{{d}}x$ bằng'''
        correct = fr'''${ans}$'''
        wrongs = [fr'''${K2 + K1}$''', fr'''${K1 - K2}$''', fr'''${ans + 2}$''']
        loi_giai = fr'''Ta có:
\[
\int_1^3 f(x)\,\mathrm{{d}}x = \int_0^3 f(x)\,\mathrm{{d}}x - \int_0^1 f(x)\,\mathrm{{d}}x = {K2} - ({K1}) = {ans}.
\]'''

    elif sub == 4:
        # Tuyến tính int [m*f + n*g] (Câu 22 & 23 ảnh 3)
        m = random.choice([2, 3])
        n = random.choice([4, 5])
        int_f = random.choice([3, 4])
        int_g = random.choice([-5, -3, 3])
        ans = m * int_f + n * int_g
        caudan = fr'''Cho $\displaystyle\int_0^2 f(x)\,\mathrm{{d}}x = {int_f}$ và $\displaystyle\int_0^2 g(x)\,\mathrm{{d}}x = {int_g}$, khi đó $\displaystyle\int_0^2 [{m}f(x) + {n}g(x)]\,\mathrm{{d}}x$ bằng'''
        correct = fr'''${ans}$'''
        wrongs = [fr'''${ans + 4}$''', fr'''${ans - 3}$''', fr'''${m * int_f - n * int_g}$''']
        loi_giai = fr'''Áp dụng tính chất tuyến tính của tích phân:
\[
\int_0^2 [{m}f(x) + {n}g(x)]\,\mathrm{{d}}x = {m}\int_0^2 f(x)\,\mathrm{{d}}x + {n}\int_0^2 g(x)\,\mathrm{{d}}x = {m} \cdot ({int_f}) + {n} \cdot ({int_g}) = {ans}.
\]'''

    else:
        # Tách tích phân trị tuyệt đối (Câu 13 ảnh 2)
        caudan = r'''Cho tích phân $I = \displaystyle\int_{-1}^3 |2x - 4|\,\mathrm{d}x$. Khẳng định nào sau đây đúng?'''
        correct = r'''$I = -\displaystyle\int_{-1}^2 (2x - 4)\,\mathrm{d}x + \int_2^3 (2x - 4)\,\mathrm{d}x$'''
        wrongs = [
            r'''$I = \left|\displaystyle\int_{-1}^3 (2x - 4)\,\mathrm{d}x\right|$''',
            r'''$I = \displaystyle\int_{-1}^2 (2x - 4)\,\mathrm{d}x + \int_2^3 (2x - 4)\,\mathrm{d}x$''',
            r'''$I = \displaystyle\int_{-1}^2 (2x - 4)\,\mathrm{d}x - \int_2^3 (2x - 4)\,\mathrm{d}x$'''
        ]
        loi_giai = r'''Xét dấu nhị thức bậc nhất $2x - 4$:\\
$2x - 4 = 0 \iff x = 2 \in (-1; 3)$.\\
- Với $x \in [-1; 2]$, ta có $2x - 4 \le 0 \implies |2x - 4| = -(2x - 4)$.\\
- Với $x \in [2; 3]$, ta có $2x - 4 \ge 0 \implies |2x - 4| = 2x - 4$.\\
Do đó: $I = -\displaystyle\int_{-1}^2 (2x - 4)\,\mathrm{d}x + \int_2^3 (2x - 4)\,\mathrm{d}x$.'''

    return caudan, shuffle_choices(correct, wrongs), loi_giai


def CuoiChuong4_MC_B2_TH():
    """B2. Tích phân - Mức độ: TH: Tính tích phân cụ thể của hàm đa thức, lượng giác, mũ, phân thức"""
    sub = random.choice([1, 2, 3, 4, 5, 6, 7])
    if sub == 1:
        # int_0^1 (3x^2 + 2x) dx = 2 hoặc int_0^1 (2024x + 2025) dx (Câu 3 & 8 ảnh 1)
        sub_p = random.choice([1, 2])
        if sub_p == 1:
            a = random.choice([3, 6])
            b = random.choice([2, 4])
            ans = a // 3 + b // 2
            caudan = fr'''Tích phân $I = \displaystyle\int_0^1 ({a}x^2 + {b}x)\,\mathrm{{d}}x$ bằng'''
            correct = fr'''${ans}$'''
            wrongs = [fr'''$0$''', fr'''${ans + 2}$''', fr'''${-ans}$''']
            loi_giai = fr'''Ta có:
\[
I = \left( \frac{{{a}x^3}}{{3}} + \frac{{{b}x^2}}{{2}} \right)\Bigg|_0^1 = \left( {a//3} \cdot 1^3 + {b//2} \cdot 1^2 \right) - 0 = {ans}.
\]'''
        else:
            K1 = 2024
            K2 = 2025
            ans = K1 // 2 + K2
            caudan = fr'''Tính tích phân $I = \displaystyle\int_0^1 ({K1}x + {K2})\,\mathrm{{d}}x$.'''
            correct = fr'''${ans}$'''
            wrongs = [fr'''${K1 + K2}$''', fr'''${-ans}$''', fr'''${K2 - K1 // 2}$''']
            loi_giai = fr'''Ta có:
\[
I = \left({K1 // 2}x^2 + {K2}x\right)\Bigg|_0^1 = {K1 // 2} \cdot 1^2 + {K2} \cdot 1 = {ans}.
\]'''

    elif sub == 2:
        # int_0^{pi/6} cos x dx hoặc int_0^{pi/3} cos x dx (Câu 5 & 10 ảnh 1)
        sub_trig = random.choice([1, 2])
        if sub_trig == 1:
            caudan = r'''Tính tích phân $\displaystyle\int_0^{\frac{\pi}{6}} \cos x\,\mathrm{d}x$.'''
            correct = r'''$\displaystyle\frac{1}{2}$'''
            wrongs = [r'''$-\displaystyle\frac{1}{2}$''', r'''$1$''', r'''$-1$''']
            loi_giai = r'''Ta có: $\displaystyle\int_0^{\frac{\pi}{6}} \cos x\,\mathrm{d}x = \sin x\Big|_0^{\frac{\pi}{6}} = \sin\left(\frac{\pi}{6}\right) - \sin(0) = \frac{1}{2} - 0 = \frac{1}{2}$.'''
        else:
            caudan = r'''Tích phân $I = \displaystyle\int_0^{\frac{\pi}{3}} \cos x\,\mathrm{d}x$ bằng'''
            correct = r'''$\displaystyle\frac{\sqrt{3}}{2}$'''
            wrongs = [r'''$-\displaystyle\frac{\sqrt{3}}{2}$''', r'''$\displaystyle\frac{1}{2}$''', r'''$-\displaystyle\frac{1}{2}$''']
            loi_giai = r'''Ta có: $I = \sin x\Big|_0^{\frac{\pi}{3}} = \sin\left(\frac{\pi}{3}\right) - \sin(0) = \frac{\sqrt{3}}{2}$.'''

    elif sub == 3:
        # int_1^2 a^x dx = (a^2 - a) / ln a (Câu 7 ảnh 1)
        a = random.choice([2, 3, 5])
        num = (a ** 2) - a
        caudan = fr'''Kết quả phép tính $\displaystyle\int_1^2 {a}^x\,\mathrm{{d}}x$ bằng'''
        correct = fr'''$\displaystyle\frac{{{num}}}{{\ln {a}}}$'''
        wrongs = [
            fr'''$\displaystyle\frac{{{num - 1}}}{{\ln {a}}}$''',
            fr'''${num}$''',
            fr'''$-\displaystyle\frac{{{num}}}{{\ln {a}}}$'''
        ]
        loi_giai = fr'''Ta có:
\[
\int_1^2 {a}^x\,\mathrm{{d}}x = \frac{{{a}^x}}{{\ln {a}}}\Bigg|_1^2 = \frac{{{a}^2 - {a}}}{{\ln {a}}} = \frac{{{num}}}{{\ln {a}}}.
\]'''

    elif sub == 4:
        # int_0^2 (x^2 + 1)^2 dx = 206 / 15 (Câu 9 ảnh 1)
        caudan = r'''Tính tích phân $I = \displaystyle\int_0^2 (x^2 + 1)^2\,\mathrm{d}x$.'''
        correct = r'''$\displaystyle\frac{206}{15}$'''
        wrongs = [r'''$\displaystyle\frac{260}{15}$''', r'''$\displaystyle\frac{33}{4}$''', r'''$\displaystyle\frac{34}{3}$''']
        loi_giai = r'''Khai triển hằng đẳng thức rồi tính tích phân:
\[
I = \int_0^2 (x^4 + 2x^2 + 1)\,\mathrm{d}x = \left(\frac{x^5}{5} + \frac{2x^3}{3} + x\right)\Bigg|_0^2 = \frac{32}{5} + \frac{16}{3} + 2 = \frac{206}{15}.
\]'''

    elif sub == 5:
        # int_1^3 (2x^2 + 1)/x dx = 8 + ln 3 (Câu 11 ảnh 1)
        caudan = r'''Tính tích phân $I = \displaystyle\int_1^3 \frac{2x^2 + 1}{x}\,\mathrm{d}x$.'''
        correct = r'''$8 + \ln 3$'''
        wrongs = [r'''$8 - \ln 3$''', r'''$8 + 2\ln 3$''', r'''$7 + \ln 3$''']
        loi_giai = r'''Ta có:
\[
I = \int_1^3 \left(2x + \frac{1}{x}\right)\,\mathrm{d}x = \left(x^2 + \ln|x|\right)\Bigg|_1^3 = (9 + \ln 3) - (1 + \ln 1) = 8 + \ln 3.
\]'''

    elif sub == 6:
        # Biết int_{pi/3}^{pi/2} cos x dx = a + b sqrt(3), tính T = 2a + 6b (Câu 24 ảnh 3)
        caudan = r'''Biết $\displaystyle\int_{\frac{\pi}{3}}^{\frac{\pi}{2}} \cos x\,\mathrm{d}x = a + b\sqrt{3}$, với $a, b$ là các số hữu tỉ. Tính $T = 2a + 6b$.'''
        correct = r'''$T = -1$'''
        wrongs = [r'''$T = 2$''', r'''$T = -4$''', r'''$T = 3$''']
        loi_giai = r'''Ta có:
\[
\int_{\frac{\pi}{3}}^{\frac{\pi}{2}} \cos x\,\mathrm{d}x = \sin x\Big|_{\frac{\pi}{3}}^{\frac{\pi}{2}} = \sin\left(\frac{\pi}{2}\right) - \sin\left(\frac{\pi}{3}\right) = 1 - \frac{\sqrt{3}}{2} = 1 + \left(-\frac{1}{2}\right)\sqrt{3}.
\]
Suy ra $a = 1$ và $b = -\frac{1}{2}$.\\
Vậy $T = 2a + 6b = 2(1) + 6\left(-\frac{1}{2}\right) = 2 - 3 = -1$.'''

    else:
        # Tích phân hàm phân nhánh (Câu 3 Đúng/Sai ảnh 4)
        caudan = r'''Cho hàm số $f(x) = \begin{cases} x^2 - 2x & \text{khi } x \ge 2 \\ x - 2 & \text{khi } x < 2 \end{cases}$. Giá trị của $\displaystyle\int_1^3 f(x)\,\mathrm{d}x$ bằng'''
        correct = r'''$\displaystyle\frac{5}{6}$'''
        wrongs = [r'''$\displaystyle\frac{1}{2}$''', r'''$\displaystyle\frac{7}{6}$''', r'''$1$''']
        loi_giai = r'''Tách tích phân theo cận $x = 2$:
\[
\int_1^3 f(x)\,\mathrm{d}x = \int_1^2 (x - 2)\,\mathrm{d}x + \int_2^3 (x^2 - 2x)\,\mathrm{d}x = \left(\frac{x^2}{2} - 2x\right)\Bigg|_1^2 + \left(\frac{x^3}{3} - x^2\right)\Bigg|_2^3 = -\frac{1}{2} + \frac{4}{3} = \frac{5}{6}.
\]'''

    return caudan, shuffle_choices(correct, wrongs), loi_giai


def CuoiChuong4_MC_B2_VD():
    """B2. Tích phân - Mức độ: VD: Bài toán thực tế tốc độ thay đổi lượng điện tiêu thụ / bơm nước"""
    sub = random.choice([1, 2])
    if sub == 1:
        # Bài toán tốc độ tiêu thụ điện năng (Câu 15 ảnh 5)
        a = random.choice([6, 8, 10])
        val = 15 / math.log(2) + 4 * a
        val_str = f"{val:.2f}".replace('.', ',')
        w1_str = f"{val + 8.5:.2f}".replace('.', ',')
        w2_str = f"{val - 7.2:.2f}".replace('.', ',')
        w3_str = f"{val + 15.0:.2f}".replace('.', ',')
        caudan = fr'''Tốc độ thay đổi lượng điện tiêu thụ (đơn vị: triệu kWh/năm) của một khu công nghiệp $A$ từ năm 2020 đến năm 2024 được mô tả bởi hàm số $E'_A(t) = 2^t + {a}$, trong đó $t$ là số năm kể từ đầu năm 2020 ($0 \le t \le 4$). Tổng lượng điện tiêu thụ tăng thêm của khu công nghiệp $A$ sau 4 năm khảo sát xấp xỉ bằng'''
        correct = fr'''${val_str}\text{{ triệu kWh}}$'''
        wrongs = [
            fr'''${w1_str}\text{{ triệu kWh}}$''',
            fr'''${w2_str}\text{{ triệu kWh}}$''',
            fr'''${w3_str}\text{{ triệu kWh}}$'''
        ]
        loi_giai = fr'''Tổng lượng điện tiêu thụ tăng thêm của khu công nghiệp $A$ sau 4 năm chính là tích phân của tốc độ tiêu thụ theo thời gian:
\[
\Delta E = \int_0^4 E'_A(t)\,\mathrm{{d}}t = \int_0^4 (2^t + {a})\,\mathrm{{d}}t = \left(\frac{{2^t}}{{\ln 2}} + {a}t\right)\Bigg|_0^4 = \frac{{15}}{{\ln 2}} + {4*a} \approx {val_str}\text{{ (triệu kWh)}}.
\]'''

    else:
        # Bơm nước vào bể với tốc độ v(t) = at + b
        a = random.choice([2, 4, 6])
        b = random.choice([10, 20, 30])
        T = random.choice([5, 10])
        V_ans = (a // 2) * (T ** 2) + b * T
        caudan = fr'''Một bể nước ban đầu không có nước. Người ta bắt đầu bơm nước vào bể với tốc độ bơm tại thời điểm $t$ (phút) được cho bởi hàm số $v(t) = {a}t + {b}\text{{ (lít/phút)}}$. Hỏi sau $T = {T}\text{{ phút}}$, tổng thể tích nước đã được bơm vào bể bằng bao nhiêu lít?'''
        correct = fr'''${V_ans}\text{{ lít}}$'''
        wrongs = [
            fr'''${V_ans + random.choice([25, 50])}\text{{ lít}}$''',
            fr'''${V_ans - random.choice([20, 30])}\text{{ lít}}$''',
            fr'''${a * T + b}\text{{ lít}}$'''
        ]
        loi_giai = fr'''Tổng thể tích nước được bơm vào bể sau ${T}$ phút chính là tích phân của tốc độ bơm theo thời gian:
\[
V = \int_0^{{{T}}} v(t)\,\mathrm{{d}}t = \int_0^{{{T}}} ({a}t + {b})\,\mathrm{{d}}t = \left( \frac{{{a}t^2}}{{2}} + {b}t \right)\Bigg|_0^{{{T}}} = {a//2} \cdot ({T})^2 + {b} \cdot {T} = {V_ans}\text{{ (lít)}}.
\]'''

    return caudan, shuffle_choices(correct, wrongs), loi_giai


# ==============================================================================
# BÀI 3: ỨNG DỤNG HÌNH HỌC CỦA TÍCH PHÂN
# ==============================================================================

def CuoiChuong4_MC_B3_NB1():
    """B3. Ứng dụng hình học - Mức độ: NB (Dạng 1): Công thức diện tích hình phẳng"""
    variant = random.choice([1, 2])
    if variant == 1:
        caudan = r'''Cho hàm số $y = f(x)$ liên tục trên đoạn $[a; b]$. Diện tích $S$ của hình phẳng giới hạn bởi đồ thị hàm số $y = f(x)$, trục hoành và hai đường thẳng $x = a, x = b$ được tính theo công thức nào dưới đây?'''
        correct = r'''$S = \displaystyle\int_a^b |f(x)|\,\mathrm{d}x$'''
        wrongs = [
            r'''$S = \displaystyle\int_a^b f(x)\,\mathrm{d}x$''',
            r'''$S = \displaystyle\pi \int_a^b [f(x)]^2\,\mathrm{d}x$''',
            r'''$S = \displaystyle\left| \int_a^b f(x)\,\mathrm{d}x \right|$'''
        ]
        loi_giai = r'''Theo công thức định nghĩa trong SGK, diện tích hình phẳng giới hạn bởi đồ thị hàm số $y = f(x)$, trục hoành và hai đường thẳng $x = a, x = b$ là $S = \displaystyle\int_a^b |f(x)|\,\mathrm{d}x$.'''
    else:
        caudan = r'''Diện tích hình phẳng giới hạn bởi đồ thị hai hàm số $y = f(x)$, $y = g(x)$ liên tục trên đoạn $[a; b]$ và hai đường thẳng $x = a, x = b$ được tính theo công thức:'''
        correct = r'''$S = \displaystyle\int_a^b |f(x) - g(x)|\,\mathrm{d}x$'''
        wrongs = [
            r'''$S = \displaystyle\int_a^b [f(x) - g(x)]\,\mathrm{d}x$''',
            r'''$S = \displaystyle\pi \int_a^b [f(x) - g(x)]^2\,\mathrm{d}x$''',
            r'''$S = \displaystyle\int_a^b |f(x)|\,\mathrm{d}x - \int_a^b |g(x)|\,\mathrm{d}x$'''
        ]
        loi_giai = r'''Công thức diện tích hình phẳng giới hạn bởi 2 đường cong là: $S = \displaystyle\int_a^b |f(x) - g(x)|\,\mathrm{d}x$.'''

    return caudan, shuffle_choices(correct, wrongs), loi_giai


def CuoiChuong4_MC_B3_NB2():
    """B3. Ứng dụng hình học - Mức độ: NB (Dạng 2): Công thức thể tích khối tròn xoay"""
    caudan = r'''Cho hình phẳng $(H)$ giới hạn bởi đồ thị hàm số $y = f(x)$ liên tục trên đoạn $[a; b]$, trục hoành và hai đường thẳng $x = a, x = b$. Thể tích $V$ của khối tròn xoay sinh ra khi quay hình $(H)$ quanh trục $Ox$ được tính theo công thức nào dưới đây?'''
    correct = r'''$V = \pi \displaystyle\int_a^b [f(x)]^2\,\mathrm{d}x$'''
    wrongs = [
        r'''$V = \displaystyle\int_a^b [f(x)]^2\,\mathrm{d}x$''',
        r'''$V = \pi \displaystyle\int_a^b |f(x)|\,\mathrm{d}x$''',
        r'''$V = \pi^2 \displaystyle\int_a^b [f(x)]^2\,\mathrm{d}x$'''
    ]
    loi_giai = r'''Thể tích khối tròn xoay quay quanh trục $Ox$ được tính theo công thức: $V = \pi \displaystyle\int_a^b [f(x)]^2\,\mathrm{d}x$.'''

    return caudan, shuffle_choices(correct, wrongs), loi_giai


def CuoiChuong4_MC_B3_TH():
    """B3. Ứng dụng hình học - Mức độ: TH: Tính diện tích hình phẳng giới hạn bởi parabol và trục hoành"""
    # y = -x^2 + a^2 => cắt trục hoành tại x = -a và x = a
    # S = int_{-a}^a (a^2 - x^2) dx = 2 * (a^3 - a^3/3) = 4*a^3/3
    a = random.choice([2, 3])
    a2 = a ** 2
    S_frac = Fraction(4 * (a ** 3), 3)
    
    caudan = fr'''Diện tích hình phẳng giới hạn bởi đồ thị hàm số $y = -x^2 + {a2}$ và trục hoành $Ox$ bằng bao nhiêu?'''
    correct = fr'''${fmt_frac(S_frac.numerator, S_frac.denominator)}$'''
    wrongs = [
        fr'''${fmt_frac(2 * (a ** 3), 3)}$''',
        fr'''${fmt_frac(8 * (a ** 3), 3)}$''',
        fr'''${a2}$'''
    ]
    
    loi_giai = fr'''Phương trình hoành độ giao điểm của parabol với trục hoành:
\[
-x^2 + {a2} = 0 \iff x = \pm {a}.
\]
Trên đoạn $[-{a}; {a}]$, ta có $-x^2 + {a2} \ge 0$.\\
Diện tích hình phẳng cần tìm là:
\[
S = \int_{{-{a}}}^{{{a}}} (-x^2 + {a2})\,\mathrm{{d}}x = \left( - \frac{{x^3}}{{3}} + {a2}x \right)\Bigg|_{{-{a}}}^{{{a}}} = \frac{{4 \cdot {a}^3}}{{3}} = {fmt_frac(S_frac.numerator, S_frac.denominator)}.
\]'''

    return caudan, shuffle_choices(correct, wrongs), loi_giai


def CuoiChuong4_MC_B3_VD():
    """B3. Ứng dụng hình học - Mức độ: VD: Toán thực tế vòm cửa parabol hoặc thùng chứa tròn xoay"""
    # Cửa vòm Parabol có chiều cao h (m) và chiều rộng đáy w = 2*d (m)
    # y = h - (h / d^2) * x^2 => S = (4/3) * h * d = (2/3) * h * w
    h = random.choice([3, 4, 6])
    w = random.choice([4, 6])
    d = w // 2
    
    # S = (2/3) * h * w
    S = (2 * h * w) // 3
    cost_per_m2 = random.choice([500, 800, 1000])  # nghìn đồng
    total_cost = S * cost_per_m2
    
    caudan = fr'''Một cổng chào có hình dáng là một đường parabol với chiều cao $h = {h}\text{{ m}}$ và chiều rộng chân cổng là $w = {w}\text{{ m}}$. Người ta muốn sơn toàn bộ bề mặt mặt trước của cổng chào đó. Biết chi phí sơn là ${cost_per_m2}\,000\text{{ đồng/m}}^2$. Tổng chi phí sơn cổng chào bằng bao nhiêu?'''
    
    cost_fmt = f"{total_cost:,}".replace(',', '.')
    cost_p2_fmt = f"{(S + 2) * cost_per_m2:,}".replace(',', '.')
    cost_hw_fmt = f"{h * w * cost_per_m2:,}".replace(',', '.')
    cost_m2_fmt = f"{(S - 2) * cost_per_m2:,}".replace(',', '.')
    
    correct = fr'''${cost_fmt}\text{{ }}000\text{{ đồng}}$'''
    wrongs = [
        fr'''${cost_p2_fmt}\text{{ }}000\text{{ đồng}}$''',
        fr'''${cost_hw_fmt}\text{{ }}000\text{{ đồng}}$''',
        fr'''${cost_m2_fmt}\text{{ }}000\text{{ đồng}}$'''
    ]
    
    loi_giai = fr'''Chọn hệ trục tọa độ $Oxy$ với gốc $O$ là trung điểm chân cổng, trục $Oy$ hướng lên trên.\\
Khi đó, đỉnh parabol là $I(0; {h})$ và cổng cắt trục hoành tại hai điểm có hoành độ $x = \pm {d}$.\\
Phương trình parabol có dạng: $y = {h} - \frac{{{h}}}{{{d}^2}} x^2 = {h} - \frac{{{h}}}{{{d**2}}} x^2$.\\
Diện tích của cổng chào là:
\[
S = \int_{{-{d}}}^{{{d}}} \left({h} - \frac{{{h}}}{{{d**2}}} x^2\right)\,\mathrm{{d}}x = \frac{{2}}{{3}} \cdot h \cdot w = \frac{{2}}{{3}} \cdot {h} \cdot {w} = {S}\text{{ (m}}^2\text{{)}}.
\]
Tổng chi phí sơn cổng chào là:
\[
T = {S} \cdot {cost_per_m2}\,000 = {cost_fmt}\text{{ }}000\text{{ (đồng)}}.
\]'''

    return caudan, shuffle_choices(correct, wrongs), loi_giai


# Alias tương thích ngược
CuoiChuong4_MC_Cau1 = CuoiChuong4_MC_B1_NB1
CuoiChuong4_MC_Cau2 = CuoiChuong4_MC_B1_NB2
CuoiChuong4_MC_Cau3 = CuoiChuong4_MC_B1_TH
CuoiChuong4_MC_Cau4 = CuoiChuong4_MC_B1_VD
CuoiChuong4_MC_Cau5 = CuoiChuong4_MC_B2_NB1
CuoiChuong4_MC_Cau6 = CuoiChuong4_MC_B2_NB2
CuoiChuong4_MC_Cau7 = CuoiChuong4_MC_B2_TH
CuoiChuong4_MC_Cau8 = CuoiChuong4_MC_B2_VD
CuoiChuong4_MC_Cau9 = CuoiChuong4_MC_B3_NB1
CuoiChuong4_MC_Cau10 = CuoiChuong4_MC_B3_NB2
CuoiChuong4_MC_Cau11 = CuoiChuong4_MC_B3_TH
CuoiChuong4_MC_Cau12 = CuoiChuong4_MC_B3_VD
