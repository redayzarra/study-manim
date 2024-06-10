import random
from manim import VGroup, Text, RIGHT, DOWN, WHITE


class Array:
    def __init__(
        self, array_len=None, font_size=24, seed=None, array=None, indexColor=WHITE
    ):
        self.array_len = array_len or len(array)
        self.font_size = font_size
        self.seed = seed
        self.array = array or self.generate_random_array()
        self.index_color = indexColor

    def generate_random_array(self):
        if self.seed is not None:
            random.seed(self.seed)
        return [random.randint(0, 10) for _ in range(self.array_len)]

    def create_indices(self):
        return VGroup(
            *[
                Text(f"{index}", font_size=self.font_size, color=self.index_color)
                for index in range(self.array_len)
            ]
        )

    def create_array_elements(self):
        return VGroup(
            *[Text(str(value), font_size=self.font_size) for value in self.array]
        )

    def construct_array(self):
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
