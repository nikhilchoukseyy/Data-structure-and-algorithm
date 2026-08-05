# Question 1: Top K Most Frequent Scores
# Problem Statement

# You are given an array of match scores and an integer K. Find the scores with the highest frequencies.

# Print the scores arranged in decreasing order of frequency and return only the first K scores.

# If two scores have the same frequency, the score that appears first in the array should come first.

# Input Format
# First line contains the array elements separated by commas.
# Second line contains an integer K.
# Output Format
# Print the top K most frequent scores separated by spaces.
# Sample Input
# 17,38,17,38,3,12,4,38
# 2
# Sample Output
# 38 17

def solve(): 
  scores = list(map(int,input().split(",")))
  k = int(input())

  freq = {}
  first = {}
  for i in range(len(scores)): 
    if scores[i] not in freq : 
      freq[scores[i]] = 1 
      first[scores[i]] = i 
    else : 
      freq[scores[i]] += 1 

  ans = sorted(freq.keys(),key = lambda x : (-freq[x],first[x]))
  return ans[:k]

print(*solve())