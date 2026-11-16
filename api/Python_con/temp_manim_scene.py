from manim import *
config.pixel_width = 720
config.pixel_height = 1280
config.frame_width = 9.0
config.frame_height = 16.0

class MyScene(Scene):
    def construct(self):
        vn_template = TexTemplate()
        vn_template.add_to_preamble(r'\usepackage[utf8]{inputenc}')
        vn_template.add_to_preamble(r'\usepackage[T5]{fontenc}')
        vn_template.add_to_preamble(r'\usepackage{amsmath, amssymb}')
        pt_pt_0_dot = Dot(point=[-2.0, 0.0, 0], color=TEAL, radius=0.05)
        pt_pt_0_label = MathTex(r"A").move_to(pt_pt_0_dot.get_center()).shift(0.33*RIGHT + 0.78*UP)
        pt_pt_1_dot = Dot(point=[-4.0, -2.0, 0], color=TEAL, radius=0.05)
        pt_pt_1_label = MathTex(r"B").move_to(pt_pt_1_dot.get_center()).shift(-0.22*RIGHT + -0.22*UP)
        pt_pt_2_dot = Dot(point=[1.0, -2.0, 0], color=TEAL, radius=0.05)
        pt_pt_2_label = MathTex(r"C").move_to(pt_pt_2_dot.get_center()).shift(-0.2*RIGHT + -0.2*UP)
        pt_pt_3_dot = Dot(point=[3.0, 0.0, 0], color=TEAL, radius=0.05)
        pt_pt_3_label = MathTex(r"D").move_to(pt_pt_3_dot.get_center()).shift(0.33*RIGHT + 0.78*UP)
        pt_pt_4_dot = Dot(point=[-2.0, 4.0, 0], color=TEAL, radius=0.05)
        pt_pt_4_label = MathTex(r"S").move_to(pt_pt_4_dot.get_center()).shift(0.0*RIGHT + 0.6*UP)
        line_pt_pt_0pt_pt_1 = DashedLine(pt_pt_0_dot.get_center(), pt_pt_1_dot.get_center(), color=BLUE, dash_length=0.15)
        line_pt_pt_1pt_pt_2 = Line(pt_pt_1_dot.get_center(), pt_pt_2_dot.get_center(), color=BLUE)
        line_pt_pt_3pt_pt_2 = Line(pt_pt_3_dot.get_center(), pt_pt_2_dot.get_center(), color=BLUE)
        line_pt_pt_3pt_pt_0 = DashedLine(pt_pt_3_dot.get_center(), pt_pt_0_dot.get_center(), color=BLUE, dash_length=0.15)
        line_pt_pt_0pt_pt_4 = DashedLine(pt_pt_0_dot.get_center(), pt_pt_4_dot.get_center(), color=BLUE, dash_length=0.15)
        line_pt_pt_4pt_pt_3 = Line(pt_pt_4_dot.get_center(), pt_pt_3_dot.get_center(), color=BLUE)
        line_pt_pt_3pt_pt_4 = Line(pt_pt_3_dot.get_center(), pt_pt_4_dot.get_center(), color=BLUE)
        line_pt_pt_4pt_pt_2 = Line(pt_pt_4_dot.get_center(), pt_pt_2_dot.get_center(), color=BLUE)
        line_pt_pt_2pt_pt_4 = Line(pt_pt_2_dot.get_center(), pt_pt_4_dot.get_center(), color=BLUE)
        line_pt_pt_4pt_pt_1 = Line(pt_pt_4_dot.get_center(), pt_pt_1_dot.get_center(), color=BLUE)
        txt_0_q = Tex(r"""Cho hình chóp $S.ABCD$""", tex_template=vn_template, font_size=44)
        txt_0_q.move_to([-1.69, -4.67, 0])
        if txt_0_q.width > config.frame_width - 1.2:
            txt_0_q.scale_to_fit_width(config.frame_width - 1.2)
        if txt_0_q.height > config.frame_height - 1.2:
            txt_0_q.scale_to_fit_height(config.frame_height - 1.2)
        self.play(Create(pt_pt_0_dot), Write(pt_pt_0_label), Create(pt_pt_1_dot), Write(pt_pt_1_label), Create(line_pt_pt_0pt_pt_1), Create(pt_pt_2_dot), Write(pt_pt_2_label), Create(line_pt_pt_1pt_pt_2), Create(pt_pt_3_dot), Write(pt_pt_3_label), Create(line_pt_pt_3pt_pt_2), Create(line_pt_pt_3pt_pt_0), Create(pt_pt_4_dot), Write(pt_pt_4_label), Create(line_pt_pt_0pt_pt_4), Create(line_pt_pt_4pt_pt_3), Create(line_pt_pt_3pt_pt_4), Create(line_pt_pt_4pt_pt_2), Create(line_pt_pt_2pt_pt_4), Create(line_pt_pt_4pt_pt_1), Write(txt_0_q))
