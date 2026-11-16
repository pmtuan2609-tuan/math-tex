import random

# ==============================================================================
# NGÂN HÀNG CÂU HỎI THI THPT QUỐC GIA: SỰ BIẾN THIÊN VÀ CỰC TRỊ CỦA HÀM SỐ
# (Đọc BBT, bảng xét dấu đạo hàm, đồ thị)
# ==============================================================================

DANH_SACH_CAU_HOI = [
    # 1. THPT – 2021 – Đề 101 – Câu 13
    {
        "source": "THPT – 2021 – Đề 101 – Câu 13",
        "prompt": r"Cho hàm số $y=f\left( x \right)$ có bảng biến thiên như sau. Giá trị cực tiểu của hàm số đã cho bằng",
        "tikz": r"""\begin{tikzpicture}
			\tkzTabInit[nocadre,lgt=1.2,espcl=1.5,deltacl=0.6]
			{$x$ /0.6, $y'$ /0.6, $y$ /1.5}
			{$-\infty$,$-1$,$1$,$+\infty$}
			\tkzTabLine{,-,$0$,+,$0$,-,}
			\tkzTabVar{+/$+\infty$,-/$-3$,+/$5$,-/$-\infty$}
		\end{tikzpicture}""",
        "correct": r"$-3$",
        "wrongs": [r"$-1$", r"$5$", r"$1$"],
        "loigiai": r"Dựa vào bảng biến thiên, hàm số đạt cực tiểu tại $x = -1$ và giá trị cực tiểu của hàm số đã cho bằng $y_{\text{CT}} = -3$."
    },

    # 2. THPT – 2021 – Đề 101 – Câu 5
    {
        "source": "THPT – 2021 – Đề 101 – Câu 5",
        "prompt": r"Cho hàm số $y=f\left( x \right)$ có bảng xét dấu của đạo hàm như sau. Số điểm cực trị của hàm số đã cho là",
        "tikz": r"""\begin{tikzpicture}
			\tkzTabInit[nocadre=true,lgt=1.2,espcl=1.25]
			{$x$ /.7,$y'$ /.7}{$-\infty$,$-2$,$-1$,$1$,$4$,$+\infty$}
			\tkzTabLine{,-,0,+,0,-,0,+,0,-,}
		\end{tikzpicture}""",
        "correct": r"$4$",
        "wrongs": [r"$5$", r"$3$", r"$2$"],
        "loigiai": r"Ta thấy đạo hàm $y'$ đổi dấu khi $x$ đi qua các điểm $-2$, $-1$, $1$, $4$. Do đó, hàm số đã cho có $4$ điểm cực trị."
    },

    # 3. THPT 2017 -- Đề 101
    {
        "source": "THPT 2017 -- Đề 101",
        "prompt": r"Cho hàm số $y=f(x)$ có bảng biến thiên như sau. Mệnh đề nào dưới đây sai?",
        "tikz": r"""\begin{tikzpicture}
			\tkzTabInit[nocadre,lgt=1.2,espcl=1.5,deltacl=0.6]
			{$x$ /0.6,$y'$ /0.6,$y$ /1.5}
			{$-\infty$,$-1$,$0$,$1$,$+\infty$}
			\tkzTabLine{,-,$0$,+,$0$,-,$0$,+,}
			\tkzTabVar{+/$+\infty$, -/$0$,+/$3$,-/$0$,+/$+\infty$}
		\end{tikzpicture}""",
        "correct": r"Hàm số có giá trị cực đại bằng $0$",
        "wrongs": [
            r"Hàm số có ba điểm cực trị",
            r"Hàm số có giá trị cực đại bằng $3$",
            r"Hàm số có hai điểm cực tiểu"
        ],
        "loigiai": r"Dựa vào bảng biến thiên, hàm số đạt cực đại tại $x = 0$ với giá trị cực đại là $y_{\text{CĐ}} = 3$. Do đó mệnh đề ``Hàm số có giá trị cực đại bằng $0$'' là sai."
    },

    # 4. THPT 2017 -- Đề 102
    {
        "source": "THPT 2017 -- Đề 102",
        "prompt": r"Cho hàm số $y=f(x)$ có bảng biến thiên như sau. Tìm giá trị cực đại $y_{\text{CĐ}}$ và giá trị cực tiểu $y_{\text{CT}}$ của hàm số đã cho.",
        "tikz": r"""\begin{tikzpicture}
			\tkzTabInit[nocadre,espcl=1.6]
			{$x$ /0.6, $y'$ /0.6,$y$ /1.6}
			{ $-\infty$,$-2$,$2$,$+\infty$ }
			\tkzTabLine{ ,+,$0$,-,$0$,+, }
			\tkzTabVar{ - /$-\infty$ ,+ /$3$/, -/ $0$, +/ $+\infty$ }
	\end{tikzpicture}""",
        "correct": r"$y_{\text{CĐ}} = 3$ và $y_{\text{CT}} = 0$",
        "wrongs": [
            r"$y_{\text{CĐ}} = 3$ và $y_{\text{CT}} = -2$",
            r"$y_{\text{CĐ}} = 2$ và $y_{\text{CT}} = 0$",
            r"$y_{\text{CĐ}} = -2$ và $y_{\text{CT}} = 2$"
        ],
        "loigiai": r"Dựa vào bảng biến thiên:\\Hàm số đạt cực đại tại $x = -2$, giá trị cực đại $y_{\text{CĐ}} = 3$.\\Hàm số đạt cực tiểu tại $x = 2$, giá trị cực tiểu $y_{\text{CT}} = 0$."
    },

    # 5. THPT 2019 -- Đề 108
    {
        "source": "THPT 2019 -- Đề 108",
        "prompt": r"Cho hàm số $f(x)$ có bảng biến thiên như sau. Hàm số đã cho đạt cực đại tại",
        "tikz": r"""\begin{tikzpicture}
			\tkzTabInit[nocadre,lgt=1.2,espcl=1.5]
			{$x$/.6,$f'(x)$/.6,$f(x)$/1.5}
			{$-\infty$,$1$,$3$,$+\infty$}
			\tkzTabLine{,-,0,+,0,-,}
			\tkzTabVar{+/$+\infty$,-/$-2$,+/$2$,-/$-\infty$}
	\end{tikzpicture}""",
        "correct": r"$x=3$",
        "wrongs": [r"$x=1$", r"$x=2$", r"$x=-2$"],
        "loigiai": r"Căn cứ bảng biến thiên, đạo hàm $f'(x)$ đổi dấu từ dương sang âm khi đi qua $x = 3$. Do đó, hàm số đạt cực đại tại $x = 3$."
    },

    # 6. Đồ thị hàm bậc ba (Câu 67)
    {
        "source": "Đề thi TN THPT",
        "prompt": r"Hình bên là đồ thị của một hàm số. Hàm số đồng biến trong khoảng nào?",
        "tikz": r"""\begin{tikzpicture}[scale=0.8, font=\footnotesize, line join=round, line cap=round, >=stealth,y=0.6cm]
			\draw (0,0) node [below left] {$O$};
			\draw[->] (-2.5,0)--(2,0) node[below left] {$x$};
			\draw[->] (0,-1.5)--(0,3.8) node[below left] {$y$};
			\draw[samples=200,domain=-2.04:2.02,smooth,variable=\x] plot (\x,{(\x)^3-3*(\x)+1});
			\draw[dashed](1,0)|-(0,-1) (-1,0)|-(0,3);
			\path
			(1,0)node[above]{$1$}
			(-1,0)node[below]{$-1$}
			(0,1)node[right]{$1$}
			(0,3)node[right]{$3$};
	\end{tikzpicture}""",
        "correct": r"$\left(1;+\infty \right)$",
        "wrongs": [
            r"$\left(-\infty;1 \right)$",
            r"$\left(-1;1 \right)$",
            r"$\left( 0;1\right)$"
        ],
        "loigiai": r"Dựa vào đồ thị, hàm số đi lên từ trái sang phải trên các khoảng $(-\infty; -1)$ và $(1; +\infty)$. Trong 4 phương án đã cho, chỉ có khoảng $(1; +\infty)$ thỏa mãn."
    },

    # 7. TN THPT Đợt 1 2020 – 101
    {
        "source": "TN THPT Đợt 1 2020 – 101",
        "prompt": r"Cho hàm số $f\left( x \right)$ có bảng biến thiên như sau. Hàm số đã cho đồng biến trên khoảng nào dưới đây?",
        "tikz": r"""\begin{tikzpicture}
			\tkzTabInit[nocadre,lgt=1.2,espcl=1.5,deltacl=0.6]
			{$x$ /0.6,$y'$ /0.6,$y$ /1.5}
			{$-\infty$,$-1$,$0$,$1$,$+\infty$}
			\tkzTabLine{,-,$0$,+,$0$,-,$0$,+,}
			\tkzTabVar{+/$+\infty$, -/$-1$,+/$4$,-/$-1$,+/$+\infty$}
		\end{tikzpicture}""",
        "correct": r"$\left( -1;0 \right)$",
        "wrongs": [
            r"$\left( -\infty ;-1 \right)$",
            r"$\left( 0;1 \right)$",
            r"$\left( -1;1 \right)$"
        ],
        "loigiai": r"Dựa vào bảng biến thiên, hàm số đồng biến trên các khoảng $(-1; 0)$ và $(1; +\infty)$. Do đó, hàm số đã cho đồng biến trên khoảng $(-1; 0)$."
    },

    # 8. TN THPT Đợt 1 2020 – 102
    {
        "source": "TN THPT Đợt 1 2020 – 102",
        "prompt": r"Cho hàm số $f\left( x \right)$ có bảng biến thiên như sau. Hàm số đã cho đồng biến trên khoảng nào dưới đây?",
        "tikz": r"""\begin{tikzpicture}
		\tkzTabInit[nocadre,lgt=1.2,espcl=1.5,deltacl=0.6]
		{$x$ /0.6,$y'$ /0.6,$y$ /1.5}
		{$-\infty$,$-1$,$0$,$1$,$+\infty$}
		\tkzTabLine{,+,$0$,-,$0$,+,$0$,-,}
		\tkzTabVar{-/$-\infty$, +/$4$,-/$1$,+/$4$,-/$-\infty$}
	\end{tikzpicture}""",
        "correct": r"$\left( 0;1 \right)$",
        "wrongs": [
            r"$\left( 1;+\infty  \right)$",
            r"$\left( -1;1 \right)$",
            r"$\left( -1;0 \right)$"
        ],
        "loigiai": r"Dựa vào bảng biến thiên, $y' > 0$ trên các khoảng $(-\infty; -1)$ và $(0; 1)$. Do đó hàm số đồng biến trên các khoảng $(-\infty; -1)$ và $(0; 1)$. Trong 4 phương án, chọn $(0; 1)$."
    },

    # 9. TN THPT Đợt 1 2020 – 103
    {
        "source": "TN THPT Đợt 1 2020 – 103",
        "prompt": r"Cho hàm số $f\left( x \right)$ có bảng biến thiên như sau. Hàm số đã cho đồng biến trên khoảng nào dưới đây?",
        "tikz": r"""\begin{tikzpicture}
\tkzTabInit[nocadre,lgt=1.2,espcl=1.5,deltacl=0.6]
{$x$ /0.6,$y'$ /0.6,$y$ /1.5}
{$-\infty$,$-2$,$0$,$2$,$+\infty$}
\tkzTabLine{,+,$0$,-,$0$,+,$0$,-,}
\tkzTabVar{-/$-\infty$, +/$3$,-/$2$,+/$3$,-/$-\infty$}		
\end{tikzpicture}""",
        "correct": r"$\left( 0;2 \right)$",
        "wrongs": [
            r"$\left( -2;2 \right)$",
            r"$\left( -2;0 \right)$",
            r"$\left( 2;+\infty  \right)$"
        ],
        "loigiai": r"Từ bảng biến thiên, hàm số đồng biến trên các khoảng $(-\infty; -2)$ và $(0; 2)$. Trong các phương án đã cho, hàm số đồng biến trên khoảng $(0; 2)$."
    },

    # 10. TN THPT Đợt 1 2020 – 104
    {
        "source": "TN THPT Đợt 1 2020 – 104",
        "prompt": r"Cho hàm số $y=f\left( x \right)$ có bảng biến thiên như sau. Hàm số đã cho đồng biến trên khoảng nào dưới đây?",
        "tikz": r"""\begin{tikzpicture}
			\tkzTabInit[nocadre,lgt=1.2,espcl=1.25,deltacl=0.6]
			{$x$ /0.6,$y'$ /0.6,$y$ /1.5}
			{$-\infty$,$-3$,$0$,$3$,$+\infty$}
			\tkzTabLine{,-,$0$,+,$0$,-,$0$,+,}
			\tkzTabVar{+/$+\infty$, -/$-1$,+/$1$,-/$-1$,+/$+\infty$}
		\end{tikzpicture}""",
        "correct": r"$\left( -3;0 \right)$",
        "wrongs": [
            r"$\left( -3;3 \right)$",
            r"$\left( 0;3 \right)$",
            r"$\left( -\infty ;-3 \right)$"
        ],
        "loigiai": r"Dựa vào bảng biến thiên, $y' > 0$ trên $(-3; 0)$ và $(3; +\infty)$. Do đó hàm số đồng biến trên khoảng $(-3; 0)$."
    },

    # 11. TN THPT 2020 Đợt 2 – 102
    {
        "source": "TN THPT 2020 Đợt 2 – 102",
        "prompt": r"Cho hàm số $y=f(x)$ có đồ thị là đường cong trong hình bên. Hàm số đã cho nghịch biến trên khoảng nào dưới đây?",
        "tikz": r"""\begin{tikzpicture}[scale=0.8, font=\footnotesize, line join=round, line cap=round, >=stealth]
			\draw (0,0) node [below left] {$O$};
			\draw[->] (-2,0)--(2,0) node[below] {$x$};
			\draw[->] (0,-0.6)--(0,2) node[right] {$y$};
			\draw[name path=c,samples=200,domain=-1.4:1.4,smooth,variable=\x] plot (\x,{-(\x)^4+2*(\x)^2});
			\draw[dashed](1,0)node[below]{$1$}|-(0,1)node[above right]{$1$} (-1,0)node[below]{$-1$}|-(0,1);
		\end{tikzpicture}""",
        "correct": r"$\left(-1; 0\right)$",
        "wrongs": [
            r"$\left(-\infty; -1\right)$",
            r"$\left(0; 1\right)$",
            r"$\left(0; +\infty\right)$"
        ],
        "loigiai": r"Dựa vào đồ thị, trên khoảng $(-1; 0)$ đường cong đi xuống từ trái sang phải, do đó hàm số nghịch biến trên khoảng $(-1; 0)$."
    },

    # 12. THPT 2020 Đợt 2 – 101
    {
        "source": "THPT 2020 Đợt 2 – 101",
        "prompt": r"Cho hàm số $y=f(x)$ có đồ thị là đường cong trong hình bên. Hàm số đã cho đồng biến trên khoảng nào dưới đây?",
        "tikz": r"""\begin{tikzpicture}[scale=0.7, font=\footnotesize, line join=round, line cap=round, >=stealth]
			\draw (0,0) node [below left] {$O$};
			\draw[->] (-2.5,0)--(2.8,0) node[below left] {$x$};
			\draw[->] (0,-2)--(0,3) node[below left] {$y$};
			\draw[samples=200,domain=-1.7:1.7,smooth,variable=\x] plot (\x,{-(\x)^4+2*(\x)^2+1});
			\path
			(0,1)node[below right]{$1$}
			(0,2)node[above right]{$2$}
			(-1,0)node[below]{$-2$}
			(1,0)node[below]{$2$};
			\draw[dashed](1,0)|-(0,2) (-1,0)|-(0,2);
		\end{tikzpicture}""",
        "correct": r"$(0; 1)$",
        "wrongs": [
            r"$(1; +\infty)$",
            r"$(-1; 0)$",
            r"$(-\infty; 0)$"
        ],
        "loigiai": r"Dựa vào đồ thị, trên khoảng $(0; 1)$ đường cong đi lên từ trái sang phải, do đó hàm số đồng biến trên khoảng $(0; 1)$."
    },

    # 13. TN THPT 2021 - Đề 101
    {
        "source": "TN THPT 2021 - Đề 101",
        "prompt": r"Cho hàm số $y=f(x)$ có đồ thị là đường cong trong hình bên. Hàm số đã cho nghịch biến trong khoảng nào dưới đây?",
        "tikz": r"""\begin{tikzpicture}[scale=.7, font=\footnotesize, line join=round, line cap=round, >=stealth]
			\def\xmin{-1.75}\def\xmax{1.75}\def\ymin{-2.25}\def\ymax{0.25}
			\draw[->] (\xmin-0.2,0)--(\xmax+0.2,0) node[below] {\footnotesize $x$};
			\draw[->] (0,\ymin-0.2)--(0,\ymax+0.2) node[right] {\footnotesize $y$};
			\draw (0,0) node [below left] {\footnotesize $O$};
			\foreach \x in {-1,1}\draw (\x,0.1)--(\x,-0.1) node [above] {\footnotesize $\x$};
			\foreach \y in {-2}\draw (0.1,\y)--(-0.1,\y) node [left] {\footnotesize $\y$};
			\clip (\xmin,\ymin) rectangle (\xmax,\ymax);
			\draw[thick,smooth,samples=200,domain=\xmin:\xmax] plot (\x,{1*((\x)^4)+-2*((\x)^2)-1});
			\draw[dashed] (-1,0)--(-1,-2)--(0,-2);\fill (-1,-2) circle (1pt);
			\draw[dashed] (1,0)--(1,-2)--(0,-2);\fill (1,-2) circle (1pt);
		\end{tikzpicture}""",
        "correct": r"$(0; 1)$",
        "wrongs": [
            r"$(-\infty; 0)$",
            r"$(0; +\infty)$",
            r"$(-1; 1)$"
        ],
        "loigiai": r"Dựa vào đồ thị, hàm số đạt cực đại tại $x = 0$ và cực tiểu tại $x = 1$. Trên khoảng $(0; 1)$, đồ thị hàm số đi xuống từ trái sang phải nên hàm số nghịch biến trên khoảng $(0; 1)$."
    },

    # 14. TN THPT 2021 - Đề 102
    {
        "source": "TN THPT 2021 - Đề 102",
        "prompt": r"Cho hàm số $y=f(x)$ có đồ thị là đường cong trong hình bên. Hàm số đã cho đồng biến trên khoảng nào dưới đây?",
        "tikz": r"""\begin{tikzpicture}[scale=.7, font=\footnotesize, line join=round, line cap=round, >=stealth]
			\def\xmin{-2}\def\xmax{2}\def\ymin{-0.25}\def\ymax{2.25}
			\draw[->] (\xmin-0.2,0)--(\xmax+0.2,0) node[below] {\footnotesize $x$};
			\draw[->] (0,\ymin-0.2)--(0,\ymax+0.2) node[right] {\footnotesize $y$};
			\draw (0,0) node [below left] {\footnotesize $O$};
			\foreach \x in {-1,1}\draw (\x,0.1)--(\x,-0.1) node [below] {\footnotesize $\x$};
			\foreach \y in {1,2}\draw (0.1,\y)--(-0.1,\y) node [left] {\footnotesize $\y$};
			\clip (\xmin,\ymin) rectangle (\xmax,\ymax);
			\draw[thick,smooth,samples=200,domain=\xmin:\xmax] plot (\x,{-1*((\x)^4)+2*((\x)^2)+1});
			\draw[dashed] (-1,0)--(-1,2)--(0,2);\fill (-1,2) circle (1pt);
			\draw[dashed] (1,0)--(1,2)--(0,2);\fill (1,2) circle (1pt);
		\end{tikzpicture}""",
        "correct": r"$(0; 1)$",
        "wrongs": [
            r"$(-1; 1)$",
            r"$(-\infty; 0)$",
            r"$(0; +\infty)$"
        ],
        "loigiai": r"Dựa vào đồ thị, hàm số đồng biến trên các khoảng $(-\infty; -1)$ và $(0; 1)$. Do đó chọn $(0; 1)$."
    },

    # 15. TN THPT 2021 - Đề 103
    {
        "source": "TN THPT 2021 - Đề 103",
        "prompt": r"Cho hàm số $y=f(x)$ có đồ thị là đường cong trong hình bên. Hàm số đã cho đồng biến trên khoảng nào dưới đây?",
        "tikz": r"""\begin{tikzpicture}[scale=.7, font=\footnotesize, line join=round, line cap=round, >=stealth]
			\def\xmin{-1.5}\def\xmax{3.25}\def\ymin{-2.15}\def\ymax{2.15}
			\draw[->] (\xmin-0.2,0)--(\xmax+0.2,0) node[below] {\footnotesize $x$};
			\draw[->] (0,\ymin-0.2)--(0,\ymax+0.2) node[right] {\footnotesize $y$};
			\draw (0,0) node [below left] {\footnotesize $O$};
			\foreach \x in {-1,1,2}\draw (\x,0.1)--(\x,-0.1) node [below] {\footnotesize $\x$};
			\foreach \y in {-2,-1,1,2}\draw (0.1,\y)--(-0.1,\y) node [left] {\footnotesize $\y$};
			\clip (\xmin,\ymin) rectangle (\xmax,\ymax);
			\draw[thick,smooth,samples=200,domain=\xmin:\xmax] plot (\x,{-1*((\x)^3)+3*((\x)^2)+0*(\x)+-2});
			\draw[dashed] (-1,0)--(-1,2)--(0,2);\fill (-1,2) circle (1pt);
			\draw[dashed] (1,0)--(1,0)--(0,0);\fill (1,0) circle (1pt);
			\draw[dashed] (2,0)--(2,2)--(0,2);\fill (2,2) circle (1pt);
	\end{tikzpicture}""",
        "correct": r"$(0; 2)$",
        "wrongs": [
            r"$(-\infty; 2)$",
            r"$(-2; 2)$",
            r"$(2; +\infty)$"
        ],
        "loigiai": r"Dựa vào đồ thị hàm số bậc ba, đồ thị đạt cực tiểu tại $x = 0$ và cực đại tại $x = 2$. Trên khoảng $(0; 2)$, đồ thị đi lên từ trái sang phải nên hàm số đồng biến trên khoảng $(0; 2)$."
    },

    # 16. TN THPT 2021 - Đề 104
    {
        "source": "TN THPT 2021 - Đề 104",
        "prompt": r"Cho hàm số $y=f(x)$ có đồ thị là đường cong trong hình bên. Hàm số đã cho nghịch biến trên khoảng nào dưới đây?",
        "tikz": r"""\begin{tikzpicture}[scale=.7, font=\footnotesize, line join=round, line cap=round, >=stealth]
			\def\xmin{-2.25}\def\xmax{2.25}\def\ymin{-1.25}\def\ymax{3.25}
			\draw[->] (\xmin-0.2,0)--(\xmax+0.2,0) node[below] {\footnotesize $x$};
			\draw[->] (0,\ymin-0.2)--(0,\ymax+0.2) node[right] {\footnotesize $y$};
			\draw (0,0) node [below left] {\footnotesize $O$};
			\foreach \x in {-2,-1,1,2}\draw (\x,0.1)--(\x,-0.1) node [below] {\footnotesize $\x$};
			\foreach \y in {-1,1,2,3}\draw (0.1,\y)--(-0.1,\y) node [left] {\footnotesize $\y$};
			\clip (\xmin,\ymin) rectangle (\xmax,\ymax);
			\draw[thick,smooth,samples=200,domain=\xmin:\xmax] plot (\x,{1*((\x)^3)+0*((\x)^2)+-3*(\x)+1});
			\draw[dashed] (-2,0)--(-2,-1)--(0,-1);\fill (-2,-1) circle (1pt);
			\draw[dashed] (-1,0)--(-1,3)--(0,3);\fill (-1,3) circle (1pt);
			\draw[dashed] (1,0)--(1,-1)--(0,-1);\fill (1,-1) circle (1pt);
			\draw[dashed] (2,0)--(2,3)--(0,3);\fill (2,3) circle (1pt);
		\end{tikzpicture}""",
        "correct": r"$(-1; 1)$",
        "wrongs": [
            r"$(1; +\infty)$",
            r"$(-\infty; 1)$",
            r"$(0; 3)$"
        ],
        "loigiai": r"Dựa vào đồ thị, hàm số đạt cực đại tại $x = -1$ và đạt cực tiểu tại $x = 1$. Trên khoảng $(-1; 1)$, đường cong đi xuống từ trái sang phải nên hàm số nghịch biến trên khoảng $(-1; 1)$."
    },

    # 17. TN THPT 2022 - Đề 101
    {
        "source": "TN THPT 2022 - Đề 101",
        "prompt": r"Cho hàm số $y=f\left( x \right)$ có bảng biến thiên như sau. Hàm số đã cho nghịch biến trên khoảng nào dưới đây?",
        "tikz": r"""\begin{tikzpicture}
			\tkzTabInit[nocadre,lgt=1.2,espcl=1.5,deltacl=0.6]
			{$x$ /0.6,$y'$ /0.6,$y$ /1.6}
			{$-\infty$,$-1$,$0$,$1$,$+\infty$}
			\tkzTabLine{,-,$0$,+,$0$,-,$0$,+,}
			\tkzTabVar{+/$+\infty$, -/$0$,+/$3$,-/$0$,+/$+\infty$}
		\end{tikzpicture}""",
        "correct": r"$\left( 0;1 \right)$",
        "wrongs": [
            r"$\left( 1;+\infty \right)$",
            r"$\left( -1;0 \right)$",
            r"$\left( 0;+\infty \right)$"
        ],
        "loigiai": r"Dựa vào bảng biến thiên, hàm số đã cho nghịch biến trên các khoảng $\left( -\infty ;-1 \right)$ và $\left( 0;1 \right)$. Do đó chọn khoảng $\left( 0;1 \right)$."
    },

    # 18. TN THPT 2022 - Đề 102
    {
        "source": "TN THPT 2022 - Đề 102",
        "prompt": r"Cho hàm số $y=f\left( x \right)$ có bảng biến thiên như sau. Hàm số đã cho nghịch biến trên khoảng nào dưới đây?",
        "tikz": r"""\begin{tikzpicture}
			\tkzTabInit[nocadre,lgt=1.2,espcl=1.5,deltacl=0.6]
			{$x$ /0.6,$y'$ /0.6,$y$ /1.4}
			{$-\infty$,$-1$,$0$,$1$,$+\infty$}
			\tkzTabLine{,-,$0$,+,$0$,-,$0$,+,}
			\tkzTabVar{+/$+\infty$, -/$0$,+/$3$,-/$0$,+/$+\infty$}
		\end{tikzpicture}""",
        "correct": r"$\left( 0;1 \right)$",
        "wrongs": [
            r"$\left( 0;+\infty \right)$",
            r"$\left( 1;+\infty \right)$",
            r"$\left( -1;0 \right)$"
        ],
        "loigiai": r"Dựa vào bảng biến thiên, hàm số nghịch biến trên các khoảng $(-\infty; -1)$ và $(0; 1)$. Trong 4 phương án, chọn $(0; 1)$."
    },

    # 19. TN THPT 2022 - Đề 103
    {
        "source": "TN THPT 2022 - Đề 103",
        "prompt": r"Cho hàm số $y=f\left( x \right)$ có bảng biến thiên như hình vẽ sau. Hàm số đã cho đồng biến trên khoảng nào dưới đây?",
        "tikz": r"""\begin{tikzpicture}
			\tkzTabInit[nocadre,lgt=1.2,espcl=1.5,deltacl=0.6]
			{$x$ /0.6,$y'$ /0.6,$y$ /1.6}
			{$-\infty$,$-1$,$0$,$1$,$+\infty$}
			\tkzTabLine{,-,$0$,+,$0$,-,$0$,+,}
			\tkzTabVar{+/$+\infty$, -/$0$,+/$3$,-/$0$,+/$+\infty$}
		\end{tikzpicture}""",
        "correct": r"$\left( -1;0 \right)$",
        "wrongs": [
            r"$\left( 0;3 \right)$",
            r"$\left( 0;+\infty \right)$",
            r"$\left( -\infty ;-1 \right)$"
        ],
        "loigiai": r"Dựa vào bảng biến thiên, hàm số đồng biến trên các khoảng $(-1; 0)$ và $(1; +\infty)$. Do đó chọn $(-1; 0)$."
    }
]

# Track shuffled indices to give varied questions across consecutive calls
_shuffled_pool = []

def sinh_cau_de_thi_thpt_don_dieu_cuc_tri():
    r"""
    Sinh ngẫu nhiên 1 câu hỏi từ ngân hàng 19 câu thi THPT Quốc gia
    (chủ đề Sự biến thiên - Cực trị qua BBT và Đồ thị).
    Tự động xáo trộn các phương án lựa chọn và đánh dấu \True.
    """
    global _shuffled_pool
    if not _shuffled_pool:
        _shuffled_pool = list(range(len(DANH_SACH_CAU_HOI)))
        random.shuffle(_shuffled_pool)
        
    idx = _shuffled_pool.pop()
    data = DANH_SACH_CAU_HOI[idx]
    
    source = data["source"]
    prompt = data["prompt"]
    tikz = data["tikz"]
    correct = data["correct"]
    wrongs = data["wrongs"]
    loigiai = data["loigiai"]
    
    # Tạo 4 phương án và xáo trộn vị trí
    phuongan = [
        f"\t\t{{\\True {correct}}}\n",
        f"\t\t{{{wrongs[0]}}}\n",
        f"\t\t{{{wrongs[1]}}}\n",
        f"\t\t{{{wrongs[2]}}}\n"
    ]
    random.shuffle(phuongan)
    choices_str = "".join(phuongan)
    
    # Cấu trúc chuẩn theo đúng đề bài của người dùng:
    # \begin{ex}[<source>]
    #     \immini{ <câu dẫn> \choice <4 phương án> }
    #     { <tikz> }
    #     \loigiai{ <lời giải> }
    # \end{ex}
    full_ex = (
        f"\\begin{{ex}}[{source}]\n"
        f"\t\\immini{{{prompt}\n"
        f"\t\t\\choice\n"
        f"{choices_str}\t}}\n"
        f"\t{{\n"
        f"{tikz}\n"
        f"\t}}\n"
        f"\\loigiai{{\n"
        f"\t{loigiai}\n"
        f"}}\n"
        f"\\end{{ex}}"
    )
    return full_ex
