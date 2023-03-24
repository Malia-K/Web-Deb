n = int(input())
zero_cnt = 0

for i in range(0, n):
    x = int(input())
    if( x == 0):
        zero_cnt += 1

print(zero_cnt)