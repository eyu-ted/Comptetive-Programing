# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def swapPairs(self, head: Optional[ListNode]) -> Optional[ListNode]:

        if not head or not head.next:
            return head

        result = head.next

        curr = head
        prev = None

        while curr and curr.next:

            next_next_node = curr.next.next
            next_node = curr.next

            next_node.next = curr
            curr.next = next_next_node

            if prev:
                prev.next = next_node
            
            prev = curr
            curr = next_next_node
        
        return result


