# Given an integer array nums of unique elements, return all possible subsets (the power set).

# The solution set must not contain duplicate subsets. Return the solution in any order.

# Example 1:

# Input: nums = [1,2,3]
# Output: [[],[1],[2],[1,2],[3],[1,3],[2,3],[1,2,3]]
# Example 2:

# Input: nums = [0]
# Output: [[],[0]]

def subset(nums): 
    result = []
    n = len(nums)
    for mask in range(1<<n): 
        res = []
        for i in range(n): 
            if mask & (1<<i): 
                res.append(nums[i])
        result.append(res)
    return result

print(subset([1,2,3]))