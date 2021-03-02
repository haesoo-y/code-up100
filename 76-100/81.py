n = int(input(), 16) # B
# print(n) # 11
xn = '%X'%n
# print(xn)  # B
for i in range(1, 16):
    xi = '%X'%i
    x_answer = '%X'%(n * i)
    print(xn + '*' + xi + '=' + x_answer)