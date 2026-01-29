def all_divisors(n):
    divs = []
    for i in range(2, int(n / 2) + 1):
        if n % i == 0:
            divs.append(i)
    return divs

k = 0
for i in range(800_001, 1000_000):
    divisors = all_divisors(i)
    if len(divisors) >= 2:
        M = min(divisors) + max(divisors)
        if str(M)[-1] == '4':
            if k < 5:
                print(i, M)
                k += 1
            else:
                break