def front_back(str):
  if len(str) <= 1:
    return str
    
  li = list(str)
  front = li[0]
  back  = li[-1]
  
  li[0] = back
  li[-1] = front
  
  return "".join(li)

