# Given an integer array nums of unique elements, return all possible subsets (the power set).
# The solution set must not contain duplicate subsets. Return the solution in any order.

# Example 1:
# Input: nums = [1,2,3]
# Output: [[],[1],[2],[1,2],[3],[1,3],[2,3],[1,2,3]]

# Example 2:
# Input: nums = [0]
# Output: [[],[0]]

class Solution:
    def subsets(self, nums):
        result = []
        def generate_subsets(nums,index=0 , curr = []): 
            if index == len(nums): 
                result.append(curr)
                return 
            
            generate_subsets(nums,index+1,curr) 

            generate_subsets(nums,index+1,curr + [nums[index]])
        
        generate_subsets(nums,0,[])
        return result