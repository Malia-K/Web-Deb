def end_other(a, b):
    a = a.lower()
    b = b.lower()
    a_len= len(a)
    b_len= len(b)
    
    if a_len == b_len and a == b:
        return True
    elif a_len > b_len:
        return a.endswith(b)
    else:
        return b.endswith(a)
