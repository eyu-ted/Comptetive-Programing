# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        slow=fast=head
        prev=None
        if head==None:
            return
        if head.next==None:
            head=None
            return
        while n:
            fast=fast.next
            n-=1
        while fast:
            prev=slow
            slow=slow.next
            fast=fast.next
        if prev!=None:
            prev.next=slow.next
        else:
            head=head.next
        return head
        

        