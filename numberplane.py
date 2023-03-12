from manim import *

class SomethingElse(Scene):
  def construct(self):

    my_plane = NumberPlane(x_range = [-6, 6], x_length = 5,
    y_range = [-10, -10], y_length=5)

    my_plane.add_coordinates()
    my_plane.shift(RIGHT * 3)

    my_function = my_plane.plot(lambda x: 0.1 * (x-5) * x * (x+5),
    x_range = [-6, 6], color = GREEN_B)
    
    area = my_plane.get_area(graph = my_function,
    x_range = [-5, 5], color = [BLUE, YELLOW])

    label = MathTex("f(x) = 0.1x(x-5)(x+5)").next_to(
      my_plane, UP, buff = 0.2)

    horiz_line = Line(
      start = my_plane.c2p(0, my_function.underlying_function(-2)),
      end = my_plane.c2p(-2, my_function.underlying_function(-2)),
      stroke_color = YELLOW, stroke_width = 10)

    self.play(DrawBorderThenFill(my_plane))
    self.play(Create(my_function), Write(label))
    self.play(FadeIn(area))
    self.play(Create(horiz_line))