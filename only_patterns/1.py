# Шаблон для 1 задачи ЕГЭ по информатике
from itertools import *

s = '258 17 56 68 138 347 26 145'.split()
v = 'AC CB BH HD DA AG GC GE EF FH'.split()
print(*range(1, 9))
for p in permutations('ABCDEFGH'):
    if all(str(p.index(a) + 1) in s[p.index(b)] for a, b in v):
        print(*p)
        break