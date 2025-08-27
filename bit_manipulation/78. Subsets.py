# Given an integer array nums of unique elements, return all possible subsets (the power set).

# The solution set must not contain duplicate subsets. Return the solution in any order.

# Example 1:

# Input: nums = [1,2,3]
# Output: [[],[1],[2],[1,2],[3],[1,3],[2,3],[1,2,3]]
# Example 2:

# Input: nums = [0]
# Output: [[],[0]]

def subsets(nums):
  n = len(nums)
  result = []
  for mask in range(1<<n): 
      subset = []
      for j in range(n): 
          if mask & (1<<j): 
              subset.append(nums[j])
      result.append(subset)
  return result

print(subsets([1,2,3]))