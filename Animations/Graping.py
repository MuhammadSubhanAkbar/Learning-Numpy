from manim import *
import numpy as np

class Graphing(Scene):
    def construct(self):
        
        #making planes
        my_Plane = NumberPlane(
            x_range=[-6,6],
            x_length=5,
            y_range=[-10,10],
            y_length=5,
            )
        
        #Adding coordinates
        my_Plane.add_coordinates()
        my_Plane.shift(RIGHT*3)


        #making the function the function
        my_function = my_Plane.get_graph(
            lambda x: np.sin(2*x**2)**2 / np.tan(x**2),  # Fixed: np.sin(...)**2 not np.sin**2(...)
            x_range=[-6,6],
            color=GREEN_B
            )
        
        area = my_Plane.get_area(
            graph=my_function, 
            x_range=[-5,5],
            color=[BLUE, YELLOW]
            )
        
        label = MathTex(r"\frac{\sin^2(2x^2)}{\tan(x^2)}").next_to(  # Fixed LaTeX
            my_Plane, UP, buff=0.2
        )

        horiz_line = Line(
            start=my_Plane.c2p(0, my_function.underlying_function(-2)),
            end=my_Plane.c2p(-2, my_function.underlying_function(-2)),  # Added missing comma
            stroke_color=YELLOW,  # Fixed: added comma above
            stroke_width=10
        )

        self.play(DrawBorderThenFill(my_Plane))
        self.play(Create(my_function), Write(label))
        self.play(FadeIn(area))