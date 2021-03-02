h, w = map(int, input().split())
lst = []
for i in range(h):
    lst.append([])
    for j in range(w):
        lst[i].append(0)

n = int(input())
for _ in range(n):
    l, d, x, y = map(int, input().split())
    x = x-1
    y = y-1
    if d == 0 :
        for i in range(l):
            lst[x][y+i] = 1
    else :
        for i in range(l):
            lst[x+i][y] = 1

for i in range(h):
    for j in range(w):
        print(lst[i][j], end=' ')
    print()