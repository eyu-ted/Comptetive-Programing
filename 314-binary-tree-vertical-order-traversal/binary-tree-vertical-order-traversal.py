# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def verticalOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        
        if not root:
            return []

        dic = defaultdict(list)

        def BFS():

            queue = deque()
            queue.append([root,0])

            while queue:

                node, col = queue.popleft()
                dic[col].append(node.val) 

                if node.left:

                    queue.append([node.left, col - 1])
                
                if node.right:

                    queue.append([node.right, col + 1])
        
        BFS()

        result = []

        for _,values in sorted(dic.items()):
            result.append(values)

        

        return result


        






