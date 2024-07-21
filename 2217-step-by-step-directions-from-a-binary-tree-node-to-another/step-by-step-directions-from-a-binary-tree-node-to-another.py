# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def getDirections(self, root: Optional[TreeNode], startValue: int, destValue: int) -> str:
        graph = defaultdict(list)
        def make_adj(node):
            if not node:
                return 

            if node.left:
                graph[node.val].append([node.left.val,"L"])
                graph[node.left.val].append([node.val,"U"])
                make_adj(node.left)
            if node.right:
                graph[node.val].append([node.right.val,"R"])
                graph[node.right.val].append([node.val,"U"])
                make_adj(node.right)
        make_adj(root)
        make_adj(root)
        
        # Use BFS to find the shortest path
        queue = deque([(startValue, "")])
        visited = set()
        visited.add(startValue)
        
        while queue:
            node, path = queue.popleft()
            
            if node == destValue:
                return path
            
            for neighbor, direction in graph[node]:
                if neighbor not in visited:
                    visited.add(neighbor)
                    queue.append((neighbor, path + direction))
        
        return ""

        