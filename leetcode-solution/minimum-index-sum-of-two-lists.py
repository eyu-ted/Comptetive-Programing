class Solution:
    def findRestaurant(self, list1: List[str], list2: List[str]) -> List[str]:
        dic={}
        for i in range(len(list1)):
            if list1[i] in list2:
                dic[list1[i]]=i
        for j in range(len(list2)):
            if list2[j] in list1:
                dic[list2[j]]+=j
        minn=min(dic.values())
        res=[]
        for key in dic.keys():
            if dic[key]==minn:
                res.append(key)
        return res