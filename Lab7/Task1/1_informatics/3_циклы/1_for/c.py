import math

a = int(input())
b = int(input())

for i in range(a, b + 1):
    # print( i ,math.sqrt(i * 1.0), int(math.sqrt(i)))
    if(math.sqrt(i * 1.0)) == int(math.sqrt(i)):
        print(i)