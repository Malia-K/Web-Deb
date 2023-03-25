def last2(str):
  if len(str) <= 2:
    return 0
    
  last2 = str[-2:]
#   print(last2)
  cnt = 0
  
  for i in range(len(str) - 2):
    if (str[i] + str[i + 1] == last2):
      cnt += 1
      
  return cnt
  
  
# str = input()
# print(last2(str))