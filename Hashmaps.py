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

        # Create indices
        self.indices = VGroup()
        for index in range(4):
            index_text = Text(f"Index", font_size=25, color=GRAY_C)
            number = MathTex(f"{index}", font_size=40, color=BLUE)
            group = VGroup(index_text, number).arrange(
                RIGHT, aligned_edge=DOWN, center=False, buff=0.2
            )
            self.indices.add(group)

        # Arrange the indices
        self.indices.arrange(DOWN, aligned_edge=LEFT, buff=0.4)

        # Create the buckets
        self.buckets = VGroup()
        for index in range(4):
            colon = Text(":", font_size=25)
            array = Text("[]", font_size=25)
            bucket = VGroup(colon, array).arrange(RIGHT, buff=0.2)
            bucket[1].shift(UP * 0.06)
            self.buckets.add(bucket)

        # Arrange the buckets
        self.buckets.arrange(DOWN, aligned_edge=LEFT, buff=0.37).next_to(
            self.indices, RIGHT, aligned_edge=DOWN
        )

        # Add braces to look like hashmap
        self.leftBrace = Brace(self.indices, LEFT, sharpness=1)
        self.rightBrace = Brace(self.buckets, RIGHT, sharpness=1)
        self.hashmap = VGroup(
            self.indices, self.buckets, self.leftBrace, self.rightBrace
        ).shift(LEFT * 4 + (UP * 0.5))

        # Adding hashmap title
        self.hashmapTitle = Text("Hashmap", font_size=25).next_to(
            self.hashmap, DOWN, buff=0.4
        )

        # Creating key-value pair
        size = 25

        insertText = Text("Key-Value Pair:", font_size=size)
        keyVal = Text(
            '["StudyDSA"] = 100',
            font_size=size,
            t2c={
                "[0:1]": "GRAY",
                "[1:11]": "GREEN",
                "[11:12]": "GRAY",
                "[15:]": "ORANGE",
            },
        )
        self.keyValuePair = (
            VGroup(insertText, keyVal)
            .arrange(RIGHT, buff=0.2)
            .shift(UP * 1.5 + RIGHT * 2.5)
        )

        mathSize = 40
        hashFunction = Text("Hash Function: ", font_size=size)
        function = MathTex(
            "f(key) = index",
            font_size=mathSize,
            tex_to_color_map={"key": GREEN, "index": BLUE},
        )

        self.hashFunction = (
            VGroup(hashFunction, function)
            .arrange(RIGHT, buff=0.1)
            .next_to(self.keyValuePair, DOWN, buff=0.5, aligned_edge=LEFT)
        )

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
        self.add(self.hashmapTitle)
        self.add(self.keyValuePair)

        self.add(self.hashFunction)
