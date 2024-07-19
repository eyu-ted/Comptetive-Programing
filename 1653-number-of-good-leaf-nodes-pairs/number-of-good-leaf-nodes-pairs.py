# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def countPairs(self, root: TreeNode, distance: int) -> int:
        ans =0
        def dfs(root):
            nonlocal ans

            if not root:
                return []
            
            if not root.left and not root.right:
                return [1]

            left = dfs(root.left)
            right = dfs(root.right)

            for l in left:
                for r in right:
                    if l+r <=distance:
                        ans+=1

            curr = [] 
            for l in left:
                if l+1 <=distance:
                    curr.append(l+1)
            
            for r in right:
                if r+1 <=distance:
                    curr.append(r+1)
            
            return curr
        
        dfs(root)

        return ans

                    
                        

        