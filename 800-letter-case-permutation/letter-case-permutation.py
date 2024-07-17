class Solution:
    def letterCasePermutation(self, s: str) -> List[str]:

        ans =[]
        def back(path,i):
            
            if len(path) == len(s):
                st = "".join(path)
                ans.append(st)
                return 
            if s[i].isalpha():
                path.append(s[i].lower())
                back(path, i+1)
                path.pop()
                
                path.append(s[i].upper())
                back(path, i+1)
                path.pop()
            else:
                path.append(s[i])
                back(path,i+1)
                path.pop()
        back([],0)

        return ans
                

        
        