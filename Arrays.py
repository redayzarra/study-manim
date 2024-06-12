from manim import *
from components.watermark import create_watermark
from components.Array import Array


class ArrayPointers(Scene):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.nums = [1, 2, 3, 4, 5, 6]
        self.array_len = len(self.nums)
        self.random_seed = 1

    def construct(self):
        self.showTitle = False
        self.setup_scene()
        self.animate_scene()

    def setup_scene(self):
        """
        Define and position the elements of the scene.
        """
        # Adding title for LinkedIn post
        self.title = Text("Two Pointers").to_edge(UP, buff=0.5)

        array_viz = Array(
            array=self.nums,
            indices_size=30,
            seed=self.random_seed,
            index_color=GRAY_C,
        )

        self.array, self.array_elements, self.indices = array_viz.construct_array()

        self.left = self.create_pointer("Left", BLUE)
        self.left[1].shift(UP * 0.1)
        self.left.next_to(self.array_elements[0], UP, buff=0.3)

        self.right = self.create_pointer("Right", ORANGE)
        self.right.next_to(self.array_elements[-1], UP, buff=0.3)

        # Adding educational steps
        step1 = Text("1. Swap elements at pointers")
        step2 = Text("2. Move the left and right pointers")

        # Step 2: Group the text objects
        self.steps = VGroup(step1, step2).arrange(DOWN, buff=0.4)

        # Step 3: Align each text object to the left
        for step in self.steps:
            step.align_to(self.steps, LEFT)

        # Optional: Scaling and shifting
        self.steps.scale(0.5).to_corner(DL)

    def create_pointer(self, label, color):
        """
        Create a pointer with a given label and color.
        """
        arrow = Arrow(start=UP, end=DOWN, buff=0.2, color=color).scale(0.8)
        text = Text(label, color=color, font_size=60)
        pointer = VGroup(arrow, text).arrange(UP, buff=0.25).scale(0.5)
        return pointer

    def swap_elements(self, left_index, right_index):
        """
        Swap the elements at the given indices using an arc motion.
        """
        left_element = self.array_elements[left_index]
        right_element = self.array_elements[right_index]

        left_center = left_element.get_center()
        right_center = right_element.get_center()

        # Create arcs for the swap motion
        arc_left_to_right = ArcBetweenPoints(left_center, right_center, angle=TAU / 4)
        arc_right_to_left = ArcBetweenPoints(right_center, left_center, angle=-TAU / 4)

        if not self.played1:
            self.play(
                Write(self.steps[0]),
                MoveAlongPath(left_element, arc_left_to_right),
                MoveAlongPath(right_element, arc_right_to_left),
            )
            self.played1 = True
        else:
            self.play(
                MoveAlongPath(left_element, arc_left_to_right),
                MoveAlongPath(right_element, arc_right_to_left),
            )

        self.array_elements[left_index], self.array_elements[right_index] = (
            right_element,
            left_element,
        )

    def animate_scene(self):
        """
        Add elements to the scene and animate them.
        """
        # Add watermark
        watermark = create_watermark()
        self.add(watermark)

        if self.showTitle:
            self.add(self.title)

        # Add array and pointers to the scene
        self.play(
            *[
                Write(element, run_time=2)
                for element in [self.array_elements, self.indices]
            ],
            Write(self.array[0]),
            Write(self.array[-1])
        )
        self.play(Write(self.left), Write(self.right))

        # Initial positions for left and right pointers
        left_index = 0
        right_index = self.array_len - 1

        # Initial positions for left and right pointers
        left_index = 0
        right_index = self.array_len - 1

        # Animate the reversal process
        self.played1 = False
        played2 = False
        while left_index < right_index:
            self.swap_elements(left_index, right_index)

            if not played2:
                self.play(
                    Write(self.steps[1]),
                    self.left.animate.next_to(
                        self.array_elements[left_index + 1], UP, buff=0.3
                    ),
                    self.right.animate.next_to(
                        self.array_elements[right_index - 1], UP, buff=0.3
                    ),
                )
                played2 = True
            else:
                self.play(
                    self.left.animate.next_to(
                        self.array_elements[left_index + 1], UP, buff=0.3
                    ),
                    self.right.animate.next_to(
                        self.array_elements[right_index - 1], UP, buff=0.3
                    ),
                )

            left_index += 1
            right_index -= 1

        self.wait()


class Stacks(Scene):
    def construct(self):
        self.showTitle = False
        self.construction()
        self.animate_scene()

    def construction(self):
        """
        Define and position the elements of the scene.
        """
        # Adding title for LinkedIn post
        self.title = Text("Stacks").to_edge(UP, buff=0.5)
        
        self.nums = [0, 1, 2, 3, 4, 5]

        array_viz = Array(
            array=self.nums,
            index_color=GRAY_C,
        )
        
        self.array, self.array_elements, self.indices = array_viz.construct_array()


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
            
        self.add(self.array)
        self.add(self.indices)