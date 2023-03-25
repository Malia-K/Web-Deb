n, m = map(int, input().split())
stack = []

for i in range(1, n-1, 2):
    string = '.|.'
    string = string * i 
    dash = '-' * int((m-len(string))/2)
    line = dash + string + dash
    print(line)
    stack.append(line)
    

print(str('-'*int((m - 7)/2)) + "WELCOME" + str('-'*int((m - 7)/2)))

for i in range(len(stack)):
    print(stack.pop())