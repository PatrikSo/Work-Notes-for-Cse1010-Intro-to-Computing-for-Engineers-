 
from graphics import *

def moveCircleFun():
    win=GraphWin("Lab 5",400,400)
    shape = Circle(Point(100,100),50)
    shape.setFill('#AA0000')
    shape.draw(win)
    shape2 = Rectangle(Point(200,200),Point(300,300))
    shape2.setFill('#00BB00')
    shape2.draw(win)
    shape3 = Circle(Point(300,100),50)
    shape3.setFill('#AA0000')
    shape3.draw(win)
    win.setBackground(color_rgb (130,130,75))

def moveCircle():
    for i in range(10):
        shape2.move(10,10)
        shape.move(10,10)

def namedWindow():
    win = GraphWin("Lab 5", 400, 400)
    text = Text(Point(200,100), "Enter your name and click mouse to proceed")
    text.draw(win)
    inputBox = Entry(Point(200,150),20)
    inputBox.draw(win)
    win.getMouse()
    text = inputBox.getText()
    win2 = GraphWin(text, 250, 250)
    text2 = Text(Point(125,125), text)
    text2.draw(win2)

#Page 169 - 170 Discussion questions
    
s1 = "spam"
s2 = "ni!"

#1-a
x1 = "The knights who say, " + s2
print(x1)

#1-b
x2 = 3 * s1 + 2 * s2
print(x2)

#1-c
x3 = s1[1]
print(x3)

#1-d
x4 = s1[1:3]
print(x4)

#1-e
x5 = s1[2] + s2[:2]
print(x5)

#1-fboard
x6 = s1[1:]
print(x6)

#1-fReal
x7 = s1 + s2[-1]
print(x7)

#1-g
x8 = s1.upper()
print(x8)

#1-h
x9 = s2.upper().ljust(4)*3
print(x9)
#ljust(number) widens the string with space

print("---------------------")

#2
s1 = "spam"
s2 = "ni!"

#2-a
"NINI"
x2a = s2[:2].upper()*2
print(x2a)

#2-b
"ni!spamni!"
x2b = s2 + s1 + s2
print(x2b)

#2-c
"Spam Ni! Spam Ni! Spam Ni!"
x2c = (s1[0].upper() + s1[1:] + " " + s2[0].upper() + s2[1:])*3
print(x2c[0:len(x2c)-1])

#2-e
["sp", "m"] #python list
x2e = s1[0:2] 
y2e = s1[3]
lst2e = [x2e,y2e]
print([lst2e])

print("--------------")

#3
#3-a
for ch in "aardvark":
    print(ch)

#3-b
for w in "Now is the winter of our discontent...".split():
    print(w)

#3-c
for w in "Mississippi".split("i"):
    print(w, end = "")

#3-d
msg = ""
for s in "secret".split("e"):
    msg = msg + s
print(msg)

def quizeScore(score):
    scores = "FFDCBA"
    return scores[score]
