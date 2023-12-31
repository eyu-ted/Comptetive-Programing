class Solution:
    def maxIceCream(self, costs: List[int], coins: int) -> int:
        costs.sort()
        total=count=0
        for n in costs:
            total+=n
            if total<=coins:
                count+=1
            else:
                break
        return count

        