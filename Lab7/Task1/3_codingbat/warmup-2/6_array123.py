def array123(nums):
  for i in range(len(nums)):
    if(nums[i] == 2 and (i - 1 >= 0) and (i + 1 < len(nums)) and nums[i - 1] == 1 and nums[i + 1] == 3 ):
      return True
  return False
    
