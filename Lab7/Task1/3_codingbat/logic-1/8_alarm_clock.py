def alarm_clock(day, vacation):
  weekday = "10:00" if vacation else "7:00"  
  weekend = "off"   if vacation else "10:00" 
  
  if day in range(1,6):
    return weekday
  
  return weekend
 