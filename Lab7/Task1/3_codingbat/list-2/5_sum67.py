def sum67(nums):
    sum = 0
    is_six= False
  
    for i in range(len(nums)):
        if nums[i] == 6:
            is_six= True
        if not is_six:
            sum += nums[i]
        if nums[i] == 7 and is_six:
            is_six= False
    return sum