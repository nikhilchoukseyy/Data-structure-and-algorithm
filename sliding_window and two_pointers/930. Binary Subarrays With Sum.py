# Given a binary array nums and an integer goal, return the number of non-empty subarrays with a sum goal.

# A subarray is a contiguous part of the array.

# Example 1:
# Input: nums = [1,0,1,0,1], goal = 2
# Output: 4
# Explanation: The 4 subarrays are bolded and underlined below:
# [1,0,1,0,1]
# [1,0,1,0,1]
# [1,0,1,0,1]
# [1,0,1,0,1]

# Example 2:
# Input: nums = [0,0,0,0,0], goal = 0
# Output: 15

from collections import defaultdict
def numSubarraysWithSum(nums,goal): 
  count_map = defaultdict(int)
  count_map[0] = 1 
  curr_sum = 0 
  result = 0 
  
  for num in nums : 
    curr_sum += num 
    if (curr_sum - goal) in count_map : 
      result += count_map[curr_sum-goal] 
    count_map[curr_sum] += 1 

  return result 

print(numSubarraysWithSum(nums = [0,0,0,0,0], goal = 0))