# Шаблон для 2 задачи ЕГЭ по информатике


# 1 вариант
from itertools import *

print('x y z w')
for x, y, z, w in product([0, 1], repeat=4):
    f = (x or y) and (not(y == z)) and (not(w))
    if f:
        print(x, y, z, w)


# 2 вариант
print('x y z w')
for x in 0, 1:
    for y in 0, 1:
        for z in 0, 1:
            for w in 0, 1:
                f = (x or y) and (not(y == z)) and (not(w))
                if f:
                    print(x, y, z, w)