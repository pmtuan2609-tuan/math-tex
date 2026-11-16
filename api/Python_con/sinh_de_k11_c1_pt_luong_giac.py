# -*- coding: utf-8 -*-
import random
import math
from fractions import Fraction

def _fmt_frac(n, d):
    if d == 1:
        return str(n)
    if d < 0:
        n, d = -n, -d
    return f"\\frac{{{n}}}{{{d}}}"

def _make_mc_choices(correct, wrongs):
    wrongs_clean = [w for w in wrongs if w != correct]
    random.shuffle(wrongs_clean)
    wrongs_clean = wrongs_clean[:3]
    while len(wrongs_clean) < 3:
        wrongs_clean.append(f"${random.randint(10, 99)}$")
    options = [correct] + wrongs_clean
    random.shuffle(options)
    letters = ["A", "B", "C", "D"]
    formatted = []
    for opt in options:
        formatted.append(f" {opt}\n")
    return formatted

def _make_tf_choices(items):
    choices = []
    for val, text in items:
        prefix = "\\True " if val else ""
        choices.append(f"{prefix}{text}\n")
    return choices

# ==============================================================================
# PHẦN 1: TRẮC NGHIỆM NHIỀU LỰA CHỌN (MC)
# ==============================================================================

def k11_mc_c1_ptlg_cot3x_bang_cotx():
    """MC: Phương trình cot 3x = cot x hoặc tan 3x = tan x kết hợp ĐK xác định."""
    caudan = "Phương trình $\\cot 3x = \\cot x$ có các nghiệm là:"
    correct = "$x = \\frac{\\pi}{2} + k\\pi, k \\in \\mathbb{Z}$"
    wrongs = [
        "$x = \\frac{k\\pi}{2}, k \\in \\mathbb{Z}$",
        "$x = k\\pi, k \\in \\mathbb{Z}$",
        "$x = \\frac{\\pi}{2} + k2\\pi, k \\in \\mathbb{Z}$"
    ]
    choices = _make_mc_choices(correct, wrongs)
    loigiai = (
        "Điều kiện xác định: $\\begin{cases} \\sin 3x \\neq 0 \\\\ \\sin x \\neq 0 \\end{cases} "
        "\\Leftrightarrow \\begin{cases} 3x \\neq k\\pi \\\\ x \\neq k\\pi \\end{cases} "
        "\\Leftrightarrow x \\neq \\frac{k\\pi}{3}$.\n\n"
        "Phương trình tương đương: $3x = x + k\\pi \\Leftrightarrow 2x = k\\pi \\Leftrightarrow x = \\frac{k\\pi}{2}, k \\in \\mathbb{Z}$.\n\n"
        "Kết hợp điều kiện:\n"
        "- Nếu $k = 2m$ (chẵn) thì $x = m\\pi$, khi đó $\\sin x = 0$ (loại).\n"
        "- Nếu $k = 2m + 1$ (lẻ) thì $x = \\frac{\\pi}{2} + m\\pi$ thỏa mãn điều kiện.\n\n"
        "Vậy nghiệm của phương trình là $x = \\frac{\\pi}{2} + k\\pi, k \\in \\mathbb{Z}$."
    )
    return caudan, choices, loigiai

def k11_mc_c1_ptlg_tan3x_bang_tanx():
    """MC: Phương trình tan 3x = tan x kết hợp ĐK xác định."""
    caudan = "Phương trình $\\tan 3x = \\tan x$ có họ nghiệm là:"
    correct = "$x = k\\pi, k \\in \\mathbb{Z}$"
    wrongs = [
        "$x = \\frac{k\\pi}{2}, k \\in \\mathbb{Z}$",
        "$x = k2\\pi, k \\in \\mathbb{Z}$",
        "$x = \\frac{k\\pi}{6}, k \\in \\mathbb{Z}$"
    ]
    choices = _make_mc_choices(correct, wrongs)
    loigiai = (
        "Điều kiện: $\\cos 3x \\neq 0$ và $\\cos x \\neq 0$.\n"
        "Phương trình $\\Leftrightarrow 3x = x + k\\pi \\Leftrightarrow 2x = k\\pi \\Leftrightarrow x = \\frac{k\\pi}{2}$.\n"
        "Loại đi các điểm làm mẫu bằng $0$ ($x = \\frac{\\pi}{2} + m\\pi$), ta còn lại các nghiệm $x = k\\pi, k \\in \\mathbb{Z}$."
    )
    return caudan, choices, loigiai

def k11_mc_c1_ptlg_so_nghiem_doan_lon():
    """MC: Số nghiệm của phương trình cot 20x = 1 trên đoạn [-50pi; 0]."""
    caudan = "Số nghiệm của phương trình $\\cot 20x = 1$ trên đoạn $[-50\\pi; 0]$ là:"
    ans = 1000
    correct = f"${ans}$"
    wrongs = [f"${ans + 1}$", f"${ans - 19}$", f"${ans - 20}$"]
    choices = _make_mc_choices(correct, wrongs)
    loigiai = (
        "Phương trình $\\cot 20x = 1 \\Leftrightarrow 20x = \\frac{\\pi}{4} + k\\pi "
        "\\Leftrightarrow x = \\frac{\\pi}{80} + \\frac{k\\pi}{20}, k \\in \\mathbb{Z}$.\n\n"
        "Vì $x \\in [-50\\pi; 0]$ nên:\n"
        "$$-50\\pi \\le \\frac{\\pi}{80} + \\frac{k\\pi}{20} \\le 0 "
        "\\Leftrightarrow -50 \\le \\frac{1}{80} + \\frac{k}{20} \\le 0 "
        "\\Leftrightarrow -1000 - 0{,}25 \\le k \\le -0{,}25.$$\n\n"
        "Do $k \\in \\mathbb{Z}$ nên $k \\in \\{-1000; -999; \\dots; -1\\}$.\n"
        "Số giá trị của $k$ là: $-1 - (-1000) + 1 = 1000$ nghiệm."
    )
    return caudan, choices, loigiai

def k11_mc_c1_ptlg_so_nghiem_khoang_0_3pi():
    """MC: Số nghiệm của phương trình sin 2x = sqrt(3)/2 trong khoảng (0; 3pi)."""
    caudan = "Số nghiệm của phương trình $\\sin 2x = \\frac{\\sqrt{3}}{2}$ trong khoảng $(0; 3\\pi)$ là:"
    ans = 6
    correct = f"${ans}$"
    wrongs = ["$2$", "$4$", "$1$"]
    choices = _make_mc_choices(correct, wrongs)
    loigiai = (
        "Ta có: $\\sin 2x = \\sin\\frac{\\pi}{3} \\Leftrightarrow "
        "\\left[\\begin{array}{l} 2x = \\frac{\\pi}{3} + k2\\pi \\\\ 2x = \\frac{2\\pi}{3} + k2\\pi \\end{array}\\right. "
        "\\Leftrightarrow \\left[\\begin{array}{l} x = \\frac{\\pi}{6} + k\\pi \\\\ x = \\frac{\\pi}{3} + k\\pi \\end{array}\\right. (k \\in \\mathbb{Z})$.\n\n"
        "Do $x \\in (0; 3\\pi)$:\n"
        "- Với $x = \\frac{\\pi}{6} + k\\pi$: $0 < \\frac{1}{6} + k < 3 \\Leftrightarrow -\\frac{1}{6} < k < \\frac{17}{6} \\Rightarrow k \\in \\{0; 1; 2\\}$ (3 nghiệm).\n"
        "- Với $x = \\frac{\\pi}{3} + k\\pi$: $0 < \\frac{1}{3} + k < 3 \\Leftrightarrow -\\frac{1}{3} < k < \\frac{8}{3} \\Rightarrow k \\in \\{0; 1; 2\\}$ (3 nghiệm).\n\n"
        "Các nghiệm này đôi một khác nhau. Vậy phương trình có tất cả $3 + 3 = 6$ nghiệm."
    )
    return caudan, choices, loigiai

def k11_mc_c1_ptlg_tong_nghiem_cot_doan():
    """MC: Tổng tất cả các nghiệm của phương trình cot x = sqrt(3) trên đoạn [0; 2pi]."""
    caudan = "Tổng tất cả các nghiệm của phương trình $\\cot x = \\sqrt{3}$ trên đoạn $[0; 2\\pi]$ bằng:"
    correct = "$\\frac{4\\pi}{3}$"
    wrongs = ["$\\frac{7\\pi}{6}$", "$\\frac{5\\pi}{6}$", "$\\frac{\\pi}{6}$"]
    choices = _make_mc_choices(correct, wrongs)
    loigiai = (
        "Điều kiện: $\\sin x \\neq 0 \\Leftrightarrow x \\neq k\\pi$.\n"
        "Phương trình $\\cot x = \\sqrt{3} = \\cot\\frac{\\pi}{6} \\Leftrightarrow x = \\frac{\\pi}{6} + k\\pi, k \\in \\mathbb{Z}$.\n\n"
        "Trên đoạn $[0; 2\\pi]$, ta có hai nghiệm tương ứng là $k = 0 \\Rightarrow x_1 = \\frac{\\pi}{6}$ và $k = 1 \\Rightarrow x_2 = \\frac{7\\pi}{6}$.\n\n"
        "Tổng các nghiệm là:\n"
        "$$S = x_1 + x_2 = \\frac{\\pi}{6} + \\frac{7\\pi}{6} = \\frac{8\\pi}{6} = \\frac{4\\pi}{3}.$$"
    )
    return caudan, choices, loigiai

def k11_mc_c1_ptlg_tong_nghiem_do_tan():
    """MC: Tổng các nghiệm phương trình tan(2x - 15°) = 1 trên khoảng (-90°; 90°)."""
    caudan = "Tổng các nghiệm của phương trình $\\tan(2x - 15^\\circ) = 1$ trên khoảng $(-90^\\circ; 90^\\circ)$ bằng:"
    correct = "$-30^\\circ$"
    wrongs = ["$30^\\circ$", "$-60^\\circ$", "$0^\\circ$"]
    choices = _make_mc_choices(correct, wrongs)
    loigiai = (
        "Phương trình $\\tan(2x - 15^\\circ) = 1 \\Leftrightarrow 2x - 15^\\circ = 45^\\circ + k180^\\circ "
        "\\Leftrightarrow 2x = 60^\\circ + k180^\\circ \\Leftrightarrow x = 30^\\circ + k90^\\circ, k \\in \\mathbb{Z}$.\n\n"
        "Vì $x \\in (-90^\\circ; 90^\\circ)$ nên $-90^\\circ < 30^\\circ + k90^\\circ < 90^\\circ "
        "\\Leftrightarrow -120^\\circ < k90^\\circ < 60^\\circ \\Leftrightarrow -\\frac{4}{3} < k < \\frac{2}{3}$.\n\n"
        "Do $k \\in \\mathbb{Z}$ nên $k \\in \\{-1; 0\\}$:\n"
        "- Với $k = -1 \\Rightarrow x = -60^\\circ$.\n"
        "- Với $k = 0 \\Rightarrow x = 30^\\circ$.\n\n"
        "Tổng các nghiệm là: $(-60^\\circ) + 30^\\circ = -30^\\circ$."
    )
    return caudan, choices, loigiai

def k11_mc_c1_ptlg_cos_u_bang_cos_v_tong_nghiem():
    """MC: Tìm tổng các nghiệm của cos(5x - pi/6) = cos(2x - pi/3) trên [0; pi]."""
    caudan = "Tìm tổng các nghiệm của phương trình $\\cos\\left(5x - \\frac{\\pi}{6}\\right) = \\cos\\left(2x - \\frac{\\pi}{3}\\right)$ trên đoạn $[0; \\pi]$."
    correct = "$\\frac{47\\pi}{18}$"
    wrongs = ["$\\frac{4\\pi}{18}$", "$\\frac{45\\pi}{18}$", "$\\frac{7\\pi}{18}$"]
    choices = _make_mc_choices(correct, wrongs)
    loigiai = (
        "Phương trình tương đương:\n"
        "$$\\left[\\begin{array}{l} 5x - \\frac{\\pi}{6} = 2x - \\frac{\\pi}{3} + k2\\pi \\\\ "
        "5x - \\frac{\\pi}{6} = -2x + \\frac{\\pi}{3} + k2\\pi \\end{array}\\right. "
        "\\Leftrightarrow \\left[\\begin{array}{l} 3x = -\\frac{\\pi}{6} + k2\\pi \\\\ "
        "7x = \\frac{\\pi}{2} + k2\\pi \\end{array}\\right. "
        "\\Leftrightarrow \\left[\\begin{array}{l} x = -\\frac{\\pi}{18} + \\frac{k2\\pi}{3} \\\\ "
        "x = \\frac{\\pi}{14} + \\frac{k2\\pi}{7} \\end{array}\\right.$$\n\n"
        "Tìm các nghiệm trên đoạn $[0; \\pi]$ rồi tính tổng ta được kết quả là $\\frac{47\\pi}{18}$."
    )
    return caudan, choices, loigiai

def k11_mc_c1_ptlg_tham_so_m_tong_nguyen():
    """MC: Gọi S là tập tất cả giá trị nguyên m để cos(2x - pi/3) - m = 2 có nghiệm. Tính tổng T."""
    caudan = (
        "Gọi $S$ là tập hợp tất cả các giá trị nguyên của tham số $m$ để phương trình "
        "$\\cos\\left(2x - \\frac{\\pi}{3}\\right) - m = 2$ có nghiệm. Tính tổng $T$ của các phần tử trong $S$."
    )
    ans = -6
    correct = f"$T = {ans}$"
    wrongs = ["$T = 6$", "$T = 3$", "$T = -2$"]
    choices = _make_mc_choices(correct, wrongs)
    loigiai = (
        "Phương trình tương đương: $\\cos\\left(2x - \\frac{\\pi}{3}\\right) = m + 2$.\n\n"
        "Phương trình có nghiệm khi và chỉ khi:\n"
        "$$-1 \\le m + 2 \\le 1 \\Leftrightarrow -3 \\le m \\le -1.$$\n\n"
        "Vì $m \\in \\mathbb{Z}$ nên $S = \\{-3; -2; -1\\}$.\n"
        "Tổng các phần tử trong $S$ là: $T = (-3) + (-2) + (-1) = -6$."
    )
    return caudan, choices, loigiai

# ==============================================================================
# PHẦN 2: TRẮC NGHIỆM ĐÚNG SAI (TF)
# ==============================================================================

def k11_tf_c1_ptlg_cos2x_bang_0():
    """TF: Cho phương trình cos 2x = 0. Xét tính đúng sai."""
    caudan = "Cho phương trình $\\cos 2x = 0$. Xét tính đúng sai của các khẳng định sau:"
    items = [
        (False, "$x = 0$ là một nghiệm của phương trình."),
        (False, "Nghiệm của phương trình là $x = \\frac{\\pi}{2} + k\\pi, k \\in \\mathbb{Z}$."),
        (True, "Phương trình có cùng tập nghiệm với phương trình $\\cos^2 x = \\frac{1}{2}$."),
        (False, "Trên khoảng $(0; 2\\pi)$, phương trình có đúng 2 nghiệm.")
    ]
    choices = _make_tf_choices(items)
    loigiai = (
        "\\begin{itemchoice}\n"
        "\\itemch Sai. Thay $x = 0$ vào phương trình: $\\cos 0 = 1 \\neq 0$.\n"
        "\\itemch Sai. Ta có $\\cos 2x = 0 \\Leftrightarrow 2x = \\frac{\\pi}{2} + k\\pi \\Leftrightarrow x = \\frac{\\pi}{4} + \\frac{k\\pi}{2}, k \\in \\mathbb{Z}$.\n"
        "\\itemch Đúng. Ta có $\\cos 2x = 2\\cos^2 x - 1 = 0 \\Leftrightarrow \\cos^2 x = \\frac{1}{2}$. Do đó hai phương trình có cùng tập nghiệm.\n"
        "\\itemch Sai. Trên $(0; 2\\pi)$, các nghiệm là $x \\in \\{\\frac{\\pi}{4}; \\frac{3\\pi}{4}; \\frac{5\\pi}{4}; \\frac{7\\pi}{4}\\}$ (có đúng 4 nghiệm).\n"
        "\\end{itemchoice}"
    )
    return caudan, choices, loigiai

def k11_tf_c1_ptlg_sinx_bang_cosx():
    """TF: Cho phương trình sin x = cos x. Xét tính đúng sai."""
    caudan = "Cho phương trình $\\sin x = \\cos x$. Xét tính đúng sai của các khẳng định sau:"
    items = [
        (False, "$x = \\frac{3\\pi}{4}$ là một nghiệm của phương trình."),
        (False, "Nghiệm của phương trình là $x = \\frac{\\pi}{2} + k2\\pi, k \\in \\mathbb{Z}$."),
        (True, "Phương trình có cùng tập nghiệm với phương trình $\\tan x = 1$."),
        (True, "Trên khoảng $(0; 2\\pi)$, phương trình có đúng 2 nghiệm.")
    ]
    choices = _make_tf_choices(items)
    loigiai = (
        "\\begin{itemchoice}\n"
        "\\itemch Sai. Tại $x = \\frac{3\\pi}{4}$, $\\sin\\frac{3\\pi}{4} = \\frac{\\sqrt{2}}{2}$ còn $\\cos\\frac{3\\pi}{4} = -\\frac{\\sqrt{2}}{2} \\neq \\sin\\frac{3\\pi}{4}$.\n"
        "\\itemch Sai. Ta có $\\sin x = \\cos x \\Leftrightarrow \\sin\\left(x - \\frac{\\pi}{4}\\right) = 0 \\Leftrightarrow x = \\frac{\\pi}{4} + k\\pi, k \\in \\mathbb{Z}$.\n"
        "\\itemch Đúng. Vì $\\cos x = 0$ không thỏa mãn phương trình nên chia hai vế cho $\\cos x$ ta được $\\tan x = 1$.\n"
        "\\itemch Đúng. Trên khoảng $(0; 2\\pi)$, phương trình có 2 nghiệm là $x = \\frac{\\pi}{4}$ và $x = \\frac{5\\pi}{4}$.\n"
        "\\end{itemchoice}"
    )
    return caudan, choices, loigiai

def k11_tf_c1_ptlg_sin2x_am():
    """TF: Cho phương trình sin 2x = -1/2 (*). Khi đó xét tính đúng sai."""
    caudan = "Cho phương trình lượng giác $\\sin 2x = -\\frac{1}{2}$ (*). Khi đó, xét tính đúng sai của các mệnh đề sau:"
    items = [
        (False, "Phương trình (*) tương đương $\\sin 2x = \\sin\\frac{\\pi}{6}$."),
        (False, "Trong khoảng $(0; \\pi)$ phương trình có 3 nghiệm."),
        (True, "Tổng các nghiệm của phương trình trong khoảng $(0; \\pi)$ bằng $\\frac{3\\pi}{2}$."),
        (True, "Trong khoảng $(0; \\pi)$ phương trình đã cho có nghiệm lớn nhất bằng $\\frac{11\\pi}{12}$.")
    ]
    choices = _make_tf_choices(items)
    loigiai = (
        "\\begin{itemchoice}\n"
        "\\itemch Sai. Vì $-\\frac{1}{2} = \\sin\\left(-\\frac{\\pi}{6}\\right)$, do đó $\\sin 2x = \\sin\\left(-\\frac{\\pi}{6}\\right)$.\n"
        "\\itemch Sai. Ta có nghiệm: $x = -\\frac{\\pi}{12} + k\\pi$ hoặc $x = \\frac{7\\pi}{12} + k\\pi$. "
        "Trong khoảng $(0; \\pi)$ có 2 nghiệm là $x = \\frac{7\\pi}{12}$ và $x = \\frac{11\\pi}{12}$.\n"
        "\\itemch Đúng. Tổng các nghiệm trong $(0; \\pi)$ là: $\\frac{7\\pi}{12} + \\frac{11\\pi}{12} = \\frac{18\\pi}{12} = \\frac{3\\pi}{2}$.\n"
        "\\itemch Đúng. Trong hai nghiệm trên thì nghiệm lớn nhất là $\\frac{11\\pi}{12}$.\n"
        "\\end{itemchoice}"
    )
    return caudan, choices, loigiai

def k11_tf_c1_ptlg_sin_u_bang_sin_v():
    """TF: Cho phương trình sin(2x - pi/4) = sin(x + 3pi/4)."""
    caudan = "Cho phương trình $\\sin\\left(2x - \\frac{\\pi}{4}\\right) = \\sin\\left(x + \\frac{3\\pi}{4}\\right)$ (*). Khi đó:"
    items = [
        (False, "Phương trình có nghiệm là $\\left[\\begin{array}{l} x = \\pi + k2\\pi \\\\ x = \\frac{\\pi}{6} + k\\frac{2\\pi}{3} \\end{array}\\right. (k \\in \\mathbb{Z})$."),
        (True, "Trong khoảng $(0; \\pi)$ phương trình có 2 nghiệm."),
        (False, "Tổng các nghiệm của phương trình trong khoảng $(0; \\pi)$ bằng $\\frac{7\\pi}{6}$."),
        (True, "Trong khoảng $(0; \\pi)$ phương trình có nghiệm lớn nhất bằng $\\frac{5\\pi}{6}$.")
    ]
    choices = _make_tf_choices(items)
    loigiai = (
        "\\begin{itemchoice}\n"
        "\\itemch Sai. Phương trình $\\Leftrightarrow \\left[\\begin{array}{l} 2x - \\frac{\\pi}{4} = x + \\frac{3\\pi}{4} + k2\\pi \\\\ "
        "2x - \\frac{\\pi}{4} = \\pi - \\left(x + \\frac{3\\pi}{4}\\right) + k2\\pi \\end{array}\\right. "
        "\\Leftrightarrow \\left[\\begin{array}{l} x = \\pi + k2\\pi \\\\ 3x = \\frac{\\pi}{2} + k2\\pi \\end{array}\\right. "
        "\\Leftrightarrow \\left[\\begin{array}{l} x = \\pi + k2\\pi \\\\ x = \\frac{\\pi}{6} + \\frac{k2\\pi}{3} \\end{array}\\right. (k \\in \\mathbb{Z})$.\n"
        "\\itemch Đúng. Trong $(0; \\pi)$, họ thứ nhất không có nghiệm; họ thứ hai có 2 nghiệm là $x_1 = \\frac{\\pi}{6}, x_2 = \\frac{5\\pi}{6}$.\n"
        "\\itemch Sai. Tổng các nghiệm trong $(0; \\pi)$ là $\\frac{\\pi}{6} + \\frac{5\\pi}{6} = \\pi \\neq \\frac{7\\pi}{6}$.\n"
        "\\itemch Đúng. Nghiệm lớn nhất trong khoảng $(0; \\pi)$ là $\\frac{5\\pi}{6}$.\n"
        "\\end{itemchoice}"
    )
    return caudan, choices, loigiai

def k11_tf_c1_ptlg_2sinx_can2():
    """TF: Cho phương trình 2sin x = sqrt(2)."""
    caudan = "Cho phương trình lượng giác $2\\sin x = \\sqrt{2}$. Khi đó, xét tính đúng sai của các khẳng định sau:"
    items = [
        (True, "Phương trình tương đương $\\sin x = \\sin\\frac{\\pi}{4}$."),
        (False, "Phương trình có nghiệm là $x = \\frac{\\pi}{3} + k2\\pi; x = \\frac{3\\pi}{4} + k2\\pi (k \\in \\mathbb{Z})$."),
        (True, "Phương trình đã cho có nghiệm dương nhỏ nhất bằng $\\frac{\\pi}{4}$."),
        (False, "Số nghiệm của phương trình trong khoảng $\\left(-\\frac{\\pi}{2}; \\frac{\\pi}{2}\\right)$ là hai nghiệm.")
    ]
    choices = _make_tf_choices(items)
    loigiai = (
        "\\begin{itemchoice}\n"
        "\\itemch Đúng. Ta có $2\\sin x = \\sqrt{2} \\Leftrightarrow \\sin x = \\frac{\\sqrt{2}}{2} = \\sin\\frac{\\pi}{4}$.\n"
        "\\itemch Sai. Nghiệm đúng phải là $x = \\frac{\\pi}{4} + k2\\pi$ và $x = \\frac{3\\pi}{4} + k2\\pi (k \\in \\mathbb{Z})$.\n"
        "\\itemch Đúng. Cho $k = 0$ ta được nghiệm dương nhỏ nhất là $x = \\frac{\\pi}{4}$.\n"
        "\\itemch Sai. Trong khoảng $\\left(-\\frac{\\pi}{2}; \\frac{\\pi}{2}\\right)$, chỉ có đúng 1 nghiệm là $x = \\frac{\\pi}{4}$.\n"
        "\\end{itemchoice}"
    )
    return caudan, choices, loigiai

def k11_tf_c1_ptlg_tan_do():
    """TF: Cho phương trình tan(2x - 15°) = 1."""
    caudan = "Cho phương trình lượng giác $\\tan(2x - 15^\\circ) = 1$ (*). Khi đó:"
    items = [
        (True, "Phương trình (*) có nghiệm $\\tan(2x - 15^\\circ) = 1 \\Leftrightarrow x = 30^\\circ + k90^\\circ (k \\in \\mathbb{Z})$."),
        (False, "Phương trình có nghiệm âm lớn nhất bằng $-30^\\circ$."),
        (False, "Tổng các nghiệm của phương trình trong khoảng $(-180^\\circ; 90^\\circ)$ bằng $180^\\circ$."),
        (True, "Trong khoảng $(-180^\\circ; 90^\\circ)$ phương trình có nghiệm lớn nhất bằng $30^\\circ$.")
    ]
    choices = _make_tf_choices(items)
    loigiai = (
        "\\begin{itemchoice}\n"
        "\\itemch Đúng. Ta có $2x - 15^\\circ = 45^\\circ + k180^\\circ \\Leftrightarrow 2x = 60^\\circ + k180^\\circ \\Leftrightarrow x = 30^\\circ + k90^\\circ$.\n"
        "\\itemch Sai. Với $k = -1 \\Rightarrow x = -60^\\circ$ là nghiệm âm lớn nhất.\n"
        "\\itemch Sai. Trong khoảng $(-180^\\circ; 90^\\circ)$, các nghiệm là: $x \\in \\{-150^\\circ; -60^\\circ; 30^\\circ\\}$. Tổng bằng $-180^\\circ$.\n"
        "\\itemch Đúng. Nghiệm lớn nhất trong khoảng $(-180^\\circ; 90^\\circ)$ là $x = 30^\\circ$.\n"
        "\\end{itemchoice}"
    )
    return caudan, choices, loigiai

def k11_tf_c1_ptlg_cos2_x_bang_nua():
    """TF: Cho phương trình cos^2 x = 1/2."""
    caudan = "Cho phương trình $\\cos^2 x = \\frac{1}{2}$. Khi đó, xét tính đúng sai của các khẳng định sau:"
    items = [
        (True, "$x = \\frac{\\pi}{4}$ là một nghiệm của phương trình."),
        (True, "Tập nghiệm của phương trình là $S = \\left\\{\\frac{\\pi}{4} + \\frac{k\\pi}{2}, k \\in \\mathbb{Z}\\right\\}$."),
        (False, "Phương trình có ba nghiệm trong đoạn $[0; \\pi]$."),
        (False, "Tổng các nghiệm của phương trình trong đoạn $[0; \\pi]$ là $\\frac{3\\pi}{2}$.")
    ]
    choices = _make_tf_choices(items)
    loigiai = (
        "\\begin{itemchoice}\n"
        "\\itemch Đúng. $\\cos^2\\frac{\\pi}{4} = \\left(\\frac{\\sqrt{2}}{2}\\right)^2 = \\frac{1}{2}$.\n"
        "\\itemch Đúng. Ta có $\\cos^2 x = \\frac{1}{2} \\Leftrightarrow \\frac{1 + \\cos 2x}{2} = \\frac{1}{2} \\Leftrightarrow \\cos 2x = 0 \\Leftrightarrow x = \\frac{\\pi}{4} + \\frac{k\\pi}{2}, k \\in \\mathbb{Z}$.\n"
        "\\itemch Sai. Trong đoạn $[0; \\pi]$ phương trình có 2 nghiệm là $x = \\frac{\\pi}{4}$ và $x = \\frac{3\\pi}{4}$.\n"
        "\\itemch Sai. Tổng hai nghiệm trong $[0; \\pi]$ là $\\frac{\\pi}{4} + \\frac{3\\pi}{4} = \\pi \\neq \\frac{3\\pi}{2}$.\n"
        "\\end{itemchoice}"
    )
    return caudan, choices, loigiai

# ==============================================================================
# PHẦN 3: TRẮC NGHIỆM TRẢ LỜI NGẮN (SA)
# ==============================================================================

def k11_sa_c1_ptlg_tong_nghiem_cot_doan():
    """SA: Tính tổng các nghiệm của phương trình cot x = sqrt(3) trên [0; 2pi]."""
    caudan = (
        "Tính tổng các nghiệm của phương trình $\\cot x = \\sqrt{3}$ trên đoạn $[0; 2\\pi]$ "
        "(viết kết quả dưới dạng $k\\pi$, điền giá trị của $k$, làm tròn đến hàng phần trăm nếu cần)."
    )
    # S = pi/6 + 7pi/6 = 4/3 pi approx 1.33 pi
    ans = "1.33"
    loigiai = (
        "Phương trình $\\cot x = \\sqrt{3} \\Leftrightarrow x = \\frac{\\pi}{6} + k\\pi, k \\in \\mathbb{Z}$.\n"
        "Các nghiệm thuộc $[0; 2\\pi]$ là $x_1 = \\frac{\\pi}{6}$ và $x_2 = \\frac{7\\pi}{6}$.\n"
        "Tổng các nghiệm: $S = \\frac{\\pi}{6} + \\frac{7\\pi}{6} = \\frac{4\\pi}{3} \\approx 1{,}33\\pi$. Do đó $k \\approx 1{,}33$."
    )
    return caudan, ans, loigiai

def k11_sa_c1_ptlg_so_nghiem_khoang_0_3pi():
    """SA: Tìm số nghiệm của phương trình sin 2x = sqrt(3)/2 trong khoảng (0; 3pi)."""
    caudan = "Tìm số nghiệm của phương trình $\\sin 2x = \\frac{\\sqrt{3}}{2}$ trong khoảng $(0; 3\\pi)$."
    ans = "6"
    loigiai = (
        "Phương trình $\\sin 2x = \\sin\\frac{\\pi}{3} \\Leftrightarrow "
        "x = \\frac{\\pi}{6} + k\\pi$ hoặc $x = \\frac{\\pi}{3} + k\\pi$.\n"
        "Trong khoảng $(0; 3\\pi)$, mỗi họ nghiệm cho đúng $3$ nghiệm ($k \\in \\{0; 1; 2\\}$).\n"
        "Vì hai họ nghiệm không có phần tử chung nên số nghiệm là $3 + 3 = 6$."
    )
    return caudan, ans, loigiai

def k11_sa_c1_ptlg_tham_so_m_tong_nguyen():
    """SA: Tính tổng các giá trị nguyên m để cos(2x - pi/3) - m = 2 có nghiệm."""
    caudan = (
        "Gọi $S$ là tập hợp tất cả các giá trị nguyên của tham số $m$ để phương trình "
        "$\\cos\\left(2x - \\frac{\\pi}{3}\\right) - m = 2$ có nghiệm. Tính tổng các phần tử trong $S$."
    )
    ans = "-6"
    loigiai = (
        "Phương trình tương đương $\\cos\\left(2x - \\frac{\\pi}{3}\\right) = m + 2$.\n"
        "Để phương trình có nghiệm: $-1 \\le m + 2 \\le 1 \\Leftrightarrow -3 \\le m \\le -1$.\n"
        "Các giá trị nguyên của $m$ là: $m \\in \\{-3; -2; -1\\}$.\n"
        "Tổng các phần tử: $(-3) + (-2) + (-1) = -6$."
    )
    return caudan, ans, loigiai

def k11_sa_c1_ptlg_tong_nghiem_do_tan():
    """SA: Tính tổng các nghiệm (theo đơn vị độ) của tan(2x - 15°) = 1 trên khoảng (-90°; 90°)."""
    caudan = "Tính tổng các nghiệm (theo đơn vị độ) của phương trình $\\tan(2x - 15^\\circ) = 1$ trên khoảng $(-90^\\circ; 90^\\circ)$."
    ans = "-30"
    loigiai = (
        "Phương trình $\\Leftrightarrow 2x - 15^\\circ = 45^\\circ + k180^\\circ \\Leftrightarrow x = 30^\\circ + k90^\\circ$.\n"
        "Trên $(-90^\\circ; 90^\\circ)$, các nghiệm là $x_1 = -60^\\circ$ ($k = -1$) và $x_2 = 30^\\circ$ ($k = 0$).\n"
        "Tổng các nghiệm: $(-60^\\circ) + 30^\\circ = -30^\\circ$."
    )
    return caudan, ans, loigiai
