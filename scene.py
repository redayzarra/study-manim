from manim import *

class CreateCircle(Scene):
    def construct(self):
        circle = Circle()
        circle.set_fill(PINK, opacity = 0.5)
        
        # Show the circle on screen
        self.play(Create(circle))
        
class SquareToCircle(Scene):
    def construct(self):
        circle = Circle()
        circle.set_fill(PINK, opacity = 0.5)
        
        square = Square()
        square.rotate(PI / 4)
        
        self.play(Create(square))
        self.play(Transform(square, circle))
        self.play(FadeOut(square))

class SquareAndCircle(Scene):
    def construct(self):
        circle = Circle()
        circle.set_fill(PINK, opacity = 0.5)
        
        square = Square()
        square.set_fill(BLUE, opacity = 0.5)
        
        square.next_to(circle, RIGHT, buff = 0.5)
        
        self.play(Create(circle), Create(square))
        
class AnimateSquareToCircle(Scene):
    def construct(self):
        circle = Circle()
        square = Square()
        
        self.play(Create(square))
        self.play(square.animate.rotate(PI / 4))
        
        self.play(ReplacementTransform(square, circle))
        self.play(circle.animate.set_fill(PINK, opacity = 0.5))
        
class DifferentRotations(Scene):
    def construct(self):
        left_square = Square(color = BLUE, fill_opacity = 0.7).shift(2 * LEFT)
        right_square = Square(color = GREEN, fill_opacity = 0.7).shift(2 * RIGHT)
        
        self.play(left_square.animate.rotate(PI), Rotate(right_square, angle = PI), run_time = 2)
        self.wait()

class Text(Scene):
    def construct(self):
        name = Tex("ReDay Z.").to_edge(UL, buff = 0.5)
        square = Square(side_length = 0.5, fill_color = BLUE).shift(LEFT * 3)
        triangle = Triangle().scale(0.6).to_edge(DR)
        
        self.play(Write(name))
        self.play(DrawBorderThenFill(square), run_time = 2)
        self.play(Create(triangle))
        self.wait()

        self.play(name.animate.to_edge(UR), run_time = 2)
        self.play(square.animate.scale(2), triangle.animate.to_edge(DL), run_time = 3)
        self.wait()

class Getters(Scene):
    def construct(self):
        rect = Rectangle(color = WHITE, height = 3, width = 2.5).to_edge(UL)
        circle = Circle().to_edge(DOWN)
        
        arrow = always_redraw(lambda: Line(start = rect.get_bottom(), end = circle.get_top(), buff = 0.2).add_tip())

        self.play(Create(VGroup(rect, circle, arrow)))
        self.wait()
        self.play(rect.animate.to_edge(UR), circle.animate.scale(0.5), run_time = 4)
        
        
class Updaters(Scene):
    def construct(self):
        num = MathTex("ln(2)")
        box = always_redraw(lambda: SurroundingRectangle(num, color = WHITE, fill_opacity = 0.4, fill_color = BLUE, buff = 1))
        name = always_redraw(lambda: Tex("ReDay Z.").next_to(box, DOWN, buff = 0.25))
        
        self.play(Create(VGroup(num, box, name)))
        self.play(num.animate.shift(RIGHT * 2), run_time = 2)
        self.wait()

class ValueTrackers(Scene):
    def construct(self):
        value = ValueTracker(6)
        num = always_redraw(lambda: DecimalNumber().set_value(value.get_value()))
        
        self.play(FadeIn(num))
        self.wait()
        
        self.play(value.animate.set_value(0), run_time = 5, rate_func = smooth)
        self.wait()
        