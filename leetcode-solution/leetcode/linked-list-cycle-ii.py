# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def detectCycle(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if head==None or  head.next==None :
            return 
        slow=fast=head
        while fast and fast.next:
            fast=fast.next.next
            slow=slow.next
            if fast==slow:
                slow=head
                break
       
        while slow and fast:
            if slow==fast:
                return slow

            slow=slow.next
            fast=fast.next
        return 
        
        