# Given a string containing digits from 2-9 inclusive, return all possible letter combinations that the number could represent. Return the answer in any order.

# A mapping of digits to letters (just like on the telephone buttons) is given below. Note that 1 does not map to any letters.
 

# Example 1:
# Input: digits = "23"
# Output: ["ad","ae","af","bd","be","bf","cd","ce","cf"]

# Example 2:
# Input: digits = ""
# Output: []

# Example 3:
# Input: digits = "2"
# Output: ["a","b","c"]

class Solution:
    def letterCombinations(self, digits: str):
        if not digits : 
            return []
        
        digitToLetters = ['', '', 'abc', 'def', 'ghi',
                      'jkl', 'mno', 'pqrs', 'tuv', 'wxyz']

        result = []

        def backtrack(i,path): 
            if i == len(digits): 
                result.append(''.join(path))
                return
            
            for letter in digitToLetters[int(digits[i])]: 
                path.append(letter)
                backtrack(i+1,path)
                path.pop()
            
        backtrack(0,[])
        return result 