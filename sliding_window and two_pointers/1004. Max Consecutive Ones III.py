# Given a binary array nums and an integer k, return the maximum number of consecutive 1's in the array if you can flip at most k 0's.

# Example 1:
# Input: nums = [1,1,1,0,0,0,1,1,1,1,0], k = 2
# Output: 6
# Explanation: [1,1,1,0,0,1,1,1,1,1,1]
# Bolded numbers were flipped from 0 to 1. The longest subarray is underlined.

# Example 2:
# Input: nums = [0,0,1,1,0,0,1,1,1,0,1,1,0,0,0,1,1,1,1], k = 3
# Output: 10
# Explanation: [0,0,1,1,1,1,1,1,1,1,1,1,0,0,0,1,1,1,1]
# Bolded numbers were flipped from 0 to 1. The longest subarray is underlined.

def maxConsOnes3(nums,k): 
  
#Brute force solution nested loops , TC = O(n^2) 
  res = 0 
  for i in range(len(nums)):
    count = 0  
    for j in range(i,len(nums)): 
      if nums[j] == 0 : 
        count +=1 
      if count <= k : 
        res = max(res,j-i+1)
  return res 

#sliding window solution , TC = O(n)
  start = 0 
  end = 0  
  result = 0 
  count = 0 
  while end < len(nums): 
    if nums[end] == 0 : 
      count += 1 
    
    while count > k : 
      if nums[start] == 0 : 
        count -=1 
      start +=1 
      
    result = max(result,end-start+1)
    
    end += 1 
    
  return result 

print(maxConsOnes3(nums = [0,0,1,1,0,0,1,1,1,0,1,1,0,0,0,1,1,1,1], k = 3))