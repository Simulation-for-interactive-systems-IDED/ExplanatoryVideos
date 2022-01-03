from manim import *
from numpy import rec

# config.pixel_height = 1920 # 1080 is default
# config.pixel_width = 1920 # 1920 is default
# config.frame_width = 5
# config.frame_height = 5

class LinearInterpolationScene(Scene):
    def construct(self):
        # create a circle
        axes = Axes(
            x_range = [-3, 3, 1],
            y_range = [-3, 3, 1],
            x_length = 6,
            y_length = 6
        )

        # Creates a grid
        coord = NumberPlane(
            x_range = [-3, 3, 1],
            y_range = [-3, 3, 1],
            x_length = 6,
            y_length = 6
        )

        # Creates a vector
        vectorA = Vector([2, 2])
        vectorA.set_color(RED)
        vectorALabel = vectorA.coordinate_label()
        vectorALabel.set_color(RED)

        # Creates another vector
        vectorB = Vector([-1, 3])
        vectorB.set_color(GREEN)
        vectorBLabel = vectorB.coordinate_label()
        vectorBLabel.set_color(GREEN)

        vectorBLabelCopy = vectorBLabel.copy()
        vectorBLabelCopy.set_color(YELLOW)
        # vectorBLabelCopy.generate_target()
        # vectorBLabelCopy.target.move_to([-2, -2, 0])

        # Creates diff vector
        vectorDiff = Vector([vectorB.get_end()[0] - vectorA.get_end()[0], vectorB.get_end()[1] - vectorA.get_end()[1]])
        vectorDiff.set_color(BLUE)
        vectorDiffCopy = vectorDiff.copy()
        vectorDiffLabel = vectorDiff.coordinate_label()
        vectorDiffLabel.set_color(BLUE)

        equalSign = Text("=")
        equalSign.move_to([-5, -2, 0])
        equalSign.set_color(YELLOW)

        plusSign = Text("+")
        plusSign.move_to([-3, -2, 0])

        self.play(Create(vectorA))
        self.play(Create(vectorALabel))

        self.play(Create(vectorB))
        self.play(Create(vectorBLabel))

        self.play(Create(vectorDiff))
        self.play(Create(vectorDiffLabel))

        self.play(Create(axes))
        # self.play(Create(coord))
        
        self.play(vectorDiffCopy.animate.shift(vectorA.get_end()).set_color(YELLOW), vectorBLabel.animate.set_color(YELLOW), vectorDiffLabel.animate.move_to([-2, -2, 0]), FadeIn(plusSign), vectorALabel.animate.move_to([-4, -2, 0]))
        
        self.wait(1)
        
        self.play(vectorBLabelCopy.animate.move_to([-6, -2, 0]), FadeIn(equalSign))

        self.wait(4)
        

class CreateCircle(Scene):
    def construct(self):
        circle = Circle() # create a circle
        circle.set_fill(PINK, opacity=0.5) # set the color and transparency
        self.play(Create(circle)) # show the circle on screen

class SquareToCircle(Scene):
    def construct(self):
        circle = Circle() # create a circle
        circle.set_fill(PINK, opacity=0.5) # set color and transparency

        square = Square() # create a square
        square.rotate(PI / 4) # rotate a certain amount

        self.play(Create(square)) # animate the creation of the square
        self.play(Transform(square, circle)) # interpolate the square into the circle
        self.play(FadeOut(square)) # fade out animation

class SquareAndCircle(Scene):
    def construct(self):
        circle = Circle() # create a circle
        circle.set_fill(PINK, opacity=0.5) # set the color and transparency

        square = Square() # create a square
        square.set_fill(BLUE, opacity=0.5) # set the color and transparency

        square.next_to(circle, DOWN, buff=0.5) # set the position
        self.play(Create(circle), Create(square)) # show the shapes on screen

class AnimatedSquareToCircle(Scene):
    def construct(self):
        circle = Circle() # create a circle
        square = Square() # create a square

        self.play(Create(square))  # show the shapes on screen
        self.play(square.animate.rotate(PI / 4)) # rotate the square
        self.play(
            ReplacementTransform(square, circle)
        ) # transform the square into a circle
        self.play(
            circle.animate.set_fill(PINK, opacity=0.5)
        ) # color the circle on screen

class DifferentRotations(Scene):
    def construct(self):
        # https://docs.manim.community/en/stable/tutorials/quickstart.html
        # This Scene illustrates the quirks of .animate. When using .animate,
        left_square = Square(color=BLUE, fill_opacity=0.7).shift(2 * LEFT)
        right_square = Square(color=GREEN, fill_opacity=0.7).shift(2 * RIGHT)
        self.play(
            left_square.animate.rotate(PI), Rotate(right_square, angle=PI), run_time=2
        )
        self.wait()