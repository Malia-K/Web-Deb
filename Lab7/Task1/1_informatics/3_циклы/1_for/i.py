import math
x = int(input())

cnt = 0

for i in range(1, int(math.sqrt(x)) + 1):
    if(x % i == 0):
        cnt += 2


if(float(math.sqrt(x)) == int(math.sqrt(x))):
    print(cnt - 1)
else:
    print(cnt)