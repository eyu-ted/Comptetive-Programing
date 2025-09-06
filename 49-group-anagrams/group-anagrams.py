class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        

        dic = defaultdict(list)

        for wrd in strs:

            sett = []

            for ch in wrd:
                sett.append(ch)
            
            sett.sort()
            
            dic[tuple(sett)].append(wrd)
    
        return [val for key, val in dic.items()]
