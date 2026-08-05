# Question 2: Last Student ID with Required Frequency
# Problem Statement

# You are given the Student ID and corresponding score of N students.

# You are also given:

# X → Score to check
# K → Required frequency

# Count how many times the score X appears.

# If the frequency of X is greater than or equal to K, print the last Student ID having score X.
# Otherwise, print -1.
# Input Format
# First line contains an integer N.
# Next N lines each contain two integers:
# StudentID Score
# Next line contains an integer X.
# Last line contains an integer K.
# Output Format
# Print the last Student ID having score X if its frequency is at least K.
# Otherwise, print -1.
# Sample Input
# 5
# 112 13
# 114 15
# 117 15
# 118 13
# 119 20
# 15
# 2
# Sample Output
# 117

def solve(): 
  n = int(input())
  sids = []
  scores = []
  for i in range(n): 
    sid , score = list(map(int,input().split()))
    sids.append(sid)
    scores.append(score)

  x = int(input())
  k = int(input())

  last_id = -1
  count = 0 
  for i in range(n): 
    if scores[i] == x : 
      count += 1 
      last_id = sids[i]

  return last_id if count >= k else -1
    
print(solve())