# Given an array of integers, find the maximum sum of any contiguous subarray of size K.
# arr = [2, 1, 5, 1, 3, 2], K = 3
# [2, 1, 5] → 8
# [1, 5, 1] → 7
# [5, 1, 3] → 9
# [1, 3, 2] → 6
# ✅ Answer = 9

def maxSumSubarray(arr,k): 
  l = 0 
  n = len(arr)
  maxSum = float('-inf')
  windowSum = 0 
  
  for r in range(n): 
    windowSum += arr[r]
    if r >= (k-1): 
      maxSum = max(maxSum , windowSum)
      windowSum -= arr[l]
      l+=1
    
  return maxSum 

print(maxSumSubarray(arr = [2, 1, 5, 1, 3, 2], k= 3))