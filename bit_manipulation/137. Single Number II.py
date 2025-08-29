# Given an integer array nums where every element appears three times except for one, which appears exactly once. Find the single element and return it.

# You must implement a solution with a linear runtime complexity and use only constant extra space.

# Example 1:
# Input: nums = [2,2,3,2]
# Output: 3


# Example 2:
# Input: nums = [0,1,0,1,0,1,99]
# Output: 99

def singleNumber(nums):
    result = 0 
    for i in range(32): 
        ones_bit = 0 
        for num in nums : 
            if (num>>i) & 1: 
                ones_bit += 1
        if ( ones_bit % 3 ) == 1: 
            result |= (1<<i)

    if result >= 2**31:
        result -= 2**32
    
    return result

nums = [3,2,3,3]
print(singleNumber(nums))