# Шаблон для 16 задачи ЕГЭ по информатике


'''
Алгоритм вычисления значения функции 
F(n) и G(n), где n – целое число, задан следующими соотношениями:
F(n)=2×(G(n−3)+8);
G(n)=2×n, если n<10.
G(n)=G(n−2)+1, если n≥10.
Чему равно значение выражения F(15548)?
'''

'''Lru_cache'''
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

'''Динамическое решение'''
g = []
for n in range(15548):
    if n < 10:
        g.append(2 * n)
    else:
        g.append(g[n - 2] + 1)


def f(n):
    return 2 * (g[n - 3] + 8)

print(f(15548))