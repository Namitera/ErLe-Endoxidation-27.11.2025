from manim import *


class Atom(VGroup):
    def __init__(self, symbol: str, charge=0, index=1, **kwargs):
        super().__init__(**kwargs)

        # symbol group
        symbolstring = symbol
        if charge != 0:
            symbolstring += "^{"+f"{charge}"+"}"
        if index != 1:
            symbolstring += "_{"+f"{index}"+"}"

        self.symbolgroup = MathTex(symbolstring)
        self.add(self.symbolgroup)

        self.current_mode = "text"

        # physics group
        circle = Circle(radius=0.3, color=RED).surround(self.symbolgroup)
        plus = Tex("+").set_color(RED)
        self.physicsgroup = VGroup(circle, plus)

        
    def to_text(self):
        if self.current_mode != "text":
            self.remove(*self.submobjects)
            self.add(self.symbolgroup)
            self.current_mode = "text"

    def to_physics(self):
        if self.current_mode != "physics":
            self.remove(*self.submobjects)
            self.add(self.physicsgroup)
            self.current_mode = "physics"



class NADplus(VGroup):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)

        outer_ring = [
            [0, 1, 0],
            [0.433, 0.75, 0],
            [0.866, 0.5, 0],
            [0.866, -0.5, 0],
            [0, -1, 0],
            [-0.866, -0.5, 0],
            [-0.866, 0.5, 0],
            [-0.433, 0.75, 0]
            ]
        
        inner_ring = [
            [0, 0.8, 0],
            [0.3464, 0.6, 0],
            [0.692, 0.4, 0],
            [0.692, -0.4, 0],
            [0, -0.8, 0],
            [-0.692, -0.4, 0],
            [-0.692, 0.4, 0],
        ]

        line1 = Line(outer_ring[0], outer_ring[1]).set_opacity(0.3)
        line2 = Line(outer_ring[1], outer_ring[2])
        line3 = Line(outer_ring[2], outer_ring[3])
        line4 = Line(outer_ring[3], outer_ring[4])
        line5 = Line(outer_ring[4], outer_ring[5])
        line6 = Line(outer_ring[5], outer_ring[6])
        line7 = Line(outer_ring[6], outer_ring[7])
        line8 = Line(outer_ring[7], outer_ring[0]).set_opacity(0.3)

        line10 = Line(inner_ring[1], inner_ring[2])
        line12 = Line(inner_ring[3], inner_ring[4])
        line14 = Line(inner_ring[5], inner_ring[6])

        hexagon_outer = VGroup(line1, line2, line3, line4, line5, line6, line7, line8)
        hexagon_inner = VGroup(line10, line12, line14)

        npos = MathTex("N^{+}").move_to(outer_ring[0]).shift(RIGHT*0.15)
        h = MathTex("H").move_to(outer_ring[4]).shift(UP*-1)
        h_line = Line(outer_ring[4], [h.get_x(), h.get_y() + 0.35, 0])

        nh2 = MathTex("NH_{2}").move_to(h).shift(RIGHT*1.732)
        nh2_line2 = Line(outer_ring[4], [h.get_x(), h.get_y() + 0.35, 0]).shift(RIGHT*1.732)
        nh2_line1 = Line(outer_ring[3], nh2_line2.get_start())

        o = MathTex("O").move_to(outer_ring[3]).shift(RIGHT*1.732 + UP*-0.1)
        o_line1 = Line(nh2_line2.get_start() + [-0.08, 0.04, 0], [o.get_x() - 0.32, o.get_y() - 0.05, 0])
        o_line2 = Line(nh2_line2.get_start() + [0, -0.1, 0], [o.get_x() - 0.23, o.get_y() - 0.2, 0])

        rib = MathTex("Rib").move_to(npos).shift(LEFT*0.4 + UP*1)
        adp = MathTex("ADP").move_to(rib).shift(RIGHT*1.6)
        rib_line = Line(npos.get_center() + [0, 0.3, 0], npos.get_center() + [0, 0.7, 0]).shift(RIGHT*-0.15)
        adp_line = Line(rib.get_center() + [0.5, 0, 0], adp.get_center() + [-0.6, 0, 0])
    
        ## acsess
        self.npos = npos
        self.h = h
        self.hexagon_outer = hexagon_outer
        self.hexagon_inner = hexagon_inner
        self.adp = adp
        self.rib = rib
        self.o = o
        self.nh2 = nh2

        all = VGroup(hexagon_outer,  hexagon_inner, npos, h, h_line, nh2, nh2_line1, nh2_line2, o, o_line1, o_line2, rib, adp, rib_line, adp_line)
        self.add(all)



class NADH(VGroup):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)

        outer_ring = [
            [0, 1, 0],
            [0.433, 0.75, 0],
            [0.866, 0.5, 0],
            [0.866, -0.5, 0],
            [0, -1, 0],
            [-0.866, -0.5, 0],
            [-0.866, 0.5, 0],
            [-0.433, 0.75, 0]
            ]
        
        inner_ring = [
            [0, 0.8, 0],
            [0.3464, 0.6, 0],
            [0.692, 0.4, 0],
            [0.692, -0.4, 0],
            [0, -0.8, 0],
            [-0.692, -0.4, 0],
            [-0.692, 0.4, 0],
        ]

        line1 = Line(outer_ring[0], outer_ring[1]).set_opacity(0.3)
        line2 = Line(outer_ring[1], outer_ring[2])
        line3 = Line(outer_ring[2], outer_ring[3])
        line4 = Line(outer_ring[3], outer_ring[4])
        line5 = Line(outer_ring[4], outer_ring[5])
        line6 = Line(outer_ring[5], outer_ring[6])
        line7 = Line(outer_ring[6], outer_ring[7])
        line8 = Line(outer_ring[7], outer_ring[0]).set_opacity(0.3)

        line11 = Line(inner_ring[2], inner_ring[3])
        line14 = Line(inner_ring[5], inner_ring[6])

        hexagon_outer = VGroup(line1, line2, line3, line4, line5, line6, line7, line8)
        hexagon_inner = VGroup(line11, line14)

        n = MathTex("N").move_to(outer_ring[0])
        h0_point = [outer_ring[4][0], outer_ring[4][1] - 1, 0] 
        h1 = MathTex("H").move_to(outer_ring[4]).shift(UP*-1 + RIGHT*-0.5)
        h2 = MathTex("H").move_to(outer_ring[4]).shift(UP*-1 + RIGHT*0.5)
        h1_line = Line(outer_ring[4], [h1.get_x() + 0.2, h1.get_y() + 0.35, 0])
        h2_line = Line(outer_ring[4], [h2.get_x() - 0.2, h2.get_y() + 0.35, 0])

        nh2 = MathTex("NH_{2}").move_to([h0_point[0], h0_point[1], 0]).shift(RIGHT*1.732)
        nh2_line2 = Line(outer_ring[4], [h0_point[0], h0_point[1] + 0.35, 0]).shift(RIGHT*1.732)
        nh2_line1 = Line(outer_ring[3], nh2_line2.get_start())

        o = MathTex("O").move_to(outer_ring[3]).shift(RIGHT*1.732 + UP*-0.1)
        o_line1 = Line(nh2_line2.get_start() + [-0.08, 0.04, 0], [o.get_x() - 0.32, o.get_y() - 0.05, 0])
        o_line2 = Line(nh2_line2.get_start() + [0, -0.1, 0], [o.get_x() - 0.23, o.get_y() - 0.2, 0])

        rib = MathTex("Rib").move_to(n).shift(LEFT*0.25 + UP*1)
        adp = MathTex("ADP").move_to(rib).shift(RIGHT*1.6)
        rib_line = Line(n.get_center() + [0, 0.3, 0], n.get_center() + [0, 0.7, 0])
        adp_line = Line(rib.get_center() + [0.5, 0, 0], adp.get_center() + [-0.6, 0, 0])
    
        all = VGroup(hexagon_outer,  hexagon_inner, n, h1, h2, h1_line, h2_line, nh2, nh2_line1, nh2_line2, o, o_line1, o_line2, rib, adp, rib_line, adp_line)
        self.add(all)



class FAD(VGroup):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)

        outer_ring1 = [
            [0, 1, 0],
            [0.433, 0.75, 0],
            [0.866, 0.5, 0],
            [0.866, -0.5, 0],
            [0.433, -0.75, 0],
            [0, -1, 0],
            [-0.433, -0.75, 0],
            [-0.866, -0.5, 0],
            [-0.866, 0.5, 0],
            [-0.433, 0.75, 0]
            ]
        
        inner_ring1 = [
            [0, 0.8, 0],
            [0.3464, 0.6, 0],
            [0.692, 0.4, 0],
            [0.692, -0.4, 0],
            [0, -0.8, 0],
            [-0.692, -0.4, 0],
            [-0.692, 0.4, 0]
        ]

        outer_ring2 = [
            [-1.732, 1, 0],
            [-0.866, 0.5, 0],
            [-0.866, -0.5, 0],
            [-1.732, -1, 0],
            [-2.598, -0.5, 0],
            [-2.598, 0.5, 0]
            ]
        
        inner_ring2 = [
            [-1.732, 0.8, 0],
            [-1.04, 0.4, 0],
            [-1.04, -0.4, 0],
            [-1.732, -0.8, 0],
            [-2.424, -0.4, 0],
            [-2.424, 0.4, 0]
        ]

        outer_ring3 = [
            [1.732, 1, 0],
            [2.165, 0.75, 0],
            [2.618, 0.5, 0],
            [2.618, 0, 0],
            [2.618, -0.5, 0],
            [2.165, -0.75, 0],
            [1.732, -1, 0],
            [1.299, -0.75, 0],
            [0.866, -0.5, 0],
            [0.866, 0.5, 0],
            [1.299, 0.75, 0]
            ]

        inner_ring3 = [
            [1.732, 0.8, 0],
            [2.424, 0.4, 0],
            [2.424, -0.4, 0],
            [1.732, -0.8, 0],
            [1.3856, -0.6, 0],
            [1.04, -0.4, 0],
            [1.04, 0.4, 0]
        ]

        line1 = Line(outer_ring1[0], outer_ring1[1]).set_opacity(0.3)
        line2 = Line(outer_ring1[1], outer_ring1[2])
        line3 = Line(outer_ring1[2], outer_ring1[3])
        line4 = Line(outer_ring1[3], outer_ring1[4])
        line5 = Line(outer_ring1[4], outer_ring1[5]).set_opacity(0.3)
        line6 = Line(outer_ring1[5], outer_ring1[6]).set_opacity(0.3)
        line7 = Line(outer_ring1[6], outer_ring1[7])
        line8 = Line(outer_ring1[7], outer_ring1[8])
        line9 = Line(outer_ring1[8], outer_ring1[9])
        line10 = Line(outer_ring1[8], outer_ring1[0]).set_opacity(0.3)
        line11 = Line(inner_ring1[1], inner_ring1[2]) #inner
        hexagon1_outer = VGroup(line1, line2, line3, line4, line5, line6, line7, line8, line9, line10)
        hexagon1_inner = VGroup(line11)

        line21 = Line(outer_ring2[0], outer_ring2[1])
        line22 = Line(outer_ring2[1], outer_ring2[2])
        line23 = Line(outer_ring2[2], outer_ring2[3])
        line24 = Line(outer_ring2[3], outer_ring2[4])
        line25 = Line(outer_ring2[4], outer_ring2[5])
        line26 = Line(outer_ring2[5], outer_ring2[0])
        line27 = Line(inner_ring2[1], inner_ring2[2]) #inner
        line28 = Line(inner_ring2[3], inner_ring2[4]) 
        line29 = Line(inner_ring2[5], inner_ring2[0])
        hexagon2_outer = VGroup(line21, line22, line23, line24, line25, line26)
        hexagon2_inner = VGroup(line27, line28, line29)

        line31 = Line(outer_ring3[0], outer_ring3[1])
        line32 = Line(outer_ring3[1], outer_ring3[2]).set_opacity(0.3)
        line33 = Line(outer_ring3[2], outer_ring3[3]).set_opacity(0.3)
        line34 = Line(outer_ring3[3], outer_ring3[4])
        line35 = Line(outer_ring3[4], outer_ring3[5])
        line36 = Line(outer_ring3[5], outer_ring3[6]).set_opacity(0.3)
        line37 = Line(outer_ring3[6], outer_ring3[7]).set_opacity(0.3)
        line38 = Line(outer_ring3[7], outer_ring3[8])
        line39 = Line(outer_ring3[8], outer_ring3[9])
        line310 = Line(outer_ring3[9], outer_ring3[0])
        line311 = Line(inner_ring3[4], inner_ring3[5]) #inner
        hexagon3_outer = VGroup(line31, line32, line33, line34, line35, line36, line37, line38, line39, line310)
        hexagon3_inner = VGroup(line311)

        ring1 = VGroup(hexagon1_outer,hexagon1_inner)
        ring2 = VGroup(hexagon2_outer,hexagon2_inner)
        ring3 = VGroup(hexagon3_outer, hexagon3_inner)

        n1 = MathTex("N").move_to(outer_ring1[0])
        n2 = MathTex("N").move_to(outer_ring1[5])
        n3 = MathTex("N").move_to(outer_ring3[6])
        nh = MathTex("NH").move_to(outer_ring3[2]).shift(RIGHT*0.2)

        h3c1 = MathTex(r"H_{3}C").move_to(outer_ring2[0]).shift(RIGHT*-1.8 +UP*-0.2)
        h3c2 = MathTex(r"H_{3}C").move_to(outer_ring2[3]).shift(RIGHT*-1.8 +UP*0.2)
        h3c1_line = Line(outer_ring2[5], [h3c1.get_x() +0.5, h3c1.get_y(), 0])
        h3c2_line = Line(outer_ring2[4], [h3c2.get_x() +0.5, h3c2.get_y(), 0])

        r = MathTex("R").move_to(outer_ring1[5]).shift(UP*-1)
        r_line = Line([n2.get_x(), n2.get_y() - 0.3, 0], [r.get_x(), r.get_y() + 0.3, 0])

        o = MathTex("O").move_to(n3).shift(RIGHT*1.6)
        o_line1 = Line(line35.get_start() + [0.01, 0.04, 0], [o.get_x() - 0.2, o.get_y() +0.1, 0])
        o_line2 = Line(line35.get_start() + [-0.1, -0.05, 0], [o.get_x() - 0.25, o.get_y() -0.05 , 0])

        o2 = MathTex("O").move_to(outer_ring3[0]).shift(UP*0.7)
        o2_line1 = Line(outer_ring3[0], [o2.get_x(), o2.get_y() - 0.2, 0]).shift(RIGHT*0.07 + UP*-0.06)
        o2_line2 = Line(outer_ring3[0], [o2.get_x(), o2.get_y() - 0.2, 0]).shift(RIGHT*-0.07 + UP*-0.06)

        symbols = VGroup(n1,n2,n3,nh,h3c1,h3c1_line,h3c2,h3c2_line,r,r_line,o,o_line1,o_line2,o2,o2_line1,o2_line2)

        all = VGroup(symbols)
        self.add(ring1,ring2,ring3,all)



class FADH2(VGroup):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)

        outer_ring1 = [
            [0, 1, 0],
            [0.433, 0.75, 0],
            [0.866, 0.5, 0],
            [0.866, -0.5, 0],
            [0.433, -0.75, 0],
            [0, -1, 0],
            [-0.433, -0.75, 0],
            [-0.866, -0.5, 0],
            [-0.866, 0.5, 0],
            [-0.433, 0.75, 0]
            ]
        
        inner_ring1 = [
            [0, 0.8, 0],
            [0.3464, 0.6, 0],
            [0.692, 0.4, 0],
            [0.692, -0.4, 0],
            [0, -0.8, 0],
            [-0.692, -0.4, 0],
            [-0.692, 0.4, 0]
        ]

        outer_ring2 = [
            [-1.732, 1, 0],
            [-0.866, 0.5, 0],
            [-0.866, -0.5, 0],
            [-1.732, -1, 0],
            [-2.598, -0.5, 0],
            [-2.598, 0.5, 0]
            ]
        
        inner_ring2 = [
            [-1.732, 0.8, 0],
            [-1.04, 0.4, 0],
            [-1.04, -0.4, 0],
            [-1.732, -0.8, 0],
            [-2.424, -0.4, 0],
            [-2.424, 0.4, 0]
        ]

        outer_ring3 = [
            [1.732, 1, 0],
            [2.165, 0.75, 0],
            [2.618, 0.5, 0],
            [2.618, 0, 0],
            [2.618, -0.5, 0],
            [2.165, -0.75, 0],
            [1.732, -1, 0],
            [1.299, -0.75, 0],
            [0.866, -0.5, 0],
            [0.866, 0.5, 0],
            [1.299, 0.75, 0]
            ]

        inner_ring3 = [
            [1.732, 0.8, 0],
            [2.424, 0.4, 0],
            [2.424, -0.4, 0],
            [1.732, -0.8, 0],
            [1.3856, -0.6, 0],
            [1.04, -0.4, 0],
            [1.04, 0.4, 0]
        ]

        line1 = Line(outer_ring1[0], outer_ring1[1]).set_opacity(0.3)
        line2 = Line(outer_ring1[1], outer_ring1[2])
        line3 = Line(outer_ring1[2], outer_ring1[3])
        line4 = Line(outer_ring1[3], outer_ring1[4])
        line5 = Line(outer_ring1[4], outer_ring1[5]).set_opacity(0.3)
        line6 = Line(outer_ring1[5], outer_ring1[6]).set_opacity(0.3)
        line7 = Line(outer_ring1[6], outer_ring1[7])
        line8 = Line(outer_ring1[7], outer_ring1[8])
        line9 = Line(outer_ring1[8], outer_ring1[9])
        line10 = Line(outer_ring1[8], outer_ring1[0]).set_opacity(0.3)
        hexagon1_outer = VGroup(line1, line2, line3, line4, line5, line6, line7, line8, line9, line10)
        hexagon1_inner = VGroup()

        line21 = Line(outer_ring2[0], outer_ring2[1])
        line22 = Line(outer_ring2[1], outer_ring2[2])
        line23 = Line(outer_ring2[2], outer_ring2[3])
        line24 = Line(outer_ring2[3], outer_ring2[4])
        line25 = Line(outer_ring2[4], outer_ring2[5])
        line26 = Line(outer_ring2[5], outer_ring2[0])
        line27 = Line(inner_ring2[1], inner_ring2[2]) #inner
        line28 = Line(inner_ring2[3], inner_ring2[4]) 
        line29 = Line(inner_ring2[5], inner_ring2[0])
        hexagon2_outer = VGroup(line21, line22, line23, line24, line25, line26)
        hexagon2_inner = VGroup(line27, line28, line29)

        line31 = Line(outer_ring3[0], outer_ring3[1])
        line32 = Line(outer_ring3[1], outer_ring3[2]).set_opacity(0.3)
        line33 = Line(outer_ring3[2], outer_ring3[3]).set_opacity(0.3)
        line34 = Line(outer_ring3[3], outer_ring3[4])
        line35 = Line(outer_ring3[4], outer_ring3[5])
        line36 = Line(outer_ring3[5], outer_ring3[6]).set_opacity(0.3)
        line37 = Line(outer_ring3[6], outer_ring3[7]).set_opacity(0.3)
        line38 = Line(outer_ring3[7], outer_ring3[8])
        line39 = Line(outer_ring3[8], outer_ring3[9])
        line310 = Line(outer_ring3[9], outer_ring3[0])
        line311 = Line(inner_ring3[5], inner_ring3[6]) #inner
        hexagon3_outer = VGroup(line31, line32, line33, line34, line35, line36, line37, line38, line39, line310)
        hexagon3_inner = VGroup(line311)

        ring1 = VGroup(hexagon1_outer,hexagon1_inner)
        ring2 = VGroup(hexagon2_outer,hexagon2_inner)
        ring3 = VGroup(hexagon3_outer, hexagon3_inner)

        n1 = MathTex("N").move_to(outer_ring1[0])
        n2 = MathTex("N").move_to(outer_ring1[5])
        n3 = MathTex("N").move_to(outer_ring3[6])
        nh = MathTex("NH").move_to(outer_ring3[2]).shift(RIGHT*0.2)

        h1 = MathTex("H").next_to(n1,UP*0.4)
        h2 = MathTex("H").next_to(n3,UP*-0.4)

        h3c1 = MathTex(r"H_{3}C").move_to(outer_ring2[0]).shift(RIGHT*-1.8 +UP*-0.2)
        h3c2 = MathTex(r"H_{3}C").move_to(outer_ring2[3]).shift(RIGHT*-1.8 +UP*0.2)
        h3c1_line = Line(outer_ring2[5], [h3c1.get_x() +0.5, h3c1.get_y(), 0])
        h3c2_line = Line(outer_ring2[4], [h3c2.get_x() +0.5, h3c2.get_y(), 0])

        r = MathTex("R").move_to(outer_ring1[5]).shift(UP*-1)
        r_line = Line([n2.get_x(), n2.get_y() - 0.3, 0], [r.get_x(), r.get_y() + 0.3, 0])

        o = MathTex("O").move_to(n3).shift(RIGHT*1.6)
        o_line1 = Line(line35.get_start() + [0.01, 0.04, 0], [o.get_x() - 0.2, o.get_y() +0.1, 0])
        o_line2 = Line(line35.get_start() + [-0.1, -0.05, 0], [o.get_x() - 0.25, o.get_y() -0.05 , 0])

        o2 = MathTex("O").move_to(outer_ring3[0]).shift(UP*0.7)
        o2_line1 = Line(outer_ring3[0], [o2.get_x(), o2.get_y() - 0.2, 0]).shift(RIGHT*0.07 + UP*-0.06)
        o2_line2 = Line(outer_ring3[0], [o2.get_x(), o2.get_y() - 0.2, 0]).shift(RIGHT*-0.07 + UP*-0.06)

        symbols = VGroup(n1,n2,n3,h1,h2,nh,h3c1,h3c1_line,h3c2,h3c2_line,r,r_line,o,o_line1,o_line2,o2,o2_line1,o2_line2)

        all = VGroup(symbols)
        self.add(ring1,ring2,ring3,all)


class Komplex1Reaktion(Scene):
    def construct(self):

        nadText = Text("NAD").shift(UP)
        nadFullText = Text("Nicotinamidadenindinukleotid").shift(-UP)
        nadFullTextCopy = Text("NAD").shift(UP)
        nadFullText[0].set_color(YELLOW)
        nadFullText[11].set_color(YELLOW)
        nadFullText[17].set_color(YELLOW)

        self.wait()
        self.play(Write(nadFullTextCopy), Write(nadText))
        self.wait()
        self.play(nadText[0].animate.set_color(YELLOW))
        self.play(ReplacementTransform(nadText[0], nadFullText[:11]))
        self.play(nadText[1].animate.set_color(YELLOW))
        self.play(ReplacementTransform(nadText[1], nadFullText[11:17]))
        self.play(nadText[2].animate.set_color(YELLOW))
        self.play(ReplacementTransform(nadText[2], nadFullText[17:]))
        self.wait(3)
        self.play(Unwrite(nadText), Unwrite(nadFullText), Unwrite(nadFullTextCopy))
        self.remove(nadFullTextCopy)
        self.wait()


        reaction = MathTex(r"NAD^{+}+2H+2e^{-}",r"\rightleftharpoons",r"NADH+H^{+}")     

        nadh = NADH()
        nadp = NADplus()
        nadp2 = NADplus().shift(LEFT*5.5)

        reaction_equal = MathTex(r"\rightleftharpoons").shift(RIGHT*0.8)
        reaction_2h = MathTex(r"+2H").shift(LEFT*2)
        reaction_2e = MathTex(r"+2e^{-}").shift(LEFT*0.3)
        reaction_hp = MathTex(r"H^{+}+").shift(RIGHT*1.9)

        efirst = MathTex(r"e^{-}").shift(LEFT*2 +UP)
        newN = MathTex("N").shift(UP)
        hfirst = MathTex(r"H").shift(LEFT*1 -2*UP)
        esecond = MathTex(r"e^{-}").shift(LEFT*1 - UP)

        self.wait()
        self.play(Write(reaction[0]), run_time=3)
        self.play(Write(reaction[1]))
        self.play(Write(reaction[2]), run_time=2)
        self.wait()
        self.play(reaction.animate.shift(UP*3))
        self.wait(2)
        self.play(Write(nadp), run_time=4)
        self.wait(2)
        self.play(Write(efirst))
        self.play(Circumscribe(efirst))
        self.play(Indicate(efirst))
        self.play(Circumscribe(nadp.npos))
        self.play(Indicate(nadp.npos))
        self.wait()
        self.play(efirst.animate.shift(RIGHT*2).set_opacity(0), Transform(nadp.npos, newN), run_time = 2)
        self.wait()
        self.play(Write(esecond))
        self.play(Write(hfirst))
        self.play(Circumscribe(esecond))
        self.play(Indicate(esecond))
        self.play(Circumscribe(hfirst))
        self.play(Indicate(hfirst))
        self.wait()
        self.play(esecond.animate.shift(RIGHT).set_opacity(0), hfirst.animate.shift(RIGHT).set_opacity(0), TransformMatchingShapes(nadp, nadh), newN.animate.set_opacity(0), run_time = 2)
        self.wait()
        self.play(nadh.animate.shift(RIGHT*3.8))
        self.wait()
        self.play(FadeIn(nadp2))
        self.wait()
        self.play(FadeIn(reaction_2h))
        self.play(FadeIn(reaction_2e))
        self.play(FadeIn(reaction_equal))
        self.wait()
        self.play(FadeIn(reaction_hp))
        self.wait(5)
        self.play(FadeOut(nadp2),FadeOut(reaction_2h),FadeOut(reaction_2e),FadeOut(reaction_equal),FadeOut(reaction_hp),FadeOut(reaction),FadeOut(nadh), run_time = 2)
        self.wait()





class Komplex2Reaktion(Scene):
    def construct(self):


        fadText = Text("FAD").shift(UP)
        fadFullText = Text("Flavinadenindinukleotid").shift(-UP)
        fadFullTextCopy = Text("FAD").shift(UP)
        fadFullText[0].set_color(YELLOW)
        fadFullText[6].set_color(YELLOW)
        fadFullText[12].set_color(YELLOW)

        self.wait()
        self.play(Write(fadFullTextCopy), Write(fadText))
        self.wait()
        self.play(fadText[0].animate.set_color(YELLOW))
        self.play(ReplacementTransform(fadText[0], fadFullText[:6]))
        self.play(fadText[1].animate.set_color(YELLOW))
        self.play(ReplacementTransform(fadText[1], fadFullText[6:12]))
        self.play(fadText[2].animate.set_color(YELLOW))
        self.play(ReplacementTransform(fadText[2], fadFullText[12:]))
        self.wait(3)
        self.play(Unwrite(fadText), Unwrite(fadFullText), Unwrite(fadFullTextCopy))
        self.remove(fadFullTextCopy)
        self.wait()


        reaction = MathTex(r"FAD+2H+2e^{-}",r"\rightleftharpoons",r"FADH_{2}")     

        fad = FAD().shift(DOWN*0.5)
        fad2 = FAD().scale(0.5).shift(LEFT*4.5)
        fadh2 = FADH2()

        reaction_equal = MathTex(r"\rightleftharpoons").shift(RIGHT*1.1)
        reaction_2h = MathTex(r"+2H").shift(LEFT*1.7)
        reaction_2e = MathTex(r"+2e^{-}").shift(LEFT*0)

        efirst = MathTex(r"e^{-}").shift(LEFT*0.8 +UP*1.5)
        hfirst = MathTex(r"H").shift(LEFT*-0.8 + 1.5*UP)
        esecond = MathTex(r"e^{-}").shift(RIGHT*1.3 + DOWN *2.4)
        hsecond = MathTex(r"H").shift(RIGHT*2.2 + DOWN *2.4)

        self.wait()
        self.play(Write(reaction[0]), run_time = 3)
        self.play(Write(reaction[1]), run_time = 1)
        self.play(Write(reaction[2]), run_time = 2)
        self.wait()
        self.play(reaction.animate.shift(UP*3))
        self.wait(2)
        self.play(Write(fad), run_time = 6)
        self.wait()
        self.play(Write(efirst))
        self.play(Write(hfirst))
        self.wait()
        self.play(Circumscribe(efirst))
        self.play(Indicate(efirst))
        self.wait()
        self.play(Circumscribe(hfirst))
        self.play(Indicate(hfirst))
        self.wait()
        self.play(efirst.animate.shift(RIGHT*0.8 + DOWN).set_opacity(0), hfirst.animate.shift(RIGHT*-0.8 + DOWN*0.5), run_time = 2)
        self.wait()
        self.play(Write(esecond))
        self.play(Write(hsecond))
        self.wait()
        self.play(Circumscribe(esecond))
        self.play(Indicate(esecond))
        self.wait()
        self.play(Circumscribe(hsecond))
        self.play(Indicate(hsecond))
        self.wait()
        self.play(esecond.animate.shift(RIGHT*0.6 + UP*1).set_opacity(0), hsecond.animate.shift(RIGHT*-0.5 + DOWN*-0.4), run_time = 2)
        self.wait()
        self.play(FadeOut(hfirst), FadeOut(hsecond), TransformMatchingShapes(fad, fadh2))
        self.play(fadh2.animate.scale(0.5).shift(RIGHT*4.5), run_time=2)
        self.wait()
        self.play(Create(fad2), run_time=2)
        self.wait()
        self.play(FadeIn(reaction_2h))
        self.play(FadeIn(reaction_2e))
        self.play(FadeIn(reaction_equal))
        self.wait(5)
        self.play(FadeOut(fad2),FadeOut(fadh2),FadeOut(reaction),FadeOut(reaction_2e),FadeOut(reaction_2h),FadeOut(reaction_equal), run_time = 2)
        self.wait()