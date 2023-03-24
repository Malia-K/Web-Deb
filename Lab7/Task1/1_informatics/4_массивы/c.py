n = int(input())
arr = list(input().split(" "))

cnt = 0

for i in arr:
    if(int(i) > 0):
        cnt += 1
    
print(cnt)
