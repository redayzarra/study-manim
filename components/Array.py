import random
from typing import List, Optional, Tuple
from manim import VGroup, Text, RIGHT, DOWN, WHITE

class Array:
    """
    A class to create and display arrays in Manim.

    Attributes:
        array_len (int): Length of the array.
        element_size (int): Font size for array elements.
        indices_size (int): Font size for indices.
        seed (Optional[int]): Seed for random number generation.
        array (Optional[List[int]]): Custom array elements.
        index_color (str): Color for the indices text.
    """

    def __init__(
        self,
        array_len: Optional[int] = None,
        element_size: int = 24,
        indices_size: int = 24,
        seed: Optional[int] = None,
        array: Optional[List[int]] = None,
        index_color: str = WHITE,
    ):
        """
        Initializes the Array object with optional parameters.

        Args:
            array_len (Optional[int]): Length of the array.
            element_size (int): Font size for array elements.
            indices_size (int): Font size for indices.
            seed (Optional[int]): Seed for random number generation.
            array (Optional[List[int]]): Custom array elements.
            index_color (str): Color for the indices text.
        """
        self.array_len = array_len or (len(array) if array else 0)
        self.element_size = element_size
        self.indices_size = indices_size
        self.seed = seed
        self.array = array or self.generate_random_array()
        self.index_color = index_color

    def generate_random_array(self) -> List[int]:
        """
        Generates a random array based on the length and seed.

        Returns:
            List[int]: Randomly generated array.
        """
        if self.seed is not None:
            random.seed(self.seed)
        return [random.randint(0, 10) for _ in range(self.array_len)]

    def create_indices(self) -> VGroup:
        """
        Creates the indices for the array.

        Returns:
            VGroup: A Manim VGroup containing the indices text objects.
        """
        return VGroup(
            *[
                Text(f"{index}", font_size=self.indices_size, color=self.index_color)
                for index in range(self.array_len)
            ]
        )

    def create_array_elements(self) -> VGroup:
        """
        Creates the array elements.

        Returns:
            VGroup: A Manim VGroup containing the array elements text objects.
        """
        return VGroup(
            *[Text(str(value), font_size=self.element_size) for value in self.array]
        )

    def construct_array(self) -> Tuple[VGroup, VGroup, VGroup]:
        """
        Constructs the visual representation of the array.

        Returns:
            Tuple[VGroup, VGroup, VGroup]: A tuple containing the array group, 
                                           array elements, and indices.
        """
        indices = self.create_indices()
        array_elements = self.create_array_elements()
        array_elements.arrange(RIGHT, buff=0.8).scale(2)

        for index, element in zip(indices, array_elements):
            index.scale(0.9)
            index.next_to(element, DOWN, buff=0.6)

        open_bracket = Text("[").scale(2)
        close_bracket = Text("]").scale(2)
        array_group = VGroup(open_bracket, array_elements, close_bracket).arrange(
            RIGHT, buff=0.2
        )

        return array_group, array_elements, indices

