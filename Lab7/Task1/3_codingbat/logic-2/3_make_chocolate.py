def make_chocolate(small, big, goal):
  big_sum = big * 5
  
  if  goal >= big_sum:
    cnt_small = goal - big_sum
  else:
    cnt_small = goal % 5
    
  if cnt_small > small:
    return -1
  else:
    return cnt_small


s,b,g = map(int, input().split())
print(make_chocolate(s,b,g))