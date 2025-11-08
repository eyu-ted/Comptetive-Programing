# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        dummyNode = ListNode()

        temp = dummyNode
        rem = 0
        while l2 or l1:
            if l2 and l1:
                summ = l1.val + l2.val +rem
                
                
                if summ >=10:
                    v = summ%10
                    rem = 1
                else:
                    v =summ
                    rem = 0
                
                temp.next = ListNode(v)
                temp = temp.next
                l1 = l1.next
                l2 = l2.next
            elif l2:
                summ = l2.val +rem
                
                
                if summ >=10:
                    v = summ%10
                    rem = 1
                else:
                    v =summ
                    rem = 0
                
                temp.next = ListNode(v)
                temp = temp.next
                l2 = l2.next
            elif l1:
                summ = l1.val +rem
                
                
                if summ >=10:
                    v = summ%10
                    rem = 1
                else:
                    v =summ
                    rem = 0
                
                temp.next = ListNode(v)
                temp = temp.next
                l1 = l1.next
        if rem:
            temp.next = ListNode(rem)
        return dummyNode.next

            

            
