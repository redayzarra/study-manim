from manim import *

class SquareAndCircle(Scene):
    def construct(self):
        circle = Circle()
        circle.set_fill(PINK, opacity = 0.5)
        
        square = Square()
        square.set_fill(BLUE, opacity = 0.5)
        
        square.next_to(circle, RIGHT, buff = 0.5)
        
        self.play(Create(circle), Create(square))