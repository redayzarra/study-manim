from manim import *

class AnimateSquareToCircle(Scene):
    def construct(self):
        circle = Circle()
        square = Square()
        
        self.play(Create(square))
        self.play(square.animate.rotate(PI / 4))
        
        self.play(ReplacementTransform(square, circle))
        self.play(circle.animate.set_fill(PINK, opacity = 0.5))