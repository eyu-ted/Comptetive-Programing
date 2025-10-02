# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        if not root and not subRoot:
            return False
    
        def traversal(node):
            if not node:
                return False
            if sametree(node,subRoot):
                return True
            
            return traversal(node.left) or traversal(node.right)
            
            return right or left or parent
        def sametree(q,p):

            if not q and not p:
                return True
            elif p and q and p.val == q.val:
                return sametree(p.left,q.left) and sametree(p.right,q.right)
            else:
                return False
        return traversal(root)