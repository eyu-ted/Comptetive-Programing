# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        t=head
        p=head
        if head is None:
            return None
        while t:
            p=t
            t=t.next
            if t is not None:
                if p.val==t.val:
                    p.next=t.next
                    t.next=None
                    t=p
        return head
        