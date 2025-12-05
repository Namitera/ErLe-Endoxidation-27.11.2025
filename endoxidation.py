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

class Electron(VGroup):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)

        body = Circle(fill_color = PURE_GREEN, fill_opacity = 1, color=PURE_GREEN)
        minus = Rectangle(fill_color = BLACK, fill_opacity = 1, color=BLACK, width=1, height=0.1)

        allObj = VGroup(body, minus)
        self.add(allObj)

        self.body = body
        self.minus = minus
        
        
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


class Thumbnail(Scene):
    def construct(self):

        self.play(Write(Text("Endoxidation").scale(3)))


class Komplex1Reaktion(Scene):
    def construct(self):

        nadText = Text("NAD").shift(UP)
        nadFullText = Text("Nicotinamidadenindinukleotid").shift(-UP)
        nadFullTextCopy = Text("NAD").shift(UP)
        nadFullText[0].set_color(YELLOW)
        nadFullText[11].set_color(YELLOW)
        nadFullText[17].set_color(YELLOW)

        self.add_sound("Sounds/Komplex1Reaktion.m4a", time_offset=1, gain=3)
        self.add_sound("Sounds/K1R.wav", time_offset=0)

        self.wait()
        self.play(Write(nadFullTextCopy), Write(nadText))
        self.wait()
        self.play(nadText[0].animate.set_color(YELLOW))
        self.play(ReplacementTransform(nadText[0], nadFullText[:11]))
        self.play(nadText[1].animate.set_color(YELLOW))
        self.play(ReplacementTransform(nadText[1], nadFullText[11:17]))
        self.play(nadText[2].animate.set_color(YELLOW))
        self.play(ReplacementTransform(nadText[2], nadFullText[17:]))
        self.wait(0.5)
        self.play(Unwrite(nadText), Unwrite(nadFullText), Unwrite(nadFullTextCopy), run_time=1)
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
        self.play(Write(reaction[0]), run_time=5)
        self.play(Write(reaction[1]))
        self.play(Write(reaction[2]), run_time=2)
        self.wait()
        self.play(reaction.animate.shift(UP*3))
        self.wait(2)
        self.play(Write(nadp), run_time=4)
        self.wait(4)
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
        self.wait(4)
        self.play(FadeOut(nadp2),FadeOut(reaction_2h),FadeOut(reaction_2e),FadeOut(reaction_equal),FadeOut(reaction_hp),FadeOut(reaction),FadeOut(nadh), run_time = 2)
        self.wait()





class Einordnung(Scene):
    def construct(self):

        self.wait()
        self.add_sound("Sounds/Einordnung.m4a", time_offset=1)
        self.add_sound("Sounds/Einordnung.wav", time_offset=0)

        
        naerstoffe = Text("Nährstoffe").shift(UP*3).set_color(YELLOW)
        atp = MathTex("ATP").scale(1.2)
        arrow = Arrow(UP*2.5, UP*0.5)

        citratzyklus = Text("Citratzyklus").shift(UP*3 +LEFT*4.5).set_color(YELLOW)
        fadh2 = MathTex("FADH_{2}").shift(UP*-2 + LEFT*4.5)
        nadh = MathTex("NADH + H^{+}").shift(UP*0 + LEFT*4.5)
        arrow2 = Arrow(UP*2.5 + LEFT*4.5, UP*0.5 + LEFT*4.5)

        glykolyse = Text("Glykolyse").shift(UP*3 + RIGHT*4.5).set_color(YELLOW)
        glucose = Tex("Glucose").shift(UP*-0.2 + RIGHT*4.5)
        arrow3 = Arrow(UP*2.5 + RIGHT*4.5, UP*0.5 + RIGHT*4.5)

        endoxidation = Text("Endoxidation").shift(UP*1).set_color(YELLOW)
        atp2 = MathTex("ATP").shift(UP*-2)
        arrow4 = Arrow(UP*0.5, UP*-1.5)

        self.wait(2)
        self.play(Write(naerstoffe))
        self.wait()
        self.play(GrowArrow(arrow))
        self.wait()
        self.play(Write(atp))
        self.wait(2)
        self.play(FadeOut(naerstoffe), FadeOut(arrow), FadeOut(atp))
        self.wait()
        self.play(Write(glykolyse), run_time=0.5)
        self.play(GrowArrow(arrow3), run_time=0.5)
        self.play(Write(glucose), run_time=0.5)
        self.wait(1)
        self.play(Write(citratzyklus))
        self.play(GrowArrow(arrow2), run_time=0.5)
        self.play(Write(nadh))
        self.wait(0.6)
        self.play(Write(fadh2))
        self.wait(1.5)
        self.play(Write(endoxidation))
        self.wait()
        self.play(GrowArrow(arrow4))
        self.wait(0.8)
        self.play(Write(atp2))
        self.wait(0.3)
        self.play(FadeOut(glykolyse), FadeOut(arrow3), FadeOut(glucose), FadeOut(citratzyklus), FadeOut(arrow2), FadeOut(fadh2), FadeOut(nadh), FadeOut(endoxidation), FadeOut(arrow4), FadeOut(atp2), run_time=2)

        glucoseText = Text("Glucose").shift(UP*3).set_color(YELLOW)
        pyruvatText1 = Text("Pyruvat").shift(UP*1.5 +LEFT*4)
        pyruvatText2 = Text("Pyruvat").shift(UP*1.5 +RIGHT*4)
        nadhText1 = MathTex("NADH + H^{+}").shift(LEFT*2)
        nadhText2 = MathTex("NADH + H^{+}").shift(RIGHT*2)
        atpText = MathTex("2 ATP").shift(UP*-1.5)
        oxidativeDecarboxylierung = Text("oxidative Decarboxylierung").shift(UP*2.5 + RIGHT*2.7)
        arrow5 = Arrow(UP*1.5 + RIGHT*3, UP*1.5 + LEFT*2.3)
        nadhText3 = MathTex("NADH + H^{+}").shift(DOWN*0 + RIGHT*0)
        nadhText4 = MathTex("NADH + H^{+}").shift(DOWN*1.5 + RIGHT*-2)

        self.wait()
        self.play(Write(glucoseText))
        self.wait(1.5)
        self.play(ReplacementTransform(glucoseText.copy(),nadhText1), ReplacementTransform(glucoseText.copy(), nadhText2), run_time=1.5)
        self.wait()
        self.play(ReplacementTransform(glucoseText.copy(),atpText))
        self.wait(0.5)
        self.play(ReplacementTransform(glucoseText.copy(),pyruvatText1), ReplacementTransform(glucoseText.copy(),pyruvatText2))
        self.wait()

        # self.play(Unwrite(glucoseText), Unwrite(pyruvatText2), Unwrite(nadhText2), Unwrite(nadhText1), Unwrite(atpText))
        self.play(Transform(VGroup(glucoseText,pyruvatText2,nadhText2,nadhText1,atpText), oxidativeDecarboxylierung.copy().set_opacity(0)), Write(oxidativeDecarboxylierung), run_time=3)

        self.play(GrowArrow(arrow5), pyruvatText1.animate.set_color(YELLOW))
        self.wait(0.5)
        placeholder1 = pyruvatText1.copy()
        placeholder2 = pyruvatText1.copy()
        self.play(ClockwiseTransform(placeholder1,nadhText3),CounterclockwiseTransform(placeholder2,nadhText4), run_time=1.5)
        self.play(AnimationGroup(Unwrite(oxidativeDecarboxylierung), Unwrite(arrow5), Unwrite(nadhText3), Unwrite(nadhText4), Unwrite(pyruvatText1), Unwrite(placeholder1), Unwrite(placeholder2), lag_ratio=0.1), run_time=2)

        citratzyklusText = Text("Citratzyklus").shift(UP*3).set_color(YELLOW)
        nadhText5 = MathTex("6 NADH + H^{+}").shift(LEFT*3)
        fadh2Text = MathTex("2 FADH_{2}").shift(RIGHT*3)
        atpText2 = MathTex("2 ATP").shift(UP*-1.5)

        self.play(Write(citratzyklusText))
        self.wait(0.5)
        self.play(Write(nadhText5), run_time=2)
        self.play(Circumscribe(nadhText5))
        self.play(Indicate(nadhText5))
        self.play(Write(fadh2Text), run_time=1)
        self.wait(0.5)
        self.play(Write(atpText2))
        self.play(Wiggle(atpText2))
        self.play(FadeOut(citratzyklusText), FadeOut(nadhText5), FadeOut(fadh2Text), FadeOut(atpText2), run_time=1)


        endoxidationText = Text("Endoxidation").shift(UP*3).set_color(YELLOW)
        nadhText6 = MathTex("10 NADH + H^{+}").shift(LEFT*3)
        nadhText6new = MathTex(r"10\cdot(NADH + H^{+})").shift(LEFT*3)
        fadh2Text2 = MathTex("2 FADH_{2}").shift(RIGHT*3)
        atpText3 = MathTex("4 ATP").shift(UP*-1.5)
        atpText4 = MathTex("ATP").shift(LEFT*3+ DOWN).set_color(YELLOW)
        atpText5 = MathTex("ATP").shift(LEFT*-3 +DOWN).set_color(YELLOW)
        self.play(Write(endoxidationText))
        self.wait(0.5)
        self.play(Write(nadhText6), run_time=2)
        self.wait(1)
        self.play(Write(fadh2Text2), run_time=1)
        self.wait(1)
        self.play(TransformMatchingShapes(nadhText6, nadhText6new), run_time=1)
        self.wait(1)
        self.play(Write(atpText3))
        self.play(atpText3.animate.shift(UP*3.5))
        self.wait()
        self.play(Write(atpText4), Write(atpText5))
        self.play(VGroup(atpText4,nadhText6new).animate.shift(LEFT*7+DOWN*4))
        self.play(VGroup(atpText5,fadh2Text2).animate.shift(RIGHT*6+DOWN*4))
        self.wait(2)
        self.play(FadeOut(endoxidationText), FadeOut(atpText3), FadeOut(atpText4), FadeOut(atpText5), run_time=2)
        self.wait()





class Komplex1Explanation(Scene):
    def construct(self):

        protonPump = ImageMobject("Sprites/ProtonPumpSprite.png").shift(UP*2).scale(2)

        nadhText = MathTex("NADH").shift(UP*-2.7 + 3*LEFT).set_z_index(1)
        nadh = NADH().scale(0.4).shift(UP*-2.7 + 5.6*LEFT).set_z_index(1)
        nadplusText = MathTex("NAD^{+}")
        nadplus = NADplus().scale(0.4)

        hText = MathTex("H^{+}").shift(UP*-2 + 2*RIGHT).set_z_index(1)

        h1 = MathTex("H^{+}").shift(RIGHT*5 + DOWN*0)
        h2 = MathTex("H^{+}").shift(RIGHT*4 + DOWN*1)
        h3 = MathTex("H^{+}").shift(RIGHT*3 + DOWN*0)
        h4 = MathTex("H^{+}").shift(RIGHT*2 + DOWN*1)
        empty1 = Text("0").shift(RIGHT*1.4 + UP*9).set_opacity(0)
        empty2 = Text("0").shift(RIGHT*1.4 + UP*9.01).set_opacity(0)
        empty3 = Text("0").shift(RIGHT*1.4 + UP*9.02).set_opacity(0)
        empty4 = Text("0").shift(RIGHT*1.4 + UP*9.03).set_opacity(0)
        allH = VGroup(h1, h2, h3, h4, empty1, empty2, empty3, empty4).shift(UP*-1 +RIGHT)

        qText = MathTex("Q").shift(UP*2 + LEFT*8).set_z_index(1)
        qh2Text = MathTex(r"QH_{2}").shift(UP*2 + LEFT*8).set_z_index(1)
        e1 = Electron().scale(0.1).set_opacity(0).set_z_index(1)
        e2 = Electron().scale(0.1).set_opacity(0).set_z_index(1)

        membrane1 = ImageMobject("SpritesOld/MembraneSprite.png").set_opacity(0.4).shift(UP*2 +LEFT*4)
        membrane2 = ImageMobject("SpritesOld/MembraneSprite.png").set_opacity(0.8).shift(UP*2 +LEFT*-4)
        membrane3 = ImageMobject("SpritesOld/MembraneSprite.png").set_opacity(0.4).shift(UP*2 +LEFT*-0)
        complex1 = Group(membrane1, membrane2, membrane3, protonPump)

        blackBox1 = SurroundingRectangle(nadhText, corner_radius=0.3, color=BLACK, fill_opacity=0.5, stroke_opacity=0).move_to(nadhText)
        blackBox2 = SurroundingRectangle(qText, corner_radius=0.3, color=BLACK, fill_opacity=0.5, stroke_opacity=0).move_to(qText)

        self.add_sound("Sounds/Komplex1Explanation.m4a", time_offset=1, gain=1.3)
        self.add_sound("Sounds/K1E.wav", time_offset=0)


        self.wait()
        self.play(Write(nadhText), Write(nadh), Write(hText))
        self.wait()
        self.play(FadeIn(complex1))
        self.wait()
        self.play(nadhText.animate.shift(2.7*UP), blackBox1.animate.shift(2.7*UP), nadh.animate.shift(2.7*UP), hText.animate.shift(LEFT*3 +2*UP), run_time=2)
        self.play(qText.animate.shift(RIGHT*5.7), blackBox2.animate.shift(RIGHT*5.7), run_time = 3)

        self.wait(3)
        nadplusText.move_to(nadhText)
        nadplus.move_to(nadh)
        self.play(Transform(nadh, nadplus), Transform(nadhText, nadplusText), run_time=2) 
        self.play(Circumscribe(hText))
        self.wait()
        self.play(hText.animate.shift(LEFT+UP).set_opacity(0), run_time = 2.5)

        self.wait(2)
        e1.move_to([-3,0.5,0])
        e2.move_to([-3,0.5,0])
        qh2Text.move_to(qText)
        blackBox3 = SurroundingRectangle(qh2Text, corner_radius=0.3, color=BLACK, fill_opacity=0.5, stroke_opacity=0).move_to(qh2Text)

        self.play(TransformMatchingShapes(qText,qh2Text), ReplacementTransform(blackBox2,blackBox3))
        self.wait()
        self.play(e1.animate.set_opacity(1).shift(UP*2 + LEFT*-0.5), e2.animate.set_opacity(1).shift(UP*2 + LEFT*-0.9),run_time=4)
        self.wait()
        self.play(VGroup(qh2Text,e1,e2,blackBox3).animate.shift(LEFT*7), run_time=2)
        self.wait(2)
        self.play(VGroup(nadhText,nadh,blackBox1).animate.shift(DOWN*4 + RIGHT*2).set_opacity(0), run_time=3)
        self.wait()

        ## pump h+
        self.play(Write(allH))
        self.wait()
        self.play(allH.animate.shift(UP*1 -RIGHT))
        self.wait(2)
        self.play(CyclicReplace(*allH, path_arc=-1.4), run_time=3)
        self.play(CyclicReplace(*allH, path_arc=-1.4), run_time=2.5)
        self.play(CyclicReplace(*allH, path_arc=-1.4), run_time=2)
        self.play(CyclicReplace(*allH, path_arc=-1.4), run_time=2)
        self.play(FadeOut(complex1))
        self.wait()





class Komplex2Reaktion(Scene):
    def construct(self):


        fadText = Text("FAD").shift(UP)
        fadFullText = Text("Flavinadenindinukleotid").shift(-UP)
        fadFullTextCopy = Text("FAD").shift(UP)
        fadFullText[0].set_color(YELLOW)
        fadFullText[6].set_color(YELLOW)
        fadFullText[12].set_color(YELLOW)

        self.add_sound("Sounds/Komplex2Reaktion.m4a", time_offset=1, gain=1.0)
        self.add_sound("Sounds/K1E.wav", time_offset=0, gain=1.5)

        self.wait()
        self.play(Write(fadFullTextCopy), Write(fadText))
        self.wait()
        self.play(fadText[0].animate.set_color(YELLOW))
        self.play(ReplacementTransform(fadText[0], fadFullText[:6]))
        self.play(fadText[1].animate.set_color(YELLOW))
        self.play(ReplacementTransform(fadText[1], fadFullText[6:12]))
        self.play(fadText[2].animate.set_color(YELLOW))
        self.play(ReplacementTransform(fadText[2], fadFullText[12:]))
        self.wait(0.5)
        self.play(Unwrite(fadText), Unwrite(fadFullText), Unwrite(fadFullTextCopy), run_time=1)
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
        self.play(Write(reaction[0]), run_time = 4.5)
        self.play(Write(reaction[1]), run_time = 1)
        self.play(Write(reaction[2]), run_time = 2)
        self.wait()
        self.play(reaction.animate.shift(UP*3))
        self.wait(2)
        self.play(Write(fad), run_time = 3)
        self.wait()
        self.play(Write(efirst))
        self.play(Indicate(efirst), run_time=1)
        self.play(Write(hfirst))
        self.play(Indicate(hfirst), run_time=1)
        self.wait()
        self.play(efirst.animate.shift(RIGHT*0.8 + DOWN).set_opacity(0), hfirst.animate.shift(RIGHT*-0.8 + DOWN*0.5), run_time = 1.5)
        self.wait()
        self.play(Write(esecond))
        self.play(Write(hsecond))
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





class Komplex2Explanation(Scene):
    def construct(self):

        dehydronator = ImageMobject("Sprites/DehydronatorSprite.png").shift(UP*0).scale(1.6)

        fadh2Text = MathTex("FADH_{2}").shift(UP*-2 + 2*LEFT).set_z_index(1)
        fadh2 = FADH2().scale(0.4).shift(4.3*LEFT +1.9*DOWN).set_z_index(1)
        fadText = MathTex("FAD").set_z_index(1)
        fad = FAD().scale(0.4).set_z_index(1)

        qText = MathTex("Q").shift(UP*1 + LEFT*8).set_z_index(1)
        qh2Text = MathTex(r"QH_{2}").shift(UP*1 + LEFT*8).set_z_index(1)
        e1 = Electron().scale(0.1).set_opacity(0).set_z_index(1)
        e2 = Electron().scale(0.1).set_opacity(0).set_z_index(1)

        membrane1 = ImageMobject("SpritesOld/MembraneSprite.png").set_opacity(0.4).shift(UP*1 +LEFT*3)
        membrane2 = ImageMobject("SpritesOld/MembraneSprite.png").set_opacity(0.8).shift(UP*1 +LEFT*-2.8)
        membrane3 = ImageMobject("SpritesOld/MembraneSprite.png").set_opacity(0.8).shift(UP*1 +LEFT*-8.6)
        membrane4 = ImageMobject("SpritesOld/MembraneSprite.png").set_opacity(0.4).shift(UP*1 +LEFT*8.8)
        complex2 = Group(membrane1, membrane2, membrane3, membrane4, dehydronator)

        blackBox1 = SurroundingRectangle(fadh2Text, corner_radius=0.3, color=BLACK, fill_opacity=0.5, stroke_opacity=0).move_to(fadh2Text)
        blackBox2 = SurroundingRectangle(qText, corner_radius=0.3, color=BLACK, fill_opacity=0.5, stroke_opacity=0).move_to(qText)


        self.add_sound("Sounds/Komplex2Explanation.m4a", time_offset=1, gain=1)
        self.add_sound("Sounds/K2E.wav", time_offset=0, gain=1.5)


        self.wait()
        self.play(Write(fadh2Text), Write(fadh2))
        self.wait()
        self.play(FadeIn(complex2))
        self.wait()
        self.play(VGroup(fadh2Text,fadh2,blackBox1).animate.shift(1.3*UP + 2*RIGHT), run_time=2)
        self.play(VGroup(qText,blackBox2).animate.shift(RIGHT*7.7), run_time = 3)

        self.wait()
        fadText.move_to(fadh2Text)
        fad.move_to(fadh2)
        self.play(Transform(fadh2, fad), Transform(fadh2Text, fadText), run_time = 2.5)

        self.wait(2)
        qh2Text.move_to(qText)
        blackBox3 = SurroundingRectangle(qh2Text, corner_radius=0.3, color=BLACK, fill_opacity=0.5, stroke_opacity=0).move_to(qh2Text)
        self.play(TransformMatchingShapes(qText,qh2Text), ReplacementTransform(blackBox2,blackBox3), run_time=2)

        e1.move_to([0,-0.5,0])
        e2.move_to([0,-0.5,0])
        self.play(e1.animate.set_opacity(1).shift(UP*1.9 + LEFT*0.5), e2.animate.set_opacity(1).shift(UP*1.9 + LEFT*0.1),run_time=5)
        self.wait()

        self.play(VGroup(qh2Text,e1,e2,blackBox3).animate.shift(LEFT*8), run_time=3)
        self.wait()
        self.play(VGroup(fadh2,fadh2Text,blackBox1).animate.shift(DOWN*4 + RIGHT*2).set_opacity(0), run_time=3)
        self.wait()


        t = ValueTracker(0)
        a = ValueTracker(0.3)
        h1 = MathTex(r"H^{+}")
        h2 = MathTex(r"H^{+}")
        h3 = MathTex(r"H^{+}")
        h4 = MathTex(r"H^{+}")
        h5 = MathTex(r"H^{+}")
        h6 = MathTex(r"H^{+}")
        h1Origin = [3, -1, 0]
        h2Origin = [1, -2.5, 0]
        h3Origin = [5.5, -2.5, 0]
        h4Origin = [-3, -2.5, 0]
        h5Origin = [-1, -1, 0]
        h6Origin = [-5.5, -1, 0]

        vector1 = Circle([0,0,0])
        vector2 = Circle([0,0,0])
        vector3 = Circle([0,0,0])
        vector4 = Circle([0,0,0])
        vector5 = Circle([0,0,0])
        vector6 = Circle([0,0,0])
        vector7 = Circle([0,0,0])
        vector8 = Circle([0,0,0])
        vector9 = Circle([0,0,0])
        vector10 = Circle([0,0,0])
        vector11 = Circle([0,0,0])
        vector12 = Circle([0,0,0])

        vector1.add_updater(lambda mob: mob.become(
            Circle(radius=30).move_to([a.get_value()*np.cos(7*PI*t.get_value()-2.094), a.get_value()*np.sin(6*PI*t.get_value()-2.094), 0])))
        vector2.add_updater(lambda mob: mob.become(
            Circle(radius=30).move_to([a.get_value()*np.cos(-4*PI*t.get_value()-2.094), a.get_value()*np.sin(-4*PI*t.get_value()-2.094), 0])))
        vector3.add_updater(lambda mob: mob.become(
            Circle(radius=30).move_to([a.get_value()*np.cos(6*PI*t.get_value()- 1.047), a.get_value()*np.sin(6*PI*t.get_value()- 1.047), 0])))
        vector4.add_updater(lambda mob: mob.become(
            Circle(radius=30).move_to([a.get_value()*np.cos(-4*PI*t.get_value()- 1.047), a.get_value()*np.sin(-4*PI*t.get_value()- 1.047), 0])))
        vector5.add_updater(lambda mob: mob.become(
            Circle(radius=30).move_to([a.get_value()*np.cos(3*PI*t.get_value()), a.get_value()*np.sin(6*PI*t.get_value()), 0])))
        vector6.add_updater(lambda mob: mob.become(
            Circle(radius=30).move_to([a.get_value()*np.cos(-4*PI*t.get_value()), a.get_value()*np.sin(-4*PI*t.get_value()), 0])))
        vector7.add_updater(lambda mob: mob.become(
            Circle(radius=30).move_to([a.get_value()*np.cos(6*PI*t.get_value()-5.235), a.get_value()*np.sin(6*PI*t.get_value()-5.235), 0])))
        vector8.add_updater(lambda mob: mob.become(
            Circle(radius=30).move_to([a.get_value()*np.cos(-8*PI*t.get_value()-5.235), a.get_value()*np.sin(-4*PI*t.get_value()-5.235), 0])))
        vector9.add_updater(lambda mob: mob.become(
            Circle(radius=30).move_to([a.get_value()*np.cos(6*PI*t.get_value()-4.188), a.get_value()*np.sin(6*PI*t.get_value()-4.188), 0])))
        vector10.add_updater(lambda mob: mob.become(
            Circle(radius=30).move_to([a.get_value()*np.cos(-2*PI*t.get_value()-4.188), a.get_value()*np.sin(-4*PI*t.get_value()-4.188), 0])))
        vector11.add_updater(lambda mob: mob.become(
            Circle(radius=30).move_to([a.get_value()*np.cos(6*PI*t.get_value()-3.141), a.get_value()*np.sin(6*PI*t.get_value()-3.141), 0])))
        vector12.add_updater(lambda mob: mob.become(
            Circle(radius=30).move_to([a.get_value()*np.cos(-5*PI*t.get_value()-3.141), a.get_value()*np.sin(-4*PI*t.get_value()-3.141), 0])))

        h1.add_updater(lambda mob: mob.move_to(vector1.get_center() + vector2.get_center() + h1Origin))
        h2.add_updater(lambda mob: mob.move_to(vector3.get_center() + vector4.get_center() + h2Origin))
        h3.add_updater(lambda mob: mob.move_to(vector5.get_center() + vector6.get_center() + h3Origin))
        h4.add_updater(lambda mob: mob.move_to(vector7.get_center() + vector8.get_center() + h4Origin))
        h5.add_updater(lambda mob: mob.move_to(vector9.get_center() + vector10.get_center() + h5Origin))
        h6.add_updater(lambda mob: mob.move_to(vector11.get_center() + vector12.get_center() + h6Origin))

        allH = VGroup(h1,h2,h3,h4,h5,h6)
        allVectors = VGroup(vector1,vector2,vector3,vector4,vector5,vector6,vector7,vector8,vector9,vector10,vector11,vector12)
        self.add(allH, allVectors)

        self.play(FadeIn(allH), t.animate.set_value(1), rate_func=linear, run_time = 2)
        self.play(t.animate.set_value(6), rate_func=linear, run_time = 10)
        self.play(FadeOut(allH), t.animate.set_value(7), rate_func=linear, run_time = 2)
        self.play(FadeOut(complex2), run_time=2)
        self.wait()





class Komplex3Explanation(Scene):
    def construct(self):

        h1 = MathTex("H^{+}").shift(RIGHT*-0.5 + UP*0.5)
        h2 = MathTex("H^{+}").shift(RIGHT*-0.5 + UP*1.5)
        h3 = MathTex("H^{+}").shift(RIGHT*-0.5 + UP*0.5)
        h4 = MathTex("H^{+}").shift(RIGHT*-0.5 + UP*1.5)
        h5 = MathTex("H^{+}").shift(RIGHT*-1 + DOWN*3.2)
        h6 = MathTex("H^{+}").shift(RIGHT*1 + DOWN*3.2)
        h7 = MathTex("H")
        h8 = MathTex("H")

        qText1 = MathTex("Q")
        qText2 = MathTex("Q").shift(DOWN*0.5 + LEFT*8)
        qText3 = MathTex("Q").shift(UP*2 + LEFT*8)
        qh2Text1 = MathTex(r"QH_{2}").shift(UP*0.5 + LEFT*8)
        qh2Text2 = MathTex(r"QH_{2}").shift(UP*0.5 + LEFT*8)
        qh2Text3 = MathTex(r"QH_{2}")
        e1 = Electron().scale(0.1).set_opacity(1)
        e2 = Electron().scale(0.1).set_opacity(1)
        e3 = Electron().scale(0.1).set_opacity(1)
        e4 = Electron().scale(0.1).set_opacity(1)

        cytc1Text = MathTex("CytC").shift(UP*0.5 + RIGHT*8)
        cytc2Text = MathTex("CytC").shift(UP*0.5 + RIGHT*8)

        qCycleHub = ImageMobject("Sprites/QCycleHubSprite.png").shift(UP*0).scale(2.7)
        membrane1 = ImageMobject("SpritesOld/MembraneSprite.png").set_opacity(0.3).shift(UP*0 +LEFT*8.4).scale(2.5)
        membrane2 = ImageMobject("SpritesOld/MembraneSprite.png").set_opacity(0.3).shift(UP*0 +LEFT*-8.4).scale(2.5)
        complex3 = Group(membrane1, membrane2, qCycleHub)

        self.add_sound("Sounds/Komplex3.m4a", time_offset=1)
        self.add_sound("Sounds/K3S2.wav", time_offset=0, gain=1)


        self.wait()
        self.play(FadeIn(complex3))
        self.wait(2)
        self.play(qh2Text1.animate.shift(RIGHT*6), run_time=3)
        self.wait(4)
        self.play(cytc1Text.animate.shift(RIGHT*-6), run_time=4)
        self.play(qCycleHub.animate.set_opacity(0.3).set_z_index(-1))
        e1.next_to(qh2Text1, UP).shift(LEFT*0.2)
        e2.next_to(qh2Text1, UP).shift(LEFT*-0.2)
        qText1.move_to(qh2Text1)
        self.wait(4)
        self.play(ReplacementTransform(qh2Text1, VGroup(qText1,e1,e2,h1,h2)), run_time=2)
        self.wait(5)
        self.play(e1.animate.next_to(cytc1Text, UP), run_time=2)
        self.wait()
        self.play(cytc1Text.animate.shift(RIGHT*6), e1.animate.shift(RIGHT*6), run_time=2)
        self.wait(3)
        self.play(AnimationGroup(h1.animate.shift(UP*5 + RIGHT*2), h2.animate.shift(UP*5 + LEFT), lag_ratio=0.2), run_time=3)
        self.wait()
        self.play(qText2.animate.shift(RIGHT*8), run_time=3)
        self.wait()
        self.play(e2.animate.next_to(qText2, UP), run_time=3)
        self.wait()
        self.play(qText1.animate.shift(LEFT*6), run_time=5)
        self.wait(2)

        self.play(qh2Text2.animate.shift(RIGHT*6), run_time=2)
        self.play(cytc2Text.animate.shift(RIGHT*-6), run_time=2)
        e3.next_to(qh2Text2, UP).shift(LEFT*0.2)
        e4.next_to(qh2Text2, UP).shift(LEFT*-0.2)
        qText3.move_to(qh2Text2)
        self.play(ReplacementTransform(qh2Text2, VGroup(qText3,e3,e4,h3,h4)), run_time=2)
        self.wait(2)
        self.play(e3.animate.next_to(cytc2Text, UP), run_time=2)
        self.wait()
        self.play(cytc2Text.animate.shift(RIGHT*6), e3.animate.shift(RIGHT*6), run_time=2)
        self.wait()
        self.play(AnimationGroup(h3.animate.shift(UP*5 + RIGHT*2), h4.animate.shift(UP*5 + LEFT), lag_ratio=0.2), run_time=3)
        self.wait()
        self.play(e4.animate.next_to(qText2, UP).shift(RIGHT*0.3), run_time=2)
        self.wait()
        self.play(qText3.animate.shift(LEFT*6), run_time=3)
        self.wait()

        self.play(Write(h5))
        self.play(h5.animate.shift(UP*1.8 + 0.6*RIGHT))
        self.play(Write(h6))
        self.play(h6.animate.shift(UP*1.8 + 0.4*LEFT))
        h7.move_to(h5)
        h8.move_to(h6)
        self.wait()
        self.play(e2.animate.move_to(h5).set_opacity(0), ReplacementTransform(h5, h7), run_time=1.5)
        self.wait()
        self.play(e4.animate.move_to(h6).set_opacity(0), ReplacementTransform(h6, h8), run_time=1.5)
        qh2Text3.move_to(qText2)
        self.play(ReplacementTransform(VGroup(qText2,h7,h8), qh2Text3), run_time=2.5)
        self.wait(2)
        self.play(qh2Text3.animate.shift(LEFT*8), run_time=5)
        self.wait()
        self.play(FadeOut(complex3), run_time=2)
        self.wait()





class Komplex4Explanation(Scene):
    def construct(self):

        o2Text = MathTex(r"O_{2}").shift(UP*-2 + -1*RIGHT).set_z_index(1)
        ofirst = MathTex(r"O").set_z_index(1)
        osecond = MathTex(r"O").set_z_index(1)
        h2o1Text = MathTex(r"H_{2}O").set_z_index(1)
        h2o2Text = MathTex(r"H_{2}O").set_z_index(1)

        blackBox1 = SurroundingRectangle(o2Text, corner_radius=0.3, color=BLACK, fill_opacity=0.5, stroke_opacity=0).move_to(o2Text)


        h1 = MathTex("H^{+}").shift(UP*-3 + -3*RIGHT).set_z_index(1)
        h2 = MathTex("H^{+}").shift(UP*-2 + -3.5*RIGHT).set_z_index(1)
        h3 = MathTex("H^{+}").shift(UP*-3 + -4*RIGHT).set_z_index(1)
        h4 = MathTex("H^{+}").shift(UP*-2 + -4.5*RIGHT).set_z_index(1)
        hReaction = VGroup(h1,h2,h3,h4).set_z_index(1)
        h1normal = MathTex("H")
        h2normal = MathTex("H")
        h3normal = MathTex("H")
        h4normal = MathTex("H")

        h5 = MathTex("H^{+}").shift(RIGHT*-3 + DOWN*0)
        h6 = MathTex("H^{+}").shift(RIGHT*-2 + DOWN*1)
        h7 = MathTex("H^{+}").shift(RIGHT*-1 + DOWN*0)
        h8 = MathTex("H^{+}").shift(RIGHT*0 + DOWN*1)
        empty1 = Text("0").shift(RIGHT*-1.1 + UP*9).set_opacity(0)
        empty2 = Text("0").shift(RIGHT*-1.1 + UP*9.01).set_opacity(0)
        empty3 = Text("0").shift(RIGHT*-1.1 + UP*9.02).set_opacity(0)
        empty4 = Text("0").shift(RIGHT*-1.1 + UP*9.03).set_opacity(0)
        allH = VGroup(h5, h6, h7, h8, empty1, empty2, empty3, empty4).shift(UP*-1 +RIGHT)

        cytc1Text = MathTex("CytC").shift(UP*1.7 + LEFT*8)
        cytc2Text = MathTex("CytC").shift(UP*1.7 + LEFT*10)
        cytc3Text = MathTex("CytC").shift(UP*1.7 + LEFT*12)
        cytc4Text = MathTex("CytC").shift(UP*1.7 + LEFT*14)
        e1 = Electron().scale(0.1).shift(UP*2.1 + LEFT*8)
        e2 = Electron().scale(0.1).shift(UP*2.1 + LEFT*10)
        e3 = Electron().scale(0.1).shift(UP*2.1 + LEFT*12)
        e4 = Electron().scale(0.1).shift(UP*2.1 + LEFT*14)
        taxi1 = VGroup(cytc1Text,e1)
        taxi2 = VGroup(cytc2Text,e2)
        taxi3 = VGroup(cytc3Text,e3)
        taxi4 = VGroup(cytc4Text,e4)

        oxidator = ImageMobject("Sprites/OxidatorSprite.png").shift(UP*1.3+ RIGHT*3).scale(2.3)
        membrane1 = ImageMobject("SpritesOld/MembraneSprite.png").set_opacity(0.4).shift(UP*2 +LEFT*1)
        membrane2 = ImageMobject("SpritesOld/MembraneSprite.png").set_opacity(0.8).shift(UP*2 +LEFT*-4.8)
        membrane3 = ImageMobject("SpritesOld/MembraneSprite.png").set_opacity(0.4).shift(UP*2 +LEFT*6.85)
        complex4 = Group(membrane1, membrane2, membrane3, oxidator)

        self.add_sound("Sounds/Komplex4.m4a", time_offset=1)
        self.add_sound("Sounds/K4E.wav", time_offset=0, gain=1.8)

        self.wait()
        self.play(Write(o2Text), Write(hReaction))
        self.wait()
        self.play(FadeIn(complex4))
        self.wait(3)
        self.play(VGroup(o2Text,blackBox1).animate.shift(1.5*UP + 4*RIGHT), hReaction.animate.shift(RIGHT*4 +0*UP), run_time=2)
        self.play(AnimationGroup(
            taxi1.animate.shift(RIGHT*8.5),taxi2.animate.shift(RIGHT*8.5),
            taxi3.animate.shift(RIGHT*8.5),taxi4.animate.shift(RIGHT*8.5), lag_ratio=0.2), run_time = 6)

        self.wait(2)
        ofirst.next_to(o2Text, LEFT)
        osecond.next_to(o2Text, RIGHT)
        blackBox2 = SurroundingRectangle(ofirst, corner_radius=0.2, color=BLACK, fill_opacity=0.5, stroke_opacity=0).scale(1.3).move_to(ofirst)
        blackBox3 = SurroundingRectangle(osecond, corner_radius=0.2, color=BLACK, fill_opacity=0.5, stroke_opacity=0).scale(1.3).move_to(osecond)
        self.play(Transform(o2Text, VGroup(ofirst,osecond)), ReplacementTransform(blackBox1, VGroup(blackBox2,blackBox3)), run_time = 2.5)

        self.wait(3)
        self.play(e1.animate.move_to([2.1,-0.2,0]))
        self.play(CyclicReplace(*VGroup(taxi4,taxi3,taxi2,cytc1Text)))
        self.play(e2.animate.move_to([2.6,-0.2,0]))
        self.play(CyclicReplace(*VGroup(cytc1Text,taxi4,taxi3,cytc2Text)))
        self.wait(3)
        self.play(h1.animate.move_to([1.9,-1.1,0]))
        self.play(h2.animate.move_to([2.7,-1.1,0]))
        self.wait(2)

        h1normal.move_to(h1)
        h2normal.move_to(h2)
        self.play(e1.animate.move_to(h1).set_opacity(0), Transform(h1, h1normal))
        self.play(e2.animate.move_to(h2).set_opacity(0), Transform(h2, h2normal))
        h2o1Text.move_to(o2Text[0])
        self.wait(2)
        blackBox4 = SurroundingRectangle(h2o1Text, corner_radius=0.2, color=BLACK, fill_opacity=0.5, stroke_opacity=0).scale(1.3).move_to(h2o1Text)
        self.play(Transform(VGroup(o2Text[0],h1,h2), h2o1Text), ReplacementTransform(blackBox2, blackBox4), run_time=2)
        self.wait()

        self.play(o2Text[0].animate.shift(LEFT*4+DOWN*4), blackBox4.animate.shift(LEFT*4+DOWN*4),
                cytc1Text.animate.set_y(y=1.7), cytc2Text.animate.set_y(y=1.7), cytc3Text.animate.set_y(y=1.7), cytc4Text.animate.set_y(y=1.7),
                e3.animate.set_y(y=2.1),e4.animate.set_y(y=2.1), run_time=3)

        self.play(hReaction.animate.shift(RIGHT*2))

        self.wait(2)
        self.play(e3.animate.move_to([3.4,-0.2,0]))
        self.play(CyclicReplace(*VGroup(cytc2Text,cytc1Text,taxi4,cytc3Text)))
        self.play(e4.animate.move_to([4,-0.2,0]))
        self.play(CyclicReplace(*VGroup(cytc3Text,cytc2Text,cytc1Text,cytc4Text)))
        self.wait()
        self.play(h3.animate.move_to([3.2,-1.1,0]))
        self.play(h4.animate.move_to([4.1,-1.1,0]))
        self.wait(2)

        h3normal.move_to(h3)
        h4normal.move_to(h4)
        self.play(e3.animate.move_to(h3).set_opacity(0), Transform(h3, h3normal))
        self.play(e4.animate.move_to(h4).set_opacity(0), Transform(h4, h4normal))
        h2o2Text.move_to(o2Text[1])
        blackBox5 = SurroundingRectangle(h2o2Text, corner_radius=0.2, color=BLACK, fill_opacity=0.5, stroke_opacity=0).scale(1.3).move_to(h2o2Text)
        self.wait()
        self.play(Transform(VGroup(o2Text[1],h3,h4), h2o2Text), ReplacementTransform(blackBox3, blackBox5))

        self.play(o2Text[1].animate.shift(LEFT*3+DOWN*5), blackBox5.animate.shift(LEFT*3+DOWN*5),
                cytc1Text.animate.set_y(y=1.7), cytc2Text.animate.set_y(y=1.7), cytc3Text.animate.set_y(y=1.7), cytc4Text.animate.set_y(y=1.7), run_time=2)

        self.play(AnimationGroup(
            cytc1Text.animate.shift(RIGHT*-8.5),cytc2Text.animate.shift(RIGHT*-8.5),
            cytc3Text.animate.shift(RIGHT*-8.5),cytc4Text.animate.shift(RIGHT*-8.5), lag_ratio=0.2), run_time = 3)

        ## pump h+
        self.play(Write(allH), run_time=1)
        self.play(allH.animate.shift(UP*1 +RIGHT))
        self.play(CyclicReplace(*allH, path_arc=1.4), run_time=3)
        self.play(CyclicReplace(*allH, path_arc=1.4), run_time=2.5)
        self.play(CyclicReplace(*allH, path_arc=1.4), run_time=1.5)
        self.play(CyclicReplace(*allH, path_arc=1.4), run_time=1)
        self.play(FadeOut(complex4))
        self.wait()





class Komplex5Explanation(ThreeDScene):
    def construct(self):
        
        atpSynthaseHead = ImageMobject("Sprites/ATPSynthaseHeadSprite.png").scale(2).set_z_index(1).shift(DOWN*0.5)
        shaft1 = ImageMobject("Sprites/ATPSynthaseShaftSprite.png").scale(2).set_z_index(1).shift(UP*0.9)
        shaft2 = ImageMobject("Sprites/ATPSynthaseShaftSprite.png").scale(2).set_z_index(1).shift(UP*0.9)
        atpSynthaseConnector = ImageMobject("Sprites/ProtonChannelSprite.png").scale(2).shift(UP*1.5).set_z_index(0)

        membrane1 = ImageMobject("SpritesOld/MembraneSprite.png").scale(1).shift(UP*1.5).set_z_index(-1).set_opacity(0.6)
        membrane2 = ImageMobject("SpritesOld/MembraneSprite.png").scale(1).shift(UP*1.5 +RIGHT*5.8).set_z_index(-1).set_opacity(0.6)
        membrane3 = ImageMobject("SpritesOld/MembraneSprite.png").scale(1).shift(UP*1.5 +RIGHT*-5.8).set_z_index(-1).set_opacity(0.6)

        complex5 = Group(atpSynthaseHead, atpSynthaseConnector, shaft1, shaft2, membrane1, membrane2, membrane3)

        h1 = MathTex(r"H^{+}").shift(UP*3 + RIGHT*8).set_z_index(2)
        h2 = MathTex(r"H^{+}").shift(UP*3 + RIGHT*9).set_z_index(2)
        h3 = MathTex(r"H^{+}").shift(UP*3 + RIGHT*10).set_z_index(2)
        h4 = MathTex(r"H^{+}").shift(UP*3 + RIGHT*11).set_z_index(2)
        h5 = MathTex(r"H^{+}").shift(UP*3 + RIGHT*12).set_z_index(2)
        h6 = MathTex(r"H^{+}").shift(UP*3 + RIGHT*13).set_z_index(2)
        h7 = MathTex(r"H^{+}").shift(UP*3 + RIGHT*14).set_z_index(2)
        h8 = MathTex(r"H^{+}").shift(UP*3 + RIGHT*15).set_z_index(2)
        allH = VGroup(h1,h2,h3,h4,h5,h6,h7,h8)

        adp1 = MathTex("ADP").shift(LEFT*5 + DOWN).set_z_index(2)
        adp2 = MathTex("ADP").shift(LEFT*5 + DOWN).set_z_index(2)
        adp3 = MathTex("ADP").shift(LEFT*5 + DOWN).set_z_index(2)

        atp1 = MathTex("ATP").set_z_index(2).shift(RIGHT + DOWN*1.5)
        atp2 = MathTex("ATP").set_z_index(2).shift(RIGHT + DOWN*1.5)
        atp3 = MathTex("ATP").set_z_index(2).shift(RIGHT + DOWN*1.5)

        p1 = MathTex("P").shift(LEFT*5 + 2.5*DOWN).set_z_index(2)
        p2 = MathTex("P").shift(LEFT*5 + 2.5*DOWN).set_z_index(2)
        p3 = MathTex("P").shift(LEFT*5 + 2.5*DOWN).set_z_index(2)

        self.add_sound("Sounds/Komplex5.m4a", time_offset=1)
        self.add_sound("Sounds/K5E.wav", time_offset=0, gain=1.6)

 
        self.wait()
        self.play(FadeIn(complex5), run_time=1)
        self.play(Write(adp1))
        self.play(Write(p1))

        blackBox1 = SurroundingRectangle(adp1, corner_radius=0.2, color=BLACK, fill_opacity=0.5, stroke_opacity=0).move_to(adp1).set_z_index(2)
        blackBox2 = SurroundingRectangle(p1, corner_radius=0.2, color=BLACK, fill_opacity=0.5, stroke_opacity=0).move_to(p1).set_z_index(2)
        self.play(VGroup(blackBox1, adp1).animate.shift(RIGHT*4.7 + DOWN*0.3), run_time=3)
        self.play(VGroup(blackBox2, p1).animate.shift(RIGHT*4.7 + UP*0.5), run_time=3)
        self.play(AnimationGroup(*[h.animate.shift(LEFT * 9) for h in allH], lag_ratio=0.1))

        shearIn = [[0.707, 0], [0, 1]]
        shearInFull = [[0.01, 0], [0, 1]]
        shearOut = [[1.415, 0], [0, 1]]
        shearOutFull = [[100, 0], [0, 1]]
        shaft2.apply_matrix(shearIn)
        shaft2.apply_matrix(shearInFull)

        blackBox3 = SurroundingRectangle(h1, corner_radius=0.2, color=BLACK, fill_opacity=0.5, stroke_opacity=0).move_to(h1).set_z_index(2)
        self.play(VGroup(blackBox3,h1).animate.shift(DOWN*1.5))
        self.play(shaft1.animate.apply_matrix(shearIn), shaft2.animate.apply_matrix(shearOutFull), VGroup(blackBox3,h1).animate.shift(RIGHT*2.2))
        self.play(VGroup(blackBox3,h1).animate.shift(DOWN*1.5))
        self.play(VGroup(blackBox3,h1).animate.shift(RIGHT*7))
        self.play(VGroup(h2,h3,h4,h5,h6,h7,h8).animate.shift(LEFT))

        blackBox3 = SurroundingRectangle(h2, corner_radius=0.2, color=BLACK, fill_opacity=0.5, stroke_opacity=0).move_to(h2).set_z_index(2)
        self.play(VGroup(blackBox3,h2).animate.shift(DOWN*1.5))
        self.play(shaft1.animate.apply_matrix(shearInFull), shaft2.animate.apply_matrix(shearOut), VGroup(blackBox3,h2).animate.shift(RIGHT*2.2))
        self.play(VGroup(blackBox3,h2).animate.shift(DOWN*1.5))
        self.play(VGroup(blackBox3,h2).animate.shift(RIGHT*7))
        self.play(VGroup(h3,h4,h5,h6,h7,h8).animate.shift(LEFT))

        blackBox3 = SurroundingRectangle(h3, corner_radius=0.2, color=BLACK, fill_opacity=0.5, stroke_opacity=0).move_to(h3).set_z_index(2)
        self.play(VGroup(blackBox3,h3).animate.shift(DOWN*1.5))
        self.play(shaft1.animate.apply_matrix(shearOutFull), shaft2.animate.apply_matrix(shearIn), VGroup(blackBox3,h3).animate.shift(RIGHT*2.2))
        self.play(VGroup(blackBox3,h3).animate.shift(DOWN*1.5))
        self.play(VGroup(blackBox3,h3).animate.shift(RIGHT*7))
        self.play(VGroup(h4,h5,h6,h7,h8).animate.shift(LEFT))


        blackBox4 = SurroundingRectangle(atp1, corner_radius=0.2, color=BLACK, fill_opacity=0.5, stroke_opacity=0).move_to(atp1).set_z_index(2)
        self.play(ReplacementTransform(VGroup(blackBox1,blackBox2), blackBox4), ReplacementTransform(VGroup(adp1,p1), atp1), run_time=3)
        self.play(VGroup(blackBox4,atp1).animate.shift(DOWN*4 + RIGHT*2), run_time=2)

        self.play(Write(adp2), run_time=3)
        self.play(Write(p2), run_time=3)

        blackBox1 = SurroundingRectangle(adp2, corner_radius=0.2, color=BLACK, fill_opacity=0.5, stroke_opacity=0).move_to(adp2).set_z_index(2)
        blackBox2 = SurroundingRectangle(p2, corner_radius=0.2, color=BLACK, fill_opacity=0.5, stroke_opacity=0).move_to(p2).set_z_index(2)
        self.play(VGroup(blackBox1, adp2).animate.shift(RIGHT*4.7 + DOWN*0.3))
        self.play(VGroup(blackBox2, p2).animate.shift(RIGHT*4.7 + UP*0.5))


        blackBox3 = SurroundingRectangle(h4, corner_radius=0.2, color=BLACK, fill_opacity=0.5, stroke_opacity=0).move_to(h4).set_z_index(2)
        self.play(VGroup(blackBox3,h4).animate.shift(DOWN*1.5))
        self.play(shaft1.animate.apply_matrix(shearOut), shaft2.animate.apply_matrix(shearInFull), VGroup(blackBox3,h4).animate.shift(RIGHT*2.2))
        self.play(VGroup(blackBox3,h4).animate.shift(DOWN*1.5))
        self.play(VGroup(blackBox3,h4).animate.shift(RIGHT*7))
        self.play(VGroup(h5,h6,h7,h8).animate.shift(LEFT))


        blackBox3 = SurroundingRectangle(h5, corner_radius=0.2, color=BLACK, fill_opacity=0.5, stroke_opacity=0).move_to(h5).set_z_index(2)
        self.play(VGroup(blackBox3,h5).animate.shift(DOWN*1.5))
        self.play(shaft1.animate.apply_matrix(shearIn), shaft2.animate.apply_matrix(shearOutFull), VGroup(blackBox3,h5).animate.shift(RIGHT*2.2))
        self.play(VGroup(blackBox3,h5).animate.shift(DOWN*1.5))
        self.play(VGroup(blackBox3,h5).animate.shift(RIGHT*7))
        self.play(VGroup(h6,h7,h8).animate.shift(LEFT))


        blackBox4 = SurroundingRectangle(atp2, corner_radius=0.2, color=BLACK, fill_opacity=0.5, stroke_opacity=0).move_to(atp2).set_z_index(2)
        self.play(ReplacementTransform(VGroup(blackBox1,blackBox2), blackBox4), ReplacementTransform(VGroup(adp2,p2), atp2), run_time=3)
        self.play(VGroup(blackBox4,atp2).animate.shift(DOWN*4 + RIGHT*2), run_time=2)

        self.play(Write(adp3), run_time=3)
        self.play(Write(p3), run_time=3)

        blackBox1 = SurroundingRectangle(adp3, corner_radius=0.2, color=BLACK, fill_opacity=0.5, stroke_opacity=0).move_to(adp3).set_z_index(2)
        blackBox2 = SurroundingRectangle(p3, corner_radius=0.2, color=BLACK, fill_opacity=0.5, stroke_opacity=0).move_to(p3).set_z_index(2)
        self.play(VGroup(blackBox1, adp3).animate.shift(RIGHT*4.7 + DOWN*0.3))
        self.play(VGroup(blackBox2, p3).animate.shift(RIGHT*4.7 + UP*0.5))


        blackBox3 = SurroundingRectangle(h6, corner_radius=0.2, color=BLACK, fill_opacity=0.5, stroke_opacity=0).move_to(h6).set_z_index(2)
        self.play(VGroup(blackBox3,h6).animate.shift(DOWN*1.5))
        self.play(shaft1.animate.apply_matrix(shearInFull), shaft2.animate.apply_matrix(shearOut), VGroup(blackBox3,h6).animate.shift(RIGHT*2.2))
        self.play(VGroup(blackBox3,h6).animate.shift(DOWN*1.5))
        self.play(VGroup(blackBox3,h6).animate.shift(RIGHT*7))
        self.play(VGroup(h7,h8).animate.shift(LEFT))

        blackBox3 = SurroundingRectangle(h7, corner_radius=0.2, color=BLACK, fill_opacity=0.5, stroke_opacity=0).move_to(h7).set_z_index(2)
        self.play(VGroup(blackBox3,h7).animate.shift(DOWN*1.5))
        self.play(shaft1.animate.apply_matrix(shearOutFull), shaft2.animate.apply_matrix(shearIn), VGroup(blackBox3,h7).animate.shift(RIGHT*2.2))
        self.play(VGroup(blackBox3,h7).animate.shift(DOWN*1.5))
        self.play(VGroup(blackBox3,h7).animate.shift(RIGHT*7))
        self.play(VGroup(h8).animate.shift(LEFT))

        blackBox3 = SurroundingRectangle(h8, corner_radius=0.2, color=BLACK, fill_opacity=0.5, stroke_opacity=0).move_to(h8).set_z_index(2)
        self.play(VGroup(blackBox3,h8).animate.shift(DOWN*1.5))
        self.play(shaft1.animate.apply_matrix(shearOut), shaft2.animate.apply_matrix(shearInFull), VGroup(blackBox3,h8).animate.shift(RIGHT*2.2))
        self.play(VGroup(blackBox3,h8).animate.shift(DOWN*1.5))
        self.play(VGroup(blackBox3,h8).animate.shift(RIGHT*7))


        blackBox4 = SurroundingRectangle(atp3, corner_radius=0.2, color=BLACK, fill_opacity=0.5, stroke_opacity=0).move_to(atp3).set_z_index(2)
        self.play(ReplacementTransform(VGroup(blackBox1,blackBox2), blackBox4), ReplacementTransform(VGroup(adp3,p3), atp3), run_time=3)
        self.play(VGroup(blackBox4,atp3).animate.shift(DOWN*4 + RIGHT*2), run_time=2)

        self.play(FadeOut(complex5))
        self.wait()



class Ending(Scene):
    def construct(self):

        self.add_sound(sound_file="Sounds/MusicEnding.wav",time_offset=0)

        banner = ManimBanner().scale(0.5)
        bannertxt = Tex("https://www.manim.community/")
        musicimg = ImageMobject("Pictures/3b1bmusiclogo.jpg").scale(0.8).set_z_index(-1)
        musicimgtxt = Tex("https://vincerubinetti.bandcamp.com/album/the-music-of-3blue1brown").scale(0.85)
        
        page1 = VGroup(banner,bannertxt,musicimgtxt)

        unity = ImageMobject("Pictures/Unity.png").scale(1)
        unitytxt = Tex("https://unity.com/").scale(1)
        download = Tex("Download zur Simulation, Skript, Quellen:")
        download2 = Tex("https://github.com/Namitera/ErLe-Endoxidation-27.11.2025").scale(0.85).shift(DOWN)

        page2 = VGroup(download,download2,unitytxt)

        self.wait()
        self.play(banner.create())
        self.play(banner.expand())
        self.play(banner.animate.to_corner(UL))
        self.play(FadeIn(bannertxt))
        self.play(bannertxt.animate.next_to(banner,DOWN).align_to(banner,LEFT))
        self.wait(3)
        self.play(FadeIn(musicimg))
        self.play(musicimg.animate.to_edge(LEFT).shift(DOWN+LEFT*0.5))
        self.play(FadeIn(musicimgtxt))
        self.play(musicimgtxt.animate.next_to(musicimg,DOWN).align_to(musicimg,LEFT).shift(RIGHT*0.5+UP*0.3))
        self.wait(5)
        self.play(FadeOut(page1),FadeOut(musicimg))
        self.wait()


        self.play(FadeIn(unity), run_time=2)
        self.play(unity.animate.to_corner(UL).shift(DOWN*0+LEFT*0.2))
        self.play(FadeIn(unitytxt), run_time=1)
        self.play(unitytxt.animate.next_to(unity,DOWN).align_to(unity,LEFT).shift(RIGHT*0.6+UP*0.3))
        self.play(FadeIn(download))
        self.play(download.animate.to_corner(UL).shift(DOWN*4+LEFT*-0.5))
        self.play(FadeIn(download2))
        self.play(download2.animate.to_corner(UL).shift(DOWN*5+LEFT*-0.5))
        self.wait(5)
        self.play(FadeOut(page2), FadeOut(unity))
        self.wait()