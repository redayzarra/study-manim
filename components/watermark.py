from manim import *

def create_watermark():
    logo = Text("StudyDSA.com").scale(0.4)
    icon = ImageMobject("icon.png").scale(0.02)
    watermark = Group(logo, icon).arrange(LEFT, buff=0.08).to_corner(DR)
    return watermark