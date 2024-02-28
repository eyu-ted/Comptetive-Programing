# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        if q==None and p==None:
            return True
        elif (p != None and q==None) or  (p==None and q!=None) or (q.val != p.val):
            return False
        return (q.val==p.val) and self.isSameTree(p.left,q.left) and self.isSameTree(p.right,q.right)
        
        
        