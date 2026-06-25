#leetcode 2574:
# nums=[10,4,8,3]
# sum1=sum(nums)
# l=[]
# left=0
# for i in range(len(nums)):
#      x=abs(left-(sum1-nums[i]-left))
#      l.append(x)
#      left+=nums[i]
# print(l)

# slicing left and right sum difference:

# nums=[10,4,8,3]
# l=[]
# for i in range(len(nums)):
#      x=sum(nums[:i])
#      y=sum(nums[i+1:])
#      l.append(abs(x-y))
# print(l)     