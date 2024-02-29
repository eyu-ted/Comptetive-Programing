# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def zigzagLevelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        ans = []
        parent_nodes = deque()
        parent_nodes.append(root)
        if root:
            ans=[[root.val]]
        else:
            ans=[]
        while parent_nodes:
            same_level = deque()
            for _ in range(len(parent_nodes)):
                node = parent_nodes.popleft()

                if node and node.left:
                    parent_nodes.append(node.left)
                    same_level.append(node.left.val)
                if node and node.right:
                    parent_nodes.append(node.right)
                    same_level.append(node.right.val)
            ans.append(list(same_level))

        ans.pop()
        for i in range(len(ans)):
            if i%2==1:
                ans[i] = ans[i][::-1] 

        

        return ans