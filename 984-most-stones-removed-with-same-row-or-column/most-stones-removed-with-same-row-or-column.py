class Solution:
    def removeStones(self, stones: List[List[int]]) -> int:
        s = [1]*(len(stones))
        par = [i for i in range(len(stones))]

        def find(x):
            t= par[x]
            while t != par[t]:
                par[t] = par[par[t]]
                t=par[t]
            return t
        

        def union(x,y):
            parent1 = find(x)
            parent2 = find(y)

            if parent1 != parent2:
                if s[parent1] > s[parent2]:
                    par[parent2]=parent1
                    s[parent1]+=s[parent2]
                else:
                    par[parent1]=parent2
                    s[parent2]+=s[parent1]
        
        for i in range(len(stones)):
            for j in range(i+1, len(stones)):
                if stones[i][0] == stones[j][0] or stones[i][1] == stones[j][1]:
                    union(i,j)
        
        sett=set()
        for i in range(len(stones)):
            sett.add(find(i))

        return len(stones) - len(sett)