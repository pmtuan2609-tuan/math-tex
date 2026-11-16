# -*- coding: utf-8 -*-
"""
Module sinh đề Toán 11 Học kì 2 - Bộ Đề Ôn Theo Chương (GV: Ngô Đức Tài)
Bao gồm:
- CHƯƠNG VI: Hàm số mũ và hàm số lôgarit (MC, TF, SA)
- CHƯƠNG VIII: Các quy tắc tính xác suất (MC, TF, SA)
- CHƯƠNG IX: Đạo hàm (MC, TF, SA)
"""

import random
import math
from fractions import Fraction

def _fmt_frac(n, d):
    f = Fraction(n, d)
    if f.denominator == 1:
        return str(f.numerator)
    return f"\\frac{{{f.numerator}}}{{{f.denominator}}}"

def _make_mc_choices(correct_ans, wrong_answers):
    # Trộn 4 đáp án và gắn \True vào đáp án đúng
    unique_wrongs = []
    for w in wrong_answers:
        if w != correct_ans and w not in unique_wrongs:
            unique_wrongs.append(w)
        if len(unique_wrongs) == 3:
            break
    while len(unique_wrongs) < 3:
        unique_wrongs.append(f"{correct_ans} + {len(unique_wrongs)+1}")
    
    items = [(True, correct_ans)] + [(False, w) for w in unique_wrongs]
    random.shuffle(items)
    res = []
    for is_true, val in items:
        prefix = "\\True " if is_true else ""
        res.append(f"{{{prefix}{val}}} ")
    return res

def _make_tf_choices(items_data):
    # items_data: list of (is_true, text)
    res = []
    for is_true, text in items_data:
        prefix = "\\True " if is_true else ""
        res.append(f"{{{prefix}{text}}} ")
    return res

# =========================================================================
# I. CHƯƠNG VI: HÀM SỐ MŨ VÀ HÀM SỐ LÔGARIT
# =========================================================================

# --- 1. MC: Hàm số mũ và lôgarit ---

def k11_mc_c6_so_sanh_luy_thua_do_thi():
    """MC: Cho đồ thị y=a^x, y=b^x. Đường thẳng y=k cắt Oy, đồ thị tại H, M, N với m*HM = n*MN."""
    m_val = random.choice([2, 3])
    n_val = random.choice([3, 5])
    k_val = random.randint(2, 5)
    # x_M = log_a(k), x_N = log_b(k). HM = x_M, MN = x_N - x_M
    # m*x_M = n*(x_N - x_M) <=> (m+n)*x_M = n*x_N
    # (m+n)/ln(a) = n/ln(b) <=> ln(b^((m+n))) = ln(a^n) <=> a^n = b^(m+n) (hoặc tương tự)
    # Cụ thể: (m+n) log_a(k) = n log_b(k) => (m+n)/log_k(a) = n/log_k(b) => log_k(a) / (m+n) = log_k(b) / n
    # => a^n = b^(m+n) hay a^(m+n) = b^m...
    # Trong đề: 2HM = 3MN => 2 x_M = 3(x_N - x_M) => 5 x_M = 3 x_N
    # => 5/log_k(a) = 3/log_k(b) => 5 ln b = 3 ln a => a^3 = b^5 (với m=2, n=3 => a^3 = b^5)
    p = n_val
    q = m_val + n_val
    # (m+n) x_M = n x_N => (m+n)/ln a = n/ln b => a^n = b^(m+n)
    caudan = (
        f"Cho các hàm số $y = a^x$ và $y = b^x$ với $a, b$ là những số thực dương khác $1$, có đồ thị như hình vẽ. "
        f"Đường thẳng $y = {k_val}$ cắt trục tung, đồ thị hàm số $y = a^x$ và $y = b^x$ lần lượt tại $H, M, N$. "
        f"Biết rằng ${m_val}HM = {n_val}MN$, khẳng định nào sau đây đúng?"
    )
    correct = f"$a^{{{p}}} = b^{{{q}}}$"
    wrongs = [f"$a^{{{q}}} = b^{{{p}}}$", f"${p}a = {q}b$", f"$a^{{{m_val}}} = b^{{{n_val}}}$"]
    choices = _make_mc_choices(correct, wrongs)
    loigiai = (
        f"Ta có hoành độ điểm $H(0; {k_val})$, $M(x_M; {k_val})$ với $x_M = \\log_a {k_val}$, "
        f"và $N(x_N; {k_val})$ với $x_N = \\log_b {k_val}$.\n\n"
        f"Độ dài các đoạn thẳng: $HM = x_M$, $MN = x_N - x_M$.\n\n"
        f"Theo giả thiết: ${m_val}HM = {n_val}MN \\Leftrightarrow {m_val}x_M = {n_val}(x_N - x_M) "
        f"\\Leftrightarrow {m_val + n_val}x_M = {n_val}x_N$.\n\n"
        f"Thay tọa độ: ${m_val + n_val}\\log_a {k_val} = {n_val}\\log_b {k_val} "
        f"\\Leftrightarrow \\frac{{{m_val + n_val}}}{{\\ln a}} = \\frac{{{n_val}}}{{\\ln b}} "
        f"\\Leftrightarrow {n_val}\\ln a = {m_val + n_val}\\ln b \\Leftrightarrow a^{{{p}}} = b^{{{q}}}$."
    )
    return caudan, choices, loigiai

def k11_mc_c6_pt_mu_can_luy_thua():
    """MC: Phương trình a^(x+1) = (1/a)^(x^2 - Sx - P), tính tổng nghiệm x1 + x2."""
    a = random.choice([2, 3, 5, 7])
    # a^(x+1) = a^(-(x^2 - Sx - P)) <=> x+1 = -x^2 + Sx + P <=> x^2 + (1-S)x + (1-P) = 0
    # Chọn S để có 2 nghiệm phân biệt
    S = random.choice([2, 3, 4])
    P = random.choice([3, 4, 5])
    # x^2 + (1-S)x + (1-P) = 0. Tổng hai nghiệm: x1 + x2 = S - 1
    sum_roots = S - 1
    caudan = (
        f"Gọi $x_1, x_2$ là hai nghiệm của phương trình ${a}^{{x+1}} = \\left(\\frac{{1}}{{{a}}}\\right)^{{x^2 - {S}x - {P}}}$. "
        f"Khi đó $x_1 + x_2$ bằng:"
    )
    correct = f"${sum_roots}$"
    wrongs = [f"${-sum_roots}$", f"${sum_roots + 1}$", f"${sum_roots - 2}$"]
    choices = _make_mc_choices(correct, wrongs)
    loigiai = (
        f"Phương trình tương đương:\n"
        f"$${a}^{{x+1}} = {a}^{{-(x^2 - {S}x - {P})}} \\Leftrightarrow x + 1 = -x^2 + {S}x + {P} \\Leftrightarrow x^2 - ({S}-1)x + (1-{P}) = 0.$$\n"
        f"Phương trình bậc hai có $\\Delta > 0$, theo định lí Viète: $x_1 + x_2 = {sum_roots}$."
    )
    return caudan, choices, loigiai

def k11_mc_c6_rut_gon_can_long_nhau():
    """MC: Rút gọn biểu thức căn lồng nhau hữu tỉ về 2^(m/n) tính P = m^2 + n^2."""
    # sqrt[5]{8 * sqrt{2 * sqrt[3]{2}}} = 2^(3/5 + 1/10 + 1/30) = 2^(18/30 + 3/30 + 1/30) = 2^(22/30) = 2^(11/15)
    # m = 11, n = 15 => m^2 + n^2 = 121 + 225 = 346
    m, n = 11, 15
    val_p = m**2 + n**2 # 346
    caudan = (
        f"Cho biểu thức $\\sqrt[5]{{8\\sqrt{{2\\sqrt[3]{{2}}}}}} = 2^{{\\frac{{m}}{{n}}}}$, trong đó "
        f"$\\frac{{m}}{{n}}$ có dạng phân số tối giản. Gọi $P = m^2 + n^2$. Khẳng định nào sau đây đúng?"
    )
    correct = f"$P \\in (340; 350)$"
    wrongs = [f"$P \\in (350; 360)$", f"$P \\in (360; 370)$", f"$P \\in (330; 340)$"]
    choices = _make_mc_choices(correct, wrongs)
    loigiai = (
        f"Ta biến đổi biểu thức về lũy thừa cơ số $2$:\n"
        f"$$\\sqrt[5]{{8\\sqrt{{2\\sqrt[3]{{2}}}}}} = \\left(2^3 \\cdot \\left(2 \\cdot 2^{{1/3}}\\right)^{{1/2}}\\right)^{{1/5}} "
        f"= \\left(2^3 \\cdot 2^{{2/3}}\\right)^{{1/5}} = \\left(2^{{11/3}}\\right)^{{1/5}} = 2^{{11/15}}.$$\n"
        f"Do phân số $\\frac{{11}}{{15}}$ tối giản nên $m = 11, n = 15$.\n\n"
        f"Suy ra $P = m^2 + n^2 = 11^2 + 15^2 = 121 + 225 = 346 \\in (340; 350)$."
    )
    return caudan, choices, loigiai

def k11_mc_c6_bien_doi_log_tong_he_so():
    """MC: Cho a và b là hai số thực dương thỏa mãn a^p * b^q = k. Tính p*log_c a + q*log_c b."""
    c = random.choice([2, 3])
    val = random.choice([16, 32, 64, 81, 243])
    log_val = int(round(math.log(val, c)))
    p = random.randint(2, 4)
    q = random.randint(2, 3)
    caudan = (
        f"Cho $a$ và $b$ là hai số thực dương thỏa mãn $a^{{{p}}}b^{{{q}}} = {val}$. "
        f"Giá trị của biểu thức ${p}\\log_{{{c}}} a + {q}\\log_{{{c}}} b$ bằng:"
    )
    correct = f"${log_val}$"
    wrongs = [f"${val}$", f"${log_val + 2}$", f"${log_val - 1}$"]
    choices = _make_mc_choices(correct, wrongs)
    loigiai = (
        f"Áp dụng tính chất lôgarit của một tích và lũy thừa:\n"
        f"$${p}\\log_{{{c}}} a + {q}\\log_{{{c}}} b = \\log_{{{c}}} a^{{{p}}} + \\log_{{{c}}} b^{{{q}}} "
        f"= \\log_{{{c}}}(a^{{{p}}}b^{{{q}}}) = \\log_{{{c}}} {val} = {log_val}.$$"
    )
    return caudan, choices, loigiai

def k11_mc_c6_log_10_alpha_beta():
    """MC: Cho 10^alpha = a, 10^beta = b. Tính 10^(alpha+beta) + 10^(alpha-beta)."""
    a = random.randint(2, 4)
    b = random.randint(3, 5)
    # 10^(a+b) = a*b, 10^(a-b) = a/b
    # Sum = a*b + a/b = (a*b^2 + a)/b
    ans_num = a * b**2 + a
    ans_den = b
    frac_str = _fmt_frac(ans_num, ans_den)
    caudan = (
        f"Biết rằng $10^\\alpha = {a}; 10^\\beta = {b}$. Tính giá trị của biểu thức $10^{{\\alpha+\\beta}} + 10^{{\\alpha-\\beta}}$."
    )
    correct = f"${frac_str}$"
    wrongs = [f"${a*b}$", f"${_fmt_frac(b, ans_num)}$", f"${_fmt_frac(a, b)}$"]
    choices = _make_mc_choices(correct, wrongs)
    loigiai = (
        f"Theo quy tắc lũy thừa ta có:\n"
        f"$$10^{{\\alpha+\\beta}} = 10^\\alpha \\cdot 10^\\beta = {a} \\cdot {b} = {a*b},$$\n"
        f"$$10^{{\\alpha-\\beta}} = \\frac{{10^\\alpha}}{{10^\\beta}} = \\frac{{{a}}}{{{b}}}.$$\n"
        f"Do đó: $10^{{\\alpha+\\beta}} + 10^{{\\alpha-\\beta}} = {a*b} + \\frac{{{a}}}{{{b}}} = {frac_str}$."
    )
    return caudan, choices, loigiai

def k11_mc_c6_tap_xac_dinh_phan_thuc_log():
    """MC: Tập xác định của hàm số y = 1 / (log_a x - b)."""
    a = random.choice([2, 3, 5])
    b = random.randint(1, 2)
    val = a**b
    caudan = f"Tập xác định của hàm số $y = \\frac{{1}}{{\\log_{{{a}}} x - {b}}}$ là:"
    correct = f"$(0; +\\infty) \\setminus \\{{{val}\\}}$"
    wrongs = [f"$\\mathbb{{R}} \\setminus \\{{{val}\\}}$", f"$(0; +\\infty)$", f"$(0; +\\infty) \\setminus \\{{{b}\\}}$"]
    choices = _make_mc_choices(correct, wrongs)
    loigiai = (
        f"Hàm số xác định khi và chỉ khi:\n"
        f"$$\\begin{{cases}} x > 0 \\\\ \\log_{{{a}}} x - {b} \\neq 0 \\end{{cases}} "
        f"\\Leftrightarrow \\begin{{cases}} x > 0 \\\\ x \\neq {a}^{{{b}}} = {val} \\end{{cases}}.$$\n"
        f"Vậy tập xác định là $D = (0; +\\infty) \\setminus \\{{{val}\\}}$."
    )
    return caudan, choices, loigiai

def k11_mc_c6_toan_thuc_te_cuong_do_am():
    """MC: Mức cường độ âm L = 10 log(I/I0) (dB)."""
    # I = 10^(-k), I0 = 10^(-12) => L = 10 log(10^(12-k)) = 10*(12-k)
    k = random.choice([2, 3, 4])
    ans_L = 10 * (12 - k)
    caudan = (
        f"Mức cường độ âm $L$ đo bằng decibel (dB) của âm thanh có cường độ $I$ (đo bằng $\\text{{W}}/\\text{{m}}^2$) "
        f"được định nghĩa $L = 10\\log\\frac{{I}}{{I_0}}$, trong đó $I_0 = 10^{{-12}}\\,\\text{{W}}/\\text{{m}}^2$ "
        f"là cường độ âm chuẩn (ngưỡng nghe). Xác định mức cường độ âm của âm thanh giao thông thành phố có cường độ $I = 10^{{-{k}}}\\,\\text{{W}}/\\text{{m}}^2$."
    )
    correct = f"${ans_L}$"
    wrongs = [f"${ans_L + 20}$", f"${ans_L - 20}$", f"${ans_L + 40}$"]
    choices = _make_mc_choices(correct, wrongs)
    loigiai = (
        f"Thay số vào công thức định nghĩa mức cường độ âm:\n"
        f"$$L = 10\\log\\left(\\frac{{10^{{-{k}}}}}{{10^{{-12}}}}\\right) = 10\\log\\left(10^{{{12 - k}}}\\right) = 10 \\cdot {12 - k} = {ans_L}\\,(\\text{{dB}}).$$"
    )
    return caudan, choices, loigiai

def k11_mc_c6_toan_thuc_te_kepler():
    """MC: Định luật thứ ba Kepler P = d^(3/2) tính chu kỳ hành tinh."""
    d = 1.52 # Sao Hỏa
    ans = round(d**1.5, 2) # 1.87
    caudan = (
        f"Định luật thứ ba của nhà thiên văn học Kepler cho biết chu kỳ quỹ đạo $P$ (tính theo năm Trái Đất) "
        f"của một hành tinh quay quanh Mặt Trời được xác định bởi hàm số $P = d^{{3/2}}$, trong đó $d$ là khoảng cách "
        f"từ hành tinh đến Mặt Trời (tính theo đơn vị thiên văn AU). Biết khoảng cách từ sao Hỏa đến Mặt Trời là $1,52\\,\\text{{AU}}$, "
        f"sao Hỏa quay quanh Mặt Trời mất bao nhiêu năm Trái Đất (làm tròn đến hàng phần trăm)?"
    )
    correct = f"${ans:,.2f}$".replace('.', ',')
    wrongs = [f"${ans - 0.09:,.2f}$".replace('.', ','), f"${ans - 0.18:,.2f}$".replace('.', ','), f"${ans + 0.09:,.2f}$".replace('.', ',')]
    choices = _make_mc_choices(correct, wrongs)
    loigiai = (
        f"Áp dụng công thức định luật Kepler:\n"
        f"$$P = (1,52)^{{3/2}} = \\sqrt{{(1,52)^3}} \\approx {ans:,.2f}\\,(\\text{{năm}}).$$"
    )
    return caudan, choices, loigiai

def k11_mc_c6_bpt_mu_co_so_nghich_dao():
    """MC: Bất phương trình (a/b)^(x-1) < b/a với a < b."""
    # (2/5)^(x-1) < 5/2 = (2/5)^(-1). Do cơ số 2/5 < 1 nên x - 1 > -1 <=> x > 0
    a, b = 2, 5
    caudan = f"Tập nghiệm của bất phương trình $\\left(\\frac{{{a}}}{{{b}}}\\right)^{{x-1}} < \\frac{{{b}}}{{{a}}}$ là:"
    correct = f"$(0; +\\infty)$"
    wrongs = [f"$(-\\infty; 0)$", f"$(-\\infty; 2)$", f"$(2; +\\infty)$"]
    choices = _make_mc_choices(correct, wrongs)
    loigiai = (
        f"Ta viết lại bất phương trình về cùng cơ số:\n"
        f"$$\\left(\\frac{{{a}}}{{{b}}}\\right)^{{x-1}} < \\left(\\frac{{{a}}}{{{b}}}\\right)^{{-1}}.$$\n"
        f"Vì cơ số $0 < \\frac{{{a}}}{{{b}}} = 0,4 < 1$ nên bất phương trình đổi chiều:\n"
        f"$$x - 1 > -1 \\Leftrightarrow x > 0.$$\n"
        f"Vậy tập nghiệm là $S = (0; +\\infty)$."
    )
    return caudan, choices, loigiai

# --- 2. TF: Đúng / Sai Hàm số mũ và lôgarit ---

def k11_tf_c6_do_thi_ham_mu_di_qua_diem():
    """TF: Đồ thị hàm số mũ y = a^x đi qua (1; 3)."""
    # y = 3^x
    caudan = (
        "Cho hàm số $y = a^x$ có đồ thị đi qua điểm $(1; 3)$. Xét tính đúng sai của các mệnh đề sau:"
    )
    items = [
        (False, "Hàm số đã cho nghịch biến trên khoảng $(0; 1)$."),
        (True, "Hàm số đã cho có công thức $y = 3^x$."),
        (False, "Đồ thị hàm số đã cho cắt đường thẳng $y = \\frac{1}{3}$ tại điểm có hoành độ không âm."),
        (True, "Đồ thị hàm số đã cho cắt đường thẳng $y = -x + 1$ tại điểm có hoành độ bằng $0$.")
    ]
    choices = _make_tf_choices(items)
    loigiai = (
        "\\begin{itemchoice}\n"
        "\\itemch Sai. Đồ thị đi qua $(1; 3) \\Rightarrow a^1 = 3 \\Rightarrow a = 3 > 1$, nên hàm số luôn đồng biến trên $\\mathbb{R}$.\n"
        "\\itemch Đúng. Vì $a = 3$ nên hàm số là $y = 3^x$.\n"
        "\\itemch Sai. Đường thẳng $y = 1/3 \\Rightarrow 3^x = 3^{-1} \\Rightarrow x = -1 < 0$ (hoành độ âm).\n"
        "\\itemch Đúng. Phương trình hoành độ giao điểm $3^x = -x + 1$ có nghiệm duy nhất $x = 0$ (vì vế trái đồng biến, vế phải nghịch biến).\n"
        "\\end{itemchoice}"
    )
    return caudan, choices, loigiai

def k11_tf_c6_bpt_log_chua_an_trong_log():
    """TF: Bất phương trình log(x - 21) < 2 - log x."""
    # log(x-21) + log x < 2 <=> log(x(x-21)) < 2 => x(x-21) < 100 <=> x^2 - 21x - 100 < 0
    # (x - 25)(x + 4) < 0 <=> -4 < x < 25. ĐK: x > 21. Nghiệm: (21; 25) => a = 21, b = 25
    caudan = "Xét bất phương trình $\\log(x - 21) < 2 - \\log x$. Xét tính đúng sai của các mệnh đề sau:"
    items = [
        (False, "Điều kiện xác định của bất phương trình đã cho là $x > 0$."),
        (False, "Tập nghiệm của bất phương trình đã cho có dạng $S = (a; b)$ khi đó $a + b = 21$."),
        (True, "Tập nghiệm của bất phương trình đã cho có dạng $S = (a; b)$ khi đó $a \\cdot b = 525$."),
        (False, "Bất phương trình đã cho vô nghiệm.")
    ]
    choices = _make_tf_choices(items)
    loigiai = (
        "\\begin{itemchoice}\n"
        "\\itemch Sai. Điều kiện xác định là $\\begin{cases} x - 21 > 0 \\\\ x > 0 \\end{cases} \\Leftrightarrow x > 21$.\n"
        "\\itemch Sai. Bất phương trình chuyển vế: $\\log[x(x - 21)] < 2 \\Leftrightarrow x^2 - 21x < 10^2 = 100 "
        "\\Leftrightarrow x^2 - 21x - 100 < 0 \\Leftrightarrow -4 < x < 25$.\n"
        "Kết hợp điều kiện $x > 21$, ta được $S = (21; 25)$. Khi đó $a = 21, b = 25 \\Rightarrow a + b = 46$.\n"
        "\\itemch Đúng. Ta có $a \\cdot b = 21 \\cdot 25 = 525$.\n"
        "\\itemch Sai. Bất phương trình có tập nghiệm $S = (21; 25) \\neq \\varnothing$.\n"
        "\\end{itemchoice}"
    )
    return caudan, choices, loigiai

def k11_tf_c6_toan_thuc_te_cent_am_nhac():
    """TF: Bài toán Cent âm nhạc n = 1200 * log_2(a/b)."""
    caudan = (
        "Cent âm nhạc là một đơn vị trong thang lôgarit của cao độ hoặc khoảng tương đối. "
        "Một quãng tám bằng $1200$ cent. Công thức xác định chênh lệch khoảng thời gian giữa hai nốt nhạc "
        "có tần số $a$ và $b$ ($a > b$) là $n = 1200 \\cdot \\log_2\\frac{a}{b}$. Xét tính đúng sai của các khẳng định sau:"
    )
    items = [
        (True, "Khoảng thời gian chênh lệch giữa hai nốt nhạc có tần số $440\\,\\text{Hz}$ và $220\\,\\text{Hz}$ đúng bằng $1200$ cent."),
        (True, "Khoảng chênh lệch giữa hai nốt nhạc có tần số $443\\,\\text{Hz}$ và $415\\,\\text{Hz}$ xấp xỉ $113$ cent."),
        (False, "Nếu tần số âm tăng gấp đôi thì khoảng cent tăng gấp bốn lần."),
        (True, "Nếu hai nốt cùng tần số $a = b$ thì chênh lệch bằng $0$ cent.")
    ]
    choices = _make_tf_choices(items)
    loigiai = (
        "\\begin{itemchoice}\n"
        "\\itemch Đúng. Vì $n = 1200 \\log_2(440/220) = 1200 \\log_2 2 = 1200$ cent (quãng tám).\n"
        "\\itemch Đúng. Thay số: $n = 1200 \\log_2(443/415) \\approx 1200 \\cdot 0,09418 \\approx 113$ cent.\n"
        "\\itemch Sai. Khi tỉ số tần số gấp đôi thì khoảng cent cộng thêm $1200$ cent chứ không tăng gấp bốn lần.\n"
        "\\itemch Đúng. Khi $a = b$ thì $\\log_2 1 = 0 \\Rightarrow n = 0$ cent.\n"
        "\\end{itemchoice}"
    )
    return caudan, choices, loigiai

# --- 3. SA: Trả lời ngắn Hàm số mũ và lôgarit ---

def k11_sa_c6_ap_suat_khong_khi():
    """SA: Áp suất không khí P = P0 * e^(kx) tại độ cao 4000m."""
    # P(1000) = 760 * e^(1000k) = 672.71 => e^(1000k) = 672.71 / 760
    # P(4000) = 760 * (e^(1000k))^4 = 760 * (672.71 / 760)^4 approx 466.08
    P0 = 760
    P1 = 672.71
    ratio = P1 / P0
    ans = round(P0 * (ratio**4))
    caudan = (
        f"Áp suất không khí $P$ theo công thức $P = P_0 \\cdot \\mathrm{{e}}^{{kx}}\\,(\\text{{mmHg}})$, trong đó $x$ là độ cao (m), "
        f"$P_0 = {P0}\\,(\\text{{mmHg}})$ là áp suất tại mực nước biển ($x = 0$), $k$ là hệ số suy giảm. "
        f"Biết rằng ở độ cao $1000\\,\\text{{m}}$ thì áp suất không khí là ${P1}\\,(\\text{{mmHg}})$. "
        f"Tính áp suất của không khí ở độ cao $4000\\,\\text{{m}}$ (lấy kết quả làm tròn đến hàng đơn vị)."
    )
    loigiai = (
        f"Tại độ cao $x = 1000\\,\\text{{m}}$: ${P1} = {P0} \\cdot \\mathrm{{e}}^{{1000k}} "
        f"\\Rightarrow \\mathrm{{e}}^{{1000k}} = \\frac{{{P1}}}{{{P0}}} \\approx {ratio:.5f}$.\n\n"
        f"Tại độ cao $x = 4000\\,\\text{{m}}$:\n"
        f"$$P = {P0} \\cdot \\mathrm{{e}}^{{4000k}} = {P0} \\cdot \\left(\\mathrm{{e}}^{{1000k}}\\right)^4 "
        f"= {P0} \\cdot \\left(\\frac{{{P1}}}{{{P0}}}\\right)^4 \\approx {ans}\\,(\\text{{mmHg}}).$$"
    )
    return caudan, str(ans), loigiai

def k11_sa_c6_tang_truong_vi_khuan():
    """SA: S(t) = S0 * e^(rt). Ban đầu 500, sau 5h đạt 1500, hỏi sau bao lâu đạt 121500 con?"""
    # S0 = 500. Sau 5h: S(5) = 500 * e^(5r) = 1500 => e^(5r) = 3 => e^r = 3^(1/5)
    # S(t) = 500 * 3^(t/5) = 121500 => 3^(t/5) = 243 = 3^5 => t/5 = 5 => t = 25 giờ
    S0 = 500
    S1 = 1500
    target = 121500
    ratio = target // S0 # 243 = 3^5
    ans = 25
    caudan = (
        f"Sự tăng trưởng của một loại vi khuẩn được tính theo công thức $S(t) = S_0 \\cdot \\mathrm{{e}}^{{rt}}$, "
        f"trong đó $S_0$ là số lượng vi khuẩn ban đầu, $S(t)$ là số lượng vi khuẩn sau $t$ giờ, $r$ là tỷ lệ tăng trưởng. "
        f"Biết số lượng vi khuẩn ban đầu có ${S0}$ con và sau $5$ giờ có ${S1}$ con. "
        f"Hỏi sau bao nhiêu giờ kể từ lúc ban đầu thì số lượng vi khuẩn đạt ${target}$ con?"
    )
    loigiai = (
        f"Tại $t = 5$ giờ: $S(5) = {S0} \\cdot \\mathrm{{e}}^{{5r}} = {S1} \\Rightarrow \\mathrm{{e}}^{{5r}} = 3$.\n\n"
        f"Khi số lượng vi khuẩn đạt ${target}$ con:\n"
        f"$${S0} \\cdot \\mathrm{{e}}^{{rt}} = {target} \\Leftrightarrow \\mathrm{{e}}^{{rt}} = {ratio} = 3^5 = (\\mathrm{{e}}^{{5r}})^5 = \\mathrm{{e}}^{{25r}}.$$\n"
        f"Suy ra $rt = 25r \\Leftrightarrow t = {ans}$ (giờ)."
    )
    return caudan, str(ans), loigiai

def k11_sa_c6_bieu_dien_log_he_so_m_n():
    """SA: Cho log2 3 = a và log3 5 = b. Biểu diễn log12 150 = (2ab + ma + n)/(a + 2). Tính L = m + n."""
    # log12 150 = log2(150) / log2(12) = log2(2 * 3 * 25) / log2(4 * 3) = (1 + log2 3 + 2 log2 5) / (2 + log2 3)
    # log2 5 = log2 3 * log3 5 = a*b
    # Tử số: 1 + a + 2ab = 2ab + a + 1 => m = 1, n = 1 => m + n = 2
    ans = 2
    caudan = (
        "Cho $\\log_2 3 = a$ và $\\log_3 5 = b$. Biết $\\log_{12} 150 = \\frac{2ab + ma + n}{a + 2}$ với $m, n \\in \\mathbb{Z}$. "
        "Tính giá trị của biểu thức $L = m + n$."
    )
    loigiai = (
        "Đổi cơ số sang cơ số $2$:\n"
        "$$\\log_2 5 = \\log_2 3 \\cdot \\log_3 5 = a \\cdot b.$$\n\n"
        "Ta có:\n"
        "$$\\log_{12} 150 = \\frac{\\log_2 150}{\\log_2 12} = \\frac{\\log_2(2 \\cdot 3 \\cdot 5^2)}{\\log_2(2^2 \\cdot 3)} "
        "= \\frac{1 + \\log_2 3 + 2\\log_2 5}{2 + \\log_2 3} = \\frac{1 + a + 2ab}{a + 2} = \\frac{2ab + a + 1}{a + 2}.$$\n\n"
        "Đồng nhất hệ số ta được $m = 1, n = 1$. Suy ra $L = m + n = 1 + 1 = 2$."
    )
    return caudan, str(ans), loigiai


# =========================================================================
# II. CHƯƠNG VIII: CÁC QUY TẮC TÍNH XÁC SUẤT
# =========================================================================

def k11_mc_c8_cong_thuc_cong_doc_lap():
    """MC: A, B độc lập, biết P(A) = 0.4, P(B) = 0.5. Tính P(A hợp B)."""
    pA = 0.4
    pB = 0.5
    # P(AB) = 0.2 => P(A hợp B) = 0.4 + 0.5 - 0.2 = 0.7
    correct = "$0,7$"
    wrongs = ["$0,9$", "$0,5$", "$0,2$"]
    caudan = f"Cho $A$ và $B$ là hai biến cố độc lập. Biết $\\mathrm{{P}}(A) = {str(pA).replace('.', ',')}$ và $\\mathrm{{P}}(B) = {str(pB).replace('.', ',')}$. Xác suất của biến cố $A \\cup B$ là:"
    choices = _make_mc_choices(correct, wrongs)
    loigiai = (
        f"Vì $A$ và $B$ là hai biến cố độc lập nên:\n"
        f"$$\\mathrm{{P}}(AB) = \\mathrm{{P}}(A) \\cdot \\mathrm{{P}}(B) = {str(pA).replace('.', ',')} \\cdot {str(pB).replace('.', ',')} = 0,2.$$\n\n"
        f"Áp dụng công thức cộng xác suất:\n"
        f"$$\\mathrm{{P}}(A \\cup B) = \\mathrm{{P}}(A) + \\mathrm{{P}}(B) - \\mathrm{{P}}(AB) = {str(pA).replace('.', ',')} + {str(pB).replace('.', ',')} - 0,2 = 0,7.$$"
    )
    return caudan, choices, loigiai

def k11_mc_c8_tim_p_b_tu_tich_doc_lap():
    """MC: Cho A, B độc lập. P(A) = 1/4, P(AB) = 1/9. Tính P(B)."""
    # P(B) = (1/9) / (1/4) = 4/9
    correct = "$\\frac{4}{9}$"
    wrongs = ["$\\frac{5}{36}$", "$\\frac{13}{36}$", "$\\frac{9}{4}$"]
    caudan = "Cho $A, B$ là hai biến cố độc lập. Biết $\\mathrm{P}(A) = \\frac{1}{4}, \\mathrm{P}(AB) = \\frac{1}{9}$. Tính $\\mathrm{P}(B)$."
    choices = _make_mc_choices(correct, wrongs)
    loigiai = (
        "Do hai biến cố $A$ và $B$ độc lập nên $\\mathrm{P}(AB) = \\mathrm{P}(A) \\cdot \\mathrm{P}(B)$.\n\n"
        "Suy ra:\n"
        "$$\\mathrm{P}(B) = \\frac{\\mathrm{P}(AB)}{\\mathrm{P}(A)} = \\frac{1/9}{1/4} = \\frac{4}{9}.$$"
    )
    return caudan, choices, loigiai

def k11_mc_c8_bien_co_xung_khac_tinh_p():
    """MC: Cho A, B xung khắc. P(A) = 1/3, P(A hợp B) = 1/2. Tính P(B)."""
    # P(B) = 1/2 - 1/3 = 1/6
    correct = "$\\frac{1}{6}$"
    wrongs = ["$\\frac{5}{6}$", "$\\frac{1}{12}$", "$\\frac{2}{3}$"]
    caudan = "Cho $A, B$ là hai biến cố xung khắc. Biết $\\mathrm{P}(A) = \\frac{1}{3}, \\mathrm{P}(A \\cup B) = \\frac{1}{2}$. Tính $\\mathrm{P}(B)$."
    choices = _make_mc_choices(correct, wrongs)
    loigiai = (
        "Vì $A$ và $B$ là hai biến cố xung khắc nên $\\mathrm{P}(A \\cup B) = \\mathrm{P}(A) + \\mathrm{P}(B)$.\n\n"
        "Suy ra $\\mathrm{P}(B) = \\mathrm{P}(A \\cup B) - \\mathrm{P}(A) = \\frac{1}{2} - \\frac{1}{3} = \\frac{1}{6}$."
    )
    return caudan, choices, loigiai

def k11_mc_c8_kiem_tra_tinh_xung_khac():
    """MC: Cho P(A)=1/3, P(B)=1/4, P(A hợp B)=1/2. Khẳng định nào đúng?"""
    # P(A) + P(B) = 7/12 != 1/2 => P(AB) = 7/12 - 1/2 = 1/12 > 0 => Không xung khắc
    caudan = "Cho hai biến cố $A$ và $B$ có $\\mathrm{P}(A) = \\frac{1}{3}, \\mathrm{P}(B) = \\frac{1}{4}, \\mathrm{P}(A \\cup B) = \\frac{1}{2}$. Khẳng định nào sau đây đúng?"
    correct = "Không xung khắc."
    wrongs = ["Độc lập.", "Xung khắc.", "Không rõ."]
    choices = _make_mc_choices(correct, wrongs)
    loigiai = (
        "Ta có: $\\mathrm{P}(AB) = \\mathrm{P}(A) + \\mathrm{P}(B) - \\mathrm{P}(A \\cup B) = \\frac{1}{3} + \\frac{1}{4} - \\frac{1}{2} = \\frac{1}{12} \\neq 0$.\n\n"
        "Vì $\\mathrm{P}(AB) > 0$ nên hai biến cố $A$ và $B$ không xung khắc.\n"
        "Ngoài ra $\\mathrm{P}(A) \\cdot \\mathrm{P}(B) = \\frac{1}{12} = \\mathrm{P}(AB)$ nên $A$ và $B$ độc lập (đáp án chính xác nhất phủ định tính xung khắc)."
    )
    return caudan, choices, loigiai

def k11_mc_c8_xa_thu_ban_bia_3_phat():
    """MC: Xạ thủ bắn 3 phát, xác suất trúng 0.6. Tính xác suất đúng 2 phát trúng."""
    # C_3^2 * 0.6^2 * 0.4 = 3 * 0.36 * 0.4 = 0.432 = 54/125
    caudan = (
        "Một xạ thủ bắn liên tiếp ba mũi tên vào bia ngắm. Biết rằng xác suất bắn trúng bia ngắm của xạ thủ là $0,6$. "
        "Xác suất để trong ba lần bắn tên có đúng hai lần tên trúng bia ngắm là:"
    )
    correct = "$\\frac{54}{125}$"
    wrongs = ["$\\frac{81}{125}$", "$\\frac{24}{125}$", "$\\frac{18}{125}$"]
    choices = _make_mc_choices(correct, wrongs)
    loigiai = (
        "Gọi $X$ là số lần bắn trúng trong $3$ lần bắn độc lập. $X$ tuân theo quy tắc phân phối Bernoulli với $n = 3, p = 0,6$.\n\n"
        "Xác suất có đúng $2$ lần trúng là:\n"
        "$$\\mathrm{P}(X = 2) = \\mathrm{C}_3^2 \\cdot (0,6)^2 \\cdot (1 - 0,6)^1 = 3 \\cdot 0,36 \\cdot 0,4 = 0,432 = \\frac{54}{125}.$$"
    )
    return caudan, choices, loigiai

def k11_mc_c8_hoc_sinh_thich_the_thao_phan_bu():
    """MC: Lớp 30 học sinh, 18 bóng đá, 16 cầu lông, 7 cả hai. Chọn 1 học sinh không thích môn nào."""
    # N(A hợp B) = 18 + 16 - 7 = 27. Không thích: 30 - 27 = 3. P = 3/30 = 1/10
    caudan = (
        "Một lớp học có $30$ học sinh, trong đó có $18$ học sinh thích đá bóng, $16$ học sinh thích cầu lông "
        "và $7$ học sinh thích chơi cả hai môn thể thao. Chọn ngẫu nhiên một học sinh. Xác suất bạn học sinh được chọn không thích chơi môn thể thao nào là:"
    )
    correct = "$\\frac{1}{10}$"
    wrongs = ["$\\frac{3}{5}$", "$\\frac{7}{30}$", "$\\frac{1}{15}$"]
    choices = _make_mc_choices(correct, wrongs)
    loigiai = (
        "Gọi $A$ là biến cố học sinh thích bóng đá, $B$ là biến cố học sinh thích cầu lông.\n\n"
        "Số học sinh thích ít nhất một trong hai môn là:\n"
        "$$n(A \\cup B) = n(A) + n(B) - n(AB) = 18 + 16 - 7 = 27.$$\n\n"
        "Số học sinh không thích môn nào là $30 - 27 = 3$.\n\n"
        "Xác suất cần tìm là: $\\mathrm{P} = \\frac{3}{30} = \\frac{1}{10}$."
    )
    return caudan, choices, loigiai

def k11_mc_c8_gieo_xuc_xac_tong_chia_het():
    """MC: Gieo hai con xúc xắc, xác suất tổng số chấm chia hết cho 5."""
    # Tổng có thể là 5 hoặc 10
    # Tổng = 5: (1,4), (2,3), (3,2), (4,1) -> 4 cặp
    # Tổng = 10: (4,6), (5,5), (6,4) -> 3 cặp
    # Tổng cộng: 7 cặp. Không gian mẫu: 36. P = 7/36
    caudan = "Gieo hai con xúc xắc cân đối và đồng chất. Xác suất của biến cố \"Tổng số chấm xuất hiện trên hai con xúc xắc chia hết cho $5$\" là:"
    correct = "$\\frac{7}{36}$"
    wrongs = ["$\\frac{5}{36}$", "$\\frac{1}{6}$", "$\\frac{2}{9}$"]
    choices = _make_mc_choices(correct, wrongs)
    loigiai = (
        "Số phần tử của không gian mẫu: $n(\\Omega) = 6 \\times 6 = 36$.\n\n"
        "Các kết quả thuận lợi có tổng số chấm chia hết cho $5$ (tổng bằng $5$ hoặc $10$):\n"
        "- Tổng bằng $5$: $\\{(1; 4), (2; 3), (3; 2), (4; 1)\\}$ ($4$ trường hợp).\n"
        "- Tổng bằng $10$: $\\{(4; 6), (5; 5), (6; 4)\\}$ ($3$ trường hợp).\n\n"
        "Có tất cả $4 + 3 = 7$ kết quả thuận lợi. Xác suất là $\\mathrm{P} = \\frac{7}{36}$."
    )
    return caudan, choices, loigiai

def k11_mc_c8_the_chia_het_giao():
    """MC: 25 tấm thẻ, P: chia hết cho 4, Q: chia hết cho 6. Nội dung biến cố giao PQ."""
    # BCNN(4, 6) = 12. Trong 1-25: 12, 24
    caudan = (
        "Một hộp đựng $25$ tấm thẻ cùng loại được đánh số từ $1$ đến $25$. Rút ngẫu nhiên một tấm thẻ trong hộp. "
        "Xét các biến cố $P$: \"Số ghi trên tấm thẻ là số chia hết cho $4$\" và $Q$: \"Số ghi trên tấm thẻ là số chia hết cho $6$\". "
        "Nội dung của biến cố giao $PQ$ là gì?"
    )
    correct = "$\\{12; 24\\}$"
    wrongs = ["$\\{3; 6; 9; 12; 15; 18; 24\\}$", "$\\{1; 2; 4\\}$", "$\\{12; 16; 20; 24\\}$"]
    choices = _make_mc_choices(correct, wrongs)
    loigiai = (
        "Biến cố giao $PQ$ xảy ra khi số được chọn vừa chia hết cho $4$ vừa chia hết cho $6$, "
        "tức là chia hết cho $\\text{BCNN}(4, 6) = 12$.\n\n"
        "Trong các số từ $1$ đến $25$, các số chia hết cho $12$ là $12$ và $24$.\n"
        "Do đó $PQ = \\{12; 24\\}$."
    )
    return caudan, choices, loigiai

def k11_tf_c8_chon_so_nguyen_duong_1_chu_so():
    """TF: Hai bạn Y và Q mỗi bạn chọn ngẫu nhiên một số nguyên dương có 1 chữ số (1 đến 9)."""
    caudan = (
        "Hai bạn Y và Q mỗi bạn chọn ngẫu nhiên một số nguyên dương có một chữ số (từ $1$ đến $9$). "
        "Xét tính đúng sai của các mệnh đề sau:"
    )
    items = [
        (True, "Xác suất để bạn Y chọn được số là số chẵn bằng $\\frac{4}{9}$."),
        (False, "Xác suất để bạn Q chọn được số là số lẻ và chia hết cho $3$ bằng $\\frac{1}{3}$."),
        (False, "Xác suất để hai bạn Y và Q chọn được hai số giống nhau là $\\frac{4}{9}$."),
        (True, "Xác suất để hai bạn Y và Q chọn được hai số có tích là một số chẵn bằng $\\frac{56}{81}$.")
    ]
    choices = _make_tf_choices(items)
    loigiai = (
        "\\begin{itemchoice}\n"
        "\\itemch Đúng. Từ $1$ đến $9$ có $4$ số chẵn $\\{2, 4, 6, 8\\}$. Xác suất là $4/9$.\n"
        "\\itemch Sai. Số lẻ chia hết cho $3$ gồm $\\{3, 9\\}$ ($2$ số). Xác suất là $2/9 \\neq 1/3$.\n"
        "\\itemch Sai. Có $9$ cặp chọn giống nhau trong $9 \\times 9 = 81$ kết quả. Xác suất là $9/81 = 1/9$.\n"
        "\\itemch Đúng. Biến cố đối là cả hai bạn cùng chọn số lẻ: $(5/9) \\times (5/9) = 25/81$. "
        "Xác suất tích là số chẵn bằng $1 - 25/81 = 56/81$.\n"
        "\\end{itemchoice}"
    )
    return caudan, choices, loigiai


# =========================================================================
# III. CHƯƠNG IX: ĐẠO HÀM
# =========================================================================

def k11_mc_c9_dao_ham_da_thuc_phan_thuc():
    """MC: Đạo hàm hàm phân thức bậc nhất y = (ax + b)/(cx + d)."""
    a = random.choice([2, 3])
    b = random.choice([-3, -1, 1, 3])
    c = 1
    d = random.choice([1, 2])
    # y' = (ad - bc) / (cx + d)^2
    det = a * d - b * c
    caudan = f"Đạo hàm của hàm số $y = \\frac{{{a}x {b:+d}}}{{x {d:+d}}}$ là:"
    correct = f"$y' = \\frac{{{det}}}{{(x {d:+d})^2}}$"
    wrongs = [f"$y' = \\frac{{{-det}}}{{(x {d:+d})^2}}$", f"$y' = \\frac{{{det}}}{{x {d:+d}}}$", f"$y' = \\frac{{{-det}}}{{x {d:+d}}}$"]
    choices = _make_mc_choices(correct, wrongs)
    loigiai = (
        f"Áp dụng công thức đạo hàm phân thức bậc nhất $\\left(\\frac{{ax+b}}{{cx+d}}\\right)' = \\frac{{ad-bc}}{{(cx+d)^2}}$:\n"
        f"$$y' = \\frac{{{a} \\cdot ({d}) - ({b}) \\cdot 1}}{{(x {d:+d})^2}} = \\frac{{{det}}}{{(x {d:+d})^2}}.$$"
    )
    return caudan, choices, loigiai

def k11_mc_c9_dao_ham_cap_hai_phan_thuc():
    """MC: Đạo hàm cấp hai của hàm phân thức y = (3x + 1)/(x + 2)."""
    # y = (3x+1)/(x+2) = 3 - 5/(x+2) => y' = 5/(x+2)^2 => y'' = -10/(x+2)^3
    caudan = "Đạo hàm cấp hai của hàm số $y = \\frac{3x + 1}{x + 2}$ là:"
    correct = "$y'' = -\\frac{10}{(x + 2)^3}$"
    wrongs = ["$y'' = \\frac{10}{(x + 2)^2}$", "$y'' = -\\frac{5}{(x + 2)^4}$", "$y'' = -\\frac{5}{(x + 2)^3}$"]
    choices = _make_mc_choices(correct, wrongs)
    loigiai = (
        "Biến đổi hàm số: $y = \\frac{3(x+2) - 5}{x+2} = 3 - \\frac{5}{x+2}$.\n\n"
        "Đạo hàm cấp một: $y' = \\frac{5}{(x+2)^2} = 5(x+2)^{-2}$.\n\n"
        "Đạo hàm cấp hai: $y'' = 5 \\cdot (-2)(x+2)^{-3} = -\\frac{10}{(x+2)^3}$."
    )
    return caudan, choices, loigiai

def k11_mc_c9_dao_ham_cap_hai_luong_giac():
    """MC: Cho f(x) = sin^2 x. Tính f''(x)."""
    # f'(x) = 2 sin x cos x = sin 2x => f''(x) = 2 cos 2x
    caudan = "Cho hàm số $f(x) = \\sin^2 x$. Với mọi $x \\in \\mathbb{R}$, giá trị của $f''(x)$ bằng:"
    correct = "$f''(x) = 2\\cos 2x$"
    wrongs = ["$f''(x) = 2\\cos x$", "$f''(x) = 2\\sin 2x$", "$f''(x) = \\cos 2x$"]
    choices = _make_mc_choices(correct, wrongs)
    loigiai = (
        "Đạo hàm cấp một: $f'(x) = 2\\sin x \\cdot (\\sin x)' = 2\\sin x\\cos x = \\sin 2x$.\n\n"
        "Đạo hàm cấp hai: $f''(x) = (\\sin 2x)' = 2\\cos 2x$."
    )
    return caudan, choices, loigiai

def k11_mc_c9_tiep_tuyen_he_so_goc_tai_x0():
    """MC: Hệ số góc của tiếp tuyến với đồ thị hàm số y = (x + 1)/(2x - 3) tại điểm x0 = -1."""
    # y' = (-3 - 2)/(2x-3)^2 = -5/(2x-3)^2. Tại x = -1: y'(-1) = -5/(-5)^2 = -5/25 = -1/5
    caudan = "Tiếp tuyến của đồ thị hàm số $y = \\frac{x + 1}{2x - 3}$ tại điểm có hoành độ $x_0 = -1$ có hệ số góc bằng:"
    correct = "$-\\frac{1}{5}$"
    wrongs = ["$5$", "$-5$", "$\\frac{1}{5}$"]
    choices = _make_mc_choices(correct, wrongs)
    loigiai = (
        "Ta có đạo hàm: $y' = \\frac{1 \\cdot (-3) - 1 \\cdot 2}{(2x - 3)^2} = \\frac{-5}{(2x - 3)^2}$.\n\n"
        "Hệ số góc của tiếp tuyến tại $x_0 = -1$ là:\n"
        "$$k = y'(-1) = \\frac{-5}{(2(-1) - 3)^2} = \\frac{-5}{25} = -\\frac{1}{5}.$$"
    )
    return caudan, choices, loigiai

def k11_mc_c9_phuong_trinh_tiep_tuyen_tai_diem():
    """MC: Viết phương trình tiếp tuyến của đồ thị hàm số f(x) = x^3 - 2x^2 + 3x + 1 tại điểm x0 = 2."""
    # f(2) = 8 - 8 + 6 + 1 = 7. f'(x) = 3x^2 - 4x + 3. f'(2) = 12 - 8 + 3 = 7.
    # Tiếp tuyến: y - 7 = 7(x - 2) <=> y = 7x - 7
    caudan = "Viết phương trình tiếp tuyến của đồ thị hàm số $f(x) = x^3 - 2x^2 + 3x + 1$ tại điểm có hoành độ $x_0 = 2$."
    correct = "$y = 7x - 7$"
    wrongs = ["$y = -x - 7$", "$y = 7x - 14$", "$y = -x + 9$"]
    choices = _make_mc_choices(correct, wrongs)
    loigiai = (
        "Tọa độ tiếp điểm: $x_0 = 2 \\Rightarrow y_0 = f(2) = 2^3 - 2(2^2) + 3(2) + 1 = 7$.\n\n"
        "Đạo hàm: $f'(x) = 3x^2 - 4x + 3 \\Rightarrow k = f'(2) = 3(2^2) - 4(2) + 3 = 7$.\n\n"
        "Phương trình tiếp tuyến là:\n"
        "$$y - 7 = 7(x - 2) \\Leftrightarrow y = 7x - 7.$$"
    )
    return caudan, choices, loigiai

def k11_tf_c9_khao_sat_tiep_tuyen_song_song():
    """TF: Hàm số f(x) = 1/2 x^4 - 3x^2 + 2024 và tiếp tuyến song song với d: y = -4x + 4043/2."""
    caudan = (
        "Cho hàm số $f(x) = \\frac{1}{2}x^4 - 3x^2 + 2024$ có đồ thị $(C)$ và đường thẳng $d: y = -4x + \\frac{4043}{2}$. "
        "Xét tính đúng sai của các khẳng định sau:"
    )
    items = [
        (True, "Đạo hàm của $f(x)$ là $f'(x) = 2x^3 - 6x$."),
        (False, "Hệ số góc của đường thẳng $d$ là $4$."),
        (True, "Gọi $\\Delta$ là tiếp tuyến của $(C)$ song song với $d$, khi đó hệ số góc của $\\Delta$ là $-4$."),
        (True, "Có hai tiếp tuyến của đồ thị $(C)$ song song với $d$.")
    ]
    choices = _make_tf_choices(items)
    loigiai = (
        "\\begin{itemchoice}\n"
        "\\itemch Đúng. Ta có $f'(x) = \\frac{1}{2}(4x^3) - 3(2x) = 2x^3 - 6x$.\n"
        "\\itemch Sai. Đường thẳng $d: y = -4x + \\frac{4043}{2}$ có hệ số góc $k_d = -4$.\n"
        "\\itemch Đúng. Tiếp tuyến song song với $d$ có hệ số góc bằng hệ số góc của $d$, tức $k_\\Delta = -4$.\n"
        "\\itemch Đúng. Phương trình $f'(x) = -4 \\Leftrightarrow 2x^3 - 6x = -4 \\Leftrightarrow 2x^3 - 6x + 4 = 0 "
        "\\Leftrightarrow 2(x - 1)^2(x + 2) = 0 \\Leftrightarrow x = 1$ hoặc $x = -2$.\n"
        "Cả hai tiếp điểm đều cho tiếp tuyến song song (không trùng) với $d$. Vậy có $2$ tiếp tuyến thỏa mãn.\n"
        "\\end{itemchoice}"
    )
    return caudan, choices, loigiai

def k11_tf_c9_ung_dung_vat_ly_nem_vat():
    """TF: Chuyển động ném thẳng đứng h = -2t^2 + 20t + 22."""
    caudan = (
        "Một vật được phóng theo phương thẳng đứng với vận tốc ban đầu là $20\\,\\text{m/s}$ "
        "thì độ cao của nó so với mặt đất (tính bằng mét) sau $t$ giây được cho bởi công thức $h(t) = -2t^2 + 20t + 22$. "
        "Xét tính đúng sai của các khẳng định sau:"
    )
    items = [
        (True, "Độ cao ban đầu của vật là $22$ mét."),
        (False, "Vận tốc của vật tại thời điểm $t$ là $v(t) = -2t + 20$."),
        (True, "Vận tốc của vật tại thời điểm $t = 3\\,\\text{s}$ là $v(3) = 8\\,\\text{m/s}$."),
        (False, "Tại thời điểm vật chạm đất thì vận tốc của vật là $15\\,\\text{m/s}$.")
    ]
    choices = _make_tf_choices(items)
    loigiai = (
        "\\begin{itemchoice}\n"
        "\\itemch Đúng. Tại $t = 0$, $h(0) = 22\\,\\text{m}$.\n"
        "\\itemch Sai. Vận tốc tức thời là đạo hàm của độ cao: $v(t) = h'(t) = -4t + 20\\,(\\text{m/s})$.\n"
        "\\itemch Đúng. Tại $t = 3\\,\\text{s}$, $v(3) = -4(3) + 20 = 8\\,\\text{m/s}$.\n"
        "\\itemch Sai. Vật chạm đất khi $h(t) = 0 \\Leftrightarrow -2t^2 + 20t + 22 = 0 "
        "\\Leftrightarrow t = 11$ (vì $t > 0$). Khi đó vận tốc chạm đất là $|v(11)| = |-4(11) + 20| = 24\\,\\text{m/s} \\neq 15\\,\\text{m/s}$.\n"
        "\\end{itemchoice}"
    )
    return caudan, choices, loigiai

def k11_sa_c9_dao_ham_luong_giac_tai_diem():
    """SA: Đạo hàm của y = (sin^2 x - cos^2 x) / (sin x * cos x) tại x = pi/6."""
    # y = -cos(2x) / ((1/2) sin(2x)) = -2 cot(2x)
    # y' = -2 * (-2 / sin^2(2x)) = 4 / sin^2(2x)
    # Tại x = pi/6: 2x = pi/3 => sin(pi/3) = sqrt(3)/2 => sin^2(2x) = 3/4
    # y'(pi/6) = 4 / (3/4) = 16/3 approx 5.33
    ans = "5.33"
    caudan = (
        "Tính đạo hàm của hàm số $y = \\frac{\\sin^2 x - \\cos^2 x}{\\sin x \\cdot \\cos x}$ tại điểm $x = \\frac{\\pi}{6}$ "
        "(làm tròn kết quả đến hàng phần trăm)."
    )
    loigiai = (
        "Rút gọn biểu thức của hàm số:\n"
        "$$y = \\frac{-(\\cos^2 x - \\sin^2 x)}{\\frac{1}{2}\\sin 2x} = \\frac{-\\cos 2x}{\\frac{1}{2}\\sin 2x} = -2\\cot 2x.$$\n\n"
        "Lấy đạo hàm của $y$ theo $x$:\n"
        "$$y' = -2 \\cdot \\left(-\\frac{2}{\\sin^2 2x}\\right) = \\frac{4}{\\sin^2 2x}.$$\n\n"
        "Tại $x = \\frac{\\pi}{6}$, ta có $2x = \\frac{\\pi}{3} \\Rightarrow \\sin 2x = \\frac{\\sqrt{3}}{2} \\Rightarrow \\sin^2 2x = \\frac{3}{4}$.\n\n"
        "Do đó $y'\\left(\\frac{\\pi}{6}\\right) = \\frac{4}{3/4} = \\frac{16}{3} \\approx 5,33$."
    )
    return caudan, ans, loigiai


# =========================================================================
# IV. CHƯƠNG V: GIỚI HẠN. HÀM SỐ LIÊN TỤC (DÃY SỐ, CSN LÙI VÔ HẠN)
# =========================================================================

def k11_mc_c5_cong_boi_csn_lui_vo_han():
    """MC: Tìm công bội q của cấp số nhân lùi vô hạn biết tổng S và u1."""
    # S = u1 / (1 - q) => 1 - q = u1 / S => q = 1 - u1 / S
    u1 = random.choice([-3, -2, 2, 3])
    q_choice = random.choice([(1, 2), (1, 3), (-1, 2), (-1, 3)])
    q_num, q_den = q_choice
    # S = u1 / (1 - q_num/q_den) = u1 * q_den / (q_den - q_num)
    S_val = u1 * q_den // (q_den - q_num)
    correct = f"${_fmt_frac(q_num, q_den)}$"
    wrongs = [f"${_fmt_frac(-q_num, q_den)}$", f"${_fmt_frac(q_den - q_num, q_den)}$", f"${_fmt_frac(1, 4)}$"]
    caudan = f"Tìm công bội của cấp số nhân lùi vô hạn, biết $S = {S_val}; u_1 = {u1}$."
    choices = _make_mc_choices(correct, wrongs)
    loigiai = (
        f"Áp dụng công thức tính tổng của cấp số nhân lùi vô hạn $S = \\frac{{u_1}}{{1 - q}}$:\n"
        f"$${S_val} = \\frac{{{u1}}}{{1 - q}} \\Leftrightarrow 1 - q = \\frac{{{u1}}}{{{S_val}}} = {_fmt_frac(u1, S_val)} "
        f"\\Leftrightarrow q = 1 - {_fmt_frac(u1, S_val)} = {_fmt_frac(q_num, q_den)}.$$"
    )
    return caudan, choices, loigiai

def k11_mc_c5_tong_csn_lui_vo_han_dan_dau():
    """MC: Tính tổng S = 1 - 1/k + 1/k^2 - 1/k^3 + ..."""
    k = random.choice([2, 3, 4, 5])
    # u1 = 1, q = -1/k => S = 1 / (1 - (-1/k)) = k / (k + 1)
    ans_num = k
    ans_den = k + 1
    frac_str = _fmt_frac(ans_num, ans_den)
    caudan = f"Tính tổng cấp số nhân lùi vô hạn $S = 1 - \\frac{{1}}{{{k}}} + \\frac{{1}}{{{k**2}}} - \\dots + \\left(-\\frac{{1}}{{{k}}}\\right)^{{n-1}} + \\dots$"
    correct = f"${frac_str}$"
    wrongs = [f"${_fmt_frac(k+1, k)}$", f"${_fmt_frac(k-1, k)}$", f"$1$"]
    choices = _make_mc_choices(correct, wrongs)
    loigiai = (
        f"Tổng trên là tổng của cấp số nhân lùi vô hạn với số hạng đầu $u_1 = 1$ và công bội $q = -\\frac{{1}}{{{k}}}$ ($|q| < 1$).\n\n"
        f"Áp dụng công thức: $S = \\frac{{u_1}}{{1 - q}} = \\frac{{1}}{{1 - \\left(-\\frac{{1}}{{{k}}}\\right)}} = \\frac{{1}}{{\\frac{{{k+1}}}{{{k}}}}} = {frac_str}$."
    )
    return caudan, choices, loigiai

def k11_mc_c5_so_thap_phan_tuan_hoan():
    """MC: Biểu diễn số thập phân vô hạn tuần hoàn 0,(a) thành phân số tối giản a/b, tính a + b."""
    a_val = random.choice([3, 6, 7])
    # 0,(a) = a / 9
    f = Fraction(a_val, 9)
    ans = f.numerator + f.denominator
    caudan = (
        f"Biểu diễn số thập phân vô hạn tuần hoàn $0,({a_val}) = 0,{a_val}{a_val}{a_val}\\dots$ "
        f"dưới dạng phân số tối giản $\\frac{{a}}{{b}}$ ($a, b \\in \\mathbb{{Z}}^+)$. Tính $a + b$."
    )
    correct = f"${ans}$"
    wrongs = [f"${ans + 2}$", f"${ans - 1}$", f"${ans + 5}$"]
    choices = _make_mc_choices(correct, wrongs)
    loigiai = (
        f"Ta viết số $0,({a_val})$ dưới dạng tổng cấp số nhân lùi vô hạn:\n"
        f"$$0,({a_val}) = \\frac{{{a_val}}}{{10}} + \\frac{{{a_val}}}{{10^2}} + \\frac{{{a_val}}}{{10^3}} + \\dots "
        f"= \\frac{{{a_val}/10}}{{1 - 1/10}} = \\frac{{{a_val}}}{{9}} = {_fmt_frac(f.numerator, f.denominator)}.$$\n\n"
        f"Vì $\\frac{{{f.numerator}}}{{{f.denominator}}}$ là phân số tối giản nên $a = {f.numerator}, b = {f.denominator}$.\n"
        f"Do đó $a + b = {f.numerator} + {f.denominator} = {ans}$."
    )
    return caudan, choices, loigiai

def k11_mc_c5_gioi_han_day_so_ham_mu():
    """MC: Giới hạn dãy số cơ số mũ lim (a*2^(n+1) - b*3^(n+1)) / (c + 3^n)."""
    b = random.randint(2, 4)
    a = random.randint(2, 3)
    c = random.randint(2, 5)
    # Tử = 2a*2^n - 3b*3^n. Mẫu = c + 3^n. Chia cả tử và mẫu cho 3^n => limit = -3b / 1 = -3b
    ans = -3 * b
    caudan = f"Tính giới hạn $\\lim \\frac{{{a} \\cdot 2^{{n+1}} - {b} \\cdot 3^{{n+1}}}}{{{c} + 3^n}}$."
    correct = f"${ans}$"
    wrongs = [f"${-ans}$", f"$0$", f"${_fmt_frac(-ans, 2)}$"]
    choices = _make_mc_choices(correct, wrongs)
    loigiai = (
        f"Chia cả tử và mẫu cho $3^n$ (lũy thừa có cơ số lớn nhất):\n"
        f"$$\\lim \\frac{{{2*a} \\cdot 2^n - {3*b} \\cdot 3^n}}{{{c} + 3^n}} "
        f"= \\lim \\frac{{{2*a} \\cdot \\left(\\frac{{2}}{{3}}\\right)^n - {3*b}}}{{{c} \\cdot \\left(\\frac{{1}}{{3}}\\right)^n + 1}} "
        f"= \\frac{{{2*a} \\cdot 0 - {3*b}}}{{{c} \\cdot 0 + 1}} = {ans}.$$"
    )
    return caudan, choices, loigiai

def k11_mc_c5_lien_hop_vo_dinh_bac_hai():
    """MC: lim(n - sqrt(n^2 - 2kn + c)) = k."""
    k = random.randint(1, 4)
    c = random.choice([1, 2, 3])
    caudan = f"Tính giới hạn $\\lim \\left(n - \\sqrt{{n^2 - {2*k}n + {c}}}\\right)$."
    correct = f"${k}$"
    wrongs = [f"${-k}$", f"$+\\infty$", f"$-\\infty$"]
    choices = _make_mc_choices(correct, wrongs)
    loigiai = (
        f"Nhân và chia với biểu thức liên hợp:\n"
        f"$$\\lim \\left(n - \\sqrt{{n^2 - {2*k}n + {c}}}\\right) "
        f"= \\lim \\frac{{n^2 - (n^2 - {2*k}n + {c})}}{{n + \\sqrt{{n^2 - {2*k}n + {c}}}}} "
        f"= \\lim \\frac{{{2*k}n - {c}}}{{n + \\sqrt{{n^2 - {2*k}n + {c}}}}} "
        f"= \\lim \\frac{{{2*k} - \\frac{{{c}}}{{n}}}}{{1 + \\sqrt{{1 - \\frac{{{2*k}}}{{n}} + \\frac{{{c}}}{{n^2}}}}}} "
        f"= \\frac{{{2*k}}}{{1 + 1}} = {k}.$$"
    )
    return caudan, choices, loigiai

def k11_mc_c5_gioi_han_phan_thuc_bac_hai_bac_ba():
    """MC: lim (an - b)(cn + d) / (en^2 + fn + g) = (ac)/e."""
    a, b = 2, 3
    c, d = 3, 1
    e = 6
    # (2n - 3)(3n + 1) / (6n^2 + n + 1) -> 6/6 = 1
    caudan = f"Giới hạn $L = \\lim \\frac{{({a}n - {b})({c}n + {d})}}{{{e}n^2 + n + 1}}$ bằng:"
    correct = "$1$"
    wrongs = ["$0$", "$-\\infty$", "$+\\infty$"]
    choices = _make_mc_choices(correct, wrongs)
    loigiai = (
        f"Khai triển bậc cao nhất ở tử số:\n"
        f"$$({a}n - {b})({c}n + {d}) = {a*c}n^2 + ({a*d - b*c})n - {b*d}.$$\n"
        f"Chia cả tử và mẫu cho $n^2$:\n"
        f"$$L = \\lim \\frac{{{a*c} + \\frac{{{a*d - b*c}}}{{n}} - \\frac{{{b*d}}}{{n^2}}}}{{{e} + \\frac{{1}}{{n}} + \\frac{{1}}{{n^2}}}} = \\frac{{{a*c}}}{{{e}}} = 1.$$"
    )
    return caudan, choices, loigiai

def k11_tf_c5_khao_sat_hai_day_bac_hai():
    """TF: Cho u_n = 4n^2 - n + 3, v_n = 3n^2 + 7. Xét tính đúng sai."""
    caudan = "Cho hai dãy số $(u_n)$ và $(v_n)$ có $u_n = 4n^2 - n + 3; v_n = 3n^2 + 7$. Xét tính đúng sai của các khẳng định sau:"
    items = [
        (True, "$\\lim \\frac{u_n}{v_n} = \\frac{4}{3}$."),
        (False, "$\\lim \\frac{u_n}{(v_n)^2} = \\frac{4}{9}$."),
        (False, "$\\lim \\frac{(u_n)^2}{v_n} = \\frac{16}{3}$."),
        (True, "$\\lim \\frac{u_n + an^2 + 7}{v_n} = 8$ khi đó $a = 20$.")
    ]
    choices = _make_tf_choices(items)
    loigiai = (
        "\\begin{itemchoice}\n"
        "\\itemch Đúng. Hai đa thức cùng bậc $2$ nên $\\lim \\frac{u_n}{v_n} = \\frac{4}{3}$.\n"
        "\\itemch Sai. Vì bậc của $(v_n)^2$ là $4$, lớn hơn bậc của $u_n$ (bậc $2$) nên $\\lim \\frac{u_n}{(v_n)^2} = 0$.\n"
        "\\itemch Sai. Vì bậc của $(u_n)^2$ là $4$, lớn hơn bậc của $v_n$ (bậc $2$) nên $\\lim \\frac{(u_n)^2}{v_n} = +\\infty$.\n"
        "\\itemch Đúng. $\\lim \\frac{u_n + an^2 + 7}{v_n} = \\lim \\frac{(4+a)n^2 - n + 10}{3n^2 + 7} = \\frac{4+a}{3}$. "
        "Theo giả thiết $\\frac{4+a}{3} = 8 \\Leftrightarrow 4 + a = 24 \\Leftrightarrow a = 20$.\n"
        "\\end{itemchoice}"
    )
    return caudan, choices, loigiai

def k11_tf_c5_gioi_han_lien_mon_parabol_luong_giac():
    """TF: lim (5n^3 - 2n + 1)/(n - 2n^3) = a = -5/2 liên kết kiến thức."""
    caudan = "Biết giới hạn $\\lim \\frac{5n^3 - 2n + 1}{n - 2n^3} = a$. Khi đó, xét tính đúng sai của các khẳng định sau:"
    items = [
        (True, "Giá trị $a < 0$."),
        (True, "$x = a$ là trục đối xứng của parabol $(P): y = x^2 + 5x + 2$."),
        (True, "Phương trình lượng giác $\\sin x = a$ vô nghiệm."),
        (False, "Cho cấp số cộng $(u_n)$ với công sai $d = 3$ và $u_1 = a$, thì $u_3 = 6$.")
    ]
    choices = _make_tf_choices(items)
    loigiai = (
        "\\begin{itemchoice}\n"
        "\\itemch Đúng. Chia cả tử và mẫu cho $n^3$: $a = \\lim \\frac{5 - 2/n^2 + 1/n^3}{1/n^2 - 2} = -\\frac{5}{2} = -2,5 < 0$.\n"
        "\\itemch Đúng. Trục đối xứng của parabol $(P)$ là $x = -\\frac{b}{2a'} = -\\frac{5}{2(1)} = -\\frac{5}{2} = a$.\n"
        "\\itemch Đúng. Phương trình $\\sin x = -2,5$ vô nghiệm do $|-2,5| > 1$.\n"
        "\\itemch Sai. Công thức số hạng tổng quát của CSC: $u_3 = u_1 + 2d = -\\frac{5}{2} + 2(3) = \\frac{7}{2} = 3,5 \\neq 6$.\n"
        "\\end{itemchoice}"
    )
    return caudan, choices, loigiai

def k11_sa_c5_tong_csn_lui_vo_han():
    """SA: Tính tổng cấp số nhân lùi vô hạn S = 1 - 1/2 + 1/4 - 1/8 + ..."""
    # S = 1 / (1 - (-1/2)) = 2/3 approx 0.67
    caudan = (
        "Tính tổng cấp số nhân lùi vô hạn $S = 1 - \\frac{1}{2} + \\frac{1}{4} - \\frac{1}{8} + \\dots$ "
        "(làm tròn kết quả đến hàng phần trăm)."
    )
    ans = "0.67"
    loigiai = (
        "Áp dụng công thức tính tổng cấp số nhân lùi vô hạn với $u_1 = 1, q = -\\frac{1}{2}$:\n"
        "$$S = \\frac{u_1}{1 - q} = \\frac{1}{1 - \\left(-\\frac{1}{2}\\right)} = \\frac{1}{3/2} = \\frac{2}{3} \\approx 0,67.$$"
    )
    return caudan, ans, loigiai

def k11_sa_c5_lien_hop_vo_dinh():
    """SA: lim(n - sqrt(n^2 - 4n + 1)) = 2."""
    caudan = "Tính giới hạn $L = \\lim \\left(n - \\sqrt{n^2 - 4n + 1}\\right)$."
    ans = "2"
    loigiai = (
        "Nhân lượng liên hợp:\n"
        "$$L = \\lim \\frac{n^2 - (n^2 - 4n + 1)}{n + \\sqrt{n^2 - 4n + 1}} "
        "= \\lim \\frac{4n - 1}{n + \\sqrt{n^2 - 4n + 1}} = \\lim \\frac{4 - 1/n}{1 + \\sqrt{1 - 4/n + 1/n^2}} = \\frac{4}{1 + 1} = 2.$$"
    )
    return caudan, ans, loigiai


def k11_mc_c5_gh_ham_so_0_chia_0():
    """MC: Giới hạn vô định 0/0 dạng phân thức hữu tỉ lim_{x->x0} (x^2 + ax + b)/(x^2 + cx)."""
    x0 = random.choice([-4, -3, -2, 2, 3, 4])
    r = random.choice([1, 2, -1, -2])
    while r == x0 or r == 0:
        r = random.choice([1, 2, -1, -2])
    # Tử = (x - x0)(x - r) = x^2 - (x0+r)x + x0*r
    # Mẫu = x(x - x0) = x^2 - x0*x
    b1 = -(x0 + r)
    c1 = x0 * r
    num = x0 - r
    den = x0
    from fractions import Fraction
    frac = Fraction(num, den)
    ans_tex = _fmt_frac(frac.numerator, frac.denominator)
    
    b1_str = f"+ {b1}x" if b1 > 0 else (f"- {-b1}x" if b1 < 0 else "")
    c1_str = f"+ {c1}" if c1 > 0 else (f"- {-c1}" if c1 < 0 else "")
    m_str = f"- {x0}x" if x0 > 0 else f"+ {-x0}x"
    
    caudan = f"Giá trị của giới hạn $\\lim_{{x \\to {x0}}} \\frac{{x^2 {b1_str} {c1_str}}}{{x^2 {m_str}}}$ bằng:"
    correct = f"${ans_tex}$"
    wrongs = [f"${_fmt_frac(-frac.numerator, frac.denominator)}$", "$1$", "$0$"]
    choices = _make_mc_choices(correct, wrongs)
    loigiai = (
        f"Phân tích tử và mẫu thành nhân tử để khử dạng vô định $\\frac{{0}}{{0}}$:\n"
        f"$$\\lim_{{x \\to {x0}}} \\frac{{(x - {x0})(x - {r})}}{{x(x - {x0})}} "
        f"= \\lim_{{x \\to {x0}}} \\frac{{x - {r}}}{{x}} = \\frac{{{x0} - {r}}}{{{x0}}} = {ans_tex}.$$\n"
    )
    return caudan, choices, loigiai

def k11_mc_c5_gh_ham_so_mot_ben():
    """MC: Giới hạn một bên vô cực lim_{x -> x0^+} (ax + b)/(x - x0)."""
    x0 = random.choice([2, 3, 4, 5])
    a = random.choice([1, 2])
    val_tu = a * x0 - 15
    caudan = f"Tính giới hạn $L = \\lim_{{x \\to {x0}^+}} \\frac{{{a}x - 15}}{{x - {x0}}}$."
    correct = "$-\\infty$"
    wrongs = ["$+\\infty$", "$0$", "$1$"]
    choices = _make_mc_choices(correct, wrongs)
    loigiai = (
        f"Khi $x \\to {x0}^+$ ta có:\n"
        f"- Tử số $\\lim_{{x \\to {x0}^+}} ({a}x - 15) = {val_tu} < 0$.\n"
        f"- Mẫu số $\\lim_{{x \\to {x0}^+}} (x - {x0}) = 0$ và $x - {x0} > 0$ với mọi $x > {x0}$.\n"
        f"Do đó $L = -\\infty$."
    )
    return caudan, choices, loigiai

def k11_mc_c5_gh_ham_so_vo_cuc_da_thuc():
    """MC: Giới hạn tại vô cực của đa thức lim_{x -> -inf} (ax^{2k+1} + bx^2 + c)."""
    a = random.choice([2, 3, 5])
    caudan = f"Tìm giới hạn $L = \\lim_{{x \\to -\\infty}} ({a}x^5 - 3x^2 + 1)$."
    correct = "$-\\infty$"
    wrongs = ["$+\\infty$", "$0$", "$2$"]
    choices = _make_mc_choices(correct, wrongs)
    loigiai = (
        f"Đặt $x^5$ làm nhân tử chung:\n"
        f"$$L = \\lim_{{x \\to -\\infty}} x^5 \\left({a} - \\frac{{3}}{{x^3}} + \\frac{{1}}{{x^5}}\\right).$$ "
        f"Vì $\\lim_{{x \\to -\\infty}} x^5 = -\\infty$ (bậc lẻ) và $\\lim_{{x \\to -\\infty}} \\left({a} - \\frac{{3}}{{x^3}} + \\frac{{1}}{{x^5}}\\right) = {a} > 0$, nên $L = -\\infty$."
    )
    return caudan, choices, loigiai

def k11_mc_c5_gh_ham_so_vo_cuc_phan_thuc():
    """MC: Giới hạn tại vô cực của phân thức bậc nhất lim_{x -> +inf} (1 - 3x)/(2x + 3) = -3/2."""
    caudan = "Tính giới hạn $L = \\lim_{x \\to +\\infty} \\frac{1 - 3x}{2x + 3}$."
    correct = "$-\\frac{3}{2}$"
    wrongs = ["$-3$", "$\\frac{1}{2}$", "$-\\infty$"]
    choices = _make_mc_choices(correct, wrongs)
    loigiai = (
        "Chia cả tử và mẫu cho $x$:\n"
        "$$L = \\lim_{x \\to +\\infty} \\frac{\\frac{1}{x} - 3}{2 + \\frac{3}{x}} = \\frac{0 - 3}{2 + 0} = -\\frac{3}{2}.$$"
    )
    return caudan, choices, loigiai

def k11_mc_c5_ham_so_lien_tuc_tai_diem():
    """MC: Tính liên tục của hàm số tại một điểm."""
    caudan = (
        "Cho hàm số $f(x) = \\begin{cases} \\frac{x^2 - 4}{x - 2} & \\text{khi } x \\neq 2 \\\\ "
        "k & \\text{khi } x = 2 \\end{cases}$. Tìm giá trị của $k$ để hàm số liên tục tại điểm $x_0 = 2$."
    )
    correct = "$k = 4$"
    wrongs = ["$k = 2$", "$k = 0$", "$k = -4$"]
    choices = _make_mc_choices(correct, wrongs)
    loigiai = (
        "Hàm số liên tục tại $x_0 = 2$ khi và chỉ khi $\\lim_{x \\to 2} f(x) = f(2)$.\n"
        "Ta có: $f(2) = k$, và:\n"
        "$$\\lim_{x \\to 2} f(x) = \\lim_{x \\to 2} \\frac{x^2 - 4}{x - 2} = \\lim_{x \\to 2} (x + 2) = 4.$$\n"
        "Vậy $k = 4$."
    )
    return caudan, choices, loigiai

def k11_mc_c5_ham_so_lien_tuc_tren_R():
    """MC: Nhận biết hàm số liên tục trên R."""
    caudan = "Trong các hàm số sau, hàm số nào liên tục trên toàn bộ tập số thực $\\mathbb{R}$?"
    correct = "$f(x) = x^3 - 3x^2 + 2x - 1$"
    wrongs = [
        "$f(x) = \\frac{x+1}{x-2}$",
        "$f(x) = \\tan x$",
        "$f(x) = \\sqrt{x-1}$"
    ]
    choices = _make_mc_choices(correct, wrongs)
    loigiai = (
        "Theo định lí về tính liên tục của các hàm số sơ cấp:\n"
        "- Hàm đa thức $f(x) = x^3 - 3x^2 + 2x - 1$ xác định và liên tục trên toàn bộ $\\mathbb{R}$.\n"
        "- Hàm phân thức hữu tỉ $f(x) = \\frac{x+1}{x-2}$ gián đoạn tại $x = 2$.\n"
        "- Hàm lượng giác $f(x) = \\tan x$ gián đoạn tại các điểm $x = \\frac{\\pi}{2} + k\\pi$.\n"
        "- Hàm căn thức $f(x) = \\sqrt{x-1}$ chỉ xác định và liên tục trên $[1; +\\infty)$."
    )
    return caudan, choices, loigiai

def k11_tf_c5_khao_sat_ham_so_lien_tuc_phan_nhanh():
    """TF: Khảo sát f(x) phân nhánh tại x=1 và g(x) đa thức."""
    caudan = (
        "Cho hai hàm số $f(x) = \\begin{cases} \\frac{x^2 - 1}{x - 1} & \\text{khi } x \\neq 1 \\\\ "
        "x + 1 & \\text{khi } x = 1 \\end{cases}$ và $g(x) = 4x^2 - x + 1$. "
        "Xét tính đúng sai của các mệnh đề sau:"
    )
    items = [
        (True, "$f(1) = 2$."),
        (True, "Hàm số $f(x)$ liên tục tại điểm $x_0 = 1$."),
        (True, "Hàm số $g(x)$ liên tục tại điểm $x_0 = 1$."),
        (False, "Hàm số $y = f(x) - g(x)$ không liên tục tại điểm $x_0 = 1$.")
    ]
    choices = _make_tf_choices(items)
    loigiai = (
        "\\begin{itemchoice}\n"
        "\\itemch Đúng. Theo định nghĩa, khi $x = 1$ thì $f(1) = 1 + 1 = 2$.\n"
        "\\itemch Đúng. $\\lim_{x \\to 1} f(x) = \\lim_{x \\to 1} \\frac{(x-1)(x+1)}{x-1} = \\lim_{x \\to 1} (x+1) = 2 = f(1)$ nên $f(x)$ liên tục tại $x_0 = 1$.\n"
        "\\itemch Đúng. Hàm số $g(x)$ là đa thức nên liên tục trên $\\mathbb{R}$, do đó liên tục tại $x_0 = 1$.\n"
        "\\itemch Sai. Vì $f(x)$ và $g(x)$ đều liên tục tại $x_0 = 1$ nên hiệu $y = f(x) - g(x)$ cũng liên tục tại $x_0 = 1$.\n"
        "\\end{itemchoice}"
    )
    return caudan, choices, loigiai

def k11_tf_c5_toan_thuc_te_gia_do_xe_lien_tuc():
    """TF: Bài toán thực tế giá tiền đỗ xe ô tô và tính liên tục."""
    caudan = (
        "Một bãi đậu xe ô tô đưa ra giá cước $T(x)$ (đồng) theo thời gian đậu xe $x$ (giờ) như sau:\n"
        "$$T(x) = \\begin{cases} "
        "50\\,000 & \\text{khi } 0 < x \\le 2 \\\\ "
        "120\\,000 & \\text{khi } 2 < x < 4 \\\\ "
        "35\\,000x & \\text{khi } x \\ge 4 "
        "\\end{cases}$$\n"
        "Xét tính đúng sai của các mệnh đề sau:"
    )
    items = [
        (True, "$T(2) = 50\\,000$ đồng."),
        (True, "$\\lim_{x \\to 4^-} T(x) = 120\\,000$."),
        (False, "Hàm số $T(x)$ liên tục tại điểm $x = 4$."),
        (True, "Hàm số $T(x)$ liên tục trên $[4; +\\infty)$.")
    ]
    choices = _make_tf_choices(items)
    loigiai = (
        "\\begin{itemchoice}\n"
        "\\itemch Đúng. Với $x = 2$, thuộc khoảng $0 < x \\le 2$ nên $T(2) = 50\\,000$.\n"
        "\\itemch Đúng. Khi $x \\to 4^-$ (tức $2 < x < 4$), $T(x) = 120\\,000$ nên giới hạn bằng $120\\,000$.\n"
        "\\itemch Sai. Ta có $\\lim_{x \\to 4^+} T(x) = 35\\,000 \\times 4 = 140\\,000 \\neq \\lim_{x \\to 4^-} T(x) = 120\\,000$. "
        "Do giới hạn hai bên khác nhau nên hàm số không liên tục tại $x = 4$.\n"
        "\\itemch Đúng. Trên $[4; +\\infty)$, $T(x) = 35\\,000x$ là hàm bậc nhất nên liên tục trên $[4; +\\infty)$.\n"
        "\\end{itemchoice}"
    )
    return caudan, choices, loigiai

def k11_tf_c5_toan_thuc_te_chi_phi_san_xuat_lien_tuc():
    """TF: Bài toán thực tế hàm chi phí sản xuất C = f(Q)."""
    caudan = (
        "Chi phí sản xuất $C$ phụ thuộc lượng đầu ra của sản phẩm $Q$ (đơn vị: nghìn chiếc) được xác định bởi:\n"
        "$$C = f(Q) = \\begin{cases} "
        "2000 & \\text{nếu } 0 < Q \\le 4 \\\\ "
        "Q^3 - 6Q^2 + 140Q + 1500 & \\text{nếu } Q > 4 "
        "\\end{cases}$$\n"
        "Xét tính đúng sai của các khẳng định sau:"
    )
    items = [
        (False, "Hàm số liên tục tại điểm $Q = 4$."),
        (True, "Hàm số gián đoạn tại điểm $Q = 4$."),
        (False, "$\\lim_{Q \\to 4^-} f(Q) = \\lim_{Q \\to 4^+} f(Q)$."),
        (True, "$\\lim_{Q \\to 4^-} f(Q) = 2000$.")
    ]
    choices = _make_tf_choices(items)
    loigiai = (
        "\\begin{itemchoice}\n"
        "\\itemch Sai. $\\lim_{Q \\to 4^+} f(Q) = 4^3 - 6(4^2) + 140(4) + 1500 = 64 - 96 + 560 + 1500 = 2028 \\neq f(4) = 2000$.\n"
        "\\itemch Đúng. Vì $\\lim_{Q \\to 4^+} f(Q) \\neq \\lim_{Q \\to 4^-} f(Q) = 2000$ nên hàm số gián đoạn tại $Q = 4$.\n"
        "\\itemch Sai. Vì giới hạn bên trái bằng $2000$ còn giới hạn bên phải bằng $2028$.\n"
        "\\itemch Đúng. Khi $Q \\to 4^-$ thì $f(Q) = 2000$ nên $\\lim_{Q \\to 4^-} f(Q) = 2000$.\n"
        "\\end{itemchoice}"
    )
    return caudan, choices, loigiai

def k11_sa_c5_tim_tham_so_a_ham_lien_tuc():
    """SA: Tìm tham số a để hàm phân nhánh có giới hạn/liên tục tại x0."""
    caudan = (
        "Cho hàm số $f(x) = \\begin{cases} "
        "\\frac{x^2 - 4}{x - 2} & \\text{khi } x > 2 \\\\ "
        "ax + 1 & \\text{khi } x \\le 2 "
        "\\end{cases}$. "
        "Tìm giá trị của tham số $a$ để hàm số liên tục tại điểm $x = 2$."
    )
    ans = "1.5"
    loigiai = (
        "Ta có:\n"
        "- Khi $x > 2$: $\\lim_{x \\to 2^+} f(x) = \\lim_{x \\to 2^+} \\frac{x^2 - 4}{x - 2} = \\lim_{x \\to 2^+} (x + 2) = 4$.\n"
        "- Khi $x \\le 2$: $\\lim_{x \\to 2^-} f(x) = f(2) = 2a + 1$.\n"
        "Để hàm số liên tục tại $x = 2$ thì $\\lim_{x \\to 2^+} f(x) = \\lim_{x \\to 2^-} f(x) = f(2)$\n"
        "$$\\Leftrightarrow 2a + 1 = 4 \\Leftrightarrow 2a = 3 \\Leftrightarrow a = 1,5.$$"
    )
    return caudan, ans, loigiai

def k11_sa_c5_gioi_han_0_chia_0_can_thuc():
    """SA: lim_{x -> 3} (sqrt(x+1) - 2) / (x - 3) = 1/4 = 0.25."""
    caudan = "Tính giới hạn $L = \\lim_{x \\to 3} \\frac{\\sqrt{x+1} - 2}{x - 3}$."
    ans = "0.25"
    loigiai = (
        "Nhân lượng liên hợp khử dạng vô định $\\frac{0}{0}$:\n"
        "$$L = \\lim_{x \\to 3} \\frac{(x+1) - 4}{(x - 3)(\\sqrt{x+1} + 2)} "
        "= \\lim_{x \\to 3} \\frac{x - 3}{(x - 3)(\\sqrt{x+1} + 2)} "
        "= \\lim_{x \\to 3} \\frac{1}{\\sqrt{x+1} + 2} = \\frac{1}{2 + 2} = \\frac{1}{4} = 0,25.$$"
    )
    return caudan, ans, loigiai
