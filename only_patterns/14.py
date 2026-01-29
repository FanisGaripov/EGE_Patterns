def f(n):
    m = n
    R = []
    while m > 0:
        R.append(m % 27)
        m //= 27
    return R


s = 2 * 2187**2020 + 729**2021 - 2 * 243**2022 + 81**2023 - 2 * 27**2024 - 6561
r = f(s)
k = 0
for i in r:
    if i > 9:
        k += 1
print(k)