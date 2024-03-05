# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def splitListToParts(self, head: Optional[ListNode], k: int) -> List[Optional[ListNode]]:
        temp = head
        l=0

        while temp :
            temp=temp.next
            l+=1


        size = l//k
        full = l%k 

        lis = [size+1]*(full) + [size]*(k-full) 
        ans=[]
        temp = head

        for n in lis:
            ans.append(temp)
            for i in range(n-1):
                temp = temp.next
            if temp:
                hold = temp.next 
                temp.next = None
                temp =hold
            

        
        

        return  ans