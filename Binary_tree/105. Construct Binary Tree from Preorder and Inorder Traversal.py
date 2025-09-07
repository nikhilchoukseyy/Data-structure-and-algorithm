# Given two integer arrays preorder and inorder where preorder is the preorder traversal of a binary tree and inorder is the inorder traversal of the same tree, construct and return the binary tree.

# Example 1:
# Input: preorder = [3,9,20,15,7], inorder = [9,3,15,20,7]
# Output: [3,9,20,null,null,15,7]

# Example 2:
# Input: preorder = [-1], inorder = [-1]
# Output: [-1]

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        if not preorder or not inorder or len(preorder) != len(inorder): 
            return None

        index_map = {val:i for i ,val in enumerate(inorder) }

        preIndex = 0 
        n = len(preorder)

        def helper(in_left:int ,in_right:int )-> Optional[TreeNode]:
            nonlocal preIndex 

            if in_left > in_right : 
                return None
            
            rootVal = preorder[preIndex]
            preIndex += 1
        
            root = TreeNode(rootVal)

            index = index_map[rootVal]

            root.left = helper(in_left,index-1)
            root.right = helper(index+1,in_right)
            
            return root 
        
        return helper(0,n-1)