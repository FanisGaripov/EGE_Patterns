from math import dist
from turtle import *

f = open('27_B_23766.txt')
points = [list(map(float, r.replace(',', '.').split())) for r in f]
clusters = []
eps = 3
while points:
    clusters.append([points[0]])
    del points[0]
    for p1 in clusters[-1]:
        for p2 in points[:]:
            if dist(p1, p2) < eps:
                clusters[-1].append(p2)
                points.remove(p2)
    if len(clusters[-1]) <= 3:
        del clusters[-1]

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
centr2 = centroid(clusters[2])
centrs = [centr0, centr1, centr2]
maxi = -float('inf')
print(len(clusters[0]), len(clusters[1]), len(clusters[2]))
q1 = int(dist(centr0, centr1) * 10000)
for i in range(3):
    for p2 in clusters[i]:
        if dist(centrs[i], p2) > maxi:
            maxi = dist(centrs[i], p2)
q2 = int(maxi * 10000)
print(q1, q2)