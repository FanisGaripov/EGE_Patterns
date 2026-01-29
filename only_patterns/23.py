def f(x, y):
    if x < y or x == 7: return 0
    if x > y: return f(x - 1, y) + f(x - 4, y) + f(x // 3, y)
    return 1

print(f(19, 13) * f(13, 2))