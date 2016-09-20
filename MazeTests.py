import unittest
from Maze import *

class testMaze(unittest.TestCase):
    def setUp(self):
        # this checks for a Maze class
        self.m=Maze()

    def testMazeExists(self):
        pass

    def testScreenExists(self):
        assert type(self.m.s) == turtle._Screen

    def testTurtleExists(self):
        assert type(self.m.t) == turtle.Turtle

    def testScreenBackgroundIsBlue(self):
        assert self.m.s.bgcolor()=='blue'

    def testForMatrix(self):
        assert len(self.m.matrix)==20

    def testTurtleIsWhite(self):
        assert self.m.t.color()[0]=='white' and self.m.t.color()[1]=='white'

    def testTurtleIsInUpperLeftHandCorner(self):
        assert self.m.t.pos()==(-190,190), "Turtle position is %d, %d" % \
               (self.m.t.pos()[0],self.m.t.pos()[1])

    def testTurtleMatrixIs0InUpperLeftHandCorner(self):
        assert self.m.matrix[0][0]==0

    def testScreenSize(self):
        assert self.m.s.screensize()==(400,400)
        
if __name__=="__main__":
    unittest.main()
