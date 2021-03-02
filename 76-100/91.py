x, y, z = map(int, input().split())
day = max(x, y, z)
while(True):
    if day%x == 0 and day%y == 0 and day%z == 0 :
        break
    day += 1
print(day)