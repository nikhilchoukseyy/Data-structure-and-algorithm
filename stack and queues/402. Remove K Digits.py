# Given string num representing a non-negative integer num, and an integer k, return the smallest possible integer after removing k digits from num.

# Example 1:
# Input: num = "1432219", k = 3
# Output: "1219"
# Explanation: Remove the three digits 4, 3, and 2 to form the new number 1219 which is the smallest.

# Example 2:
# Input: num = "10200", k = 1
# Output: "200"
# Explanation: Remove the leading 1 and the number is 200. Note that the output must not contain leading zeroes.

# Example 3:
# Input: num = "10", k = 2
# Output: "0"
# Explanation: Remove all the digits from the number and it is left with nothing which is 0.


def removeKdigits(num,k): 
  n = len(num)
  
  if n == k : 
    return "0"

  stack = []
  
  for i in range(len(num)): 
    while stack and stack[-1] > num[i] and k > 0: 
      stack.pop()
      k -= 1 
    
    stack.append(num[i])
  
  while k > 0 : 
    stack.pop()
    k -= 1 
  
  result = "".join(stack).lstrip("0") # convert into string and remove leading zeros 
  
  return result if result else "0" # for cases like num = 12344678 , k = 3
  
num = "1432219"
k = 3 
print(removeKdigits(num,k))
