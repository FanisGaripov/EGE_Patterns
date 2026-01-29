from functools import lru_cache

@lru_cache(maxsize=None)
def G(n):
    if n < 10:
        return 2 * n
    else:
        return G(n - 2) + 1


def F(n):
    return 2 * (G(n - 3) + 8)

for i in range(16000):
    G(i)

print(F(15548))