# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def goodNodes(self, root: TreeNode) -> int:
     
        def dfs(root,maxx):
         
            if not root:
                return 0
            
            if root.val >= maxx:
                res =1
            else:
                res = 0

            res += dfs(root.left,max(maxx,root.val))
            res += dfs(root.right,max(maxx,root.val))       
            return res
        return dfs(root,float(-inf))

        