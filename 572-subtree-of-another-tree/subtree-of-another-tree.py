# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        

        
        def issame(p,q):

            if not q and not p:
                return True
            elif q and p and q.val == p.val:
                return issame(p.left,q.left) and issame(p.right ,q.right)
            else:
                return False
        
        
        
        
        def dfs(r,s):
            if not r:
                return False
            if issame(r,s):
                return True
           
            
            return dfs(r.left, s) or dfs(r.right,s)
        
        
        return dfs(root,subRoot)



        