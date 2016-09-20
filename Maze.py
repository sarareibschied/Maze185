import random
import turtle

class Maze():
    def __init__(self):
        self.s = turtle.Screen()
        self.s.screensize(400,400)
        self.t = turtle.Turtle()
        self.s.bgcolor('blue')
        self.s.register_shape("custom",((10, 10),(10, -10),\
                                        (10,-10),(-10,-10),\
                                        (-10,-10),(-10,10),\
                                        (-10,10), (10,10)))
        self.t.shape("custom")
        self.matrix = [[1 for i in range(20)] for i in range(20)]
        self.t.color('white')
        self.t.penup()
        self.t.goto(-190,190)
        self.matrix[0][0]=0
