class Solution:
    def dividePlayers(self, skill: List[int]) -> int:
        skill.sort()
        flag=0
        l=0
        r=len(skill)-1
        prev=skill[0]+skill[-1]
        chem=0
        while r>l:

            summ=skill[r]+skill[l]
            if summ!=prev:
                flag=1
            prev=summ
            chem+=skill[r]*skill[l]
            r-=1
            l+=1
        return chem if flag!=1 else -1


        