from manim import *

# 4K vertical resolution
config.pixel_width = 2160
config.pixel_height = 3840
config.frame_width = 9
config.frame_height = 16

class GradientDescent(Scene):
    def construct(self):
        data = [
            (500, 150000),
            (800, 200000),
            (1000, 250000),
            (1200, 300000),
            (1500, 350000),
            (1800, 420000),
            (2000, 480000),
        ]

        def calculate_cost(m):
            total_error = 0
            for area, price in data:
                predicted = m * area
                total_error += (price - predicted) ** 2
            return total_error

        # Scale cost function to fit in same coordinate system as top graph
        min_cost = calculate_cost(240)
        max_cost = max(calculate_cost(150), calculate_cost(320))

        def scaled_cost(slope_val):
            x = 500 + (slope_val - 150) * (2000 - 500) / (320 - 150)
            cost = calculate_cost(slope_val)
            y = 50000 + ((cost - min_cost) / (max_cost - min_cost)) * 450000
            return x, y

        # Top graph: House Price vs Area
        ax_top = Axes(
            x_range=[0, 2500, 500],
            y_range=[0, 600000, 100000],
            x_length=6,
            y_length=5,
            axis_config={"include_tip": True, "tip_length": 0.15},
        ).shift(UP * 4)

        top_x_label = Text("Area (sq ft)", font_size=28).next_to(
            ax_top.x_axis, DOWN, buff=0.3
        )
        top_y_label = (
            Text("Price ($)", font_size=28)
            .rotate(90 * DEGREES)
            .next_to(ax_top.y_axis, LEFT, buff=0.3)
        )
        top_labels = VGroup(top_x_label, top_y_label)

        dots = VGroup()
        for area, price in data:
            dot = Dot(point=ax_top.c2p(area, price), color=WHITE, radius=0.1)
            dots.add(dot)
        dots.set_z_index(2)

        # Bottom graph: Cost Function (MSE)
        ax_bottom = Axes(
            x_range=[0, 2500, 500],
            y_range=[0, 600000, 100000],
            x_length=6,
            y_length=5,
            axis_config={"include_tip": True, "tip_length": 0.15},
        ).shift(DOWN * 4)

        bottom_x_label = Text("Slope (m)", font_size=28).next_to(
            ax_bottom.x_axis, DOWN, buff=0.3
        )
        bottom_y_label = (
            Text("Cost (MSE)", font_size=28)
            .rotate(90 * DEGREES)
            .next_to(ax_bottom.y_axis, LEFT, buff=0.3)
        )
        bottom_labels = VGroup(bottom_x_label, bottom_y_label)

        def cost_curve_function(x):
            slope_val = 150 + (x - 500) * (320 - 150) / (2000 - 500)
            _, y = scaled_cost(slope_val)
            return y

        x_start = 500 + (140 - 150) * (2000 - 500) / (320 - 150)
        x_end = 500 + (340 - 150) * (2000 - 500) / (320 - 150)

        cost_curve = ax_bottom.plot(
            cost_curve_function, x_range=[x_start, x_end], color=GREEN, stroke_width=4
        )
        cost_curve.set_z_index(1)

        slope = ValueTracker(240)

        def get_regression_line():
            m = slope.get_value()
            start = ax_top.c2p(0, 0)
            end = ax_top.c2p(2250, m * 2250)
            return Line(start, end, color=YELLOW, stroke_width=4)

        regression_line = always_redraw(get_regression_line)

        def get_slope_label():
            m = slope.get_value()
            label = Text(f"Slope = {int(m)}", color=YELLOW).scale(0.6)
            label.move_to(ORIGIN)
            return label

        slope_label = always_redraw(get_slope_label)

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
            lines.set_z_index(1)
            return lines

        error_lines = always_redraw(get_error_lines)

        def get_cost_dot():
            m = slope.get_value()
            x, y = scaled_cost(m)
            dot = Dot(color=RED, radius=0.1)
            dot.move_to(ax_bottom.c2p(x, y))
            dot.set_z_index(2)
            return dot

        cost_dot = always_redraw(get_cost_dot)

        # Animation sequence
        self.play(
            LaggedStart(
                DrawBorderThenFill(ax_top),
                Write(top_labels),
                run_time=2,
                lag_ratio=0.5,
            )
        )

        self.play(
            LaggedStart(
                DrawBorderThenFill(ax_bottom),
                Write(bottom_labels),
                run_time=2,
                lag_ratio=0.5,
            )
        )

        self.wait(0.3)
        for dot in dots:
            self.play(FadeIn(dot, scale=0.5), run_time=0.2)

        self.wait(0.5)
        self.play(Create(regression_line), run_time=1.5)
        self.play(Write(slope_label), run_time=0.8)
        self.wait(0.5)

        self.play(Create(error_lines), FadeIn(cost_dot, scale=0.5), run_time=1)
        self.wait(0.5)

        self.play(slope.animate.set_value(320), run_time=2)
        self.wait(0.3)
        x_high, y_high = scaled_cost(320)
        dot_high = Dot(ax_bottom.c2p(x_high, y_high), color=RED, radius=0.1)
        dot_high.set_z_index(2)
        self.add(dot_high)
        self.wait(0.5)

        self.play(slope.animate.set_value(150), run_time=2)
        self.wait(0.3)
        x_low, y_low = scaled_cost(150)
        dot_low = Dot(ax_bottom.c2p(x_low, y_low), color=RED, radius=0.1)
        dot_low.set_z_index(2)
        self.add(dot_low)
        self.wait(0.3)

        self.play(slope.animate.set_value(320), run_time=1.5)
        self.play(slope.animate.set_value(150), run_time=1.5)
        self.play(slope.animate.set_value(300), run_time=1.2)
        self.play(slope.animate.set_value(180), run_time=1.2)
        self.play(slope.animate.set_value(240), run_time=1)
        self.wait(0.5)

        self.play(Create(cost_curve), run_time=1.5)
        self.wait(2)
