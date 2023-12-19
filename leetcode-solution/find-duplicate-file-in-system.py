class Solution:
    def findDuplicate(self, paths: List[str]) -> List[List[str]]:
        dic=defaultdict(list)
        ans=[]
        for path in paths:
            path=path.split()
            root=path[0]
            for strr in path[1:]:
                name,dash,data=strr.partition("(")
                dic[data].append(root+"/"+name)
        for value in dic.values() :
            if len(value)>1:
                ans.append(value)
        return ans
