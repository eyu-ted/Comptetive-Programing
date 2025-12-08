class Solution:
    def findJudge(self, n: int, trust: List[List[int]]) -> int:
        
        trust_dic = defaultdict(list)
        trusted_by_dic = defaultdict(list)


        for a,b in trust:
            trust_dic[a].append(b)
            trusted_by_dic[b].append(a)
        
        for num in range(1,n+1):
            
            if len(trusted_by_dic[num]) == n-1 and num not in trust_dic:
                return num
        
        return -1
