from manim import Circle, Text, MathTex, VGroup, WHITE, UP

class ListNode:
    """
    A class to create and display a list node in Manim.

    Attributes
    ----------
    label : str
        The label text for the node.
    value : str
        The value inside the node.
    radius : float
        The radius of the node circle.
    color : str
        The color of the node circle.
    label_color : str
        The color of the label text.
    label_font_size : int
        The font size of the label text.
    value_color : str
        The color of the value text.
    value_font_size : int
        The font size of the value text.

    Methods
    -------
    create() -> VGroup
        Creates the visual representation of the list node.

    Examples
    --------
    Basic usage:

    >>> node = ListNode(label="Node 1", value="10")
    >>> node.create()

    Custom colors and sizes:

    >>> node = ListNode(
    ...     label="Node 1",
    ...     value="10",
    ...     radius=1.5,
    ...     color=WHITE,
    ...     label_color=WHITE,
    ...     label_font_size=40,
    ...     value_color=WHITE,
    ...     value_font_size=70
    ... )
    >>> node.create()
    """

    def __init__(
        self,
        value: str,
        label: str = "",
        radius: float = 1.25,
        color: str = WHITE,
        label_color: str = WHITE,
        label_font_size: int = 35,
        value_color: str = WHITE,
        value_font_size: int = 60,
    ):
        """
        Initializes the ListNode object with specified parameters.

        Parameters
        ----------
        label : str
            The label text for the node.
        value : str
            The value inside the node.
        radius : float, optional
            The radius of the node circle. Defaults to 1.25.
        color : str, optional
            The color of the node circle. Defaults to WHITE.
        label_color : str, optional
            The color of the label text. Defaults to WHITE.
        label_font_size : int, optional
            The font size of the label text. Defaults to 35.
        value_color : str, optional
            The color of the value text. Defaults to WHITE.
        value_font_size : int, optional
            The font size of the value text. Defaults to 60.
        """
        self.node = Circle(color=color, radius=radius)
        self.node_label = Text(label, color=label_color, font_size=label_font_size)
        self.node_value = MathTex(value, color=value_color, font_size=value_font_size)

        self.node_label.next_to(self.node, UP)
        self.node_value.move_to(self.node.get_center())

    def create(self) -> VGroup:
        """
        Creates the visual representation of the list node.

        Returns
        -------
        VGroup
            A Manim VGroup containing the node, label, and value.
        """
        return VGroup(self.node, self.node_label, self.node_value)
