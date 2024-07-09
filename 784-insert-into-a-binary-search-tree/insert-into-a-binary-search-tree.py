# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def insertIntoBST(self, root: Optional[TreeNode], val: int) -> Optional[TreeNode]:
        node=TreeNode(val)
        if root==None:
            return node

        
        def insert(root):
            if root and root.val<val:
                if root.right==None:
                    root.right=node
                    return
                insert(root.right)
            if root and root.val>val:
                if root.left==None:
                    root.left=node
                    return
                insert(root.left)
        insert(root)
        return root
            
            