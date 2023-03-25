def in1to10(n, outside_mode):
  if (n in range(1,11) and outside_mode != True) or (outside_mode and (n <= 1 or n >= 10)) :
    return True
  return False