# A balanced binary tree is a type of binary tree where the heights of the left and right subtrees of every node differ by at most one

def isBalanced(self, root: Optional[TreeNode]) -> bool:
        isBalanced = True
        def height(root): 
            nonlocal isBalanced
            if not root :
                return 0 
            
            left_height = height(root.left)
            right_height = height(root.right)
        
            if abs(left_height - right_height) > 1 : 
                isBalanced = False
            
            return 1 + max(left_height,right_height)
        
        height(root)
        return isBalanced
    
# 🔹 Dry Run Example

# Let’s take this tree:

#         1
#        / \
#       2   3
#      /
#     4

# Step 1 → Call isBalanced(root=1)
# isBalanced = True
# Call height(1)

# Step 2 → Inside height(1)
# Compute left_height = height(2)
# Compute right_height = height(3)

# Step 3 → Compute height(2)
# Compute left_height = height(4)
# Compute right_height = height(None)
# height(4):
# left = height(None) = 0
# right = height(None) = 0
# difference = 0 → balanced ✅
# return 1 + max(0,0) = 1
# So left_height(2) = 1.
# height(None):
# return 0
# So right_height(2) = 0.
# → At node 2: abs(1-0) = 1 → still balanced ✅
# Return height(2) = 1 + max(1,0) = 2

# Step 4 → Compute height(3)
# left = 0, right = 0
# difference = 0 → balanced ✅
# Return height(3) = 1

# Step 5 → Back to height(1)
# left_height = 2 (from node 2)
# right_height = 1 (from node 3)
# Check: abs(2-1) = 1 → balanced ✅
# Return height(1) = 1 + max(2,1) = 3

# Step 6 → Finish
# No imbalance found.
# isBalanced = True
# Return True.