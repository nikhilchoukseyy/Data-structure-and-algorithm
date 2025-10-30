# Given a string s consisting only of characters a, b and c.

# Return the number of substrings containing at least one occurrence of all these characters a, b and c.

# Example 1:
# Input: s = "abcabc"
# Output: 10
# Explanation: The substrings containing at least one occurrence of the characters a, b and c are "abc", "abca", "abcab", "abcabc", "bca", "bcab", "bcabc", "cab", "cabc" and "abc" (again). 

# Example 2:
# Input: s = "aaacb"
# Output: 3
# Explanation: The substrings containing at least one occurrence of the characters a, b and c are "aaacb", "aacb" and "acb". 

# Example 3:
# Input: s = "abc"
# Output: 1

def numOfSubstring(s): 
  left , right , n , a , b , c , result  = 0 , 0 , len(s) , 0 , 0 , 0 , 0 
  
  while right < n : 
    if s[right] == 'a': 
      a+=1
    elif s[right] == 'b': 
      b+=1 
    else : 
      c +=1 
    
    while a > 0 and b > 0 and c > 0 : 
      result += (n-right)
      if s[left] == 'a': 
        a-=1
      elif s[left] == 'b': 
        b-=1 
      else : 
        c -=1 
      left += 1 
      
    right +=1 
    
  return result 

print(numOfSubstring(s = "aaacb"))