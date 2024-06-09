from manim import *

# config.pixel_width = 1080
# config.pixel_height = 1920
# config.frame_width = 9
# config.frame_height = 16

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
        axes.to_edge(LEFT, buff=0.2)

        # Create a circle with the properties you want
        circle = Circle(
            stroke_width=6, stroke_color=GREEN, fill_color=BLUE_D, fill_opacity=0.8
        )
        # Place the circle of width 8 near the edge (down right)
        circle.set_width(8).to_edge(DR)

        # Create a triangle with the properties we want
        triangle = Triangle(stroke_color=ORANGE, stroke_width=10, fill_color=GREY)
        # Place the triangle of height 2 wherever we want
        triangle.set_height(2).shift(DOWN * 3 + RIGHT * 3)

        # Animate and write the axes in a pretty way
        self.play(Write(axes))
        # Draw the circle then fill it with the color we specified earlier
        self.play(DrawBorderThenFill(circle))
        # Animate and change the width of the circle
        self.play(circle.animate.set_width(1))
        # Morph the circle into the triangle we defined earlier
        self.play(Transform(circle, triangle), run_time=3)
        self.wait()


class RectangleWithText(Scene):
    def construct(self):
        
        # Create and define the rectangle we want and position it
        rectangle = RoundedRectangle(
            stroke_width=8, stroke_color=WHITE, fill_color=BLUE_B, width=4.5, height=2
        ).shift(UP * 3 + LEFT * 4)

        # Create and define text (LaTeX)
        text = (
            MathTex("\\frac{3}{4} = 0.75")
            .set_color_by_gradient(GREEN, PINK)
            .set_height(1.5)
        )
        
        # Move the text to the center of rectangle and make sure it stays
        text.move_to(rectangle.get_center())
        text.add_updater(lambda x: x.move_to(rectangle.get_center()))

        # Animate the rectangle and write text
        self.play(FadeIn(rectangle))
        self.play(Write(text))

        # Move the rectangle around - text stays with it
        self.play(rectangle.animate.shift(RIGHT * 1.5 + DOWN * 5), run_time=6)
        self.wait()

        # Remove all updaters and then move rectangle - text leaves behind
        text.clear_updaters()
        self.play(rectangle.animate.shift(LEFT * 2 + UP), run_time=2)
        self.wait()
