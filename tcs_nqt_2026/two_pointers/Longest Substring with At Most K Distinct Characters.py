# TCS NQT Problem

# Given a string S and an integer K, find the length of the longest substring containing at most K distinct characters.

# Input Format
# S
# K
# Output Format
# Length of longest substring
# Example
# Input
# eceba
# 2
# Output
# 3

# Explanation:

# ece

# contains only

# e
# c

# 2 distinct characters.

from collections import Counter
def solve(): 
  text = input().strip()
  k = int(input())
  freq= Counter()
  left = 0 
  ans = 0 
  for right in range(len(text)): 
    freq[text[right]] += 1 

    while len(freq) > k : 
      freq[text[left]] -= 1 
      if freq[text[left]] == 0 : 
        del freq[text[left]]
      left += 1 
    ans = max(ans,right-left + 1 )
  return ans 

print(solve())
