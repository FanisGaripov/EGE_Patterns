for N in range(5, 10001):
    R = bin(N)[2:]
    if N % 3 == 0:
        R = R + R[-3] + R[-2] + R[-1]
    else:
        R += bin((N % 3) * 3)[2:]
    answ = int(R, 2)
    if answ >= 200:
        print(N)
        break