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
        self.show_title = False
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
            "Initialize `cur` pointer at the head node",
            "Move `cur` pointer to the next node",
        ]
        self.steps = Steps(steps_text).create()

        self.create_linked_list([1, 2, 3, 4, "null"])
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
        self.next_arrows = VGroup()
        for index, node in enumerate(self.linked_list[:-1]):
            next_node = self.linked_list[index + 1]
            arrow = ArcBetweenPoints(
                start=node.get_bottom() + (DR * 0.2),
                end=next_node.get_bottom() + (DL * 0.2),
                radius=1.5,
                color=GRAY_C,
            ).add_tip(tip_width=0.25)
            next = Text("next", font_size=25, color=GRAY_A).next_to(arrow, DOWN)
            element = VGroup().add(arrow, next)
            self.next_arrows.add(element)

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
                for elements in [self.linked_list, self.next_arrows]
            ],
        )

        # Add cur pointer at the head - Step 1
        self.play(
            Write(self.cur),
            Write(self.steps[0], run_time=1.5),
            ApplyMethod(self.linked_list[0].set_color, GREEN),
        )

        played = False
        for i in range(len(self.linked_list) - 1):
            self.play(Indicate(self.next_arrows[i][1], scale_factor=1.2, color=YELLOW))

            # Flash the "next" label and move cur pointer to the next node

            # Move cur pointer to the next node
            if not played:
                self.play(
                    ApplyMethod(self.cur.next_to, self.linked_list[i + 1], UP),
                    ApplyMethod(self.linked_list[i].set_color, WHITE),
                    ApplyMethod(self.linked_list[i + 1].set_color, GREEN),
                    Write(self.steps[1], run_time=1.5),
                )
                played = True
            else:
                self.play(
                    ApplyMethod(self.cur.next_to, self.linked_list[i + 1], UP),
                    ApplyMethod(self.linked_list[i].set_color, WHITE),
                    ApplyMethod(self.linked_list[i + 1].set_color, GREEN),
                )

        self.wait()


class DoublyLinkedList(Scene):
    def construct(self):
        self.showTitle = True
        self.construction()
        self.animate_scene()

    def construction(self):
        """
        Define and position the elements of the scene.
        """
        # Adding steps for LinkedIn post
        steps_text = [
            "Initialize `cur` pointer at the head node",
            "Move `cur` pointer to the next node",
        ]
        self.steps = Steps(steps_text).create()

        self.create_linked_list([1, 2, 3, 4, "null"])
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

        self.linked_list.arrange(RIGHT, aligned_edge=DOWN, buff=1)

    def create_arrows(self):
        """Creates arrows pointing from one list node to the next and previous."""
        self.next_arrows = VGroup()
        self.prev_arrows = VGroup()

        for index, node in enumerate(self.linked_list):

            # Next arrow
            if not index == len(self.linked_list) - 1:
                next_node = self.linked_list[index + 1]
                next_arrow = ArcBetweenPoints(
                    start=node.get_bottom() + (RIGHT * 0.2 - SMALL_BUFF),
                    end=next_node.get_bottom() + (LEFT * 0.2 - SMALL_BUFF),
                    radius=2,
                    color=GRAY_C,
                ).add_tip(tip_width=0.25)
                next_label = Text("next", font_size=22, color=GRAY_A).next_to(
                    next_arrow, DOWN
                )
                next_element = VGroup().add(next_arrow, next_label)
                self.next_arrows.add(next_element)

            # Prev arrow
            if index > 0:  # Skip the first node since it has no previous node
                prev_node = self.linked_list[index - 1]
                prev_arrow = ArcBetweenPoints(
                    start=node.get_top() + (LEFT * 0.2 + SMALL_BUFF),
                    end=prev_node.get_top() + (RIGHT * 0.2 + SMALL_BUFF),
                    radius=2,  # Negative radius for the upward arc
                    color=GRAY_C,
                ).add_tip(tip_width=0.25)
                prev_label = Text("prev", font_size=22, color=GRAY_A).next_to(
                    prev_arrow, UP
                )
                prev_element = VGroup().add(prev_arrow, prev_label)
                self.prev_arrows.add(prev_element)

    def animate_scene(self):
        """
        Add elements to the scene and animate them.
        """
        # Add watermark
        watermark = create_watermark()
        self.add(watermark)

        # Conditionally add title
        title = Text("Doubly Linked List").to_edge(UP, buff=0.5)
        if self.showTitle:
            self.add(title)

        self.add(self.linked_list)

        # Draw the linked list with pointers
        self.play(
            *[
                Write(elements, run_time=2)
                for elements in [self.linked_list, self.next_arrows, self.prev_arrows]
            ],
        )

        # Add cur pointer at the head - Step 1
        self.play(
            # Write(self.cur),
            Write(self.steps[0], run_time=1.5),
            ApplyMethod(self.linked_list[0].set_color, GREEN),
        )

        self.wait(3)
