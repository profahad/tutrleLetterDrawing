import turtle


class TurtleShapes:

    def __init__(self, speed=None) -> None:
        super().__init__()
        self.obj = turtle.Turtle()
        self.obj.width(5)
        self.obj.speed(speed if (speed != None) else 1)

    def shapeM(self):
        self.obj.color('#37474F')
        self.obj.right(90)
        self.obj.forward(90)
        self.obj.back(90)
        self.obj.right(-45)
        self.obj.forward(45)
        self.obj.right(-90)
        self.obj.forward(45)
        self.obj.right(45 * 3)
        self.obj.forward(90)
        self.obj.right(-90)

    def shapeSpace(self):
        self.obj.color("#FFFFFF")
        self.obj.forward(45)

    def shapeF(self):
        self.obj.color('#37474F')
        self.obj.right(90)
        self.obj.forward(-45)
        self.obj.back(45)
        self.obj.right(-90)
        self.obj.forward(45)
        self.obj.back(45)
        self.obj.right(90)
        self.obj.forward(45)
        self.obj.right(-90)
        self.obj.forward(45)
        self.obj.back(45)

    def shapeU(self):
        self.obj.color('#37474F')
        self.obj.left(90)
        self.obj.forward(90)
        self.obj.back(90)
        self.obj.right(90)
        self.obj.forward(45)
        self.obj.left(90)
        self.obj.forward(90)
        self.obj.back(90)

    def draw_Name_Initials(self):
        self.shapeM()
        self.shapeSpace()
        self.shapeF()


helper = TurtleShapes(speed=2)
helper.draw_Name_Initials()
