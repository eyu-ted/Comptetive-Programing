class Solution:
    def longestPalindrome(self, s: str) -> int:
    
        dic=Counter(s)
        ans=0
        flag=0
        for keys in dic.keys():
            if dic[keys]%2==0:
                ans+=dic[keys]
            else:
                flag=1
                ans+=dic[keys]-1
        if flag:
            ans+=1
        return ans

        
        