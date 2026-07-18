# ◇
# Problem Statement
# Given an array of integers and a target sum S, count all subsets of the array whose elements sum equals S, and print the answer modulo 10^9+7.

# Constraints:
# - 1 <= N <= 1000 for DP/backtracking style inputs; use modulo where asked.
#    - Input is assumed valid unless the problem explicitly asks for validation.
#    - Use O(N) or better whenever a direct traversal solution exists.

# I/O format:
# - Input: N followed by N array elements. Extra values such as K/S are read after the array when needed.
# - Output: The answer required by the question.
# ◇
# Complexity
# Time
# O(N * S)
# Space
# O(S)
# DP over target sum S.

# ◇
# Examples & Test Cases
# Dry-run these inputs before reading the solution — each shows why the output is correct.

# Example 1
# Input
# 3 6
# 1 2 3
# Output
# 1
# Why this output? Only subset {1,2,3} sums to 6 (or count per problem).

# Example 2
# Input
# 4 5
# 2 2 1 3
# Output
# 2
# Why this output? Two subsets may sum to 5 depending on duplicates.
def subset(nums):
  result = []
  def generate_subset(nums,index,curr): 
    if len(nums) == index : 
      result.append(curr)
      return 
    
    generate_subset(nums,index+1,curr)
    generate_subset(nums,index+1,curr+[nums[index]])
  generate_subset(nums,0,[])
  return result 


input_arr = list(map(int,input().split()))
N = input_arr[0]
S = input_arr[1]

arr = list(map(int,input().split()))

result = subset(arr)

count = 0 
for res in result : 
  if sum(res) == S : 
    count += 1 

print(count)

# If you want to remove duplicate subsets


# def subset(nums):
#     result = set()

#     def generate_subset(index, curr):
#         if index == len(nums):
#             result.add(tuple(sorted(curr)))
#             return

#         generate_subset(index + 1, curr)
#         generate_subset(index + 1, curr + [nums[index]])

#     generate_subset(0, [])
#     return result

# result = subset(arr)

# count = 0
# for res in result:
#     if sum(res) == S:
#         count += 1

# print(count)