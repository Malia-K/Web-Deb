def caught_speeding(speed, is_birthday):
  speed = speed - (65 if is_birthday else 60)
  if speed > 20:
    return 2
  elif speed > 0:
    return 1
  else:
    return 0
