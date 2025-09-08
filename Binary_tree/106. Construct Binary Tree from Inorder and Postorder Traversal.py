# Given two integer arrays inorder and postorder where inorder is the inorder traversal of a binary tree and postorder is the postorder traversal of the same tree, construct and return the binary tree.

# Example 1:
# Input: inorder = [9,3,15,20,7], postorder = [9,15,7,20,3]
# Output: [3,9,20,null,null,15,7]

# Example 2:
# Input: inorder = [-1], postorder = [-1]
# Output: [-1]

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def buildTree(self, inorder: List[int], postorder: List[int]) -> Optional[TreeNode]:
        if not inorder or not postorder or len(inorder) != len(postorder): 
            return None 
        
        index_map = {val:i for i ,val in enumerate(inorder)}
    
        n = len(postorder)
        postIndex = n-1 
    
        def helper(in_left:int ,in_right:int )-> Optional[TreeNode]: 
            nonlocal postIndex 

            if in_left > in_right: 
                return None
            
            rootVal = postorder[postIndex]
            postIndex -= 1 

            root  = TreeNode(rootVal)

            index = index_map[rootVal]

            root.right = helper(index+1,in_right)
            root.left = helper(in_left,index-1)
            

            return root
        
        return helper(0,n-1)