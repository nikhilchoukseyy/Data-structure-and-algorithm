# Given an array of integers arr[] and a number k, count the number of subarrays having XOR of their elements as k.

# Examples: 
# Input: arr[] = [4, 2, 2, 6, 4], k = 6
# Output: 4
# Explanation: The subarrays having XOR of their elements as 6 are [4, 2], [4, 2, 2, 6, 4], [2, 2, 6], and [6]. Hence, the answer is 4.

# Input: arr[] = [5, 6, 7, 8, 9], k = 5
# Output: 2
# Explanation: The subarrays having XOR of their elements as 5 are [5] and [5, 6, 7, 8, 9]. Hence, the answer is 2.

# Input: arr[] = [1, 1, 1, 1], k = 0
# Output: 4
# Explanation: The subarrays are [1, 1], [1, 1], [1, 1] and [1, 1, 1, 1].


def subArrayXor(nums,k): 
  n = len(nums)
  count = 0 
  prefXor = 0 
  map = {}
  for i in range(n): 
    prefXor^=nums[i]
    
    count += map.get(prefXor^k,0)
    
    if prefXor == k : 
      count += 1
    
    map[prefXor] = map.get(prefXor,0) + 1
    
  return count 

print(subArrayXor(nums = [4, 2, 2, 6, 4],k = 6 ))