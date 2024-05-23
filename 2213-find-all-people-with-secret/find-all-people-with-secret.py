class Solution:
    def findAllPeople(self, n: int, meetings: List[List[int]], firstPerson: int) -> List[int]:
        par = [i for i in range(n+1)]
        def find(x):
            t= par[x]
            while t != par[t]:
                par[t] = par[par[t]]
                t=par[t]
            return t

        def union(x,y):
            parent1 = find(x)
            parent2 = find(y)

            if parent1!= parent2:
                par[parent1] = min(parent1,parent2)
                par[parent2] = min(parent1,parent2)
        def my(arr):
            return arr[2]
        meetings.sort(key = my)
        union(0,firstPerson)
        i=0
        while i<len(meetings):
            time = meetings[i][2]
            lis = []
            while i<len(meetings) and time == meetings[i][2]:
                p1, p2 = meetings[i][0],meetings[i][1]
                union(p1,p2)
                lis.append(p1)
                lis.append(p2)
                i+=1
            print(lis)
            for nu in lis:
                print(find(nu))
                if find(nu) !=0:
                    par[nu] =nu

        ans = []


        for num in range(n+1):
            print(find(num))
            if find(num) ==0:
                ans.append(num)
        return ans
        