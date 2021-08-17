import numpy as np
import sys
import PIL.ImageGrab

#Red is (172,46,46)
#Green is (0,72,32)
#178 is high y
#972 is y low

im = PIL.ImageGrab.grab()
pix = im.load()

allKnowingList = []
startingPoint = 1817
lastY = 178
lastX = 0
i = 0
for x in range(1817):
    currX = 1817 - x
    if currX < 23:
        val = input("f for next SS. q for quit")
        if val == 'q':
            break
        x = 0
    for y in range(178, 972):
        lastX = currX
        if y != lastY and (pix[x,y] == (172,46,46) or pix[x,y] == (0,72,32)):
            allKnowingList.append(972-y)
            lastY = y
            break

with open('tickdata.txt', 'w') as f:
    sys.stdout = f
    for i in range(len(allKnowingList)):
        print(allKnowingList[i])