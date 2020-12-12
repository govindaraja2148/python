def Bubble(nums):
    for i in range(len(nums)-1,0,-1):
        for j in range(i):
            if nums[j]> nums[j+1]:
                temp = nums[j]
                nums[j] = nums[j+1]
                nums[j+1] = temp
nums=[22,11,55,44,88,2,1]
Bubble(nums)
print(nums)
