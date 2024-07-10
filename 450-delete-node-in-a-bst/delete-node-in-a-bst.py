# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def deleteNode(self, root: Optional[TreeNode], key: int) -> Optional[TreeNode]:

        # to hold [1] key=0,
        # to hold [0] key=0 case we have to add this conditions
        if root and not root.left and root.val==key:
            return root.right
        elif root and not root.right and  root.val==key:
            return root.left
        temp=root
        def findmin(node):

            while node.left:
                node=node.left
            
            return node
        def delete(root,key):

            if not root:
                return 
            
            if root.val > key:
                root.left = delete(root.left , key)
            elif root.val < key:
                root.right = delete(root.right , key)
            else:

                if not root.left:
                    return root.right
                elif not root.right:
                    return root.left
                
                min_node = findmin( root.right )
                root.val = min_node.val

                root.right = delete(root.right , min_node.val)
            return root

        delete(root , key)
        return temp


            


        