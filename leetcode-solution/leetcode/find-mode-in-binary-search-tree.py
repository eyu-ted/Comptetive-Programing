# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def findMode(self, root: Optional[TreeNode]) -> List[int]:
        dic=defaultdict(int)
        def traverse(node):
            if not node:
                return 
            
            if node.left:
                traverse(node.left)
            
            if node.right:
                traverse(node.right)

            dic[node.val]+=1
            
            

        
        traverse(root)
        print(dic)
        ans = []
        maxx = max(dic.values())


        for key in dic.keys():
            if dic[key] == maxx:
                ans.append(key)
        return ans
        