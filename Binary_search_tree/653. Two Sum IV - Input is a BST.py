# Given the root of a binary search tree and an integer k, return true if there exist two elements in the BST such that their sum is equal to k, or false otherwise.

# Example 1:
# Input: root = [5,3,6,2,4,null,7], k = 9
# Output: true

# Example 2:
# Input: root = [5,3,6,2,4,null,7], k = 28
# Output: false

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def findTarget(self, root: Optional[TreeNode], k: int) -> bool:
        hash_set = {}

        if not root : 
            return None 
        
        queue = deque([root])

        while queue: 
            size = len(queue)
            node = queue.popleft()
            if node.left : queue.append(node.left)
            if node.right : queue.append(node.right)

            if node.val in hash_set : 
                return True 
            else : 
                hash_set[(k - node.val)] = k - node.val

        return False 