# Find all valid combinations of k numbers that sum up to n such that the following conditions are true:

# Only numbers 1 through 9 are used.
# Each number is used at most once.
# Return a list of all possible valid combinations. The list must not contain the same combination twice, and the combinations may be returned in any order.

 

# Example 1:
# Input: k = 3, n = 7
# Output: [[1,2,4]]
# Explanation:
# 1 + 2 + 4 = 7
# There are no other valid combinations.

# Example 2:
# Input: k = 3, n = 9
# Output: [[1,2,6],[1,3,5],[2,3,4]]
# Explanation:
# 1 + 2 + 6 = 9
# 1 + 3 + 5 = 9
# 2 + 3 + 4 = 9
# There are no other valid combinations.

# Example 3:
# Input: k = 4, n = 1
# Output: []
# Explanation: There are no valid combinations.
# Using 4 different numbers in the range [1,9], the smallest sum we can get is 1+2+3+4 = 10 and since 10 > 1, there are no valid combination.
 
class Solution:
    def combinationSum3(self, k: int, n: int):

#intutive approach 
        result = []
        nums = [1,2,3,4,5,6,7,8,9]
        def backtrack(index,current): 
 
            if len(current) == k : 
                if sum(current) == n : 
                    result.append(current[:])
                    return 

            if index >= len(nums) : 
                return

            backtrack(index+1,current)

            current.append(nums[index])
            backtrack(index+1,current)
            current.pop()
            

        backtrack(0,[])
        return result 

#better approach 
        result = [] 

        def backtrack(start,target,k,path): 
            if target == 0 and k ==  0: 
                result.append(path[:])
                return 
            
            for i in range(start,10):
                if i > target or k <=0 : 
                    break 

                path.append(i) 
                backtrack(i+1 , target-i,k-1,path)
                path.pop()
        
        backtrack(1,n,k,[])
        return result
