# Problem

# Given a sorted array and Q queries, print the index of each queried element. If it doesn't exist, print -1.

# Input
# 7
# 2 5 8 10 14 19 25
# 3
# 10
# 19
# 7
# Output
# 3
# 5
# -1
# Skills Tested
# Standard Binary Search
# Multiple Queries

def solve(): 
  n = int(input())
  nums = list(map(int,input().split()))
  k = int(input())
  result = []
  for i in range(k): 
    num = int(input())
    result.append(num)
  return nums , result 

def binarySearch(nums,target): 
  if not nums : 
    return -1 
  n = len(nums)

  low , high = 0 , n -1 
  while low <= high : 
    mid  = (low+high)//2 
    if nums[mid] == target : 
      return mid 
    elif nums[mid] < target: 
      low = mid + 1 
    else : 
      high = mid - 1
  return -1 



nums , targets = solve()
for target in targets : 
  print(binarySearch(nums,target))
