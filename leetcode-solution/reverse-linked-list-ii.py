# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseBetween(self, head: Optional[ListNode], left: int, right: int) -> Optional[ListNode]:
        curr=head
        temp=head
        prev=head
        if right==left or curr.next==None:
            return head
        if left==1:
            for _ in range(right):
                temp=temp.next
            newlist=temp
            for _ in range((right-left)+1):
                nextnode=curr.next
                curr.next=newlist
                newlist=curr
                curr=nextnode
            return newlist
            
        for _ in range(left-1):
            prev=curr
            curr=curr.next
        for _ in range(right):
            temp=temp.next
        newlist=temp
        for _ in range((right-left)+1):

            nextnode=curr.next
            curr.next=newlist
            newlist=curr
            prev.next=newlist
            curr=nextnode
        return head
        
        