def f(n):
    m = n
    R = []
    while m > 0:
        R.append(m % 11)
        m //= 11
    return R

for x in range(1, 3001):
    s = 9 * 11**210 + 8 * 11**150 - x
    R = f(s)
    if R.count(0) == 60:
        print(x)