# Problem

# Given a string.

# Ignore spaces and case.

# Check whether it is a palindrome.

# Input
# A man a plan a canal Panama
# Output
# YES

# Another

# race a car

# Output

# NO


s = input().replace(" ","")
s = s.lower()

left , right = 0 , len(s)-1
palindrome = True
while left < right : 
  if s[left] != s[right]: 
    palindrome = False 
  left +=  1 
  right -= 1 
if palindrome : 
  print("YES")
else : 
  print("NO")


