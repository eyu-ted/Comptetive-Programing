# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        maxx = float("inf")
        minn = float("-inf")

       

        def helper(root, maxx, minn):

            if not root:
                return True

            
            if minn < root.val < maxx:

                left = helper(root.left, root.val , minn)

                right = helper(root.right, maxx, root.val)

                return left and right

            else:
                return False


        
        return helper(root, maxx,minn) 


     

    
    
       
        
        

        
