f = open('26_23765.txt')
N = int(f.readline())
s = []
for _ in range(N):
    s.append(list(map(int, f.readline().split())))
spisok = []
s_copy = s[:]
for l, r in s:
    spisok.append(l)
    spisok.append(r)
spisok.sort()
rating_start = []
rating_end = []
for i in spisok:
    for j in s:
        if i in j:
            if i == j[0]:
                rating_start.append([j[0], j[1]])
                spisok.remove(j[1])
            else:
                rating_end.append([j[0], j[1]])
                spisok.remove(j[0])
print(s_copy.index(rating_end[-1]) + 1)
print(len(rating_end) - 1)
