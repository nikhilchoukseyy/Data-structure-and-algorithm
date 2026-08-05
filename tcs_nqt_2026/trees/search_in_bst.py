# Question
# Given N integers.

# Construct a BST.

# Search X.

# If found print YES otherwise print NO.
# Input
# 7
# 10 5 20 3 8 15 30
# 15

# Output

# YES

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

def search(root,target): 
  if not root : 
    return False

  if root.data == target : 
    return True
  elif root.data > target: 
    return search(root.left,target)
  else : 
    return search(root.right,target)

  


n = int(input())
nums = list(map(int,input().split()))
target = int(input())
root = None 

for num in nums : 
  root = insert(root,num)

result = search(root,target)
if result : 
  print("YES")
else : 
  print("NO")