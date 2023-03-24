def min (a,b,c,d):
    arr = []
    arr.append(a)
    arr.append(b)
    arr.append(c)
    arr.append(d)
    min_num = a
    for i in arr:
        if(i < min_num):
            min_num = i
    
    return min_num

a, b, c ,d = input().split()

print(min(a,b,c,d))