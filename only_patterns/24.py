import string

f = open('24_23762.txt').read()
maxi_len = -float('inf')
maxi_stroka = ''
l = 0

def find_count(s):
    cnt = 0
    for j in s:
        if j == 'Y':
            cnt += 1
    return cnt

for r in range(len(f)):
    s = f[l:r + 1]
    print(f'{r} / {len(f)}')
    while find_count(s) > 80:
        l += 1
        s = f[l: r + 1]
    else:
        cnt = find_count(s)
        if s.count('2025') >= 90 and cnt == 80:
            if len(s) > maxi_len:
                maxi_len = len(s)
                maxi_stroka = ''
print(maxi_len)
print(maxi_stroka)