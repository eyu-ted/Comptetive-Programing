class Solution:
    def smallestStringWithSwaps(self, s: str, pairs: List[List[int]]) -> str:
        parent = list(range(len(s)))
        rank = [1] * len(s)
        
        def find(x):
            if parent[x] != x:
                parent[x] = find(parent[x])
            return parent[x]

        def union(x, y):
            rootX = find(x)
            rootY = find(y)
            
            if rootX != rootY:
                if rank[rootX] > rank[rootY]:
                    parent[rootY] = rootX
                elif rank[rootX] < rank[rootY]:
                    parent[rootX] = rootY
                else:
                    parent[rootY] = rootX
                    rank[rootX] += 1
            
    
        for a, b in pairs:
            union(a, b)

   
        dic = defaultdict(list)
        for i in range(len(s)):
            root = find(i)
            dic[root].append(s[i])

        for key in dic.keys():
            dic[key].sort(reverse=True)

        ans = []
        for i in range(len(s)):
            root = find(i)
            ans.append(dic[root].pop())

        return "".join(ans)
