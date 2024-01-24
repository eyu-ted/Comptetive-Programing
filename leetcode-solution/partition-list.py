# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def partition(self, head: Optional[ListNode], x: int) -> Optional[ListNode]:
        temp=head
        flag=True
        prev=None
        if head==None:
            return 
        if temp.next==None:
            return head
        # if temp.val==x:
        #     temp=temp.next
        #     change.next=temp.next
        #     temp.next=change
        #     head=temp
  

        while temp:
            if temp.val>=x and flag:
                prevlarger=prev
                larger=temp
                flag=False
            if temp.val<x and flag==False :
                if prevlarger==None:
                    prev.next=temp.next
                    temp.next=larger
                    prevlarger=temp
                    head=prevlarger
                else:
                    prev.next=temp.next
                    prevlarger.next=temp
                    temp.next=larger
                    prevlarger=temp
            prev=temp
            temp=temp.next
        return head 





