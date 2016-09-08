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
        assert type(self.m.t) == turtle._Turtle

unittest.main()
