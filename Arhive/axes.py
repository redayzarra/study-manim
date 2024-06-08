from manim import *

class GraphingMovement(Scene):
  def construct(self):

    axes = Axes(x_range = [0, 5, 1], y_range = [0, 3, 1],
    x_length = 5, y_length=3, 
    axis_config= {"include_tip":True, "numbers_to_exclude": [0]}
    ).add_coordinates()

    axes.to_edge(UR)
    axis_labels = axes.get_axis_labels(x_label = "x", y_label = "f(x)")

    graph = axes.plot(lambda x : x**0.5, x_range = [0, 4], color = YELLOW)

    graphing = VGroup(axes, graph, axis_labels)

    self.play(DrawBorderThenFill(axes), Write(axis_labels))
    self.play(Create(graph))
    self.play(graphing.animate.shift(DOWN*4))
    self.play(axes.animate.shift(LEFT*3), run_time = 3)