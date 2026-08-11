# TCS NQT Problem

# Given a string text and a string pattern, find the number of substrings in text that are anagrams of pattern.

# Input Format
# text
# pattern
# Output Format
# Count of anagrams
# Example

# Input

# forxxorfxdofr
# for

# Output

# 3

# Explanation:

# "for"
# "orf"
# "ofr"

from collections import Counter
def solve(): 
  text = input().strip()
  pattern = input().strip()

  k = len(pattern)
  window = text[:k]
  count = 0 
  n = len(text)

  pattern_freq = Counter(pattern)
  window_freq = Counter(window)

  if pattern_freq == window_freq: 
    count += 1 


  for i in range(k,n): 
    window_freq[text[i]] += 1
    left_char = text[i - k]
    window_freq[left_char] -= 1

    if window_freq[left_char] == 0:
      del window_freq[left_char]

    if window_freq == pattern_freq:
      count += 1
  return count 

print(solve())
