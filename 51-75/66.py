x, y, z = map(int, input().split())
for i in (x, y, z):
    if i % 2 == 0 :
        print('even')
    else :
        print('odd')