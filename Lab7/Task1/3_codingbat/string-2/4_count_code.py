def count_code(str):
    alp = "abcdefghijklmnopqersuvwxuz"
    cnt = 0
    for c in alp:
        d  = "co" + c + "e"
        for i in range(len(str)-1):
            if str[i:i+4] == d:
                cnt += 1
                
    return cnt
