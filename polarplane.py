from manim import *

class PolarPlane(Scene):
  def construct(self):

    e = ValueTracker(0.01)

    plane = PolarPlane(radius_max = 3).add_coordinates()
    plane.shift(LEFT * 2)
    graph1 = always_redraw(lambda:
    ParametricFunction(lambda t: plane.polar_to_point(2 * np.sin(3*t), t),
    t_range=[0, e.get_value()], color = GREEN)
    )
    dot1 = always_redraw(lab)