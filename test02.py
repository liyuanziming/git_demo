import random

from manim import *

class Shapes(Scene):

    def construct(self):
        self.camera.background_color=WHITE
        circle = Circle(color= DARK_BLUE)
        square = Square(color=PURE_RED)
        triangle = Polygon(np.array([0, 0, 0]), np.array([1, 1, 0]), np.array([1, -1, 0]),color= YELLOW)
        square.shift(LEFT)
        self.play(Create(circle))
        self.wait(0.5)
        self.play(FadeOut(circle))
        self.play(Create(square))
        self.wait(0.5)
        self.play(Transform (square,triangle))
        #self.play(GrowFromCenter(square))
        #self.play(Transform(square, triangle))