f = open('9.txt')
s = []
for i in range(42000):
    s.append(list(map(int, f.readline().split())))
for i in s:
    f = False
    repeated = 0
    summa = 0
    for j in i:
        if i.count(j) == 3:
            f = True
            repeated = j
        elif i.count(j) == 2 or i.count(j) > 3:
            f = False
            repeated = 0
            break
    if f:
        for l in i:
            if l != repeated:
                summa += l
        if summa / 4 <= repeated:
            print(sum(i))

