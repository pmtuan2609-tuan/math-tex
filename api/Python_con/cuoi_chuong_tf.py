# -*- coding: utf-8 -*-
import random
import math
from fractions import Fraction

def clean_option(s):
    if not isinstance(s, str):
        s = str(s)
    s = s.strip()
    for pfx in ['a)', 'b)', 'c)', 'd)', 'A.', 'B.', 'C.', 'D.', 'a.', 'b.', 'c.', 'd.']:
        if s.startswith(pfx):
            s = s[len(pfx):].strip()
    while s.endswith('.'):
        s = s[:-1].strip()
    return s


def make_tf_choices(items_data):
    """
    items_data: danh sách 4 tuple (true_text, false_text, true_expl, false_expl)
    Sinh ngẫu nhiên tính Đúng/Sai cho từng ý (có thể lần 1 đúng, lần 2 sai)
    Trả về (choices, loi_giai)
    """
    flags = [random.choice([True, False]) for _ in range(4)]
    if all(flags):
        flags[random.randint(0, 3)] = False
    elif not any(flags):
        flags[random.randint(0, 3)] = True

    labels = ['a', 'b', 'c', 'd']
    choices = []
    expl_lines = []

    for i in range(4):
        t_text, f_text, t_expl, f_expl = items_data[i]
        lbl = labels[i]
        t_clean = clean_option(t_text)
        f_clean = clean_option(f_text)
        if flags[i]:
            choices.append(fr'''{{\True {t_clean}}}
''')
            expl_lines.append(fr'''  \item {t_expl.strip()} (Ý {lbl} \textbf{{Đúng}})''')
        else:
            choices.append(fr'''{{{f_clean}}}
''')
            expl_lines.append(fr'''  \item {f_expl.strip()} (Ý {lbl} \textbf{{Sai}})''')

    loi_giai = "\\begin{itemize}\n" + "\n".join(expl_lines) + "\n\\end{itemize}"
    return choices, loi_giai


# ==============================================================================
# CHƯƠNG I: ĐÚNG - SAI (16 CÂU)
# ==============================================================================

def CuoiChuong1_TF_Cau1():
    # Khảo sát hàm số bậc ba y = x^3 - 3k^2 x + c
    k = random.choice([1, 2])
    c = random.randint(-3, 3)
    k2_3 = 3 * k * k
    y_cd = 2 * (k**3) + c
    y_ct = -2 * (k**3) + c
    
    # Đoạn [-k, M]
    M = k + random.choice([2, 3])
    max_val = M**3 - k2_3 * M + c
    
    # Tam giác ABC với C(-k, y_cd - h)
    h = random.randint(1, 3)
    y_C = y_cd - h
    dt_tamgiac = k * h

    sign_k2 = f"- {k2_3}x" if k2_3 > 0 else ""
    sign_c = f" + {c}" if c > 0 else (f" - {abs(c)}" if c < 0 else "")
    caudan = fr'''Cho hàm số $y = x^3 {sign_k2}{sign_c}$.'''

    items = [
        (
            fr'''Điểm cực tiểu của hàm số là $x = {k}$.''',
            fr'''Điểm cực tiểu của hàm số là $x = {-k}$.''',
            fr'''$y' = 3x^2 - {k2_3} = 0 \iff x = \pm {k}$; $y''({k}) = 6({k}) > 0 \implies x = {k}$ là điểm cực tiểu.''',
            fr'''$y' = 3x^2 - {k2_3} = 0 \iff x = \pm {k}$; $x = {-k}$ là điểm cực đại, điểm cực tiểu là $x = {k}$.'''
        ),
        (
            fr'''Hàm số nghịch biến trên khoảng $(-{k}; {k})$.''',
            fr'''Hàm số đồng biến trên khoảng $(-{k}; {k})$.''',
            fr'''Trên khoảng $(-{k}; {k})$, $y' < 0$ nên hàm số nghịch biến.''',
            fr'''Trên khoảng $(-{k}; {k})$, $y' < 0$ nên hàm số nghịch biến, khẳng định đồng biến là sai.'''
        ),
        (
            fr'''Giá trị lớn nhất của hàm số đã cho trên đoạn $[- {k}; {M}]$ là ${max_val}$.''',
            fr'''Giá trị lớn nhất của hàm số đã cho trên đoạn $[- {k}; {M}]$ là ${max_val + random.choice([5, 10])}$.''',
            fr'''Ta có $y(-{k}) = {y_cd}$, $y({k}) = {y_ct}$, $y({M}) = {max_val} \implies \max\limits_{{[-{k}; {M}]}} y = {max_val}$.''',
            fr'''Ta có $y(-{k}) = {y_cd}$, $y({k}) = {y_ct}$, $y({M}) = {max_val} \implies \max\limits_{{[-{k}; {M}]}} y = {max_val} \neq {max_val + 5}$.'''
        ),
        (
            fr'''Gọi $A, B$ lần lượt là điểm cực đại và điểm cực tiểu của đồ thị hàm số. Khi đó, diện tích tam giác $ABC$ bằng ${dt_tamgiac}$ với $C(-{k}; {y_C})$.''',
            fr'''Gọi $A, B$ lần lượt là điểm cực đại và điểm cực tiểu của đồ thị hàm số. Khi đó, diện tích tam giác $ABC$ bằng ${dt_tamgiac + random.choice([2, 4])}$ với $C(-{k}; {y_C})$.''',
            fr'''$A(-{k}; {y_cd}), B({k}; {y_ct}), C(-{k}; {y_C})$. Độ dài $AC = {h}$, khoảng cách $d(B, AC) = 2({k}) = {2*k} \implies S_{{ABC}} = \dfrac{{1}}{{2}} \cdot {h} \cdot {2*k} = {dt_tamgiac}$.''',
            fr'''$A(-{k}; {y_cd}), B({k}; {y_ct}), C(-{k}; {y_C})$. Đoạn $AC = {h}$, đường cao $h_B = {2*k} \implies S_{{ABC}} = {dt_tamgiac} \neq {dt_tamgiac + 2}$.'''
        )
    ]
    choices, loi_giai = make_tf_choices(items)
    return caudan, choices, loi_giai


def CuoiChuong1_TF_Cau2():
    # Tối ưu hóa lợi nhuận bán hàng
    c_in = random.choice([14, 16, 18])  # nghìn đồng
    q0 = 100
    k_step = 10
    p0 = c_in + random.choice([12, 14])  # nghìn đồng
    
    ln0 = (p0 - c_in) * q0 * 1000
    p1 = p0 - random.choice([6, 8])
    q1 = q0 + k_step * (p0 - p1)
    
    x_opt = int((p0 + c_in + q0 // k_step) / 2)
    max_ln = (x_opt - c_in) * (q0 + k_step * (p0 - x_opt)) * 1000
    q_const = q0 + k_step * p0

    caudan = fr'''Một cửa hàng bán nông sản với giá bán là ${p0 * 1000}$ đồng/1kg. Giá nhập vào là ${c_in * 1000}$ đồng/1kg. Với giá này cửa hàng ước chừng bán được ${q0}$ kg/ngày. Cửa hàng dự định giảm giá bán, ước tính cứ giảm $1000$ đồng/1kg thì số lượng bán được sẽ tăng thêm là ${k_step}$ kg/ngày.'''

    items = [
        (
            fr'''Nếu giữ nguyên giá ban đầu, lợi nhuận theo ngày của cửa hàng là ${ln0}$ đồng.''',
            fr'''Nếu giữ nguyên giá ban đầu, lợi nhuận theo ngày của cửa hàng là ${ln0 + 200000}$ đồng.''',
            fr'''Lợi nhuận ban đầu: $({p0 * 1000} - {c_in * 1000}) \times {q0} = {ln0}$ đồng/ngày.''',
            fr'''Lợi nhuận ban đầu là $({p0 * 1000} - {c_in * 1000}) \times {q0} = {ln0}$ đồng/ngày, không phải ${ln0 + 200000}$ đồng.'''
        ),
        (
            fr'''Nếu giá bán là ${p1 * 1000}$ đồng/1kg, cửa hàng bán được ${q1}$ kg/ngày.''',
            fr'''Nếu giá bán là ${p1 * 1000}$ đồng/1kg, cửa hàng bán được ${q1 + 50}$ kg/ngày.''',
            fr'''Giá giảm ${p0 - p1}$ nghìn đồng $\implies$ lượng bán tăng ${k_step} \times {p0 - p1} = {k_step * (p0 - p1)}$ kg $\implies$ tổng bán ${q0} + {k_step * (p0 - p1)} = {q1}$ kg/ngày.''',
            fr'''Giá giảm ${p0 - p1}$ nghìn đồng $\implies$ lượng bán là ${q1}$ kg/ngày $\neq {q1 + 50}$ kg/ngày.'''
        ),
        (
            fr'''Gọi $x$ (nghìn đồng) là giá tiền mà cửa hàng dự định bán (${c_in} < x < {p0}$), khi đó lợi nhuận theo ngày của cửa hàng là hàm số $f(x) = (x - {c_in})({q_const} - {k_step}x)$.''',
            fr'''Gọi $x$ (nghìn đồng) là giá tiền mà cửa hàng dự định bán (${c_in} < x < {p0}$), khi đó lợi nhuận theo ngày của cửa hàng là hàm số $f(x) = (x - {c_in})({q_const + 50} - {k_step}x)$.''',
            fr'''Khi bán giá $x$ (nghìn đồng), số lượng bán là ${q0} + {k_step}({p0} - x) = {q_const} - {k_step}x$. Lợi nhuận $f(x) = (x - {c_in})({q_const} - {k_step}x)$.''',
            fr'''Lợi nhuận đúng là $f(x) = (x - {c_in})({q_const} - {k_step}x)$ nghìn đồng.'''
        ),
        (
            fr'''Lợi nhuận tối đa theo ngày của cửa hàng là ${max_ln}$ đồng.''',
            fr'''Lợi nhuận tối đa theo ngày của cửa hàng là ${max_ln + 160000}$ đồng.''',
            fr'''$f(x) = -{k_step}(x - {c_in})(x - {q_const // k_step})$ đạt cực đại tại $x = {x_opt}$ với lợi nhuận tối đa $f({x_opt}) = {max_ln // 1000}$ nghìn đồng $= {max_ln}$ đồng.''',
            fr'''Lợi nhuận tối đa đạt được tại $x = {x_opt}$ là ${max_ln}$ đồng $\neq {max_ln + 160000}$ đồng.'''
        )
    ]
    choices, loi_giai = make_tf_choices(items)
    return caudan, choices, loi_giai


def CuoiChuong1_TF_Cau3():
    # BBT hàm phân thức
    x0 = random.choice([1, 2, 3])
    y0 = random.choice([-2, -1, 1, 2])
    k1 = random.choice([2, 3])
    k2 = random.choice([1, 3])
    lim_val = k1 * y0 - k2
    
    a1 = x0 - 4
    a2 = x0 - 1

    caudan = fr'''\immini{{Cho hàm số $y=f(x)$ có bảng biến thiên như hình bên. Hãy cho biết tính đúng sai của mỗi khẳng định sau:}}
{{\begin{{tikzpicture}}
	\tkzTabInit[nocadre,lgt=1.2,espcl=2.2,deltacl=0.5]
	{{$x$/0.6, $y'$/0.6, $y$/1.4}}
	{{$-\infty$, ${x0}$, $+\infty$}}
	\tkzTabLine{{,+,d,+,}}
	\tkzTabVar{{-/ ${y0}$, +D-/$+\infty$/$-\infty$, +/${y0}$}}
\end{{tikzpicture}}}}'''

    items = [
        (
            fr'''Hàm số đã cho đồng biến trên từng khoảng $(-\infty; {x0})$ và $({x0}; +\infty)$.''',
            fr'''Hàm số đã cho đồng biến trên $\mathbb{{R}}$.''',
            fr'''Hàm số có $y' > 0$ trên $(-\infty; {x0})$ và $({x0}; +\infty)$ nên đồng biến trên mỗi khoảng đó.''',
            fr'''Hàm số không xác định tại $x = {x0}$ nên không đồng biến trên $\mathbb{{R}}$.'''
        ),
        (
            fr'''$\lim\limits_{{x\to -\infty}} \left[ {k1}f(x)-{k2} \right]={lim_val}$.''',
            fr'''$\lim\limits_{{x\to -\infty}} \left[ {k1}f(x)-{k2} \right]={lim_val + 2}$.''',
            fr'''$\lim\limits_{{x \to -\infty}} f(x) = {y0} \implies \lim\limits_{{x \to -\infty}} [{k1}f(x) - {k2}] = {k1}({y0}) - {k2} = {lim_val}$.''',
            fr'''$\lim\limits_{{x \to -\infty}} f(x) = {y0} \implies \lim\limits_{{x \to -\infty}} [{k1}f(x) - {k2}] = {lim_val} \neq {lim_val + 2}$.'''
        ),
        (
            fr'''Đồ thị hàm số đã cho có tiệm cận ngang là đường thẳng $y={y0}$.''',
            fr'''Đồ thị hàm số đã cho có tiệm cận ngang là đường thẳng $x={y0}$.''',
            fr'''Vì $\lim\limits_{{x \to \pm\infty}} f(x) = {y0}$ nên tiệm cận ngang là đường thẳng $y = {y0}$.''',
            fr'''Tiệm cận ngang là đường thẳng $y = {y0}$, không phải $x = {y0}$.'''
        ),
        (
            fr'''Giá trị lớn nhất của hàm số đã cho trên đoạn $[{a1};{a2}]$ là $f({a2})$.''',
            fr'''Giá trị lớn nhất của hàm số đã cho trên đoạn $[{a1};{a2}]$ là $f({a1})$.''',
            fr'''Hàm số đồng biến trên $(-\infty; {x0})$ nên trên $[{a1}; {a2}]$ đạt GTLN tại $x = {a2}$.''',
            fr'''Hàm số đồng biến trên $[{a1}; {a2}]$ nên GTLN là $f({a2})$, không phải $f({a1})$.'''
        )
    ]
    choices, loi_giai = make_tf_choices(items)
    return caudan, choices, loi_giai


def CuoiChuong1_TF_Cau4():
    # Khảo sát hàm số y = x^3 - 3k^2 x + c
    k = random.choice([1, 2])
    c = random.choice([2, 3, 4])
    k2_3 = 3 * k * k
    y_max = 2 * (k**3) + c
    
    sign_k2 = f"- {k2_3}x"
    caudan = fr'''Cho hàm số $y = x^3 {sign_k2} + {c}$.'''

    items = [
        (
            fr'''Tập xác định của hàm số là $D = \mathbb{{R}}$.''',
            fr'''Tập xác định của hàm số là $D = \mathbb{{R}} \setminus \{{{k}\}}$.''',
            fr'''Hàm số đa thức bậc ba luôn có tập xác định $D = \mathbb{{R}}$.''',
            fr'''Hàm số đa thức bậc ba xác định trên toàn bộ $\mathbb{{R}}$.'''
        ),
        (
            fr'''Giá trị lớn nhất của hàm số trên đoạn $[- {k+1}; {k+1}]$ bằng ${y_max}$.''',
            fr'''Giá trị lớn nhất của hàm số trên đoạn $[- {k+1}; {k+1}]$ bằng ${y_max + 3}$.''',
            fr'''$y' = 3x^2 - {k2_3} = 0 \iff x = \pm {k}$. Ta có $y(-{k}) = {y_max}, y({k}) = {-2*(k**3)+c}, y({k+1}) \le {y_max} \implies \max = {y_max}$.''',
            fr'''Giá trị lớn nhất của hàm số trên đoạn $[- {k+1}; {k+1}]$ là ${y_max} \neq {y_max + 3}$.'''
        ),
        (
            fr'''Đạo hàm của hàm số là $y' = 3x^2 - {k2_3}$.''',
            fr'''Đạo hàm của hàm số là $y' = 3x^2 - {k2_3}x$.''',
            fr'''$(x^3 - {k2_3}x + {c})' = 3x^2 - {k2_3}$.''',
            fr'''Đạo hàm đúng là $y' = 3x^2 - {k2_3} \neq 3x^2 - {k2_3}x$.'''
        ),
        (
            fr'''Hàm số đạt cực đại tại $x = -{k}$.''',
            fr'''Hàm số đạt cực đại tại $x = {k}$.''',
            fr'''$y''(-{k}) = -6({k}) < 0 \implies x = -{k}$ là điểm cực đại.''',
            fr'''$y''({k}) = 6({k}) > 0 \implies x = {k}$ là điểm cực tiểu, cực đại là $x = -{k}$.'''
        )
    ]
    choices, loi_giai = make_tf_choices(items)
    return caudan, choices, loi_giai


def CuoiChuong1_TF_Cau5():
    # Khảo sát hàm phân thức y = (-x^2 - bx + c)/(x - x0)
    x0 = random.choice([2, 3])
    u = 1
    v = -x0 - 1
    b_val = -(u + v)
    c_val = -u * v
    tcx_b = -(b_val + x0)
    y_I = -x0 + tcx_b

    caudan = fr'''Cho hàm số $y = \dfrac{{-x^2 - {b_val}x + {c_val}}}{{x - {x0}}}$ có đồ thị là $(C)$.'''

    items = [
        (
            fr'''$(C)$ cắt trục hoành tại hai điểm phân biệt.''',
            fr'''$(C)$ không cắt trục hoành.''',
            fr'''Phương trình tử số $-x^2 - {b_val}x + {c_val} = 0$ có hai nghiệm phân biệt $x = {u}$ và $x = {v}$ (khác ${x0}$) nên đồ thị cắt trục hoành tại hai điểm phân biệt.''',
            fr'''Phương trình tử số có hai nghiệm phân biệt $x = {u}$ và $x = {v}$ khác ${x0}$ nên $(C)$ cắt trục hoành tại $2$ điểm phân biệt.'''
        ),
        (
            fr'''$(C)$ nhận điểm $I({x0}; {y_I})$ là tâm đối xứng.''',
            fr'''$(C)$ nhận điểm $I({x0}; {y_I + 4})$ là tâm đối xứng.''',
            fr'''Tọa độ tâm đối xứng là giao điểm của hai đường tiệm cận $x = {x0}$ và $y = -x + {tcx_b} \implies I({x0}; {y_I})$.''',
            fr'''Tâm đối xứng là giao của tiệm cận đứng $x = {x0}$ và tiệm cận xiên $y = -x + {tcx_b} \implies I({x0}; {y_I}) \neq I({x0}; {y_I + 4})$.'''
        ),
        (
            fr'''Phương trình đường tiệm cận đứng của $(C)$ là $x={x0}$.''',
            fr'''Phương trình đường tiệm cận đứng của $(C)$ là $y={x0}$.''',
            fr'''Mẫu số bằng $0$ khi $x = {x0}$ và tử số khác $0$ nên tiệm cận đứng là $x = {x0}$.''',
            fr'''Tiệm cận đứng là đường thẳng $x = {x0}$, không phải $y = {x0}$.'''
        ),
        (
            fr'''Phương trình đường tiệm cận xiên của $(C)$ là $y=-x{"+" if tcx_b >= 0 else ""}{tcx_b}$.''',
            fr'''Phương trình đường tiệm cận xiên của $(C)$ là $y=-x{"+" if -tcx_b >= 0 else ""}{-tcx_b}$.''',
            fr'''Chia đa thức ta được $y = -x + {tcx_b} + \dfrac{{R}}{{x - {x0}}} \implies$ tiệm cận xiên là $y = -x + {tcx_b}$.''',
            fr'''Tiệm cận xiên đúng là $y = -x + {tcx_b}$, khẳng định đã cho bị sai dấu hệ số tự do.'''
        )
    ]
    choices, loi_giai = make_tf_choices(items)
    return caudan, choices, loi_giai


def CuoiChuong1_TF_Cau6():
    # Chuyển động s(t) = 1/3 t^3 - k^2 t + s0
    k = random.choice([6, 8, 10])
    k2 = k * k
    s0 = random.randint(5, 15)
    t_test = k + 5
    v_test = t_test**2 - k2

    caudan = fr'''Một chất điểm chuyển động theo phương trình $s(t) = \dfrac{{1}}{{3}}t^3 - {k2}t + {s0}$, trong đó $t$ tính bằng giây ($t \ge 0$), $s(t)$ tính bằng mét. Hãy cho biết tính đúng sai của các khẳng định sau:'''

    items = [
        (
            fr'''Gia tốc tại thời điểm chất điểm đạt vận tốc bị triệt tiêu bằng ${2 * k}\text{{ m/s}}^2$.''',
            fr'''Gia tốc tại thời điểm chất điểm đạt vận tốc bị triệt tiêu bằng ${2 * k + 4}\text{{ m/s}}^2$.''',
            fr'''Vận tốc bị triệt tiêu: $v(t) = s'(t) = t^2 - {k2} = 0 \iff t = {k}$ (s). Khi đó gia tốc $a({k}) = 2({k}) = {2 * k}\text{{ m/s}}^2$.''',
            fr'''$v(t) = 0 \iff t = {k}\text{{ s}} \implies a({k}) = 2({k}) = {2 * k}\text{{ m/s}}^2 \neq {2 * k + 4}\text{{ m/s}}^2$.'''
        ),
        (
            fr'''Gia tốc của chất điểm tại thời điểm $t = 2\text{{ s}}$ là $4\text{{ m/s}}^2$.''',
            fr'''Gia tốc của chất điểm tại thời điểm $t = 2\text{{ s}}$ là $8\text{{ m/s}}^2$.''',
            fr'''Gia tốc $a(t) = s''(t) = 2t \implies a(2) = 4\text{{ m/s}}^2$.''',
            fr'''$a(t) = 2t \implies a(2) = 4\text{{ m/s}}^2 \neq 8\text{{ m/s}}^2$.'''
        ),
        (
            fr'''Vận tốc của chất điểm tại thời điểm $t={t_test}\text{{ s}}$ là ${v_test}\text{{ m/s}}$.''',
            fr'''Vận tốc của chất điểm tại thời điểm $t={t_test}\text{{ s}}$ là ${v_test + 20}\text{{ m/s}}$.''',
            fr'''$v({t_test}) = {t_test}^2 - {k2} = {v_test}\text{{ m/s}}$.''',
            fr'''$v({t_test}) = {t_test}^2 - {k2} = {v_test}\text{{ m/s}} \neq {v_test + 20}\text{{ m/s}}$.'''
        ),
        (
            fr'''Hàm số $s(t)$ nghịch biến trên khoảng $(0; {k})$.''',
            fr'''Hàm số $s(t)$ đồng biến trên khoảng $(0; {k})$.''',
            fr'''Trên khoảng $(0; {k})$, $s'(t) = t^2 - {k2} < 0$ nên $s(t)$ nghịch biến.''',
            fr'''Trên khoảng $(0; {k})$, $s'(t) < 0$ nên $s(t)$ nghịch biến, không phải đồng biến.'''
        )
    ]
    choices, loi_giai = make_tf_choices(items)
    return caudan, choices, loi_giai


def CuoiChuong1_TF_Cau7():
    # Chuyển động s(t) = -t^3 + 9t^2 + 21t + d
    d = random.randint(5, 12)
    caudan = fr'''Một chất điểm chuyển động theo phương trình $s(t) = -t^3 + 9t^2 + 21t + {d}$ với $t$ tính bằng giây ($t \ge 0$), $s(t)$ tính bằng mét. Hãy xác định tính đúng sai của các khẳng định sau:'''

    items = [
        (
            fr'''Vận tốc của chất điểm tại thời điểm $t$ (giây) là $v(t) = -3t^2 + 18t + 21$.''',
            fr'''Vận tốc của chất điểm tại thời điểm $t$ (giây) là $v(t) = -3t^2 + 9t + 21$.''',
            fr'''$v(t) = s'(t) = (-t^3 + 9t^2 + 21t + {d})' = -3t^2 + 18t + 21$.''',
            fr'''Đạo hàm đúng là $v(t) = -3t^2 + 18t + 21 \neq -3t^2 + 9t + 21$.'''
        ),
        (
            fr'''Vận tốc của chất điểm tại giây thứ $2$ là $45\,\text{{m/s}}$.''',
            fr'''Vận tốc của chất điểm tại giây thứ $2$ là $35\,\text{{m/s}}$.''',
            fr'''Tại $t = 2$: $v(2) = -3(2^2) + 18(2) + 21 = 45\,\text{{m/s}}$.''',
            fr'''Tại $t = 2$: $v(2) = -12 + 36 + 21 = 45\,\text{{m/s}} \neq 35\,\text{{m/s}}$.'''
        ),
        (
            fr'''Quãng đường chất điểm đi được từ lúc bắt đầu đến lúc dừng hẳn là $245\,\text{{m}}$.''',
            fr'''Quãng đường chất điểm đi được từ lúc bắt đầu đến lúc dừng hẳn là $265\,\text{{m}}$.''',
            fr'''Dừng hẳn khi $v(t) = 0 \iff -3(t + 1)(t - 7) = 0 \iff t = 7\,\text{{s}}$. Quãng đường: $s(7) - s(0) = 245\,\text{{m}}$.''',
            fr'''Quãng đường đi được từ lúc bắt đầu đến khi dừng hẳn là $s(7) - s(0) = 245\,\text{{m}} \neq 265\,\text{{m}}$.'''
        ),
        (
            fr'''Vận tốc chuyển động của chất điểm đạt giá trị lớn nhất tại thời điểm $t = 3\,\text{{s}}$.''',
            fr'''Vận tốc chuyển động của chất điểm đạt giá trị lớn nhất tại thời điểm $t = 7\,\text{{s}}$.''',
            fr'''$v(t) = -3(t - 3)^2 + 48 \le 48 \implies$ lớn nhất tại $t = 3\,\text{{s}}$.''',
            fr'''$v(t)$ là parabol có đỉnh tại $t = 3\,\text{{s}}$, tại $t = 7\,\text{{s}}$ là thời điểm dừng hẳn ($v = 0$).'''
        )
    ]
    choices, loi_giai = make_tf_choices(items)
    return caudan, choices, loi_giai


def CuoiChuong1_TF_Cau8():
    # Khảo sát BBT hàm phân thức nghịch biến
    x0 = random.choice([-2, -1, 1, 2])
    y0 = random.choice([-1, 1, 2])
    caudan = fr'''\immini{{Cho hàm số $y=f(x)$ có bảng biến thiên như hình bên. Hãy cho biết tính đúng sai của mỗi khẳng định sau:}}
{{\begin{{tikzpicture}}
	\tkzTabInit[nocadre,lgt=1.2,espcl=2.5,deltacl=0.6]
	{{$x$ /0.6,$y'$ /0.6,$y$ /1.5}}
	{{$-\infty$,${x0}$,$+\infty$}}
	\tkzTabLine{{,-,d,-,}}
	\tkzTabVar{{+/${y0}$,-D+/$-\infty$/$+\infty$,-/${y0}$}}
\end{{tikzpicture}}}}'''

    items = [
        (
            fr'''Đồ thị hàm số $y=f(x)$ có tiệm cận ngang là $y={y0}$.''',
            fr'''Đồ thị hàm số $y=f(x)$ có tiệm cận ngang là $x={x0}$.''',
            fr'''Vì $\lim\limits_{{x \to \pm\infty}} f(x) = {y0}$ nên tiệm cận ngang là đường thẳng $y = {y0}$.''',
            fr'''Tiệm cận ngang là đường thẳng $y = {y0}$, không phải $x = {x0}$ (đây là tiệm cận đứng).'''
        ),
        (
            fr'''Hàm số $y=f(x)$ có tập xác định là $D = \mathbb{{R}} \setminus \\{{{x0}\\}}$.''',
            fr'''Hàm số $y=f(x)$ có tập xác định là $D = \mathbb{{R}} \setminus \\{{{y0}\\}}$.''',
            fr'''Tại $x = {x0}$ hàm số không xác định nên $D = \mathbb{{R}} \setminus \\{{{x0}\\}}$.''',
            fr'''Điểm gián đoạn là $x = {x0}$, do đó $D = \mathbb{{R}} \setminus \\{{{x0}\\}}$, không phải $\mathbb{{R}} \setminus \\{{{y0}\\}}$.'''
        ),
        (
            fr'''Đồ thị hàm số $y=f(x)$ có tiệm cận đứng là $x={x0}$.''',
            fr'''Đồ thị hàm số $y=f(x)$ có tiệm cận đứng là $y={x0}$.''',
            fr'''$\lim\limits_{{x \to {x0}^-}} f(x) = -\infty \implies$ tiệm cận đứng là đường thẳng $x = {x0}$.''',
            fr'''Tiệm cận đứng là đường thẳng $x = {x0}$, không phải $y = {x0}$.'''
        ),
        (
            fr'''Hàm số nghịch biến trên từng khoảng $(-\infty; {x0})$ và $({x0}; +\infty)$.''',
            fr'''Hàm số nghịch biến trên $\mathbb{{R}} \setminus \\{{{x0}\\}}$.''',
            fr'''Trên mỗi khoảng $(-\infty; {x0})$ và $({x0}; +\infty)$, đạo hàm $y' < 0$ nên hàm số nghịch biến trên từng khoảng đó.''',
            fr'''Không kết luận hàm số nghịch biến trên tập hợp chứa dấu hiệu loại trừ $\mathbb{{R}} \setminus \\{{{x0}\\}}$ mà phải theo từng khoảng rời nhau.'''
        )
    ]
    choices, loi_giai = make_tf_choices(items)
    return caudan, choices, loi_giai


def CuoiChuong1_TF_Cau9():
    # Khảo sát f(x) = 2x^3 - 6k^2 x + d
    k = random.choice([5, 6, 7])
    coeff = 6 * k * k
    d = random.randint(-5, 5)
    y_cd = -2 * (k**3) + coeff * k + d
    y_ct = 2 * (k**3) - coeff * k + d

    sign_d = f" + {d}" if d > 0 else (f" - {abs(d)}" if d < 0 else "")
    caudan = fr'''Cho hàm số $f(x) = 2x^3 - {coeff}x{sign_d}$. Hãy cho biết tính đúng sai của mỗi khẳng định sau:'''

    items = [
        (
            fr'''Hàm số $y = f(x)$ đạt cực đại tại điểm $x = -{k}$.''',
            fr'''Hàm số $y = f(x)$ đạt cực đại tại điểm $x = {k}$.''',
            fr'''$f'(x) = 6x^2 - {coeff} = 0 \iff x = \pm {k}$. Vì $f''(-{k}) = 12(-{k}) < 0 \implies x = -{k}$ là điểm cực đại.''',
            fr'''$f''({k}) > 0 \implies x = {k}$ là điểm cực tiểu; điểm cực đại là $x = -{k}$.'''
        ),
        (
            fr'''Hàm số $y = f(x)$ đạt cực tiểu tại điểm $x = {k}$.''',
            fr'''Giá trị cực tiểu của hàm số là $x = {k}$.''',
            fr'''$f''({k}) = 12({k}) > 0 \implies x = {k}$ là điểm cực tiểu của hàm số.''',
            fr'''Khái niệm $x = {k}$ là "điểm cực tiểu của hàm số", không phải "giá trị cực tiểu".'''
        ),
        (
            fr'''Điểm cực đại của đồ thị hàm số là $\left(-{k}; {y_cd}\right)$.''',
            fr'''Điểm cực đại của đồ thị hàm số là $\left({k}; {y_ct}\right)$.''',
            fr'''Thay $x = -{k}$ vào $f(x)$ được $f(-{k}) = {y_cd} \implies$ tọa độ cực đại là $\left(-{k}; {y_cd}\right)$.''',
            fr'''Điểm $\left({k}; {y_ct}\right)$ là điểm cực tiểu của đồ thị, không phải điểm cực đại.'''
        ),
        (
            fr'''Giá trị cực tiểu của hàm số là $y = {y_ct}$.''',
            fr'''Giá trị cực tiểu của hàm số là $y = {y_cd}$.''',
            fr'''Giá trị cực tiểu là $f({k}) = {y_ct}$.''',
            fr'''Giá trị cực tiểu là $f({k}) = {y_ct}$, còn ${y_cd}$ là giá trị cực đại.'''
        )
    ]
    choices, loi_giai = make_tf_choices(items)
    return caudan, choices, loi_giai


def CuoiChuong1_TF_Cau10():
    # Bảng biến thiên hàm bậc ba
    x1 = random.choice([-3, -2])
    x2 = random.choice([2, 4])
    y1 = random.choice([-6, -5, -4])
    y2 = random.choice([6, 8, 10])

    caudan = fr'''\immini{{Cho hàm số $y=f(x)$ có bảng biến thiên như hình bên. Hãy cho biết tính đúng sai của mỗi khẳng định sau:}}
{{\begin{{tikzpicture}}
	\tkzTabInit[nocadre,lgt=1.2,espcl=2.5,deltacl=0.6]
	{{$x$ /0.6, $y'$ /0.6, $y$ /1.5}}
	{{$-\infty$,${x1}$,${x2}$,$+\infty$}}
	\tkzTabLine{{,-,$0$,+,$0$,-,}}
	\tkzTabVar{{+/$+\infty$,-/${y1}$,+/${y2}$,-/$-\infty$}}
\end{{tikzpicture}}}}'''

    items = [
        (
            fr'''Hàm số đạt cực đại tại $x={x2}$.''',
            fr'''Hàm số đạt cực đại tại $x={x1}$.''',
            fr'''Đạo hàm đổi dấu từ $+$ sang $-$ khi qua $x = {x2}$ nên đạt cực đại tại $x = {x2}$.''',
            fr'''Tại $x = {x1}$ đạo hàm đổi dấu từ $-$ sang $+$ nên đạt cực tiểu, không phải cực đại.'''
        ),
        (
            fr'''Giá trị cực đại của hàm số là $y={y2}$.''',
            fr'''Giá trị cực đại của hàm số là $y={x2}$.''',
            fr'''Giá trị cực đại chính là tung độ tại điểm cực đại: $y_{{CĐ}} = {y2}$.''',
            fr'''Giá trị cực đại là $y = {y2}$, số ${x2}$ là điểm cực đại của hàm số.'''
        ),
        (
            fr'''Hàm số đồng biến trên khoảng $({x1}; {x2})$.''',
            fr'''Hàm số đồng biến trên khoảng $({y1}; {y2})$.''',
            fr'''Trên khoảng $({x1}; {x2})$, $y' > 0$ nên hàm số đồng biến.''',
            fr'''Khoảng đồng biến phải lấy theo biến $x \in ({x1}; {x2})$, không lấy theo giá trị $y$.'''
        ),
        (
            fr'''Hàm số nghịch biến trên khoảng $({x2}; +\infty)$.''',
            fr'''Hàm số đồng biến trên khoảng $({x2}; +\infty)$.''',
            fr'''Trên khoảng $({x2}; +\infty)$, đạo hàm mang dấu âm nên hàm số nghịch biến.''',
            fr'''Trên khoảng $({x2}; +\infty)$, đạo hàm $y' < 0$ nên hàm số nghịch biến, khẳng định đồng biến là sai.'''
        )
    ]
    choices, loi_giai = make_tf_choices(items)
    return caudan, choices, loi_giai


def CuoiChuong1_TF_Cau11():
    # Chuyển động S(t) = -t^3 + 9t^2 + t + d
    d = random.randint(8, 15)
    caudan = fr'''Một chất điểm chuyển động được quãng đường $S$ (đơn vị mét) là hàm số phụ thuộc thời gian $t$ (đơn vị giây, $t \ge 0$) theo công thức $S(t) = -t^3 + 9t^2 + t + {d}$.'''

    items = [
        (
            fr'''Vận tốc trung bình của chuyển động trong $2$ giây đầu tiên bằng $15\,\text{{m/s}}$.''',
            fr'''Vận tốc trung bình của chuyển động trong $2$ giây đầu tiên bằng $25\,\text{{m/s}}$.''',
            fr'''$v_{{\text{{tb}}}} = \dfrac{{S(2) - S(0)}}{{2}} = \dfrac{{(30 + {d}) - {d}}}{{2}} = 15\,\text{{m/s}}$.''',
            fr'''$v_{{\text{{tb}}}} = \dfrac{{S(2) - S(0)}}{{2}} = 15\,\text{{m/s}} \neq 25\,\text{{m/s}}$.'''
        ),
        (
            fr'''Quãng đường chất điểm đi được sau khi xuất phát $1$ giây bằng $9\,\text{{m}}$.''',
            fr'''Quãng đường chất điểm đi được sau khi xuất phát $1$ giây bằng $18\,\text{{m}}$.''',
            fr'''Quãng đường sau $1$ giây là $\Delta S = S(1) - S(0) = (9 + {d}) - {d} = 9\,\text{{m}}$.''',
            fr'''Quãng đường sau $1$ giây là $S(1) - S(0) = 9\,\text{{m}} \neq 18\,\text{{m}}$.'''
        ),
        (
            fr'''Gia tốc của chuyển động tại thời điểm $t=2$ giây lớn hơn gia tốc tại thời điểm $t=4$ giây.''',
            fr'''Gia tốc của chuyển động tại thời điểm $t=2$ giây nhỏ hơn gia tốc tại thời điểm $t=4$ giây.''',
            fr'''$a(t) = S''(t) = -6t + 18 \implies a(2) = 6\,\text{{m/s}}^2 > a(4) = -6\,\text{{m/s}}^2$.''',
            fr'''$a(2) = 6\,\text{{m/s}}^2 > a(4) = -6\,\text{{m/s}}^2$, khẳng định nhỏ hơn là sai.'''
        ),
        (
            fr'''Vận tốc của chuyển động đạt giá trị lớn nhất là $28\,\text{{m/s}}$.''',
            fr'''Vận tốc của chuyển động đạt giá trị lớn nhất là $38\,\text{{m/s}}$.''',
            fr'''$v(t) = S'(t) = -3t^2 + 18t + 1 = -3(t - 3)^2 + 28 \le 28\,\text{{m/s}}$.''',
            fr'''Vận tốc lớn nhất đạt tại $t = 3\,\text{{s}}$ là $28\,\text{{m/s}} \neq 38\,\text{{m/s}}$.'''
        )
    ]
    choices, loi_giai = make_tf_choices(items)
    return caudan, choices, loi_giai


def CuoiChuong1_TF_Cau12():
    # Khảo sát y = x^3 - 3k^2 x + c
    k = random.choice([1, 2])
    c = random.randint(-3, 3)
    k2_3 = 3 * k * k
    
    sign_k2 = f"- {k2_3}x"
    sign_c = f" + {c}" if c > 0 else (f" - {abs(c)}" if c < 0 else "")
    caudan = fr'''Cho hàm số $y = x^3 {sign_k2}{sign_c}$.'''

    items = [
        (
            fr'''Điểm cực tiểu của hàm số là $x = {k}$.''',
            fr'''Điểm cực tiểu của hàm số là $x = {-k}$.''',
            fr'''$y' = 3x^2 - {k2_3} = 0 \iff x = \pm {k}$. Điểm cực tiểu là $x = {k}$.''',
            fr'''$x = {-k}$ là điểm cực đại, điểm cực tiểu là $x = {k}$.'''
        ),
        (
            fr'''Giả sử hàm số đã cho có hai điểm cực trị là $x_1, x_2$. Khi đó giá trị $x_1 \cdot x_2 = -{k*k}$.''',
            fr'''Giả sử hàm số đã cho có hai điểm cực trị là $x_1, x_2$. Khi đó giá trị $x_1 \cdot x_2 = {k*k}$.''',
            fr'''Hai điểm cực trị là $x_1 = -{k}$ và $x_2 = {k} \implies x_1 x_2 = -{k*k}$.''',
            fr'''$x_1 x_2 = (-{k})({k}) = -{k*k} \neq {k*k}$.'''
        ),
        (
            fr'''Hàm số nghịch biến trên khoảng $(-{k}; {k})$.''',
            fr'''Hàm số đồng biến trên khoảng $(-{k}; {k})$.''',
            fr'''Trên khoảng $(-{k}; {k})$, $y' < 0$ nên hàm số nghịch biến.''',
            fr'''Trên khoảng $(-{k}; {k})$, $y' < 0$ nên hàm số nghịch biến, không phải đồng biến.'''
        ),
        (
            fr'''Đồ thị hàm số có tâm đối xứng là điểm $I(0; {c})$.''',
            fr'''Đồ thị hàm số có tâm đối xứng là điểm $I(0; {c + 2})$.''',
            fr'''Điểm uốn của đồ thị hàm số bậc ba là tâm đối xứng: $y'' = 6x = 0 \iff x = 0 \implies I(0; {c})$.''',
            fr'''Tâm đối xứng là điểm uốn $I(0; {c}) \neq I(0; {c + 2})$.'''
        )
    ]
    choices, loi_giai = make_tf_choices(items)
    return caudan, choices, loi_giai


def CuoiChuong1_TF_Cau13():
    # Khảo sát hàm phân thức y = (2x^2 - 3x + 6)/(x - 2)
    caudan = fr'''Cho hàm số $y=\dfrac{{2x^2-3x+6}}{{x-2}}$. Các khẳng định sau đúng hay sai?'''

    items = [
        (
            fr'''Hàm số đạt cực đại tại điểm $x=0$.''',
            fr'''Hàm số đạt cực đại tại điểm $x=4$.''',
            fr'''$y' = \dfrac{{2x^2 - 8x}}{{(x - 2)^2}} = 0 \iff x = 0$ hoặc $x = 4$. Hàm số đạt cực đại tại $x = 0$.''',
            fr'''Tại $x = 4$ hàm số đạt cực tiểu, cực đại đạt tại $x = 0$.'''
        ),
        (
            fr'''Giá trị nhỏ nhất của hàm số trên khoảng $(2;+\infty)$ bằng $13$.''',
            fr'''Giá trị nhỏ nhất của hàm số trên khoảng $(2;+\infty)$ bằng $10$.''',
            fr'''Trên $(2; +\infty)$, điểm cực tiểu là $x = 4$ với $y(4) = 2(4) + 1 + \dfrac{{8}}{{2}} = 13 \implies \min = 13$.''',
            fr'''Trên $(2; +\infty)$, giá trị nhỏ nhất là $y(4) = 13 \neq 10$.'''
        ),
        (
            fr'''Tiệm cận xiên của đồ thị hàm số là đường thẳng có phương trình $y=2x+1$.''',
            fr'''Tiệm cận xiên của đồ thị hàm số là đường thẳng có phương trình $y=2x-1$.''',
            fr'''Chia đa thức: $y = 2x + 1 + \dfrac{{8}}{{x - 2}} \implies$ tiệm cận xiên là $y = 2x + 1$.''',
            fr'''Tiệm cận xiên đúng là $y = 2x + 1 \neq 2x - 1$.'''
        ),
        (
            fr'''Hàm số nghịch biến trên từng khoảng $(0; 2)$ và $(2; 4)$.''',
            fr'''Hàm số nghịch biến trên khoảng $(0; 4)$.''',
            fr'''$y' < 0$ với mọi $x \in (0; 2) \cup (2; 4)$, do hàm số không xác định tại $x = 2$ nên không nghịch biến trên khoảng $(0; 4)$.''',
            fr'''Hàm số gián đoạn tại $x = 2$ nên không thể nghịch biến trên toàn bộ khoảng $(0; 4)$.'''
        )
    ]
    choices, loi_giai = make_tf_choices(items)
    return caudan, choices, loi_giai


def CuoiChuong1_TF_Cau14():
    # Đồ thị hàm bậc ba y = -x^3 + 6x^2 - 9x + 5
    caudan = fr'''\immini{{Cho hàm số bậc ba $y=f(x)=ax^3+bx^2+cx+d$ có đồ thị như hình vẽ bên. Các khẳng định sau đúng hay sai?}}
{{\begin{{tikzpicture}}[scale=0.55, line join=round, line cap=round, >=stealth,font=\footnotesize]
	\def\xmin{{-0.5}}\def\xmax{{4}}\def\ymin{{-0.5}}\def\ymax{{5.5}}
	\draw[->] (\xmin-0.2,0)--(\xmax+0.2,0) node[below]{{$x$}};
	\draw[->] (0,\ymin-0.2)--(0,\ymax+0.2) node[right]{{$y$}};
	\draw (0,0) node[below left]{{$O$}};
	\foreach \x in {{1,2,3}}\draw (\x,0.1)--(\x,-0.1) node[below]{{$\x$}};
	\foreach \y in {{1,2,3,5}}\draw (0.1,\y)--(-0.1,\y) node[left]{{$\y$}};
	\clip (\xmin,\ymin) rectangle (\xmax,\ymax);
	\draw[thick,smooth,samples=200,domain=\xmin:\xmax] plot (\x,{{-1*((\x)^3)+6*((\x)^2)+-9*(\x)+5}});
	\draw[dashed] (1,0)--(1,1)--(0,1);\fill (1,1)circle(1.5pt);
	\draw[dashed] (3,0)--(3,5)--(0,5);\fill (3,5)circle(1.5pt);
\end{{tikzpicture}}}}'''

    items = [
        (
            fr'''Giá trị cực đại của hàm số bằng $5$.''',
            fr'''Giá trị cực đại của hàm số bằng $3$.''',
            fr'''Điểm cực đại là $(3; 5)$ nên giá trị cực đại bằng $5$.''',
            fr'''Giá trị cực đại là $y = 5$, số $3$ là hoành độ điểm cực đại.'''
        ),
        (
            fr'''Hàm số đồng biến trên khoảng $(1;3)$.''',
            fr'''Hàm số nghịch biến trên khoảng $(1;3)$.''',
            fr'''Trên $(1; 3)$ đồ thị đi lên từ trái sang phải nên hàm số đồng biến.''',
            fr'''Trên $(1; 3)$ đồ thị đi lên nên hàm số đồng biến, khẳng định nghịch biến là sai.'''
        ),
        (
            fr'''Giá trị cực tiểu của hàm số bằng $1$.''',
            fr'''Giá trị cực tiểu của hàm số bằng $0$.''',
            fr'''Điểm cực tiểu là $(1; 1)$ nên giá trị cực tiểu bằng $1$.''',
            fr'''Giá trị cực tiểu là $y = 1 \neq 0$.'''
        ),
        (
            fr'''Hệ số $a$ của hàm số bậc ba thỏa mãn $a < 0$.''',
            fr'''Hệ số $a$ của hàm số bậc ba thỏa mãn $a > 0$.''',
            fr'''Nhánh bên phải cùng của đồ thị đi xuống ($x \to +\infty \implies y \to -\infty$) nên $a < 0$.''',
            fr'''Đồ thị đi xuống khi $x \to +\infty$ chứng tỏ hệ số đầu $a < 0$, không phải $a > 0$.'''
        )
    ]
    choices, loi_giai = make_tf_choices(items)
    return caudan, choices, loi_giai


def CuoiChuong1_TF_Cau15():
    # f(x) = 2 sin(x) - x
    caudan = fr'''Cho hàm số $f(x) = 2\sin x - x$.'''

    items = [
        (
            fr'''Hàm số $f(x)$ liên tục trên $\mathbb{{R}}$.''',
            fr'''Hàm số $f(x)$ gián đoạn tại $x = 0$.''',
            fr'''Hàm lượng giác $\sin x$ và đa thức $-x$ đều liên tục trên $\mathbb{{R}}$ nên tổng của chúng liên tục trên $\mathbb{{R}}$.''',
            fr'''Hàm số xác định và liên tục trên toàn bộ $\mathbb{{R}}$.'''
        ),
        (
            fr'''Đạo hàm của hàm số đã cho là $f'(x) = 2\cos x - 1$.''',
            fr'''Đạo hàm của hàm số đã cho là $f'(x) = 2\cos x + 1$.''',
            fr'''$(2\sin x - x)' = 2\cos x - 1$.''',
            fr'''Đạo hàm đúng là $f'(x) = 2\cos x - 1 \neq 2\cos x + 1$.'''
        ),
        (
            fr'''Tập nghiệm của phương trình $f'(x) = 0$ là $\left\{{\pm \dfrac{{\pi}}{{3}} + k2\pi, k \in \mathbb{{Z}}\right\}}$.''',
            fr'''Tập nghiệm của phương trình $f'(x) = 0$ là $\left\{{\pm \dfrac{{\pi}}{{6}} + k2\pi, k \in \mathbb{{Z}}\right\}}$.''',
            fr'''$2\cos x - 1 = 0 \iff \cos x = \dfrac{{1}}{{2}} \iff x = \pm \dfrac{{\pi}}{{3}} + k2\pi$.''',
            fr'''$\cos x = \dfrac{{1}}{{2}} \iff x = \pm \dfrac{{\pi}}{{3}} + k2\pi \neq \pm \dfrac{{\pi}}{{6}} + k2\pi$.'''
        ),
        (
            fr'''Giá trị nhỏ nhất của $f(x)$ trên đoạn $\left[0; \dfrac{{\pi}}{{3}}\right]$ là $0$.''',
            fr'''Giá trị nhỏ nhất của $f(x)$ trên đoạn $\left[0; \dfrac{{\pi}}{{3}}\right]$ là $\sqrt{{3}} - \dfrac{{\pi}}{{3}}$.''',
            fr'''Trên $\left[0; \dfrac{{\pi}}{{3}}\right]$, $f'(x) = 2\cos x - 1 \ge 0 \implies f(x)$ đồng biến $\implies \min = f(0) = 0$.''',
            fr'''Vì $f(x)$ đồng biến trên $\left[0; \dfrac{{\pi}}{{3}}\right]$ nên $\min = f(0) = 0$, giá trị $\sqrt{{3}} - \dfrac{{\pi}}{{3}}$ là GTLN tại $\dfrac{{\pi}}{{3}}$.'''
        )
    ]
    choices, loi_giai = make_tf_choices(items)
    return caudan, choices, loi_giai


def CuoiChuong1_TF_Cau16():
    # BBT y = ax^3 + bx^2 + cx + d
    caudan = fr'''\immini{{Cho hàm số $y = f(x) = ax^3 + bx^2 + cx + d$ có bảng biến thiên như hình bên. Xét tính đúng sai của các khẳng định sau:}}
{{\begin{{tikzpicture}}
  \tkzTabInit[nocadre,lgt=1.2,espcl=2,deltacl=0.5]
     {{$x$/0.7,$f'(x)$/0.7,$f(x)$/2}}
     {{$-\infty$,$-2$,$0$,$+\infty$}}
  \tkzTabLine{{,-,0,+,0,-,}}
  \tkzTabVar{{+/$+\infty$,-/$0$,+/$4$,-/$-\infty$}}
\end{{tikzpicture}}}}'''

    items = [
        (
            fr'''Hàm số nghịch biến trên khoảng $(-\infty; -2)$.''',
            fr'''Hàm số nghịch biến trên khoảng $(-\infty; 4)$.''',
            fr'''Trên khoảng $(-\infty; -2)$, $f'(x) < 0$ nên hàm số nghịch biến.''',
            fr'''$(-\infty; 4)$ chứa khoảng $(-2; 0)$ mà trên đó hàm số đồng biến, nên khẳng định sai.'''
        ),
        (
            fr'''Hàm số không có giá trị lớn nhất trên $\mathbb{{R}}$.''',
            fr'''Hàm số đạt giá trị lớn nhất là $4$.''',
            fr'''Vì $\lim\limits_{{x \to -\infty}} f(x) = +\infty$ nên hàm số không có giá trị lớn nhất trên $\mathbb{{R}}$.''',
            fr'''Số $4$ chỉ là giá trị cực đại địa phương, hàm số tiến tới $+\infty$ khi $x \to -\infty$ nên không có GTLN.'''
        ),
        (
            fr'''Đường thẳng $y = 2$ cắt đồ thị hàm số tại ba điểm phân biệt.''',
            fr'''Đường thẳng $y = 2$ cắt đồ thị hàm số tại đúng một điểm.''',
            fr'''Vì $y_{{CT}} = 0 < 2 < y_{{CD}} = 4$ nên đường thẳng $y = 2$ cắt đồ thị tại $3$ điểm phân biệt.''',
            fr'''Do $0 < 2 < 4$, đường thẳng $y = 2$ nằm giữa cực tiểu và cực đại nên cắt đồ thị tại $3$ điểm, không phải $1$.'''
        ),
        (
            fr'''Trong bốn hệ số $a, b, c, d$ có đúng hai số âm.''',
            fr'''Trong bốn hệ số $a, b, c, d$ có đúng một số âm.''',
            fr'''$a < 0$ (nhánh phải đi xuống); $d = f(0) = 4 > 0$; $f'(x) = 3ax^2 + 2bx + c = 0$ có nghiệm $0$ và $-2 \implies c = 0, -\dfrac{{2b}}{{3a}} = -2 \implies b = 3a < 0$. Vậy có đúng $2$ số âm là $a$ và $b$.''',
            fr'''Ta xác định được $a < 0, b < 0, c = 0, d > 0$ nên có đúng $2$ số âm là $a, b$, khẳng định đúng $1$ số âm là sai.'''
        )
    ]
    choices, loi_giai = make_tf_choices(items)
    return caudan, choices, loi_giai


# ==============================================================================
# CHƯƠNG II: ĐÚNG - SAI (4 CÂU)
# ==============================================================================

def CuoiChuong2_TF_Cau1():
    # Vectơ trong hình lập phương
    caudan = fr'''Cho hình lập phương $ABCD.A'B'C'D'$ cạnh $a$. Gọi $M$ là giao điểm của $CD'$ và $C'D$.'''

    items = [
        (
            fr'''$\vec{{DC'}} = \vec{{DC}} + \vec{{DD'}}$.''',
            fr'''$\vec{{DC'}} = \vec{{DC}} - \vec{{DD'}}$.''',
            fr'''Trong hình vuông $CDD'C'$, theo quy tắc hình bình hành ta có $\vec{{DC'}} = \vec{{DC}} + \vec{{DD'}}$.''',
            fr'''Theo quy tắc hình bình hành $\vec{{DC'}} = \vec{{DC}} + \vec{{DD'}} \neq \vec{{DC}} - \vec{{DD'}}$.'''
        ),
        (
            fr'''$\vec{{AD'}} \cdot \vec{{CC'}} = a^2$.''',
            fr'''$\vec{{AD'}} \cdot \vec{{CC'}} = 0$.''',
            fr'''$\vec{{AD'}} \cdot \vec{{CC'}} = (\vec{{AD}} + \vec{{DD'}}) \cdot \vec{{DD'}} = \vec{{AD}} \cdot \vec{{DD'}} + \vec{{DD'}}^2 = 0 + a^2 = a^2$.''',
            fr'''$\vec{{AD'}} \cdot \vec{{CC'}} = a^2 \neq 0$ vì hình chiếu của $\vec{{AD'}}$ lên đường thẳng $CC'$ có độ dài bằng $a$.'''
        ),
        (
            fr'''$\vec{{AM}} = \dfrac{{1}}{{2}}\vec{{AB}} + \vec{{AD}} + \dfrac{{1}}{{2}}\vec{{AA'}}$.''',
            fr'''$\vec{{AM}} = \vec{{AB}} + \dfrac{{1}}{{2}}\vec{{AD}} + \dfrac{{1}}{{2}}\vec{{AA'}}$.''',
            fr'''$M$ là trung điểm $CD' \implies \vec{{AM}} = \dfrac{{1}}{{2}}(\vec{{AC}} + \vec{{AD'}}) = \dfrac{{1}}{{2}}(\vec{{AB}} + \vec{{AD}} + \vec{{AD}} + \vec{{AA'}}) = \dfrac{{1}}{{2}}\vec{{AB}} + \vec{{AD}} + \dfrac{{1}}{{2}}\vec{{AA'}}$.''',
            fr'''Phân tích đúng là $\vec{{AM}} = \dfrac{{1}}{{2}}\vec{{AB}} + \vec{{AD}} + \dfrac{{1}}{{2}}\vec{{AA'}}$.'''
        ),
        (
            fr'''Góc giữa hai đường thẳng $A'C$ và $BD$ bằng $90^\circ$.''',
            fr'''Góc giữa hai đường thẳng $A'C$ và $BD$ bằng $60^\circ$.''',
            fr'''Ta có $BD \perp AC$ và $BD \perp AA' \implies BD \perp (ACC'A') \implies BD \perp A'C \implies$ góc bằng $90^\circ$.''',
            fr'''$BD \perp (ACC'A') \implies BD \perp A'C \implies$ góc giữa chúng bằng $90^\circ \neq 60^\circ$.'''
        )
    ]
    choices, loi_giai = make_tf_choices(items)
    return caudan, choices, loi_giai


def CuoiChuong2_TF_Cau2():
    # Lực căng cần cẩu
    F_val = random.choice([4000, 4500, 5000])
    P_khung = random.choice([2500, 2800, 3000])
    F_tong = round(2 * math.sqrt(3) * F_val, 1)
    P_max = round(F_tong - P_khung, 1)

    caudan = fr'''\immini{{Một chiếc ô tô được đặt trên mặt đáy dưới của một khung sắt có dạng hình hộp chữ nhật với đáy trên là hình chữ nhật $ABCD$, mặt phẳng $(ABCD)$ song song với mặt phẳng nằm ngang. Khung sắt đó được buộc vào móc $E$ của chiếc cần cẩu sao cho các đoạn dây cáp $EA, EB, EC, ED$ có độ dài bằng nhau và cùng tạo với mặt phẳng $(ABCD)$ một góc bằng $60^\circ$. Chiếc cần cẩu kéo khung sắt lên theo phương thẳng đứng. Biết rằng các lực căng $\vec{{F}}_1, \vec{{F}}_2, \vec{{F}}_3, \vec{{F}}_4$ đều có cường độ là ${F_val}\text{{ N}}$ và trọng lượng của khung sắt là ${P_khung}\text{{ N}}$. Xét tính đúng sai của các mệnh đề sau:}}
{{\begin{{tikzpicture}}[scale=0.6, line join=round, line cap=round, >=stealth]
  \coordinate (A) at (0,1);
  \coordinate (B) at (1.2,0);
  \coordinate (C) at (4,0.3);
  \coordinate (D) at (2.8,1.3);
  \coordinate (E) at (2,4);
  \draw[thick] (E)--(A) (E)--(B) (E)--(C) (E)--(D);
  \draw[dashed] (A)--(B)--(C)--(D)--cycle;
  \fill (E) circle(1.5pt) node[above]{{$E$}};
  \fill (A) circle(1.5pt) node[left]{{$A$}};
  \fill (B) circle(1.5pt) node[below left]{{$B$}};
  \fill (C) circle(1.5pt) node[right]{{$C$}};
  \fill (D) circle(1.5pt) node[above right]{{$D$}};
\end{{tikzpicture}}}}'''

    items = [
        (
            fr'''Các lực $\vec{{F}}_1, \vec{{F}}_2, \vec{{F}}_3, \vec{{F}}_4$ có cùng độ lớn bằng ${F_val}\text{{ N}}$.''',
            fr'''Hợp lực của hai lực đối diện $\vec{{F}}_1 + \vec{{F}}_3 = \vec{{0}}$.''',
            fr'''Theo giả thiết đề bài, các lực căng đều có cường độ bằng ${F_val}\text{{ N}}$.''',
            fr'''Hai lực $\vec{{F}}_1$ và $\vec{{F}}_3$ không đối nhau (cùng hướng kéo lên móc $E$) nên tổng khác vectơ không.'''
        ),
        (
            fr'''Hợp lực tác dụng của $4$ sợi dây cáp theo phương thẳng đứng có độ lớn xấp xỉ ${F_tong}\text{{ N}}$.''',
            fr'''Hợp lực tác dụng của $4$ sợi dây cáp theo phương thẳng đứng có độ lớn là ${4 * F_val}\text{{ N}}$.''',
            fr'''Chiếu lên phương thẳng đứng: $F_z = 4 \cdot {F_val} \cdot \sin 60^\circ = 2\sqrt{{3}} \cdot {F_val} \approx {F_tong}\text{{ N}}$.''',
            fr'''Do dây cáp nghiêng $60^\circ$ so với mặt phẳng ngang nên $F_z = 4 F \sin 60^\circ \approx {F_tong}\text{{ N}} \neq {4 * F_val}\text{{ N}}$.'''
        ),
        (
            fr'''Trọng lượng tối đa của chiếc ô tô để cần cẩu có thể nhấc lên được xấp xỉ ${P_max}\text{{ N}}$.''',
            fr'''Trọng lượng tối đa của chiếc ô tô để cần cẩu có thể nhấc lên được xấp xỉ ${P_max + 1000}\text{{ N}}$.''',
            fr'''Để nâng được thì $P_{{xe}} + P_{{khung}} \le F_z \implies P_{{xe}} \le {F_tong} - {P_khung} \approx {P_max}\text{{ N}}$.''',
            fr'''Trọng lượng tối đa của ô tô là ${P_max}\text{{ N}} \neq {P_max + 1000}\text{{ N}}$.'''
        ),
        (
            fr'''Hình chiếu vuông góc của đỉnh $E$ lên mặt phẳng $(ABCD)$ là tâm đối xứng của hình chữ nhật $ABCD$.''',
            fr'''Hình chiếu vuông góc của đỉnh $E$ lên mặt phẳng $(ABCD)$ trùng với đỉnh $A$.''',
            fr'''Vì $EA = EB = EC = ED$ nên hình chiếu của $E$ cách đều $A, B, C, D$, chính là tâm đường tròn ngoại tiếp (tâm đối xứng) của $ABCD$.''',
            fr'''Vì các đoạn dây cáp bằng nhau nên hình chiếu của $E$ phải rơi vào tâm hình chữ nhật, không thể rơi vào $A$.'''
        )
    ]
    choices, loi_giai = make_tf_choices(items)
    return caudan, choices, loi_giai


def CuoiChuong2_TF_Cau3():
    # Hình hộp chữ nhật trong không gian Oxyz
    a_side = random.choice([4, 6])
    b_side = random.choice([3, 8])

    caudan = fr'''Trong không gian $Oxyz$, cho hình hộp chữ nhật $ABCD.A'B'C'D'$ có đỉnh $A$ trùng với gốc tọa độ $O$, các vectơ $\vec{{AB}}, \vec{{AD}}, \vec{{AA'}}$ theo thứ tự cùng hướng với các vectơ $\vec{{i}}, \vec{{j}}, \vec{{k}}$ và $AB = {a_side}, AD = {b_side}, \left(\widehat{{\vec{{AC}}, \vec{{AC'}}}}\right) = 30^\circ$.'''

    items = [
        (
            fr'''$\vec{{AB}} = {a_side}\vec{{i}} + 0\vec{{j}} + 0\vec{{k}}$.''',
            fr'''$\vec{{AB}} = 0\vec{{i}} + {a_side}\vec{{j}} + 0\vec{{k}}$.''',
            fr'''$\vec{{AB}}$ cùng hướng với $\vec{{i}}$ và có độ dài bằng ${a_side}$ nên $\vec{{AB}} = ({a_side}; 0; 0) = {a_side}\vec{{i}}$.''',
            fr'''$\vec{{AB}}$ nằm trên trục $Ox$ nên tọa độ là $({a_side}; 0; 0)$, không phải $(0; {a_side}; 0)$.'''
        ),
        (
            fr'''Tọa độ điểm $C$ là $({a_side}; {b_side}; 0)$.''',
            fr'''Tọa độ điểm $C$ là $({b_side}; {a_side}; 0)$.''',
            fr'''$\vec{{AC}} = \vec{{AB}} + \vec{{AD}} = ({a_side}; {b_side}; 0) \implies C({a_side}; {b_side}; 0)$.''',
            fr'''Do $AB$ dọc theo $Ox$ và $AD$ dọc theo $Oy$ nên $C({a_side}; {b_side}; 0) \neq ({b_side}; {a_side}; 0)$.'''
        ),
        (
            fr'''Độ dài đường chéo đáy $AC = \sqrt{{{a_side**2 + b_side**2}}}$.''',
            fr'''Độ dài đường chéo đáy $AC = {a_side + b_side}$.''',
            fr'''$AC = \sqrt{{AB^2 + AD^2}} = \sqrt{{{a_side}^2 + {b_side}^2}} = \sqrt{{{a_side**2 + b_side**2}}}$.''',
            fr'''Theo định lý Pythagore: $AC = \sqrt{{{a_side}^2 + {b_side}^2}} = \sqrt{{{a_side**2 + b_side**2}}} \neq {a_side + b_side}$.'''
        ),
        (
            fr'''Gọi $\alpha, \beta, \gamma$ theo thứ tự là số đo các góc hợp bởi vectơ $\vec{{AC'}}$ với các vectơ $\vec{{i}}, \vec{{j}}, \vec{{k}}$. Khi đó $\cos^2 \alpha + \cos^2 \beta + \cos^2 \gamma = 1$.''',
            fr'''Gọi $\alpha, \beta, \gamma$ theo thứ tự là số đo các góc hợp bởi vectơ $\vec{{AC'}}$ với các vectơ $\vec{{i}}, \vec{{j}}, \vec{{k}}$. Khi đó $\cos^2 \alpha + \cos^2 \beta + \cos^2 \gamma = 2$.''',
            fr'''Tổng bình phương các cosin chỉ phương của một vectơ trong không gian luôn bằng $1$.''',
            fr'''Theo tính chất hình học giải tích không gian: $\cos^2 \alpha + \cos^2 \beta + \cos^2 \gamma = 1 \neq 2$.'''
        )
    ]
    choices, loi_giai = make_tf_choices(items)
    return caudan, choices, loi_giai


def CuoiChuong2_TF_Cau4():
    # Chuyển động máy bay chiến đấu và ra đa
    z0 = random.choice([8, 10, 12])
    xM = random.choice([400, 500])
    yM = random.choice([200, 300])
    xN = random.choice([200, 300])
    yN = random.choice([700, 800])
    T_min = 40
    
    dx = xN - xM
    dy = yN - yM
    dist_MN = round(math.sqrt(dx**2 + dy**2), 1)

    caudan = fr'''Trong không gian chọn hệ trục tọa độ $Oxyz$ cho trước, trong đó xem mặt phẳng $(Oxy)$ là mặt đất, mỗi đơn vị trên trục tương ứng với $1\text{{ km}}$, một ra đa được đặt tại vị trí gốc tọa độ $O$ phát hiện một máy bay chiến đấu di chuyển với vận tốc và hướng không đổi từ điểm $M({xM}; {yM}; {z0})$ đến điểm $N({xN}; {yN}; {z0})$ trong ${T_min}$ phút.'''

    items = [
        (
            fr'''Khoảng cách giữa hai điểm $M$ và $N$ xấp xỉ ${dist_MN}\text{{ km}}$.''',
            fr'''Khoảng cách giữa hai điểm $M$ và $N$ xấp xỉ ${round(dist_MN + 50, 1)}\text{{ km}}$.''',
            fr'''$MN = \sqrt{{({xN} - {xM})^2 + ({yN} - {yM})^2 + ({z0} - {z0})^2}} = \sqrt{{{dx}^2 + {dy}^2}} \approx {dist_MN}\text{{ km}}$.''',
            fr'''$MN = \sqrt{{{dx}^2 + {dy}^2}} \approx {dist_MN}\text{{ km}} \neq {round(dist_MN + 50, 1)}\text{{ km}}$.'''
        ),
        (
            fr'''Máy bay chiến đấu khi bay từ $M$ đến $N$ luôn cách mặt đất là ${z0}\text{{ km}}$.''',
            fr'''Máy bay chiến đấu khi bay từ $M$ đến $N$ có độ cao thay đổi liên tục so với mặt đất.''',
            fr'''Cao độ $z = {z0}$ của cả $M$ và $N$ đều bằng nhau và chuyển động thẳng đều nên độ cao luôn cố định bằng ${z0}\text{{ km}}$.''',
            fr'''Vì $z_M = z_N = {z0}$ và máy bay bay thẳng đều nên cao độ $z(t) = {z0}$ không đổi.'''
        ),
        (
            fr'''Vectơ chỉ phương chuyển động của máy bay có cao độ bằng $0$.''',
            fr'''Vectơ chỉ phương chuyển động của máy bay có cao độ khác $0$.''',
            fr'''$\vec{{MN}} = ({dx}; {dy}; 0)$ có cao độ bằng $0$.''',
            fr'''$\vec{{MN}} = ({dx}; {dy}; 0)$ có thành phần $z = 0$, khẳng định khác $0$ là sai.'''
        ),
        (
            fr'''Tọa độ trung điểm của đoạn thẳng $MN$ là $I\left({(xM + xN) // 2}; {(yM + yN) // 2}; {z0}\right)$.''',
            fr'''Tọa độ trung điểm của đoạn thẳng $MN$ là $I\left({(xM + xN) // 2}; {(yM + yN) // 2}; 0\right)$.''',
            fr'''Tọa độ trung điểm $I = \left(\dfrac{{{xM} + {xN}}}{{2}}; \dfrac{{{yM} + {yN}}}{{2}}; \dfrac{{{z0} + {z0}}}{{2}}\right) = \left({(xM + xN) // 2}; {(yM + yN) // 2}; {z0}\right)$.''',
            fr'''Trung điểm của $MN$ có cao độ là ${z0}$, không thể bằng $0$.'''
        )
    ]
    choices, loi_giai = make_tf_choices(items)
    return caudan, choices, loi_giai


from cuoi_chuong_tf_32 import *

