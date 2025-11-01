# Given an array of positive integers nums and a positive integer target, return the minimal length of a subarray whose sum is greater than or equal to target. If there is no such subarray, return 0 instead.

# Example 1:
# Input: target = 7, nums = [2,3,1,2,4,3]
# Output: 2
# Explanation: The subarray [4,3] has the minimal length under the problem constraint.

# Example 2:
# Input: target = 4, nums = [1,4,4]
# Output: 1

# Example 3:
# Input: target = 11, nums = [1,1,1,1,1,1,1,1]
# Output: 0

def minSizeSubarraySum(target,nums):
  left = 0 
  right = 0 
  minSum = float('inf')
  windowSum = 0 
  
  while right < len(nums): 
    windowSum += nums[right]
    while windowSum >= target : 
      minSum = min(minSum, right - left + 1)
      windowSum -= nums[left]
      left += 1 
    right +=1  
  return minSum if minSum != float('inf') else 0 

print(minSizeSubarraySum(target = 7, nums = [2,3,1,2,4,3]))