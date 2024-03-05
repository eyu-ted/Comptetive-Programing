class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        lis=[[],[],['a','b','c'],['d','e','f'],['g','h','i'],['j','k','l'],['m','n','o'],['p','q','r','s'],['t','u','v'],['w','x','y','z']]
        ans = []

        def back(start,path):
            print(path)
            if len(path) == len(digits) and path !=[]:
                ans.append("".join(path))
                return 


            for i in range(start,len(digits)):
                for ch in lis[int(digits[i])] :
                    path.append(ch)

                    back(i+1,path)

                    path.pop()
        back(0,[])
        return ans

                



        