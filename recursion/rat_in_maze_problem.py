# Given an N x N grid (matrix) of 0s and 1s:
# 1 = open cell, 0 = blocked.
# Rat starts at top-left (0,0) and must reach bottom-right (N-1,N-1).
# Moves allowed: usually Up, Down, Left, Right (some variants restrict to only Right and Down).
# Output variants:
# Return any path (boolean/one path).
# Return all possible simple paths (no revisiting cells).
# Return the shortest path (fewest steps).
# Count number of paths (sometimes modulo large prime).


def rat_in_maze(matrix): 
  n = len(matrix)
  result = []
  
  if n == 0 : return result 
  
  if matrix[0][0] == 0 or matrix[n-1][n-1] == 0 : return result 
  
  paths = []
  
  directions = [('D',1,0) , ('U',-1,0) , ('L',0,-1) , ('R',0,1)]
  
  visited = [[False]*n for _ in range(n)]
  
  def backtrack(row,col,paths): 
    if row == n-1 and col == n-1 : 
      result.append(''.join(paths))
      return 
    
    
    # here dd , dr , dc represents the value of direction , row , col respectively from direction array element
    for dd , dr ,  dc in directions :
      nr = row + dr 
      nc = col + dc 
    
      if 0<=nr<n and 0<= nc < n and matrix[nr][nc] == 1 and not visited[nr][nc]: 
        paths.append(dd)
        visited[nr][nc] = True 
      
        backtrack(nr,nc,paths)
        
        #backtrack from this choice 
        paths.pop() 
        visited[nr][nc] = False 
        
  visited[0][0] = True
  backtrack(0,0,[])
  return result 
  

matrix = [ [1, 0, 0, 0] , [1, 1, 0, 1], [1, 1, 0, 0], [0, 1, 1, 1] ]
print(rat_in_maze(matrix))