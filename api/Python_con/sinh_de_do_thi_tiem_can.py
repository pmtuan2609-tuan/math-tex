# -*- coding: utf-8 -*-
"""
Module sinh câu hỏi trắc nghiệm Toán 12 theo hình ảnh đề thi:
1. sinh_cau_tcx_do_thi(): Xác định phương trình tiệm cận xiên từ đồ thị hàm số (TikZ)
2. sinh_cau_tcx_cong_thuc(): Tìm tiệm cận xiên từ công thức giải tích y = ax + b + c/(x - x0)
3. sinh_cau_gtln_gtnn_do_thi(): Tìm GTLN/GTNN của hàm số trên đoạn từ đồ thị
4. sinh_cau_dau_he_so_bac_ba(): Xác định dấu hệ số a, d của hàm số bậc ba từ đồ thị
5. sinh_cau_don_dieu_do_thi(): Đọc khoảng đồng biến / nghịch biến từ đồ thị hàm số
6. sinh_cau_tam_doi_xung_nhat_bien(): Xác định tọa độ tâm đối xứng từ đồ thị hàm nhất biến
7. sinh_cau_dung_sai_do_thi_dao_ham(): Câu hỏi Đúng/Sai dựa trên đồ thị đạo hàm f'(x)
"""

import random

def format_linear(a, b):
    str_a = 'x' if a == 1 else ('-x' if a == -1 else f'{a}x')
    if b > 0:
        return f'{str_a} + {b}'
    elif b < 0:
        return f'{str_a} - {abs(b)}'
    return str_a

def format_pt(a, b):
    return f'y = {format_linear(a, b)}'

# ==============================================================================
# 1. DẠNG: TÌM TIỆM CẬN XIÊN TỪ ĐỒ THỊ HÀM PHÂN THỨC 2/1 (CÂU 11 ĐỢT 1)
# ==============================================================================
def sinh_cau_tcx_do_thi():
    patterns = [
        # Nhóm a = 1
        (1, 2, -2, 1),
        (1, 1, -1, 1),
        (1, 3, -3, 1),
        (1, 2, -1, 1),
        (1, 1, -2, 1),
        (1, -2, 2, 1),
        (1, -1, 1, 1),
        (1, -3, 3, 1),
        (1, -1, 2, 1),
        (1, -2, 1, 1),
        # Nhóm a = -1
        (-1, 2, 2, 1),
        (-1, 3, 3, 1),
        (-1, 1, 1, 1),
        (-1, 2, 1, 1),
        (-1, -2, -2, 1),
        (-1, -3, -3, 1),
        (-1, -1, -1, 1),
        # Nhóm a = 2, -2
        (2, 2, -1, 1),
        (2, 4, -2, 1),
        (2, -2, 1, 1),
        (-2, 2, 1, 1),
        (-2, 4, 2, 1),
        (-2, -2, -1, 1),
    ]
    a, b, x0, k = random.choice(patterns)
    xA = -b // a
    yB = b
    
    xmin = min(-4, x0 - 2, xA - 1)
    xmax = max(4, x0 + 2, xA + 1)
    ymin = min(-4, yB - 2, -2)
    ymax = max(4, yB + 2, 2)
    
    ans_dung = f'${format_pt(a, b)}$'
    sai1 = f'$y = {format_linear(a, 0)}$'
    if a == 1:
        sai2 = random.choice(['$y = 2x$', '$y = x - 2$' if b > 0 else '$y = x + 2$'])
    elif a == -1:
        sai2 = random.choice(['$y = -2x$', '$y = -x - 2$' if b > 0 else '$y = -x + 2$'])
    else:
        sai2 = f'$y = x + {b}$' if b > 0 else f'$y = x - {abs(b)}$'
    sai3 = f'$x = {x0}$'
    
    options = [
        f'{{\\True {ans_dung} }}',
        f'{{{sai1} }}',
        f'{{{sai2} }}',
        f'{{{sai3} }}'
    ]
    # Clean any trailing periods
    options = [opt.replace('.$', '$').replace('. }', ' }') for opt in options]
    random.shuffle(options)
    
    d1 = round(x0 - 0.22, 2)
    d2 = round(x0 + 0.22, 2)
    x0_label = f"\\draw ({x0},0.1)--({x0},-0.1) node[below right]{{${x0}$}};" if x0 != xA else ""

    tikz = f'''\\begin{{tikzpicture}}[scale=0.55, font=\\footnotesize, line join=round, line cap=round, >=stealth]
    \\def\\xmin{{{xmin}}}\\def\\xmax{{{xmax}}}\\def\\ymin{{{ymin}}}\\def\\ymax{{{ymax}}}
    \\draw[->] (\\xmin-0.2,0)--(\\xmax+0.2,0) node[below]{{$x$}};
    \\draw[->] (0,\\ymin-0.2)--(0,\\ymax+0.2) node[left]{{$y$}};
    \\draw (0,0) node[below right]{{$O$}};
    \\begin{{scope}}
    \\clip (\\xmin,\\ymin) rectangle (\\xmax,\\ymax);
    % Tiệm cận đứng (nét đứt)
    \\draw[dashed, blue!80!black, thick] ({x0},\\ymin)--({x0},\\ymax);
    % Tiệm cận xiên (nét đứt)
    \\draw[dashed, red!80!black, thick] (\\xmin,{{{a}*(\\xmin)+({b})}})--(\\xmax,{{{a}*(\\xmax)+({b})}});
    % Đồ thị hai nhánh
    \\draw[thick, smooth, samples=150, domain=\\xmin:{d1}] plot (\\x, {{{a}*\\x + ({b}) + ({k})/(\\x - ({x0}))}});
    \\draw[thick, smooth, samples=150, domain={d2}:\\xmax] plot (\\x, {{{a}*\\x + ({b}) + ({k})/(\\x - ({x0}))}});
    \\end{{scope}}
    % Các giao điểm trên trục tọa độ
    \\fill ({xA},0) circle (1.5pt) node[below left]{{${xA}$}};
    \\fill (0,{yB}) circle (1.5pt) node[above left]{{${yB}$}};
    {x0_label}
\\end{{tikzpicture}}'''

    caudan = f'''Cho hàm số $y = f(x)$ có đồ thị như hình vẽ bên. Đường tiệm cận xiên của đồ thị hàm số đã cho là đường thẳng có phương trình là'''
    sign_str = f'+ {yB}' if yB >= 0 else f'- {abs(yB)}'
    loigiai = f'''Quan sát đồ thị hàm số:
- Đường tiệm cận xiên cắt trục tung tại điểm $B(0; {yB})$ và cắt trục hoành tại điểm $A({xA}; 0)$.
- Phương trình đường thẳng đi qua hai điểm $A({xA}; 0)$ và $B(0; {yB})$ có dạng $y = ax + b$:
  + Do đường thẳng cắt trục tung tại $(0; {yB})$ nên $b = {yB}$.
  + Do đường thẳng đi qua $A({xA}; 0)$ nên ta có:
    $$a \\cdot ({xA}) {sign_str} = 0 \\iff a = {a}.$$
Vậy phương trình đường tiệm cận xiên của đồ thị hàm số là ${format_pt(a, b)}$.'''.replace('+-', '-').replace('--', '+')

    return caudan, options, loigiai, tikz

# ==============================================================================
# 2. DẠNG: TÌM TIỆM CẬN XIÊN TỪ CÔNG THỨC GIẢI TÍCH y = ax + b + c/(x - x0)
# ==============================================================================
def sinh_cau_tcx_cong_thuc():
    a = random.choice([1, 2, 3, -1, -2])
    b = random.choice([-5, -4, -3, -2, -1, 1, 2, 3, 4, 5])
    c = random.choice([-5, -4, -3, -2, -1, 1, 2, 3, 4, 5])
    x0 = random.choice([-4, -3, -2, -1, 1, 2, 3, 4])
    
    lin_str = format_linear(a, b)
    den_str = f'x - {x0}' if x0 > 0 else f'x + {abs(x0)}'
    
    if c > 0:
        func_tex = f'y = {lin_str} + \\dfrac{{{c}}}{{{den_str}}}'
    else:
        func_tex = f'y = {lin_str} - \\dfrac{{{abs(c)}}}{{{den_str}}}'
        
    caudan = f'''Tiệm cận xiên của đồ thị hàm số ${func_tex}$ là đường thẳng có phương trình'''
    ans_dung = f'${format_pt(a, b)}$'
    sai1 = f'$y = {format_linear(-a, -b)}$'
    sai2 = f'$y = {format_linear(1 if a != 1 else 2, b)}$'
    sai3 = f'$y = {format_linear(a, -b)}$'
    
    options = [
        f'{{\\True {ans_dung} }}',
        f'{{{sai1} }}',
        f'{{{sai2} }}',
        f'{{{sai3} }}'
    ]
    random.shuffle(options)
    
    loigiai = f'''Ta có:
$$\\lim\\limits_{{x \\to \\pm\\infty}} \\left[ f(x) - ({lin_str}) \\right] = \\lim\\limits_{{x \\to \\pm\\infty}} \\dfrac{{{c}}}{{{den_str}}} = 0.$$
Do đó, đường tiệm cận xiên của đồ thị hàm số là đường thẳng có phương trình ${format_pt(a, b)}$.'''
    return caudan, options, loigiai

# ==============================================================================
# 3. DẠNG: GTLN/GTNN CỦA HÀM SỐ TRÊN ĐOẠN TỪ ĐỒ THỊ
# ==============================================================================
def sinh_cau_gtln_gtnn_do_thi():
    M = random.choice([4, 5, 6])
    y_max = random.choice([5, 6, 7, 8])
    y_min = random.choice([-4, -3, -2])
    
    is_max = random.choice([True, False])
    loai = "lớn nhất" if is_max else "nhỏ nhất"
    ans_val = y_max if is_max else y_min
    
    tikz = f'''\\begin{{tikzpicture}}[scale=0.55, font=\\footnotesize, line join=round, line cap=round, >=stealth]
    \\def\\xmin{{-{M+1}}}\\def\\xmax{{{M+1}}}\\def\\ymin{{{y_min-2}}}\\def\\ymax{{{y_max+1.5}}}
    \\draw[->] (\\xmin,0)--(\\xmax,0) node[above]{{$x$}};
    \\draw[->] (0,\\ymin)--(0,\\ymax) node[right]{{$y$}};
    \\draw (0,0) node[below right]{{$O$}};
    \\clip (\\xmin-0.2,\\ymin-0.2) rectangle (\\xmax+0.2,\\ymax+0.2);
    
    \\draw[thick, smooth] plot coordinates {{
        (-{M}, {y_max}) (-{M-2}, {y_min}) (-1, {y_max-3}) (1, {y_min+2}) (3, {y_max-2}) ({M}, {y_max-1})
    }};
    \\draw[dashed] (-{M},0) node[below]{{$-{M}$}} -- (-{M},{y_max}) -- (0,{y_max}) node[right]{{${y_max}$}};
    \\draw[dashed] (-{M-2},0) node[above]{{$-{M-2}$}} -- (-{M-2},{y_min}) -- (0,{y_min}) node[left]{{${y_min}$}};
    \\draw[dashed] ({M},0) node[below]{{${M}$}} -- ({M},{y_max-1});
\\end{{tikzpicture}}'''

    caudan = fr'''\immini{{Cho hàm số $y = f(x)$ có đồ thị như hình bên. Khi đó giá trị {loai} của hàm số $y = f(x)$ trên đoạn $[-{M}; {M}]$ là}}{{{tikz}}}'''
    cand_vals = [-M, M, y_min if is_max else y_max, ans_val + 1, ans_val - 1, 0, -M - 2]
    distractors = []
    for cv in cand_vals:
        if cv != ans_val and cv not in distractors:
            distractors.append(cv)
        if len(distractors) == 3:
            break
    
    options = [
        f'{{\\True ${ans_val}$ }}',
        f'{{${distractors[0]}$ }}',
        f'{{${distractors[1]}$ }}',
        f'{{${distractors[2]}$ }}'
    ]
    random.shuffle(options)
    
    loigiai = f'''Dựa vào đồ thị hàm số trên đoạn $[-{M}; {M}]$:
- Điểm cao nhất của đồ thị có tung độ bằng ${y_max}$ đạt tại $x = -{M}$.
- Điểm thấp nhất của đồ thị có tung độ bằng ${y_min}$ đạt tại $x = -{M-2}$.
Vậy giá trị {loai} của hàm số trên đoạn $[-{M}; {M}]$ là ${ans_val}$.'''

    return caudan, options, loigiai

# ==============================================================================
# 4. DẠNG: XÁC ĐỊNH DẤU a, d CỦA HÀM BẬC BA TỪ ĐỒ THỊ
# ==============================================================================
def sinh_cau_dau_he_so_bac_ba():
    a_pos = random.choice([True, False])
    d_pos = random.choice([True, False])
    d_val = random.choice([1, 2, 3]) if d_pos else random.choice([-1, -2, -3])
    
    a_sign_str = "a > 0" if a_pos else "a < 0"
    d_sign_str = "d > 0" if d_pos else "d < 0"
    
    if a_pos:
        coords = f"(-1, {d_val-4}) (0, {d_val}) (1, {d_val-1.5}) (2, {d_val-3}) (3, {d_val+2})"
    else:
        coords = f"(-2, {d_val+3}) (-1, {d_val-2}) (0, {d_val}) (1, {d_val+2}) (2, {d_val-3})"
        
    tikz = f'''\\begin{{tikzpicture}}[scale=0.6, font=\\footnotesize, line join=round, line cap=round, >=stealth]
    \\def\\xmin{{-3}}\\def\\xmax{{3.5}}\\def\\ymin{{-4}}\\def\\ymax{{4.5}}
    \\draw[->] (\\xmin,0)--(\\xmax,0) node[above]{{$x$}};
    \\draw[->] (0,\\ymin)--(0,\\ymax) node[right]{{$y$}};
    \\draw (0,0) node[below left]{{$O$}};
    \\clip (\\xmin-0.2,\\ymin-0.2) rectangle (\\xmax+0.2,\\ymax+0.2);
    \\draw[thick, smooth] plot coordinates {{{coords}}};
    \\fill (0,{d_val}) circle (1.2pt) node[{'above left' if d_pos else 'below left'}]{{${d_val}$}};
\\end{{tikzpicture}}'''

    caudan = fr'''\immini{{Cho hàm số bậc ba $y = ax^3 + bx^2 + cx + d$ có đồ thị là đường cong như hình bên. Khi đó, khẳng định nào sau đây là đúng?}}{{{tikz}}}'''
    ans_dung = f'${a_sign_str}, {d_sign_str}$'
    sai1 = f'${a_sign_str}, {"d < 0" if d_pos else "d > 0"}$'
    sai2 = f'${"a < 0" if a_pos else "a > 0"}, {d_sign_str}$'
    sai3 = f'${"a < 0" if a_pos else "a > 0"}, {"d < 0" if d_pos else "d > 0"}$'
    
    options = [
        f'{{\\True {ans_dung} }}',
        f'{{{sai1} }}',
        f'{{{sai2} }}',
        f'{{{sai3} }}'
    ]
    random.shuffle(options)
    
    loigiai = f'''Quan sát đồ thị hàm số bậc ba $y = ax^3 + bx^2 + cx + d$:
- Khi $x \\to +\\infty$, đồ thị hàm số {'đi lên' if a_pos else 'đi xuống'}, do đó ${a_sign_str}$.
- Đồ thị cắt trục tung $Oy$ tại điểm có tọa độ $(0; d)$. Nhìn vào hình vẽ ta thấy giao điểm có tung độ bằng ${d_val}$ nên ${d_sign_str}$.
Vậy khẳng định đúng là ${a_sign_str}, {d_sign_str}$.'''

    return caudan, options, loigiai

# ==============================================================================
# 5. DẠNG: TÌM KHOẢNG ĐƠN ĐIỆU TỪ ĐỒ THỊ
# ==============================================================================
def sinh_cau_don_dieu_do_thi():
    x1 = 0
    x2 = random.choice([2, 3])
    y1 = random.choice([3, 4])
    y2 = random.choice([0, -1])
    
    is_nghich_bien = random.choice([True, False])
    loai = "nghịch biến" if is_nghich_bien else "đồng biến"
    
    tikz = f'''\\begin{{tikzpicture}}[scale=0.65, font=\\footnotesize, line join=round, line cap=round, >=stealth]
    \\def\\xmin{{-2}}\\def\\xmax{{{x2+1.5}}}\\def\\ymin{{-2}}\\def\\ymax{{{y1+1.5}}}
    \\draw[->] (\\xmin,0)--(\\xmax,0) node[above]{{$x$}};
    \\draw[->] (0,\\ymin)--(0,\\ymax) node[right]{{$y$}};
    \\draw (0,0) node[below left]{{$O$}};
    \\clip (\\xmin-0.2,\\ymin-0.2) rectangle (\\xmax+0.2,\\ymax+0.2);
    \\draw[thick, smooth] plot coordinates {{
        (-1.5, -1) (0, {y1}) ({x2/2}, {(y1+y2)/2}) ({x2}, {y2}) ({x2+1}, {y1})
    }};
    \\draw[dashed] ({x2},0) node[below]{{${x2}$}} -- ({x2},{y2}) -- (0,{y2}) node[left]{{${y2}$}};
    \\fill (0,{y1}) circle (1.2pt) node[above right]{{${y1}$}};
\\end{{tikzpicture}}'''

    caudan = fr'''\immini{{Cho hàm số $y = f(x)$ có đồ thị như hình bên. Khi đó, hàm số đã cho {loai} trên khoảng nào dưới đây?}}{{{tikz}}}'''
    if is_nghich_bien:
        ans_dung = f'$({x1}; {x2})$'
        sai1 = f'$(-\\infty; {x1})$'
        sai2 = f'$({x2}; +\\infty)$'
        sai3 = f'$(-1; {x2+1})$'
    else:
        ans_dung = random.choice([f'$(-\\infty; {x1})$', f'$({x2}; +\\infty)$'])
        sai1 = f'$({x1}; {x2})$'
        sai2 = f'$(-1; {x2})$'
        sai3 = f'$(0; +\\infty)$'
        
    options = [
        f'{{\\True {ans_dung} }}',
        f'{{{sai1} }}',
        f'{{{sai2} }}',
        f'{{{sai3} }}'
    ]
    random.shuffle(options)
    
    loigiai = f'''Quan sát đồ thị hàm số:
- Trên các khoảng $(-\\infty; {x1})$ và $({x2}; +\\infty)$, đồ thị đi lên từ trái sang phải nên hàm số đồng biến.
- Trên khoảng $({x1}; {x2})$, đồ thị đi xuống từ trái sang phải nên hàm số nghịch biến.
Vậy hàm số {loai} trên khoảng {ans_dung}.'''

    return caudan, options, loigiai

# ==============================================================================
# 6. DẠNG: TÂM ĐỐI XỨNG CỦA ĐỒ THỊ HÀM NHẤT BIẾN (CÂU 11 ĐỢT 2)
# ==============================================================================
def sinh_cau_tam_doi_xung_nhat_bien():
    patterns = [
        (1, 2, 3),    # yB = -1 (mẫu gốc của ảnh)
        (1, 1, 2),    # yB = -1
        (1, 2, 1),    # yB = 1
        (-1, 2, -3),  # yB = -1
        (-1, 1, -2),  # yB = -1
        (2, 1, 4),    # yB = -1
        (2, 2, 2),    # yB = 1
        (-2, 1, -4),  # yB = -1
        (-1, -2, 3),  # yB = 1
        (1, -2, -3),  # yB = 1
    ]
    x0, y0, k = random.choice(patterns)
    yB = y0 - k // x0
    
    xmin = min(-3, x0 - 2)
    xmax = max(3, x0 + 2)
    ymin = min(-3, yB - 1, y0 - 2)
    ymax = max(3, yB + 1, y0 + 2)
    
    tikz = f'''\\begin{{tikzpicture}}[scale=0.55, font=\\footnotesize, line join=round, line cap=round, >=stealth]
    \\def\\xmin{{{xmin}}}\\def\\xmax{{{xmax}}}\\def\\ymin{{{ymin}}}\\def\\ymax{{{ymax}}}
    \\draw[->] (\\xmin-0.2,0)--(\\xmax+0.2,0) node[below]{{$x$}};
    \\draw[->] (0,\\ymin-0.2)--(0,\\ymax+0.2) node[left]{{$y$}};
    \\draw (0,0) node[below left]{{$O$}};
    \\clip (\\xmin,\\ymin) rectangle (\\xmax,\\ymax);
    % Tiệm cận đứng và ngang (nét đứt)
    \\draw[dashed, blue!80!black, thick] ({x0},\\ymin)--({x0},\\ymax);
    \\draw[dashed, blue!80!black, thick] (\\xmin,{y0})--(\\xmax,{y0});
    % Đồ thị hai nhánh
    \\draw[thick, smooth, samples=200, domain=\\xmin:{x0}-0.15] plot (\\x, {{{y0} + ({k})/(\\x - ({x0}))}});
    \\draw[thick, smooth, samples=200, domain={x0}+0.15:\\xmax] plot (\\x, {{{y0} + ({k})/(\\x - ({x0}))}});
    % Đánh dấu số trên các trục
    \\fill ({x0},0) circle (1.2pt) node[below]{{${x0}$}};
    \\fill (0,{y0}) circle (1.2pt) node[left]{{${y0}$}};
    \\fill[blue!70!black] (0,{yB}) circle (1.2pt) node[right]{{${yB}$}};
\\end{{tikzpicture}}'''

    caudan = f'''Cho hàm số $y = \\dfrac{{ax + b}}{{cx + d}}$ có đồ thị như hình vẽ bên. Tâm đối xứng của đồ thị hàm số đã cho có tọa độ là'''
    ans_dung = f'$({x0}; {y0})$'
    sai1 = f'$(0; {yB})$'
    sai2 = f'$({-x0}; {y0})$'
    sai3 = f'$({-x0}; {1 if y0 == 2 else 2})$'
    
    options = [
        f'{{\\True {ans_dung} }}',
        f'{{{sai1} }}',
        f'{{{sai2} }}',
        f'{{{sai3} }}'
    ]
    random.shuffle(options)
    
    loigiai = f'''Quan sát đồ thị hàm số ta thấy:
- Đường tiệm cận đứng là $x = {x0}$.
- Đường tiệm cận ngang là $y = {y0}$.
Giao điểm của hai đường tiệm cận là điểm $I({x0}; {y0})$.
Tâm đối xứng của đồ thị hàm phân thức bậc nhất trên bậc nhất $y = \\dfrac{{ax+b}}{{cx+d}}$ chính là giao điểm của hai đường tiệm cận.
Vậy tọa độ tâm đối xứng là $I({x0}; {y0})$.'''

    return caudan, options, loigiai, tikz

# ==============================================================================
# 7. DẠNG: ĐÚNG / SAI TỪ ĐỒ THỊ ĐẠO HÀM f'(x) (CÂU 1 ĐỢT 2)
# ==============================================================================
def sinh_cau_dung_sai_do_thi_dao_ham():
    x1 = random.choice([-4, -3, -2])
    x2 = random.choice([1, 2, 3])
    x_trai = x1 - 2
    x_phai = x2 + 6
    
    y_a_dung = random.choice([True, False])
    if y_a_dung:
        opt_a_str = f"Hàm số $y = f(x)$ nghịch biến trên khoảng $({x1}; {x2})$"
        lg_a = f"a) Đúng. Do trên khoảng $({x1}; {x2})$, đồ thị $f'(x)$ nằm hoàn toàn phía dưới trục hoành ($f'(x) < 0$) nên hàm số nghịch biến trên khoảng $({x1}; {x2})$."
    else:
        opt_a_str = f"Hàm số $y = f(x)$ đồng biến trên khoảng $({x1}; {x2})$"
        lg_a = f"a) Sai. Do trên khoảng $({x1}; {x2})$, đồ thị $f'(x)$ nằm phía dưới trục hoành ($f'(x) < 0$) nên hàm số nghịch biến trên khoảng này, không phải đồng biến."

    y_b_dung = random.choice([True, False])
    if y_b_dung:
        opt_b_str = f"Hàm số đạt cực đại tại $x = {x1}$"
        lg_b = f"b) Đúng. Khi đi qua điểm $x = {x1}$, $f'(x)$ đổi dấu từ dương sang âm, do đó hàm số đạt cực đại tại $x = {x1}$."
    else:
        opt_b_str = f"Hàm số đạt cực tiểu tại $x = {x1}$"
        lg_b = f"b) Sai. Khi qua $x = {x1}$, $f'(x)$ đổi dấu từ dương sang âm nên $x = {x1}$ là điểm cực đại, không phải cực tiểu."

    u = x1 - 1
    v = x1
    y_c_dung = random.choice([True, False])
    if y_c_dung:
        opt_c_str = f"$f({u}) < f({v})$"
        lg_c = f"c) Đúng. Do trên khoảng $({x_trai}; {x1})$, $f'(x) > 0$ nên hàm số đồng biến. Vì ${u} < {v}$ nên $f({u}) < f({v})$."
    else:
        opt_c_str = f"$f({u}) > f({v})$"
        lg_c = f"c) Sai. Do trên khoảng $({x_trai}; {x1})$, hàm số đồng biến nên từ ${u} < {v}$ suy ra $f({u}) < f({v})$."

    u_d = 0
    v_d = 1
    y_d_dung = random.choice([True, False])
    if y_d_dung:
        opt_d_str = f"Trên đoạn $[{u_d}; {v_d}]$, giá trị lớn nhất của hàm số là $\\max_{{[{u_d}; {v_d}]}} f(x) = f({u_d})$"
        lg_d = f"d) Đúng. Do hàm số liên tục và có $f'(x) \\le 0$ trên đoạn $[{u_d}; {v_d}] \\subset [{x1}; {x2}]$, hàm số nghịch biến trên đoạn này, do đó giá trị lớn nhất đạt tại đầu mút trái: $\\max_{{[{u_d}; {v_d}]}} f(x) = f({u_d})$."
    else:
        opt_d_str = f"Trên đoạn $[{u_d}; {v_d}]$, giá trị lớn nhất của hàm số là $\\max_{{[{u_d}; {v_d}]}} f(x) = f({v_d})$"
        lg_d = f"d) Sai. Do hàm số nghịch biến trên $[{u_d}; {v_d}]$ nên giá trị lớn nhất phải là $f({u_d})$, còn $f({v_d})$ là giá trị nhỏ nhất."

    tikz = f'''\\begin{{tikzpicture}}[scale=0.55, font=\\footnotesize, line join=round, line cap=round, >=stealth]
    \\def\\xmin{{{x_trai-1}}}\\def\\xmax{{{x_phai+1}}}\\def\\ymin{{-2.5}}\\def\\ymax{{4.5}}
    \\draw[->] (\\xmin,0)--(\\xmax,0) node[below]{{$x$}};
    \\draw[->] (0,\\ymin)--(0,\\ymax) node[right]{{$y$}};
    \\draw (0,0) node[below left]{{$O$}};
    \\clip (\\xmin-0.2,\\ymin-0.2) rectangle (\\xmax+0.2,\\ymax+0.2);
    
    \\draw[thick, red!70!black, smooth] plot coordinates {{
        ({x_trai}, 4) ({x1}, 0) ({(x1+x2)/2}, -1.8) ({x2}, 0) ({x2+3}, 2.5) ({x_phai}, 1.5)
    }};
    \\draw[dashed] ({x_trai},0) node[below]{{${x_trai}$}} -- ({x_trai},4);
    \\draw[dashed] ({x_phai},0) node[below]{{${x_phai}$}} -- ({x_phai},1.5);
    \\node[below left] at ({x1},0) {{${x1}$}};
    \\node[below right] at ({x2},0) {{${x2}$}};
\\end{{tikzpicture}}'''

    caudan = fr'''\immini{{Cho hàm số $y = f(x)$ có đạo hàm trên $\mathbb{{R}}$ và đồ thị hàm số $f'(x)$ được biểu diễn như hình bên.}}{{{tikz}}}'''

    choice_a = f"{{\\True {opt_a_str}}}" if y_a_dung else f"{{{opt_a_str}}}"
    choice_b = f"{{\\True {opt_b_str}}}" if y_b_dung else f"{{{opt_b_str}}}"
    choice_c = f"{{\\True {opt_c_str}}}" if y_c_dung else f"{{{opt_c_str}}}"
    choice_d = f"{{\\True {opt_d_str}}}" if y_d_dung else f"{{{opt_d_str}}}"

    choices = [choice_a, choice_b, choice_c, choice_d]
    
    loigiai = f'''\\begin{{itemchoice}}
\\itemch {lg_a}
\\itemch {lg_b}
\\itemch {lg_c}
\\itemch {lg_d}
\\end{{itemchoice}}'''

    return caudan, choices, loigiai


# Alias for CuoiChuong1_TF_Cau17
CuoiChuong1_TF_Cau17 = sinh_cau_dung_sai_do_thi_dao_ham

# ==============================================================================
# 8. DẠNG: NHẬN DẠNG HÀM BẬC BA TỪ BẢNG BIẾN THIÊN (NGHIỆM KÉP HOẶC VÔ NGHIỆM)
# ==============================================================================
def sinh_cau_bbt_bac_ba_nghiem_kep_vo_nghiem():
    loai = random.choice(["nghiem_kep", "vo_nghiem"])
    
    if loai == "nghiem_kep":
        a_sign = 1 if random.random() < 0.75 else -1
        kieu = random.choice(["phan_so", "nguyen"])
        
        x0 = random.choice([-2, -1, 1, 2, 3])
        y0 = random.choice([-3, -2, -1, 1, 2, 3])
        
        if kieu == "phan_so":
            d_num = 3 * y0 - a_sign * (x0**3)
            d_den = 3
            # Rút gọn d
            import math
            gcd_d = math.gcd(abs(d_num), d_den)
            d_num //= gcd_d
            d_den //= gcd_d
            
            def fmt_frac_poly(a_s, x_val, num_d, den_d):
                sgn = "" if a_s == 1 else "-"
                t1 = f"{sgn}\\dfrac{{x^3}}{{3}}"
                if abs(x_val) == 1:
                    t2 = f"- x^2" if a_s * x_val > 0 else f"+ x^2"
                else:
                    t2 = f"- {abs(x_val)}x^2" if a_s * x_val > 0 else f"+ {abs(x_val)}x^2"
                
                x0_sq = x_val**2
                if x0_sq == 1:
                    t3 = f"+ x" if a_s > 0 else f"- x"
                else:
                    t3 = f"+ {x0_sq}x" if a_s > 0 else f"- {x0_sq}x"
                
                if num_d == 0:
                    t4 = ""
                elif den_d == 1:
                    t4 = f"+ {num_d}" if num_d > 0 else f"- {abs(num_d)}"
                else:
                    t4 = f"+ \\dfrac{{{num_d}}}{{{den_d}}}" if num_d > 0 else f"- \\dfrac{{{abs(num_d)}}}{{{den_d}}}"
                
                return f"y = {t1} {t2} {t3} {t4}".replace("  ", " ").strip()
                
            f_true = fmt_frac_poly(a_sign, x0, d_num, d_den)
            der_str = f"(x - {x0})^2" if a_sign == 1 and x0 > 0 else (f"(x + {abs(x0)})^2" if a_sign == 1 else (f"-(x - {x0})^2" if x0 > 0 else f"-(x + {abs(x0)})^2"))
        else:
            d = y0 - a_sign * (x0**3)
            t1 = "x^3" if a_sign == 1 else "-x^3"
            c2 = -3 * a_sign * x0
            t2 = f"+ {c2}x^2" if c2 > 0 else (f"- {abs(c2)}x^2" if c2 < 0 else "")
            c3 = 3 * a_sign * (x0**2)
            t3 = f"+ {c3}x" if c3 > 0 else (f"- {abs(c3)}x" if c3 < 0 else "")
            t4 = f"+ {d}" if d > 0 else (f"- {abs(d)}" if d < 0 else "")
            f_true = f"y = {t1} {t2} {t3} {t4}".replace("  ", " ").strip()
            der_str = f"3(x - {x0})^2" if a_sign == 1 and x0 > 0 else (f"3(x + {abs(x0)})^2" if a_sign == 1 else (f"-3(x - {x0})^2" if x0 > 0 else f"-3(x + {abs(x0)})^2"))
            
        if a_sign > 0:
            line_str = "+,$0$,+,"
            var_str = f"\\tkzTabVar{{-/$-\\infty$,R/,+/$+\\infty$}}\n\t\\tkzTabVal{{1}}{{3}}{{0.5}}{{${x0}$}}{{${y0}$}}"
            chieu_str = "đồng biến"
        else:
            line_str = "-,$0$,-,"
            var_str = f"\\tkzTabVar{{+/$+\\infty$,R/,-/$-\\infty$}}\n\t\\tkzTabVal{{1}}{{3}}{{0.5}}{{${x0}$}}{{${y0}$}}"
            chieu_str = "nghịch biến"

        caudan = f"""\\immini{{Bảng biến thiên sau đây là của hàm số nào?}}
{{\\begin{{tikzpicture}}
\t\\tkzTabInit[nocadre,lgt=1.2,espcl=2.5,deltacl=0.6]
\t{{$x$ /0.6,$y\'$ /0.6,$y$ /2}}
\t{{$-\\infty$,${x0}$,$+\\infty$}}
\t\\tkzTabLine{{,{line_str}}}
\t{var_str}
\\end{{tikzpicture}}}}"""

        def clean_poly(s):
            return s.replace("+-", "- ").replace("--", "+ ").replace("+ -", "- ").replace("- -", "+ ").replace("  ", " ").strip()

        p2 = clean_poly(random.choice([
            f"y = -3x^2 + {y0}", 
            f"y = 2x^2 + {3*x0}x + {y0}", 
            f"y = -x^2 + 2x - 1", 
            f"y = 3x^2 + 1"
        ]))
        p4 = clean_poly(random.choice([
            f"y = x^4 + 3x^2 - 1", 
            f"y = -x^4 + 2x^2 + {y0}", 
            f"y = x^4 - 2x^2 + 1", 
            f"y = -2x^4 - x^2 + 3"
        ]))
        p3_wrong = clean_poly(random.choice([
            f"y = x^3 - {y0}", 
            f"y = -x^3 + {y0}", 
            f"y = x^3 + 3x - 1", 
            f"y = \\dfrac{{x^3}}{{3}} - x + {y0}"
        ]))
        
        loigiai = f"""Dựa vào bảng biến thiên ta có:
\\begin{{itemize}}
\t\\item Nhánh đồ thị đi từ $-\\infty$ lên $+\\infty$ (hoặc từ $+\\infty$ xuống $-\\infty$) và hàm số {chieu_str} trên $\\mathbb{{R}}$ nên đây là hàm số bậc ba với hệ số $a {'> 0' if a_sign > 0 else '< 0'}$. Loại các hàm số bậc hai và bậc bốn.
\t\\item Đạo hàm $y' = 0$ có nghiệm kép tại $x = {x0}$, tức là $y' = {der_str}$.
\t\\item Tại $x = {x0}$, giá trị của hàm số là $y({x0}) = {y0}$.
\t\\item Thử lại với hàm số ${f_true}$:\\\\
Ta có đạo hàm $y' = {der_str} {'\\ge 0' if a_sign > 0 else '\\le 0'}, \\forall x \\in \\mathbb{{R}}$ và $y({x0}) = {y0}$, hoàn toàn phù hợp với bảng biến thiên.
\\end{{itemize}}
Vậy hàm số cần tìm là ${f_true}$."""

    else:
        a_sign = 1 if random.random() < 0.75 else -1
        k = random.choice([1, 2, 3])
        d = random.choice([-3, -2, -1, 1, 2, 3])
        
        def fmt_sgn(v):
            return f"+ {v}" if v > 0 else f"- {abs(v)}"

        if a_sign > 0:
            f_true = f"y = x^3 + {3*k}x" if d == 0 else f"y = x^3 + {3*k}x {fmt_sgn(d)}".strip()
            line_str = "+,"
            var_str = "\\tkzTabVar{-/$-\\infty$,+/$+\\infty$}"
            chieu_str = "đồng biến"
            der_formula = f"3x^2 + {3*k} > 0, \\forall x \\in \\mathbb{{R}}"
        else:
            f_true = f"y = -x^3 - {3*k}x" if d == 0 else f"y = -x^3 - {3*k}x {fmt_sgn(d)}".strip()
            line_str = "-,"
            var_str = "\\tkzTabVar{+/$+\\infty$,-/$-\\infty$}"
            chieu_str = "nghịch biến"
            der_formula = f"-3x^2 - {3*k} < 0, \\forall x \\in \\mathbb{{R}}"

        caudan = f"""\\immini{{Bảng biến thiên sau đây là của hàm số nào?}}
{{\\begin{{tikzpicture}}
\t\\tkzTabInit[nocadre,lgt=1.2,espcl=2.5,deltacl=0.6]
\t{{$x$ /0.6,$y\'$ /0.6,$y$ /1.8}}
\t{{$-\\infty$,$+\\infty$}}
\t\\tkzTabLine{{,{line_str}}}
\t{var_str}
\\end{{tikzpicture}}}}"""

        p2 = random.choice([f"y = 2x^2 + 3x - 1", f"y = -x^2 + 2x + 1", f"y = 3x^2 + 2"])
        p4 = random.choice([f"y = x^4 + 2x^2 - 1", f"y = -x^4 + x^2 + 2", f"y = x^4 - 4x^2 + 3"])
        p3_wrong = f"y = -x^3 + {3*k}x + 1" if a_sign > 0 else f"y = x^3 - {3*k}x + 1"

        loigiai = f"""Dựa vào bảng biến thiên ta có:
\\begin{{itemize}}
\t\\item Nhánh đồ thị đi từ $-\\infty$ lên $+\\infty$ (hoặc ngược lại) và hàm số {chieu_str} trên $\\mathbb{{R}}$ nên đây là hàm số bậc ba với hệ số $a {'> 0' if a_sign > 0 else '< 0'}$. Do đó ta loại các hàm bậc hai và bậc bốn.
\t\\item Đạo hàm của hàm số không có nghiệm thực (luôn mang dấu {'dương' if a_sign > 0 else 'âm'} với mọi $x$).
\t\\item Xét hàm số ${f_true}$, ta có đạo hàm $y' = {der_formula}$, hoàn toàn phù hợp với bảng biến thiên đã cho.
\\end{{itemize}}
Vậy hàm số cần tìm là ${f_true}$."""

    dapan_a = f"{{\\True ${f_true}$}}\n"
    dapan_b = f"{{${p2}$}}\n"
    dapan_c = f"{{${p4}$}}\n"
    dapan_d = f"{{${p3_wrong}$}}\n"
    
    phuongan = [dapan_a, dapan_b, dapan_c, dapan_d]
    random.shuffle(phuongan)
    return caudan, phuongan, loigiai


# ==============================================================================
# 12. DẠNG: TIỆM CẬN XIÊN DẠNG TỔNG QUÁT ax + by + c = 0 (a > 0) CỦA HÀM BẬC 2/1
# ==============================================================================
def sinh_cau_tln_tiem_can_xien_tong_quat():
    """
    Sinh câu hỏi Trắc nghiệm Trả lời ngắn (TLN):
    Xác định tiệm cận xiên dạng tổng quát ax + by + c = 0 (a > 0, gcd(a, |b|, |c|) = 1)
    của hàm phân thức bậc 2 trên bậc nhất y = (Ax^2 + Bx + C) / (Dx + E).
    Tính giá trị biểu thức P (ví dụ: a - 5b, a + b, a + b + c, 2a - b,...).
    """
    import math

    def fmt_first_term(coef, var):
        if coef == 1: return var
        if coef == -1: return f"-{var}"
        return f"{coef}{var}"

    def fmt_signed(coef, var=""):
        if coef == 0: return ""
        sign = "+" if coef > 0 else "-"
        val = abs(coef)
        if var:
            val_str = "" if val == 1 else str(val)
            return f" {sign} {val_str}{var}"
        return f" {sign} {val}"

    # 1. Chọn D, E cho mẫu số Dx + E (D > 0)
    D = random.choice([1, 2, 3, 5])
    E = random.choice([-5, -4, -3, -2, -1, 1, 2, 3, 4, 5])
    while math.gcd(D, abs(E)) != 1:
        E = random.choice([-5, -4, -3, -2, -1, 1, 2, 3, 4, 5])

    # 2. Chọn thương mx + n
    m = random.choice([1, 2, -1, -2]) if D == 1 else random.choice([1, -1])
    n = random.choice([-4, -3, -2, -1, 1, 2, 3, 4])
    
    # 3. Phần dư R khác 0
    R = random.choice([-5, -4, -3, -2, -1, 1, 2, 3, 4, 5])
    
    # Tử số: (Dx + E)(mx + n) + R = D*m x^2 + (D*n + E*m) x + (E*n + R)
    A = D * m
    B = D * n + E * m
    C = E * n + R

    # Chuỗi hiển thị hàm số
    num_str = f"{fmt_first_term(A, 'x^2')}{fmt_signed(B, 'x')}{fmt_signed(C)}".strip()
    den_str = f"{fmt_first_term(D, 'x')}{fmt_signed(E)}".strip()
    lin_str = f"{fmt_first_term(m, 'x')}{fmt_signed(n)}".strip()

    # Phương trình tiệm cận xiên dạng tổng quát ax + by + c = 0 (a > 0, gcd=1)
    if m > 0:
        a_val = m
        b_val = -1
        c_val = n
    else:
        a_val = -m
        b_val = 1
        c_val = -n

    g = math.gcd(math.gcd(a_val, abs(b_val)), abs(c_val))
    a_val //= g
    b_val //= g
    c_val //= g

    line_pt = f"{fmt_first_term(a_val, 'x')}{fmt_signed(b_val, 'y')}{fmt_signed(c_val)} = 0".strip()

    # Chọn câu hỏi biểu thức
    forms = [
        ("a - 5b", a_val - 5 * b_val, f"a - 5b = {a_val} - 5\\cdot({b_val}) = {a_val - 5*b_val}"),
        ("a + b", a_val + b_val, f"a + b = {a_val} + ({b_val}) = {a_val + b_val}"),
        ("a + b + c", a_val + b_val + c_val, f"a + b + c = {a_val} + ({b_val}) + ({c_val}) = {a_val + b_val + c_val}"),
        ("2a - b", 2 * a_val - b_val, f"2a - b = 2\\cdot({a_val}) - ({b_val}) = {2*a_val - b_val}"),
        ("a - 2b", a_val - 2 * b_val, f"a - 2b = {a_val} - 2\\cdot({b_val}) = {a_val - 2*b_val}"),
        ("a + 2b - c", a_val + 2 * b_val - c_val, f"a + 2b - c = {a_val} + 2\\cdot({b_val}) - ({c_val}) = {a_val + 2*b_val - c_val}"),
    ]
    expr_name, ans_val, expr_calc = random.choice(forms)

    rem_tex = f"+ \\dfrac{{{R}}}{{{den_str}}}" if R > 0 else f"- \\dfrac{{{abs(R)}}}{{{den_str}}}"
    rem_limit_tex = f"\\dfrac{{{R}}}{{{den_str}}}"

    caudan = f"Biết đồ thị hàm số $y = \\dfrac{{{num_str}}}{{{den_str}}}$ nhận đường thẳng $ax + by + c = 0$ ($a > 0$, $a, b, c$ là các số nguyên tối giản) làm đường tiệm cận xiên. Tính ${expr_name}$."
    loigiai = f"""Thực hiện phép chia đa thức tử cho mẫu, ta có:
$$y = \\dfrac{{{num_str}}}{{{den_str}}} = {lin_str} {rem_tex}.$$
Vì $\\lim\\limits_{{x \\to \\pm\\infty}} \\left[ y - ({lin_str}) \\right] = \\lim\\limits_{{x \\to \\pm\\infty}} \\left({rem_limit_tex}\\right) = 0$ nên đồ thị hàm số nhận đường thẳng $y = {lin_str}$ làm đường tiệm cận xiên.\\\\
Chuyển phương trình đường tiệm cận xiên về dạng tổng quát với $a > 0$:
$${line_pt}.$$
Do đó $a = {a_val}$, $b = {b_val}$, $c = {c_val}$ (các hệ số nguyên tối giản).\\\\
Vậy ${expr_calc}$."""

    dapan = str(ans_val)
    return caudan, loigiai, dapan


# ==============================================================================
# 13. DẠNG: KHOẢNG CÁCH GIỮA HAI ĐIỂM CỰC TRỊ CỦA HÀM SỐ BẬC HAI TRÊN BẬC NHẤT (2/1)
# ==============================================================================
def sinh_cau_tln_khoang_cach_hai_cuc_tri_2_1():
    """
    Sinh câu hỏi Trắc nghiệm Trả lời ngắn (TLN):
    Cho hàm số phân thức bậc hai trên bậc nhất y = (Ax^2 + Bx + C) / (Dx + E).
    Biết đồ thị hàm số có hai điểm cực trị A và B.
    Tính khoảng cách giữa hai điểm cực trị A và B (hoặc bình phương khoảng cách AB^2).
    """
    import math
    import random

    def fmt_coef(c, var, is_lead=False):
        if c == 0: return ""
        if is_lead:
            if c == 1: return var
            if c == -1: return f"-{var}"
            return f"{c}{var}"
        else:
            sgn = "+" if c > 0 else "-"
            ac = abs(c)
            term = var if ac == 1 else f"{ac}{var}"
            return f" {sgn} {term}"

    def fmt_num(c):
        if c == 0: return ""
        sgn = "+" if c > 0 else "-"
        return f" {sgn} {abs(c)}"

    mode = random.choice(["rounded_dist", "squared_dist", "integer_dist"])

    def fmt_binom_sq(val):
        if val == 0: return "x^2"
        if val > 0: return f"(x - {val})^2"
        return f"(x + {abs(val)})^2"

    if mode == "integer_dist":
        sign_A = random.choice([1, -1])
        x0 = random.choice([-2, -1, 0, 1, 2, 3])
        k = random.choice([1, 2])
        A = 2 * sign_A
        D = 3
        M_int = random.choice([-3, -2, -1, 0, 1, 2, 3])
        R = 9 * (k ** 2) * A

        coef_u2 = A
        coef_u1 = 3 * M_int - 2 * A * x0
        coef_u0 = A * (x0 ** 2) - 3 * M_int * x0 + R

        coef_v1 = 3
        coef_v0 = -3 * x0

        x1 = x0 - 3 * k
        x2 = x0 + 3 * k
        y1 = -4 * sign_A * k + M_int
        y2 = 4 * sign_A * k + M_int

        if x1 > x2:
            x1, x2 = x2, x1
            y1, y2 = y2, y1

        AB = 10 * k
        dapan = str(AB)

        num_str = fmt_coef(coef_u2, "x^2", True) + fmt_coef(coef_u1, "x") + fmt_num(coef_u0)
        den_str = fmt_coef(coef_v1, "x", True) + fmt_num(coef_v0)

        der_a = 6 * sign_A
        der_b = -12 * sign_A * x0
        der_c = 6 * sign_A * (x0 ** 2 - 9 * (k ** 2))
        der_num_str = fmt_coef(der_a, "x^2", True) + fmt_coef(der_b, "x") + fmt_num(der_c)

        m_str = "\\dfrac{4}{3}" if sign_A > 0 else "-\\dfrac{4}{3}"
        n_val = 3 * M_int - 2 * A * x0
        n_str = f"+ \\dfrac{{{n_val}}}{{3}}" if n_val > 0 else (f"- \\dfrac{{{abs(n_val)}}}{{3}}" if n_val < 0 else "")

        caudan = f"Cho hàm số $y = \\dfrac{{{num_str}}}{{{den_str}}}$. Biết đồ thị hàm số có hai điểm cực trị $A$ và $B$. Tính khoảng cách giữa hai điểm cực trị $A$ và $B$."

        dx_sq = (x2 - x1) ** 2
        dy_sq = (y2 - y1) ** 2
        d_sum = dx_sq + dy_sq

        loigiai = f"""Tập xác định: $D = \\mathbb{{R}} \\setminus \\{{{x0}\\}}.$ \\\\
Ta có đạo hàm:
$$y' = \\dfrac{{({fmt_coef(2*A, 'x', True)} {fmt_num(coef_u1)})({den_str}) - 3({num_str})}}{{({den_str})^2}} = \\dfrac{{{der_num_str}}}{{({den_str})^2}}.$$
Cho $y' = 0 \\iff {der_num_str} = 0 \\iff {fmt_binom_sq(x0)} = {9 * k**2} \\iff \\hoac{{x = {x1} \\\\ x = {x2}.}}$ \\\\
Đường thẳng đi qua hai điểm cực trị có phương trình:
$$y = \\dfrac{{u'(x)}}{{v'(x)}} = {m_str}x {n_str}.$$
Tọa độ hai điểm cực trị của đồ thị hàm số là:
$$A({x1}; {y1}), \\quad B({x2}; {y2}).$$
Khoảng cách giữa hai điểm cực trị $A$ và $B$ là:
$$AB = \\sqrt{{(x_B - x_A)^2 + (y_B - y_A)^2}} = \\sqrt{{({x2} - ({x1}))^2 + ({y2} - ({y1}))^2}} = \\sqrt{{{dx_sq} + {dy_sq}}} = \\sqrt{{{d_sum}}} = {dapan}.$$"""

    elif mode == "squared_dist":
        A = random.choice([1, -1])
        x0 = random.choice([-3, -2, -1, 1, 2, 3])
        k = random.choice([1, 2, 3])
        M = random.choice([-3, -2, -1, 0, 1, 2, 3])
        R = A * (k ** 2)
        B = M - 2 * A * x0
        C = A * (x0 ** 2) - M * x0 + R
        x1, x2 = x0 - k, x0 + k
        y1 = -2 * A * k + M
        y2 = 2 * A * k + M

        if x1 > x2:
            x1, x2 = x2, x1
            y1, y2 = y2, y1

        dx_sq = (x2 - x1) ** 2
        dy_sq = (y2 - y1) ** 2
        AB_sq = dx_sq + dy_sq
        dapan = str(AB_sq)

        num_str = fmt_coef(A, "x^2", True) + fmt_coef(B, "x") + fmt_num(C)
        den_str = "x" + fmt_num(-x0)

        caudan = f"Cho hàm số $y = \\dfrac{{{num_str}}}{{{den_str}}}$. Biết đồ thị hàm số có hai điểm cực trị là $A$ và $B$. Tính bình phương khoảng cách giữa hai điểm cực trị của đồ thị hàm số (tức tính $AB^2$)."

        line_m = 2 * A
        line_m_str = "2x" if line_m == 2 else "-2x"
        line_b_str = fmt_num(B)

        loigiai = f"""Tập xác định: $D = \\mathbb{{R}} \\setminus \\{{{x0}\\}}.$ \\\\
Ta có đạo hàm:
$$y' = \\dfrac{{({fmt_coef(2*A, 'x', True)} {fmt_num(B)})({den_str}) - ({num_str})}}{{({den_str})^2}} = \\dfrac{{{fmt_coef(A, fmt_binom_sq(x0), True)} - ({R})}}{{({den_str})^2}}.$$
Cho $y' = 0 \\iff {fmt_binom_sq(x0)} = {k**2} \\iff \\hoac{{x = {x1} \\\\ x = {x2}.}}$ \\\\
Đường thẳng đi qua hai điểm cực trị có phương trình $y = \\dfrac{{u'(x)}}{{v'(x)}} = {line_m_str}{line_b_str}.$ \\\\
Tọa độ hai điểm cực trị của đồ thị hàm số là:
$$A({x1}; {y1}), \\quad B({x2}; {y2}).$$
Bình phương khoảng cách giữa hai điểm cực trị là:
$$AB^2 = (x_B - x_A)^2 + (y_B - y_A)^2 = ({x2} - ({x1}))^2 + ({y2} - ({y1}))^2 = {dx_sq} + {dy_sq} = {dapan}.$$"""

    else:
        A = random.choice([1, -1])
        x0 = random.choice([-3, -2, -1, 1, 2, 3])
        k = random.choice([1, 2, 3])
        M = random.choice([-3, -2, -1, 0, 1, 2, 3])
        R = A * (k ** 2)
        B = M - 2 * A * x0
        C = A * (x0 ** 2) - M * x0 + R
        x1, x2 = x0 - k, x0 + k
        y1 = -2 * A * k + M
        y2 = 2 * A * k + M

        if x1 > x2:
            x1, x2 = x2, x1
            y1, y2 = y2, y1

        AB_val = math.sqrt((x2 - x1) ** 2 + (y2 - y1) ** 2)
        AB_sq = (x2 - x1) ** 2 + (y2 - y1) ** 2
        dapan = str(round(AB_val, 1)).replace(".", ",")

        num_str = fmt_coef(A, "x^2", True) + fmt_coef(B, "x") + fmt_num(C)
        den_str = "x" + fmt_num(-x0)

        caudan = f"Cho hàm số $y = \\dfrac{{{num_str}}}{{{den_str}}}$. Biết đồ thị hàm số có hai điểm cực trị là $A$ và $B$. Tính khoảng cách giữa hai điểm cực trị $A$ và $B$ (kết quả làm tròn đến hàng phần mười)."

        line_m = 2 * A
        line_m_str = "2x" if line_m == 2 else "-2x"
        line_b_str = fmt_num(B)

        loigiai = f"""Tập xác định: $D = \\mathbb{{R}} \\setminus \\{{{x0}\\}}.$ \\\\
Ta có đạo hàm:
$$y' = \\dfrac{{({fmt_coef(2*A, 'x', True)} {fmt_num(B)})({den_str}) - ({num_str})}}{{({den_str})^2}} = \\dfrac{{{fmt_coef(A, fmt_binom_sq(x0), True)} - ({R})}}{{({den_str})^2}}.$$
Cho $y' = 0 \\iff {fmt_binom_sq(x0)} = {k**2} \\iff \\hoac{{x = {x1} \\\\ x = {x2}.}}$ \\\\
Đường thẳng đi qua hai điểm cực trị có phương trình $y = \\dfrac{{u'(x)}}{{v'(x)}} = {line_m_str}{line_b_str}.$ \\\\
Tọa độ hai điểm cực trị của đồ thị hàm số là:
$$A({x1}; {y1}), \\quad B({x2}; {y2}).$$
Khoảng cách giữa hai điểm cực trị là:
$$AB = \\sqrt{{(x_B - x_A)^2 + (y_B - y_A)^2}} = \\sqrt{{({x2} - ({x1}))^2 + ({y2} - ({y1}))^2}} = \\sqrt{{{AB_sq}}} \\approx {dapan}.$$"""

    return caudan, loigiai, dapan


def sinh_cau_mc_khoang_cach_hai_cuc_tri_2_1():
    """
    Sinh câu hỏi Trắc nghiệm 4 lựa chọn (MC):
    Khoảng cách giữa hai điểm cực trị của hàm phân thức bậc 2 trên bậc nhất.
    """
    caudan, loigiai, dapan = sinh_cau_tln_khoang_cach_hai_cuc_tri_2_1()
    if "," in dapan:
        val = float(dapan.replace(",", "."))
        wrongs = [f"{round(val + d, 1)}".replace(".", ",") for d in [-1.2, 1.5, 2.8, -2.1, 3.2] if round(val + d, 1) > 0][:3]
        correct_tex = f"${dapan}$"
        wrong_texs = [f"${w}$" for w in wrongs]
    else:
        val = int(dapan)
        wrongs = [str(val + d) for d in [-4, 5, 8, -6, 12] if val + d > 0][:3]
        correct_tex = f"${dapan}$"
        wrong_texs = [f"${w}$" for w in wrongs]

    phuongan = [f"{{\\True {correct_tex}}}\n"] + [f"{{{w}}}\n" for w in wrong_texs]
    random.shuffle(phuongan)
    return caudan, phuongan, loigiai


