def squirrel_play(temp, is_summer):
  if temp in range(60, 91) or (is_summer and temp in range(60, 101)):
    return True
  return False
