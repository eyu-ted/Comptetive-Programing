# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        index = 0
        soln = 0
        def dfs(root):
            nonlocal index, soln
            if not root:
                return 0
            

            dfs(root.left) 
            index +=1
            if index == k:
                soln = root.val
            dfs(root.right)
            

            return index
        
        dfs(root)
        return soln