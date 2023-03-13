from manim import *

class CoordinateSystem(Scene):
  def construct(self):
    
    plane = NumberPlane(x_range= [-4, 4, 1], x_length=4, y_range=[0, 20, 5]).add_coordinates()
    plane.shift