def wrap(string, max_width):
    new_string = []

    for i in range(0, len(string)):
        if(i % max_width == 0 and i != 0):
            new_string.append("\n")
            
        new_string.append(string[i])
        
    return "".join(new_string)


string, max_width = input(), int(input())
result = wrap(string, max_width)
print(result)