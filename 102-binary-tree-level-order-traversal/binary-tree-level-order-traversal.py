# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if not root:
            return []
        lis = [root]
        result = []

        while lis:

            temp = []
            next_list = []
            for rot in lis:
                if rot:
                    temp.append(rot.val)
                if rot and rot.left:
                    next_list.append(rot.left)
                if rot and rot.right:
                    next_list.append(rot.right)
            
            lis = next_list
            result.append(temp)

        return result



        