# The n-queens puzzle is the problem of placing n queens on an n x n chessboard such that no two queens attack each other.

# Given an integer n, return all distinct solutions to the n-queens puzzle. You may return the answer in any order.

# Each solution contains a distinct board configuration of the n-queens' placement, where 'Q' and '.' both indicate a queen and an empty space, respectively.


# Example 1:
# Input: n = 4
# Output: [[".Q..","...Q","Q...","..Q."],["..Q.","Q...","...Q",".Q.."]]
# Explanation: There exist two distinct solutions to the 4-queens puzzle as shown above

# Example 2:
# Input: n = 1
# Output: [["Q"]]

from typing import List
class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        
        def isValid(board,row,col): 

            #check upward col 
            for i in range(row): 
                if board[i][col] == "Q": 
                    return False 
                
            #check left upward diagonal 
            i = row-1 
            j = col-1 
            while i >= 0 and j >= 0 : 
                if board[i][j] == 'Q': 
                    return False 
                
                i -= 1 
                j -= 1 
            
            #check right upward diagonal 
            i = row-1 
            j = col+1 
            while i >= 0 and j < n : 
                if board[i][j] == 'Q': 
                    return False 
                i -= 1 
                j += 1 
                
            return True 

        def backtrack(board,row,n): 
            if n == row : 
                solution = ["".join(r) for r in board]
                solutions.append(solution)
                return 
            
            for col in range(n): 
                if isValid(board,row,col): 
                    board[row][col] = 'Q'

                    backtrack(board,row+1,n)

                    board[row][col] = "."

        solutions = []
        board = [['.' for _ in range(n)] for _ in range(n)]
        backtrack(board,0,n)
        return solutions