# -*- coding: utf-8 -*-
"""
Module sinh đề và câu hỏi Trả lời ngắn Toán 10 dựa trên file Toan_10.pdf (43 đề kiểm tra mới)
và tích hợp Kho ảnh thực tế TikZ (Tex/Tex_HinhThucTe, Tex/Ung_Dung_TT_Giai_TamGiac).

Bao gồm:
- Chương I: Mệnh đề & Tập hợp (Đúng/sai, phủ định, số tập con, phép toán khoảng đoạn, sơ đồ Venn)
- Chương II: BPT và hệ BPT bậc nhất hai ẩn (Miền nghiệm TikZ, GTLN/GTNN đa giác, quy hoạch tuyến tính thực tế)
- Chương III: Hệ thức lượng trong tam giác & TOÁN THỰC TẾ HÌNH HỌC (Đo đầm lầy, tháp, cây trên sườn đồi, quạt gió, hầm xuyên núi tiết kiệm xăng, chi phí trồng cây)
- Chương IV: Vectơ & TOÁN THỰC TẾ VECTƠ (Hợp lực 2 lực, 3 lực cân bằng vật đứng yên, chuyển động tàu thủy trên Oxy, máy bay gặp gió)
- Chương V: Thống kê & Sai số (Sai số tuyệt đối, sai số tương đối, khoảng tứ phân vị, độ phân tán)
- Tổng hợp Toán thực tế từ ngân hàng 87 câu hỏi TikZ
"""

import math
import random
from fractions import Fraction

# ==============================================================================
# PHẦN 1: TOÁN THỰC TẾ HÌNH HỌC (GIẢI TAM GIÁC) DỰA THEO TOAN_10.PDF
# ==============================================================================

def k10_tln_tt_ham_xuyen_nui_tiet_kiem_xang():
    """
    Toan_10.pdf Đề 18 Câu 3:
    Ô tô đi từ A đến C qua ngọn núi phải đi hai đoạn AB và BC tạo góc ABC.
    Làm hầm xuyên núi chạy thẳng AC. Tính số tiền xăng tiết kiệm được.
    """
    AB = random.choice([120, 150, 160, 180, 200])
    BC = random.choice([180, 200, 220, 240, 250])
    B_deg = random.choice([120, 135])
    km_per_lit = random.choice([15, 20, 25])
    gia_xang = random.choice([20000, 22000, 24000, 25000])

    rad = math.radians(B_deg)
    AC = math.sqrt(AB**2 + BC**2 - 2 * AB * BC * math.cos(rad))
    km_cu = AB + BC
    km_tiet_kiem = km_cu - AC
    tien_tiet_kiem_dong = (km_tiet_kiem / km_per_lit) * gia_xang
    tien_nghin_dong = tien_tiet_kiem_dong / 1000
    dapan = f"{tien_nghin_dong:.1f}".replace(".", ",")

    gia_xang_fmt = f"{gia_xang:,}".replace(",", ".")
    caudan = rf"""\immini{{Một ô tô muốn đi từ $A$ đến $C$ nhưng giữa $A$ và $C$ là một ngọn núi cao nên ô tô phải đi thành hai đoạn từ $A$ đến $B$ rồi từ $B$ đến $C$. Các đoạn đường tạo thành tam giác $ABC$ có $AB = {AB}\text{{ km}}$, $BC = {BC}\text{{ km}}$ và $\widehat{{ABC}} = {B_deg}^\circ$ (tham khảo hình vẽ). Giả sử ô tô chạy {km_per_lit} km tốn một lít xăng, giá một lít xăng là {gia_xang_fmt} đồng. Nếu người ta làm một đoạn đường hầm xuyên núi chạy thẳng từ $A$ đến $C$, khi đó ô tô chạy trên con đường này sẽ tiết kiệm được bao nhiêu nghìn đồng tiền xăng so với chạy trên đường cũ (làm tròn kết quả đến hàng phần mười)?}}{{
\begin{{tikzpicture}}[scale=0.7, font=\footnotesize, line join=round, line cap=round, >=stealth]
    \coordinate (A) at (0,0);
    \coordinate (B) at (3,2);
    \coordinate (C) at (7,0.5);
    \draw[thick, blue] (A) -- (B) node[midway, above left] {{${AB}\text{{ km}}$}};
    \draw[thick, blue] (B) -- (C) node[midway, above right] {{${BC}\text{{ km}}$}};
    \draw[thick, dashed, red] (A) -- (C) node[midway, below] {{Đường hầm}};
    \fill[black] (A) circle (2pt) node[below left] {{$A$}};
    \fill[black] (B) circle (2pt) node[above] {{$B$}};
    \fill[black] (C) circle (2pt) node[below right] {{$C$}};
    \draw (2.6,1.7) arc (210:330:0.4);
    \node at (3,1.3) {{${B_deg}^\circ$}};
\end{{tikzpicture}}
}}"""

    loigiai = rf"""Áp dụng định lý côsin trong tam giác $ABC$:
$$AC^2 = AB^2 + BC^2 - 2AB \cdot BC \cos \widehat{{ABC}} = {AB}^2 + {BC}^2 - 2 \cdot {AB} \cdot {BC} \cdot \cos {B_deg}^\circ$$
$$\implies AC \approx {AC:.2f}\text{{ km}}.$$
Quãng đường đi theo đường cũ là:
$$S_{{cũ}} = AB + BC = {AB} + {BC} = {km_cu}\text{{ km}}.$$
Quãng đường tiết kiệm được là:
$$\Delta S = S_{{cũ}} - AC \approx {km_cu} - {AC:.2f} \approx {km_tiet_kiem:.2f}\text{{ km}}.$$
Lượng xăng tiết kiệm được:
$$\Delta V = \dfrac{{{km_tiet_kiem:.2f}}}{{{km_per_lit}}} \approx {km_tiet_kiem/km_per_lit:.3f}\text{{ lít}}.$$
Số tiền tiết kiệm được là:
$$\Delta T = {km_tiet_kiem/km_per_lit:.3f} \times {gia_xang} \approx {tien_tiet_kiem_dong:.0f}\text{{ đồng}} \approx {tien_nghin_dong:.1f}\text{{ nghìn đồng}}.$$"""

    return caudan, dapan, loigiai


def k10_tln_tt_quat_gio_canh_quat():
    """
    Toan_10.pdf Đề 16 Câu 2:
    Một người đứng cách thân quạt gió d mét nhìn thấy tâm cánh quạt với góc nâng alpha.
    Mắt người cách đất h0 mét. Tính khoảng cách từ tâm cánh quạt đến mặt đất (làm tròn đơn vị).
    """
    d = random.choice([16, 20, 24, 25, 30])
    alpha_deg = random.choice([70.5, 72.4, 75.6, 78.2])
    h0 = random.choice([1.6, 1.7, 1.65])

    h_tam = h0 + d * math.tan(math.radians(alpha_deg))
    dapan = str(round(h_tam))

    caudan = rf"""\immini{{Một người đứng cách thân một cái quạt gió ${d}\text{{ m}}$ và nhìn thấy tâm của cánh quạt với góc nâng ${str(alpha_deg).replace('.', ',')}^\circ$ (như hình vẽ). Biết khoảng cách từ mắt của người đó đến mặt đất là ${str(h0).replace('.', ',')}\text{{ m}}$, khoảng cách từ tâm của cánh quạt đến mặt đất bằng bao nhiêu mét (làm tròn kết quả đến hàng đơn vị)?}}{{
\begin{{tikzpicture}}[scale=0.6, font=\footnotesize, line join=round, line cap=round, >=stealth]
    \coordinate (O) at (0,0);
    \coordinate (M) at (0,1.7);
    \coordinate (C) at (4,0);
    \coordinate (T) at (4,5.5);
    \draw[thick] (-0.5,0) -- (5,0) node[right] {{Mặt đất}};
    \draw[thick, fill=gray!30] (3.8,0) rectangle (4.2,5.5);
    \draw[thick] (M) -- (4,1.7);
    \draw[thick, blue] (M) -- (T);
    \fill[black] (M) circle (2pt) node[left] {{Mắt}};
    \fill[red] (T) circle (3pt) node[above right] {{Tâm quạt}};
    \draw[<->] (0,-0.3) -- (4,-0.3) node[midway, below] {{${d}\text{{ m}}$}};
    \draw[<->] (-0.3,0) -- (-0.3,1.7) node[midway, left] {{${str(h0).replace('.', ',')}\text{{ m}}$}};
    \draw (0.8,1.7) arc (0:{alpha_deg/2}:0.8);
    \node at (1.5,2.1) {{${str(alpha_deg).replace('.', ',')}^\circ$}};
\end{{tikzpicture}}
}}"""

    loigiai = rf"""Gọi $T$ là tâm của cánh quạt gió, $M$ là vị trí mắt của người quan sát, $H$ là hình chiếu của $M$ lên trục thẳng đứng của quạt gió.
Ta có: $MH = {d}\text{{ m}}$, $\widehat{{TMH}} = {str(alpha_deg).replace('.', ',')}^\circ$.
Khoảng cách từ tâm quạt gió đến đường nằm ngang qua mắt người quan sát là:
$$TH = MH \cdot \tan {str(alpha_deg).replace('.', ',')}^\circ = {d} \cdot \tan {str(alpha_deg).replace('.', ',')}^\circ \approx {d * math.tan(math.radians(alpha_deg)):.2f}\text{{ m}}.$$
Khoảng cách từ tâm cánh quạt đến mặt đất là:
$$h = TH + h_0 \approx {d * math.tan(math.radians(alpha_deg)):.2f} + {str(h0).replace('.', ',')} \approx {h_tam:.2f} \approx {dapan}\text{{ m}}.$$"""

    return caudan, dapan, loigiai


def k10_tln_tt_cay_tren_suon_doi():
    """
    Toan_10.pdf Đề 15 Câu 2:
    Trên sườn đồi có một cái cây thẳng đứng đổ bóng dài AB = L m xuống đồi.
    Góc nghiêng của đồi là alpha, góc tia nắng qua ngọn cây là beta.
    Tính chiều cao BC của cây.
    """
    L = random.choice([15.5, 18.5, 20.0, 22.5])
    alpha = random.choice([25, 26, 28, 30])
    beta = random.choice([50, 54, 55, 60])

    # Tam giác ABC:
    # A là điểm bóng, B là gốc cây trên đồi, C là ngọn cây (BC vuông góc ngang)
    # Góc tại A: beta - alpha
    # Góc tại C: 90 - beta
    goc_A = beta - alpha
    goc_C = 90 - beta
    BC = L * math.sin(math.radians(goc_A)) / math.sin(math.radians(goc_C))
    dapan = f"{BC:.1f}".replace(".", ",")

    caudan = rf"""\immini{{Trên sườn đồi có một cái cây thẳng đứng đổ bóng dài $AB = {str(L).replace('.', ',')}\text{{ m}}$ xuống đồi. Biết góc nghiêng của sườn đồi là $\alpha = {alpha}^\circ$ so với phương nằm ngang và góc nghiêng của tia nắng mặt trời đi qua ngọn cây là $\beta = {beta}^\circ$ (tham khảo hình vẽ). Giả sử cây mọc thẳng đứng vuông góc với mặt phẳng nằm ngang, chiều cao $BC$ của cây bằng bao nhiêu mét (làm tròn kết quả đến hàng phần mười)?}}{{
\begin{{tikzpicture}}[scale=0.7, font=\footnotesize, line join=round, line cap=round, >=stealth]
    \coordinate (O) at (0,0);
    \coordinate (A) at (1,0.5);
    \coordinate (B) at (4,2);
    \coordinate (C) at (4,4.2);
    \draw[thick] (0,0) -- (6,0) node[right] {{Phương ngang}};
    \draw[thick, brown] (0,0) -- (5,2.5) node[right] {{Sườn đồi}};
    \draw[very thick, green!50!black] (B) -- (C) node[midway, right] {{Cây}};
    \draw[dashed, yellow!70!orange, thick] (C) -- (A);
    \fill[black] (A) circle (2pt) node[below left] {{$A$}};
    \fill[black] (B) circle (2pt) node[below right] {{$B$}};
    \fill[black] (C) circle (2pt) node[above] {{$C$}};
    \draw (1.5,0) arc (0:{alpha}:1.5);
    \node at (1.8,0.3) {{$\alpha$}};
    \draw (2,0) arc (0:{beta}:2);
    \node at (2.4,0.8) {{$\beta$}};
\end{{tikzpicture}}
}}"""

    loigiai = rf"""Xét tam giác $ABC$:
- Điểm $A$ là bóng của ngọn cây trên sườn đồi, $B$ là gốc cây, $C$ là ngọn cây.
- Vì sườn đồi nghiêng góc $\alpha = {alpha}^\circ$ và tia nắng mặt trời nghiêng góc $\beta = {beta}^\circ$ so với phương ngang nên góc tại $A$ của tam giác $ABC$ là:
$$\widehat{{BAC}} = \beta - \alpha = {beta}^\circ - {alpha}^\circ = {goc_A}^\circ.$$
- Vì cây thẳng đứng (vuông góc với phương nằm ngang) và tia nắng nghiêng góc $\beta = {beta}^\circ$ so với phương nằm ngang nên:
$$\widehat{{BCA}} = 90^\circ - \beta = 90^\circ - {beta}^\circ = {goc_C}^\circ.$$
Áp dụng định lý sin trong tam giác $ABC$:
$$\dfrac{{BC}}{{\sin \widehat{{BAC}}}} = \dfrac{{AB}}{{\sin \widehat{{BCA}}}} \iff BC = \dfrac{{AB \cdot \sin {goc_A}^\circ}}{{\sin {goc_C}^\circ}} = \dfrac{{{str(L).replace('.', ',')} \cdot \sin {goc_A}^\circ}}{{\sin {goc_C}^\circ}} \approx {BC:.2f}\text{{ m}}.$$
Làm tròn đến hàng phần mười, chiều cao cây là ${dapan}\text{{ m}}$."""

    return caudan, dapan, loigiai


def k10_tln_tt_chieu_cao_thap_giac_ke():
    """
    Toan_10.pdf Đề 16 Câu 1:
    Tòa tháp được rào lại. Giác kế tại A đo góc alpha, tiến thẳng d mét đến B đo góc beta.
    Tính chiều cao h của tháp (làm tròn hàng phần mười).
    """
    d = random.choice([20, 25, 30, 40])
    alpha = random.choice([18, 20, 24, 25])
    beta = random.choice([31, 35, 38, 42])

    goc_T = beta - alpha
    BT = d * math.sin(math.radians(alpha)) / math.sin(math.radians(goc_T))
    h = BT * math.sin(math.radians(beta))
    dapan = f"{h:.1f}".replace(".", ",")

    caudan = rf"""\immini{{Một tòa tháp cổ được rào chắn xung quanh để bảo tồn. Để tìm chiều cao $CT$ của tháp (như hình vẽ), người đo sử dụng giác kế đặt tại điểm $A$ và đo được góc nhìn lên đỉnh tháp là $\widehat{{CAT}} = {alpha}^\circ$. Sau đó người đo tiến thẳng ${d}\text{{ mét}}$ về phía chân tháp đến điểm $B$ và đo được góc nhìn là $\widehat{{CBT}} = {beta}^\circ$. Chiều cao của tháp bằng bao nhiêu mét (làm tròn kết quả đến hàng phần mười)?}}{{
\begin{{tikzpicture}}[scale=0.7, font=\footnotesize, line join=round, line cap=round, >=stealth]
    \coordinate (C) at (5,0);
    \coordinate (T) at (5,3.2);
    \coordinate (A) at (0,0);
    \coordinate (B) at (2.2,0);
    \draw[thick] (-0.5,0) -- (6,0);
    \draw[very thick, brown] (4.8,0) rectangle (5.2,3.2);
    \draw[thick, blue] (A) -- (T);
    \draw[thick, red] (B) -- (T);
    \fill[black] (A) circle (2pt) node[below] {{$A$}};
    \fill[black] (B) circle (2pt) node[below] {{$B$}};
    \fill[black] (C) circle (2pt) node[below] {{$C$}};
    \fill[black] (T) circle (2pt) node[above] {{$T$}};
    \draw[<->] (0,-0.3) -- (2.2,-0.3) node[midway, below] {{${d}\text{{ m}}$}};
    \draw (0.6,0) arc (0:{alpha}:0.6);
    \node at (0.9,0.2) {{${alpha}^\circ$}};
    \draw (2.6,0) arc (0:{beta}:0.4);
    \node at (2.9,0.3) {{${beta}^\circ$}};
\end{{tikzpicture}}
}}"""

    loigiai = rf"""Xét tam giác $ABT$:
- Góc ngoài tại đỉnh $B$ là $\widehat{{CBT}} = {beta}^\circ \implies \widehat{{ATB}} = {beta}^\circ - {alpha}^\circ = {goc_T}^\circ$.
Áp dụng định lý sin trong tam giác $ABT$:
$$\dfrac{{BT}}{{\sin \widehat{{BAT}}}} = \dfrac{{AB}}{{\sin \widehat{{ATB}}}} \implies BT = \dfrac{{{d} \cdot \sin {alpha}^\circ}}{{\sin {goc_T}^\circ}} \approx {BT:.2f}\text{{ m}}.$$
Trong tam giác vuông $BCT$ tại $C$:
$$CT = BT \cdot \sin {beta}^\circ \approx {BT:.2f} \cdot \sin {beta}^\circ \approx {h:.2f}\text{{ m}}.$$
Vậy chiều cao của tháp xấp xỉ bằng ${dapan}\text{{ m}}$."""

    return caudan, dapan, loigiai


# ==============================================================================
# PHẦN 2: TOÁN THỰC TẾ ỨNG DỤNG VECTƠ DỰA THEO TOAN_10.PDF
# ==============================================================================

def k10_tln_tt_hop_luc_hai_luc():
    """
    Toan_10.pdf Đề 41 Câu 1 & Đề 27 Câu 1:
    Hai lực F1, F2 cùng tác dụng vào chất điểm M tạo góc alpha.
    Tính cường độ lực tổng hợp F = F1 + F2 (làm tròn đơn vị Newton).
    """
    F1 = random.choice([100, 120, 150, 160, 200, 240])
    F2 = random.choice([100, 120, 150, 180, 200])
    alpha = random.choice([45, 60, 90, 120])

    rad = math.radians(alpha)
    F = math.sqrt(F1**2 + F2**2 + 2 * F1 * F2 * math.cos(rad))
    dapan = str(round(F))

    caudan = rf"""\immini{{Cho hai lực $\vec{{F}}_1, \vec{{F}}_2$ cùng tác dụng vào một chất điểm $M$. Biết cường độ lực $\vec{{F}}_1$ bằng ${F1}\text{{ N}}$, cường độ lực $\vec{{F}}_2$ bằng ${F2}\text{{ N}}$ và góc tạo bởi hai lực $\vec{{F}}_1, \vec{{F}}_2$ bằng ${alpha}^\circ$. Gọi $\vec{{F}} = \vec{{F}}_1 + \vec{{F}}_2$ là lực tổng hợp tác động vào chất điểm $M$. Cường độ của lực tổng hợp $\vec{{F}}$ bằng bao nhiêu Newton (làm tròn kết quả đến hàng đơn vị)?}}{{
\begin{{tikzpicture}}[scale=0.7, font=\footnotesize, line join=round, line cap=round, >=stealth]
    \coordinate (M) at (0,0);
    \coordinate (F1) at (3,0);
    \coordinate (F2) at ({2.5*math.cos(rad)},{2.5*math.sin(rad)});
    \coordinate (F) at ($(F1)+(F2)$);
    \draw[->, thick, blue] (M) -- (F1) node[below] {{$\vec{{F}}_1$}};
    \draw[->, thick, green!60!black] (M) -- (F2) node[above left] {{$\vec{{F}}_2$}};
    \draw[dashed] (F1) -- (F) -- (F2);
    \draw[->, very thick, red] (M) -- (F) node[above right] {{$\vec{{F}}$}};
    \fill[black] (M) circle (2pt) node[below left] {{$M$}};
    \draw (0.6,0) arc (0:{alpha}:0.6);
    \node at (0.9,0.3) {{${alpha}^\circ$}};
\end{{tikzpicture}}
}}"""

    loigiai = rf"""Theo quy tắc hình bình hành, lực tổng hợp tác dụng vào chất điểm $M$ là $\vec{{F}} = \vec{{F}}_1 + \vec{{F}}_2$.
Bình phương vô hướng hai vế:
$$|\vec{{F}}|^2 = (\vec{{F}}_1 + \vec{{F}}_2)^2 = |\vec{{F}}_1|^2 + |\vec{{F}}_2|^2 + 2 |\vec{{F}}_1| |\vec{{F}}_2| \cos(\vec{{F}}_1, \vec{{F}}_2)$$
$$|\vec{{F}}|^2 = {F1}^2 + {F2}^2 + 2 \cdot {F1} \cdot {F2} \cdot \cos {alpha}^\circ$$
$$\implies |\vec{{F}}| = \sqrt{{{F1**2 + F2**2} + 2 \cdot {F1*F2} \cdot \cos {alpha}^\circ}} \approx {F:.2f}\text{{ N}}.$$
Làm tròn đến hàng đơn vị, cường độ lực tổng hợp bằng ${dapan}\text{{ N}}$."""

    return caudan, dapan, loigiai


def k10_tln_tt_ba_luc_can_bang():
    """
    Toan_10.pdf Đề 30 Câu 3 & Đề 21 Câu 2:
    Ba lực F1 = MA, F2 = MB, F3 = MC cùng tác động vào vật tại điểm M và vật đứng yên.
    Cường độ F1, F2 và góc giữa F1, F2. Tính cường độ của lực F3 (làm tròn hàng phần mười).
    """
    F1 = random.choice([40, 50, 60, 80, 100])
    F2 = F1  # Thường bằng nhau hoặc tùy biến
    alpha = random.choice([60, 90, 120])

    rad = math.radians(alpha)
    # Vì F1 + F2 + F3 = 0 => F3 = - (F1 + F2) => |F3| = |F1 + F2|
    F3 = math.sqrt(F1**2 + F2**2 + 2 * F1 * F2 * math.cos(rad))
    dapan = f"{F3:.1f}".replace(".", ",")

    caudan = rf"""\immini{{Cho ba lực $\vec{{F}}_1 = \vec{{MA}}, \vec{{F}}_2 = \vec{{MB}}, \vec{{F}}_3 = \vec{{MC}}$ cùng tác động vào một vật tại điểm $M$ và vật đứng yên cân bằng. Cho biết cường độ của $\vec{{F}}_1, \vec{{F}}_2$ đều bằng ${F1}\text{{ N}}$ và $\widehat{{AMB}} = {alpha}^\circ$. Cường độ lực của lực $\vec{{F}}_3$ bằng bao nhiêu Newton (kết quả làm tròn đến hàng phần mười)?}}{{
\begin{{tikzpicture}}[scale=0.7, font=\footnotesize, line join=round, line cap=round, >=stealth]
    \coordinate (M) at (0,0);
    \coordinate (A) at ({2*math.cos(rad/2)},{2*math.sin(rad/2)});
    \coordinate (B) at ({2*math.cos(-rad/2)},{2*math.sin(-rad/2)});
    \coordinate (C) at ({-2*math.cos(0)},0);
    \draw[->, thick, blue] (M) -- (A) node[above right] {{$\vec{{F}}_1$}};
    \draw[->, thick, blue] (M) -- (B) node[below right] {{$\vec{{F}}_2$}};
    \draw[->, very thick, red] (M) -- (C) node[left] {{$\vec{{F}}_3$}};
    \fill[black] (M) circle (2pt) node[below] {{$M$}};
    \draw (0.5,-0.2) arc (-{alpha/2}:{alpha/2}:0.5);
    \node at (0.8,0) {{${alpha}^\circ$}};
\end{{tikzpicture}}
}}"""

    loigiai = rf"""Vì vật đứng yên cân bằng dưới tác dụng của ba lực nên:
$$\vec{{F}}_1 + \vec{{F}}_2 + \vec{{F}}_3 = \vec{{0}} \iff \vec{{F}}_3 = -(\vec{{F}}_1 + \vec{{F}}_2).$$
Do đó:
$$|\vec{{F}}_3| = |\vec{{F}}_1 + \vec{{F}}_2| = \sqrt{{|\vec{{F}}_1|^2 + |\vec{{F}}_2|^2 + 2 |\vec{{F}}_1| |\vec{{F}}_2| \cos \widehat{{AMB}}}}.$$
Thay số vào ta được:
$$|\vec{{F}}_3| = \sqrt{{{F1}^2 + {F2}^2 + 2 \cdot {F1} \cdot {F2} \cdot \cos {alpha}^\circ}} \approx {F3:.2f}\text{{ N}}.$$
Vậy cường độ của lực $\vec{{F}}_3$ bằng ${dapan}\text{{ N}}$."""

    return caudan, dapan, loigiai


def k10_tln_tt_chuyen_dong_tau_thuy_oxy():
    """
    Toan_10.pdf Đề 43 Câu 2:
    Chuyển động của một tàu thủy mô hình hóa trên Oxy: khởi hành từ A(x0; y0),
    chuyển động thẳng đều với vận tốc v = (vx; vy) km/h.
    B(x; y) là vị trí của tàu sau t giờ. Tính x * y.
    """
    x0 = random.randint(1, 4)
    y0 = random.randint(1, 4)
    vx = random.randint(2, 5)
    vy = random.randint(2, 5)
    t = random.randint(2, 4)

    xB = x0 + vx * t
    yB = y0 + vy * t
    ans_val = xB * yB
    dapan = str(ans_val)

    caudan = rf"""Sự chuyển động của một tàu thủy được mô hình hóa trên mặt phẳng tọa độ $Oxy$ như sau: Tàu khởi hành từ vị trí $A({x0}; {y0})$, chuyển động thẳng đều với vận tốc (tính theo đơn vị km/h) được biểu thị bởi vectơ $\vec{{v}} = ({vx}; {vy})$. Gọi $B(x; y)$ là vị trí của tàu tại thời điểm sau khi tàu khởi hành ${t}\text{{ giờ}}$. Giá trị của biểu thức tích $x \cdot y$ bằng bao nhiêu?"""

    loigiai = rf"""Sau ${t}$ giờ, vectơ độ dời của tàu thủy là:
$$\vec{{AB}} = t \cdot \vec{{v}} = {t} \cdot ({vx}; {vy}) = ({vx * t}; {vy * t}).$$
Gọi tọa độ điểm $B$ là $(x; y)$. Ta có:
$$\vec{{AB}} = (x - {x0}; y - {y0}) = ({vx * t}; {vy * t}) \implies \begin{{cases}} x - {x0} = {vx * t} \\ y - {y0} = {vy * t} \end{{cases}} \implies \begin{{cases}} x = {xB} \\ y = {yB} \end{{cases}}.$$
Vậy vị trí của tàu sau ${t}$ giờ là $B({xB}; {yB})$.
Giá trị của biểu thức tích $x \cdot y$ là:
$$x \cdot y = {xB} \cdot {yB} = {dapan}.$$"""

    return caudan, dapan, loigiai


# ==============================================================================
# PHẦN 3: CÁC DẠNG TOÁN LỚP 10 THEO TOAN_10.PDF (CHƯƠNG 1, 2, 4, 5)
# ==============================================================================

def k10_tln_c1_b1_tinh_dung_sai_menh_de():
    """Toan_10.pdf Đề 1: Đếm số mệnh đề đúng trong các khẳng định số học, logic"""
    items = [
        ("Số 2024 chia hết cho 4.", True),
        (r"$\sqrt{2}$ là một số hữu tỉ.", False),
        ("Số 17 là một số nguyên tố.", True),
        (r"$\forall x \in \mathbb{R}, x^2 + 1 > 0$.", True),
        (r"$\exists x \in \mathbb{R}, x^2 < 0$.", False),
        ("Một tứ giác có hai đường chéo bằng nhau là hình chữ nhật.", False),
        (r"Nếu một số chia hết cho 9 thì số đó chia hết cho 3.", True),
        (r"Tổng của hai số nguyên lẻ là một số lẻ.", False)
    ]
    chosen = random.sample(items, 4)
    so_dung = sum(1 for _, val in chosen if val)
    dapan = str(so_dung)

    caudan = r"""Trong các mệnh đề sau, có bao nhiêu mệnh đề đúng?
""" + "\n".join([f"• ({chr(65+i)}) {text}" for i, (text, _) in enumerate(chosen)])

    loigiai = r"""Xét tính đúng sai của từng mệnh đề:
""" + "\n".join([f"• ({chr(65+i)}) {'ĐÚNG' if val else 'SAI'}." for i, (_, val) in enumerate(chosen)]) + f"\nVậy có tất cả ${dapan}$ mệnh đề đúng."

    return caudan, dapan, loigiai


def k10_tln_c1_b2_so_tap_con():
    """Toan_10.pdf Đề 3 Câu 2: Tìm số tập con k phần tử của tập hợp n phần tử"""
    n = random.randint(5, 7)
    k = random.randint(2, 4)
    # Tổ hợp C_n^k
    ans = math.comb(n, k)
    dapan = str(ans)

    elements = ", ".join(str(i) for i in range(1, n + 1))
    caudan = rf"""Cho tập hợp $A = \{{{elements}\}}$ gồm ${n}$ phần tử. Có bao nhiêu tập con của $A$ chứa đúng ${k}$ phần tử?"""

    loigiai = rf"""Số tập con gồm ${k}$ phần tử của tập hợp $A$ có ${n}$ phần tử chính là số tổ hợp chập ${k}$ của ${n}$ phần tử:
$$C_{{{n}}}^{{{k}}} = \dfrac{{{n}!}}{{{k}!({n} - {k})!}} = {ans}.$$
Vậy có ${dapan}$ tập con thỏa mãn."""

    return caudan, dapan, loigiai


def k10_tln_c1_b3_phep_toan_khoang_doan():
    """Toan_10.pdf Đề 43 Câu 1: Cho A = [-m; n), B = {x | x^2 - 4 < 0}. Tìm A \ B = [a; b], tính a^2 - b^2"""
    m = random.randint(3, 6)
    k = 2  # B = (-2; 2)
    # A = [-m; 1), B = (-2; 2) => A \ B = [-m; -2]
    # a = -m, b = -2
    a_val = -m
    b_val = -k
    ans_val = a_val**2 - b_val**2
    dapan = str(ans_val)

    caudan = rf"""Cho các tập hợp $A = [{-m}; 1)$ và $B = ({-k}; {k})$. Biết $A \setminus B = [a; b]$. Giá trị của biểu thức $P = a^2 - b^2$ bằng bao nhiêu?"""

    loigiai = rf"""Ta có:
- Tập hợp $A = [{-m}; 1)$.
- Tập hợp $B = ({-k}; {k})$.
Khi đó hiệu của hai tập hợp là:
$$A \setminus B = [{-m}; 1) \setminus ({-k}; {k}) = [{-m}; {-k}].$$
Do đó $a = {-m}$ và $b = {-k}$.
Giá trị của biểu thức $P$ là:
$$P = a^2 - b^2 = ({-m})^2 - ({-k})^2 = {m**2} - {k**2} = {ans_val}.$$"""

    return caudan, dapan, loigiai


def k10_tln_c1_b3_toan_venn_thuc_te():
    """Toan_10.pdf Đề 3 Câu 4: Bài toán Venn 3 tập hợp học sinh giỏi các môn"""
    # Lớp có N em giỏi ít nhất 1 môn.
    total = random.choice([34, 35, 40])
    TV = random.randint(7, 9)
    VA = random.randint(6, 8)
    TA = random.randint(5, 7)
    both_all = random.randint(2, 4)

    # Giỏi Toán và Văn nhưng không giỏi Anh = TV - both_all
    # Giỏi đúng 1 môn = total - (TV + VA + TA - 2*both_all)
    overlap = (TV - both_all) + (VA - both_all) + (TA - both_all) + both_all
    dung_1_mon = total - overlap
    dapan = str(dung_1_mon)

    caudan = rf"""Lớp 10A có ${total}$ học sinh giỏi ít nhất một trong ba môn Toán, Ngữ văn, Tiếng Anh. Có ${TV}$ học sinh giỏi đồng thời Toán và Văn, ${VA}$ học sinh giỏi đồng thời Văn và Anh, ${TA}$ học sinh giỏi đồng thời Toán và Anh; trong mỗi số liệu trên đều đã tính cả các học sinh giỏi cả ba môn. Biết có đúng ${both_all}$ học sinh giỏi cả ba môn. Hỏi có bao nhiêu học sinh chỉ giỏi đúng một môn trong ba môn trên?"""

    loigiai = rf"""Theo công thức sơ đồ Venn cho ba tập hợp:
- Số học sinh giỏi ít nhất 2 môn:
$$N_{{2+}} = ({TV} - {both_all}) + ({VA} - {both_all}) + ({TA} - {both_all}) + {both_all} = {overlap}.$$
- Số học sinh chỉ giỏi đúng 1 môn là:
$$N_{{1}} = N_{{\text{{tổng}}}} - N_{{2+}} = {total} - {overlap} = {dung_1_mon}.$$
Vậy có ${dapan}$ học sinh chỉ giỏi đúng một môn."""

    return caudan, dapan, loigiai


def k10_tln_c2_b4_mien_nghiem_bpt():
    """Toan_10.pdf Đề 7 Câu 1: Xác định tham số a từ miền nghiệm trên Oxy"""
    # BPT: 2x - y <= a hoặc x + 2y <= a, đường thẳng đi qua (x0, 0)
    x0 = random.randint(2, 5)
    # đường thẳng 2x - y = 2*x0 => a = 2*x0
    a_val = 2 * x0
    dapan = str(a_val)

    caudan = rf"""\immini{{Miền nghiệm của bất phương trình $2x - y \le a$ là nửa mặt phẳng chứa gốc tọa độ $O(0; 0)$ có bờ là đường thẳng $d$ cắt trục hoành tại điểm $A({x0}; 0)$ (như hình vẽ bên). Tìm giá trị của $a$.}}{{
\begin{{tikzpicture}}[scale=0.6, font=\footnotesize, line join=round, line cap=round, >=stealth]
    \draw[->] (-1,0) -- (4.5,0) node[right] {{$x$}};
    \draw[->] (0,-3) -- (0,3) node[above] {{$y$}};
    \fill (0,0) circle (1.5pt) node[below left] {{$O$}};
    \fill ({x0},0) circle (1.5pt) node[below right] {{$A({x0};0)$}};
    \draw[thick, blue] ({x0-1},-2) -- ({x0+1},2) node[above right] {{$d$}};
    \fill[pattern=north west lines, opacity=0.3] ({x0-1},-2) -- ({x0+1},2) -- (4.5,2) -- (4.5,-2) -- cycle;
\end{{tikzpicture}}
}}"""

    loigiai = rf"""Đường thẳng bờ $d$ có phương trình dạng: $2x - y = a$.
Vì $d$ đi qua điểm $A({x0}; 0)$ nên tọa độ điểm $A$ thỏa mãn phương trình đường thẳng:
$$2 \cdot {x0} - 0 = a \iff a = {a_val}.$$
Kiểm tra với gốc tọa độ $O(0; 0)$: $2 \cdot 0 - 0 = 0 \le {a_val}$ (đúng), phù hợp với miền nghiệm chứa gốc tọa độ.
Vậy $a = {dapan}$."""

    return caudan, dapan, loigiai


def k10_tln_c2_b5_quy_hoach_tuyen_tinh():
    """Toan_10.pdf Đề 11 Câu 3: Tối ưu lợi nhuận sản xuất hai loại sản phẩm A và B"""
    t1 = random.choice([2, 3])
    t2 = random.choice([3, 4])
    T_max = random.choice([60, 72, 80])
    lai_A = 100
    lai_B = 150

    # Max F = 100x + 150y s.t. t1*x + t2*y <= T_max, x >= 0, y >= 0
    # Đỉnh (0, T_max/t2) hoặc (T_max/t1, 0)
    # Lãi tại (0, T_max//t2) và (T_max//t1, 0)
    val1 = (T_max // t1) * lai_A
    val2 = (T_max // t2) * lai_B
    max_lai = max(val1, val2)
    dapan = str(max_lai)

    caudan = rf"""Một xưởng sản xuất hai loại sản phẩm $A$ và $B$. Lợi nhuận từ mỗi sản phẩm loại $A$ là ${lai_A}\text{{ nghìn đồng}}$, từ mỗi sản phẩm loại $B$ là ${lai_B}\text{{ nghìn đồng}}$. Để sản xuất một sản phẩm loại $A$ cần ${t1}\text{{ giờ}}$ lao động, một sản phẩm loại $B$ cần ${t2}\text{{ giờ}}$ lao động. Tổng quỹ thời gian lao động của xưởng không vượt quá ${T_max}\text{{ giờ}}$. Lợi nhuận lớn nhất mà xưởng có thể đạt được là bao nhiêu nghìn đồng?"""

    loigiai = rf"""Gọi $x, y \ge 0$ lần lượt là số lượng sản phẩm loại $A$ và loại $B$ cần sản xuất ($x, y \in \mathbb{{N}}$).
Ta có hệ bất phương trình ràng buộc:
$$\begin{{cases}} {t1}x + {t2}y \le {T_max} \\ x \ge 0 \\ y \ge 0 \end{{cases}}$$
Hàm mục tiêu biểu diễn lợi nhuận (nghìn đồng):
$$F(x, y) = {lai_A}x + {lai_B}y.$$
Xét các điểm cực biên:
- Nếu chỉ sản xuất sản phẩm $A$ ($y = 0$): $x \le \dfrac{{{T_max}}}{{{t1}}} = {T_max // t1} \implies F = {T_max // t1} \times {lai_A} = {val1}\text{{ nghìn đồng}}.$
- Nếu chỉ sản xuất sản phẩm $B$ ($x = 0$): $y \le \dfrac{{{T_max}}}{{{t2}}} = {T_max // t2} \implies F = {T_max // t2} \times {lai_B} = {val2}\text{{ nghìn đồng}}.$
So sánh hai giá trị, lợi nhuận lớn nhất đạt được là ${dapan}\text{{ nghìn đồng}}$."""

    return caudan, dapan, loigiai


def k10_tln_c5_b14_tich_vo_huong_oxy():
    """Toan_10.pdf Đề 42 Câu 2: Tìm góc giữa hai vectơ u và v trong Oxy"""
    # Cho u = (-4; 3), v = (2; 4) => cos alpha = (-8 + 12) / (5 * sqrt(20)) = 4 / (10*sqrt(5)) => alpha approx 80 độ
    pairs = [
        ((-4, 3), (2, 4)),
        ((1, 2), (-3, 1)),
        ((3, -1), (2, 4)),
        ((2, 1), (-1, 3))
    ]
    u, v = random.choice(pairs)
    dot = u[0]*v[0] + u[1]*v[1]
    len_u = math.sqrt(u[0]**2 + u[1]**2)
    len_v = math.sqrt(v[0]**2 + v[1]**2)
    cos_val = dot / (len_u * len_v)
    angle_deg = math.degrees(math.acos(max(-1.0, min(1.0, cos_val))))
    dapan = str(round(angle_deg))

    caudan = rf"""Trong mặt phẳng tọa độ $Oxy$, cho hai vectơ $\vec{{u}} = ({u[0]}; {u[1]})$ và $\vec{{v}} = ({v[0]}; {v[1]})$. Góc giữa hai vectơ $\vec{{u}}$ và $\vec{{v}}$ bằng bao nhiêu độ (kết quả làm tròn đến hàng đơn vị)?"""

    loigiai = rf"""Tích vô hướng của hai vectơ là:
$$\vec{{u}} \cdot \vec{{v}} = ({u[0]}) \cdot ({v[0]}) + ({u[1]}) \cdot ({v[1]}) = {dot}.$$
Độ dài của hai vectơ:
$$|\vec{{u}}| = \sqrt{{{u[0]}^2 + {u[1]}^2}} = {len_u:.2f}, \quad |\vec{{v}}| = \sqrt{{{v[0]}^2 + {v[1]}^2}} = {len_v:.2f}.$$
Côsin của góc giữa hai vectơ:
$$\cos(\vec{{u}}, \vec{{v}}) = \dfrac{{\vec{{u}} \cdot \vec{{v}}}}{{|\vec{{u}}| \cdot |\vec{{v}}|}} = \dfrac{{{dot}}}{{{len_u:.2f} \times {len_v:.2f}}} \approx {cos_val:.4f}.$$
Suy ra góc giữa hai vectơ xấp xỉ bằng ${dapan}^\circ$."""

    return caudan, dapan, loigiai


def k10_tln_c5_sai_so_tuong_doi():
    """Toan_10.pdf Đề 42 Câu 4: Sai số tương đối của phép đo diện tích"""
    s0 = random.choice([1250.0, 1572.5, 2040.0, 3150.0])
    d = random.choice([1.5, 2.0, 2.5, 3.0])
    delta = (d / s0) * 100
    dapan = f"{delta:.2f}".replace(".", ",")

    caudan = rf"""Diện tích của một khu đất nông nghiệp được đo là $s = {str(s0).replace('.', ',')}\text{{ m}}^2 \pm {str(d).replace('.', ',')}\text{{ m}}^2$. Sai số tương đối của phép đo này là $a\%$. Giá trị của $a$ bằng bao nhiêu (kết quả làm tròn đến hàng phần trăm)?"""

    loigiai = rf"""Sai số tương đối của phép đo được tính theo công thức:
$$\delta_s \le \dfrac{{d}}{{|s_0|}} = \dfrac{{{str(d).replace('.', ',')}}}{{{str(s0).replace('.', ',')}}} \approx {d / s0:.6f} = {delta:.4f}\%.$$
Làm tròn đến hàng phần trăm, ta được $a \approx {dapan}$."""

    return caudan, dapan, loigiai


# ==============================================================================
# HÀM BỐC THĂM TỔNG HỢP TOÁN THỰC TẾ LỚP 10
# ==============================================================================

def k10_tln_toan_thuc_te_tong_hop_toan_pdf():
    """Bốc thăm ngẫu nhiên 1 câu thực tế hình học hoặc vectơ đặc sắc nhất từ Toan_10.pdf"""
    pool = [
        k10_tln_tt_ham_xuyen_nui_tiet_kiem_xang,
        k10_tln_tt_quat_gio_canh_quat,
        k10_tln_tt_cay_tren_suon_doi,
        k10_tln_tt_chieu_cao_thap_giac_ke,
        k10_tln_tt_hop_luc_hai_luc,
        k10_tln_tt_ba_luc_can_bang,
        k10_tln_tt_chuyen_dong_tau_thuy_oxy,
        k10_tln_c2_b5_quy_hoach_tuyen_tinh,
        k10_tln_c1_b3_toan_venn_thuc_te,
        k10_tln_c5_sai_so_tuong_doi,
    ]
    fn = random.choice(pool)
    return fn()


def k10_tln_c1_b1_menh_de_chua_bien():
    """Toan_10.pdf Đề 1 Câu 3: Mệnh đề chứa biến P(x), tìm x để mệnh đề đúng"""
    a = random.choice([2, 3, 4])
    b = a**2
    # P(x): x^2 - b <= 0 với x nguyên
    # Tập nghiệm [-a, a], có 2a + 1 giá trị nguyên
    so_nghiem = 2 * a + 1
    dapan = str(so_nghiem)
    
    caudan = rf"""Cho mệnh đề chứa biến (x): 	ext{{}}x^2 - {b} \le 0	ext{{''}}$ với  \in \mathbb{{Z}}$. Có bao nhiêu giá trị nguyên của $ để mệnh đề (x)$ trở thành một mệnh đề đúng?"""
    
    loigiai = rf"""Bất phương trình ^2 - {b} \le 0 \iff -{a} \le x \le {a}$.
Vì  \in \mathbb{{Z}}$ nên  \in \{{{-a}, \ldots, {a}\}}$.
Số giá trị nguyên thỏa mãn là:
30171({a}) - ({-a}) + 1 = {so_nghiem}.30171
Vậy có tất cả $ giá trị nguyên của $ để mệnh đề đúng."""
    return caudan, dapan, loigiai


def k10_tln_c1_b2_tim_m_tap_con():
    """Toan_10.pdf Đề 3 Câu 3: Tìm m nguyên để A con B"""
    # A = [m; m + 3], B = (1; 10)
    # A con B <=> 1 < m và m + 3 < 10 <=> 1 < m < 7 => m in {2, 3, 4, 5, 6}
    left_B = 1
    right_B = random.choice([9, 10, 11])
    diff = random.choice([3, 4])
    
    # m > left_B and m + diff < right_B
    m_min = left_B + 1
    m_max = right_B - diff - 1
    count = max(0, m_max - m_min + 1)
    dapan = str(count)
    
    caudan = rf"""Cho hai tập hợp  = [m; m + {diff}]$ và  = ({left_B}; {right_B})$. Có bao nhiêu giá trị nguyên của tham số $ để tập hợp $ là tập con của tập hợp $ ( \subset B$)?"""
    
    loigiai = rf"""Để  \subset B$, ta cần có:
30171egin{{cases}} m > {left_B} \ m + {diff} < {right_B} \end{{cases}} \iff egin{{cases}} m \ge {m_min} \ m \le {m_max} \end{{cases}} \iff {m_min} \le m \le {m_max}.30171
Vì  \in \mathbb{{Z}}$ nên  \in \{{{m_min}, \ldots, {m_max}\}}$.
Số giá trị nguyên của $ là:
30171{m_max} - {m_min} + 1 = {count}.30171
Vậy có tất cả $ giá trị nguyên của $."""
    return caudan, dapan, loigiai


def k10_tln_c5_b11_so_vecto_luc_giac_deu():
    """Toan_10.pdf Đề 30 Câu 1: Cho lục giác đều ABCDEF tâm O, đếm số vectơ bằng một vectơ cho trước"""
    # Cho lục giác đều ABCDEF tâm O. Có bao nhiêu vectơ bằng BA có điểm đầu và điểm cuối thuộc 7 điểm
    # BA cùng hướng và cùng độ dài với: CO, OF, DE. Vậy có đúng 3 vectơ bằng BA: CO, OF, DE (không tính chính nó nếu hỏi khác BA, hoặc tính nếu hỏi có bao nhiêu vectơ bằng BA)
    # Trong Toan_10.pdf: Đề 30 Câu 1 hỏi: Có bao nhiêu vectơ bằng BA có điểm đầu và cuối thuộc 7 điểm A, B, C, D, E, F, O (kể cả chính nó là 3 vectơ khác: CO, OF, DE). Đáp án = 3.
    dapan = "3"
    caudan = r"""Cho lục giác đều $ tâm $. Có bao nhiêu vectơ khác vectơ $ec{BA}$ nhưng bằng vectơ $ec{BA}$ mà điểm đầu và điểm cuối thuộc tập hợp $ điểm $\{A, B, C, D, E, F, O\}0"""
    loigiai = r"""Theo tính chất của hình lục giác đều $ tâm $:
Các đoạn thẳng song song và bằng đoạn $ là: $, $, $.
Các vectơ có cùng hướng và cùng độ dài với vectơ $ec{BA}$ (khác $ec{BA}$) là:
30171ec{CO}, \quad ec{OF}, \quad ec{DE}.30171
Vậy có tất cả $ vectơ thỏa mãn."""
    return caudan, dapan, loigiai


def k10_tln_c5_b11_do_dai_vecto_hinh_vuong():
    """Toan_10.pdf Đề 38 Câu 1: Cho hình vuông ABCD cạnh a, tính độ dài vectơ"""
    a = random.choice([4, 6, 8, 10])
    # |AB + AD| = |AC| = a * sqrt(2)
    ans = round(a * math.sqrt(2), 2)
    dapan = f"{ans:.2f}".replace(".", ",")
    
    caudan = rf"""Cho hình vuông $ có cạnh bằng 	ext{{ cm}}$. Độ dài của vectơ tổng $ec{{u}} = ec{{AB}} + ec{{AD}}$ bằng bao nhiêu xentimét (kết quả làm tròn đến hàng phần trăm)?"""
    
    loigiai = rf"""Theo quy tắc hình bình hành áp dụng cho hình vuông $:
30171ec{{u}} = ec{{AB}} + ec{{AD}} = ec{{AC}}.30171
Độ dài của đường chéo hình vuông cạnh $ là:
30171|ec{{u}}| = AC = {a}\sqrt{{2}} pprox {ans}	ext{{ cm}}.30171
Vậy $|ec{{u}}| pprox {dapan}	ext{{ cm}}.30171
"""
    return caudan, dapan, loigiai


def k10_tln_c5_b12_quy_tac_hbh_tong_hieu():
    """Toan_10.pdf Đề 21: Cho hình chữ nhật ABCD có AB = a, AD = b, tính |AB + AD| và |AB - AD|"""
    a = random.choice([6, 8, 12])
    b = random.choice([5, 9, 16])
    diag = math.sqrt(a**2 + b**2)
    dapan = f"{diag:.1f}".replace(".", ",")
    
    caudan = rf"""Cho hình chữ nhật $ có cạnh  = {a}$,  = {b}$. Độ dài của vectơ hiệu $ec{{v}} = ec{{AB}} - ec{{AD}}$ bằng bao nhiêu (kết quả làm tròn đến hàng phần mười)?"""
    
    loigiai = rf"""Ta có:
30171ec{{v}} = ec{{AB}} - ec{{AD}} = ec{{DB}}.30171
Độ dài của vectơ $ec{{v}}$ là độ dài đoạn chéo $:
30171|ec{{v}}| = BD = \sqrt{{AB^2 + AD^2}} = \sqrt{{{a}^2 + {b}^2}} = \sqrt{{{a**2 + b**2}}} pprox {diag:.2f}.30171
Làm tròn đến hàng phần mười, kết quả là ."""
    return caudan, dapan, loigiai


def k10_tln_c5_b13_phan_tich_vecto():
    """Toan_10.pdf Đề 23: Phân tích một vectơ theo 2 vectơ không cùng phương"""
    dapan = "5"
    caudan = r"""Cho tam giác $. Gọi $ là điểm trên cạnh $ sao cho  = 2MC$. Giả sử vectơ $ec{AM}$ được phân tích theo hai vectơ $ec{AB}, ec{AC}$ dưới dạng $ec{AM} = x ec{AB} + y ec{AC}$ với , y \in \mathbb{R}$. Giá trị của biểu thức  = 3x + 6y$ bằng bao nhiêu?"""
    
    loigiai = r"""Vì $ nằm trên đoạn $ và  = 2MC$ nên:
\[ec{BM} = 2ec{MC} \iff ec{AM} - ec{AB} = 2(ec{AC} - ec{AM}) \iff 3ec{AM} = ec{AB} + 2ec{AC} \iff ec{AM} = \dfrac{1}{3}ec{AB} + \dfrac{2}{3}ec{AC}.\]
Do đó  = \dfrac{1}{3}$ và  = \dfrac{2}{3}$.
Giá trị của biểu thức $ là:
\[P = 3 \cdot \dfrac{1}{3} + 6 \cdot \dfrac{2}{3} = 1 + 4 = 5.\]
Vậy  = 5$."""
    return caudan, dapan, loigiai


def k10_tln_c5_b13_ba_diem_thang_hang():
    """Toan_10.pdf Đề 30 Câu 2: Tìm k để 3 điểm thẳng hàng"""
    dapan = "2,5"
    caudan = r"""Cho tam giác $. Gọi , N, P$ là các điểm thỏa mãn $ec{MA} + ec{MB} = ec{0}$, ec{NA} + 3ec{NC} = ec{0}$ và $ec{BC} = k ec{BP}$. Tìm $ để ba điểm , N, P$ thẳng hàng (kết quả viết dưới dạng số thập phân)?"""
    
    loigiai = r"""Chọn hệ vectơ gốc $:
- $ là trung điểm  \implies ec{AM} = \dfrac{1}{2}ec{AB}$.
- ec{NA} + 3ec{NC} = ec{0} \iff -2ec{AN} + 3(ec{AC} - ec{AN}) = ec{0} \implies ec{AN} = \dfrac{3}{5}ec{AC}$.
- $ec{BC} = kec{BP} \iff ec{AC} - ec{AB} = k(ec{AP} - ec{AB}) \implies ec{AP} = \left(1 - \dfrac{1}{k}ight)ec{AB} + \dfrac{1}{k}ec{AC}$.
Ta có:
\[ec{MN} = ec{AN} - ec{AM} = -\dfrac{1}{2}ec{AB} + \dfrac{3}{5}ec{AC}.\]
\[ec{MP} = ec{AP} - ec{AM} = \left(\dfrac{1}{2} - \dfrac{1}{k}ight)ec{AB} + \dfrac{1}{k}ec{AC}.\]
Để , N, P$ thẳng hàng thì $ec{MP}$ cùng phương với $ec{MN}$, suy ra tỉ số:
\[\dfrac{rac{1}{2} - rac{1}{k}}{-rac{1}{2}} = \dfrac{rac{1}{k}}{rac{3}{5}} \iff \dfrac{3}{5}\left(\dfrac{1}{2} - \dfrac{1}{k}ight) = -\dfrac{1}{2k} \iff \dfrac{3}{10} - \dfrac{3}{5k} = -\dfrac{1}{2k} \iff \dfrac{3}{10} = \dfrac{1}{10k} \iff k = \dfrac{5}{2} = 2{,}5.\]
Vậy  = 2{,}5$."""
    return caudan, dapan, loigiai


def k10_tln_c5_b14_vuong_goc_tich_vo_huong():
    """Toan_10.pdf Đề 27: Tìm tham số để 2 vectơ vuông góc"""
    k = random.randint(2, 5)
    u_y = random.randint(2, 4)
    ans = k
    dapan = str(ans)
    
    caudan = rf"""Trong mặt phẳng tọa độ $, cho hai vectơ $ec{{u}} = (m; {u_y})$ và $ec{{v}} = ({u_y}; -{k})$. Tìm giá trị của tham số $ để hai vectơ $ec{{u}}$ và $ec{{v}}$ vuông góc với nhau."""
    
    loigiai = rf"""Hai vectơ $ec{{u}}$ và $ec{{v}}$ vuông góc với nhau khi và chỉ khi tích vô hướng của chúng bằng /bin/zsh$:
\[ec{{u}} \cdot ec{{v}} = 0 \iff m \cdot {u_y} + {u_y} \cdot (-{k}) = 0 \iff {u_y}m - {u_y * k} = 0 \iff m = {ans}.\]
Vậy  = {dapan}$."""
    return caudan, dapan, loigiai



# -*- coding: utf-8 -*-
import math
import random
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

def shuffle_choices(correct_text, wrong_texts):
    opts = [(True, clean_option(correct_text))] + [(False, clean_option(w)) for w in wrong_texts]
    random.shuffle(opts)
    choices = []
    for is_correct, text in opts:
        if is_correct:
            choices.append(f"{{\\True {text}}}\n")
        else:
            choices.append(f"{{{text}}}\n")
    return choices

def make_tf_choices(items):
    choices = []
    loi_giai_parts = []
    for i, item in enumerate(items):
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
# PHẦN I: TRẮC NGHIỆM NHIỀU LỰA CHỌN (MC)
# ==============================================================================

def k10_mc_c1_b1_menh_de():
    """Chương 1 Bài 1: Mệnh đề, phủ định mệnh đề, mệnh đề với mọi/tồn tại"""
    mode = random.choice(["phu_dinh", "menh_de_chua_bien", "tinh_dung_sai"])
    if mode == "phu_dinh":
        a = random.randint(1, 5)
        P = rf"\forall x \in \mathbb{{R}}, x^2 + {a} > 0"
        correct = rf"$\exists x \in \mathbb{{R}}, x^2 + {a} \le 0$"
        wrongs = [
            rf"$\exists x \in \mathbb{{R}}, x^2 + {a} < 0$",
            rf"$\forall x \in \mathbb{{R}}, x^2 + {a} \le 0$",
            rf"$\exists x \in \mathbb{{R}}, x^2 + {a} > 0$"
        ]
        caudan = rf"Phủ định của mệnh đề $P: ``{P}\text{{''}}$ là"
        loigiai = rf"Phủ định của mệnh đề chứa ký hiệu $\forall$ là $\exists$, và phủ định của dấu $>$ là $\le$. Do đó phủ định của $P$ là $\overline{{P}}: ``{correct[1:-1]}\text{{''}}$."
    elif mode == "menh_de_chua_bien":
        x0 = random.randint(2, 6)
        val = x0**2 - 1
        caudan = rf"Cho mệnh đề chứa biến $P(x): ``x^2 - 1 = {val}\text{{''}}$. Với giá trị nào của $x$ dưới đây thì $P(x)$ là mệnh đề đúng?"
        correct = f"$x = {x0}$"
        wrongs = [f"$x = {x0 + 1}$", f"$x = {x0 - 1}$", f"$x = {x0 + 2}$"]
        loigiai = rf"Thay $x = {x0}$ vào phương trình: ${x0}^2 - 1 = {x0**2} - 1 = {val}$ (thỏa mãn). Vậy với $x = {x0}$ thì $P(x)$ là mệnh đề đúng."
    else:
        caudan = "Trong các mệnh đề sau, mệnh đề nào là mệnh đề \\textbf{đúng}?"
        correct = "Số $2$ là số nguyên tố chẵn duy nhất"
        wrongs = [
            "Tổng ba góc trong một tam giác bằng $360^\\circ$",
            "Mọi hình thoi đều là hình vuông",
            "Số $\\pi$ là một số hữu tỉ"
        ]
        loigiai = "Số 2 là số nguyên tố chẵn duy nhất (các số chẵn lớn hơn 2 đều chia hết cho 2 nên là hợp số). Các khẳng định còn lại đều sai."
    choices = shuffle_choices(correct, wrongs)
    return caudan, choices, loigiai

def k10_mc_c1_b2_tap_hop():
    """Chương 1 Bài 2: Liệt kê phần tử, số tập con"""
    mode = random.choice(["so_tap_con", "liet_ke"])
    if mode == "so_tap_con":
        n = random.randint(3, 5)
        num_sub = 2**n
        caudan = rf"Một tập hợp $A$ có {n} phần tử. Số tập con của tập hợp $A$ là"
        correct = f"${num_sub}$"
        wrongs = [f"${2**(n-1)}$", f"${n**2}$", f"${2*n}$"]
        loigiai = rf"Số tập con của một tập hợp có $n$ phần tử là $2^n = 2^{{{n}}} = {num_sub}$."
    else:
        x1, x2 = random.sample([-2, -1, 1, 2, 3, 4], 2)
        b = -(x1 + x2)
        c = x1 * x2
        sign_b = f"+ {b}" if b > 0 else f"- {-b}" if b < 0 else ""
        sign_c = f"+ {c}" if c > 0 else f"- {-c}"
        caudan = rf"Liệt kê các phần tử của tập hợp $X = \{{x \in \mathbb{{Z}} \mid x^2 {sign_b}x {sign_c} = 0\}}.$"
        correct = rf"$\{{{min(x1, x2)}; {max(x1, x2)}\}}$"
        wrongs = [
            rf"$\{{{min(-x1, -x2)}; {max(-x1, -x2)}\}}$",
            rf"$\{{{min(x1, x2)}\}}$",
            rf"$\{{{max(x1, x2)}\}}$"
        ]
        loigiai = rf"Phương trình $x^2 {sign_b}x {sign_c} = 0 \iff (x - {x1})(x - {x2}) = 0 \iff \left[\begin{{aligned}} x &= {x1} \\ x &= {x2} \end{{aligned}}\right.$. Vì cả hai nghiệm đều thuộc $\mathbb{{Z}}$ nên $X = \{{{min(x1, x2)}; {max(x1, x2)}\}}$."
    choices = shuffle_choices(correct, wrongs)
    return caudan, choices, loigiai

def k10_mc_c1_b3_phep_toan_tap_hop():
    """Chương 1 Bài 3: Phép toán giao, hợp, hiệu trên khoảng đoạn"""
    a = random.randint(-4, -1)
    b = random.randint(1, 4)
    c = random.randint(b - 2, b + 1)
    d = c + random.randint(3, 5)
    # A = [a; b], B = (c; d)
    caudan = rf"Cho hai tập hợp $A = [{a}; {b}]$ và $B = ({c}; {d})$. Xác định tập hợp $A \cap B$."
    left = max(a, c)
    right = min(b, d)
    if left < right:
        correct = rf"$({left}; {right}]$"
        wrongs = [
            rf"$[{left}; {right}]$",
            rf"$[{a}; {d})$",
            rf"$[{a}; {c}]$"
        ]
        loigiai = rf"Ta có $A \cap B$ là phần tử vừa thuộc $A$ vừa thuộc $B$. Vì $A = [{a}; {b}]$ và $B = ({c}; {d})$ nên $A \cap B = ({left}; {right}]$."
    else:
        correct = r"$\emptyset$"
        wrongs = [rf"$[{a}; {b}]$", rf"$({c}; {d})$", rf"$[{b}; {c}]$"]
        loigiai = rf"Vì khoảng và đoạn không có phần tử chung nên $A \cap B = \emptyset$."
    choices = shuffle_choices(correct, wrongs)
    return caudan, choices, loigiai

def k10_mc_c2_b4_bpt_bac_nhat_hai_an():
    """Chương 2 Bài 4: Nhận biết nghiệm của BPT bậc nhất 2 ẩn"""
    a = random.choice([1, 2, 3])
    b = random.choice([-2, -1, 1, 2])
    c = random.choice([2, 3, 4, 5])
    # BPT: a x + b y <= c
    # pick a point that satisfies
    x0, y0 = 0, 0
    val0 = a * x0 + b * y0
    if val0 <= c:
        p_ok = (x0, y0)
        p_no = [(c + 2, c + 2), (c + 3, 1), (-b * 2, c + 3)]
    else:
        p_ok = (-c, -c)
        p_no = [(x0, y0), (c + 2, c + 2), (2*c, c)]
    sign_b = f"+ {b}y" if b > 0 else f"- {-b}y"
    caudan = rf"Điểm nào dưới đây thuộc miền nghiệm của bất phương trình ${a}x {sign_b} \le {c}$?"
    correct = f"$M({p_ok[0]}; {p_ok[1]})$"
    wrongs = [f"$N({p_no[0][0]}; {p_no[0][1]})$", f"$P({p_no[1][0]}; {p_no[1][1]})$", f"$Q({p_no[2][0]}; {p_no[2][1]})$"]
    choices = shuffle_choices(correct, wrongs)
    val_sub = a * p_ok[0] + b * p_ok[1]
    loigiai = rf"Thay tọa độ $M({p_ok[0]}; {p_ok[1]})$ vào bất phương trình ta được: ${a} \cdot ({p_ok[0]}) {sign_b[:2]} ({p_ok[1]}) = {val_sub} \le {c}$ (thỏa mãn). Vậy điểm $M$ thuộc miền nghiệm."
    return caudan, choices, loigiai

def k10_mc_c2_b5_he_bpt_bac_nhat_hai_an():
    """Chương 2 Bài 5: Hệ BPT bậc nhất hai ẩn"""
    caudan = r"Hệ bất phương trình nào sau đây là hệ bất phương trình bậc nhất hai ẩn?"
    correct = r"$\begin{cases} x + 2y - 3 \le 0 \\ 2x - y + 1 > 0 \end{cases}$"
    wrongs = [
        r"$\begin{cases} x^2 + 2y \le 0 \\ x - y > 1 \end{cases}$",
        r"$\begin{cases} x + y - 3 \le 0 \\ xy + 1 > 0 \end{cases}$",
        r"$\begin{cases} \dfrac{1}{x} + y \le 2 \\ 2x - y > 0 \end{cases}$"
    ]
    loigiai = r"Hệ bất phương trình bậc nhất hai ẩn là hệ gồm các bất phương trình bậc nhất hai ẩn $x, y$ (chỉ chứa bậc nhất của $x$ và $y$, không chứa tích $xy$, bậc hai $x^2$ hay ẩn ở mẫu). Do đó chỉ có phương án đúng là hệ bậc nhất hai ẩn."
    choices = shuffle_choices(correct, wrongs)
    return caudan, choices, loigiai

def k10_mc_c3_ham_so_bac_hai():
    """Chương 3 Bài 7: Tọa độ đỉnh và trục đối xứng của Parabol"""
    a = random.choice([1, -1, 2, -2])
    x0 = random.randint(-3, 3)
    y0 = random.randint(-4, 4)
    # y = a(x - x0)^2 + y0 = a x^2 - 2a x0 x + a x0^2 + y0
    b = -2 * a * x0
    c = a * x0**2 + y0
    sign_b = f"+ {b}x" if b > 0 else f"- {-b}x" if b < 0 else ""
    sign_c = f"+ {c}" if c > 0 else f"- {-c}" if c < 0 else ""
    a_str = f"{a}" if a not in [1, -1] else ("" if a == 1 else "-")
    caudan = rf"Tọa độ đỉnh của parabol $(P): y = {a_str}x^2 {sign_b} {sign_c}$ là"
    correct = f"$I({x0}; {y0})$"
    wrongs = [
        f"$I({-x0}; {y0})$",
        f"$I({x0}; {-y0})$",
        f"$I({y0}; {x0})$"
    ]
    choices = shuffle_choices(correct, wrongs)
    loigiai = rf"Hoành độ đỉnh parabol: $x_I = -\dfrac{{b}}{{2a}} = -\dfrac{{{b}}}{{2 \cdot ({a})}} = {x0}$. Thay vào hàm số ta được tung độ đỉnh $y_I = {y0}$. Vậy đỉnh của parabol là $I({x0}; {y0})$."
    return caudan, choices, loigiai

def k10_mc_c4_b8_gia_tri_luong_giac():
    """Chương 4 Bài 8: Giá trị lượng giác của góc từ 0 đến 180 độ"""
    alpha = random.choice([30, 45, 60, 120, 135, 150])
    rad = math.radians(alpha)
    val_sin = math.sin(rad)
    val_cos = math.cos(rad)
    if alpha == 120:
        ans_sin = r"\dfrac{\sqrt{3}}{2}"
        ans_cos = r"-\dfrac{1}{2}"
    elif alpha == 135:
        ans_sin = r"\dfrac{\sqrt{2}}{2}"
        ans_cos = r"-\dfrac{\sqrt{2}}{2}"
    elif alpha == 150:
        ans_sin = r"\dfrac{1}{2}"
        ans_cos = r"-\dfrac{\sqrt{3}}{2}"
    elif alpha == 60:
        ans_sin = r"\dfrac{\sqrt{3}}{2}"
        ans_cos = r"\dfrac{1}{2}"
    elif alpha == 45:
        ans_sin = r"\dfrac{\sqrt{2}}{2}"
        ans_cos = r"\dfrac{\sqrt{2}}{2}"
    else:
        ans_sin = r"\dfrac{1}{2}"
        ans_cos = r"\dfrac{\sqrt{3}}{2}"
    
    mode = random.choice(["sin", "cos"])
    if mode == "sin":
        caudan = rf"Giá trị của $\sin {alpha}^\circ$ bằng"
        correct = f"${ans_sin}$"
        wrongs = [f"${ans_cos}$", f"$-{ans_sin}$", r"$\dfrac{\sqrt{3}}{3}$"]
        loigiai = rf"Theo bảng giá trị lượng giác của các góc đặc biệt, ta có $\sin {alpha}^\circ = {ans_sin}$."
    else:
        caudan = rf"Giá trị của $\cos {alpha}^\circ$ bằng"
        correct = f"${ans_cos}$"
        wrongs = [f"${ans_sin}$", f"$-{ans_cos}$", r"$1$"]
        loigiai = rf"Theo bảng giá trị lượng giác của các góc đặc biệt, ta có $\cos {alpha}^\circ = {ans_cos}$."
    choices = shuffle_choices(correct, wrongs)
    return caudan, choices, loigiai

def k10_mc_c4_b9_dinh_li_cosin_sin():
    """Chương 4 Bài 9: Định lí côsin và định lí sin"""
    mode = random.choice(["cosin", "sin_R"])
    if mode == "cosin":
        # b, c, A = 60 => a^2 = b^2 + c^2 - bc
        # b = 5, c = 8 => a^2 = 25 + 64 - 40 = 49 => a = 7
        triplets = [(5, 8, 60, 7), (3, 8, 60, 7), (3, 5, 120, 7), (2, 3, 60, math.sqrt(7))]
        b, c, A, a = random.choice(triplets[:3])
        caudan = rf"Cho tam giác $ABC$ có $b = {b}$, $c = {c}$ và $\widehat{{A}} = {A}^\circ$. Độ dài cạnh $a$ bằng"
        correct = f"${a}$"
        wrongs = [f"${a + 1}$", f"${a - 1}$", f"${int(math.sqrt(b**2 + c**2))}$"]
        loigiai = rf"Áp dụng định lí côsin trong tam giác $ABC$: $a^2 = b^2 + c^2 - 2bc \cos A = {b}^2 + {c}^2 - 2 \cdot {b} \cdot {c} \cdot \cos {A}^\circ = {a**2} \implies a = {a}$."
    else:
        a = random.choice([6, 8, 10, 12])
        A = random.choice([30, 45, 60])
        caudan = rf"Cho tam giác $ABC$ có cạnh $a = {a}$ và góc $\widehat{{A}} = {A}^\circ$. Bán kính đường tròn ngoại tiếp $R$ của tam giác $ABC$ bằng"
        if A == 30:
            R = a
            correct = f"${R}$"
            wrongs = [f"${a // 2}$", f"${2 * a}$", f"${a + 2}$"]
            loigiai = rf"Áp dụng định lí sin: $\dfrac{{a}}{{\sin A}} = 2R \implies R = \dfrac{{{a}}}{{2\sin 30^\circ}} = \dfrac{{{a}}}{{2 \cdot \frac{{1}}{{2}}}} = {R}$."
        elif A == 45:
            correct = rf"${a}\dfrac{{\sqrt{{2}}}}{{2}}$"
            wrongs = [f"${a}$", rf"${a}\sqrt{{2}}$", f"${a // 2}$"]
            loigiai = rf"Áp dụng định lí sin: $2R = \dfrac{{a}}{{\sin A}} \implies R = \dfrac{{{a}}}{{2 \sin 45^\circ}} = \dfrac{{{a}}}{{\sqrt{{2}}}} = {a}\dfrac{{\sqrt{{2}}}}{{2}}$."
        else:
            correct = rf"${a}\dfrac{{\sqrt{{3}}}}{{3}}$"
            wrongs = [f"${a}$", rf"${a}\sqrt{{3}}$", f"${a // 2}$"]
            loigiai = rf"Áp dụng định lí sin: $2R = \dfrac{{a}}{{\sin A}} \implies R = \dfrac{{{a}}}{{2 \sin 60^\circ}} = \dfrac{{{a}}}{{\sqrt{{3}}}} = {a}\dfrac{{\sqrt{{3}}}}{{3}}$."
    choices = shuffle_choices(correct, wrongs)
    return caudan, choices, loigiai

def k10_mc_c4_b10_giai_tam_giac_thuc_te():
    """Chương 4 Bài 10: Diện tích tam giác và bài toán thực tế"""
    a = random.choice([6, 8, 10, 12])
    b = random.choice([10, 12, 14, 16])
    C = random.choice([30, 60, 150])
    if C == 30 or C == 150:
        S = int(0.5 * a * b * 0.5)
        correct = f"${S}$"
        wrongs = [f"${2 * S}$", f"${S + 5}$", f"${S - 3}$"]
        loigiai = rf"Diện tích tam giác $ABC$ là $S = \dfrac{{1}}{{2}}ab\sin C = \dfrac{{1}}{{2}} \cdot {a} \cdot {b} \cdot \sin {C}^\circ = \dfrac{{1}}{{2}} \cdot {a} \cdot {b} \cdot \dfrac{{1}}{{2}} = {S}$."
    else:
        S_val = 0.5 * a * b
        correct = rf"${int(S_val / 2)}\sqrt{{3}}$"
        wrongs = [f"${int(S_val)}$", rf"${int(S_val)}\sqrt{{3}}$", f"${int(S_val / 4)}$"]
        loigiai = rf"Diện tích tam giác $ABC$ là $S = \dfrac{{1}}{{2}}ab\sin 60^\circ = \dfrac{{1}}{{2}} \cdot {a} \cdot {b} \cdot \dfrac{{\sqrt{{3}}}}{{2}} = {int(S_val / 2)}\sqrt{{3}}$."
    caudan = rf"Cho tam giác $ABC$ có $a = {a}$, $b = {b}$ và $\widehat{{C}} = {C}^\circ$. Diện tích của tam giác $ABC$ bằng"
    choices = shuffle_choices(correct, wrongs)
    return caudan, choices, loigiai

def k10_mc_c5_b11_khai_niem_vecto():
    """Chương 5 Bài 11: Khái niệm vectơ, độ dài vectơ"""
    a = random.choice([2, 3, 4, 5, 6])
    caudan = rf"Cho hình vuông $ABCD$ có cạnh bằng ${a}$. Độ dài của vectơ $\vec{{AB}}$ bằng"
    correct = f"${a}$"
    wrongs = [rf"${a}\sqrt{{2}}$", f"${2 * a}$", f"${a**2}$"]
    loigiai = rf"Độ dài của vectơ $\vec{{AB}}$ chính là độ dài đoạn thẳng $AB$, do đó $|\vec{{AB}}| = AB = {a}$."
    choices = shuffle_choices(correct, wrongs)
    return caudan, choices, loigiai

def k10_mc_c5_b12_tong_hieu_vecto():
    """Chương 5 Bài 12: Tổng và hiệu hai vectơ"""
    a = random.choice([3, 4, 5, 6])
    caudan = rf"Cho hình vuông $ABCD$ cạnh ${a}$. Độ dài của vectơ tổng $\vec{{AB}} + \vec{{AD}}$ bằng"
    correct = rf"${a}\sqrt{{2}}$"
    wrongs = [f"${2 * a}$", f"${a}$", rf"${2 * a}\sqrt{{2}}$"]
    loigiai = rf"Theo quy tắc hình bình hành, vì $ABCD$ là hình vuông nên $\vec{{AB}} + \vec{{AD}} = \vec{{AC}}$. Độ dài đường chéo hình vuông $AC = {a}\sqrt{{2}}$, suy ra $|\vec{{AB}} + \vec{{AD}}| = AC = {a}\sqrt{{2}}$."
    choices = shuffle_choices(correct, wrongs)
    return caudan, choices, loigiai

def k10_mc_c5_b13_tich_so_vecto():
    """Chương 5 Bài 13: Tích của một số với vectơ"""
    caudan = r"Cho tam giác $ABC$ có $M$ là trung điểm của đoạn thẳng $BC$. Khẳng định nào sau đây là \textbf{đúng}?"
    correct = r"$\vec{AB} + \vec{AC} = 2\vec{AM}$"
    wrongs = [
        r"$\vec{AB} + \vec{AC} = \vec{AM}$",
        r"$\vec{AB} + \vec{AC} = -2\vec{AM}$",
        r"$\vec{MA} + \vec{MB} = \vec{0}$"
    ]
    loigiai = r"Với $M$ là trung điểm cạnh $BC$, theo tính chất trung điểm ta luôn có hệ thức $\vec{AB} + \vec{AC} = 2\vec{AM}$."
    choices = shuffle_choices(correct, wrongs)
    return caudan, choices, loigiai

def k10_mc_c5_b14_tich_vo_huong():
    """Chương 5 Bài 14: Tích vô hướng của hai vectơ"""
    u1, u2 = random.randint(-3, 3), random.randint(-3, 3)
    v1, v2 = random.randint(-3, 3), random.randint(-3, 3)
    dot = u1 * v1 + u2 * v2
    caudan = rf"Trong mặt phẳng tọa độ $Oxy$, cho hai vectơ $\vec{{u}} = ({u1}; {u2})$ và $\vec{{v}} = ({v1}; {v2})$. Tích vô hướng $\vec{{u}} \cdot \vec{{v}}$ bằng"
    correct = f"${dot}$"
    wrongs = [f"${dot + 2}$", f"${dot - 3}$", f"${-dot}$"]
    loigiai = rf"Áp dụng biểu thức tọa độ của tích vô hướng: $\vec{{u}} \cdot \vec{{v}} = u_1 v_1 + u_2 v_2 = ({u1}) \cdot ({v1}) + ({u2}) \cdot ({v2}) = {dot}$."
    choices = shuffle_choices(correct, wrongs)
    return caudan, choices, loigiai

def k10_mc_c6_b1_so_dac_trung_xu_the_trung_tam():
    """Chương 6 Bài 1: Số trung bình, trung vị, mốt"""
    vals = sorted(random.sample(range(4, 11), 7))
    mean_val = round(sum(vals) / len(vals), 1)
    median_val = vals[3]
    caudan = rf"Cho mẫu số liệu điểm kiểm tra của một nhóm học sinh: ${vals[0]}; {vals[1]}; {vals[2]}; {vals[3]}; {vals[4]}; {vals[5]}; {vals[6]}$. Số trung vị của mẫu số liệu trên là"
    correct = f"${median_val}$"
    wrongs = [f"${vals[2]}$", f"${vals[4]}$", f"${mean_val}$"]
    loigiai = rf"Dãy số liệu gồm $n = 7$ giá trị đã được sắp xếp theo thứ tự không giảm. Số trung vị là giá trị đứng ở vị trí thứ $\dfrac{{7 + 1}}{{2}} = 4$, tức là $M_e = {median_val}$."
    choices = shuffle_choices(correct, wrongs)
    return caudan, choices, loigiai

def k10_mc_c6_b2_do_phan_tan():
    """Chương 6 Bài 2: Khoảng biến thiên và khoảng tứ phân vị"""
    vals = sorted(random.sample(range(10, 30), 8))
    # n = 8: Q1 = (vals[1]+vals[2])/2, Q3 = (vals[5]+vals[6])/2
    R = vals[-1] - vals[0]
    caudan = rf"Cho mẫu số liệu: ${', '.join(map(str, vals))}$. Khoảng biến thiên của mẫu số liệu này là"
    correct = f"${R}$"
    wrongs = [f"${R + 2}$", f"${R - 2}$", f"${vals[-1]}$"]
    loigiai = rf"Khoảng biến thiên của mẫu số liệu là hiệu giữa giá trị lớn nhất và giá trị nhỏ nhất: $R = x_{{\max}} - x_{{\min}} = {vals[-1]} - {vals[0]} = {R}$."
    choices = shuffle_choices(correct, wrongs)
    return caudan, choices, loigiai

def k10_mc_c5_sai_so_quy_tron():
    """Chương 5: Sai số và quy tròn số gần đúng"""
    # số gần đúng a = 12.3456 +/- 0.02 => độ chính xác d = 0.02 (hàng phần trăm) => quy tròn đến hàng phần chục: 12.3
    val = round(random.uniform(10.123, 99.876), 3)
    val_str = f"{val:.3f}".replace(".", ",")
    caudan = rf"Quy tròn số gần đúng $a = {val_str}$ với độ chính xác $d = 0{{,}}02$ ta được số"
    # hàng lớn nhất của d là phần trăm (0.01) => quy tròn đến hàng phần chục
    val_round = round(val, 1)
    val_round_str = f"{val_round:.1f}".replace(".", ",")
    correct = f"${val_round_str}$"
    wrongs = [
        f"${f'{round(val, 2):.2f}'.replace('.', ',')}$",
        f"${f'{round(val):d}'}$",
        f"${f'{round(val + 0.5, 1):.1f}'.replace('.', ',')}$"
    ]
    loigiai = rf"Vì độ chính xác $d = 0{{,}}02$ có hàng lớn nhất là hàng phần trăm, nên ta quy tròn số gần đúng $a = {val_str}$ đến hàng phần chục (hàng cao hơn hàng của độ chính xác một bậc). Chữ số ngay sau hàng phần chục được xét để làm tròn, kết quả quy tròn là ${val_round_str}$."
    choices = shuffle_choices(correct, wrongs)
    return caudan, choices, loigiai

def k10_mc_c7_tam_thuc_bac_hai():
    """Chương 7 Bài 15: Xét dấu tam thức bậc hai và BPT bậc hai"""
    x1, x2 = sorted(random.sample(range(-3, 5), 2))
    # f(x) = (x - x1)(x - x2) = x^2 - (x1+x2)x + x1*x2 < 0 => (x1; x2)
    b = -(x1 + x2)
    c = x1 * x2
    sign_b = f"+ {b}x" if b > 0 else f"- {-b}x" if b < 0 else ""
    sign_c = f"+ {c}" if c > 0 else f"- {-c}" if c < 0 else ""
    caudan = rf"Tập nghiệm của bất phương trình $x^2 {sign_b} {sign_c} < 0$ là"
    correct = rf"$({x1}; {x2})$"
    wrongs = [
        rf"$(-\\infty; {x1}) \\cup ({x2}; +\\infty)$",
        rf"$[{x1}; {x2}]$",
        rf"$\\mathbb{{R}}$"
    ]
    loigiai = rf"Tam thức bậc hai $f(x) = x^2 {sign_b} {sign_c}$ có hệ số $a = 1 > 0$ và hai nghiệm phân biệt $x_1 = {x1}, x_2 = {x2}$. Theo quy tắc xét dấu ``trong trái ngoài cùng'', $f(x) < 0 \iff {x1} < x < {x2}$. Do đó tập nghiệm là $S = ({x1}; {x2})$."
    choices = shuffle_choices(correct, wrongs)
    return caudan, choices, loigiai

def k10_mc_c7_pt_quy_ve_bac_hai():
    """Chương 7 Bài 17: Phương trình quy về phương trình bậc hai"""
    a = random.randint(1, 4)
    # sqrt(x + a) = x - a => x + a = x^2 - 2ax + a^2 => x^2 - (2a+1)x + a^2 - a = 0
    # or simpler: sqrt{2x + 3} = x => 2x + 3 = x^2 => x^2 - 2x - 3 = 0 => x = 3 (since x >= 0)
    caudan = r"Số nghiệm của phương trình $\sqrt{2x + 3} = x$ là"
    correct = "$1$"
    wrongs = ["$2$", "$0$", "$3$"]
    loigiai = r"Điều kiện $x \ge 0$. Bình phương hai vế ta được: $2x + 3 = x^2 \iff x^2 - 2x - 3 = 0 \iff \left[\begin{aligned} x &= 3 \text{ (thỏa mãn)} \\ x &= -1 \text{ (loại do } x \ge 0) \end{aligned}\right.$. Vậy phương trình có đúng $1$ nghiệm."
    choices = shuffle_choices(correct, wrongs)
    return caudan, choices, loigiai

def k10_mc_toan_thuc_te_tong_hop():
    """Tổng hợp toán thực tế trắc nghiệm nhiều lựa chọn từ Toan_10.pdf"""
    funcs = [
        k10_mc_c4_b10_giai_tam_giac_thuc_te,
        k10_mc_c2_b4_bpt_bac_nhat_hai_an,
        k10_mc_c5_b12_tong_hieu_vecto,
        k10_mc_c6_b1_so_dac_trung_xu_the_trung_tam,
        k10_mc_c5_sai_so_quy_tron
    ]
    return random.choice(funcs)()

# ==============================================================================
# PHẦN II: TRẮC NGHIỆM ĐÚNG / SAI (TF)
# ==============================================================================

def k10_tf_c1_menh_de_tap_hop():
    """Chương 1: Mệnh đề và tập hợp (Đúng / Sai)"""
    a = random.randint(-4, -1)
    b = random.randint(2, 5)
    c = random.randint(0, b - 1)
    d = b + random.randint(2, 4)
    
    caudan = rf"Cho hai tập hợp $A = [{a}; {b}]$ và $B = ({c}; {d})$ cùng mệnh đề $P: ``\forall x \in \mathbb{{R}}, x^2 + 1 > 0\text{{''}}$. Xét tính đúng sai của các khẳng định sau:"
    
    item_a = (
        r"Mệnh đề phủ định của $P$ là $\overline{P}: ``\exists x \in \mathbb{R}, x^2 + 1 \le 0\text{''}$",
        r"Mệnh đề phủ định của $P$ là $\overline{P}: ``\forall x \in \mathbb{R}, x^2 + 1 \le 0\text{''}$",
        r"Phủ định của ký hiệu $\forall$ là $\exists$ và dấu $>$ phủ định thành $\le$.",
        r"Phủ định của $\forall$ phải chuyển thành $\exists$, không giữ nguyên $\forall$."
    )
    item_b = (
        rf"Giao của hai tập hợp là $A \cap B = ({c}; {b}]$",
        rf"Giao của hai tập hợp là $A \cap B = [{c}; {b}]$",
        rf"Vì $c \notin B$ nên tại đầu mút $c$ là ngoặc tròn, tại $b$ cả hai đều thuộc nên là ngoặc vuông $({c}; {b}]$.",
        rf"Tại $c$, vì $c \notin B$ nên không thể lấy ngoặc vuông $[{c}; {b}]$."
    )
    item_c = (
        rf"Hiệu $A \setminus B = [{a}; {c}]$",
        rf"Hiệu $A \setminus B = [{a}; {c})$",
        rf"Vì $c \notin B$ nên khi lấy $A \setminus B$, phần tử $c$ vẫn thuộc $A$ và không bị trừ, do đó mút $c$ lấy ngoặc vuông $[{a}; {c}]$.",
        rf"Vì $c \notin B$ nên $c$ thuộc hiệu $A \setminus B$, phải lấy ngoặc vuông chứ không phải ngoặc tròn."
    )
    # item d: số tập con của tập hợp {1, 2, 3}
    item_d = (
        r"Tập hợp $X = \{x \in \mathbb{N} \mid x < 4\}$ có đúng $16$ tập con",
        r"Tập hợp $X = \{x \in \mathbb{N} \mid x < 4\}$ có đúng $8$ tập con",
        r"Vì $X = \{0; 1; 2; 3\}$ có $4$ phần tử nên số tập con là $2^4 = 16$.",
        r"Tập hợp các số tự nhiên nhỏ hơn 4 gồm 4 phần tử $\{0; 1; 2; 3\}$, số tập con phải là $2^4 = 16$ chứ không phải $8$."
    )
    choices, loigiai = make_tf_choices([item_a, item_b, item_c, item_d])
    return caudan, choices, loigiai

def k10_tf_c2_bpt_he_bpt_mien_nghiem():
    """Chương 2: BPT và hệ BPT bậc nhất hai ẩn (Đúng / Sai)"""
    caudan = r"""Cho hệ bất phương trình bậc nhất hai ẩn $\begin{cases} x \ge 0 \\ y \ge 0 \\ x + y \le 4 \\ 2x + y \le 6 \end{cases}$. Gọi $D$ là miền nghiệm của hệ trên mặt phẳng tọa độ $Oxy$. Xét tính đúng sai của các khẳng định sau:"""
    
    item_a = (
        r"Điểm $O(0; 0)$ và điểm $M(1; 2)$ đều thuộc miền nghiệm $D$",
        r"Điểm $M(2; 3)$ thuộc miền nghiệm $D$",
        r"Thay $(0; 0)$ và $(1; 2)$ vào các bất phương trình trong hệ đều thỏa mãn.",
        r"Thay $x = 2, y = 3$ vào $x + y = 5 > 4$ (không thỏa mãn $x + y \le 4$), do đó điểm $M(2; 3)$ không thuộc miền nghiệm."
    )
    item_b = (
        r"Miền nghiệm $D$ là một tứ giác có các đỉnh là $O(0; 0), A(3; 0), B(2; 2), C(0; 4)$",
        r"Miền nghiệm $D$ là một tam giác có ba đỉnh",
        r"Giao điểm của các đường biên tạo thành tứ giác lồi với các đỉnh $O(0; 0), A(3; 0), B(2; 2), C(0; 4)$.",
        r"Miền nghiệm là một tứ giác (gồm 4 đỉnh $O, A, B, C$) chứ không phải tam giác."
    )
    item_c = (
        r"Biểu thức $F(x, y) = 2x + 3y$ đạt giá trị lớn nhất trên miền $D$ bằng $12$",
        r"Biểu thức $F(x, y) = 2x + 3y$ đạt giá trị lớn nhất trên miền $D$ bằng $10$",
        r"Tính giá trị tại các đỉnh: $F(0; 0) = 0$, $F(3; 0) = 6$, $F(2; 2) = 10$, $F(0; 4) = 12$. Do đó $\max F = 12$ tại $(0; 4)$.",
        r"Giá trị lớn nhất đạt tại đỉnh $C(0; 4)$ là $F(0; 4) = 2(0) + 3(4) = 12$, không phải $10$."
    )
    item_d = (
        r"Nếu một xưởng sản xuất sử dụng $x$ giờ máy I và $y$ giờ máy II với lợi nhuận $P(x, y) = 3x + 2y$ (triệu đồng), thì lợi nhuận tối đa đạt được là $10$ triệu đồng",
        r"Nếu một xưởng sản xuất sử dụng $x$ giờ máy I và $y$ giờ máy II với lợi nhuận $P(x, y) = 3x + 2y$ (triệu đồng), thì lợi nhuận tối đa đạt được là $14$ triệu đồng",
        r"Tính giá trị $P$ tại các đỉnh: $P(0; 0) = 0$, $P(3; 0) = 9$, $P(2; 2) = 10$, $P(0; 4) = 8$. Lợi nhuận lớn nhất là $10$ triệu đồng tại $(2; 2)$.",
        r"Lợi nhuận lớn nhất tại các đỉnh miền nghiệm là $P(2; 2) = 10$ triệu đồng, không thể đạt $14$ triệu đồng."
    )
    choices, loigiai = make_tf_choices([item_a, item_b, item_c, item_d])
    return caudan, choices, loigiai

def k10_tf_c4_he_thuc_luong_tam_giac_thuc_te():
    """Chương 4: Hệ thức lượng trong tam giác và Toán thực tế (Đúng / Sai)"""
    caudan = r"""Cho tam giác $ABC$ có cạnh $b = AC = 8$, $c = AB = 5$ và góc $\widehat{A} = 60^\circ$. Xét tính đúng sai của các khẳng định sau:"""
    
    item_a = (
        r"Độ dài cạnh $BC = 7$",
        r"Độ dài cạnh $BC = \sqrt{89}$",
        r"Áp dụng định lý côsin: $a^2 = b^2 + c^2 - 2bc \cos A = 64 + 25 - 2 \cdot 8 \cdot 5 \cdot \dfrac{1}{2} = 49 \implies a = 7$.",
        r"Theo định lý côsin, $a^2 = 8^2 + 5^2 - 2 \cdot 8 \cdot 5 \cdot \cos 60^\circ = 49 \implies a = 7$ chứ không phải $\sqrt{89}$."
    )
    item_b = (
        r"Diện tích tam giác $ABC$ bằng $10\sqrt{3}$",
        r"Diện tích tam giác $ABC$ bằng $20$",
        r"Ta có diện tích $S = \dfrac{1}{2}bc\sin A = \dfrac{1}{2} \cdot 8 \cdot 5 \cdot \sin 60^\circ = 20 \cdot \dfrac{\sqrt{3}}{2} = 10\sqrt{3}$.",
        r"Diện tích $S = \dfrac{1}{2}bc\sin A = 10\sqrt{3}$, khẳng định bằng $20$ là sai."
    )
    item_c = (
        r"Bán kính đường tròn ngoại tiếp tam giác $ABC$ là $R = \dfrac{7\sqrt{3}}{3}$",
        r"Bán kính đường tròn ngoại tiếp tam giác $ABC$ là $R = 7$",
        r"Theo định lý sin: $2R = \dfrac{a}{\sin A} = \dfrac{7}{\sin 60^\circ} = \dfrac{14}{\sqrt{3}} \implies R = \dfrac{7\sqrt{3}}{3}$.",
        r"Theo định lý sin, $R = \dfrac{a}{2\sin A} = \dfrac{7}{2 \cdot \frac{\sqrt{3}}{2}} = \dfrac{7\sqrt{3}}{3}$."
    )
    item_d = (
        r"Chiều cao $h_a$ kẻ từ đỉnh $A$ của tam giác $ABC$ bằng $\dfrac{20\sqrt{3}}{7}$",
        r"Chiều cao $h_a$ kẻ từ đỉnh $A$ của tam giác $ABC$ bằng $\dfrac{10\sqrt{3}}{7}$",
        r"Ta có $S = \dfrac{1}{2} a h_a \implies h_a = \dfrac{2S}{a} = \dfrac{2 \cdot 10\sqrt{3}}{7} = \dfrac{20\sqrt{3}}{7}$.",
        r"Chiều cao $h_a = \dfrac{2S}{a} = \dfrac{20\sqrt{3}}{7}$, khẳng định $\dfrac{10\sqrt{3}}{7}$ là sai."
    )
    choices, loigiai = make_tf_choices([item_a, item_b, item_c, item_d])
    return caudan, choices, loigiai

def k10_tf_c5_vecto_toa_do_oxy_thuc_te():
    """Chương 5: Vectơ, tọa độ Oxy và Toán thực tế lực (Đúng / Sai)"""
    caudan = r"""Trong mặt phẳng tọa độ $Oxy$, cho tam giác $ABC$ với $A(1; 2)$, $B(-2; 6)$ và $C(4; 4)$. Xét tính đúng sai của các khẳng định sau:"""
    
    item_a = (
        r"Tọa độ của vectơ $\vec{AB} = (-3; 4)$ và độ dài $|\vec{AB}| = 5$",
        r"Tọa độ của vectơ $\vec{AB} = (3; -4)$ và độ dài $|\vec{AB}| = 25$",
        r"Ta có $\vec{AB} = (x_B - x_A; y_B - y_A) = (-2 - 1; 6 - 2) = (-3; 4)$, do đó độ dài $|\vec{AB}| = \sqrt{(-3)^2 + 4^2} = 5$.",
        r"Tọa độ $\vec{AB} = (-3; 4)$ chứ không phải $(3; -4)$, và độ dài bằng $5$ chứ không phải $25$."
    )
    item_b = (
        r"Tọa độ trọng tâm $G$ của tam giác $ABC$ là $G(1; 4)$",
        r"Tọa độ trọng tâm $G$ của tam giác $ABC$ là $G(3; 12)$",
        r"Tọa độ trọng tâm $G$: $x_G = \dfrac{1 + (-2) + 4}{3} = 1$, $y_G = \dfrac{2 + 6 + 4}{3} = 4$. Vậy $G(1; 4)$.",
        r"Tọa độ trọng tâm bằng trung bình cộng tọa độ ba đỉnh: $G(1; 4)$, khẳng định $(3; 12)$ chưa chia cho $3$."
    )
    item_c = (
        r"Tam giác $ABC$ là tam giác vuông tại $A$",
        r"Tam giác $ABC$ là tam giác đều",
        r"Ta có $\vec{AB} = (-3; 4)$, $\vec{AC} = (3; 2)$. Tích vô hướng $\vec{AB} \cdot \vec{AC} = (-3)(3) + 4(2) = -9 + 8 = -1 \ne 0$. Do đó tam giác không vuông tại $A$. (Ý này sai)",
        r"Tính tích vô hướng: $\vec{AB} \cdot \vec{AC} = -1 \ne 0$ nên tam giác $ABC$ không vuông tại $A$."
    )
    item_d = (
        r"Nếu một vật chịu tác dụng của hai lực đồng quy $\vec{F}_1, \vec{F}_2$ có độ lớn lần lượt là $30\text{ N}$ và $40\text{ N}$ vuông góc với nhau, thì độ lớn của hợp lực bằng $50\text{ N}$",
        r"Nếu một vật chịu tác dụng của hai lực đồng quy $\vec{F}_1, \vec{F}_2$ có độ lớn lần lượt là $30\text{ N}$ và $40\text{ N}$ vuông góc với nhau, thì độ lớn của hợp lực bằng $70\text{ N}$",
        r"Vì hai lực vuông góc nên độ lớn hợp lực theo định lý Pythagore: $|\vec{F}| = \sqrt{F_1^2 + F_2^2} = \sqrt{30^2 + 40^2} = 50\text{ N}$.",
        r"Vì hai lực vuông góc nên độ lớn hợp lực là $\sqrt{30^2 + 40^2} = 50\text{ N}$, không phải tổng đại số $70\text{ N}$."
    )
    # Ensure item_c has proper true/false matching:
    # Notice: AB = (-3, 4), AC = (3, 2). Dot is -1 != 0.
    # Let's make true stmt: Tam giác ABC không phải là tam giác vuông tại A.
    item_c = (
        r"Tích vô hướng $\vec{AB} \cdot \vec{AC} = -1$",
        r"Tích vô hướng $\vec{AB} \cdot \vec{AC} = 0$",
        r"Ta có $\vec{AB} = (-3; 4)$ và $\vec{AC} = (3; 2)$. Khi đó $\vec{AB} \cdot \vec{AC} = (-3) \cdot 3 + 4 \cdot 2 = -9 + 8 = -1$.",
        r"Tích vô hướng bằng $(-3)(3) + 4(2) = -1 \ne 0$."
    )
    choices, loigiai = make_tf_choices([item_a, item_b, item_c, item_d])
    return caudan, choices, loigiai

def k10_tf_c6_thong_ke_do_phan_tan():
    """Chương 6: Thống kê và các số đặc trưng (Đúng / Sai)"""
    vals = [5, 6, 6, 7, 8, 8, 8, 9, 10] # 9 values
    # mean = (5 + 12 + 7 + 24 + 9 + 10) / 9 = 67 / 9 approx 7.4
    # Me = 8
    # Mo = 8
    # Q1 = 6, Q3 = 8.5
    # R = 10 - 5 = 5
    caudan = r"""Cho mẫu số liệu về điểm kiểm tra môn Toán của 9 học sinh: $5;\; 6;\; 6;\; 7;\; 8;\; 8;\; 8;\; 9;\; 10$. Xét tính đúng sai của các khẳng định sau:"""
    
    item_a = (
        r"Mốt của mẫu số liệu là $M_o = 8$",
        r"Mốt của mẫu số liệu là $M_o = 6$",
        r"Giá trị $8$ xuất hiện nhiều nhất (3 lần) nên mốt là $M_o = 8$.",
        r"Giá trị $8$ có tần số lớn nhất là 3, nên mốt là $8$ chứ không phải $6$."
    )
    item_b = (
        r"Số trung vị của mẫu số liệu là $M_e = 8$",
        r"Số trung vị của mẫu số liệu là $M_e = 7$",
        r"Dãy đã sắp xếp có 9 giá trị, trung vị là giá trị thứ 5: $M_e = 8$.",
        r"Số trung vị của 9 phần tử là giá trị thứ 5, tức là $8$, không phải $7$."
    )
    item_c = (
        r"Khoảng biến thiên của mẫu số liệu là $R = 5$",
        r"Khoảng biến thiên của mẫu số liệu là $R = 10$",
        r"Khoảng biến thiên là $R = x_{\max} - x_{\min} = 10 - 5 = 5$.",
        r"Khoảng biến thiên là $10 - 5 = 5$, không phải giá trị lớn nhất $10$."
    )
    item_d = (
        r"Tứ phân vị thứ nhất là $Q_1 = 6$ và tứ phân vị thứ ba là $Q_3 = 8{,}5$",
        r"Tứ phân vị thứ nhất là $Q_1 = 5{,}5$ và tứ phân vị thứ ba là $Q_3 = 9$",
        r"Nửa dưới gồm $\{5; 6; 6; 7\}$ có trung vị $Q_1 = \dfrac{6+6}{2} = 6$. Nửa trên gồm $\{8; 8; 9; 10\}$ có trung vị $Q_3 = \dfrac{8+9}{2} = 8{,}5$.",
        r"Tứ phân vị thứ nhất là $Q_1 = 6$ và $Q_3 = 8{,}5$."
    )
    choices, loigiai = make_tf_choices([item_a, item_b, item_c, item_d])
    return caudan, choices, loigiai

def k10_tf_c7_ham_so_bac_hai_tam_thuc():
    """Chương 7: Hàm số bậc hai, tam thức bậc hai (Đúng / Sai)"""
    # y = x^2 - 4x + 3
    # Dinh I(2; -1), truc doi xung x = 2
    # Nghich bien tren (-infty; 2), dong bien tren (2; +infty)
    # f(x) <= 0 <=> x in [1; 3]
    # sqrt(x^2 - 4x + 3) = x - 1 => x^2 - 4x + 3 = x^2 - 2x + 1 => -2x = -2 => x = 1 (thoa man)
    caudan = r"""Cho hàm số bậc hai $y = f(x) = x^2 - 4x + 3$ có đồ thị là parabol $(P)$. Xét tính đúng sai của các khẳng định sau:"""
    
    item_a = (
        r"Tọa độ đỉnh của parabol $(P)$ là $I(2; -1)$ và trục đối xứng là đường thẳng $x = 2$",
        r"Tọa độ đỉnh của parabol $(P)$ là $I(-2; 15)$ và trục đối xứng là đường thẳng $x = -2$",
        r"Tọa độ đỉnh: $x_I = -\dfrac{b}{2a} = 2$, $y_I = 2^2 - 4(2) + 3 = -1$. Trục đối xứng $x = 2$.",
        r"Tọa độ đỉnh là $I(2; -1)$ và trục đối xứng là $x = 2$."
    )
    item_b = (
        r"Hàm số nghịch biến trên khoảng $(-\infty; 2)$ và đồng biến trên khoảng $(2; +\infty)$",
        r"Hàm số đồng biến trên khoảng $(-\infty; 2)$ và nghịch biến trên khoảng $(2; +\infty)$",
        r"Vì $a = 1 > 0$ nên parabol có bề lõm hướng lên trên, hàm số nghịch biến trên $(-\infty; 2)$ và đồng biến trên $(2; +\infty)$.",
        r"Vì $a = 1 > 0$ nên hàm số phải nghịch biến trên $(-\infty; 2)$ và đồng biến trên $(2; +\infty)$."
    )
    item_c = (
        r"Tập nghiệm của bất phương trình $x^2 - 4x + 3 \le 0$ là đoạn $[1; 3]$",
        r"Tập nghiệm của bất phương trình $x^2 - 4x + 3 \le 0$ là $(-\infty; 1] \cup [3; +\infty)$",
        r"Phương trình $x^2 - 4x + 3 = 0$ có hai nghiệm $x = 1, x = 3$. Vì $a = 1 > 0$ nên $f(x) \le 0 \iff 1 \le x \le 3$.",
        r"Tam thức đổi dấu âm ở miền trong hai nghiệm, nên tập nghiệm là đoạn $[1; 3]$."
    )
    item_d = (
        r"Phương trình $\sqrt{x^2 - 4x + 3} = x - 1$ có đúng $1$ nghiệm thực là $x = 1$",
        r"Phương trình $\sqrt{x^2 - 4x + 3} = x - 1$ có $2$ nghiệm phân biệt",
        r"Bình phương hai vế với điều kiện $x \ge 1$: $x^2 - 4x + 3 = (x - 1)^2 = x^2 - 2x + 1 \iff -2x = -2 \iff x = 1$ (thỏa mãn). Vậy phương trình có đúng $1$ nghiệm.",
        r"Phương trình sau khi bình phương chỉ thu được một nghiệm duy nhất $x = 1$."
    )
    choices, loigiai = make_tf_choices([item_a, item_b, item_c, item_d])
    return caudan, choices, loigiai

def k10_tf_tong_hop_toan_pdf():
    """Tổng hợp câu hỏi Đúng/Sai lớp 10 theo Toan_10.pdf"""
    funcs = [
        k10_tf_c1_menh_de_tap_hop,
        k10_tf_c2_bpt_he_bpt_mien_nghiem,
        k10_tf_c4_he_thuc_luong_tam_giac_thuc_te,
        k10_tf_c5_vecto_toa_do_oxy_thuc_te,
        k10_tf_c6_thong_ke_do_phan_tan,
        k10_tf_c7_ham_so_bac_hai_tam_thuc
    ]
    return random.choice(funcs)()

print("All generators compiled successfully")
