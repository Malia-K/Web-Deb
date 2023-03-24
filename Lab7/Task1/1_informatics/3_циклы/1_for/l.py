import math
str = input()
to_dec = 0
for i in range(0, len(str)):
    to_dec += int(str[i]) * math.pow(2, len(str) - i - 1)


print(int(to_dec))