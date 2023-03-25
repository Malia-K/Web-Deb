def lucky_sum(a, b, c):
  sum = 0
  li = [a,b,c]
  for i in li:
    if(i == 13):
      break
    sum += i
  return sum

