# Given a string s and a dictionary of strings wordDict, return true if s can be segmented into a space-separated sequence of one or more dictionary words.

# Note that the same word in the dictionary may be reused multiple times in the segmentation.

# Example 1:
# Input: s = "leetcode", wordDict = ["leet","code"]
# Output: true
# Explanation: Return true because "leetcode" can be segmented as "leet code".
# Example 2:

# Input: s = "applepenapple", wordDict = ["apple","pen"]
# Output: true
# Explanation: Return true because "applepenapple" can be segmented as "apple pen apple".
# Note that you are allowed to reuse a dictionary word.

# Example 3:
# Input: s = "catsandog", wordDict = ["cats","dog","sand","and","cat"]
# Output: false

def wordBreak(s,wordDict): 
  
  n = len(s)
  memo = {}
  word_set = set(wordDict)
  
  def solve(index): 
    if index == n : 
      return True 

    if index in memo : 
      return memo[index]
    
    
  
    for i in range(index+1 , n + 1 ): 
      if s[index:i] in word_set and solve(i): 
        memo[index] = True 
        return True 
    
    memo[index] = False 
    return False 
  
  return solve(0)

s = "leetcode"
wordDict = ["leet","code"]
print(wordBreak(s,wordDict))