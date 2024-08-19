# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def hasPathSum(self, root: Optional[TreeNode], targetSum: int) -> bool:
        sett =set()
        if not root:
            return 0
        def travers(root,summ):
            if not root.left and not root.right:
                sett.add(summ+root.val)
                return 
            if root.left:
                travers(root.left,summ+root.val)
            if root.right:
                travers(root.right,summ+root.val)
        
        travers(root,0)
        return targetSum in sett