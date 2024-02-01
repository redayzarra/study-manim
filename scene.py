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
