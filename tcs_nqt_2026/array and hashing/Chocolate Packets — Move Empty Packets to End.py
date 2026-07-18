# Chocolate Packets — Move Empty Packets to End
# PYQ
# Easy
# O(N)
# Array
# Two Pointers
# Verified PYQ

# Previous
# 03 · 3 / 72

# Next
# ◇
# Problem Statement
# A factory produces N chocolate packets. Empty (defective) packets are represented as 0. Push all empty packets (0s) to the end of the array while maintaining the relative order of non-zero packets.

# Constraints:
# - 1 <= N <= 100000 unless the statement says a smaller limit.
#    - Input is assumed valid unless the problem explicitly asks for validation.
#    - Use O(N) or better whenever a direct traversal solution exists.

# I/O format:
# - Input: N followed by N array elements. Extra values such as K/S are read after the array when needed.
# - Output: The answer required by the question.
# ◇
# Complexity
# Time
# O(N)
# Space
# O(1)
# Single pass reordering (two pointers).

# ◇
# Examples & Test Cases
# Dry-run these inputs before reading the solution — each shows why the output is correct.

# Example 1
# Input
# 5
# 1 0 2 0 3
# Output
# 1 2 3 0 0
# Why this output? Non-zeros keep order; zeros shift right.

# Example 2
# Input
# 4
# 0 4 0 1
# Output
# 4 1 0 0
# Why this output? Same rule for any arrangement.

# N = int(input())
# arr = list(map(int,input().split()))

# empty_arr = []
# nonempty_arr = []

# for num in arr : 
#   if num == 0 : 
#     empty_arr.append(num)
#   else : 
#     nonempty_arr.append(num)

# print(*(nonempty_arr+empty_arr))


# two pointer approach 
N = int(input())
arr = list(map(int,input().split()))
j= 0 
for i in range(len(arr)): 
  if arr[i] != 0 : 
    arr[i],arr[j] = arr[j],arr[i]
    j += 1 
  
print(*arr)