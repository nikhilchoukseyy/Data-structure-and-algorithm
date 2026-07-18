def findKey(): 
  n = int(input())
  nums = list(map(int, input().split()))
  key = int(input())

  low = 0
  high = n - 1

  while low <= high:
      mid = (low + high) // 2

      if nums[mid] == key:
          return nums[mid]
      elif nums[mid] < key:
          low = mid + 1
      else:
          high = mid - 1

  if high < 0:
      return nums[0]

  if low >= n:
      return nums[-1]

  if key - nums[high] <= nums[low] - key:
      return nums[high]      # smaller element on tie

  return nums[low] 

print(findKey())