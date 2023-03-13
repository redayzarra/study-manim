from manim import *

class CoordinateSystem(Scene):
  def construct(self):
    
    plane = NumberPlane(x_range= [-4, 4, 1], x_length=4, y_range=[0, 20, 5]).add_coordinates()
    plane.shift(LEFT * 3 + DOWN * 1.5)
    plane_graph = plane.get_graph(lambda x: x**2, x_range = [-4, 4], color = GREEN)
    area = plane.get_riemann_rectangles(graph = plane_graph, x_range=[-2, 2], dx = 0.05)

    axes = Axes(x_range = [-4, 4, 1], x_length=4, y_range = [-20, 20, 5], 
    y_length=4).add_coordinates()
    axes.shift(RIGHT * 3 + DOWN * 1.5)
    axes_graph = axes.get_graph(lambda x: 2*x, 
    x_range = [-4, 4], color = YELLOW)
    v_lines = axes.get_vertical_lines_to_graph(graph = axes_graph,
    x_range=[-3, 3], num_lines=12)
    
    self.play(Write(plane), Create(axes))
    self.play(Create(plane_graph), Create(axes_graph), run_time = 2)
    self.add(area, v_lines)