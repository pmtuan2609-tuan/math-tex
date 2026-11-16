# -*- coding: utf-8 -*-
"""
Module sinh đề trắc nghiệm chuẩn ma trận Bài tập Cuối Chương 3 (Toán 12)
Các số đặc trưng đo mức độ phân tán của mẫu số liệu ghép nhóm
Gồm 2 bài x 6 câu = 12 câu chuẩn ma trận giống Chương 1 và Chương 2:
- Bài 1: Khoảng biến thiên và khoảng tứ phân vị của mẫu số liệu ghép nhóm (2 NB, 3 TH, 1 VD)
- Bài 2: Phương sai và độ lệch chuẩn của mẫu số liệu ghép nhóm (2 NB, 3 TH, 1 VD)
Tất cả đều sinh ngẫu nhiên số liệu, tự động tính toán đáp án và lời giải chi tiết theo chuẩn ex_test.
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


def fmt_num(x):
    """Định dạng số theo chuẩn tiếng Việt (dấu phẩy thập phân)."""
    if isinstance(x, float):
        if x.is_integer():
            return str(int(x))
        s = f"{x:.2f}".rstrip('0').rstrip('.')
        return s.replace('.', ',')
    return str(x)


# ==============================================================================
# BÀI 1: KHOẢNG BIẾN THIÊN VÀ KHOẢNG TỨ PHÂN VỊ CỦA MẪU SỐ LIỆU GHÉP NHÓM
# ==============================================================================

def CuoiChuong3_MC_B1_NB1():
    """B1. Khoảng biến thiên và khoảng tứ phân vị - Mức độ: NB (Dạng 1): Tìm khoảng biến thiên R"""
    topic = random.choice(['thời gian truy cập Internet (phút/ngày)', 'chiều cao của học sinh (cm)', 'mức lương nhân viên (triệu đồng)', 'thời gian hoàn thành công việc (phút)'])
    step = random.choice([5, 10, 2])
    start = random.choice([20, 50, 150, 6]) if step != 2 else random.choice([4, 6, 8])
    num_groups = random.choice([4, 5])
    
    bounds = [start + i * step for i in range(num_groups + 1)]
    freqs = [random.randint(4, 25) for _ in range(num_groups)]
    
    groups_str = ' & '.join([f"[{bounds[i]}; {bounds[i+1]})" for i in range(num_groups)])
    freqs_str = ' & '.join([str(f) for f in freqs])
    align_str = 'c' * (num_groups + 1)
    
    R = bounds[-1] - bounds[0]
    
    caudan = fr'''Khảo sát {topic} của một nhóm đối tượng được kết quả cho bởi bảng tần số ghép nhóm sau:
\begin{{center}}
\begin{{tabular}}{{|{align_str}|}}
\hline
Nhóm & {groups_str} \\ \hline
Tần số & {freqs_str} \\ \hline
\end{{tabular}}
\end{{center}}
Khoảng biến thiên của mẫu số liệu ghép nhóm trên bằng bao nhiêu?'''

    correct = fr'''${fmt_num(R)}$'''
    wrongs = [
        fr'''${fmt_num(bounds[-1] - bounds[1])}$''',
        fr'''${fmt_num(bounds[-2] - bounds[0])}$''',
        fr'''${fmt_num(R / 2)}$'''
    ]
    
    loi_giai = fr'''Giá trị đầu mút lớn nhất của nhóm cuối cùng là $a_{{{num_groups}}} = {bounds[-1]}$.\\
Giá trị đầu mút nhỏ nhất của nhóm đầu tiên là $a_0 = {bounds[0]}$.\\
Khoảng biến thiên của mẫu số liệu ghép nhóm là:
\[
R = a_{{{num_groups}}} - a_0 = {bounds[-1]} - {bounds[0]} = {R}.
\]'''

    return caudan, shuffle_choices(correct, wrongs), loi_giai


def CuoiChuong3_MC_B1_NB2():
    """B1. Khoảng biến thiên và khoảng tứ phân vị - Mức độ: NB (Dạng 2): Nhóm chứa tứ phân vị"""
    step = random.choice([4, 5, 10])
    start = random.choice([10, 20, 50, 140])
    num_groups = 5
    bounds = [start + i * step for i in range(num_groups + 1)]
    freqs = [random.randint(5, 15) for _ in range(num_groups)]
    n = sum(freqs)
    
    cf = []
    curr = 0
    for f in freqs:
        curr += f
        cf.append(curr)
        
    target = random.choice(['Q1', 'Q2', 'Q3'])
    if target == 'Q1':
        pos = n / 4
        name_target = 'tứ phân vị thứ nhất $Q_1$'
        k_idx = next(i for i, c in enumerate(cf) if c >= pos)
    elif target == 'Q2':
        pos = n / 2
        name_target = 'trung vị $M_e$ (hoặc $Q_2$)'
        k_idx = next(i for i, c in enumerate(cf) if c >= pos)
    else:
        pos = 3 * n / 4
        name_target = 'tứ phân vị thứ ba $Q_3$'
        k_idx = next(i for i, c in enumerate(cf) if c >= pos)
        
    groups_str = ' & '.join([f"[{bounds[i]}; {bounds[i+1]})" for i in range(num_groups)])
    freqs_str = ' & '.join([str(f) for f in freqs])
    align_str = 'c' * (num_groups + 1)
    
    caudan = fr'''Cho mẫu số liệu ghép nhóm về kết quả thống kê có bảng tần số sau:
\begin{{center}}
\begin{{tabular}}{{|{align_str}|}}
\hline
Nhóm & {groups_str} \\ \hline
Tần số & {freqs_str} \\ \hline
\end{{tabular}}
\end{{center}}
Nhóm chứa {name_target} của mẫu số liệu ghép nhóm trên là nhóm nào?'''

    correct = fr'''$[{bounds[k_idx]}; {bounds[k_idx+1]})$'''
    wrongs_idx = [i for i in range(num_groups) if i != k_idx]
    random.shuffle(wrongs_idx)
    wrongs = [fr'''$[{bounds[i]}; {bounds[i+1]})$''' for i in wrongs_idx[:3]]
    
    loi_giai = fr'''Cỡ mẫu là $n = {' + '.join(str(f) for f in freqs)} = {n}$.\\
Tần số tích lũy của các nhóm lần lượt là: ${', '.join(str(c) for c in cf)}$.\\
Ta có vị trí xét tứ phân vị là: $\frac{{{1 if target == 'Q1' else (2 if target == 'Q2' else 3)} \cdot {n}}}{{4}} = {fmt_num(pos)}$.\\
Do $cf_{{{k_idx}}} = {cf[k_idx - 1] if k_idx > 0 else 0} < {fmt_num(pos)} \le cf_{{{k_idx + 1}}} = {cf[k_idx]}$, nên nhóm chứa {name_target} là $[{bounds[k_idx]}; {bounds[k_idx+1]})$.'''

    return caudan, shuffle_choices(correct, wrongs), loi_giai


def CuoiChuong3_MC_B1_TH1():
    """B1. Khoảng biến thiên và khoảng tứ phân vị - Mức độ: TH (Dạng 1): Tính tứ phân vị thứ nhất Q1"""
    step = random.choice([5, 10, 4])
    start = random.choice([10, 20, 50, 150])
    num_groups = 4
    bounds = [start + i * step for i in range(num_groups + 1)]
    freqs = [random.randint(6, 16) for _ in range(num_groups)]
    n = sum(freqs)
    
    cf = []
    curr = 0
    for f in freqs:
        curr += f
        cf.append(curr)
        
    pos = n / 4
    k = next(i for i, c in enumerate(cf) if c >= pos)
    C = cf[k-1] if k > 0 else 0
    q1 = bounds[k] + ((pos - C) / freqs[k]) * step
    q1_round = round(q1, 2)
    
    groups_str = ' & '.join([f"[{bounds[i]}; {bounds[i+1]})" for i in range(num_groups)])
    freqs_str = ' & '.join([str(f) for f in freqs])
    align_str = 'c' * (num_groups + 1)
    
    caudan = fr'''Khảo sát thời gian làm một bài tập (tính bằng phút) của một nhóm học sinh thu được bảng sau:
\begin{{center}}
\begin{{tabular}}{{|{align_str}|}}
\hline
Thời gian (phút) & {groups_str} \\ \hline
Số học sinh & {freqs_str} \\ \hline
\end{{tabular}}
\end{{center}}
Tứ phân vị thứ nhất $Q_1$ của mẫu số liệu ghép nhóm trên gần bằng giá trị nào sau đây?'''

    correct = fr'''${fmt_num(q1_round)}$'''
    wrongs = [
        fr'''${fmt_num(round(q1_round + random.choice([1.2, 1.5, 2.1]), 2))}$''',
        fr'''${fmt_num(round(q1_round - random.choice([0.8, 1.1, 1.4]), 2))}$''',
        fr'''${fmt_num(round(bounds[k] + step / 2, 2))}$'''
    ]
    
    loi_giai = fr'''Cỡ mẫu là $n = {n}$. Ta có $\frac{{n}}{{4}} = \frac{{{n}}}{{4}} = {fmt_num(pos)}$.\\
Nhóm chứa $Q_1$ là nhóm $[{bounds[k]}; {bounds[k+1]})$ vì có tần số tích lũy nhỏ nhất lớn hơn hoặc bằng ${fmt_num(pos)}$.\\
Áp dụng công thức tính tứ phân vị thứ nhất cho mẫu số liệu ghép nhóm:
\[
Q_1 = u_m + \frac{{\frac{{n}}{{4}} - C}}{{n_m}} \cdot (u_{{m+1}} - u_m) = {bounds[k]} + \frac{{{fmt_num(pos)} - {C}}}{{{freqs[k]}}} \cdot {step} \approx {fmt_num(q1_round)}.
\]'''

    return caudan, shuffle_choices(correct, wrongs), loi_giai


def CuoiChuong3_MC_B1_TH2():
    """B1. Khoảng biến thiên và khoảng tứ phân vị - Mức độ: TH (Dạng 2): Tính tứ phân vị thứ ba Q3"""
    step = random.choice([5, 10, 4])
    start = random.choice([10, 20, 50, 150])
    num_groups = 4
    bounds = [start + i * step for i in range(num_groups + 1)]
    freqs = [random.randint(6, 16) for _ in range(num_groups)]
    n = sum(freqs)
    
    cf = []
    curr = 0
    for f in freqs:
        curr += f
        cf.append(curr)
        
    pos = 3 * n / 4
    k = next(i for i, c in enumerate(cf) if c >= pos)
    C = cf[k-1] if k > 0 else 0
    q3 = bounds[k] + ((pos - C) / freqs[k]) * step
    q3_round = round(q3, 2)
    
    groups_str = ' & '.join([f"[{bounds[i]}; {bounds[i+1]})" for i in range(num_groups)])
    freqs_str = ' & '.join([str(f) for f in freqs])
    align_str = 'c' * (num_groups + 1)
    
    caudan = fr'''Khảo sát mức thu nhập hàng tháng (đơn vị: triệu đồng) của các hộ gia đình ở một khu dân cư thu được bảng sau:
\begin{{center}}
\begin{{tabular}}{{|{align_str}|}}
\hline
Thu nhập & {groups_str} \\ \hline
Số hộ & {freqs_str} \\ \hline
\end{{tabular}}
\end{{center}}
Tứ phân vị thứ ba $Q_3$ của mẫu số liệu ghép nhóm trên gần bằng giá trị nào dưới đây?'''

    correct = fr'''${fmt_num(q3_round)}$'''
    wrongs = [
        fr'''${fmt_num(round(q3_round + random.choice([1.2, 1.6, 2.0]), 2))}$''',
        fr'''${fmt_num(round(q3_round - random.choice([1.0, 1.4, 1.8]), 2))}$''',
        fr'''${fmt_num(round(bounds[k] + step / 2, 2))}$'''
    ]
    
    loi_giai = fr'''Cỡ mẫu $n = {n}$. Ta có $\frac{{3n}}{{4}} = \frac{{3 \cdot {n}}}{{4}} = {fmt_num(pos)}$.\\
Nhóm chứa $Q_3$ là nhóm $[{bounds[k]}; {bounds[k+1]})$ vì tần số tích lũy trước đó là ${C}$ và nhóm này có $cf = {cf[k]} \ge {fmt_num(pos)}$.\\
Áp dụng công thức:
\[
Q_3 = u_p + \frac{{\frac{{3n}}{{4}} - C}}{{n_p}} \cdot (u_{{p+1}} - u_p) = {bounds[k]} + \frac{{{fmt_num(pos)} - {C}}}{{{freqs[k]}}} \cdot {step} \approx {fmt_num(q3_round)}.
\]'''

    return caudan, shuffle_choices(correct, wrongs), loi_giai


def CuoiChuong3_MC_B1_TH3():
    """B1. Khoảng biến thiên và khoảng tứ phân vị - Mức độ: TH (Dạng 3): Khoảng tứ phân vị Delta_Q"""
    step = random.choice([5, 4, 10])
    start = random.choice([10, 20, 150])
    num_groups = 4
    bounds = [start + i * step for i in range(num_groups + 1)]
    freqs = [random.randint(6, 14) for _ in range(num_groups)]
    n = sum(freqs)
    
    cf = []
    curr = 0
    for f in freqs:
        curr += f
        cf.append(curr)
        
    pos1 = n / 4
    k1 = next(i for i, c in enumerate(cf) if c >= pos1)
    C1 = cf[k1-1] if k1 > 0 else 0
    q1 = bounds[k1] + ((pos1 - C1) / freqs[k1]) * step
    
    pos3 = 3 * n / 4
    k3 = next(i for i, c in enumerate(cf) if c >= pos3)
    C3 = cf[k3-1] if k3 > 0 else 0
    q3 = bounds[k3] + ((pos3 - C3) / freqs[k3]) * step
    
    delta_q = round(q3 - q1, 2)
    
    groups_str = ' & '.join([f"[{bounds[i]}; {bounds[i+1]})" for i in range(num_groups)])
    freqs_str = ' & '.join([str(f) for f in freqs])
    align_str = 'c' * (num_groups + 1)
    
    caudan = fr'''Cho bảng số liệu ghép nhóm về điểm kiểm tra của học sinh một khối:
\begin{{center}}
\begin{{tabular}}{{|{align_str}|}}
\hline
Điểm số & {groups_str} \\ \hline
Số học sinh & {freqs_str} \\ \hline
\end{{tabular}}
\end{{center}}
Khoảng tứ phân vị $\Delta_Q$ của mẫu số liệu ghép nhóm này bằng bao nhiêu (làm tròn đến hàng phần trăm)?'''

    correct = fr'''${fmt_num(delta_q)}$'''
    wrongs = [
        fr'''${fmt_num(round(delta_q + 1.25, 2))}$''',
        fr'''${fmt_num(round(abs(delta_q - 1.15), 2))}$''',
        fr'''${fmt_num(round(bounds[-1] - bounds[0], 2))}$'''
    ]
    
    loi_giai = fr'''Ta có cỡ mẫu $n = {n}$.\\
- Tính $Q_1$: $\frac{{n}}{{4}} = {fmt_num(pos1)}$. Nhóm chứa $Q_1$ là $[{bounds[k1]}; {bounds[k1+1]})$.\\
$Q_1 = {bounds[k1]} + \frac{{{fmt_num(pos1)} - {C1}}}{{{freqs[k1]}}} \cdot {step} \approx {fmt_num(round(q1, 2))}$.\\
- Tính $Q_3$: $\frac{{3n}}{{4}} = {fmt_num(pos3)}$. Nhóm chứa $Q_3$ là $[{bounds[k3]}; {bounds[k3+1]})$.\\
$Q_3 = {bounds[k3]} + \frac{{{fmt_num(pos3)} - {C3}}}{{{freqs[k3]}}} \cdot {step} \approx {fmt_num(round(q3, 2))}$.\\
Khoảng tứ phân vị là:
\[
\Delta_Q = Q_3 - Q_1 \approx {fmt_num(round(q3, 2))} - {fmt_num(round(q1, 2))} = {fmt_num(delta_q)}.
\]'''

    return caudan, shuffle_choices(correct, wrongs), loi_giai


def CuoiChuong3_MC_B1_VD():
    """B1. Khoảng biến thiên và khoảng tứ phân vị - Mức độ: VD: So sánh độ phân tán bằng khoảng biến thiên / khoảng tứ phân vị"""
    step = 5
    bounds = [150 + i * step for i in range(5)]
    freqs_A = [random.randint(4, 10), random.randint(12, 18), random.randint(14, 20), random.randint(3, 8)]
    freqs_B = [random.randint(8, 14), random.randint(7, 12), random.randint(8, 14), random.randint(9, 15)]
    
    nA = sum(freqs_A)
    nB = sum(freqs_B)
    
    cfA = []
    s = 0
    for f in freqs_A:
        s += f
        cfA.append(s)
    q1_A = bounds[next(i for i, c in enumerate(cfA) if c >= nA/4)]
    q3_A = bounds[next(i for i, c in enumerate(cfA) if c >= 3*nA/4)]
    dqA = q3_A - q1_A
    
    cfB = []
    s = 0
    for f in freqs_B:
        s += f
        cfB.append(s)
    q1_B = bounds[next(i for i, c in enumerate(cfB) if c >= nB/4)]
    q3_B = bounds[next(i for i, c in enumerate(cfB) if c >= 3*nB/4)]
    dqB = q3_B - q1_B
    
    groups_str = ' & '.join([f"[{bounds[i]}; {bounds[i+1]})" for i in range(4)])
    fA_str = ' & '.join(str(x) for x in freqs_A)
    fB_str = ' & '.join(str(x) for x in freqs_B)
    
    caudan = fr'''Thầy giáo đo chiều cao (cm) của học sinh hai lớp 12A và 12B, thu được bảng thống kê như sau:
\begin{{center}}
\begin{{tabular}}{{|c|c|c|c|c|}}
\hline
Chiều cao & {groups_str} \\ \hline
Lớp 12A & {fA_str} \\ \hline
Lớp 12B & {fB_str} \\ \hline
\end{{tabular}}
\end{{center}}
So sánh khoảng biến thiên $R$ và khoảng tứ phân vị $\Delta_Q$ về chiều cao của hai lớp trên, nhận định nào sau đây là đúng?'''

    if dqA < dqB:
        correct = r'''Hai lớp có khoảng biến thiên bằng nhau, nhưng chiều cao của học sinh lớp 12A đồng đều hơn học sinh lớp 12B.'''
        wrongs = [
            r'''Chiều cao học sinh lớp 12B có khoảng biến thiên lớn hơn lớp 12A.''',
            r'''Chiều cao của học sinh lớp 12B đồng đều hơn học sinh lớp 12A.''',
            r'''Khoảng tứ phân vị của lớp 12A lớn hơn khoảng tứ phân vị của lớp 12B.'''
        ]
        loi_giai = fr'''Khoảng biến thiên của hai lớp đều là: $R = {bounds[-1]} - {bounds[0]} = {bounds[-1] - bounds[0]}$ cm.\\
Khoảng tứ phân vị của lớp 12A nhỏ hơn lớp 12B (do tần số lớp 12A tập trung chủ yếu ở các nhóm giữa), chứng tỏ chiều cao học sinh lớp 12A có độ phân tán nhỏ hơn, tức là đồng đều hơn học sinh lớp 12B.'''
    else:
        correct = r'''Hai lớp có khoảng biến thiên bằng nhau, nhưng chiều cao của học sinh lớp 12B đồng đều hơn học sinh lớp 12A.'''
        wrongs = [
            r'''Chiều cao học sinh lớp 12A có khoảng biến thiên lớn hơn lớp 12B.''',
            r'''Chiều cao của học sinh lớp 12A đồng đều hơn học sinh lớp 12B.''',
            r'''Khoảng tứ phân vị của lớp 12B lớn hơn khoảng tứ phân vị của lớp 12A.'''
        ]
        loi_giai = fr'''Khoảng biến thiên của hai lớp đều là: $R = {bounds[-1]} - {bounds[0]} = {bounds[-1] - bounds[0]}$ cm.\\
Khoảng tứ phân vị của lớp 12B nhỏ hơn lớp 12A, do đó chiều cao của học sinh lớp 12B đồng đều hơn lớp 12A.'''

    return caudan, shuffle_choices(correct, wrongs), loi_giai


# ==============================================================================
# BÀI 2: PHƯƠNG SAI VÀ ĐỘ LỆCH CHUẨN CỦA MẪU SỐ LIỆU GHÉP NHÓM
# ==============================================================================

def CuoiChuong3_MC_B2_NB1():
    """B2. Phương sai và độ lệch chuẩn - Mức độ: NB (Dạng 1): Giá trị đại diện & Số trung bình"""
    step = random.choice([5, 10, 4])
    start = random.choice([10, 20, 60])
    num_groups = 4
    bounds = [start + i * step for i in range(num_groups + 1)]
    freqs = [random.randint(4, 12) for _ in range(num_groups)]
    mids = [(bounds[i] + bounds[i+1]) / 2 for i in range(num_groups)]
    
    n = sum(freqs)
    mean_val = sum(f * m for f, m in zip(freqs, mids)) / n
    mean_round = round(mean_val, 2)
    
    groups_str = ' & '.join([f"[{bounds[i]}; {bounds[i+1]})" for i in range(num_groups)])
    freqs_str = ' & '.join([str(f) for f in freqs])
    align_str = 'c' * (num_groups + 1)
    
    caudan = fr'''Cho bảng tần số ghép nhóm thống kê thời gian ôn tập mỗi ngày (phút) của học sinh:
\begin{{center}}
\begin{{tabular}}{{|{align_str}|}}
\hline
Thời gian & {groups_str} \\ \hline
Tần số & {freqs_str} \\ \hline
\end{{tabular}}
\end{{center}}
Số trung bình $\bar{{x}}$ của mẫu số liệu ghép nhóm trên bằng bao nhiêu (làm tròn đến hàng phần trăm)?'''

    correct = fr'''${fmt_num(mean_round)}$'''
    wrongs = [
        fr'''${fmt_num(round(mean_round + random.choice([1.25, 2.5]), 2))}$''',
        fr'''${fmt_num(round(abs(mean_round - random.choice([1.5, 2.0])), 2))}$''',
        fr'''${fmt_num(round((bounds[0] + bounds[-1]) / 2, 2))}$'''
    ]
    
    calc_str = ' + '.join(f"{f} \\cdot {fmt_num(m)}" for f, m in zip(freqs, mids))
    loi_giai = fr'''Giá trị đại diện của các nhóm lần lượt là: ${', '.join(fmt_num(m) for m in mids)}$.\\
Tổng số học sinh là $n = {n}$.\\
Số trung bình của mẫu số liệu ghép nhóm là:
\[
\bar{{x}} = \frac{{{calc_str}}}{{{n}}} = \frac{{{fmt_num(sum(f * m for f, m in zip(freqs, mids)))}}}{{{n}}} \approx {fmt_num(mean_round)}.
\]'''

    return caudan, shuffle_choices(correct, wrongs), loi_giai


def CuoiChuong3_MC_B2_NB2():
    """B2. Phương sai và độ lệch chuẩn - Mức độ: NB (Dạng 2): Công thức tính phương sai và độ lệch chuẩn"""
    variant = random.choice([1, 2])
    if variant == 1:
        caudan = r'''Cho mẫu số liệu ghép nhóm gồm $k$ nhóm có giá trị đại diện lần lượt là $c_1, c_2, \dots, c_k$ với tần số tương ứng là $n_1, n_2, \dots, n_k$. Gọi $n = \sum_{i=1}^k n_i$ là cỡ mẫu và $\bar{x}$ là số trung bình. Công thức nào sau đây là công thức tính phương sai $s^2$ của mẫu số liệu ghép nhóm?'''
        correct = r'''$s^2 = \frac{1}{n} \sum_{i=1}^k n_i c_i^2 - (\bar{x})^2$'''
        wrongs = [
            r'''$s^2 = \frac{1}{n} \sum_{i=1}^k n_i c_i - (\bar{x})^2$''',
            r'''$s^2 = \frac{1}{n} \sum_{i=1}^k n_i (c_i - \bar{x})$''',
            r'''$s^2 = \sqrt{\frac{1}{n} \sum_{i=1}^k n_i c_i^2 - (\bar{x})^2}$'''
        ]
        loi_giai = r'''Phương sai của mẫu số liệu ghép nhóm được tính theo công thức:
\[
s^2 = \frac{1}{n} \sum_{i=1}^k n_i (c_i - \bar{x})^2 = \frac{1}{n} \sum_{i=1}^k n_i c_i^2 - (\bar{x})^2.
\]'''
    else:
        caudan = r'''Mối liên hệ giữa độ lệch chuẩn $s$ và phương sai $s^2$ của một mẫu số liệu ghép nhóm được phát biểu đúng bởi khẳng định nào sau đây?'''
        correct = r'''Độ lệch chuẩn là căn bậc hai số học của phương sai: $s = \sqrt{s^2}$.'''
        wrongs = [
            r'''Phương sai là căn bậc hai số học của độ lệch chuẩn: $s^2 = \sqrt{s}$.''',
            r'''Độ lệch chuẩn bằng hai lần phương sai: $s = 2s^2$.''',
            r'''Độ lệch chuẩn luôn luôn bằng số trung bình của mẫu số liệu: $s = \bar{x}$.'''
        ]
        loi_giai = r'''Theo định nghĩa trong sách giáo khoa, độ lệch chuẩn $s$ của mẫu số liệu ghép nhóm là căn bậc hai số học của phương sai: $s = \sqrt{s^2}$.'''

    return caudan, shuffle_choices(correct, wrongs), loi_giai


def CuoiChuong3_MC_B2_TH1():
    """B2. Phương sai và độ lệch chuẩn - Mức độ: TH (Dạng 1): Tính phương sai s^2"""
    step = random.choice([2, 4, 5])
    start = random.choice([2, 4, 10])
    num_groups = 4
    bounds = [start + i * step for i in range(num_groups + 1)]
    freqs = [random.randint(4, 10) for _ in range(num_groups)]
    mids = [(bounds[i] + bounds[i+1]) / 2 for i in range(num_groups)]
    n = sum(freqs)
    
    mean = sum(f * m for f, m in zip(freqs, mids)) / n
    var = sum(f * (m ** 2) for f, m in zip(freqs, mids)) / n - (mean ** 2)
    var_round = round(var, 2)
    
    groups_str = ' & '.join([f"[{bounds[i]}; {bounds[i+1]})" for i in range(num_groups)])
    freqs_str = ' & '.join([str(f) for f in freqs])
    align_str = 'c' * (num_groups + 1)
    
    caudan = fr'''Khảo sát năng suất lúa (tạ/ha) của một số thửa ruộng thí nghiệm được kết quả ở bảng sau:
\begin{{center}}
\begin{{tabular}}{{|{align_str}|}}
\hline
Năng suất & {groups_str} \\ \hline
Số thửa ruộng & {freqs_str} \\ \hline
\end{{tabular}}
\end{{center}}
Phương sai $s^2$ của mẫu số liệu ghép nhóm trên gần bằng giá trị nào sau đây?'''

    correct = fr'''${fmt_num(var_round)}$'''
    wrongs = [
        fr'''${fmt_num(round(math.sqrt(var_round), 2))}$''',
        fr'''${fmt_num(round(var_round + random.choice([1.35, 2.15]), 2))}$''',
        fr'''${fmt_num(round(abs(var_round - random.choice([1.1, 1.6])), 2))}$'''
    ]
    
    loi_giai = fr'''Giá trị đại diện của các nhóm lần lượt là: ${', '.join(fmt_num(m) for m in mids)}$.\\
Cỡ mẫu là $n = {n}$.\\
Số trung bình của mẫu là $\bar{{x}} \approx {fmt_num(round(mean, 2))}$.\\
Phương sai của mẫu số liệu ghép nhóm là:
\[
s^2 = \frac{{1}}{{{n}}} \sum_{{i=1}}^{{{num_groups}}} n_i c_i^2 - (\bar{{x}})^2 \approx {fmt_num(var_round)}.
\]'''

    return caudan, shuffle_choices(correct, wrongs), loi_giai


def CuoiChuong3_MC_B2_TH2():
    """B2. Phương sai và độ lệch chuẩn - Mức độ: TH (Dạng 2): Tính độ lệch chuẩn s"""
    step = random.choice([5, 10, 4])
    start = random.choice([10, 20, 50])
    num_groups = 4
    bounds = [start + i * step for i in range(num_groups + 1)]
    freqs = [random.randint(5, 12) for _ in range(num_groups)]
    mids = [(bounds[i] + bounds[i+1]) / 2 for i in range(num_groups)]
    n = sum(freqs)
    
    mean = sum(f * m for f, m in zip(freqs, mids)) / n
    var = sum(f * (m ** 2) for f, m in zip(freqs, mids)) / n - (mean ** 2)
    std = math.sqrt(var)
    std_round = round(std, 2)
    
    groups_str = ' & '.join([f"[{bounds[i]}; {bounds[i+1]})" for i in range(num_groups)])
    freqs_str = ' & '.join([str(f) for f in freqs])
    align_str = 'c' * (num_groups + 1)
    
    caudan = fr'''Khảo sát thời gian tự học ở nhà mỗi ngày (phút) của học sinh lớp 12 thu được kết quả:
\begin{{center}}
\begin{{tabular}}{{|{align_str}|}}
\hline
Thời gian (phút) & {groups_str} \\ \hline
Số học sinh & {freqs_str} \\ \hline
\end{{tabular}}
\end{{center}}
Độ lệch chuẩn $s$ của mẫu số liệu ghép nhóm này bằng bao nhiêu (làm tròn đến hàng phần trăm)?'''

    correct = fr'''${fmt_num(std_round)}$'''
    wrongs = [
        fr'''${fmt_num(round(var, 2))}$''',
        fr'''${fmt_num(round(std_round + random.choice([0.75, 1.25]), 2))}$''',
        fr'''${fmt_num(round(abs(std_round - random.choice([0.65, 0.95])), 2))}$'''
    ]
    
    loi_giai = fr'''Giá trị đại diện các nhóm lần lượt là: ${', '.join(fmt_num(m) for m in mids)}$.\\
Cỡ mẫu $n = {n}$.\\
Số trung bình $\bar{{x}} \approx {fmt_num(round(mean, 2))}$.\\
Phương sai: $s^2 \approx {fmt_num(round(var, 2))}$.\\
Độ lệch chuẩn của mẫu số liệu ghép nhóm là:
\[
s = \sqrt{{s^2}} = \sqrt{{{fmt_num(round(var, 2))}}} \approx {fmt_num(std_round)}.
\]'''

    return caudan, shuffle_choices(correct, wrongs), loi_giai


def CuoiChuong3_MC_B2_TH3():
    """B2. Phương sai và độ lệch chuẩn - Mức độ: TH (Dạng 3): So sánh độ phân tán / độ rủi ro bằng độ lệch chuẩn"""
    s1 = round(random.uniform(2.1, 4.5), 2)
    s2 = round(s1 + random.choice([1.2, 1.6, 2.0]), 2)
    mean1 = round(random.uniform(7.0, 8.5), 1)
    mean2 = round(mean1 + random.choice([-0.2, 0.0, 0.3]), 1)
    
    caudan = fr'''Kết quả phân tích điểm thi thử tốt nghiệp môn Toán của hai trường THPT X và THPT Y cho kết quả thống kê như sau:
- Trường X có điểm trung bình $\bar{{x}}_X = {fmt_num(mean1)}$ và độ lệch chuẩn $s_X = {fmt_num(s1)}$.
- Trường Y có điểm trung bình $\bar{{x}}_Y = {fmt_num(mean2)}$ và độ lệch chuẩn $s_Y = {fmt_num(s2)}$.
Dựa vào các số đặc trưng đo mức độ phân tán, khẳng định nào sau đây là khẳng định đúng?'''

    correct = fr'''Điểm thi của trường X đồng đều hơn điểm thi của trường Y (vì $s_X < s_Y$).'''
    wrongs = [
        fr'''Điểm thi của trường Y đồng đều hơn điểm thi của trường X (vì $s_Y > s_X$).''',
        fr'''Mức độ phân tán điểm thi của trường X lớn hơn trường Y.''',
        fr'''Không thể so sánh độ đồng đều vì điểm trung bình của hai trường khác nhau.'''
    ]
    
    loi_giai = fr'''Độ lệch chuẩn đo mức độ phân tán của dữ liệu quanh giá trị trung bình.\\
Vì $s_X = {fmt_num(s1)} < s_Y = {fmt_num(s2)}$, nên điểm thi của học sinh trường X ít phân tán hơn, tức là kết quả học sinh trường X đồng đều hơn học sinh trường Y.'''

    return caudan, shuffle_choices(correct, wrongs), loi_giai


def CuoiChuong3_MC_B2_VD():
    """B2. Phương sai và độ lệch chuẩn - Mức độ: VD: Vận dụng cao bài toán thực tế có tần số khuyết hoặc phân tích cổ phiếu"""
    step = 2
    bounds = [0, 2, 4, 6, 8]
    freqs_base = [5, 10, 4]
    x_val = random.choice([6, 8, 10])
    freqs = [freqs_base[0], x_val, freqs_base[1], freqs_base[2]]
    mids = [1, 3, 5, 7]
    n = sum(freqs)
    
    mean = sum(f * m for f, m in zip(freqs, mids)) / n
    var = sum(f * (m ** 2) for f, m in zip(freqs, mids)) / n - (mean ** 2)
    var_round = round(var, 2)
    std_round = round(math.sqrt(var), 2)
    
    caudan = fr'''Khảo sát thời gian sử dụng điện thoại thông minh (giờ/ngày) của một nhóm $n = {n}$ bạn học sinh được cho bởi bảng sau:
\begin{{center}}
\begin{{tabular}}{{|c|c|c|c|c|}}
\hline
Thời gian (giờ) & $[0; 2)$ & $[2; 4)$ & $[4; 6)$ & $[6; 8)$ \\ \hline
Số học sinh & ${freqs_base[0]}$ & $x$ & ${freqs_base[1]}$ & ${freqs_base[2]}$ \\ \hline
\end{{tabular}}
\end{{center}}
Biết tổng số học sinh được khảo sát là $n = {n}$. Độ lệch chuẩn của mẫu số liệu ghép nhóm trên gần bằng giá trị nào sau đây?'''

    correct = fr'''${fmt_num(std_round)}$'''
    wrongs = [
        fr'''${fmt_num(var_round)}$''',
        fr'''${fmt_num(round(std_round + 0.85, 2))}$''',
        fr'''${fmt_num(round(abs(std_round - 0.75), 2))}$'''
    ]
    
    loi_giai = fr'''Tổng số học sinh khảo sát là $n = {n}$, do đó:
\[
{freqs_base[0]} + x + {freqs_base[1]} + {freqs_base[2]} = {n} \implies x = {x_val}.
\]
Giá trị đại diện các nhóm: $c_1 = 1; c_2 = 3; c_3 = 5; c_4 = 7$.\\
Số trung bình của mẫu là:
\[
\bar{{x}} = \frac{{{freqs_base[0]} \cdot 1 + {x_val} \cdot 3 + {freqs_base[1]} \cdot 5 + {freqs_base[2]} \cdot 7}}{{{n}}} = \frac{{{sum(f * m for f, m in zip(freqs, mids))}}}{{{n}}} \approx {fmt_num(round(mean, 2))}.
\]
Phương sai:
\[
s^2 = \frac{{1}}{{{n}}}({freqs_base[0]} \cdot 1^2 + {x_val} \cdot 3^2 + {freqs_base[1]} \cdot 5^2 + {freqs_base[2]} \cdot 7^2) - (\bar{{x}})^2 \approx {fmt_num(var_round)}.
\]
Độ lệch chuẩn là: $s = \sqrt{{s^2}} \approx {fmt_num(std_round)}$.'''

    return caudan, shuffle_choices(correct, wrongs), loi_giai


# Alias tương thích ngược
CuoiChuong3_MC_Cau1 = CuoiChuong3_MC_B1_NB1
CuoiChuong3_MC_Cau2 = CuoiChuong3_MC_B1_NB2
CuoiChuong3_MC_Cau3 = CuoiChuong3_MC_B1_TH1
CuoiChuong3_MC_Cau4 = CuoiChuong3_MC_B1_TH2
CuoiChuong3_MC_Cau5 = CuoiChuong3_MC_B1_TH3
CuoiChuong3_MC_Cau6 = CuoiChuong3_MC_B1_VD
CuoiChuong3_MC_Cau7 = CuoiChuong3_MC_B2_NB1
CuoiChuong3_MC_Cau8 = CuoiChuong3_MC_B2_NB2
CuoiChuong3_MC_Cau9 = CuoiChuong3_MC_B2_TH1
CuoiChuong3_MC_Cau10 = CuoiChuong3_MC_B2_TH2
CuoiChuong3_MC_Cau11 = CuoiChuong3_MC_B2_TH3
CuoiChuong3_MC_Cau12 = CuoiChuong3_MC_B2_VD
