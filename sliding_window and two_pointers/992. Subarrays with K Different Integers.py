# Given an integer array nums and an integer k, return the number of good subarrays of nums.

# A good array is an array where the number of different integers in that array is exactly k.

# For example, [1,2,3,1,2] has 3 different integers: 1, 2, and 3.
# A subarray is a contiguous part of an array.

# Example 1:
# Input: nums = [1,2,1,2,3], k = 2
# Output: 7
# Explanation: Subarrays formed with exactly 2 different integers: [1,2], [2,1], [1,2], [2,3], [1,2,1], [2,1,2], [1,2,1,2]

# Example 2:
# Input: nums = [1,2,1,3,4], k = 3
# Output: 3
# Explanation: Subarrays formed with exactly 3 different integers: [1,2,1,3], [2,1,3], [1,3,4].



# This question is solved by a mathematical formula 
# exactlyK(k) = atMostK(k) - atMostK(k-1)


from collections import defaultdict
def exactlyK(nums,k): 
  def atMostK(nums,k): 
    start , end , count  = 0 , 0 , 0 
    freq_map = defaultdict(int)
    
    while end < len(nums): 
      freq_map[nums[end]] += 1 
      while len(freq_map) > k : 
        freq_map[nums[start]] -= 1 
        if freq_map[nums[start]] == 0 : 
          del freq_map[nums[start]]
        start +=1 
      
      count += end - start + 1 
      end +=1  
    
    return count
    
  
  return atMostK(nums,k) - atMostK(nums,k-1)

print(exactlyK(nums = [1,2,1,3,4], k = 3))
  