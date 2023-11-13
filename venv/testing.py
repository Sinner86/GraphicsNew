import graphics as gr
import random

def ran_f(max = 500):
    x = random.randint(0, max)
    y = random.randint(0, max)
    list = [x,y]
    return list

pole = {'point1':[ran_f()[0], ran_f()[1]], 'point2':[ran_f()[0], ran_f()[1]],'point3':[ran_f()[0], ran_f()[1]]}
print(pole.items())