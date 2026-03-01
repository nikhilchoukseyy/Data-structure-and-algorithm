# The power of the string is the maximum length of a non-empty substring that contains only one unique character.

# Given a string s, return the power of s.

 

# Example 1:

# Input: s = "leetcode"
# Output: 2
# Explanation: The substring "ee" is of length 2 with the character 'e' only.
# Example 2:

# Input: s = "abbcccddddeeeeedcba"
# Output: 5
# Explanation: The substring "eeeee" is of length 5 with the character 'e' only.
 

# Constraints:

# 1 <= s.length <= 500
# s consists of only lowercase English letters.


def consChar(s): 
  i = 0 
  maxLength = 0 
  while i < len(s):
    j = i 
    length = 0 

    while j < len(s) and s[j] == s[i]: 
      length += 1
      j += 1 
    maxLength = max(maxLength,length)
    i = j 
  return maxLength

s = "abbcccddddeeeeedcba"
print(consChar(s))