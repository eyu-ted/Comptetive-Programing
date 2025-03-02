# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:    
    def closestKValues(self, root: TreeNode, target: float, k: int) -> List[int]:
        from collections import deque
        import heapq

        def solve(root, target, k):                              
            queue = deque()
            queue.append(root)
            visited = set()
            heap = []
            ans = []
            
            while queue:
                node = queue.popleft()
                print(node)
                value = node.val
                
                if node in visited:
                    continue
                visited.add(node)
                
                if node.left != None:
                    queue.append(node.left)
                    
                if node.right != None:
                    queue.append(node.right)
                    
                diff = abs(value - target)
                
                heapq.heappush(heap, [diff, value])
                    
            while len(ans) < k:
                if heap:
                    ans.append(heapq.heappop(heap)[1])
                            
            return ans
        
        return solve(root,target,k)