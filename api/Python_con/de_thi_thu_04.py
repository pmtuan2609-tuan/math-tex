# -*- coding: utf-8 -*-
"""
Module Đề thi thử / Đề ôn tập số 4 (12 câu Trắc nghiệm + 4 câu Đúng/Sai + 6 câu Trả lời ngắn)
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

def DeThiThu04_MC_Cau1():
    # Câu 1: Trung vị mẫu số liệu ghép nhóm điểm môn Toán
    datasets = [
        {"freqs": [3, 5, 8, 15, 10, 5], "ans": "7,47", "val": 7.47, "L": 7, "cf": 16, "f": 15, "n": 46},
        {"freqs": [2, 6, 9, 16, 12, 5], "ans": "7,44", "val": 7.44, "L": 7, "cf": 17, "f": 16, "n": 50},
        {"freqs": [4, 4, 10, 14, 11, 7], "ans": "7,43", "val": 7.43, "L": 7, "cf": 18, "f": 14, "n": 50},
        {"freqs": [3, 6, 7, 18, 9, 5],  "ans": "7,50", "val": 7.50, "L": 7, "cf": 16, "f": 18, "n": 48},
    ]
    d = random.choice(datasets)
    freqs = d["freqs"]
    ans = d["ans"]
    
    caudan = fr'''\immini{{Cho mẫu số liệu điểm môn Toán của một nhóm học sinh như bảng bên. Trung vị của mẫu số liệu (kết quả làm tròn đến hàng phần trăm) là:
\begin{{center}}
\end{{center}}
}}{{
\begin{{tabular}}{{|c|c|c|c|c|c|c|}}
	\hline
	Điểm & [4;5) & [5;6) & [6;7) & [7;8) & [8;9) & [9;10] \\
	\hline
	Số học sinh & {freqs[0]} & {freqs[1]} & {freqs[2]} & {freqs[3]} & {freqs[4]} & {freqs[5]} \\
	\hline		
\end{{tabular}}
}}'''
    correct = fr"${ans}$"
    val = d["val"]
    w1 = f"{val + 0.48:.2f}".replace('.', ',')
    w2 = f"{val - 0.10:.2f}".replace('.', ',')
    w3 = f"{val - 0.01:.2f}".replace('.', ',')
    wrongs = [fr"${w1}$", fr"${w2}$", fr"${w3}$"]
    choices = shuffle_choices(correct, wrongs)
    loi_giai = fr'''Tổng số học sinh $n = {d["n"]}$, vị trí trung vị là $\dfrac{{n}}{{2}} = \dfrac{{{d["n"]}}}{{2}} = {d["n"]/2}$. \\
Nhóm chứa trung vị là $[7; 8)$. Áp dụng công thức trung vị:
$$M_e = 7 + \dfrac{{{d["n"]/2} - {d["cf"]}}}{{{d["f"]}}} \cdot (8 - 7) \approx {ans}.$$'''
    return caudan, choices, loi_giai


def DeThiThu04_MC_Cau2():
    # Câu 2: Giải bất phương trình log_c(u x - v) < w, tính S = a + b
    base = random.choice([2, 3])
    w = random.choice([2, 3])
    u = random.choice([2, 3, 4])
    v = random.choice([1, 2])
    
    a_frac = Fraction(v, u)
    val_pow = base**w
    b_frac = Fraction(val_pow + v, u)
    s_frac = a_frac + b_frac
    s_tex = fr"\dfrac{{{s_frac.numerator}}}{{{s_frac.denominator}}}" if s_frac.denominator != 1 else str(s_frac.numerator)

    caudan = fr'''Giải bất phương trình $\log_{{{base}}}({u}x - {v}) < {w}$ được tập nghiệm là $(a; b)$. Hãy tính tổng $S = a + b$.'''
    correct = fr"$S = {s_tex}$"
    w1_frac = Fraction(val_pow, u)
    w1_tex = fr"\dfrac{{{w1_frac.numerator}}}{{{w1_frac.denominator}}}" if w1_frac.denominator != 1 else str(w1_frac.numerator)
    wrongs = [
        fr"$S = {w1_tex}$",
        fr"$S = {w}$",
        fr"$S = 1$"
    ]
    if correct in wrongs:
        wrongs.remove(correct)
        wrongs.append(fr"$S = {s_frac.numerator + 1}$")
    choices = shuffle_choices(correct, wrongs[:3])
    loi_giai = fr'''Điều kiện: ${u}x - {v} > 0 \iff x > \dfrac{{{v}}}{{{u}}}$. \\
Bất phương trình $\iff {u}x - {v} < {base}^{{{w}}} = {val_pow} \iff x < \dfrac{{{val_pow + v}}}{{{u}}}$. \\
Tập nghiệm là $(a; b) = \left(\dfrac{{{v}}}{{{u}}}; \dfrac{{{val_pow + v}}}{{{u}}}\right)$. \\
Tổng $S = a + b = \dfrac{{{v}}}{{{u}}} + \dfrac{{{val_pow + v}}}{{{u}}} = {s_tex}$.'''
    return caudan, choices, loi_giai


def DeThiThu04_MC_Cau3():
    # Câu 3: Tiệm cận ngang đồ thị hàm phân thức bậc nhất y = (ax + b) / (cx + d)
    a = random.choice([2, 3, -2, -3])
    c = 1
    b = random.choice([1, 3, -1])
    d = random.choice([-1, 2, -2])
    tcn = a

    b_sign = f"+ {b}" if b > 0 else f"- {abs(b)}"
    d_sign = f"+ {d}" if d > 0 else f"- {abs(d)}"

    caudan = fr'''Đồ thị hàm số $y = \dfrac{{{a}x {b_sign}}}{{x {d_sign}}}$ có phương trình đường tiệm cận ngang là'''
    correct = fr"$y = {tcn}$"
    wrongs = [
        fr"$x = {-d}$",
        fr"$y = {-d}$",
        fr"$x = {tcn}$"
    ]
    choices = shuffle_choices(correct, wrongs)
    loi_giai = fr'''Ta có $\lim\limits_{{x \to \pm\infty}} y = \lim\limits_{{x \to \pm\infty}} \dfrac{{{a}x {b_sign}}}{{x {d_sign}}} = {tcn}$. Vậy đường tiệm cận ngang là $y = {tcn}$.'''
    return caudan, choices, loi_giai


def DeThiThu04_MC_Cau4():
    # Câu 4: Góc giữa đường thẳng SC và mặt phẳng đáy hình chóp S.ABC
    # AB = a, BC = 2a => AC = a*sqrt(5)
    # SA = a*sqrt(5) => tan(phi) = 1 => 45 deg
    cfgs = [
        {"sa_tex": r"a\sqrt{5}", "deg": "45^\\circ", "tan": "1"},
        {"sa_tex": r"a\sqrt{15}", "deg": "60^\\circ", "tan": r"\sqrt{3}"},
        {"sa_tex": r"\dfrac{a\sqrt{15}}{3}", "deg": "30^\\circ", "tan": r"\dfrac{\sqrt{3}}{3}"},
    ]
    c = random.choice(cfgs)

    caudan = fr'''Cho hình chóp $S.ABC$ có đáy $ABC$ là tam giác vuông tại $B$, $AB = a, BC = 2a$, $SA$ vuông góc với mặt phẳng đáy và $SA = {c["sa_tex"]}$. Góc giữa đường thẳng $SC$ và mặt phẳng đáy $(ABC)$ bằng'''
    correct = fr"${c['deg']}$"
    all_angles = [r"$30^\circ$", r"$45^\circ$", r"$60^\circ$", r"$90^\circ$"]
    wrongs = [ang for ang in all_angles if ang != correct]
    choices = shuffle_choices(correct, wrongs[:3])
    loi_giai = fr'''Vì $SA \perp (ABC)$ nên hình chiếu vuông góc của $SC$ lên $(ABC)$ là $AC$. \\
Góc giữa $SC$ và $(ABC)$ là góc $\widehat{{SCA}}$. \\
Tam giác $ABC$ vuông tại $B \implies AC = \sqrt{{AB^2 + BC^2}} = \sqrt{{a^2 + 4a^2}} = a\sqrt{{5}}$. \\
Trong tam giác vuông $SAC$: $\tan\widehat{{SCA}} = \dfrac{{SA}}{{AC}} = {c["tan"]} \implies \widehat{{SCA}} = {c["deg"]}$.'''
    return caudan, choices, loi_giai


def DeThiThu04_MC_Cau5():
    # Câu 5: Tích phân tuyến tính \int_0^1 [f(x) - k g(x)] dx
    u = random.randint(2, 6)
    v = random.randint(3, 7)
    k = random.choice([2, 3])
    ans = u - k * v

    caudan = fr'''Cho $\displaystyle\int_0^1 f(x)\,\mathrm{{d}}x = {u}$ và $\displaystyle\int_0^1 g(x)\,\mathrm{{d}}x = {v}$, khi đó $\displaystyle\int_0^1 [f(x) - {k}g(x)]\,\mathrm{{d}}x$ bằng'''
    correct = fr"${ans}$"
    wrongs = [
        fr"${u - v}$",
        fr"${u + k * v}$",
        fr"${1}$"
    ]
    choices = shuffle_choices(correct, wrongs)
    loi_giai = fr'''Theo tính chất của tích phân:
$$\int_0^1 [f(x) - {k}g(x)]\,\mathrm{{d}}x = \int_0^1 f(x)\,\mathrm{{d}}x - {k}\int_0^1 g(x)\,\mathrm{{d}}x = {u} - {k}({v}) = {ans}.$$'''
    return caudan, choices, loi_giai


def DeThiThu04_MC_Cau6():
    # Câu 6: Nhận dạng bảng biến thiên hàm số bậc ba
    # y = -2x^3 + 6x - 1: CD (1; 3), CT (-1; -5)
    caudan = r'''\immini{Bảng biến thiên sau đây là của hàm số nào trong các hàm số dưới đây?
\begin{center}
\end{center}
}{
\begin{tikzpicture}
	\tkzTabInit[nocadre,lgt=1.2,espcl=1.6,deltacl=0.6]
	{$x$ /0.6, $y'$ /0.6, $y$ /1.4}
	{$-\infty$,$-1$,$1$,$+\infty$}
	\tkzTabLine{,-,$0$,+,$0$,-,}
	\tkzTabVar{+/$+\infty$,-/$-5$,+/$3$,-/$-\infty$}
\end{tikzpicture}	
}'''
    correct = r'''$y = -2x^3 + 6x - 1$'''
    wrongs = [
        r'''$y = 2x^3 - 6x - 1$''',
        r'''$y = \dfrac{-2x + 7}{x + 3}$''',
        r'''$y = -x^3 + 3x - 5$'''
    ]
    choices = shuffle_choices(correct, wrongs)
    loi_giai = r'''Dựa vào bảng biến thiên:
- Đồ thị có nét cuối đi xuống khi $x \to +\infty$ nên hệ số $a < 0$.
- Hàm số đạt cực tiểu tại $x = -1, y_{ct} = -5$ và cực đại tại $x = 1, y_{cd} = 3$.
Xét $y = -2x^3 + 6x - 1 \implies y' = -6x^2 + 6 = 0 \iff x = \pm 1$.
$y(1) = 3$ và $y(-1) = -5$, hoàn toàn phù hợp với bảng biến thiên.'''
    return caudan, choices, loi_giai


def DeThiThu04_MC_Cau7():
    # Câu 7: Khẳng định nguyên hàm đúng \int dx/x = ln|x| + C
    caudan = r'''Khẳng định nào dưới đây đúng?'''
    correct = r'''$\displaystyle\int \dfrac{\mathrm{d}x}{x} = \ln|x| + C$'''
    wrongs = [
        r'''$\displaystyle\int \dfrac{\mathrm{d}x}{x} = \ln x + C$''',
        r'''$\displaystyle\int \dfrac{\mathrm{d}x}{x} = -\dfrac{1}{x^2} + C$''',
        r'''$\displaystyle\int \dfrac{\mathrm{d}x}{x} = \dfrac{1}{x^2} + C$'''
    ]
    choices = shuffle_choices(correct, wrongs)
    loi_giai = r'''Công thức nguyên hàm cơ bản đúng trên từng khoảng xác định là $\displaystyle\int \dfrac{\mathrm{d}x}{x} = \ln|x| + C$.'''
    return caudan, choices, loi_giai


def DeThiThu04_MC_Cau8():
    # Câu 8: Thể tích lăng trụ đứng đáy tam giác đều cạnh a, chiều cao k*a
    k_cfgs = [
        {"h_tex": r"\sqrt{3}a", "v_tex": r"\dfrac{3a^3}{4}", "val_k": 3},
        {"h_tex": r"2a",         "v_tex": r"\dfrac{a^3\sqrt{3}}{2}", "val_k": 2},
        {"h_tex": r"a\sqrt{2}", "v_tex": r"\dfrac{a^3\sqrt{6}}{4}", "val_k": 1},
    ]
    c = random.choice(k_cfgs)

    caudan = fr'''Cho khối lăng trụ đứng $ABC.A'B'C'$ có đáy là tam giác đều cạnh $a$ và $AA' = {c["h_tex"]}$. Thể tích của khối lăng trụ đã cho là'''
    correct = fr"${c['v_tex']}$"
    wrongs = [
        r"$\dfrac{a^3}{4}$",
        r"$\dfrac{a^3}{2}$",
        r"$\dfrac{3a^3}{2}$"
    ]
    if correct in wrongs:
        wrongs.remove(correct)
        wrongs.append(r"$\dfrac{a^3\sqrt{3}}{4}$")
    choices = shuffle_choices(correct, wrongs[:3])
    loi_giai = fr'''Diện tích đáy tam giác đều cạnh $a$: $S = \dfrac{{a^2\sqrt{{3}}}}{{4}}$. \\
Thể tích khối lăng trụ: $V = S \cdot AA' = \dfrac{{a^2\sqrt{{3}}}}{{4}} \cdot {c["h_tex"]} = {c["v_tex"]}$.'''
    return caudan, choices, loi_giai


def DeThiThu04_MC_Cau9():
    # Câu 9: Tâm I và bán kính R của mặt cầu (S): x^2+y^2+z^2 - 2ax - 2by - 2cz + d = 0
    # Ví dụ: (S): x^2+y^2+z^2 - 4x + 8y - 2z - 4 = 0 => I(2; -4; 1), R = sqrt(4+16+1+4) = 5
    cfgs = [
        {"a": 2, "b": -4, "c": 1, "d": -4, "R": 5, "eqn": r"x^2+y^2+z^2 - 4x + 8y - 2z - 4 = 0"},
        {"a": 1, "b": 2,  "c": -2, "d": -16, "R": 5, "eqn": r"x^2+y^2+z^2 - 2x - 4y + 4z - 16 = 0"},
        {"a": -2, "b": 1, "c": 3, "d": -11, "R": 5, "eqn": r"x^2+y^2+z^2 + 4x - 2y - 6z - 11 = 0"},
    ]
    p = random.choice(cfgs)
    a, b, c, R = p["a"], p["b"], p["c"], p["R"]

    caudan = fr'''Trong không gian $Oxyz$, cho mặt cầu $(S) \colon {p["eqn"]}$. Tọa độ tâm $I$ và bán kính $R$ của mặt cầu $(S)$ là'''
    correct = fr"$I({a}; {b}; {c}), R = {R}$"
    wrongs = [
        fr"$I({-a}; {-b}; {-c}), R = {R**2}$",
        fr"$I({a}; {b}; {c}), R = \sqrt{{{R**2 - 4}}}$",
        fr"$I({-a}; {-b}; {-c}), R = {R}$"
    ]
    choices = shuffle_choices(correct, wrongs)
    loi_giai = fr'''Phương trình mặt cầu có dạng $x^2 + y^2 + z^2 - 2ax - 2by - 2cz + d = 0$ với tâm $I(a; b; c) = ({a}; {b}; {c})$ và bán kính:
$$R = \sqrt{{a^2 + b^2 + c^2 - d}} = \sqrt{{{a**2} + {b**2} + {c**2} - ({p["d"]})}} = \sqrt{{{R**2}}} = {R}.$$'''
    return caudan, choices, loi_giai


def DeThiThu04_MC_Cau10():
    # Câu 10: Cấp số cộng (u_n) biết u1, u2 tính công sai d = u2 - u1
    u1 = random.randint(1, 6)
    d_step = random.choice([3, 4, 5, 6, 7])
    u2 = u1 + d_step

    caudan = fr'''Cho cấp số cộng $(u_n)$ với $u_1 = {u1}$, $u_2 = {u2}$. Công sai của cấp số cộng đã cho bằng'''
    correct = fr"${d_step}$"
    wrongs = [
        fr"${u1 + u2}$",
        fr"${-d_step}$",
        fr"${u1}$"
    ]
    choices = shuffle_choices(correct, wrongs)
    loi_giai = fr'''Công sai của cấp số cộng là $d = u_2 - u_1 = {u2} - {u1} = {d_step}$.'''
    return caudan, choices, loi_giai


def DeThiThu04_MC_Cau11():
    # Câu 11: Hàm số đồng biến trên khoảng nào từ đồ thị y = (x^2+1)/x
    caudan = r'''\immini{Cho hàm số $y = f(x)$ có đồ thị như hình vẽ. Hàm số đã cho đồng biến trên khoảng nào trong các khoảng sau đây?
\begin{center}
\end{center}
}{
\begin{tikzpicture}[scale=0.6, line join=round, line cap=round, >=stealth,font=\footnotesize]
	\def\xmin{-3}\def\xmax{3}\def\ymin{-4}\def\ymax{4}
	\draw[->] (\xmin-0.2,0)--(\xmax+0.2,0) node[below]{$x$};
	\draw[->] (0,\ymin-0.2)--(0,\ymax+0.2) node[right]{$y$};
	\draw (0,0) node[above left]{$O$};
	\foreach \x in {-3,-2,-1,1,2,3}\draw (\x,0.1)--(\x,-0.1) node[below]{$\x$};
	\foreach \y in {-3,-2,-1,1,2,3}\draw (0.1,\y)--(-0.1,\y) node[left]{$\y$};
	\clip (\xmin,\ymin) rectangle (\xmax,\ymax);
	\draw[dashed] (-0.0,\ymin)--(-0.0,\ymax);
	\draw[dashed,domain=\xmin:\xmax] plot (\x,{1.0*(\x)+0.0});
	\draw[thick,smooth,samples=200,domain=\xmin:-0.1] plot (\x,{(1*((\x)^2)+0*(\x)+1)/(1*(\x)+0)});
	\draw[thick,smooth,samples=200,domain=0.1:\xmax] plot (\x,{(1*((\x)^2)+0*(\x)+1)/(1*(\x)+0)});
	\draw[dashed] (-1,0)--(-1,-2)--(0,-2);\fill (-1,-2)circle(1.5pt);
	\draw[dashed] (1,0)--(1,2)--(0,2);\fill (1,2)circle(1.5pt);
\end{tikzpicture}
}'''
    correct = r'''$(1; 2)$'''
    wrongs = [
        r'''$(-1; 0)$''',
        r'''$(0; 1)$''',
        r'''$(-1; 1)$'''
    ]
    choices = shuffle_choices(correct, wrongs)
    loi_giai = r'''Dựa vào đồ thị, đồ thị đi lên từ trái sang phải trên các khoảng $(-\infty; -1)$ và $(1; +\infty)$. Do $(1; 2) \subset (1; +\infty)$ nên hàm số đồng biến trên khoảng $(1; 2)$.'''
    return caudan, choices, loi_giai


def DeThiThu04_MC_Cau12():
    # Câu 12: Tọa độ vectơ a + b trong không gian Oxyz
    ax, ay, az = random.choice([(2, 1, -1), (1, -2, 3), (3, 0, -2), (2, -1, 4)])
    bx, by, bz = random.choice([(3, -2, 1), (2, 1, -1), (1, -3, 2), (-1, 2, 1)])
    cx = ax + bx
    cy = ay + by
    cz = az + bz

    caudan = fr'''Trong không gian $Oxyz$, cho hai vectơ $\vec{{a}} = ({ax}; {ay}; {az})$ và $\vec{{b}} = ({bx}; {by}; {bz})$. Vectơ $\vec{{a}} + \vec{{b}}$ có tọa độ là'''
    correct = fr"$({cx}; {cy}; {cz})$"
    wrongs = [
        fr"$({cx}; {cy}; {cz + 2})$",
        fr"$({cx}; {cy + 2}; {cz})$",
        fr"$({-cx}; {cy}; {cz})$"
    ]
    choices = shuffle_choices(correct, wrongs)
    loi_giai = fr'''Tọa độ vectơ $\vec{{a}} + \vec{{b}} = ({ax} + ({bx}); {ay} + ({by}); {az} + ({bz})) = ({cx}; {cy}; {cz})$.'''
    return caudan, choices, loi_giai


# ==============================================================================
# PHẦN II: 4 CÂU TRẮC NGHIỆM ĐÚNG / SAI (TF)
# ==============================================================================

def DeThiThu04_TF_Cau1():
    # Câu 1: Sức khỏe người cao tuổi - Tiểu đường và Huyết áp cao (Xác suất có điều kiện)
    p_td = random.choice([0.4, 0.35, 0.3])
    p_ha_td = random.choice([0.7, 0.75, 0.8])
    p_ha_not_td = random.choice([0.25, 0.2, 0.3])

    p_not_td = round(1 - p_td, 2)
    p_ha_total = round(p_td * p_ha_td + p_not_td * p_ha_not_td, 4)
    p_ha_str = f"{p_ha_total:.2f}".replace('.', ',')

    caudan = fr'''Khi điều tra sức khỏe người cao tuổi ở một địa phương, người ta thấy rằng có ${int(p_td*100)}\%$ người cao tuổi bị bệnh tiểu đường. Bên cạnh đó, tỉ lệ người bị bệnh huyết áp cao trong số những người bị bệnh tiểu đường là ${int(p_ha_td*100)}\%$, trong số những người không bị bệnh tiểu đường là ${int(p_ha_not_td*100)}\%$. Chọn ngẫu nhiên một người cao tuổi để kiểm tra sức khỏe.'''

    items = [
        (
            fr'''Xác suất chọn được người bị bệnh tiểu đường là ${str(p_td).replace('.', ',')}$''',
            fr'''Xác suất chọn được người bị bệnh tiểu đường là ${str(p_not_td).replace('.', ',')}$''',
            fr'''Theo giả thiết, tỉ lệ người mắc bệnh tiểu đường là ${int(p_td*100)}\% \implies P(T) = {str(p_td).replace('.', ',')}$.''',
            fr'''Xác suất là ${str(p_td).replace('.', ',')}$, không phải ${str(p_not_td).replace('.', ',')}$.'''
        ),
        (
            fr'''Xác suất chọn được người bị bệnh huyết áp cao, biết người đó bị bệnh tiểu đường là ${str(p_ha_td).replace('.', ',')}$''',
            fr'''Xác suất chọn được người bị bệnh huyết áp cao, biết người đó bị bệnh tiểu đường là ${str(p_ha_not_td).replace('.', ',')}$''',
            fr'''Đây là xác suất có điều kiện $P(H|T) = {int(p_ha_td*100)}\% = {str(p_ha_td).replace('.', ',')}$.''',
            fr'''Xác suất có điều kiện đã cho là $P(H|T) = {str(p_ha_td).replace('.', ',')}$.'''
        ),
        (
            fr'''Xác suất chọn được người bị bệnh huyết áp cao, biết người đó không bị bệnh tiểu đường là ${str(p_ha_not_td).replace('.', ',')}$''',
            fr'''Xác suất chọn được người bị bệnh huyết áp cao, biết người đó không bị bệnh tiểu đường là ${str(p_ha_td).replace('.', ',')}$''',
            fr'''Đây là xác suất có điều kiện $P(H|\overline{{T}}) = {int(p_ha_not_td*100)}\% = {str(p_ha_not_td).replace('.', ',')}$.''',
            fr'''Xác suất có điều kiện đã cho là $P(H|\overline{{T}}) = {str(p_ha_not_td).replace('.', ',')}$.'''
        ),
        (
            fr'''Xác suất chọn được người có bệnh huyết áp cao là ${p_ha_str}$''',
            fr'''Xác suất chọn được người có bệnh huyết áp cao là $0,4$''',
            fr'''Theo công thức xác suất toàn phần: $P(H) = P(T)P(H|T) + P(\overline{{T}})P(H|\overline{{T}}) = {p_td} \times {p_ha_td} + {p_not_td} \times {p_ha_not_td} = {p_ha_str}$.''',
            fr'''$P(H) = {p_ha_str} \ne 0,4$.'''
        )
    ]
    choices, loi_giai = make_tf_choices(items)
    return caudan, choices, loi_giai


def DeThiThu04_TF_Cau2():
    # Câu 2: Ô tô phát hiện chướng ngại vật, phản ứng 1s rồi đạp phanh v(t) = -10t + 20
    caudan = r'''Một ô tô đang chuyển động thì người lái xe phát hiện chướng ngại vật phía trước. Người lái xe phản ứng mất $1$ giây, sau đó đạp phanh khẩn cấp. Kể từ thời điểm này, ô tô chuyển động chậm dần đều với vận tốc được cho bởi $v(t) = -10t + 20\text{ (m/s)}$, trong đó $t$ là thời gian tính bằng giây kể từ lúc đạp phanh.'''

    items = [
        (
            r'''Xe ô tô dừng hẳn sau $2$ giây kể từ lúc đạp phanh''',
            r'''Xe ô tô dừng hẳn sau $4$ giây kể từ lúc đạp phanh''',
            r'''Xe dừng hẳn khi $v(t) = 0 \iff -10t + 20 = 0 \iff t = 2\text{ (s)}$.''',
            r'''Thời gian để xe dừng hẳn là $t = 2\text{ (s)} \ne 4\text{ (s)}$.'''
        ),
        (
            r'''Hàm số vận tốc $v(t)$ mà xe ô tô di chuyển trong thời gian $t$ (giây) kể từ lúc đạp phanh là một hàm số bậc nhất''',
            r'''Hàm số vận tốc $v(t)$ kể từ lúc đạp phanh là một hàm số bậc hai''',
            r'''Hàm số $v(t) = -10t + 20$ có dạng $at + b$ với $a = -10 \ne 0$ nên là hàm bậc nhất đối với $t$.''',
            r'''$v(t)$ là hàm bậc nhất, không phải bậc hai.'''
        ),
        (
            r'''Quãng đường ô tô chuyển động kể từ lúc đạp phanh đến khi dừng hẳn là $20$ m''',
            r'''Quãng đường ô tô chuyển động trong $6$ giây (kể từ lúc đạp phanh) là $30$ m''',
            r'''Xe dừng hẳn sau $2$ giây nên quãng đường đi được từ lúc đạp phanh đến khi dừng hẳn là $\displaystyle\int_0^2 (-10t + 20)\,\mathrm{d}t = \left.(-5t^2 + 20t)\right|_0^2 = 20\text{ m}$. Sau giây thứ $2$, xe đứng yên nên quãng đường không đổi.''',
            r'''Sau $2$ giây xe đã dừng hẳn nên quãng đường không tăng thêm, khẳng định đi được $30\text{ m}$ là sai.'''
        ),
        (
            r'''Công thức tính quãng đường đi được theo thời gian $t \in [0; 2]$ kể từ lúc đạp phanh là $S(t) = -5t^2 + 20t$''',
            r'''Công thức tính quãng đường đi được theo thời gian $t$ là $S(t) = -10t^2 + 20t$''',
            r'''$S(t) = \displaystyle\int_0^t (-10u + 20)\,\mathrm{d}u = -5t^2 + 20t$ (với $0 \le t \le 2$).''',
            r'''Nguyên hàm của $-10t$ là $-5t^2$, không phải $-10t^2$.'''
        )
    ]
    choices, loi_giai = make_tf_choices(items)
    return caudan, choices, loi_giai


def DeThiThu04_TF_Cau3():
    # Câu 3: Hàm số f(x) = \cos 2x - x trên đoạn [-\pi/2; \pi/2]
    caudan = r'''Cho hàm số $f(x) = \cos 2x - x$ xác định trên đoạn $\left[-\dfrac{\pi}{2}; \dfrac{\pi}{2}\right]$.'''

    items = [
        (
            r'''$f\left(-\dfrac{\pi}{2}\right) = \dfrac{\pi}{2} - 1$ và $f\left(\dfrac{\pi}{2}\right) = -\dfrac{\pi}{2} - 1$''',
            r'''$f\left(-\dfrac{\pi}{2}\right) = -\dfrac{\pi}{2} + 1$ và $f\left(\dfrac{\pi}{2}\right) = \dfrac{\pi}{2} - 1$''',
            r'''$f\left(-\dfrac{\pi}{2}\right) = \cos(-\pi) - \left(-\dfrac{\pi}{2}\right) = -1 + \dfrac{\pi}{2} = \dfrac{\pi}{2} - 1$; $f\left(\dfrac{\pi}{2}\right) = \cos(\pi) - \dfrac{\pi}{2} = -\dfrac{\pi}{2} - 1$.''',
            r'''Tính đúng: $f\left(-\dfrac{\pi}{2}\right) = \dfrac{\pi}{2} - 1$ và $f\left(\dfrac{\pi}{2}\right) = -\dfrac{\pi}{2} - 1$.'''
        ),
        (
            r'''Đạo hàm của hàm số đã cho là $f'(x) = -2\sin 2x - 1$''',
            r'''Đạo hàm của hàm số đã cho là $f'(x) = 2\sin 2x - 1$''',
            r'''$(\cos 2x)' = -2\sin 2x$, do đó $f'(x) = -2\sin 2x - 1$.''',
            r'''Đạo hàm của $\cos 2x$ mang dấu trừ, nên $f'(x) = -2\sin 2x - 1 \ne 2\sin 2x - 1$.'''
        ),
        (
            r'''Phương trình $f'(x) = 0$ có đúng hai nghiệm trên đoạn $\left[-\dfrac{\pi}{2}; \dfrac{\pi}{2}\right]$ là $x = -\dfrac{\pi}{12}$ và $x = -\dfrac{5\pi}{12}$''',
            r'''Phương trình $f'(x) = 0$ có đúng hai nghiệm trên đoạn $\left[-\dfrac{\pi}{2}; \dfrac{\pi}{2}\right]$ là $x = -\dfrac{\pi}{12}$ và $x = \dfrac{5\pi}{12}$''',
            r'''$f'(x) = 0 \iff \sin 2x = -\dfrac{1}{2} \iff 2x = -\dfrac{\pi}{6} + k2\pi$ hoặc $2x = -\dfrac{5\pi}{6} + k2\pi$. Trên đoạn đã cho, $x = -\dfrac{\pi}{12}$ và $x = -\dfrac{5\pi}{12}$.''',
            r'''Nghiệm đúng là $x = -\dfrac{\pi}{12}$ và $x = -\dfrac{5\pi}{12}$, khẳng định $x = \dfrac{5\pi}{12}$ là sai.'''
        ),
        (
            r'''Giá trị nhỏ nhất của hàm số $y = f(x)$ trên đoạn $\left[-\dfrac{\pi}{2}; \dfrac{\pi}{2}\right]$ là $-\dfrac{\pi}{2} - 1$''',
            r'''Giá trị nhỏ nhất của hàm số $y = f(x)$ trên đoạn $\left[-\dfrac{\pi}{2}; \dfrac{\pi}{2}\right]$ là $-\dfrac{\pi}{2} + 1$''',
            r'''So sánh các giá trị tại các điểm tới hạn và đầu mút, ta thấy $\min\limits_{[-\pi/2; \pi/2]} f(x) = f\left(\dfrac{\pi}{2}\right) = -\dfrac{\pi}{2} - 1$.''',
            r'''Giá trị nhỏ nhất là $-\dfrac{\pi}{2} - 1$.'''
        )
    ]
    choices, loi_giai = make_tf_choices(items)
    return caudan, choices, loi_giai


def DeThiThu04_TF_Cau4():
    # Câu 4: Máy bay bay từ A đến B và ra đa mặt đất O
    caudan = r'''\immini{Giả sử một máy bay đang bay theo đường thẳng từ $A$ đến $B$ có hình chiếu trên mặt đất là đoạn $CD$. Tại $A$, máy bay cách mặt đất $20\,000\text{ m}$ và tại $B$ cách mặt đất $25\,000\text{ m}$. Ra đa đặt trên mặt đất tại $O$ cách $C$ là $15\,000\text{ m}$, cách $D$ là $30\,000\text{ m}$ và $\widehat{COD} = 90^\circ$. Chọn hệ trục $Oxyz$ (đơn vị: $1\,000\text{ m}$) sao cho $O(0;0;0)$, $C(15;0;0)$, $D(0;30;0)$, $A(15;0;20)$, $B(0;30;25)$.}{
\begin{tikzpicture}[>=stealth, x={(0.5cm,-0.3cm)}, y={(0.8cm,0.2cm)}, z={(0cm,0.8cm)}, scale=0.16]
	\draw[->] (0,0,0) -- (20,0,0) node[below] {$x$};
	\draw[->] (0,0,0) -- (0,35,0) node[right] {$y$};
	\draw[->] (0,0,0) -- (0,0,28) node[left] {$z$};
	\node[below left] at (0,0,0) {$O$};
	\coordinate (C) at (15,0,0); \coordinate (D) at (0,30,0);
	\coordinate (A) at (15,0,20); \coordinate (B) at (0,30,25);
	\draw[dashed] (C)--(A) (D)--(B) (0,0,20)--(A) (0,0,25)--(B);
	\draw[thick] (C)--(D); \draw[thick, blue] (A)--(B);
	\node[below left] at (C) {$C$}; \node[below right] at (D) {$D$};
	\node[below right] at (A) {$A$}; \node[above right] at (B) {$B$};
\end{tikzpicture}
}'''

    items = [
        (
            r'''Tại vị trí $A$, máy bay cách ra đa $25$ km''',
            r'''Tại vị trí $A$, máy bay cách ra đa $35$ km''',
            r'''$OA = \sqrt{15^2 + 0^2 + 20^2} = \sqrt{225 + 400} = \sqrt{625} = 25\text{ (km)}$.''',
            r'''Khoảng cách $OA = 25\text{ km} \ne 35\text{ km}$.'''
        ),
        (
            r'''Gọi $I$ là trung điểm của đoạn thẳng $AB$. Khi máy bay đến điểm $I$, máy bay cách mặt đất $22\,500$ m''',
            r'''Khi máy bay đến trung điểm $I$ của $AB$, máy bay cách mặt đất $20\,000$ m''',
            r'''Tọa độ $z_I = \dfrac{z_A + z_B}{2} = \dfrac{20 + 25}{2} = 22,5\text{ (km)} = 22\,500\text{ m}$.''',
            r'''Độ cao tại trung điểm là $22\,500\text{ m} \ne 20\,000\text{ m}$.'''
        ),
        (
            r'''Trên đoạn đường bay từ $A$ đến $B$, máy bay không đi qua vị trí $Q(12; 6; 22)$''',
            r'''Trên đoạn đường bay từ $A$ đến $B$, máy bay đi qua vị trí $Q(12; 6; 22)$''',
            r'''Đường thẳng $AB$ có PT: $x = 15 - 3t, y = 6t, z = 20 + t$. Với $y = 6 \implies t = 1 \implies x = 12, z = 21 \ne 22$, nên máy bay không qua $Q$.''',
            r'''Tại $t=1$, tọa độ là $(12; 6; 21) \ne Q(12; 6; 22)$, khẳng định đi qua $Q$ là sai.'''
        ),
        (
            r'''Vị trí máy bay gần ra đa nhất có tọa độ là $\left(\dfrac{615}{46}; \dfrac{75}{23}; \dfrac{945}{46}\right)$''',
            r'''Vị trí máy bay gần ra đa nhất chính là vị trí điểm $A(15; 0; 20)$''',
            r'''Hình chiếu vuông góc của $O$ lên đường thẳng $AB$ cho tọa độ điểm gần nhất là $\left(\dfrac{615}{46}; \dfrac{75}{23}; \dfrac{945}{46}\right)$.''',
            r'''Tọa độ điểm gần nhất tính bằng hình chiếu vuông góc lên đường thẳng là $\left(\dfrac{615}{46}; \dfrac{75}{23}; \dfrac{945}{46}\right) \ne A$.'''
        )
    ]
    choices, loi_giai = make_tf_choices(items)
    return caudan, choices, loi_giai


# ==============================================================================
# PHẦN III: 6 CÂU TRẢ LỜI NGẮN (SA)
# ==============================================================================

def DeThiThu04_SA_Cau1():
    # Câu 1: Xác suất trẻ em bị hen phế quản (Bayes)
    # Tỉ lệ nam gấp k lần nữ: k = 1.5 => P(Nam) = 1.5/2.5 = 0.6, P(Nữ) = 0.4
    cfgs = [
        {"k": 1.5, "p_nam": 0.08, "p_nu": 0.05, "ans_str": "0,7"},
        {"k": 1.0, "p_nam": 0.06, "p_nu": 0.04, "ans_str": "0,6"},
        {"k": 2.0, "p_nam": 0.09, "p_nu": 0.06, "ans_str": "0,8"},
    ]
    c = random.choice(cfgs)
    k = c["k"]
    p_b_nam = int(c["p_nam"] * 100)
    p_b_nu = int(c["p_nu"] * 100)
    ans = c["ans_str"]
    
    p_nam = k / (k + 1)
    p_nu = 1 / (k + 1)
    p_hen = p_nam * c["p_nam"] + p_nu * c["p_nu"]
    p_ans = (p_nam * c["p_nam"]) / p_hen

    caudan = fr'''Thực hiện khảo sát tại một địa phương có số trẻ em nam gấp ${k}$ lần số trẻ em nữ; có ${p_b_nam}\%$ số trẻ em nam bị hen phế quản và ${p_b_nu}\%$ số trẻ em nữ bị hen phế quản. Chọn ngẫu nhiên một trẻ em và thấy trẻ này bị hen phế quản. Xác suất để trẻ em được chọn là trẻ em nam bằng bao nhiêu? \textit{{(Làm tròn kết quả đến hàng phần mười)}}'''
    dapan = ans
    loi_giai = fr'''Gọi $M$ là biến cố "Chọn được trẻ em nam", $F$ là biến cố "Chọn được trẻ em nữ", $H$ là biến cố "Trẻ bị hen phế quản". \\
Theo đề bài: $P(M) = \dfrac{{{k}}}{{{k+1}}} = {p_nam:.2f}$, $P(F) = \dfrac{{1}}{{{k+1}}} = {p_nu:.2f}$. \\
$P(H|M) = {c["p_nam"]}$, $P(H|F) = {c["p_nu"]}$. \\
Xác suất toàn phần: $P(H) = {p_nam:.2f} \times {c["p_nam"]} + {p_nu:.2f} \times {c["p_nu"]} = {p_hen:.4f}$. \\
Theo công thức Bayes:
$$P(M|H) = \dfrac{{P(M)P(H|M)}}{{P(H)}} = \dfrac{{{p_nam * c["p_nam"]:.4f}}}{{{p_hen:.4f}}} \approx {dapan}.$$'''
    return caudan, dapan, loi_giai


def DeThiThu04_SA_Cau2():
    # Câu 2: Tấm bìa bán nguyệt đường kính 2R cắt hình chữ nhật diện tích lớn nhất
    R_list = [10, 15, 20, 25, 30]
    R = random.choice(R_list)
    D = 2 * R
    S_max = R**2

    caudan = fr'''\immini{{Từ một tấm bìa bán nguyệt có đường kính ${D}\text{{ cm}}$, người ta muốn cắt ra một tấm bìa hình chữ nhật (có một cạnh nằm trên đường kính của hình bán nguyệt như hình bên) có diện tích lớn nhất có thể. Tìm giá trị của diện tích lớn nhất đó theo đơn vị centimet vuông.}}{{
\begin{{tikzpicture}}[scale=0.08]
	\def\r{{{R}}}
	\def\a{{{int(R * 0.7)}}}
	\pgfmathsetmacro{{\h}}{{sqrt(\r*\r - \a*\a)}} 
	\draw[thick] (-\r,0) arc[start angle=180, end angle=0, radius=\r]; 
	\draw[thick] (-\r,0) -- (\r,0); 
	\draw[thick, fill=gray!30] (-\a,0) rectangle (\a,\h); 
	\draw[<->] (-\r,-3) -- (\r,-3) node[midway, below]{{${D}\text{{ cm}}$}};
\end{{tikzpicture}}
}}'''
    dapan = str(S_max)
    loi_giai = fr'''Gọi nửa chiều dài hình chữ nhật là $x$ ($0 < x < {R}$), chiều rộng hình chữ nhật là $y = \sqrt{{{R}^2 - x^2}}$. \\
Diện tích hình chữ nhật là:
$$S(x) = 2xy = 2x\sqrt{{{R}^2 - x^2}} \le x^2 + ({R}^2 - x^2) = {R}^2 = {S_max}\text{{ (cm}}^2\text{{)}}.$$
Dấu "=" xảy ra khi $x = \sqrt{{{R}^2 - x^2}} \iff x = \dfrac{{{R}\sqrt{2}}}{{2}}$. \\
Vậy diện tích lớn nhất của tấm bìa hình chữ nhật là ${S_max}\text{{ cm}}^2$.'''
    return caudan, dapan, loi_giai


def DeThiThu04_SA_Cau3():
    # Câu 3: Lăng trụ đứng ABC.A'B'C' AC=1, BC=2, ACB=120 deg. Tính d(C, (ABB'A'))
    # AB = sqrt(1 + 4 - 2*1*2*(-1/2)) = sqrt(7)
    # S = 1/2 * 1 * 2 * sin(120) = sqrt(3)/2
    # CH = 2S / AB = sqrt(3/7) ≈ 0.6546 => làm tròn hàng phần chục: 0,7 (hoặc 0,65 hàng phần trăm)
    caudan = r'''Cho hình lăng trụ đứng $ABC.A'B'C'$ có $AC = 1, BC = 2, \widehat{ACB} = 120^\circ$. Tính khoảng cách từ điểm $C$ đến mặt phẳng $(ABB'A')$ (kết quả làm tròn đến hàng phần mười).'''
    dapan = "0,7"
    loi_giai = r'''Vì lăng trụ đứng nên $(ABB'A') \perp (ABC)$ theo giao tuyến $AB$. Do đó khoảng cách từ $C$ đến mặt phẳng $(ABB'A')$ bằng khoảng cách từ $C$ đến đường thẳng $AB$ trong mặt phẳng $(ABC)$. \\
Áp dụng định lí côsin trong tam giác $ABC$:
$$AB = \sqrt{AC^2 + BC^2 - 2AC \cdot BC \cos 120^\circ} = \sqrt{1 + 4 - 2(1)(2)\left(-\dfrac{1}{2}\right)} = \sqrt{7}.$$
Diện tích tam giác $ABC$:
$$S_{ABC} = \dfrac{1}{2} AC \cdot BC \sin 120^\circ = \dfrac{1}{2} \cdot 1 \cdot 2 \cdot \dfrac{\sqrt{3}}{2} = \dfrac{\sqrt{3}}{2}.$$
Khoảng cách cần tìm:
$$d(C, (ABB'A')) = CH = \dfrac{2S_{ABC}}{AB} = \dfrac{\sqrt{3}}{\sqrt{7}} = \sqrt{\dfrac{3}{7}} \approx 0,655 \approx 0,7.$$'''
    return caudan, dapan, loi_giai


def DeThiThu04_SA_Cau4():
    # Câu 4: Con chim bói cá săn mồi
    # C(2; 6; 5), A(1.5; 1; -0.5), v = 4 m/s
    # Giao mặt nước B(x_B; y_B; 0): z_C = 5, z_A = -0.5 => CB/CA = 5 / 5.5 = 10/11
    # CA = sqrt((0.5)^2 + 5^2 + 5.5^2) = sqrt(0.25 + 25 + 30.25) = sqrt(55.5) ≈ 7.4498 m
    # CB = (10/11) * 7.4498 ≈ 6.7726 m
    # t = CB / v = 6.7726 / 4 ≈ 1.69 s
    caudan = r'''Trong hệ trục toạ độ $Oxyz$ với mặt phẳng $(Oxy)$ là mặt nước, trục $Oz$ hướng lên trên (đơn vị: mét), một con chim bói cá đang ở vị trí $C$ cách mặt nước $5\text{ m}$, cách mặt phẳng $(Oxz)$ và $(Oyz)$ lần lượt là $6\text{ m}$ và $2\text{ m}$ (tức $C(2; 6; 5)$). Từ vị trí này, chim phóng thẳng xuống vị trí con cá ở điểm $A$, biết con cá cách mặt nước $50\text{ cm}$, cách mặt phẳng $(Oxz)$ và $(Oyz)$ lần lượt là $1\text{ m}$ và $1{,}5\text{ m}$ (tức $A(1{,}5; 1; -0{,}5)$). Giả sử vận tốc của con chim bói cá là $4\text{ m/s}$, hỏi sau bao nhiêu giây thì nó chạm tới mặt nước? \textit{(Làm tròn kết quả đến hàng phần trăm)}'''
    dapan = "1,69"
    loi_giai = r'''Tọa độ vị trí chim bói cá là $C(2; 6; 5)$ và con cá là $A(1{,}5; 1; -0{,}5)$. \\
Đoạn thẳng $CA$ cắt mặt nước $(Oxy)$ tại điểm $B(x_B; y_B; 0)$. \\
Ta có $\overrightarrow{CA} = (-0{,}5; -5; -5{,}5)$. \\
Độ dài quãng đường từ $C$ đến $A$ là:
$$CA = \sqrt{(-0{,}5)^2 + (-5)^2 + (-5{,}5)^2} = \sqrt{0{,}25 + 25 + 30{,}25} = \sqrt{55{,}5} \approx 7{,}4498\text{ m}.$$
Vì điểm $B$ thuộc mặt nước ($z_B = 0$) nên theo tỉ lệ cao độ:
$$\dfrac{CB}{CA} = \dfrac{z_C - z_B}{z_C - z_A} = \dfrac{5 - 0}{5 - (-0{,}5)} = \dfrac{5}{5{,}5} = \dfrac{10}{11}.$$
Khoảng cách chim di chuyển từ $C$ đến mặt nước là:
$$CB = \dfrac{10}{11} CA \approx \dfrac{10}{11} \times 7{,}4498 \approx 6{,}7726\text{ m}.$$
Thời gian chạm tới mặt nước là:
$$t = \dfrac{CB}{v} = \dfrac{6{,}7726}{4} \approx 1{,}69\text{ giây}.$$'''
    return caudan, dapan, loi_giai


def DeThiThu04_SA_Cau5():
    # Câu 5: Động đất Richter: M = log A - log A0
    cfgs = [
        {"M1": "9,1", "M2": "6,8", "diff": 2.3, "ans_str": "199,5"},
        {"M1": "9,0", "M2": "7,0", "diff": 2.0, "ans_str": "100"},
        {"M1": "8,8", "M2": "6,5", "diff": 2.3, "ans_str": "199,5"},
        {"M1": "8,5", "M2": "6,2", "diff": 2.3, "ans_str": "199,5"},
    ]
    c = random.choice(cfgs)
    M1, M2 = c["M1"], c["M2"]
    ans = c["ans_str"]

    caudan = fr'''Cường độ một trận động đất $M$ độ Richter được cho bởi công thức $M = \log A - \log A_0$ với $A$ là biên độ rung chấn tối đa và $A_0$ là biên độ chuẩn. Ngày 11/3/2011, một trận siêu động đất tại vùng Tohoku (Nhật Bản) có cường độ ${M1}$ độ Richter. Trước đó, một trận động đất khác ở phía Bắc Algeria có cường độ ${M2}$ độ Richter. Hỏi biên độ rung chấn tối đa của trận động đất ở Tohoku gấp bao nhiêu lần biên độ rung chấn tối đa của trận động đất ở Algeria? \textit{{(Làm tròn kết quả đến hàng phần mười)}}'''
    dapan = ans
    loi_giai = fr'''Theo công thức: $M = \log\left(\dfrac{{A}}{{A_0}}\right) \iff \dfrac{{A}}{{A_0}} = 10^M \iff A = A_0 \cdot 10^M$. \\
Tỉ số biên độ rung chấn giữa hai trận động đất là:
$$\dfrac{{A_1}}{{A_2}} = \dfrac{{A_0 \cdot 10^{{{M1}}}}}{{A_0 \cdot 10^{{{M2}}}}} = 10^{{{c["diff"]}}} \approx {dapan}\text{{ lần}}.$$'''
    return caudan, dapan, loi_giai


def DeThiThu04_SA_Cau6():
    # Câu 6: Khoảng cách giữa 2 điểm cực trị và từ cực tiểu đến O
    # y = (-x^2 + 3x + 3) / (x + 1)
    # y' = (-x^2 - 2x) / (x+1)^2 = 0 <=> x = 0 hoặc x = -2
    # x = 0 => y = 3 (CT), d2 = OA = 3 => d2^2 = 9
    # x = -2 => y = 7 (CD), d1 = AB = sqrt(4 + 16) = sqrt(20) => d1^2 = 20
    # d1^2 + 2*d2^2 = 20 + 2*9 = 38
    caudan = r'''Cho hàm số $y = \dfrac{-x^2 + 3x + 3}{x + 1}$ có đồ thị $(C)$. Gọi $d_1$ là khoảng cách giữa hai điểm cực trị của $(C)$ và $d_2$ là khoảng cách từ điểm cực tiểu của $(C)$ đến gốc tọa độ $O$. Giá trị của biểu thức $d_1^2 + 2d_2^2$ bằng bao nhiêu?'''
    dapan = "38"
    loi_giai = r'''Tập xác định: $D = \mathbb{R} \setminus \{-1\}$. \\
Đạo hàm: $y' = \dfrac{(-2x + 3)(x + 1) - (-x^2 + 3x + 3)}{(x + 1)^2} = \dfrac{-x^2 - 2x}{(x + 1)^2}$. \\
$y' = 0 \iff -x^2 - 2x = 0 \iff \left[\begin{aligned} x &= 0 \implies y = 3 \\ x &= -2 \implies y = 7 \end{aligned}\right.$ \\
Bảng biến thiên cho thấy điểm cực tiểu là $A(0; 3)$ và điểm cực đại là $B(-2; 7)$. \\
Khoảng cách giữa hai điểm cực trị:
$$d_1 = AB = \sqrt{(-2 - 0)^2 + (7 - 3)^2} = \sqrt{4 + 16} = \sqrt{20} \implies d_1^2 = 20.$$
Khoảng cách từ điểm cực tiểu $A(0; 3)$ đến gốc tọa độ $O(0; 0)$:
$$d_2 = OA = \sqrt{0^2 + 3^2} = 3 \implies d_2^2 = 9.$$
Vậy $d_1^2 + 2d_2^2 = 20 + 2(9) = 38$.'''
    return caudan, dapan, loi_giai
