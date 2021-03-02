lst = []
for i in range(19):
    lst.append([])
    for j in range(19):
        lst[i].append(0)

n = int(input())
for _ in range(n):
    x, y = map(int, input().split())
    lst[x-1][y-1] = 1

for i in range(19):
    for j in range(19):
        print(lst[i][j], end=' ')
    print()