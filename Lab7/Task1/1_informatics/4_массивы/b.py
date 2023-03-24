n = int(input())

arr = list(input().split(" "))

for i in arr:
    if(int(i) % 2 == 0):
        print(i, end = " ")
