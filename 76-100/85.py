w, h, b = map(int, input().split())

size = w * h * b

bit = 1
byte = 8*bit
KB = 1024 * byte
MB = 1024 * KB

print('%.2f'%(size/MB), 'MB')

