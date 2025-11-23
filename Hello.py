from manim import *
import numpy as np

class Example(Scene):
    def construct(self):
        cos_fuc = FunctionGraph(
            lambda t: np.cos(t),
        )

        self.add(cos_fuc)


if __name__ == "__main__":
    scene = Example()
    scene.render()