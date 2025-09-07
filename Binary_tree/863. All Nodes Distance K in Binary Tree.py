# Given the root of a binary tree, the value of a target node target, and an integer k, return an array of the values of all nodes that have a distance k from the target node.

# You can return the answer in any order.

# Example 1:
# Input: root = [3,5,1,6,2,0,8,null,null,7,4], target = 5, k = 2
# Output: [7,4,1]
# Explanation: The nodes that are a distance 2 from the target node (with value 5) have values 7, 4, and 1.

# Example 2:
# Input: root = [1], target = 1, k = 3
# Output: []

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def distanceK(self, root: TreeNode, target: TreeNode, k: int) -> List[int]:

        result = []

        if not root : 
            return result 
        
        parent_map = {}

        def build_parent_map(root,parent,parent_map): 
            if not root : 
                return 
            if parent : 
                parent_map[root] = parent 
            build_parent_map(root.left,root,parent_map)
            build_parent_map(root.right,root,parent_map)

            return parent_map

        build_parent_map(root,None,parent_map)
        queue  = deque([(target,0)])
        visited = {target}

        while queue : 
            size = len(queue)
            for i in range(size): 
                node , distance = queue.popleft()
                
                if distance == k : 
                    result.append(node.val)
                
                for neighbour in [node.left,node.right,parent_map.get(node)]: 
                    if neighbour and neighbour not in visited : 
                        visited.add(neighbour)
                        queue.append((neighbour,distance+1))
        
        return result 
