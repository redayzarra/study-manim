from manim import *

class MovingBox(Scene):
  def construct(self):

    box = Rectangle(stroke_color = GREEN_C, stroke_opacity = 0.7, 
    fill_color = RED_B, fill_opacity = 0.5, height = 1, width = 1)

    self.add(box)
    self.play(box.animate.shift(RIGHT*2), run_time = 2)
    self.play(box.animate.shift(UP*2), run_time = 2)
    self.play(box.animate.shift(DOWN*5+LEFT*5), run_time = 2)
    self.play(box.animate.shift(UP*1.5+RIGHT*1), run_time = 2)