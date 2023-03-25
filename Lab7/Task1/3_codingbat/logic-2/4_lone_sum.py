def lone_sum(a, b, c):
  sum = 0
  sum += 0 if a in [b,c] else a
  sum += 0 if b in [a,c] else b
  sum += 0 if c in [a,b] else c
  return sum
