from manim import *
from SinglyLinkedList import SinglyListNode
from watermark import create_watermark

class AddingNodeToBeginning(Scene):
    def construct(self):
        self.construction()
        self.animate_scene()

    def construction(self):
        """
        Define and position the elements of the scene.
        """
        # Adding list nodes for the scene
        self.head = SinglyListNode("Head", "null", color=GREEN_D).create().shift(LEFT * 4)
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

