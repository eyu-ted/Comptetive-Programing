# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeNodes(self, head: Optional[ListNode]) -> Optional[ListNode]:
        dummy = ListNode()
        ans = dummy

        temp = head
        summ = 0
        while temp:
            summ+=temp.val
            if temp.val==0:
                print(summ)
                ans.next=ListNode(summ)
                ans =ans.next
                summ=0

            temp = temp.next
        return dummy.next.next

        

        