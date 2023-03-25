n = int(input())
arr = list(map(int, input().split()))
arr = sorted(arr)

max = arr[0]
runner_up = max

for i in arr:
    if(i > max):
        runner_up = max
        max = i

print(runner_up)
