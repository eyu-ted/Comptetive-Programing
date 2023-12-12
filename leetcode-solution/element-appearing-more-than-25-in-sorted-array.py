class Solution:
    def findSpecialInteger(self, arr: List[int]) -> int:
        from collections import Counter
        dic=Counter(arr)


        for keys,values in dic.items():
            if (dic[keys]/len(arr))* 100 > 25:
                return keys
        