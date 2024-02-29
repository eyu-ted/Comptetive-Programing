# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxAncestorDiff(self, root: Optional[TreeNode]) -> int:
        ans=-1
        maxx = float("-inf")
        minn = float("inf")
        def helper(root,minn,maxx,ans):
            if root:
                minn = min(root.val, minn)
                maxx = max(root.val, maxx)

                left = helper(root.left , minn , maxx , ans)
                right = helper(root.right , minn , maxx , ans)


                ans=max(left,right)

            else:
                ans = max(ans,abs(maxx-minn))

            return ans    
        x=helper(root,minn,maxx,ans)
        return x

            

            
           




        