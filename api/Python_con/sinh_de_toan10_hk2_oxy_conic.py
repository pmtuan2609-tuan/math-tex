"""Ngân hàng câu hỏi sinh ngẫu nhiên cho Toán 10 Học kì 2 - Chương VII:
Phương pháp tọa độ trong mặt phẳng (Oxy) & Ba đường Conic:
- Bài 19: Phương trình đường thẳng (bổ sung & nâng cấp các dạng trong đề ôn HK2)
- Bài 20: Vị trí tương đối giữa hai đường thẳng, góc và khoảng cách
- Bài 21: Phương trình đường tròn
- Bài 22: Ba đường Conic (Elip, Hypebol, Parabol)
"""

import math
import random
from fractions import Fraction

from sinh_de_toan10_hk2_chuong6_7 import (
    _frac_tex,
    _signed_frac_term,
    _lin_tex,
    _signed_factor,
    _make_choices,
)


# ==============================================================================
# CÁC HÀM PHỤ TRỢ ĐỊNH DẠNG OXY & CONIC
# ==============================================================================

def _simplify_sqrt(n):
    """Phân tích số nguyên dương n = k^2 * r với r không chứa nhân tử chính phương."""
    if n <= 0:
        return 0, 0
    k = 1
    r = n
    d = 2
    while d * d <= r:
        while r % (d * d) == 0:
            k *= d
            r //= (d * d)
        d += 1
    return k, r


def _sqrt_tex(n):
    """Định dạng căn bậc hai của số nguyên không âm n (VD: 12 -> 2\\sqrt{3})."""
    if n == 0:
        return "0"
    k, r = _simplify_sqrt(n)
    if r == 1:
        return str(k)
    if k == 1:
        return f"\\sqrt{{{r}}}"
    return f"{k}\\sqrt{{{r}}}"


def _rat_sqrt_tex(num, den_sq):
    """Định dạng |num| / sqrt(den_sq) về dạng tối giản chuẩn LaTeX."""
    num = abs(int(num))
    if num == 0:
        return "0"
    k, r = _simplify_sqrt(int(den_sq))
    f = Fraction(num, k * r)
    if r == 1:
        return _frac_tex(f)
    p, q = f.numerator, f.denominator
    sqrt_part = f"\\sqrt{{{r}}}"
    num_str = sqrt_part if p == 1 else f"{p}{sqrt_part}"
    if q == 1:
        return num_str
    return f"\\dfrac{{{num_str}}}{{{q}}}"


def _line_eq_tex(a, b, c):
    """Định dạng phương trình tổng quát ax + by + c = 0 chuẩn LaTeX."""
    fa = Fraction(a).limit_denominator()
    fb = Fraction(b).limit_denominator()
    fc = Fraction(c).limit_denominator()
    parts = []
    if fa != 0:
        parts.append(_lin_tex(fa, 0, "x"))
    if fb != 0:
        if not parts:
            parts.append(_lin_tex(fb, 0, "y"))
        else:
            parts.append(_signed_frac_term(fb, "y"))
    if fc != 0:
        if not parts:
            parts.append(_frac_tex(fc))
        else:
            parts.append(_signed_frac_term(fc))
    lhs = "".join(parts) if parts else "0"
    return f"{lhs} = 0"


def _reduce_abc(a, b, c):
    """Rút gọn bộ hệ số nguyên (a, b, c) sao cho UCLN = 1 và hệ số đầu dương."""
    g = math.gcd(math.gcd(abs(a), abs(b)), abs(c))
    if g > 1:
        a //= g
        b //= g
        c //= g
    if a < 0 or (a == 0 and b < 0):
        a, b, c = -a, -b, -c
    return a, b, c


def _param_row(x0, u):
    """Định dạng một dòng phương trình tham số: x_0 + u*t."""
    fx = Fraction(x0).limit_denominator()
    fu = Fraction(u).limit_denominator()
    if fx == 0 and fu == 0:
        return "0"
    if fx == 0:
        return _lin_tex(fu, 0, "t")
    if fu == 0:
        return _frac_tex(fx)
    return f"{_frac_tex(fx)}{_signed_frac_term(fu, 't')}"


def _ptts_tex(x0, y0, u1, u2):
    """Định dạng hệ phương trình tham số đường thẳng."""
    rx = _param_row(x0, u1)
    ry = _param_row(y0, u2)
    return f"\\begin{{cases}} x = {rx} \\\\ y = {ry} \\end{{cases}}"


def _ptts_inline_tex(x0, y0, u1, u2):
    """Định dạng hệ PTTS đặt trong dấu ngoặc nhọn cho lời giải hoặc đề."""
    return _ptts_tex(x0, y0, u1, u2)


def _sub_num_tex(val, center):
    """Định dạng (val - center) an toàn khi center âm hoặc val là tên biến ('x', 'y')."""
    fc = Fraction(center).limit_denominator()
    v_str = val if isinstance(val, str) else _frac_tex(Fraction(val).limit_denominator())
    if fc >= 0:
        return f"{v_str} - {_frac_tex(fc)}"
    return f"{v_str} + {_frac_tex(-fc)}"


def _circle_std_tex(a, b, r2):
    """Định dạng (x - a)^2 + (y - b)^2 = r2."""
    fa = Fraction(a).limit_denominator()
    fb = Fraction(b).limit_denominator()
    px = "x^2" if fa == 0 else f"{_signed_factor(fa, 'x')}^2"
    py = "y^2" if fb == 0 else f"{_signed_factor(fb, 'y')}^2"
    return f"{px} + {py} = {_frac_tex(r2)}"


def _circle_gen_tex(D, E, F):
    """Định dạng x^2 + y^2 + Dx + Ey + F = 0."""
    s = "x^2 + y^2"
    s += _signed_frac_term(D, "x")
    s += _signed_frac_term(E, "y")
    s += _signed_frac_term(F)
    return f"{s} = 0"


def _pt_tex(x, y):
    """Định dạng tọa độ điểm (x; y)."""
    return f"({_frac_tex(x)}; {_frac_tex(y)})"


def _vec_tex(x, y):
    """Định dạng tọa độ vectơ (x; y)."""
    return f"({_frac_tex(x)}; {_frac_tex(y)})"


# ==============================================================================
# BÀI 19: PHƯƠNG TRÌNH ĐƯỜNG THẲNG (BỔ SUNG DẠNG ÔN HK2)
# ==============================================================================

def K10_Oxy_MC_PTDT_ChuyenPTTQ_Sang_PTTS():
    """Chuyển PTTQ sang PTTS, hoặc viết PTTS qua 2 điểm / đường thẳng OG."""
    variant = random.choice([1, 2, 3])
    if variant == 1:
        # Cho d: ax + by + c = 0. Tìm PTTS tương ứng
        while True:
            a = random.choice([-5, -4, -3, -2, 2, 3, 4, 5])
            b = random.choice([-5, -4, -3, -2, 2, 3, 4, 5])
            if math.gcd(abs(a), abs(b)) == 1:
                break
        # Chọn điểm nguyên M(x0, y0) nằm trên d để c gọn
        x0 = random.choice([0, 1, -1, 2, -2])
        y0 = random.choice([-3, -2, -1, 1, 2, 3, 4])
        c = -(a * x0 + b * y0)
        eq_d = _line_eq_tex(a, b, c)

        # VTCP đúng: u = (b, -a) hoặc (1, -a/b)
        mode_u = random.choice([1, 2])
        if mode_u == 1:
            u1, u2 = b, -a
            ans = f"${_ptts_tex(x0, y0, u1, u2)}$."
            d1 = f"${_ptts_tex(x0, y0, a, b)}$."
            d2 = f"${_ptts_tex(x0, y0, b, a)}$."
            d3 = f"${_ptts_tex(x0 + 1, y0, u1, u2)}$."
            d4 = f"${_ptts_tex(y0, x0, u1, u2)}$."
        else:
            # Dạng giống Img 2 Câu 1: x = 2t, y = (a/b)t + y0 hoặc x = x0 + bt, y = y0 - at
            u1 = Fraction(b)
            u2 = Fraction(-a)
            # Dùng x = b*t hoặc x = t (y có phân số)
            x_base = 0
            y_base = Fraction(-c, b)
            u1_alt = b
            u2_alt = -a
            # Nếu cho x = b*t -> y = y_base - a*t thì y vẫn đẹp nếu b | -c
            ans = f"${_ptts_tex(x_base, y_base, u1_alt, u2_alt)}$."
            d1 = f"${_ptts_tex(x_base, y_base, a, b)}$."
            d2 = f"${_ptts_tex(x_base, y_base, -a, b)}$."
            d3 = f"${_ptts_tex(x_base, y_base + 1, u1_alt, u2_alt)}$."
            d4 = f"${_ptts_tex(x_base, -y_base, u1_alt, u2_alt)}$."
            u1, u2 = u1_alt, u2_alt
            x0, y0 = x_base, y_base

        caudan = f"Phương trình nào sau đây là phương trình tham số của đường thẳng $d: {eq_d}$?"
        loigiai = (
            f"Đường thẳng $d: {eq_d}$ có một vectơ pháp tuyến là $\\vec{{n}} = {_vec_tex(a, b)}$.\n"
            f"Suy ra một vectơ chỉ phương của $d$ là $\\vec{{u}} = {_vec_tex(u1, u2)}$.\n"
            f"Chọn điểm $M{_pt_tex(x0, y0)} \\in d$ (thay vào phương trình của $d$ thấy thỏa mãn).\n"
            f"Vậy phương trình tham số của đường thẳng $d$ là:\n"
            f"$${_ptts_tex(x0, y0, u1, u2)}.$$"
        )
        phuongan = _make_choices(ans, [d1, d2, d3, d4])
        return caudan, phuongan, loigiai

    if variant == 2:
        # Img 5 Câu 8: PTTS đường thẳng d đi qua hai điểm A(xA; yA) và B(xB; yB)
        while True:
            xA = random.randint(-4, 4)
            yA = random.randint(-4, 4)
            dx = random.choice([-5, -4, -3, -2, 2, 3, 4, 5])
            dy = random.choice([-5, -4, -3, -2, 2, 3, 4, 5])
            if abs(dx) != abs(dy):
                break
        xB = xA + dx
        yB = yA + dy
        ans = f"${_ptts_tex(xA, yA, dx, dy)}$."
        d1 = f"${_ptts_tex(xA, yA, dy, dx)}$."
        d2 = f"${_ptts_tex(xA, yA, dx, -dy)}$."
        d3 = f"${_ptts_tex(dx, dy, xA, yA)}$."
        d4 = f"${_ptts_tex(xB, yB, -dy, dx)}$."
        caudan = f"Phương trình tham số của đường thẳng $d$ đi qua hai điểm $A{_pt_tex(xA, yA)}$ và $B{_pt_tex(xB, yB)}$ là"
        loigiai = (
            f"Đường thẳng $d$ đi qua $A{_pt_tex(xA, yA)}$ và nhận $\\overrightarrow{{AB}} = {_vec_tex(dx, dy)}$ làm một vectơ chỉ phương.\n"
            f"Suy ra phương trình tham số của đường thẳng $d$ là:\n"
            f"$${_ptts_tex(xA, yA, dx, dy)}.$$"
        )
        phuongan = _make_choices(ans, [d1, d2, d3, d4])
        return caudan, phuongan, loigiai

    # variant == 3 (Img 5 Câu 7): Cho tam giác ABC, viết PTTS đường thẳng OG (G là trọng tâm)
    while True:
        xG = random.choice([-3, -2, -1, 1, 2, 3, 4])
        yG = random.choice([-3, -2, -1, 1, 2, 3, 4])
        if xG != yG and xG != -yG:
            break
    xA = random.randint(-3, 5)
    yA = random.randint(-3, 5)
    xB = random.randint(-3, 5)
    yB = random.randint(-3, 5)
    xC = 3 * xG - xA - xB
    yC = 3 * yG - yA - yB

    g = math.gcd(abs(xG), abs(yG))
    u1, u2 = xG // g, yG // g

    ans = f"${_ptts_tex(0, 0, u1, u2)}$."
    d1 = f"${_ptts_tex(u1, u2, 1, 1)}$."
    d2 = f"${_ptts_tex(0, 0, u2, u1)}$."
    d3 = f"${_ptts_tex(0, 0, u1, -u2)}$."
    d4 = f"${_ptts_tex(u2, u1, 0, 1)}$."
    caudan = (
        f"Cho tam giác $ABC$ có $A{_pt_tex(xA, yA)}$, $B{_pt_tex(xB, yB)}$, $C{_pt_tex(xC, yC)}$. "
        f"Viết phương trình tham số đường thẳng $OG$ trong đó $O$ là gốc tọa độ và điểm $G$ là trọng tâm của tam giác $ABC$."
    )
    loigiai = (
        f"Trọng tâm $G$ của tam giác $ABC$ có tọa độ:\n"
        f"$$x_G = \\dfrac{{{xA} + ({xB}) + ({xC})}}{{3}} = {xG}, \\quad y_G = \\dfrac{{{yA} + ({yB}) + ({yC})}}{{3}} = {yG}.$$\n"
        f"Suy ra $G{_pt_tex(xG, yG)}$. Đường thẳng $OG$ đi qua $O(0; 0)$ và có vectơ chỉ phương $\\overrightarrow{{OG}} = {_vec_tex(xG, yG)}$"
        + (f" (cùng phương với $\\vec{{u}} = {_vec_tex(u1, u2)}$)" if g > 1 else "")
        + f".\nVậy phương trình tham số của đường thẳng $OG$ là:\n$${_ptts_tex(0, 0, u1, u2)}.$$"
    )
    phuongan = _make_choices(ans, [d1, d2, d3, d4])
    return caudan, phuongan, loigiai


def K10_Oxy_MC_PTDT_DoanChan_TrungTruc_SongSongTruc():
    """Đường thẳng có VTCP song song trục tọa độ, phương trình đoạn chắn, đường trung trực."""
    variant = random.choice([1, 2, 3])
    if variant == 1:
        # Img 2 Câu 2 & Img 3 Câu 2: qua M(x0, y0), VTCP u = (k, 0) hoặc (0, k)
        axis_x = random.choice([True, False])
        k = random.choice([-4, -3, -2, 2, 3, 4])
        if axis_x:
            x0 = random.choice([0, random.randint(-3, 3)])
            y0 = random.choice([-4, -3, -2, -1, 1, 2, 3, 4])
            u1, u2 = k, 0
            # y - y0 = 0
            ans = f"$d: {_line_eq_tex(0, 1, -y0)}$."
            d1 = f"$d: {_line_eq_tex(1, 0, -x0)}$."
            d2 = f"$d: {_line_eq_tex(0, 1, y0)}$."
            d3 = f"$d: {_line_eq_tex(1, 0, -y0)}$."
            d4 = f"$d: {_line_eq_tex(k, 0, -k * x0)}$."
            n_vec = "(0; 1)"
            step_eq = f"$0(x - ({x0})) + 1(y - ({y0})) = 0 \\iff {_line_eq_tex(0, 1, -y0)}$"
        else:
            x0 = random.choice([-4, -3, -2, -1, 1, 2, 3, 4])
            y0 = random.choice([0, random.randint(-3, 3)])
            u1, u2 = 0, k
            ans = f"$d: {_line_eq_tex(1, 0, -x0)}$."
            d1 = f"$d: {_line_eq_tex(0, 1, -y0)}$."
            d2 = f"$d: {_line_eq_tex(1, 0, x0)}$."
            d3 = f"$d: {_line_eq_tex(0, 1, -x0)}$."
            d4 = f"$d: {_line_eq_tex(0, k, -k * y0)}$."
            n_vec = "(1; 0)"
            step_eq = f"$1(x - ({x0})) + 0(y - ({y0})) = 0 \\iff {_line_eq_tex(1, 0, -x0)}$"

        caudan = (
            f"Đường thẳng $d$ đi qua điểm $M{_pt_tex(x0, y0)}$ và có vectơ chỉ phương "
            f"$\\vec{{u}} = {_vec_tex(u1, u2)}$ có phương trình tổng quát là"
        )
        loigiai = (
            f"Đường thẳng $d$ có vectơ chỉ phương $\\vec{{u}} = {_vec_tex(u1, u2)}$ "
            f"nên có một vectơ pháp tuyến là $\\vec{{n}} = {n_vec}$.\n"
            f"Vì $d$ đi qua điểm $M{_pt_tex(x0, y0)}$ nên phương trình tổng quát của $d$ là:\n"
            f"{step_eq}."
        )
        phuongan = _make_choices(ans, [d1, d2, d3, d4])
        return caudan, phuongan, loigiai

    if variant == 2:
        # Img 2 Câu 10: Phương trình đoạn chắn đi qua A(0; b) và B(a; 0)
        while True:
            a = random.choice([-7, -6, -5, -4, -3, -2, 2, 3, 4, 5, 6, 7])
            b = random.choice([-7, -6, -5, -4, -3, -2, 2, 3, 4, 5, 6, 7])
            if abs(a) != abs(b):
                break
        ans = f"$\\dfrac{{x}}{{{a}}} + \\dfrac{{y}}{{{b}}} = 1$."
        d1 = f"$\\dfrac{{x}}{{{b}}} + \\dfrac{{y}}{{{a}}} = 1$."
        d2 = f"$\\dfrac{{x}}{{{-a}}} + \\dfrac{{y}}{{{-b}}} = 1$."
        d3 = f"$\\dfrac{{x}}{{{a}}} + \\dfrac{{y}}{{{-b}}} = 1$."
        d4 = f"$\\dfrac{{x}}{{{-b}}} + \\dfrac{{y}}{{{a}}} = 1$."
        caudan = f"Phương trình đường thẳng đi qua hai điểm $A(0; {b})$, $B({a}; 0)$ là"
        loigiai = (
            f"Áp dụng phương trình đường thẳng theo đoạn chắn đi qua $B({a}; 0)$ trên $Ox$ và $A(0; {b})$ trên $Oy$, ta có:\n"
            f"$$\\dfrac{{x}}{{{a}}} + \\dfrac{{y}}{{{b}}} = 1.$$"
        )
        phuongan = _make_choices(ans, [d1, d2, d3, d4])
        return caudan, phuongan, loigiai

    # variant == 3 (Img 3 Câu 3): Đường trung trực đoạn AB
    while True:
        xI = random.randint(-3, 4)
        yI = random.randint(-3, 4)
        hx = random.choice([-3, -2, -1, 1, 2, 3])
        hy = random.choice([-3, -2, -1, 1, 2, 3])
        if abs(hx) != abs(hy):
            break
    xA, yA = xI - hx, yI - hy
    xB, yB = xI + hx, yI + hy
    dx, dy = 2 * hx, 2 * hy
    # Đường trung trực qua I(xI, yI), VTPT n = (hx, hy)
    a, b, c = _reduce_abc(hx, hy, -(hx * xI + hy * yI))
    ans = f"${_line_eq_tex(a, b, c)}$."
    d1 = f"${_line_eq_tex(*_reduce_abc(a, b, c + 1))}$."
    d2 = f"${_line_eq_tex(*_reduce_abc(a, -b, -(a * xI - b * yI)))}$."
    d3 = f"${_line_eq_tex(*_reduce_abc(a, -b, -(a * xI - b * yI) + 1))}$."
    d4 = f"${_line_eq_tex(*_reduce_abc(b, -a, -(b * xI - a * yI)))}$."
    caudan = (
        f"Trong mặt phẳng $Oxy$, đường trung trực của đoạn $AB$ với "
        f"$A{_pt_tex(xA, yA)}$ và $B{_pt_tex(xB, yB)}$ có phương trình là"
    )
    loigiai = (
        f"Trung điểm của đoạn thẳng $AB$ là $I{_pt_tex(xI, yI)}$.\n"
        f"Ta có $\\overrightarrow{{AB}} = {_vec_tex(dx, dy)}$. Đường trung trực của đoạn $AB$ đi qua $I$ và vuông góc với $AB$ nên nhận "
        f"$\\vec{{n}} = {_vec_tex(a, b)}$ làm vectơ pháp tuyến.\n"
        f"Phương trình đường trung trực là: "
        f"${a}({_sub_num_tex('x', xI)})"
        + (f" + {b}" if b > 0 else f" - {-b}")
        + f"({_sub_num_tex('y', yI)}) = 0 \\iff {_line_eq_tex(a, b, c)}$."
    )
    phuongan = _make_choices(ans, [d1, d2, d3, d4])
    return caudan, phuongan, loigiai


def K10_Oxy_MC_PTDT_DienTichTamGiac_HeSoGoc_TimDiem():
    """Đường thẳng qua A(0; y0) có hệ số góc k tạo tam giác diện tích S, hoặc tìm C thuộc Delta sao cho S_ABC = S0."""
    variant = random.choice([1, 2])
    if variant == 1:
        # Img 5 Câu 5: qua A(0; y0), hệ số góc k nguyên dương tạo với 2 trục tọa độ tam giác diện tích S
        y0 = random.choice([1, 2, 3, 4])
        k = random.choice([1, 2, 3, 4])
        # d: y = k x + y0 <=> k x - y + y0 = 0
        # Cắt Ox tại B(-y0/k; 0), Oy tại A(0; y0) => S = y0^2 / (2k)
        S_frac = Fraction(y0 * y0, 2 * k)
        S_str = str(float(S_frac)).replace(".", ",") if S_frac.denominator == 2 and S_frac.numerator == 1 else _frac_tex(S_frac)
        if S_frac == Fraction(1, 2):
            S_str = "0{,}5"
        else:
            S_str = _frac_tex(S_frac)

        ans = f"$d: {_line_eq_tex(k, -1, y0)}$."
        d1 = f"$d: {_line_eq_tex(1, -2 * k, 2 * k * y0)}$."
        d2 = f"$d: {_line_eq_tex(k, 1, -y0)}$."
        d3 = f"$d: {_line_eq_tex(1, -4 * k, 4 * k * y0)}$."
        d4 = f"$d: {_line_eq_tex(k + 1, -1, y0)}$."
        caudan = (
            f"Trong mặt phẳng $Oxy$, cho đường thẳng $d$ đi qua $A(0; {y0})$ có hệ số góc $k$ nguyên dương. "
            f"Viết phương trình đường thẳng $d$ biết $d$ tạo với hai trục tọa độ một tam giác có diện tích bằng ${S_str}$."
        )
        loigiai = (
            f"Đường thẳng $d$ đi qua $A(0; {y0})$ và có hệ số góc $k > 0$ ($k \\in \\mathbb{{Z}}$) có phương trình dạng $y = kx + {y0}$.\n"
            f"Giao điểm của $d$ với trục $Ox$ là $B\\left(-\\dfrac{{{y0}}}{{k}}; 0\\right)$.\n"
            f"Diện tích tam giác $OAB$ là $S = \\dfrac{{1}}{{2}} OA \\cdot OB = \\dfrac{{1}}{{2}} \\cdot {y0} \\cdot \\dfrac{{{y0}}}{{k}} = \\dfrac{{{y0 * y0}}}{{2k}}$.\n"
            f"Theo giả thiết $\\dfrac{{{y0 * y0}}}{{2k}} = {S_str} \\iff k = {k}$ (thỏa mãn $k \\in \\mathbb{{Z}}^+$).\n"
            f"Vậy $d: y = {_lin_tex(k, y0)} \\iff {_line_eq_tex(k, -1, y0)}$."
        )
        phuongan = _make_choices(ans, [d1, d2, d3, d4])
        return caudan, phuongan, loigiai

    # variant == 2 (Img 5 Câu 12): Tìm tọa độ điểm C trên Delta sao cho diện tích tam giác ABC bằng S0
    while True:
        xA, yA = random.randint(-2, 3), random.randint(-2, 3)
        vx = random.choice([-3, -2, -1, 1, 2, 3])
        vy = random.choice([-3, -2, -1, 1, 2, 3])
        xB, yB = xA + vx, yA + vy
        # Chọn C1 là điểm trên Delta dạng nguyên, Delta có hệ số a_d, b_d với a_d*u_x + b_d*u_y = 0
        # Đường thẳng Delta: x = x_base + p*t, y = y_base + q*t <=> q*x - p*y + c_d = 0
        p = random.choice([-2, -1, 1, 2])
        q = random.choice([-1, 1])
        # Vector AB = (vx, vy), nếu AB song song Delta thì S không đổi -> tránh vx*q - vy*p == 0
        det_dir = vx * q - vy * p
        if det_dir == 0:
            continue
        x_base = random.randint(-2, 2)
        y_base = random.randint(1, 5)
        t1 = random.choice([2, 3, 4])
        xC1, yC1 = x_base + p * t1, y_base + q * t1
        # Tính 2 * S = |vx*(yC1 - yA) - vy*(xC1 - xA)|
        cross1 = vx * (yC1 - yA) - vy * (xC1 - xA)
        if abs(cross1) < 4 or abs(cross1) % 2 != 0:
            continue
        S0 = abs(cross1) // 2
        # Nghiệm thứ 2: vx*(y_base + q*t - yA) - vy*(x_base + p*t - xA) = -cross1
        # Đặt cross(t) = C0 + D*t với D = vx*q - vy*p, C0 = vx*(y_base - yA) - vy*(x_base - xA)
        D = det_dir
        C0 = vx * (y_base - yA) - vy * (x_base - xA)
        # D * t2 = -cross1 - C0
        t2 = Fraction(-cross1 - C0, D)
        if t2 == t1:
            continue
        xC2 = x_base + p * t2
        yC2 = y_base + q * t2
        break

    a_d, b_d, c_d = _reduce_abc(q, -p, -(q * x_base - p * y_base))
    eq_delta = _line_eq_tex(a_d, b_d, c_d)

    c1_tex = _pt_tex(xC1, yC1)
    c2_tex = _pt_tex(xC2, yC2)
    ans = f"$C{c1_tex}$ và $C{c2_tex}$."
    d1 = f"$C{c1_tex}$."
    d2 = f"$C{_pt_tex(-xC1, yC1)}$."
    d3 = f"$C{c2_tex}$."
    d4 = f"$C{_pt_tex(xC1 + 1, yC1 - 1)}$."

    caudan = (
        f"Trong mặt phẳng $Oxy$, cho hai điểm $A{_pt_tex(xA, yA)}$, $B{_pt_tex(xB, yB)}$. "
        f"Tìm tọa độ điểm $C$ trên đường thẳng $\\Delta: {eq_delta}$ sao cho diện tích tam giác $ABC$ bằng ${S0}$."
    )
    # Độ dài AB = sqrt(vx^2 + vy^2), tính trực tiếp qua d(C, AB)
    # Phương trình AB: vy(x - xA) - vx(y - yA) = 0 <=> vy*x - vx*y + (vx*yA - vy*xA) = 0
    a_ab, b_ab, c_ab = vy, -vx, vx * yA - vy * xA
    ab_sq = vx * vx + vy * vy
    loigiai = (
        f"Ta có $\\overrightarrow{{AB}} = {_vec_tex(vx, vy)} \\Rightarrow AB = \\sqrt{{{ab_sq}}}$ và đường thẳng $AB$ có phương trình "
        f"${_line_eq_tex(*_reduce_abc(a_ab, b_ab, c_ab))}$.\n"
        f"Tham số hóa điểm $C \\in \\Delta$ theo biến $t$: $C\\left({_param_row(x_base, p)};\\, {_param_row(y_base, q)}\\right)$.\n"
        f"Diện tích tam giác $ABC$ là $S_{{\\triangle ABC}} = \\dfrac{{1}}{{2}} AB \\cdot d(C, AB) = \\dfrac{{1}}{{2}} |{_lin_tex(D, C0, 't')}| = {S0}$.\n"
        f"Giải phương trình $|{_lin_tex(D, C0, 't')}| = {2 * S0}$, ta được $t = {t1}$ hoặc $t = {_frac_tex(t2)}$.\n"
        f"Vậy có hai điểm thỏa mãn là $C{c1_tex}$ và $C{c2_tex}$."
    )
    phuongan = _make_choices(ans, [d1, d2, d3, d4])
    return caudan, phuongan, loigiai


# ==============================================================================
# BÀI 20: VỊ TRÍ TƯƠNG ĐỐI, GÓC VÀ KHOẢNG CÁCH (NÂNG CẤP & MỚI)
# ==============================================================================

def K10_Oxy_MC_VTTD_HaiDuongThang():
    """Xét vị trí tương đối giữa hai đường thẳng (cắt không vuông, vuông góc, song song, trùng)."""
    case = random.choice(["song_song", "trung_nhau", "vuong_goc", "cat_khong_vuong"])
    while True:
        a1 = random.choice([-7, -5, -4, -3, -2, 2, 3, 4, 5, 7, 11])
        b1 = random.choice([-7, -5, -4, -3, -2, 2, 3, 4, 5, 7, 12])
        if math.gcd(abs(a1), abs(b1)) == 1 and abs(a1) != abs(b1):
            break
    c1 = random.choice([-5, -3, -2, -1, 1, 2, 3, 5])

    if case == "song_song":
        k = random.choice([-2, 2, 3])
        a2, b2 = k * a1, k * b1
        c2 = k * c1 + random.choice([-3, -2, 2, 3])
        ans = "$d_1 \\parallel d_2$."
        why = (
            f"Ta có $\\dfrac{{{a1}}}{{{a2}}} = \\dfrac{{{b1}}}{{{b2}}} \\ne \\dfrac{{{c1}}}{{{c2}}}$ "
            f"nên hai đường thẳng $d_1$ và $d_2$ song song với nhau."
        )
    elif case == "trung_nhau":
        k = random.choice([-3, -2, 2, 3])
        a2, b2, c2 = k * a1, k * b1, k * c1
        ans = "$d_1 \\equiv d_2$."
        why = (
            f"Ta có $\\dfrac{{{a1}}}{{{a2}}} = \\dfrac{{{b1}}}{{{b2}}} = \\dfrac{{{c1}}}{{{c2}}}$ "
            f"nên hai đường thẳng $d_1$ và $d_2$ trùng nhau."
        )
    elif case == "vuong_goc":
        # a2 = -b1, b2 = a1 (hoặc đổi dấu)
        if random.choice([True, False]):
            a2, b2 = -b1, a1
        else:
            a2, b2 = b1, -a1
        c2 = random.choice([-9, -4, -1, 1, 4, 9])
        ans = "$d_1 \\perp d_2$."
        why = (
            f"Đường thẳng $d_1$ có VTPT $\\vec{{n}}_1 = ({a1}; {b1})$ và $d_2$ có VTPT $\\vec{{n}}_2 = ({a2}; {b2})$.\n"
            f"Ta có $\\vec{{n}}_1 \\cdot \\vec{{n}}_2 = ({a1})({a2}) + ({b1})({b2}) = 0$, suy ra $d_1 \\perp d_2$."
        )
    else:
        while True:
            a2 = random.choice([-5, -3, -2, 1, 2, 3, 5])
            b2 = random.choice([-5, -3, -2, 1, 2, 3, 5])
            if a1 * b2 - a2 * b1 != 0 and a1 * a2 + b1 * b2 != 0:
                break
        c2 = random.choice([-5, -2, 1, 3, 4])
        ans = "$d_1$ cắt $d_2$ nhưng không vuông góc."
        why = (
            f"Ta có $a_1 b_2 - a_2 b_1 = ({a1})({b2}) - ({a2})({b1}) = {a1 * b2 - a2 * b1} \\ne 0$ nên $d_1$ cắt $d_2$.\n"
            f"Hơn nữa $\\vec{{n}}_1 \\cdot \\vec{{n}}_2 = ({a1})({a2}) + ({b1})({b2}) = {a1 * a2 + b1 * b2} \\ne 0$ nên $d_1$ và $d_2$ không vuông góc."
        )

    caudan = (
        f"Cho hai đường thẳng $d_1: {_line_eq_tex(a1, b1, c1)}$ và $d_2: {_line_eq_tex(a2, b2, c2)}$. "
        f"Xét vị trí tương đối giữa $d_1$ và $d_2$."
    )
    all_choices = [
        "$d_1 \\parallel d_2$.",
        "$d_1 \\equiv d_2$.",
        "$d_1$ cắt $d_2$ nhưng không vuông góc.",
        "$d_1 \\perp d_2$.",
    ]
    phuongan = _make_choices(ans, all_choices)
    return caudan, phuongan, why


def K10_Oxy_MC_VTTD_ToaDoGiaoDiem():
    """Tìm tọa độ giao điểm của hai đường thẳng."""
    x0 = random.randint(-4, 4)
    y0 = random.randint(-4, 4)
    while True:
        a1, b1 = random.choice([-3, -2, -1, 1, 2, 3]), random.choice([-3, -2, -1, 1, 2, 3])
        a2, b2 = random.choice([-3, -2, -1, 1, 2, 3]), random.choice([-3, -2, -1, 1, 2, 3])
        if a1 * b2 - a2 * b1 != 0 and (a1, b1) != (a2, b2):
            break
    c1 = -(a1 * x0 + b1 * y0)
    c2 = -(a2 * x0 + b2 * y0)

    ans = f"${_pt_tex(x0, y0)}$."
    d1 = f"${_pt_tex(y0, x0)}$." if x0 != y0 else f"${_pt_tex(x0 + 1, y0)}$."
    d2 = f"${_pt_tex(-x0, -y0)}$." if (x0, y0) != (0, 0) else f"${_pt_tex(0, 1)}$."
    d3 = f"${_pt_tex(x0 + 1, y0 - 1)}$."
    d4 = f"${_pt_tex(x0 - 1, y0 + 2)}$."

    use_ptts = random.choice([True, False])
    if use_ptts:
        # d1 PTTQ, d2 PTTS qua (x0, y0) nhưng biểu diễn qua điểm lệch k bước t
        u1, u2 = -b2, a2
        t_shift = random.choice([-2, -1, 1, 2])
        x_s, y_s = x0 - u1 * t_shift, y0 - u2 * t_shift
        caudan = (
            f"Tìm tọa độ giao điểm của hai đường thẳng $d_1: {_line_eq_tex(a1, b1, c1)}$ "
            f"và $d_2: {_ptts_tex(x_s, y_s, u1, u2)}$."
        )
        coef_t = a1 * u1 + b1 * u2
        const_t = a1 * x_s + b1 * y_s + c1
        loigiai = (
            f"Thay phương trình tham số của $d_2$ vào phương trình $d_1$, ta có:\n"
            f"${a1}({_param_row(x_s, u1)})"
            + (f" + {b1}" if b1 > 0 else f" - {-b1}")
            + f"({_param_row(y_s, u2)})"
            + f"{_signed_frac_term(c1)} = 0 \\iff {_lin_tex(coef_t, const_t, 't')} = 0 \\iff t = {t_shift}$.\n"
            f"Thay $t = {t_shift}$ vào phương trình $d_2$, ta được giao điểm là ${_pt_tex(x0, y0)}$."
        )
    else:
        caudan = (
            f"Tìm tọa độ giao điểm của hai đường thẳng $d_1: {_line_eq_tex(a1, b1, c1)}$ "
            f"và $d_2: {_line_eq_tex(a2, b2, c2)}$."
        )
        loigiai = (
            f"Tọa độ giao điểm của $d_1$ và $d_2$ là nghiệm của hệ phương trình:\n"
            f"$$\\begin{{cases}} {_line_eq_tex(a1, b1, c1)} \\\\ {_line_eq_tex(a2, b2, c2)} \\end{{cases}} "
            f"\\iff \\begin{{cases}} x = {x0} \\\\ y = {y0} \\end{{cases}}.$$\n"
            f"Vậy giao điểm là ${_pt_tex(x0, y0)}$."
        )
    phuongan = _make_choices(ans, [d1, d2, d3, d4])
    return caudan, phuongan, loigiai


def K10_Oxy_MC_VTTD_ThamSoM_CatNhau_SongSong_TrungNhau():
    """Tìm tham số m để hai đường thẳng song song hoặc vuông góc hoặc trùng nhau."""
    mode = random.choice(["song_song", "vuong_goc"])
    if mode == "song_song":
        # d1: m x + a1 y + c1 = 0; d2: a2 x + m y + c2 = 0 với a1*a2 = k^2
        k = random.choice([2, 3, 4])
        # Chọn a1, a2 dương cùng tích k^2
        pairs = [(1, k * k), (k, k)]
        a1, a2 = random.choice(pairs)
        if random.choice([True, False]):
            a1, a2 = -a1, -a2
        # Để d1 // d2 khi m = k hoặc m = -k, đặt c1, c2 sao cho một giá trị bị trùng nhau và chỉ còn 1 giá trị!
        m_valid = random.choice([k, -k])
        # Với m = -m_valid: muốn trùng nhau => (-m_valid)/a2 = c1/c2
        # Đặt c1 = -m_valid, c2 = a2 => tại m = -m_valid thì (-m_valid)/a2 == c1/c2 (trùng), tại m = m_valid thì m_valid/a2 != c1/c2 (song song)
        c1 = -m_valid
        c2 = a2
        # Kiểm tra c1/c2 = -m_valid/a2 != m_valid/a2 vì m_valid != 0
        ans = f"$m = {m_valid}$."
        d1 = f"$m = {-m_valid}$."
        d2 = f"$m = \\pm {k}$."
        d3 = f"$m = 0$."
        d4 = f"$m = {k + 1}$."
        caudan = (
            f"Tìm giá trị của tham số $m$ để hai đường thẳng "
            f"$d_1: mx{_signed_frac_term(a1, 'y')}{_signed_frac_term(c1)} = 0$ và "
            f"$d_2: {_lin_tex(a2, 0, 'x')} + my{_signed_frac_term(c2)} = 0$ song song với nhau."
        )
        loigiai = (
            f"Hai đường thẳng $d_1$ và $d_2$ song song khi $\\dfrac{{m}}{{{a2}}} = \\dfrac{{{a1}}}{{m}} \\ne \\dfrac{{{c1}}}{{{c2}}}$.\n"
            f"Từ $\\dfrac{{m}}{{{a2}}} = \\dfrac{{{a1}}}{{m}} \\iff m^2 = {k * k} \\iff m = {k}$ hoặc $m = -{k}$.\n"
            f"Thử lại:\n"
            f"- Với $m = {-m_valid}$, ta có $\\dfrac{{{ -m_valid }}}{{{a2}}} = \\dfrac{{{c1}}}{{{c2}}}$ nên $d_1 \\equiv d_2$ (loại).\n"
            f"- Với $m = {m_valid}$, ta có $\\dfrac{{{m_valid}}}{{{a2}}} \\ne \\dfrac{{{c1}}}{{{c2}}}$ nên $d_1 \\parallel d_2$ (thỏa mãn).\n"
            f"Vậy $m = {m_valid}$."
        )
        phuongan = _make_choices(ans, [d1, d2, d3, d4])
        return caudan, phuongan, loigiai

    # mode == "vuong_goc"
    m_ans = random.choice([-3, -2, -1, 1, 2, 3, 4])
    a1 = random.choice([1, 2, 3])
    b1 = random.choice([-3, -2, -1, 1, 2, 3])
    # n1 = (a1, b1), n2 = (m, b2) -> a1*m + b1*b2 = 0 => b2*b1 = -a1*m_ans
    # Chọn d1: (m + k1)x + b1 y + c1 = 0, d2: a2 x + b2 y + c2 = 0
    a2 = random.choice([1, 2, 3])
    b2 = random.choice([-3, -2, 2, 3])
    # Đặt d1 có hệ số x là m + s, với a2*(m + s) + b1*b2 = 0 => m_ans + s = -b1*b2/a2
    # Để nguyên: chọn b1 = a2 * t_val => -(t_val * b2) = m_ans + s
    t_val = random.choice([-2, -1, 1, 2])
    b1 = a2 * t_val
    c_target = -(t_val * b2)  # giá trị của (m + s)
    s = c_target - m_ans
    c1 = random.choice([-3, -1, 2, 4])
    c2 = random.choice([-4, -2, 1, 3])
    coef_x_str = "m" if s == 0 else f"(m{_signed_frac_term(s)})"
    ans = f"$m = {m_ans}$."
    d1 = f"$m = {-m_ans}$." if m_ans != 0 else "$m = 1$."
    d2 = f"$m = {m_ans + 2}$."
    d3 = f"$m = {m_ans - 1}$."
    d4 = f"$m = {m_ans + 3}$."
    d5 = f"$m = {m_ans - 2}$."
    caudan = (
        f"Tìm giá trị của tham số $m$ để hai đường thẳng "
        f"$d_1: {coef_x_str}x{_signed_frac_term(b1, 'y')}{_signed_frac_term(c1)} = 0$ và "
        f"$d_2: {_line_eq_tex(a2, b2, c2)}$ vuông góc với nhau."
    )
    loigiai = (
        f"Vectơ pháp tuyến của $d_1, d_2$ lần lượt là $\\vec{{n}}_1 = ({_lin_tex(1, s, 'm')}; {b1})$ và $\\vec{{n}}_2 = ({a2}; {b2})$.\n"
        f"Ta có $d_1 \\perp d_2 \\iff \\vec{{n}}_1 \\cdot \\vec{{n}}_2 = 0 \\iff {a2}{coef_x_str} + ({b1})({b2}) = 0 \\iff m = {m_ans}$."
    )
    phuongan = _make_choices(ans, [d1, d2, d3, d4, d5])
    return caudan, phuongan, loigiai


def K10_Oxy_MC_VTTD_BaDuongThangDongQuy():
    """Tìm m để ba đường thẳng đồng quy."""
    while True:
        x0 = random.choice([-2, -1, 1, 2, 3])
        y0 = random.choice([-2, -1, 1, 2, 3])
        a1, b1 = random.choice([1, 2]), random.choice([-2, -1, 1, 2])
        a2, b2 = random.choice([-2, 1, 3]), random.choice([-1, 1, 2])
        if a1 * b2 - a2 * b1 != 0:
            break
    c1 = -(a1 * x0 + b1 * y0)
    c2 = -(a2 * x0 + b2 * y0)

    # d3: m x + b3 y + c3 = 0 qua (x0, y0) => m = -(b3*y0 + c3)/x0
    m_ans = random.choice([-4, -3, -2, -1, 1, 2, 3, 4])
    b3 = random.choice([-3, -2, -1, 1, 2, 3])
    c3 = -(m_ans * x0 + b3 * y0)

    ans = f"$m = {m_ans}$."
    d1 = f"$m = {-m_ans}$."
    d2 = f"$m = {m_ans + 2}$."
    d3 = f"$m = {m_ans - 1}$."
    d4 = f"$m = {m_ans + 3}$."
    caudan = (
        f"Tìm tất cả các giá trị của tham số $m$ để ba đường thẳng "
        f"$d_1: {_line_eq_tex(a1, b1, c1)}$, $d_2: {_line_eq_tex(a2, b2, c2)}$ và "
        f"$d_3: mx{_signed_frac_term(b3, 'y')}{_signed_frac_term(c3)} = 0$ đồng quy."
    )
    loigiai = (
        f"Tọa độ giao điểm $I$ của $d_1$ và $d_2$ là nghiệm của hệ:\n"
        f"$$\\begin{{cases}} {_line_eq_tex(a1, b1, c1)} \\\\ {_line_eq_tex(a2, b2, c2)} \\end{{cases}} \\Rightarrow I{_pt_tex(x0, y0)}.$$\n"
        f"Để ba đường thẳng đồng quy thì $I \\in d_3 \\iff m \\cdot ({x0}) + ({b3}) \\cdot ({y0}) + ({c3}) = 0 \\iff m = {m_ans}$."
    )
    phuongan = _make_choices(ans, [d1, d2, d3, d4])
    return caudan, phuongan, loigiai


def K10_Oxy_MC_Goc_GiuaHaiDuongThang():
    """Tính cosin góc hoặc số đo góc giữa hai đường thẳng."""
    variant = random.choice([1, 1, 2])
    if variant == 1:
        # Tính cos(d1, d2) -> dạng PTTQ+PTTQ hoặc PTTQ+PTTS
        while True:
            a1 = random.choice([-4, -3, -2, -1, 1, 2, 3, 5, 10])
            b1 = random.choice([-4, -3, -2, -1, 1, 2, 3, 5])
            a2 = random.choice([-3, -2, -1, 1, 2, 3])
            b2 = random.choice([-3, -2, -1, 1, 2, 3])
            dot = abs(a1 * a2 + b1 * b2)
            cross = abs(a1 * b2 - a2 * b1)
            if dot > 0 and cross > 0 and math.gcd(abs(a1), abs(b1)) == 1:
                break
        c1 = random.choice([-3, -2, -1, 0, 1, 2])
        c2 = random.choice([-2, -1, 0, 1, 2])
        n1_sq = a1 * a1 + b1 * b1
        n2_sq = a2 * a2 + b2 * b2
        den_sq = n1_sq * n2_sq
        cos_tex = _rat_sqrt_tex(dot, den_sq)
        ans = f"${cos_tex}$."

        # Nhiễu hợp lý
        k_r, r_r = _simplify_sqrt(den_sq)
        cands = [
            f"${_rat_sqrt_tex(dot + 1, den_sq)}$." if dot + 1 < k_r else f"${_rat_sqrt_tex(max(1, dot - 1), den_sq)}$.",
            f"${_rat_sqrt_tex(dot, den_sq + 2)}$." if den_sq + 2 != den_sq else f"${_rat_sqrt_tex(dot, den_sq + 3)}$.",
            f"${_frac_tex(Fraction(dot, max(2, k_r * r_r)))}$." if r_r > 1 else f"${_frac_tex(Fraction(dot + 1, k_r + 1))}$.",
            f"${_sqrt_tex(r_r)}$." if r_r > 1 else f"${_frac_tex(Fraction(1, 2))}$.",
            f"${_rat_sqrt_tex(abs(a1 * b2 - a2 * b1), den_sq)}$.",
        ]

        use_ptts = random.choice([True, False])
        if use_ptts:
            # Cho d2 dưới dạng PTTS nhận VTCP u2 = (-b2, a2) -> VTPT n2 = (a2, b2)
            u1_2, u2_2 = -b2, a2
            x2_0, y2_0 = random.randint(0, 3), random.randint(-2, 2)
            caudan = (
                f"Cho đường thẳng $d_1: {_line_eq_tex(a1, b1, c1)}$ và "
                f"$d_2: {_ptts_tex(x2_0, y2_0, u1_2, u2_2)}$. "
                f"Tính côsin của góc tạo bởi giữa hai đường thẳng đã cho."
            )
            loigiai = (
                f"Đường thẳng $d_1$ có VTPT $\\vec{{n}}_1 = ({a1}; {b1})$.\n"
                f"Đường thẳng $d_2$ có VTCP $\\vec{{u}}_2 = ({u1_2}; {u2_2})$ nên có một VTPT là $\\vec{{n}}_2 = ({a2}; {b2})$.\n"
                f"Côsin góc giữa hai đường thẳng là:\n"
                f"$$\\cos(d_1, d_2) = \\dfrac{{|\\vec{{n}}_1 \\cdot \\vec{{n}}_2|}}{{|\\vec{{n}}_1| \\cdot |\\vec{{n}}_2|}} "
                f"= \\dfrac{{|({a1})({a2}) + ({b1})({b2})|}}{{\\sqrt{{{n1_sq}}} \\cdot \\sqrt{{{n2_sq}}}}} "
                f"= \\dfrac{{{dot}}}{{\\sqrt{{{den_sq}}}}} = {cos_tex}.$$"
            )
        else:
            caudan = (
                f"Cho hai đường thẳng $d_1: {_line_eq_tex(a1, b1, c1)}$ và $d_2: {_line_eq_tex(a2, b2, c2)}$. "
                f"Tính côsin của góc tạo bởi hai đường thẳng đã cho."
            )
            loigiai = (
                f"Đường thẳng $d_1$ có VTPT $\\vec{{n}}_1 = ({a1}; {b1})$ và $d_2$ có VTPT $\\vec{{n}}_2 = ({a2}; {b2})$.\n"
                f"Ta có:\n"
                f"$$\\cos(d_1, d_2) = \\dfrac{{|({a1})({a2}) + ({b1})({b2})|}}{{\\sqrt{{{a1}^2 + {b1}^2}} \\cdot \\sqrt{{{a2}^2 + {b2}^2}}}} "
                f"= \\dfrac{{{dot}}}{{\\sqrt{{{den_sq}}}}} = {cos_tex}.$$"
            )
        phuongan = _make_choices(ans, cands)
        return caudan, phuongan, loigiai

    # variant == 2 (Img 5 Câu 3): Góc đặc biệt 30, 45, 60, 90
    angle_type = random.choice([45, 90, 30, 60])
    c1 = random.choice([-3, -2, -1, 1, 2, 3])
    c2 = random.choice([-3, -2, -1, 1, 2, 3])
    if angle_type == 45:
        a = random.choice([-3, -2, -1, 1, 2, 3])
        b = random.choice([-2, -1, 1, 2])
        while a == b or a == -b:
            a = random.choice([-3, -2, 1, 2, 3])
        a1, b1 = a, b
        a2, b2 = a - b, a + b
        eq1 = _line_eq_tex(a1, b1, c1)
        eq2 = _line_eq_tex(a2, b2, c2)
        dot = abs(a1 * a2 + b1 * b2)
        n1_sq = a1 * a1 + b1 * b1
        n2_sq = a2 * a2 + b2 * b2
        ans = "$45^\\circ$."
        loigiai = (
            f"Ta có $\\vec{{n}}_1 = ({a1}; {b1})$ và $\\vec{{n}}_2 = ({a2}; {b2})$.\n"
            f"$\\cos(d_1, d_2) = \\dfrac{{|{dot}|}}{{\\sqrt{{{n1_sq}}} \\cdot \\sqrt{{{n2_sq}}}}} = \\dfrac{{\\sqrt{{2}}}}{{2}} \\Rightarrow (d_1, d_2) = 45^\\circ$."
        )
    elif angle_type == 90:
        a1 = random.choice([-4, -3, -2, 2, 3, 4])
        b1 = random.choice([-3, -2, -1, 1, 2, 3])
        a2, b2 = -b1, a1
        eq1 = _line_eq_tex(a1, b1, c1)
        eq2 = _line_eq_tex(a2, b2, c2)
        ans = "$90^\\circ$."
        loigiai = (
            f"Ta có $\\vec{{n}}_1 = ({a1}; {b1})$ và $\\vec{{n}}_2 = ({a2}; {b2})$.\n"
            f"Vì $\\vec{{n}}_1 \\cdot \\vec{{n}}_2 = ({a1})({a2}) + ({b1})({b2}) = 0$ nên $d_1 \\perp d_2$, suy ra $(d_1, d_2) = 90^\\circ$."
        )
    elif angle_type == 30:
        # d1: sqrt(3)x - y + c1 = 0, d2: x + c2 = 0 (hoặc y + c2 = 0 cho 60)
        if random.choice([True, False]):
            eq1 = f"\\sqrt{{3}}x - y{_signed_frac_term(c1)} = 0"
            eq2 = f"x{_signed_frac_term(c2)} = 0"
            n_desc = "$\\vec{n}_1 = (\\sqrt{3}; -1)$ và $\\vec{n}_2 = (1; 0)$"
        else:
            eq1 = f"x - \\sqrt{{3}}y{_signed_frac_term(c1)} = 0"
            eq2 = f"y{_signed_frac_term(c2)} = 0"
            n_desc = "$\\vec{n}_1 = (1; -\\sqrt{3})$ và $\\vec{n}_2 = (0; 1)$"
        ans = "$30^\\circ$."
        loigiai = (
            f"Ta có {n_desc}.\n"
            f"Suy ra $\\cos(d_1, d_2) = \\dfrac{{|\\vec{{n}}_1 \\cdot \\vec{{n}}_2|}}{{|\\vec{{n}}_1|\\cdot|\\vec{{n}}_2|}} = \\dfrac{{\\sqrt{{3}}}}{{2}} \\Rightarrow (d_1, d_2) = 30^\\circ$."
        )
    else:
        if random.choice([True, False]):
            eq1 = f"\\sqrt{{3}}x - y{_signed_frac_term(c1)} = 0"
            eq2 = f"y{_signed_frac_term(c2)} = 0"
            n_desc = "$\\vec{n}_1 = (\\sqrt{3}; -1)$ và $\\vec{n}_2 = (0; 1)$"
        else:
            eq1 = f"x + \\sqrt{{3}}y{_signed_frac_term(c1)} = 0"
            eq2 = f"x{_signed_frac_term(c2)} = 0"
            n_desc = "$\\vec{n}_1 = (1; \\sqrt{3})$ và $\\vec{n}_2 = (1; 0)$"
        ans = "$60^\\circ$."
        loigiai = (
            f"Ta có {n_desc}.\n"
            f"Suy ra $\\cos(d_1, d_2) = \\dfrac{{|\\vec{{n}}_1 \\cdot \\vec{{n}}_2|}}{{|\\vec{{n}}_1|\\cdot|\\vec{{n}}_2|}} = \\dfrac{{1}}{{2}} \\Rightarrow (d_1, d_2) = 60^\\circ$."
        )

    caudan = f"Tính góc giữa hai đường thẳng $d_1: {eq1}$ và $d_2: {eq2}$."
    phuongan = _make_choices(ans, ["$30^\\circ$.", "$45^\\circ$.", "$60^\\circ$.", "$90^\\circ$."])
    return caudan, phuongan, loigiai


def K10_Oxy_MC_KhoangCach_Diem_Den_DuongThang():
    """Tính khoảng cách từ điểm M đến đường thẳng cho dưới dạng PTTQ hoặc PTTS."""
    mode = random.choice(["ptts", "pttq"])
    if mode == "ptts":
        # Img 3 Câu 10 & Img 5 Câu 11
        u_pair = random.choice([(3, 4), (4, -3), (5, 12), (1, 2), (2, -1), (1, 3)])
        u1, u2 = u_pair
        # VTPT n = (a, b) = (u2, -u1)
        a, b = u2, -u1
        x1 = random.randint(-2, 3)
        y1 = random.randint(-2, 3)
        c = -(a * x1 + b * y1)
        while True:
            x0 = random.randint(-3, 4)
            y0 = random.randint(-3, 4)
            num = abs(a * x0 + b * y0 + c)
            if num > 0:
                break
        den_sq = a * a + b * b
        dist_tex = _rat_sqrt_tex(num, den_sq)
        ans = f"${dist_tex}$."
        d1 = f"${_rat_sqrt_tex(num + 1, den_sq)}$."
        d2 = f"${_frac_tex(Fraction(num, a * a + b * b))}$."
        d3 = f"${_rat_sqrt_tex(num, den_sq + 3)}$."
        d4 = f"${_rat_sqrt_tex(max(1, num - 1), den_sq)}$."

        caudan = (
            f"Khoảng cách từ điểm $M{_pt_tex(x0, y0)}$ đến đường thẳng "
            f"$\\Delta: {_ptts_tex(x1, y1, u1, u2)}$ bằng"
        )
        loigiai = (
            f"Đường thẳng $\\Delta$ đi qua $A{_pt_tex(x1, y1)}$ và có vectơ chỉ phương $\\vec{{u}} = ({u1}; {u2})$ "
            f"nên có vectơ pháp tuyến $\\vec{{n}} = ({a}; {b})$.\n"
            f"Phương trình tổng quát của $\\Delta$ là: "
            f"${a}({_sub_num_tex('x', x1)})"
            + (f" + {b}" if b > 0 else f" - {-b}")
            + f"({_sub_num_tex('y', y1)}) = 0 \\iff {_line_eq_tex(a, b, c)}$.\n"
            f"Khoảng cách từ điểm $M{_pt_tex(x0, y0)}$ đến $\\Delta$ là:\n"
            f"$$d(M, \\Delta) = \\dfrac{{|{a}\\cdot({x0}) + ({b})\\cdot({y0}) + ({c})|}}{{\\sqrt{{{a}^2 + ({b})^2}}}} "
            f"= \\dfrac{{{num}}}{{\\sqrt{{{den_sq}}}}} = {dist_tex}.$$"
        )
        phuongan = _make_choices(ans, [d1, d2, d3, d4])
        return caudan, phuongan, loigiai

    # mode == "pttq"
    a, b = random.choice([(3, -4), (4, 3), (5, -12), (1, -2), (2, 3), (1, -1)])
    c = random.choice([-6, -4, -3, -1, 1, 2, 5, 7])
    while True:
        x0 = random.randint(-3, 4)
        y0 = random.randint(-3, 4)
        num = abs(a * x0 + b * y0 + c)
        if num > 0:
            break
    den_sq = a * a + b * b
    dist_tex = _rat_sqrt_tex(num, den_sq)
    ans = f"${dist_tex}$."
    d1 = f"${_rat_sqrt_tex(num + 2, den_sq)}$."
    d2 = f"${_frac_tex(Fraction(num, den_sq))}$."
    d3 = f"${_rat_sqrt_tex(max(1, num - 1), den_sq)}$."
    d4 = f"${_rat_sqrt_tex(num, den_sq + 4)}$."

    caudan = (
        f"Trong mặt phẳng $Oxy$, khoảng cách từ điểm $M{_pt_tex(x0, y0)}$ "
        f"đến đường thẳng $\\Delta: {_line_eq_tex(a, b, c)}$ bằng"
    )
    loigiai = (
        f"Áp dụng công thức khoảng cách từ điểm $M{_pt_tex(x0, y0)}$ đến $\\Delta: {_line_eq_tex(a, b, c)}$:\n"
        f"$$d(M, \\Delta) = \\dfrac{{|{a}\\cdot({x0}) + ({b})\\cdot({y0}) + ({c})|}}{{\\sqrt{{{a}^2 + ({b})^2}}}} "
        f"= \\dfrac{{{num}}}{{\\sqrt{{{den_sq}}}}} = {dist_tex}.$$"
    )
    phuongan = _make_choices(ans, [d1, d2, d3, d4])
    return caudan, phuongan, loigiai


# ==============================================================================
# BÀI 21: PHƯƠNG TRÌNH ĐƯỜNG TRÒN (NÂNG CẤP & MỚI)
# ==============================================================================

def K10_Oxy_MC_DuongTron_NhanDang_DieuKien():
    """Nhận dạng phương trình đường tròn hoặc tìm m để phương trình là đường tròn."""
    variant = random.choice([1, 2])
    if variant == 1:
        # Img 2 Câu 7, Img 5 Câu 1: Trong các PT sau, PT nào là PT đường tròn?
        a_ok = random.choice([-3, -2, -1, 1, 2, 3])
        b_ok = random.choice([-3, -2, -1, 1, 2, 3])
        R_sq = random.choice([4, 5, 8, 9, 10])
        D_ok, E_ok, F_ok = -2 * a_ok, -2 * b_ok, a_ok * a_ok + b_ok * b_ok - R_sq
        eq_ok = f"${_circle_gen_tex(D_ok, E_ok, F_ok)}$."

        # Tạo 3 phương trình sai chuẩn khác nhau hoàn toàn: a^2 + b^2 - F <= 0
        wrong_eqs = []
        seen_w = {eq_ok}
        while len(wrong_eqs) < 3:
            aw = random.choice([-3, -2, -1, 1, 2, 3])
            bw = random.choice([-3, -2, -1, 1, 2, 3])
            extra = random.choice([0, 1, 2, 3, 5])
            Fw = aw * aw + bw * bw + extra
            cand = f"${_circle_gen_tex(-2 * aw, -2 * bw, Fw)}$."
            if len(wrong_eqs) == 2 and random.choice([True, False]):
                Dw = random.choice([-3, -1, 1, 3])
                Ew = random.choice([-3, -1, 1, 3])
                Fw = (Dw * Dw + Ew * Ew) // 4 + random.choice([2, 3, 4])
                cand = f"${_circle_gen_tex(Dw, Ew, Fw)}$."
            if cand not in seen_w:
                seen_w.add(cand)
                wrong_eqs.append(cand)

        caudan = "Trong các phương trình sau, phương trình nào là phương trình đường tròn?"
        loigiai = (
            f"Phương trình dạng $x^2 + y^2 - 2ax - 2by + c = 0$ là phương trình đường tròn khi và chỉ khi $a^2 + b^2 - c > 0$.\n"
            f"Xét phương trình ${_circle_gen_tex(D_ok, E_ok, F_ok)}$, ta có $a = {a_ok}, b = {b_ok}, c = {F_ok}$.\n"
            f"Khi đó $a^2 + b^2 - c = ({a_ok})^2 + ({b_ok})^2 - ({F_ok}) = {R_sq} > 0$.\n"
            f"Các phương trình còn lại đều có $a^2 + b^2 - c \\le 0$ nên không phải phương trình đường tròn."
        )
        phuongan = _make_choices(eq_ok, wrong_eqs)
        return caudan, phuongan, loigiai

    # variant == 2: Tìm m để x^2 + y^2 - 2mx - 2by + k*m + c0 = 0 hoặc tương tự là PT đường tròn
    r1 = random.randint(-3, 1)
    r2 = r1 + random.randint(2, 5)
    # a^2 + b^2 - c > 0 <=> m^2 - (r1+r2)m + r1*r2 > 0
    # Đặt a = m, b = b0 => m^2 + b0^2 - c > 0 => c = (r1+r2)m + (b0^2 - r1*r2)
    b0 = random.choice([-2, -1, 1, 2])
    p_coef = r1 + r2
    q_const = b0 * b0 - r1 * r2
    # phương trình: x^2 + y^2 - 2mx - 2*b0*y + (p_coef*m + q_const) = 0
    rhs_m = _lin_tex(p_coef, q_const, "m")
    D_str = "- 2mx"
    E_str = _signed_frac_term(-2 * b0, "y")
    eq_str = f"x^2 + y^2 {D_str}{E_str}{_signed_frac_term(p_coef, 'm')}{_signed_frac_term(q_const)} = 0"

    ans = f"$m < {r1}$ hoặc $m > {r2}$."
    d1 = f"${r1} < m < {r2}$."
    d2 = f"$m \\le {r1}$ hoặc $m \\ge {r2}$."
    d3 = f"${r1} \\le m \\le {r2}$."
    d4 = f"$m > {r2}$."
    caudan = f"Tìm tất cả các giá trị của tham số $m$ để phương trình ${eq_str}$ là phương trình đường tròn."
    loigiai = (
        f"Ta có $a = m$, $b = {b0}$, $c = {rhs_m}$.\n"
        f"Điều kiện để phương trình là phương trình đường tròn là $a^2 + b^2 - c > 0$:\n"
        f"$$m^2 + ({b0})^2 - ({rhs_m}) > 0 \\iff m^2{_signed_frac_term(-p_coef, 'm')}{_signed_frac_term(r1 * r2)} > 0 \\iff m < {r1} \\text{{ hoặc }} m > {r2}.$$"
    )
    phuongan = _make_choices(ans, [d1, d2, d3, d4])
    return caudan, phuongan, loigiai


def K10_Oxy_MC_DuongTron_Tam_Va_BanKinh():
    """Xác định tâm, bán kính, đường kính hoặc dạng chính tắc của đường tròn."""
    variant = random.choice([1, 2, 3])
    while True:
        a = random.choice([-5, -4, -3, -2, -1, 1, 2, 3, 4, 5])
        b = random.choice([-5, -4, -3, -2, -1, 1, 2, 3, 4, 5])
        if abs(a) != abs(b):
            break
    R = random.choice([2, 3, 4, 5, 6])
    R2 = R * R
    D, E, F = -2 * a, -2 * b, a * a + b * b - R2
    gen_eq = _circle_gen_tex(D, E, F)
    std_eq = _circle_std_tex(a, b, R2)

    if variant == 1:
        # Img 2 Câu 9: Xác định tâm I và bán kính R
        ans = f"$I{_pt_tex(a, b)}$, $R = {R}$."
        d1 = f"$I{_pt_tex(-a, -b)}$, $R = {R}$."
        d2 = f"$I{_pt_tex(a, b)}$, $R = {R2}$."
        d3 = f"$I{_pt_tex(-a, -b)}$, $R = {R2}$."
        d4 = f"$I{_pt_tex(D, E)}$, $R = {R}$."
        caudan = f"Cho đường tròn $(C): {gen_eq}$. Hãy xác định tâm $I$ và bán kính $R$ của đường tròn $(C)$."
        loigiai = (
            f"Đường tròn $(C)$ có $a = -\\dfrac{{{D}}}{{2}} = {a}$, $b = -\\dfrac{{{E}}}{{2}} = {b}$, $c = {F}$.\n"
            f"Vậy $(C)$ có tâm $I{_pt_tex(a, b)}$ và bán kính $R = \\sqrt{{{a}^2 + ({b})^2 - ({F})}} = \\sqrt{{{R2}}} = {R}$."
        )
        phuongan = _make_choices(ans, [d1, d2, d3, d4])
        return caudan, phuongan, loigiai

    if variant == 2:
        # Img 3 Câu 5: Đường kính của đường tròn (C)
        diam = 2 * R
        ans = f"${diam}$."
        d1 = f"${R}$."
        d2 = f"${R2}$."
        d3 = f"${2 * R2}$."
        d4 = f"${R + 1}$."
        caudan = f"Trong mặt phẳng $Oxy$, cho đường tròn $(C): {std_eq}$. Đường kính của đường tròn $(C)$ bằng"
        loigiai = (
            f"Đường tròn $(C): {std_eq}$ có bán kính $R = \\sqrt{{{R2}}} = {R}$.\n"
            f"Suy ra đường kính của $(C)$ là $2R = 2 \\cdot {R} = {diam}$."
        )
        phuongan = _make_choices(ans, [d1, d2, d3, d4])
        return caudan, phuongan, loigiai

    # variant == 3 (Img 4 Câu 10): Phương trình chính tắc tương đương
    ans = f"${std_eq}$."
    d1 = f"${_circle_std_tex(-a, -b, R2)}$."
    d2 = f"${_circle_std_tex(a, -b, R2)}$."
    d3 = f"${_circle_std_tex(-a, b, R2)}$."
    d4 = f"${_circle_std_tex(a, b, R)}$."
    caudan = (
        f"Trong mặt phẳng $Oxy$, cho đường tròn $(C): {gen_eq}$. "
        f"Phương trình nào sau đây cũng là phương trình của $(C)$?"
    )
    loigiai = (
        f"Đường tròn $(C)$ có tâm $I{_pt_tex(a, b)}$ và bán kính $R = \\sqrt{{{a}^2 + ({b})^2 - ({F})}} = {R}$.\n"
        f"Do đó $(C)$ có phương trình chính tắc là: ${std_eq}$."
    )
    phuongan = _make_choices(ans, [d1, d2, d3, d4])
    return caudan, phuongan, loigiai


def K10_Oxy_MC_DuongTron_DiemThuoc():
    """Kiểm tra điểm thuộc đường tròn (Img 2 Câu 8)."""
    a = random.choice([-3, -2, -1, 1, 2, 3])
    b = random.choice([-3, -2, -1, 1, 2, 3])
    # Chọn R nguyên từ 2..5
    R = random.choice([2, 3, 4, 5])
    R2 = R * R
    if R == 5 and random.choice([True, False]):
        dx, dy = random.choice([(3, 4), (-3, 4), (4, -3), (0, 5)])
    else:
        dx, dy = random.choice([(0, R), (0, -R), (R, 0), (-R, 0)])
    xM, yM = a + dx, b + dy

    ans = f"${_pt_tex(xM, yM)}$."
    d1 = f"${_pt_tex(a, b)}$."
    d2 = f"${_pt_tex(xM, b)}$." if yM != b else f"${_pt_tex(a, yM + 1)}$."
    d3 = f"${_pt_tex(a, yM - 1)}$."
    d4 = f"${_pt_tex(xM + 1, yM)}$."
    d5 = f"${_pt_tex(a + 1, b + 1)}$."

    std_eq = _circle_std_tex(a, b, R2)
    caudan = f"Trong mặt phẳng tọa độ $Oxy$, điểm nào sau đây thuộc đường tròn có phương trình ${std_eq}$?"
    loigiai = (
        f"Thay tọa độ điểm ${_pt_tex(xM, yM)}$ vào vế trái phương trình đường tròn, ta được:\n"
        f"$$({_sub_num_tex(xM, a)})^2 + ({_sub_num_tex(yM, b)})^2 = {dx}^2 + {dy}^2 = {R2}.$$\n"
        f"Đẳng thức đúng nên điểm ${_pt_tex(xM, yM)}$ thuộc đường tròn."
    )
    phuongan = _make_choices(ans, [d1, d2, d3, d4, d5])
    return caudan, phuongan, loigiai


def K10_Oxy_MC_DuongTron_VietPT_Tam_Va_BanKinh_Hoac_DiemDiQua():
    """Viết PT đường tròn biết tâm I và đi qua điểm M (hoặc bán kính R)."""
    while True:
        a = random.randint(-4, 4)
        b = random.randint(-4, 4)
        dx = random.choice([-4, -3, -2, -1, 1, 2, 3, 4])
        dy = random.choice([-4, -3, -2, -1, 1, 2, 3, 4])
        R2 = dx * dx + dy * dy
        if R2 >= 2:
            break
    xM, yM = a + dx, b + dy
    ans = f"${_circle_std_tex(a, b, R2)}$."
    d1 = f"${_circle_std_tex(-a, -b, R2)}$."
    d2 = f"${_circle_std_tex(a, b, R2 + 2)}$."
    d3 = f"${_circle_std_tex(xM, yM, R2)}$."
    d4 = f"${_circle_std_tex(a, -b, R2)}$."
    d5 = f"${_circle_std_tex(a + 1, b - 1, R2)}$."
    d6 = f"${_circle_std_tex(a, b, R2 + 5)}$."
    caudan = (
        f"Trong mặt phẳng $Oxy$, phương trình đường tròn tâm $I{_pt_tex(a, b)}$ và đi qua điểm $M{_pt_tex(xM, yM)}$ là"
    )
    loigiai = (
        f"Đường tròn có tâm $I{_pt_tex(a, b)}$ và bán kính $R = IM = \\sqrt{{({_sub_num_tex(xM, a)})^2 + ({_sub_num_tex(yM, b)})^2}} = \\sqrt{{{R2}}}$.\n"
        f"Vậy phương trình đường tròn là: ${_circle_std_tex(a, b, R2)}$."
    )
    phuongan = _make_choices(ans, [d1, d2, d3, d4, d5, d6])
    return caudan, phuongan, loigiai


def K10_Oxy_MC_DuongTron_DuongKinh_AB():
    """Viết phương trình đường tròn đường kính AB (Img 3 Câu 9, Img 4 Câu 3, Img 5 Câu 10)."""
    while True:
        a = random.choice([-3, -2, -1, 1, 2, 3])
        b = random.choice([-3, -2, -1, 1, 2, 3])
        hx = random.choice([-4, -3, -2, -1, 1, 2, 3, 4])
        hy = random.choice([-4, -3, -2, -1, 1, 2, 3, 4])
        R2 = hx * hx + hy * hy
        if R2 >= 4:
            break
    xA, yA = a + hx, b + hy
    xB, yB = a - hx, b - hy
    ans = f"${_circle_std_tex(a, b, R2)}$."
    d1 = f"${_circle_std_tex(a, b, 4 * R2)}$."
    d2 = f"${_circle_std_tex(-a, -b, R2)}$."
    d3 = f"${_circle_std_tex(a, b, 0).replace('= 0', f'= {_sqrt_tex(R2)}')}$."
    d4 = f"${_circle_std_tex(2 * a, 2 * b, 4 * R2)}$."
    caudan = f"Viết phương trình đường tròn đường kính $AB$ biết $A{_pt_tex(xA, yA)}$, $B{_pt_tex(xB, yB)}$."
    loigiai = (
        f"Tâm đường tròn là trung điểm $I$ của $AB$: $I\\left(\\dfrac{{{xA}+({xB})}}{{2}}; \\dfrac{{{yA}+({yB})}}{{2}}\\right) = {_pt_tex(a, b)}$.\n"
        f"Bán kính $R = IA = \\sqrt{{({_sub_num_tex(xA, a)})^2 + ({_sub_num_tex(yA, b)})^2}} = \\sqrt{{{R2}}}$.\n"
        f"Vậy phương trình đường tròn là: ${_circle_std_tex(a, b, R2)}$."
    )
    phuongan = _make_choices(ans, [d1, d2, d3, d4])
    return caudan, phuongan, loigiai


def K10_Oxy_MC_DuongTron_TiepXuc_Truc_Hoac_DuongThang():
    """Đường tròn tâm I tiếp xúc đường thẳng Delta hoặc trục tọa độ (tìm R hoặc viết PT)."""
    variant = random.choice([1, 2, 3])
    if variant in (1, 2):
        # Dùng bộ Pythagore (3,4,5) hoặc (5,12,13)
        A, B = random.choice([(3, -4), (4, 3), (3, 4), (5, -12), (12, 5)])
        den = int(math.isqrt(A * A + B * B))
        a = random.randint(-4, 4)
        b = random.randint(-4, 4)
        # Nếu variant == 1 (Img 3 Câu 4): tạo sao cho R nguyên đẹp (|Aa+Bb+C| chia hết den)
        if variant == 1:
            R = random.choice([1, 2, 3, 4])
            s = random.choice([-1, 1])
            C = s * R * den - (A * a + B * b)
            R2 = R * R
            ans = f"$(C): {_circle_std_tex(a, b, R2)}$."
            d1 = f"$(C): {_circle_std_tex(a, b, R)}$." if R > 1 else f"$(C): {_circle_std_tex(a, b, 3)}$."
            d2 = f"$(C): {_circle_std_tex(-a, -b, R2)}$." if (a, b) != (0, 0) else f"$(C): {_circle_std_tex(1, 1, R2)}$."
            d3 = f"$(C): {_circle_std_tex(a, b, (R + 2) ** 2)}$."
            d4 = f"$(C): {_circle_std_tex(-a, b, R2)}$." if a != 0 else f"$(C): {_circle_std_tex(a, b, R2 + 4)}$."
            caudan = (
                f"Trong mặt phẳng $Oxy$, đường tròn có tâm $I{_pt_tex(a, b)}$ tiếp xúc với đường thẳng "
                f"$(d): {_line_eq_tex(A, B, C)}$ có phương trình là"
            )
            loigiai = (
                f"Vì $(C)$ tiếp xúc với $(d)$ nên bán kính $R = d(I, d) = "
                f"\\dfrac{{|{A}\\cdot({a}) + ({B})\\cdot({b}) + ({C})|}}{{\\sqrt{{{A}^2 + ({B})^2}}}} = {R}$.\n"
                f"Vậy phương trình đường tròn là $(C): {_circle_std_tex(a, b, R2)}$."
            )
            phuongan = _make_choices(ans, [d1, d2, d3, d4])
            return caudan, phuongan, loigiai

        # variant == 2 (Img 4 Câu 4): Tìm bán kính R (có thể phân số tối giản)
        while True:
            C = random.randint(-12, 12)
            num = abs(A * a + B * b + C)
            if num > 0:
                break
        R_frac = Fraction(num, den)
        ans = f"$R = {_frac_tex(R_frac)}$."
        d1 = f"$R = {_frac_tex(R_frac + 1)}$."
        d2 = f"$R = {_frac_tex(Fraction(num + 2, den))}$." if Fraction(num + 2, den) != R_frac + 1 else f"$R = {_frac_tex(Fraction(num + 3, den))}$."
        d3 = f"$R = {_frac_tex(Fraction(num, den * den))}$."
        d4 = f"$R = {_frac_tex(Fraction(num + 4, den))}$."
        caudan = (
            f"Cho đường tròn $(C)$ có tâm $I{_pt_tex(a, b)}$ và tiếp xúc với đường thẳng "
            f"$\\Delta: {_line_eq_tex(A, B, C)}$. Bán kính $R$ của đường tròn $(C)$ bằng"
        )
        loigiai = (
            f"Do đường tròn $(C)$ tiếp xúc với $\\Delta$ nên bán kính $R$ chính bằng khoảng cách từ tâm $I$ đến $\\Delta$:\n"
            f"$$R = d(I, \\Delta) = \\dfrac{{|{A}\\cdot({a}) + ({B})\\cdot({b}) + ({C})|}}{{\\sqrt{{{A}^2 + ({B})^2}}}} "
            f"= \\dfrac{{{num}}}{{{den}}} = {_frac_tex(R_frac)}.$$"
        )
        phuongan = _make_choices(ans, [d1, d2, d3, d4])
        return caudan, phuongan, loigiai

    # variant == 3: Tâm I(a; b) tiếp xúc trục Ox hoặc Oy
    a = random.choice([-4, -3, -2, 2, 3, 4])
    b = random.choice([-4, -3, -2, 2, 3, 4])
    while abs(a) == abs(b):
        b = random.choice([-5, -3, -2, 2, 3, 5])
    axis = random.choice(["Ox", "Oy"])
    R = abs(b) if axis == "Ox" else abs(a)
    R_wrong = abs(a) if axis == "Ox" else abs(b)
    R2 = R * R
    ans = f"${_circle_std_tex(a, b, R2)}$."
    d1 = f"${_circle_std_tex(a, b, R_wrong * R_wrong)}$."
    d2 = f"${_circle_std_tex(a, b, R)}$."
    d3 = f"${_circle_std_tex(-a, -b, R2)}$."
    d4 = f"${_circle_std_tex(a, b, R_wrong)}$."
    caudan = f"Trong mặt phẳng $Oxy$, viết phương trình đường tròn có tâm $I{_pt_tex(a, b)}$ và tiếp xúc với trục ${axis}$."
    loigiai = (
        f"Đường tròn tâm $I{_pt_tex(a, b)}$ tiếp xúc với trục ${axis}$ nên có bán kính "
        f"$R = d(I, {axis}) = " + (f"|{b}| = {R}$." if axis == "Ox" else f"|{a}| = {R}$.") + "\n"
        f"Vậy phương trình đường tròn là: ${_circle_std_tex(a, b, R2)}$."
    )
    phuongan = _make_choices(ans, [d1, d2, d3, d4])
    return caudan, phuongan, loigiai


def K10_Oxy_MC_DuongTron_QuaBaDiem():
    """Viết PT đường tròn đi qua ba điểm A, B, C (ngẫu nhiên hóa tâm nguyên I)."""
    a = random.choice([-3, -2, -1, 0, 1, 2, 3])
    b = random.choice([-3, -2, -1, 0, 1, 2, 3])
    # Chọn 3 vector khác nhau có cùng độ dài bình phương R2 để bảo đảm A, B, C nguyên không thẳng hàng
    triplet_pool = [
        [(3, 4), (-3, 4), (4, -3)],
        [(5, 0), (-3, 4), (4, 3)],
        [(1, 3), (-3, 1), (3, -1)],
        [(2, 1), (-1, 2), (-2, -1)],
        [(1, 2), (-2, 1), (2, -1)],
    ]
    v1, v2, v3 = random.choice(triplet_pool)
    xA, yA = a + v1[0], b + v1[1]
    xB, yB = a + v2[0], b + v2[1]
    xC, yC = a + v3[0], b + v3[1]
    R2 = v1[0] ** 2 + v1[1] ** 2
    D, E, F = -2 * a, -2 * b, a * a + b * b - R2

    use_gen = random.choice([True, False])
    if use_gen:
        ans = f"${_circle_gen_tex(D, E, F)}$."
        d1 = f"${_circle_gen_tex(-D, -E, F)}$."
        d2 = f"${_circle_gen_tex(D, E, F + 4)}$."
        d3 = f"${_circle_gen_tex(D - 2, E + 2, F)}$."
        d4 = f"${_circle_gen_tex(D, -E, F - 2)}$."
    else:
        ans = f"${_circle_std_tex(a, b, R2)}$."
        d1 = f"${_circle_std_tex(-a, -b, R2)}$." if (a, b) != (0, 0) else f"${_circle_std_tex(1, 0, R2)}$."
        d2 = f"${_circle_std_tex(a, b, R2 + 4)}$."
        d3 = f"${_circle_std_tex(a + 1, b - 1, R2)}$."
        d4 = f"${_circle_std_tex(a, b, R2 - 1)}$."

    caudan = (
        f"Viết phương trình đường tròn ngoại tiếp tam giác $ABC$ biết "
        f"$A{_pt_tex(xA, yA)}$, $B{_pt_tex(xB, yB)}$, $C{_pt_tex(xC, yC)}$."
    )
    rhs_A = -(xA * xA + yA * yA)
    rhs_B = -(xB * xB + yB * yB)
    rhs_C = -(xC * xC + yC * yC)
    loigiai = (
        f"Giả sử phương trình đường tròn có dạng $x^2 + y^2 - 2ax - 2by + c = 0$.\n"
        f"Vì đường tròn đi qua ba điểm $A, B, C$ nên ta có hệ phương trình:\n"
        f"$$\\begin{{cases}} {-2*xA}a + ({-2*yA})b + c = {rhs_A} \\\\ "
        f"{-2*xB}a + ({-2*yB})b + c = {rhs_B} \\\\ "
        f"{-2*xC}a + ({-2*yC})b + c = {rhs_C} \\end{{cases}} "
        f"\\iff \\begin{{cases}} a = {a} \\\\ b = {b} \\\\ c = {F}. \\end{{cases}}$$\n"
        f"Suy ra tâm $I{_pt_tex(a, b)}$ và $R^2 = {a}^2 + ({b})^2 - ({F}) = {R2}$.\n"
        f"Vậy phương trình đường tròn là: " + (f"${_circle_gen_tex(D, E, F)}$." if use_gen else f"${_circle_std_tex(a, b, R2)}$.")
    )
    phuongan = _make_choices(ans, [d1, d2, d3, d4])
    return caudan, phuongan, loigiai


def K10_Oxy_MC_DuongTron_SoGiaoDiem_DuongThang():
    """Tìm số giao điểm của đường thẳng d và đường tròn (C) (Img 5 Câu 9)."""
    a = random.choice([-2, -1, 0, 1, 2])
    b = random.choice([-2, -1, 0, 1, 2])
    A, B = random.choice([(3, -4), (4, 3), (3, 4)])
    den = 5
    target = random.choice([0, 1, 2])
    R = random.choice([1, 2, 3, 4])
    if target == 1:
        # d(I, d) == R
        s = random.choice([-1, 1])
        C = s * R * den - (A * a + B * b)
        cmp_str = f"d(I, d) = R = {R}"
        ans_num = 1
    elif target == 2:
        # 0 <= d(I, d) < R -> R >= 2
        if R < 2:
            R = 2
        k_dist = random.randint(0, R - 1)
        C = k_dist * den - (A * a + B * b)
        cmp_str = f"d(I, d) = {k_dist} < R = {R}"
        ans_num = 2
    else:
        # d(I, d) > R
        k_dist = R + random.randint(1, 3)
        C = k_dist * den - (A * a + B * b)
        cmp_str = f"d(I, d) = {k_dist} > R = {R}"
        ans_num = 0

    std_eq = _circle_std_tex(a, b, R * R)
    line_eq = _line_eq_tex(A, B, C)
    caudan = (
        f"Trong mặt phẳng $Oxy$, số giao điểm của đường thẳng $(d): {line_eq}$ "
        f"và đường tròn $(C): {std_eq}$ là"
    )
    ans = f"${ans_num}$."
    loigiai = (
        f"Đường tròn $(C)$ có tâm $I{_pt_tex(a, b)}$ và bán kính $R = {R}$.\n"
        f"Khoảng cách từ tâm $I$ đến $(d)$ là:\n"
        f"$$d(I, d) = \\dfrac{{|{A}\\cdot({a}) + ({B})\\cdot({b}) + ({C})|}}{{\\sqrt{{{A}^2 + ({B})^2}}}}.\n$$\n"
        f"Ta có ${cmp_str}$, nên đường thẳng $(d)$ và đường tròn $(C)$ có ${ans_num}$ giao điểm."
    )
    phuongan = _make_choices(ans, ["$0$.", "$1$.", "$2$.", "$3$."])
    return caudan, phuongan, loigiai


def K10_Oxy_MC_DuongTron_TiepTuyen():
    """Viết phương trình tiếp tuyến của đường tròn (C) tại điểm M thuộc (C)."""
    a = random.randint(-3, 3)
    b = random.randint(-3, 3)
    while True:
        dx = random.choice([-4, -3, -2, -1, 1, 2, 3, 4])
        dy = random.choice([-4, -3, -2, -1, 1, 2, 3, 4])
        if abs(dx) != abs(dy):
            break
    xM, yM = a + dx, b + dy
    R2 = dx * dx + dy * dy

    # Tiếp tuyến qua M(xM, yM), VTPT IM = (dx, dy)
    A, B, C = _reduce_abc(dx, dy, -(dx * xM + dy * yM))
    ans = f"${_line_eq_tex(A, B, C)}$."
    d1 = f"${_line_eq_tex(*_reduce_abc(B, -A, -(B * xM - A * yM)))}$."
    d2 = f"${_line_eq_tex(*_reduce_abc(A, -B, -(A * xM - B * yM)))}$."
    d3 = f"${_line_eq_tex(*_reduce_abc(A, B, -(A * a + B * b)))}$."
    d4 = f"${_line_eq_tex(*_reduce_abc(A, B, C + 2))}$."

    std_eq = _circle_std_tex(a, b, R2)
    caudan = (
        f"Trong mặt phẳng $Oxy$, viết phương trình tiếp tuyến của đường tròn $(C): {std_eq}$ "
        f"tại điểm $M{_pt_tex(xM, yM)}$."
    )
    loigiai = (
        f"Đường tròn $(C)$ có tâm $I{_pt_tex(a, b)}$. Kiểm tra $M{_pt_tex(xM, yM)} \\in (C)$ (thỏa mãn phương trình).\n"
        f"Tiếp tuyến tại $M$ nhận $\\overrightarrow{{IM}} = ({dx}; {dy})$ làm vectơ pháp tuyến "
        f"nên có phương trình:\n"
        f"$${dx}({_sub_num_tex('x', xM)})"
        + (f" + {dy}" if dy > 0 else f" - {-dy}")
        + f"({_sub_num_tex('y', yM)}) = 0 \\iff {_line_eq_tex(A, B, C)}.$$"
    )
    phuongan = _make_choices(ans, [d1, d2, d3, d4])
    return caudan, phuongan, loigiai


def K10_Oxy_MC_DuongTron_DayCung_NganNhat():
    """Viết PT đường thẳng đi qua điểm A nằm trong (C) cắt (C) theo dây cung ngắn nhất."""
    a = random.randint(-2, 3)
    b = random.randint(-2, 3)
    while True:
        dx = random.choice([-2, -1, 1, 2])
        dy = random.choice([-2, -1, 1, 2])
        if abs(dx) != abs(dy):
            break
    ia2 = dx * dx + dy * dy
    R2 = ia2 + random.choice([4, 5, 8, 9])
    xA, yA = a + dx, b + dy
    D, E, F = -2 * a, -2 * b, a * a + b * b - R2

    # d vuông góc IA tại A -> VTPT = (dx, dy)
    A, B, C = _reduce_abc(dx, dy, -(dx * xA + dy * yA))
    ans = f"${_line_eq_tex(A, B, C)}$."
    d1 = f"${_line_eq_tex(*_reduce_abc(B, -A, -(B * xA - A * yA)))}$."
    d2 = f"${_line_eq_tex(*_reduce_abc(A, -B, -(A * xA - B * yA)))}$."
    d3 = f"${_line_eq_tex(*_reduce_abc(A, B, -(A * a + B * b)))}$."
    d4 = f"${_line_eq_tex(*_reduce_abc(A, B, C + 3))}$."

    caudan = (
        f"Trong mặt phẳng $Oxy$, cho đường tròn $(C): {_circle_gen_tex(D, E, F)}$ và điểm $A{_pt_tex(xA, yA)}$. "
        f"Phương trình đường thẳng $d$ đi qua $A$ và cắt $(C)$ theo một dây cung có độ dài ngắn nhất là"
    )
    loigiai = (
        f"Đường tròn $(C)$ có tâm $I{_pt_tex(a, b)}$ và $R^2 = {R2}$.\n"
        f"Ta có $IA^2 = {dx}^2 + ({dy})^2 = {ia2} < R^2$ nên điểm $A$ nằm bên trong $(C)$.\n"
        f"Dây cung đi qua $A$ ngắn nhất khi và chỉ khi $d(I, d)$ lớn nhất, tức là $d \\perp IA$ tại $A$.\n"
        f"Vậy $d$ đi qua $A{_pt_tex(xA, yA)}$ và nhận $\\overrightarrow{{IA}} = ({dx}; {dy})$ làm VTPT, suy ra $d: {_line_eq_tex(A, B, C)}$."
    )
    phuongan = _make_choices(ans, [d1, d2, d3, d4])
    return caudan, phuongan, loigiai


# ==============================================================================
# BÀI 22: BA ĐƯỜNG CONIC (ELIP, HYPEBOL, PARABOL)
# ==============================================================================

def K10_Oxy_MC_Conic_Elip_YeuTo():
    """Tìm tiêu cự, tiêu điểm hoặc độ dài trục lớn/trục nhỏ của Elip."""
    # Chọn (a^2, b^2) đa dạng cả c nguyên và c chứa căn
    pair_pool = [
        (25, 9), (25, 16), (100, 36), (169, 25), (169, 144),
        (9, 6), (16, 7), (16, 11), (25, 20), (36, 11), (10, 6), (20, 4),
    ]
    a2, b2 = random.choice(pair_pool)
    c2 = a2 - b2
    c_tex = _sqrt_tex(c2)
    two_c_tex = _sqrt_tex(4 * c2)

    ask_type = random.choice(["tieu_cu", "tieu_diem", "truc"])
    elip_eq = f"\\dfrac{{x^2}}{{{a2}}} + \\dfrac{{y^2}}{{{b2}}} = 1"

    if ask_type == "tieu_cu":
        # Img 2 Câu 6, Img 3 Câu 8, Img 4 Câu 6
        ans = f"${two_c_tex}$."
        d1 = f"${c_tex}$."
        d2 = f"${c2}$."
        d3 = f"${2 * c2}$."
        d4 = f"${_sqrt_tex(a2 + b2)}$."
        d5 = f"${2 * (int(math.isqrt(a2)) if int(math.isqrt(a2))**2 == a2 else 1)}$."
        caudan = f"Trong mặt phẳng tọa độ $Oxy$, đường elip ${elip_eq}$ có tiêu cự bằng"
        loigiai = (
            f"Elip có $a^2 = {a2}$, $b^2 = {b2} \\Rightarrow c = \\sqrt{{a^2 - b^2}} = \\sqrt{{{a2} - {b2}}} = {c_tex}$.\n"
            f"Vậy tiêu cự của elip là $2c = {two_c_tex}$."
        )
        phuongan = _make_choices(ans, [d1, d2, d3, d4, d5])
        return caudan, phuongan, loigiai

    if ask_type == "tieu_diem":
        ans = f"$F_1(-{c_tex}; 0)$ và $F_2({c_tex}; 0)$."
        d1 = f"$F_1(0; -{c_tex})$ và $F_2(0; {c_tex})$."
        d2 = f"$F_1(-{c2}; 0)$ và $F_2({c2}; 0)$."
        d3 = f"$F_1(-{_sqrt_tex(a2 + b2)}; 0)$ và $F_2({_sqrt_tex(a2 + b2)}; 0)$."
        d4 = f"$F_1(-{_sqrt_tex(b2)}; 0)$ và $F_2({_sqrt_tex(b2)}; 0)$."
        caudan = f"Trong mặt phẳng tọa độ $Oxy$, tọa độ hai tiêu điểm của elip $(E): {elip_eq}$ là"
        loigiai = (
            f"Từ phương trình $(E)$, ta có $a^2 = {a2}, b^2 = {b2} \\Rightarrow c = \\sqrt{{{a2} - {b2}}} = {c_tex}$.\n"
            f"Vậy hai tiêu điểm là $F_1(-{c_tex}; 0)$ và $F_2({c_tex}; 0)$."
        )
        phuongan = _make_choices(ans, [d1, d2, d3, d4])
        return caudan, phuongan, loigiai

    # ask_type == "truc" -> dùng (a^2, b^2) đều chính phương
    a, b = random.choice([(5, 3), (5, 4), (10, 6), (13, 5), (6, 4), (7, 3)])
    a2, b2 = a * a, b * b
    elip_eq = f"\\dfrac{{x^2}}{{{a2}}} + \\dfrac{{y^2}}{{{b2}}} = 1"
    ask_major = random.choice([True, False])
    if ask_major:
        ans = f"${2 * a}$."
        cands = [f"${a}$."] + [f"${2 * b}$."] + [f"${a2}$."] + [f"${a + b}$."]
        caudan = f"Trong mặt phẳng $Oxy$, độ dài trục lớn của elip $(E): {elip_eq}$ bằng"
        loigiai = f"Ta có $a^2 = {a2} \\Rightarrow a = {a}$. Độ dài trục lớn là $2a = {2 * a}$."
    else:
        ans = f"${2 * b}$."
        cands = [f"${b}$."] + [f"${2 * a}$."] + [f"${b2}$."] + [f"${a + b}$."]
        caudan = f"Trong mặt phẳng $Oxy$, độ dài trục nhỏ của elip $(E): {elip_eq}$ bằng"
        loigiai = f"Ta có $b^2 = {b2} \\Rightarrow b = {b}$. Độ dài trục nhỏ là $2b = {2 * b}$."
    phuongan = _make_choices(ans, cands)
    return caudan, phuongan, loigiai


def K10_Oxy_MC_Conic_Elip_VietPT():
    """Viết phương trình chính tắc của Elip (Img 4 Câu 11, Img 5 Câu 6)."""
    variant = random.choice([1, 2])
    if variant == 1:
        # Img 4 Câu 11: Tiêu cự bằng 2c và đi qua điểm A(a; 0)
        a, b, c = random.choice([(5, 4, 3), (5, 3, 4), (10, 8, 6), (10, 6, 8), (13, 12, 5), (13, 5, 12)])
        a2, b2, c2 = a * a, b * b, c * c
        ans = f"$\\dfrac{{x^2}}{{{a2}}} + \\dfrac{{y^2}}{{{b2}}} = 1$."
        d1 = f"$\\dfrac{{x^2}}{{{a2}}} + \\dfrac{{y^2}}{{{c2}}} = 1$."
        d2 = f"$\\dfrac{{x^2}}{{{b2}}} + \\dfrac{{y^2}}{{{a2}}} = 1$."
        d3 = f"$\\dfrac{{x^2}}{{{4 * a2}}} + \\dfrac{{y^2}}{{{4 * b2}}} = 1$."
        d4 = f"$\\dfrac{{x^2}}{{{a2 - b2}}} + \\dfrac{{y^2}}{{{b2}}} = 1$."
        caudan = (
            f"Trong mặt phẳng tọa độ $Oxy$, phương trình chính tắc của elip $(E)$ có tiêu cự bằng ${2 * c}$ "
            f"và đi qua điểm $A({a}; 0)$ là"
        )
        loigiai = (
            f"Elip $(E)$ đi qua điểm $A({a}; 0)$ nằm trên trục $Ox$ nên $a = {a} \\Rightarrow a^2 = {a2}$.\n"
            f"Tiêu cự $2c = {2 * c} \\Rightarrow c = {c}$.\n"
            f"Suy ra $b^2 = a^2 - c^2 = {a2} - {c2} = {b2}$.\n"
            f"Vậy phương trình chính tắc của elip $(E)$ là $\\dfrac{{x^2}}{{{a2}}} + \\dfrac{{y^2}}{{{b2}}} = 1$."
        )
        phuongan = _make_choices(ans, [d1, d2, d3, d4])
        return caudan, phuongan, loigiai

    # variant == 2 (Img 5 Câu 6): Đi qua M(0; b) và khoảng cách lớn nhất giữa hai điểm trên (E) bằng 2a
    b = random.choice([2, 3, 4, 5])
    a = b + random.choice([1, 2, 3, 4])
    a2, b2 = a * a, b * b
    ans = f"$\\dfrac{{x^2}}{{{a2}}} + \\dfrac{{y^2}}{{{b2}}} = 1$."
    d1 = f"$\\dfrac{{x^2}}{{{b2}}} + \\dfrac{{y^2}}{{{a2}}} = 1$."
    d2 = f"$\\dfrac{{x^2}}{{{b2}}} + \\dfrac{{y^2}}{{{4 * a2}}} = 1$."
    d3 = f"$\\dfrac{{x^2}}{{{4 * a2}}} + \\dfrac{{y^2}}{{{b2}}} = 1$."
    d4 = f"$\\dfrac{{x^2}}{{{a2 + b2}}} + \\dfrac{{y^2}}{{{b2}}} = 1$."
    caudan = (
        f"Trong mặt phẳng tọa độ $Oxy$, cho Elip $(E)$ đi qua điểm $M(0; {b})$. "
        f"Biết khoảng cách lớn nhất giữa hai điểm trên $(E)$ bằng ${2 * a}$. Phương trình chính tắc của Elip là"
    )
    loigiai = (
        f"Khoảng cách lớn nhất giữa hai điểm trên $(E)$ chính là độ dài trục lớn: $2a = {2 * a} \\Rightarrow a = {a} \\Rightarrow a^2 = {a2}$.\n"
        f"Elip đi qua $M(0; {b})$ trên trục $Oy$ nên $\\dfrac{{0^2}}{{a^2}} + \\dfrac{{{b}^2}}{{b^2}} = 1 \\Rightarrow b^2 = {b2}$.\n"
        f"Vậy phương trình chính tắc của $(E)$ là $\\dfrac{{x^2}}{{{a2}}} + \\dfrac{{y^2}}{{{b2}}} = 1$."
    )
    phuongan = _make_choices(ans, [d1, d2, d3, d4])
    return caudan, phuongan, loigiai


def K10_Oxy_MC_Conic_Hypebol_YeuTo():
    """Tìm tiêu điểm, |MF1 - MF2| = 2a, hoặc điểm thuộc / không thuộc Hypebol."""
    variant = random.choice([1, 2, 3])
    if variant == 1:
        # Img 3 Câu 6 & Img 4 Câu 7: Tìm hai tiêu điểm của Hypebol
        pair_pool = [(16, 9), (9, 16), (25, 144), (36, 64), (25, 9), (16, 5), (9, 4), (4, 9)]
        a2, b2 = random.choice(pair_pool)
        c2 = a2 + b2
        c_tex = _sqrt_tex(c2)
        hyp_eq = f"\\dfrac{{x^2}}{{{a2}}} - \\dfrac{{y^2}}{{{b2}}} = 1"

        ans = f"$F_1(-{c_tex}; 0)$ và $F_2({c_tex}; 0)$."
        d1 = f"$F_1(-{c2}; 0)$ và $F_2({c2}; 0)$."
        d2 = f"$F_1(0; -{c_tex})$ và $F_2(0; {c_tex})$."
        c_minus = abs(a2 - b2)
        d3 = f"$F_1(-{_sqrt_tex(c_minus)}; 0)$ và $F_2({_sqrt_tex(c_minus)}; 0)$." if c_minus > 0 else "$F_1(0; 0)$ và $F_2(1; 0)$."
        d4 = f"$F_1(-{_sqrt_tex(a2 * a2 + b2 * b2)}; 0)$ và $F_2({_sqrt_tex(a2 * a2 + b2 * b2)}; 0)$."

        caudan = f"Trong mặt phẳng tọa độ $Oxy$, cho hypebol $(H): {hyp_eq}$. Các tiêu điểm của hypebol là"
        loigiai = (
            f"Hypebol có $a^2 = {a2}, b^2 = {b2} \\Rightarrow c = \\sqrt{{a^2 + b^2}} = \\sqrt{{{a2} + {b2}}} = {c_tex}$.\n"
            f"Vậy hypebol có hai tiêu điểm là $F_1(-{c_tex}; 0)$ và $F_2({c_tex}; 0)$."
        )
        phuongan = _make_choices(ans, [d1, d2, d3, d4])
        return caudan, phuongan, loigiai

    if variant == 2:
        # Img 5 Câu 2: |MF1 - MF2| = 2a
        a = random.choice([2, 3, 4, 5, 6])
        b = random.choice([3, 4, 5, 6, 7])
        a2, b2 = a * a, b * b
        hyp_eq = f"\\dfrac{{x^2}}{{{a2}}} - \\dfrac{{y^2}}{{{b2}}} = 1"
        ans = f"${2 * a}$."
        d1 = f"${2 * b}$." if b != a else f"${2 * a + 2}$."
        d2 = f"${a}$."
        d3 = f"${a + b}$."
        d4 = f"${a2}$."
        caudan = (
            f"Trong mặt phẳng tọa độ $Oxy$, cho hypebol có phương trình chính tắc ${hyp_eq}$ "
            f"và điểm $M$ thuộc hypebol. Khi đó $|MF_1 - MF_2|$ bằng"
        )
        loigiai = (
            f"Từ phương trình hypebol ta có $a^2 = {a2} \\Rightarrow a = {a}$.\n"
            f"Theo định nghĩa hypebol, mọi điểm $M \\in (H)$ đều thỏa mãn $|MF_1 - MF_2| = 2a = {2 * a}$."
        )
        phuongan = _make_choices(ans, [d1, d2, d3, d4])
        return caudan, phuongan, loigiai

    # variant == 3 (Img 5 Câu 4): Điểm nào KHÔNG nằm trên Hypebol (H)
    a = random.choice([2, 3, 4, 5])
    b = random.choice([2, 3, 4, 5])
    a2, b2 = a * a, b * b
    hyp_eq = f"\\dfrac{{x^2}}{{{a2}}} - \\dfrac{{y^2}}{{{b2}}} = 1"
    # 3 điểm nằm trên (H): (a; 0), (-a; 0), (-a*sqrt(2); b) hoặc (a*sqrt(2); b)
    on1 = f"$Q({a}; 0)$."
    on2 = f"$P(-{a}; 0)$."
    x_rad = f"{a}\\sqrt{{2}}"
    on3 = f"$N(-{x_rad}; {b})$."
    # 1 điểm KHÔNG nằm trên (H)
    x_bad = a - 1 if a > 2 else a + 1
    ans = f"$M({x_bad}; 1)$."

    caudan = f"Cho đường hypebol có phương trình chính tắc $(H): {hyp_eq}$. Điểm nào sau đây \\textbf{{không nằm}} trên đường hypebol?"
    loigiai = (
        f"Thay tọa độ điểm $M({x_bad}; 1)$ vào vế trái phương trình $(H)$:\n"
        f"$$\\dfrac{{{x_bad}^2}}{{{a2}}} - \\dfrac{{1^2}}{{{b2}}} = {_frac_tex(Fraction(x_bad**2, a2) - Fraction(1, b2))} \\ne 1.$$\n"
        f"Các điểm $Q({a}; 0), P(-{a}; 0), N(-{x_rad}; {b})$ đều thỏa mãn $\\dfrac{{x^2}}{{{a2}}} - \\dfrac{{y^2}}{{{b2}}} = 1$.\n"
        f"Vậy điểm $M({x_bad}; 1)$ không nằm trên đường hypebol."
    )
    phuongan = _make_choices(ans, [on1, on2, on3])
    return caudan, phuongan, loigiai


def K10_Oxy_MC_Conic_Hypebol_VietPT():
    """Viết phương trình chính tắc của Hypebol (Img 2 Câu 5, Img 4 Câu 9)."""
    variant = random.choice([1, 2])
    if variant == 1:
        # Img 2 Câu 5: Qua hai điểm A(xA, yA) và B(xB, yB)
        # Chọn trước a2, b2 là bội nhỏ, ví dụ a2 = 4*k_a hoặc chọn a, b và điểm theo công thức x^2/a2 - y^2/b2 = 1
        a2, b2 = random.choice([(16, 4), (9, 4), (16, 9), (25, 4), (4, 9), (12, 4)])
        # Điểm A: yA^2 = b2 => xA^2 = 2*a2 (nên xA = sqrt(2*a2) rất gọn)
        xA_tex = _sqrt_tex(2 * a2)
        yA_val = int(math.isqrt(b2))
        yA_tex = str(yA_val)
        # Điểm B: chọn B nằm ở nhánh âm/dương với yB^2 = b2 + 1 -> xB^2 = a2*(2 + 1/b2) không luôn nguyên, nên chọn xB^2 = k_ratio * a2
        # Chọn tỉ lệ bội m = 9/4 (yB^2 = 5*b2/4) hoặc xB = +/- 3*a/2? Tốt nhất cho yB^2 = (k - 1)*b2 thì xB^2 = k*a2 với k in {3, 4}!
        k = random.choice([3, 4])
        # Tránh k = 2 (trùng A)
        xB_sq = k * a2
        yB_sq = (k - 1) * b2
        xB_tex = f"-{_sqrt_tex(xB_sq)}"
        yB_tex = f"-{_sqrt_tex(yB_sq)}"

        ans = f"$\\dfrac{{x^2}}{{{a2}}} - \\dfrac{{y^2}}{{{b2}}} = 1$."
        d1 = f"$\\dfrac{{x^2}}{{{b2}}} - \\dfrac{{y^2}}{{{a2}}} = 1$." if a2 != b2 else "$\\dfrac{x^2}{31} - \\dfrac{y^2}{31} = 1$."
        d2 = f"$\\dfrac{{x^2}}{{{a2 + 8}}} - \\dfrac{{y^2}}{{{b2 + 8}}} = 1$."
        d3 = f"$\\dfrac{{x^2}}{{{2 * a2}}} - \\dfrac{{y^2}}{{{2 * b2}}} = 1$."
        d4 = f"$\\dfrac{{x^2}}{{{a2}}} + \\dfrac{{y^2}}{{{b2}}} = 1$."

        caudan = (
            f"Trong mặt phẳng $Oxy$, phương trình chính tắc của hypebol $(H)$ đi qua hai điểm "
            f"$A({xA_tex}; {yA_tex})$ và $B({xB_tex}; {yB_tex})$ là"
        )
        loigiai = (
            f"Phương trình chính tắc của hypebol $(H)$ có dạng $\\dfrac{{x^2}}{{a^2}} - \\dfrac{{y^2}}{{b^2}} = 1$.\n"
            f"Thay tọa độ $A, B$ vào phương trình $(H)$, ta có hệ:\n"
            f"$$\\begin{{cases}} \\dfrac{{{2 * a2}}}{{a^2}} - \\dfrac{{{b2}}}{{b^2}} = 1 \\\\ "
            f"\\dfrac{{{xB_sq}}}{{a^2}} - \\dfrac{{{yB_sq}}}{{b^2}} = 1 \\end{{cases}} "
            f"\\iff \\begin{{cases}} \\dfrac{{1}}{{a^2}} = \\dfrac{{1}}{{{a2}}} \\\\ \\dfrac{{1}}{{b^2}} = \\dfrac{{1}}{{{b2}}} \\end{{cases}} "
            f"\\iff \\begin{{cases}} a^2 = {a2} \\\\ b^2 = {b2}. \\end{{cases}}$$\n"
            f"Vậy phương trình chính tắc của $(H)$ là $\\dfrac{{x^2}}{{{a2}}} - \\dfrac{{y^2}}{{{b2}}} = 1$."
        )
        phuongan = _make_choices(ans, [d1, d2, d3, d4])
        return caudan, phuongan, loigiai

    # variant == 2 (Img 4 Câu 9): Biết một tiêu điểm F1(-c; 0) và đi qua M(a; 0)
    a = random.choice([2, 3, 4, 5])
    c = a + random.choice([1, 2, 3])
    a2, c2 = a * a, c * c
    b2 = c2 - a2
    f_str = f"F_1(-{c}; 0)" if random.choice([True, False]) else f"F_2({c}; 0)"

    ans = f"$\\dfrac{{x^2}}{{{a2}}} - \\dfrac{{y^2}}{{{b2}}} = 1$."
    d1 = f"$\\dfrac{{x^2}}{{{a2}}} + \\dfrac{{y^2}}{{{b2}}} = 1$."
    d2 = f"$\\dfrac{{x^2}}{{{b2}}} - \\dfrac{{y^2}}{{{a2}}} = 1$." if a2 != b2 else f"$\\dfrac{{x^2}}{{{a2 + 2}}} - \\dfrac{{y^2}}{{{b2}}} = 1$."
    d3 = f"$\\dfrac{{x^2}}{{{a}}} - \\dfrac{{y^2}}{{{b2}}} = 1$."
    d4 = f"$\\dfrac{{x^2}}{{{a2}}} - \\dfrac{{y^2}}{{{c2}}} = 1$."

    caudan = (
        f"Phương trình chính tắc của hypebol $(H)$ có một tiêu điểm ${f_str}$ và đi qua điểm $M({a}; 0)$ là"
    )
    loigiai = (
        f"Hypebol có tiêu điểm ${f_str}$ nên $c = {c} \\Rightarrow c^2 = {c2}$.\n"
        f"Vì $(H)$ đi qua $M({a}; 0)$ nên $a = {a} \\Rightarrow a^2 = {a2}$.\n"
        f"Suy ra $b^2 = c^2 - a^2 = {c2} - {a2} = {b2}$.\n"
        f"Vậy phương trình chính tắc của $(H)$ là $\\dfrac{{x^2}}{{{a2}}} - \\dfrac{{y^2}}{{{b2}}} = 1$."
    )
    phuongan = _make_choices(ans, [d1, d2, d3, d4])
    return caudan, phuongan, loigiai


def K10_Oxy_MC_Conic_Parabol_ChinhTac():
    """Phương trình chính tắc, tiêu điểm và đường chuẩn của Parabol (Img 2 Câu 4, Img 3 Câu 7, Img 4 Câu 5)."""
    # p là số nguyên dương (có cả lẻ -> nửa nguyên p/2, và chẵn -> p/2 nguyên)
    p = random.choice([1, 2, 3, 4, 5, 6, 8, 10])
    two_p = 2 * p
    half_p = Fraction(p, 2)
    half_p_tex = _frac_tex(half_p)

    variant = random.choice([1, 2, 3])
    if variant == 1:
        # Img 2 Câu 4: Biết đường chuẩn x + p/2 = 0 -> Tìm PT chính tắc y^2 = 2px
        ans = f"$y^2 = {_lin_tex(two_p, 0, 'x')}$."
        d1 = f"$y^2 = {_lin_tex(two_p * 2, 0, 'x')}$."
        d2 = f"$y^2 = {_lin_tex(p, 0, 'x')}$."
        d3 = f"$y^2 = {_lin_tex(half_p, 0, 'x')}$." if half_p != p else f"$y^2 = {_lin_tex(two_p + 2, 0, 'x')}$."
        d4 = f"$y^2 = {_lin_tex(Fraction(p, 4), 0, 'x')}$."
        caudan = (
            f"Trong mặt phẳng $Oxy$, cho parabol $(P)$ có phương trình đường chuẩn $x + {half_p_tex} = 0$. "
            f"Phương trình chính tắc của parabol $(P)$ là"
        )
        loigiai = (
            f"Đường chuẩn của parabol $(P)$ có phương trình $x + \\dfrac{{p}}{{2}} = 0$.\n"
            f"So với $x + {half_p_tex} = 0$, ta suy ra $\\dfrac{{p}}{{2}} = {half_p_tex} \\iff p = {p}$.\n"
            f"Vậy phương trình chính tắc của $(P)$ là $y^2 = 2px = {_lin_tex(two_p, 0, 'x')}$."
        )
        phuongan = _make_choices(ans, [d1, d2, d3, d4])
        return caudan, phuongan, loigiai

    if variant == 2:
        # Img 3 Câu 7: Cho y^2 = 2px -> Tìm tọa độ tiêu điểm F(p/2; 0)
        ans = f"$F({_frac_tex(half_p)}; 0)$."
        d1 = f"$F(-{_frac_tex(half_p)}; 0)$."
        d2 = f"$F(0; {_frac_tex(half_p)})$."
        d3 = f"$F(0; -{_frac_tex(half_p)})$."
        d4 = f"$F({p}; 0)$."
        caudan = (
            f"Trong mặt phẳng $Oxy$, cho parabol $(P)$ có phương trình $y^2 = {_lin_tex(two_p, 0, 'x')}$. "
            f"Tọa độ tiêu điểm của parabol $(P)$ là"
        )
        loigiai = (
            f"Parabol $(P): y^2 = {_lin_tex(two_p, 0, 'x')}$ có $2p = {two_p} \\Rightarrow p = {p} \\Rightarrow \\dfrac{{p}}{{2}} = {half_p_tex}$.\n"
            f"Vậy tọa độ tiêu điểm của $(P)$ là $F({_frac_tex(half_p)}; 0)$."
        )
        phuongan = _make_choices(ans, [d1, d2, d3, d4])
        return caudan, phuongan, loigiai

    # variant == 3 (Img 4 Câu 5): Biết tiêu điểm F(p/2; 0) -> Tìm PT chính tắc y^2 = 2px
    ans = f"$y^2 = {_lin_tex(two_p, 0, 'x')}$."
    d1 = f"$y^2 = {_lin_tex(p, 0, 'x')}$."
    d2 = f"$y^2 = {_lin_tex(two_p * 2, 0, 'x')}$."
    d3 = f"$y^2 = {_lin_tex(two_p + 5, 0, 'x')}$."
    d4 = f"$y^2 = {_lin_tex(Fraction(p, 2), 0, 'x')}$." if p > 1 else "$y^2 = 4x$."
    caudan = (
        f"Trong mặt phẳng $Oxy$, phương trình chính tắc của parabol $(P)$ có tiêu điểm là $F({_frac_tex(half_p)}; 0)$ là"
    )
    loigiai = (
        f"Parabol $(P)$ có tiêu điểm $F\\left(\\dfrac{{p}}{{2}}; 0\\right) = F({_frac_tex(half_p)}; 0)$ nên $\\dfrac{{p}}{{2}} = {half_p_tex} \\iff p = {p}$.\n"
        f"Vậy phương trình chính tắc của $(P)$ là $y^2 = 2px = {_lin_tex(two_p, 0, 'x')}$."
    )
    phuongan = _make_choices(ans, [d1, d2, d3, d4])
    return caudan, phuongan, loigiai


# ==============================================================================
# PHẦN II: TRẮC NGHIỆM ĐÚNG SAI (TF) - CHƯƠNG VII (BÀI 19, 20, 21)
# ==============================================================================

def _sqrt_frac_tex(val):
    """Định dạng căn bậc hai của số hữu tỉ không âm p/q về dạng tối giản LaTeX."""
    f = Fraction(val).limit_denominator()
    if f <= 0:
        return "0"
    p, q = f.numerator, f.denominator
    k, r = _simplify_sqrt(p * q)
    if r == 1:
        return _frac_tex(Fraction(k, q))
    red = Fraction(k, q)
    num_str = f"\\sqrt{{{r}}}" if red.numerator == 1 else f"{red.numerator}\\sqrt{{{r}}}"
    if red.denominator == 1:
        return num_str
    return f"\\dfrac{{{num_str}}}{{{red.denominator}}}"


def _make_tf_choices(items):
    """Tạo 4 mệnh đề Đúng/Sai và lời giải itemchoice từ list [(stmt_t, stmt_f, exp_t, exp_f)]."""
    choices = []
    sol_parts = []
    for stmt_t, stmt_f, exp_t, exp_f in items:
        if random.choice([True, False]):
            choices.append(f"{{\\True {stmt_t.strip()}}}\n")
            sol_parts.append(f"\\itemch \\textbf{{ĐÚNG.}} {exp_t.strip()}")
        else:
            choices.append(f"{{{stmt_f.strip()}}}\n")
            sol_parts.append(f"\\itemch \\textbf{{SAI.}} {exp_f.strip()}")
    loigiai = "\\begin{itemchoice}\n" + "\n".join(sol_parts) + "\n\\end{itemchoice}"
    return choices, loigiai


def K10_Oxy_TF_VTTD_Goc_BonCapDuongThang():
    """Đúng/Sai: VTTĐ giữa 4 cặp đường thẳng (PTTQ, PTTS) và góc giữa 2 đường thẳng (Ảnh 1 Câu 13)."""
    # Ý a): d1, d2 dạng PTTQ (cắt nhau vs song song)
    a1, b1 = random.choice([1, 2, -1]), random.choice([3, 4, -2])
    c1 = random.choice([-1, 1, 2])
    while True:
        a2, b2 = random.choice([2, 3, -3]), random.choice([-3, -2, 1, 5])
        if a1 * b2 - a2 * b1 != 0:
            break
    c2 = random.choice([-5, 3, 5])
    # Song song để tạo stmt_f
    k_ss = random.choice([2, -2, 3])
    c2_ss = k_ss * c1 + random.choice([1, 2, -1])
    stmt_a_t = f"$d_1: {_line_eq_tex(a1, b1, c1)}$ cắt $d_2: {_line_eq_tex(a2, b2, c2)}$."
    exp_a_t = (
        f"Ta có ${a1}\\cdot({b2}) - ({a2})\\cdot({b1}) = {a1*b2 - a2*b1} \\ne 0$ nên $d_1$ cắt $d_2$."
    )
    stmt_a_f = f"$d_1: {_line_eq_tex(a1, b1, c1)}$ cắt $d_2: {_line_eq_tex(k_ss*a1, k_ss*b1, c2_ss)}$."
    exp_a_f = (
        f"Ta có $\\dfrac{{{a1}}}{{{k_ss*a1}}} = \\dfrac{{{b1}}}{{{k_ss*b1}}} \\ne \\dfrac{{{c1}}}{{{c2_ss}}}$ nên $d_1 \\parallel d_2$ (không cắt nhau)."
    )

    # Ý b): m1 (PTTS) song song m2 (PTTQ)
    u1, u2 = random.choice([(3, -4), (2, -5), (4, 3), (1, -3)])
    x1, y1 = random.randint(1, 5), random.randint(-5, -1)
    # m2 nhận VTPT (2*u2, -2*u1) hoặc cắt m1
    n2a, n2b = 2 * u2, -2 * u1
    val_at_pt = n2a * x1 + n2b * y1
    c_m2_ss = -val_at_pt + random.choice([1, 3, -2])
    stmt_b_t = f"$m_1: {_ptts_tex(x1, y1, u1, u2)}$ song song $m_2: {_line_eq_tex(n2a, n2b, c_m2_ss)}$."
    exp_b_t = (
        f"Đường thẳng $m_1$ qua $A{_pt_tex(x1, y1)}$ có VTCP $\\vec{{u}}_1 = ({u1}; {u2})$ và VTPT $\\vec{{n}}_1 = ({u2}; {-u1})$ cùng phương $\\vec{{n}}_2 = ({n2a}; {n2b})$ của $m_2$. "
        f"Thay $A$ vào $m_2$ được ${val_at_pt + c_m2_ss} \\ne 0$ nên $m_1 \\parallel m_2$."
    )
    stmt_b_f = f"$m_1: {_ptts_tex(x1, y1, u1, u2)}$ song song $m_2: {_line_eq_tex(n2a, n2b, -val_at_pt)}$."
    exp_b_f = (
        f"Thay $A{_pt_tex(x1, y1)} \\in m_1$ vào $m_2$ thấy thỏa mãn và $\\vec{{n}}_1, \\vec{{n}}_2$ cùng phương nên $m_1 \\equiv m_2$ (trùng nhau)."
    )

    # Ý c): a1 (t) trùng a2 (k)
    p1, p2 = random.choice([(1, -3), (2, -1), (-1, 3)])
    v1, v2 = random.choice([(1, 3), (2, -1), (1, -2)])
    k_step = random.choice([1, 2])
    q1_t, q2_t = p1 + k_step * v1, p2 + k_step * v2
    q1_f, q2_f = q1_t + 1, q2_t
    stmt_c_t = f"$a_1: {_ptts_tex(p1, p2, v1, v2)}$ trùng $a_2: {_ptts_tex(q1_t, q2_t, 2*v1, 2*v2).replace('t', 'k')}$ (với $t, k$ là các tham số)."
    exp_c_t = (
        f"Hai đường thẳng có cùng phương VTCP $\\vec{{u}}_2 = 2\\vec{{u}}_1$ và điểm $M{_pt_tex(q1_t, q2_t)} \\in a_2$ cũng thuộc $a_1$ (ứng với $t = {k_step}$) nên $a_1 \\equiv a_2$."
    )
    stmt_c_f = f"$a_1: {_ptts_tex(p1, p2, v1, v2)}$ trùng $a_2: {_ptts_tex(q1_f, q2_f, 2*v1, 2*v2).replace('t', 'k')}$ (với $t, k$ là các tham số)."
    exp_c_f = (
        f"Thay điểm $M{_pt_tex(q1_f, q2_f)} \\in a_2$ vào $a_1$ thấy vô nghiệm $t$ nên $a_1 \\parallel a_2$ (không trùng)."
    )

    # Ý d): Góc giữa hai đường thẳng
    c_ang = random.choice([1, 2, -2])
    mode_ang = random.choice([45, 30])
    if mode_ang == 45:
        d1_str = f"x + y - {random.choice([1, 2, 3])} = 0"
        d2_str = f"x + {c_ang} = 0" if c_ang > 0 else f"x - {-c_ang} = 0"
        ang_true, ang_wrong = "45^\\circ", "30^\\circ"
        exp_ang = "$\\cos\\varphi = \\dfrac{|1\\cdot 1 + 1\\cdot 0|}{\\sqrt{2}\\cdot 1} = \\dfrac{\\sqrt{2}}{2} \\Rightarrow \\varphi = 45^\\circ$."
    else:
        d1_str = f"\\sqrt{{3}}x - y + {random.choice([1, 2])} = 0"
        d2_str = f"x + {c_ang} = 0" if c_ang > 0 else f"x - {-c_ang} = 0"
        ang_true, ang_wrong = "30^\\circ", "60^\\circ"
        exp_ang = "$\\cos\\varphi = \\dfrac{|\\sqrt{3}\\cdot 1 + (-1)\\cdot 0|}{2\\cdot 1} = \\dfrac{\\sqrt{3}}{2} \\Rightarrow \\varphi = 30^\\circ$."
    stmt_d_t = f"$\\Delta_1: {d1_str}$ và $\\Delta_2: {d2_str}$; góc giữa hai đường thẳng là ${ang_true}$."
    stmt_d_f = f"$\\Delta_1: {d1_str}$ và $\\Delta_2: {d2_str}$; góc giữa hai đường thẳng là ${ang_wrong}$."
    exp_d_t = exp_ang
    exp_d_f = f"{exp_ang} Do đó ghi ${ang_wrong}$ là sai."

    caudan = "Các mệnh đề sau đúng hay sai?"
    phuongan, loigiai = _make_tf_choices([
        (stmt_a_t, stmt_a_f, exp_a_t, exp_a_f),
        (stmt_b_t, stmt_b_f, exp_b_t, exp_b_f),
        (stmt_c_t, stmt_c_f, exp_c_t, exp_c_f),
        (stmt_d_t, stmt_d_f, exp_d_t, exp_d_f),
    ])
    return caudan, phuongan, loigiai


def K10_Oxy_TF_HaiDuongThang_PTTS_GiaoDiem_VTTD():
    """Đúng/Sai: Cho hai đường thẳng PTTS Delta1, Delta2 - xét VTCP, song song, giao điểm, vuông góc (Ảnh 1 Câu 14)."""
    xM = random.randint(2, 8)
    yM = random.randint(-4, 5)
    is_perp = random.choice([True, False])
    if is_perp:
        u1, u2 = random.choice([(3, -4), (2, 5), (1, -3), (4, 3)])
        v1, v2 = -u2, u1
    else:
        while True:
            u1, u2 = random.choice([2, 3, 5, -2]), random.choice([-6, -4, 3, 5])
            v1, v2 = random.choice([2, 5, -3]), random.choice([3, 6, -4])
            if u1 * v2 - u2 * v1 != 0 and u1 * v1 + u2 * v2 != 0:
                break
    t1 = random.choice([-1, 1])
    t2 = random.choice([-1, 1])
    x1, y1 = xM - u1 * t1, yM - u2 * t1
    x2, y2 = xM - v1 * t2, yM - v2 * t2

    d1_str = _ptts_tex(x1, y1, u1, u2)
    d2_str = _ptts_tex(x2, y2, v1, v2).replace("t", "t'")
    caudan = (
        f"Cho hai đường thẳng $\\Delta_1: {d1_str}$ và $\\Delta_2: {d2_str}$.\n"
        f"Các mệnh đề sau đúng hay sai?"
    )

    stmt_a_t = f"Hai đường thẳng $\\Delta_1, \\Delta_2$ lần lượt có vectơ chỉ phương $\\vec{{u}}_1 = {_vec_tex(u1, u2)}$, $\\vec{{u}}_2 = {_vec_tex(v1, v2)}$."
    exp_a_t = f"Đọc hệ số của $t, t'$ ta có VTCP của $\\Delta_1$ là $({_frac_tex(u1)}; {_frac_tex(u2)})$ và của $\\Delta_2$ là $({_frac_tex(v1)}; {_frac_tex(v2)})$."
    stmt_a_f = f"Hai đường thẳng $\\Delta_1, \\Delta_2$ lần lượt có vectơ chỉ phương $\\vec{{u}}_1 = {_vec_tex(x1, y1)}$, $\\vec{{u}}_2 = {_vec_tex(x2, y2)}$."
    exp_a_f = f"Vectơ chỉ phương phải là hệ số của tham số $t, t'$ là $({_frac_tex(u1)}; {_frac_tex(u2)})$ và $({_frac_tex(v1)}; {_frac_tex(v2)})$."

    stmt_b_t = "Hai đường thẳng $\\Delta_1, \\Delta_2$ cắt nhau."
    exp_b_t = f"Vì ${u1}\\cdot({v2}) - ({u2})\\cdot({v1}) = {u1*v2 - u2*v1} \\ne 0$ nên $\\vec{{u}}_1, \\vec{{u}}_2$ không cùng phương, suy ra $\\Delta_1$ và $\\Delta_2$ cắt nhau."
    stmt_b_f = "Hai đường thẳng $\\Delta_1, \\Delta_2$ song song."
    exp_b_f = f"Hai VTCP $\\vec{{u}}_1 = ({u1}; {u2})$ và $\\vec{{u}}_2 = ({v1}; {v2})$ không cùng phương nên $\\Delta_1$ cắt $\\Delta_2$, không song song."

    stmt_c_t = f"$M{_pt_tex(xM, yM)}$ là tọa độ giao điểm hai đường $\\Delta_1, \\Delta_2$."
    exp_c_t = f"Với $t = {t1}$ trên $\\Delta_1$ và $t' = {t2}$ trên $\\Delta_2$, ta đều được điểm $M{_pt_tex(xM, yM)}$."
    stmt_c_f = f"$M{_pt_tex(xM + 1, yM - 1)}$ là tọa độ giao điểm hai đường $\\Delta_1, \\Delta_2$."
    exp_c_f = f"Giải hệ tìm giao điểm được $t = {t1}, t' = {t2}$, giao điểm là ${_pt_tex(xM, yM)}$."

    dot = u1 * v1 + u2 * v2
    if is_perp:
        stmt_d_t = "$\\Delta_1, \\Delta_2$ vuông góc với nhau."
        exp_d_t = f"Tích vô hướng $\\vec{{u}}_1 \\cdot \\vec{{u}}_2 = ({u1})({v1}) + ({u2})({v2}) = 0$ nên $\\Delta_1 \\perp \\Delta_2$."
        stmt_d_f = "$\\Delta_1, \\Delta_2$ không vuông góc với nhau."
        exp_d_f = f"Tích vô hướng $\\vec{{u}}_1 \\cdot \\vec{{u}}_2 = 0$ nên $\\Delta_1 \\perp \\Delta_2$."
    else:
        stmt_d_t = "$\\Delta_1, \\Delta_2$ không vuông góc với nhau."
        exp_d_t = f"Tích vô hướng $\\vec{{u}}_1 \\cdot \\vec{{u}}_2 = ({u1})({v1}) + ({u2})({v2}) = {dot} \\ne 0$ nên $\\Delta_1$ không vuông góc với $\\Delta_2$."
        stmt_d_f = "$\\Delta_1, \\Delta_2$ vuông góc với nhau."
        exp_d_f = f"Tích vô hướng $\\vec{{u}}_1 \\cdot \\vec{{u}}_2 = {dot} \\ne 0$ nên hai đường thẳng không vuông góc."

    phuongan, loigiai = _make_tf_choices([
        (stmt_a_t, stmt_a_f, exp_a_t, exp_a_f),
        (stmt_b_t, stmt_b_f, exp_b_t, exp_b_f),
        (stmt_c_t, stmt_c_f, exp_c_t, exp_c_f),
        (stmt_d_t, stmt_d_f, exp_d_t, exp_d_f),
    ])
    return caudan, phuongan, loigiai


def K10_Oxy_TF_KhoangCach_Diem_Va_HaiDuongSongSong():
    """Đúng/Sai: Khoảng cách từ điểm đến đường thẳng (PTTQ, PTTS) và khoảng cách 2 đường song song (Ảnh 1 Câu 15)."""
    # Ý a): d(M, Delta) với Delta PTTQ bộ Pythagore
    A1, B1 = random.choice([(3, -4), (4, 3), (5, -12)])
    den1 = int(math.isqrt(A1 * A1 + B1 * B1))
    C1 = random.choice([-12, -10, -7, 4, 8])
    xM = random.randint(-2, 4)
    yM = random.randint(-3, 3)
    num1 = abs(A1 * xM + B1 * yM + C1)
    while num1 == 0:
        C1 += 1
        num1 = abs(A1 * xM + B1 * yM + C1)
    d1_t = _frac_tex(Fraction(num1, den1))
    d1_f = _frac_tex(Fraction(num1 + 2, den1))
    stmt_a_t = f"$M{_pt_tex(xM, yM)}$; $\\Delta: {_line_eq_tex(A1, B1, C1)}$, khi đó $d(M, \\Delta) = {d1_t}$."
    exp_a_t = f"$d(M, \\Delta) = \\dfrac{{|{A1}({xM}) + ({B1})({yM}) + ({C1})|}}{{\\sqrt{{{A1}^2 + ({B1})^2}}}} = {d1_t}$."
    stmt_a_f = f"$M{_pt_tex(xM, yM)}$; $\\Delta: {_line_eq_tex(A1, B1, C1)}$, khi đó $d(M, \\Delta) = {d1_f}$."
    exp_a_f = f"Tính đúng phải là $d(M, \\Delta) = \\dfrac{{{num1}}}{{{den1}}} = {d1_t} \\ne {d1_f}$."

    # Ý b): d(N, Delta') với Delta' PTTS
    u1, u2 = random.choice([(2, 3), (1, 2), (3, -2), (1, -3)])
    y0_p = random.choice([1, 2, -2, 3])
    # Delta': x = u1*t, y = y0_p + u2*t => u2*x - u1*y + u1*y0_p = 0
    A2, B2, C2 = u2, -u1, u1 * y0_p
    xN = random.choice([2, 3, 4, -2])
    yN = random.choice([-5, -3, 1, 4])
    num2 = abs(A2 * xN + B2 * yN + C2)
    while num2 == 0:
        xN += 1
        num2 = abs(A2 * xN + B2 * yN + C2)
    den2_sq = A2 * A2 + B2 * B2
    d2_t = _rat_sqrt_tex(num2, den2_sq)
    d2_f = _rat_sqrt_tex(num2 + 3, den2_sq)
    ptts_b = _ptts_tex(0, y0_p, u1, u2)
    stmt_b_t = f"$M{_pt_tex(xN, yN)}$; $\\Delta: {ptts_b}$, khi đó $d(M, \\Delta) = {d2_t}$."
    exp_b_t = f"Chuyển $\\Delta$ về PTTQ: ${_line_eq_tex(A2, B2, C2)}$. Khi đó $d(M, \\Delta) = \\dfrac{{{num2}}}{{\\sqrt{{{den2_sq}}}}} = {d2_t}$."
    stmt_b_f = f"$M{_pt_tex(xN, yN)}$; $\\Delta: {ptts_b}$, khi đó $d(M, \\Delta) = {d2_f}$."
    exp_b_f = f"Chuyển $\\Delta$ về PTTQ: ${_line_eq_tex(A2, B2, C2)}$, tính được $d(M, \\Delta) = {d2_t} \\ne {d2_f}$."

    # Ý c) và d): Hai đường thẳng song song Delta1, Delta2
    a3, b3 = random.choice([(7, 1), (3, -4), (1, -1), (2, -1)])
    c3a = random.choice([-5, -3, -1, 2])
    c3b = c3a + random.choice([5, 10, 15, 6])
    eq3a = _line_eq_tex(a3, b3, c3a)
    eq3b = _line_eq_tex(a3, b3, c3b)
    stmt_c_t = f"$\\Delta_1: {eq3a}$ và $\\Delta_2: {eq3b}$ song song với nhau."
    exp_c_t = f"Ta có $\\dfrac{{{a3}}}{{{a3}}} = \\dfrac{{{b3}}}{{{b3}}} \\ne \\dfrac{{{c3a}}}{{{c3b}}}$ nên $\\Delta_1 \\parallel \\Delta_2$."
    stmt_c_f = f"$\\Delta_1: {eq3a}$ và $\\Delta_2: {eq3b}$ cắt nhau."
    exp_c_f = f"Hai đường thẳng có cùng VTPT $({a3}; {b3})$ và hệ số tự do khác nhau (${c3a} \\ne {c3b}$) nên song song."

    den3_sq = a3 * a3 + b3 * b3
    diff_c = abs(c3a - c3b)
    d3_t = _rat_sqrt_tex(diff_c, den3_sq)
    d3_f = _rat_sqrt_tex(abs(c3a + c3b) + 1, den3_sq)
    stmt_d_t = f"$\\Delta_1: {eq3a}$ và $\\Delta_2: {eq3b}$, khi đó $d(\\Delta_1, \\Delta_2) = {d3_t}$."
    exp_d_t = f"$d(\\Delta_1, \\Delta_2) = \\dfrac{{|{c3a} - ({c3b})|}}{{\\sqrt{{{a3}^2 + ({b3})^2}}}} = \\dfrac{{{diff_c}}}{{\\sqrt{{{den3_sq}}}}} = {d3_t}$."
    stmt_d_f = f"$\\Delta_1: {eq3a}$ và $\\Delta_2: {eq3b}$, khi đó $d(\\Delta_1, \\Delta_2) = {d3_f}$."
    exp_d_f = f"Công thức đúng cho $d(\\Delta_1, \\Delta_2) = \\dfrac{{{diff_c}}}{{\\sqrt{{{den3_sq}}}}} = {d3_t} \\ne {d3_f}$."

    caudan = "Các mệnh đề sau đúng hay sai?"
    phuongan, loigiai = _make_tf_choices([
        (stmt_a_t, stmt_a_f, exp_a_t, exp_a_f),
        (stmt_b_t, stmt_b_f, exp_b_t, exp_b_f),
        (stmt_c_t, stmt_c_f, exp_c_t, exp_c_f),
        (stmt_d_t, stmt_d_f, exp_d_t, exp_d_f),
    ])
    return caudan, phuongan, loigiai


def K10_Oxy_TF_PTTS_VTCP_GiaoDiemPhanSo_SongSong():
    """Đúng/Sai: Hai đường thẳng PTTS có giao điểm phân số gọn (Ảnh 1 Câu 16)."""
    while True:
        x1, y1 = random.randint(1, 4), random.randint(1, 4)
        u1, u2 = random.choice([-1, 1, 2]), random.choice([-1, 1, -2])
        x2, y2 = random.randint(-2, 3), random.randint(-2, 3)
        v1, v2 = random.choice([2, 3, -2]), random.choice([-3, -1, 3])
        det = -u1 * v2 + u2 * v1  # giải u1*t - v1*t' = x2 - x1; u2*t - v2*t' = y2 - y1
        if det != 0:
            t_sol = Fraction(-(x2 - x1) * v2 + (y2 - y1) * v1, det)
            xM = x1 + u1 * t_sol
            yM = y1 + u2 * t_sol
            if xM.denominator > 1 or yM.denominator > 1:
                break

    d1_str = _ptts_tex(x1, y1, u1, u2)
    d2_str = _ptts_tex(x2, y2, v1, v2).replace("t", "t'")
    caudan = (
        f"Cho $\\Delta_1: {d1_str}$, $\\Delta_2: {d2_str}$.\n"
        f"Các mệnh đề sau đúng hay sai?"
    )

    stmt_a_t = f"$\\Delta_1$ có vectơ chỉ phương $\\vec{{u}}_1 = ({u1}; {u2})$."
    exp_a_t = f"Hệ số của tham số $t$ là $({u1}; {u2})$ nên đây là một VTCP của $\\Delta_1$."
    stmt_a_f = f"$\\Delta_1$ có vectơ chỉ phương $\\vec{{u}}_1 = ({x1}; {y1})$."
    exp_a_f = f"$({x1}; {y1})$ là tọa độ điểm đi qua, VTCP đúng là $({u1}; {u2})$."

    stmt_b_t = f"$\\Delta_2$ có vectơ chỉ phương $\\vec{{u}}_2 = ({v1}; {v2})$."
    exp_b_t = f"Hệ số của tham số $t'$ là $({v1}; {v2})$ nên đây là một VTCP của $\\Delta_2$."
    stmt_b_f = f"$\\Delta_2$ có vectơ chỉ phương $\\vec{{u}}_2 = ({v1}; {-v2})$."
    exp_b_f = f"VTCP đúng của $\\Delta_2$ là $({v1}; {v2})$."

    stmt_c_t = "Hai đường thẳng $\\Delta_1, \\Delta_2$ cắt nhau."
    exp_c_t = f"Vì $\\vec{{u}}_1 = ({u1}; {u2})$ và $\\vec{{u}}_2 = ({v1}; {v2})$ không cùng phương nên $\\Delta_1$ cắt $\\Delta_2$."
    stmt_c_f = "Hai đường thẳng $\\Delta_1, \\Delta_2$ song song."
    exp_c_f = f"Hai VTCP không cùng phương nên $\\Delta_1$ cắt $\\Delta_2$, không song song."

    tp_var = "t'"
    stmt_d_t = f"$\\Delta_1, \\Delta_2$ cắt nhau tại điểm có tọa độ ${_pt_tex(xM, yM)}$."
    exp_d_t = f"Giải hệ ${x1}{_signed_frac_term(u1, 't')} = {x2}{_signed_frac_term(v1, tp_var)}$, ${y1}{_signed_frac_term(u2, 't')} = {y2}{_signed_frac_term(v2, tp_var)}$ được $t = {_frac_tex(t_sol)}$, giao điểm là ${_pt_tex(xM, yM)}$."
    stmt_d_f = f"$\\Delta_1, \\Delta_2$ cắt nhau tại điểm có tọa độ ${_pt_tex(xM + 1, yM)}$."
    exp_d_f = f"Tọa độ giao điểm đúng là ${_pt_tex(xM, yM)}$."

    phuongan, loigiai = _make_tf_choices([
        (stmt_a_t, stmt_a_f, exp_a_t, exp_a_f),
        (stmt_b_t, stmt_b_f, exp_b_t, exp_b_f),
        (stmt_c_t, stmt_c_f, exp_c_t, exp_c_f),
        (stmt_d_t, stmt_d_f, exp_d_t, exp_d_f),
    ])
    return caudan, phuongan, loigiai


def K10_Oxy_TF_ChuyenDongThangDeu_Oxy():
    """Đúng/Sai: Bài toán thực tế chuyển động thẳng đều của vật thể trên Oxy (Ảnh 2 Câu 13)."""
    x0 = random.randint(1, 6)
    y0 = random.randint(1, 6)
    while True:
        v1 = random.choice([1, 2, 3])
        v2 = random.choice([1, 2, 3, 4])
        if v1 != v2 and math.gcd(v1, v2) == 1:
            break
    T = random.choice([3, 4, 5, 6])
    # Đường thẳng: v2*x - v1*y - (v2*x0 - v1*y0) = 0
    A, B, C = _reduce_abc(v2, -v1, -(v2 * x0 - v1 * y0))
    eq_ok = _line_eq_tex(A, B, C)
    # Phương trình sai (nhầm thứ tự hoặc sai dấu)
    eq_bad = _line_eq_tex(v1, v2, -(v1 * x0 + v2 * y0))

    dist_sq = T * T * (v1 * v1 + v2 * v2)
    dist_t = _sqrt_tex(dist_sq)
    dist_f = _sqrt_tex((T - 1) * (T - 1) * (v1 * v1 + v2 * v2))

    caudan = (
        f"Chuyển động của vật thể $M$ được thể hiện trên mặt phẳng tọa độ $Oxy$. "
        f"Vật thể $M$ khởi hành từ điểm $A{_pt_tex(x0, y0)}$ và chuyển động thẳng đều với vectơ vận tốc là $\\vec{{v}}{_vec_tex(v1, v2)}$. "
        f"Các mệnh đề sau đúng hay sai?"
    )

    stmt_a_t = f"Vectơ chỉ phương của đường thẳng biểu diễn chuyển động của vật thể là $\\vec{{v}}{_vec_tex(v1, v2)}$."
    exp_a_t = f"Vật thể chuyển động thẳng đều theo hướng vectơ vận tốc $\\vec{{v}}{_vec_tex(v1, v2)}$ nên $\\vec{{v}}$ là một VTCP."
    stmt_a_f = f"Vectơ chỉ phương của đường thẳng biểu diễn chuyển động của vật thể là $\\vec{{u}}{_vec_tex(v2, v1)}$."
    exp_a_f = f"VTCP đúng là vectơ vận tốc $\\vec{{v}}{_vec_tex(v1, v2)}$."

    stmt_b_t = f"Vật thể $M$ chuyển động trên đường thẳng ${eq_ok}$."
    exp_b_t = f"Đường thẳng qua $A{_pt_tex(x0, y0)}$ có VTCP $\\vec{{v}} = ({v1}; {v2})$ nên có VTPT $({A}; {B})$, phương trình là ${eq_ok}$."
    stmt_b_f = f"Vật thể $M$ chuyển động trên đường thẳng ${eq_bad}$."
    exp_b_f = f"Phương trình đúng phải là ${eq_ok}$."

    stmt_c_t = f"Tọa độ của vật thể $M$ tại thời điểm $t$ ($t > 0$) tính từ khi khởi hành là ${_ptts_tex(x0, y0, v1, v2)}$."
    exp_c_t = f"Tọa độ chuyển động thẳng đều: $M(t) = A + t\\vec{{v}} \\Rightarrow {_ptts_tex(x0, y0, v1, v2)}$."
    stmt_c_f = f"Tọa độ của vật thể $M$ tại thời điểm $t$ ($t > 0$) tính từ khi khởi hành là ${_ptts_tex(v1, v2, x0, y0)}$."
    exp_c_f = f"Bị nhầm điểm xuất phát $A{_pt_tex(x0, y0)}$ và vận tốc $\\vec{{v}}{_vec_tex(v1, v2)}$."

    stmt_d_t = f"Khi $t = {T}$ thì vật thể $M$ chuyển động được quãng đường dài bằng ${dist_t}$."
    exp_d_t = f"Tốc độ của vật là $|\\vec{{v}}| = \\sqrt{{{v1}^2 + {v2}^2}} = {_sqrt_tex(v1*v1+v2*v2)}$. Sau $t = {T}$, quãng đường đi được là $S = {T}\\cdot {_sqrt_tex(v1*v1+v2*v2)} = {dist_t}$."
    stmt_d_f = f"Khi $t = {T}$ thì vật thể $M$ chuyển động được quãng đường dài bằng ${dist_f}$."
    exp_d_f = f"Quãng đường phải bằng $t|\\vec{{v}}| = {dist_t} \\ne {dist_f}$."

    phuongan, loigiai = _make_tf_choices([
        (stmt_a_t, stmt_a_f, exp_a_t, exp_a_f),
        (stmt_b_t, stmt_b_f, exp_b_t, exp_b_f),
        (stmt_c_t, stmt_c_f, exp_c_t, exp_c_f),
        (stmt_d_t, stmt_d_f, exp_d_t, exp_d_f),
    ])
    return caudan, phuongan, loigiai


def K10_Oxy_TF_TamGiac_TrungTruc_TrungTuyen():
    """Đúng/Sai: Tam giác ABC biết đỉnh A, đường trung trực BC và trung tuyến từ C (Ảnh 2 Câu 14)."""
    while True:
        xA = random.randint(1, 5)
        yA = random.randint(1, 5)
        # Chọn M nguyên là trung điểm BC, và B = M - v, C = M + v sao cho C khác A và B khác C
        xM = random.randint(-2, 6)
        yM = random.randint(2, 8)
        px = random.choice([-2, -1, 1, 2])
        py = random.choice([-2, -1, 1, 2])
        xB, yB = xM - px, yM - py
        xC, yC = xM + px, yM + py
        # Kiểm tra không thẳng hàng
        if (xB - xA) * (yC - yA) - (yB - yA) * (xC - xA) == 0:
            continue
        # Trung điểm N của AB
        xN = Fraction(xA + xB, 2)
        yN = Fraction(yA + yB, 2)
        # d_tt đi qua M và nhận (px, py) làm VTPT: px*x + py*y + c_tt = 0
        a_tt, b_tt, c_tt = _reduce_abc(px, py, -(px * xM + py * yM))
        # d_CM đi qua C và N:
        # Chiều (xC - xN, yC - yN) -> VTPT (-dy_cm, dx_cm) -> nhân 2 để nguyên
        dx2 = int(2 * (xC - xN))
        dy2 = int(2 * (yC - yN))
        if dx2 == 0 and dy2 == 0:
            continue
        a_cm, b_cm, c_cm = _reduce_abc(-dy2, dx2, -(-dy2 * xC + dx2 * yC))
        # Kiểm tra hệ giải M, C duy nhất: det của n_tt (trên d_tt) và n_cm
        # M nằm trên d_tt và C nằm trên d_cm, kiểm tra d_BC // ... không song song d_cm
        if a_tt * b_cm - a_cm * b_tt == 0:
            continue
        break

    # Phương trình BC: qua M(xM, yM) vuông góc d_tt -> nhận (b_tt, -a_tt) = (py, -px) làm VTPT
    a_bc, b_bc, c_bc = _reduce_abc(py, -px, -(py * xM - px * yM))

    caudan = (
        f"Trong mặt phẳng tọa độ $Oxy$, cho tam giác $ABC$ có $A{_pt_tex(xA, yA)}$, "
        f"đường trung trực cạnh $BC$ có phương trình ${_line_eq_tex(a_tt, b_tt, c_tt)}$, "
        f"đường trung tuyến kẻ từ $C$ có phương trình ${_line_eq_tex(a_cm, b_cm, c_cm)}$. Xét tính đúng sai các mệnh đề sau"
    )

    stmt_a_t = f"Gọi $M$ là trung điểm cạnh $BC$. Khi đó $M{_pt_tex(xM, yM)}$."
    exp_a_t = f"Vì $BC$ vuông góc với đường trung trực nên $BC: {_line_eq_tex(a_bc, b_bc, c_bc)}$. Giao điểm $M = BC \\cap d_{{tt}}$ là $M{_pt_tex(xM, yM)}$."
    stmt_a_f = f"Gọi $M$ là trung điểm cạnh $BC$. Khi đó $M{_pt_tex(xM + 1, yM - 2)}$."
    exp_a_f = f"Giải đúng hệ tìm được trung điểm $M{_pt_tex(xM, yM)}$."

    stmt_b_t = f"Phương trình đường thẳng $BC$ là ${_line_eq_tex(a_bc, b_bc, c_bc)}$."
    exp_b_t = f"Đường thẳng $BC$ đi qua $M{_pt_tex(xM, yM)}$ và vuông góc đường trung trực nên có phương trình ${_line_eq_tex(a_bc, b_bc, c_bc)}$."
    stmt_b_f = f"Phương trình đường thẳng $BC$ là ${_line_eq_tex(a_bc, b_bc, c_bc + 3)}$."
    exp_b_f = f"Phương trình đúng của $BC$ là ${_line_eq_tex(a_bc, b_bc, c_bc)}$."

    stmt_c_t = f"Tọa độ đỉnh $C$ là $C{_pt_tex(xC, yC)}$."
    exp_c_t = f"Giao điểm của $BC$ và trung tuyến kẻ từ $C$ là $C{_pt_tex(xC, yC)}$."
    stmt_c_f = f"Tọa độ đỉnh $C$ là $C{_pt_tex(-xC, yC + 1)}$."
    exp_c_f = f"Giải hệ $BC$ và trung tuyến kẻ từ $C$ được $C{_pt_tex(xC, yC)}$."

    stmt_d_t = f"Tọa độ đỉnh $B$ là $B{_pt_tex(xB, yB)}$."
    exp_d_t = f"Vì $M$ là trung điểm $BC$ nên $B = 2M - C = {_pt_tex(xB, yB)}$."
    stmt_d_f = f"Tọa độ đỉnh $B$ là $B{_pt_tex(xB + 2, yB - 1)}$."
    exp_d_f = f"Tính $B = 2M - C$ cho $B{_pt_tex(xB, yB)}$."

    phuongan, loigiai = _make_tf_choices([
        (stmt_a_t, stmt_a_f, exp_a_t, exp_a_f),
        (stmt_b_t, stmt_b_f, exp_b_t, exp_b_f),
        (stmt_c_t, stmt_c_f, exp_c_t, exp_c_f),
        (stmt_d_t, stmt_d_f, exp_d_t, exp_d_f),
    ])
    return caudan, phuongan, loigiai


def K10_Oxy_TF_HinhChuNhat_TamI_TrungDiem():
    """Đúng/Sai: Hình chữ nhật ABCD tâm I, M trên AB, N trên BC, trung điểm E của CD thuộc Delta (Ảnh 2 Câu 15)."""
    while True:
        xI = random.randint(2, 7)
        yI = random.randint(1, 5)
        e1, e2 = random.choice([(3, 0), (0, 3), (2, 1), (1, -2), (-2, 1)])
        xE, yE = xI + e1, yI + e2
        xF, yF = xI - e1, yI - e2
        # AB qua F với direction (-e2, e1)
        kB = random.choice([2, 3])
        kM = random.choice([-2, -1, 1])
        if abs(kM) == abs(kB):
            continue
        xB, yB = xF - kB * e2, yF + kB * e1
        xA, yA = xF + kB * e2, yF - kB * e1
        xM, yM = xF - kM * e2, yF + kM * e1
        # N thuộc BC (BC đi từ B theo +e)
        xN, yN = xB + e1, yB + e2

        # Chọn Delta đi qua E(xE, yE) với hướng (d1, d2), đảm bảo nghiệm thứ 2 E' có xE' != xE và d1 != 0
        d1, d2 = random.choice([(1, -1), (1, 1), (1, -2), (2, -1)])
        vec_m = (xM - xI, yM - yI)
        num_t2 = -(2 * (e1 * d1 + e2 * d2) + (vec_m[0] * d1 + vec_m[1] * d2))
        den_t2 = d1 * d1 + d2 * d2
        t2 = Fraction(num_t2, den_t2)
        if t2 == 0:
            continue
        xE2 = xE + t2 * d1
        if xE2 == xE:
            continue
        break

    # Delta: d2*x - d1*y + c_del = 0
    a_del, b_del, c_del = _reduce_abc(d2, -d1, -(d2 * xE - d1 * yE))
    # Bound K nguyên giữa xE và xE2
    if xE < xE2:
        k_bound = math.floor(xE) + 1
        while k_bound >= xE2:
            # Nếu xE2 < xE + 1 thì dùng < (xE + xE2)/2
            break
        cond_str = f"nhỏ hơn {_frac_tex(Fraction(xE + xE2, 2))}" if k_bound >= xE2 else f"nhỏ hơn {k_bound}"
    else:
        k_bound = math.ceil(xE) - 1
        cond_str = f"lớn hơn {_frac_tex(Fraction(xE + xE2, 2))}" if k_bound <= xE2 else f"lớn hơn {k_bound}"

    # Phương trình BC: qua B, N -> VTCP (e1, e2), VTPT (e2, -e1)
    a_bc, b_bc, c_bc = _reduce_abc(e2, -e1, -(e2 * xB - e1 * yB))
    # Phương trình AB: qua F, M -> VTPT (e1, e2)
    a_ab, b_ab, c_ab = _reduce_abc(e1, e2, -(e1 * xF + e2 * yF))

    caudan = (
        f"Trong mặt phẳng tọa độ $Oxy$, cho hình chữ nhật $ABCD$ có tâm $I{_pt_tex(xI, yI)}$ "
        f"và các điểm $M{_pt_tex(xM, yM)}$, $N{_pt_tex(xN, yN)}$ lần lượt thuộc các đường thẳng $AB, BC$. "
        f"Biết rằng trung điểm $E$ của cạnh $CD$ thuộc đường thẳng $\\Delta: {_line_eq_tex(a_del, b_del, c_del)}$ "
        f"và hoành độ của điểm $E$ {cond_str}. Khi đó"
    )

    stmt_a_t = f"Phương trình $BC$ là ${_line_eq_tex(a_bc, b_bc, c_bc)}$."
    exp_a_t = f"Tìm được $E{_pt_tex(xE, yE)}$ thỏa mãn $\\overrightarrow{{IE}} \\cdot (\\overrightarrow{{IE}} + \\overrightarrow{{IM}}) = 0$ và điều kiện hoành độ. Đường thẳng $BC$ qua $N{_pt_tex(xN, yN)}$ và song song $IE$ nên có phương trình ${_line_eq_tex(a_bc, b_bc, c_bc)}$."
    stmt_a_f = f"Phương trình $BC$ là ${_line_eq_tex(a_bc, b_bc, c_bc + 2)}$."
    exp_a_f = f"Phương trình đúng của $BC$ là ${_line_eq_tex(a_bc, b_bc, c_bc)}$."

    stmt_b_t = f"Phương trình $AB$ là ${_line_eq_tex(a_ab, b_ab, c_ab)}$."
    exp_b_t = f"Đường thẳng $AB$ đi qua $M{_pt_tex(xM, yM)}$ và nhận $\\overrightarrow{{IE}} = ({e1}; {e2})$ làm VTPT nên có phương trình ${_line_eq_tex(a_ab, b_ab, c_ab)}$."
    stmt_b_f = f"Phương trình $AB$ là ${_line_eq_tex(a_ab, b_ab, c_ab - 3)}$."
    exp_b_f = f"Phương trình đúng của $AB$ là ${_line_eq_tex(a_ab, b_ab, c_ab)}$."

    stmt_c_t = f"Tọa độ điểm $A$ là $A{_pt_tex(xA, yA)}$."
    exp_c_t = f"Trung điểm $F$ của $AB$ đối xứng $E$ qua $I$ nên $F{_pt_tex(xF, yF)}$; từ $B = AB \\cap BC$ suy ra $A = 2F - B = {_pt_tex(xA, yA)}$."
    stmt_c_f = f"Tọa độ điểm $A$ là $A{_pt_tex(xA + 1, yA - 1)}$."
    exp_c_f = f"Tọa độ đúng là $A{_pt_tex(xA, yA)}$."

    stmt_d_t = f"Tọa độ điểm $B$ là $B{_pt_tex(xB, yB)}$."
    exp_d_t = f"Giao điểm $B$ của $AB$ và $BC$ là $B{_pt_tex(xB, yB)}$."
    stmt_d_f = f"Tọa độ điểm $B$ là $B{_pt_tex(xB - 1, yB + 2)}$."
    exp_d_f = f"Giao điểm đúng là $B{_pt_tex(xB, yB)}$."

    phuongan, loigiai = _make_tf_choices([
        (stmt_a_t, stmt_a_f, exp_a_t, exp_a_f),
        (stmt_b_t, stmt_b_f, exp_b_t, exp_b_f),
        (stmt_c_t, stmt_c_f, exp_c_t, exp_c_f),
        (stmt_d_t, stmt_d_f, exp_d_t, exp_d_f),
    ])
    return caudan, phuongan, loigiai


def K10_Oxy_TF_DuongTron_QuaBaDiem():
    """Đúng/Sai: Đường tròn (C) đi qua 3 điểm A, B, C có tâm I (Ảnh 3 Câu 13)."""
    while True:
        xB = random.randint(-2, 2)
        yB = random.randint(-4, 0)
        dx_bc = random.choice([3, 4, 5, 6])
        xC, yC = xB + dx_bc, yB
        xA = xB + random.choice([1, 2, 3])
        yA = yB + random.choice([2, 3, 4])
        # Giải tâm I(xI, yI) của tam giác vuông/thường với BC ngang
        # IB^2 = IC^2 => xI = (xB + xC)/2
        xI = Fraction(xB + xC, 2)
        # IA^2 = IB^2 => (xA - xI)^2 + (yA - yI)^2 = (xB - xI)^2 + (yB - yI)^2
        # => (yA^2 - yB^2) - 2(yA - yB)*yI = (xB - xI)^2 - (xA - xI)^2
        rhs = (xB - xI) ** 2 - (xA - xI) ** 2 + (yB ** 2 - yA ** 2)
        yI = Fraction(rhs, 2 * (yB - yA))
        R2 = (xA - xI) ** 2 + (yA - yI) ** 2
        if R2 > 0 and (xI != 0 or yI != 0) and (4 * R2).denominator == 1:
            break

    diam_tex = _sqrt_frac_tex(4 * R2)
    diam_wrong = _sqrt_frac_tex(R2)
    io_tex = _sqrt_frac_tex(xI ** 2 + yI ** 2)
    io_wrong = _sqrt_frac_tex(4 * (xI ** 2 + yI ** 2) + 1)

    # Điểm N đối xứng A qua đường thẳng x = xI (nếu 2*xI nguyên thì xN nguyên!)
    xN_on = 2 * xI - xA
    yN_on = yA
    if xN_on == xA:
        xN_on, yN_on = xB, 2 * yI - yB
    if xN_on == xC and yN_on == yC:
        xN_on, yN_on = 2 * xI - xC, 2 * yI - yC
    xN_off = xN_on + 1
    yN_off = yN_on

    caudan = (
        f"Trong mặt phẳng $Oxy$, cho đường tròn $(C)$ đi qua ba điểm "
        f"$A{_pt_tex(xA, yA)}$, $B{_pt_tex(xB, yB)}$, $C{_pt_tex(xC, yC)}$ có tâm $I$."
    )

    stmt_a_t = f"Đường kính của đường tròn $(C)$ bằng ${diam_tex}$."
    exp_a_t = f"Giải hệ $IA^2 = IB^2 = IC^2$ được tâm $I{_pt_tex(xI, yI)}$ và $R^2 = {_frac_tex(R2)}$, suy ra đường kính $2R = {diam_tex}$."
    stmt_a_f = f"Đường kính của đường tròn $(C)$ bằng ${diam_wrong}$."
    exp_a_f = f"${diam_wrong}$ là bán kính $R$, đường kính phải là $2R = {diam_tex}$."

    stmt_b_t = f"Tung độ của $I$ là ${_frac_tex(yI)}$."
    exp_b_t = f"Từ $IA^2 = IB^2 = IC^2$ tìm được $I{_pt_tex(xI, yI)}$ nên $y_I = {_frac_tex(yI)}$."
    stmt_b_f = f"Tung độ của $I$ là ${_frac_tex(-yI if yI != 0 else 1)}$."
    exp_b_f = f"Tung độ đúng của $I$ là ${_frac_tex(yI)}$."

    stmt_c_t = f"Đường tròn $(C)$ đi qua điểm $N{_pt_tex(xN_on, yN_on)}$."
    exp_c_t = f"Ta có $IN^2 = ({_frac_tex(xN_on - xI)})^2 + ({_frac_tex(yN_on - yI)})^2 = {_frac_tex(R2)} = R^2$ nên $N \\in (C)$."
    stmt_c_f = f"Đường tròn $(C)$ đi qua điểm $N{_pt_tex(xN_off, yN_off)}$."
    off_r2 = (xN_off - xI) ** 2 + (yN_off - yI) ** 2
    exp_c_f = f"Ta có $IN^2 = {_frac_tex(off_r2)} \\ne R^2 = {_frac_tex(R2)}$ nên $N \\notin (C)$."

    stmt_d_t = f"$IO = {io_tex}$."
    exp_d_t = f"$IO = \\sqrt{{x_I^2 + y_I^2}} = {io_tex}$."
    stmt_d_f = f"$IO = {io_wrong}$."
    exp_d_f = f"Tính đúng phải là $IO = {io_tex}$."

    phuongan, loigiai = _make_tf_choices([
        (stmt_a_t, stmt_a_f, exp_a_t, exp_a_f),
        (stmt_b_t, stmt_b_f, exp_b_t, exp_b_f),
        (stmt_c_t, stmt_c_f, exp_c_t, exp_c_f),
        (stmt_d_t, stmt_d_f, exp_d_t, exp_d_f),
    ])
    return caudan, phuongan, loigiai


def K10_Oxy_TF_DuongTron_QuaA_TiepXucDeltaTaiB():
    """Đúng/Sai: Đường tròn (C) qua điểm A và tiếp xúc đường thẳng Delta tại B (Ảnh 3 Câu 14)."""
    # Dùng vector trực giao từ tâm I đến B và A: bộ (3, -4) -> R = 5
    k = random.choice([1, 2])
    u, v = random.choice([(3, -4), (4, 3), (-3, 4)])
    xI = random.randint(-2, 3)
    yI = random.randint(-3, 2)
    xB, yB = xI + k * u, yI + k * v
    # A là điểm nguyên khác trên (C): I + k*(-v, u) hoặc I - k*(u, v)
    xA, yA = xI - k * v, yI + k * u
    R = 5 * k
    R2 = R * R
    # Delta qua B có VTPT (u, v)
    A_d, B_d, C_d = _reduce_abc(u, v, -(u * xB + v * yB))
    io2 = xI * xI + yI * yI
    o_in = io2 < R2
    if io2 == R2:
        xI += 1
        xB += 1
        xA += 1
        A_d, B_d, C_d = _reduce_abc(u, v, -(u * xB + v * yB))
        io2 = xI * xI + yI * yI
        o_in = io2 < R2

    caudan = (
        f"Trong mặt phẳng $Oxy$, đường tròn $(C)$ đi qua điểm $A{_pt_tex(xA, yA)}$ và tiếp xúc với đường thẳng "
        f"$\\Delta: {_line_eq_tex(A_d, B_d, C_d)}$ tại $B{_pt_tex(xB, yB)}$. Khi đó"
    )

    stmt_a_t = f"Đường kính của $(C)$ bằng ${2 * R}$."
    exp_a_t = f"Tâm $I$ là giao điểm của đường trung trực $AB$ và đường thẳng qua $B$ vuông góc $\\Delta$, giải ra $I{_pt_tex(xI, yI)}$, $R = IB = {R} \\Rightarrow 2R = {2 * R}$."
    stmt_a_f = f"Đường kính của $(C)$ bằng ${R}$."
    exp_a_f = f"Bán kính $R = {R}$ nên đường kính là $2R = {2 * R}$."

    stmt_b_t = f"Tâm của $(C)$ có tung độ bằng ${yI}$."
    exp_b_t = f"Tìm được tâm $I{_pt_tex(xI, yI)}$ nên $y_I = {yI}$."
    stmt_b_f = f"Tâm của $(C)$ có tung độ bằng ${yI + 2}$."
    exp_b_f = f"Tung độ đúng của tâm $I$ là ${yI}$."

    stmt_c_t = f"Khoảng cách từ tâm của đường tròn $(C)$ đến đường thẳng $\\Delta$ bằng ${R}$."
    exp_c_t = f"Vì $(C)$ tiếp xúc $\\Delta$ nên $d(I, \\Delta) = R = {R}$."
    stmt_c_f = f"Khoảng cách từ tâm của đường tròn $(C)$ đến đường thẳng $\\Delta$ bằng ${R - 1}$."
    exp_c_f = f"Vì tiếp xúc nên $d(I, \\Delta) = R = {R} \\ne {R - 1}$."

    if o_in:
        stmt_d_t = "Điểm $O(0; 0)$ nằm bên trong đường tròn $(C)$."
        stmt_d_f = "Điểm $O(0; 0)$ nằm bên ngoài đường tròn $(C)$."
        exp_d = f"Ta có $IO^2 = {xI}^2 + ({yI})^2 = {io2} < R^2 = {R2}$ nên $O(0; 0)$ nằm bên trong $(C)$."
    else:
        stmt_d_t = "Điểm $O(0; 0)$ nằm bên ngoài đường tròn $(C)$."
        stmt_d_f = "Điểm $O(0; 0)$ nằm bên trong đường tròn $(C)$."
        exp_d = f"Ta có $IO^2 = {xI}^2 + ({yI})^2 = {io2} > R^2 = {R2}$ nên $O(0; 0)$ nằm bên ngoài $(C)$."

    phuongan, loigiai = _make_tf_choices([
        (stmt_a_t, stmt_a_f, exp_a_t, exp_a_f),
        (stmt_b_t, stmt_b_f, exp_b_t, exp_b_f),
        (stmt_c_t, stmt_c_f, exp_c_t, exp_c_f),
        (stmt_d_t, stmt_d_f, exp_d, exp_d),
    ])
    return caudan, phuongan, loigiai


def K10_Oxy_TF_DuongTron_QuaA_TiepXucTaiM_TongQuat():
    """Đúng/Sai: (C) qua A tiếp xúc đường thẳng d tại M - giải hệ phân số, tiếp xúc y = k, vị trí O (Ảnh 3 Câu 15)."""
    while True:
        xM = random.randint(-2, 2)
        yM = random.randint(-3, 2)
        ad, bd = random.choice([(3, -2), (2, -3), (1, -2), (2, 1)])
        cd = -(ad * xM + bd * yM)
        # Đường thẳng Delta qua M vuông góc d: có VTCP (ad, bd) -> tâm I(t) = (xM + ad*t, yM + bd*t)
        # VTPT của Delta là (bd, -ad)
        xA = random.randint(-3, 3)
        yA = random.randint(-2, 3)
        if ad * xA + bd * yA + cd == 0:
            continue
        # IA^2 = IM^2 <=> (xM + ad*t - xA)^2 + (yM + bd*t - yA)^2 = (ad^2 + bd^2)*t^2
        # Đặt dx = xM - xA, dy = yM - yA => 2*(dx*ad + dy*bd)*t + dx^2 + dy^2 = 0
        dx, dy = xM - xA, yM - yA
        denom_t = 2 * (dx * ad + dy * bd)
        if denom_t == 0:
            continue
        t_sol = Fraction(-(dx * dx + dy * dy), denom_t)
        xI = xM + ad * t_sol
        yI = yM + bd * t_sol
        R2 = (xI - xM) ** 2 + (yI - yM) ** 2
        io2 = xI ** 2 + yI ** 2
        if io2 != R2 and R2 > 0:
            break

    a_perp, b_perp, c_perp = _reduce_abc(bd, -ad, -(bd * xM - ad * yM))
    # Đường thẳng ngang y = k_line tiếp xúc hay không: chọn k_line = yA -> tiếp xúc nếu R^2 == (yI - yA)^2
    y_test = yA
    is_tan_y = (yI - y_test) ** 2 == R2
    o_out = io2 > R2

    caudan = (
        f"Trong mặt phẳng $Oxy$, cho $(C)$ đi qua $A{_pt_tex(xA, yA)}$ và tiếp xúc với đường thẳng "
        f"$d: {_line_eq_tex(ad, bd, cd)}$ tại $M{_pt_tex(xM, yM)}$. Khi đó"
    )

    stmt_a_t = f"Đường thẳng qua $M{_pt_tex(xM, yM)}$ và vuông góc với $d$ là $\\Delta: {_line_eq_tex(a_perp, b_perp, c_perp)}$."
    exp_a_t = f"Đường thẳng $\\Delta \\perp d$ qua $M{_pt_tex(xM, yM)}$ nhận VTCP của $d$ là $({b_perp}; {-a_perp})$ hay VTPT $({a_perp}; {b_perp})$ nên có phương trình ${_line_eq_tex(a_perp, b_perp, c_perp)}$."
    stmt_a_f = f"Đường thẳng qua $M{_pt_tex(xM, yM)}$ và vuông góc với $d$ là $\\Delta: {_line_eq_tex(ad, bd, -(ad * xM - bd * yM) + 2)}$."
    exp_a_f = f"Phương trình đúng phải là ${_line_eq_tex(a_perp, b_perp, c_perp)}$."

    stmt_b_t = f"Hoành độ tâm của đường tròn $(C)$ bằng ${_frac_tex(xI)}$."
    exp_b_t = f"Tâm $I \\in \\Delta$ nên $I({xM}{_signed_frac_term(ad, 't')};\\,{yM}{_signed_frac_term(bd, 't')})$. Giải $IA^2 = IM^2$ được $t = {_frac_tex(t_sol)}$, suy ra $I{_pt_tex(xI, yI)}$."
    stmt_b_f = f"Hoành độ tâm của đường tròn $(C)$ bằng ${_frac_tex(xI + 1)}$."
    exp_b_f = f"Hoành độ đúng của tâm $I$ là ${_frac_tex(xI)}$."

    if is_tan_y:
        stmt_c_t = f"Đường tròn $(C)$ tiếp xúc với đường thẳng $y = {y_test}$."
        stmt_c_f = f"Đường tròn $(C)$ không tiếp xúc với đường thẳng $y = {y_test}$."
        exp_c = f"Khoảng cách từ $I$ đến $y = {y_test}$ là $|{_frac_tex(yI - y_test)}|$, bình phương bằng $R^2 = {_frac_tex(R2)}$ nên có tiếp xúc."
    else:
        stmt_c_t = f"Đường tròn $(C)$ không tiếp xúc với đường thẳng $y = {y_test}$."
        stmt_c_f = f"Đường tròn $(C)$ tiếp xúc với đường thẳng $y = {y_test}$."
        exp_c = f"Ta có $[d(I, y={y_test})]^2 = {_frac_tex((yI - y_test)**2)} \\ne R^2 = {_frac_tex(R2)}$ nên không tiếp xúc."

    if o_out:
        stmt_d_t = "Điểm $O(0; 0)$ nằm ngoài đường tròn $(C)$."
        stmt_d_f = "Điểm $O(0; 0)$ nằm trong đường tròn $(C)$."
        exp_d = f"$IO^2 = {_frac_tex(io2)} > R^2 = {_frac_tex(R2)}$ nên $O(0; 0)$ nằm ngoài $(C)$."
    else:
        stmt_d_t = "Điểm $O(0; 0)$ nằm trong đường tròn $(C)$."
        stmt_d_f = "Điểm $O(0; 0)$ nằm ngoài đường tròn $(C)$."
        exp_d = f"$IO^2 = {_frac_tex(io2)} < R^2 = {_frac_tex(R2)}$ nên $O(0; 0)$ nằm trong $(C)$."

    phuongan, loigiai = _make_tf_choices([
        (stmt_a_t, stmt_a_f, exp_a_t, exp_a_f),
        (stmt_b_t, stmt_b_f, exp_b_t, exp_b_f),
        (stmt_c_t, stmt_c_f, exp_c, exp_c),
        (stmt_d_t, stmt_d_f, exp_d, exp_d),
    ])
    return caudan, phuongan, loigiai


def K10_Oxy_TF_DuongTron_TamBanKinh_TiepTuyen():
    """Đúng/Sai: (C): (x - a)^2 + (y - b)^2 = R^2 - tâm, bán kính, tiếp tuyến tại M, số tiếp tuyến vuông góc Delta (Ảnh 3 Câu 16)."""
    a = random.choice([-4, -3, -2, 1, 2, 3])
    b = random.choice([-4, -3, -2, 1, 2, 3])
    while abs(a) == abs(b):
        b = random.choice([-5, -3, 2, 4])
    R, dx, dy = random.choice([(5, 3, 4), (5, 4, -3), (5, -3, 4), (10, 6, 8), (13, 5, 12)])
    R2 = R * R
    xM, yM = a + dx, b + dy
    A_t, B_t, C_t = _reduce_abc(dx, dy, -(dx * xM + dy * yM))

    caudan = f"Trong mặt phẳng $Oxy$, cho đường tròn $(C): {_circle_std_tex(a, b, R2)}$. Khi đó"

    stmt_a_t = f"Đường tròn $(C)$ có tâm $I{_pt_tex(a, b)}$."
    exp_a_t = f"Từ phương trình chính tắc $(C)$ suy ra tâm $I{_pt_tex(a, b)}$."
    stmt_a_f = f"Đường tròn $(C)$ có tâm $I{_pt_tex(-a, -b)}$."
    exp_a_f = f"Nhầm dấu tọa độ tâm; tâm đúng là $I{_pt_tex(a, b)}$."

    stmt_b_t = f"Đường tròn $(C)$ có bán kính $R = {R}$."
    exp_b_t = f"Ta có $R^2 = {R2} \\Rightarrow R = {R}$."
    stmt_b_f = f"Đường tròn $(C)$ có bán kính $R = {R2}$."
    exp_b_f = f"$R = \\sqrt{{{R2}}} = {R} \\ne {R2}$."

    stmt_c_t = f"Phương trình tiếp tuyến $\\Delta$ của $(C)$ tại điểm $M{_pt_tex(xM, yM)}$ là ${_line_eq_tex(A_t, B_t, C_t)}$."
    exp_c_t = f"Điểm $M \\in (C)$, tiếp tuyến $\\Delta$ qua $M$ nhận $\\overrightarrow{{IM}} = ({dx}; {dy})$ làm VTPT nên có PT ${_line_eq_tex(A_t, B_t, C_t)}$."
    stmt_c_f = f"Phương trình tiếp tuyến $\\Delta$ của $(C)$ tại điểm $M{_pt_tex(xM, yM)}$ là ${_line_eq_tex(*_reduce_abc(A_t, -B_t, -(A_t * xM - B_t * yM)))}$."
    exp_c_f = f"Phương trình đúng của tiếp tuyến tại $M$ là ${_line_eq_tex(A_t, B_t, C_t)}$."

    stmt_d_t = "Có hai phương trình tiếp tuyến $\\Delta'$ của đường tròn $(C)$ biết $\\Delta'$ vuông góc với $\\Delta$."
    exp_d_t = "Ứng với phương vuông góc với $\\Delta$, luôn có đúng hai tiếp tuyến đối xứng nhau qua tâm $I$."
    stmt_d_f = "Chỉ có duy nhất một tiếp tuyến $\\Delta'$ của đường tròn $(C)$ biết $\\Delta'$ vuông góc với $\\Delta$."
    exp_d_f = "Luôn có đúng hai tiếp tuyến của $(C)$ vuông góc với đường thẳng $\\Delta$ cho trước."

    phuongan, loigiai = _make_tf_choices([
        (stmt_a_t, stmt_a_f, exp_a_t, exp_a_f),
        (stmt_b_t, stmt_b_f, exp_b_t, exp_b_f),
        (stmt_c_t, stmt_c_f, exp_c_t, exp_c_f),
        (stmt_d_t, stmt_d_f, exp_d_t, exp_d_f),
    ])
    return caudan, phuongan, loigiai


def K10_Oxy_TF_DuongTron_TamI_TiepXucDelta_TiepDiem():
    """Đúng/Sai: Tâm I tiếp xúc Delta (có R chứa căn) - khoảng cách, đường kính, PT, dấu hoành độ tiếp điểm (Ảnh 4 Câu 13)."""
    while True:
        a = random.randint(-3, 3)
        b = random.randint(-3, 3)
        A, B = random.choice([(1, -2), (2, 1), (1, 3), (2, -3)])
        C = random.choice([3, 5, 7, -4, -6])
        num = abs(A * a + B * b + C)
        if num > 0:
            break
    den_sq = A * A + B * B
    R2 = Fraction(num * num, den_sq)
    R_tex = _rat_sqrt_tex(num, den_sq)
    R_wrong = _rat_sqrt_tex(num + 1, den_sq)
    diam_tex = _rat_sqrt_tex(2 * num, den_sq)
    diam_wrong = _rat_sqrt_tex(2 * num + 2, den_sq)

    # Tiếp điểm H = I - ((Aa+Bb+C)/(A^2+B^2)) * (A, B)
    k_h = Fraction(A * a + B * b + C, den_sq)
    xH = a - k_h * A
    while xH == 0:
        C += 1
        num = abs(A * a + B * b + C)
        R2 = Fraction(num * num, den_sq)
        R_tex = _rat_sqrt_tex(num, den_sq)
        R_wrong = _rat_sqrt_tex(num + 1, den_sq)
        diam_tex = _rat_sqrt_tex(2 * num, den_sq)
        diam_wrong = _rat_sqrt_tex(2 * num + 2, den_sq)
        k_h = Fraction(A * a + B * b + C, den_sq)
        xH = a - k_h * A

    caudan = (
        f"Trong mặt phẳng $Oxy$, cho đường tròn $(C)$ có tâm $I{_pt_tex(a, b)}$ và tiếp xúc với "
        f"đường thẳng $\\Delta: {_line_eq_tex(A, B, C)}$."
    )

    stmt_a_t = f"$d(I, \\Delta) = {R_tex}$."
    exp_a_t = f"$d(I, \\Delta) = \\dfrac{{|{A}({a}) + ({B})({b}) + ({C})|}}{{\\sqrt{{{A}^2 + ({B})^2}}}} = {R_tex}$."
    stmt_a_f = f"$d(I, \\Delta) = {R_wrong}$."
    exp_a_f = f"Tính đúng được $d(I, \\Delta) = {R_tex} \\ne {R_wrong}$."

    stmt_b_t = f"Đường kính của đường tròn có độ dài bằng ${diam_tex}$."
    exp_b_t = f"$R = d(I, \\Delta) = {R_tex} \\Rightarrow 2R = {diam_tex}$."
    stmt_b_f = f"Đường kính của đường tròn có độ dài bằng ${diam_wrong}$."
    exp_b_f = f"Đường kính đúng là $2R = {diam_tex}$."

    stmt_c_t = f"Phương trình đường tròn là ${_circle_std_tex(a, b, R2)}$."
    exp_c_t = f"Tâm $I{_pt_tex(a, b)}$ và $R^2 = {_frac_tex(R2)}$ nên PT là ${_circle_std_tex(a, b, R2)}$."
    stmt_c_f = f"Phương trình đường tròn là ${_circle_std_tex(a, b, R2 + 1)}$."
    exp_c_f = f"Vế phải là $R^2 = {_frac_tex(R2)}$."

    if xH > 0:
        stmt_d_t = "Đường tròn $(C)$ tiếp xúc với đường thẳng $\\Delta$ tại điểm có hoành độ lớn hơn $0$."
        stmt_d_f = "Đường tròn $(C)$ tiếp xúc với đường thẳng $\\Delta$ tại điểm có hoành độ nhỏ hơn $0$."
    else:
        stmt_d_t = "Đường tròn $(C)$ tiếp xúc với đường thẳng $\\Delta$ tại điểm có hoành độ nhỏ hơn $0$."
        stmt_d_f = "Đường tròn $(C)$ tiếp xúc với đường thẳng $\\Delta$ tại điểm có hoành độ lớn hơn $0$."
    exp_d = f"Tiếp điểm $H$ là hình chiếu của $I$ lên $\\Delta$, giải ra $x_H = {_frac_tex(xH)}$."

    phuongan, loigiai = _make_tf_choices([
        (stmt_a_t, stmt_a_f, exp_a_t, exp_a_f),
        (stmt_b_t, stmt_b_f, exp_b_t, exp_b_f),
        (stmt_c_t, stmt_c_f, exp_c_t, exp_c_f),
        (stmt_d_t, stmt_d_f, exp_d, exp_d),
    ])
    return caudan, phuongan, loigiai


def K10_Oxy_TF_DuongTron_QuaAB_TamTrenDelta():
    """Đúng/Sai: (C) qua A, B và tâm thuộc Delta - tìm tâm I, vị trí O(0;0), bán kính/đường kính, điểm thuộc (Ảnh 4 Câu 14)."""
    while True:
        xA, yA = random.randint(1, 4), random.randint(1, 4)
        xB, yB = random.randint(-3, 1), random.randint(-2, 2)
        if (xA, yA) == (xB, yB):
            continue
        # Trung trực AB: 2(xA - xB)x + 2(yA - yB)y + (xB^2+yB^2 - xA^2-yA^2) = 0
        a1, b1, c1 = _reduce_abc(
            2 * (xA - xB),
            2 * (yA - yB),
            xB ** 2 + yB ** 2 - xA ** 2 - yA ** 2,
        )
        a2 = random.choice([1, 2])
        b2 = random.choice([-3, -2, -1, 1, 2])
        det = a1 * b2 - a2 * b1
        if det == 0:
            continue
        c2 = random.choice([-11, -7, -5, 3, 5])
        xI = Fraction(b1 * c2 - b2 * c1, det)
        yI = Fraction(c1 * a2 - c2 * a1, det)
        R2 = (xA - xI) ** 2 + (yA - yI) ** 2
        io2 = xI ** 2 + yI ** 2
        if R2 > 0 and io2 != R2 and xI.denominator <= 6:
            break

    o_in = io2 < R2
    diam_tex = _sqrt_frac_tex(4 * R2)
    diam_wrong = _frac_tex(R2)

    # Điểm đối xứng A qua đường y = yI hoặc x = xI
    xN_on, yN_on = xB, yB
    # Tạo một điểm khác trên (C) nếu 2*yI là số nguyên hoặc dùng điểm (-xA + 2*xI, yA)
    x_alt, y_alt = 2 * xI - xA, yA
    if (x_alt, y_alt) in ((xA, yA), (xB, yB)):
        x_alt, y_alt = xA, 2 * yI - yA
    x_bad = xA + 1
    y_bad = yB - 1

    caudan = (
        f"Trong mặt phẳng $Oxy$, cho đường tròn $(C)$ đi qua hai điểm $A{_pt_tex(xA, yA)}$, $B{_pt_tex(xB, yB)}$ "
        f"và có tâm thuộc $\\Delta: {_line_eq_tex(a2, b2, c2)}$."
    )

    stmt_a_t = f"Tâm của đường tròn $(C)$ là $I{_pt_tex(xI, yI)}$."
    exp_a_t = f"Tâm $I$ là giao điểm của $\\Delta$ và trung trực $AB: {_line_eq_tex(a1, b1, c1)}$, giải hệ được $I{_pt_tex(xI, yI)}$."
    stmt_a_f = f"Tâm của đường tròn $(C)$ là $I{_pt_tex(-xI if xI != 0 else 1, yI)}$."
    exp_a_f = f"Tâm đúng của đường tròn là $I{_pt_tex(xI, yI)}$."

    if o_in:
        stmt_b_t = "Điểm $O(0; 0)$ nằm bên trong đường tròn $(C)$."
        stmt_b_f = "Điểm $O(0; 0)$ nằm bên ngoài đường tròn $(C)$."
        exp_b = f"$IO^2 = {_frac_tex(io2)} < R^2 = {_frac_tex(R2)}$ nên $O(0; 0)$ nằm bên trong $(C)$."
    else:
        stmt_b_t = "Điểm $O(0; 0)$ nằm bên ngoài đường tròn $(C)$."
        stmt_b_f = "Điểm $O(0; 0)$ nằm bên trong đường tròn $(C)$."
        exp_b = f"$IO^2 = {_frac_tex(io2)} > R^2 = {_frac_tex(R2)}$ nên $O(0; 0)$ nằm bên ngoài $(C)$."

    stmt_c_t = f"Đường kính của đường tròn $(C)$ bằng ${diam_tex}$."
    exp_c_t = f"$R^2 = IA^2 = {_frac_tex(R2)} \\Rightarrow 2R = {diam_tex}$."
    stmt_c_f = f"Đường kính của đường tròn $(C)$ bằng ${diam_wrong}$."
    exp_c_f = f"Đường kính đúng bằng $2R = {diam_tex} \\ne {diam_wrong}$."

    stmt_d_t = f"Đường tròn $(C)$ đi qua điểm ${_pt_tex(x_alt, y_alt)}$."
    exp_d_t = f"Thử khoảng cách từ tâm $I$ đến điểm ${_pt_tex(x_alt, y_alt)}$ được $R^2 = {_frac_tex(R2)}$ nên điểm này thuộc $(C)$."
    bad_r2 = (x_bad - xI) ** 2 + (y_bad - yI) ** 2
    stmt_d_f = f"Đường tròn $(C)$ đi qua điểm ${_pt_tex(x_bad, y_bad)}$."
    exp_d_f = f"Khoảng cách bình phương từ $I$ đến ${_pt_tex(x_bad, y_bad)}$ là ${_frac_tex(bad_r2)} \\ne {_frac_tex(R2)}$ nên không thuộc $(C)$."

    phuongan, loigiai = _make_tf_choices([
        (stmt_a_t, stmt_a_f, exp_a_t, exp_a_f),
        (stmt_b_t, stmt_b_f, exp_b, exp_b),
        (stmt_c_t, stmt_c_f, exp_c_t, exp_c_f),
        (stmt_d_t, stmt_d_f, exp_d_t, exp_d_f),
    ])
    return caudan, phuongan, loigiai


def K10_Oxy_TF_DuongTron_ViTriDiem_TiepTuyenQuaB():
    """Đúng/Sai: Đường tròn (C) ở dạng tổng quát, điểm A trên (C), B ngoài (C), tiếp tuyến tại A và 2 tiếp tuyến qua B (Ảnh 4 Câu 15)."""
    a = random.choice([1, 2, 3, -2])
    b = random.choice([-2, -1, 1, 2])
    R = random.choice([2, 3, 4])
    R2 = R * R
    # Chọn A = (a - R, b) thuộc (C) -> tiếp tuyến tại A là x = a - R
    xA, yA = a - R, b
    # Chọn B = (a - R, b + h) ngoài (C) với h != 0
    h = random.choice([3, 4, -3, -4])
    while h == 0:
        h = 3
    xB, yB = a - R, b + h
    # Hai tiếp tuyến qua B:
    # d1: x = xA (tức x - xA = 0)
    t1_str = f"x = {xA}"
    # d2: độ dốc k = (R^2 - h^2) / (2*R*h)
    k_slope = Fraction(R2 - h * h, 2 * R * h)
    # y - yB = k*(x - xB) <=> k_num*x - k_den*y + (k_den*yB - k_num*xB) = 0
    A2, B2, C2 = _reduce_abc(k_slope.numerator, -k_slope.denominator, k_slope.denominator * yB - k_slope.numerator * xB)
    t2_str = _line_eq_tex(A2, B2, C2)
    t2_wrong = _line_eq_tex(A2, B2, C2 + 3)

    D, E, F = -2 * a, -2 * b, a * a + b * b - R2
    caudan = (
        f"Trong mặt phẳng $Oxy$, cho đường tròn $(C)$ có phương trình ${_circle_gen_tex(D, E, F)}$ "
        f"và hai điểm $A{_pt_tex(xA, yA)}, B{_pt_tex(xB, yB)}$."
    )

    stmt_a_t = "Điểm $A$ thuộc đường tròn $(C)$."
    exp_a_t = f"Tâm $I{_pt_tex(a, b)}$, bán kính $R = {R}$. Ta có $IA^2 = {R}^2 = {R2}$ nên $A \\in (C)$."
    stmt_a_f = "Điểm $A$ nằm bên trong đường tròn $(C)$."
    exp_a_f = f"$IA = {R} = R$ nên $A$ nằm trên đường tròn $(C)$."

    stmt_b_t = "Điểm $B$ nằm ngoài đường tròn $(C)$."
    exp_b_t = f"$IB^2 = {R}^2 + ({h})^2 = {R2 + h*h} > R^2 = {R2}$ nên $B$ nằm ngoài $(C)$."
    stmt_b_f = "Điểm $B$ nằm trong đường tròn $(C)$."
    exp_b_f = f"$IB^2 = {R2 + h*h} > R^2 = {R2}$ nên $B$ nằm ngoài $(C)$."

    stmt_c_t = f"${t1_str}$ là phương trình tiếp tuyến của $(C)$ tại điểm $A$."
    exp_c_t = f"Tiếp tuyến tại $A{_pt_tex(xA, yA)}$ có VTPT $\\overrightarrow{{IA}} = (-{R}; 0)$ nên có PT ${t1_str}$."
    stmt_c_f = f"$y = {yA}$ là phương trình tiếp tuyến của $(C)$ tại điểm $A$."
    exp_c_f = f"VTPT là $\\overrightarrow{{IA}} = (-{R}; 0)$ nên tiếp tuyến tại $A$ phải là ${t1_str}$."

    stmt_d_t = f"Qua $B$ kẻ được hai tiếp tuyến với $(C)$ có phương trình là ${t1_str}$; ${t2_str}$."
    exp_d_t = f"Đường thẳng $x = {xA}$ có $d(I, d) = {R} = R$. Đường thẳng ${t2_str}$ qua $B$ có $d(I, d) = {R} = R$. Vậy đây là hai tiếp tuyến cần tìm."
    stmt_d_f = f"Qua $B$ kẻ được hai tiếp tuyến với $(C)$ có phương trình là ${t1_str}$; ${t2_wrong}$."
    exp_d_f = f"Khoảng cách từ $I$ đến ${t2_wrong}$ khác $R$. Hai tiếp tuyến đúng là ${t1_str}$ và ${t2_str}$."

    phuongan, loigiai = _make_tf_choices([
        (stmt_a_t, stmt_a_f, exp_a_t, exp_a_f),
        (stmt_b_t, stmt_b_f, exp_b_t, exp_b_f),
        (stmt_c_t, stmt_c_f, exp_c_t, exp_c_f),
        (stmt_d_t, stmt_d_f, exp_d_t, exp_d_f),
    ])
    return caudan, phuongan, loigiai


def K10_Oxy_TF_DuongTron_TiepTuyenSongSongDelta():
    """Đúng/Sai: (C): (x-a)^2+(y-b)^2=R^2 - tâm, bán kính, 2 tiếp tuyến song song Delta, kiểm tra điểm thuộc tiếp tuyến (Ảnh 4 Câu 16)."""
    a = random.choice([-2, -1, 1, 2, 3])
    b = random.choice([-3, -2, -1, 1, 2])
    A, B = random.choice([(3, -4), (4, 3), (3, 4)])
    den = 5
    R = random.choice([3, 4, 5])
    R2 = R * R
    C_delta = random.choice([-7, -4, 7, 14])
    if A * a + B * b + C_delta == 0:
        C_delta += 3

    # Hai tiếp tuyến song song Delta: A*x + B*y + C1 = 0 và C2 = 0 với |A*a + B*b + C'| = 5*R
    base = -(A * a + B * b)
    C_tan1 = base + den * R
    C_tan2 = base - den * R

    # Tạo điểm M1 nằm trên tiếp tuyến 1 (ví dụ tìm xM sao cho (A*xM + C_tan1) chia hết cho B hoặc đơn giản chọn yM = 1, xM phân số gọn)
    # Tốt hơn: chọn (A, B) và điểm nguyên M_on trên tiếp tuyến 1 bằng brute-force nhỏ
    xM_on, yM_on = 0, 0
    for xx in range(-6, 7):
        num_y = -(A * xx + C_tan1)
        if num_y % B == 0:
            xM_on, yM_on = xx, num_y // B
            break
    xM_off, yM_off = xM_on + 1, yM_on

    caudan = (
        f"Trong mặt phẳng tọa độ $Oxy$, cho đường tròn $(C): {_circle_std_tex(a, b, R2)}$. Khi đó"
    )

    stmt_a_t = f"Đường tròn $(C)$ có tâm $I{_pt_tex(a, b)}$."
    exp_a_t = f"Đọc từ phương trình chính tắc được tâm $I{_pt_tex(a, b)}$."
    stmt_a_f = f"Đường tròn $(C)$ có tâm $I{_pt_tex(-a, -b)}$."
    exp_a_f = f"Nhầm dấu; tâm đúng là $I{_pt_tex(a, b)}$."

    stmt_b_t = f"Đường tròn $(C)$ có bán kính $R = {R}$."
    exp_b_t = f"$R = \\sqrt{{{R2}}} = {R}$."
    stmt_b_f = f"Đường tròn $(C)$ có bán kính $R = {R2}$."
    exp_b_f = f"$R = {R} \\ne {R2}$."

    del_eq = _line_eq_tex(A, B, C_delta)
    stmt_c_t = f"Có $2$ tiếp tuyến đường tròn $(C)$ song song với đường thẳng $\\Delta: {del_eq}$."
    exp_c_t = f"Đặt tiếp tuyến $d: {_lin_tex(A, 0, 'x')}{_signed_frac_term(B, 'y')} + m = 0$. Giải $d(I, d) = {R}$ được $m = {C_tan1}$ hoặc $m = {C_tan2}$ (đều khác ${C_delta}$), nên có 2 tiếp tuyến."
    stmt_c_f = f"Chỉ có $1$ tiếp tuyến đường tròn $(C)$ song song với đường thẳng $\\Delta: {del_eq}$."
    exp_c_f = f"Phương trình $|{A}({a}) + ({B})({b}) + m| = {den * R}$ cho 2 nghiệm $m$ khác ${C_delta}$, nên có đúng 2 tiếp tuyến."

    stmt_d_t = f"Có một tiếp tuyến của $(C)$ song song với $\\Delta: {del_eq}$ đi qua điểm $M{_pt_tex(xM_on, yM_on)}$."
    exp_d_t = f"Thay $M{_pt_tex(xM_on, yM_on)}$ vào tiếp tuyến $d_1: {_line_eq_tex(A, B, C_tan1)}$ thấy thỏa mãn."
    stmt_d_f = f"Có một tiếp tuyến của $(C)$ song song với $\\Delta: {del_eq}$ đi qua điểm $M{_pt_tex(xM_off, yM_off)}$."
    exp_d_f = f"Hai tiếp tuyến là ${_line_eq_tex(A, B, C_tan1)}$ và ${_line_eq_tex(A, B, C_tan2)}$; thay $M{_pt_tex(xM_off, yM_off)}$ vào cả hai đều không thỏa mãn."

    phuongan, loigiai = _make_tf_choices([
        (stmt_a_t, stmt_a_f, exp_a_t, exp_a_f),
        (stmt_b_t, stmt_b_f, exp_b_t, exp_b_f),
        (stmt_c_t, stmt_c_f, exp_c_t, exp_c_f),
        (stmt_d_t, stmt_d_f, exp_d_t, exp_d_f),
    ])
    return caudan, phuongan, loigiai


K10_HK2_OXY_TF_MAP = {
    "Đúng sai - Oxy (Bài 19-20): Xét vị trí tương đối và góc giữa bốn cặp đường thẳng": K10_Oxy_TF_VTTD_Goc_BonCapDuongThang,
    "Đúng sai - Oxy (Bài 19-20): Hai đường thẳng tham số (VTCP, song song, giao điểm, vuông góc)": K10_Oxy_TF_HaiDuongThang_PTTS_GiaoDiem_VTTD,
    "Đúng sai - Oxy (Bài 20): Khoảng cách từ điểm đến đường thẳng và khoảng cách hai đường song song": K10_Oxy_TF_KhoangCach_Diem_Va_HaiDuongSongSong,
    "Đúng sai - Oxy (Bài 19-20): Hai đường thẳng tham số có giao điểm phân số và tính song song": K10_Oxy_TF_PTTS_VTCP_GiaoDiemPhanSo_SongSong,
    "Đúng sai - Oxy (Bài 19): Bài toán thực tế chuyển động thẳng đều trong mặt phẳng Oxy": K10_Oxy_TF_ChuyenDongThangDeu_Oxy,
    "Đúng sai - Oxy (Bài 19-20): Tam giác ABC biết đỉnh A, trung trực BC và trung tuyến từ C": K10_Oxy_TF_TamGiac_TrungTruc_TrungTuyen,
    "Đúng sai - Oxy (Bài 19-20): Hình chữ nhật ABCD tâm I, điểm trên cạnh và điều kiện hoành độ": K10_Oxy_TF_HinhChuNhat_TamI_TrungDiem,
    "Đúng sai - Đường tròn (Bài 21): Đường tròn qua ba điểm A, B, C (tâm, đường kính, điểm thuộc, độ dài IO)": K10_Oxy_TF_DuongTron_QuaBaDiem,
    "Đúng sai - Đường tròn (Bài 21): Đường tròn qua A và tiếp xúc đường thẳng Delta tại B (R nguyên)": K10_Oxy_TF_DuongTron_QuaA_TiepXucDeltaTaiB,
    "Đúng sai - Đường tròn (Bài 21): Đường tròn qua A tiếp xúc đường thẳng d tại M (dạng tổng quát)": K10_Oxy_TF_DuongTron_QuaA_TiepXucTaiM_TongQuat,
    "Đúng sai - Đường tròn (Bài 21): Tâm, bán kính, tiếp tuyến tại điểm M và tiếp tuyến vuông góc": K10_Oxy_TF_DuongTron_TamBanKinh_TiepTuyen,
    "Đúng sai - Đường tròn (Bài 21): Tâm I tiếp xúc đường thẳng Delta (bán kính căn thức và tiếp điểm)": K10_Oxy_TF_DuongTron_TamI_TiepXucDelta_TiepDiem,
    "Đúng sai - Đường tròn (Bài 21): Đường tròn qua A, B có tâm thuộc đường thẳng Delta": K10_Oxy_TF_DuongTron_QuaAB_TamTrenDelta,
    "Đúng sai - Đường tròn (Bài 21): Vị trí điểm, tiếp tuyến tại điểm và hai tiếp tuyến kẻ từ điểm ngoài": K10_Oxy_TF_DuongTron_ViTriDiem_TiepTuyenQuaB,
    "Đúng sai - Đường tròn (Bài 21): Tiếp tuyến của đường tròn song song với đường thẳng Delta cho trước": K10_Oxy_TF_DuongTron_TiepTuyenSongSongDelta,
}


def dispatch_k10_hk2_oxy_tf(item):
    """Sinh block LaTeX Đúng/Sai hoàn chỉnh cho các dạng Chương VII Oxy trong K10_HK2_OXY_TF_MAP."""
    fn = K10_HK2_OXY_TF_MAP.get(item)
    if fn is None:
        return None
    caudan, phuongan, loigiai = fn()
    return "\\begin{ex}\n" + caudan + "\n\\choiceTF\n" + "".join(phuongan) + "\\loigiai{" + loigiai + "}\n\\end{ex}"
