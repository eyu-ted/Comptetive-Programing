# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        if not root:
            return []
        q = deque()
        q.append(root)
        ans = [root.val]
        while q:
            temp= deque()
            while q:
                popp = q.popleft()
                if popp.left:
                    temp.append(popp.left)
                if popp.right:
                    temp.append(popp.right)

            if temp:
                ans.append(temp[-1].val)
            q =temp
        return ans

