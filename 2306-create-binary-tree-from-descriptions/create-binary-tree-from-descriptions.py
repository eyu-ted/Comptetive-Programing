# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def createBinaryTree(self, descriptions: List[List[int]]) -> Optional[TreeNode]:
        sett =set()

        graph = defaultdict(list)
        for par,child,isleft in descriptions:
            sett.add(child)
            graph[par].append([child, isleft])

        for par, child ,isleft in descriptions:
            if par not in sett:
                root = TreeNode(par)
        
      
        stack = [root]
        while stack:
            pop = stack.pop()
            temp = pop

            for child,isleft in graph[pop.val]:
                node =TreeNode(child)
                if isleft:
                    temp.left = node
                else:
                    temp.right = node

                stack.append(node)
        
        return root
                
                
                

        
        
    

        