# Question
# Given N integers.

# Construct a BST.

# Print total number of nodes.
# Input
# 7
# 10 5 20 3 8 15 30
# Output
# 7

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

def countNodes(root): 
  if not root : 
    return 0 

  return 1 + countNodes(root.left) + countNodes(root.right)


n = int(input())
nums = list(map(int,input().split()))
root = None 
for num in nums : 
  root = insert(root,num)

print(countNodes(root))