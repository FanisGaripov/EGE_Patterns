from itertools import *


for num, p in enumerate(product('АКОРСТ', repeat=5), 1):
    s = ''.join(p)
    if num % 2 == 0:
        if s.count('О') == 2 and s[0] not in 'АСТ':
            print(f'{num}) {s}')