"""Ngân hàng câu hỏi sinh ngẫu nhiên bổ sung cho Toán 10 Học kì 1:
- Chương IV: Vectơ (đếm cặp vectơ cùng hướng trên lưới, tích vô hướng hình vuông, Đúng/Sai tọa độ Oxy)
- Chương V:
  + Bài 12: Số gần đúng và sai số (MC & TLN)
  + Bài 13: Các số đặc trưng đo xu thế trung tâm (MC & TLN, gồm biểu đồ cột đôi TikZ)
  + Bài 14: Các số đặc trưng đo độ phân tán (MC & TLN, gồm biểu đồ đoạn thẳng TikZ)
  + Trắc nghiệm Đúng/Sai Chương V (5 dạng mẫu số liệu, bảng tần số, so sánh 2 mẫu, biểu đồ cột TikZ)
"""

import math
import random
from fractions import Fraction


# ==============================================================================
# CÁC HÀM PHỤ TRỢ TOÁN HỌC & THỐNG KÊ CHUẨN SGK TOÁN 10
# ==============================================================================

def _fmt_vn(val, decimals=2):
    """Định dạng số thập phân kiểu Việt Nam (dấu phẩy), bỏ số 0 thừa ở cuối nếu là số nguyên."""
    if isinstance(val, int):
        return str(val)
    if abs(val - round(val)) < 1e-9:
        return str(int(round(val)))
    s = f"{val:.{decimals}f}".rstrip("0").rstrip(".")
    return s.replace(".", ",")


def _frac_tex(val):
    f = Fraction(val).limit_denominator()
    if f.denominator == 1:
        return str(f.numerator)
    if f.numerator < 0:
        return f"-\\dfrac{{{-f.numerator}}}{{{f.denominator}}}"
    return f"\\dfrac{{{f.numerator}}}{{{f.denominator}}}"


def _make_mc_choices(correct_str, distractors):
    """Tạo 4 phương án \\choice đôi một khác nhau và xáo trộn."""
    seen = {correct_str}
    pool = []
    for d in distractors:
        if d not in seen:
            seen.add(d)
            pool.append(d)
    if len(pool) < 3:
        raise ValueError(f"Không đủ phương án nhiễu phân biệt cho: {correct_str}")
    items = [(True, correct_str)] + [(False, x) for x in pool[:3]]
    random.shuffle(items)
    res = []
    for ok, txt in items:
        prefix = "{\\True " if ok else "{"
        res.append(f"{prefix}{txt}}}\n")
    return res


def _make_tf_choices(statements):
    """statements: list of 4 tuples (is_true: bool, text: str)."""
    return [f"{'{\\True ' if ok else '{'}{txt}}}\n" for ok, txt in statements]


def _median_sorted(arr):
    n = len(arr)
    mid = n // 2
    if n % 2 == 1:
        return float(arr[mid])
    return (arr[mid - 1] + arr[mid]) / 2.0


def _quartiles(data):
    """Tính Q1, Q2, Q3 theo chuẩn SGK Toán 10."""
    s = sorted(data)
    n = len(s)
    mid = n // 2
    q2 = _median_sorted(s)
    if n % 2 == 0:
        lower = s[:mid]
        upper = s[mid:]
    else:
        lower = s[:mid]
        upper = s[mid + 1:]
    q1 = _median_sorted(lower)
    q3 = _median_sorted(upper)
    return q1, q2, q3


def _stats_summary(data):
    """Tính đầy đủ các số đặc trưng của mẫu số liệu."""
    n = len(data)
    mean = sum(data) / n
    q1, q2, q3 = _quartiles(data)
    dq = q3 - q1
    r = max(data) - min(data)
    var = sum((x - mean) ** 2 for x in data) / n
    std = math.sqrt(var)
    freq = {}
    for x in data:
        freq[x] = freq.get(x, 0) + 1
    max_f = max(freq.values())
    modes = sorted(k for k, v in freq.items() if v == max_f)
    low_fence = q1 - 1.5 * dq
    high_fence = q3 + 1.5 * dq
    outliers = [x for x in data if x < low_fence or x > high_fence]
    return {
        "n": n,
        "mean": mean,
        "q1": q1,
        "q2": q2,
        "q3": q3,
        "dq": dq,
        "r": r,
        "var": var,
        "std": std,
        "modes": modes,
        "low_fence": low_fence,
        "high_fence": high_fence,
        "outliers": outliers,
        "freq": freq,
    }


def _round_half_up(val, ndigits=0):
    factor = 10 ** ndigits
    if val >= 0:
        return math.floor(val * factor + 0.5 + 1e-12) / factor
    return -math.floor(-val * factor + 0.5 + 1e-12) / factor


# ==============================================================================
# PHẦN 1: BỔ SUNG CHƯƠNG IV - VECTƠ & TỌA ĐỘ OXY
# ==============================================================================

def k10_mc_vecto_dem_cap_cung_huong_luoi():
    """Đếm số cặp vectơ cùng hướng trên lưới ô vuông gồm 7 vectơ (TikZ)."""
    # Sinh 7 vectơ trên lưới ô vuông với 1 hoặc 2 hoặc 3 cặp cùng hướng
    scenarios = [
        # (danh sách (tên, x0, y0, dx, dy, lx, ly), số cặp đúng)
        ([
            ("\\vec{a}", 1, 0, 2, 2, 1.8, 1.5),
            ("\\vec{b}", 7, 0, -1, 3, 6.9, 1.7),
            ("\\vec{c}", 0, 4, 4, 0, 2.0, 3.6),
            ("\\vec{d}", 2, 0, 3, 0, 3.5, 0.4),
            ("\\vec{e}", 10, 4, 1, -3, 10.9, 2.6),
            ("\\vec{f}", 8, 0, 1, 1, 8.8, 0.3),
            ("\\vec{g}", 6, 4, 3, -1, 7.5, 3.1),
        ], 2),  # (a, f) cùng hướng (1,1) và (c, d) cùng hướng (1,0)
        ([
            ("\\vec{a}", 0, 0, 2, 1, 1.0, 0.9),
            ("\\vec{b}", 3, 4, 0, -3, 3.4, 2.5),
            ("\\vec{c}", 5, 0, 4, 2, 7.0, 1.4),
            ("\\vec{d}", 1, 4, 3, 0, 2.5, 3.6),
            ("\\vec{e}", 9, 4, -2, -1, 8.0, 3.1),
            ("\\vec{f}", 11, 1, 0, 2, 11.4, 2.0),
            ("\\vec{g}", 4, 2, 2, 0, 5.0, 2.4),
        ], 1),  # Chỉ (a, c) cùng hướng (2,1); (d, g) cùng hướng (1,0) -> thực ra 2 cặp! Sửa g thành (2,-1) để đúng 1 cặp
        ([
            ("\\vec{a}", 0, 1, 3, 0, 1.5, 1.4),
            ("\\vec{b}", 4, 0, 1, 2, 4.9, 1.0),
            ("\\vec{c}", 6, 1, 2, 0, 7.0, 1.4),
            ("\\vec{d}", 9, 0, 2, 4, 10.4, 2.0),
            ("\\vec{e}", 0, 4, 4, 0, 2.0, 3.6),
            ("\\vec{f}", 5, 4, 2, -1, 6.0, 3.1),
            ("\\vec{g}", 10, 4, -1, -2, 9.1, 3.0),
        ], 4),  # (a, c), (a, e), (c, e) = 3 cặp + (b, d) = 1 cặp => 4 cặp! Đổi để đa dạng: 3 cặp
    ]
    # Xây dựng kịch bản kiểm đếm tự động chính xác tuyệt đối
    presets = [
        [
            ("\\vec{a}", 1, 0, 2, 2, 1.7, 1.4),
            ("\\vec{b}", 7, 0, -1, 3, 6.9, 1.6),
            ("\\vec{c}", 0, 4, 4, 0, 2.0, 3.6),
            ("\\vec{d}", 2, 0, 3, 0, 3.5, 0.4),
            ("\\vec{e}", 10, 4, 1, -3, 10.9, 2.6),
            ("\\vec{f}", 8, 0, 1, 1, 8.8, 0.3),
            ("\\vec{g}", 6, 4, 3, -1, 7.5, 3.1),
        ],
        [
            ("\\vec{a}", 0, 0, 2, 1, 1.0, 0.9),
            ("\\vec{b}", 3, 4, 0, -3, 3.4, 2.5),
            ("\\vec{c}", 5, 0, 4, 2, 7.0, 1.4),
            ("\\vec{d}", 1, 4, 3, 0, 2.5, 3.6),
            ("\\vec{e}", 9, 4, -2, -1, 8.0, 3.1),
            ("\\vec{f}", 11, 1, 0, 2, 11.4, 2.0),
            ("\\vec{g}", 5, 3, 2, -1, 6.0, 2.1),
        ],
        [
            ("\\vec{a}", 0, 1, 3, 0, 1.5, 1.4),
            ("\\vec{b}", 4, 0, 1, 2, 4.9, 1.0),
            ("\\vec{c}", 6, 1, 2, 0, 7.0, 1.4),
            ("\\vec{d}", 9, 0, 2, 4, 10.4, 2.0),
            ("\\vec{e}", 0, 4, 4, 0, 2.0, 3.6),
            ("\\vec{f}", 5, 4, 2, -1, 6.0, 3.1),
            ("\\vec{g}", 10, 4, -1, -2, 9.1, 3.0),
        ],
        [
            ("\\vec{a}", 0, 0, 0, 3, 0.4, 1.5),
            ("\\vec{b}", 2, 4, 0, -2, 2.4, 3.0),
            ("\\vec{c}", 4, 1, 0, 2, 4.4, 2.0),
            ("\\vec{d}", 6, 0, 3, 1, 7.5, 0.9),
            ("\\vec{e}", 10, 1, 2, 2, 11.2, 1.8),
            ("\\vec{f}", 6, 4, 3, -1, 7.5, 3.1),
            ("\\vec{g}", 8, 2, 1, 1, 8.8, 2.3),
        ],
    ]
    vecs = random.choice(presets)
    # Đếm chính xác số cặp cùng hướng: dx1*dy2 == dy1*dx2 và dx1*dx2 + dy1*dy2 > 0
    same_pairs = []
    for i in range(len(vecs)):
        for j in range(i + 1, len(vecs)):
            n1, _, _, dx1, dy1, _, _ = vecs[i]
            n2, _, _, dx2, dy2, _, _ = vecs[j]
            if dx1 * dy2 == dy1 * dx2 and (dx1 * dx2 + dy1 * dy2) > 0:
                same_pairs.append(f"${n1}$ và ${n2}$")
    ans = len(same_pairs)

    tikz_lines = [
        "\\begin{center}",
        "\\begin{tikzpicture}[scale=0.65,>=stealth]",
        "\\draw[gray!35,thin] (0,0) grid (12,4);",
    ]
    for name, x0, y0, dx, dy, lx, ly in vecs:
        tikz_lines.append(f"\\draw[->,thick] ({x0},{y0}) -- ({x0+dx},{y0+dy});")
        tikz_lines.append(f"\\fill ({x0},{y0}) circle (1.8pt);")
        tikz_lines.append(f"\\node at ({lx},{ly}) {{${name}$}};")
    tikz_lines.append("\\end{tikzpicture}")
    tikz_lines.append("\\end{center}")
    tikz = "\n".join(tikz_lines)

    caudan = f"Hình bên dưới có bao nhiêu cặp vectơ cùng hướng?\n{tikz}"
    cand_nums = [0, 1, 2, 3, 4, 5]
    distractors = [f"${k}$." for k in cand_nums if k != ans]
    phuongan = _make_mc_choices(f"${ans}$.", distractors)
    loigiai = (
        f"Quan sát phương và chiều của các vectơ trên lưới ô vuông, các cặp vectơ cùng hướng là: "
        f"{', '.join(same_pairs) if same_pairs else 'không có cặp nào'}.\n"
        f"Vậy có tất cả ${ans}$ cặp vectơ cùng hướng."
    )
    return caudan, phuongan, loigiai


def k10_mc_vecto_tich_vo_huong_hinh_vuong_duong_cheo():
    """Cho hình vuông ABCD cạnh a. Tính (AB + AD).BD hoặc (AB - AD).AC."""
    a_sym = random.choice(["a", "2a", "3a"])
    mode = random.choice(["sum_bd", "diff_ac"])
    if mode == "sum_bd":
        expr = r"(\overrightarrow{AB} + \overrightarrow{AD}) \cdot \overrightarrow{BD}"
        explain = (
            r"Theo quy tắc hình bình hành, $\overrightarrow{AB} + \overrightarrow{AD} = \overrightarrow{AC}$. "
            r"Vì $ABCD$ là hình vuông nên $AC \perp BD$, suy ra $\overrightarrow{AC} \perp \overrightarrow{BD}$. "
            r"Do đó $(\overrightarrow{AB} + \overrightarrow{AD}) \cdot \overrightarrow{BD} = \overrightarrow{AC} \cdot \overrightarrow{BD} = 0$."
        )
    else:
        expr = r"(\overrightarrow{AB} - \overrightarrow{AD}) \cdot \overrightarrow{AC}"
        explain = (
            r"Ta có $\overrightarrow{AB} - \overrightarrow{AD} = \overrightarrow{DB}$. "
            r"Vì $ABCD$ là hình vuông nên $DB \perp AC$, suy ra $\overrightarrow{DB} \perp \overrightarrow{AC}$. "
            r"Do đó $(\overrightarrow{AB} - \overrightarrow{AD}) \cdot \overrightarrow{AC} = \overrightarrow{DB} \cdot \overrightarrow{AC} = 0$."
        )
    caudan = f"Cho hình vuông $ABCD$ có cạnh bằng ${a_sym}$. Tính $P = {expr}$."
    distractors = [
        f"$P = {a_sym}^2$." if a_sym == "a" else f"$P = {int(a_sym[0])**2}a^2$.",
        f"$P = \\sqrt{{2}}{a_sym}^2$." if a_sym == "a" else f"$P = {int(a_sym[0])**2}\\sqrt{{2}}a^2$.",
        f"$P = 2\\sqrt{{2}}{a_sym}^2$." if a_sym == "a" else f"$P = {2*int(a_sym[0])**2}\\sqrt{{2}}a^2$.",
    ]
    phuongan = _make_mc_choices("$P = 0$.", distractors)
    return caudan, phuongan, explain


def k10_tf_oxy_to_hop_c_a_2b_va_pq():
    """Đúng/Sai Oxy: a = x i + y j, b = (bx; by), c = a - 2b và P, Q."""
    while True:
        ax = random.choice([-4, -3, 3, 4, 5, 6])
        ay = random.choice([-6, -5, -4, 4, 5, 6])
        bx = random.choice([-4, -3, 3, 4])
        by = random.choice([-4, -3, 3, 4])
        if abs(bx) == 3 and abs(by) == 4:
            len_b_true = 5
        elif abs(bx) == 4 and abs(by) == 3:
            len_b_true = 5
        else:
            continue
        cx = ax - 2 * bx
        cy = ay - 2 * by
        if cx == 0 or cy == 0:
            continue
        px = random.randint(-2, 4)
        py = random.randint(-2, 4)
        k = random.choice([1, -1, 2])
        collinear_d = random.choice([True, False])
        if collinear_d:
            qx = px + k * cx
            qy = py + k * cy
        else:
            qx = px + cx + random.choice([1, -1])
            qy = py + cy
        break

    pqx = qx - px
    pqy = qy - py

    def _fmt_ij(x, y):
        sx = f"{x}\\vec{{i}}"
        sy = f"+ {y}\\vec{{j}}" if y > 0 else f"- {-y}\\vec{{j}}"
        return f"{sx} {sy}"

    a_true = random.choice([True, False])
    a_shown = (ax, ay) if a_true else (ax // 2 if ax % 2 == 0 else -ax, ay // 2 if ay % 2 == 0 else -ay)

    b_true = random.choice([True, False])
    b_shown = (pqx, pqy) if b_true else (pqx + 1, pqy - 1)

    c_true = random.choice([True, False])
    c_shown = len_b_true if c_true else 1

    caudan = (
        f"Trong mặt phẳng tọa độ $Oxy$, cho các vectơ $\\vec{{a}} = {_fmt_ij(ax, ay)}$, "
        f"$\\vec{{b}} = ({bx}; {by})$, $\\vec{{c}} = \\vec{{a}} - 2\\vec{{b}}$ "
        f"và hai điểm $P({px}; {py})$, $Q({qx}; {qy})$."
    )
    choices = _make_tf_choices([
        (a_true, f"$\\vec{{a}} = ({a_shown[0]}; {a_shown[1]})$."),
        (b_true, f"$\\overrightarrow{{PQ}} = ({b_shown[0]}; {b_shown[1]})$."),
        (c_true, f"$|\\vec{{b}}| = {c_shown}$."),
        (collinear_d, "Hai vectơ $\\overrightarrow{PQ}$ và $\\vec{c}$ cùng phương."),
    ])
    loigiai = (
        f"\\begin{{itemchoice}}\n"
        f"\\itemch {'Đúng' if a_true else 'Sai'}. Ta có $\\vec{{a}} = ({ax}; {ay})$.\n"
        f"\\itemch {'Đúng' if b_true else 'Sai'}. $\\overrightarrow{{PQ}} = ({qx}-({px}); {qy}-({py})) = ({pqx}; {pqy})$.\n"
        f"\\itemch {'Đúng' if c_true else 'Sai'}. $|\\vec{{b}}| = \\sqrt{{({bx})^2 + ({by})^2}} = {len_b_true}$.\n"
        f"\\itemch {'Đúng' if collinear_d else 'Sai'}. Ta có $\\vec{{c}} = \\vec{{a}} - 2\\vec{{b}} = ({cx}; {cy})$. "
        f"Xét $({pqx})\\cdot({cy}) - ({pqy})\\cdot({cx}) = {pqx*cy - pqy*cx}$ "
        f"{'$= 0$ nên cùng phương' if collinear_d else '$\\neq 0$ nên không cùng phương'}.\n"
        f"\\end{{itemchoice}}"
    )
    return caudan, choices, loigiai


# ==============================================================================
# PHẦN 2: CHƯƠNG V - BÀI 12. SỐ GẦN ĐÚNG VÀ SAI SỐ
# ==============================================================================

def k10_mc_c5_b12_ly_thuyet_sai_so():
    """Lý thuyết về số gần đúng và sai số tuyệt đối."""
    caudan = "Cho số $a$ là số gần đúng của số đúng $\\bar{a}$. Mệnh đề nào sau đây là mệnh đề đúng?"
    variant = random.choice([1, 2])
    if variant == 1:
        phuongan = _make_mc_choices(
            "$\\Delta_a = |\\bar{a} - a|$ được gọi là sai số tuyệt đối của số gần đúng $a$.",
            [
                "$a > \\bar{a}$.",
                "$a < \\bar{a}$.",
                "$|\\bar{a} - a| > 0$ luôn đúng với mọi số gần đúng $a$.",
            ],
        )
        loigiai = "Theo định nghĩa, sai số tuyệt đối của số gần đúng $a$ là $\\Delta_a = |\\bar{a} - a| \\ge 0$."
    else:
        phuongan = _make_mc_choices(
            "Nếu $|\\bar{a} - a| \\le d$ thì $d$ gọi là độ chính xác của số gần đúng $a$.",
            [
                "Nếu $|\\bar{a} - a| \\le d$ thì $d$ gọi là sai số tương đối.",
                "Sai số tuyệt đối của số gần đúng $a$ là $\\bar{a} - a$.",
                "Số gần đúng $a$ luôn nhỏ hơn số đúng $\\bar{a}$.",
            ],
        )
        loigiai = "Nếu $\\Delta_a = |\\bar{a} - a| \\le d$ thì $d$ được gọi là độ chính xác của số gần đúng $a$."
    return caudan, phuongan, loigiai


def k10_mc_c5_b12_quy_tron_do_chinh_xac_d():
    """Tìm số quy tròn của số gần đúng a với độ chính xác d (số nguyên lớn hoặc số thập phân)."""
    mode = random.choice(["int_tens", "int_hundreds", "dec_hundredths"])
    if mode == "int_tens":
        # d ở hàng chục -> quy tròn đến hàng trăm
        a = random.randint(10, 95) * 1000 + random.randint(1, 9) * 100 + random.choice([15, 25, 42, 68, 74])
        d = random.choice([30, 40, 50, 60, 70, 80])
        ans_val = int(_round_half_up(a, -2))
        d_show = str(d)
        a_show = str(a)
        ans_str = f"${ans_val}$."
        wrong_vals = [
            int(_round_half_up(a, -1)),
            int(_round_half_up(a, -3)),
            ans_val + 100,
            ans_val - 100,
            ans_val + 200,
        ]
        distractors = [f"${w}$." for w in wrong_vals]
        loigiai = (
            f"Vì độ chính xác $d = {d}$ đến hàng chục nên ta quy tròn số $a = {a}$ đến hàng trăm.\n"
            f"Kết quả số quy tròn là ${ans_val}$."
        )
    elif mode == "int_hundreds":
        # d ở hàng trăm -> quy tròn đến hàng nghìn
        a = random.randint(1200, 8900) * 1000 + random.randint(1, 9) * 100 + random.randint(11, 89)
        d = random.choice([200, 300, 400, 500, 600])
        ans_val = int(_round_half_up(a, -3))
        a_show = str(a)
        d_show = str(d)
        ans_str = f"${ans_val}$."
        wrong_vals = [
            int(_round_half_up(a, -2)),
            ans_val + 1000,
            ans_val - 1000,
            ans_val + 500,
            ans_val - 500,
        ]
        distractors = [f"${w}$." for w in wrong_vals]
        loigiai = (
            f"Vì độ chính xác $d = {d}$ đến hàng trăm nên ta quy tròn số $a = {a}$ đến hàng nghìn.\n"
            f"Kết quả số quy tròn là ${ans_val}$."
        )
    else:
        # d = 0,01 -> quy tròn đến hàng phần chục
        base = random.choice([math.e, math.pi, math.sqrt(2), math.sqrt(3), math.sqrt(5)])
        name_map = {
            math.e: ("e", "2{,}718281828\\dots"),
            math.pi: ("\\pi", "3{,}14159265\\dots"),
            math.sqrt(2): ("\\sqrt{2}", "1{,}41421356\\dots"),
            math.sqrt(3): ("\\sqrt{3}", "1{,}7320508\\dots"),
            math.sqrt(5): ("\\sqrt{5}", "2{,}2360679\\dots"),
        }
        sym, dec_tex = name_map[base]
        d_val = 0.01
        ans_val = _round_half_up(base, 1)
        caudan = (
            f"Viết số gần đúng của ${sym} = {dec_tex}$ với độ chính xác $d = 0{{,}}01$, ta được kết quả là"
        )
        ans_str = f"${_fmt_vn(ans_val, 1)}$."
        distractors = [
            f"${_fmt_vn(_round_half_up(base, 2), 2)}$.",
            f"${_fmt_vn(_round_half_up(base, 3), 3)}$.",
            f"${_fmt_vn(ans_val + 0.1 if ans_val < base else ans_val - 0.1, 1)}$.",
        ]
        phuongan = _make_mc_choices(ans_str, distractors)
        loigiai = (
            f"Vì độ chính xác $d = 0{{,}}01$ ở hàng phần trăm nên ta quy tròn đến hàng phần chục.\n"
            f"Vậy số gần đúng cần tìm là ${_fmt_vn(ans_val, 1)}$."
        )
        return caudan, phuongan, loigiai

    caudan = f"Cho số gần đúng $a = {a_show}$ với độ chính xác $d = {d_show}$. Số quy tròn của số $a$ bằng"
    phuongan = _make_mc_choices(ans_str, distractors)
    return caudan, phuongan, loigiai


def k10_mc_c5_b12_quy_tron_dang_chuan():
    """Tìm số quy tròn của chiều dài/khối lượng viết dưới dạng l = a ± d."""
    whole = random.randint(120, 1850)
    dec = random.choice([14, 25, 36, 48, 62, 75, 84])
    val = whole + dec / 100.0
    d_mode = random.choice([0.01, 0.1])
    if d_mode == 0.01:
        ans_val = _round_half_up(val, 1)
        ans_str = f"${_fmt_vn(ans_val, 1)}$ m."
        distractors = [
            f"${whole}$ m.",
            f"${whole + 1}$ m.",
            f"${_fmt_vn(ans_val + 0.1 if ans_val <= val else ans_val - 0.1, 1)}$ m.",
        ]
        place_txt = "hàng phần trăm nên ta quy tròn đến hàng phần chục"
    else:
        ans_val = int(_round_half_up(val, 0))
        ans_str = f"${ans_val}$ m."
        distractors = [
            f"${_fmt_vn(_round_half_up(val, 1), 1)}$ m.",
            f"${ans_val + 1}$ m.",
            f"${ans_val - 1}$ m.",
        ]
        place_txt = "hàng phần chục nên ta quy tròn đến hàng đơn vị"

    caudan = (
        f"Chiều dài của một cây cầu là $l = {_fmt_vn(val, 2)}\\text{{ m}} \\pm {_fmt_vn(d_mode, 2)}\\text{{ m}}$. "
        f"Hãy cho biết số quy tròn của $l$."
    )
    phuongan = _make_mc_choices(ans_str, distractors)
    loigiai = f"Vì độ chính xác $d = {_fmt_vn(d_mode, 2)}$ đến {place_txt}, nên số quy tròn của $l$ là {ans_str}"
    return caudan, phuongan, loigiai


def k10_mc_c5_b12_gan_dung_can_thuc():
    """Giá trị gần đúng của căn bậc hai chính xác đến hàng phần trăm / phần chục."""
    n = random.choice([2, 3, 5, 6, 7, 10, 11, 13])
    val = math.sqrt(n)
    digits_10 = f"{val:.9f}".replace(".", ",")
    nd = random.choice([1, 2])
    ans_val = _round_half_up(val, nd)
    place = "hàng phần chục" if nd == 1 else "hàng phần trăm"
    ans_str = f"${_fmt_vn(ans_val, nd)}$."

    # Tạo nhiễu hợp lý gần kết quả
    other_nd = 2 if nd == 1 else 1
    trunc_nd = math.floor(val * (10 ** nd)) / (10 ** nd)
    if abs(trunc_nd - ans_val) < 1e-9:
        trunc_nd = ans_val - (10 ** (-nd))
    distractors = [
        f"${_fmt_vn(trunc_nd, nd)}$.",
        f"${_fmt_vn(_round_half_up(val, other_nd), other_nd)}$.",
        f"${_fmt_vn(_round_half_up(val, 3), 3)}$.",
        f"${_fmt_vn(ans_val + (10 ** (-nd)), nd)}$.",
        f"${_fmt_vn(ans_val + 2 * (10 ** (-nd)), nd)}$.",
    ]
    caudan = (
        f"Khi sử dụng máy tính bỏ túi với $10$ chữ số thập phân ta được $\\sqrt{{{n}}} = {digits_10}\\dots$. "
        f"Giá trị gần đúng của $\\sqrt{{{n}}}$ chính xác đến {place} là"
    )
    phuongan = _make_mc_choices(ans_str, distractors)
    loigiai = f"Làm tròn số ${digits_10}\\dots$ đến {place}, ta được kết quả là ${_fmt_vn(ans_val, nd)}$."
    return caudan, phuongan, loigiai


def k10_mc_c5_b12_sai_so_tuong_doi():
    """Tính sai số tương đối của phép đo (dạng S = a ± d)."""
    a = round(random.uniform(110.0, 280.0), 2)
    d = random.choice([0.2, 0.3, 0.4, 0.5, 0.6, 0.8])
    rel_pct = (d / a) * 100.0
    ans_val = _round_half_up(rel_pct, 2)
    ans_str = f"${_fmt_vn(ans_val, 2)}\\%$."
    distractors = [
        f"${_fmt_vn(_round_half_up(ans_val * 10, 2), 2)}\\%$.",
        f"${_fmt_vn(_round_half_up(ans_val / 10, 2), 2)}\\%$.",
        f"${_fmt_vn(_round_half_up(ans_val + 0.15, 2), 2)}\\%$.",
    ]
    caudan = (
        f"Một hình chữ nhật có diện tích $S = {_fmt_vn(a, 2)}\\text{{ cm}}^2 \\pm {_fmt_vn(d, 1)}\\text{{ cm}}^2$. "
        f"Tính sai số tương đối của phép đo trên (làm tròn đến hàng phần trăm)."
    )
    phuongan = _make_mc_choices(ans_str, distractors)
    loigiai = (
        f"Sai số tương đối của phép đo không vượt quá "
        f"$\\delta_S \\le \\dfrac{{d}}{{S}} = \\dfrac{{{_fmt_vn(d, 1)}}}{{{_fmt_vn(a, 2)}}} \\approx {_fmt_vn(ans_val, 2)}\\%$."
    )
    return caudan, phuongan, loigiai


def k10_sa_c5_b12_chieu_dai_gan_dung_tu_sai_so():
    """TLN: Biết độ chính xác d và sai số tương đối <= delta%, tìm chiều dài gần đúng của cây cầu."""
    pct = random.choice([0.1, 0.15, 0.2, 0.25, 0.4, 0.5])
    true_len = random.choice([250, 300, 400, 500, 600, 750, 800])
    d = round(true_len * pct / 100.0, 2)
    caudan = (
        f"Kết quả đo chiều dài một cây cầu có độ chính xác là ${_fmt_vn(d, 2)}$ m "
        f"với dụng cụ đo đảm bảo sai số tương đối không vượt quá ${_fmt_vn(pct, 2)}\\%$. "
        f"Chiều dài gần đúng của cây cầu là bao nhiêu mét?"
    )
    dapan = str(true_len)
    loigiai = (
        f"Gọi $a$ (m) là chiều dài gần đúng của cây cầu. Vì sai số tương đối không vượt quá ${_fmt_vn(pct, 2)}\\%$ nên:\n"
        f"$$\\delta_a \\le \\dfrac{{d}}{{a}} \\le {_fmt_vn(pct, 2)}\\% \\Rightarrow a \\ge \\dfrac{{{_fmt_vn(d, 2)}}}{{{_fmt_vn(pct / 100.0, 4)}}} = {true_len}\\text{{ (m)}}.$$\n"
        f"Vậy chiều dài gần đúng của cây cầu là ${true_len}$ m."
    )
    return caudan, dapan, loigiai


# ==============================================================================
# PHẦN 3: CHƯƠNG V - BÀI 13. XU THẾ TRUNG TÂM (BỔ SUNG)
# ==============================================================================

def k10_mc_c5_b13_tong_co_mau_bang_tan_so():
    """Tìm tổng cỡ mẫu (số học sinh tham gia) từ bảng phân bố tần số."""
    scores = [4, 5, 6, 7, 8, 9, 10]
    freqs = [
        random.randint(2, 8),
        random.randint(8, 20),
        random.randint(25, 60),
        random.randint(60, 120),
        random.randint(35, 80),
        random.randint(4, 15),
        random.randint(1, 6),
    ]
    total = sum(freqs)
    max_f = max(freqs)
    cols = "c|" * len(scores)
    row1 = " & ".join(str(x) for x in scores)
    row2 = " & ".join(str(x) for x in freqs)
    table = (
        f"\\begin{{center}}\\begin{{tabular}}{{|l|{cols}}}\\hline "
        f"Điểm số & {row1} \\\\ \\hline "
        f"Số học sinh & {row2} \\\\ \\hline "
        f"\\end{{tabular}}\\end{{center}}"
    )
    caudan = (
        f"Nhà trường thống kê điểm thi môn Ngoại ngữ của học sinh trong kì thi khảo sát chất lượng. "
        f"Kết quả thống kê bằng bảng dưới đây:\n{table}\nHỏi có bao nhiêu học sinh tham gia kì thi?"
    )
    distractors = [
        f"${max_f}$.",
        f"${total + random.choice([12, 24, 35])}$.",
        f"${total - random.choice([10, 18, 25])}$.",
    ]
    phuongan = _make_mc_choices(f"${total}$.", distractors)
    loigiai = f"Tổng số học sinh tham gia kì thi là: ${' + '.join(str(x) for x in freqs)} = {total}$."
    return caudan, phuongan, loigiai


def k10_mc_c5_b13_trung_binh_hop_nhat_nhieu_nhom():
    """Tính khối lượng/điểm trung bình hợp nhất của 3 nhóm có cỡ mẫu và trung bình khác nhau."""
    n1, n2, n3 = random.choice([(10, 15, 25), (12, 18, 20), (15, 20, 25), (10, 20, 30)])
    x1 = random.randint(44, 56)
    x2 = random.randint(36, 46)
    x3 = random.randint(38, 48)
    total_n = n1 + n2 + n3
    mean = (n1 * x1 + n2 * x2 + n3 * x3) / total_n
    mean_r = _round_half_up(mean, 2)
    ans_str = f"${_fmt_vn(mean_r, 2)}$ kg."
    naive_mean = _round_half_up((x1 + x2 + x3) / 3.0, 2)
    distractors = [
        f"${_fmt_vn(naive_mean, 2)}$ kg.",
        f"${_fmt_vn(mean_r + 1.0, 2)}$ kg.",
        f"${_fmt_vn(mean_r - 1.5, 2)}$ kg.",
        f"${_fmt_vn(mean_r + 2.5, 2)}$ kg.",
        f"${_fmt_vn(mean_r - 2.5, 2)}$ kg.",
    ]
    caudan = (
        f"Ba nhóm học sinh gồm ${n1}$ người, ${n2}$ người, ${n3}$ người. "
        f"Cân nặng trung bình của mỗi nhóm lần lượt là ${x1}$ kg, ${x2}$ kg, ${x3}$ kg. "
        f"Khối lượng trung bình của ba nhóm học sinh đó là"
    )
    phuongan = _make_mc_choices(ans_str, distractors)
    loigiai = (
        f"Khối lượng trung bình của cả ba nhóm là:\n"
        f"$$\\bar{{x}} = \\dfrac{{{n1}\\cdot{x1} + {n2}\\cdot{x2} + {n3}\\cdot{x3}}}{{{n1}+{n2}+{n3}}} = {_fmt_vn(mean_r, 2)}\\text{{ kg}}.$$"
    )
    return caudan, phuongan, loigiai


def k10_mc_c5_b13_mot_day_so_nhieu_mot():
    """Tìm mốt của dãy số liệu rời rạc (có thể có 2 mốt)."""
    m1, m2 = sorted(random.sample([5, 6, 7, 8, 9], 2))
    others = [x for x in [5, 6, 7, 8, 9, 10] if x not in (m1, m2)]
    k_mode = random.choice([4, 5])
    data = [m1] * k_mode + [m2] * k_mode + [others[0]] * 2 + [others[1]] * 2 + [others[2]] * 1
    random.shuffle(data)
    seq = ";\\; ".join(str(x) for x in data)
    caudan = f"Điểm kiểm tra $15$ phút môn Toán của một nhóm học sinh được thống kê như sau:\n$${seq}.$$\nMốt của mẫu số liệu này bằng"
    ans_str = f"${m1}$ và ${m2}$."
    distractors = [
        f"${m1}$.",
        f"${m2}$.",
        f"${others[0]}$.",
    ]
    phuongan = _make_mc_choices(ans_str, distractors)
    loigiai = f"Các giá trị ${m1}$ và ${m2}$ cùng có tần số lớn nhất bằng ${k_mode}$, nên mẫu số liệu có hai mốt là ${m1}$ và ${m2}$."
    return caudan, phuongan, loigiai


def k10_mc_c5_b13_bieu_do_cot_doi_ti_le():
    """Biểu đồ cột đôi (TikZ) so sánh lợi nhuận 4 chi nhánh A, B, C, D qua 2 năm, tìm chi nhánh có tỉ lệ tăng cao nhất."""
    names = ["A", "B", "C", "D"]
    # Tạo 4 cặp (y20, y21) sao cho tỉ lệ tăng y21/y20 khác nhau rõ rệt
    ratios = [1.10, 1.20, 1.28, 1.42]
    random.shuffle(ratios)
    y20s = [random.choice([200, 240, 280, 320, 360, 400, 450]) for _ in range(4)]
    y21s = [int(round(y20 * r)) for y20, r in zip(y20s, ratios)]
    max_idx = max(range(4), key=lambda i: y21s[i] / y20s[i])
    best_branch = names[max_idx]

    # Vẽ TikZ biểu đồ cột đôi (scale y theo 100 -> 1 đơn vị)
    tikz = [
        "\\begin{center}",
        "\\begin{tikzpicture}[scale=0.8,>=stealth]",
        "\\draw[->] (0,0) -- (9.2,0);",
        "\\draw[->] (0,0) -- (0,6.6);",
    ]
    for y_val in range(0, 601, 100):
        yy = y_val / 100.0
        tikz.append(f"\\draw (-0.08,{yy}) -- (0.08,{yy}) node[left=4pt] {{\\scriptsize {y_val}}};")
    for idx, br in enumerate(names):
        x_base = 1.0 + idx * 2.0
        h1 = y20s[idx] / 100.0
        h2 = y21s[idx] / 100.0
        tikz.append(f"\\filldraw[fill=gray!60,draw=black] ({x_base-0.35},0) rectangle ({x_base},{h1});")
        tikz.append(f"\\node[above] at ({x_base-0.175},{h1}) {{\\tiny {y20s[idx]}}};")
        tikz.append(f"\\filldraw[fill=gray!20,draw=black] ({x_base+0.05},0) rectangle ({x_base+0.4},{h2});")
        tikz.append(f"\\node[above] at ({x_base+0.225},{h2}) {{\\tiny {y21s[idx]}}};")
        tikz.append(f"\\node[below] at ({x_base+0.025},-0.1) {{\\small {br}}};")
    tikz.append("\\filldraw[fill=gray!60,draw=black] (2.0,-1.0) rectangle (2.4,-0.75);")
    tikz.append("\\node[right] at (2.45,-0.88) {\\scriptsize Năm 2020};")
    tikz.append("\\filldraw[fill=gray!20,draw=black] (5.2,-1.0) rectangle (5.6,-0.75);")
    tikz.append("\\node[right] at (5.65,-0.88) {\\scriptsize Năm 2021};")
    tikz.append("\\end{tikzpicture}")
    tikz.append("\\end{center}")

    caudan = (
        "Biểu đồ dưới đây biểu diễn lợi nhuận (tỉ đồng) của $4$ chi nhánh $A, B, C, D$ trong năm 2020 và 2021. "
        "Trong năm 2021, chi nhánh nào có tỉ lệ lợi nhuận so với năm 2020 cao nhất?\n" + "\n".join(tikz)
    )
    ans_str = f"Chi nhánh {best_branch}."
    distractors = [f"Chi nhánh {n}." for n in names if n != best_branch]
    phuongan = _make_mc_choices(ans_str, distractors)
    ratio_txt = ", ".join(
        f"{names[i]}: $\\dfrac{{{y21s[i]}}}{{{y20s[i]}}} \\approx {_fmt_vn(y21s[i]/y20s[i], 2)}$"
        for i in range(4)
    )
    loigiai = f"Tính tỉ lệ lợi nhuận năm 2021 so với năm 2020 của từng chi nhánh: {ratio_txt}.\nVậy chi nhánh {best_branch} có tỉ lệ cao nhất."
    return caudan, phuongan, loigiai


def k10_sa_c5_b13_tim_x_biet_trung_binh_cong():
    """TLN: Tìm giá trị x còn thiếu trong bảng tần số khi biết điểm trung bình cộng."""
    x_true = random.choice([6.5, 6.8, 7.2, 7.5])
    scores_base = [4.0, 5.0, 6.0, 7.0, 8.0]
    freqs = [
        random.randint(4, 8),
        random.randint(4, 8),
        random.randint(10, 16),
        random.randint(4, 7),  # tần số ứng với x
        random.randint(6, 10),
        random.randint(4, 8),
    ]
    n_tot = sum(freqs)
    mean_val = round(
        (scores_base[0] * freqs[0] + scores_base[1] * freqs[1] + scores_base[2] * freqs[2]
         + x_true * freqs[3] + scores_base[3] * freqs[4] + scores_base[4] * freqs[5]) / n_tot,
        2,
    )
    # Tính lại x_true chính xác nếu mean_val làm tròn để ra đẹp -> dùng tổng chia hết hoặc làm tròn 1 chữ số thập phân
    # Đảm bảo đề cho mean_val chính xác, hỏi x làm tròn đến hàng phần chục
    x_exact = (
        mean_val * n_tot
        - (scores_base[0] * freqs[0] + scores_base[1] * freqs[1] + scores_base[2] * freqs[2]
           + scores_base[3] * freqs[4] + scores_base[4] * freqs[5])
    ) / freqs[3]
    x_round = _round_half_up(x_exact, 1)

    table = (
        "\\begin{center}\\begin{tabular}{|l|c|c|c|c|c|c|}\\hline "
        f"Điểm & $4{{,}}0$ & $5{{,}}0$ & $6{{,}}0$ & $x$ & $7{{,}}0$ & $8{{,}}0$ \\\\ \\hline "
        f"Số học sinh & ${freqs[0]}$ & ${freqs[1]}$ & ${freqs[2]}$ & ${freqs[3]}$ & ${freqs[4]}$ & ${freqs[5]}$ \\\\ \\hline "
        "\\end{tabular}\\end{center}"
    )
    caudan = (
        f"Điểm kiểm tra định kì của ${n_tot}$ học sinh lớp 10A được thống kê lại theo bảng số liệu sau:\n{table}\n"
        f"Biết điểm trung bình của lớp bằng ${_fmt_vn(mean_val, 2)}$. Giá trị của $x$ bằng bao nhiêu? (làm tròn kết quả đến hàng phần chục)"
    )
    dapan = _fmt_vn(x_round, 1)
    loigiai = (
        f"Ta có phương trình điểm trung bình:\n"
        f"$$\\dfrac{{4\\cdot{freqs[0]} + 5\\cdot{freqs[1]} + 6\\cdot{freqs[2]} + {freqs[3]}x + 7\\cdot{freqs[4]} + 8\\cdot{freqs[5]}}}{{{n_tot}}} = {_fmt_vn(mean_val, 2)}$$\n"
        f"Suy ra $x \\approx {_fmt_vn(x_round, 1)}$."
    )
    return caudan, dapan, loigiai


# ==============================================================================
# PHẦN 4: CHƯƠNG V - BÀI 14. ĐỘ PHÂN TÁN (BỔ SUNG)
# ==============================================================================

def k10_mc_c5_b14_cong_thuc_R_deltaQ_ngoai_le():
    """Lý thuyết công thức khoảng biến thiên R, khoảng tứ phân vị Delta_Q hoặc nhận biết giá trị ngoại lệ."""
    mode = random.choice(["R", "DQ", "outlier"])
    if mode == "R":
        caudan = "Trong thống kê, khoảng biến thiên của một mẫu số liệu được xác định bằng công thức nào sau đây?"
        phuongan = _make_mc_choices(
            "$R = x_{\\max} - x_{\\min}$.",
            [
                "$R = x_{\\min} - x_{\\max}$.",
                "$R = x_{\\max} + x_{\\min}$.",
                "$R = \\dfrac{x_{\\max} + x_{\\min}}{2}$.",
            ],
        )
        loigiai = "Khoảng biến thiên của mẫu số liệu là hiệu giữa giá trị lớn nhất và giá trị nhỏ nhất: $R = x_{\\max} - x_{\\min}$."
    elif mode == "DQ":
        caudan = "Trong thống kê, khoảng tứ phân vị của một mẫu số liệu được xác định bằng công thức nào sau đây?"
        phuongan = _make_mc_choices(
            "$\\Delta_Q = Q_3 - Q_1$.",
            [
                "$\\Delta_Q = Q_3 - Q_2$.",
                "$\\Delta_Q = Q_3 + Q_1$.",
                "$\\Delta_Q = Q_2 - Q_1$.",
            ],
        )
        loigiai = "Khoảng tứ phân vị là hiệu giữa tứ phân vị thứ ba và tứ phân vị thứ nhất: $\\Delta_Q = Q_3 - Q_1$."
    else:
        base = sorted(random.sample(range(1, 12), 7))
        outlier = random.randint(20, 28)
        data = base + [outlier]
        random.shuffle(data)
        st = _stats_summary(data)
        seq = ";\\; ".join(str(x) for x in data)
        caudan = f"Cho mẫu số liệu ${seq}$. Khẳng định nào sau đây là đúng?"
        phuongan = _make_mc_choices(
            f"Mẫu có một giá trị ngoại lệ là ${outlier}$.",
            [
                f"$R = {st['r'] + 1}$.",
                f"$Q_2 = {_fmt_vn(st['q2'] + 1)}$.",
                f"$\\Delta_Q = {_fmt_vn(st['dq'] + 5)}$.",
            ],
        )
        loigiai = (
            f"Sắp xếp mẫu số liệu: ${'; '.join(str(x) for x in sorted(data))}$.\n"
            f"Ta có $Q_1 = {_fmt_vn(st['q1'])}$, $Q_3 = {_fmt_vn(st['q3'])}$, $\\Delta_Q = {_fmt_vn(st['dq'])}$.\n"
            f"Vì ${outlier} > Q_3 + 1{{,}}5\\Delta_Q = {_fmt_vn(st['high_fence'])}$ nên ${outlier}$ là giá trị ngoại lệ."
        )
    return caudan, phuongan, loigiai


def k10_mc_c5_b14_tim_x_khoang_bien_thien():
    """Tìm giá trị x để mẫu số liệu có khoảng biến thiên R cho trước."""
    base = random.sample(range(145, 176), 7)
    mn, mx = min(base), max(base)
    span = mx - mn
    r_target = span + random.randint(4, 12)
    choice_side = random.choice(["high", "low"])
    if choice_side == "high":
        x_ans = mn + r_target
        distractors = [
            f"${x_ans - 5}$.",
            f"${x_ans + 5}$.",
            f"${mx + 2}$.",
            f"${x_ans + 10}$.",
            f"${x_ans - 10}$.",
        ]
    else:
        x_ans = mx - r_target
        distractors = [
            f"${x_ans - 5}$.",
            f"${x_ans + 5}$.",
            f"${mn - 2}$.",
            f"${x_ans + 10}$.",
            f"${x_ans - 10}$.",
        ]
    data_str = "\\quad ".join(str(v) for v in base) + "\\quad x"
    caudan = (
        f"Cho mẫu số liệu sau:\n$${data_str}$$\n"
        f"Khi đó $x$ nhận giá trị nào để mẫu số liệu này có khoảng biến thiên là ${r_target}$?"
    )
    phuongan = _make_mc_choices(f"${x_ans}$.", distractors)
    loigiai = (
        f"Trong $7$ số đã biết, giá trị nhỏ nhất là ${mn}$ và giá trị lớn nhất là ${mx}$ (hiệu là ${span} < {r_target}$).\n"
        f"Để khoảng biến thiên bằng ${r_target}$ thì {'$x = ' + str(mn) + ' + ' + str(r_target) + ' = ' + str(x_ans) + '$' if choice_side == 'high' else '$x = ' + str(mx) + ' - ' + str(r_target) + ' = ' + str(x_ans) + '$'}."
    )
    return caudan, phuongan, loigiai


def k10_mc_c5_b14_phuong_sai_phan_so():
    """Tính phương sai của mẫu số liệu dưới dạng phân số tối giản."""
    while True:
        data = [random.randint(2, 12) for _ in range(random.choice([7, 8, 9]))]
        mean_f = Fraction(sum(data), len(data))
        var_f = sum((Fraction(x) - mean_f) ** 2 for x in data) / len(data)
        if var_f.denominator > 1:
            break
    ans_tex = _frac_tex(var_f)
    w1 = _frac_tex(var_f + Fraction(1, var_f.denominator))
    w2 = _frac_tex(var_f + Fraction(2, var_f.denominator))
    w3 = _frac_tex(var_f * 2)
    row = " & ".join(str(x) for x in data)
    cols = "c|" * len(data)
    caudan = (
        f"Kết quả điều tra mức lương (đơn vị: triệu đồng) hàng tháng của một số công nhân nhà máy $A$ được ghi lại như sau:\n"
        f"\\begin{{center}}\\begin{{tabular}}{{|{cols}}}\\hline {row} \\\\ \\hline \\end{{tabular}}\\end{{center}}\n"
        f"Phương sai của mẫu số liệu đã cho bằng"
    )
    phuongan = _make_mc_choices(f"${ans_tex}$.", [f"${w1}$.", f"${w2}$.", f"${w3}$."])
    loigiai = (
        f"Số trung bình cộng là $\\bar{{x}} = {_frac_tex(mean_f)}$.\n"
        f"Phương sai của mẫu số liệu là $s^2 = \\dfrac{{1}}{{{len(data)}}}\\sum (x_i - \\bar{{x}})^2 = {ans_tex}$."
    )
    return caudan, phuongan, loigiai


def k10_mc_c5_b14_khoang_chua_do_lech_chuan():
    """Xác định khoảng chứa độ lệch chuẩn s của mẫu số liệu."""
    while True:
        data = [random.randint(76, 88) for _ in range(12)]
        st = _stats_summary(data)
        s = st["std"]
        # Chọn khoảng (a; b) độ rộng 0.5 chứa s nhưng không quá sát biên
        a = math.floor(s * 2) / 2.0
        b = a + 0.5
        if 0.05 < s - a < 0.45:
            break
    ans_tex = f"$\\left({_frac_tex(Fraction(a).limit_denominator())}; {_frac_tex(Fraction(b).limit_denominator())}\\right)$."
    w1 = f"$\\left({_frac_tex(Fraction(a - 1).limit_denominator())}; {_frac_tex(Fraction(b - 1).limit_denominator())}\\right)$."
    w2 = f"$\\left({_frac_tex(Fraction(b).limit_denominator())}; {_frac_tex(Fraction(b + 0.5).limit_denominator())}\\right)$."
    w3 = f"$\\left({_frac_tex(Fraction(b + 0.5).limit_denominator())}; {_frac_tex(Fraction(b + 1.0).limit_denominator())}\\right)$."
    row = " & ".join(str(x) for x in data)
    cols = "c|" * len(data)
    caudan = (
        f"Kiểm tra khối lượng một số quả măng cụt của lô hàng $B$ (đơn vị: gam) thu được bảng số liệu:\n"
        f"\\begin{{center}}\\begin{{tabular}}{{|l|{cols}}}\\hline Lô B & {row} \\\\ \\hline \\end{{tabular}}\\end{{center}}\n"
        f"Độ lệch chuẩn của khối lượng măng cụt ở lô $B$ thuộc khoảng nào?"
    )
    phuongan = _make_mc_choices(ans_tex, [w1, w2, w3])
    loigiai = (
        f"Ta có $\\bar{{x}} = {_fmt_vn(st['mean'], 3)}$, phương sai $s^2 \\approx {_fmt_vn(st['var'], 3)}$, "
        f"suy ra độ lệch chuẩn $s \\approx {_fmt_vn(s, 3)}$.\n"
        f"Vậy $s \\in {ans_tex}$"
    )
    return caudan, phuongan, loigiai


def k10_sa_c5_b14_phuong_sai_bieu_do_doan_thang():
    """TLN: Tính phương sai từ biểu đồ đoạn thẳng (TikZ) tốc độ tăng trưởng GDP."""
    years = list(range(2012, 2020))
    vals = [round(random.uniform(5.2, 7.3), 2) for _ in years]
    st = _stats_summary(vals)
    var_r = _round_half_up(st["var"], 2)

    tikz = [
        "\\begin{center}",
        "\\begin{tikzpicture}[xscale=0.95,yscale=1.4,>=stealth]",
        "\\draw[->] (0.5,5) -- (9.2,5) node[right] {\\scriptsize Năm};",
        "\\draw[->] (0.5,5) -- (0.5,7.8) node[above] {\\scriptsize Tốc độ tăng trưởng GDP (\\%)};",
    ]
    for ytick in [5.0, 5.5, 6.0, 6.5, 7.0, 7.5]:
        tikz.append(f"\\draw (0.42,{ytick}) -- (0.58,{ytick}) node[left=4pt] {{\\scriptsize {_fmt_vn(ytick, 1)}}};")
    pts = []
    for i, (yr, v) in enumerate(zip(years, vals), start=1):
        pts.append(f"({i},{v})")
        tikz.append(f"\\draw ({i},4.95) -- ({i},5.05) node[below=4pt] {{\\scriptsize {yr}}};")
        tikz.append(f"\\fill ({i},{v}) circle (1.8pt) node[above=2pt] {{\\scriptsize {_fmt_vn(v, 2)}}};")
    tikz.append(f"\\draw[thick] {' -- '.join(pts)};")
    tikz.append("\\end{tikzpicture}")
    tikz.append("\\end{center}")

    caudan = (
        "Biểu đồ đoạn thẳng ở hình bên dưới biểu diễn tốc độ tăng trưởng GDP của Việt Nam giai đoạn $2012 - 2019$.\n"
        + "\n".join(tikz)
        + "\nTính phương sai của mẫu số liệu đó (kết quả làm tròn đến hàng phần trăm)."
    )
    dapan = _fmt_vn(var_r, 2)
    loigiai = (
        f"Giá trị trung bình của mẫu số liệu là $\\bar{{x}} = {_fmt_vn(st['mean'], 4)}$.\n"
        f"Phương sai của mẫu số liệu là $s^2 = \\dfrac{{1}}{{8}}\\sum_{{i=1}}^8 (x_i - \\bar{{x}})^2 \\approx {_fmt_vn(var_r, 2)}$."
    )
    return caudan, dapan, loigiai


# ==============================================================================
# PHẦN 5: CHƯƠNG V - TRẮC NGHIỆM ĐÚNG/SAI (5 DẠNG BỔ SUNG)
# ==============================================================================

def k10_tf_c5_day_so_ngoai_le_va_tb_tv():
    """Đúng/Sai: Dãy số liệu rời rạc 24 ngày có 1 giá trị ngoại lệ (TB, TV, độ lệch, đếm)."""
    base = [random.randint(58, 98) for _ in range(23)]
    outlier = random.randint(230, 290)
    data = base + [outlier]
    random.shuffle(data)
    st = _stats_summary(data)

    mean_r = int(_round_half_up(st["mean"], 0))
    med = st["q2"]
    diff_true = round(abs(st["mean"] - med), 2)
    thresh = 90
    cnt_gt = sum(1 for x in data if x > thresh)

    rows = []
    for r_idx in range(3):
        rows.append(" & ".join(str(x) for x in data[r_idx * 8:(r_idx + 1) * 8]) + " \\\\ \\hline")
    table = "\\begin{center}\\begin{tabular}{|" + "c|" * 8 + "}\\hline\n" + "\n".join(rows) + "\n\\end{tabular}\\end{center}"

    a_ok = random.choice([True, False])
    a_val = mean_r if a_ok else mean_r + random.choice([-4, 5])
    b_ok = random.choice([True, False])
    b_val = med if b_ok else med + 2
    c_ok = random.choice([True, False])
    c_val = diff_true if c_ok else round(diff_true + 3.25, 2)
    d_ok = random.choice([True, False])
    d_val = cnt_gt if d_ok else cnt_gt + 2

    caudan = f"Thống kê số bao xi măng được bán ra tại một cửa hàng vật liệu xây dựng trong $24$ ngày cho kết quả như sau:\n{table}"
    choices = _make_tf_choices([
        (a_ok, f"Mỗi ngày cửa hàng bán trung bình ${a_val}$ bao (làm tròn đến hàng đơn vị)."),
        (b_ok, f"Số trung vị của mẫu số liệu là ${_fmt_vn(b_val)}$.",),
        (c_ok, f"Số trung bình và số trung vị lệch nhau ${_fmt_vn(c_val, 2)}$."),
        (d_ok, f"Có ${d_val}$ ngày cửa hàng đó bán được trên ${thresh}$ bao xi măng."),
    ])
    loigiai = (
        f"\\begin{{itemchoice}}\n"
        f"\\itemch {'Đúng' if a_ok else 'Sai'}. Số trung bình $\\bar{{x}} = {_fmt_vn(st['mean'], 2)} \\approx {mean_r}$.\n"
        f"\\itemch {'Đúng' if b_ok else 'Sai'}. Trung vị $M_e = {_fmt_vn(med)}$.\n"
        f"\\itemch {'Đúng' if c_ok else 'Sai'}. Độ lệch $|\\bar{{x}} - M_e| \\approx {_fmt_vn(diff_true, 2)}$.\n"
        f"\\itemch {'Đúng' if d_ok else 'Sai'}. Đếm các giá trị lớn hơn ${thresh}$ có ${cnt_gt}$ ngày.\n"
        f"\\end{{itemchoice}}"
    )
    return caudan, choices, loigiai


def k10_tf_c5_chieu_cao_10_ban_r_me_dq_s2():
    """Đúng/Sai: Mẫu số liệu 10 bạn (R, Me, Delta_Q, phương sai s^2)."""
    data = random.sample(range(155, 176), 10)
    st = _stats_summary(data)
    row = " & ".join(str(x) for x in data)
    table = "\\begin{center}\\begin{tabular}{|" + "c|" * 10 + "}\\hline " + row + " \\\\ \\hline \\end{tabular}\\end{center}"

    a_ok = random.choice([True, False])
    b_ok = random.choice([True, False])
    c_ok = random.choice([True, False])
    d_ok = random.choice([True, False])
    r_sh = st["r"] if a_ok else st["r"] + 2
    me_sh = st["q2"] if b_ok else st["q2"] + 1
    dq_sh = st["dq"] if c_ok else st["dq"] + 2
    var_r = _round_half_up(st["var"], 1)
    var_sh = var_r if d_ok else round(var_r + 2.4, 1)

    caudan = f"Mẫu số liệu sau cho biết chiều cao (đơn vị: cm) của các bạn trong một tổ:\n{table}"
    choices = _make_tf_choices([
        (a_ok, f"Khoảng biến thiên là $R = {r_sh}$."),
        (b_ok, f"Số trung vị là $M_e = {_fmt_vn(me_sh)}$."),
        (c_ok, f"Khoảng tứ phân vị là $\\Delta_Q = {_fmt_vn(dq_sh)}$."),
        (d_ok, f"Phương sai là $s^2 = {_fmt_vn(var_sh, 1)}$ (làm tròn đến hàng phần mười)."),
    ])
    loigiai = (
        f"\\begin{{itemchoice}}\n"
        f"\\itemch {'Đúng' if a_ok else 'Sai'}. $R = {max(data)} - {min(data)} = {st['r']}$.\n"
        f"\\itemch {'Đúng' if b_ok else 'Sai'}. $M_e = {_fmt_vn(st['q2'])}$.\n"
        f"\\itemch {'Đúng' if c_ok else 'Sai'}. $Q_1 = {_fmt_vn(st['q1'])}$, $Q_3 = {_fmt_vn(st['q3'])}$ $\\Rightarrow \\Delta_Q = {_fmt_vn(st['dq'])}$.\n"
        f"\\itemch {'Đúng' if d_ok else 'Sai'}. $\\bar{{x}} = {_fmt_vn(st['mean'], 2)}$, $s^2 \\approx {_fmt_vn(var_r, 1)}$.\n"
        f"\\end{{itemchoice}}"
    )
    return caudan, choices, loigiai


def k10_tf_c5_bang_tan_so_ngoai_le_mot_dq():
    """Đúng/Sai: Bảng tần số (giá trị ngoại lệ, TB làm tròn, mốt, Delta_Q)."""
    vals = [5, 6, 7, 8, 9, 10]
    freqs = [random.randint(6, 12), random.randint(8, 14), random.randint(6, 11), random.randint(13, 18), random.randint(5, 9), random.randint(3, 6)]
    data = []
    for v, f in zip(vals, freqs):
        data.extend([v] * f)
    st = _stats_summary(data)
    has_outlier = len(st["outliers"]) > 0
    mean_round = int(_round_half_up(st["mean"], 0))
    mode_val = st["modes"][0]

    a_ok = not has_outlier  # mệnh đề: "Mẫu số liệu không có giá trị ngoại lệ"
    b_ok = random.choice([True, False])
    c_ok = random.choice([True, False])
    d_ok = random.choice([True, False])

    mean_sh = mean_round if b_ok else mean_round + 2
    mode_sh = mode_val if c_ok else (mode_val - 1 if mode_val > 5 else mode_val + 1)
    dq_sh = st["dq"] if d_ok else st["dq"] + 1

    r1 = " & ".join(str(x) for x in vals)
    r2 = " & ".join(str(x) for x in freqs)
    table = (
        "\\begin{center}\\begin{tabular}{|l|c|c|c|c|c|c|}\\hline "
        f"Số lượng thiệp & {r1} \\\\ \\hline "
        f"Số lớp & {r2} \\\\ \\hline "
        "\\end{tabular}\\end{center}"
    )
    caudan = f"Số lượng thiệp xuân của các lớp làm được trong cuộc thi thiết kế được thống kê như sau:\n{table}"
    choices = _make_tf_choices([
        (a_ok, "Mẫu số liệu không có giá trị ngoại lệ."),
        (b_ok, f"Trung bình mỗi lớp làm được $\\bar{{x}} \\approx {mean_sh}$ thiệp (làm tròn đến hàng đơn vị)."),
        (c_ok, f"Mốt của mẫu số liệu $M_0 = {mode_sh}$."),
        (d_ok, f"Khoảng tứ phân vị của mẫu số liệu $\\Delta_Q = {_fmt_vn(dq_sh)}$."),
    ])
    loigiai = (
        f"\\begin{{itemchoice}}\n"
        f"\\itemch {'Đúng' if a_ok else 'Sai'}. $Q_1 = {_fmt_vn(st['q1'])}$, $Q_3 = {_fmt_vn(st['q3'])}$, $\\Delta_Q = {_fmt_vn(st['dq'])}$ nên khoảng bình thường $[{_fmt_vn(st['low_fence'])}; {_fmt_vn(st['high_fence'])}]$ "
        f"{'chứa toàn bộ mẫu' if a_ok else 'không chứa tất cả giá trị'}.\n"
        f"\\itemch {'Đúng' if b_ok else 'Sai'}. $\\bar{{x}} = {_fmt_vn(st['mean'], 2)} \\approx {mean_round}$.\n"
        f"\\itemch {'Đúng' if c_ok else 'Sai'}. Giá trị có tần số lớn nhất là $M_0 = {mode_val}$.\n"
        f"\\itemch {'Đúng' if d_ok else 'Sai'}. $\\Delta_Q = Q_3 - Q_1 = {_fmt_vn(st['dq'])}$.\n"
        f"\\end{{itemchoice}}"
    )
    return caudan, choices, loigiai


def k10_tf_c5_so_sanh_hai_mau_nam_nu_nha_may_bong_da():
    """Đúng/Sai: So sánh hai mẫu số liệu (TB, mốt, R, trung vị / ổn định qua độ lệch chuẩn)."""
    a_data = [random.randint(1, 6) for _ in range(12)]
    b_data = [random.randint(0, 8) for _ in range(12)]
    st_a = _stats_summary(a_data)
    st_b = _stats_summary(b_data)

    a_ok = random.choice([True, False])
    r_a_sh = st_a["r"] if a_ok else st_a["r"] + 2
    b_stable_a_more = st_b["std"] < st_a["std"]  # mệnh đề nói B ổn định hơn A
    c_means_diff = abs(st_a["mean"] - st_b["mean"]) > 1e-6
    d_ok = random.choice([True, False])
    s_a_r = _round_half_up(st_a["std"], 2)
    var_a_r = _round_half_up(st_a["var"], 3)
    s_sh = s_a_r if d_ok else round(s_a_r + 0.45, 2)
    var_sh = var_a_r if d_ok else round(var_a_r + 0.5, 3)

    row_a = " & ".join(str(x) for x in a_data)
    row_b = " & ".join(str(x) for x in b_data)
    cols = "c|" * 12
    table = (
        f"\\begin{{center}}\\begin{{tabular}}{{|l|{cols}}}\\hline "
        f"Đội Việt Nam & {row_a} \\\\ \\hline "
        f"Đội Thái Lan & {row_b} \\\\ \\hline "
        "\\end{tabular}\\end{center}"
    )
    caudan = (
        "Mẫu số liệu sau ghi rõ số bàn thắng của hai đội tuyển Việt Nam và Thái Lan trong $12$ trận thi đấu:\n"
        + table
    )
    choices = _make_tf_choices([
        (a_ok, f"Khoảng biến thiên của mẫu số liệu về số bàn thắng đội tuyển Việt Nam là $R = {r_a_sh}$."),
        (b_stable_a_more, "Khả năng ghi bàn của đội tuyển Thái Lan có tính ổn định hơn so với đội tuyển Việt Nam."),
        (c_means_diff, "Số bàn thắng trung bình của đội tuyển Việt Nam và đội tuyển Thái Lan là không bằng nhau."),
        (d_ok, f"Mẫu số liệu về số bàn thắng của đội tuyển Việt Nam có độ lệch chuẩn là ${_fmt_vn(s_sh, 2)}$ và phương sai là ${_fmt_vn(var_sh, 3)}$."),
    ])
    loigiai = (
        f"\\begin{{itemchoice}}\n"
        f"\\itemch {'Đúng' if a_ok else 'Sai'}. $R_{{VN}} = {max(a_data)} - {min(a_data)} = {st_a['r']}$.\n"
        f"\\itemch {'Đúng' if b_stable_a_more else 'Sai'}. Ta có $s_{{VN}} \\approx {_fmt_vn(s_a_r, 2)}$, $s_{{TL}} \\approx {_fmt_vn(st_b['std'], 2)}$.\n"
        f"\\itemch {'Đúng' if c_means_diff else 'Sai'}. $\\bar{{x}}_{{VN}} = {_fmt_vn(st_a['mean'], 2)}$, $\\bar{{x}}_{{TL}} = {_fmt_vn(st_b['mean'], 2)}$.\n"
        f"\\itemch {'Đúng' if d_ok else 'Sai'}. $s_{{VN}} \\approx {_fmt_vn(s_a_r, 2)}$, $s^2_{{VN}} \\approx {_fmt_vn(var_a_r, 3)}$.\n"
        f"\\end{{itemchoice}}"
    )
    return caudan, choices, loigiai


def k10_tf_c5_bieu_do_cot_chieu_cao_tu_phan_vi():
    """Đúng/Sai (TikZ): Biểu đồ cột chiều cao (nhóm 25% thấp nhất / Q1, TB, độ lệch chuẩn, R)."""
    heights = [150, 155, 160, 165, 170]
    counts = [
        random.randint(20, 35),
        random.randint(15, 25),
        random.randint(80, 110),
        random.randint(35, 50),
        random.randint(10, 20),
    ]
    data = []
    for h, c in zip(heights, counts):
        data.extend([h] * c)
    st = _stats_summary(data)
    total_n = len(data)
    q1 = st["q1"]
    h_test = 155
    a_ok = (h_test <= q1)
    mean_r = _round_half_up(st["mean"], 1)
    std_r = _round_half_up(st["std"], 3)

    b_ok = random.choice([True, False])
    c_ok = random.choice([True, False])
    d_ok = random.choice([True, False])
    mean_sh = mean_r if b_ok else round(mean_r + 1.5, 1)
    std_sh = std_r if c_ok else round(std_r + 0.5, 3)
    r_sh = st["r"] if d_ok else st["r"] - 10

    tikz = [
        "\\begin{center}",
        "\\begin{tikzpicture}[scale=0.85,>=stealth]",
        "\\draw[->] (0,0) -- (6.5,0) node[right] {\\scriptsize chiều cao (cm)};",
        "\\draw[->] (0,0) -- (0,3.6) node[above] {\\scriptsize tần số};",
    ]
    for i, (h, c) in enumerate(zip(heights, counts), start=1):
        bh = round(c / 35.0, 2)
        tikz.append(f"\\filldraw[fill=gray!35,draw=black] ({i-0.2},0) rectangle ({i+0.2},{bh});")
        tikz.append(f"\\node[above] at ({i},{bh}) {{\\scriptsize {c}}};")
        tikz.append(f"\\node[below] at ({i},0) {{\\scriptsize {h}}};")
    tikz.append("\\end{tikzpicture}")
    tikz.append("\\end{center}")

    caudan = "Cho biểu đồ chiều cao đầu năm học của một nhóm học sinh lớp 10 như hình vẽ:\n" + "\n".join(tikz)
    choices = _make_tf_choices([
        (a_ok, f"Trong số các học sinh trên, bạn $A$ cao ${h_test}$ cm thuộc nhóm $25\\%$ học sinh có chiều cao thấp nhất."),
        (b_ok, f"Số trung bình cộng của mẫu số liệu là $\\bar{{x}} = {_fmt_vn(mean_sh, 1)}$ (làm tròn đến hàng phần mười)."),
        (c_ok, f"Độ lệch chuẩn của mẫu số liệu là $s = {_fmt_vn(std_sh, 3)}$ (làm tròn đến hàng phần nghìn)."),
        (d_ok, f"Khoảng biến thiên của mẫu số liệu là $R = {r_sh}$."),
    ])
    loigiai = (
        f"\\begin{{itemchoice}}\n"
        f"\\itemch {'Đúng' if a_ok else 'Sai'}. Cỡ mẫu $n = {total_n}$, tứ phân vị thứ nhất $Q_1 = {_fmt_vn(q1)}$.\n"
        f"\\itemch {'Đúng' if b_ok else 'Sai'}. $\\bar{{x}} \\approx {_fmt_vn(mean_r, 1)}$.\n"
        f"\\itemch {'Đúng' if c_ok else 'Sai'}. $s \\approx {_fmt_vn(std_r, 3)}$.\n"
        f"\\itemch {'Đúng' if d_ok else 'Sai'}. $R = 170 - 150 = {st['r']}$.\n"
        f"\\end{{itemchoice}}"
    )
    return caudan, choices, loigiai


def k10_tf_c5_thu_nhap_bat_bien_do_lech_chuan():
    """Đúng/Sai: Bảng thu nhập 6 vùng kinh tế (min, TB, R, tính bất biến của độ lệch chuẩn khi cộng hằng số)."""
    regions = [
        "Đồng bằng sông Hồng",
        "Trung du và miền núi phía Bắc",
        "Bắc Trung Bộ và Duyên hải miền Trung",
        "Tây Nguyên",
        "Đông Nam Bộ",
        "Đồng bằng sông Cửu Long",
    ]
    vals = [round(random.uniform(3.2, 6.8), 1) for _ in range(6)]
    # Đảm bảo min là duy nhất
    min_val = min(vals)
    min_idx = vals.index(min_val)
    min_region = regions[min_idx]
    wrong_region = regions[(min_idx + 1) % 6]

    st = _stats_summary(vals)
    mean_r = _round_half_up(st["mean"], 2)
    r_val = round(st["r"], 1)
    shift = random.choice([1, 2])

    a_ok = random.choice([True, False])
    reg_shown = min_region if a_ok else wrong_region
    b_ok = random.choice([True, False])
    mean_sh = mean_r if b_ok else round(mean_r + 0.5, 2)
    c_ok = random.choice([True, False])
    r_sh = r_val if c_ok else round(r_val + 0.6, 1)
    d_ok = True  # Tính chất bất biến khi cộng cùng hằng số

    rows = "\n".join(f"{reg} & ${_fmt_vn(v, 1)}$ \\\\ \\hline" for reg, v in zip(regions, vals))
    table = (
        "\\begin{center}\\begin{tabular}{|l|c|}\\hline\n"
        "Vùng kinh tế - xã hội & Thu nhập (triệu đồng) \\\\ \\hline\n"
        f"{rows}\n\\end{{tabular}}\\end{{center}}"
    )
    caudan = f"Số liệu thu nhập bình quân đầu người một tháng (đơn vị: triệu đồng) của $6$ vùng kinh tế - xã hội được cho trong bảng sau:\n{table}"
    choices = _make_tf_choices([
        (a_ok, f"Vùng kinh tế {reg_shown} có mức thu nhập bình quân thấp nhất trong $6$ vùng."),
        (b_ok, f"Thu nhập trung bình của các vùng là ${_fmt_vn(mean_sh, 2)}$ triệu đồng/tháng."),
        (c_ok, f"Khoảng biến thiên của mẫu số liệu thu nhập giữa các vùng là ${_fmt_vn(r_sh, 1)}$ triệu đồng."),
        (d_ok, f"Nếu tất cả các vùng đều có thu nhập tăng thêm ${shift}$ triệu đồng/tháng thì độ lệch chuẩn của mẫu số liệu mới không thay đổi so với số liệu ban đầu."),
    ])
    loigiai = (
        f"\\begin{{itemchoice}}\n"
        f"\\itemch {'Đúng' if a_ok else 'Sai'}. Vùng có mức thu nhập thấp nhất là {min_region} (${_fmt_vn(min_val, 1)}$ triệu đồng).\n"
        f"\\itemch {'Đúng' if b_ok else 'Sai'}. $\\bar{{x}} = {_fmt_vn(mean_r, 2)}$ triệu đồng.\n"
        f"\\itemch {'Đúng' if c_ok else 'Sai'}. $R = {_fmt_vn(max(vals), 1)} - {_fmt_vn(min_val, 1)} = {_fmt_vn(r_val, 1)}$.\n"
        f"\\itemch Đúng. Khi cộng tất cả các giá trị với cùng một hằng số ${shift}$ thì hiệu $x_i - \\bar{{x}}$ không đổi nên độ lệch chuẩn không đổi.\n"
        f"\\end{{itemchoice}}"
    )
    return caudan, choices, loigiai
