import math
n = int(input())

ans = 0
while(True):
    if(math.pow(2, ans) >= n):
        print(ans)
        break
    ans += 1