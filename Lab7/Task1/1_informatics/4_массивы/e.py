n = int(input())

arr = list(input().split())

arr = [int(i) for i in arr]
isPaired = False

for i in range(0, len(arr)):
    if(i != len(arr) - 1):
        if((arr[i] > 0 and  arr[i + 1] > 0) or (arr[i] < 0 and  arr[i + 1] < 0)):
            isPaired = True
            break

if(isPaired):
    print("YES")
else:
    print("NO")