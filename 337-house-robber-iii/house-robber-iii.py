# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rob(self, root: Optional[TreeNode]) -> int:
        dp = {}
        def dfs(root):

            if not root:
                return 0
            
            

            if root in dp:
                return dp[root]
            
            current = root.val

            if root.left:
                current += dfs(root.left.left) + dfs(root.left.right)
            if root.right:
                current += dfs(root.right.left) + dfs(root.right.right)
            

            skip = dfs(root.left) + dfs(root.right)

            dp[root] = max(current,skip)
             

            return dp[root]

        
        return dfs(root)