# Given an unsorted array arr[] of size n, containing elements from the range 1 to n, it is known that one number in this range is missing, and another number occurs twice in the array, find both the duplicate number and the missing number.

# Examples:
# Input: arr[] = [2, 2]
# Output: [2, 1]
# Explanation: Repeating number is 2 and the missing number is 1.

# Input: arr[] = [1, 3, 3] 
# Output: [3, 2]
# Explanation: Repeating number is 3 and the missing number is 2.

# Input: arr[] = [4, 3, 6, 2, 1, 1]
# Output: [1, 5]
# Explanation: Repeating number is 1 and the missing number is 5.

def array1stapproach(arr): #1st approach
  n = len(arr)
  missing = -1 
  repeated = -1 
  
  freq = [0]*(n+1) # space complexity O(n)
  
  for a in arr : # time complexity O(n)
    freq[a] += 1 
  
  for i in range(1,n+1): # time complexity O(n)
    if freq[i] == 0 : 
      missing = i 
    elif freq[i] == 2  : 
      repeated = i 
    
  return [repeated,missing]



def findTwoElement(self, arr): #2nd approach
  # code here
  n = len(arr)
      
  missing = -1 
  repeated = -1 
  
  for i in range(n): # time complexity O(n)
      val = abs(arr[i]) - 1 
      
      if arr[val] > 0 : 
          arr[val] = -arr[val]
      else : 
          repeated = val + 1 
      
      
  for i in range(n): # time complexity O(n)
      if arr[i] > 0 : 
          missing = i+1
          break
  
  return [repeated,missing] # space complexity O(1)


def findTwoElement(self, arr): #3rd approach
  # code here
  n = len(arr)
      
  xor_total = 0 

  for i in range(n): 
      xor_total ^=( arr[i]^(i+1))
      

  right_set_bit = xor_total & -(xor_total)

  x = 0 
  y = 0 

  for i in range(n): 
      if arr[i] & right_set_bit : 
          x^=arr[i]
      else : 
          y^=arr[i]
          
  for i in range(1,n+1):
      if i & right_set_bit : 
          x^=i 
      else : 
          y^= i 
      

  if arr.count(x) == 2 : 
      return (x,y)
  else: 
      return (y,x)