# Question: First and Last Occurrence Using Binary Search
# Problem Statement

# You are given a sorted array of N integers and a target value X.

# Your task is to:

# Find the first occurrence of X in the array.
# Find the last occurrence of X in the array.
# Find the difference between the last and first occurrence indices.

# If the target element X is not present in the array, print -1.

# Note: The solution must be implemented using Binary Search with a time complexity of O(log N).

# Input Format
# The first line contains an integer N, the size of the array.
# The second line contains N space-separated integers in sorted order.
# The third line contains the target integer X.
# Output Format
# If X is present, print three space-separated integers:
# FirstOccurrence LastOccurrence Difference

# where

# FirstOccurrence = index of the first occurrence of X
# LastOccurrence = index of the last occurrence of X
# Difference = LastOccurrence - FirstOccurrence
# If X is not present, print:
# -1
# Constraints
# 1 ≤ N ≤ 10^5
# -10^9 ≤ Array[i] ≤ 10^9
# -10^9 ≤ X ≤ 10^9
# Sample Input 1
# 8
# 1 2 2 2 3 4 5 5
# 2
# Sample Output 1
# 1 3 2
# Explanation

# The target element 2 occurs at indices:

# 1, 2, 3
# First occurrence = 1
# Last occurrence = 3
# Difference = 3 - 1 = 2

# Hence the output is:

# 1 3 2
# Sample Input 2
# 6
# 1 3 5 7 9 11
# 8
# Sample Output 2
# -1
# Explanation

# The target element 8 is not present in the array, so the output is:

# -1

def solve():
  n = int(input())
  nums = list(map(int, input().split()))
  target = int(input())

  def first_occurence():
      low, high = 0, n - 1
      ans = -1

      while low <= high:
          mid = (low + high) // 2

          if nums[mid] == target:
              ans = mid
              high = mid - 1

          elif nums[mid] < target:
              low = mid + 1

          else:
              high = mid - 1

      return ans

  def last_occurence():
      low, high = 0, n - 1
      ans = -1

      while low <= high:
          mid = (low + high) // 2

          if nums[mid] == target:
              ans = mid
              low = mid + 1

          elif nums[mid] < target:
              low = mid + 1

          else:
              high = mid - 1

      return ans

  first = first_occurence()
  last = last_occurence()

  if first == -1:
      return -1

  return first, last, last - first


print(*solve())