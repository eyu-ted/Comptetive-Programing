class Solution:
    def numRescueBoats(self, people: List[int], limit: int) -> int:
        
        people.sort()
        left = 0
        right = len(people)-1
        count =0

        while left <= right:
            summ = people[left] + people[right]

            if summ > limit:
                right-=1
            else:
                right-=1
                left+=1
            count += 1
        
        return count
            


