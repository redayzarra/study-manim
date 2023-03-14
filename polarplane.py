from manim import *

class PolarPlane(Scene):
  def construct(self):

    e = ValueTracker(0.01)

    plane = PolarPlane(radius_max = 3).add_coordinates()