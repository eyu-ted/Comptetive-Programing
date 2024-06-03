# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def findBottomLeftValue(self, root: Optional[TreeNode]) -> int:
        qeue = deque()
        qeue.append(root)

        ans = root.val
        while qeue:
            temp = deque()
            while qeue:
                node = qeue.popleft()

                if node.left:
                    temp.append(node.left)
                if node.right:
                    temp.append(node.right)
            
            if len(temp):
                ans = temp[0].val
            qeue = temp
        
        return ans
            
        