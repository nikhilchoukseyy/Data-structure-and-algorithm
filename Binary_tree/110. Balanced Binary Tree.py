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