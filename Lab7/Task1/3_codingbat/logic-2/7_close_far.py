def close_far(a, b, c):
  if ( abs(b - c) >= 2 ) and ( (abs(b - a) <= 1 and abs(c - a) >= 2 ) or (abs(c- a) <= 1 and abs(b-a) >= 2 )):
    return True
    
  return False
