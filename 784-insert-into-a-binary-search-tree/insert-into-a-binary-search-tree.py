# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def insertIntoBST(self, root: Optional[TreeNode], val: int) -> Optional[TreeNode]:
        if not root:
            return TreeNode(val)
        def dfs(root):

            if not root:
                return TreeNode(val)
            

            if root.val > val:
                left = dfs(root.left)
                if left:
                    root.left = left
            
            if root.val < val:
                right = dfs(root.right)
                if right:
                    root.right = right
                

        dfs(root)

        return root

        