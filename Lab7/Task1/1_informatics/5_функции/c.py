def  xor(x, y):
    if((x == 1 and  y != 1) or (x != 1 and y == 1)):
        return 1
    return 0

x, y = input().split()

print(xor(int(x), int(y)))