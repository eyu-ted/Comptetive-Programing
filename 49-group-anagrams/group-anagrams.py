class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        
        soln_dic = defaultdict(list)
        for word in strs:
            soln_dic["".join(sorted(word))].append(word)
        
        soln = []
        for _, value in soln_dic.items():
            soln.append(value)

        return soln

        # nat = [n,a,t] = [a,n,t] = [ant] = nat

        # tan = [t,a,n] = [a,n,t] = [ant] = nat , tan