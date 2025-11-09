# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        from heapq import heappush, heappop
        setattr(ListNode, "__lt__", lambda a, b: a.val < b.val)
        heap = []

        for head in lists:
            if head:
                heapq.heappush(heap,head)
        
        dummy = ListNode()
        temp = dummy
        while heap:
            node = heappop(heap)
            if node.next:
                heappush(heap,node.next)
            temp.next = node
            temp = temp.next

        return dummy.next