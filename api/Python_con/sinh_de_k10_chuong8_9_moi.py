import random
import math
from fractions import Fraction

def _fmt_frac(n, d):
    f = Fraction(n, d)
    if f.denominator == 1:
        return str(f.numerator)
    return f"\\frac{{{f.numerator}}}{{{f.denominator}}}"

def _make_tf_choices(items_data):
    # items_data is list of (is_true, text)
    res = []
    for is_true, text in items_data:
        prefix = "\\True " if is_true else ""
        res.append(f"{{{prefix}{text}}} ")
    return res

# =========================================================================
# CHƯƠNG VIII: ĐẠI SỐ TỔ HỢP - TRẮC NGHIỆM ĐÚNG / SAI (TF)
# =========================================================================

def k10_tf_c8_chon_hoa_ly_hong_lan():
    """Đúng/Sai: Bài toán cửa hàng hoa (Quy tắc cộng và quy tắc nhân)."""
    ly = random.randint(6, 9)
    hong = random.randint(12, 16)
    lan = random.randint(5, 8)
    
    # a) Chọn 1 bông hoa: ly + hong + lan
    ans_a = ly + hong + lan
    # b) Chọn 3 bông khác loại: ly * hong * lan
    ans_b = ly * hong * lan
    # c) Chọn 2 bông khác loại: ly*hong + hong*lan + lan*ly
    ans_c = ly * hong + hong * lan + lan * ly
    # d) Chọn 1 bông hoa Hồng: hong
    ans_d = hong
    
    a_ok = random.choice([True, False])
    b_ok = random.choice([True, False])
    c_ok = random.choice([True, False])
    d_ok = random.choice([True, False])
    
    sh_a = ans_a if a_ok else ans_a + 2
    sh_b = ans_b if b_ok else ans_b + 50
    sh_c = ans_c if c_ok else ans_c * 10 + 26
    sh_d = ans_d if d_ok else ans_d - 2
    
    caudan = (
        f"Một cửa hàng có ${ly}$ bông hoa Ly, ${hong}$ bông hoa Hồng và ${lan}$ bông hoa Lan. "
        f"Bạn Nam muốn mua một số bông hoa từ cửa hàng đó. Xét tính đúng sai của các khẳng định sau:"
    )
    choices = _make_tf_choices([
        (a_ok, f"Có ${sh_a}$ cách chọn mua $1$ bông hoa từ cửa hàng."),
        (b_ok, f"Có ${sh_b}$ cách chọn mua một bó gồm $3$ bông khác loại từ cửa hàng."),
        (c_ok, f"Có ${sh_c}$ cách chọn mua $2$ bông khác loại từ cửa hàng."),
        (d_ok, f"Có ${sh_d}$ cách chọn mua $1$ bông Hồng từ cửa hàng.")
    ])
    loigiai = (
        f"\\begin{{itemchoice}}\n"
        f"\\itemch {'Đúng' if a_ok else 'Sai'}. Mua $1$ bông hoa bất kì có: ${ly} + {hong} + {lan} = {ans_a}$ cách.\n"
        f"\\itemch {'Đúng' if b_ok else 'Sai'}. Mua $3$ bông khác loại (mỗi loại 1 bông) có: ${ly} \\times {hong} \\times {lan} = {ans_b}$ cách.\n"
        f"\\itemch {'Đúng' if c_ok else 'Sai'}. Mua $2$ bông khác loại có: ${ly} \\times {hong} + {hong} \\times {lan} + {lan} \\times {ly} = {ans_c}$ cách.\n"
        f"\\itemch {'Đúng' if d_ok else 'Sai'}. Mua $1$ bông Hồng có: ${hong}$ cách.\n"
        f"\\end{{itemchoice}}"
    )
    return caudan, choices, loigiai

def k10_tf_c8_xep_hang_nam_nu():
    """Đúng/Sai: Xếp hàng dọc học sinh nam và nữ (hoán vị, vách ngăn)."""
    nam = random.randint(4, 6)
    nu = random.randint(3, 4)
    tot = nam + nu
    
    ans_a = math.factorial(tot)
    ans_b = 2 * math.factorial(nam) * math.factorial(nu)
    ans_c = math.factorial(nam + 1) * math.factorial(nu)
    ans_d = math.factorial(nam) * math.perm(nam + 1, nu)
    
    a_ok = random.choice([True, False])
    b_ok = random.choice([True, False])
    c_ok = random.choice([True, False])
    d_ok = random.choice([True, False])
    
    sh_a = ans_a if a_ok else ans_a // 2
    sh_b = ans_b if b_ok else ans_b // 2
    sh_c = ans_c if c_ok else ans_c // 2
    sh_d = ans_d if d_ok else ans_d // 6
    
    caudan = f"Có ${nam}$ nam sinh và ${nu}$ nữ sinh cần được xếp vào một hàng dọc. Xét tính đúng sai của các khẳng định sau:"
    choices = _make_tf_choices([
        (a_ok, f"Số cách xếp ${tot}$ học sinh theo một hàng dọc là ${sh_a}$ cách."),
        (b_ok, f"Số cách xếp học sinh cùng giới đứng cạnh nhau là ${sh_b}$ cách."),
        (c_ok, f"Số cách xếp học sinh nữ luôn đứng cạnh nhau là ${sh_c}$ cách."),
        (d_ok, f"Số cách xếp không có em nữ nào đứng cạnh nhau là ${sh_d}$ cách.")
    ])
    loigiai = (
        f"\\begin{{itemchoice}}\n"
        f"\\itemch {'Đúng' if a_ok else 'Sai'}. Xếp ${tot}$ bạn có ${tot}! = {ans_a}$ cách.\n"
        f"\\itemch {'Đúng' if b_ok else 'Sai'}. Học sinh cùng giới cạnh nhau: có $2! \\times {nam}! \\times {nu}! = {ans_b}$ cách.\n"
        f"\\itemch {'Đúng' if c_ok else 'Sai'}. Coi ${nu}$ nữ là $1$ phần tử, xếp cùng ${nam}$ nam có: $({nam} + 1)! \\times {nu}! = {ans_c}$ cách.\n"
        f"\\itemch {'Đúng' if d_ok else 'Sai'}. Xếp ${nam}$ nam có ${nam}!$ cách tạo ra ${nam+1}$ vị trí trống, xếp ${nu}$ nữ vào có $A_{{{nam+1}}}^{{{nu}}}$ cách. "
        f"Vậy có ${nam}! \\times A_{{{nam+1}}}^{{{nu}}} = {ans_d}$ cách.\n"
        f"\\end{{itemchoice}}"
    )
    return caudan, choices, loigiai

def k10_tf_c8_xep_ghe_dai_5_ban():
    """Đúng/Sai: Sắp xếp 5 bạn học sinh An, Bình, Chi, Dũng, Lan vào ghế dài 5 chỗ."""
    ans_a = math.factorial(5) # 120
    ans_b = math.factorial(4) # 24
    ans_c = 2 * math.factorial(3) # 12
    ans_d = 2 * math.factorial(4) # 48
    
    a_ok = random.choice([True, False])
    b_ok = random.choice([True, False])
    c_ok = random.choice([True, False])
    d_ok = random.choice([True, False])
    
    sh_a = ans_a if a_ok else 100
    sh_b = ans_b if b_ok else 16
    sh_c = ans_c if c_ok else 24
    sh_d = ans_d if d_ok else 36
    
    caudan = "Sắp xếp $5$ bạn học sinh An, Bình, Chi, Dũng, Lan vào một chiếc ghế dài có $5$ chỗ ngồi. Xét tính đúng sai của các khẳng định sau:"
    choices = _make_tf_choices([
        (a_ok, f"Có ${sh_a}$ cách sắp xếp tùy ý."),
        (b_ok, f"Có ${sh_b}$ cách sắp xếp sao cho bạn Chi luôn ngồi chính giữa."),
        (c_ok, f"Có ${sh_c}$ cách sắp xếp sao cho bạn An và bạn Dũng luôn ngồi ở hai đầu ghế."),
        (d_ok, f"Có ${sh_d}$ cách sắp xếp sao cho An và Bình ngồi cạnh nhau.")
    ])
    loigiai = (
        f"\\begin{{itemchoice}}\n"
        f"\\itemch {'Đúng' if a_ok else 'Sai'}. Số cách xếp tùy ý là $5! = {ans_a}$.\n"
        f"\\itemch {'Đúng' if b_ok else 'Sai'}. Chi ngồi chính giữa có $1$ cách, xếp $4$ bạn còn lại có $4! = {ans_b}$ cách.\n"
        f"\\itemch {'Đúng' if c_ok else 'Sai'}. Xếp An và Dũng ở $2$ đầu ghế có $2! = 2$ cách, $3$ bạn còn lại có $3! = 6$ cách. Vậy có $2 \\times 6 = {ans_c}$ cách.\n"
        f"\\itemch {'Đúng' if d_ok else 'Sai'}. Coi An và Bình là $1$ phần tử, có $2! \\times 4! = {ans_d}$ cách.\n"
        f"\\end{{itemchoice}}"
    )
    return caudan, choices, loigiai

def k10_tf_c8_chon_hoc_sinh_phan_khoi_abc():
    """Đúng/Sai: Chọn 15 học sinh từ 15 khối A, 10 khối B, 5 khối C."""
    # 15 A, 10 B, 5 C -> 30 HS, chọn 15
    ans_a = math.comb(15, 5) * math.comb(10, 5) * math.comb(5, 5) # 756756
    ans_b_text = "C_5^2 C_{25}^{13}"
    ans_c_text = "C_5^2 C_{10}^{10} C_{15}^3"
    
    # d: it nhat 5 A va dung 2 C
    c_rem = math.comb(25, 13) - math.comb(15, 3) * math.comb(10, 10) - math.comb(15, 4) * math.comb(10, 9)
    ans_d = math.comb(5, 2) * c_rem # 51861950
    
    a_ok = random.choice([True, False])
    b_ok = random.choice([True, False])
    c_ok = random.choice([True, False])
    d_ok = random.choice([True, False])
    
    sh_a = ans_a if a_ok else 252252
    sh_b_str = ans_b_text if b_ok else "C_5^2 C_{15}^{13}"
    sh_c_str = ans_c_text if c_ok else "C_5^3 C_{10}^{10} C_{15}^2"
    sh_d = ans_d if d_ok else ans_d - 1000000
    
    caudan = (
        "Từ một nhóm $30$ học sinh lớp 12 gồm $15$ học sinh khối A, $10$ học sinh khối B và $5$ học sinh khối C, "
        "cần chọn ra $15$ học sinh. Xét tính đúng sai của các khẳng định sau:"
    )
    choices = _make_tf_choices([
        (a_ok, f"Số cách chọn để học sinh mỗi khối là bằng nhau là ${sh_a}$."),
        (b_ok, f"Số cách chọn để có $2$ học sinh khối C, $13$ học sinh khối B hoặc khối A là ${sh_b_str}$ cách."),
        (c_ok, f"Số cách chọn để có $2$ học sinh khối C, $10$ học sinh khối B và $3$ học sinh khối A là ${sh_c_str}$ cách."),
        (d_ok, f"Số cách chọn để có ít nhất $5$ học sinh khối A và có đúng $2$ học sinh khối C là ${sh_d}$ cách.")
    ])
    loigiai = (
        f"\\begin{{itemchoice}}\n"
        f"\\itemch {'Đúng' if a_ok else 'Sai'}. Mỗi khối $5$ học sinh: $C_{{15}}^5 C_{{10}}^5 C_5^5 = {ans_a}$ cách.\n"
        f"\\itemch {'Đúng' if b_ok else 'Sai'}. Chọn $2$ HS khối C có $C_5^2$, chọn $13$ HS từ khối A và B ($25$ em) có $C_{{25}}^{{13}}$ cách. "
        f"Vậy là $C_5^2 C_{{25}}^{{13}}$ cách.\n"
        f"\\itemch {'Đúng' if c_ok else 'Sai'}. Chọn $2$ C, $10$ B, $3$ A có $C_5^2 C_{{10}}^{{10}} C_{{15}}^3$ cách.\n"
        f"\\itemch {'Đúng' if d_ok else 'Sai'}. Chọn $2$ C có $C_5^2 = 10$ cách. Cần chọn $13$ HS từ $25$ HS (15 A, 10 B) sao cho số HS khối A $\\ge 5$. "
        f"Số cách chọn bằng $C_5^2 [C_{{25}}^{{13}} - C_{{15}}^3 C_{{10}}^{{10}} - C_{{15}}^4 C_{{10}}^9] = {ans_d}$ cách.\n"
        f"\\end{{itemchoice}}"
    )
    return caudan, choices, loigiai

def k10_tf_c8_nhi_thuc_newton_he_so_phan_thuc():
    """Đúng/Sai: Khai triển (1 - 1/2 x)^5 = a_0 + a_1 x + ... + a_5 x^5."""
    # a_k = C_5^k * (-1/2)^k
    # a_3 = C_5^3 * (-1/8) = -10/8 = -5/4 (hoặc nếu là 2x thì khác)
    # Trong đề: (1 - 1/2 x)^5:
    # a_0 = 1, a_1 = -5/2, a_2 = 10/4 = 5/2, a_3 = -10/8 = -5/4, a_4 = 5/16, a_5 = -1/32
    # a_3 = 5/2 (Sai, a_3 = -5/4)
    # a_5 = -1/32 (Đúng)
    # Hệ số lớn nhất: max là a_2 = 5/2 (Đúng)
    # Tổng a_0 + ... + a_5 = P(1) = (1/2)^5 = 1/32 (Sai vì đề ghi 1/16)
    a_ok = random.choice([True, False])
    b_ok = random.choice([True, False])
    c_ok = random.choice([True, False])
    d_ok = random.choice([True, False])
    
    sh_a = "-\\frac{5}{4}" if a_ok else "\\frac{5}{2}"
    sh_b = "-\\frac{1}{32}" if b_ok else "\\frac{1}{32}"
    sh_c = "\\frac{5}{2}" if c_ok else "1"
    sh_d = "\\frac{1}{32}" if d_ok else "\\frac{1}{16}"
    
    caudan = r"Cho khai triển $\left(1 - \frac{1}{2}x\right)^5 = a_0 + a_1 x + a_2 x^2 + a_3 x^3 + a_4 x^4 + a_5 x^5$. Xét tính đúng sai của các mệnh đề sau:"
    choices = _make_tf_choices([
        (a_ok, f"$a_3 = {sh_a}$."),
        (b_ok, f"$a_5 = {sh_b}$."),
        (c_ok, f"Hệ số lớn nhất trong tất cả các hệ số của khai triển là ${sh_c}$."),
        (d_ok, f"Tổng $a_0 + a_1 + a_2 + a_3 + a_4 + a_5 = {sh_d}$.")
    ])
    loigiai = (
        f"\\begin{{itemchoice}}\n"
        f"\\itemch {'Đúng' if a_ok else 'Sai'}. Số hạng chứa $x^3$ là $C_5^3 \\cdot 1^2 \\cdot \\left(-\\frac{{1}}{{2}}x\\right)^3 = -\\frac{{10}}{{8}}x^3 = -\\frac{{5}}{{4}}x^3 \\implies a_3 = -\\frac{{5}}{{4}}$.\n"
        f"\\itemch {'Đúng' if b_ok else 'Sai'}. Số hạng $a_5 x^5 = \\left(-\\frac{{1}}{{2}}x\\right)^5 = -\\frac{{1}}{{32}}x^5 \\implies a_5 = -\\frac{{1}}{{32}}$.\n"
        f"\\itemch {'Đúng' if c_ok else 'Sai'}. Các hệ số dương là $a_0 = 1, a_2 = \\frac{{5}}{{2}}, a_4 = \\frac{{5}}{{16}}$. Do đó hệ số lớn nhất là $a_2 = \\frac{{5}}{{2}}$.\n"
        f"\\itemch {'Đúng' if d_ok else 'Sai'}. Cho $x = 1$, ta có $P(1) = \\left(1 - \\frac{{1}}{{2}}\\right)^5 = \\frac{{1}}{{32}}$.\n"
        f"\\end{{itemchoice}}"
    )
    return caudan, choices, loigiai

def k10_tf_c8_lap_so_tu_nhien_tap_x():
    """Đúng/Sai: Cho tập X = {1; 2; ...; 9}. Lập số tự nhiên chẵn, lẻ, không có 2 số chẵn liên tiếp."""
    ans_a = math.perm(9, 4) # 3024
    ans_b = math.perm(9, 5) # 15120
    # c: số lẻ 4 chữ số khác nhau: 5 * A_8^3 = 5 * 336 = 1680
    ans_c = 5 * math.perm(8, 3) # 1680
    # d: 4 chữ số khác nhau không có 2 số liên tiếp nào cùng chẵn: 2520
    ans_d = 2520
    
    a_ok = random.choice([True, False])
    b_ok = random.choice([True, False])
    c_ok = random.choice([True, False])
    d_ok = random.choice([True, False])
    
    sh_a = ans_a if a_ok else 9**4
    sh_b = ans_b if b_ok else 12000
    sh_c = ans_c if c_ok else 1440
    sh_d = ans_d if d_ok else 2160
    
    caudan = r"Cho tập hợp $X = \{1; 2; 3; 4; 5; 6; 7; 8; 9\}$. Xét tính đúng sai của các khẳng định sau:"
    choices = _make_tf_choices([
        (a_ok, f"Có ${sh_a}$ số tự nhiên có $4$ chữ số đôi một khác nhau lấy từ tập $X$."),
        (b_ok, f"Có ${sh_b}$ số tự nhiên có $5$ chữ số đôi một khác nhau lấy từ tập $X$."),
        (c_ok, f"Có ${sh_c}$ số tự nhiên lẻ có $4$ chữ số đôi một khác nhau lấy từ tập $X$."),
        (d_ok, f"Có ${sh_d}$ số tự nhiên có $4$ chữ số đôi một khác nhau lấy từ tập $X$ sao cho không có hai chữ số liên tiếp nào cùng chẵn.")
    ])
    loigiai = (
        f"\\begin{{itemchoice}}\n"
        f"\\itemch {'Đúng' if a_ok else 'Sai'}. Số các số có $4$ chữ số khác nhau là $A_9^4 = {ans_a}$.\n"
        f"\\itemch {'Đúng' if b_ok else 'Sai'}. Số các số có $5$ chữ số khác nhau là $A_9^5 = {ans_b}$.\n"
        f"\\itemch {'Đúng' if c_ok else 'Sai'}. Chữ số tận cùng lẻ có $5$ cách chọn, $3$ chữ số còn lại có $A_8^3 = 336$ cách. Vậy có $5 \\times 336 = {ans_c}$ số.\n"
        f"\\itemch {'Đúng' if d_ok else 'Sai'}. Tập $X$ có $5$ số lẻ và $4$ số chẵn. Số cách lập số không có $2$ chữ số chẵn đứng cạnh nhau là ${ans_d}$ số.\n"
        f"\\end{{itemchoice}}"
    )
    return caudan, choices, loigiai

def k10_tf_c8_an_binh_xep_hang_9_ghe():
    """Đúng/Sai: An và Bình cùng 7 bạn khác (tổng 9 bạn) xếp vào 9 ghế hàng ngang."""
    ans_a = math.factorial(9) # 362880
    ans_b = 2 * math.factorial(8) # 80640
    ans_c = ans_a - ans_b # 282240
    ans_d = 2 * math.factorial(7) # 10080
    
    a_ok = random.choice([True, False])
    b_ok = random.choice([True, False])
    c_ok = random.choice([True, False])
    d_ok = random.choice([True, False])
    
    sh_a = ans_a if a_ok else 40320
    sh_b = ans_b if b_ok else 40320
    sh_c = ans_c if c_ok else 240000
    sh_d = ans_d if d_ok else 5040
    
    caudan = "An và Bình cùng $7$ bạn khác rủ nhau đi xem bóng đá. Cả $9$ bạn được xếp vào $9$ ghế theo hàng ngang. Xét tính đúng sai của các khẳng định sau:"
    choices = _make_tf_choices([
        (a_ok, f"Có ${sh_a}$ cách xếp chỗ ngồi tùy ý."),
        (b_ok, f"Có ${sh_b}$ cách xếp An và Bình ngồi cạnh nhau."),
        (c_ok, f"Có ${sh_c}$ cách xếp An và Bình không ngồi cạnh nhau."),
        (d_ok, f"Có ${sh_d}$ cách xếp để An và Bình ngồi ở hai đầu dãy ghế.")
    ])
    loigiai = (
        f"\\begin{{itemchoice}}\n"
        f"\\itemch {'Đúng' if a_ok else 'Sai'}. Xếp tùy ý $9$ bạn có $9! = {ans_a}$ cách.\n"
        f"\\itemch {'Đúng' if b_ok else 'Sai'}. Coi An và Bình là $1$ khối: có $2! \\times 8! = {ans_b}$ cách.\n"
        f"\\itemch {'Đúng' if c_ok else 'Sai'}. Số cách An và Bình không cạnh nhau: ${ans_a} - {ans_b} = {ans_c}$ cách.\n"
        f"\\itemch {'Đúng' if d_ok else 'Sai'}. An và Bình ở $2$ đầu ghế có $2! = 2$ cách, $7$ bạn còn lại có $7! = 5040$ cách. Vậy có $2 \\times 5040 = {ans_d}$ cách.\n"
        f"\\end{{itemchoice}}"
    )
    return caudan, choices, loigiai

# =========================================================================
# CHƯƠNG VIII: ĐẠI SỐ TỔ HỢP - TRẮC NGHIỆM TRẢ LỜI NGẮN (TLN / SA)
# =========================================================================

def k10_sa_c8_he_so_tong_hai_nhi_thuc():
    """TLN: Tìm hệ số của x^3 trong khai triển x(ax + 1)^4 + (x + b)^5."""
    a = random.choice([2, 3])
    b = random.choice([2, 3])
    # x * (ax + 1)^4: x * C_4^2 (ax)^2 = 6 * a^2 * x^3
    c1 = 6 * (a ** 2)
    # (x + b)^5: C_5^3 x^3 b^2 = 10 * b^2 * x^3
    c2 = 10 * (b ** 2)
    ans = c1 + c2
    caudan = f"Tìm hệ số của số hạng chứa $x^3$ trong khai triển của đa thức $P(x) = x({a}x + 1)^4 + (x + {b})^5$."
    loigiai = (
        f"- Khai triển $x({a}x + 1)^4$: Số hạng chứa $x^3$ là $x \\cdot C_4^2 ({a}x)^2 = {c1}x^3$.\n"
        f"- Khai triển $(x + {b})^5$: Số hạng chứa $x^3$ là $C_5^3 x^3 ({b})^2 = {c2}x^3$.\n"
        f"Vậy hệ số của $x^3$ trong khai triển là: ${c1} + {c2} = {ans}$."
    )
    return caudan, str(ans), loigiai

def k10_sa_c8_lap_so_3_chu_so_khac_nhau_tu_tap_co_0():
    """TLN: Lập số tự nhiên có 3 chữ số khác nhau từ {0; 1; 2; ...; n}."""
    max_d = random.choice([5, 6, 7])
    # tập từ 0 đến max_d có max_d + 1 chữ số
    # a in {1..max_d} (max_d cách), b != a (max_d cách), c != a, b (max_d - 1 cách)
    ans = max_d * max_d * (max_d - 1)
    d_list = "; ".join(str(i) for i in range(max_d + 1))
    caudan = f"Từ các chữ số ${{{d_list}}}$ có thể lập được bao nhiêu số tự nhiên có $3$ chữ số đôi một khác nhau?"
    loigiai = (
        f"Gọi số cần tìm là $\\overline{{abc}}$ ($a \\ne 0$; $a, b, c$ đôi một khác nhau).\n"
        f"- Chọn $a \\in \\{{1; \\dots; {max_d}\\}}$: có ${max_d}$ cách chọn.\n"
        f"- Chọn $b$ khác $a$: có ${max_d}$ cách chọn.\n"
        f"- Chọn $c$ khác $a, b$: có ${max_d - 1}$ cách chọn.\n"
        f"Theo quy tắc nhân, có ${max_d} \\times {max_d} \\times {max_d - 1} = {ans}$ số."
    )
    return caudan, str(ans), loigiai

def k10_sa_c8_tam_giac_tu_hai_duong_song_song():
    """TLN: Đếm số tam giác tạo thành từ 2 đường thẳng song song có m và n điểm."""
    m = random.randint(12, 18)
    n = random.randint(15, 22)
    ans = m * math.comb(n, 2) + math.comb(m, 2) * n
    caudan = (
        f"Cho hai đường thẳng song song $d_1$ và $d_2$. Trên $d_1$ lấy ${m}$ điểm phân biệt, "
        f"trên $d_2$ lấy ${n}$ điểm phân biệt. Tính số tam giác có các đỉnh là $3$ điểm trong số ${m+n}$ điểm đã chọn trên $d_1$ và $d_2$."
    )
    loigiai = (
        f"Để tạo thành một tam giác, ta có $2$ trường hợp:\n"
        f"- Trường hợp 1: Chọn $1$ điểm trên $d_1$ và $2$ điểm trên $d_2$: có $C_{{{m}}}^1 C_{{{n}}}^2 = {m} \\times {math.comb(n, 2)} = {m * math.comb(n, 2)}$ tam giác.\n"
        f"- Trường hợp 2: Chọn $2$ điểm trên $d_1$ và $1$ điểm trên $d_2$: có $C_{{{m}}}^2 C_{{{n}}}^1 = {math.comb(m, 2)} \\times {n} = {math.comb(m, 2) * n}$ tam giác.\n"
        f"Tổng số tam giác tạo thành là: ${m * math.comb(n, 2)} + {math.comb(m, 2) * n} = {ans}$."
    )
    return caudan, str(ans), loigiai

def k10_sa_c8_so_hang_khong_chua_x_phan_thuc():
    """TLN: Tìm hệ số của số hạng không chứa x trong khai triển (x/a + b/x)^4."""
    a = random.choice([2, 3])
    b = random.choice([3, 4, 6])
    # T_k = C_4^k (x/a)^(4-k) (b/x)^k = C_4^k * b^k / a^(4-k) * x^(4-2k)
    # k = 2 -> C_4^2 * b^2 / a^2 = 6 * (b/a)^2
    # Chọn sao cho b/a chia hết
    if b % a != 0:
        b = a * random.choice([2, 3])
    ans = 6 * ((b // a) ** 2)
    caudan = f"Tìm hệ số của số hạng không chứa $x$ trong khai triển biểu thức $\\left(\\frac{{x}}{{{a}}} + \\frac{{{b}}}{{x}}\\right)^4$ với $x \\ne 0$."
    loigiai = (
        f"Số hạng tổng quát trong khai triển là:\n"
        f"$$T_{{k+1}} = C_4^k \\left(\\frac{{x}}{{{a}}}\\right)^{{4-k}} \\left(\\frac{{{b}}}{{x}}\\right)^k = C_4^k \\frac{{{b}^k}}{{{a}^{{4-k}}}} x^{{4-2k}}$$\n"
        f"Số hạng không chứa $x$ ứng với $4 - 2k = 0 \\iff k = 2$.\n"
        f"Hệ số cần tìm là: $C_4^2 \\frac{{{b}^2}}{{{a}^2}} = 6 \\times \\left(\\frac{{{b}}}{{{a}}}\\right)^2 = {ans}$."
    )
    return caudan, str(ans), loigiai

def k10_sa_c8_tong_he_so_nhi_thuc_p_x():
    """TLN: Khai triển (1 - x/2)^5 = a_0 + ... + a_5 x^5. Tính S = a_0 + 2a_1 + ... + 2^5 a_5."""
    ans = 0
    caudan = (
        r"Khai triển $\left(1 - \frac{1}{2}x\right)^5 = a_0 + a_1 x + a_2 x^2 + a_3 x^3 + a_4 x^4 + a_5 x^5$. "
        r"Tính tổng $S = a_0 + 2a_1 + 2^2 a_2 + 2^3 a_3 + 2^4 a_4 + 2^5 a_5$."
    )
    loigiai = (
        r"Xét hàm số $P(x) = \left(1 - \frac{1}{2}x\right)^5 = a_0 + a_1 x + a_2 x^2 + a_3 x^3 + a_4 x^4 + a_5 x^5$." "\n"
        r"Thay $x = 2$ vào hai vế, ta được:" "\n"
        r"$$S = a_0 + a_1 (2) + a_2 (2)^2 + a_3 (2)^3 + a_4 (2)^4 + a_5 (2)^5 = P(2)$$" "\n"
        r"Mà $P(2) = \left(1 - \frac{1}{2} \cdot 2\right)^5 = (1 - 1)^5 = 0$." "\n"
        r"Vậy $S = 0$."
    )
    return caudan, str(ans), loigiai

# =========================================================================
# CHƯƠNG IX: MỘT SỐ YẾU TỐ XÁC SUẤT - ĐÚNG / SAI (TF) & TRẢ LỜI NGẮN (TLN)
# =========================================================================

def k10_tf_c9_xac_suat_chon_hoc_sinh_nam_nu():
    """Đúng/Sai: Lớp có a nữ và b nam. Chọn 5 bạn tham gia văn nghệ."""
    nu = random.randint(6, 8)
    nam = random.randint(12, 14)
    tot = nu + nam
    n_omega = math.comb(tot, 5)
    
    # a: 5 nữ -> C_nu^5 / C_tot^5
    ans_a_frac = _fmt_frac(math.comb(nu, 5), n_omega)
    # b: đúng 3 nam -> C_nam^3 * C_nu^2 / C_tot^5
    ans_b_text = f"\\frac{{C_{{{nam}}}^3 C_{{{nu}}}^2}}{{C_{{{tot}}}^5}}"
    # c: ít nhất 1 nữ -> 1 - C_nam^5 / C_tot^5
    ans_c_frac = _fmt_frac(n_omega - math.comb(nam, 5), n_omega)
    # d: số nữ nhiều hơn số nam: (3 nữ 2 nam, 4 nữ 1 nam, 5 nữ)
    fav_d = math.comb(nu, 3) * math.comb(nam, 2) + math.comb(nu, 4) * math.comb(nam, 1) + math.comb(nu, 5)
    ans_d_frac = _fmt_frac(fav_d, n_omega)
    
    a_ok = random.choice([True, False])
    b_ok = random.choice([True, False])
    c_ok = random.choice([True, False])
    d_ok = random.choice([True, False])
    
    sh_a = ans_a_frac if a_ok else _fmt_frac(math.comb(nu, 5) + 5, n_omega)
    sh_b = ans_b_text if b_ok else f"\\frac{{C_{{{nam}}}^2 C_{{{nu}}}^3}}{{C_{{{tot}}}^5}}"
    sh_c = ans_c_frac if c_ok else _fmt_frac(n_omega - math.comb(nam, 5) - 50, n_omega)
    sh_d = ans_d_frac if d_ok else _fmt_frac(fav_d + 100, n_omega)
    
    caudan = f"Lớp 10A có ${nu}$ học sinh nữ và ${nam}$ học sinh nam. Cô chủ nhiệm chọn ra $5$ bạn để tham gia văn nghệ. Xét tính đúng sai của các mệnh đề sau:"
    choices = _make_tf_choices([
        (a_ok, f"Xác suất để chọn được $5$ học sinh nữ là ${sh_a}$."),
        (b_ok, f"Xác suất để chọn được đúng $3$ học sinh nam là ${sh_b}$."),
        (c_ok, f"Xác suất để chọn được ít nhất $1$ học sinh nữ là ${sh_c}$."),
        (d_ok, f"Xác suất để chọn được số học sinh nữ nhiều hơn số học sinh nam là ${sh_d}$.")
    ])
    loigiai = (
        f"Không gian mẫu: $n(\\Omega) = C_{{{tot}}}^5 = {n_omega}$.\n"
        f"\\begin{{itemchoice}}\n"
        f"\\itemch {'Đúng' if a_ok else 'Sai'}. Xác suất $5$ nữ: $P = \\frac{{C_{{{nu}}}^5}}{{C_{{{tot}}}^5}} = {ans_a_frac}$.\n"
        f"\\itemch {'Đúng' if b_ok else 'Sai'}. Chọn đúng $3$ nam ($3$ nam, $2$ nữ): $P = {ans_b_text}$.\n"
        f"\\itemch {'Đúng' if c_ok else 'Sai'}. Biến cố đối 'không có nữ nào' (chọn $5$ nam): $P = 1 - \\frac{{C_{{{nam}}}^5}}{{C_{{{tot}}}^5}} = {ans_c_frac}$.\n"
        f"\\itemch {'Đúng' if d_ok else 'Sai'}. Số nữ > nam gồm các trường hợp ($3$ nữ $2$ nam; $4$ nữ $1$ nam; $5$ nữ): $P = {ans_d_frac}$.\n"
        f"\\end{{itemchoice}}"
    )
    return caudan, choices, loigiai

def k10_tf_c9_xac_suat_so_tu_nhien_3_chu_so():
    """Đúng/Sai: S là tập hợp các số tự nhiên có 3 chữ số (100 đến 999). Chọn ngẫu nhiên 1 số."""
    # n(Omega) = 900
    # A: 3 chữ số khác nhau: 9 * 9 * 8 = 648
    # B: chia hết cho 5: (995 - 100)/5 + 1 = 180
    # C: số chẵn: 450
    a_ok = random.choice([True, False])
    b_ok = random.choice([True, False])
    c_ok = random.choice([True, False])
    d_ok = random.choice([True, False])
    
    sh_a = "900" if a_ok else "1000"
    sh_b = "648" if b_ok else "720"
    sh_c = "180" if c_ok else "200"
    sh_d = "450" if d_ok else "500"
    
    caudan = "Gọi $S$ là tập hợp các số tự nhiên có $3$ chữ số. Chọn ngẫu nhiên một số từ tập $S$. Xét tính đúng sai của các mệnh đề sau:"
    choices = _make_tf_choices([
        (a_ok, f"$n(\\Omega) = {sh_a}$."),
        (b_ok, f"Gọi $A$ là biến cố 'Chọn được số tự nhiên có các chữ số đôi một khác nhau', khi đó $n(A) = {sh_b}$."),
        (c_ok, f"Gọi $B$ là biến cố 'Chọn được số tự nhiên chia hết cho $5$', khi đó $n(B) = {sh_c}$."),
        (d_ok, f"Gọi $C$ là biến cố 'Chọn được số tự nhiên chẵn', khi đó $n(C) = {sh_d}$.")
    ])
    loigiai = (
        f"\\begin{{itemchoice}}\n"
        f"\\itemch {'Đúng' if a_ok else 'Sai'}. Tập các số có $3$ chữ số từ $100$ đến $999$ có: $999 - 100 + 1 = 900$ số $\\implies n(\\Omega) = 900$.\n"
        f"\\itemch {'Đúng' if b_ok else 'Sai'}. Số có $3$ chữ số khác nhau $\\overline{{abc}}$: $a \\in \\{{1..9\\}}$ ($9$ cách), $b \\ne a$ ($9$ cách), $c \\ne a, b$ ($8$ cách). Vậy $n(A) = 9 \\times 9 \\times 8 = 648$.\n"
        f"\\itemch {'Đúng' if c_ok else 'Sai'}. Số chia hết cho $5$: tận cùng là $0$ hoặc $5$, có $\\frac{{995 - 100}}{{5}} + 1 = 180$ số $\\implies n(B) = 180$.\n"
        f"\\itemch {'Đúng' if d_ok else 'Sai'}. Số chẵn gồm một nửa tập hợp $S$: $\\frac{{900}}{{2}} = 450$ số $\\implies n(C) = 450$.\n"
        f"\\end{{itemchoice}}"
    )
    return caudan, choices, loigiai

def k10_sa_c9_xac_suat_rut_the_tong_le():
    """TLN: Hộp đựng 11 tấm thẻ từ 1 đến 11. Chọn ngẫu nhiên 6 tấm thẻ. Tính xác suất tổng là số lẻ (làm tròn hoặc phân số)."""
    # 1..11 có 6 số lẻ (1,3,5,7,9,11) và 5 số chẵn (2,4,6,8,10).
    # Chọn 6 thẻ: tổng lẻ <=> số thẻ lẻ được chọn là 1, 3, 5.
    # C_11^6 = 462
    # k_le = 1: C_6^1 * C_5^5 = 6 * 1 = 6
    # k_le = 3: C_6^3 * C_5^3 = 20 * 10 = 200
    # k_le = 5: C_6^5 * C_5^1 = 6 * 5 = 30
    # fav = 6 + 200 + 30 = 236.
    # P = 236 / 462 = 118 / 231.
    ans_str = "118/231"
    caudan = (
        "Một hộp đựng $11$ tấm thẻ được đánh số từ $1$ đến $11$. Chọn ngẫu nhiên $6$ tấm thẻ. "
        "Tính xác suất để tổng số ghi trên $6$ tấm thẻ ấy là một số lẻ (viết kết quả dưới dạng phân số tối giản a/b)."
    )
    loigiai = (
        "Trong $11$ tấm thẻ có $6$ thẻ mang số lẻ và $5$ thẻ mang số chẵn.\n"
        "Số phần tử của không gian mẫu: $n(\\Omega) = C_{11}^6 = 462$.\n"
        "Tổng $6$ số là một số lẻ khi và chỉ khi số lượng thẻ lẻ được chọn là một số lẻ ($1$, $3$, hoặc $5$ thẻ lẻ):\n"
        "- Chọn $1$ thẻ lẻ và $5$ thẻ chẵn: $C_6^1 C_5^5 = 6 \\times 1 = 6$ cách.\n"
        "- Chọn $3$ thẻ lẻ và $3$ thẻ chẵn: $C_6^3 C_5^3 = 20 \\times 10 = 200$ cách.\n"
        "- Chọn $5$ thẻ lẻ và $1$ thẻ chẵn: $C_6^5 C_5^1 = 6 \\times 5 = 30$ cách.\n"
        "Số kết quả thuận lợi là: $n(A) = 6 + 200 + 30 = 236$.\n"
        f"Xác suất cần tìm là: $P(A) = \\frac{{236}}{{462}} = \\frac{{118}}{{231}}$."
    )
    return caudan, ans_str, loigiai


# =========================================================================
# BỔ SUNG CÁC DẠNG ĐÚNG SAI & TRẢ LỜI NGẮN MỚI TỪ BỘ ẢNH ĐỢT 3
# =========================================================================

def k10_tf_c9_xac_suat_rut_the_100():
    """Đúng/Sai: Có 100 tấm thẻ từ 1 đến 100. Lấy ngẫu nhiên 5 thẻ."""
    # n(Omega) = C_100^5 = 75.287.520
    # A (đều chẵn): C_50^5 = 2.118.760
    # B (đều lẻ): C_50^5 = 2.118.760
    # C (ít nhất 1 số chia hết cho 3): trong 100 số có 33 số chia hết cho 3, 67 số không chia hết cho 3.
    # n(C) = C_100^5 - C_67^5 = 75287520 - 9657648 = 65.629.872.
    ans_omega = 75287520
    ans_a = 2118760
    ans_b = 2118760
    ans_c = 65629872

    a_ok = random.choice([True, False])
    b_ok = random.choice([True, False])
    c_ok = random.choice([True, False])
    d_ok = random.choice([True, False])

    sh_omega = ans_omega if a_ok else 75200000
    sh_a = ans_a if b_ok else 2128760
    sh_b = ans_b if c_ok else 2128760
    sh_c = ans_c if d_ok else 65000000

    caudan = (
        "Có $100$ tấm thẻ được đánh số từ $1$ đến $100$. Lấy ngẫu nhiên $5$ thẻ. "
        "Xét tính đúng sai của các khẳng định sau:"
    )
    choices = _make_tf_choices([
        (a_ok, f"$n(\\Omega) = {sh_omega}$."),
        (b_ok, f"Gọi $A$ là biến cố 'Số ghi trên các tấm thẻ được chọn đều là số chẵn'. Khi đó $n(A) = {sh_a}$."),
        (c_ok, f"Gọi $B$ là biến cố 'Số ghi trên các tấm thẻ được chọn đều là số lẻ'. Khi đó $n(B) = {sh_b}$."),
        (d_ok, f"Gọi $C$ là biến cố 'Có ít nhất một số ghi trên thẻ được chọn chia hết cho $3$'. Khi đó $n(C) = {sh_c}$.")
    ])
    loigiai = (
        f"\\begin{{itemchoice}}\n"
        f"\\itemch {'Đúng' if a_ok else 'Sai'}. Số phần tử không gian mẫu là $n(\\Omega) = C_{{100}}^5 = {ans_omega}$.\n"
        f"\\itemch {'Đúng' if b_ok else 'Sai'}. Có $50$ thẻ mang số chẵn nên $n(A) = C_{{50}}^5 = {ans_a}$.\n"
        f"\\itemch {'Đúng' if c_ok else 'Sai'}. Có $50$ thẻ mang số lẻ nên $n(B) = C_{{50}}^5 = {ans_b}$.\n"
        f"\\itemch {'Đúng' if d_ok else 'Sai'}. Có $33$ số chia hết cho $3$ và $67$ số không chia hết cho $3$. "
        f"Số cách chọn $5$ thẻ không có số nào chia hết cho $3$ là $C_{{67}}^5 = 9657648$. "
        f"Do đó $n(C) = C_{{100}}^5 - C_{{67}}^5 = {ans_c}$.\n"
        f"\\end{{itemchoice}}"
    )
    return caudan, choices, loigiai

def k10_tf_c9_xac_suat_binh_16_bi_3_mau():
    """Đúng/Sai: Bình đựng 16 viên bi (7 trắng, 6 đen, 3 đỏ). Lấy ngẫu nhiên 4 viên bi."""
    # n(Omega) = C_16^4 = 1820
    # b: 4 trắng: C_7^4 / 1820 = 35 / 1820 = 1 / 52
    # c: đủ 3 màu: (2T 1D 1DO: 21*6*3=378) + (1T 2D 1DO: 7*15*3=315) + (1T 1D 2DO: 7*6*3=126) = 819.
    #    P = 819 / 1820 = 9 / 20.
    # d: đúng 2 màu: P = 1 - P(1 màu) - P(3 màu) = 1 - 50/1820 - 819/1820 = 951/1820.
    a_ok = random.choice([True, False])
    b_ok = random.choice([True, False])
    c_ok = random.choice([True, False])
    d_ok = random.choice([True, False])

    sh_a = "C_{16}^4" if a_ok else "A_{16}^4"
    sh_b = "\\frac{1}{52}" if b_ok else "\\frac{1}{26}"
    sh_c = "\\frac{9}{20}" if c_ok else "\\frac{7}{20}"
    sh_d = "\\frac{951}{1820}" if d_ok else "\\frac{11}{20}"

    caudan = (
        "Một bình đựng $16$ viên bi, trong đó có $7$ viên bi trắng, $6$ viên bi đen và $3$ viên bi đỏ. "
        "Lấy ngẫu nhiên $4$ viên bi. Xét tính đúng sai của các khẳng định sau:"
    )
    choices = _make_tf_choices([
        (a_ok, f"Số phần tử của không gian mẫu là ${sh_a}$."),
        (b_ok, f"Xác suất lấy được đúng $4$ viên bi trắng là ${sh_b}$."),
        (c_ok, f"Xác suất lấy được đủ cả $3$ màu là ${sh_c}$."),
        (d_ok, f"Xác suất lấy được đúng $2$ màu là ${sh_d}$.")
    ])
    loigiai = (
        f"\\begin{{itemchoice}}\n"
        f"\\itemch {'Đúng' if a_ok else 'Sai'}. Lấy đồng thời $4$ viên bi từ $16$ viên là tổ hợp: $n(\\Omega) = C_{{16}}^4 = 1820$.\n"
        f"\\itemch {'Đúng' if b_ok else 'Sai'}. Số cách lấy $4$ bi trắng là $C_7^4 = 35 \\implies P = \\frac{{35}}{{1820}} = \\frac{{1}}{{52}}$.\n"
        f"\\itemch {'Đúng' if c_ok else 'Sai'}. Số cách lấy đủ $3$ màu là $C_7^2 C_6^1 C_3^1 + C_7^1 C_6^2 C_3^1 + C_7^1 C_6^1 C_3^2 = 378 + 315 + 126 = 819 "
        f"\\implies P = \\frac{{819}}{{1820}} = \\frac{{9}}{{20}}$.\n"
        f"\\itemch {'Đúng' if d_ok else 'Sai'}. Số cách lấy $4$ bi cùng màu là $C_7^4 + C_6^4 = 35 + 15 = 50$. "
        f"Vậy xác suất lấy đúng $2$ màu là $1 - \\frac{{50}}{{1820}} - \\frac{{9}}{{20}} = \\frac{{951}}{{1820}}$.\n"
        f"\\end{{itemchoice}}"
    )
    return caudan, choices, loigiai

def k10_sa_c9_xac_suat_bi_do_hon_vang_co_xanh():
    """TLN: Hộp có 5 đỏ, 3 vàng, 4 xanh. Chọn 4 bi. Số bi đỏ > bi vàng VÀ nhất thiết có bi xanh. P = a/b. Tính T = a + 2b."""
    # Đỏ: 5, Vàng: 3, Xanh: 4. Tổng: 12. Chọn 4 bi -> C_12^4 = 495.
    # Số bi đỏ > số bi vàng và có bi xanh (số xanh >= 1):
    # Các bộ (Đỏ, Vàng, Xanh) có tổng = 4, Xanh >= 1, Đỏ > Vàng:
    # Vàng = 0:
    #   Đỏ = 1, Xanh = 3: C_5^1 * C_3^0 * C_4^3 = 5 * 1 * 4 = 20
    #   Đỏ = 2, Xanh = 2: C_5^2 * C_3^0 * C_4^2 = 10 * 1 * 6 = 60
    #   Đỏ = 3, Xanh = 1: C_5^3 * C_3^0 * C_4^1 = 10 * 1 * 4 = 40
    # Vàng = 1:
    #   Đỏ = 2, Xanh = 1: C_5^2 * C_3^1 * C_4^1 = 10 * 3 * 4 = 120
    # Tổng thuận lợi = 20 + 60 + 40 + 120 = 240.
    # P = 240 / 495 = 16 / 33 -> a = 16, b = 33 -> T = a + 2b = 16 + 66 = 82.
    ans_t = 16 + 2 * 33 # 82
    caudan = (
        "Một hộp có $5$ viên bi đỏ, $3$ viên bi vàng và $4$ viên bi xanh. Chọn ngẫu nhiên từ hộp $4$ viên bi. "
        "Xác suất để $4$ viên bi được chọn có số bi đỏ lớn hơn số bi vàng và nhất thiết phải có mặt bi xanh bằng $\\frac{a}{b}$ "
        "với $\\frac{a}{b}$ là phân số tối giản và $a, b \\in \\mathbb{Z}$. Tính $T = a + 2b$."
    )
    loigiai = (
        "Không gian mẫu: $n(\\Omega) = C_{12}^4 = 495$.\n"
        "Gọi số bi đỏ, vàng, xanh được chọn lần lượt là $d, v, x$ ($d + v + x = 4$; $x \\ge 1$; $d > v$):\n"
        "- Với $v = 0$:\n"
        "  + $d = 1, x = 3$: có $C_5^1 C_3^0 C_4^3 = 20$ cách.\n"
        "  + $d = 2, x = 2$: có $C_5^2 C_3^0 C_4^2 = 60$ cách.\n"
        "  + $d = 3, x = 1$: có $C_5^3 C_3^0 C_4^1 = 40$ cách.\n"
        "- Với $v = 1$:\n"
        "  + $d = 2, x = 1$: có $C_5^2 C_3^1 C_4^1 = 120$ cách.\n"
        "Tổng số kết quả thuận lợi: $20 + 60 + 40 + 120 = 240$.\n"
        "Xác suất: $P = \\frac{240}{495} = \\frac{16}{33} \\implies a = 16, b = 33$.\n"
        f"Vậy $T = a + 2b = 16 + 2(33) = {ans_t}$."
    )
    return caudan, str(ans_t), loigiai

def k10_sa_c9_xac_suat_chon_hoc_sinh_2_khoi_nam_nu():
    """TLN: 13 HS xuất sắc: K12 có 8 nam 3 nữ, K11 có 2 nam. Chọn 3 HS có cả nam và nữ đồng thời cả 2 khối. Tính T = 3a + 2b."""
    # K12: 8 nam, 3 nữ. K11: 2 nam (0 nữ). Tổng 13 HS.
    # Chọn 3 HS -> C_13^3 = 286.
    # Cần: có cả nam và nữ (số nữ >= 1), đồng thời có cả K11 và K12 (số K11 >= 1).
    # Vì K11 chỉ có nam nên bắt buộc phải chọn ít nhất 1 bạn nữ từ K12!
    # K11 có thể chọn 1 hoặc 2 nam:
    # - Chọn 1 nam K11 ($C_2^1 = 2$ cách):
    #   Cần chọn 2 em từ K12 sao cho có ít nhất 1 nữ:
    #   + 1 nữ K12, 1 nam K12: C_3^1 * C_8^1 = 24
    #   + 2 nữ K12, 0 nam K12: C_3^2 * C_8^0 = 3
    #   -> 2 * (24 + 3) = 2 * 27 = 54 cách.
    # - Chọn 2 nam K11 ($C_2^2 = 1$ cách):
    #   Cần chọn 1 em từ K12 mà bắt buộc phải là nữ để có nữ:
    #   + 1 nữ K12: C_3^1 = 3 cách.
    #   -> 1 * 3 = 3 cách.
    # Tổng thuận lợi = 54 + 3 = 57.
    # P = 57 / 286 (tối giản vì 57 = 3*19, 286 = 2*11*13).
    # a = 57, b = 286 -> T = 3a + 2b = 3*57 + 2*286 = 171 + 572 = 743.
    ans_t = 3 * 57 + 2 * 286 # 743
    caudan = (
        "Có $13$ học sinh của một trường THPT đạt danh hiệu học sinh xuất sắc, trong đó khối 12 có $8$ học sinh nam và $3$ học sinh nữ, "
        "khối 11 có $2$ học sinh nam. Chọn ngẫu nhiên $3$ học sinh bất kỳ để trao thưởng. "
        "Xác suất để $3$ học sinh được chọn có cả nam và nữ đồng thời có cả khối 11 và khối 12 bằng $\\frac{a}{b}$ "
        "với $\\frac{a}{b}$ là phân số tối giản và $a, b \\in \\mathbb{Z}$. Tính $T = 3a + 2b$."
    )
    loigiai = (
        "Không gian mẫu: $n(\\Omega) = C_{13}^3 = 286$.\n"
        "Vì khối 11 chỉ có học sinh nam nên để có học sinh nữ thì bắt buộc phải chọn học sinh nữ từ khối 12:\n"
        "- Trường hợp 1: Chọn $1$ học sinh nam khối 11 và $2$ học sinh khối 12 (trong đó có ít nhất $1$ nữ):\n"
        "  + $1$ nam K11, $1$ nữ K12, $1$ nam K12: $C_2^1 \\times C_3^1 \\times C_8^1 = 2 \\times 3 \\times 8 = 48$ cách.\n"
        "  + $1$ nam K11, $2$ nữ K12: $C_2^1 \\times C_3^2 = 2 \\times 3 = 6$ cách.\n"
        "  Suy ra có $48 + 6 = 54$ cách.\n"
        "- Trường hợp 2: Chọn $2$ học sinh nam khối 11 và $1$ học sinh nữ khối 12: $C_2^2 \\times C_3^1 = 1 \\times 3 = 3$ cách.\n"
        "Số kết quả thuận lợi là: $54 + 3 = 57$.\n"
        "Xác suất: $P = \\frac{57}{286} \\implies a = 57, b = 286$.\n"
        f"Vậy $T = 3a + 2b = 3(57) + 2(286) = {ans_t}$."
    )
    return caudan, str(ans_t), loigiai

def k10_sa_c9_hop_bi_danh_so_khac_mau_khac_so():
    """TLN: Hộp 1 có 6 bi xanh (1-6), Hộp 2 có 5 bi đỏ (1-5), Hộp 3 có 4 bi vàng (1-4). Lấy mỗi hộp 1 bi. Tính số phần tử vừa khác màu vừa khác số."""
    # Lấy 1 xanh x in {1..6}, 1 đỏ d in {1..5}, 1 vàng v in {1..4}.
    # Đã khác màu (vì mỗi viên từ 1 hộp). Cần x != d, d != v, x != v.
    # Chọn v in {1..4}: có 4 cách.
    # Chọn d in {1..5} \ {v}: có 5 - 1 = 4 cách.
    # Chọn x in {1..6} \ {d, v}: có 6 - 2 = 4 cách.
    # Tổng số cách: 4 * 4 * 4 = 64 cách!
    ans = 4 * 4 * 4 # 64
    caudan = (
        "Có ba chiếc hộp: hộp thứ nhất chứa $6$ viên bi xanh được đánh số từ $1$ đến $6$, "
        "hộp thứ hai chứa $5$ viên bi đỏ được đánh số từ $1$ đến $5$, "
        "hộp thứ ba chứa $4$ viên bi vàng được đánh số từ $1$ đến $4$. "
        "Lấy ngẫu nhiên từ mỗi hộp một viên bi. Tính số phần tử của biến cố $A$: 'Ba viên bi được chọn vừa khác màu vừa khác số'."
    )
    loigiai = (
        "Vì mỗi viên bi được lấy từ một hộp khác nhau nên ba viên bi đã chắc chắn khác màu.\n"
        "Để ba viên bi có số ghi đôi một khác nhau, ta thực hiện liên tiếp các công đoạn:\n"
        "- Chọn $1$ viên bi vàng từ hộp thứ ba: có $4$ cách chọn số (từ $1$ đến $4$).\n"
        "- Chọn $1$ viên bi đỏ từ hộp thứ hai có số khác số của viên bi vàng vừa chọn: có $5 - 1 = 4$ cách chọn.\n"
        "- Chọn $1$ viên bi xanh từ hộp thứ nhất có số khác cả hai số đã chọn ở hai viên bi trên: có $6 - 2 = 4$ cách chọn.\n"
        f"Theo quy tắc nhân, số kết quả thuận lợi của biến cố $A$ là:\n"
        f"$$n(A) = 4 \\times 4 \\times 4 = {ans}$$\n"
        f"Vậy số phần tử cần tìm là ${ans}$."
    )
    return caudan, str(ans), loigiai


# =========================================================================
# CÁC DẠNG BỔ SUNG ĐỢT 4 (Ảnh Xác suất mới)
# =========================================================================

def k10_tf_c9_xac_suat_lop_40_hs():
    """Đúng/Sai: Lớp 10A có 40 học sinh (25 nữ, 15 nam). Chọn 4 học sinh đi lao động."""
    # n(Omega) = C_40^4 = 91390
    # a: 3 nam, 1 nữ: C_15^3 * C_25^1 / 91390 = 455 * 25 / 91390 = 11375 / 91390 = 175 / 1406
    # b: có cả nam và nữ: 1 - (C_15^4 + C_25^4)/91390 = 1 - (1365 + 12650)/91390 = 77375 / 91390 = 3150 / 9139?
    #    77375 / 91390 = 15475 / 18278 (hoặc đề ghi 3150/9139)
    # c: 1 nam, 3 nữ: C_15^1 * C_25^3 / 91390 = 15 * 2300 / 91390 = 34500 / 91390 = 1725 / 4569.
    # d: 4 nam: C_15^4 / 91390 = 1365 / 91390 = 39 / 2611.
    a_ok = random.choice([True, False])
    b_ok = random.choice([True, False])
    c_ok = random.choice([True, False])
    d_ok = random.choice([True, False])

    sh_a = "\\frac{175}{1406}" if a_ok else "\\frac{155}{1406}"
    sh_b = "\\frac{77375}{91390}" if b_ok else "\\frac{3150}{9139}"
    sh_c = "\\frac{1725}{4569}" if c_ok else "\\frac{1753}{1406}"
    sh_d = "\\frac{1365}{91390}" if d_ok else "\\frac{1265}{9139}"

    caudan = (
        "Lớp 10A có $40$ học sinh gồm $25$ nữ và $15$ nam. Cần chọn ra $4$ học sinh của lớp đi lao động. "
        "Xét tính đúng sai của các khẳng định sau:"
    )
    choices = _make_tf_choices([
        (a_ok, f"Xác suất để chọn được $4$ học sinh trong đó có $3$ nam và $1$ nữ là ${sh_a}$."),
        (b_ok, f"Xác suất để chọn được $4$ học sinh trong đó có cả nam và nữ là ${sh_b}$."),
        (c_ok, f"Xác suất để chọn được $4$ học sinh trong đó có $1$ nam và $3$ nữ là ${sh_c}$."),
        (d_ok, f"Xác suất để chọn được $4$ học sinh đều là nam là ${sh_d}$.")
    ])
    loigiai = (
        "Không gian mẫu: $n(\\Omega) = C_{40}^4 = 91390$.\n"
        f"\\begin{{itemchoice}}\n"
        f"\\itemch {'Đúng' if a_ok else 'Sai'}. Xác suất $3$ nam $1$ nữ: $P = \\frac{{C_{{15}}^3 C_{{25}}^1}}{{C_{{40}}^4}} = \\frac{{11375}}{{91390}} = \\frac{{175}}{{1406}}$.\n"
        f"\\itemch {'Đúng' if b_ok else 'Sai'}. Xác suất cả nam và nữ: $1 - \\frac{{C_{{15}}^4 + C_{{25}}^4}}{{C_{{40}}^4}} = \\frac{{77375}}{{91390}}$.\n"
        f"\\itemch {'Đúng' if c_ok else 'Sai'}. Xác suất $1$ nam $3$ nữ: $P = \\frac{{C_{{15}}^1 C_{{25}}^3}}{{C_{{40}}^4}} = \\frac{{34500}}{{91390}} = \\frac{{1725}}{{4569}}$.\n"
        f"\\itemch {'Đúng' if d_ok else 'Sai'}. Xác suất $4$ nam: $P = \\frac{{C_{{15}}^4}}{{C_{{40}}^4}} = \\frac{{1365}}{{91390}} = \\frac{{39}}{{2611}}$.\n"
        f"\\end{{itemchoice}}"
    )
    return caudan, choices, loigiai

def k10_tf_c9_gia_sach_toan_ly_hoa():
    """Đúng/Sai: Giá sách có 4 Toán, 3 Lý, 2 Hóa (tổng 9 quyển). Lấy ngẫu nhiên 3 quyển."""
    # n(Omega) = C_9^3 = 84
    # A (thuộc 3 môn khác nhau): 4 * 3 * 2 = 24
    # B (đều là môn toán): C_4^3 = 4
    # C (có ít nhất 1 quyển toán): C_9^3 - C_5^3 = 84 - 10 = 74
    ans_omega = 84
    ans_a = 24
    ans_b = 4
    ans_c = 74

    a_ok = random.choice([True, False])
    b_ok = random.choice([True, False])
    c_ok = random.choice([True, False])
    d_ok = random.choice([True, False])

    sh_omega = ans_omega if a_ok else 90
    sh_a = ans_a if b_ok else 20
    sh_b = ans_b if c_ok else 6
    sh_c = ans_c if d_ok else 70

    caudan = (
        "Trên giá sách có $4$ quyển sách Toán, $3$ quyển sách Lý và $2$ quyển sách Hóa. "
        "Lấy ngẫu nhiên $3$ quyển sách. Xét tính đúng sai của các khẳng định sau:"
    )
    choices = _make_tf_choices([
        (a_ok, f"$n(\\Omega) = {sh_omega}$."),
        (b_ok, f"Số phần tử của biến cố $A$ 'Thuộc $3$ môn khác nhau' bằng ${sh_a}$."),
        (c_ok, f"Số phần tử của biến cố $B$ 'Đều là môn Toán' bằng ${sh_b}$."),
        (d_ok, f"Số phần tử của biến cố $C$ 'Có ít nhất một quyển sách Toán' bằng ${sh_c}$.")
    ])
    loigiai = (
        f"\\begin{{itemchoice}}\n"
        f"\\itemch {'Đúng' if a_ok else 'Sai'}. Không gian mẫu: $n(\\Omega) = C_9^3 = {ans_omega}$.\n"
        f"\\itemch {'Đúng' if b_ok else 'Sai'}. Biến cố $A$ có $4 \\times 3 \\times 2 = {ans_a}$ cách.\n"
        f"\\itemch {'Đúng' if c_ok else 'Sai'}. Biến cố $B$ có $C_4^3 = {ans_b}$ cách.\n"
        f"\\itemch {'Đúng' if d_ok else 'Sai'}. Biến cố đối 'không có sách Toán': chọn $3$ quyển từ $5$ quyển Lý và Hóa có $C_5^3 = 10$. "
        f"Vậy $n(C) = 84 - 10 = {ans_c}$.\n"
        f"\\end{{itemchoice}}"
    )
    return caudan, choices, loigiai

def k10_tf_c9_rut_the_40_chia_het_3():
    """Đúng/Sai: Hộp 40 thẻ từ 1 đến 40. Rút 3 thẻ."""
    # n(Omega) = C_40^3 = 9880
    # 20 lẻ, 20 chẵn
    # b: 3 thẻ lẻ: C_20^3 / 9880 = 1140 / 9880 = 3 / 26
    # c: ít nhất 1 chẵn: 1 - 3/26 = 23 / 26
    # d: tổng chia hết cho 3:
    # chia 3 dư 0: {3,6,...,39} có 13 số
    # chia 3 dư 1: {1,4,...,40} có 14 số
    # chia 3 dư 2: {2,5,...,38} có 13 số
    # tổng chia hết cho 3:
    # - 3 số cùng dư 0: C_13^3 = 286
    # - 3 số cùng dư 1: C_14^3 = 364
    # - 3 số cùng dư 2: C_13^3 = 286
    # - mỗi nhóm 1 số: 13 * 14 * 13 = 2366
    # tổng thuận lợi = 286 + 364 + 286 + 2366 = 3302.
    # P = 3302 / 9880 = 127 / 380!
    ans_omega = 9880
    ans_b = "\\frac{3}{26}"
    ans_c = "\\frac{23}{26}"
    ans_d = "\\frac{127}{380}"

    a_ok = random.choice([True, False])
    b_ok = random.choice([True, False])
    c_ok = random.choice([True, False])
    d_ok = random.choice([True, False])

    sh_omega = ans_omega if a_ok else 9800
    sh_b = ans_b if b_ok else "\\frac{1}{13}"
    sh_c = ans_c if c_ok else "\\frac{5}{13}"
    sh_d = ans_d if d_ok else "\\frac{117}{380}"

    caudan = (
        "Trong một hộp có $40$ cái thẻ được đánh số từ $1$ đến $40$. Rút ngẫu nhiên đồng thời $3$ chiếc thẻ từ hộp. "
        "Xét tính đúng sai của các khẳng định sau:"
    )
    choices = _make_tf_choices([
        (a_ok, f"Số phần tử của không gian mẫu của phép thử trên là $n(\\Omega) = {sh_omega}$."),
        (b_ok, f"Xác suất để rút được $3$ chiếc thẻ đều ghi số lẻ bằng ${sh_b}$."),
        (c_ok, f"Xác suất để rút được $3$ chiếc thẻ trong đó có ít nhất một thẻ ghi số chẵn bằng ${sh_c}$."),
        (d_ok, f"Xác suất để tổng ba số trên ba thẻ rút được là số chia hết cho $3$ bằng ${sh_d}$.")
    ])
    loigiai = (
        f"\\begin{{itemchoice}}\n"
        f"\\itemch {'Đúng' if a_ok else 'Sai'}. Không gian mẫu: $n(\\Omega) = C_{{40}}^3 = {ans_omega}$.\n"
        f"\\itemch {'Đúng' if b_ok else 'Sai'}. Có $20$ thẻ lẻ, xác suất $3$ thẻ lẻ: $\\frac{{C_{{20}}^3}}{{9880}} = \\frac{{1140}}{{9880}} = {ans_b}$.\n"
        f"\\itemch {'Đúng' if c_ok else 'Sai'}. Ít nhất $1$ thẻ chẵn là biến cố đối của '$3$ thẻ lẻ': $1 - \\frac{{3}}{{26}} = {ans_c}$.\n"
        f"\\itemch {'Đúng' if d_ok else 'Sai'}. Phân loại $40$ số theo số dư khi chia cho $3$: có $13$ số dư $0$, $14$ số dư $1$, $13$ số dư $2$. "
        f"Tổng chia hết cho $3$ gồm: $C_{{13}}^3 + C_{{14}}^3 + C_{{13}}^3 + 13 \\times 14 \\times 13 = 3302$ cách. "
        f"Xác suất bằng $\\frac{{3302}}{{9880}} = {ans_d}$.\n"
        f"\\end{{itemchoice}}"
    )
    return caudan, choices, loigiai

def k10_sa_c9_rut_3_bi_khac_mau():
    """TLN: Hộp đựng 10 xanh, 20 đỏ, 15 vàng. Chọn 3 bi. Tính số kết quả thuận lợi '3 bi có màu khác nhau'."""
    ans = 10 * 20 * 15 # 3000
    caudan = (
        "Một hộp đựng $10$ viên bi xanh, $20$ viên bi đỏ và $15$ viên bi vàng. "
        "Chọn ngẫu nhiên cùng một lúc ra $3$ viên bi. Hãy xác định số các kết quả thuận lợi cho biến cố '3 viên bi được chọn có màu khác nhau'."
    )
    loigiai = (
        "Để $3$ viên bi được chọn có màu khác nhau, ta phải chọn được $1$ bi xanh, $1$ bi đỏ và $1$ bi vàng.\n"
        "- Chọn $1$ bi xanh có $10$ cách.\n"
        "- Chọn $1$ bi đỏ có $20$ cách.\n"
        "- Chọn $1$ bi vàng có $15$ cách.\n"
        f"Theo quy tắc nhân, số kết quả thuận lợi là: $10 \\times 20 \\times 15 = {ans}$."
    )
    return caudan, str(ans), loigiai

def k10_sa_c9_chon_truc_nhat_it_nhat_1_nu():
    """TLN: Nhóm có 4 nam và 6 nữ. Chọn 3 bạn trực nhật. Tính số kết quả thuận lợi 'có ít nhất 1 bạn nữ'."""
    ans = math.comb(10, 3) - math.comb(4, 3) # 120 - 4 = 116
    caudan = (
        "Một nhóm có $4$ bạn nam và $6$ bạn nữ. Chọn ngẫu nhiên cùng một lúc ra $3$ bạn đi trực nhật. "
        "Hãy xác định số các kết quả thuận lợi cho biến cố 'Trong $3$ bạn được chọn có ít nhất $1$ bạn nữ'."
    )
    loigiai = (
        "Tổng số bạn trong nhóm là $4 + 6 = 10$ bạn.\n"
        "Số cách chọn tùy ý $3$ bạn từ $10$ bạn là: $C_{10}^3 = 120$ cách.\n"
        "Số cách chọn $3$ bạn mà không có bạn nữ nào (chỉ toàn bạn nam) là: $C_4^3 = 4$ cách.\n"
        f"Số kết quả thuận lợi để có ít nhất $1$ bạn nữ là: $120 - 4 = {ans}$."
    )
    return caudan, str(ans), loigiai


# =========================================================================
# BỔ SUNG CÁC DẠNG ĐỢT 5
# =========================================================================

def k10_tf_c9_hop_10_the_rut_2():
    """Đúng/Sai: Hộp chứa 10 tấm thẻ từ 1 đến 10. Rút 2 tấm thẻ."""
    # n(Omega) = C_10^2 = 45
    # Chẵn: {2,4,6,8,10} (5 thẻ)
    # Lẻ: {1,3,5,7,9} (5 thẻ)
    # Nguyên tố: {2,3,5,7} (4 thẻ)
    # b: 2 thẻ cùng chia hết cho 2 (2 thẻ chẵn): C_5^2 / 45 = 10 / 45 = 2 / 9
    # c: 2 thẻ đều là số nguyên tố: C_4^2 / 45 = 6 / 45 = 2 / 15 (đề ghi 1/15)
    # d: tổng là 1 số lẻ (1 chẵn 1 lẻ): (5 * 5) / 45 = 25 / 45 = 5 / 9
    ans_omega = 45
    ans_b = "\\frac{2}{9}"
    ans_c = "\\frac{2}{15}"
    ans_d = "\\frac{5}{9}"

    a_ok = random.choice([True, False])
    b_ok = random.choice([True, False])
    c_ok = random.choice([True, False])
    d_ok = random.choice([True, False])

    sh_omega = ans_omega if a_ok else 90
    sh_b = ans_b if b_ok else "\\frac{1}{9}"
    sh_c = ans_c if c_ok else "\\frac{1}{15}"
    sh_d = ans_d if d_ok else "\\frac{4}{9}"

    caudan = (
        "Một hộp chứa $10$ tấm thẻ được đánh số từ $1$ đến $10$. Rút ngẫu nhiên hai tấm thẻ từ hộp đó. "
        "Xét tính đúng sai của các khẳng định sau:"
    )
    choices = _make_tf_choices([
        (a_ok, f"Số phần tử của không gian mẫu là ${sh_omega}$."),
        (b_ok, f"Xác suất để rút được hai tấm thẻ được đánh số cùng chia hết cho $2$ là ${sh_b}$."),
        (c_ok, f"Xác suất để rút được hai tấm thẻ được đánh số đều là số nguyên tố là ${sh_c}$."),
        (d_ok, f"Xác suất để rút được hai tấm thẻ có tổng là một số lẻ là ${sh_d}$.")
    ])
    loigiai = (
        f"\\begin{{itemchoice}}\n"
        f"\\itemch {'Đúng' if a_ok else 'Sai'}. Không gian mẫu: $n(\\Omega) = C_{{10}}^2 = {ans_omega}$.\n"
        f"\\itemch {'Đúng' if b_ok else 'Sai'}. Có $5$ thẻ mang số chẵn, xác suất rút được $2$ thẻ chẵn: $\\frac{{C_5^2}}{{45}} = {ans_b}$.\n"
        f"\\itemch {'Đúng' if c_ok else 'Sai'}. Có $4$ thẻ mang số nguyên tố $\\{{2; 3; 5; 7\\}}$, xác suất: $\\frac{{C_4^2}}{{45}} = \\frac{{6}}{{45}} = {ans_c}$.\n"
        f"\\itemch {'Đúng' if d_ok else 'Sai'}. Tổng là số lẻ khi rút được $1$ thẻ chẵn và $1$ thẻ lẻ: $\\frac{{5 \\times 5}}{{45}} = {ans_d}$.\n"
        f"\\end{{itemchoice}}"
    )
    return caudan, choices, loigiai

def k10_tf_c9_doan_truong_17_thanh_vien():
    """Đúng/Sai: Ban chấp hành đoàn trường gồm 17 thành viên (8 nam, 9 nữ). Chọn ngẫu nhiên 2 thành viên."""
    # n(Omega) = C_17^2 = 136
    # b: chọn 2 thành viên phân công nhiệm vụ -> A_17^2
    # c: 2 nam -> C_8^2 = 28
    # d: ít nhất 1 nam -> 1 - C_9^2 / C_17^2 = 1 - 36 / 136 = 100 / 136 = 25 / 34
    ans_a = 136
    ans_c = 28
    ans_d = "\\frac{25}{34}"

    a_ok = random.choice([True, False])
    b_ok = random.choice([True, False])
    c_ok = random.choice([True, False])
    d_ok = random.choice([True, False])

    sh_a = ans_a if a_ok else 72
    sh_b_str = "A_{17}^2" if b_ok else "C_{17}^2"
    sh_c = ans_c if c_ok else 56
    sh_d = ans_d if d_ok else "\\frac{23}{34}"

    caudan = (
        "Ban chấp hành đoàn trường gồm $17$ thành viên trong đó có $8$ đoàn viên nam và $9$ đoàn viên nữ. "
        "Chọn ngẫu nhiên $2$ thành viên tham gia trực tuần. Xét tính đúng sai của các khẳng định sau:"
    )
    choices = _make_tf_choices([
        (a_ok, f"Số cách chọn $2$ thành viên là ${sh_a}$."),
        (b_ok, f"Số cách chọn hai thành viên để một người theo dõi sĩ số, một người phát bản tin hàng ngày là ${sh_b_str}$."),
        (c_ok, f"Biến cố 'Hai người được chọn đều là đoàn viên nam' có số các kết quả thuận lợi là ${sh_c}$."),
        (d_ok, f"Xác suất của biến cố 'Có ít nhất một thành viên được chọn là đoàn viên nam' bằng ${sh_d}$.")
    ])
    loigiai = (
        f"\\begin{{itemchoice}}\n"
        f"\\itemch {'Đúng' if a_ok else 'Sai'}. Số cách chọn $2$ thành viên tùy ý là $C_{{17}}^2 = {ans_a}$.\n"
        f"\\itemch {'Đúng' if b_ok else 'Sai'}. Chọn $2$ người có phân công nhiệm vụ cụ thể là chỉnh hợp $A_{{17}}^2$.\n"
        f"\\itemch {'Đúng' if c_ok else 'Sai'}. Số kết quả thuận lợi chọn $2$ nam là $C_8^2 = {ans_c}$.\n"
        f"\\itemch {'Đúng' if d_ok else 'Sai'}. Số cách chọn $2$ nữ là $C_9^2 = 36$. "
        f"Xác suất có ít nhất $1$ nam là $1 - \\frac{{36}}{{136}} = {ans_d}$.\n"
        f"\\end{{itemchoice}}"
    )
    return caudan, choices, loigiai



def _make_mc_choices(da_dung, da_sai1, da_sai2, da_sai3):
    opts = [str(da_dung)]
    for s in [da_sai1, da_sai2, da_sai3]:
        s_str = str(s)
        if s_str not in opts:
            opts.append(s_str)
        else:
            opts.append(s_str + " ")
    choices_label = ["\\True " + opts[0]] + opts[1:4]
    random.shuffle(choices_label)
    return [f"{{{c}}} " for c in choices_label]

# --- 2 DẠNG ĐÚNG SAI MỚI (CHƯƠNG IX) ---

def k10_tf_c9_xep_hang_5_nam_5_nu():
    n_nam = 5
    n_nu = 5
    tong = n_nam + n_nu
    omega = math.factorial(tong)
    
    # a: Không gian mẫu
    a_ok = random.choice([True, False])
    val_a = f"{tong}!" if a_ok else f"{tong-1}!"
    
    # b: 5 bạn nữ đứng cạnh nhau
    # Gộp 5 bạn nữ thành 1 khối: 5! cách. Khối này cùng 5 bạn nam: 6! cách.
    # P = (6! * 5!) / 10! = 120 / (10*9*8*7) = 1/42
    b_ok = random.choice([True, False])
    p_b_exact = Fraction(math.factorial(n_nam + 1) * math.factorial(n_nu), omega)
    val_b = _fmt_frac(p_b_exact.numerator, p_b_exact.denominator) if b_ok else _fmt_frac(1, 21)
    
    # c: Nam nữ xen kẽ nhau: 2 * 5! * 5! / 10! = 2 / 252 = 1 / 126
    c_ok = random.choice([True, False])
    p_c_exact = Fraction(2 * math.factorial(n_nam) * math.factorial(n_nu), omega)
    val_c = _fmt_frac(p_c_exact.numerator, p_c_exact.denominator) if c_ok else _fmt_frac(1, 63)
    
    # d: 2 người đứng đầu hàng và cuối hàng là nữ
    # Chọn 2 bạn nữ xếp đầu và cuối: A_5^2 = 20. Xếp 8 bạn còn lại: 8!
    # P = (20 * 8!) / 10! = 20 / 90 = 2/9
    d_ok = random.choice([True, False])
    p_d_exact = Fraction(20 * math.factorial(8), omega)
    val_d = _fmt_frac(p_d_exact.numerator, p_d_exact.denominator) if d_ok else _fmt_frac(1, 9)
    
    caudan = (
        f"Một nhóm học sinh gồm ${n_nam}$ bạn nam và ${n_nu}$ bạn nữ được xếp thành một hàng dọc. "
        f"Xét tính đúng sai của các mệnh đề sau:"
    )
    items = [
        (f"Số phần tử của không gian mẫu là ${val_a}$.", a_ok),
        (f"Xác suất để ${n_nu}$ bạn nữ đứng cạnh nhau bằng ${val_b}$.", b_ok),
        (f"Xác suất để học sinh nam và học sinh nữ đứng xen kẽ nhau bằng ${val_c}$.", c_ok),
        (f"Xác suất để $2$ người đứng đầu hàng và cuối hàng là nữ bằng ${val_d}$.", d_ok)
    ]
    choices = _make_tf_choices(items)
    loigiai = (
        f"\\begin{{itemchoice}}\\itemch {'Đúng' if a_ok else 'Sai'}. Số phần tử của không gian mẫu là xếp $10$ học sinh vào hàng dọc nên $n(\\Omega) = 10! = {omega}.\\par"
        f"\\itemch {'Đúng' if b_ok else 'Sai'}. Coi $5$ bạn nữ là một khối $X$ có $5!$ cách xếp nội bộ. Xếp khối $X$ cùng $5$ bạn nam có $6!$ cách. Do đó xác suất là \\dfrac{{6! \\times 5!}}{{10!}} = {_fmt_frac(p_b_exact.numerator, p_b_exact.denominator)}.\\par"
        f"\\itemch {'Đúng' if c_ok else 'Sai'}. Để nam nữ xen kẽ nhau có $2$ trường hợp: bắt đầu bằng nam hoặc bắt đầu bằng nữ. Mỗi trường hợp có $5! \\times 5!$ cách xếp. Xác suất là \\dfrac{{2 \\times 5! \\times 5!}}{{10!}} = {_fmt_frac(p_c_exact.numerator, p_c_exact.denominator)}.\\par"
        f"\\itemch {'Đúng' if d_ok else 'Sai'}. Chọn $2$ bạn nữ xếp ở hai đầu hàng có $A_5^2 = 20$ cách. Xếp $8$ bạn còn lại có $8!$ cách. Xác suất là \\dfrac{{20 \\times 8!}}{{10!}} = \\dfrac{{20}}{{90}} = {_fmt_frac(p_d_exact.numerator, p_d_exact.denominator)}.\\end{{itemchoice}}"
    )
    return caudan, choices, loigiai

def k10_tf_c9_xep_7_hs_ban_dai():
    a_ok = random.choice([True, False])
    val_a = "7!" if a_ok else "6!"
    
    # b: D không ngồi đầu bàn: 5 vị trí trong -> P = 5/7
    b_ok = random.choice([True, False])
    val_b = "\\dfrac{5}{7}" if b_ok else "\\dfrac{6}{7}"
    
    # c: A và B không ngồi cạnh nhau: 1 - 2/7 = 5/7
    c_ok = random.choice([True, False])
    val_c = "\\dfrac{5}{7}" if c_ok else "\\dfrac{2}{7}"
    
    # d: A, B cạnh nhau, C, D không cạnh nhau và không cạnh A, B:
    # 2! * 3! * 4 * A_3^2 = 288. P = 288 / 5040 = 2/35
    d_ok = random.choice([True, False])
    val_d = "\\dfrac{2}{35}" if d_ok else "\\dfrac{4}{21}"
    
    caudan = (
        "Xét phép thử: Xếp ngẫu nhiên $7$ học sinh $A, B, C, D, E, F, G$ vào một chiếc bàn dài có đúng $7$ ghế. "
        "Xét tính đúng sai của các mệnh đề sau:"
    )
    items = [
        (f"Số phần tử của không gian mẫu là $n(\\Omega) = {val_a}$.", a_ok),
        (f"Xác suất để bạn $D$ không ngồi đầu bàn là ${val_b}$.", b_ok),
        (f"Xác suất để $A$ và $B$ không ngồi cạnh nhau là ${val_c}$.", c_ok),
        (f"Xác suất để $A$ và $B$ ngồi cạnh nhau, đồng thời $C, D$ không ngồi cạnh nhau và không ngồi cạnh $A, B$ là ${val_d}$.", d_ok)
    ]
    choices = _make_tf_choices(items)
    loigiai = (
        f"\\begin{{itemchoice}}\\itemch {'Đúng' if a_ok else 'Sai'}. Xếp $7$ học sinh vào $7$ ghế có $n(\\Omega) = 7! = 5040.\\par"
        f"\\itemch {'Đúng' if b_ok else 'Sai'}. Đầu bàn có $2$ vị trí ngoài cùng (ghế $1$ và $7$). Để $D$ không ngồi đầu bàn thì $D$ có $5$ vị trí ghế bên trong. Xếp $6$ bạn còn lại có $6!$ cách. Xác suất là \\dfrac{{5 \\times 6!}}{{7!}} = \\dfrac{{5}}{{7}}.\\par"
        f"\\itemch {'Đúng' if c_ok else 'Sai'}. Ghép $A, B$ ngồi cạnh nhau có $2! \\times 6!$ cách, xác suất là \\dfrac{{2}}{{7}}. Xác suất để $A$ và $B$ không ngồi cạnh nhau là $1 - \\dfrac{{2}}{{7}} = \\dfrac{{5}}{{7}}.\\par"
        f"\\itemch {'Đúng' if d_ok else 'Sai'}. Gọi $(AB)$ là khối $X$ có $2!$ cách xếp nội bộ. Xếp $3$ bạn $E, F, G$ trước có $3!$ cách, tạo $4$ vách ngăn. Đặt khối $X$ vào $1$ trong $4$ vách ngăn có $4$ cách. Khi đó còn $3$ vách ngăn không kề $X$, xếp $C, D$ vào $3$ vách ngăn này có $A_3^2$ cách. Số cách thuận lợi: $2! \\times 3! \\times 4 \\times A_3^2 = 288$. Xác suất là \\dfrac{{288}}{{5040}} = \\dfrac{{2}}{{35}}.\\end{{itemchoice}}"
    )
    return caudan, choices, loigiai

# --- 12 DẠNG TRẮC NGHIỆM 4 PHƯƠNG ÁN (CHƯƠNG IX) ---

def k10_mc_c9_hop_keo_2_vi():
    a = random.randint(6, 8)  # hoa quả
    b = random.randint(5, 7)  # socola
    k = 5
    tong = a + b
    omega = math.comb(tong, k)
    thuan_loi = omega - math.comb(a, k) - math.comb(b, k)
    frac = Fraction(thuan_loi, omega)
    
    da_dung = f"$P = {_fmt_frac(frac.numerator, frac.denominator)}$"
    da_sai1 = f"$P = {_fmt_frac(frac.numerator - 10, frac.denominator)}$"
    da_sai2 = f"$P = {_fmt_frac(frac.numerator - 30, frac.denominator + 5)}$"
    da_sai3 = f"$P = {_fmt_frac(math.comb(a, 3) * math.comb(b, 2), omega)}$"
    
    caudan = (
        f"Bạn $A$ có ${a}$ cái kẹo vị hoa quả và ${b}$ cái kẹo vị socola. Bạn $A$ lấy ngẫu nhiên ${k}$ cái kẹo cho vào hộp "
        f"để tặng em gái. Tính xác suất để ${k}$ cái kẹo lấy ra có cả vị hoa quả và vị socola."
    )
    loigiai = (
        f"Không gian mẫu là $n(\\Omega) = C_{{{tong}}}^{{{k}}} = {omega}.\\par"
        f"Biến cố đối $\\overline{{E}}$ là lấy được ${k}$ cái kẹo chỉ có một vị:\\par"
        f"- Chỉ có vị hoa quả: $C_{{{a}}}^{{{k}}} = {math.comb(a, k)}$ cách.\\par"
        f"- Chỉ có vị socola: $C_{{{b}}}^{{{k}}} = {math.comb(b, k)}$ cách.\\par"
        f"Số kết quả thuận lợi là $n(E) = {omega} - {math.comb(a, k)} - {math.comb(b, k)} = {thuan_loi}.\\par"
        f"Vậy xác suất là $P(E) = \\dfrac{{{thuan_loi}}}{{{omega}}} = {_fmt_frac(frac.numerator, frac.denominator)}$."
    )
    return caudan, _make_mc_choices(da_dung, da_sai1, da_sai2, da_sai3), loigiai

def k10_mc_c9_rut_3_the_tong_khong_vuot_qua_8():
    M = random.choice([8, 9])
    valid = []
    for a in range(1, 11):
        for b in range(a + 1, 11):
            for c in range(b + 1, 11):
                if a + b + c <= M:
                    valid.append((a, b, c))
    ans = len(valid)
    da_dung = f"${ans}$"
    da_sai1 = f"${ans + 1}$"
    da_sai2 = f"${ans - 1 if ans > 1 else ans + 2}$"
    da_sai3 = f"${ans + 3}$"
    
    caudan = (
        f"Một hộp đựng $10$ thẻ được đánh số từ $1$ đến $10$. Chọn ngẫu nhiên $3$ thẻ. "
        f"Gọi $A$ là biến cố để tổng các số ghi trên $3$ thẻ được chọn không vượt quá ${M}$. "
        f"Số phần tử của biến cố $A$ là:"
    )
    liet_ke_str = ", ".join([f"\\{{{x[0]}, {x[1]}, {x[2]}\\}}" for x in valid])
    loigiai = (
        f"Các bộ $3$ thẻ phân biệt có tổng không vượt quá ${M}$ là: {liet_ke_str}.\\par"
        f"Vậy số phần tử của biến cố $A$ là $n(A) = {ans}$."
    )
    return caudan, _make_mc_choices(da_dung, da_sai1, da_sai2, da_sai3), loigiai

def k10_mc_c9_xuc_xac_tong_nho_hon_5():
    S = random.choice([5, 6])
    valid = []
    for i in range(1, 7):
        for j in range(1, 7):
            if i + j < S:
                valid.append((i, j))
    ans = len(valid)
    frac = Fraction(ans, 36)
    da_dung = f"${_fmt_frac(frac.numerator, frac.denominator)}$"
    da_sai1 = f"${_fmt_frac(ans + 2, 36)}$"
    da_sai2 = f"${_fmt_frac(ans - 1, 36)}$"
    da_sai3 = f"${_fmt_frac(ans, 30)}$"
    
    caudan = (
        f"Gieo đồng thời hai con xúc xắc cân đối và đồng chất. "
        f"Tính xác suất của biến cố \"Tổng số chấm trên hai mặt xuất hiện nhỏ hơn ${S}$\"."
    )
    liet_ke = ", ".join([f"({x[0]}; {x[1]})" for x in valid])
    loigiai = (
        f"Số phần tử của không gian mẫu là $n(\\Omega) = 6 \\times 6 = 36.\\par"
        f"Các kết quả thuận lợi có tổng số chấm nhỏ hơn ${S}$ là: {liet_ke}.\\par"
        f"Số kết quả thuận lợi là $n(A) = {ans}.\\par"
        f"Vậy xác suất là $P(A) = \\dfrac{{{ans}}}{{36}} = {_fmt_frac(frac.numerator, frac.denominator)}$."
    )
    return caudan, _make_mc_choices(da_dung, da_sai1, da_sai2, da_sai3), loigiai

def k10_mc_c9_rut_6_the_tong_le():
    N = 11
    k = 6
    n_le = 6
    n_chan = 5
    omega = math.comb(N, k)
    
    thuan_loi = (
        math.comb(n_le, 1) * math.comb(n_chan, 5) +
        math.comb(n_le, 3) * math.comb(n_chan, 3) +
        math.comb(n_le, 5) * math.comb(n_chan, 1)
    )
    frac = Fraction(thuan_loi, omega)
    da_dung = f"${_fmt_frac(frac.numerator, frac.denominator)}$"
    da_sai1 = f"$\\dfrac{{{thuan_loi - 18}}}{{{omega // 2}}}$"
    da_sai2 = f"$\\dfrac{{1}}{{2}}$"
    da_sai3 = f"$\\dfrac{{{thuan_loi - 3}}}{{{omega // 2}}}$"
    
    caudan = (
        f"Một hộp đựng ${N}$ tấm thẻ được đánh số từ $1$ đến ${N}$. Chọn ngẫu nhiên ${k}$ tấm thẻ. "
        f"Tính xác suất để tổng số ghi trên ${k}$ tấm thẻ ấy là một số lẻ."
    )
    loigiai = (
        f"Không gian mẫu: $n(\\Omega) = C_{{{N}}}^{{{k}}} = {omega}.\\par"
        f"Trong ${N}$ thẻ có $6$ thẻ mang số lẻ và $5$ thẻ mang số chẵn.\\par"
        f"Tổng các số trên ${k}$ thẻ là số lẻ khi và chỉ khi số thẻ lẻ được chọn là một số lẻ:\\par"
        f"- Trường hợp 1: Chọn $1$ thẻ lẻ, $5$ thẻ chẵn: $C_6^1 \\times C_5^5 = {math.comb(6,1)*math.comb(5,5)}$ cách.\\par"
        f"- Trường hợp 2: Chọn $3$ thẻ lẻ, $3$ thẻ chẵn: $C_6^3 \\times C_5^3 = {math.comb(6,3)*math.comb(5,3)}$ cách.\\par"
        f"- Trường hợp 3: Chọn $5$ thẻ lẻ, $1$ thẻ chẵn: $C_6^5 \\times C_5^1 = {math.comb(6,5)*math.comb(5,1)}$ cách.\\par"
        f"Số kết quả thuận lợi: $n(A) = 6 + 200 + 30 = {thuan_loi}.\\par"
        f"Vậy xác suất là $P(A) = \\dfrac{{{thuan_loi}}}{{{omega}}} = {_fmt_frac(frac.numerator, frac.denominator)}$."
    )
    return caudan, _make_mc_choices(da_dung, da_sai1, da_sai2, da_sai3), loigiai

def k10_mc_c9_tich_hai_the_la_so_chan():
    N = random.choice([9, 11])
    n_le = (N + 1) // 2
    omega = math.comb(N, 2)
    le_cases = math.comb(n_le, 2)
    thuan_loi = omega - le_cases
    frac = Fraction(thuan_loi, omega)
    
    da_dung = f"${_fmt_frac(frac.numerator, frac.denominator)}$"
    da_sai1 = f"${_fmt_frac(le_cases, omega)}$"
    da_sai2 = f"$\\dfrac{{1}}{{3}}$"
    da_sai3 = f"$\\dfrac{{2}}{{3}}$"
    
    caudan = (
        f"Có ${N}$ chiếc thẻ được đánh số từ $1$ đến ${N}$, người ta rút ngẫu nhiên hai thẻ khác nhau. "
        f"Xác suất để rút được hai thẻ mà tích hai số được đánh trên thẻ là một số chẵn bằng:"
    )
    loigiai = (
        f"Không gian mẫu là $n(\\Omega) = C_{{{N}}}^2 = {omega}.\\par"
        f"Biến cố đối $\\overline{{A}}$: Tích hai số được chọn là số lẻ $\\Leftrightarrow$ cả hai thẻ đều mang số lẻ.\\par"
        f"Từ $1$ đến ${N}$ có ${n_le}$ số lẻ nên số cách rút $2$ thẻ lẻ là $C_{{{n_le}}}^2 = {le_cases}.\\par"
        f"Số kết quả thuận lợi: $n(A) = {omega} - {le_cases} = {thuan_loi}.\\par"
        f"Vậy xác suất là $P(A) = \\dfrac{{{thuan_loi}}}{{{omega}}} = {_fmt_frac(frac.numerator, frac.denominator)}$."
    )
    return caudan, _make_mc_choices(da_dung, da_sai1, da_sai2, da_sai3), loigiai

def k10_mc_c9_gieo_dong_tien_5_lan():
    n = random.choice([4, 5, 6])
    ans = 2 ** n
    da_dung = f"${ans}$"
    da_sai1 = f"${2 * n}$"
    da_sai2 = f"${2 ** (n-1)}$"
    da_sai3 = f"${2 ** (n+1)}$"
    
    caudan = f"Gieo ngẫu nhiên một đồng tiền cân đối và đồng chất ${n}$ lần. Tính số phần tử của không gian mẫu."
    loigiai = (
        f"Mỗi lần gieo đồng tiền có $2$ kết quả có thể xảy ra (Sấp hoặc Ngửa).\\par"
        f"Gieo đồng tiền ${n}$ lần liên tiếp thì theo quy tắc nhân số phần tử của không gian mẫu là $n(\\Omega) = 2^{{{n}}} = {ans}$."
    )
    return caudan, _make_mc_choices(da_dung, da_sai1, da_sai2, da_sai3), loigiai

def k10_mc_c9_chon_so_nguyen_to_tu_tap_cho_truoc():
    pools = [
        ([1, 2, 4, 6, 8, 9], [2]),
        ([1, 2, 3, 4, 6, 8], [2, 3]),
        ([2, 3, 5, 6, 8, 9], [2, 3, 5]),
        ([1, 3, 4, 6, 7, 8], [3, 7])
    ]
    digits, primes = random.choice(pools)
    m = len(digits)
    k = len(primes)
    frac = Fraction(k, m)
    
    da_dung = f"${_fmt_frac(frac.numerator, frac.denominator)}$"
    da_sai1 = f"$\\dfrac{{1}}{{2}}$" if frac != Fraction(1, 2) else f"$\\dfrac{{1}}{{4}}$"
    da_sai2 = f"$\\dfrac{{1}}{{3}}$" if frac != Fraction(1, 3) else f"$\\dfrac{{2}}{{3}}$"
    da_sai3 = f"$\\dfrac{{1}}{{6}}$" if frac != Fraction(1, 6) else f"$\\dfrac{{5}}{{6}}$"
    
    dig_str = "; ".join(map(str, digits))
    prime_str = ", ".join(map(str, primes))
    caudan = (
        f"Từ các chữ số $\\{{{dig_str}\\}}$ lấy ngẫu nhiên một số. Xác suất để lấy được một số nguyên tố là:"
    )
    loigiai = (
        f"Số phần tử không gian mẫu là $n(\\Omega) = {m}.\\par"
        f"Trong tập hợp đã cho, các số nguyên tố là: $\\{{{prime_str}\\}}$ (gồm ${k}$ số).\\par"
        f"Vậy xác suất lấy được số nguyên tố là $P = \\dfrac{{{k}}}{{{m}}} = {_fmt_frac(frac.numerator, frac.denominator)}$."
    )
    return caudan, _make_mc_choices(da_dung, da_sai1, da_sai2, da_sai3), loigiai

def k10_mc_c9_xep_hang_nam_nu_nu_khong_canh_nhau():
    m = 7
    n = 4
    omega = math.factorial(m + n)
    thuan_loi = math.factorial(m) * math.comb(m + 1, n) * math.factorial(n)
    frac = Fraction(thuan_loi, omega)
    
    da_dung = f"${_fmt_frac(frac.numerator, frac.denominator)}$"
    da_sai1 = f"$\\dfrac{{4}}{{33}}$"
    da_sai2 = f"$\\dfrac{{3}}{{7}}$"
    da_sai3 = f"$\\dfrac{{8}}{{11}}$"
    
    caudan = (
        f"Một nhóm gồm ${m}$ học sinh nam và ${n}$ học sinh nữ xếp thành một hàng ngang để tham gia một trò chơi. "
        f"Tính xác suất để khi xếp, hai học sinh nữ bất kì không đứng cạnh nhau."
    )
    loigiai = (
        f"Xếp ${m}$ học sinh nam vào hàng ngang trước có ${m}!$ cách.\\par"
        f"Sau khi xếp ${m}$ bạn nam sẽ tạo ra ${m+1}$ khoảng trống (khe).\\par"
        f"Để không có $2$ bạn nữ nào đứng cạnh nhau, ta chọn ${n}$ khoảng trống trong ${m+1}$ khoảng trống đó "
        f"và xếp ${n}$ bạn nữ vào: có $A_{{{m+1}}}^{{{n}}}$ cách.\\par"
        f"Số cách xếp thuận lợi là $n(A) = {m}! \\times A_{{{m+1}}}^{{{n}}}.\\par"
        f"Không gian mẫu là $n(\\Omega) = {m+n}!$. Xác suất là $P(A) = \\dfrac{{{m}! \\times A_{{{m+1}}}^{{{n}}}}}{{{m+n}!}} = {_fmt_frac(frac.numerator, frac.denominator)}$."
    )
    return caudan, _make_mc_choices(da_dung, da_sai1, da_sai2, da_sai3), loigiai

def k10_mc_c9_xuc_xac_3_lan_mat_5_lan_2():
    k = random.choice([3, 4, 5, 6])
    da_dung = r"$\dfrac{1}{6}$"
    da_sai1 = r"$\dfrac{5}{36}$"
    da_sai2 = r"$\dfrac{1}{120}$"
    da_sai3 = r"$\dfrac{5}{6}$"
    
    caudan = f"Gieo một con xúc xắc $3$ lần liên tiếp. Tính xác suất sao cho mặt ${k}$ chấm xuất hiện ở lần thứ hai."
    loigiai = (
        f"Không gian mẫu là $n(\\Omega) = 6^3 = 216.\\par"
        f"Lần gieo thứ nhất có $6$ kết quả có thể xảy ra.\\par"
        f"Lần gieo thứ hai xuất hiện mặt ${k}$ chấm nên chỉ có $1$ kết quả.\\par"
        f"Lần gieo thứ ba có $6$ kết quả có thể xảy ra.\\par"
        f"Số kết quả thuận lợi là $n(A) = 6 \\times 1 \\times 6 = 36.\\par"
        f"Vậy xác suất là $P(A) = \\dfrac{{36}}{{216}} = \\dfrac{{1}}{{6}}$."
    )
    return caudan, _make_mc_choices(da_dung, da_sai1, da_sai2, da_sai3), loigiai

def k10_mc_c9_bien_co_doi_it_nhat_1_mau_vang():
    caudan = (
        "Từ một hộp chứa $6$ quả cầu trắng, $7$ quả cầu đỏ, $4$ quả cầu vàng, các quả cầu có kích thước và khối lượng giống nhau. "
        "Xét phép thử \"Lấy ngẫu nhiên đồng thời $3$ quả cầu\". Biến cố đối của biến cố $A$: \"$3$ quả cầu lấy ra có ít nhất một quả màu vàng\" là:"
    )
    da_dung = "$\\overline{A}$: \"$3$ quả cầu lấy ra không có màu vàng\"."
    da_sai1 = "$\\overline{A}$: \"$3$ quả cầu lấy ra cùng màu trắng\"."
    da_sai2 = "$\\overline{A}$: \"$3$ quả cầu lấy ra cùng màu đỏ\"."
    da_sai3 = "$\\overline{A}$: \"$3$ quả cầu lấy ra có $3$ màu khác nhau\"."
    loigiai = (
        "Biến cố $A$ là \"Có ít nhất một quả màu vàng\" (nghĩa là có $1$, $2$ hoặc $3$ quả vàng).\\par"
        "Do đó biến cố đối $\\overline{A}$ là phủ định của $A$, tức là \"Không có quả cầu nào màu vàng\" (hay \"$3$ quả cầu lấy ra không có màu vàng\")."
    )
    return caudan, _make_mc_choices(da_dung, da_sai1, da_sai2, da_sai3), loigiai

def k10_mc_c9_hop_lap_phuong_mat_doi_cung_mau():
    color = random.choice(["xanh", "đỏ", "vàng"])
    da_dung = r"$\dfrac{1}{3}$"
    da_sai1 = r"$\dfrac{2}{3}$"
    da_sai2 = r"$\dfrac{1}{2}$"
    da_sai3 = r"$\dfrac{1}{6}$"
    
    caudan = (
        f"Quỳnh có một chiếc hộp hình lập phương mà sáu mặt được tô bởi ba màu đỏ, vàng, xanh sao cho chỉ có các mặt đối nhau thì tô cùng màu. "
        f"Hỏi tung ngẫu nhiên hộp đó thì xác suất để được mặt màu {color} ngửa là bao nhiêu?"
    )
    loigiai = (
        f"Một khối lập phương có $6$ mặt gồm $3$ cặp mặt đối diện nhau.\\par"
        f"Vì các mặt đối diện tô cùng màu và có $3$ màu đỏ, vàng, xanh nên mỗi màu được tô ở đúng $2$ mặt.\\par"
        f"Khi tung ngẫu nhiên, không gian mẫu $n(\\Omega) = 6$ mặt.\\par"
        f"Số mặt tô màu {color} là $2$. Xác suất được mặt {color} ngửa là $P = \\dfrac{{2}}{{6}} = \\dfrac{{1}}{{3}}$."
    )
    return caudan, _make_mc_choices(da_dung, da_sai1, da_sai2, da_sai3), loigiai

def k10_mc_c9_hieu_so_cham_xuc_xac_bang_2():
    d = random.choice([1, 2, 3])
    valid = []
    for i in range(1, 7):
        for j in range(1, 7):
            if abs(i - j) == d:
                valid.append((i, j))
    ans = len(valid)
    frac = Fraction(ans, 36)
    
    da_dung = f"${_fmt_frac(frac.numerator, frac.denominator)}$"
    da_sai1 = f"$\\dfrac{{1}}{{9}}$" if frac != Fraction(1, 9) else f"$\\dfrac{{5}}{{18}}$"
    da_sai2 = f"$\\dfrac{{5}}{{18}}$" if frac != Fraction(5, 18) else f"$\\dfrac{{2}}{{9}}$"
    da_sai3 = f"$\\dfrac{{5}}{{6}}$"
    
    caudan = (
        f"Gieo ngẫu nhiên $2$ con xúc xắc cân đối đồng chất. "
        f"Tìm xác suất của biến cố \"Hiệu số chấm xuất hiện trên $2$ con xúc xắc bằng ${d}$\"."
    )
    liet_ke = ", ".join([f"({x[0]}; {x[1]})" for x in valid])
    loigiai = (
        f"Số phần tử của không gian mẫu: $n(\\Omega) = 6 \\times 6 = 36.\\par"
        f"Các kết quả thuận lợi thỏa mãn $|i - j| = {d}$ là: {liet_ke}.\\par"
        f"Số kết quả thuận lợi là $n(A) = {ans}.\\par"
        f"Vậy xác suất là $P(A) = \\dfrac{{{ans}}}{{36}} = {_fmt_frac(frac.numerator, frac.denominator)}$."
    )
    return caudan, _make_mc_choices(da_dung, da_sai1, da_sai2, da_sai3), loigiai
