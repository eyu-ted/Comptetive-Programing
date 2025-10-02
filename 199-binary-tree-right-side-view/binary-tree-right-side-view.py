# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        dic = defaultdict(list)
        def dfs(root,level):

            if not root:
                return root
            dic[level].append(root.val)

            dfs(root.left,level+1)
            dfs(root.right,level+1)
        dfs(root,0)

        result = []
        for _,value in dic.items():
            result.append(value[-1])
        return result 