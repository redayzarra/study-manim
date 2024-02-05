from manim import *


class CreateCircle(Scene):
    def construct(self):
        circle = Circle()
        circle.set_fill(PINK, opacity=0.5)

        # Show the circle on screen
        self.play(Create(circle))


class SquareToCircle(Scene):
    def construct(self):
        circle = Circle()
        circle.set_fill(PINK, opacity=0.5)

        square = Square()
        square.rotate(PI / 4)

        self.play(Create(square))
        self.play(Transform(square, circle))
        self.play(FadeOut(square))


class SquareAndCircle(Scene):
    def construct(self):
        circle = Circle()
        circle.set_fill(PINK, opacity=0.5)

        square = Square()
        square.set_fill(BLUE, opacity=0.5)

        square.next_to(circle, RIGHT, buff=0.5)

        self.play(Create(circle), Create(square))


class AnimateSquareToCircle(Scene):
    def construct(self):
        circle = Circle()
        square = Square()

        self.play(Create(square))
        self.play(square.animate.rotate(PI / 4))

        self.play(ReplacementTransform(square, circle))
        self.play(circle.animate.set_fill(PINK, opacity=0.5))


class DifferentRotations(Scene):
    def construct(self):
        left_square = Square(color=BLUE, fill_opacity=0.7).shift(2 * LEFT)
        right_square = Square(color=GREEN, fill_opacity=0.7).shift(2 * RIGHT)

        self.play(
            left_square.animate.rotate(PI), Rotate(right_square, angle=PI), run_time=2
        )
        self.wait()


class Text(Scene):
    def construct(self):
        name = Tex("ReDay Z.").to_edge(UL, buff=0.5)
        square = Square(side_length=0.5, fill_color=BLUE).shift(LEFT * 3)
        triangle = Triangle().scale(0.6).to_edge(DR)

        self.play(Write(name))
        self.play(DrawBorderThenFill(square), run_time=2)
        self.play(Create(triangle))
        self.wait()

        self.play(name.animate.to_edge(UR), run_time=2)
        self.play(square.animate.scale(2), triangle.animate.to_edge(DL), run_time=3)
        self.wait()


class Getters(Scene):
    def construct(self):
        rect = Rectangle(color=WHITE, height=3, width=2.5).to_edge(UL)
        circle = Circle().to_edge(DOWN)

        arrow = always_redraw(
            lambda: Line(
                start=rect.get_bottom(), end=circle.get_top(), buff=0.2
            ).add_tip()
        )

        self.play(Create(VGroup(rect, circle, arrow)))
        self.wait()
        self.play(rect.animate.to_edge(UR), circle.animate.scale(0.5), run_time=4)


class Updaters(Scene):
    def construct(self):
        num = MathTex("ln(2)")
        box = always_redraw(
            lambda: SurroundingRectangle(
                num, color=WHITE, fill_opacity=0.4, fill_color=BLUE, buff=1
            )
        )
        name = always_redraw(lambda: Tex("ReDay Z.").next_to(box, DOWN, buff=0.25))

        self.play(Create(VGroup(num, box, name)))
        self.play(num.animate.shift(RIGHT * 2), run_time=2)
        self.wait()


class ValueTrackers(Scene):
    def construct(self):
        value = ValueTracker(6)
        num = always_redraw(lambda: DecimalNumber().set_value(value.get_value()))

        self.play(FadeIn(num))
        self.wait()

        self.play(value.animate.set_value(0), run_time=5, rate_func=smooth)
        self.wait()


class Graphing(Scene):
    def construct(self):
        plane = (
            NumberPlane(x_range=[-4, 4, 2], x_length=7, y_range=[0, 16, 4], y_length=4)
            .to_edge(DOWN)
            .add_coordinates()
        )

        labels = plane.get_axis_labels(x_label="x", y_label="f(x)")
        parabola = plane.plot(lambda x: x**2, x_range=[-4, 4], color=GREEN)
        func_label = (
            MathTex("f(x) = {x}^{2}")
            .scale(0.6)
            .next_to(parabola, UR, buff=0.5)
            .set_color(GREEN)
        )

        area = plane.get_riemann_rectangles(
            graph=parabola,
            x_range=[-2, 3],
            dx=0.2,
            stroke_width=0.1,
            stroke_color=WHITE,
        )

        self.play(DrawBorderThenFill(plane))
        self.play(Create(VGroup(labels, parabola, func_label)))
        self.wait()
        self.play(Create(area))


class UpdaterGraphing(Scene):
    def my_function(self, x: int):
        return x**2

    def construct(self):
        k = ValueTracker(-4)
        axis = (
            Axes(x_range=[-4, 4, 1], y_range=[-2, 16, 2], x_length=10, y_length=6)
            .to_edge(DOWN)
            .add_coordinates()
            .set_color(WHITE)
        )

        function = axis.plot(lambda x: x**2, x_range=[-4, 4], color=BLUE)
        slope = always_redraw(
            lambda: axis.get_secant_slope_group(
                x=k.get_value(),
                graph=function,
                dx=0.01,
                secant_line_color=GREEN,
                secant_line_length=3,
            )
        )

        point = always_redraw(
            lambda: Dot().move_to(
                axis.c2p(k.get_value(), function.underlying_function(k.get_value()))
            )
        )

        self.add(axis, function, slope, point)
        self.wait()
        self.play(k.animate.set_value(4), run_time=3)
        self.wait()


class Shifting(Scene):
    def construct(self):
        box = Rectangle(
            fill_color=RED_B,
            fill_opacity=0.5,
            stroke_opacity=0.7,
            stroke_color=GREEN_C,
            height=1,
            width=1,
        )

        self.add(box)
        self.play(box.animate.shift(RIGHT * 2), run_time=2)
        self.play(box.animate.shift(UP * 3), run_time=2)
        self.play(box.animate.shift(DOWN * 5 + LEFT * 5), run_time=2)
        self.play(box.animate.shift(UP * 1.5 + RIGHT), run_time=2)
        self.wait()


class Fitting(Scene):
    def construct(self):
        axes = Axes(x_range=[-3, 3, 1], y_range=[-3, 3, 1], x_length=6, y_length=6)
        axes.to_edge(LEFT, buff=0.5)

        circle = Circle(
            stroke_width=6, stroke_color=YELLOW, fill_color=RED_C, fill_opacity=0.8
        )
        circle.set_width(2).to_edge(DR)

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


class Updaters(Scene):
    def construct(self):
        rectangle = RoundedRectangle(
            stroke_width=8, stroke_color=WHITE, fill_color=BLUE_B, width=4.5, height=2
        ).shift(UP * 3 + LEFT * 4)

        text = (
            MathTex("\\frac{3}{4} = 0.75")
            .set_color_by_gradient(GREEN, PINK)
            .set_height(1.5)
        )
        text.move_to(rectangle.get_center())
        text.add_updater(lambda x: x.move_to(rectangle.get_center()))

        self.play(FadeIn(rectangle))
        self.play(Write(text))

        self.play(rectangle.animate.shift(RIGHT * 1.5 + DOWN * 5), run_time=6)
        self.wait()

        text.clear_updaters()
        self.play(rectangle.animate.shift(LEFT * 2 + UP), run_time=2)
        self.wait()


class Tree(Scene):
    def construct(self):
        val = ValueTracker(0.5)

        circle = always_redraw(
            lambda: Circle(radius=val.get_value(), stroke_color=YELLOW, stroke_width=5)
        )

        line_radius = always_redraw(
            lambda: Line(
                start=circle.get_center(),
                end=circle.get_bottom(),
                stroke_color=RED_B,
                stroke_width=10,
            )
        )

        line_circumfrence = always_redraw(
            lambda: Line(stroke_color=YELLOW, stroke_width=5)
            .set_length(2 * val.get_value() * PI)
            .next_to(circle, DOWN, buff=0.2)
        )

        triangle = always_redraw(
            lambda: Polygon(
                circle.get_top(),
                circle.get_left(),
                circle.get_right(),
                fill_color=GREEN_C,
            )
        )

        self.play(
            LaggedStart(
                Create(circle),
                DrawBorderThenFill(line_radius),
                DrawBorderThenFill(triangle),
                run_time=4,
                lag_ratio=0.75,
            )
        )

        self.play(ReplacementTransform(circle.copy(), line_circumfrence), run_time=2)
        self.play(val.animate.set_value(2), run_time=5)
        self.wait()


class GraphingMovement(Scene):
    def construct(self):
        axes = Axes(
            x_range=[0, 5, 1],
            y_range=[0, 3, 1],
            x_length=5,
            y_length=3,
            axis_config={"include_tip": True, "numbers_to_exclude": [0]},
        ).add_coordinates()

        axes.to_edge(UR)
        axis_labels = axes.get_axis_labels(x_label="x", y_label="f(x)")

        graph = axes.plot(lambda x: x**0.5, x_range=[0, 4], color=YELLOW)
        graphing_all = VGroup(axes, graph, axis_labels)

        self.play(DrawBorderThenFill(axes), Write(axis_labels))
        self.play(Create(graph))
        self.play(graphing_all.animate.shift(DOWN * 4))
        self.play(axes.animate.shift(LEFT * 3), run_time=3)


class GraphingFunction(Scene):
    def construct(self):
        plane = NumberPlane(x_range=[-6, 6], x_length=5, y_range=[-10, 10], y_length=5)
        plane.add_coordinates()

        function = plane.plot(
            lambda x: 0.1 * x * (x - 5) * (x + 5), x_range=[-6, 6], color=GREEN_B
        )

        area = plane.get_area(graph=function, x_range=[-5, 5], color=[BLUE, YELLOW])
        label = MathTex("f(x) = 0.1x(x-5)(x-5)").next_to(plane, UP, buff=0.2)

        horizontal = Line(
            start=plane.c2p(0, function.underlying_function(-2)),
            end=plane.c2p(-2, function.underlying_function(-2)),
            stroke_color=YELLOW,
            stroke_width=3,
        )

        self.play(DrawBorderThenFill(plane))
        self.play(Create(function), Write(label))
        self.play(FadeIn(area))
        self.play(Create(horizontal))


class CoordinateSystem(Scene):
    def construct(self):
        plane = NumberPlane(
            x_range=[-4, 4, 1], x_length=4, y_range=[0, 20, 5], y_length=4
        ).add_coordinates()
        plane.shift(LEFT * 3 + DOWN * 1.5)

        graph = plane.plot(lambda x: x**2, x_range=[-4, 4], color=GREEN)
        area = plane.get_riemann_rectangles(graph=graph, x_range=[-2, 2], dx=0.05)

        axes = Axes(
            x_range=[-4, 4, 1], x_length=4, y_range=[-20, 20, 5], y_length=4
        ).add_coordinates()
        axes.shift(RIGHT * 3 + DOWN * 1.5)

        axes_graph = axes.plot(lambda x: 2 * x, x_range=[-4, 4], color=YELLOW)
        v_lines = axes.get_vertical_lines_to_graph(
            graph=axes_graph, x_range=[-3, 3], num_lines=12
        )

        self.play(Write(plane), Create(axes))
        self.play(Create(graph), Create(axes_graph), run_time=2)
        self.add(area, v_lines)


class GraphingPolar(Scene):
    def construct(self):
        value = ValueTracker(0.01)

        plane = PolarPlane(radius_max=3).add_coordinates()
        plane.shift(LEFT * 2)

        graph1 = always_redraw(
            lambda: ParametricFunction(
                lambda t: plane.polar_to_point(2 * np.sin(3 * t), t),
                t_range=[0, value.get_value()],
                color=GREEN,
            )
        )
        dot1 = always_redraw(
            lambda: Dot(fill_color=GREEN, fill_opacity=0.8)
            .scale(0.5)
            .move_to(graph1.get_end())
        )

        axes = Axes(
            x_range=[0, 4, 1], x_length=3, y_range=[-3, 3, 1], y_length=3
        ).shift(RIGHT * 4)
        axes.add_coordinates()

        graph2 = always_redraw(
            lambda: axes.plot(
                lambda x: 2 * np.sin(3 * x), x_range=[0, value.get_value()], color=GREEN
            )
        )
        dot2 = always_redraw(
            lambda: Dot(fill_color=GREEN, fill_opacity=0.8)
            .scale(0.5)
            .move_to(graph2.get_end())
        )

        title = MathTex("f(\\theta) = 2sin(3\\theta)", color=GREEN).next_to(
            axes, UP, buff=0.2
        )

        self.play(
            LaggedStart(
                Write(plane), Create(axes), Write(title), run_time=3, lag_ratio=0.5
            )
        )
        self.add(graph1, graph2, dot1, dot2)
        self.play(value.animate.set_value(PI), run_time = 10, rate_func = linear)
        self.wait()

class Vectors(VectorScene):
    def construct(self):
        plane = self.add_plane(animate = True).add_coordinates()
        vector = self.add_vector([-3, 2], color = YELLOW)
        
        basis = self.get_basis_vectors()
        self.add(basis)
        
        self.vector_to_coords(vector = vector)
        
        vector2 = self.add_vector([2, 2])
        self.write_vector_coordinates(vector = vector2)