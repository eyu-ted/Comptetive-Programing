# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0

        q = deque()
        

        q.append(root)
        
        depth = 0
        while q:
            temp = deque()
            while q:
                node = q.popleft()

                if node.left:
                    temp.append(node.left)
                if node.right:
                    temp.append(node.right)
            q = temp
            depth +=1
        return depth


            




        