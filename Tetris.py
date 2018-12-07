from sense_hat import SenseHat
from time import  sleep
from random import randint
sense = SenseHat()
r = (200, 0, 0)
o = (200, 100, 0)
y = (100, 200, 0)
g = (0, 200, 0)
t = (0, 200, 200)
b = (0, 0, 200)
v = (200, 0, 200)
n = (0, 0, 0)
up = 0
left = 0
right = 0
time = 100
sleepvar = 0.5
peice = 0
peicedone = 1
score = 0
rotation = 0
peicex = 0
peicey = 0
peicex2 = 0
peicey2 = 0
color = 0
peices = []
mpeices = []
while time > 0:
    time -= 1
    for event in sense.stick.get_event():
        if event.action == "pressed" and event.direction == "up":
          up = 1
        else:
          up = 0
        if event.action == "pressed" and event.direction == "left":
          left = 1
        else:
          left = 0
        if event.action == "pressed" and event.direction == "right":
          right = 1
        else:
          right = 0
    """choosing random peice and color"""
    if peicedone == 1:
        peice = 1
        color = randint(0,6)
        if color == 0:
            color = r
        elif color == 1:
            color = o
        elif color == 2:
            color = y
        elif color == 3:
            color = g
        elif color == 4:
            color = t
        elif color == 5:
            color = b
        elif color == 6:
            color = v
    """moving peice"""
    peicey2 -= 1
    if left == 1:
        peicex2 -= 1
    if right == 1:
        peicex2 += 1
    if up == 1:
        rotation += 1
    if rotation == 2:
        rotation = 0
    if rotation == 0 and peice == 1:
        mpeices.clear
        for block in mpeices:
            block[0] += peicex2
            block[1] += peicey2
    peicex2 = 0
    peicey2 = 0
    """starting peice"""
    if peice == 1 and peicedone == 1:
        peicex = 4
        peicey = 7
        mpeices.append([4,7,color])
        mpeices.append([3,7,color])
        mpeices.append([2,7,color])
        mpeices.append([5,7,color])
        peicedone = 0
    sense.clear()
    for block in peices:
            sense.set_pixel(block[0],block[1],block[2])
    for block in mpeices:
            sense.set_pixel(block[0],block[1],block[2])
    sleep(1)

