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
        self.buckets = VGroup()
        for index in range(5):
            index_text = Text(f"Index", font_size=25, color=GRAY_C)
            number = MathTex(f"{index}", font_size=40, color=GREEN)
            array = Text(": []", font_size=25)
            bucket = VGroup(index_text, number, array).arrange(
                RIGHT, aligned_edge=DOWN, center=False, buff=0.2
            )
            self.buckets.add(bucket)

        # Arrange the buckets
        self.buckets.arrange(DOWN, aligned_edge=LEFT, buff=0.2)

        # Add braces to look like hashmap
        self.leftBrace = Brace(self.buckets, LEFT, sharpness=1, buff=0.3)
        self.rightBrace = Brace(self.buckets, RIGHT, sharpness=1, buff=0.3)
        self.hashmap = VGroup(self.buckets, self.leftBrace, self.rightBrace)
        
        self.hashmapTitle = Text("Hashmap", font_size=35).next_to(self.hashmap, DOWN, buff=0.4)

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

        self.add(self.hashmap)
        self.play(Write(self.hashmapTitle))

        self.wait(3)