from manim import *

class TreeCircle(Scene):
  def construct(self):

    r = ValueTracker(0.5)

    circle = always_redraw(lambda:
    Circle(radius=r.get_value(), stroke_color = YELLOW,
    stroke_width = 5))

    line_radius = always_redraw(lambda:
    Line(start=circle.get_center(), end = circle.get_bottom(), stroke_color = RED_B, stroke_width = 10))

    line_circumfrence = always_redraw(lambda:
    Line(stroke_color = YELLOW, stroke_width = 5
    ).set_length(2 * r.get_value() * PI).next_to(circle, DOWN, buff = 0.2))

    traingle = always_redraw(lambda:
    Polygon(circle.get_top(), circle.get_left(), circle.get_right(), fill_color = GREEN_C))

    self.play(LaggedStart(
      Create(circle), DrawBorderThenFill(line_radius), DrawBorderThenFill(traingle), 
      run_time = 4, lag_rate = 0.75
    ))

    self.play(ReplacementTransform(circle.copy(), line_circumfrence), run_time = 2)
    self.play(r.animate.set_value(2), run_time = 5)
