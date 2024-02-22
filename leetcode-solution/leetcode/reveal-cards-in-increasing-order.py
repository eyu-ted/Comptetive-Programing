class Solution:
    def deckRevealedIncreasing(self, deck: List[int]) -> List[int]:
        deck.sort(reverse=True)
        queue=temp=deque()
        for n in deck:
            if len(temp):
                x=temp.popleft()
                temp.append(x)
              
            queue.append(n)
            temp=queue
        lis=list(queue)
        return lis[::-1]
            
            


        