from manim import VGroup, Text, MathTex, UP, DOWN, RIGHT, LEFT, DL
from typing import List

class Steps:
    """
    A class to create and display steps in Manim.

    Attributes:
        step_texts (List[str]): Array of strings representing the steps.
        font_size (int): Font size for the steps.
        step_size (int): Font size for the step numbers.
        line_spacing (float): Buffer between the steps.
        scale (float): Scale factor for the steps.
    """

    def __init__(
        self,
        step_texts: List[str],
        font_size: int = 24,
        step_size: int = 34,
        line_spacing: float = 0.4,
    ):
        """
        Initializes the Steps object with specified parameters.

        Args:
            step_texts (List[str]): Array of strings representing the steps.
            font_size (int, optional): Font size for the steps. Defaults to 24.
            step_size (int, optional): Font size for the step numbers. Defaults to 30.
            line_spacing (float, optional): Buffer between the steps. Defaults to 0.4.
        """
        self.step_texts = step_texts
        self.font_size = font_size
        self.step_size = step_size
        self.line_spacing = line_spacing
        self.steps = self.create_steps()

    def create_steps(self) -> VGroup:
        """
        Creates a VGroup of steps from the array of strings.

        Returns:
            VGroup: A Manim VGroup containing the steps.
        """
        steps = VGroup()
        for i, step in enumerate(self.step_texts):
            step_number = MathTex(f"{i + 1}.", font_size=self.step_size)
            step_text = Text(step, font_size=self.font_size)
            step_group = VGroup(step_number, step_text).arrange(RIGHT, buff=0.2)
            steps.add(step_group)
        
        steps.arrange(DOWN, center=False, aligned_edge=LEFT, buff=self.line_spacing)
        steps.to_corner(DL)
        
        return steps

