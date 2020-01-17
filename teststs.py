from graphics import *

def square():
    win = GraphWin()
    shape = Rectangle(Point(50, 50), Point(70, 70))
    shape.setOutline('red')
    shape.setFill('blue')
    shape.draw(win)

    for i in range(10):
        m = win.getMouse()
        c = shape.getCenter()
        x = m.getX() - c.getX()
        y = m.getY() - c.getY()
        shapeClone = shape.clone()
        shapeClone.move(x, y)
        shapeClone.draw(win)
        shape = shapeClone

def happyFace():
    win = GraphWin("Face", 400, 400)   #initialize the graph window, parameters determin window size
    leftEye = Circle(Point(50,50), 20)
    rightEye = Circle(Point(200, 50), 20)
    mouth = Rectangle(Point(50, 50), Point(170, 110))
    leftEye.draw(win)
    rightEye.draw(win)
    mouth.draw(win)
