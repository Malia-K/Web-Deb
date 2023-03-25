# Enter your code here. Read input from STDIN. Print output to STDOut
nums = []
for i in range(4):
    x = int(input())
    nums.append(x)
    
print(pow(nums[0], nums[1]) + pow(nums[2], nums[3]))