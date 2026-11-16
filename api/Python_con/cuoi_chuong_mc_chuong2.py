# -*- coding: utf-8 -*-
"""
Module sinh đề trắc nghiệm chuẩn ma trận Bài tập Cuối Chương 2 (Toán 12)
Gồm 3 bài x 4 câu = 12 câu chuẩn:
- Bài 1: Vectơ trong không gian (2 NB, 1 TH, 1 VD)
- Bài 2: Toạ độ của điểm và vectơ trong không gian (2 NB, 1 TH, 1 VD)
- Bài 3: Biểu thức toạ độ của các phép toán vectơ (2 NB, 1 TH, 1 VD)
Tất cả đều sinh ngẫu nhiên số đẹp, tự động tính toán đáp án và lời giải chi tiết.
"""

import random
import math


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


# ==============================================================================
# BÀI 1: VECTƠ TRONG KHÔNG GIAN
# ==============================================================================

def CuoiChuong2_MC_B1_NB1():
    """B1. Vectơ trong không gian - Mức độ: NB (Dạng 1): Quy tắc hình hộp & hình lập phương"""
    variant = random.choice([1, 2, 3])
    if variant == 1:
        caudan = r'''Cho hình hộp $ABCD.A'B'C'D'$. Khẳng định nào sau đây là khẳng định đúng?'''
        correct = r'''$\vec{AC'} = \vec{AB} + \vec{AD} + \vec{AA'}$'''
        wrongs = [
            r'''$\vec{AC'} = \vec{AB} + \vec{AD} + \vec{AC}$''',
            r'''$\vec{AC'} = \vec{AB} + \vec{BC} + \vec{AA'}$''',
            r'''$\vec{AC'} = \vec{AB} - \vec{AD} + \vec{AA'}$'''
        ]
        loi_giai = r'''Theo quy tắc hình hộp, với hình hộp $ABCD.A'B'C'D'$, ta có $\vec{AC'} = \vec{AB} + \vec{AD} + \vec{AA'}$.'''
    elif variant == 2:
        pairs = [
            (r"\vec{AA'}", r"\vec{BB'}", [r"\vec{AB}", r"\vec{A'C'}", r"\vec{BD}"]),
            (r"\vec{AB}", r"\vec{DC}", [r"\vec{AD}", r"\vec{BC}", r"\vec{A'D'}"]),
            (r"\vec{A'B'}", r"\vec{D'C'}", [r"\vec{B'C'}", r"\vec{AC}", r"\vec{AA'}"]),
            (r"\vec{AD}", r"\vec{BC}", [r"\vec{AB}", r"\vec{CD}", r"\vec{BB'}"])
        ]
        v1, v_correct, wrongs_v = random.choice(pairs)
        caudan = fr'''Cho hình hộp $ABCD.A'B'C'D'$. Vectơ nào dưới đây bằng vectơ ${v1}$?'''
        correct = fr"${v_correct}$"
        wrongs = [fr"${w}$" for w in wrongs_v]
        loi_giai = fr'''Trong hình hộp $ABCD.A'B'C'D'$, các cạnh đối diện song song và bằng nhau, do đó ta có đẳng thức vectơ: ${v1} = {v_correct}$.'''
    else:
        caudan = r'''Cho hình hộp chữ nhật $ABCD.A'B'C'D'$. Tổng $\vec{BA} + \vec{BC} + \vec{BB'}$ bằng vectơ nào sau đây?'''
        correct = r'''$\vec{BD'}$'''
        wrongs = [r'''$\vec{BD}$''', r'''$\vec{B'D}$''', r'''$\vec{AC'}$''']
        loi_giai = r'''Theo quy tắc hình hộp xuất phát từ đỉnh $B$, ta có: $\vec{BA} + \vec{BC} + \vec{BB'} = \vec{BD'}$.'''
    
    return caudan, shuffle_choices(correct, wrongs), loi_giai


def CuoiChuong2_MC_B1_NB2():
    """B1. Vectơ trong không gian - Mức độ: NB (Dạng 2): Quy tắc cộng trừ vectơ, quy tắc 3 điểm"""
    sub = random.choice([1, 2, 3])
    if sub == 1:
        pts = random.sample(['A', 'B', 'C', 'D', 'S', 'M', 'N'], 3)
        P, Q, R = pts[0], pts[1], pts[2]
        caudan = fr'''Trong không gian, với ba điểm phân biệt ${P}, {Q}, {R}$ bất kì, vectơ $\vec{{{P}{Q}}} - \vec{{{P}{R}}}$ bằng vectơ nào dưới đây?'''
        correct = fr'''$\vec{{{R}{Q}}}$'''
        wrongs = [fr'''$\vec{{{Q}{R}}}$''', fr'''$\vec{{{P}{P}}}$''', fr'''$\vec{{{Q}{P}}}$''']
        loi_giai = fr'''Theo quy tắc trừ hai vectơ chung gốc: $\vec{{{P}{Q}}} - \vec{{{P}{R}}} = \vec{{{R}{Q}}}$.'''
    elif sub == 2:
        pts = random.sample(['A', 'B', 'C', 'D'], 4)
        A, B, C, D = pts[0], pts[1], pts[2], pts[3]
        caudan = fr'''Cho bốn điểm phân biệt ${A}, {B}, {C}, {D}$ trong không gian. Đẳng thức nào sau đây luôn đúng?'''
        correct = fr'''$\vec{{{A}{B}}} + \vec{{{B}{C}}} + \vec{{{C}{D}}} = \vec{{{A}{D}}}$'''
        wrongs = [
            fr'''$\vec{{{A}{B}}} + \vec{{{B}{C}}} + \vec{{{C}{D}}} = \vec{{{D}{A}}}$''',
            fr'''$\vec{{{A}{B}}} + \vec{{{B}{C}}} + \vec{{{C}{D}}} = \vec{{{C}{A}}}$''',
            fr'''$\vec{{{A}{B}}} + \vec{{{B}{C}}} + \vec{{{C}{D}}} = \vec{{0}}$'''
        ]
        loi_giai = fr'''Áp dụng quy tắc cộng liên tiếp: $\vec{{{A}{B}}} + \vec{{{B}{C}}} + \vec{{{C}{D}}} = \vec{{{A}{C}}} + \vec{{{C}{D}}} = \vec{{{A}{D}}}$.'''
    else:
        caudan = r'''Cho đoạn thẳng $AB$ trong không gian có trung điểm là $M$. Mệnh đề nào dưới đây là đúng?'''
        correct = r'''$\vec{MA} + \vec{MB} = \vec{0}$'''
        wrongs = [
            r'''$\vec{MA} - \vec{MB} = \vec{0}$''',
            r'''$\vec{MA} = \vec{MB}$''',
            r'''$\vec{AB} = 2\vec{MA}$'''
        ]
        loi_giai = r'''Vì $M$ là trung điểm của đoạn thẳng $AB$ nên hai vectơ $\vec{MA}$ và $\vec{MB}$ là hai vectơ đối nhau, do đó $\vec{MA} + \vec{MB} = \vec{0}$.'''
    
    return caudan, shuffle_choices(correct, wrongs), loi_giai


def CuoiChuong2_MC_B1_TH():
    """B1. Vectơ trong không gian - Mức độ: TH: Độ dài vectơ tổng / hiệu, góc giữa 2 vectơ"""
    sub = random.choice([1, 2, 3])
    if sub == 1:
        a = random.choice([1, 2, 3, 4, 5, 6, 7])
        caudan = fr'''Cho hình lập phương $ABCD.A'B'C'D'$ có cạnh bằng ${a}$. Độ dài của vectơ $\vec{{u}} = \vec{{AB}} + \vec{{AD}} + \vec{{AA'}}$ bằng'''
        correct = fr'''${a}\sqrt{{3}}$'''
        wrongs = [fr'''${a}\sqrt{{2}}$''', fr'''${a}$''', fr'''${2*a}$''']
        loi_giai = fr'''Theo quy tắc hình hộp, ta có $\vec{{u}} = \vec{{AB}} + \vec{{AD}} + \vec{{AA'}} = \vec{{AC'}}$. \\
Độ dài đường chéo hình lập phương cạnh ${a}$ là $AC' = \sqrt{{{a}^2 + {a}^2 + {a}^2}} = {a}\sqrt{{3}}$. \\
Vậy $|\vec{{u}}| = {a}\sqrt{{3}}$.'''
    elif sub == 2:
        a = random.choice([2, 3, 4, 5, 6])
        caudan = fr'''Cho hình lập phương $ABCD.A'B'C'D'$ cạnh bằng ${a}$. Độ dài của vectơ $\vec{{AB}} + \vec{{AD}}$ bằng'''
        correct = fr'''${a}\sqrt{{2}}$'''
        wrongs = [fr'''${a}\sqrt{{3}}$''', fr'''${2*a}$''', fr'''${a}$''']
        loi_giai = fr'''Theo quy tắc hình bình hành ở mặt đáy $ABCD$: $\vec{{AB}} + \vec{{AD}} = \vec{{AC}}$. \\
Mặt đáy là hình vuông cạnh ${a}$ nên độ dài đường chéo $AC = {a}\sqrt{{2}}$. \\
Do đó $|\vec{{AB}} + \vec{{AD}}| = {a}\sqrt{{2}}$.'''
    else:
        caudan = r'''Cho hình lập phương $ABCD.A'B'C'D'$. Góc giữa hai vectơ $\vec{AB}$ và $\vec{A'D'}$ bằng'''
        correct = r'''$90^\circ$'''
        wrongs = [r'''$45^\circ$''', r'''$60^\circ$''', r'''$120^\circ$''']
        loi_giai = r'''Vì $A'D' // AD$ nên $\vec{A'D'} = \vec{AD}$. \\
Khi đó $(\vec{AB}, \vec{A'D'}) = (\vec{AB}, \vec{AD}) = \widehat{BAD} = 90^\circ$ (do $ABCD$ là hình vuông).'''
    
    return caudan, shuffle_choices(correct, wrongs), loi_giai


def CuoiChuong2_MC_B1_VD():
    """B1. Vectơ trong không gian - Mức độ: VD: Hợp lực 3D / Biểu diễn vectơ / Điểm đặc biệt"""
    sub = random.choice([1, 2])
    if sub == 1:
        triplets = [
            (1, 2, 2, 3),
            (2, 3, 6, 7),
            (1, 4, 8, 9),
            (4, 4, 7, 9),
            (2, 6, 9, 11),
            (6, 6, 7, 11),
            (3, 4, 12, 13)
        ]
        f1, f2, f3, ans = random.choice(triplets)
        mult = random.choice([1, 10, 100])
        f1_m, f2_m, f3_m, ans_m = f1 * mult, f2 * mult, f3 * mult, ans * mult
        caudan = fr'''Một chiếc đèn chùm treo trong phòng chịu tác dụng của ba lực $\vec{{F}}_1, \vec{{F}}_2, \vec{{F}}_3$ có điểm đặt tại một điểm và đôi một vuông góc với nhau, với độ lớn lần lượt là ${f1_m}\text{{ N}}$, ${f2_m}\text{{ N}}$ và ${f3_m}\text{{ N}}$. Độ lớn hợp lực của ba lực đó bằng'''
        correct = fr'''${ans_m}\text{{ N}}$'''
        wrongs = [
            fr'''${ans_m + 2*mult}\text{{ N}}$''',
            fr'''${ans_m - mult if ans_m > mult else ans_m + 3*mult}\text{{ N}}$''',
            fr'''${f1_m + f2_m + f3_m}\text{{ N}}$'''
        ]
        loi_giai = fr'''Hợp lực là $\vec{{F}} = \vec{{F}}_1 + \vec{{F}}_2 + \vec{{F}}_3$. \\
Vì ba lực đôi một vuông góc với nhau nên: \\
$|\vec{{F}}| = \sqrt{{|\vec{{F}}_1|^2 + |\vec{{F}}_2|^2 + |\vec{{F}}_3|^2}} = \sqrt{{{f1_m}^2 + {f2_m}^2 + {f3_m}^2}} = {ans_m}\text{{ N}}$.'''
    else:
        caudan = r'''Cho tứ diện $ABCD$. Gọi $G$ là trọng tâm của tứ diện $ABCD$. Khẳng định nào sau đây là đúng?'''
        correct = r'''$\vec{GA} + \vec{GB} + \vec{GC} + \vec{GD} = \vec{0}$'''
        wrongs = [
            r'''$\vec{GA} + \vec{GB} + \vec{GC} + \vec{GD} = \vec{AB}$''',
            r'''$\vec{GA} + \vec{GB} + \vec{GC} = \vec{GD}$''',
            r'''$\vec{GA} + \vec{GB} = \vec{GC} + \vec{GD}$'''
        ]
        loi_giai = r'''Theo tính chất của trọng tâm tứ diện $G$, ta luôn có đẳng thức vectơ: $\vec{GA} + \vec{GB} + \vec{GC} + \vec{GD} = \vec{0}$.'''
    
    return caudan, shuffle_choices(correct, wrongs), loi_giai


# ==============================================================================
# BÀI 2: TOẠ ĐỘ CỦA ĐIỂM VÀ VECTƠ TRONG KHÔNG GIAN
# ==============================================================================

def CuoiChuong2_MC_B2_NB1():
    """B2. Toạ độ của điểm và vectơ - Mức độ: NB (Dạng 1): Toạ độ điểm và biểu diễn vectơ đơn vị"""
    sub = random.choice([1, 2])
    if sub == 1:
        x = random.choice([-5, -4, -3, -2, -1, 1, 2, 3, 4, 5])
        y = random.choice([-5, -4, -3, -2, -1, 1, 2, 3, 4, 5])
        z = random.choice([-5, -4, -3, -2, -1, 1, 2, 3, 4, 5])
        
        def term(c, unit):
            if c == 1: return f"+ \\vec{{{unit}}}"
            if c == -1: return f"- \\vec{{{unit}}}"
            if c > 0: return f"+ {c}\\vec{{{unit}}}"
            return f"- {abs(c)}\\vec{{{unit}}}"
        
        formula = f"{x}\\vec{{i}} " + term(y, 'j') + " " + term(z, 'k')
        if formula.startswith("+ "): formula = formula[2:]
        
        caudan = fr'''Trong không gian $Oxyz$, cho vectơ $\vec{{u}} = {formula}$. Toạ độ của vectơ $\vec{{u}}$ là'''
        correct = fr'''$({x}; {y}; {z})$'''
        wrongs = [
            fr'''$({y}; {x}; {z})$''',
            fr'''$({x}; {-y}; {z})$''',
            fr'''$({-x}; {-y}; {-z})$'''
        ]
        loi_giai = fr'''Theo định nghĩa toạ độ của vectơ: $\vec{{u}} = x\vec{{i}} + y\vec{{j}} + z\vec{{k}} \iff \vec{{u}} = (x; y; z)$. \\
Do đó $\vec{{u}} = ({x}; {y}; {z})$.'''
    else:
        xA = random.randint(-4, 4)
        yA = random.randint(-4, 4)
        zA = random.randint(-4, 4)
        dx = random.choice([-3, -2, -1, 1, 2, 3])
        dy = random.choice([-3, -2, -1, 1, 2, 3])
        dz = random.choice([-3, -2, -1, 1, 2, 3])
        xB, yB, zB = xA + dx, yA + dy, zA + dz
        
        caudan = fr'''Trong không gian $Oxyz$, cho hai điểm $A({xA}; {yA}; {zA})$ và $B({xB}; {yB}; {zB})$. Toạ độ của vectơ $\vec{{AB}}$ là'''
        correct = fr'''$({dx}; {dy}; {dz})$'''
        wrongs = [
            fr'''$({-dx}; {-dy}; {-dz})$''',
            fr'''$({xA + xB}; {yA + yB}; {zA + zB})$''',
            fr'''$({dx}; {dz}; {dy})$'''
        ]
        loi_giai = fr'''Toạ độ của vectơ $\vec{{AB}}$ được tính theo công thức: \\
$\vec{{AB}} = (x_B - x_A; y_B - y_A; z_B - z_A) = ({xB} - ({xA}); {yB} - ({yA}); {zB} - ({zA})) = ({dx}; {dy}; {dz})$.'''
    
    return caudan, shuffle_choices(correct, wrongs), loi_giai


def CuoiChuong2_MC_B2_NB2():
    """B2. Toạ độ của điểm và vectơ - Mức độ: NB (Dạng 2): Hình chiếu vuông góc và điểm đối xứng"""
    sub = random.choice([1, 2, 3])
    x = random.choice([-6, -5, -4, -3, -2, 2, 3, 4, 5, 6])
    y = random.choice([-6, -5, -4, -3, -2, 2, 3, 4, 5, 6])
    z = random.choice([-6, -5, -4, -3, -2, 2, 3, 4, 5, 6])
    
    if sub == 1:
        axis = random.choice(['Ox', 'Oy', 'Oz'])
        if axis == 'Ox':
            correct = fr'''$({x}; 0; 0)$'''
            wrongs = [fr'''$(0; {y}; 0)$''', fr'''$(0; 0; {z})$''', fr'''$({x}; {y}; 0)$''']
            explanation = fr'''Hình chiếu vuông góc của điểm $M({x}; {y}; {z})$ lên trục $Ox$ giữ nguyên hoành độ $x$ và cho các toạ độ còn lại bằng $0$, tức là $({x}; 0; 0)$.'''
        elif axis == 'Oy':
            correct = fr'''$(0; {y}; 0)$'''
            wrongs = [fr'''$({x}; 0; 0)$''', fr'''$(0; 0; {z})$''', fr'''$(0; {y}; {z})$''']
            explanation = fr'''Hình chiếu vuông góc của điểm $M({x}; {y}; {z})$ lên trục $Oy$ là $(0; {y}; 0)$.'''
        else:
            correct = fr'''$(0; 0; {z})$'''
            wrongs = [fr'''$({x}; 0; 0)$''', fr'''$(0; {y}; 0)$''', fr'''$({x}; 0; {z})$''']
            explanation = fr'''Hình chiếu vuông góc của điểm $M({x}; {y}; {z})$ lên trục $Oz$ là $(0; 0; {z})$.'''
        
        caudan = fr'''Trong không gian $Oxyz$, hình chiếu vuông góc của điểm $M({x}; {y}; {z})$ lên trục ${axis}$ có toạ độ là'''
        loi_giai = explanation
    elif sub == 2:
        plane = random.choice(['Oxy', 'Oyz', 'Oxz'])
        if plane == 'Oxy':
            correct = fr'''$({x}; {y}; 0)$'''
            wrongs = [fr'''$({x}; 0; {z})$''', fr'''$(0; {y}; {z})$''', fr'''$({x}; {y}; {z})$''']
            explanation = fr'''Hình chiếu vuông góc của $M({x}; {y}; {z})$ lên mặt phẳng $(Oxy)$ có cao độ $z = 0$, toạ độ là $({x}; {y}; 0)$.'''
        elif plane == 'Oyz':
            correct = fr'''$(0; {y}; {z})$'''
            wrongs = [fr'''$({x}; 0; {z})$''', fr'''$({x}; {y}; 0)$''', fr'''$(0; 0; {z})$''']
            explanation = fr'''Hình chiếu vuông góc của $M({x}; {y}; {z})$ lên mặt phẳng $(Oyz)$ có hoành độ $x = 0$, toạ độ là $(0; {y}; {z})$.'''
        else:
            correct = fr'''$({x}; 0; {z})$'''
            wrongs = [fr'''$({x}; {y}; 0)$''', fr'''$(0; {y}; {z})$''', fr'''$({x}; 0; 0)$''']
            explanation = fr'''Hình chiếu vuông góc của $M({x}; {y}; {z})$ lên mặt phẳng $(Oxz)$ có tung độ $y = 0$, toạ độ là $({x}; 0; {z})$.'''
        
        caudan = fr'''Trong không gian $Oxyz$, hình chiếu vuông góc của điểm $M({x}; {y}; {z})$ lên mặt phẳng $({plane})$ có toạ độ là'''
        loi_giai = explanation
    else:
        caudan = fr'''Trong không gian $Oxyz$, điểm đối xứng với điểm $M({x}; {y}; {z})$ qua mặt phẳng $(Oxy)$ có toạ độ là'''
        correct = fr'''$({x}; {y}; {-z})$'''
        wrongs = [
            fr'''$({-x}; {-y}; {z})$''',
            fr'''$({-x}; {y}; {z})$''',
            fr'''$({-x}; {-y}; {-z})$'''
        ]
        loi_giai = fr'''Điểm đối xứng với $M({x}; {y}; {z})$ qua mặt phẳng $(Oxy)$ giữ nguyên hoành độ và tung độ, đổi dấu cao độ: $M'({x}; {y}; {-z})$.'''
    
    return caudan, shuffle_choices(correct, wrongs), loi_giai


def CuoiChuong2_MC_B2_TH():
    """B2. Toạ độ của điểm và vectơ - Mức độ: TH: Toạ độ trung điểm, trọng tâm"""
    sub = random.choice([1, 2])
    if sub == 1:
        xM = random.randint(-4, 4)
        yM = random.randint(-4, 4)
        zM = random.randint(-4, 4)
        dx = random.randint(-3, 3)
        dy = random.randint(-3, 3)
        dz = random.randint(-3, 3)
        xA, yA, zA = xM - dx, yM - dy, zM - dz
        xB, yB, zB = xM + dx, yM + dy, zM + dz
        
        caudan = fr'''Trong không gian $Oxyz$, toạ độ trung điểm $M$ của đoạn thẳng nối hai điểm $A({xA}; {yA}; {zA})$ và $B({xB}; {yB}; {zB})$ là'''
        correct = fr'''$({xM}; {yM}; {zM})$'''
        wrongs = [
            fr'''$({xB - xA}; {yB - yA}; {zB - zA})$''',
            fr'''$({xA + xB}; {yA + yB}; {zA + zB})$''',
            fr'''$({-xM}; {-yM}; {-zM})$'''
        ]
        loi_giai = fr'''Toạ độ trung điểm $M$ của đoạn thẳng $AB$ là: \\
$x_M = \dfrac{{{xA} + ({xB})}}{{2}} = {xM}$, \\
$y_M = \dfrac{{{yA} + ({yB})}}{{2}} = {yM}$, \\
$z_M = \dfrac{{{zA} + ({zB})}}{{2}} = {zM}$. \\
Vậy $M({xM}; {yM}; {zM})$.'''
    else:
        xG = random.randint(-3, 3)
        yG = random.randint(-3, 3)
        zG = random.randint(-3, 3)
        xA, yA, zA = random.randint(-3, 3), random.randint(-3, 3), random.randint(-3, 3)
        xB, yB, zB = random.randint(-3, 3), random.randint(-3, 3), random.randint(-3, 3)
        xC = 3 * xG - xA - xB
        yC = 3 * yG - yA - yB
        zC = 3 * zG - zA - zB
        
        caudan = fr'''Trong không gian $Oxyz$, cho tam giác $ABC$ có $A({xA}; {yA}; {zA})$, $B({xB}; {yB}; {zB})$, $C({xC}; {yC}; {zC})$. Toạ độ trọng tâm $G$ của tam giác $ABC$ là'''
        correct = fr'''$({xG}; {yG}; {zG})$'''
        wrongs = [
            fr'''$({3*xG}; {3*yG}; {3*zG})$''',
            fr'''$({-xG}; {-yG}; {-zG})$''',
            fr'''$({xG + 1}; {yG}; {zG - 1})$'''
        ]
        loi_giai = fr'''Toạ độ trọng tâm $G$ của tam giác $ABC$ là: \\
$x_G = \dfrac{{{xA} + ({xB}) + ({xC})}}{{3}} = {xG}$, \\
$y_G = \dfrac{{{yA} + ({yB}) + ({yC})}}{{3}} = {yG}$, \\
$z_G = \dfrac{{{zA} + ({zB}) + ({zC})}}{{3}} = {zG}$. \\
Vậy $G({xG}; {yG}; {zG})$.'''
    
    return caudan, shuffle_choices(correct, wrongs), loi_giai


def CuoiChuong2_MC_B2_VD():
    """B2. Toạ độ của điểm và vectơ - Mức độ: VD: Đỉnh thứ tư hình bình hành / hình hộp"""
    xA, yA, zA = random.randint(-3, 3), random.randint(-3, 3), random.randint(-3, 3)
    xB, yB, zB = random.randint(-3, 3), random.randint(-3, 3), random.randint(-3, 3)
    xC, yC, zC = random.randint(-3, 3), random.randint(-3, 3), random.randint(-3, 3)
    xD = xA + xC - xB
    yD = yA + yC - yB
    zD = zA + zC - zB
    
    caudan = fr'''Trong không gian $Oxyz$, cho ba điểm $A({xA}; {yA}; {zA})$, $B({xB}; {yB}; {zB})$, $C({xC}; {yC}; {zC})$. Tìm toạ độ đỉnh $D$ để tứ giác $ABCD$ là một hình bình hành.'''
    correct = fr'''$D({xD}; {yD}; {zD})$'''
    wrongs = [
        fr'''$D({xB + xC - xA}; {yB + yC - yA}; {zB + zC - zA})$''',
        fr'''$D({xA + xB - xC}; {yA + yB - yC}; {zA + zB - zC})$''',
        fr'''$D({-xD}; {-yD}; {-zD})$'''
    ]
    loi_giai = fr'''Để tứ giác $ABCD$ là hình bình hành thì $\vec{{AD}} = \vec{{BC}}$. \\
Ta có $\vec{{BC}} = ({xC} - ({xB}); {yC} - ({yB}); {zC} - ({zB})) = ({xC - xB}; {yC - yB}; {zC - zB})$. \\
Gọi $D(x; y; z)$, ta có $\vec{{AD}} = (x - ({xA}); y - ({yA}); z - ({zA}))$. \\
Do đó: \\
$\begin{{cases}} x - ({xA}) = {xC - xB} \\ y - ({yA}) = {yC - yB} \\ z - ({zA}) = {zC - zB} \end{{cases}} \iff \begin{{cases}} x = {xD} \\ y = {yD} \\ z = {zD} \end{{cases}}$. \\
Vậy $D({xD}; {yD}; {zD})$.'''
    
    return caudan, shuffle_choices(correct, wrongs), loi_giai


# ==============================================================================
# BÀI 3: BIỂU THỨC TOẠ ĐỘ CỦA CÁC PHÉP TOÁN VECTƠ
# ==============================================================================

def CuoiChuong2_MC_B3_NB1():
    """B3. Biểu thức toạ độ phép toán vectơ - Mức độ: NB (Dạng 1): Tổng hiệu và tích với một số"""
    sub = random.choice([1, 2])
    x1, y1, z1 = random.randint(-4, 4), random.randint(-4, 4), random.randint(-4, 4)
    x2, y2, z2 = random.randint(-4, 4), random.randint(-4, 4), random.randint(-4, 4)
    
    if sub == 1:
        op = random.choice(['+', '-'])
        if op == '+':
            rx, ry, rz = x1 + x2, y1 + y2, z1 + z2
            caudan = fr'''Trong không gian $Oxyz$, cho hai vectơ $\vec{{u}} = ({x1}; {y1}; {z1})$ và $\vec{{v}} = ({x2}; {y2}; {z2})$. Toạ độ của vectơ $\vec{{u}} + \vec{{v}}$ là'''
            correct = fr'''$({rx}; {ry}; {rz})$'''
            wrongs = [
                fr'''$({x1 - x2}; {y1 - y2}; {z1 - z2})$''',
                fr'''$({rx}; {ry}; {rz + 1})$''',
                fr'''$({-rx}; {-ry}; {-rz})$'''
            ]
            loi_giai = fr'''Ta có $\vec{{u}} + \vec{{v}} = ({x1} + ({x2}); {y1} + ({y2}); {z1} + ({z2})) = ({rx}; {ry}; {rz})$.'''
        else:
            rx, ry, rz = x1 - x2, y1 - y2, z1 - z2
            caudan = fr'''Trong không gian $Oxyz$, cho hai vectơ $\vec{{u}} = ({x1}; {y1}; {z1})$ và $\vec{{v}} = ({x2}; {y2}; {z2})$. Toạ độ của vectơ $\vec{{u}} - \vec{{v}}$ là'''
            correct = fr'''$({rx}; {ry}; {rz})$'''
            wrongs = [
                fr'''$({x1 + x2}; {y1 + y2}; {z1 + z2})$''',
                fr'''$({x2 - x1}; {y2 - y1}; {z2 - z1})$''',
                fr'''$({rx}; {-ry}; {rz})$'''
            ]
            loi_giai = fr'''Ta có $\vec{{u}} - \vec{{v}} = ({x1} - ({x2}); {y1} - ({y2}); {z1} - ({z2})) = ({rx}; {ry}; {rz})$.'''
    else:
        k = random.choice([2, 3])
        rx, ry, rz = k * x1, k * y1, k * z1
        caudan = fr'''Trong không gian $Oxyz$, cho vectơ $\vec{{u}} = ({x1}; {y1}; {z1})$. Toạ độ của vectơ ${k}\vec{{u}}$ là'''
        correct = fr'''$({rx}; {ry}; {rz})$'''
        wrongs = [
            fr'''$({x1 + k}; {y1 + k}; {z1 + k})$''',
            fr'''$({-rx}; {-ry}; {-rz})$''',
            fr'''$({rx}; {ry}; {z1})$'''
        ]
        loi_giai = fr'''Toạ độ của vectơ ${k}\vec{{u}} = ({k} \cdot ({x1}); {k} \cdot ({y1}); {k} \cdot ({z1})) = ({rx}; {ry}; {rz})$.'''
    
    return caudan, shuffle_choices(correct, wrongs), loi_giai


def CuoiChuong2_MC_B3_NB2():
    """B3. Biểu thức toạ độ phép toán vectơ - Mức độ: NB (Dạng 2): Độ dài vectơ và tích vô hướng"""
    sub = random.choice([1, 2])
    if sub == 1:
        triplets = [
            (1, 2, 2, 3),
            (2, 3, 6, 7),
            (1, 4, 8, 9),
            (4, 4, 7, 9),
            (2, 6, 9, 11),
            (6, 6, 7, 11),
            (3, 4, 12, 13)
        ]
        a, b, c, ans = random.choice(triplets)
        sx = a * random.choice([-1, 1])
        sy = b * random.choice([-1, 1])
        sz = c * random.choice([-1, 1])
        
        caudan = fr'''Trong không gian $Oxyz$, độ dài của vectơ $\vec{{u}} = ({sx}; {sy}; {sz})$ bằng'''
        correct = fr'''${ans}$'''
        wrongs = [fr'''${ans**2}$''', fr'''${ans + 2}$''', fr'''$\sqrt{{{ans}}}$''']
        loi_giai = fr'''Độ dài của vectơ $\vec{{u}}$ là: \\
$|\vec{{u}}| = \sqrt{{{sx}^2 + ({sy})^2 + ({sz})^2}} = \sqrt{{{sx**2 + sy**2 + sz**2}}} = {ans}$.'''
    else:
        x1, y1, z1 = random.randint(-4, 4), random.randint(-4, 4), random.randint(-4, 4)
        x2, y2, z2 = random.randint(-4, 4), random.randint(-4, 4), random.randint(-4, 4)
        dot = x1 * x2 + y1 * y2 + z1 * z2
        
        caudan = fr'''Trong không gian $Oxyz$, cho hai vectơ $\vec{{u}} = ({x1}; {y1}; {z1})$ và $\vec{{v}} = ({x2}; {y2}; {z2})$. Tích vô hướng $\vec{{u}} \cdot \vec{{v}}$ bằng'''
        correct = fr'''${dot}$'''
        wrongs = [fr'''${dot + 2}$''', fr'''${-dot if dot != 0 else 5}$''', fr'''${dot - 3}$''']
        loi_giai = fr'''Tích vô hướng của hai vectơ là: \\
$\vec{{u}} \cdot \vec{{v}} = x_1x_2 + y_1y_2 + z_1z_2 = ({x1})({x2}) + ({y1})({y2}) + ({z1})({z2}) = {dot}$.'''
    
    return caudan, shuffle_choices(correct, wrongs), loi_giai


def CuoiChuong2_MC_B3_TH():
    """B3. Biểu thức toạ độ phép toán vectơ - Mức độ: TH: Góc giữa hai vectơ, hai vectơ vuông góc / cùng phương"""
    sub = random.choice([1, 2, 3])
    if sub == 1:
        x1, y1, z1 = random.choice([-3, -2, -1, 1, 2, 3]), random.choice([-3, -2, 1, 2, 3]), 1
        x2, y2 = random.randint(-3, 3), random.randint(-3, 3)
        c_val = x1 * x2 + y1 * y2
        ans_m = -c_val
        
        caudan = fr'''Trong không gian $Oxyz$, cho hai vectơ $\vec{{u}} = ({x1}; {y1}; {z1})$ và $\vec{{v}} = ({x2}; {y2}; m)$. Tìm giá trị của tham số $m$ để $\vec{{u}} \perp \vec{{v}}$.'''
        correct = fr'''$m = {ans_m}$'''
        wrongs = [fr'''$m = {-ans_m}$''', fr'''$m = {ans_m + 1}$''', fr'''$m = {ans_m - 2}$''']
        loi_giai = fr'''Hai vectơ $\vec{{u}}$ và $\vec{{v}}$ vuông góc khi và chỉ khi: \\
$\vec{{u}} \cdot \vec{{v}} = 0 \iff ({x1})({x2}) + ({y1})({y2}) + ({z1}) \cdot m = 0$ \\
$\iff {c_val} + m = 0 \iff m = {ans_m}$.'''
    elif sub == 2:
        k = random.choice([2, 3, -2, -3])
        x1 = random.choice([-3, -2, -1, 1, 2, 3])
        y1 = random.choice([-3, -2, -1, 1, 2, 3])
        z1 = random.choice([-3, -2, -1, 1, 2, 3])
        x2 = k * x1
        z2 = k * z1
        ans_m = k * y1
        
        caudan = fr'''Trong không gian $Oxyz$, cho hai vectơ $\vec{{a}} = ({x1}; {y1}; {z1})$ và $\vec{{b}} = ({x2}; m; {z2})$. Hai vectơ $\vec{{a}}$ và $\vec{{b}}$ cùng phương khi $m$ bằng'''
        correct = fr'''${ans_m}$'''
        wrongs = [fr'''${-ans_m}$''', fr'''${ans_m + 1}$''', fr'''${y1}$''']
        loi_giai = fr'''Hai vectơ $\vec{{a}}$ và $\vec{{b}}$ cùng phương khi tồn tại số $k$ sao cho $\vec{{b}} = k\vec{{a}}$. \\
Do $\dfrac{{{x2}}}{{{x1}}} = \dfrac{{{z2}}}{{{z1}}} = {k}$, nên ta có: \\
$m = {k} \cdot ({y1}) = {ans_m}$.'''
    else:
        caudan = r'''Trong không gian $Oxyz$, cho hai vectơ $\vec{u} = (1; 1; 0)$ và $\vec{v} = (0; 1; 1)$. Góc giữa hai vectơ $\vec{u}$ và $\vec{v}$ bằng'''
        correct = r'''$60^\circ$'''
        wrongs = [r'''$30^\circ$''', r'''$45^\circ$''', r'''$90^\circ$''']
        loi_giai = r'''Ta có: \\
$\vec{u} \cdot \vec{v} = 1 \cdot 0 + 1 \cdot 1 + 0 \cdot 1 = 1$, \\
$|\vec{u}| = \sqrt{1^2 + 1^2 + 0^2} = \sqrt{2}$, \\
$|\vec{v}| = \sqrt{0^2 + 1^2 + 1^2} = \sqrt{2}$. \\
Do đó $\cos(\vec{u}, \vec{v}) = \dfrac{\vec{u} \cdot \vec{v}}{|\vec{u}||\vec{v}|} = \dfrac{1}{\sqrt{2} \cdot \sqrt{2}} = \dfrac{1}{2}$. \\
Suy ra $(\vec{u}, \vec{v}) = 60^\circ$.'''
    
    return caudan, shuffle_choices(correct, wrongs), loi_giai


def CuoiChuong2_MC_B3_VD():
    """B3. Biểu thức toạ độ phép toán vectơ - Mức độ: VD: Toán thực tế máy bay/lực"""
    sub = random.choice([1, 2])
    if sub == 1:
        triplets = [
            (300, 400, 0, 500),
            (100, 200, 200, 300),
            (200, 300, 600, 700),
            (120, 160, 0, 200),
            (400, 400, 700, 900)
        ]
        vx, vy, vz, v_mag = random.choice(triplets)
        caudan = fr'''Một máy bay dân dụng đang bay trên bầu trời có vectơ vận tốc $\vec{{v}} = ({vx}; {vy}; {vz})$ (đơn vị: km/h). Tốc độ (độ lớn của vận tốc) của máy bay bằng'''
        correct = fr'''${v_mag}\text{{ km/h}}$'''
        wrongs = [
            fr'''${v_mag + 50}\text{{ km/h}}$''',
            fr'''${vx + vy + vz}\text{{ km/h}}$''',
            fr'''${v_mag - 100}\text{{ km/h}}$'''
        ]
        loi_giai = fr'''Tốc độ của máy bay chính là độ lớn của vectơ vận tốc $\vec{{v}}$: \\
$|\vec{{v}}| = \sqrt{{{vx}^2 + {vy}^2 + {vz}^2}} = {v_mag}\text{{ km/h}}$.'''
    else:
        fx1, fy1, fz1 = random.randint(10, 50), random.randint(-40, 40), random.randint(10, 50)
        fx2, fy2, fz2 = random.randint(-50, -10), random.randint(-40, 40), random.randint(10, 50)
        fx3 = -(fx1 + fx2)
        fy3 = -(fy1 + fy2)
        fz3 = -(fz1 + fz2)
        
        caudan = fr'''Một vật nằm yên cân bằng trong không gian $Oxyz$ chịu tác dụng của ba lực $\vec{{F}}_1, \vec{{F}}_2, \vec{{F}}_3$. Biết $\vec{{F}}_1 = ({fx1}; {fy1}; {fz1})\text{{ N}}$ và $\vec{{F}}_2 = ({fx2}; {fy2}; {fz2})\text{{ N}}$. Toạ độ của lực $\vec{{F}}_3$ là'''
        correct = fr'''$({fx3}; {fy3}; {fz3})\text{{ N}}$'''
        wrongs = [
            fr'''$({-fx3}; {-fy3}; {-fz3})\text{{ N}}$''',
            fr'''$({fx1 + fx2}; {fy1 + fy2}; {fz1 + fz2})\text{{ N}}$''',
            fr'''$({fx3}; {fy3}; {-fz3})\text{{ N}}$'''
        ]
        loi_giai = fr'''Vì vật ở trạng thái cân bằng nên tổng hợp lực bằng vectơ-không: \\
$\vec{{F}}_1 + \vec{{F}}_2 + \vec{{F}}_3 = \vec{{0}} \iff \vec{{F}}_3 = -(\vec{{F}}_1 + \vec{{F}}_2)$. \\
Do đó: \\
$\vec{{F}}_3 = -({fx1} + ({fx2}); {fy1} + ({fy2}); {fz1} + ({fz2})) = ({fx3}; {fy3}; {fz3})\text{{ N}}$.'''
    
    return caudan, shuffle_choices(correct, wrongs), loi_giai
