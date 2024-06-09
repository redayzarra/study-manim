from manim import *

class LinkedListNode:
    def __init__(
        self,
        label: str,
        value: str,
        radius=1.25,
        color=WHITE,  # Color of the node
        labelColor=WHITE,  # Label color
        valueColor=WHITE,  # Inner value color
    ):
        self.node = Circle(color=color, radius=radius)
        self.node_label = Text(label, color=labelColor).scale(0.75)
        self.node_value = MathTex(value, color=valueColor).scale(1.5)

        # Position label and value
        self.node_label.next_to(self.node, UP)
        self.node_value.move_to(self.node.get_center())

    def create(self):
        return VGroup(self.node, self.node_label, self.node_value)


class LinkedListPointer(Scene):
    def construct(self):
        # Define the head linked list node
        head = LinkedListNode("Head", "null", color=GREEN_D).create().shift(LEFT * 4)

        # Define the Node 1 which will connect to head
        node1 = LinkedListNode("Node A", "1").create()

        # Define the Node 2
        node2 = LinkedListNode("Node B", "2").create().shift(RIGHT * 4)

        # Arrow connecting head to node2
        arrow = Arrow(start=head[0].get_right(), end=node2[0].get_left(), color=GREEN_D)
        arrowLabel = MathTex("next", color=GREEN_A).next_to(arrow, UP * 0.5)

        step1 = Text("1. Create new node")
        step2 = Text("2. Update head's next pointer")
        step3 = Text("3. Link new node to next node")

        # Group and arrange text steps with buff
        steps = VGroup(step1, step2, step3).arrange(DOWN, buff=0.4).scale(0.5).shift(DOWN * 3)
        steps[1].shift(RIGHT * 0.78)
        steps[2].shift(RIGHT * 0.8 + UP * 0.08)
        
        steps.to_edge(LEFT)
        
        logo = Text("StudyDSA.com").scale(0.4)
        icon = ImageMobject("icon.png").scale(0.02)
        
        watermark = Group(logo, icon).arrange(LEFT, buff=0.01).to_corner(DR)

        # Add head and its elements
        self.add(head)
        self.add(watermark)
        

        # Add node2 and its elements
        self.add(node2)

        # Add the arrow
        self.add(arrow)
        self.play(Write(arrowLabel))
        self.wait()
        self.play(FadeOut(arrow), Unwrite(arrowLabel))

        # Animation to shift head and node2 and add node1
        self.play(
            head.animate.shift(LEFT),
            node2.animate.shift(RIGHT),
            FadeIn(node1, shift=UP, scale=0.66),
            Write(step1),
        )
        self.wait()

        arrow2 = Arrow(
            start=head[0].get_right(), end=node1[0].get_left(), color=GREEN_D
        )
        arrow2Label = MathTex("next", color=GREEN_A).next_to(arrow2, UP * 0.5)
        arrow3 = Arrow(start=node1[0].get_right(), end=node2[0].get_left(), color=WHITE)
        arrow3Label = MathTex("next").next_to(arrow3, UP * 0.5)

        self.play(GrowArrow(arrow2), Write(arrow2Label), Write(step2))
        self.play(GrowArrow(arrow3), Write(arrow3Label), Write(step3))
        self.wait(duration=2)


# To run the scene, use the following command in your terminal:
# manim -pql <script_name>.py LinkedListPointer
