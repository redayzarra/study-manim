from manim import Circle, Text, MathTex, VGroup, WHITE, UP

class ListNode:
    """
    A class to create and display a list node in Manim.

    Attributes:
        label (str): The label text for the node.
        value (str): The value inside the node.
        radius (float): The radius of the node circle.
        color (str): The color of the node circle.
        label_color (str): The color of the label text.
        value_color (str): The color of the value text.
    """

    def __init__(
        self,
        label: str,
        value: str,
        radius: float = 1.25,
        color: str = WHITE,
        label_color: str = WHITE,
        value_color: str = WHITE,
    ):
        """
        Initializes the ListNode object with specified parameters.

        Args:
            label (str): The label text for the node.
            value (str): The value inside the node.
            radius (float, optional): The radius of the node circle. Defaults to 1.25.
            color (str, optional): The color of the node circle. Defaults to WHITE.
            label_color (str, optional): The color of the label text. Defaults to WHITE.
            value_color (str, optional): The color of the value text. Defaults to WHITE.
        """
        self.node = Circle(color=color, radius=radius)
        self.node_label = Text(label, color=label_color).scale(0.75)
        self.node_value = MathTex(value, color=value_color).scale(1.5)

        self.node_label.next_to(self.node, UP)
        self.node_value.move_to(self.node.get_center())

    def create(self) -> VGroup:
        """
        Creates the visual representation of the list node.

        Returns:
            VGroup: A Manim VGroup containing the node, label, and value.
        """
        return VGroup(self.node, self.node_label, self.node_value)

