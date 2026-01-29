from math import dist
from turtle import *

f = open('27_A_23766.txt')
points = [list(map(float, r.replace(',', '.').split())) for r in f]
clusters = []
eps = 2
while points:
    clusters.append([points[0]])
    del points[0]
    for p1 in clusters[-1]:
        for p2 in points[:]:
            if dist(p1, p2) < eps:
                clusters[-1].append(p2)
                points.remove(p2)

def centroid(cluster):
    c = []
    for x1, y1 in cluster:
        c += [[sum(dist([x1, y1], [x2, y2]) for x2, y2 in cluster), (x1, y1)]]
    return min(c)[1]


def visual(clusters):
    tracer(0); screensize(2000, 2000); penup();
    colors = ['red', 'green', 'blue']
    k = 30
    for i in range(len(clusters)):
        for x, y in clusters[i]:
            goto(x * k, y * k)
            dot(3, colors[i])
    update()
    done()


centr0 = centroid(clusters[0])
centr1 = centroid(clusters[1])
p_x = min([x for x, y in (centr0, centr1)])
p_y = min([y for x, y in (centr0, centr1)])
print(int(p_x * 10000), int(p_y * 10000))