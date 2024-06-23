from manim import *
from components.Hashmap import Hashmap
from components.Steps import Steps
from components.watermark import create_watermark


class HashFunction(Scene):
    def construct(self):
        self.showTitle = True
        self.construction()
        self.animate_scene()

    def construction(self):
        """
        Define and position the elements of the scene.
        """
        # Adding title for LinkedIn post
        self.title = Text("Hash Function").to_edge(UP, buff=0.5)

        # Adding educational steps
        steps = [
            "Input the key into hash function",
            "Compute the hash value",
            "Use hash value to determine the index in the hashmap",
        ]
        self.steps = Steps(steps).create()

        # Create hashmap
        hashmap = {"Hello": 1, "World": 2, "StudyDSA": 3}

        self.pairs = VGroup()
        for key, value in hashmap.items():
            key_text = Text(f"{key}:", font_size=25)
            value_text = MathTex(value)
            pair = VGroup(key_text, value_text).arrange(RIGHT, center = False, aligned_edge=DOWN)
            self.pairs.add(pair)
        
        self.pairs.arrange(UP, buff=0.5)

    def animate_scene(self):
        """
        Add elements to the scene and animate them.
        """
        # Add watermark
        watermark = create_watermark()
        self.add(watermark)

        # Conditionally add title
        if self.showTitle:
            self.add(self.title)

        self.add(self.steps)

        self.add(self.pairs)