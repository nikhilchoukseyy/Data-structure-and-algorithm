# Find Minimum and Maximum in BST ⭐⭐⭐⭐⭐
# Question
# Given N integers.

# Construct a BST.

# Print the minimum and maximum element.

# Input

# 7
# 10 5 20 3 8 15 30

# Output

# 3
# 30


class Node : 
  def __init__(self,data): 
    self.data = data 
    self.left = None 
    self.right = None 

def insert(root,key): 
  if root is None : 
    return Node(key)

  if key < root.data : 
    root.left = insert(root.left,key)
  else : 
    root.right = insert(root.right,key)
  return root 


def findMinInBST(root): 
  if not root : 
    return None 
  
  if not root.left : 
    return root.data 

  return findMinInBST(root.left)

def findMaxInBST(root): 
  if not root : 
      return None 
  if not root.right : 
    return root.data 

  return findMaxInBST(root.right)


n = int(input())
nums = list(map(int,input().split()))
root = None 
for num in nums : 
  root = insert(root,num)

print(findMinInBST(root))
print(findMaxInBST(root))