# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        if root == None:
            return []
        soln = []
        def dfs(root):
            nonlocal soln

            if root.left:
                dfs(root.left)
            soln.append(root.val)
            if root.right:
                dfs(root.right)
        
        dfs(root)

        return soln




        