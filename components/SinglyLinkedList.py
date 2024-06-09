from manim import Circle, Text, MathTex, VGroup, WHITE, UP

class SinglyListNode:
    def __init__(
        self,
        label: str,
        value: str,
        radius=1.25,
        color=WHITE,  # Color of the node
        label_color=WHITE,  # Label color
        value_color=WHITE,  # Inner value color
    ):
        # Rendering the node itself
        self.node = Circle(color=color, radius=radius)
        self.node_label = Text(label, color=label_color).scale(0.75)
        self.node_value = MathTex(value, color=value_color).scale(1.5)

        # Position label and value
        self.node_label.next_to(self.node, UP)
        self.node_value.move_to(self.node.get_center())

    def create(self):
        return VGroup(self.node, self.node_label, self.node_value)
