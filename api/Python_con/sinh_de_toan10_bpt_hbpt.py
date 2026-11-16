# -*- coding: utf-8 -*-
"""
sinh_de_toan10_bpt_hbpt.py: Bộ sinh đề trắc nghiệm Toán 10 - Chương II:
BẤT PHƯƠNG TRÌNH VÀ HỆ BẤT PHƯƠNG TRÌNH BẬC NHẤT HAI ẨN
Gồm:
- Trắc nghiệm 4 lựa chọn (MC)
- Trắc nghiệm Đúng - Sai (TF)
- Tối ưu hóa quy hoạch tuyến tính (GTLN, GTNN của F(x, y) trên miền đa giác)
- Tự động đổi số ngẫu nhiên khi bấm, sinh chuẩn LaTeX ex / choice / choiceTF / loigiai.
"""

import random
import math
from fractions import Fraction

def clean_option(opt):
    s = str(opt).strip()
    if s.endswith('.'):
        s = s[:-1].strip()
    return s

def shuffle_choices(correct_text, wrong_texts):
    c_clean = clean_option(correct_text)
    wrongs_clean = []
    seen = {c_clean}
    for w in wrong_texts:
        w_c = clean_option(w)
        if w_c not in seen:
            wrongs_clean.append(w_c)
            seen.add(w_c)
    while len(wrongs_clean) < 3:
        wrongs_clean.append(f"{c_clean} + {len(wrongs_clean) + 1}")
    all_choices = [c_clean] + wrongs_clean[:3]
    random.shuffle(all_choices)
    correct_idx = all_choices.index(c_clean)
    letters = ['A', 'B', 'C', 'D']
    dapan = letters[correct_idx]
    formatted = []
    for i, ch in enumerate(all_choices):
        if i == correct_idx:
            formatted.append(f"{{\\True {ch}}}\n")
        else:
            formatted.append(f"{{{ch}}}\n")
    return formatted, dapan

def make_tf_choices(items):
    choices = []
    loi_giai_parts = []
    for item in items:
        stmt_t, stmt_f, exp_t, exp_f = item
        is_true = random.choice([True, False])
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
# BÀI 3: BẤT PHƯƠNG TRÌNH BẬC NHẤT HAI ẨN (MC & TF)
# ==============================================================================

def k10_mc_bpt_nhan_biet_bpt_bac_nhat_2_an():
    """Nhận biết bất phương trình bậc nhất hai ẩn"""
    correct = r"$2x - 3y \ge 5$"
    wrongs = [
        r"$x^2 + 2y < 3$",
        r"$2x - 3y^2 + 1 > 0$",
        r"$\dfrac{1}{x} + 2y \le 4$"
    ]
    caudan = "Trong các bất phương trình sau, bất phương trình nào là bất phương trình bậc nhất hai ẩn?"
    choices, dapan = shuffle_choices(correct, wrongs)
    loigiai = (
        r"Bất phương trình bậc nhất hai ẩn có dạng tổng quát là $ax + by < c$ "
        r"(hoặc $\le, >, \ge$), trong đó $a, b$ không đồng thời bằng 0. "
        r"Do đó $2x - 3y \ge 5$ là bất phương trình bậc nhất hai ẩn."
    )
    return caudan, choices, loigiai


def k10_mc_bpt_kiem_tra_diem_thuoc_mien_nghiem():
    """Kiểm tra cặp số nào là / không là nghiệm của BPT ax + by >= c"""
    a = random.choice([2, 3, -2, 1])
    b = random.choice([1, -2, 2, -1])
    c = random.choice([3, 4, 5, 6])

    # Sinh điểm thỏa mãn và không thỏa mãn
    pts_satisfy = []
    pts_not_satisfy = []
    for x in range(-3, 5):
        for y in range(-3, 5):
            if a * x + b * y >= c:
                pts_satisfy.append((x, y))
            else:
                pts_not_satisfy.append((x, y))

    if not pts_not_satisfy or len(pts_satisfy) < 3:
        pts_satisfy = [(2, 3), (3, 0), (1, 2)]
        pts_not_satisfy = [(1, -3)]
        a, b, c = 2, 1, 4

    # Hỏi cặp nào KHÔNG là nghiệm
    not_pt = random.choice(pts_not_satisfy)
    good_pts = random.sample(pts_satisfy, 3)

    caudan = f"Cặp số nào sau đây \\textbf{{không}} là nghiệm của bất phương trình ${a}x + {b}y \\ge {c}$?"
    correct = f"$({not_pt[0]}; {not_pt[1]})$"
    wrongs = [f"$({p[0]}; {p[1]})$" for p in good_pts]
    choices, dapan = shuffle_choices(correct, wrongs)

    val_not = a * not_pt[0] + b * not_pt[1]
    loigiai = (
        f"Thay tọa độ điểm $({not_pt[0]}; {not_pt[1]})$ vào bất phương trình ta có: "
        f"${a} \\cdot ({not_pt[0]}) + {b} \\cdot ({not_pt[1]}) = {val_not} < {c}$ (vô lý).\\\\\n"
        f"Vậy điểm $({not_pt[0]}; {not_pt[1]})$ không thuộc miền nghiệm của bất phương trình."
    )
    return caudan, choices, loigiai


def k10_mc_bpt_xac_dinh_bpt_tu_nua_mat_phang():
    """Xác định BPT từ miền nghiệm có bờ là đường thẳng d (ảnh Câu 16, 17, 18)"""
    scenarios = [
        {"d": "x - y = 4", "ans": r"$x - y \ge 4$", "w1": r"$x - y > 4$", "w2": r"$x - y < 4$", "w3": r"$x - y \le 4$", "test": (0, 0), "side": "chứa O sai"},
        {"d": "x <= 0", "ans": r"$x \le 0$", "w1": r"$x \ge 0$", "w2": r"$y \ge 0$", "w3": r"$y \le 0$", "test": (1, 0), "side": "bên trái Oy"},
        {"d": "2x - y = 3", "ans": r"$2x - y < 3$", "w1": r"$2x - y > 3$", "w2": r"$x - 2y < 3$", "w3": r"$x - 2y > 3$", "test": (0, 0), "side": "chứa gốc O (bờ nét đứt)"},
    ]
    sc = random.choice(scenarios)
    if sc["d"] == "x - y = 4":
        caudan = (
            r"Cho đường thẳng $d$ đi qua hai điểm $(4; 0)$ và $(0; -4)$. "
            r"Hãy chọn bất phương trình mà miền nghiệm của nó là nửa mặt phẳng kể cả bờ $d$ không chứa gốc toạ độ $O$."
        )
    elif sc["d"] == "x <= 0":
        caudan = (
            r"Nửa mặt phẳng nằm bên trái trục tung $Oy$ (kể cả trục $Oy$) là miền nghiệm của bất phương trình nào dưới đây?"
        )
    else:
        caudan = (
            r"Đường thẳng $d$ đi qua hai điểm $(1; -1)$ và $(0; -3)$. "
            r"Nửa mặt phẳng không kể bờ $d$ và chứa gốc toạ độ $O(0;0)$ là miền nghiệm của bất phương trình nào?"
        )

    correct = sc["ans"]
    wrongs = [sc["w1"], sc["w2"], sc["w3"]]
    choices, dapan = shuffle_choices(correct, wrongs)
    loigiai = (
        f"Kiểm tra bằng cách thay toạ độ gốc toạ độ $O(0;0)$ vào các phương án để xác định chiều của bất phương trình.\\\\\n"
        f"Đáp án đúng là {correct}."
    )
    return caudan, choices, loigiai


def k10_tf_bpt_khao_sat_bpt_bac_nhat_2_an():
    """Đúng sai: Khảo sát BPT 3(x-1) + 4(y-2) < x - 3 (ảnh Câu 7)"""
    caudan = r"Cho bất phương trình $3(x - 1) + 4(y - 2) < x - 3 \quad (1)$. Khi đó:"

    item_a = (
        r"Bất phương trình $(1)$ là bất phương trình bậc nhất hai ẩn.",
        r"Bất phương trình $(1)$ không phải là bất phương trình bậc nhất hai ẩn.",
        r"Biến đổi $(1) \Leftrightarrow 3x - 3 + 4y - 8 < x - 3 \Leftrightarrow 2x + 4y < 8 \Leftrightarrow x + 2y < 4$. Đây là bất phương trình bậc nhất hai ẩn.",
        r"Sai vì sau khi rút gọn ta được $x + 2y < 4$, là bất phương trình bậc nhất hai ẩn."
    )
    item_b = (
        r"Điểm $B(-2; 2)$ thuộc miền nghiệm của bất phương trình $(1)$.",
        r"Điểm $B(-2; 2)$ không thuộc miền nghiệm của bất phương trình $(1)$.",
        r"Thay $x = -2, y = 2$ vào $x + 2y < 4$: $-2 + 2(2) = 2 < 4$ (đúng). Do đó $B(-2;2)$ thuộc miền nghiệm.",
        r"Sai vì $-2 + 2(2) = 2 < 4$ nên $B$ thuộc miền nghiệm."
    )
    item_c = (
        r"Miền nghiệm của bất phương trình $(1)$ chứa gốc toạ độ $O(0;0)$.",
        r"Miền nghiệm của bất phương trình $(1)$ không chứa gốc toạ độ $O(0;0)$.",
        r"Thay $x = 0, y = 0$ vào $x + 2y < 4$: $0 + 0 = 0 < 4$ (đúng). Do đó miền nghiệm chứa gốc tọa độ $O$.",
        r"Sai vì $0 < 4$ nên gốc toạ độ thuộc miền nghiệm."
    )
    item_d = (
        r"Đường thẳng bờ $d: x + 2y = 4$ cắt hai trục toạ độ tại $(4;0)$ và $(0;2)$.",
        r"Đường thẳng bờ $d: x + 2y = 4$ cắt hai trục toạ độ tại $(2;0)$ và $(0;4)$.",
        r"Với $y=0 \Rightarrow x=4 \Rightarrow (4;0)$; với $x=0 \Rightarrow y=2 \Rightarrow (0;2)$.",
        r"Sai vì giao điểm với $Ox$ là $(4;0)$ và với $Oy$ là $(0;2)$."
    )

    items = [item_a, item_b, item_c, item_d]
    choices, loigiai = make_tf_choices(items)
    return caudan, choices, loigiai


# ==============================================================================
# BÀI 4: HỆ BẤT PHƯƠNG TRÌNH BẬC NHẤT HAI ẨN (MC & TF)
# ==============================================================================

def k10_mc_hbpt_nhan_biet_he_bpt_bac_nhat():
    """Nhận biết / đếm / tìm điều kiện hệ BPT bậc nhất hai ẩn (Ảnh 1 C9, Ảnh 3 C8, Ảnh 5 C6, C7)"""
    case = random.choice([1, 2, 3, 4])
    if case == 1:
        # Không phải hệ BPT bậc nhất hai ẩn
        correct = random.choice([
            r"$\begin{cases} x^2 - y \le 2 \\ 4x + 5y \le 1 \end{cases}$",
            r"$\begin{cases} x^2 \ge 0 \\ 20x + 3y \le 10 \end{cases}$",
        ])
        wrongs = [
            r"$\begin{cases} y \ge 0 \\ x - y \ge 0 \\ 2x + 3y \le 5 \end{cases}$",
            r"$\begin{cases} x > 0 \\ x + \sqrt{3}y + 1 \le 0 \end{cases}$",
            r"$\begin{cases} x + y \ge 2024 \\ y - x < 0 \end{cases}$",
        ]
        caudan = "Trong các hệ bất phương trình sau, hệ bất phương trình nào \\textbf{không} phải là hệ bất phương trình bậc nhất hai ẩn?"
        loigiai = "Hệ chứa ẩn bậc hai ($x^2$) nên không phải là hệ bất phương trình bậc nhất hai ẩn."
    elif case == 2:
        # Tìm hệ ĐÚNG là hệ BPT bậc nhất hai ẩn (Ảnh 1 Câu 9)
        correct = r"$\begin{cases} 2x - 3y \le 5 \\ -3x > 2 \end{cases}$"
        wrongs = [
            r"$\begin{cases} 2x^2 - 3y \le 5 \\ -3x > 2 \end{cases}$",
            r"$\begin{cases} 2x - 3y \le 5 \\ -3x + y^2 > 2 \end{cases}$",
            r"$\begin{cases} 2x - 3y^3 \le 5 \\ -3x + 5y \le 2 \end{cases}$",
        ]
        caudan = "Hệ bất phương trình nào sau đây là hệ bất phương trình bậc nhất hai ẩn?"
        loigiai = r"Hệ $\begin{cases} 2x - 3y \le 5 \\ -3x > 2 \end{cases}$ gồm các bất phương trình bậc nhất đối với $x, y$ nên là hệ bất phương trình bậc nhất hai ẩn."
    elif case == 3:
        # Điều kiện tham số (Ảnh 3 Câu 8)
        c1 = random.choice([2, 3, 4])
        c2 = random.choice([3, 5, 7])
        c3 = random.choice([-3, -2, 1, 4])
        caudan = f"Điều kiện để hệ $\\begin{{cases}} ax + by < 0 \\\\ {c1}x + {c2}y \\ge {c3} \\end{{cases}}$ là một hệ bất phương trình bậc nhất hai ẩn $x, y$ là"
        correct = r"$a^2 + b^2 \neq 0$"
        wrongs = [r"$a \neq 0$", r"$b \neq 0$", r"$a^2 + b^2 \ge 0$"]
        loigiai = r"Để $ax + by < 0$ là bất phương trình bậc nhất hai ẩn thì $a$ và $b$ không đồng thời bằng $0$, tức $a^2 + b^2 \neq 0$."
    else:
        # Đếm số hệ BPT bậc nhất hai ẩn trong 4 hệ (Ảnh 5 Câu 6)
        good_systems = [
            r"$\begin{cases} x - 4y \le 0 \\ x \ge 0 \\ y \ge 0 \end{cases}$",
            r"$\begin{cases} x - 2y > 2 \\ x + 3y > 0 \end{cases}$",
            r"$\begin{cases} x > -2 \\ 5x - \sqrt{3}y < \sqrt{11} \end{cases}$",
            r"$\begin{cases} 2x + y \le 4 \\ y \ge 1 \end{cases}$",
        ]
        bad_systems = [
            r"$\begin{cases} x - 2y > 5 \\ x^2 > 3y \end{cases}$",
            r"$\begin{cases} x + y^2 \le 3 \\ x - y > 1 \end{cases}$",
            r"$\begin{cases} xy > 2 \\ x + y \le 5 \end{cases}$",
        ]
        n_good = random.choice([1, 2, 3])
        chosen = random.sample(good_systems, n_good) + random.sample(bad_systems, 4 - n_good)
        random.shuffle(chosen)
        sys_str = ";\\quad ".join(chosen)
        caudan = f"Cho bốn hệ bất phương trình sau: $${sys_str}.$$ Số hệ bất phương trình bậc nhất hai ẩn là"
        correct = f"${n_good}$"
        wrongs = [f"${k}$" for k in [0, 1, 2, 3, 4] if k != n_good][:3]
        loigiai = f"Các bất phương trình bậc nhất hai ẩn chỉ chứa $x, y$ bậc nhất (không chứa $x^2, y^2, xy$). Đếm được ${n_good}$ hệ thỏa mãn."

    choices, dapan = shuffle_choices(correct, wrongs)
    return caudan, choices, loigiai


def k10_mc_hbpt_diem_thuoc_mien_nghiem():
    """Kiểm tra điểm thuộc / không thuộc miền nghiệm, hoặc tìm hệ BPT chứa điểm M (Ảnh 1, 3, 5)"""
    mode = random.choice(["thuoc", "khong_thuoc", "chon_he"])
    if mode in ("thuoc", "khong_thuoc"):
        while True:
            a1, b1, c1 = random.choice([(1, 3, 2), (2, -3, 5), (1, -2, 2), (4, -1, 6), (1, 1, 2)])
            a2, b2, c2 = random.choice([(2, 1, -1), (2, 0, 3), (-2, 1, -4), (0, 1, 1), (1, 3, 7)])
            op1 = random.choice(["\\le", "\\ge", "<", ">"])
            op2 = random.choice(["\\le", "\\ge", "<", ">"])
            def ok(x, y):
                v1 = a1 * x + b1 * y
                v2 = a2 * x + b2 * y
                f1 = (v1 <= c1) if op1 == "\\le" else (v1 >= c1) if op1 == "\\ge" else (v1 < c1) if op1 == "<" else (v1 > c1)
                f2 = (v2 <= c2) if op2 == "\\le" else (v2 >= c2) if op2 == "\\ge" else (v2 < c2) if op2 == "<" else (v2 > c2)
                return f1 and f2
            good = [(x, y) for x in range(-4, 6) for y in range(-4, 6) if ok(x, y)]
            bad = [(x, y) for x in range(-4, 6) for y in range(-4, 6) if not ok(x, y)]
            if len(good) >= 4 and len(bad) >= 4:
                break

        def fmt_ineq(a, b, op, c):
            parts = []
            if a != 0:
                parts.append("x" if a == 1 else "-x" if a == -1 else f"{a}x")
            if b != 0:
                if not parts:
                    parts.append("y" if b == 1 else "-y" if b == -1 else f"{b}y")
                else:
                    if b == 1:
                        parts.append("+ y")
                    elif b == -1:
                        parts.append("- y")
                    elif b > 0:
                        parts.append(f"+ {b}y")
                    else:
                        parts.append(f"- {abs(b)}y")
            return f"{' '.join(parts)} {op} {c}"

        he_tex = f"\\begin{{cases}} {fmt_ineq(a1, b1, op1, c1)} \\\\ {fmt_ineq(a2, b2, op2, c2)} \\end{{cases}}"
        if mode == "thuoc":
            ans_pt = random.choice(good)
            wrong_pts = random.sample(bad, 3)
            caudan = f"Cho hệ bất phương trình ${he_tex}$. Điểm nào sau đây thuộc miền nghiệm của hệ bất phương trình đã cho?"
            loigiai = f"Thay tọa độ $({ans_pt[0]}; {ans_pt[1]})$ vào từng bất phương trình trong hệ ta thấy đều thỏa mãn."
        else:
            ans_pt = random.choice(bad)
            wrong_pts = random.sample(good, 3)
            caudan = f"Cặp số nào sau đây \\textbf{{không}} là một nghiệm của hệ bất phương trình ${he_tex}$?"
            loigiai = f"Thay tọa độ $({ans_pt[0]}; {ans_pt[1]})$ vào hệ ta thấy có ít nhất một bất phương trình không thỏa mãn."
        correct = f"$({ans_pt[0]}; {ans_pt[1]})$"
        wrongs = [f"$({p[0]}; {p[1]})$" for p in wrong_pts]
    else:
        # Cho điểm M(x0, y0), hỏi thuộc miền nghiệm của hệ nào (Ảnh 3 Câu 9, Ảnh 5 Câu 2)
        px = random.choice([0, 1, 2])
        py = random.choice([-3, 2, 3])
        if (px, py) == (2, 3):
            caudan = "Điểm $M(2; 3)$ thuộc miền nghiệm của hệ bất phương trình bậc nhất hai ẩn nào sau đây?"
            correct = r"$\begin{cases} x + 3y \ge 1 \\ x - y < 0 \end{cases}$"
            wrongs = [
                r"$\begin{cases} x + 3y \ge 1 \\ x - y > 0 \end{cases}$",
                r"$\begin{cases} x + 3y < 1 \\ x - y < 0 \end{cases}$",
                r"$\begin{cases} x - 3y \ge 1 \\ x - y > 0 \end{cases}$",
            ]
            loigiai = r"Thay $x = 2, y = 3$ vào hệ $\begin{cases} x + 3y \ge 1 \\ x - y < 0 \end{cases}$ được $2 + 9 = 11 \ge 1$ và $2 - 3 = -1 < 0$ (đều đúng)."
        elif (px, py) == (0, -3):
            caudan = "Điểm $M(0; -3)$ thuộc miền nghiệm của hệ bất phương trình nào sau đây?"
            correct = r"$\begin{cases} 2x - y \le 3 \\ 10x - 5y \ge -8 \end{cases}$"
            wrongs = [
                r"$\begin{cases} 2x - y > 3 \\ 10x - 5y \ge -8 \end{cases}$",
                r"$\begin{cases} 2x - y > -3 \\ 10x - 5y < -8 \end{cases}$",
                r"$\begin{cases} 2x - y \le -3 \\ 10x - 5y \le -8 \end{cases}$",
            ]
            loigiai = r"Thay $x = 0, y = -3$ vào hệ $\begin{cases} 2x - y \le 3 \\ 10x - 5y \ge -8 \end{cases}$ được $3 \le 3$ và $15 \ge -8$ (đều đúng)."
        else:
            caudan = f"Điểm $M({px}; {py})$ thuộc miền nghiệm của hệ bất phương trình nào sau đây?"
            v1 = 2 * px + py
            v2 = px - py
            correct = f"$\\begin{{cases}} 2x + y \\le {v1 + 1} \\\\ x - y \\ge {v2 - 1} \\end{{cases}}$"
            wrongs = [
                f"$\\begin{{cases}} 2x + y > {v1 + 1} \\\\ x - y \\ge {v2 - 1} \\end{{cases}}$",
                f"$\\begin{{cases}} 2x + y \\le {v1 + 1} \\\\ x - y < {v2 - 1} \\end{{cases}}$",
                f"$\\begin{{cases}} 2x + y \\le {v1 - 2} \\\\ x - y \\ge {v2 - 1} \\end{{cases}}$",
            ]
            loigiai = f"Thay $x = {px}, y = {py}$ vào hệ $\\begin{{cases}} 2x + y \\le {v1 + 1} \\\\ x - y \\ge {v2 - 1} \\end{{cases}}$ ta thấy cả hai bất phương trình đều đúng."

    choices, dapan = shuffle_choices(correct, wrongs)
    return caudan, choices, loigiai


def k10_mc_hbpt_dem_so_diem_thuoc_mien_nghiem():
    """Đếm số điểm thuộc miền nghiệm của hệ (ảnh Câu 3)"""
    # Hệ: y >= 0 và 3x + 2y - 6 < 0
    # O(0,0): 0>=0, -6<0 (Đúng)
    # A(2,3): 3>=0, 6+6-6=6<0 (Sai)
    # B(-1,1): 1>=0, -3+2-6=-7<0 (Đúng)
    # C(-1,3): 3>=0, -3+6-6=-3<0 (Đúng)
    # Có 3 điểm thuộc miền nghiệm
    caudan = (
        r"Cho hệ bất phương trình $\begin{cases} y \ge 0 \\ 3x + 2y - 6 < 0 \end{cases}$ "
        r"có miền nghiệm là $S$ và bốn điểm $O(0;0), A(2;3), B(-1;1), C(-1;3)$. Có bao nhiêu điểm thuộc $S$?"
    )
    correct = "$3$"
    wrongs = ["$1$", "$2$", "$4$"]
    choices, dapan = shuffle_choices(correct, wrongs)
    loigiai = (
        r"Kiểm tra từng điểm:\\"
        r"- Với $O(0;0)$: $y = 0 \ge 0$ và $3(0) + 2(0) - 6 = -6 < 0$ (thỏa mãn).\\"
        r"- Với $A(2;3)$: $3(2) + 2(3) - 6 = 6 > 0$ (không thỏa mãn).\\"
        r"- Với $B(-1;1)$: $y = 1 \ge 0$ và $3(-1) + 2(1) - 6 = -7 < 0$ (thỏa mãn).\\"
        r"- Với $C(-1;3)$: $y = 3 \ge 0$ và $3(-1) + 2(3) - 6 = -3 < 0$ (thỏa mãn).\\\\"
        r"Vậy có 3 điểm thuộc miền nghiệm $S$."
    )
    return caudan, choices, loigiai


def k10_mc_hbpt_xac_dinh_he_bpt_tu_tam_giac_mien_nghiem():
    """Xác định hệ BPT có miền nghiệm là miền tam giác OAB (ảnh Câu 12, 13)"""
    # Miền tam giác OAB tạo bởi x <= 0, y >= 0 và đường thẳng x - 2y >= -2
    caudan = (
        r"Miền tam giác $OAB$ (kể cả biên) với $O(0;0), A(0;1), B(-2;0)$ là miền nghiệm của hệ bất phương trình nào sau đây?"
    )
    correct = r"$\begin{cases} x \le 0 \\ y \ge 0 \\ x - 2y \ge -2 \end{cases}$"
    wrongs = [
        r"$\begin{cases} x \le 0 \\ y \ge 0 \\ x + 2y \ge -2 \end{cases}$",
        r"$\begin{cases} x \le 0 \\ y \le 0 \\ x - 2y \ge 2 \end{cases}$",
        r"$\begin{cases} x \ge 0 \\ y \ge 0 \\ x - 2y \ge -2 \end{cases}$"
    ]
    choices, dapan = shuffle_choices(correct, wrongs)
    loigiai = (
        r"Đường thẳng $AB$ đi qua $A(0;1)$ và $B(-2;0)$ có phương trình $\dfrac{x}{-2} + \dfrac{y}{1} = 1 \Leftrightarrow x - 2y + 2 = 0$.\\"
        r"Gốc $O(0;0)$ thuộc miền tam giác $OAB$, thay vào $x - 2y + 2$ được $2 \ge 0$.\\"
        r"Hơn nữa tam giác nằm ở góc phần tư thứ II nên $x \le 0, y \ge 0$.\\"
        r"Vậy hệ cần tìm là $\begin{cases} x \le 0 \\ y \ge 0 \\ x - 2y \ge -2 \end{cases}$."
    )
    return caudan, choices, loigiai


def k10_mc_hbpt_toan_thuc_te_mo_hinh_hoa():
    """Bài toán thực tế mô hình hóa điều kiện thành hệ BPT (ảnh Câu 23)"""
    caudan = (
        "Để trở thành một thành viên của ban nhạc thì một sinh viên phải đạt điểm trung bình các môn học "
        "ít nhất là 7,0 và phải có tối thiểu 5 lần thực hành sau giờ học. "
        "Gọi $x$ là điểm trung bình các môn học và $y$ là số lần thực hành sau giờ học, "
        "hãy chọn hệ bất phương trình thể hiện tốt nhất tình huống này."
    )
    correct = r"$\begin{cases} x \ge 7 \\ y \ge 5 \end{cases}$"
    wrongs = [
        r"$\begin{cases} x \le 7 \\ y \le 5 \end{cases}$",
        r"$\begin{cases} x < 7 \\ y < 5 \end{cases}$",
        r"$\begin{cases} x > 7 \\ y > 5 \end{cases}$"
    ]
    choices, dapan = shuffle_choices(correct, wrongs)
    loigiai = (
        r"``Ít nhất 7,0'' nghĩa là $x \ge 7$.\\"
        r"``Tối thiểu 5 lần'' nghĩa là $y \ge 5$.\\\\"
        r"Vậy hệ bất phương trình tương ứng là $\begin{cases} x \ge 7 \\ y \ge 5 \end{cases}$."
    )
    return caudan, choices, loigiai


def k10_mc_hbpt_quy_hoach_tuyen_tinh_max_min():
    """Quy hoạch tuyến tính: Tìm GTLN của F(x, y) trên miền đa giác (ảnh Câu 20, 21, 22)"""
    scenarios = [
        {
            "he": r"\begin{cases} x \ge 0 \\ y \ge 0 \\ x + 2y \le 4 \\ x - y \le 1 \end{cases}",
            "F": "F(x; y) = 3x + 2y",
            "F_name": "M",
            "vertices": [(0, 0), (1, 0), (2, 1), (0, 2)],
            "F_vals": [0, 3, 3*2 + 2*1, 4], # max = 8 tai (2, 1)
            "ans": 8, "w": [6, 10, 9]
        },
        {
            "he": r"\begin{cases} 0 \le y \le 4 \\ x \ge 0 \\ x - y - 1 \le 0 \\ x + 2y - 10 \le 0 \end{cases}",
            "F": "F(x; y) = x + 2y",
            "F_name": "F_{\\max}",
            "vertices": [(0, 0), (1, 0), (4, 3), (2, 4), (0, 4)],
            "F_vals": [0, 1, 4 + 6, 2 + 8, 0 + 8], # max = 10 tai (4, 3) va (2, 4)
            "ans": 10, "w": [6, 8, 12]
        },
        {
            "he": r"\begin{cases} x - 2y + 2 \ge 0 \\ 3x + 8y - 24 \le 0 \\ x \ge 0 \\ y \ge 0 \end{cases}",
            "F": "F(x; y) = x - y - 1",
            "F_name": "F_{\\max}",
            "vertices": [(0, 0), (0, 1), (8, 0), (2.28, 2.14)], # tai (8,0): 8 - 0 - 1 = 7
            "F_vals": [-1, -2, 7, -0.86],
            "ans": 7, "w": [5, 6, 8]
        }
    ]
    sc = random.choice(scenarios)
    caudan = (
        f"Xét các số thực $x, y$ thoả mãn hệ điều kiện ${sc['he']}$. "
        f"Tìm giá trị lớn nhất {sc['F_name']} của biểu thức ${sc['F']}$."
    )
    correct = f"${sc['F_name']} = {sc['ans']}$" if "max" in sc['F_name'] or "M" in sc['F_name'] else f"${sc['ans']}$"
    wrongs = [f"${sc['F_name']} = {w}$" if "max" in sc['F_name'] or "M" in sc['F_name'] else f"${w}$" for w in sc['w']]
    choices, dapan = shuffle_choices(correct, wrongs)

    loigiai = (
        f"Miền nghiệm của hệ là một miền đa giác lồi.\\\\\n"
        f"Giá trị lớn nhất của biểu thức bậc nhất $F(x; y)$ luôn đạt tại một trong các đỉnh của miền đa giác nghiệm.\\\\\n"
        f"Thay toạ độ các đỉnh vào biểu thức $F(x; y)$, ta thu được giá trị lớn nhất là ${sc['ans']}$."
    )
    return caudan, choices, loigiai


def k10_tf_hbpt_khao_sat_he_3_bpt():
    """Đúng sai: Khảo sát hệ 3 BPT (ảnh Câu 6 & Câu 2)"""
    caudan = (
        r"Cho hệ bất phương trình $(I): \begin{cases} 2x + 3y - 6 \le 0 \\ x \ge 0 \\ 2x - 3y - 1 \le 0 \end{cases}$. Khi đó:"
    )

    item_a = (
        r"Hệ $(I)$ là hệ bất phương trình bậc nhất hai ẩn.",
        r"Hệ $(I)$ không phải là hệ bất phương trình bậc nhất hai ẩn.",
        r"Các bất phương trình trong hệ đều là bậc nhất hai ẩn nên $(I)$ là hệ bất phương trình bậc nhất hai ẩn.",
        r"Sai vì $(I)$ là hệ bất phương trình bậc nhất hai ẩn."
    )
    item_b = (
        r"Hệ $(I)$ có vô số nghiệm.",
        r"Hệ $(I)$ vô nghiệm.",
        r"Miền nghiệm của hệ $(I)$ là một miền tam giác nên có vô số nghiệm.",
        r"Sai vì hệ có miền nghiệm là miền tam giác chứa vô số nghiệm."
    )
    item_c = (
        r"Điểm $M\left(0; -\dfrac{1}{3}\right)$ thuộc miền nghiệm của hệ bất phương trình.",
        r"Điểm $M\left(0; -\dfrac{1}{3}\right)$ không thuộc miền nghiệm của hệ bất phương trình.",
        r"Thay $x = 0, y = -\dfrac{1}{3}$ vào hệ: $2(0) + 3\left(-\dfrac{1}{3}\right) - 6 = -7 \le 0$, $0 \ge 0$, $2(0) - 3\left(-\dfrac{1}{3}\right) - 1 = 0 \le 0$. Cả ba đều thỏa mãn.",
        r"Sai vì điểm $M$ thỏa mãn tất cả các bất phương trình trong hệ."
    )
    item_d = (
        r"Miền nghiệm của hệ là miền tam giác (kể cả các cạnh của tam giác).",
        r"Miền nghiệm của hệ là một miền tứ giác không bị giới hạn.",
        r"Ba đường thẳng giới hạn tạo thành một hình tam giác đóng kín kể cả các cạnh.",
        r"Sai vì miền nghiệm là một miền tam giác đóng kín."
    )

    items = [item_a, item_b, item_c, item_d]
    choices, loigiai = make_tf_choices(items)
    return caudan, choices, loigiai


def k10_tf_hbpt_khao_sat_he_2_bpt_va_nghiem():
    """Đúng sai: Khảo sát hệ 2 BPT bậc nhất hai ẩn (ảnh Câu 4 & Câu 5)"""
    caudan = (
        r"Cho hệ bất phương trình $\begin{cases} 2x - y + 2 < 0 \\ 2x + 3y - 6 < 0 \end{cases}$. Khi đó:"
    )

    item_a = (
        r"Hệ đã cho là hệ bất phương trình bậc nhất hai ẩn.",
        r"Hệ đã cho không phải là hệ bất phương trình bậc nhất hai ẩn.",
        r"Tất cả các bất phương trình đều có bậc nhất đối với hai biến $x, y$.",
        r"Sai vì đây là hệ bất phương trình bậc nhất hai ẩn."
    )
    item_b = (
        r"Hệ đã cho có vô số nghiệm.",
        r"Hệ đã cho có một nghiệm duy nhất là $(-2; 1)$.",
        r"Miền nghiệm của hệ là một góc mặt phẳng (giao của hai nửa mặt phẳng mở), do đó có vô số nghiệm.",
        r"Sai vì hệ bất phương trình bậc nhất hai ẩn có miền nghiệm chứa vô số nghiệm, không có nghiệm duy nhất."
    )
    item_c = (
        r"Gốc toạ độ $O(0;0)$ không thuộc miền nghiệm của hệ đã cho.",
        r"Gốc toạ độ $O(0;0)$ thuộc miền nghiệm của hệ đã cho.",
        r"Thay $x=0, y=0$ vào bất phương trình thứ nhất: $2(0) - 0 + 2 = 2 < 0$ (sai). Do đó gốc tọa độ không thuộc miền nghiệm.",
        r"Sai vì $2 < 0$ là vô lý nên gốc tọa độ không thuộc miền nghiệm."
    )
    item_d = (
        r"Điểm $K(-3; 0)$ thuộc miền nghiệm của hệ đã cho.",
        r"Điểm $K(-3; 0)$ không thuộc miền nghiệm của hệ đã cho.",
        r"Thay $x = -3, y = 0$ vào hệ: $2(-3) - 0 + 2 = -4 < 0$ (đúng) và $2(-3) + 3(0) - 6 = -12 < 0$ (đúng).",
        r"Sai vì $K(-3; 0)$ thỏa mãn cả hai bất phương trình của hệ."
    )

    items = [item_a, item_b, item_c, item_d]
    choices, loigiai = make_tf_choices(items)
    return caudan, choices, loigiai


# ==============================================================================
# BỔ SUNG CÁC DẠNG CÓ HÌNH VẼ TIKZ & 4 DẠNG ĐÚNG/SAI MỚI (ẢNH 1-5)
# ==============================================================================

def k10_mc_hbpt_doc_he_bpt_tu_hinh_ve_mien_nghiem():
    """Đọc hệ BPT từ hình vẽ miền nghiệm không tô đậm / không gạch chéo (Ảnh 1 & 3 Câu 11, 12)"""
    case = random.choice([1, 2])
    if case == 1:
        # Miền nghiệm: 2x + y < 3 và x - y > -1 (bờ nét đứt hoặc nét liền)
        is_strict = random.choice([True, False])
        op1 = "<" if is_strict else "\\le"
        op2 = ">" if is_strict else "\\ge"
        op1_opp = ">" if is_strict else "\\ge"
        op2_opp = "<" if is_strict else "\\le"
        line_style = "dashed, thick" if is_strict else "thick"
        shade_desc = "không tô đậm" if is_strict else "không gạch chéo"
        border_desc = "không kể bờ" if is_strict else "kể cả bờ"

        tikz = r"""\begin{tikzpicture}[line cap=round, line join=round, >=stealth, font=\footnotesize, scale=0.65, transform shape]
	\begin{scope}
		\clip (-1.5,-1.2) rectangle (3.2,3.8);
		\draw[gray!30, very thin] (-1.5,-1.2) grid (3.2,3.8);
		\fill[gray!35, opacity=0.65] (-0.4,3.8) -- (2.1,-1.2) -- (3.2,-1.2) -- (3.2,3.8) -- cycle;
		\fill[gray!35, opacity=0.65] (-1.5,-0.5) -- (2.8,3.8) -- (-1.5,3.8) -- cycle;
		\draw[__STYLE__] (-0.4,3.8) -- (2.1,-1.2);
		\draw[__STYLE__] (-1.5,-0.5) -- (2.8,3.8);
	\end{scope}
	\draw[->] (-1.6,0) -- (3.4,0) node[below] {$x$};
	\draw[->] (0,-1.3) -- (0,4.0) node[left] {$y$};
	\node[below left] at (0,0) {$O$};
	\node[left] at (0,3) {$3$};
	\node[left] at (0,1) {$1$};
	\node[above left] at (-1,0) {$-1$};
	\node[below] at (1.5,0) {$\frac{3}{2}$};
\end{tikzpicture}""".replace("__STYLE__", line_style)

        prompt = (
            f"Phần {shade_desc} ({border_desc}) trong hình vẽ bên biểu diễn miền nghiệm của hệ bất phương trình nào trong các hệ bất phương trình sau?"
        )
        caudan = "\\immini{" + prompt + "}{\n" + tikz + "\n}"
        correct = f"$\\begin{{cases}} 2x + y {op1} 3 \\\\ x - y {op2} -1 \\end{{cases}}$"
        wrongs = [
            f"$\\begin{{cases}} 2x + y {op1_opp} 3 \\\\ x - y {op2_opp} -1 \\end{{cases}}$",
            f"$\\begin{{cases}} 2x + y {op1_opp} 3 \\\\ x - y {op2} -1 \\end{{cases}}$",
            f"$\\begin{{cases}} 2x + y {op1} 3 \\\\ x - y {op2_opp} -1 \\end{{cases}}$",
        ]
        loigiai = (
            f"Đường thẳng đi qua $(0; 3)$ và $(\\frac{{3}}{{2}}; 0)$ là $2x + y = 3$; "
            f"đường thẳng đi qua $(-1; 0)$ và $(0; 1)$ là $x - y = -1$.\\\\\n"
            f"Gốc tọa độ $O(0; 0)$ nằm trong phần {shade_desc}: thay $(0;0)$ được $0 < 3$ và $0 > -1$.\\\\\n"
            f"Vậy hệ cần tìm là $\\begin{{cases}} 2x + y {op1} 3 \\\\ x - y {op2} -1 \\end{{cases}}$."
        )
    else:
        # Miền nghiệm: 3x - y < 2 và x + y > 0 (Ảnh 1 & 3 Câu 12)
        is_strict = random.choice([True, False])
        op1 = "<" if is_strict else "\\le"
        op2 = ">" if is_strict else "\\ge"
        op1_opp = ">" if is_strict else "\\ge"
        op2_opp = "<" if is_strict else "\\le"
        line_style = "dashed, thick" if is_strict else "thick"
        shade_desc = "không tô đậm" if is_strict else "không gạch chéo"
        border_desc = "không kể bờ" if is_strict else "kể cả bờ"

        tikz = r"""\begin{tikzpicture}[line cap=round, line join=round, >=stealth, font=\footnotesize, scale=0.65, transform shape]
	\begin{scope}
		\clip (-1.5,-2.8) rectangle (2.6,1.8);
		\draw[gray!30, very thin] (-1.5,-2.8) grid (2.6,1.8);
		\fill[gray!35, opacity=0.65] (-0.266,-2.8) -- (1.266,1.8) -- (2.6,1.8) -- (2.6,-2.8) -- cycle;
		\fill[gray!35, opacity=0.65] (-1.5,1.5) -- (2.6,-2.6) -- (2.6,-2.8) -- (-1.5,-2.8) -- cycle;
		\draw[__STYLE__] (-0.266,-2.8) -- (1.266,1.8);
		\draw[__STYLE__] (-1.5,1.5) -- (2.6,-2.6);
	\end{scope}
	\draw[->] (-1.6,0) -- (2.8,0) node[below] {$x$};
	\draw[->] (0,-2.9) -- (0,2.0) node[left] {$y$};
	\node[below left] at (0,0) {$O$};
	\node[above right] at (0.67,0) {$\frac{2}{3}$};
	\node[left] at (0,-2) {$-2$};
\end{tikzpicture}""".replace("__STYLE__", line_style)

        prompt = (
            f"Phần {shade_desc} ({border_desc}) trong hình vẽ bên biểu diễn miền nghiệm của hệ bất phương trình nào trong các hệ bất phương trình sau?"
        )
        caudan = "\\immini{" + prompt + "}{\n" + tikz + "\n}"
        correct = f"$\\begin{{cases}} 3x - y {op1} 2 \\\\ x + y {op2} 0 \\end{{cases}}$"
        wrongs = [
            f"$\\begin{{cases}} 3x - y {op1_opp} 2 \\\\ x + y {op2_opp} 0 \\end{{cases}}$",
            f"$\\begin{{cases}} 3x + y {op1_opp} -2 \\\\ x + y {op2_opp} 0 \\end{{cases}}$",
            f"$\\begin{{cases}} 3x + y {op1_opp} -2 \\\\ x + y {op2} 0 \\end{{cases}}$",
        ]
        loigiai = (
            f"Đường thẳng đi qua $(\\frac{{2}}{{3}}; 0)$ và $(0; -2)$ là $3x - y = 2$; đường thẳng qua $O(0;0)$ và $(1;-1)$ là $x + y = 0$.\\\\\n"
            f"Điểm $(0; 1)$ thuộc phần {shade_desc}, thay vào được $-1 < 2$ và $1 > 0$.\\\\\n"
            f"Vậy hệ cần tìm là $\\begin{{cases}} 3x - y {op1} 2 \\\\ x + y {op2} 0 \\end{{cases}}$."
        )

    choices, dapan = shuffle_choices(correct, wrongs)
    return caudan, choices, loigiai


# DS 1 (Ảnh 4 Câu 1): Hệ x >= 0, y >= 0, ax + y <= b -> điểm, đếm điểm nguyên, hình tam giác, GTLN
def k10_tf_hbpt_tam_giac_goc_toa_do_diem_nguyen():
    a = random.choice([2, 3])
    b = random.choice([3, 4, 5])
    # Đếm chính xác số điểm nguyên (x, y) thỏa x >= 0, y >= 0, ax + y <= b
    int_pts = []
    for x in range(0, b + 1):
        for y in range(0, b + 1):
            if a * x + y <= b:
                int_pts.append((x, y))
    n_int = len(int_pts)
    n_wrong = n_int - 2 if n_int > 3 else n_int + 2

    # Điểm M(1, 2) luôn có a*1 + 2 >= 4: kiểm tra thuộc hay không
    pt_test = (1, 2)
    is_m_in = (a * pt_test[0] + pt_test[1] <= b)
    m_true_s = f"Điểm $M({pt_test[0]}; {pt_test[1]})$ {'thuộc' if is_m_in else 'không thuộc'} miền nghiệm của hệ bất phương trình đã cho."
    m_false_s = f"Điểm $M({pt_test[0]}; {pt_test[1]})$ {'không thuộc' if is_m_in else 'thuộc'} miền nghiệm của hệ bất phương trình đã cho."

    # Biểu thức F(x; y) = x + c_y * y tại 3 đỉnh (0,0), (b/a, 0), (0, b)
    c_y = random.choice([2, 3])
    f_max = max(0, b / a, c_y * b)
    f_max_int = int(f_max)
    f_wrong = f_max_int + random.choice([2, 3])

    caudan = (
        f"Cho hệ bất phương trình $\\begin{{cases}} x \\ge 0 \\\\ y \\ge 0 \\\\ {a}x + y \\le {b} \\end{{cases}}$."
    )
    item_a = (
        m_true_s,
        m_false_s,
        f"Thay $x = {pt_test[0]}, y = {pt_test[1]}$ vào ${a}x + y \\le {b}$ được ${a + 2}$ {'≤' if is_m_in else '>'} ${b}$.",
        f"Sai vì thay $M({pt_test[0]}; {pt_test[1]})$ vào ${a}x + y$ được ${a + 2}$."
    )
    item_b = (
        f"Miền nghiệm của hệ bất phương trình chứa đúng ${n_int}$ điểm có tọa độ là các số nguyên.",
        f"Miền nghiệm của hệ bất phương trình chứa đúng ${n_wrong}$ điểm có tọa độ là các số nguyên.",
        f"Liệt kê các cặp nguyên $(x; y)$ với $x \\ge 0, y \\ge 0, {a}x + y \\le {b}$: có ${n_int}$ điểm ({', '.join(f'({p[0]};{p[1]})' for p in int_pts)}).",
        f"Sai vì đếm được đúng ${n_int}$ điểm nguyên trong miền nghiệm."
    )
    item_c = (
        r"Miền nghiệm của hệ bất phương trình là một miền tam giác.",
        r"Miền nghiệm của hệ bất phương trình là một miền tứ giác không giới hạn.",
        f"Ba đường thẳng $x = 0$, $y = 0$ và ${a}x + y = {b}$ tạo thành một miền tam giác đóng kín.",
        r"Sai vì miền nghiệm của hệ là một miền tam giác."
    )
    item_d = (
        f"Giá trị lớn nhất của biểu thức $F(x; y) = x + {c_y}y$ với $(x; y)$ thuộc miền nghiệm của hệ bất phương trình là ${f_max_int}$.",
        f"Giá trị lớn nhất của biểu thức $F(x; y) = x + {c_y}y$ với $(x; y)$ thuộc miền nghiệm của hệ bất phương trình là ${f_wrong}$.",
        f"Tính $F$ tại $3$ đỉnh $(0;0)$, $\\left(\\dfrac{{{b}}}{{{a}}}; 0\\right)$, $(0; {b})$ ta được giá trị lớn nhất bằng ${f_max_int}$ (tại $(0; {b})$).",
        f"Sai vì giá trị lớn nhất của $F(x;y)$ trên miền tam giác đạt tại đỉnh $(0; {b})$ bằng ${f_max_int}$."
    )
    choices, loigiai = make_tf_choices([item_a, item_b, item_c, item_d])
    return caudan, choices, loigiai


# DS 2 (Ảnh 4 Câu 2): Bài toán thực tế trồng rau và dưa leo
def k10_tf_hbpt_thuc_te_trong_rau_dua_leo():
    S_area, w1, w2, W_tot, p1, p2 = random.choice([
        (6, 10, 20, 90, 3, 5),   # đỉnh (0, 4.5)->22.5, (3,3)->24, (6,0)->18 => max = 24 tại (3,3)!
        (8, 10, 20, 120, 4, 6),  # đỉnh (0, 6)->36, (4,4)->40, (8,0)->32 => max = 40 tại (4,4)!
        (7, 10, 20, 100, 3, 5),  # đỉnh (0, 5)->25, (4,3)->27, (7,0)->21 => max = 27 tại (4,3)!
    ])
    # Giao điểm x + y = S_area và w1*x + w2*y = W_tot:
    x_opt = (W_tot - w2 * S_area) // (w1 - w2)
    y_opt = S_area - x_opt
    max_profit = p1 * x_opt + p2 * y_opt
    profit_s = str(max_profit)
    profit_wrong = f"{max_profit - 1.5:.1f}".replace(".", "{,}")

    # Kiểm tra phương án (2, S_area - 2)
    feas_x, feas_y = 2, S_area - 2
    is_feas = (w1 * feas_x + w2 * feas_y <= W_tot)

    caudan = (
        f"Một hộ gia đình dự định trồng $x$ ha rau và $y$ ha dưa leo trên một mảnh đất có diện tích ${S_area}$ ha. "
        f"Nếu trồng $1$ ha rau thì cần ${w1}$ ngày công và thu lợi ${p1}$ triệu đồng. "
        f"Nếu trồng $1$ ha dưa leo thì cần ${w2}$ ngày công và thu lợi ${p2}$ triệu đồng. "
        f"Biết rằng hộ gia đình chỉ có thể sử dụng không quá ${W_tot}$ ngày công để trồng rau và dưa leo."
    )
    item_a = (
        f"Hệ bất phương trình bậc nhất hai ẩn thể hiện mối quan hệ giữa $x$ và $y$ là $\\begin{{cases}} x \\ge 0 \\\\ y \\ge 0 \\\\ x + y \\le {S_area} \\\\ {w1}x + {w2}y \\le {W_tot} \\end{{cases}}$.",
        f"Hệ bất phương trình bậc nhất hai ẩn thể hiện mối quan hệ giữa $x$ và $y$ là $\\begin{{cases}} x \\ge 0 \\\\ y \\ge 0 \\\\ x + y \\le {W_tot} \\\\ {w1}x + {w2}y \\le {S_area} \\end{{cases}}$.",
        f"Tổng diện tích $x + y \\le {S_area}$ và tổng ngày công ${w1}x + {w2}y \\le {W_tot}$, với $x \\ge 0, y \\ge 0$.",
        f"Sai vì viết nhầm vế phải của tổng diện tích (${S_area}$) và tổng ngày công (${W_tot}$)."
    )
    item_b = (
        f"Hộ gia đình {'có thể' if is_feas else 'không thể'} trồng ${feas_x}$ ha rau và ${feas_y}$ ha dưa leo trên mảnh đất này.",
        f"Hộ gia đình {'không thể' if is_feas else 'có thể'} trồng ${feas_x}$ ha rau và ${feas_y}$ ha dưa leo trên mảnh đất này.",
        f"Với $x = {feas_x}, y = {feas_y}$: tổng diện tích là ${S_area} \\le {S_area}$, tổng ngày công cần là ${w1*feas_x + w2*feas_y}$ {'≤' if is_feas else '>'} ${W_tot}$.",
        f"Sai vì ${w1}\\cdot {feas_x} + {w2}\\cdot {feas_y} = {w1*feas_x + w2*feas_y}$ {'≤' if is_feas else '>'} ${W_tot}$."
    )
    item_c = (
        f"Hộ gia đình cần trồng ${x_opt}$ ha rau và ${y_opt}$ ha dưa leo để thu được lợi nhuận lớn nhất.",
        f"Hộ gia đình cần trồng ${x_opt + 1}$ ha rau và ${y_opt - 1}$ ha dưa leo để thu được lợi nhuận lớn nhất.",
        f"Xét $F(x; y) = {p1}x + {p2}y$ tại các đỉnh của miền tứ giác nghiệm, giá trị lớn nhất đạt tại $({x_opt}; {y_opt})$.",
        f"Sai vì lợi nhuận lớn nhất đạt tại đỉnh $({x_opt}; {y_opt})$."
    )
    item_d = (
        f"Lợi nhuận lớn nhất hộ gia đình có thể thu được khi trồng rau và dưa leo trên mảnh đất này là ${profit_s}$ triệu đồng.",
        f"Lợi nhuận lớn nhất hộ gia đình có thể thu được khi trồng rau và dưa leo trên mảnh đất này là ${profit_wrong}$ triệu đồng.",
        f"Tại $({x_opt}; {y_opt})$, lợi nhuận lớn nhất là $F({x_opt}; {y_opt}) = {p1}\\cdot {x_opt} + {p2}\\cdot {y_opt} = {profit_s}$ triệu đồng.",
        f"Sai vì $F_{{\\max}} = {profit_s}$ triệu đồng."
    )
    choices, loigiai = make_tf_choices([item_a, item_b, item_c, item_d])
    return caudan, choices, loigiai


# DS 3 (Ảnh 2 Câu 1 - có hình vẽ TikZ): Miền tam giác không gạch chéo trên lưới tọa độ
def k10_tf_hbpt_hinh_ve_tam_giac_diem_nguyen_gtnn():
    # Bộ 3 đỉnh tam giác nguyên đẹp
    p1, p2, p3 = random.choice([
        ((1, 2), (2, 4), (4, 1)),
        ((1, 1), (2, 4), (4, 2)),
        ((1, 2), (3, 4), (4, 1)),
    ])
    # Hàm kiểm tra điểm (x, y) nằm trong hoặc trên biên tam giác p1, p2, p3 bằng tích có hướng
    def sign(pa, pb, pc):
        return (pa[0] - pc[0]) * (pb[1] - pc[1]) - (pb[0] - pc[0]) * (pa[1] - pc[1])
    def in_tri(pt):
        d1 = sign(pt, p1, p2)
        d2 = sign(pt, p2, p3)
        d3 = sign(pt, p3, p1)
        has_neg = (d1 < 0) or (d2 < 0) or (d3 < 0)
        has_pos = (d1 > 0) or (d2 > 0) or (d3 > 0)
        return not (has_neg and has_pos)

    int_pts = [(x, y) for x in range(0, 6) for y in range(0, 6) if in_tri((x, y))]
    n_int = len(int_pts)
    n_wrong = max(2, n_int - 3)

    in_pt = (2, 2) if in_tri((2, 2)) else p1
    out_pt = (3, 3) if not in_tri((3, 3)) else (0, 4)

    c_x = random.choice([29, 20, 15])
    c_y = random.choice([5, 6, 4])
    t_vals = [c_x * p[0] + c_y * p[1] for p in (p1, p2, p3)]
    t_min = min(t_vals)
    t_wrong = t_min - 5

    # Tạo 3 đường thẳng kéo dài qua các cặp đỉnh để vẽ đẹp trong hộp [-0.6, 5.2]
    def ext_line(pa, pb):
        dx, dy = pb[0] - pa[0], pb[1] - pa[1]
        return f"({pa[0] - 2.5*dx:.2f},{pa[1] - 2.5*dy:.2f}) -- ({pb[0] + 2.5*dx:.2f},{pb[1] + 2.5*dy:.2f})"

    tikz = r"""\begin{tikzpicture}[line cap=round, line join=round, >=stealth, font=\footnotesize, scale=0.65, transform shape]
	\begin{scope}
		\clip (-0.6,-0.6) rectangle (5.1,5.1);
		\draw[gray!35, dashed, thin] (-0.6,-0.6) grid (5.1,5.1);
		\fill[pattern=north east lines, pattern color=gray!70, even odd rule] (-0.6,-0.6) rectangle (5.1,5.1) __P1__ -- __P2__ -- __P3__ -- cycle;
		\draw[thick] __L1__;
		\draw[thick] __L2__;
		\draw[thick] __L3__;
	\end{scope}
	\draw[->] (-0.7,0) -- (5.3,0) node[below] {$x$};
	\draw[->] (0,-0.7) -- (0,5.3) node[left] {$y$};
	\node[below left] at (0,0) {$O$};
	\foreach \k in {1,2,3,4} {
		\node[below] at (\k,0) {$\k$};
		\node[left] at (0,\k) {$\k$};
	}
\end{tikzpicture}""".replace("__P1__", str(p1)).replace("__P2__", str(p2)).replace("__P3__", str(p3)).replace("__L1__", ext_line(p1, p2)).replace("__L2__", ext_line(p2, p3)).replace("__L3__", ext_line(p3, p1))

    prompt = (
        "Cho hệ bất phương trình có miền nghiệm là miền tam giác \\textbf{không} gạch chéo như hình vẽ (kể cả bờ các đường thẳng)."
    )
    caudan = "\\immini{" + prompt + "}{\n" + tikz + "\n}"

    item_a = (
        f"Điểm $A({in_pt[0]}; {in_pt[1]})$ thuộc miền nghiệm của hệ bất phương trình đã cho.",
        f"Điểm $A({in_pt[0]}; {in_pt[1]})$ không thuộc miền nghiệm của hệ bất phương trình đã cho.",
        f"Trên hình vẽ, điểm $A({in_pt[0]}; {in_pt[1]})$ nằm trong phần tam giác không gạch chéo nên thuộc miền nghiệm.",
        f"Sai vì điểm $A({in_pt[0]}; {in_pt[1]})$ nằm trong miền nghiệm tam giác."
    )
    item_b = (
        f"Hệ bất phương trình đã cho có đúng ${n_int}$ cặp số $(x_0; y_0)$ (với $x_0, y_0 \\in \\mathbb{{Z}}$) thỏa mãn.",
        f"Hệ bất phương trình đã cho có đúng ${n_wrong}$ cặp số $(x_0; y_0)$ (với $x_0, y_0 \\in \\mathbb{{Z}}$) thỏa mãn.",
        f"Các điểm nguyên nằm trong hoặc trên biên tam giác gồm ${n_int}$ điểm: {', '.join(f'({p[0]};{p[1]})' for p in int_pts)}.",
        f"Sai vì trong miền tam giác (kể cả bờ) có tất cả ${n_int}$ điểm nguyên."
    )
    item_c = (
        f"Điểm $B({out_pt[0]}; {out_pt[1]})$ không thuộc miền nghiệm của hệ bất phương trình đã cho.",
        f"Điểm $B({out_pt[0]}; {out_pt[1]})$ thuộc miền nghiệm của hệ bất phương trình đã cho.",
        f"Trên hình vẽ, điểm $B({out_pt[0]}; {out_pt[1]})$ nằm trong phần bị gạch chéo nên không thuộc miền nghiệm.",
        f"Sai vì điểm $B({out_pt[0]}; {out_pt[1]})$ nằm ngoài miền tam giác nghiệm."
    )
    item_d = (
        f"Biểu thức $T = {c_x}x + {c_y}y$ đạt giá trị bé nhất trên miền nghiệm của hệ bất phương trình đã cho bằng ${t_min}$.",
        f"Biểu thức $T = {c_x}x + {c_y}y$ đạt giá trị bé nhất trên miền nghiệm của hệ bất phương trình đã cho bằng ${t_wrong}$.",
        f"Tính $T$ tại ba đỉnh {p1}, {p2}, {p3} lần lượt được {', '.join(str(v) for v in t_vals)}, nên $T_{{\\min}} = {t_min}$.",
        f"Sai vì giá trị nhỏ nhất của $T$ tại $3$ đỉnh của tam giác là ${t_min}$."
    )
    choices, loigiai = make_tf_choices([item_a, item_b, item_c, item_d])
    return caudan, choices, loigiai


# DS 4 (Ảnh 2 Câu 2): Hệ 4 BPT (miền tứ giác) và GTLN, GTNN của F(x, y)
def k10_tf_hbpt_mien_tu_giac_gtln_gtnn():
    # Bộ các hệ 4 BPT tạo thành miền tứ giác lồi có đỉnh nguyên đẹp
    systems = [
        {
            "he": r"\begin{cases} 3x + 2y \ge 9 \\ x - 2y \le 3 \\ x + y \le 6 \\ x \ge 1 \end{cases}",
            "F": "F(x; y) = 3x - y",
            "fn": lambda x, y: 3 * x - y,
            "verts": [(3, 0), (1, 3), (5, 1), (1, 5)],
            "pt_in": (3, 2),
        },
        {
            "he": r"\begin{cases} x + y \ge 2 \\ x - y \le 2 \\ x + 2y \le 8 \\ x \ge 0 \end{cases}",
            "F": "F(x; y) = 2x + y",
            "fn": lambda x, y: 2 * x + y,
            "verts": [(0, 2), (2, 0), (4, 2), (0, 4)],
            "pt_in": (2, 2),
        },
    ]
    sc = random.choice(systems)
    f_vals = [sc["fn"](x, y) for x, y in sc["verts"]]
    f_max = max(f_vals)
    f_min = min(f_vals)
    pt = sc["pt_in"]

    caudan = (
        f"Cho hệ bất phương trình ${sc['he']}$ và biểu thức ${sc['F']}$ với $(x; y)$ là nghiệm của hệ bất phương trình trên."
    )
    item_a = (
        r"Miền nghiệm của hệ bất phương trình là miền tứ giác.",
        r"Miền nghiệm của hệ bất phương trình là miền tam giác.",
        f"Miền nghiệm của hệ là tứ giác lồi có $4$ đỉnh là {', '.join(f'({x};{y})' for x, y in sc['verts'])}.",
        r"Sai vì miền nghiệm của hệ có $4$ đỉnh tạo thành một miền tứ giác."
    )
    item_b = (
        f"$({pt[0]}; {pt[1]})$ là một nghiệm của hệ bất phương trình.",
        f"$({pt[0]}; {pt[1]})$ không là nghiệm của hệ bất phương trình.",
        f"Thay $x = {pt[0]}, y = {pt[1]}$ vào tất cả $4$ bất phương trình trong hệ đều thỏa mãn.",
        f"Sai vì $({pt[0]}; {pt[1]})$ thỏa mãn cả $4$ bất phương trình của hệ."
    )
    item_c = (
        f"Giá trị lớn nhất của $F(x; y)$ là ${f_max}$.",
        f"Giá trị lớn nhất của $F(x; y)$ là ${f_max - 5}$.",
        f"Tính giá trị $F(x; y)$ tại $4$ đỉnh được {', '.join(str(v) for v in f_vals)}, suy ra $\\max F = {f_max}$.",
        f"Sai vì giá trị lớn nhất của $F(x; y)$ tại các đỉnh là ${f_max}$."
    )
    item_d = (
        f"Giá trị nhỏ nhất của $F(x; y)$ là ${f_min}$.",
        f"Giá trị nhỏ nhất của $F(x; y)$ là ${f_min + 2}$.",
        f"Tính giá trị $F(x; y)$ tại $4$ đỉnh được {', '.join(str(v) for v in f_vals)}, suy ra $\\min F = {f_min}$.",
        f"Sai vì giá trị nhỏ nhất của $F(x; y)$ tại các đỉnh là ${f_min}$."
    )
    choices, loigiai = make_tf_choices([item_a, item_b, item_c, item_d])
    return caudan, choices, loigiai


# ==============================================================================
# BẢNG ÁNH XẠ DẠNG TOÁN & HÀM ĐIỀU PHỐI (DISPATCHER)
# ==============================================================================

K10_BPT_HBPT_MAP = {
    # Bài 3: Bất phương trình bậc nhất hai ẩn
    "Trắc nghiệm - BPT: Nhận biết bất phương trình bậc nhất hai ẩn": (k10_mc_bpt_nhan_biet_bpt_bac_nhat_2_an, "mc"),
    "Trắc nghiệm - BPT: Kiểm tra điểm thuộc hoặc không thuộc miền nghiệm": (k10_mc_bpt_kiem_tra_diem_thuoc_mien_nghiem, "mc"),
    "Trắc nghiệm - BPT: Xác định bất phương trình từ hình vẽ miền nghiệm": (k10_mc_bpt_xac_dinh_bpt_tu_nua_mat_phang, "mc"),
    "Đúng sai - BPT: Khảo sát bất phương trình bậc nhất hai ẩn, điểm và miền nghiệm": (k10_tf_bpt_khao_sat_bpt_bac_nhat_2_an, "tf"),

    # Bài 4: Hệ bất phương trình bậc nhất hai ẩn
    "Trắc nghiệm - Hệ BPT: Nhận biết hệ bất phương trình bậc nhất hai ẩn": (k10_mc_hbpt_nhan_biet_he_bpt_bac_nhat, "mc"),
    "Trắc nghiệm - Hệ BPT: Điểm thuộc miền nghiệm của hệ bất phương trình": (k10_mc_hbpt_diem_thuoc_mien_nghiem, "mc"),
    "Trắc nghiệm - Hệ BPT: Đếm số điểm thuộc miền nghiệm của hệ": (k10_mc_hbpt_dem_so_diem_thuoc_mien_nghiem, "mc"),
    "Trắc nghiệm - Hệ BPT: Xác định hệ bất phương trình từ miền đa giác nghiệm": (k10_mc_hbpt_xac_dinh_he_bpt_tu_tam_giac_mien_nghiem, "mc"),
    "Trắc nghiệm - Hệ BPT: Bài toán thực tế mô hình hóa điều kiện": (k10_mc_hbpt_toan_thuc_te_mo_hinh_hoa, "mc"),
    "Trắc nghiệm - Hệ BPT: Quy hoạch tuyến tính tìm GTLN và GTNN của biểu thức": (k10_mc_hbpt_quy_hoach_tuyen_tinh_max_min, "mc"),
    "Trắc nghiệm - Hệ BPT: Xác định hệ bất phương trình từ hình vẽ miền nghiệm (có hình vẽ)": (k10_mc_hbpt_doc_he_bpt_tu_hinh_ve_mien_nghiem, "mc"),
    "Đúng sai - Hệ BPT: Khảo sát hệ ba bất phương trình và miền tam giác": (k10_tf_hbpt_khao_sat_he_3_bpt, "tf"),
    "Đúng sai - Hệ BPT: Khảo sát hệ hai bất phương trình, điểm và số nghiệm": (k10_tf_hbpt_khao_sat_he_2_bpt_va_nghiem, "tf"),
    "Đúng sai - Hệ BPT: Miền tam giác góc phần tư I, đếm điểm nguyên và GTLN": (k10_tf_hbpt_tam_giac_goc_toa_do_diem_nguyen, "tf"),
    "Đúng sai - Hệ BPT: Bài toán thực tế lập hệ và tối ưu lợi nhuận trồng trọt": (k10_tf_hbpt_thuc_te_trong_rau_dua_leo, "tf"),
    "Đúng sai - Hệ BPT: Miền tam giác không gạch chéo trên hình vẽ, đếm điểm nguyên và GTNN": (k10_tf_hbpt_hinh_ve_tam_giac_diem_nguyen_gtnn, "tf"),
    "Đúng sai - Hệ BPT: Hệ bốn bất phương trình, miền tứ giác và GTLN, GTNN của F(x;y)": (k10_tf_hbpt_mien_tu_giac_gtln_gtnn, "tf"),
}


def dispatch_k10_bpt_hbpt(item):
    """
    Hàm sinh câu hỏi tự động cho Chương II (BPT & Hệ BPT bậc nhất hai ẩn).
    """
    if item not in K10_BPT_HBPT_MAP:
        return None

    fn, q_type = K10_BPT_HBPT_MAP[item]
    if q_type == "mc":
        caudan, choices, loigiai = fn()
        return f"\\begin{{ex}}\n{caudan}\n\\choice\n{''.join(choices)}\\loigiai{{{loigiai}}}\n\\end{{ex}}"
    elif q_type == "tf":
        caudan, choices, loigiai = fn()
        return f"\\begin{{ex}}\n{caudan}\n\\choiceTF\n{''.join(choices)}\\loigiai{{{loigiai}}}\n\\end{{ex}}"
    return None
