# Given an integer array nums, in which exactly two elements appear only once and all the other elements appear exactly twice. Find the two elements that appear only once. You can return the answer in any order.

# You must write an algorithm that runs in linear runtime complexity and uses only constant extra space.

 

# Example 1:

# Input: nums = [1,2,1,3,2,5]
# Output: [3,5]
# Explanation:  [5, 3] is also a valid answer.

# Example 2:
# Input: nums = [-1,0]
# Output: [-1,0]

# Example 3:
# Input: nums = [0,1]
# Output: [1,0]
 

# Constraints:

# 2 <= nums.length <= 3 * 104
# -231 <= nums[i] <= 231 - 1
# Each integer in nums will appear twice, only two integers will appear once.

def singleNumber3(nums): 
  xor_all = 0 
  for num in nums : 
    xor_all^=num 
  
  mask = xor_all & (-xor_all) #mask = the lowest bit where the two unique numbers differ. 
                              #It’s used to separate them into two groups so you can find each individually. 
                              
  group_a = 0 
  group_b = 0 
  
  for num in nums : 
    if (mask & num ) != 0 : 
      group_a^=num 
    else : 
      group_b^=num
    
  return [group_a,group_b]
  
  
nums= [1,2,3,2,1,5]
print(singleNumber3(nums))