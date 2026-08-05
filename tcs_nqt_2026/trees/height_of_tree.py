# Question
# Given N integers.

# Construct a BST.

# Print the height of the BST.
# Input
# 7
# 10 5 20 3 8 15 30
# Output
# 3

from collections import deque

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

n = int(input())
nums = list(map(int,input().split()))
root = None
for num in nums : 
  root = insert(root,num)

def height(root): 
  
  if not root : 
    return 0
  left = height(root.left)
  right = height(root.right)

  return 1 + max(left,right)
  # q = deque([root])
  # h = 0 
  # while q : 
  #   size = len(q)
  #   for _ in range(size): 
  #     node = q.popleft()
  #     if node.left : 
  #       q.append(node.left)
  #     if node.right : 
  #       q.append(node.right)
  #   h+= 1

  # return h 

print(height(root))


