# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def deleteNode(self, root: Optional[TreeNode], key: int) -> Optional[TreeNode]:
        

        def dfs(root,key):

            if not root:
                return root

            if root.val > key:
                root.left = dfs(root.left,key)
            elif root.val< key:
                root.right = dfs(root.right,key)
            else:
                if root.right and root.left:

                    curr = root.right
                    while curr.left:
                        curr = curr.left
                    
                    root.val = curr.val
                   
                    root.right = dfs(root.right,curr.val)
                
                elif root.right:
                    return root.right
                elif root.left:
                    return root.left
                else:
                    return None
            return root
        return dfs(root,key)

        