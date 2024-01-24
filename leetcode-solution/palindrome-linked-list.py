# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        lis=[]
        temp=head
        while temp:
            lis.append(temp.val)
            temp=temp.next
        return lis[::-1]==lis
        
        