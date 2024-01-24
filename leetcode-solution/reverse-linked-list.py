# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        revnode=None
        temp=head
        while temp :
            nextnode=temp.next
            temp.next=revnode
            revnode=temp
            temp=nextnode
        return revnode
            

        