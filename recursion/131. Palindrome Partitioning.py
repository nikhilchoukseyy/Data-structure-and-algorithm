# Given a string s, partition s such that every substring of the partition is a palindrome. Return all possible palindrome partitioning of s.

# Example 1:
# Input: s = "aab"
# Output: [["a","a","b"],["aa","b"]]

# Example 2:
# Input: s = "a"
# Output: [["a"]]

class Solution:
    def partition(self, s: str):
        s_arr = list(s)

        def isPalindrome(arr): 
            return arr == arr[::-1] 

        result = []
        def backtrack(index,s,path): 
            if index == len(s): 
                result.append(path[:])
                return 

            for i in range(index,len(s)): 
                part = s[index : i+1]
                if isPalindrome(part): 
                    path.append(part)
                    backtrack(i+1,s,path)
                    path.pop()
        
        backtrack(0,s,[])
        return result 
