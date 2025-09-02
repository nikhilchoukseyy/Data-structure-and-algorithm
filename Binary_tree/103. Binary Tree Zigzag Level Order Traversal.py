# Given the root of a binary tree, return the zigzag level order traversal of its nodes' values. (i.e., from left to right, then right to left for the next level and alternate between).

# Example 1:
# Input: root = [3,9,20,null,null,15,7]
# Output: [[3],[20,9],[15,7]]

# Example 2:
# Input: root = [1]
# Output: [[1]]

# Example 3:
# Input: root = []
# Output: []

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import deque
class Solution:
    def zigzagLevelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        result = []

        if not root :
            return result

        queue = deque([root])
        level_num = 0 
        while queue: 
            size = len(queue)
            level = []
            for _ in range(size): 
                node = queue.popleft()
                if node.left : 
                    queue.append(node.left)
                if node.right : 
                    queue.append(node.right)
                level.append(node.val)
            
            if level_num %2 == 1: 
                result.append(level[::-1])
            else : 
                result.append(level)

            level_num += 1 # increase level number 

        return result 
