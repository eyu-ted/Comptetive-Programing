class Solution:
    def relativeSortArray(self, arr1: List[int], arr2: List[int]) -> List[int]:
        arr1.sort()
        dic=Counter(arr1)
        dic2=Counter(arr2)
        ans=[]
        for n in arr2:
            ans.extend([n]*dic[n])
        for n in arr1:
            if n not in arr2:
                ans.append(n)
        return ans
        
        
        