# Given a binary tree, find the lowest common ancestor (LCA) of two given nodes in the tree.

# According to the definition of LCA on Wikipedia: “The lowest common ancestor is defined between two nodes p and q as the lowest node in T that has both p and q as descendants (where we allow a node to be a descendant of itself).

# Example 1:
# Input: root = [3,5,1,6,2,0,8,null,null,7,4], p = 5, q = 1
# Output: 3
# Explanation: The LCA of nodes 5 and 1 is 3.

# Example 2:
# Input: root = [3,5,1,6,2,0,8,null,null,7,4], p = 5, q = 4
# Output: 5
# Explanation: The LCA of nodes 5 and 4 is 5, since a node can be a descendant of itself according to the LCA definition.

# Example 3:
# Input: root = [1,2], p = 1, q = 2
# Output: 1
 
 
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':


# path-array approach

        # def findPath(node,target,path):
        #     if not node : 
        #         return False 
            
        #     path.append(node)

        #     if node == target : 
        #         return True 
            
        #     if (findPath(node.left,target,path) or findPath(node.right,target,path) ): 
        #         return True 
            
        #     path.pop()
        #     return False
        
        # p_array, q_array = [],[]
    
        # if (not findPath(root,p,p_array)) or (not findPath(root,q,q_array) ): 
        #     return None 
        
        # i = 0 
        # while i < len(p_array) and i < len(q_array) and p_array[i] == q_array[i]: 
        #     i += 1
        
        # return p_array[i-1]
    
#recursive approach 

        if not root or root == p or root == q: 
            return root 
        

        left = self.lowestCommonAncestor(root.left,p,q)
        right = self.lowestCommonAncestor(root.right,p,q)

        if left and right  :
            return root 
        
        return left or right 
            

