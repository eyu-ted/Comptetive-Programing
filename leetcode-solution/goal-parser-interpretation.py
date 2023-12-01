class Solution:
    def interpret(self, command: str) -> str:
        res=""
        for i in range(len(command)):
            if command[i].isalpha():
                res+=command[i]
            elif i+1<len(command) and command[i]=="(" and command[i+1]==")":
                res+="o"
        return res
        