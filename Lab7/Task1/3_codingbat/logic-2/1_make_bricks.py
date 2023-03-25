def make_bricks(small, big, goal):
  temp = goal
  temp -= 5 * min(big, goal/5)
  
  return temp - small <= 0
