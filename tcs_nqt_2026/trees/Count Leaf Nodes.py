# Question

# Given N integers.

# Construct a BST.

# Print the number of leaf nodes.

# Input

# 7
# 10 5 20 3 8 15 30

# Output

# 4

# Leaf nodes hain:

# 3
# 8
# 15
# 30

class Node: 
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

def countLeafNodes(root): 
  if not root : 
    return 0 

  if not root.left and not root.right : 
    return 1 

  return countLeafNodes(root.left) + countLeafNodes(root.right)

n = int(input())
nums = list(map(int,input().split()))
root = None 
for num in nums : 
  root = insert(root,num)

print(countLeafNodes(root))