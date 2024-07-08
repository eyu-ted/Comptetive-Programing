# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0
        maxx = 1
        def dfs(i,root):

            nonlocal maxx
            if not root:
                return 
            
            if root.left:
                maxx = max(i+1,maxx)
                dfs(i+1, root.left)
            if root.right:
                maxx = max(i+1,maxx)
                dfs(i+1,root.right)
        dfs(1,root)

        return maxx
        