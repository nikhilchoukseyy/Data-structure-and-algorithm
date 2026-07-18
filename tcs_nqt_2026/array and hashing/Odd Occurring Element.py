# Given an array of integers where every element appears an even number of times except one element which appears an odd number of times, find that odd-occurring element in O(log N) time. Equal elements appear in pairs and no element appears more than two times consecutively.

# Constraints:
# - 1 <= N <= 1000 for DP/backtracking style inputs; use modulo where asked.
#    - Input is assumed valid unless the problem explicitly asks for validation.
#    - Use O(N) or better whenever a direct traversal solution exists.

# I/O format:
# - Input: N followed by N array elements. Extra values such as K/S are read after the array when needed.
# - Output: The answer required by the question.◇
# Examples & Test Cases
# Dry-run these inputs before reading the solution — each shows why the output is correct.

# Example 1
# Input
# 5
# 1 1 2 2 3
# Output
# 3
# Why this output? 3 appears once; pairs cancel — binary search finds the odd one.

# Example 2
# Input
# 7
# 4 4 7 8 8 9 9
# Output
# 7
# Why this output? Only 7 has odd frequency in sorted pair layout.


N = int(input())
arr = list(map(int,input().split()))
num = arr[0]
for i in range(1,N) : 
   num^=arr[i]
  
print(num)

