from string import ascii_uppercase, digits

alph = digits + ascii_uppercase
for x in range(29):
    s1 = '923' + alph[x] + '874'
    s2 = '524' + alph[x] + '6152'
    s = int(s1, 29) + int(s2, 29)
    if s % 28 == 0:
        print(s // 28)