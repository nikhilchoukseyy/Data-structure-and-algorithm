# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
        
# Given the root of a binary tree, return the preorder traversal of its nodes' values.

# Example 1:
# Input: root = [1,null,2,3]
# Output: [1,2,3]


# Example 2:
# Input: root = [1,2,3,4,5,null,8,null,null,6,7,9]
# Output: [1,2,4,5,6,7,3,8,9]


# Example 3:
# Input: root = []
# Output: []

# Example 4:
# Input: root = [1]
# Output: [1]
        
class Solution:
    def preorderTraversal(self, root: Optional[TreeNode]) -> List[int]: 
        result = []
        def preorder(root): 
            if not root :
                return
            
            result.append(root.val)
            preorder(root.left)
            preorder(root.right)
        
        preorder(root)
        return result