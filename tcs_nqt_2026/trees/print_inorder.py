# Question
# Given N integers.
# Construct a BST.
# Print inorder traversal.

# Input
# 7
# 10 5 20 3 8 15 30

# Output
# 3 5 8 10 15 20 30

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

def inorder(root): 
  if root : 
    inorder(root.left) 
    print(root.data , end = " ")
    inorder(root.right)


n = int(input())
nums = list(map(int,input().split()))
root = None
for num in nums : 
  root = insert(root,num)

inorder(root)