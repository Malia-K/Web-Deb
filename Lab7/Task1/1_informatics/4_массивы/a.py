n = int(input())

# for i in range(0, n):
arr = list(input().split(" "))
# print(arr)

for i in range(0, len(arr)):
    if(i % 2 == 0):
        print(arr[i], end=" ")