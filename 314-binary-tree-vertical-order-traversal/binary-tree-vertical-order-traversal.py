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
        
        def bfs():

            queue = deque()
            queue.append((root,0))

            while queue:

                node , level = queue.popleft()

                dic[level].append(node.val)

                if node.left:
                    queue.append((node.left, level-1))
                if node.right:
                    queue.append((node.right, level+1)) 
            
            
        
        bfs()

        lis = list(dic.items())
        lis.sort()

        result = []
        for arr in lis:
            result.append(arr[1])


        return result

        