def insertion(nums):
              for i in range(len(nums)):
                            key=nums[i]
                            j=i-1
                            while j>=0 and key < nums[j]:
                                          nums[j+1]=nums[j]
                                          j-=1
                                          nums[j+1]=key
nums=[8,6,9,3,4,1]
insertion(nums)
print("sorted arry")
for i in range(len(nums)):
              print(nums[i],end=" ")
              
                                          
