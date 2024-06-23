from manim import *
from components.Hashmap import Hashmap
from components.watermark import create_watermark

class HashFunction(Scene):
    def construct(self):
        self.showTitle = False
        self.construction()
        self.animate_scene()

    def construction(self):
        """
        Define and position the elements of the scene.
        """
        # Adding title for LinkedIn post
        self.title = Text("Hash Function").to_edge(UP, buff=0.5)
        

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

        self.hashmap = Hashmap(num_buckets=5).create()
        self.add(self.hashmap)