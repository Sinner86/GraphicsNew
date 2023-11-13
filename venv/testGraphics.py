import graphics as gr
import random

def pointsDrawRandom(space, max = 500):
    x = random.randint(0, max)
    y = random.randint(0, max)
    gr.Point(x, y).draw(space)

def pointsDraw(space, point, xPrev, yPrev, max = 500):
    a = point
    if xNext < xPrev:
        xNext = (xPrev - xNext) / 2 + xNext
    else: xNext = (xNext - xPrev) / 2 + xPrev
    if yNext < yPrev:
        yNext = (yPrev - yNext) / 2 + yNext
    else: yNext = (yNext - yPrev) / 2 + yPrev
    print(xNext, yNext)
    gr.Point(xNext, yNext).draw(space)
    xPrev, yPrev = xNext, yNext
    return xPrev, yPrev



def ran_f(max = 500):
    x = random.randint(0, max)
    y = random.randint(0, max)
    list = [x,y]
    return list

spaceX = 500
spaceY = 500
window = gr.GraphWin("Space", spaceX, spaceY)

# постороение треугольника
pole = {'point1':[ran_f()[0], ran_f()[1]], 'point2':[ran_f()[0], ran_f()[1]],'point3':[ran_f()[0], ran_f()[1]]}

x1,y1 = ran_f()[0], ran_f()[1]
x2,y2 = ran_f()[0], ran_f()[1]
x3,y3 = ran_f()[0], ran_f()[1]

points = [gr.Point(pole['point1'][0], pole['point1'][1]), gr.Point(pole['point2'][0], pole['point2'][1]), gr.Point(pole['point3'][0], pole['point3'][1])]
# gr.Polygon(points).draw(window)

# первая точка
xPrev = random.randint(0, 500)
yPrev = random.randint(0, 500)
# gr.Point(xPrev, yPrev).draw(window)
# window.getMouse()

print(type(points[0]))

# for i in range(5):
#     point = random.randint(0, 2)
#     pointsDraw(window,points[point],xPrev,yPrev)
#     window.getMouse()
#     gr.time.sleep(0.01)

# window.getMouse()
window.close()



