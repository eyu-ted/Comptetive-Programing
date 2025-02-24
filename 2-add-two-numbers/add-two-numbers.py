# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        head_l1 = l1
        head_l2 = l2

        dummy = ListNode(0)
        ans = dummy
        carry =0

        while head_l1 and head_l2:
            if head_l1.val+ head_l2.val + carry < 10:
                new_node = ListNode(head_l1.val+ head_l2.val + carry )
                dummy.next = new_node
                carry = 0
            else:
                num = str(head_l1.val + head_l2.val + carry)
                carry = int(num[0])
                dummy.next = ListNode(int(num[1]))

            head_l1 = head_l1.next
            head_l2 = head_l2.next
            dummy = dummy.next

        if head_l1:
            while head_l1:
                if head_l1.val + carry < 10:
                    new_node = ListNode(head_l1.val + carry )
                    dummy.next = new_node
                    carry =0
                else:
                    num = str(head_l1.val  + carry)
                    carry = int(num[0])
                    dummy.next = ListNode(int(num[1]))
                head_l1 = head_l1.next
                dummy = dummy.next
        if head_l2:
            while head_l2:
                if head_l2.val + carry < 10:
                    new_node = ListNode(head_l2.val + carry )
                    dummy.next = new_node
                    carry = 0
                else:
                    num = str(head_l2.val  + carry)
                    carry = int(num[0])
                    dummy.next = ListNode(int(num[1]))
                head_l2 = head_l2.next
                dummy = dummy.next
                
        if carry:
            dummy.next = ListNode(carry)


        return ans.next


