n = int(input())

arr = list(input().split())

cnt = 0

for i in range(0, len(arr)):
    if i == 0:
        continue
    if(int(arr[i]) > int(arr[i-1])):
        cnt += 1

print(cnt)