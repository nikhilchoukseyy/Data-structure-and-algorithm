def nextGreaterElement(): 
  n = int(input()) 
  nums = list(map(int,input().split()))
  result = [-1]*n
  stack = []
  for i in range(n-1,-1,-1): 
    while stack and stack[-1] <= nums[i] : 
      stack.pop()
    if stack : 
      result[i] = stack[-1]
    stack.append(nums[i])
  
  return result 

print(nextGreaterElement())

