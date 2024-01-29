from manim import * 

class CreateCircle(Scene):
    def construct(self):
        circle = Circle()
        circle.set_fill(PINK, opacity = 0.5)
        
        # Show the circle on screen
        self.play(Create(circle))