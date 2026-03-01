#Two Sums

# Given an array of integers nums and an integer target, return indices of the two numbers such that they add up to target.
#
# You may assume that each input would have exactly one solution, and you may not use the same element twice.
#
# You can return the answer in any orde

def twoSum(nums , target):
    """Return the position of  list the sum up to the target."""
    for i in range(0,len(nums)):
        value = nums[i]
        for j in range(i+1,len(nums)):
            if value+nums[j]==target:
                return [i,j]
    return []

#Test Cases
print(twoSum(nums = [2,7,11,15], target = 9))
print(twoSum(nums = [3,2,4], target = 6))
print(twoSum(nums = [3,3], target = 6))