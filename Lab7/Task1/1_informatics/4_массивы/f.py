n = int(input())

arr = list(input().split())
arr = [int(i) for i in arr]


cnt = 0

for i in range(0, len(arr)):
    if(i != 0 and i != len(arr) - 1):
        if(arr[i] > arr[i - 1] and arr[i] > arr[i + 1]):
            cnt += 1

print(cnt)