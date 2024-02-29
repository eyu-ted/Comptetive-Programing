# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        arr1 = []
        arr2 = []
        def lowest(root, key ,arr):
            if not root:
                return
            arr.append(root.val)
            if root.val == key.val:
                return root
            else:
                if root.val > key.val:
                    lowest(root.left, key, arr)
                else:
                    lowest(root.right, key, arr)
            
        
        lowest(root, p ,arr1)
        lowest(root, q ,arr2)

        ans=0
        for i in range(len(arr1)):
            if i < len(arr2):
                if arr1[i] == arr2[i]:
                    ans = arr1[i]
            else:
                break



        return TreeNode(ans)
                

            

        
        