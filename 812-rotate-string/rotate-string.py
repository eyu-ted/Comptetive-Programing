class Solution:
    def rotateString(self, s: str, goal: str) -> bool:
        if len(s) != len(goal):
            return False
        
        for k in range(len(s)):
            flag = True
            for j in range(len(s)):
                r = (j+k)%len(s)
                if s[j] != goal[r]:
                    flag = False
            
            if flag:
                return True
        return False

