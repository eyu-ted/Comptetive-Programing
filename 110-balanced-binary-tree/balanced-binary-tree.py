# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        if not root:
            return True

        soln = True
        def dfs(root):
            nonlocal soln
            if not root :
                return 0
            if not soln:
                return 0
            
            left = dfs(root.left) 
            right = dfs(root.right) 
            soln = soln &( abs(left-right) <= 1)
            return 1 + max(left,right)

        dfs(root)
        return soln
           
        