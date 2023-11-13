import graphics as gr
import random

def pointsDraw(space, goal, xPrev, yPrev):
    x,y = goal[0],goal[1]
    xNext = (max([x,xPrev]) - min([x,xPrev])) / 2 + min([x,xPrev])
    yNext = (max([y, xPrev]) - min([y, xPrev])) / 2 + min([y, xPrev])
    gr.Point(xNext, yNext).draw(space)
    xPrev, yPrev = xNext, yNext
    return xPrev, yPrev

spaceX = 500
spaceY = 500
window = gr.GraphWin("Space", spaceX, spaceY)

# постороение треугольника
x1,y1 = random.randint(0, 500), random.randint(0, 500)
x2,y2 = random.randint(0, 500), random.randint(0, 500)
x3,y3 = random.randint(0, 500), random.randint(0, 500)
pole = {1:[x1,y1], 2:[x2,y2], 3:[x3,y3]}
points = [gr.Point(pole[1][0], pole[1][1]), gr.Point(pole[2][0], pole[2][1]), gr.Point(pole[3][0], pole[3][1])]
gr.Polygon(points).draw(window)


# первая точка
xPrev = random.randint(0, 500)
yPrev = random.randint(0, 500)
gr.Point(xPrev, yPrev).draw(window)
window.getMouse()



for i in range(10):
    point = random.randint(0, 2)
    pointsDraw(window,pole[random.randint(1, 3)],xPrev,yPrev)
    # gr.time.sleep(0.01)

window.getMouse()
window.close()



