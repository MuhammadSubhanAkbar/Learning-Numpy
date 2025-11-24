from manim import *
import numpy as np

class ExampleFunctionGraph(Scene):
    def construct(self):
        cos_func = FunctionGraph(
            lambda t: np.cos(t) + 0.5 * np.cos(7 * t) + (1 / 7) * np.cos(14 * t),
            color=RED,
            x_range=[-3*PI, 3*PI]
        )

        sin_func_1 = FunctionGraph(
            lambda t: np.sin(t) + 0.5 * np.sin(7 * t) + (1 / 7) * np.sin(14 * t),
            color=BLUE,
            x_range=[-3*PI, 3*PI]
        )

        sin_func_2 = FunctionGraph(
            lambda t: np.sin(t) + 0.5 * np.sin(7 * t) + (1 / 7) * np.sin(14 * t),
            x_range=[-4, 4],
            color=GREEN,
        )

        cos_fuc_2 = FunctionGraph(
            lambda t: np.cos(t) + 0.2 * np.sin(6*t) + (3/2) * np.cos(6*t),
            color=ORANGE,  # Added color
            x_range=[-3*PI, 3*PI]  # Added x_range
        )

        # Corrected: self.play() instead of self.pay()
        self.play(Create(cos_func))
        self.play(Create(cos_fuc_2))
        self.play(Create(sin_func_1))
        self.play(Create(sin_func_2))  # Fixed typo: pay -> play
        self.wait()