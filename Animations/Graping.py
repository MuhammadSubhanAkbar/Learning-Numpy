from manim import *
import numpy as np

class TrigGraph(Scene):
    def construct(self):
        # Create axes with appropriate range for trig functions
        axes = Axes(
            x_range=[0, 5, 0.5],  # Finer increments for trig
            y_range=[-2, 3, 1],   # Expanded y-range for oscillations
            x_length=8,
            y_length=5,
            axis_config={
                "include_numbers": True,
                "include_tip": True,
                "font_size": 24,
            }
        )
        
        # Position axes
        axes.to_edge(UP, buff=0.5)
        
        # Add axis labels
        axis_labels = axes.get_axis_labels(x_label="x", y_label="f(x)")
        
        # Define the function - fix the square root issue
        def trig_func(x):
            # Use absolute value or handle negative cos(x) properly
            cos_term = np.sqrt(np.abs(np.cos(x))) * np.sign(np.cos(x))
            sin_term = np.sin(2 * x**2)
            constant = np.pi / 4
            return cos_term + sin_term + constant
        
        # Create the graph
        graph = axes.plot(
            trig_func,
            x_range=[0, 5, 0.01],  # Fine step for smooth curve
            color=YELLOW,
            use_smoothing=True
        )
        
        # Add graph label
        graph_label = axes.get_graph_label(
            graph,
            label=r"f(x) = \sqrt{|\cos(x)|}\cdot\text{sign}(\cos(x)) + \sin(2x^2) + \frac{\pi}{4}",
            x_val=3,
            direction=UP,
            font_size=28
        )
        
        # Animate everything
        self.play(Create(axes), Write(axis_labels))
        self.wait(0.5)
        self.play(Create(graph), run_time=3)  # Longer run time for complex graph
        self.play(Write(graph_label))
        self.wait(2)