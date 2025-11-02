class Solution:
    def findJudge(self, n: int, trust: List[List[int]]) -> int:
        if n == 1 and trust == []:
            return 1
        trusted_person = []
        dic = defaultdict(set)

        for trustee , trusted in trust:
            trusted_person.append(trusted)
            dic[trustee].add(trusted)
        
        for person in trusted_person:
            if person not in dic:
                flag = True
                for key in range(1,n+1):
                    if key != person and person not in dic[key]:
                        flag = False
                        break
                if flag:
                    return person
        return -1
