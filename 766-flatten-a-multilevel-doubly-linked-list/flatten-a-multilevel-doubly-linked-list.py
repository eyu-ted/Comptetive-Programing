"""
# Definition for a Node.
class Node:
    def __init__(self, val, prev, next, child):
        self.val = val
        self.prev = prev
        self.next = next
        self.child = child
"""

class Solution:
    def flatten(self, head: 'Optional[Node]') -> 'Optional[Node]':
        if not head:
            return 
        dummyNode = temp = Node(0,None,None,None)
        
        stack = [head]

        while stack:
            node = stack.pop()

            temp.next = Node(node.val, temp,None,None)
            temp = temp.next

            if node.next:
                stack.append(node.next)
            if node.child:
                stack.append(node.child)
        
        dummyNode = dummyNode.next

        if dummyNode:

            dummyNode.prev = None
        
        return dummyNode
        

