"""Ngân hàng câu hỏi sinh ngẫu nhiên cho Toán 10 Học kì 2 - Chương VI & VII:
- Bài 15: Hàm số và đồ thị
- Bài 16: Hàm số bậc hai
- Bài 17: Dấu của tam thức bậc hai & Bất phương trình bậc hai
- Bài 18: Phương trình quy về phương trình bậc hai
"""

import math
import random
from fractions import Fraction


# ==============================================================================
# CÁC HÀM PHỤ TRỢ ĐỊNH DẠNG TOÁN HỌC & TRẮC NGHIỆM CHUẨN
# ==============================================================================

def _frac_tex(val):
    """Định dạng số nguyên hoặc phân số tối giản sang chuỗi LaTeX (dùng \\dfrac)."""
    f = Fraction(val).limit_denominator()
    if f.denominator == 1:
        return str(f.numerator)
    if f.numerator < 0:
        return f"-\\dfrac{{{-f.numerator}}}{{{f.denominator}}}"
    return f"\\dfrac{{{f.numerator}}}{{{f.denominator}}}"


def _signed_frac_term(val, var=""):
    """Định dạng hạng tử có dấu ở giữa biểu thức: + 3x, - \\dfrac{1}{2}, v.v."""
    f = Fraction(val).limit_denominator()
    if f == 0:
        return ""
    sign = " + " if f > 0 else " - "
    af = abs(f)
    if var:
        coef = "" if af == 1 else _frac_tex(af)
        return f"{sign}{coef}{var}"
    return f"{sign}{_frac_tex(af)}"


def _lin_tex(a, b, var="x"):
    """Định dạng nhị thức ax + b chuẩn LaTeX."""
    fa = Fraction(a).limit_denominator()
    fb = Fraction(b).limit_denominator()
    parts = []
    if fa != 0:
        if fa == 1:
            parts.append(var)
        elif fa == -1:
            parts.append(f"-{var}")
        else:
            parts.append(f"{_frac_tex(fa)}{var}")
    if fb != 0:
        if not parts:
            parts.append(_frac_tex(fb))
        else:
            parts.append(_signed_frac_term(fb))
    return "".join(parts) if parts else "0"


def _quad_tex(a, b, c, var="x"):
    """Định dạng tam thức ax^2 + bx + c chuẩn LaTeX."""
    fa = Fraction(a).limit_denominator()
    fb = Fraction(b).limit_denominator()
    fc = Fraction(c).limit_denominator()
    parts = []
    if fa != 0:
        if fa == 1:
            parts.append(f"{var}^2")
        elif fa == -1:
            parts.append(f"-{var}^2")
        else:
            parts.append(f"{_frac_tex(fa)}{var}^2")
    if fb != 0:
        if not parts:
            parts.append(_lin_tex(fb, 0, var))
        else:
            parts.append(_signed_frac_term(fb, var))
    if fc != 0:
        if not parts:
            parts.append(_frac_tex(fc))
        else:
            parts.append(_signed_frac_term(fc))
    return "".join(parts) if parts else "0"


def _signed_factor(r, var="x"):
    """Định dạng nhân tử (x - r) không bị lỗi (x - -2)."""
    fr = Fraction(r).limit_denominator()
    if fr == 0:
        return var
    if fr > 0:
        return f"({var} - {_frac_tex(fr)})"
    return f"({var} + {_frac_tex(-fr)})"


def _make_choices(true_ans, candidates):
    """Đảm bảo 4 phương án phân biệt hoàn toàn và xáo trộn ngẫu nhiên."""
    pool = [true_ans]
    seen = {true_ans.strip()}
    for c in candidates:
        cs = c.strip()
        if cs not in seen:
            seen.add(cs)
            pool.append(c)
        if len(pool) == 4:
            break
    labeled = [f"{{\\True {pool[0]}}}\n"] + [f"{{{p}}}\n" for p in pool[1:]]
    random.shuffle(labeled)
    return labeled


# ==============================================================================
# BÀI 15: HÀM SỐ VÀ ĐỒ THỊ
# ==============================================================================

def K10_C3_MC_HamSo_TinhGiaTri_HamChoBoiNhieuCongThuc():
    variant = random.choice([1, 2, 3])
    if variant == 1:
        # Nhánh 1: p/(x - k) trên (-inf; m]; Nhánh 2: ax^2 + b trên (m; n]
        m = random.choice([1, 2, 3])
        n = m + random.choice([3, 4])
        k = m - random.choice([1, 2])
        p = random.choice([2, 3, 4, 6])
        a = random.choice([1, 2])
        b = random.choice([-2, -1, 1, 2, 3])
        x0 = random.choice([m + 1, m + 2]) if random.choice([True, False]) else (k - random.choice([1, 2]))
        if x0 > m:
            ans_val = Fraction(a * x0 * x0 + b)
            other_val = Fraction(p, x0 - k) if x0 != k else ans_val + 1
            branch_desc = f"vì ${x0} \\in ({m}; {n}]$ nên dùng công thức thứ hai"
            calc_tex = f"f({x0}) = {_quad_tex(a, 0, b, var=f'({x0})')} = {_frac_tex(ans_val)}"
            if a == 1:
                calc_tex = f"f({x0}) = {x0}^2 {_signed_frac_term(b)} = {_frac_tex(ans_val)}"
        else:
            ans_val = Fraction(p, x0 - k)
            other_val = Fraction(a * x0 * x0 + b)
            branch_desc = f"vì ${x0} \\in (-\\infty; {m}]$ nên dùng công thức thứ nhất"
            calc_tex = f"f({x0}) = \\dfrac{{{p}}}{{{x0} - ({k})}} = {_frac_tex(ans_val)}"

        f2_expr = _quad_tex(a, 0, b)
        caudan = (
            f"Cho hàm số $y = f(x) = \\begin{{cases}} \\dfrac{{{p}}}{{{_lin_tex(1, -k)}}}, & x \\in (-\\infty; {m}] \\\\ "
            f"{f2_expr}, & x \\in ({m}; {n}] \\end{{cases}}$. Tính $f({x0})$."
        )
        cands = [
            f"${_frac_tex(other_val)}$",
            f"${_frac_tex(ans_val + 1)}$",
            f"${_frac_tex(ans_val - 1)}$",
            f"${_frac_tex(ans_val + 2)}$",
            f"${_frac_tex(-ans_val)}$",
        ]
        choices = _make_choices(f"${_frac_tex(ans_val)}$", cands)
        loigiai = f"Do {branch_desc}:\n$${calc_tex}.$$"
        return caudan, choices, loigiai

    if variant == 2:
        # f(x) = sqrt(x^2 + ...) hoặc sqrt((x-a)^2)
        a = random.choice([0, 1, -1, 2, -2, 3])
        x0 = random.choice([0, -1, -2, 1, 2])
        ans = abs(x0 - a)
        expr = "x^2" if a == 0 else f"({ _lin_tex(1, -a) })^2"
        caudan = f"Cho hàm số $f(x)$ xác định trên $\\mathbb{{R}}$, biết $f(x) = \\sqrt{{{expr}}}$. Giá trị $f({x0})$ bằng"
        cands = [
            f"${ans + 1}$",
            f"${ans + 2}$",
            f"${-ans - 1}$",
            "không tồn tại",
        ]
        choices = _make_choices(f"${ans}$", cands)
        loigiai = (
            f"Thay $x = {x0}$ vào biểu thức của hàm số:\n"
            f"$$f({x0}) = \\sqrt{{({x0} {_signed_frac_term(-a)})^2}} = |{x0 - a}| = {ans}.$$"
            if a != 0 else
            f"Thay $x = {x0}$ vào biểu thức của hàm số:\n$$f({x0}) = \\sqrt{{{x0}^2}} = |{x0}| = {ans}.$$"
        )
        return caudan, choices, loigiai

    # Variant 3: Tính P = f(x1) + f(x2)
    m = random.choice([1, 2, 3])
    d = m - random.choice([1, 2])
    t = random.choice([0, 1, 2])
    x1 = m + t * t
    k = random.choice([2, 3])
    c = random.choice([1, 2, 3, 4])
    x2 = random.choice([-2, -1, 0])
    b2 = random.choice([1, 2, 3])

    f_x1 = Fraction(k * t - c, x1 - d)
    f_x2 = Fraction(x2 * x2 + b2)
    P = f_x1 + f_x2

    num_expr = f"{k}\\sqrt{{{_lin_tex(1, -m)}}} - {c}"
    den_expr = _lin_tex(1, -d)
    b2_expr = _quad_tex(1, 0, b2)
    caudan = (
        f"Hàm số $f(x) = \\begin{{cases}} \\dfrac{{{num_expr}}}{{{den_expr}}} & \\text{{khi }} x \\ge {m} \\\\ "
        f"{b2_expr} & \\text{{khi }} x < {m} \\end{{cases}}$. Tính $P = f({x1}) + f({x2})$."
    )
    cands = [
        f"$P = {_frac_tex(P + 1)}$",
        f"$P = {_frac_tex(P - 1)}$",
        f"$P = {_frac_tex(P + Fraction(1, 2))}$",
        f"$P = {_frac_tex(f_x2 - f_x1)}$",
    ]
    choices = _make_choices(f"$P = {_frac_tex(P)}$", cands)
    loigiai = (
        f"Ta có:\n"
        f"- Vì ${x1} \\ge {m}$ nên $f({x1}) = \\dfrac{{{k}\\sqrt{{{x1} - {m}}} - {c}}}{{{x1 - d}}} = {_frac_tex(f_x1)}$.\n"
        f"- Vì ${x2} < {m}$ nên $f({x2}) = ({x2})^2 + {b2} = {_frac_tex(f_x2)}$.\n"
        f"Vậy $P = f({x1}) + f({x2}) = {_frac_tex(f_x1)} + {_frac_tex(f_x2)} = {_frac_tex(P)}$."
    )
    return caudan, choices, loigiai


def K10_C3_MC_HamSo_TapXacDinh_PhanThuc():
    variant = random.choice([1, 2])
    if variant == 1:
        r = random.choice([-4, -3, -2, -1, 1, 2, 3, 4])
        num_r = random.choice([-3, -2, -1, 0, 1, 2, 3])
        while num_r == r:
            num_r = random.choice([-3, -2, -1, 0, 1, 2, 3])
        num_tex = _lin_tex(1, -num_r)
        den_tex = _lin_tex(1, -r)
        caudan = f"Tìm tập xác định $\\mathcal{{D}}$ của hàm số $y = \\dfrac{{{num_tex}}}{{{den_tex}}}$."
        true_ans = f"$\\mathcal{{D}} = \\mathbb{{R}} \\setminus \\{{{r}\\}}$"
        cands = [
            f"$\\mathcal{{D}} = \\mathbb{{R}} \\setminus \\{{{min(r, num_r)}; {max(r, num_r)}\\}}$",
            r"$\mathcal{D} = \mathbb{R}$",
            f"$\\mathcal{{D}} = ({r}; +\\infty)$",
            f"$\\mathcal{{D}} = \\mathbb{{R}} \\setminus \\{{{-r}\\}}$",
        ]
        choices = _make_choices(true_ans, cands)
        loigiai = (
            f"Hàm số xác định khi và chỉ khi mẫu thức khác $0$:\n"
            f"$${den_tex} \\ne 0 \\iff x \\ne {r}.$$\n"
            f"Vậy tập xác định của hàm số là $\\mathcal{{D}} = \\mathbb{{R}} \\setminus \\{{{r}\\}}$."
        )
        return caudan, choices, loigiai

    # Variant 2: Mẫu bậc hai có 2 nghiệm phân biệt r1 < r2
    a = random.choice([1, 2])
    r1 = Fraction(random.choice([-3, -2, -1]))
    if a == 2:
        r2 = Fraction(random.choice([1, 3, 5]), 2)
    else:
        r2 = Fraction(random.choice([1, 2, 3, 4]))
    b = -a * (r1 + r2)
    c = a * r1 * r2
    px = random.choice([2, 3, 4])
    qx = random.choice([-2, -1, 1, 2])
    num_tex = _lin_tex(px, qx)
    den_tex = _quad_tex(a, b, c)
    r1_s, r2_s = _frac_tex(r1), _frac_tex(r2)
    caudan = f"Tìm tập xác định $\\mathcal{{D}}$ của hàm số $y = \\dfrac{{{num_tex}}}{{{den_tex}}}$."
    true_ans = f"$\\mathcal{{D}} = \\mathbb{{R}} \\setminus \\left\\{{{r1_s}; {r2_s}\\right\\}}$"
    cands = [
        f"$\\mathcal{{D}} = \\left[{r1_s}; {r2_s}\\right]$",
        f"$\\mathcal{{D}} = \\mathbb{{R}} \\setminus \\{{{r1_s}\\}}$",
        f"$\\mathcal{{D}} = \\left({r1_s}; {r2_s}\\right)$",
        f"$\\mathcal{{D}} = \\mathbb{{R}} \\setminus \\{{{r2_s}\\}}$",
    ]
    choices = _make_choices(true_ans, cands)
    loigiai = (
        f"Hàm số xác định khi và chỉ khi mẫu thức khác $0$:\n"
        f"$${den_tex} \\ne 0 \\iff \\begin{{cases}} x \\ne {r1_s} \\\\ x \\ne {r2_s}. \\end{{cases}}$$\n"
        f"Vậy tập xác định của hàm số là $\\mathcal{{D}} = \\mathbb{{R}} \\setminus \\left\\{{{r1_s}; {r2_s}\\right\\}}$."
    )
    return caudan, choices, loigiai


def K10_C3_MC_HamSo_TapXacDinh_ChuaCan():
    variant = random.choice([1, 2])
    if variant == 1:
        r1 = random.choice([-4, -3, -2, -1, 0, 1])
        r2 = r1 + random.choice([1, 2, 3])
        # sqrt(x - r1) - sqrt(x - r2) => x >= max(r1, r2) = r2
        e1 = _lin_tex(1, -r1)
        e2 = _lin_tex(1, -r2)
        op = random.choice(["-", "+"])
        caudan = f"Tìm tập xác định $\\mathcal{{D}}$ của hàm số $y = \\sqrt{{{e1}}} {op} \\sqrt{{{e2}}}$."
        true_ans = f"$\\mathcal{{D}} = [{r2}; +\\infty)$"
        cands = [
            f"$\\mathcal{{D}} = [{r1}; +\\infty)$",
            r"$\mathcal{D} = \mathbb{R}$",
            f"$\\mathcal{{D}} = ({r2}; +\\infty)$",
            f"$\\mathcal{{D}} = [{r1}; {r2}]$",
        ]
        choices = _make_choices(true_ans, cands)
        loigiai = (
            f"Hàm số xác định khi và chỉ khi các biểu thức dưới dấu căn đều không âm:\n"
            f"$$\\begin{{cases}} {e1} \\ge 0 \\\\ {e2} \\ge 0 \\end{{cases}} "
            f"\\iff \\begin{{cases}} x \\ge {r1} \\\\ x \\ge {r2} \\end{{cases}} \\iff x \\ge {r2}.$$\n"
            f"Vậy tập xác định của hàm số là $\\mathcal{{D}} = [{r2}; +\\infty)$."
        )
        return caudan, choices, loigiai

    # Variant 2: sqrt(x - r1) + sqrt(r2 - x) => [r1; r2]
    r1 = random.choice([-3, -2, -1, 0, 1])
    r2 = r1 + random.choice([2, 3, 4, 5])
    e1 = _lin_tex(1, -r1)
    e2 = _lin_tex(-1, r2)
    caudan = f"Tìm tập xác định $\\mathcal{{D}}$ của hàm số $y = \\sqrt{{{e1}}} + \\sqrt{{{e2}}}$."
    true_ans = f"$\\mathcal{{D}} = [{r1}; {r2}]$"
    cands = [
        f"$\\mathcal{{D}} = ({r1}; {r2})$",
        f"$\\mathcal{{D}} = [{r1}; +\\infty)$",
        f"$\\mathcal{{D}} = (-\\infty; {r2}]$",
        f"$\\mathcal{{D}} = \\mathbb{{R}} \\setminus [{r1}; {r2}]$",
    ]
    choices = _make_choices(true_ans, cands)
    loigiai = (
        f"Hàm số xác định khi và chỉ khi:\n"
        f"$$\\begin{{cases}} {e1} \\ge 0 \\\\ {e2} \\ge 0 \\end{{cases}} "
        f"\\iff \\begin{{cases}} x \\ge {r1} \\\\ x \\le {r2} \\end{{cases}} \\iff {r1} \\le x \\le {r2}.$$\n"
        f"Vậy tập xác định của hàm số là $\\mathcal{{D}} = [{r1}; {r2}]$."
    )
    return caudan, choices, loigiai


def K10_C3_MC_HamSo_NhanDien_HamBacNhat():
    """Ảnh 1 Câu 8: Nhận diện hàm số bậc nhất."""
    a = random.choice([-5, -3, -2, 2, 3, 4, 5, 7, 10])
    b = random.choice([-7, -5, -3, 1, 3, 5, 8])
    m_coef = random.choice([-4, -3, -2, 2, 3])
    m_const = random.choice([-2, 1, 2, 4])
    q_coef = random.choice([-3, -2, 2, 3])
    c_val = random.choice([-5, 4, 6, 9])

    true_expr = _lin_tex(a, b) if random.choice([True, False]) else f"{b} {_signed_frac_term(a, 'x')}"
    w_param = f"({_lin_tex(m_coef, m_const, var='m')})x {_signed_frac_term(b)}"
    w_quad = f"{_lin_tex(a, 0)}{_signed_frac_term(q_coef, 'x^2')}"
    w_const = f"{c_val}"

    caudan = "Trong các hàm số sau, hàm số nào là hàm số bậc nhất?"
    choices = _make_choices(
        f"$y = {true_expr}$",
        [f"$y = {w_param}$", f"$y = {w_quad}$", f"$y = {w_const}$"],
    )
    loigiai = (
        f"Hàm số bậc nhất có dạng $y = ax + b$ với $a, b \\in \\mathbb{{R}}$ và $a \\ne 0$.\n"
        f"- $y = {w_const}$ là hàm hằng ($a = 0$, không phải hàm bậc nhất).\n"
        f"- $y = {w_quad}$ là hàm số bậc hai.\n"
        f"- $y = {w_param}$ chưa chắc có hệ số của $x$ khác $0$ với mọi $m$.\n"
        f"Vậy hàm số bậc nhất là $y = {true_expr}$."
    )
    return caudan, choices, loigiai


def K10_C3_MC_HamSo_DongBien_NghichBien_BacNhat():
    a = random.choice([-3, -2, 2, 3, 4])
    b = random.choice([-5, -3, -1, 1, 2, 3, 5])
    cm = random.choice([-2, -1, 1, 2])
    d = random.choice([-4, -3, 1, 2, 3])
    ask_inc = random.choice([True, False])
    trend_vn = "đồng biến" if ask_inc else "nghịch biến"
    cond_sym = ">" if ask_inc else "<"

    bound = Fraction(-b, a)
    # Nếu ask_inc và a > 0 -> m > bound; nếu ask_inc và a < 0 -> m < bound
    is_gt = (ask_inc and a > 0) or ((not ask_inc) and a < 0)
    ans_sym = ">" if is_gt else "<"
    opp_sym = "<" if is_gt else ">"
    ge_sym = "\\ge" if is_gt else "\\le"

    coef_m = _lin_tex(a, b, var="m")
    const_m = _lin_tex(cm, d, var="m")
    if not const_m.startswith("-"):
        const_m_rhs = " + " + const_m
    else:
        const_m_rhs = " - " + const_m[1:]

    caudan = f"Hàm số $y = ({coef_m})x{const_m_rhs}$ {trend_vn} trên $\\mathbb{{R}}$ khi"
    true_ans = f"$m {ans_sym} {_frac_tex(bound)}$"
    cands = [
        f"$m {ge_sym} {_frac_tex(bound)}$",
        f"$m {opp_sym} {_frac_tex(bound)}$",
        f"$m {ans_sym} {_frac_tex(-bound)}$",
        f"$m {opp_sym} {_frac_tex(-bound)}$",
    ]
    choices = _make_choices(true_ans, cands)
    loigiai = (
        f"Hàm số bậc nhất $y = Ax + B$ {trend_vn} trên $\\mathbb{{R}}$ khi và chỉ khi hệ số $A {cond_sym} 0$.\n"
        f"Do đó:\n"
        f"$${coef_m} {cond_sym} 0 \\iff m {ans_sym} {_frac_tex(bound)}.$$"
    )
    return caudan, choices, loigiai


def K10_C3_MC_HamSo_DuongThang_SongSong_DiQuaDiem():
    k = random.choice([-3, -2, -1, 2, 3, 4])
    c = random.choice([-3, -1, 1, 2, 3, 5])
    x0 = random.choice([-2, -1, 1, 2])
    b_true = random.choice([-4, -3, -2, -1, 1, 2, 4])
    while b_true == c:
        b_true = random.choice([-4, -3, -2, -1, 1, 2, 4])
    y0 = k * x0 + b_true

    line_tex = _lin_tex(k, c)
    caudan = (
        f"Tìm $a$ và $b$ biết rằng đường thẳng $y = ax + b$ đi qua điểm $M({x0}; {y0})$ "
        f"và song song với đường thẳng $y = {line_tex}$."
    )
    true_ans = f"$\\begin{{cases}} a = {k} \\\\ b = {b_true} \\end{{cases}}$"
    cands = [
        f"$\\begin{{cases}} a = {-k} \\\\ b = {b_true} \\end{{cases}}$",
        f"$\\begin{{cases}} a = {k} \\\\ b = {c} \\end{{cases}}$",
        f"$\\begin{{cases}} a = {k} \\\\ b = {-b_true} \\end{{cases}}$",
        f"$\\begin{{cases}} a = {x0} \\\\ b = {y0} \\end{{cases}}$",
    ]
    choices = _make_choices(true_ans, cands)
    loigiai = (
        f"Vì đường thẳng $y = ax + b$ song song với đường thẳng $y = {line_tex}$ nên:\n"
        f"$$a = {k} \\text{{ và }} b \\ne {c}.$$\n"
        f"Đường thẳng đi qua điểm $M({x0}; {y0})$, thay $x = {x0}, y = {y0}$ vào phương trình:\n"
        f"$${y0} = {k}\\cdot({x0}) + b \\iff b = {b_true} \\text{{ (thỏa mãn }} b \\ne {c}\\text{{)}}.$$\n"
        f"Vậy $a = {k}$ và $b = {b_true}$."
    )
    return caudan, choices, loigiai


# ==============================================================================
# BÀI 16: HÀM SỐ BẬC HAI
# ==============================================================================

def K10_C3_MC_Parabol_DiemThuocDoThi():
    """Ảnh 3 Câu 1 & Trang 36 Câu 9: Kiểm tra điểm thuộc / không thuộc đồ thị parabol."""
    if random.choice([True, False]):
        # Biến thể 1: Điểm thuộc đồ thị y = ax^2 + bx + c
        a = random.choice([-2, -1, 1, 2])
        b = random.choice([-4, -3, -2, 1, 2, 3, 4])
        c = random.choice([-3, -2, -1, 1, 2, 3])
        xs = random.sample([-2, -1, 0, 1, 2, 3], 4)
        x_ok = xs[0]
        y_ok = a * x_ok * x_ok + b * x_ok + c

        labels = ["M", "N", "P", "Q"]
        random.shuffle(labels)
        true_ans = f"${labels[0]}({x_ok}; {y_ok})$"
        cands = []
        for idx, xw in enumerate(xs[1:], start=1):
            yw_real = a * xw * xw + b * xw + c
            yw_fake = yw_real + random.choice([-3, -2, -1, 1, 2, 3])
            cands.append(f"${labels[idx]}({xw}; {yw_fake})$")

        f_tex = _quad_tex(a, b, c)
        caudan = f"Đồ thị hàm số $y = {f_tex}$ đi qua điểm nào sau đây?"
        choices = _make_choices(true_ans, cands)
        loigiai = (
            f"Thay tọa độ điểm ${labels[0]}({x_ok}; {y_ok})$ vào hàm số $y = {f_tex}$:\n"
            f"$$y({x_ok}) = {a}\\cdot({x_ok})^2 {_signed_frac_term(b)}\\cdot({x_ok}) {_signed_frac_term(c)} = {y_ok}.$$\n"
            f"Vậy đồ thị hàm số đi qua điểm ${labels[0]}({x_ok}; {y_ok})$."
        )
        return caudan, choices, loigiai

    # Biến thể 2: Điểm KHÔNG thuộc đồ thị y = a x^2 (hoặc ax^2 + bx + c)
    a = random.choice([Fraction(1, 2), Fraction(-1, 2), Fraction(1, 3), Fraction(2, 1), Fraction(-1, 1)])
    b = random.choice([0, 0, 1, -1])
    c = random.choice([0, 0, 1, -2])
    cand_x = [-2, 0, 1, 2, 3, -3]
    if a.denominator == 2:
        xs_ok = [0, 2, -2]
        x_bad = random.choice([1, -1, 3])
    elif a.denominator == 3:
        xs_ok = [0, 3, -3]
        x_bad = random.choice([1, 2, -1])
    else:
        xs_ok = [0, 1, -1]
        x_bad = random.choice([2, -2])

    pts_ok = [(x, a * x * x + b * x + c) for x in xs_ok]
    y_bad_real = a * x_bad * x_bad + b * x_bad + c
    y_bad_fake = y_bad_real + random.choice([1, 2, -1, -2])
    if y_bad_fake == y_bad_real:
        y_bad_fake = y_bad_real + 1

    f_tex = _quad_tex(a, b, c)
    caudan = f"Cho biết điểm nào sau đây \\textbf{{không}} thuộc đồ thị của hàm số $y = {f_tex}$?"
    true_ans = f"$({_frac_tex(x_bad)}; {_frac_tex(y_bad_fake)})$."
    cands = [f"$({_frac_tex(x)}; {_frac_tex(y)})$." for x, y in pts_ok]
    loigiai = (
        f"Thay hoành độ $x = {_frac_tex(x_bad)}$ vào hàm số $y = {f_tex}$ ta được "
        f"$y = {_frac_tex(y_bad_real)} \\ne {_frac_tex(y_bad_fake)}$.\n"
        f"Vậy điểm $({_frac_tex(x_bad)}; {_frac_tex(y_bad_fake)})$ không thuộc đồ thị hàm số."
    )
    return caudan, _make_choices(true_ans, cands), loigiai


def K10_C3_MC_Parabol_LyThuyet_TinhChat():
    """Ảnh 2 Câu 2: Khẳng định đúng về tính chất đồ thị hàm số bậc hai."""
    a = random.choice([-2, -1, 1, 2])
    b = random.choice([-4, -2, 2, 4])
    c = random.choice([-5, -3, -1, 1, 3])
    f_tex = _quad_tex(a, b, c)
    caudan = f"Cho hàm số $y = {f_tex}$. Khẳng định nào sau đây là đúng?"
    true_ans = "Đồ thị hàm số là một Parabol."
    cands = [
        "Đồ thị hàm số là một đường thẳng.",
        r"Hàm số đồng biến trên $\mathbb{R}$.",
        r"Hàm số nghịch biến trên $\mathbb{R}$.",
    ]
    choices = _make_choices(true_ans, cands)
    loigiai = (
        f"Hàm số $y = {f_tex}$ là hàm số bậc hai với hệ số $a = {a} \\ne 0$.\n"
        f"Do đó đồ thị của hàm số là một đường Parabol (không phải đường thẳng và không đơn điệu trên toàn $\\mathbb{{R}}$)."
    )
    return caudan, choices, loigiai


def K10_C3_MC_Parabol_ToaDoDinh_TrucDoiXung():
    variant = random.choice([1, 2])
    a = random.choice([-3, -2, -1, 1, 2, 3])
    b = random.choice([-6, -4, -3, -2, 2, 3, 4, 6])
    c = random.choice([-3, -2, -1, 1, 2, 3])
    f_tex = _quad_tex(a, b, c)
    xI = Fraction(-b, 2 * a)
    yI = a * xI * xI + b * xI + c

    if variant == 1:
        lbl = random.choice(["I", "S"])
        caudan = f"Tọa độ đỉnh ${lbl}$ của parabol $(P): y = {f_tex}$ là"
        x_s, y_s = _frac_tex(xI), _frac_tex(yI)
        true_ans = f"${lbl}\\left({x_s}; {y_s}\\right)$" if ("\\dfrac" in x_s or "\\dfrac" in y_s) else f"${lbl}({x_s}; {y_s})$"
        cands = [
            f"${lbl}\\left({_frac_tex(-xI)}; {y_s}\\right)$" if xI != 0 else f"${lbl}(1; {y_s})$",
            f"${lbl}\\left({x_s}; {_frac_tex(-yI)}\\right)$" if yI != 0 else f"${lbl}({x_s}; {yI + 1})$",
            f"${lbl}\\left({_frac_tex(xI * 2)}; {_frac_tex(yI + 1)}\\right)$",
            f"${lbl}\\left({x_s}; {_frac_tex(yI - 1)}\\right)$",
        ]
        choices = _make_choices(true_ans, cands)
        loigiai = (
            f"Tọa độ đỉnh ${lbl}(x_{lbl}; y_{lbl})$ của parabol $(P): y = ax^2 + bx + c$ là:\n"
            f"- Hoành độ đỉnh: $x_{lbl} = -\\dfrac{{b}}{{2a}} = -\\dfrac{{{b}}}{{2\\cdot({a})}} = {x_s}$.\n"
            f"- Tung độ đỉnh: $y_{lbl} = y\\left({x_s}\\right) = {y_s}$.\n"
            f"Vậy đỉnh của parabol là ${lbl}\\left({x_s}; {y_s}\\right)$."
        )
        return caudan, choices, loigiai

    caudan = f"Trục đối xứng của parabol $(P): y = {f_tex}$ là đường thẳng nào dưới đây?"
    x_s = _frac_tex(xI)
    true_ans = f"$x = {x_s}$"
    cands = [
        f"$y = {x_s}$",
        f"$x = {_frac_tex(-xI)}$" if xI != 0 else "$x = 1$",
        f"$y = {_frac_tex(-xI)}$" if xI != 0 else "$y = -1$",
        f"$x = {_frac_tex(2 * xI)}$",
    ]
    choices = _make_choices(true_ans, cands)
    loigiai = (
        f"Trục đối xứng của parabol $y = ax^2 + bx + c$ là đường thẳng:\n"
        f"$$x = -\\dfrac{{b}}{{2a}} = -\\dfrac{{{b}}}{{2\\cdot({a})}} = {x_s}.$$"
    )
    return caudan, choices, loigiai


def K10_C3_MC_Parabol_KhoangDongBien_NghichBien():
    a = random.choice([-2, -1, 1, 2])
    xI = random.choice([-4, -3, -2, -1, 1, 2, 3, 4])
    b = -2 * a * xI
    c = random.choice([-5, -2, 1, 3, 7, 11, 12])
    f_tex = _quad_tex(a, b, c)

    ask_inc = random.choice([True, False])
    trend_vn = "đồng biến" if ask_inc else "nghịch biến"
    # Nếu a > 0: nghịch biến (-inf; xI), đồng biến (xI; +inf)
    # Nếu a < 0: đồng biến (-inf; xI), nghịch biến (xI; +inf)
    right_branch = (a > 0 and ask_inc) or (a < 0 and not ask_inc)
    true_ans = f"$({xI}; +\\infty)$" if right_branch else f"$(-\\infty; {xI})$"
    opp_ans = f"$(-\\infty; {xI})$" if right_branch else f"$({xI}; +\\infty)$"

    caudan = f"Hàm số $y = {f_tex}$ {trend_vn} trên khoảng nào dưới đây?"
    cands = [
        opp_ans,
        f"$({-xI}; +\\infty)$",
        r"$(-\infty; +\infty)$",
        f"$(-\\infty; {2 * xI})$",
    ]
    choices = _make_choices(true_ans, cands)
    be_lom = "quay lên ($a > 0$)" if a > 0 else "quay xuống ($a < 0$)"
    loigiai = (
        f"Hàm số có $a = {a}$ và hoành độ đỉnh $x_I = -\\dfrac{{{b}}}{{2\\cdot({a})}} = {xI}$.\n"
        f"Vì parabol có bề lõm {be_lom} nên hàm số {trend_vn} trên khoảng ${true_ans.strip('$')}$."
    )
    return caudan, choices, loigiai


def K10_C3_MC_Parabol_NhanDangDoThi_BangBienThien():
    variant = random.choice([1, 2])
    if variant == 1:
        # Tạo parabol dạng y = a(x - r1)(x - r2) sao cho đi qua (0; c) khác 0 và qua (r1; 0)
        a = random.choice([-2, -1, 1, 2])
        r1 = random.choice([1, 2])
        r2 = random.choice([-1, 1, 2, 3])
        if r1 == r2:
            # Tiếp xúc trục hoành tại (r1; 0) cũng rất đẹp
            pass
        b = -a * (r1 + r2)
        c = a * r1 * r2
        if c == 0:
            r2 = -1 if r1 > 0 else 1
            b = -a * (r1 + r2)
            c = a * r1 * r2

        # Giá trị xI, yI
        xI = (r1 + r2) / 2.0
        yI = a * (xI - r1) * (xI - r2)
        xmin = min(-0.8, xI - 1.5, -0.5)
        xmax = max(2.5, xI + 1.5, r1 + 0.8)
        ymin = min(-0.8, yI - 0.6, c - 0.6)
        ymax = max(3.2, yI + 0.8, c + 1.2)
        dom_l = round(xI - 1.4, 2)
        dom_r = round(xI + 1.4, 2)

        tikz = (
            "\\begin{tikzpicture}[scale=0.65, line join=round, line cap=round, >=stealth]\n"
            f"    \\draw[->] ({xmin:.1f},0) -- ({xmax:.1f},0) node[below] {{$x$}};\n"
            f"    \\draw[->] (0,{ymin:.1f}) -- (0,{ymax:.1f}) node[left] {{$y$}};\n"
            "    \\node[below left] at (0,0) {$O$};\n"
            f"    \\draw[thick, blue, domain={dom_l}:{dom_r}, samples=100] plot (\\x, {{{a}*(\\x)*(\\x) + ({b})*(\\x) + ({c})}});\n"
            f"    \\node[left] at (0,{c}) {{${c}$}};\n"
            f"    \\node[below] at ({r1},0) {{${r1}$}};\n"
            f"    \\fill (0,{c}) circle (1.5pt);\n"
            f"    \\fill ({r1},0) circle (1.5pt);\n"
            "\\end{tikzpicture}"
        )
        caudan = f"\\immini{{Hàm số nào sau đây có đồ thị như hình dưới đây?}}{{\n{tikz}\n}}"
        true_ans = f"$y = {_quad_tex(a, b, c)}$"
        alt_a = a + 1 if a > 0 else a - 1
        cands = [
            f"$y = {_quad_tex(-a, -b, c)}$",
            f"$y = {_quad_tex(-a, b, -c)}$",
            f"$y = {_quad_tex(alt_a, b, c)}$",
            f"$y = {_quad_tex(a, -b, c)}$",
        ]
        choices = _make_choices(true_ans, cands)
        direction = "quay lên trên nên $a > 0$" if a > 0 else "quay xuống dưới nên $a < 0$"
        loigiai = (
            f"Quan sát đồ thị ta thấy:\n"
            f"- Bề lõm parabol {direction}.\n"
            f"- Đồ thị cắt trục tung tại $(0; {c}) \\implies c = {c}$.\n"
            f"- Đồ thị đi qua điểm $({r1}; 0)$; thay $x = {r1}$ vào hàm số $y = {_quad_tex(a, b, c)}$ được $y({r1}) = 0$.\n"
            f"Vậy hàm số cần tìm là $y = {_quad_tex(a, b, c)}$."
        )
        return caudan, choices, loigiai

    # Variant 2: Bảng biến thiên
    a = random.choice([-2, -1, 1, 2])
    xI = random.choice([-2, -1, 1, 2, 3])
    yI = random.choice([-3, -2, -1, 1, 2, 3])
    b = -2 * a * xI
    c = a * xI * xI + yI

    if a > 0:
        tab_var = f"\\tkzTabVar{{+/$+\\infty$,-/${yI}$,+/$+\\infty$}}"
        be_lom = "quay lên trên nên $a > 0$"
    else:
        tab_var = f"\\tkzTabVar{{-/$ -\\infty$,+/${yI}$,-/$-\\infty$}}"
        be_lom = "quay xuống dưới nên $a < 0$"

    tikz = (
        "\\begin{tikzpicture}[scale=0.8]\n"
        f"    \\tkzTabInit[lgt=1.2,espcl=2.5,deltacl=0.6]{{$x$/0.8,$y$/1.5}}{{$ -\\infty$,${xI}$,$+\\infty$}}\n"
        f"    {tab_var}\n"
        "\\end{tikzpicture}"
    )
    caudan = f"\\immini{{Hàm số nào có bảng biến thiên như hình dưới đây?}}{{\n{tikz}\n}}"
    true_ans = f"$y = {_quad_tex(a, b, c)}$"
    alt_a = 2 if a == 1 else (1 if a == 2 else (-2 if a == -1 else -1))
    cands = [
        f"$y = {_quad_tex(-a, -b, c)}$",
        f"$y = {_quad_tex(a, b, c + 1)}$",
        f"$y = {_quad_tex(alt_a, -2 * alt_a * xI, alt_a * xI * xI + yI + 1)}$",
        f"$y = {_quad_tex(a, -b, c)}$",
    ]
    choices = _make_choices(true_ans, cands)
    loigiai = (
        f"Từ bảng biến thiên ta có:\n"
        f"- Parabol có bề lõm {be_lom}.\n"
        f"- Tọa độ đỉnh là $I({xI}; {yI})$.\n"
        f"Kiểm tra với $y = {_quad_tex(a, b, c)}$: $x_I = -\\dfrac{{{b}}}{{2\\cdot({a})}} = {xI}$ và $y({xI}) = {yI}$ (thỏa mãn)."
    )
    return caudan, choices, loigiai


def K10_C3_MC_Parabol_NhanDangDoThi_TheoDauABC():
    """Ảnh 3 Câu 7: Nhận dạng dạng đồ thị parabol từ dấu a, b, c (4 hình TikZ)."""
    # 4 cấu hình parabol tách biệt rõ ràng bằng dấu (a, đỉnh xI, tung độ gốc c)
    # y = a(x - xI)^2 + yI; chọn (a, xI, c) phân biệt cả 4 đáp án
    configs = [
        # (a, xI, yI, mô tả)
        (1, -1.0, -1.5, "a > 0, b > 0, c < 0"),     # c = 1*(1) - 1.5 = -0.5 < 0
        (-1, -0.5, 0.25, "a < 0, b < 0, c = 0"),    # c = 0 (đỉnh góc phần tư II)
        (-1, 0.8, 2.0, "a < 0, b > 0, c > 0"),      # c = -0.64 + 2 = 1.36 > 0
        (1, 1.0, 0.8, "a > 0, b < 0, c > 0"),       # c = 1.8 > 0
        (1, -1.0, 0.8, "a > 0, b > 0, c > 0"),      # c = 1.8 > 0
        (-1, 1.0, -0.5, "a < 0, b > 0, c < 0"),     # c = -1.5 < 0
    ]
    chosen = random.sample(configs, 4)
    target = chosen[0]
    a_t, xI_t, yI_t, desc_t = target
    c_t = a_t * xI_t * xI_t + yI_t
    b_t = -2 * a_t * xI_t

    def _sign_txt(name, val):
        if abs(val) < 1e-9:
            return f"{name} = 0"
        return f"{name} > 0" if val > 0 else f"{name} < 0"

    cond_str = f"${_sign_txt('a', a_t)}$; ${_sign_txt('b', b_t)}$ và ${_sign_txt('c', c_t)}$"
    caudan = f"Nếu hàm số $y = ax^2 + bx + c$ có {cond_str} thì đồ thị hàm số của nó có dạng"

    def _draw_mini_parab(aa, x0, y0):
        d1 = round(x0 - 1.6, 2)
        d2 = round(x0 + 1.6, 2)
        return (
            "\\begin{tikzpicture}[scale=0.42, line join=round, line cap=round, >=stealth]\n"
            "    \\draw[->] (-2.4,0) -- (2.4,0) node[below] {\\scriptsize $x$};\n"
            "    \\draw[->] (0,-2.0) -- (0,2.4) node[left] {\\scriptsize $y$};\n"
            "    \\node[below left] at (0,0) {\\scriptsize $O$};\n"
            f"    \\draw[thick, domain={d1}:{d2}, samples=80] plot (\\x, {{{aa}*(\\x-({x0}))*(\\x-({x0})) + ({y0})}});\n"
            "\\end{tikzpicture}"
        )

    true_fig = _draw_mini_parab(a_t, xI_t, yI_t)
    wrong_figs = [_draw_mini_parab(aa, x0, y0) for aa, x0, y0, _ in chosen[1:]]
    choices = _make_choices(true_fig, wrong_figs)

    huong = "quay lên trên" if a_t > 0 else "quay xuống dưới"
    ben = "bên trái trục $Oy$" if xI_t < 0 else "bên phải trục $Oy$"
    cat_oy = "cắt trục $Oy$ tại điểm có tung độ dương" if c_t > 0 else ("cắt trục $Oy$ tại điểm có tung độ âm" if c_t < 0 else "đi qua gốc tọa độ $O(0;0)$")
    loigiai = (
        f"Dựa vào dấu của các hệ số:\n"
        f"- Vì $a {'>' if a_t > 0 else '<'} 0$ nên bề lõm parabol {huong}.\n"
        f"- Hoành độ đỉnh $x_I = -\\dfrac{{b}}{{2a}} {'<' if xI_t < 0 else '>'} 0$ nên đỉnh nằm về phía {ben}.\n"
        f"- Giao điểm với trục tung là $(0; c)$ với ${desc_t.split(', ')[2]}$ nên đồ thị {cat_oy}."
    )
    return caudan, choices, loigiai


def K10_C3_MC_Parabol_XacDinhHeSo_Dinh_DiemDiQua():
    variant = random.choice([1, 2, 3])
    if variant == 1:
        # Ảnh 2 Câu 5: Biết a, điểm M(0; c) và trục đối xứng x = xI
        a = random.choice([-2, -1, 1, 2])
        xI = random.choice([-2, -1, 1, 2])
        b = -2 * a * xI
        c = random.choice([-3, -2, 2, 3, 4, 5])
        f_tex = _quad_tex(a, b, c)
        caudan = f"Xác định parabol $(P): y = {a if abs(a) > 1 else ('-' if a < 0 else '')}x^2 + bx + c$, biết $(P)$ đi qua điểm $M(0; {c})$ và có trục đối xứng $x = {xI}$."
        true_ans = f"$y = {f_tex}$"
        cands = [
            f"$y = {_quad_tex(a, -b, c)}$",
            f"$y = {_quad_tex(a, b + 1, c)}$",
            f"$y = {_quad_tex(a, -b, c - 2)}$",
            f"$y = {_quad_tex(-a, b, c)}$",
        ]
        choices = _make_choices(true_ans, cands)
        loigiai = (
            f"- Điểm $M(0; {c}) \\in (P) \\implies c = {c}$.\n"
            f"- Trục đối xứng $x = -\\dfrac{{b}}{{2\\cdot({a})}} = {xI} \\iff b = {b}$.\n"
            f"Vậy $(P): y = {f_tex}$."
        )
        return caudan, choices, loigiai

    if variant == 2:
        # Ảnh 2 Câu 6: Biết b, hoành độ đỉnh xI và điểm đi qua M(x0; y0) -> tính S = a + c
        a = random.choice([-2, -1, 1, 2])
        xI = random.choice([-3, -2, -1, 1, 2])
        b = -2 * a * xI
        c = random.choice([-4, -3, -2, 1, 2, 3, 4])
        x0 = random.choice([-2, -1, 1, 2])
        while x0 == 0:
            x0 = 1
        y0 = a * x0 * x0 + b * x0 + c
        S = a + c
        b_part = _signed_frac_term(b, "x")
        caudan = (
            f"Biết rằng $(P): y = ax^2{b_part} + c$ có hoành độ đỉnh bằng ${xI}$ "
            f"và đi qua điểm $M({x0}; {y0})$. Tính tổng $S = a + c$."
        )
        cands = [
            f"$S = {-S}$" if S != 0 else "$S = 2$",
            f"$S = {S + 1}$",
            f"$S = {S - 1}$",
            f"$S = {a - c}$" if a - c != S else f"$S = {S + 3}$",
        ]
        choices = _make_choices(f"$S = {S}$", cands)
        loigiai = (
            f"- Hoành độ đỉnh $x_I = -\\dfrac{{{b}}}{{2a}} = {xI} \\iff a = {a}$.\n"
            f"- Điểm $M({x0}; {y0}) \\in (P) \\implies {y0} = {a}\\cdot({x0})^2 {_signed_frac_term(b)}\\cdot({x0}) + c \\iff c = {c}$.\n"
            f"Vậy $S = a + c = {a} + ({c}) = {S}$."
        )
        return caudan, choices, loigiai

    # Variant 3: Ảnh 2 Câu 7: Biết c, đỉnh I(xI; yI) -> tìm a và b
    a = random.choice([-2, -1, 1, 2])
    xI = random.choice([-2, -1, 1, 2])
    b = -2 * a * xI
    yI = random.choice([-5, -3, -1, 1, 2, 4])
    c = yI - a * xI * xI - b * xI
    while c == 0:
        yI += 1
        c = yI - a * xI * xI - b * xI
    c_str = _signed_frac_term(c)
    caudan = f"Biết parabol $y = ax^2 + bx{c_str}$ có đỉnh $I({xI}; {yI})$. Tìm $a$ và $b$."
    true_ans = f"$a = {a};\\ b = {b}$"
    cands = [
        f"$a = {a};\\ b = {-b}$",
        f"$a = {-a};\\ b = {b}$",
        f"$a = {-a};\\ b = {-b}$",
        f"$a = 0;\\ b = {b - 1}$",
    ]
    choices = _make_choices(true_ans, cands)
    loigiai = (
        f"Parabol có đỉnh $I({xI}; {yI})$ nên:\n"
        f"- Hoành độ đỉnh: $-\\dfrac{{b}}{{2a}} = {xI} \\iff b = {-2 * xI}a$.\n"
        f"- Điểm $I({xI}; {yI})$ thuộc $(P)$ nên ${yI} = {xI**2}a {_signed_frac_term(xI, 'b')} {c_str}$.\n"
        f"Giải hệ tìm được $a = {a},\\ b = {b}$."
    )
    return caudan, choices, loigiai


def K10_C3_MC_Parabol_CatTrucHoanh_ThamSo():
    """Ảnh 2 Câu 8: Tìm m để y = x^2 + 2mx + m^2 - km + c0 cắt trục hoành tại hai điểm phân biệt."""
    k = random.choice([-4, -3, -2, 2, 3, 4])
    c0 = random.choice([-2, -1, 1, 2, 3])
    # x^2 + 2mx + (m^2 - km + c0) = 0 => Delta' = m^2 - (m^2 - km + c0) = km - c0 > 0
    bound = Fraction(c0, k)
    sym = ">" if k > 0 else "<"
    opp = "<" if k > 0 else ">"
    ge_sym = "\\ge" if k > 0 else "\\le"

    const_expr = f"m^2 {_signed_frac_term(-k, 'm')} {_signed_frac_term(c0)}"
    caudan = (
        f"Tìm tất cả các giá trị của tham số $m$ để đồ thị hàm số "
        f"$y = x^2 + 2mx + {const_expr}$ cắt trục hoành tại hai điểm phân biệt."
    )
    true_ans = f"$m {sym} {_frac_tex(bound)}$"
    cands = [
        f"$m {opp} {_frac_tex(bound)}$",
        f"$m {ge_sym} {_frac_tex(bound)}$",
        f"$m {sym} {_frac_tex(-bound)}$",
        f"$m = {_frac_tex(-bound)}$",
    ]
    choices = _make_choices(true_ans, cands)
    loigiai = (
        f"Phương trình hoành độ giao điểm với trục hoành $Ox$: $x^2 + 2mx + {const_expr} = 0$.\n"
        f"Đồ thị cắt trục hoành tại hai điểm phân biệt khi và chỉ khi $\\Delta' > 0$:\n"
        f"$$\\Delta' = m^2 - ({const_expr}) = {_lin_tex(k, -c0, var='m')} > 0 \\iff m {sym} {_frac_tex(bound)}.$$"
    )
    return caudan, choices, loigiai


def K10_C3_MC_Parabol_ThucTe_CongParabol():
    w = random.choice([4, 6, 8, 10])
    half = w // 2
    denom = random.choice([1, 2, 4])
    while (half * half) % denom != 0:
        denom = 1
    h = (half * half) // denom
    eq_tex = "y = -x^2" if denom == 1 else f"y = -\\dfrac{{1}}{{{denom}}}x^2"
    k_draw = 4.0 / (half * half)
    tikz = (
        "\\begin{tikzpicture}[scale=0.5, line join=round, line cap=round, >=stealth]\n"
        f"    \\draw[->] ({-half - 1},0) -- ({half + 1},0) node[below] {{$x$}};\n"
        "    \\draw[->] (0,-4.5) -- (0,1.2) node[left] {$y$};\n"
        "    \\node[above left] at (0,0) {$O$};\n"
        f"    \\draw[thick, domain={-half}:{half}, samples=100] plot (\\x, {{-{k_draw:.4f}*\\x*\\x}});\n"
        f"    \\draw[dashed] ({-half},-4) -- ({half},-4) node[midway, above] {{$d = {w}\\text{{m}}$}};\n"
        "    \\draw[<->] (0,0) -- (0,-4) node[midway, left] {$h$};\n"
        "\\end{tikzpicture}"
    )
    caudan = f"\\immini{{Một chiếc cổng hình parabol có phương trình dạng ${eq_tex}$ và chiều rộng chân cổng là $d = {w}\\text{{ m}}$. Hãy tính chiều cao $h$ của cổng.}}{{\n{tikz}\n}}"
    choices = _make_choices(
        f"$h = {h}\\text{{ m}}$",
        [f"$h = {h + 2}\\text{{ m}}$", f"$h = {max(1, h - 3)}\\text{{ m}}$", f"$h = {w}\\text{{ m}}$", f"$h = {h + 4}\\text{{ m}}$"],
    )
    loigiai = (
        f"Chọn hệ trục tọa độ như hình vẽ, hai chân cổng ứng với $x = -{half}$ và $x = {half}$.\n"
        f"Tung độ tại chân cổng là $y({half}) = -{h}$.\n"
        f"Vậy chiều cao của cổng là $h = |-{h}| = {h}\\text{{ m}}$."
    )
    return caudan, choices, loigiai


def K10_C3_MC_Parabol_DocDoThi_DauHeSo_Va_BatPhuongTrinh():
    x1 = random.choice([-3, -2, -1])
    x2 = random.choice([1, 2, 3])
    a_sign = random.choice([-1, 1])
    ask_gt = random.choice([True, False])  # f(x) > 0 hay f(x) < 0
    ineq = ">" if ask_gt else "<"

    # Điều chỉnh hệ số vẽ sao cho đỉnh cao khoảng ~2.5-3.0 đơn vị
    span = (x2 - x1) / 2.0
    a_draw = a_sign * (2.5 / (span * span))
    y_v = -a_draw * span * span
    xmin, xmax = x1 - 1.0, x2 + 1.0
    ymin = min(-1.5, y_v - 0.6)
    ymax = max(1.5, y_v + 0.6)
    dom_l, dom_r = x1 - 0.5, x2 + 0.5

    tikz = (
        "\\begin{tikzpicture}[scale=0.6, line join=round, line cap=round, >=stealth]\n"
        f"    \\draw[->] ({xmin:.1f},0) -- ({xmax:.1f},0) node[below] {{$x$}};\n"
        f"    \\draw[->] (0,{ymin:.1f}) -- (0,{ymax:.1f}) node[left] {{$y$}};\n"
        "    \\node[below right] at (0,0) {$O$};\n"
        f"    \\draw[thick, blue, domain={dom_l:.1f}:{dom_r:.1f}, samples=100] plot (\\x, {{{a_draw:.3f}*(\\x-({x1}))*(\\x-({x2}))}});\n"
        f"    \\node[below left] at ({x1},0) {{${x1}$}};\n"
        f"    \\node[below right] at ({x2},0) {{${x2}$}};\n"
        f"    \\fill ({x1},0) circle (1.5pt);\n"
        f"    \\fill ({x2},0) circle (1.5pt);\n"
        "\\end{tikzpicture}"
    )
    inside = f"$({x1}; {x2})$"
    outside = f"$(-\\infty; {x1}) \\cup ({x2}; +\\infty)$"
    is_inside = (a_sign < 0 and ask_gt) or (a_sign > 0 and not ask_gt)
    true_ans = inside if is_inside else outside
    opp_ans = outside if is_inside else inside

    caudan = f"\\immini{{Cho hàm số bậc hai $y = f(x)$ có đồ thị như hình vẽ bên. Tập nghiệm của bất phương trình $f(x) {ineq} 0$ là:}}{{\n{tikz}\n}}"
    choices = _make_choices(
        true_ans,
        [opp_ans, f"$[{x1}; {x2}]$", f"$(0; {x2})$"],
    )
    pos_txt = "phía trên trục hoành $Ox$" if ask_gt else "phía dưới trục hoành $Ox$"
    loigiai = (
        f"Bất phương trình $f(x) {ineq} 0$ ứng với phần đồ thị nằm {pos_txt}.\n"
        f"Quan sát đồ thị cắt $Ox$ tại $x = {x1}$ và $x = {x2}$, ta được tập nghiệm là ${true_ans.strip('$')}$."
    )
    return caudan, choices, loigiai


# ==============================================================================
# BÀI 17: DẤU TAM THỨC BẬC HAI & BẤT PHƯƠNG TRÌNH BẬC HAI
# ==============================================================================

def K10_C7_MC_TamThuc_NhanDien_Va_DieuKien():
    """Ảnh 4 Câu 1, 4: Nhận diện tam thức bậc hai và điều kiện tham số."""
    variant = random.choice([1, 2])
    if variant == 1:
        a = random.choice([-4, -3, -2, 2, 3, 5])
        b = random.choice([-5, -3, -2, 2, 3, 4])
        c = random.choice([-7, -5, -1, 1, 5, 7])
        f_ok = _quad_tex(a, b, c)
        w1 = _lin_tex(b, c)
        w2 = f"{a}x^3 {_signed_frac_term(b, 'x')} {_signed_frac_term(c)}"
        w3 = f"x^4 {_signed_frac_term(-1, 'x^2')} {_signed_frac_term(1)}"
        caudan = "Tìm khẳng định đúng trong các khẳng định sau?"
        choices = _make_choices(
            f"$f(x) = {f_ok}$ là tam thức bậc hai.",
            [
                f"$f(x) = {w1}$ là tam thức bậc hai.",
                f"$f(x) = {w2}$ là tam thức bậc hai.",
                f"$f(x) = {w3}$ là tam thức bậc hai.",
            ],
        )
        loigiai = (
            f"Tam thức bậc hai đối với $x$ là biểu thức có dạng $ax^2 + bx + c$ với $a, b, c \\in \\mathbb{{R}}$ và $a \\ne 0$.\n"
            f"Vậy $f(x) = {f_ok}$ là tam thức bậc hai."
        )
        return caudan, choices, loigiai

    # Variant 2: Điều kiện m để (am + k)x^2 + bx + c là tam thức bậc hai
    a = random.choice([1, 2, 3])
    k = random.choice([-4, -3, -2, -1, 1, 2, 3, 4])
    b = random.choice([-3, -2, 2, 3, 5])
    c = random.choice([-5, -3, -1, 1, 3, 5])
    r = Fraction(-k, a)
    m_coef = _lin_tex(a, k, var="m")
    caudan = (
        f"Tìm tất cả các giá trị của tham số $m$ để biểu thức "
        f"$f(x) = ({m_coef})x^2 {_signed_frac_term(b, 'x')} {_signed_frac_term(c)}$ là một tam thức bậc hai."
    )
    choices = _make_choices(
        f"$m \\ne {_frac_tex(r)}$",
        [r"$m \in \mathbb{R}$", f"$m > {_frac_tex(r)}$", f"$m < {_frac_tex(r)}$", f"$m \\ne {_frac_tex(-r)}$"],
    )
    loigiai = (
        f"Biểu thức $f(x)$ là tam thức bậc hai khi và chỉ khi hệ số của $x^2$ khác $0$:\n"
        f"$${m_coef} \\ne 0 \\iff m \\ne {_frac_tex(r)}.$$"
    )
    return caudan, choices, loigiai


def K10_C7_MC_TamThuc_Dau_VoNghiem_Hoac_NghiemKep():
    """Ảnh 4 Câu 3, 6: Dấu của tam thức vô nghiệm hoặc có nghiệm kép."""
    variant = random.choice([1, 2])
    if variant == 1:
        c = random.choice([1, 2, 3, 4, 5, 9])
        pos = random.choice([True, False])
        f_tex = f"x^2 + {c}" if pos else f"-x^2 - {c}"
        sym = ">" if pos else "<"
        opp = "<" if pos else ">"
        caudan = f"Cho $f(x) = {f_tex}$. Khẳng định nào sau đây là đúng?"
        true_ans = f"$f(x) {sym} 0, \\forall x \\in \\mathbb{{R}}$."
        choices = _make_choices(
            true_ans,
            [
                f"$f(x) {opp} 0, \\forall x \\in \\mathbb{{R}}$.",
                r"$f(x) = 0, \forall x \in \mathbb{R}$.",
                f"$f(x) {opp} 0, \\forall x \\in (-\\infty; -{c}) \\cup ({c}; +\\infty)$.",
            ],
        )
        loigiai = (
            f"Ta có $x^2 \\ge 0, \\forall x \\in \\mathbb{{R}} \\implies {f_tex} {sym} 0, \\forall x \\in \\mathbb{{R}}$."
        )
        return caudan, choices, loigiai

    # Variant 2: f(x) = ±(x - r)^2
    r = random.choice([-4, -3, -2, -1, 1, 2, 3, 4])
    pos = random.choice([True, False])
    a = 1 if pos else -1
    b = -2 * a * r
    c = a * r * r
    f_tex = _quad_tex(a, b, c)
    sym = ">" if pos else "<"
    opp = "<" if pos else ">"
    caudan = f"Cho $f(x) = {f_tex}$. Mệnh đề nào sau đây là đúng?"
    choices = _make_choices(
        f"$f(x) {sym} 0, \\forall x \\ne {r}$.",
        [
            f"$f(x) {sym} 0, \\forall x \\in \\mathbb{{R}}$.",
            f"$f(x) {sym} 0, \\forall x \\ne {2 * r}$.",
            f"$f(x) {opp} 0, \\forall x \\in \\mathbb{{R}}$.",
        ],
    )
    loigiai = (
        f"Ta có $f(x) = {f_tex} = {'' if pos else '-'}{_signed_factor(r)}^2$.\n"
        f"Suy ra $f(x) {sym} 0$ với mọi $x \\ne {r}$ (tại $x = {r}$ thì $f({r}) = 0$)."
    )
    return caudan, choices, loigiai


def K10_C7_MC_TamThuc_TimNghiem():
    """Ảnh 4 Câu 7: Tìm nghiệm của tam thức bậc hai."""
    variant = random.choice([1, 2])
    if variant == 1:
        r = random.choice([2, 3, 4, 5, 6])
        r1, r2 = r, -r
        f_tex = f"x^2 - {r * r}"
    else:
        r1 = random.choice([-4, -3, -2, -1])
        r2 = random.choice([1, 2, 3, 4])
        while r1 + r2 == 0:
            r2 = random.choice([1, 2, 3, 4])
        f_tex = _quad_tex(1, -(r1 + r2), r1 * r2)

    caudan = f"Nghiệm của tam thức bậc hai $f(x) = {f_tex}$ là"
    true_ans = f"$\\left[\\begin{{aligned}} x &= {r1} \\\\ x &= {r2} \\end{{aligned}}\\right.$"
    cands = [
        f"$x = {r1}$",
        f"$x = {r2}$",
        f"$\\left[\\begin{{aligned}} x &= 0 \\\\ x &= {r * r if variant == 1 else r1 + r2} \\end{{aligned}}\\right.$",
        f"$\\left[\\begin{{aligned}} x &= {-r1} \\\\ x &= {-r2 + 1} \\end{{aligned}}\\right.$",
    ]
    choices = _make_choices(true_ans, cands)
    loigiai = (
        f"Giải phương trình $f(x) = 0 \\iff {f_tex} = 0 \\iff \\left[\\begin{{aligned}} x &= {r1} \\\\ x &= {r2}. \\end{{aligned}}\\right.$"
    )
    return caudan, choices, loigiai


def K10_C7_MC_TamThuc_XetDau_CoBan():
    """Ảnh 4 Câu 8, 10, 11 & Ảnh 5 Câu 1, 4, 9."""
    case = random.choice([1, 2, 3, 4])
    x1 = random.randint(-4, 0)
    x2 = random.randint(1, 6)
    if case == 1:
        # f(x) = x^2 - Sx + P >= 0
        f_tex = _quad_tex(1, -(x1 + x2), x1 * x2)
        caudan = f"Tam thức bậc hai $f(x) = {f_tex}$ nhận giá trị không âm khi và chỉ khi"
        true_ans = f"$x \\in (-\\infty; {x1}] \\cup [{x2}; +\\infty)$."
        cands = [
            f"$x \\in [{x1}; {x2}]$.",
            f"$x \\in ({x1}; {x2})$.",
            f"$x \\in (-\\infty; {x1}) \\cup ({x2}; +\\infty)$.",
        ]
        loigiai = (
            f"Tam thức $f(x) = {f_tex}$ có $a = 1 > 0$ và hai nghiệm $x_1 = {x1}, x_2 = {x2}$.\n"
            f"Vậy $f(x) \\ge 0 \\iff x \\in (-\\infty; {x1}] \\cup [{x2}; +\\infty)$."
        )
    elif case == 2:
        # f(x) = -x^2 + Sx - P >= 0
        x1 = random.randint(1, 3)
        x2 = x1 + random.randint(1, 4)
        f_tex = _quad_tex(-1, x1 + x2, -(x1 * x2))
        caudan = f"Tam thức bậc hai $f(x) = {f_tex}$ nhận giá trị không âm khi và chỉ khi"
        true_ans = f"$x \\in [{x1}; {x2}]$."
        cands = [
            f"$x \\in (-\\infty; {x1}] \\cup [{x2}; +\\infty)$.",
            f"$x \\in ({x1}; {x2})$.",
            f"$x \\in (-\\infty; {x1}) \\cup ({x2}; +\\infty)$.",
        ]
        loigiai = (
            f"Tam thức $f(x) = {f_tex}$ có $a = -1 < 0$ và hai nghiệm $x_1 = {x1}, x_2 = {x2}$.\n"
            f"Trong trái, ngoài cùng $\\implies f(x) \\ge 0 \\iff x \\in [{x1}; {x2}]$."
        )
    elif case == 3:
        # f(x) < 0 với a = 1 (Ảnh 4 Câu 8 & Ảnh 5 Câu 9)
        f_tex = _quad_tex(1, -(x1 + x2), x1 * x2)
        caudan = f"Tam thức bậc hai $f(x) = {f_tex}$ nhận giá trị âm khi và chỉ khi"
        true_ans = f"$x \\in ({x1}; {x2})$."
        cands = [
            f"$x \\in [{x1}; {x2}]$.",
            f"$x \\in (-\\infty; {x1}) \\cup ({x2}; +\\infty)$.",
            f"$x \\in (-\\infty; {x1}] \\cup [{x2}; +\\infty)$.",
        ]
        loigiai = (
            f"Tam thức $f(x) = {f_tex}$ có $a = 1 > 0$ và hai nghiệm $x_1 = {x1}, x_2 = {x2}$.\n"
            f"Vậy $f(x) < 0 \\iff x \\in ({x1}; {x2})$."
        )
    else:
        # Ảnh 4 Câu 11: Mô tả đồng thời dấu > 0 và < 0
        a_sign = random.choice([-1, 1])
        x1 = random.randint(1, 3)
        x2 = x1 + random.randint(1, 3)
        f_tex = _quad_tex(a_sign, -a_sign * (x1 + x2), a_sign * x1 * x2)
        caudan = f"Dấu của tam thức bậc hai $f(x) = {f_tex}$ được xác định như sau"
        in_gt = a_sign < 0
        s_in = ">" if in_gt else "<"
        s_out = "<" if in_gt else ">"
        true_ans = f"$f(x) {s_in} 0$ với ${x1} < x < {x2}$ và $f(x) {s_out} 0$ với $x < {x1}$ hoặc $x > {x2}$."
        cands = [
            f"$f(x) {s_out} 0$ với ${x1} < x < {x2}$ và $f(x) {s_in} 0$ với $x < {x1}$ hoặc $x > {x2}$.",
            f"$f(x) {s_in} 0$ với ${-x2} < x < {-x1}$ và $f(x) {s_out} 0$ với $x < {-x2}$ hoặc $x > {-x1}$.",
            f"$f(x) {s_out} 0$ với ${-x2} < x < {-x1}$ và $f(x) {s_in} 0$ với $x < {-x2}$ hoặc $x > {-x1}$.",
        ]
        loigiai = (
            f"Tam thức $f(x) = {f_tex}$ có $a = {a_sign}$ và hai nghiệm $x_1 = {x1}, x_2 = {x2}$.\n"
            f"Áp dụng quy tắc trong trái, ngoài cùng: {true_ans}"
        )

    return caudan, _make_choices(true_ans, cands), loigiai


def K10_C7_MC_TamThuc_DinhLyVeDau_HeThuc():
    case = random.choice(["le", "ge", "lt", "gt"])
    cfg = {
        "le": ("\\le", "a < 0", "\\Delta \\le 0", [("a < 0", "\\Delta \\ge 0"), ("a \\le 0", "\\Delta < 0"), ("a > 0", "\\Delta \\le 0")]),
        "ge": ("\\ge", "a > 0", "\\Delta \\le 0", [("a > 0", "\\Delta \\ge 0"), ("a < 0", "\\Delta \\le 0"), ("a \\ge 0", "\\Delta < 0")]),
        "lt": ("<", "a < 0", "\\Delta < 0", [("a < 0", "\\Delta \\le 0"), ("a > 0", "\\Delta < 0"), ("a < 0", "\\Delta > 0")]),
        "gt": (">", "a > 0", "\\Delta < 0", [("a > 0", "\\Delta \\le 0"), ("a < 0", "\\Delta < 0"), ("a > 0", "\\Delta > 0")]),
    }
    ineq, a_ok, d_ok, wrongs = cfg[case]
    caudan = (
        f"Cho tam thức $f(x) = ax^2 + bx + c\\ (a \\ne 0), \\Delta = b^2 - 4ac$. "
        f"Ta có $f(x) {ineq} 0$ với mọi $x \\in \\mathbb{{R}}$ khi và chỉ khi"
    )
    true_ans = f"$\\begin{{cases}} {a_ok} \\\\ {d_ok} \\end{{cases}}$."
    cands = [f"$\\begin{{cases}} {wa} \\\\ {wd} \\end{{cases}}$." for wa, wd in wrongs]
    loigiai = f"Theo định lý về dấu tam thức bậc hai: $f(x) {ineq} 0, \\forall x \\in \\mathbb{{R}} \\iff \\begin{{cases}} {a_ok} \\\\ {d_ok}. \\end{{cases}}$"
    return caudan, _make_choices(true_ans, cands), loigiai


def K10_C7_MC_TamThuc_HaiNghiemPhanBiet_ThamSo():
    k = random.choice([2, 4, 6])
    c2 = (k // 2) ** 2
    M0 = random.choice([12, 16, 20, 24, 28])
    c1 = (k + M0) // 2
    caudan = f"Các giá trị của tham số $m$ để tam thức bậc hai $f(x) = x^2 - (m + {k})x + {c1}m + {c2}$ có hai nghiệm phân biệt là"
    true_ans = f"$m < 0$ hay $m > {M0}$."
    cands = [
        f"$0 < m < {M0}$.",
        f"$m \\le 0$ hay $m \\ge {M0}$.",
        "$m > 0$.",
    ]
    loigiai = (
        f"Tam thức có hai nghiệm phân biệt khi và chỉ khi $\\Delta > 0$:\n"
        f"$$\\Delta = [-(m + {k})]^2 - 4({c1}m + {c2}) = m^2 - {M0}m = m(m - {M0}) > 0 "
        f"\\iff \\left[\\begin{{aligned}} m &< 0 \\\\ m &> {M0}. \\end{{aligned}}\\right.$$"
    )
    return caudan, _make_choices(true_ans, cands), loigiai


def K10_C7_MC_TamThuc_NhanDang_BangXetDau():
    x1 = random.choice([-3, -2, -1])
    x2 = random.choice([1, 2, 3])
    a_sign = random.choice([-1, 1])
    if a_sign < 0:
        tab_line = r"\tkzTabLine{ , -, 0, +, 0, -, }"
        out_txt = "nhận giá trị âm ($f(x) < 0$)"
        in_txt = "nhận giá trị dương ($f(x) > 0$)"
    else:
        tab_line = r"\tkzTabLine{ , +, 0, -, 0, +, }"
        out_txt = "nhận giá trị dương ($f(x) > 0$)"
        in_txt = "nhận giá trị âm ($f(x) < 0$)"

    caudan = (
        "Cho bảng xét dấu dưới đây:\n"
        "\\begin{center}\n"
        "\\begin{tikzpicture}\n"
        f"\\tkzTabInit[nocadre=false,lgt=1.5,espcl=2]{{$x$ / 0.8, $f(x)$ / 0.8}}{{$ -\\infty$, ${x1}$, ${x2}$, $+\\infty$}}\n"
        f"{tab_line}\n"
        "\\end{tikzpicture}\n"
        "\\end{center}\n"
        "Bảng xét dấu trên là của biểu thức nào dưới đây?"
    )
    b = -a_sign * (x1 + x2)
    c = a_sign * x1 * x2
    true_ans = f"$f(x) = {_quad_tex(a_sign, b, c)}$."
    cands = [
        f"$f(x) = {_quad_tex(-a_sign, -b, c)}$." if c != 0 else f"$f(x) = {_quad_tex(-a_sign, -b, c + 1)}$.",
        f"$f(x) = {_quad_tex(-a_sign, b, -c)}$." if (-a_sign * (x1 * x2) != c or b != -b) else f"$f(x) = {_signed_factor(x1)}{_signed_factor(x2)}$.",
        f"$f(x) = {_signed_factor(-x1)}{_signed_factor(x2)}$.",
        f"$f(x) = {_signed_factor(x1)}{_signed_factor(-x2)}$.",
    ]
    loigiai = (
        f"Từ bảng xét dấu ta thấy $f(x) = 0$ tại $x = {x1}$ và $x = {x2}$.\n"
        f"Ngoài khoảng $({x1}; {x2})$, {out_txt}; trong khoảng $({x1}; {x2})$, {in_txt}.\n"
        f"Do đó hệ số $a = {a_sign}$, suy ra $f(x) = {_quad_tex(a_sign, b, c)}$."
    )
    return caudan, _make_choices(true_ans, cands), loigiai


def K10_C7_MC_TamThuc_DienDau_BangXetDau():
    a = random.choice([2, 3, 4])
    lead = random.choice([1, -1])
    f_tex = f"x^2(x^2 - {a * a})" if lead > 0 else f"-x^2(x^2 - {a * a})"
    caudan = (
        f"Cho biểu thức $f(x) = {f_tex}$ có bảng xét dấu như sau:\n"
        "\\begin{center}\n"
        "\\begin{tikzpicture}\n"
        f"\\tkzTabInit[nocadre=false,lgt=1.5,espcl=1.5]{{$x$ / 0.8, $f(x)$ / 0.8}}{{$ -\\infty$, ${-a}$, $0$, ${a}$, $+\\infty$}}\n"
        "\\tkzTabLine{ , ?, 0, ?, 0, ?, 0, ?, }\n"
        "\\end{tikzpicture}\n"
        "\\end{center}\n"
        "Dấu trong các dấu chấm hỏi theo thứ tự từ trái sang phải là"
    )
    if lead > 0:
        true_ans = "$+, -, -, +$."
        cands = ["$+, -, +, -$.", "$-, +, -, +$.", "$+, +, -, +$."]
    else:
        true_ans = "$-, +, +, -$."
        cands = ["$-, +, -, +$.", "$+, -, +, -$.", "$-, -, +, -$."]
    loigiai = (
        f"Vì $x^2 \\ge 0$ với mọi $x \\in \\mathbb{{R}}$ và $x = 0$ là nghiệm bội chẵn nên dấu của $f(x)$ phụ thuộc vào "
        f"{'$x^2 - ' + str(a * a) + '$' if lead > 0 else '$-(x^2 - ' + str(a * a) + ')$'} "
        f"trên từng khoảng khác $0$.\nVậy thứ tự dấu từ trái sang phải là {true_ans}"
    )
    return caudan, _make_choices(true_ans, cands), loigiai


def K10_C7_MC_TamThuc_BangXetDau_XetDau_HeSo():
    # 3 cấu hình vị trí số 0 với hai nghiệm x1 < x2
    cfg = random.choice([
        # (nodes_list, line_str, a_sign, b_sign, c_sign, reason)
        (
            r"$-\infty$, $0$, $x_1$, $x_2$, $+\infty$",
            r"\tkzTabLine{ , +, d, +, 0, -, 0, +, }",
            ">", "<", ">",
            "0 < x_1 < x_2 \\text{ và } a > 0",
        ),
        (
            r"$-\infty$, $x_1$, $0$, $x_2$, $+\infty$",
            r"\tkzTabLine{ , +, 0, -, d, -, 0, +, }",
            ">", "<", "<",
            "x_1 < 0 < x_2 \\text{ nên } f(0) = c < 0",
        ),
        (
            r"$-\infty$, $x_1$, $x_2$, $0$, $+\infty$",
            r"\tkzTabLine{ , -, 0, +, 0, -, d, -, }",
            "<", "<", "<",
            "x_1 < x_2 < 0 \\text{ và } a < 0",
        ),
    ])
    nodes, line_str, sa, sb, sc, hint = cfg
    if sa == ">" and sb == "<" and sc == "<":
        # Với x1 < 0 < x2 không đủ kết luận dấu b duy nhất nếu chưa biết |x1| vs |x2|, nên tránh dùng cấu hình mơ hồ dấu b!
        nodes = r"$-\infty$, $0$, $x_1$, $x_2$, $+\infty$"
        line_str = r"\tkzTabLine{ , -, d, -, 0, +, 0, -, }"
        sa, sb, sc, hint = "<", ">", "<", "0 < x_1 < x_2 \\text{ và } a < 0"

    caudan = (
        "Cho $f(x) = ax^2 + bx + c\\ (a \\ne 0)$ có bảng xét dấu dưới đây:\n"
        "\\begin{center}\n"
        "\\begin{tikzpicture}\n"
        f"\\tkzTabInit[nocadre=false,lgt=1.5,espcl=1.8]{{$x$ / 0.8, $f(x)$ / 0.8}}{{{nodes}}}\n"
        f"{line_str}\n"
        "\\end{tikzpicture}\n"
        "\\end{center}\n"
        "Hỏi mệnh đề nào dưới đây đúng?"
    )
    true_ans = f"$a {sa} 0, b {sb} 0, c {sc} 0$."
    opp = lambda s: "<" if s == ">" else ">"
    cands = [
        f"$a {opp(sa)} 0, b {sb} 0, c {sc} 0$.",
        f"$a {sa} 0, b {opp(sb)} 0, c {sc} 0$.",
        f"$a {sa} 0, b {sb} 0, c {opp(sc)} 0$.",
    ]
    loigiai = (
        f"Từ bảng xét dấu ta có ${hint}$:\n"
        f"- Dấu ngoài khoảng hai nghiệm suy ra $a {sa} 0$.\n"
        f"- Tổng hai nghiệm $x_1 + x_2 = -\\dfrac{{b}}{{a}}$ cùng dấu với $x_1, x_2$ $\\implies b {sb} 0$.\n"
        f"- Tích hai nghiệm $x_1 x_2 = \\dfrac{{c}}{{a}} > 0 \\implies c {sc} 0$.\n"
        f"Vậy $a {sa} 0, b {sb} 0, c {sc} 0$."
    )
    return caudan, _make_choices(true_ans, cands), loigiai


def K10_C7_MC_TamThuc_DauPhanThuc_TrenKhoang():
    x0 = random.choice([2, 3, 4])
    x1 = random.choice([1, 2, 3])
    k = random.choice([2, 3, 5])
    caudan = (
        f"Cho biểu thức $f(x) = \\dfrac{{(x^2 - {2 * x0}x + {x0**2})(x + {x1})}}{{{k}x}}$. "
        f"Trong khoảng $(0; {x0})$, $f(x)$ mang dấu gì?"
    )
    choices = _make_choices("dương.", ["âm.", "không dương.", "không âm."])
    loigiai = (
        f"Ta có $f(x) = \\dfrac{{(x - {x0})^2(x + {x1})}}{{{k}x}}$.\n"
        f"Với $x \\in (0; {x0})$: $(x - {x0})^2 > 0$, $x + {x1} > 0$, ${k}x > 0$ nên $f(x) > 0$ (mang dấu dương)."
    )
    return caudan, choices, loigiai


def K10_C7_MC_TamThuc_BieuThuc_LuonDuong():
    p = random.choice([1, 3])
    q_ok = random.choice([1, 2, 3]) if p == 1 else random.choice([3, 4])
    caudan = "Với số thực $x$ bất kì, biểu thức nào sau đây luôn nhận giá trị dương?"
    true_ans = f"$x^2 + {p if p > 1 else ''}x + {q_ok}$."
    p_even = random.choice([2, 4])
    half = p_even // 2
    cands = [
        f"$x^2 - {p_even}x + {half * half}$.",
        f"$x^2 + {p_even}x + {half * half}$.",
        f"$x^2 + {p if p > 1 else ''}x - 1$.",
    ]
    loigiai = (
        f"Xét $f(x) = {true_ans.strip('$.')}$: có $a = 1 > 0$ và $\\Delta = {p}^2 - 4\\cdot{q_ok} = {p*p - 4*q_ok} < 0$.\n"
        f"Do đó $f(x) > 0$ với mọi $x \\in \\mathbb{{R}}$."
    )
    return caudan, _make_choices(true_ans, cands), loigiai


# ==============================================================================
# BÀI 18: PHƯƠNG TRÌNH QUY VỀ PHƯƠNG TRÌNH BẬC HAI
# ==============================================================================

def K10_C7_MC_PT_CanF_Bang_CanG():
    """Ảnh 6 Câu 1, 7, 10, 11: sqrt(A(x)) = sqrt(B(x)) ngẫu nhiên & kiểm tra điều kiện tự động."""
    mode = random.choice(["two_valid", "one_valid", "zero_valid"])

    for _ in range(80):
        r1 = random.randint(-6, 5)
        r2 = random.randint(-5, 6)
        if r1 == r2:
            continue
        # Chọn g(x) = m*x + n sao cho tại r1 và r2, g có dấu theo ý muốn
        m = random.choice([-5, -3, -2, -1, 1, 2, 3])
        if mode == "two_valid":
            # g(r1) > 0 và g(r2) > 0
            min_mr = min(m * r1, m * r2)
            n = -min_mr + random.choice([2, 3, 5])
        elif mode == "one_valid":
            # Giữa m*r1 và m*r2 lấy n để 1 dương, 1 âm
            lo, hi = min(m * r1, m * r2), max(m * r1, m * r2)
            if hi - lo < 2:
                continue
            n = -((lo + hi) // 2)
            if m * r1 + n == 0 or m * r2 + n == 0:
                continue
        else:
            # Cả hai âm
            max_mr = max(m * r1, m * r2)
            n = -max_mr - random.choice([2, 4, 6])

        # A(x) - (mx + n) = (x - r1)(x - r2) => A(x) = x^2 - (r1+r2-m)x + (r1*r2 + n)
        bA = -(r1 + r2) + m
        cA = r1 * r2 + n
        val1 = m * r1 + n
        val2 = m * r2 + n
        valid = [r for r, v in [(r1, val1), (r2, val2)] if v >= 0]
        if (mode == "two_valid" and len(valid) == 2) or (mode == "one_valid" and len(valid) == 1) or (mode == "zero_valid" and len(valid) == 0):
            break

    A_tex = _quad_tex(1, bA, cA)
    B_tex = _lin_tex(m, n)

    if mode == "two_valid":
        s_val = r1 + r2
        caudan = f"Tổng tất cả các nghiệm của phương trình $\\sqrt{{{A_tex}}} = \\sqrt{{{B_tex}}}$ là"
        true_ans = f"${s_val}$."
        cands = [f"${-s_val}$." if s_val != 0 else "$1$.", f"${s_val + 2}$.", f"${s_val - 2}$."]
        loigiai = (
            f"Bình phương hai vế của phương trình:\n"
            f"$${A_tex} = {B_tex} \\iff {_quad_tex(1, -(r1+r2), r1*r2)} = 0 \\iff \\left[\\begin{{aligned}} x &= {r1} \\\\ x &= {r2}. \\end{{aligned}}\\right.$$\n"
            f"Thử lại cả hai giá trị đều làm biểu thức dưới căn bằng ${val1}$ và ${val2}$ (không âm, thỏa mãn).\n"
            f"Tổng các nghiệm là ${r1} + ({r2}) = {s_val}$."
        )
    elif mode == "one_valid":
        ok_r = valid[0]
        bad_r = r2 if ok_r == r1 else r1
        caudan = f"Nghiệm của phương trình $\\sqrt{{{A_tex}}} = \\sqrt{{{B_tex}}}$ là"
        true_ans = f"$x = {ok_r}$."
        cands = [
            f"$x = {bad_r}$.",
            f"$\\left[\\begin{{aligned}} x &= {ok_r} \\\\ x &= {bad_r}. \\end{{aligned}}\\right.$",
            "$x \\in \\emptyset$.",
        ]
        loigiai = (
            f"Bình phương hai vế:\n"
            f"$${A_tex} = {B_tex} \\iff {_quad_tex(1, -(r1+r2), r1*r2)} = 0 \\iff \\left[\\begin{{aligned}} x &= {r1} \\\\ x &= {r2}. \\end{{aligned}}\\right.$$\n"
            f"Thử lại vào phương trình:\n"
            f"- Với $x = {ok_r}$: hai vế bằng $\\sqrt{{{m*ok_r + n}}}$ (thỏa mãn).\n"
            f"- Với $x = {bad_r}$: biểu thức dưới căn bằng ${m*bad_r + n} < 0$ (loại).\n"
            f"Vậy nghiệm của phương trình là $x = {ok_r}$."
        )
    else:
        caudan = f"Số nghiệm của phương trình $\\sqrt{{{A_tex}}} = \\sqrt{{{B_tex}}}$ là"
        true_ans = "$0$."
        cands = ["$1$.", "$2$.", "vô số."]
        loigiai = (
            f"Bình phương hai vế thu được nghiệm $x = {r1}$ hoặc $x = {r2}$.\n"
            f"Tuy nhiên khi thử lại, tại $x = {r1}$ và $x = {r2}$ biểu thức dưới căn đều âm (${val1} < 0$, ${val2} < 0$).\n"
            f"Vậy phương trình vô nghiệm (có $0$ nghiệm)."
        )

    return caudan, _make_choices(true_ans, cands), loigiai


def K10_C7_MC_PT_CanF_Bang_G():
    """Ảnh 6 Câu 2, 4, 5, 6, 12: sqrt(f(x)) = ax + b ngẫu nhiên các biến thể."""
    variant = random.choice([1, 2, 3])
    if variant == 1:
        # sqrt(x^2 - a^2) = x - a -> S = {a}
        a = random.choice([2, 3, 4, 5, 6])
        caudan = f"Tập nghiệm $S$ của phương trình $\\sqrt{{x^2 - {a * a}}} = x - {a}$ là"
        true_ans = f"$S = \\{{{a}\\}}$."
        cands = ["$S = \\{0\\}$.", f"$S = \\{{0; {a}\\}}$.", r"$S = \emptyset$."]
        loigiai = (
            f"Phương trình tương đương:\n"
            f"$$\\begin{{cases}} x - {a} \\ge 0 \\\\ x^2 - {a * a} = (x - {a})^2 \\end{{cases}} "
            f"\\iff \\begin{{cases}} x \\ge {a} \\\\ {2 * a}x = {2 * a * a} \\end{{cases}} \\iff x = {a}.$$\n"
            f"Vậy $S = \\{{{a}\\}}$."
        )
        return caudan, _make_choices(true_ans, cands), loigiai

    if variant == 2:
        # sqrt(px + q) = x - k có 2 nghiệm r1 < k < r2 => chỉ nhận r2 (giống Câu 4, 6)
        r1 = random.choice([1, 2, 3])
        r2 = random.choice([6, 7, 10, 12, 15])
        k = random.randint(r1 + 1, r2 - 1)
        # (x - k)^2 - (px + q) = (x - r1)(x - r2) => px + q = (-2k + r1 + r2)x + (k^2 - r1*r2)
        p = -2 * k + r1 + r2
        q = k * k - r1 * r2
        while p == 0:
            r2 += 1
            p = -2 * k + r1 + r2
            q = k * k - r1 * r2
        A_tex = _lin_tex(p, q)
        B_tex = _lin_tex(1, -k)
        caudan = f"Tập nghiệm $S$ của phương trình $\\sqrt{{{A_tex}}} = {B_tex}$ là"
        true_ans = f"$S = \\{{{r2}\\}}$."
        cands = [f"$S = \\{{{r1}\\}}$.", f"$S = \\{{{r1}; {r2}\\}}$.", r"$S = \emptyset$."]
        loigiai = (
            f"Phương trình tương đương:\n"
            f"$$\\begin{{cases}} {B_tex} \\ge 0 \\\\ {A_tex} = ({B_tex})^2 \\end{{cases}} "
            f"\\iff \\begin{{cases}} x \\ge {k} \\\\ {_quad_tex(1, -(r1 + r2), r1 * r2)} = 0 \\end{{cases}} \\iff x = {r2}.$$\n"
            f"Vậy $S = \\{{{r2}\\}}$."
        )
        return caudan, _make_choices(true_ans, cands), loigiai

    # Variant 3: sqrt(Ax^2 + Bx + C) = dx + e (Câu 5, 12)
    r1 = random.choice([-2, -1])
    r2 = random.choice([1, 2, 3])
    d = random.choice([1, 2])
    e = random.choice([1, 2])
    # Vế phải tại r2 dương, tại r1 âm nếu d*r1 + e < 0
    k_lead = random.choice([1, 2])  # (dx+e)^2 - k_lead*(x-r1)*(x-r2)
    while d * d == k_lead:
        k_lead += 1
    # A = d^2 - k_lead? Tùy chọn A = d^2 + 1 để dễ tính:
    # Ta chọn A(x) = (dx+e)^2 - (x - r1)(x - r2) sao cho A(x) > 0 ở r2
    aA = d * d - 1
    if aA == 0:
        aA = 2  # dùng hệ số 2 cho (x-r1)(x-r2)
        c_mult = -1
    else:
        c_mult = 1
    # A(x) = (dx+e)^2 - c_mult*(x-r1)(x-r2)
    a_coef = d * d - c_mult
    b_coef = 2 * d * e + c_mult * (r1 + r2)
    c_coef = e * e - c_mult * r1 * r2
    valid = [r for r in (r1, r2) if d * r + e >= 0]
    A_tex = _quad_tex(a_coef, b_coef, c_coef)
    B_tex = _lin_tex(d, e)
    caudan = f"Số nghiệm của phương trình $\\sqrt{{{A_tex}}} = {B_tex}$ là"
    n_ok = len(valid)
    true_ans = f"${n_ok}$."
    cands = [f"${m}$." for m in (0, 1, 2, 3) if m != n_ok]
    loigiai = (
        f"Điều kiện vế phải không âm: ${B_tex} \\ge 0 \\iff x \\ge {_frac_tex(Fraction(-e, d))}$.\n"
        f"Bình phương hai vế thu được nghiệm $x = {r1}$ và $x = {r2}$.\n"
        f"Đối chiếu điều kiện có đúng ${n_ok}$ nghiệm thỏa mãn."
    )
    return caudan, _make_choices(true_ans, cands), loigiai


def K10_C7_MC_PT_PhepBienDoi_TuongDuong():
    a = random.choice([2, 3, 4, 5])
    b = random.choice([1, 4, 6, 7])
    c = random.choice([0, -1, 1, 2])
    rhs = _lin_tex(1, -c)
    caudan = f"Cho phương trình $\\sqrt{{{a}x + {b}}} = {rhs}$ (1). Mệnh đề nào sau đây đúng?"
    true_ans = f"(1) $\\iff \\begin{{cases}} {rhs} \\ge 0 \\\\ {a}x + {b} = ({rhs})^2 \\end{{cases}}$" if c != 0 else f"(1) $\\iff \\begin{{cases}} x \\ge 0 \\\\ {a}x + {b} = x^2 \\end{{cases}}$"
    sq_rhs = f"({rhs})^2" if c != 0 else "x^2"
    cands = [
        f"(1) $\\iff {a}x + {b} = {sq_rhs}$.",
        f"(1) $\\iff {a}x + {b} = {rhs}$.",
        f"(1) $\\iff \\begin{{cases}} {a}x + {b} \\ge 0 \\\\ {a}x + {b} = {sq_rhs} \\end{{cases}}$",
    ]
    loigiai = (
        f"Phương trình dạng $\\sqrt{{A}} = B \\iff \\begin{{cases}} B \\ge 0 \\\\ A = B^2. \\end{{cases}}$\n"
        f"Áp dụng với $A = {a}x + {b}$ và $B = {rhs}$ ta được {true_ans}"
    )
    return caudan, _make_choices(true_ans, cands), loigiai


def K10_C7_MC_PT_HeSo_CanF_Bang_CanG():
    # Dịch tịnh tiến từ 2*sqrt(t^2 - t - 1) = sqrt(t^2 + 2t + 5), nghiệm t = -1, 3
    shift = random.choice([-1, 0, 1, 2])
    # x = t + shift => t = x - shift
    # t^2 - t - 1 = (x-s)^2 - (x-s) - 1 = x^2 - (2s+1)x + (s^2 + s - 1)
    b1, c1 = -(2 * shift + 1), shift * shift + shift - 1
    # t^2 + 2t + 5 = (x-s)^2 + 2(x-s) + 5 = x^2 - (2s-2)x + (s^2 - 2s + 5)
    b2, c2 = -(2 * shift - 2), shift * shift - 2 * shift + 5
    r1, r2 = -1 + shift, 3 + shift

    A_tex = _quad_tex(1, b1, c1)
    B_tex = _quad_tex(1, b2, c2)
    caudan = f"Tập nghiệm của phương trình $2\\sqrt{{{A_tex}}} = \\sqrt{{{B_tex}}}$ là"
    true_ans = f"$S = \\{{{r1}; {r2}\\}}$."
    cands = [
        f"$S = \\{{{r1}\\}}$.",
        f"$S = \\{{{r2}\\}}$.",
        r"$S = \emptyset$.",
    ]
    loigiai = (
        f"Bình phương hai vế phương trình:\n"
        f"$$4({A_tex}) = {B_tex} \\iff {_quad_tex(3, 4*b1 - b2, 4*c1 - c2)} = 0 \\iff \\left[\\begin{{aligned}} x &= {r1} \\\\ x &= {r2}. \\end{{aligned}}\\right.$$\n"
        f"Thử lại cả hai nghiệm đều thỏa mãn phương trình.\nVậy $S = \\{{{r1}; {r2}\\}}$."
    )
    return caudan, _make_choices(true_ans, cands), loigiai


def K10_C7_MC_PT_CanF_Bang_TriTuyetDoi():
    # Dịch tịnh tiến từ sqrt(3t^2 - 9t + 1) = |t - 2| (nghiệm t = -1/2 và t = 3; hai giá trị đều > 0 dưới căn)
    shift = random.choice([0, 1, 2, -1])
    # 3(x-s)^2 - 9(x-s) + 1 = 3x^2 - (6s + 9)x + (3s^2 + 9s + 1)
    bA = -(6 * shift + 9)
    cA = 3 * shift * shift + 9 * shift + 1
    rhs_k = -(2 + shift)
    A_tex = _quad_tex(3, bA, cA)
    rhs_tex = _lin_tex(1, rhs_k)
    caudan = f"Số nghiệm của phương trình $\\sqrt{{{A_tex}}} = |{rhs_tex}|$ là"
    choices = _make_choices("$2$.", ["$0$.", "$1$.", "$3$."])
    r1 = Fraction(-1, 2) + shift
    r2 = Fraction(3 + shift)
    loigiai = (
        f"Vì hai vế đều không âm nên bình phương hai vế:\n"
        f"$${A_tex} = ({rhs_tex})^2 \\iff \\left[\\begin{{aligned}} x &= {_frac_tex(r1)} \\\\ x &= {_frac_tex(r2)}. \\end{{aligned}}\\right.$$\n"
        f"Thử lại cả hai giá trị đều thỏa mãn. Vậy phương trình có $2$ nghiệm."
    )
    return caudan, choices, loigiai



# ==============================================================================
# BỔ SUNG CHƯƠNG VI (BÀI 15–18): MC BỘ ĐỀ ÔN HK2 & PHẦN 2 ĐÚNG SAI
# ==============================================================================

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


def K10_C3_MC_HamSo_TapXacDinh_CanTamThuc_Va_KetHop():
    """TXĐ hàm số chứa căn tam thức bậc hai sqrt(-x^2+bx+c) hoặc phân thức + sqrt(r^2-x^2)."""
    variant = random.choice([1, 2])
    if variant == 1:
        r1 = random.choice([-4, -3, -2, -1])
        r2 = random.choice([2, 3, 4, 5, 6])
        b = r1 + r2
        c = -r1 * r2
        f_tex = _quad_tex(-1, b, c)
        caudan = f"Tập xác định của hàm số $f(x) = \\sqrt{{{f_tex}}}$ là"
        true_ans = f"$[{r1}; {r2}]$."
        cands = [
            f"$({r1}; {r2})$.",
            f"$(-\\infty; {r1}] \\cup [{r2}; +\\infty)$.",
            r"$\mathbb{R}$.",
            f"$[{-r2}; {-r1}]$.",
        ]
        loigiai = (
            f"Điều kiện xác định: ${f_tex} \\ge 0 \\iff {r1} \\le x \\le {r2}$.\n"
            f"Vậy tập xác định của hàm số là $\\mathcal{{D}} = [{r1}; {r2}]$."
        )
        return caudan, _make_choices(true_ans, cands), loigiai

    # Variant 2: k/(r - x) + sqrt(r^2 - x^2) hoặc k/(x + r) + sqrt(r^2 - x^2)
    r = random.choice([2, 3, 4])
    k = random.choice([1, 2, 3, 5])
    excl_right = random.choice([True, False])
    if excl_right:
        den_tex = f"{r} - x"
        true_ans = f"$[-{r}; {r})$."
        excl_val = r
        opp_ans = f"$(-{r}; {r}]$."
    else:
        den_tex = f"x + {r}"
        true_ans = f"$(-{r}; {r}]$."
        excl_val = -r
        opp_ans = f"$[-{r}; {r})$."
    rad_tex = f"{r * r} - x^2"
    caudan = f"Hàm số $y = \\dfrac{{{k}}}{{{den_tex}}} + \\sqrt{{{rad_tex}}}$ có tập xác định là"
    cands = [
        opp_ans,
        f"$(-{r}; {r})$.",
        f"$[-{r}; {r}]$."
    ]
    loigiai = (
        f"Điều kiện xác định:\n"
        f"$$\\begin{{cases}} {den_tex} \\ne 0 \\\\ {rad_tex} \\ge 0 \\end{{cases}} "
        f"\\iff \\begin{{cases}} x \\ne {excl_val} \\\\ -{r} \\le x \\le {r}. \\end{{cases}}$$\n"
        f"Vậy tập xác định là {true_ans}"
    )
    return caudan, _make_choices(true_ans, cands), loigiai


def K10_C3_MC_HamSo_NhanDien_TapXacDinh_R():
    """Trang 36 Câu 7: Nhận diện hàm số có tập xác định là R."""
    a = random.choice([2, 3, 4, 5])
    b = random.choice([-3, -2, 1, 2, 3])
    c = random.choice([-4, -1, 1, 3])
    r1 = random.choice([1, 2, -1, -2])
    if random.choice([True, False]):
        true_tex = f"y = x^3 {_signed_frac_term(a, 'x^2')} {_signed_frac_term(c)}"
        reason = "là hàm đa thức"
    else:
        true_tex = f"y = \\dfrac{{{_lin_tex(1, b)}}}{{x^2 + {abs(b) + 1}}}"
        reason = f"có mẫu $x^2 + {abs(b) + 1} > 0, \\forall x \\in \\mathbb{{R}}$"

    w1 = f"y = \\dfrac{{{_lin_tex(1, 2)}}}{{{_lin_tex(1, -r1)}}}"
    w2 = f"y = \\dfrac{{{_quad_tex(1, 0, abs(c))}}}{{x}}"
    w3 = f"y = \\dfrac{{{_lin_tex(2, abs(b))}}}{{x^2}}"
    caudan = "Trong các hàm số sau, hàm số nào có tập xác định là $\\mathbb{R}$?"
    true_ans = f"${true_tex}$."
    cands = [f"${w1}$.", f"${w2}$.", f"${w3}$."]
    loigiai = (
        f"Hàm số ${true_tex}$ {reason} nên xác định với mọi $x \\in \\mathbb{{R}}$.\n"
        f"Các hàm phân thức còn lại đều có giá trị làm mẫu bằng $0$."
    )
    return caudan, _make_choices(true_ans, cands), loigiai


def K10_C3_MC_HamSo_NhanDien_HamBacHai():
    """Bộ đề Câu 10: Nhận diện hàm số bậc hai / không phải hàm số bậc hai."""
    a1 = random.choice([-2, -1, 1, 2, 3])
    b1 = random.choice([-4, 2, 3, 4, 6])
    c1 = random.choice([-3, 1, 2, 5])
    k = random.choice([2, 3, 4])
    m = random.choice([-5, -3, 2, 4])
    n = random.choice([-8, -5, 3, 7])

    quad_1 = f"y = {_quad_tex(a1, b1, c1)}"
    quad_2 = f"y = {-k}x({_lin_tex(k + 3, n)})"
    quad_3 = f"y = {_quad_tex(1, b1 + 2, 0)}"
    not_quad_opts = [
        f"y = x({_quad_tex(2, abs(m), -1)})",
        f"y = {_lin_tex(k, c1)}",
        f"y = \\dfrac{{{k}}}{{x^2}} {_signed_frac_term(c1)}",
    ]
    bad_expr = random.choice(not_quad_opts)

    if random.choice([True, False]):
        caudan = "Trong các hàm số sau, hàm số nào \\textbf{không} là hàm số bậc hai?"
        true_ans = f"${bad_expr}$."
        cands = [f"${quad_1}$.", f"${quad_2}$.", f"${quad_3}$."]
        loigiai = (
            f"Hàm số bậc hai có dạng $y = ax^2 + bx + c$ ($a \\ne 0$).\n"
            f"Biểu thức ${bad_expr}$ không có dạng này nên không phải hàm số bậc hai."
        )
    else:
        bads = [f"${e}$." for e in not_quad_opts]
        caudan = "Trong các hàm số sau, hàm số nào là hàm số bậc hai?"
        true_ans = f"${quad_2}$."
        cands = bads
        loigiai = (
            f"Khai triển ${quad_2}$ được dạng $y = ax^2 + bx$ với $a = {-k * (k + 3)} \\ne 0$, "
            f"nên đây là hàm số bậc hai."
        )
    return caudan, _make_choices(true_ans, cands), loigiai


def K10_C3_MC_HamSo_GiaoDiem_HaiDuongThang():
    """Bộ đề Câu 4: Tìm tọa độ giao điểm của hai đường thẳng."""
    x0 = random.choice([-3, -2, -1, 1, 2, 3, 4])
    y0 = random.choice([-3, -2, -1, 1, 2, 3])
    b1 = random.choice([2, 3, 4])
    a1 = random.choice([-3, -2, 2, 3])
    # d1: y = (c1 - a1*x) / b1 => c1 = b1*y0 + a1*x0
    c1 = b1 * y0 + a1 * x0
    b2 = random.choice([2, 3, 4])
    while Fraction(-a1, b1) == Fraction(-1, b2):
        b2 = random.choice([2, 3, 4, 5])
    # d2: y = -x/b2 + c2 => c2 = y0 + x0/b2
    # Để c2 nguyên, chọn x0 chia hết cho b2 hoặc đặt d2 dạng tổng quát hơn: y = -(x + k)/b2
    # y0 = -(x0 + k)/b2 => k = -b2*y0 - x0
    k = -b2 * y0 - x0
    d1_num = f"{c1} {_signed_frac_term(-a1, 'x')}" if c1 != 0 else _lin_tex(-a1, 0)
    d1_tex = f"y = \\dfrac{{{d1_num}}}{{{b1}}}"
    if k % b2 == 0:
        c2_int = k // b2
        inner = f"\\dfrac{{x}}{{{b2}}} {_signed_frac_term(c2_int)}"
        d2_tex = f"y = -\\left({inner}\\right)" if c2_int != 0 else f"y = -\\dfrac{{x}}{{{b2}}}"
    else:
        d2_tex = f"y = \\dfrac{{{_lin_tex(-1, -k)}}}{{{b2}}}"

    caudan = f"Tọa độ giao điểm của hai đường thẳng ${d1_tex}$ và ${d2_tex}$ là"
    true_ans = f"$({x0}; {y0})$."
    cands = [
        f"$({y0}; {x0})$.",
        f"$(0; {y0 - 1})$.",
        f"$({x0 - 1}; {y0 + 1})$.",
        f"$({-x0}; {-y0})$.",
    ]
    loigiai = (
        f"Hoành độ giao điểm thỏa mãn phương trình:\n"
        f"$$\\dfrac{{{d1_num}}}{{{b1}}} = {d2_tex.split('= ')[1]} \\iff x = {x0}.$$\n"
        f"Thay $x = {x0}$ vào đường thẳng thứ nhất được $y = {y0}$. Vậy giao điểm là $({x0}; {y0})$."
    )
    return caudan, _make_choices(true_ans, cands), loigiai


def K10_C3_MC_Parabol_GiaoDiem_DuongThang():
    """Bộ đề Câu 6: Tọa độ giao điểm của parabol (P) và đường thẳng d."""
    x1 = random.choice([-2, -1, 0, 1])
    x2 = x1 + random.choice([1, 2, 3])
    # (P): y = a*x^2 + b*x + c_p; d: y = m*x + n
    # (P) - d = a*(x - x1)*(x - x2) = a*x^2 - a*(x1+x2)*x + a*x1*x2
    a = random.choice([1, -1])
    m = random.choice([-2, -1, 1, 2])
    n = random.choice([-3, -2, -1, 1, 2, 3])
    b = m - a * (x1 + x2)
    c_p = n + a * x1 * x2

    y1 = m * x1 + n
    y2 = m * x2 + n
    p_tex = _quad_tex(a, b, c_p)
    d_tex = _lin_tex(m, n)

    caudan = f"Tọa độ giao điểm của $(P): y = {p_tex}$ với đường thẳng $d: y = {d_tex}$ là"
    true_ans = f"$M({x1}; {y1}),\\ N({x2}; {y2})$."
    cands = [
        f"$M({x1}; {y2}),\\ N({x2}; {y1})$.",
        f"$M({-x1}; {y1 + 1}),\\ N({-x2}; {y2 + 1})$.",
        f"$M(0; {n}),\\ N({x2}; {y2})$." if x1 != 0 else f"$M({x1 + 1}; {y1 - 1}),\\ N({x2}; {y2})$.",
        f"$M({x1}; {-y1}),\\ N({x2}; {-y2})$.",
    ]
    diff_tex = _quad_tex(a, -(a * (x1 + x2)), a * x1 * x2)
    loigiai = (
        f"Phương trình hoành độ giao điểm của $(P)$ và $d$:\n"
        f"$${p_tex} = {d_tex} \\iff {diff_tex} = 0 \\iff \\left[\\begin{{aligned}} x &= {x1} \\implies y = {y1} \\\\ x &= {x2} \\implies y = {y2}. \\end{{aligned}}\\right.$$\n"
        f"Vậy giao điểm là $M({x1}; {y1}),\\ N({x2}; {y2})$."
    )
    return caudan, _make_choices(true_ans, cands), loigiai


def K10_C7_MC_BPT_NhanDien_BacHaiMotAn():
    """Bộ đề Câu 11: Nhận diện bất phương trình bậc hai một ẩn."""
    a = random.choice([2, 3, 4, 5])
    k = random.choice([2, 3, 5, 7])
    c = random.choice([-5, -3, -1, 1, 3, 4])
    ineq = random.choice(["\\le", "\\ge", "<", ">"])
    true_expr = f"{a}x^2 + x\\sqrt{{{k}}} {_signed_frac_term(c)} {ineq} 0"

    w1 = f"x^3 {_signed_frac_term(-a, 'x')} + {abs(c) + 1} > 0"
    w2 = f"{a}x^2 - {abs(c) + 2}\\sqrt{{x}} + 2 < 0"
    w3 = f"{a + 1}x^2 + \\dfrac{{1}}{{x}} + 2 > 0"
    caudan = "Bất phương trình nào sau đây là bất phương trình bậc hai một ẩn?"
    true_ans = f"${true_expr}$."
    cands = [f"${w1}$.", f"${w2}$.", f"${w3}$."]
    loigiai = (
        f"Bất phương trình bậc hai một ẩn có dạng $ax^2 + bx + c {ineq} 0$ (với $a, b, c \\in \\mathbb{{R}}, a \\ne 0$).\n"
        f"Trong đó ${true_expr}$ có dạng chuẩn với $a = {a},\\ b = \\sqrt{{{k}}},\\ c = {c}$."
    )
    return caudan, _make_choices(true_ans, cands), loigiai


def K10_C7_MC_BPT_Giai_CoBan():
    """Giải bất phương trình bậc hai một ẩn (2 nghiệm phân biệt, nghiệm kép, vô nghiệm)."""
    case = random.choice([1, 2, 3])
    if case == 1:
        r1 = random.choice([-4, -3, -2, -1, 0])
        r2 = random.choice([1, 2, 3, 4, 5, 7])
        while r1 >= r2:
            r2 = r1 + random.choice([2, 3, 4])
        a = random.choice([1, -1])
        b = -a * (r1 + r2)
        c = a * r1 * r2
        ineq = random.choice(["<", "\\le", ">", "\\ge"])
        f_tex = _quad_tex(a, b, c)
        want_inside = (a > 0 and ineq in ("<", "\\le")) or (a < 0 and ineq in (">", "\\ge"))
        closed = ineq in ("\\le", "\\ge")
        lb, rb = ("[", "]") if closed else ("(", ")")
        lb_out, rb_out = ("]", "[") if closed else (")", "(")
        # Khoảng trong/ngoài đúng và các nhiễu kinh điển
        in_str = f"${lb}{r1}; {r2}{rb}$."
        in_wrong_b = f"${lb_out}{r1}; {r2}{rb_out}$." if not closed else f"$({r1}; {r2})$."
        if closed:
            in_wrong_b = f"$({r1}; {r2})$."
        else:
            in_wrong_b = f"$[{r1}; {r2}]$."
        out_str = f"$(-\\infty; {r1}{rb} \\cup {lb}{r2}; +\\infty)$."
        out_wrong_b = f"$(-\\infty; {r1}) \\cup ({r2}; +\\infty)$." if closed else f"$(-\\infty; {r1}] \\cup [{r2}; +\\infty)$."
        swap_str = f"$[{-r2}; {-r1}]$." if closed else f"$({-r2}; {-r1})$."

        if want_inside:
            true_ans = in_str
            cands = [out_str, out_wrong_b, in_wrong_b, swap_str]
        else:
            true_ans = out_str
            cands = [in_str, in_wrong_b, out_wrong_b, swap_str]

        caudan = f"Tập nghiệm $S$ của bất phương trình ${f_tex} {ineq} 0$ là"
        loigiai = (
            f"Tam thức $f(x) = {f_tex}$ có hai nghiệm $x = {r1}$ và $x = {r2}$, hệ số $a = {a}$.\n"
            f"Xét dấu tam thức ta được tập nghiệm $S = {true_ans[:-1]}$."
        )
        return caudan, _make_choices(true_ans, cands), loigiai

    if case == 2:
        # Nghiệm kép: (x - r)^2 > 0 => R\{r}, <= 0 => {r}, < 0 => emptyset
        r = random.choice([-4, -3, -2, 1, 2, 3, 4])
        f_tex = _quad_tex(1, -2 * r, r * r)
        sub = random.choice([">", "<", "\\le"])
        caudan = f"Tập nghiệm của bất phương trình ${f_tex} {sub} 0$ là"
        if sub == ">":
            true_ans = f"$\\mathbb{{R}} \\setminus \\{{{r}\\}}$."
            cands = [
                r"$\mathbb{R}$.",
                f"$({r}; +\\infty)$.",
                f"$\\mathbb{{R}} \\setminus \\{{{-r}\\}}$."
            ]
        elif sub == "<":
            true_ans = r"$\emptyset$."
            cands = [f"$\\{{{r}\\}}$.", f"$\\mathbb{{R}} \\setminus \\{{{r}\\}}$.", r"$\mathbb{R}$."]
        else:
            true_ans = f"$\\{{{r}\\}}$."
            cands = [r"$\emptyset$.", f"$\\mathbb{{R}} \\setminus \\{{{r}\\}}$.", f"$(-\\infty; {r}]$."]
        loigiai = (
            f"Ta có ${f_tex} = {_signed_factor(r)}^2 \\ge 0, \\forall x \\in \\mathbb{{R}}$.\n"
            f"Suy ra tập nghiệm của bất phương trình ${f_tex} {sub} 0$ là {true_ans}"
        )
        return caudan, _make_choices(true_ans, cands), loigiai

    # Case 3: Tam thức vô nghiệm
    a = random.choice([1, 2, -1, -2])
    c_off = random.choice([1, 2, 3])
    b_val = random.choice([-2, 2, 4])
    # a*(x + k)^2 + sign(a)*c_off
    k = random.choice([-1, 1, 2])
    b = 2 * a * k
    c = a * k * k + (c_off if a > 0 else -c_off)
    f_tex = _quad_tex(a, b, c)
    ineq = random.choice([">", "<"])
    caudan = f"Tập nghiệm của bất phương trình ${f_tex} {ineq} 0$ là"
    if (a > 0 and ineq == ">") or (a < 0 and ineq == "<"):
        true_ans = r"$\mathbb{R}$."
        cands = [r"$\emptyset$.", f"$({-k}; +\\infty)$.", f"$\\mathbb{{R}} \\setminus \\{{{-k}\\}}$."]
    else:
        true_ans = r"$\emptyset$."
        cands = [r"$\mathbb{R}$.", f"$\\{{{-k}\\}}$.", f"$(-\\infty; {-k})$."]
    loigiai = (
        f"Tam thức $f(x) = {f_tex}$ có $\\Delta' < 0$ và $a = {a}$, nên luôn "
        f"{'dương' if a > 0 else 'âm'} với mọi $x \\in \\mathbb{{R}}$.\nVậy tập nghiệm là {true_ans}"
    )
    return caudan, _make_choices(true_ans, cands), loigiai


def K10_C7_MC_BPT_KiemTraNghiem_Va_PhatBieu():
    """Trang 40 Câu 4 & Bộ đề Câu 10: Chọn giá trị nghiệm của BPT hoặc tìm phát biểu sai."""
    if random.choice([True, False]):
        # Biến thể 1: Số nào là một nghiệm của BPT bậc hai hệ số hữu tỉ (r1 < x < r2)
        configs = [
            # (b_frac, c_int, r1_frac, r2_frac, x_ok, x_bad_list)
            (Fraction(3, 2), -1, Fraction(-2, 1), Fraction(1, 2), Fraction(1, 3), [Fraction(-2, 1), Fraction(1, 2), Fraction(1, 1)]),
            (Fraction(1, 2), -3, Fraction(-2, 1), Fraction(3, 2), Fraction(1, 1), [Fraction(-3, 1), Fraction(2, 1), Fraction(3, 2)]),
            (Fraction(-5, 2), 1, Fraction(1, 2), Fraction(2, 1), Fraction(1, 1), [Fraction(0, 1), Fraction(2, 1), Fraction(-1, 1)]),
            (Fraction(-1, 2), -5, Fraction(-2, 1), Fraction(5, 2), Fraction(2, 1), [Fraction(-2, 1), Fraction(3, 1), Fraction(-3, 1)]),
        ]
        bf, ci, r1, r2, x_ok, x_bads = random.choice(configs)
        f_tex = _quad_tex(1, bf, ci)
        caudan = f"Cho bất phương trình ${f_tex} < 0$. Số nào sau đây là một nghiệm của bất phương trình trên?"
        true_ans = f"$x = {_frac_tex(x_ok)}$."
        cands = [f"$x = {_frac_tex(xb)}$." for xb in x_bads]
        loigiai = (
            f"Giải phương trình ${f_tex} = 0$ được hai nghiệm $x = {_frac_tex(r1)}$ và $x = {_frac_tex(r2)}$.\n"
            f"Tập nghiệm của bất phương trình là $\\left({_frac_tex(r1)}; {_frac_tex(r2)}\\right)$.\n"
            f"Trong các giá trị đã cho, chỉ có $x = {_frac_tex(x_ok)}$ thuộc khoảng nghiệm."
        )
        return caudan, _make_choices(true_ans, cands), loigiai

    # Biến thể 2: Phát biểu nào SAI về tập nghiệm của tam thức bậc hai (bẫy ngoặc tròn '(' ở >= 0 hoặc <= 0)
    r1 = random.choice([-3, -2, -1])
    r2 = random.choice([1, 2, 3, 4])
    f_tex = _quad_tex(1, -(r1 + r2), r1 * r2)
    stmt_gt = f"${f_tex} > 0$ khi và chỉ khi $x \\in (-\\infty; {r1}) \\cup ({r2}; +\\infty)$."
    stmt_lt = f"${f_tex} < 0$ khi và chỉ khi $x \\in ({r1}; {r2})$."
    stmt_le = f"${f_tex} \\le 0$ khi và chỉ khi $x \\in [{r1}; {r2}]$."
    stmt_ge_bad = f"${f_tex} \\ge 0$ khi và chỉ khi $x \\in (-\\infty; {r1}) \\cup ({r2}; +\\infty)$."

    caudan = "Trong các phát biểu sau, phát biểu nào \\textbf{sai}?"
    loigiai = (
        f"Tam thức $f(x) = {f_tex}$ có hai nghiệm $x = {r1}$ và $x = {r2}$.\n"
        f"Do đó ${f_tex} \\ge 0 \\iff x \\in (-\\infty; {r1}] \\cup [{r2}; +\\infty)$ (phải lấy cả dấu ngoặc vuông tại ${r1}$ và ${r2}$)."
    )
    return caudan, _make_choices(stmt_ge_bad, [stmt_gt, stmt_lt, stmt_le]), loigiai


def K10_C7_MC_BPT_DemNghiemNguyen():
    """Bộ đề Câu 8: Đếm số nghiệm nguyên / nguyên âm / nguyên dương của BPT bậc hai."""
    r1 = random.choice([-5, -4, -3, -2])
    r2 = random.choice([2, 3, 4, 5])
    strict = random.choice([True, False])
    ineq = "<" if strict else "\\le"
    f_tex = _quad_tex(1, -(r1 + r2), r1 * r2)

    low = r1 + 1 if strict else r1
    high = r2 - 1 if strict else r2
    all_ints = list(range(low, high + 1))

    ask_type = random.choice(["neg", "pos", "all"])
    if ask_type == "neg":
        sol_ints = [x for x in all_ints if x < 0]
        label = "nguyên âm"
    elif ask_type == "pos":
        sol_ints = [x for x in all_ints if x > 0]
        label = "nguyên dương"
    else:
        sol_ints = all_ints
        label = "nguyên"

    cnt = len(sol_ints)
    caudan = f"Tập nghiệm của bất phương trình ${f_tex} {ineq} 0$ có số nghiệm {label} là"
    true_ans = f"${cnt}$."
    cand_nums = [n for n in [cnt - 2, cnt - 1, cnt + 1, cnt + 2, 0, cnt + 3] if n >= 0 and n != cnt]
    cands = [f"${n}$." for n in cand_nums]
    interval_tex = f"({r1}; {r2})" if strict else f"[{r1}; {r2}]"
    list_str = ", ".join(str(v) for v in sol_ints) if sol_ints else "\\text{không có}"
    loigiai = (
        f"Tập nghiệm của bất phương trình là $S = {interval_tex}$.\n"
        f"Các nghiệm {label} trong $S$ là: ${list_str}$. Vậy có ${cnt}$ nghiệm {label}."
    )
    return caudan, _make_choices(true_ans, cands), loigiai


def K10_C7_MC_TamThuc_ChonBangXetDau_TikZ():
    """Ảnh Câu 12 (Trang 36/162): Cho tam thức f(x), chọn bảng xét dấu đúng trong 4 bảng TikZ."""
    x1 = random.choice([-3, -2, -1])
    x2 = random.choice([1, 2, 3, 4])
    while x1 == -x2:
        x2 += 1
    a = random.choice([-1, 1, -2, 2])
    b = -a * (x1 + x2)
    c = a * x1 * x2

    def _tab_tikz(r_left, r_right, same_as_a_positive):
        line = "\\tkzTabLine{ , +, 0, -, 0, +, }" if same_as_a_positive else "\\tkzTabLine{ , -, 0, +, 0, -, }"
        return (
            "\\begin{tikzpicture}[scale=0.72]\n"
            f"\\tkzTabInit[nocadre=false,lgt=1.3,espcl=1.4]{{$x$ / 0.7, $f(x)$ / 0.7}}{{$ -\\infty$, ${r_left}$, ${r_right}$, $+\\infty$}}\n"
            f"{line}\n"
            "\\end{tikzpicture}"
        )

    is_pos = a > 0
    true_ans = _tab_tikz(x1, x2, is_pos)
    cands = [
        _tab_tikz(x1, x2, not is_pos),
        _tab_tikz(-x2, -x1, is_pos),
        _tab_tikz(-x2, -x1, not is_pos),
    ]
    f_tex = _quad_tex(a, b, c)
    caudan = f"Bảng xét dấu nào sau đây là của tam thức bậc hai $f(x) = {f_tex}$?"
    in_out = "trong khoảng hai nghiệm trái dấu $a$, ngoài khoảng hai nghiệm cùng dấu $a$"
    loigiai = (
        f"Tam thức $f(x) = {f_tex}$ có hai nghiệm $x_1 = {x1},\\ x_2 = {x2}$ và hệ số $a = {a}$ "
        f"({'$> 0$' if a > 0 else '$< 0$'}).\n"
        f"Áp dụng quy tắc {in_out}, chọn bảng có hai nghiệm ${x1}; {x2}$ và dấu ngoài khoảng là "
        f"{'$+$' if a > 0 else '$-$'}."
    )
    return caudan, _make_choices(true_ans, cands), loigiai


def K10_C7_MC_BPT_DocDoThiParabol():
    """Ảnh Câu 11: Cho đồ thị parabol y = ax^2 + bx + c, giải bất phương trình tương ứng."""
    r1 = random.choice([-3, -2, -1])
    r2 = random.choice([2, 3, 4])
    # Chọn a sao cho f(x) = a(x - r1)(x - r2) gọn, có thể a = 1 hoặc a = -1 hoặc a = 0.5/1
    a = random.choice([1, -1])
    b = -a * (r1 + r2)
    c = a * r1 * r2
    xI = (r1 + r2) / 2.0
    yI = a * (xI - r1) * (xI - r2)

    xmin = min(r1 - 1.2, -1.0)
    xmax = max(r2 + 1.2, 1.5)
    ymin = min(-1.2, yI - 1.0, c - 0.8)
    ymax = max(2.2, yI + 1.0, c + 1.0)
    dom_l = r1 - 0.8
    dom_r = r2 + 0.8

    tikz = (
        "\\begin{tikzpicture}[scale=0.62, line join=round, line cap=round, >=stealth]\n"
        f"    \\draw[->] ({xmin:.1f},0) -- ({xmax:.1f},0) node[below] {{$x$}};\n"
        f"    \\draw[->] (0,{ymin:.1f}) -- (0,{ymax:.1f}) node[left] {{$y$}};\n"
        "    \\node[below left] at (0,0) {$O$};\n"
        f"    \\draw[thick, blue, domain={dom_l}:{dom_r}, samples=100] plot (\\x, {{{a}*(\\x)*(\\x) + ({b})*(\\x) + ({c})}});\n"
        f"    \\node[below left] at ({r1},0) {{${r1}$}};\n"
        f"    \\node[below right] at ({r2},0) {{${r2}$}};\n"
        f"    \\node[{'below left' if c < 0 else 'above left'}] at (0,{c}) {{${c}$}};\n"
        f"    \\fill ({r1},0) circle (1.5pt) ({r2},0) circle (1.5pt) (0,{c}) circle (1.5pt);\n"
        "\\end{tikzpicture}"
    )

    ineq = random.choice(["\\le", "<", "\\ge", ">"])
    f_tex = _quad_tex(a, b, c)
    want_inside = (a > 0 and ineq in ("\\le", "<")) or (a < 0 and ineq in ("\\ge", ">"))
    closed = ineq in ("\\le", "\\ge")
    lb, rb = ("[", "]") if closed else ("(", ")")
    lb_o, rb_o = ("(", ")") if closed else ("[", "]")

    in_str = f"$x \\in {lb}{r1}; {r2}{rb}$."
    in_opp = f"$x \\in {lb_o}{r1}; {r2}{rb_o}$."
    out_str = f"$x \\in (-\\infty; {r1}{rb} \\cup {lb}{r2}; +\\infty)$."
    out_opp = f"$x \\in (-\\infty; {r1}{rb_o} \\cup {lb_o}{r2}; +\\infty)$."

    if want_inside:
        true_ans = in_str
        cands = [out_str, out_opp, in_opp]
        region_desc = "nằm phía dưới (hoặc trên)" if ineq in ("\\le", "<") else "nằm phía trên (hoặc trên)"
    else:
        true_ans = out_str
        cands = [in_str, in_opp, out_opp]
        region_desc = "nằm phía trên (hoặc trên)" if ineq in ("\\ge", ">") else "nằm phía dưới (hoặc trên)"

    caudan = (
        f"\\immini{{Cho hàm số $y = {f_tex}$ có đồ thị như hình vẽ. "
        f"Giải bất phương trình ${f_tex} {ineq} 0$.}}{{\n{tikz}\n}}"
    )
    loigiai = (
        f"Dựa vào đồ thị cắt trục hoành tại $x = {r1}$ và $x = {r2}$:\n"
        f"Phần đồ thị {region_desc} trục hoành ứng với {true_ans}"
    )
    return caudan, _make_choices(true_ans, cands), loigiai


def K10_C7_MC_TamThuc_ThamSoM_CungDauTrenR():
    """Bộ đề Câu 12: Tìm tham số m để x^2 - 2kx + m >= 0 (hoặc > 0, <= 0, < 0) với mọi x thuộc R."""
    a = random.choice([1, -1])
    k = random.choice([-3, -2, -1, 1, 2, 3])
    b = 2 * a * k
    m_bound = a * k * k
    if a > 0:
        ineq = random.choice(["\\ge", ">"])
        sym_true = "\\ge" if ineq == "\\ge" else ">"
        sym_wrong1 = ">" if ineq == "\\ge" else "\\ge"
        sym_wrong2 = "<"
    else:
        ineq = random.choice(["\\le", "<"])
        sym_true = "\\le" if ineq == "\\le" else "<"
        sym_wrong1 = "<" if ineq == "\\le" else "\\le"
        sym_wrong2 = ">"

    f_tex = f"{'x^2' if a == 1 else '-x^2'} {_signed_frac_term(b, 'x')} + m"
    caudan = (
        f"Cho hàm số $f(x) = {f_tex}$. Với giá trị nào của tham số $m$ thì "
        f"$f(x) {ineq} 0,\\ \\forall x \\in \\mathbb{{R}}$?"
    )
    true_ans = f"$m {sym_true} {m_bound}$."
    cands = [
        f"$m {sym_wrong1} {m_bound}$.",
        f"$m {sym_wrong2} {m_bound + 1}$.",
        f"$m {sym_true} {m_bound + 1}$.",
        f"$m {sym_wrong2} 0$.",
    ]
    loigiai = (
        f"Ta có $\\Delta' = {(-a * k)}^2 - ({a})m = {k * k} {'-' if a > 0 else '+'} m$.\n"
        f"Để $f(x) {ineq} 0, \\forall x \\in \\mathbb{{R}}$ thì $\\Delta' {'\\le' if ineq in ('\\ge', '\\le') else '<'} 0 "
        f"\\iff m {sym_true} {m_bound}$."
    )
    return caudan, _make_choices(true_ans, cands), loigiai


def K10_C7_MC_PT_CanF_Bang_CanG_BieuThucNghiem():
    """Bộ đề Câu 8: Phương trình sqrt(f(x)) = sqrt(g(x)) có 2 nghiệm x1, x2, tính S = x1*x2 + k(x1+x2)."""
    # Chọn hai nghiệm hữu tỉ phân biệt x1 < x2 sao cho f(x) và g(x) nhận giá trị dương tại x1, x2
    root_pairs = [
        (Fraction(-11, 7), Fraction(1, 5)),
        (Fraction(-5, 3), Fraction(1, 2)),
        (Fraction(-3, 2), Fraction(1, 3)),
        (Fraction(-4, 3), Fraction(2, 5)),
        (Fraction(-2, 3), Fraction(3, 4)),
    ]
    r1, r2 = random.choice(root_pairs)
    # H(x) = (q1*x - p1)(q2*x - p2) = A*x^2 + B*x + C
    A = r1.denominator * r2.denominator
    B = -(r1.numerator * r2.denominator + r2.numerator * r1.denominator)
    C = r1.numerator * r2.numerator

    # P(x) = c0*(x^2 + 1) + d0*x luôn dương nếu d0^2 < 4*c0^2
    c0 = random.choice([3, 4, 5])
    d0 = random.choice([-2, -1, 1, 2])
    # f(x) = P(x) + H(x) ? Hoặc chọn tỉ lệ sao cho f(x) dương tại r1, r2 và hệ số gọn:
    # Đặt g(x) = P(x) - k_g * H(x) và f(x) = P(x) + k_f * H(x) với k_f + k_g > 0
    # Tại x = r1, r2 thì H(x)=0 => f(x)=g(x)=P(x) > 0 chắc chắn!
    k_f = 1
    k_g = random.choice([1, 2])
    a1, b1, c1 = c0 + k_f * A, d0 + k_f * B, c0 + k_f * C
    a2, b2, c2 = c0 - k_g * A, d0 - k_g * B, c0 - k_g * C

    f_tex = _quad_tex(a1, b1, c1)
    g_tex = _quad_tex(a2, b2, c2)

    m_coef = random.choice([1, 2, -2, 3])
    S_val = r1 * r2 + m_coef * (r1 + r2)
    expr_tex = (
        "x_1 x_2 + (x_1 + x_2)" if m_coef == 1
        else f"x_1 x_2 {_signed_frac_term(m_coef)}(x_1 + x_2)"
    )

    caudan = (
        f"Biết phương trình $\\sqrt{{{f_tex}}} = \\sqrt{{{g_tex}}}$ có hai nghiệm $x_1;\\ x_2$. "
        f"Tính giá trị của biểu thức $S = {expr_tex}$."
    )
    true_ans = f"${_frac_tex(S_val)}$."
    cands = [
        f"${_frac_tex(-S_val)}$.",
        f"${_frac_tex(S_val + 1)}$.",
        f"${_frac_tex(r1 * r2 - m_coef * (r1 + r2))}$.",
        f"${_frac_tex(S_val + Fraction(2, A))}$.",
    ]
    diff_tex = _quad_tex((k_f + k_g) * A, (k_f + k_g) * B, (k_f + k_g) * C)
    loigiai = (
        f"Bình phương hai vế phương trình:\n"
        f"$${f_tex} = {g_tex} \\iff {diff_tex} = 0 \\iff \\left[\\begin{{aligned}} x &= {_frac_tex(r1)} \\\\ x &= {_frac_tex(r2)}. \\end{{aligned}}\\right.$$\n"
        f"Thử lại cả hai giá trị đều làm biểu thức dưới hai dấu căn dương nên đều là nghiệm.\n"
        f"Theo định lí Vi-ét: $x_1 + x_2 = {_frac_tex(r1 + r2)},\\ x_1 x_2 = {_frac_tex(r1 * r2)}$. "
        f"Suy ra $S = {_frac_tex(S_val)}$."
    )
    return caudan, _make_choices(true_ans, cands), loigiai


def K10_C7_MC_PT_CanF_Bang_G_BieuThucPhanSo_VoTi():
    """Trang 36 Câu 3 & Câu 7: Phương trình sqrt(f(x)) = g(x) nghiệm phân số a/b hoặc vô tỉ (a+sqrt(b))/c."""
    if random.choice([True, False]):
        # Biến thể 1: sqrt(x^2 + b1*x + c1) = x + d  => (b1 - 2d)x = d^2 - c1 => x = a/b > -d
        while True:
            d = random.choice([1, 2, 3])
            p = random.choice([2, 3, 5, 7])
            # Chọn b1 - 2d = p (hay -p) và d^2 - c1 = q sao cho x + d > 0
            denom = random.choice([-4, -5, -6, 4, 5, 6])
            b1 = 2 * d + denom
            c1 = random.choice([2, 3, 5, 6, 7])
            num = d * d - c1
            if num == 0:
                continue
            sol = Fraction(num, denom)
            if sol + d >= 0 and math.gcd(abs(sol.numerator), sol.denominator) == 1 and sol.denominator > 1:
                break
        a_res = sol.numerator
        b_res = sol.denominator
        S_val = a_res + b_res
        f_tex = _quad_tex(1, b1, c1)
        g_tex = _lin_tex(1, d)
        caudan = (
            f"Giải phương trình $\\sqrt{{{f_tex}}} = {g_tex}$ ta được nghiệm $x = \\dfrac{{a}}{{b}}$ "
            f"với $a \\in \\mathbb{{Z}},\\ b \\in \\mathbb{{N}}^*$ và $\\dfrac{{a}}{{b}}$ là phân số tối giản. Tính $a + b$."
        )
        true_ans = f"${S_val}$."
        cands = [f"${v}$." for v in [S_val - 2, S_val + 2, abs(a_res) + b_res + 1, -S_val] if v != S_val]
        loigiai = (
            f"Điều kiện ${g_tex} \\ge 0 \\iff x \\ge {-d}$.\n"
            f"Bình phương hai vế: ${f_tex} = ({g_tex})^2 \\iff {denom}x = {num} \\iff x = {_frac_tex(sol)}$ (thỏa mãn).\n"
            f"Suy ra $a = {a_res},\\ b = {b_res} \\implies a + b = {S_val}$."
        )
        return caudan, _make_choices(true_ans, cands), loigiai

    # Biến thể 2: Nghiệm vô tỉ (a + sqrt(b))/c với a, b, c nguyên dương và a/c, b/c tối giản
    def _is_square_free(n):
        if n <= 1:
            return False
        k = 2
        while k * k <= n:
            if n % (k * k) == 0:
                return False
            k += 1
        return True

    while True:
        d = random.choice([2, 3])
        k_lead = d * d - random.choice([1, 2, 3])
        A_sq = d * d - k_lead  # > 0
        b_rad = random.choice([1, 3, 5, 7])
        c_rad = random.choice([1, 2, 3, 5])
        # (d^2 - k_lead)x^2 - b_rad*x - c_rad = 0 => x = (b_rad + sqrt(b_rad^2 + 4*A_sq*c_rad)) / (2*A_sq)
        delta = b_rad * b_rad + 4 * A_sq * c_rad
        denom = 2 * A_sq
        if _is_square_free(delta) and math.gcd(b_rad, denom) == 1 and math.gcd(delta, denom) == 1:
            break

    a_res, b_res, c_res = b_rad, delta, denom
    S_val = a_res * c_res - b_res
    f_tex = _quad_tex(k_lead, b_rad, c_rad)
    g_tex = f"{d}x"
    caudan = (
        f"Biết phương trình $\\sqrt{{{f_tex}}} = {g_tex}$ có một nghiệm $x = \\dfrac{{a + \\sqrt{{b}}}}{{c}}$, "
        f"với $a, b, c \\in \\mathbb{{N}}^*$ và $\\dfrac{{a}}{{c}}, \\dfrac{{b}}{{c}}$ là các phân số tối giản. "
        f"Tính $S = ac - b$."
    )
    true_ans = f"${S_val}$."
    cands = [f"${v}$." for v in [-S_val, a_res + c_res + b_res, S_val + 4, a_res * c_res + b_res] if v != S_val]
    loigiai = (
        f"Điều kiện $x \\ge 0$. Bình phương hai vế phương trình:\n"
        f"$${f_tex} = {d * d}x^2 \\iff {_quad_tex(A_sq, -b_rad, -c_rad)} = 0.$$\n"
        f"Giải phương trình bậc hai với $\\Delta = {delta}$, lấy nghiệm dương: "
        f"$x = \\dfrac{{{a_res} + \\sqrt{{{b_res}}}}}{{{c_res}}}$.\n"
        f"Vậy $a = {a_res},\\ b = {b_res},\\ c = {c_res} \\implies S = ac - b = {S_val}$."
    )
    return caudan, _make_choices(true_ans, cands), loigiai


# ==============================================================================
# PHẦN 2: CÂU TRẮC NGHIỆM ĐÚNG SAI - CHƯƠNG VI LỚP 10
# ==============================================================================

def K10_C6_TF_DoThi_Parabol_QuaGocToaDo():
    """Trang 18 Câu 1 (Đúng/Sai): Đồ thị parabol qua O(0;0) và (r;0), đọc nghiệm, f(0), đơn điệu, GTLN/GTNN."""
    downward = random.choice([True, False])
    r = random.choice([1, 2])
    a = -2 if downward else 2
    # f(x) = a*x*(x - r)
    y_mark = random.choice([1, 2])
    x_mark2 = 2 * r
    xmin = -1.2
    xmax = x_mark2 + 0.8
    y_v = a * (r / 2.0) * (r / 2.0 - r)
    ymin = -2.2 if downward else -0.8
    ymax = max(y_mark + 0.8, 1.5) if downward else 2.6

    tikz = (
        "\\begin{tikzpicture}[scale=0.68, line join=round, line cap=round, >=stealth]\n"
        f"    \\draw[->] ({xmin:.1f},0) -- ({xmax:.1f},0) node[below] {{$x$}};\n"
        f"    \\draw[->] (0,{ymin:.1f}) -- (0,{ymax:.1f}) node[left] {{$y$}};\n"
        "    \\node[above left] at (0,0) {$O$};\n"
        f"    \\draw[thick, blue, domain=-0.65:{r + 0.65:.2f}, samples=100] plot (\\x, {{{a}*\\x*(\\x - {r})}});\n"
        f"    \\node[left] at (0,{y_mark}) {{${y_mark}$}};\n"
        f"    \\node[below] at ({r},0) {{${r}$}};\n"
        f"    \\node[below] at ({x_mark2},0) {{${x_mark2}$}};\n"
        f"    \\fill (0,0) circle (1.6pt) ({r},0) circle (1.6pt) (0,{y_mark}) circle (1.4pt) ({x_mark2},0) circle (1.4pt);\n"
        "\\end{tikzpicture}"
    )

    caudan = (
        f"\\immini{{Cho hàm số bậc hai $y = f(x)$ có đồ thị như hình vẽ bên. "
        f"Mỗi kết quả dưới đây đúng hay sai?}}{{\n{tikz}\n}}"
    )
    items = [
        (
            f"$f(x) = 0 \\iff \\left[\\begin{{aligned}} x &= 0 \\\\ x &= {r}. \\end{{aligned}}\\right.$",
            f"$f(x) = 0 \\iff \\left[\\begin{{aligned}} x &= 0 \\\\ x &= {x_mark2}. \\end{{aligned}}\\right.$",
            f"Đồ thị cắt trục hoành tại đúng hai điểm $(0; 0)$ và $({r}; 0)$ nên $f(x) = 0 \\iff x = 0$ hoặc $x = {r}$.",
            f"Đồ thị cắt trục hoành tại $x = 0$ và $x = {r}$ (không đi qua $x = {x_mark2}$)."
        ),
        (
            "$f(0) = 0$.",
            f"$f(0) = {y_mark}$.",
            "Đồ thị đi qua gốc tọa độ $O(0; 0)$ nên $f(0) = 0$.",
            f"Tại $x = 0$, đồ thị đi qua $O(0; 0)$ nên $f(0) = 0 \\ne {y_mark}$."
        ),
        (
            f"Hàm số {'đồng biến' if downward else 'nghịch biến'} trên $(-\\infty; 0)$.",
            f"Hàm số {'nghịch biến' if downward else 'đồng biến'} trên $(-\\infty; 0)$.",
            f"Parabol có hoành độ đỉnh $x_I = {_frac_tex(Fraction(r, 2))} > 0$ và quay {'xuống dưới' if downward else 'lên trên'} nên {'đồng biến' if downward else 'nghịch biến'} trên $(-\\infty; 0)$.",
            f"Trên khoảng $(-\\infty; 0)$, đồ thị đi {'lên' if downward else 'xuống'} từ trái sang phải nên hàm số {'đồng biến' if downward else 'nghịch biến'}."
        ),
        (
            f"Hàm số {'không có giá trị nhỏ nhất' if downward else 'không có giá trị lớn nhất'} trên $\\mathbb{{R}}$.",
            f"${y_mark} \\le f(x), \\forall x \\in \\mathcal{{D}}$." if downward else f"$f(x) \\le -{y_mark}, \\forall x \\in \\mathcal{{D}}$.",
            "Đồ thị parabol kéo dài ra vô cực theo nhánh hướng xuống/lên tương ứng.",
            f"Đồ thị {'quay xuống vô hạn nên không có giá trị nhỏ nhất' if downward else 'quay lên vô hạn nên không bị chặn trên'}."
        ),
    ]
    choices, loigiai = _make_tf_choices(items)
    return caudan, choices, loigiai


def K10_C6_TF_KhaoSat_DoThi_Parabol_Dinh_GiaoDiem():
    """Bộ đề Câu 1 (Đúng/Sai): Đồ thị parabol đỉnh (x0; y0) và cắt Oy tại (0; c)."""
    a = random.choice([1, -1])
    x0 = random.choice([1, 2])
    # Chọn d = |y0 - c| = 1 => y0 = c - a*x0^2, hoặc đặt c cố định đẹp rồi suy ra y0
    # Đơn giản: y = a*(x - x0)^2 + y0, chọn y0 sao cho c = a*x0^2 + y0 khác 0 và gọn
    y0 = -2 if a > 0 else 2
    if x0 == 2 and a == 1:
        y0 = -3  # c = 4 - 3 = 1
    elif x0 == 2 and a == -1:
        y0 = 3   # c = -4 + 3 = -1
    b = -2 * a * x0
    c = a * x0 * x0 + y0

    ymin = min(y0 - 0.8, c - 0.8, -1.0)
    ymax = max(y0 + 1.0, c + 1.2, 2.2)
    dom_l = x0 - 1.9
    dom_r = x0 + 1.9

    tikz = (
        "\\begin{tikzpicture}[scale=0.65, line join=round, line cap=round, >=stealth]\n"
        f"    \\draw[->] (-1.2,0) -- ({2*x0 + 1.4:.1f},0) node[below] {{$x$}};\n"
        f"    \\draw[->] (0,{ymin:.1f}) -- (0,{ymax:.1f}) node[left] {{$y$}};\n"
        "    \\node[above left] at (0,0) {$O$};\n"
        f"    \\draw[thick, blue, domain={dom_l}:{dom_r}, samples=100] plot (\\x, {{{a}*(\\x - {x0})*(\\x - {x0}) + ({y0})}});\n"
        f"    \\draw[dashed] ({x0},0) -- ({x0},{y0}) -- (0,{y0});\n"
        f"    \\node[{'above' if y0 < 0 else 'below'}] at ({x0},0) {{${x0}$}};\n"
        f"    \\node[left] at (0,{y0}) {{${y0}$}};\n"
        f"    \\node[{'below left' if c < 0 else 'above left'}] at (0,{c}) {{${c}$}};\n"
        f"    \\fill ({x0},{y0}) circle (1.6pt) (0,{c}) circle (1.6pt);\n"
        "\\end{tikzpicture}"
    )

    f_tex = _quad_tex(a, b, c)
    wrong_f_tex = _quad_tex(a, -b, c)
    caudan = (
        f"\\immini{{Cho hàm số $y = f(x)$ có đồ thị là đường cong trong hình vẽ. "
        f"Xét tính đúng, sai của các mệnh đề sau}}{{\n{tikz}\n}}"
    )
    items = [
        (
            f"$f(x) = {f_tex}$.",
            f"$f(x) = {wrong_f_tex}$.",
            f"Parabol có đỉnh $I({x0}; {y0})$, hệ số $a = {a}$ và đi qua $(0; {c})$ nên $f(x) = {f_tex}$.",
            f"Kiểm tra hoành độ đỉnh của $y = {wrong_f_tex}$ là $x_I = {-x0} \\ne {x0}$."
        ),
        (
            f"Phương trình $f(x) = {y0}$ có nghiệm duy nhất $x = {x0}$.",
            f"Phương trình $f(x) = {y0}$ có đúng hai nghiệm thực phân biệt.",
            f"Đường thẳng $y = {y0}$ tiếp xúc với parabol tại đỉnh $I({x0}; {y0})$ nên chỉ có nghiệm duy nhất $x = {x0}$.",
            f"Vì $I({x0}; {y0})$ là đỉnh parabol nên đường thẳng $y = {y0}$ chỉ cắt đồ thị tại 1 điểm."
        ),
        (
            f"Hàm số đã cho {'đồng biến' if a > 0 else 'nghịch biến'} trên $({x0}; +\\infty)$.",
            f"Hàm số đã cho {'nghịch biến' if a > 0 else 'đồng biến'} trên $({x0}; +\\infty)$.",
            f"Do $a = {a}$ {'$> 0$' if a > 0 else '$< 0$'} và đỉnh có hoành độ $x_I = {x0}$, hàm số {'đồng biến' if a > 0 else 'nghịch biến'} trên $({x0}; +\\infty)$.",
            f"Quan sát nhánh bên phải $x = {x0}$, đồ thị đi {'lên' if a > 0 else 'xuống'} nên hàm số {'đồng biến' if a > 0 else 'nghịch biến'}."
        ),
        (
            f"Giá trị {'nhỏ nhất' if a > 0 else 'lớn nhất'} của hàm số là ${y0}$.",
            f"Giá trị {'lớn nhất' if a > 0 else 'nhỏ nhất'} của hàm số là ${y0}$.",
            f"Đỉnh $I({x0}; {y0})$ là điểm {'thấp nhất' if a > 0 else 'cao nhất'} của đồ thị.",
            f"Vì $a = {a}$ nên ${y0}$ là giá trị {'nhỏ nhất' if a > 0 else 'lớn nhất'}, không phải {'lớn nhất' if a > 0 else 'nhỏ nhất'}."
        ),
    ]
    choices, loigiai = _make_tf_choices(items)
    return caudan, choices, loigiai


def K10_C6_TF_KhaoSat_HamBacHai_BangBienThien():
    """Bộ đề Câu 1 (Đúng/Sai): Cho hàm bậc hai f(x) có f(x1)=y1 và bảng biến thiên, tìm hàm số & tính giá trị."""
    a = random.choice([-2, -1, 1, 2])
    xI = random.choice([-1, 1, 2])
    yI = random.choice([-3, 2, 3, 4])
    b = -2 * a * xI
    c = a * xI * xI + yI

    x_given = xI + 1
    y_given = a * x_given * x_given + b * x_given + c
    x_test = xI - 2
    y_test = a * x_test * x_test + b * x_test + c

    if a > 0:
        tab_var = f"\\tkzTabVar{{+/$+\\infty$,-/${yI}$,+/$+\\infty$}}"
        ext_label = "nhỏ nhất"
        opp_label = "lớn nhất"
    else:
        tab_var = f"\\tkzTabVar{{-/$ -\\infty$,+/${yI}$,-/$-\\infty$}}"
        ext_label = "lớn nhất"
        opp_label = "nhỏ nhất"

    tikz = (
        "\\begin{tikzpicture}[scale=0.8]\n"
        f"    \\tkzTabInit[lgt=1.3,espcl=2.5,deltacl=0.6]{{$x$/0.8,$f(x)$/1.5}}{{$ -\\infty$,${xI}$,$+\\infty$}}\n"
        f"    {tab_var}\n"
        "\\end{tikzpicture}"
    )

    f_tex = _quad_tex(a, b, c)
    wrong_f_tex = _quad_tex(a, b + (2 if a > 0 else -2), c + 1)
    caudan = (
        f"Cho hàm số bậc hai $y = f(x)$ có $f({x_given}) = {y_given}$ và bảng biến thiên như hình dưới đây:\n"
        f"\\begin{{center}}\n{tikz}\n\\end{{center}}\n"
        f"Các khẳng định sau đây đúng hay sai?"
    )
    items = [
        (
            f"Hàm số đạt giá trị {ext_label} bằng ${yI}$.",
            f"Hàm số đạt giá trị {opp_label} bằng ${yI}$.",
            f"Từ bảng biến thiên thấy ngay giá trị {ext_label} của $f(x)$ bằng ${yI}$ tại $x = {xI}$.",
            f"Từ bảng biến thiên, ${yI}$ là giá trị {ext_label}, không phải {opp_label}."
        ),
        (
            f"Hàm số bậc hai là $y = {f_tex}$.",
            f"Hàm số bậc hai là $y = {wrong_f_tex}$.",
            f"Từ $f(x) = a(x - {xI})^2 + ({yI})$ và $f({x_given}) = {y_given}$ suy ra $a = {a}$, tức $f(x) = {f_tex}$.",
            f"Công thức đúng phải là $y = {f_tex}$."
        ),
        (
            f"Giá trị của hàm số tại $x = 0$ là ${c}$.",
            f"Giá trị của hàm số tại $x = 0$ là ${c + 2}$.",
            f"$f(0) = c = {c}$.",
            f"$f(0) = {c} \\ne {c + 2}$."
        ),
        (
            f"Giá trị của hàm số tại $x = {x_test}$ là ${y_test}$.",
            f"Giá trị của hàm số tại $x = {x_test}$ là ${y_test + 2}$.",
            f"Thay $x = {x_test}$ vào $f(x) = {f_tex}$ được $f({x_test}) = {y_test}$.",
            f"$f({x_test}) = {y_test} \\ne {y_test + 2}$."
        ),
    ]
    choices, loigiai = _make_tf_choices(items)
    return caudan, choices, loigiai


def K10_C6_TF_PhuongTrinh_CanF_Bang_CanG_NghiemNgoaiLai():
    """Trang 18 Câu 2 (Đúng/Sai): Phương trình sqrt(f(x)) = sqrt(g(x)) bình phương ra PT bậc hai có 1 nghiệm ngoại lai."""
    # Thiết kế phương trình: sqrt(a*x^2 + b*x + c) = sqrt(d*x + e)  (1)
    # Bình phương: a*x^2 + (b - d)*x + (c - e) = 0  (2)
    # Muốn (2) có 2 nghiệm r_ok và r_bad với d*r_ok + e >= 0 và d*r_bad + e < 0:
    # Đặt P(x) = -(x - r_ok)*(x - r_bad) = -x^2 + (r_ok + r_bad)*x - r_ok*r_bad = 0 (nếu muốn hệ số -1 như sách!)
    configs = [
        # (r_ok, r_bad, d, e) -> kiểm tra g(r_ok) > 0, g(r_bad) < 0
        (-1, 12, -10, -5),   # g(-1)=5>0, g(12)=-125<0 -> PT giống Trang 18 Câu 2!
        (-2, 9, -5, -1),     # g(-2)=9>0, g(9)=-46<0
        (1, 10, -3, 8),      # g(1)=5>0, g(10)=-22<0
        (-1, 8, -4, 3),      # g(-1)=7>0, g(8)=-29<0
        (2, -7, 3, 4),       # g(2)=10>0, g(-7)=-17<0
    ]
    r_ok, r_bad, d, e = random.choice(configs)
    # Đặt g(x) = d*x + e, và bình phương hai vế: (a*x^2+b*x+c) - (d*x+e) = -(x - r_ok)*(x - r_bad) = -x^2 + (r_ok+r_bad)*x - r_ok*r_bad
    a = -1
    b = (r_ok + r_bad) + d
    c = -(r_ok * r_bad) + e
    f_tex = _quad_tex(a, b, c)
    g_tex = _lin_tex(d, e)
    sq_tex = _quad_tex(-1, r_ok + r_bad, -(r_ok * r_bad))

    caudan = (
        f"Cho phương trình $\\sqrt{{{f_tex}}} = \\sqrt{{{g_tex}}}$ \\quad (1). "
        f"Bình phương hai vế của phương trình (1) ta được phương trình ${sq_tex} = 0$ \\quad (2)."
    )
    items = [
        (
            "Phương trình (1) và phương trình (2) không tương đương (khác tập nghiệm).",
            "Phương trình (1) và phương trình (2) có cùng tập nghiệm.",
            f"Phương trình (2) có hai nghiệm $x = {r_ok}$ và $x = {r_bad}$, nhưng $x = {r_bad}$ không thỏa mãn điều kiện ${g_tex} \\ge 0$ nên không phải nghiệm của (1).",
            f"Bình phương hai vế chỉ là phép biến đổi hệ quả; $x = {r_bad}$ là nghiệm của (2) nhưng không thỏa điều kiện của (1)."
        ),
        (
            "Phương trình (1) có duy nhất một nghiệm.",
            "Phương trình (1) có hai nghiệm phân biệt.",
            f"Chỉ có $x = {r_ok}$ thỏa mãn điều kiện xác định ${g_tex} \\ge 0$ nên (1) có đúng 1 nghiệm.",
            f"Trong hai nghiệm của (2) chỉ có $x = {r_ok}$ thỏa mãn (1) (do ${g_tex} < 0$ tại $x = {r_bad}$)."
        ),
        (
            f"$x = {r_bad}$ không là nghiệm của phương trình (1).",
            f"$x = {r_bad}$ là nghiệm của phương trình (1).",
            f"Thay $x = {r_bad}$ vào biểu thức dưới dấu căn bên phải được ${d * r_bad + e} < 0$ nên không xác định.",
            f"Tại $x = {r_bad}$, biểu thức dưới dấu căn có giá trị âm (${d * r_bad + e} < 0$) nên bị loại."
        ),
        (
            f"$x = {r_ok}$ là nghiệm của phương trình (1).",
            f"$x = {r_ok}$ không là nghiệm của phương trình (1).",
            f"Thay $x = {r_ok}$ vào (1) thấy cả hai vế đều bằng $\\sqrt{{{d * r_ok + e}}}$ nên $x = {r_ok}$ là nghiệm.",
            f"Thay trực tiếp $x = {r_ok}$ thỏa mãn điều kiện và hai vế bằng nhau."
        ),
    ]
    choices, loigiai = _make_tf_choices(items)
    return caudan, choices, loigiai


K10_HK2_CHUONG6_MC_EXTRA_MAP = {
    "Dạng: Tập xác định hàm số chứa căn tam thức bậc hai (và phân thức)": K10_C3_MC_HamSo_TapXacDinh_CanTamThuc_Va_KetHop,
    "Dạng: Nhận diện hàm số có tập xác định là R": K10_C3_MC_HamSo_NhanDien_TapXacDinh_R,
    "Dạng: Nhận diện hàm số bậc hai": K10_C3_MC_HamSo_NhanDien_HamBacHai,
    "Dạng: Tìm tọa độ giao điểm của hai đồ thị hàm số bậc nhất": K10_C3_MC_HamSo_GiaoDiem_HaiDuongThang,
    "Dạng: Tìm tọa độ giao điểm của parabol và đường thẳng": K10_C3_MC_Parabol_GiaoDiem_DuongThang,
    "Dạng: Nhận diện bất phương trình bậc hai một ẩn": K10_C7_MC_BPT_NhanDien_BacHaiMotAn,
    "Dạng: Giải bất phương trình bậc hai một ẩn": K10_C7_MC_BPT_Giai_CoBan,
    "Dạng: Kiểm tra nghiệm và phát biểu đúng sai về bất phương trình bậc hai": K10_C7_MC_BPT_KiemTraNghiem_Va_PhatBieu,
    "Dạng: Đếm số nghiệm nguyên của bất phương trình bậc hai": K10_C7_MC_BPT_DemNghiemNguyen,
    "Dạng: Chọn bảng xét dấu đúng của tam thức bậc hai": K10_C7_MC_TamThuc_ChonBangXetDau_TikZ,
    "Dạng: Đọc đồ thị parabol để giải bất phương trình bậc hai": K10_C7_MC_BPT_DocDoThiParabol,
    "Dạng: Tìm tham số m để tam thức bậc hai luôn cùng dấu trên R": K10_C7_MC_TamThuc_ThamSoM_CungDauTrenR,
    "Dạng: Phương trình căn f(x) bằng căn g(x) tính biểu thức hai nghiệm": K10_C7_MC_PT_CanF_Bang_CanG_BieuThucNghiem,
    "Dạng: Phương trình chứa căn có nghiệm phân số hoặc vô tỉ tính biểu thức": K10_C7_MC_PT_CanF_Bang_G_BieuThucPhanSo_VoTi,
}

K10_HK2_CHUONG6_TF_MAP = {
    "Đúng sai - Hàm số (Bài 15-16): Đồ thị parabol qua gốc tọa độ O(0;0) (nghiệm, f(0), đơn điệu, GTLN/GTNN)": K10_C6_TF_DoThi_Parabol_QuaGocToaDo,
    "Đúng sai - Hàm số bậc hai (Bài 16): Khảo sát đồ thị parabol từ đỉnh và giao trục tung": K10_C6_TF_KhaoSat_DoThi_Parabol_Dinh_GiaoDiem,
    "Đúng sai - Hàm số bậc hai (Bài 16): Khảo sát hàm số bậc hai từ bảng biến thiên và giá trị f(x0)": K10_C6_TF_KhaoSat_HamBacHai_BangBienThien,
    "Đúng sai - Phương trình chứa căn (Bài 18): Bình phương hai vế và phân tích nghiệm ngoại lai": K10_C6_TF_PhuongTrinh_CanF_Bang_CanG_NghiemNgoaiLai,
}


def dispatch_k10_hk2_chuong6_extra(item):
    """Sinh block LaTeX MC hoặc Đúng/Sai cho các dạng bổ sung Chương VI Lớp 10."""
    fn_mc = K10_HK2_CHUONG6_MC_EXTRA_MAP.get(item)
    if fn_mc is not None:
        caudan, phuongan, loigiai = fn_mc()
        return "\\begin{ex}\n" + caudan + "\n\\choice\n" + "".join(phuongan) + "\\loigiai{" + loigiai + "}\n\\end{ex}"
    fn_tf = K10_HK2_CHUONG6_TF_MAP.get(item)
    if fn_tf is not None:
        caudan, phuongan, loigiai = fn_tf()
        return "\\begin{ex}\n" + caudan + "\n\\choiceTF\n" + "".join(phuongan) + "\\loigiai{" + loigiai + "}\n\\end{ex}"
    return None
