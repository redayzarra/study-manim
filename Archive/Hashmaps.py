from manim import *
from components.Hashmap import Hashmap
from components.Steps import Steps
from components.watermark import create_watermark


class HashFunction(Scene):
    def construct(self):
        self.show_title = False
        self.construction()
        self.animate_scene()

    def construction(self):
        """
        Define and position the elements of the scene.
        """
        # Title for LinkedIn post
        self.title = Text("Hash Function").to_edge(UP, buff=0.5)

        # Educational steps
        steps_list = [
            "Input the key into hash function",
            "Compute the hash value",
            "Use hash value to store key-value pair at index",
        ]
        self.steps = Steps(steps_list).create()

        # Create indices
        self.indices = VGroup(
            *[
                VGroup(
                    Text("Index", font_size=25, color=GRAY_C),
                    MathTex(f"{i}", font_size=40, color=BLUE),
                ).arrange(RIGHT, aligned_edge=DOWN, buff=0.2)
                for i in range(4)
            ]
        ).arrange(DOWN, aligned_edge=LEFT, buff=0.4)

        # Create the buckets
        self.buckets = (
            VGroup(
                *[
                    VGroup(
                        Text(":", font_size=25),
                        Text("[]", font_size=25).shift(UP * 0.06),
                    ).arrange(RIGHT, buff=0.2)
                    for _ in range(4)
                ]
            )
            .arrange(DOWN, aligned_edge=LEFT, buff=0.37)
            .next_to(self.indices, RIGHT, aligned_edge=DOWN)
        )

        # Add braces to look like hashmap
        self.hashmap = VGroup(
            self.indices,
            self.buckets,
            Brace(self.indices, LEFT, sharpness=1),
            Brace(self.buckets, RIGHT, sharpness=1),
        ).shift(LEFT * 4 + UP * 0.5)

        # Hashmap title
        self.hashmap_title = Text("Hashmap", font_size=25).next_to(
            self.hashmap, DOWN, buff=0.4
        )

        # Key-value pair
        self.key_value_pair = (
            VGroup(
                Text("Key-Value Pair:", font_size=25),
                Text(
                    '["StudyDSA"] = 100',
                    font_size=25,
                    t2c={
                        "[0:1]": "GRAY",
                        "[1:11]": "GREEN",
                        "[11:12]": "GRAY",
                        "[15:]": "ORANGE",
                    },
                ),
            )
            .arrange(RIGHT, buff=0.2)
            .shift(UP * 1.5 + RIGHT * 2)
        )

        # Hash function representation
        self.hash_function = (
            VGroup(
                Text("Hash Function: ", font_size=25),
                MathTex(
                    "f(key) = index",
                    font_size=40,
                    tex_to_color_map={"key": GREEN, "index": BLUE},
                ),
            )
            .arrange(RIGHT, buff=0.1)
            .next_to(self.key_value_pair, DOWN, buff=0.5, aligned_edge=LEFT)
        )

    def animate_scene(self):
        """
        Add elements to the scene and animate them.
        """
        # Add watermark
        watermark = create_watermark()
        self.add(watermark)

        # Conditionally add title
        if self.show_title:
            self.add(self.title)

        self.add(self.hashmap)
        self.add(self.hashmap_title)
        self.add(self.key_value_pair)
        self.add(self.hash_function)

        # Get the part of the MathTex corresponding to "key"
        key_part = self.hash_function[1].get_part_by_tex("key")

        # Create a Text object to transform into
        target_key = (
            Text('"StudyDSA"', font_size=25, color=GREEN)
            .move_to(key_part.get_center())
            .shift(RIGHT * 0.6)
        )

        # Transform the key part into the Text object
        self.play(
            Transform(key_part, target_key),
            self.hash_function[1][2:]
            .animate.move_to(target_key.get_center())
            .shift(RIGHT * 1.8),
            Write(self.steps[0], run_time=1.5),
        )
        self.wait()

        two = (
            MathTex("2", font_size=40, color=BLUE)
            .next_to(self.hash_function[1][-1].get_center())
            .shift(LEFT * 0.75)
        )

        self.play(
            Transform(self.hash_function[1][-1], two),
            Write(self.steps[1], run_time=1.5),
        )
        self.wait()

        self.play(
            Indicate(self.indices[2][-1], scale_factor=1.5, color=YELLOW),
            Indicate(self.hash_function[1][-1], scale_factor=1.5, color=YELLOW),
        )

        # Create a new group containing copies of self.indices[2] and self.buckets[2]
        index_two_copy = self.indices[2].copy()
        bucket_two_copy = self.buckets[2].copy()
        new_group = (
            VGroup(index_two_copy, bucket_two_copy)
            .arrange(RIGHT, buff=0.2)
            .next_to(self.hash_function, DOWN, buff=0.5, aligned_edge=LEFT)
        )

        # Animate the transformation from the original objects to the new group
        self.play(Transform(VGroup(self.indices[2], self.buckets[2]), new_group))

        self.wait()

        text = Text(
            '("StudyDSA", 100)',
            font_size=25,
            t2c={
                "[0:1]": "GRAY",
                "[1:11]": "GREEN",
                "[11:12]": "GRAY",
                "[13:16]": "ORANGE",
                "[16:]": "GRAY",
            },
        ).next_to(self.buckets[2][1][0], RIGHT, buff=0.1)

        self.play(
            self.buckets[2][1][1].animate.next_to(text, RIGHT, buff=0.1),
            Write(text),
            Write(self.steps[2]),
        )
        self.wait()
