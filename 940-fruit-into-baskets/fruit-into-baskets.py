class Solution:
    def totalFruit(self, fruits: List[int]) -> int:
        l=0
        dic={}
        maxx=0
        c=0
        for r in range(len(fruits)):
            c+=1
            while len(dic)==2 and fruits[r] not in dic:
                dic[fruits[l]]-=1
                c-=1
                if dic[fruits[l]]==0:
                    dic.pop(fruits[l])
                l+=1
                
            dic[fruits[r]]=1+dic.get(fruits[r],0)
            maxx=max(maxx,c)
        return maxx
        
