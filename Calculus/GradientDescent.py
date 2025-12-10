from manim import *

# 4K vertical resolution
config.pixel_width = 2160
config.pixel_height = 3840
config.frame_width = 9
config.frame_height = 16


class GradientDescent(Scene):
    def construct(self):
        # Data points: (Area in sq ft, Price in $)
        data = [
            (500, 150000),
            (800, 200000),
            (1000, 250000),
            (1200, 300000),
            (1500, 350000),
            (1800, 420000),
            (2000, 480000),
        ]

        # Cost function: Sum of squared errors
        def calculate_cost(m):
            total_error = 0
            for area, price in data:
                predicted = m * area
                total_error += (price - predicted) ** 2
            return total_error

        # Top graph axes for House Price vs Area
        ax_top = Axes(
            x_range=[0, 2500, 500],
            y_range=[0, 600000, 100000],
            x_length=6,
            y_length=5,
            axis_config={"include_tip": False},
        ).shift(UP * 4)

        # Top axis labels
        x_label_top = Text("Area (sq ft)").scale(0.5).next_to(ax_top.x_axis, DOWN)
        y_label_top = (
            Text("Price ($)")
            .scale(0.5)
            .rotate(90 * DEGREES)
            .next_to(ax_top.y_axis, LEFT, buff=0.3)
        )

        # Data point dots
        dots = VGroup()
        for area, price in data:
            dot = Dot(point=ax_top.c2p(area, price), color=WHITE, radius=0.1)
            dots.add(dot)

        # Bottom graph axes for Cost Function
        ax_bottom = Axes(
            x_range=[40, 440, 100],
            y_range=[0, 5e11, 1e11],
            x_length=6,
            y_length=5,
            axis_config={"include_tip": False},
        ).shift(DOWN * 4)

        # Bottom axis labels
        x_label_bottom = Text("Slope").scale(0.5).next_to(ax_bottom.x_axis, DOWN)
        y_label_bottom = (
            Text("Amount of Error (Cost)")
            .scale(0.5)
            .rotate(90 * DEGREES)
            .next_to(ax_bottom.y_axis, LEFT, buff=0.3)
        )

        # Cost function curve (parabola)
        cost_curve = ax_bottom.plot(
            calculate_cost, x_range=[60, 420], color=BLUE, stroke_width=4
        )

        # Slope tracker for the best fit slope
        slope = ValueTracker(240)  # Best fit slope

        # Dynamic regression line
        def get_regression_line():
            m = slope.get_value()
            start = ax_top.c2p(0, 0)
            end = ax_top.c2p(2250, m * 2250)
            line = Line(start, end, color=YELLOW, stroke_width=4)
            return line

        regression_line = always_redraw(get_regression_line)

        # Dynamic slope label
        def get_slope_label():
            m = slope.get_value()
            label = Text(f"Slope = {int(m)}", color=YELLOW).scale(0.5)
            label.move_to(ax_top.c2p(2000, 80000))
            return label

        slope_label = always_redraw(get_slope_label)

        # Dynamic error lines
        def get_error_lines():
            m = slope.get_value()
            lines = VGroup()
            for area, price in data:
                predicted_price = m * area
                line = Line(
                    ax_top.c2p(area, price),
                    ax_top.c2p(area, predicted_price),
                    color=RED,
                    stroke_width=4,
                )
                lines.add(line)
            return lines

        error_lines = always_redraw(get_error_lines)

        # Dynamic dot on cost curve
        def get_cost_dot():
            m = slope.get_value()
            cost = calculate_cost(m)
            dot = Dot(color=RED, radius=0.15)
            dot.move_to(ax_bottom.c2p(m, cost))
            return dot

        cost_dot = always_redraw(get_cost_dot)

        # Draw axes and labels for top graph
        self.play(Create(ax_top), run_time=1)
        self.play(Write(x_label_top), Write(y_label_top), run_time=1)

        # Draw axes and labels for bottom graph
        self.play(Create(ax_bottom), run_time=1)
        self.play(Write(x_label_bottom), Write(y_label_bottom), run_time=1)

        # Draw the cost curve
        self.play(Create(cost_curve), run_time=1.5)

        # Add data points one by one
        self.wait(0.3)
        for dot in dots:
            self.play(FadeIn(dot, scale=0.5), run_time=0.2)

        self.wait(0.5)

        # Draw the best fit regression line
        self.play(Create(regression_line), run_time=1.5)

        # Show slope label
        self.play(Write(slope_label), run_time=0.8)

        self.wait(0.5)

        # Show error lines and cost dot on the cost curve
        self.play(Create(error_lines), FadeIn(cost_dot, scale=0.5), run_time=1)
        self.wait(0.5)

        # Move regression line up and down to show errors changing
        self.play(slope.animate.set_value(320), run_time=2)
        self.play(slope.animate.set_value(150), run_time=2)
        self.play(slope.animate.set_value(240), run_time=2)

        self.wait(2)
