class Solution:
    def shiftingLetters(self, s: str, shifts: List[List[int]]) -> str:
        prefsum=[0]*(len(s)+1)
        curr=0
        for i in range(len(shifts)):
            if shifts[i][2]:
                change=1
            else:
                change=-1
            prefsum[shifts[i][0]]+=change
            prefsum[shifts[i][1]+1]-=change
    
        ans=[]
        for i, c in enumerate(s):
            curr = (curr + prefsum[i]) % 26
            num = (ord(s[i]) - ord('a') + curr + 26) % 26
            ans.append(chr(ord('a') + num))
        

        return "".join(ans)