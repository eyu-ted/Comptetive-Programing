# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def bstFromPreorder(self, preorder: List[int]) -> Optional[TreeNode]:
        if len(preorder) == 0:
            return None
        root = TreeNode(preorder[0])

        def insertNode(root, newVal):
            if root.val > newVal:
                if root.left is None:
                    root.left = TreeNode(newVal)
                    return
                insertNode(root.left, newVal)
            if root.val < newVal:
                if root.right is None:
                    root.right = TreeNode(newVal)
                    return
                insertNode(root.right, newVal)
        
        for val in preorder[1:]:
            insertNode(root, val)
        return root
        