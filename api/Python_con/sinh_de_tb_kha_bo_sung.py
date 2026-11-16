"""Ngân hàng câu hỏi bổ sung mức Trung bình - Khá cho các phần còn thiếu của Lớp 10 & Lớp 11:
Lớp 10:
- Chương I (TLN & Đúng/Sai): Mệnh đề, Tập hợp, Biểu đồ Ven, Tham số nguyên
- Chương II (TLN): Đếm nghiệm nguyên BPT, GTLN/GTNN trên miền đa giác, Bài toán thực tế lợi nhuận
- Chương V Bài 12 & Chương VI Bài 17 (Đúng/Sai): Số gần đúng & Dấu tam thức bậc hai
- Chương VIII (TLN & Đúng/Sai): Quy tắc đếm, Tổ hợp - Chỉnh hợp - Hoán vị, Nhị thức Newton
- Chương IX (TLN & Đúng/Sai): Xác suất cổ điển

Lớp 11:
- Chương I Bài 3 (MC & TLN): Tập xác định, chẵn/lẻ, chu kì, GTLN/GTNN hàm số lượng giác
- Chương III Bài 8 (TLN): Mẫu số liệu ghép nhóm (cỡ mẫu, giá trị đại diện)
- Chương IV (MC & TLN): Quan hệ song song trong không gian (giao tuyến, song song, Thales, phép chiếu)
- Chương VII (MC): Quan hệ vuông góc (góc hai đường thẳng, đường vuông góc mặt phẳng, khoảng cách cơ bản)
- Chương VIII (TLN): Công thức cộng xác suất & Biến cố độc lập
"""

import math
import random
from fractions import Fraction


def _fmt_vn(val, decimals=2):
    if isinstance(val, int):
        return str(val)
    if abs(val - round(val)) < 1e-9:
        return str(int(round(val)))
    return f"{val:.{decimals}f}".rstrip("0").rstrip(".").replace(".", ",")


def _round_half_up(val, ndigits=0):
    factor = 10 ** ndigits
    if val >= 0:
        return math.floor(val * factor + 0.5 + 1e-12) / factor
    return -math.floor(-val * factor + 0.5 + 1e-12) / factor


def _make_mc_choices(correct_str, distractors):
    seen = {correct_str}
    pool = []
    for d in distractors:
        if d not in seen:
            seen.add(d)
            pool.append(d)
    if len(pool) < 3:
        raise ValueError(f"Thiếu phương án nhiễu phân biệt cho: {correct_str}")
    items = [(True, correct_str)] + [(False, x) for x in pool[:3]]
    random.shuffle(items)
    return [f"{'{\\True ' if ok else '{'}{txt}}}\n" for ok, txt in items]


def _make_tf_choices(statements):
    return [f"{'{\\True ' if ok else '{'}{txt}}}\n" for ok, txt in statements]


# ==============================================================================
# LỚP 10 - CHƯƠNG I: MỆNH ĐỀ VÀ TẬP HỢP (TLN & ĐÚNG/SAI)
# ==============================================================================

def tbk_k10_sa_c1_dem_tap_con_giao_hop():
    """TLN: Đếm số phần tử của A hợp B, A giao B, A \\ B hoặc số tập con."""
    mode = random.choice(["union", "inter_diff", "subsets"])
    u = list(range(1, 10))
    a = sorted(random.sample(u, random.randint(4, 5)))
    b = sorted(random.sample(u, random.randint(4, 5)))
    set_a, set_b = set(a), set(b)
    a_tex = "\\{" + "; ".join(str(x) for x in a) + "\\}"
    b_tex = "\\{" + "; ".join(str(x) for x in b) + "\\}"

    if mode == "union":
        ans = len(set_a | set_b)
        caudan = f"Cho hai tập hợp $A = {a_tex}$ và $B = {b_tex}$. Tập hợp $A \\cup B$ có bao nhiêu phần tử?"
        loigiai = f"Ta có $A \\cup B = \\{{{'; '.join(str(x) for x in sorted(set_a | set_b))}\\}}$ nên có ${ans}$ phần tử."
    elif mode == "inter_diff":
        ans = len(set_a - set_b)
        caudan = f"Cho hai tập hợp $A = {a_tex}$ và $B = {b_tex}$. Tập hợp $A \\setminus B$ có bao nhiêu phần tử?"
        loigiai = f"Ta có $A \\setminus B = \\{{{'; '.join(str(x) for x in sorted(set_a - set_b))}\\}}$ nên có ${ans}$ phần tử."
    else:
        n = len(a)
        ans = (1 << n)
        caudan = f"Cho tập hợp $A = {a_tex}$. Tập hợp $A$ có tất cả bao nhiêu tập con?"
        loigiai = f"Tập hợp $A$ có ${n}$ phần tử nên số tập con của $A$ là $2^{{{n}}} = {ans}$."
    return caudan, str(ans), loigiai


def tbk_k10_sa_c1_venn_thuc_te_hai_tap():
    """TLN: Bài toán thực tế hai tập hợp (biểu đồ Ven)."""
    n_both = random.randint(6, 15)
    only_math = random.randint(10, 18)
    only_lit = random.randint(8, 16)
    none_cnt = random.randint(3, 8)
    n_math = only_math + n_both
    n_lit = only_lit + n_both
    total = only_math + only_lit + n_both + none_cnt

    if random.choice([True, False]):
        caudan = (
            f"Lớp 10A có ${total}$ học sinh, trong đó có ${n_math}$ học sinh thích môn Toán, "
            f"${n_lit}$ học sinh thích môn Ngữ văn và ${none_cnt}$ học sinh không thích môn nào trong hai môn trên. "
            f"Hỏi có bao nhiêu học sinh thích cả hai môn Toán và Ngữ văn?"
        )
        ans = n_both
        loigiai = (
            f"Số học sinh thích ít nhất một trong hai môn là ${total} - {none_cnt} = {total - none_cnt}$.\n"
            f"Số học sinh thích cả hai môn là ${n_math} + {n_lit} - {total - none_cnt} = {ans}$."
        )
    else:
        caudan = (
            f"Một nhóm có ${total}$ học sinh, trong đó có ${n_math}$ bạn biết chơi bóng đá, "
            f"${n_lit}$ bạn biết bơi lội và ${n_both}$ bạn biết cả hai môn. "
            f"Hỏi có bao nhiêu học sinh không biết môn nào trong hai môn trên?"
        )
        ans = none_cnt
        loigiai = (
            f"Số học sinh biết ít nhất một môn là ${n_math} + {n_lit} - {n_both} = {total - none_cnt}$.\n"
            f"Số học sinh không biết môn nào là ${total} - {total - none_cnt} = {ans}$."
        )
    return caudan, str(ans), loigiai


def tbk_k10_sa_c1_tham_so_nguyen_tap_hop():
    """TLN: Đếm số giá trị nguyên của m để A là tập con của B."""
    b_left = random.randint(-6, -2)
    b_right = random.randint(6, 10)
    span = random.randint(2, 4)
    # A = [m; m + span], B = [b_left; b_right] => b_left <= m <= b_right - span
    ans = (b_right - span) - b_left + 1
    caudan = (
        f"Cho hai tập hợp $A = [m; m + {span}]$ và $B = [{b_left}; {b_right}]$. "
        f"Có bao nhiêu giá trị nguyên của tham số $m$ để $A \\subset B$?"
    )
    loigiai = (
        f"Để $A \\subset B$ thì $\\begin{{cases}} m \\ge {b_left} \\\\ m + {span} \\le {b_right} \\end{{cases}} "
        f"\\Leftrightarrow {b_left} \\le m \\le {b_right - span}$.\n"
        f"Vì $m \\in \\mathbb{{Z}}$ nên có ${b_right - span} - ({b_left}) + 1 = {ans}$ giá trị."
    )
    return caudan, str(ans), loigiai


def tbk_k10_tf_c1_menh_de_phu_dinh_keo_theo():
    """Đúng/Sai: Mệnh đề chứa biến, phủ định, kéo theo và điều kiện cần/đủ."""
    k = random.choice([2, 3, 4])
    x0 = random.randint(2, 5)
    p_x0 = x0 * x0 > k * x0
    a_ok = p_x0

    b_ok = random.choice([True, False])
    c_ok = random.choice([True, False])
    d_ok = random.choice([True, False])

    b_txt = (
        "Phủ định của mệnh đề \"$\\forall x \\in \\mathbb{R},\\; x^2 + 1 > 0$\" là \"$\\exists x \\in \\mathbb{R},\\; x^2 + 1 \\le 0$\"."
        if b_ok
        else "Phủ định của mệnh đề \"$\\forall x \\in \\mathbb{R},\\; x^2 + 1 > 0$\" là \"$\\forall x \\in \\mathbb{R},\\; x^2 + 1 \\le 0$\"."
    )
    c_txt = (
        "Mệnh đề \"$\\exists n \\in \\mathbb{N},\\; n^2 = n$\" là mệnh đề đúng."
        if c_ok
        else "Mệnh đề \"$\\forall n \\in \\mathbb{N},\\; n^2 > n$\" là mệnh đề đúng."
    )
    d_txt = (
        "Mệnh đề \"Nếu một số nguyên chia hết cho $6$ thì chia hết cho $3$\" là mệnh đề đúng."
        if d_ok
        else "Mệnh đề \"Nếu một số nguyên chia hết cho $3$ thì chia hết cho $6$\" là mệnh đề đúng."
    )

    caudan = f"Xét tính đúng sai của các mệnh đề sau (cho mệnh đề chứa biến $P(x):\\; \"x^2 > {k}x\"$):"
    choices = _make_tf_choices([
        (a_ok, f"$P({x0})$ là mệnh đề đúng."),
        (b_ok, b_txt),
        (c_ok, c_txt),
        (d_ok, d_txt),
    ])
    loigiai = (
        f"\\begin{{itemchoice}}\n"
        f"\\itemch {'Đúng' if a_ok else 'Sai'}. Với $x = {x0}$ ta có ${x0}^2 = {x0*x0}$ và ${k}\\cdot{x0} = {k*x0}$.\n"
        f"\\itemch {'Đúng' if b_ok else 'Sai'}. Phủ định của $\\forall$ là $\\exists$ và phủ định của $>$ là $\\le$.\n"
        f"\\itemch {'Đúng' if c_ok else 'Sai'}. Với $n = 0$ (hoặc $n = 1$) ta có $n^2 = n$.\n"
        f"\\itemch {'Đúng' if d_ok else 'Sai'}. Chia hết cho $6$ thì luôn chia hết cho $3$, chiều ngược lại sai (ví dụ số $3$).\n"
        f"\\end{{itemchoice}}"
    )
    return caudan, choices, loigiai


def tbk_k10_tf_c1_phep_toan_tap_hop():
    """Đúng/Sai: Phép toán trên hai tập hợp số (giao, hợp, hiệu, số tập con)."""
    a = sorted(random.sample(range(0, 8), 4))
    b = sorted(random.sample(range(2, 10), 4))
    sa, sb = set(a), set(b)
    inter = sorted(sa & sb)
    union = sorted(sa | sb)
    diff = sorted(sa - sb)

    a_ok = random.choice([True, False])
    b_ok = random.choice([True, False])
    c_ok = random.choice([True, False])
    d_ok = random.choice([True, False])

    cnt_inter = len(inter) if a_ok else len(inter) + 1
    cnt_union = len(union) if b_ok else len(union) - 1
    cnt_diff = len(diff) if c_ok else len(diff) + 2
    sub_a = 16 if d_ok else 8

    a_tex = "\\{" + "; ".join(str(x) for x in a) + "\\}"
    b_tex = "\\{" + "; ".join(str(x) for x in b) + "\\}"
    caudan = f"Cho hai tập hợp $A = {a_tex}$ và $B = {b_tex}$."
    choices = _make_tf_choices([
        (a_ok, f"Tập hợp $A \\cap B$ có đúng ${cnt_inter}$ phần tử."),
        (b_ok, f"Tập hợp $A \\cup B$ có đúng ${cnt_union}$ phần tử."),
        (c_ok, f"Tập hợp $A \\setminus B$ có đúng ${cnt_diff}$ phần tử."),
        (d_ok, f"Tập hợp $A$ có tất cả ${sub_a}$ tập con."),
    ])
    loigiai = (
        f"\\begin{{itemchoice}}\n"
        f"\\itemch {'Đúng' if a_ok else 'Sai'}. $A \\cap B$ có ${len(inter)}$ phần tử.\n"
        f"\\itemch {'Đúng' if b_ok else 'Sai'}. $A \\cup B$ có ${len(union)}$ phần tử.\n"
        f"\\itemch {'Đúng' if c_ok else 'Sai'}. $A \\setminus B$ có ${len(diff)}$ phần tử.\n"
        f"\\itemch {'Đúng' if d_ok else 'Sai'}. $A$ có $4$ phần tử nên có $2^4 = 16$ tập con.\n"
        f"\\end{{itemchoice}}"
    )
    return caudan, choices, loigiai


# ==============================================================================
# LỚP 10 - CHƯƠNG II: BPT & HỆ BPT BẬC NHẤT HAI ẨN (TLN)
# ==============================================================================

def tbk_k10_sa_c2_dem_nghiem_nguyen_bpt():
    """TLN: Đếm số cặp số nguyên dương (x; y) thỏa mãn ax + by <= c."""
    a = random.choice([2, 3, 4])
    b = random.choice([2, 3, 5])
    c = random.randint(10, 18)
    pts = [(x, y) for x in range(1, c + 1) for y in range(1, c + 1) if a * x + b * y <= c]
    ans = len(pts)
    caudan = f"Có bao nhiêu cặp số nguyên dương $(x; y)$ thỏa mãn bất phương trình ${a}x + {b}y \\le {c}$?"
    loigiai = (
        f"Liệt kê theo $x \\in \\mathbb{{N}}^*$ với $y \\ge 1$ sao cho ${a}x + {b}y \\le {c}$, "
        f"ta đếm được tất cả ${ans}$ cặp $(x; y)$ thỏa mãn."
    )
    return caudan, str(ans), loigiai


def tbk_k10_sa_c2_gtln_gtnn_mien_tam_giac():
    """TLN: Tìm GTLN của F(x; y) = px + qy trên miền hệ BPT x >= 0, y >= 0, ax + by <= c."""
    a = random.choice([1, 2])
    b = random.choice([1, 2, 3])
    k = random.randint(3, 6)
    c = a * b * k  # Để giao điểm trục tọa độ đều nguyên: (c/a, 0) và (0, c/b)
    p = random.randint(2, 6)
    q = random.randint(2, 6)
    vertices = [(0, 0), (c // a, 0), (0, c // b)]
    vals = [p * x + q * y for x, y in vertices]
    ans = max(vals)
    caudan = (
        f"Tìm giá trị lớn nhất của biểu thức $F(x; y) = {p}x + {q}y$ trên miền nghiệm của hệ bất phương trình:\n"
        f"$$\\begin{{cases}} x \\ge 0 \\\\ y \\ge 0 \\\\ {'' if a == 1 else a}x + {'' if b == 1 else b}y \\le {c} \\end{{cases}}$$"
    )
    loigiai = (
        f"Miền nghiệm là miền tam giác $OAB$ với các đỉnh $O(0; 0)$, $A({c // a}; 0)$, $B(0; {c // b})$.\n"
        f"Tại các đỉnh: $F(0; 0) = 0$, $F({c // a}; 0) = {p * (c // a)}$, $F(0; {c // b}) = {q * (c // b)}$.\n"
        f"Vậy giá trị lớn nhất là ${ans}$."
    )
    return caudan, str(ans), loigiai


def tbk_k10_sa_c2_toan_thuc_te_loi_nhuan():
    """TLN: Bài toán thực tế lập hệ BPT đơn giản tìm lợi nhuận tối đa (nghìn đồng/triệu đồng)."""
    x_max = random.randint(4, 7)
    y_max = random.randint(4, 7)
    tot_max = x_max + y_max - random.randint(2, 3)
    p1 = random.choice([3, 4, 5])
    p2 = random.choice([4, 5, 6])
    # Miền: 0 <= x <= x_max, 0 <= y <= y_max, x + y <= tot_max
    # Đỉnh có lợi nhuận cao nhất nằm ở (x_max, tot_max - x_max) hoặc (tot_max - y_max, y_max)
    cands = [
        (0, 0),
        (x_max, 0),
        (0, y_max),
        (x_max, tot_max - x_max),
        (tot_max - y_max, y_max),
    ]
    ans = max(p1 * x + p2 * y for x, y in cands)
    caudan = (
        f"Một xưởng sản xuất hai loại sản phẩm A và B. Mỗi ngày xưởng sản xuất được tối đa ${x_max}$ sản phẩm A, "
        f"tối đa ${y_max}$ sản phẩm B và tổng số sản phẩm cả hai loại không vượt quá ${tot_max}$. "
        f"Biết mỗi sản phẩm A lãi ${p1}$ triệu đồng, mỗi sản phẩm B lãi ${p2}$ triệu đồng. "
        f"Lợi nhuận cao nhất mỗi ngày xưởng có thể thu được là bao nhiêu triệu đồng?"
    )
    loigiai = (
        f"Gọi $x, y$ lần lượt là số sản phẩm A và B ($0 \\le x \\le {x_max}$, $0 \\le y \\le {y_max}$, $x + y \\le {tot_max}$).\n"
        f"Hàm lợi nhuận $L = {p1}x + {p2}y$ đạt giá trị lớn nhất tại một trong các đỉnh của miền đa giác nghiệm.\n"
        f"Tính tại các đỉnh ta được $L_{{\\max}} = {ans}$ (triệu đồng)."
    )
    return caudan, str(ans), loigiai


# ==============================================================================
# LỚP 10 - CHƯƠNG V BÀI 12 & CHƯƠNG VI BÀI 17 (ĐÚNG/SAI CÒN THIẾU)
# ==============================================================================

def tbk_k10_tf_c5_b12_so_gan_dung_sai_so():
    """Đúng/Sai: Số gần đúng, sai số tuyệt đối, sai số tương đối và số quy tròn."""
    a_true = random.choice([125.4, 248.6, 312.5, 456.8])
    d = 0.2
    rel_max = round((d / a_true) * 100.0, 2)
    rounded_unit = int(_round_half_up(a_true, 0))

    a_ok = random.choice([True, False])
    b_ok = random.choice([True, False])
    c_ok = random.choice([True, False])
    d_ok = random.choice([True, False])

    round_sh = rounded_unit if a_ok else rounded_unit + 1
    rel_sh = rel_max if b_ok else round(rel_max + 0.5, 2)
    a_low = round(a_true - d, 1)
    a_high = round(a_true + d, 1)
    interval_txt = (
        f"Giá trị đúng $\\bar{{l}}$ nằm trong đoạn $[{_fmt_vn(a_low, 1)}; {_fmt_vn(a_high, 1)}]$."
        if c_ok
        else f"Giá trị đúng $\\bar{{l}}$ nằm trong đoạn $[{_fmt_vn(a_low - 1, 1)}; {_fmt_vn(a_high - 1, 1)}]$."
    )
    d_txt = (
        "Độ chính xác của phép đo là $d = 0{,}2$ m."
        if d_ok
        else "Sai số tuyệt đối của phép đo chắc chắn bằng đúng $0{,}2$ m."
    )

    caudan = f"Kết quả đo chiều dài một đoạn đường được ghi là $l = {_fmt_vn(a_true, 1)}\\text{{ m}} \\pm 0{{,}}2\\text{{ m}}$."
    choices = _make_tf_choices([
        (a_ok, f"Số quy tròn của số gần đúng ${_fmt_vn(a_true, 1)}$ với độ chính xác $d = 0{{,}}2$ là ${round_sh}$."),
        (b_ok, f"Sai số tương đối của phép đo không vượt quá ${_fmt_vn(rel_sh, 2)}\\%$."),
        (c_ok, interval_txt),
        (d_ok, d_txt),
    ])
    loigiai = (
        f"\\begin{{itemchoice}}\n"
        f"\\itemch {'Đúng' if a_ok else 'Sai'}. Vì $d = 0{{,}}2$ ở hàng phần chục nên quy tròn đến hàng đơn vị được ${rounded_unit}$.\n"
        f"\\itemch {'Đúng' if b_ok else 'Sai'}. $\\delta \\le \\dfrac{{0{{,}}2}}{{{_fmt_vn(a_true, 1)}}} \\approx {_fmt_vn(rel_max, 2)}\\%$.\n"
        f"\\itemch {'Đúng' if c_ok else 'Sai'}. $\\bar{{l}} \\in [a - d; a + d] = [{_fmt_vn(a_low, 1)}; {_fmt_vn(a_high, 1)}]$.\n"
        f"\\itemch {'Đúng' if d_ok else 'Sai'}. Độ chính xác là $d = 0{{,}}2$ m (còn $|\\bar{{l}} - l| \\le 0{{,}}2$, không nhất thiết bằng $0{{,}}2$).\n"
        f"\\end{{itemchoice}}"
    )
    return caudan, choices, loigiai


def tbk_k10_tf_c6_b17_tam_thuc_bac_hai():
    """Đúng/Sai: Dấu tam thức bậc hai và bất phương trình bậc hai."""
    r1, r2 = sorted(random.sample([-3, -2, -1, 1, 2, 3, 4], 2))
    # f(x) = x^2 - (r1 + r2)x + r1*r2
    b_coef = -(r1 + r2)
    c_coef = r1 * r2
    delta = (r1 - r2) ** 2

    def _fx_tex():
        sb = f"{b_coef:+}x".replace("+1x", "+x").replace("-1x", "-x")
        if b_coef == 0:
            sb = ""
        sc = f"{c_coef:+}" if c_coef != 0 else ""
        return f"x^2 {sb} {sc}".strip()

    a_ok = random.choice([True, False])
    b_ok = random.choice([True, False])
    c_ok = random.choice([True, False])
    d_ok = random.choice([True, False])

    delta_sh = delta if a_ok else delta + 4
    b_txt = (
        f"$f(x) < 0$ khi và chỉ khi $x \\in ({r1}; {r2})$."
        if b_ok
        else f"$f(x) < 0$ khi và chỉ khi $x \\in (-\\infty; {r1}) \\cup ({r2}; +\\infty)$."
    )
    c_txt = (
        f"Tập nghiệm của bất phương trình $f(x) \\ge 0$ là $(-\\infty; {r1}] \\cup [{r2}; +\\infty)$."
        if c_ok
        else f"Tập nghiệm của bất phương trình $f(x) \\ge 0$ là $[{r1}; {r2}]$."
    )
    # m để x^2 - 2x + m > 0 với mọi x in R <=> m > 1
    m_bound = 1 if d_ok else 0
    d_txt = f"Bất phương trình $x^2 - 2x + m > 0$ nghiệm đúng với mọi $x \\in \\mathbb{{R}}$ khi và chỉ khi $m > {m_bound}$."

    caudan = f"Cho tam thức bậc hai $f(x) = {_fx_tex()}$."
    choices = _make_tf_choices([
        (a_ok, f"Biệt thức của tam thức $f(x)$ là $\\Delta = {delta_sh}$."),
        (b_ok, b_txt),
        (c_ok, c_txt),
        (d_ok, d_txt),
    ])
    loigiai = (
        f"\\begin{{itemchoice}}\n"
        f"\\itemch {'Đúng' if a_ok else 'Sai'}. $\\Delta = ({b_coef})^2 - 4\\cdot 1\\cdot({c_coef}) = {delta}$.\n"
        f"\\itemch {'Đúng' if b_ok else 'Sai'}. $f(x)$ có hai nghiệm ${r1}, {r2}$ và hệ số $a = 1 > 0$ nên $f(x) < 0 \\Leftrightarrow x \\in ({r1}; {r2})$.\n"
        f"\\itemch {'Đúng' if c_ok else 'Sai'}. $f(x) \\ge 0 \\Leftrightarrow x \\in (-\\infty; {r1}] \\cup [{r2}; +\\infty)$.\n"
        f"\\itemch {'Đúng' if d_ok else 'Sai'}. Điều kiện là $\\Delta' = 1 - m < 0 \\Leftrightarrow m > 1$.\n"
        f"\\end{{itemchoice}}"
    )
    return caudan, choices, loigiai


# ==============================================================================
# LỚP 10 - CHƯƠNG VIII: ĐẠI SỐ TỔ HỢP (TLN & ĐÚNG/SAI)
# ==============================================================================

def tbk_k10_sa_c8_quy_tac_dem_lap_so():
    """TLN: Đếm số tự nhiên có 3 chữ số đôi một khác nhau (hoặc chẵn) từ tập chữ số."""
    digits = sorted(random.sample([1, 2, 3, 4, 5, 6, 7, 8], 6))
    d_tex = "\\{" + "; ".join(str(x) for x in digits) + "\\}"
    mode = random.choice(["all3", "even3"])
    if mode == "all3":
        ans = 6 * 5 * 4
        caudan = f"Từ tập hợp $A = {d_tex}$, có thể lập được bao nhiêu số tự nhiên có $3$ chữ số đôi một khác nhau?"
        loigiai = f"Số các số lập được là chỉnh hợp chập $3$ của $6$: $A_6^3 = 6 \\cdot 5 \\cdot 4 = {ans}$."
    else:
        evens = [x for x in digits if x % 2 == 0]
        ans = len(evens) * 5 * 4
        caudan = f"Từ tập hợp $A = {d_tex}$, có thể lập được bao nhiêu số tự nhiên chẵn có $3$ chữ số đôi một khác nhau?"
        loigiai = (
            f"Trong $A$ có ${len(evens)}$ chữ số chẵn nên hàng đơn vị có ${len(evens)}$ cách chọn.\n"
            f"Hai chữ số còn lại có $A_5^2 = 20$ cách chọn. Vậy có ${len(evens)} \\cdot 20 = {ans}$ số."
        )
    return caudan, str(ans), loigiai


def tbk_k10_sa_c8_chon_nhom_to_hop():
    """TLN: Chọn nhóm học sinh (tổ hợp cơ bản)."""
    boys = random.randint(5, 8)
    girls = random.randint(4, 7)
    k_b = random.choice([2, 3])
    k_g = random.choice([1, 2])
    ans = math.comb(boys, k_b) * math.comb(girls, k_g)
    caudan = (
        f"Một tổ có ${boys}$ học sinh nam và ${girls}$ học sinh nữ. "
        f"Hỏi có bao nhiêu cách chọn một nhóm gồm ${k_b}$ học sinh nam và ${k_g}$ học sinh nữ đi trực nhật?"
    )
    loigiai = f"Số cách chọn là $C_{{{boys}}}^{{{k_b}}} \\cdot C_{{{girls}}}^{{{k_g}}} = {math.comb(boys, k_b)} \\cdot {math.comb(girls, k_g)} = {ans}$."
    return caudan, str(ans), loigiai


def tbk_k10_sa_c8_dem_hinh_tam_giac_doan_thang():
    """TLN: Đếm số tam giác hoặc vectơ lập từ n điểm (không thẳng hàng hoặc có 1 nhóm thẳng hàng)."""
    n = random.randint(8, 12)
    if random.choice([True, False]):
        ans = math.comb(n, 3)
        caudan = f"Cho ${n}$ điểm phân biệt trong mặt phẳng sao cho không có $3$ điểm nào thẳng hàng. Hỏi tạo được bao nhiêu tam giác có đỉnh là $3$ điểm trong ${n}$ điểm đó?"
        loigiai = f"Mỗi tam giác ứng với một tổ hợp chập $3$ của ${n}$ điểm nên có $C_{{{n}}}^{{3}} = {ans}$ tam giác."
    else:
        ans = n * (n - 1)
        caudan = f"Cho ${n}$ điểm phân biệt trong mặt phẳng. Hỏi có bao nhiêu vectơ khác $\\vec{{0}}$ có điểm đầu và điểm cuối là $2$ điểm trong ${n}$ điểm đã cho?"
        loigiai = f"Mỗi vectơ khác $\\vec{{0}}$ là một chỉnh hợp chập $2$ của ${n}$ điểm nên có $A_{{{n}}}^{{2}} = {n}\\cdot{n-1} = {ans}$ vectơ."
    return caudan, str(ans), loigiai


def tbk_k10_sa_c8_he_so_nhi_thuc_newton():
    """TLN: Tìm hệ số của x^k trong khai triển (ax + b)^n với n in {4, 5}."""
    n = random.choice([4, 5])
    a = random.choice([1, 2, 3])
    b = random.choice([-2, -1, 1, 2])
    k = random.choice([2, 3])
    coef = math.comb(n, k) * (a ** k) * (b ** (n - k))
    a_str = "x" if a == 1 else f"{a}x"
    b_str = f"+ {b}" if b > 0 else f"- {-b}"
    caudan = f"Tìm hệ số của $x^{k}$ trong khai triển biểu thức $({a_str} {b_str})^{n}$."
    loigiai = (
        f"Số hạng chứa $x^{k}$ là $C_{{{n}}}^{{{n - k}}} ({a_str})^{{{k}}} ({b})^{{{n - k}}} = {coef}x^{{{k}}}$.\n"
        f"Vậy hệ số cần tìm là ${coef}$."
    )
    return caudan, str(coef), loigiai


def tbk_k10_tf_c8_quy_tac_dem_hoan_vi_chinh_hop():
    """Đúng/Sai: Quy tắc cộng/nhân, hoán vị, chỉnh hợp, tổ hợp cơ bản."""
    n = random.randint(5, 7)
    boys = random.randint(4, 6)
    girls = random.randint(3, 5)
    a_ok = random.choice([True, False])
    b_ok = random.choice([True, False])
    c_ok = random.choice([True, False])
    d_ok = random.choice([True, False])

    perm_sh = math.factorial(n) if a_ok else math.factorial(n - 1)
    pick1_sh = (boys + girls) if b_ok else (boys * girls)
    pair_sh = (boys * girls) if c_ok else (boys + girls)
    comb_sh = math.comb(boys + girls, 2) if d_ok else math.perm(boys + girls, 2)

    caudan = f"Một nhóm học sinh gồm ${boys}$ bạn nam và ${girls}$ bạn nữ. Xét tính đúng sai của các khẳng định sau:"
    choices = _make_tf_choices([
        (a_ok, f"Số cách xếp ${n}$ học sinh đứng thành một hàng dọc là ${perm_sh}$."),
        (b_ok, f"Số cách chọn $1$ học sinh từ nhóm trên đi trực nhật là ${pick1_sh}$."),
        (c_ok, f"Số cách chọn $1$ bạn nam và $1$ bạn nữ làm cặp đôi dẫn chương trình là ${pair_sh}$."),
        (d_ok, f"Số cách chọn $2$ học sinh bất kì từ nhóm trên tham gia hội trại là ${comb_sh}$."),
    ])
    loigiai = (
        f"\\begin{{itemchoice}}\n"
        f"\\itemch {'Đúng' if a_ok else 'Sai'}. Số cách xếp là ${n}! = {math.factorial(n)}$.\n"
        f"\\itemch {'Đúng' if b_ok else 'Sai'}. Theo quy tắc cộng có ${boys} + {girls} = {boys + girls}$ cách.\n"
        f"\\itemch {'Đúng' if c_ok else 'Sai'}. Theo quy tắc nhân có ${boys} \\cdot {girls} = {boys * girls}$ cách.\n"
        f"\\itemch {'Đúng' if d_ok else 'Sai'}. Có $C_{{{boys + girls}}}^{{2}} = {math.comb(boys + girls, 2)}$ cách.\n"
        f"\\end{{itemchoice}}"
    )
    return caudan, choices, loigiai


def tbk_k10_tf_c8_nhi_thuc_newton():
    """Đúng/Sai: Khai triển nhị thức Newton (ax + b)^4."""
    a = random.choice([1, 2])
    b = random.choice([-1, 1, 2])
    n = 4
    c0 = b ** 4
    c2 = math.comb(4, 2) * (a ** 2) * (b ** 2)
    sum_coef = (a + b) ** 4
    a_str = "x" if a == 1 else f"{a}x"
    b_str = f"+ {b}" if b > 0 else f"- {-b}"

    a_ok = random.choice([True, False])
    b_ok = random.choice([True, False])
    c_ok = random.choice([True, False])
    d_ok = random.choice([True, False])

    terms_sh = 5 if a_ok else 4
    c2_sh = c2 if b_ok else c2 + 2
    c0_sh = c0 if c_ok else c0 + 1
    sum_sh = sum_coef if d_ok else sum_coef + 4

    caudan = f"Cho khai triển nhị thức Newton $P(x) = ({a_str} {b_str})^{n}$."
    choices = _make_tf_choices([
        (a_ok, f"Khai triển trên có tất cả ${terms_sh}$ số hạng."),
        (b_ok, f"Hệ số của $x^2$ trong khai triển là ${c2_sh}$."),
        (c_ok, f"Số hạng không chứa $x$ trong khai triển là ${c0_sh}$."),
        (d_ok, f"Tổng các hệ số trong khai triển $P(x)$ bằng ${sum_sh}$."),
    ])
    loigiai = (
        f"\\begin{{itemchoice}}\n"
        f"\\itemch {'Đúng' if a_ok else 'Sai'}. Khai triển bậc $4$ có $4 + 1 = 5$ số hạng.\n"
        f"\\itemch {'Đúng' if b_ok else 'Sai'}. Hệ số $x^2$ là $C_4^2\\cdot {a}^2\\cdot ({b})^2 = {c2}$.\n"
        f"\\itemch {'Đúng' if c_ok else 'Sai'}. Số hạng tự do là $({b})^4 = {c0}$.\n"
        f"\\itemch {'Đúng' if d_ok else 'Sai'}. Tổng hệ số bằng $P(1) = ({a} + {b})^4 = {sum_coef}$.\n"
        f"\\end{{itemchoice}}"
    )
    return caudan, choices, loigiai


# ==============================================================================
# LỚP 10 - CHƯƠNG IX: XÁC SUẤT CỔ ĐIỂN (TLN & ĐÚNG/SAI)
# ==============================================================================

def tbk_k10_sa_c9_xac_suat_rut_bi_the():
    """TLN: Tính xác suất lấy ngẫu nhiên 2 viên bi cùng màu / khác màu (làm tròn hàng phần trăm)."""
    red = random.randint(4, 7)
    blue = random.randint(3, 6)
    tot = red + blue
    same = random.choice([True, False])
    omega = math.comb(tot, 2)
    if same:
        fav = math.comb(red, 2) + math.comb(blue, 2)
        cond_txt = "cùng màu"
    else:
        fav = red * blue
        cond_txt = "khác màu"
    prob = _round_half_up(fav / omega, 2)
    caudan = (
        f"Một hộp chứa ${red}$ viên bi đỏ và ${blue}$ viên bi xanh. Lấy ngẫu nhiên đồng thời $2$ viên bi từ hộp. "
        f"Tính xác suất để $2$ viên bi lấy được {cond_txt} (kết quả làm tròn đến hàng phần trăm)."
    )
    loigiai = (
        f"Số phần tử không gian mẫu $n(\\Omega) = C_{{{tot}}}^2 = {omega}$.\n"
        f"Số kết quả thuận lợi là ${fav}$. Suy ra $P(A) = \\dfrac{{{fav}}}{{{omega}}} \\approx {_fmt_vn(prob, 2)}$."
    )
    return caudan, _fmt_vn(prob, 2), loigiai


def tbk_k10_sa_c9_xac_suat_xuc_xac_dong_xu():
    """TLN: Tính xác suất gieo 2 con xúc xắc cân đối (làm tròn hàng phần trăm)."""
    target_sum = random.choice([7, 8, 9, 10])
    mode = random.choice(["eq", "ge"])
    pairs = [(i, j) for i in range(1, 7) for j in range(1, 7)]
    if mode == "eq":
        fav = sum(1 for i, j in pairs if i + j == target_sum)
        cond_txt = f"tổng số chấm trên hai con xúc xắc bằng ${target_sum}$"
    else:
        fav = sum(1 for i, j in pairs if i + j >= target_sum)
        cond_txt = f"tổng số chấm trên hai con xúc xắc lớn hơn hoặc bằng ${target_sum}$"
    prob = _round_half_up(fav / 36.0, 2)
    caudan = (
        f"Gieo ngẫu nhiên một con xúc xắc cân đối và đồng chất hai lần liên tiếp. "
        f"Tính xác suất để {cond_txt} (kết quả làm tròn đến hàng phần trăm)."
    )
    loigiai = (
        f"Ta có $n(\\Omega) = 6 \\cdot 6 = 36$, số kết quả thuận lợi là ${fav}$.\n"
        f"Vậy $P = \\dfrac{{{fav}}}{{36}} \\approx {_fmt_vn(prob, 2)}$."
    )
    return caudan, _fmt_vn(prob, 2), loigiai


def tbk_k10_tf_c9_xac_suat_co_dien():
    """Đúng/Sai: Không gian mẫu, biến cố và xác suất cổ điển (rút thẻ từ 1 đến n)."""
    n = random.choice([10, 12, 15, 20])
    even_cnt = n // 2
    div3_cnt = n // 3
    # Thẻ chia hết cho 2 hoặc 3
    p_even = Fraction(even_cnt, n)
    p_div3 = Fraction(div3_cnt, n)

    a_ok = random.choice([True, False])
    b_ok = random.choice([True, False])
    c_ok = random.choice([True, False])
    d_ok = random.choice([True, False])

    omega_sh = n if a_ok else n * 2
    p_even_sh = p_even if b_ok else Fraction(even_cnt - 1, n)
    p_odd_sh = (1 - p_even) if c_ok else Fraction(1, 3)
    p_div3_sh = p_div3 if d_ok else Fraction(div3_cnt + 1, n)

    def _f(fr):
        if fr.denominator == 1:
            return str(fr.numerator)
        return f"\\dfrac{{{fr.numerator}}}{{{fr.denominator}}}"

    caudan = f"Một hộp có ${n}$ chiếc thẻ cùng loại được đánh số từ $1$ đến ${n}$. Rút ngẫu nhiên $1$ chiếc thẻ từ hộp."
    choices = _make_tf_choices([
        (a_ok, f"Số phần tử của không gian mẫu là $n(\\Omega) = {omega_sh}$."),
        (b_ok, f"Xác suất rút được thẻ ghi số chẵn là ${_f(p_even_sh)}$."),
        (c_ok, f"Xác suất rút được thẻ ghi số lẻ là ${_f(p_odd_sh)}$."),
        (d_ok, f"Xác suất rút được thẻ ghi số chia hết cho $3$ là ${_f(p_div3_sh)}$."),
    ])
    loigiai = (
        f"\\begin{{itemchoice}}\n"
        f"\\itemch {'Đúng' if a_ok else 'Sai'}. $n(\\Omega) = {n}$.\n"
        f"\\itemch {'Đúng' if b_ok else 'Sai'}. Có ${even_cnt}$ số chẵn nên xác suất là ${_f(p_even)}$.\n"
        f"\\itemch {'Đúng' if c_ok else 'Sai'}. Biến cố đối có xác suất $1 - {_f(p_even)} = {_f(1 - p_even)}$.\n"
        f"\\itemch {'Đúng' if d_ok else 'Sai'}. Có ${div3_cnt}$ số chia hết cho $3$ nên xác suất là ${_f(p_div3)}$.\n"
        f"\\end{{itemchoice}}"
    )
    return caudan, choices, loigiai


# ==============================================================================
# LỚP 11 - BÀI 3 (HSLG), BÀI 8 (GHÉP NHÓM), CHƯƠNG IV (SONG SONG),
# CHƯƠNG VII (VUÔNG GÓC), CHƯƠNG VIII (XÁC SUẤT TLN)
# ==============================================================================

def tbk_k11_mc_c1_b3_txd_chan_le_chu_ki():
    """K11 MC Bài 3: Tập xác định, tính chẵn/lẻ hoặc chu kì tuần hoàn của hàm số lượng giác."""
    mode = random.choice(["txd", "even_odd", "period"])
    if mode == "txd":
        k = random.choice([2, 3, 4])
        caudan = f"Tập xác định của hàm số $y = \\tan\\left(x - \\dfrac{{\\pi}}{{{k}}}\\right)$ là"
        ans = f"$\\mathbb{{R}} \\setminus \\left\\{{\\dfrac{{\\pi}}{{2}} + \\dfrac{{\\pi}}{{{k}}} + k\\pi \\mid k \\in \\mathbb{{Z}}\\right\\}}$."
        distractors = [
            f"$\\mathbb{{R}} \\setminus \\left\\{{\\dfrac{{\\pi}}{{{k}}} + k\\pi \\mid k \\in \\mathbb{{Z}}\\right\\}}$.",
            f"$\\mathbb{{R}} \\setminus \\left\\{{\\dfrac{{\\pi}}{{2}} + k2\\pi \\mid k \\in \\mathbb{{Z}}\\right\\}}$.",
            "$\\mathbb{R}$.",
        ]
        loigiai = f"Điều kiện: $\\cos\\left(x - \\dfrac{{\\pi}}{{{k}}}\\right) \\neq 0 \\Leftrightarrow x \\neq \\dfrac{{\\pi}}{{2}} + \\dfrac{{\\pi}}{{{k}}} + k\\pi,\\; k \\in \\mathbb{{Z}}$."
    elif mode == "even_odd":
        caudan = "Trong các hàm số sau, hàm số nào là hàm số chẵn trên tập xác định của nó?"
        ans = "$y = \\cos 2x$."
        distractors = ["$y = \\sin 2x$.", "$y = \\tan x$.", "$y = \\cot x$."]
        loigiai = "Vì $\\cos(-2x) = \\cos 2x$ với mọi $x \\in \\mathbb{R}$ nên $y = \\cos 2x$ là hàm số chẵn."
    else:
        w = random.choice([2, 3, 4])
        caudan = f"Chu kì tuần hoàn của hàm số $y = \\sin({w}x)$ là"
        ans = "$\\pi$." if w == 2 else f"$\\dfrac{{2\\pi}}{{{w}}}$."
        distractors = [
            "$2\\pi$.",
            "$4\\pi$.",
            f"$\\dfrac{{\\pi}}{{{w}}}$." if w != 2 else "$\\dfrac{\\pi}{2}$.",
        ]
        loigiai = f"Hàm số $y = \\sin({w}x)$ tuần hoàn với chu kì $T = \\dfrac{{2\\pi}}{{{w}}}$."
    phuongan = _make_mc_choices(ans, distractors)
    return caudan, phuongan, loigiai


def tbk_k11_sa_c1_b3_gtln_gtnn_hslg():
    """K11 TLN Bài 3: Tìm GTLN hoặc GTNN của y = a sin(x) + b hoặc a cos(x) + b."""
    a = random.choice([2, 3, 4, 5])
    b = random.randint(-4, 7)
    fn = random.choice(["\\sin", "\\cos"])
    ask_max = random.choice([True, False])
    ans = a + b if ask_max else b - a
    kind = "lớn nhất" if ask_max else "nhỏ nhất"
    b_str = f"+ {b}" if b > 0 else (f"- {-b}" if b < 0 else "")
    caudan = f"Tìm giá trị {kind} của hàm số $y = {a}{fn} x {b_str}$ trên $\\mathbb{{R}}$."
    loigiai = (
        f"Vì $-1 \\le {fn} x \\le 1$ nên ${b - a} \\le {a}{fn} x {b_str} \\le {a + b}$.\n"
        f"Vậy giá trị {kind} của hàm số là ${ans}$."
    )
    return caudan, str(ans), loigiai


def tbk_k11_sa_c3_b8_gia_tri_dai_dien_co_mau():
    """K11 TLN Chương III Bài 8: Tính tổng cỡ mẫu hoặc giá trị trung bình xấp xỉ từ bảng ghép nhóm."""
    start = random.choice([10, 20, 30])
    width = 10
    freqs = [random.randint(3, 8), random.randint(6, 12), random.randint(8, 15), random.randint(4, 9)]
    mids = [start + width * i + width / 2.0 for i in range(4)]
    n_tot = sum(freqs)
    mean_v = _round_half_up(sum(m * f for m, f in zip(mids, freqs)) / n_tot, 1)
    row1 = " & ".join(f"$[{start + width*i}; {start + width*(i+1)})$" for i in range(4))
    row2 = " & ".join(str(f) for f in freqs)
    table = (
        "\\begin{center}\\begin{tabular}{|l|c|c|c|c|}\\hline "
        f"Nhóm & {row1} \\\\ \\hline "
        f"Tần số & {row2} \\\\ \\hline "
        "\\end{tabular}\\end{center}"
    )
    caudan = f"Cho mẫu số liệu ghép nhóm sau:\n{table}\nTính số trung bình của mẫu số liệu ghép nhóm trên (làm tròn đến hàng phần mười)."
    loigiai = (
        f"Giá trị đại diện các nhóm lần lượt là ${'; '.join(_fmt_vn(m) for m in mids)}$, cỡ mẫu $n = {n_tot}$.\n"
        f"Số trung bình là $\\bar{{x}} \\approx {_fmt_vn(mean_v, 1)}$."
    )
    return caudan, _fmt_vn(mean_v, 1), loigiai


def tbk_k11_mc_c4_giao_tuyen_hai_mat_phang():
    """K11 MC Chương IV: Giao tuyến của hai mặt phẳng trong hình chóp S.ABCD đáy hình bình hành."""
    pair = random.choice([
        ("(SAB)", "(SCD)", "đường thẳng qua $S$ và song song với $AB, CD$"),
        ("(SAD)", "(SBC)", "đường thẳng qua $S$ và song song với $AD, BC$"),
    ])
    m1, m2, ans_txt = pair
    caudan = (
        f"Cho hình chóp $S.ABCD$ có đáy $ABCD$ là hình bình hành. "
        f"Giao tuyến của hai mặt phẳng ${m1}$ và ${m2}$ là"
    )
    phuongan = _make_mc_choices(
        f"{ans_txt}.",
        [
            "đường thẳng $SO$ (với $O$ là tâm hình bình hành $ABCD$).",
            "đường thẳng qua $S$ và cắt $AC$.",
            "đường thẳng $AC$.",
        ],
    )
    loigiai = (
        f"Hai mặt phẳng ${m1}$ và ${m2}$ có điểm chung $S$ và lần lượt chứa hai đường thẳng song song "
        f"của đáy hình bình hành $ABCD$, nên giao tuyến là {ans_txt}."
    )
    return caudan, phuongan, loigiai


def tbk_k11_mc_c4_hai_duong_song_song_cheo_nhau():
    """K11 MC Chương IV: Hai đường thẳng song song, chéo nhau trong hình chóp / tứ diện."""
    mode = random.choice(["skew", "midline"])
    if mode == "skew":
        caudan = "Cho tứ diện $ABCD$. Cặp đường thẳng nào sau đây chéo nhau?"
        phuongan = _make_mc_choices(
            "$AB$ và $CD$.",
            ["$AB$ và $AC$.", "$BC$ và $BD$.", "$AD$ và $CD$."],
        )
        loigiai = "Trong tứ diện $ABCD$, hai cạnh đối $AB$ và $CD$ không cùng nằm trong một mặt phẳng nên chéo nhau."
    else:
        caudan = (
            "Cho tứ diện $ABCD$. Gọi $M, N$ lần lượt là trung điểm của $AB$ và $AC$. "
            "Đường thẳng $MN$ song song với đường thẳng nào sau đây?"
        )
        phuongan = _make_mc_choices("$BC$.", ["$BD$.", "$CD$.", "$AD$."])
        loigiai = "Trong tam giác $ABC$, $MN$ là đường trung bình nên $MN \\parallel BC$."
    return caudan, phuongan, loigiai


def tbk_k11_mc_c4_duong_song_song_mat_phang():
    """K11 MC Chương IV: Đường thẳng song song với mặt phẳng."""
    caudan = (
        "Cho hình chóp $S.ABCD$ có đáy $ABCD$ là hình bình hành. Gọi $M, N$ lần lượt là trung điểm của $SA$ và $SD$. "
        "Đường thẳng $MN$ song song với mặt phẳng nào sau đây?"
    )
    phuongan = _make_mc_choices("$(SBC)$.", ["$(SAB)$.", "$(SCD)$.", "$(SAC)$."])
    loigiai = (
        "Trong tam giác $SAD$, $MN$ là đường trung bình nên $MN \\parallel AD$. "
        "Mà $AD \\parallel BC$ nên $MN \\parallel BC \\subset (SBC)$, suy ra $MN \\parallel (SBC)$."
    )
    return caudan, phuongan, loigiai


def tbk_k11_mc_c4_hai_mat_phang_song_song_thales():
    """K11 MC Chương IV: Hai mặt phẳng song song và định lí Thales trong không gian."""
    mode = random.choice(["parallel_planes", "thales"])
    if mode == "parallel_planes":
        caudan = (
            "Cho hình lăng trụ $ABC.A'B'C'$. Mặt phẳng $(ABC)$ song song với mặt phẳng nào sau đây?"
        )
        phuongan = _make_mc_choices("$(A'B'C')$.", ["$(ABB'A')$.", "$(ACC'A')$.", "$(BCC'B')$."])
        loigiai = "Theo tính chất hình lăng trụ, hai mặt đáy $(ABC)$ và $(A'B'C')$ song song với nhau."
    else:
        a = random.choice([2, 3, 4])
        b = random.choice([3, 5, 6])
        c = a * random.choice([2, 3])
        ans_d = b * (c // a)
        caudan = (
            f"Ba mặt phẳng $(P), (Q), (R)$ đôi một song song cắt hai đường thẳng $d$ và $d'$ lần lượt tại $A, B, C$ và $A', B', C'$. "
            f"Biết $AB = {a}$, $BC = {b}$ và $A'B' = {c}$. Độ dài đoạn $B'C'$ bằng"
        )
        phuongan = _make_mc_choices(
            f"${ans_d}$.",
            [f"${ans_d + 2}$.", f"${ans_d - 1}$.", f"${c + b}$.", f"${ans_d + 4}$.", f"${ans_d + 1}$."],
        )
        loigiai = (
            f"Theo định lí Thales trong không gian: $\\dfrac{{AB}}{{BC}} = \\dfrac{{A'B'}}{{B'C'}} "
            f"\\Rightarrow B'C' = \\dfrac{{{b}\\cdot{c}}}{{{a}}} = {ans_d}$."
        )
    return caudan, phuongan, loigiai


def tbk_k11_mc_c4_phep_chieu_song_song():
    """K11 MC Chương IV: Tính chất phép chiếu song song."""
    caudan = "Qua phép chiếu song song lên mặt phẳng $(P)$ theo phương chiếu $l$ (không song song với các cạnh của hình bình hành), hình chiếu của một hình bình hành không nằm trong mặt phẳng song song với $l$ là"
    phuongan = _make_mc_choices(
        "một hình bình hành.",
        ["một hình thang chỉ có hai cạnh song song.", "một tam giác.", "một hình tròn."],
    )
    loigiai = "Phép chiếu song song bảo toàn tính song song của hai đường thẳng nên hình chiếu của hình bình hành là một hình bình hành."
    return caudan, phuongan, loigiai


def tbk_k11_sa_c4_thales_ti_so_doan_thang():
    """K11 TLN Chương IV: Định lí Thales trong không gian tính độ dài đoạn thẳng."""
    ab = random.choice([3, 4, 5])
    bc = random.choice([6, 8, 9, 10])
    k = random.choice([2, 3])
    apbp = ab * k
    ans = bc * k
    caudan = (
        f"Ba mặt phẳng $(P) \\parallel (Q) \\parallel (R)$ cắt hai đường thẳng $d, d'$ lần lượt tại $A, B, C$ và $A', B', C'$. "
        f"Biết $AB = {ab}$, $BC = {bc}$, $A'B' = {apbp}$. Tính độ dài đoạn thẳng $A'C'$."
    )
    tot = apbp + ans
    loigiai = (
        f"Theo định lí Thales: $\\dfrac{{B'C'}}{{A'B'}} = \\dfrac{{BC}}{{AB}} = \\dfrac{{{bc}}}{{{ab}}} \\Rightarrow B'C' = {ans}$.\n"
        f"Do $B'$ nằm giữa $A'$ và $C'$ nên $A'C' = {apbp} + {ans} = {tot}$."
    )
    return caudan, str(tot), loigiai


def tbk_k11_sa_c4_thiet_dien_song_song_chu_vi():
    """K11 TLN Chương IV: Chu vi thiết diện song song với mặt đáy hình chóp đều."""
    edge = random.choice([6, 9, 12, 15])
    ratio_num = random.choice([1, 2])
    ratio_den = 3
    side_sub = edge * ratio_num / ratio_den
    perim = int(round(4 * side_sub))
    caudan = (
        f"Cho hình chóp tứ giác đều $S.ABCD$ có cạnh đáy bằng ${edge}$. "
        f"Mặt phẳng $(\\alpha)$ đi qua điểm $M$ trên cạnh $SA$ thỏa mãn $\\dfrac{{SM}}{{SA}} = \\dfrac{{{ratio_num}}}{{{ratio_den}}}$ "
        f"và song song với mặt đáy $(ABCD)$. Tính chu vi của thiết diện tạo bởi $(\\alpha)$ và hình chóp."
    )
    loigiai = (
        f"Vì $(\\alpha) \\parallel (ABCD)$ nên thiết diện là hình vuông $MNPQ$ đồng dạng với đáy $ABCD$ theo tỉ số $k = \\dfrac{{SM}}{{SA}} = \\dfrac{{{ratio_num}}}{{{ratio_den}}}$.\n"
        f"Cạnh hình vuông thiết diện là ${edge} \\cdot \\dfrac{{{ratio_num}}}{{{ratio_den}}} = {_fmt_vn(side_sub)}$, chu vi bằng $4 \\cdot {_fmt_vn(side_sub)} = {perim}$."
    )
    return caudan, str(perim), loigiai


def tbk_k11_mc_c7_goc_hai_duong_thang():
    """K11 MC Chương VII: Góc giữa hai đường thẳng trong hình lập phương hoặc tứ diện đều."""
    mode = random.choice(["cube_90", "cube_45", "tetra_60"])
    if mode == "cube_90":
        caudan = "Cho hình lập phương $ABCD.A'B'C'D'$. Góc giữa hai đường thẳng $AA'$ và $CD$ bằng"
        ans = "$90^\\circ$."
        distractors = ["$45^\\circ$.", "$60^\\circ$.", "$30^\\circ$."]
        loigiai = "Vì $AA' \\perp (ABCD)$ nên $AA' \\perp CD$, suy ra góc giữa $AA'$ và $CD$ bằng $90^\\circ$."
    elif mode == "cube_45":
        caudan = "Cho hình lập phương $ABCD.A'B'C'D'$. Góc giữa hai đường thẳng $AB$ và $B'D'$ bằng"
        ans = "$45^\\circ$."
        distractors = ["$90^\\circ$.", "$60^\\circ$.", "$30^\\circ$."]
        loigiai = "Vì $B'D' \\parallel BD$ nên góc giữa $AB$ và $B'D'$ bằng góc $\\widehat{ABD} = 45^\\circ$."
    else:
        caudan = "Cho tứ diện đều $ABCD$. Góc giữa hai đường thẳng $AB$ và $BC$ bằng"
        ans = "$60^\\circ$."
        distractors = ["$90^\\circ$.", "$45^\\circ$.", "$120^\\circ$."]
        loigiai = "Vì $ABC$ là tam giác đều nên góc giữa hai đường thẳng $AB$ và $BC$ bằng $60^\\circ$."
    phuongan = _make_mc_choices(ans, distractors)
    return caudan, phuongan, loigiai


def tbk_k11_mc_c7_duong_vuong_goc_mat_phang():
    """K11 MC Chương VII: Đường thẳng vuông góc với mặt phẳng trong hình chóp SA vuông góc đáy."""
    caudan = (
        "Cho hình chóp $S.ABCD$ có đáy $ABCD$ là hình chữ nhật và $SA \\perp (ABCD)$. "
        "Khẳng định nào sau đây đúng?"
    )
    phuongan = _make_mc_choices(
        "$BC \\perp (SAB)$.",
        ["$BD \\perp (SAC)$.", "$SC \\perp (ABCD)$.", "$CD \\perp (SAB)$."],
    )
    loigiai = "Vì $BC \\perp AB$ (hình chữ nhật) và $BC \\perp SA$ (do $SA \\perp (ABCD)$) nên $BC \\perp (SAB)$."
    return caudan, phuongan, loigiai


def tbk_k11_mc_c7_khoang_cach_co_ban():
    """K11 MC Chương VII: Khoảng cách từ điểm S đến (ABCD) hoặc từ B đến (SAD)."""
    a = random.randint(2, 8)
    h = random.randint(3, 9)
    while h == a:
        h = random.randint(3, 9)
    if random.choice([True, False]):
        caudan = (
            f"Cho hình chóp $S.ABCD$ có đáy $ABCD$ là hình vuông cạnh ${a}$, $SA \\perp (ABCD)$ và $SA = {h}$. "
            f"Khoảng cách từ điểm $S$ đến mặt phẳng $(ABCD)$ bằng"
        )
        ans = f"${h}$."
        distractors = [f"${a}$.", f"${a + h}$.", f"${h}\\sqrt{{2}}$."]
        loigiai = f"Vì $SA \\perp (ABCD)$ nên $d(S, (ABCD)) = SA = {h}$."
    else:
        caudan = (
            f"Cho hình chóp $S.ABCD$ có đáy $ABCD$ là hình chữ nhật với $AB = {a}, AD = {h}$ và $SA \\perp (ABCD)$. "
            f"Khoảng cách từ điểm $B$ đến mặt phẳng $(SAD)$ bằng"
        )
        ans = f"${a}$."
        distractors = [f"${h}$.", f"${a + h}$.", f"${a}\\sqrt{{2}}$."]
        loigiai = f"Vì $AB \\perp AD$ và $AB \\perp SA$ nên $AB \\perp (SAD)$, suy ra $d(B, (SAD)) = AB = {a}$."
    phuongan = _make_mc_choices(ans, distractors)
    return caudan, phuongan, loigiai


def tbk_k11_sa_c8_cong_thuc_cong_xac_suat():
    """K11 TLN Chương VIII: Tính P(A hợp B) theo công thức cộng xác suất."""
    pa = random.choice([0.3, 0.35, 0.4, 0.45, 0.5])
    pb = random.choice([0.25, 0.3, 0.4, 0.45])
    pab = random.choice([0.1, 0.12, 0.15, 0.2])
    ans = round(pa + pb - pab, 2)
    caudan = (
        f"Cho hai biến cố $A$ và $B$ có $P(A) = {_fmt_vn(pa, 2)}$, $P(B) = {_fmt_vn(pb, 2)}$ "
        f"và $P(A \\cap B) = {_fmt_vn(pab, 2)}$. Tính xác suất của biến cố $A \\cup B$."
    )
    loigiai = (
        f"Áp dụng công thức cộng xác suất:\n"
        f"$P(A \\cup B) = P(A) + P(B) - P(A \\cap B) = {_fmt_vn(pa, 2)} + {_fmt_vn(pb, 2)} - {_fmt_vn(pab, 2)} = {_fmt_vn(ans, 2)}$."
    )
    return caudan, _fmt_vn(ans, 2), loigiai


def tbk_k11_sa_c8_bien_co_doc_lap_ban_bia():
    """K11 TLN Chương VIII: Biến cố độc lập (2 xạ thủ bắn bia hoặc 2 động cơ hoạt động độc lập)."""
    p1 = random.choice([0.6, 0.7, 0.75, 0.8])
    p2 = random.choice([0.7, 0.8, 0.85, 0.9])
    mode = random.choice(["both", "at_least_one"])
    if mode == "both":
        ans = round(p1 * p2, 2)
        ask = "cả hai người đều bắn trúng bia"
        loigiai = f"Vì hai biến cố độc lập nên $P = {_fmt_vn(p1, 2)} \\cdot {_fmt_vn(p2, 2)} = {_fmt_vn(ans, 2)}$."
    else:
        ans = round(1.0 - (1.0 - p1) * (1.0 - p2), 2)
        ask = "có ít nhất một người bắn trúng bia"
        loigiai = (
            f"Xác suất không ai bắn trúng là $(1 - {_fmt_vn(p1, 2)})(1 - {_fmt_vn(p2, 2)}) = {_fmt_vn(round((1-p1)*(1-p2), 4), 4)}$.\n"
            f"Vậy xác suất có ít nhất một người trúng là $1 - {_fmt_vn(round((1-p1)*(1-p2), 4), 4)} = {_fmt_vn(ans, 2)}$."
        )
    caudan = (
        f"Hai xạ thủ cùng bắn độc lập vào một mục tiêu. Xác suất bắn trúng của người thứ nhất và người thứ hai "
        f"lần lượt là ${_fmt_vn(p1, 2)}$ và ${_fmt_vn(p2, 2)}$. Tính xác suất để {ask} (làm tròn đến hàng phần trăm)."
    )
    return caudan, _fmt_vn(ans, 2), loigiai
