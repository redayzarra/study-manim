from manim import *


class MovingRedBox(Scene):
    def construct(self):

        # Create a rectangle with the properties you want
        box = Rectangle(
            stroke_color=GREEN_C,
            stroke_opacity=0.7,
            fill_color=RED_B,
            fill_opacity=0.5,
            height=1,
            width=1,
        )

        # Start with the box on the scene
        self.add(box)

        # Play some animations of you moving the box around
        self.play(box.animate.shift(RIGHT * 2), run_time=2)
        self.play(box.animate.shift(UP * 3), run_time=2)
        self.play(box.animate.shift(DOWN * 5 + LEFT * 5), run_time=2)
        self.play(box.animate.shift(UP * 1.5 + RIGHT), run_time=2)


class MorphingTriangleGrid(Scene):
    def construct(self):

        # Create an axes (number plane)
        axes = Axes(x_range=[-3, 3, 1], y_range=[-3, 3, 1], x_length=6, y_length=6)

        # Place the axes on the very left as starting position (with padding 0.5)
        axes.to_edge(LEFT, buff=0.5)

        # Create a circle with the properties you want
        circle = Circle(
            stroke_width=6, stroke_color=YELLOW, fill_color=RED_C, fill_opacity=0.8
        )
        # Place the circle
        circle.set_width(8).to_edge(DR)

        triangle = (
            Triangle(stroke_color=ORANGE, stroke_width=10, fill_color=GREY)
            .set_height(2)
            .shift(DOWN * 3 + RIGHT * 3)
        )

        self.play(Write(axes))
        self.play(DrawBorderThenFill(circle))
        self.play(circle.animate.set_width(1))
        self.play(Transform(circle, triangle), run_time=3)
        self.wait()


