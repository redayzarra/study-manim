from manim import *

class FittingObjects(Scene):
  def construct(self):
    
    axes = Axes(x_range=[-3, 3, 1], y_range=[-3, 3, 1], 
    x_length=6, y_length=6)
    axes.to_edge(LEFT, buff = 0.5)

    circle = Circle(stroke_width = 6, stroke_color = YELLOW, 
    fill_color = RED_C, fill_opacity = 0.8)
    circle.set_width(2).to_edge(DR, buff = 0)

    triangle = Triangle(stroke_color = ORANGE, stroke_width = 10,
    fill_color = GREY).set_height(2).shift(DOWN*3+RIGHT*3)

    self.play(Write(axes))
    self.play(DrawBorderThenFill(circle))
    self.play(circle.animate.set_width(1))
    self.play(Transform(circle, triangle), run_time= 3)