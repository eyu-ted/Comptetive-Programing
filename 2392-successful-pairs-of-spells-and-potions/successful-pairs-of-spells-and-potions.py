class Solution:
    def successfulPairs(self, spells: List[int], potions: List[int], success: int) -> List[int]:
        
        result  = []
        potions.sort()
        for spell in spells:
            num = math.ceil(success/spell)
            indx = bisect_left(potions,num)
     
            result.append(len(potions)- indx)
        return result

