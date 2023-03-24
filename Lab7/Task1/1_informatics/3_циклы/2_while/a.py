import math
n = int(input())

x = 1
while(x <= n):
    if(math.sqrt(x * 1.0) == int(math.sqrt(x))):
        print(x)
    x += 1