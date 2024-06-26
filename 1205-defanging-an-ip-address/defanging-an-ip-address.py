class Solution:
    def defangIPaddr(self, address: str) -> str:
        ans = address.split(".")

        res = []

        for wrd in ans:
            res.append(wrd)
            res.append("[.]")
        
        res.pop()
        
        return "".join(res)
        
        