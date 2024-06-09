from manim import *
from components.SinglyLinkedList import SinglyListNode
from components.watermark import create_watermark

class AddingNodeToBeginning(Scene):
    def construct(self):
        self.construction()
        self.animate_scene()

    def construction(self):
        """
        Define and position the elements of the scene.
        """
        # Adding list nodes for the scene
        self.head = SinglyListNode("Head", "0", color=GREEN_D, value_color=GREEN_A).create().shift(LEFT * 4)
        self.node1 = SinglyListNode("Node A", "1").create()
        self.node2 = SinglyListNode("Node B", "2").create().shift(RIGHT * 4)

        # Adding arrows to connect list nodes
        self.arrow = Arrow(start=self.head[0].get_right(), end=self.node2[0].get_left(), color=GREEN_D)
        self.arrow_label = MathTex("next", color=GREEN_A).next_to(self.arrow, UP * 0.5)

        # Adding educational steps
        step1 = Text("1. Create new node")
        step2 = Text("2. Update head's next pointer")
        step3 = Text("3. Link new node to next node")
        
        # Positioning steps, need to do this in better way
        self.steps = VGroup(step1, step2, step3).arrange(DOWN, buff=0.4).scale(0.5).shift(DOWN * 3)
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
        arrow2 = Arrow(start=self.head[0].get_right(), end=self.node1[0].get_left(), color=GREEN_D)
        arrow2_label = MathTex("next", color=GREEN_A).next_to(arrow2, UP * 0.5)
        arrow3 = Arrow(start=self.node1[0].get_right(), end=self.node2[0].get_left(), color=WHITE)
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
        # Adding list nodes for the scene
        self.left = SinglyListNode("Left", "null", color=GREEN_D, value_color=GREEN_A).create().shift(LEFT * 4)
        self.node1 = SinglyListNode("Head", "0").create()
        self.right = SinglyListNode("Right", "null", color=GREEN_D, value_color=GREEN_A).create().shift(RIGHT * 4)

        # Adding arrows to connect list nodes
        self.arrow = Arrow(start=self.left[0].get_right(), end=self.right[0].get_left(), color=GREEN_D)
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
        arrow2 = Arrow(start=self.left[0].get_right(), end=self.node1[0].get_left(), color=GREEN_D)
        arrow2_label = MathTex("next", color=GREEN_A).next_to(arrow2, UP * 0.5)
        arrow3 = Arrow(start=self.node1[0].get_right(), end=self.right[0].get_left(), color=WHITE)
        arrow3_label = MathTex("next").next_to(arrow3, UP * 0.5)

        # Display new arrows and steps
        self.play(GrowArrow(arrow2), Write(arrow2_label), Write(self.steps[1]))
        self.play(GrowArrow(arrow3), Write(arrow3_label))
        self.wait(duration=2)