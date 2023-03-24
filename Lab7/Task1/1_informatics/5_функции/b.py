def power(a, n):
    ans = 1

    while(n):
        ans *= a
        n -= 1
    if(float(ans) == int(ans)):
        return int(ans)
    else:
        return float(ans)



a, n  = input().split()
print(power(float(a), float(n)))
