P = range(25, 65)
Q = range(40, 116)
for a in range(1, 1000):
    A = range(40, a)
    flag = 0
    for x in range(-500, 500):
        f = (x in P) <= (((x in Q) and (not(x in A))) <= (not(x in P)))
        if f:
            flag += 1
    if flag == 1000:
        print(list(A))
        print(len(list(A)))
        break