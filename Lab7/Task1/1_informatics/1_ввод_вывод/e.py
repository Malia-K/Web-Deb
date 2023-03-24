v = int(input())
t = int(input())

s = abs(v) * t
mod = s % 109

if(mod == 0):
    print(0)
else:
    if(v < 0):
        print(109 - mod)
    elif(v > 0):
        print(mod)


