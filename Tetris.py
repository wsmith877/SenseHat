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
counter = 0
up = 0
left = 0
right = 0
time = 100
sleepvar = 0.5
peice = 1
start = 1
peicedone = 0
score = 0
rotation = 0
protation = 0
line = 0
color = g
peicex = 0
peicey = 0
peices = []
mpeices = []
mpeices2 = []
bounds = [
    [-1,0],[-1,1],[-1,2],[-1,3],[-1,4],[-1,5],[-1,6],[-1,7],
    [8,0],[8,1],[8,2],[8,3],[8,4],[8,5],[8,6],[8,7],
    [0,-1],[1,-1],[2,-1],[3,-1],[4,-1],[5,-1],[6,-1],[7,-1],
    [0,8],[1,8],[2,8],[3,8],[4,8],[5,8],[6,8],[7,8]
    ]
good1 = 1
good2 = 1
while time > 0:
    good1 = 1
    good2 = 1
    good3 = 1
    time -= 1
    up = 0
    right = 0
    left = 0
    down = 0
    right2 = 0
    left2 = 0
    for event in sense.stick.get_events():
        if event.action == "pressed":
          # Check which direction
          if event.direction == "up":
             up = 1   # Up arrow
          if event.direction == "down":
             down = 1      # Down arrow
          if event.direction == "left": 
             left = 1      # Left arrow
          if event.direction == "right":
             right = 1      # Right arrow
    """clearing lines"""
    if peicedone == 1:
        for oop in range(0,8):
            for oof in peices:
                if oof[1] == oop:
                    line += 1
            print(line)
            if line == 8:
                counter = 0
                for what in peices:
                    if what[1] == oop:
                        del peices[counter]
                    else:
                        counter += 1
                for wat in peices:
                    if wat[1] > oop:
                        wat[1] -= 1
            line = 0
    """choosing random peice and color"""
    if start == 1:
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
    if peicedone == 1 or start == 1:
        peice = 1
        peicedone = 2
    """moving peice"""
    protation = rotation
    if up == 1:
        rotation += 1
    if rotation == 2:
        rotation = 0
    """Collision"""
    mpeices2 = mpeices
    if start == 0:
        for b in mpeices2: 
            if rotation == 1 and protation == 0 and peice == 1 and peicey < 6:
                for m in peices:
                    if good3 == 0:
                        if [peicex,peicey] == m:
                            good3 = 0
                        if [peicex,peicey-1] == m:
                            good3 = 0
                        if [peicex,peicey+1] == m:
                            good3 = 0
                        if [peicex,peicey+2] == m:
                            good3 = 0
                for x in bounds:
                    if good3 == 0:
                        if [peicex,peicey] == x:
                            good3 = 0
                        if [peicex,peicey-1] == x:
                            good3 = 0
                        if [peicex,peicey+1] == x:
                            good3 = 0
                        if [peicex,peicey+2] == x:
                            good3 = 0
                if good3 == 1 and peicey > 1:
                    del mpeices[0]
                    del mpeices[0]
                    del mpeices[0]
                    del mpeices[0]
                    mpeices.append([peicex,peicey])
                    mpeices.append([peicex,peicey-1])
                    mpeices.append([peicex,peicey+1])
                    mpeices.append([peicex,peicey+2])
                else:
                    rotation = 0
            if rotation == 0 and protation == 1 and peice == 1 and peicey < 6:
                for m in peices:
                    if good3 == 0:
                        if [peicex,peicey] == m:
                            good3 = 0
                        if [peicex-1,peicey] == m:
                            good3 = 0
                        if [peicex+1,peicey] == m:
                            good3 = 0
                        if [peicex-2,peicey] == m:
                            good3 = 0
                for x in bounds:
                    if good3 == 0:
                        if [peicex,peicey] == x:
                            good3 = 0
                        if [peicex-1,peicey] == x:
                            good3 = 0
                        if [peicex+1,peicey] == x:
                            good3 = 0
                        if [peicex-2,peicey] == x:
                            good3 = 0
                if good3 == 1 and peicey > 1:
                    del mpeices[0]
                    del mpeices[0]
                    del mpeices[0]
                    del mpeices[0]
                    mpeices.append([peicex,peicey])
                    mpeices.append([peicex-1,peicey])
                    mpeices.append([peicex+1,peicey])
                    mpeices.append([peicex-2,peicey])
                else:
                    rotation = 1
            if left == 1:
                b[0] -= 1
            if right == 1:
                if peice != 1 or rotation != 1 or peicex != 7:
                    b[0] += 1
            for i in bounds:
                if good1 == 1:
                    if b == i:
                        good1 = 0
            for k in peices:
                if good1 == 1:
                    if b == k:
                        good1 = 0
            if good1 == 0:
                if left2 == 0 and left == 1:
                    for p in mpeices2:
                        p[0] += 1
                    left2 = 1
                if right2 == 0 and right == 1:
                    for p in mpeices2:
                        b[0] -= 1
                    right2 = 1
            b[1] -= 1
            for l in bounds:
                if good2 == 1:
                    if b == l:
                        good2 = 0
            for z in peices:
                if good2 == 1:
                    if b == z:
                        good2 = 0
        for block in mpeices:
            if good2 == 0:
                peicedone = 1
                block[1] += 1
    if left == 1:
        peicex -= 1
    if right == 1:
        if peice != 1 or rotation != 1 or peicex != 7:
            peicex += 1
    if good2 == 1:
        peicey -= 1
    left2 = 0
    right2 = 0
    """adding block to "global" peices"""
    if peicedone == 1:
        for i in mpeices:
            peices.append(i)
        del mpeices[0]
        del mpeices[0]
        del mpeices[0]
        del mpeices[0]
    """starting peice"""
    if (peice == 1 and peicedone == 2) or start == 1:
        mpeices.append([4,7])
        mpeices.append([3,7])
        mpeices.append([2,7])
        mpeices.append([5,7])
        peicex = 4
        peicey = 7
        peicedone = 0
    sense.clear()
    if start == 0:
        if len(peices) >= 1:
            for j in peices:
                if j[1] < 8:
                    sense.set_pixel(j[0],7 - j[1],color)
        for u in mpeices:
            if u[1] < 8:
                sense.set_pixel(u[0],7 - u[1],color)
    else:
        start = 0
    if down == 1:
        sleep(0.3)
    else:
        sleep(1)
