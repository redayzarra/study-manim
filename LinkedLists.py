from manim import *
from components.ListNode import ListNode
from components.Steps import Steps
from components.watermark import create_watermark


class AddingNodeToBeginning(Scene):
    def construct(self):
        self.construction()
        self.animate_scene()

    def construction(self):
        """
        Define and position the elements of the scene.
        """
        # Adding listNums nodes for the scene
        self.head = (
            ListNode("Head", "0", color=GREEN_D, value_color=GREEN_A)
            .create()
            .shift(LEFT * 4)
        )
        self.node1 = ListNode("Node A", "1").create()
        self.node2 = ListNode("Node B", "2").create().shift(RIGHT * 4)

        # Adding arrows to connect listNums nodes
        self.arrow = Arrow(
            start=self.head[0].get_right(), end=self.node2[0].get_left(), color=GREEN_D
        )
        self.arrow_label = MathTex("next", color=GREEN_A).next_to(self.arrow, UP * 0.5)

        # Adding educational steps
        step1 = Text("1. Create new node")
        step2 = Text("2. Update head's next pointer")
        step3 = Text("3. Link new node to next node")

        # Positioning steps, need to do this in better way
        self.steps = (
            VGroup(step1, step2, step3)
            .arrange(DOWN, buff=0.4)
            .scale(0.5)
            .shift(DOWN * 3)
        )
        self.steps[1].shift(RIGHT * 0.78)
        self.steps[2].shift(RIGHT * 0.8 + UP * 0.08)
        self.steps.to_edge(LEFT)

    def animate_scene(self):
        """
        Add elements to the scene and animate them.
        """
        # Add watermark
        watermark = create_watermark()
        self.add(watermark)

        # Add nodes and their elements
        self.add(self.head, self.node2, self.arrow)
        self.play(Write(self.arrow_label))
        self.wait()
        self.play(FadeOut(self.arrow), Unwrite(self.arrow_label))

        # Animation to shift head and node2, and add node1
        self.play(
            self.head.animate.shift(LEFT),
            self.node2.animate.shift(RIGHT),
            FadeIn(self.node1, shift=UP, scale=0.66),
            Write(self.steps[0]),
        )
        self.wait()

        # New arrows for updated connections
        arrow2 = Arrow(
            start=self.head[0].get_right(), end=self.node1[0].get_left(), color=GREEN_D
        )
        arrow2_label = MathTex("next", color=GREEN_A).next_to(arrow2, UP * 0.5)
        arrow3 = Arrow(
            start=self.node1[0].get_right(), end=self.node2[0].get_left(), color=WHITE
        )
        arrow3_label = MathTex("next").next_to(arrow3, UP * 0.5)

        # Display new arrows and steps
        self.play(GrowArrow(arrow2), Write(arrow2_label), Write(self.steps[1]))
        self.play(GrowArrow(arrow3), Write(arrow3_label), Write(self.steps[2]))
        self.wait(duration=2)


class SentinelNodes(Scene):
    def construct(self):
        self.construction()
        self.animate_scene()

    def construction(self):
        """
        Define and position the elements of the scene.
        """
        # Adding title for LinkedIn post
        self.title = Text("Sentinel Nodes").to_edge(UP, buff=0.5)
        # Adding listNums nodes for the scene
        self.left = (
            ListNode("Left", "null", color=GREEN_D, value_color=GREEN_A)
            .create()
            .shift(LEFT * 4)
        )
        self.node1 = ListNode("Head", "0").create()
        self.right = (
            ListNode("Right", "null", color=GREEN_D, value_color=GREEN_A)
            .create()
            .shift(RIGHT * 4)
        )

        # Adding arrows to connect listNums nodes
        self.arrow = Arrow(
            start=self.left[0].get_right(), end=self.right[0].get_left(), color=GREEN_D
        )
        self.arrow_label = MathTex("next", color=GREEN_A).next_to(self.arrow, UP * 0.5)

        # Adding educational steps
        step1 = Text("1. Create a new head node")
        step3 = Text("2. Link the head node to sentinel nodes")

        # Step 2: Group the text objects
        self.steps = VGroup(step1, step3).arrange(DOWN, buff=0.4)

        # Step 3: Align each text object to the left
        for step in self.steps:
            step.align_to(self.steps, LEFT)

        # Optional: Scaling and shifting
        self.steps.scale(0.5).to_corner(DL)

    def animate_scene(self):
        """
        Add elements to the scene and animate them.
        """
        # Add watermark
        watermark = create_watermark()
        self.add(watermark)

        self.add(self.title)

        # Add nodes and their elements
        self.add(self.left, self.right, self.arrow)
        self.play(Write(self.arrow_label))
        self.wait()
        self.play(FadeOut(self.arrow), Unwrite(self.arrow_label))

        # Animation to shift left and right, and add head
        self.play(
            self.left.animate.shift(LEFT),
            self.right.animate.shift(RIGHT),
            FadeIn(self.node1, shift=UP, scale=0.66),
            Write(self.steps[0]),
        )
        self.wait()

        # New arrows for updated connections
        arrow2 = Arrow(
            start=self.left[0].get_right(), end=self.node1[0].get_left(), color=GREEN_D
        )
        arrow2_label = MathTex("next", color=GREEN_A).next_to(arrow2, UP * 0.5)
        arrow3 = Arrow(
            start=self.node1[0].get_right(), end=self.right[0].get_left(), color=WHITE
        )
        arrow3_label = MathTex("next").next_to(arrow3, UP * 0.5)

        # Display new arrows and steps
        self.play(GrowArrow(arrow2), Write(arrow2_label), Write(self.steps[1]))
        self.play(GrowArrow(arrow3), Write(arrow3_label))
        self.wait(duration=2)


class SinglyLinkedList(Scene):
    def construct(self):
        self.show_title = True
        self.construction()
        self.animate_scene()

    def construction(self):
        """
        Define and position the elements of the scene.
        """
        # Add title
        self.title = Text("Singly Linked List").to_edge(UP, buff=0.5)

        # Adding steps for LinkedIn post
        steps_text = [
            "Start pointer at the head",
            "Move the pointer",
            "Peek at the top element",
        ]
        self.steps = Steps(steps_text).create()

        self.create_linked_list([0, 1, 2, 3, 4])
        self.create_arrows()

        self.cur = Text("cur", font_size=30, color=GREEN).next_to(
            self.linked_list[0], UP
        )

    def create_linked_list(self, nums: List[int]) -> None:
        """Creates the linked list nodes and positions them."""
        self.linked_list = VGroup()
        radius = 0.75

        for num in nums:
            list_node = ListNode(str(num), radius=radius).create()
            self.linked_list.add(list_node)

        self.linked_list.arrange(RIGHT, aligned_edge=DOWN, buff=1).shift(UP * 0.65)

    def create_arrows(self):
        """Creates arrows pointing from one list node to the next."""
        self.arrows = VGroup()
        for index, node in enumerate(self.linked_list[:-1]):
            next_node = self.linked_list[index + 1]
            arrow = ArcBetweenPoints(
                start=node.get_bottom() + (DR * 0.2),
                end=next_node.get_bottom() + (DL * 0.2),
                radius=1.5,
                color=GRAY_C,
            ).add_tip(tip_width=0.25)
            next = Text("next", font_size=25, color=GRAY_A).next_to(arrow, DOWN)
            self.arrows.add(arrow, next)

    def animate_scene(self):
        """
        Add elements to the scene and animate them.
        """
        # Add watermark
        watermark = create_watermark()
        self.add(watermark)

        # Conditionally render the title
        if self.show_title:
            self.add(self.title)

        self.add(self.linked_list)

        # Draw the linked list with pointers
        self.play(
            *[
                Write(elements, run_time=2)
                for elements in [self.linked_list, self.arrows]
            ],
        )

        # Add cur pointer at the head - Step 1
        self.play(
            Write(self.cur),
            Write(self.steps[0]),
            self.linked_list[0].animate.set_color(GREEN),
        )

        self.wait(3)
