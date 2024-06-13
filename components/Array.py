import random
from typing import List, Optional
from manim import VGroup, Text, MathTex, RIGHT, DOWN, WHITE, GRAY_C

class Array:
    """
    A class to create and display arrays in Manim.

    Attributes
    ----------
    array_len : int
        Length of the array.
    element_size : int
        Font size for array elements.
    indices_size : int
        Font size for indices.
    line_spacing : float
        Spacing between array elements.
    element_spacing : float
        Spacing between indices and elements.
    seed : Optional[int]
        Seed for random number generation.
    array : Optional[List[int]]
        Custom array elements.
    element_color : str
        Color for the elements text.
    index_color : str
        Color for the indices text.

    Methods
    -------
    generate_random_array() -> List[int]
        Generates a random array based on the length and seed.
    create_indices() -> VGroup
        Creates the indices for the array.
    create_array_elements() -> VGroup
        Creates the array elements.
    create() -> VGroup
        Constructs the visual representation of the array.

    Examples
    --------
    Basic usage:

    >>> array = Array(array_len=5)
    >>> array.create()

    Custom array and attributes:

    >>> custom_array = [1, 2, 3, 4, 5]
    >>> array = Array(array=custom_array, element_size=48, indices_size=36, index_color=GRAY_C)
    >>> array.create()
    """

    def __init__(
        self,
        array_len: Optional[int] = None,
        element_size: int = 60,
        indices_size: int = 48,
        line_spacing: float = 0.5,
        element_spacing: float = 0.85,
        seed: Optional[int] = 5,
        array: Optional[List[int]] = None,
        element_color: str = WHITE,
        index_color: str = GRAY_C,
    ):
        """
        Initializes the Array object with optional parameters.

        Parameters
        ----------
        `array_len` : Optional[int]
            Length of the array. If None, it will be determined by the length of `array`.
        `element_size` : int
            Font size for array elements. Defaults to 60.
        `indices_size` : int
            Font size for indices. Defaults to 48.
        `line_spacing` : float, optional
            Spacing between array elements. Defaults to 0.5.
        `element_spacing` : float, optional
            Spacing between indices and elements. Defaults to 0.85.
        `seed` : Optional[int], optional
            Seed for random number generation. Defaults to 5.
        `array` : Optional[List[int]], optional
            Custom array elements. If None, a random array will be generated.
        `element_color` : str
            Color for the elements text. Defaults to WHITE.
        `index_color` : str
            Color for the indices text. Defaults to GRAY_C.
        """
        self.array_len = array_len or (len(array) if array else 0)
        self.element_size = element_size
        self.indices_size = indices_size
        self.line_spacing = line_spacing
        self.element_spacing = element_spacing
        self.seed = seed
        self.array = array or self.generate_random_array()
        self.element_color = element_color
        self.index_color = index_color

    def generate_random_array(self) -> List[int]:
        """
        Generates a random array based on the length and seed.

        Returns
        -------
        List[int]
            Randomly generated array.
        """
        random.seed(self.seed)
        return [random.randint(0, 10) for _ in range(self.array_len)]

    def create_indices(self) -> VGroup:
        """
        Creates the indices for the array.

        Returns
        -------
        VGroup
            A Manim VGroup containing the indices text objects.
        """
        return VGroup(
            *[
                MathTex(f"{index}", font_size=self.indices_size, color=self.index_color)
                for index in range(self.array_len)
            ]
        )

    def create_array_elements(self) -> VGroup:
        """
        Creates the array elements.

        Returns
        -------
        VGroup
            A Manim VGroup containing the array elements text objects.
        """
        return VGroup(
            *[MathTex(str(value), font_size=self.element_size, color=self.element_color) for value in self.array]
        )

    def create(self) -> VGroup:
        """
        Constructs the visual representation of the array.

        Returns
        -------
        VGroup
            A VGroup containing the array elements, brackets, and indices.
        """
        array_elements = self.create_array_elements()
        array_elements.arrange(RIGHT, buff=self.element_spacing)

        indices = self.create_indices()
        for index, element in zip(indices, array_elements):
            index.next_to(element, DOWN, buff=self.line_spacing)

        open_bracket = Text("[")
        close_bracket = Text("]")
        array = VGroup(open_bracket, array_elements, close_bracket).arrange(
            RIGHT, buff=0.2
        )

        return VGroup(array, indices)

