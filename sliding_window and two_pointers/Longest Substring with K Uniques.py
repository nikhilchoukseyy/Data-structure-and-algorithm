# You are given a string s consisting only lowercase alphabets and an integer k. Your task is to find the length of the longest substring that contains exactly k distinct characters.

# Note : If no such substring exists, return -1. 

# Examples:
# Input: s = "aabacbebebe", k = 3
# Output: 7
# Explanation: The longest substring with exactly 3 distinct characters is "cbebebe", which includes 'c', 'b', and 'e'.
# Input: s = "aaaa", k = 2
# Output: -1
# Explanation: There's no substring with 2 distinct characters.
# Input: s = "aabaaab", k = 2
# Output: 7
# Explanation: The entire string "aabaaab" has exactly 2 unique characters 'a' and 'b', making it the longest valid substring.

from collections import defaultdict
def longSubKUnique(s,k): 
  start , end = 0 , 0 
  maxLen = 0 
  freq_map = defaultdict(int)
  
  while end < len(s): 
    freq_map[s[end]] +=1 
    
    while len(freq_map) > k : 
      freq_map[s[start]] -=1 
      if freq_map[s[start]] == 0 : 
        del freq_map[s[start]]
      start +=1 
      
    if len(freq_map) == k : maxLen = max(maxLen,end-start+1)
    
    end +=1 
    
  return maxLen

print(longSubKUnique(s = "aabaaab", k = 2))