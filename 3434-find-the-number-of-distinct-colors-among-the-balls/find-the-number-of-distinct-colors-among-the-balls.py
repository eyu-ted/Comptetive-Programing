class Solution:
    def queryResults(self, limit: int, queries: List[List[int]]) -> List[int]:

        colors = set()
        result = []


        dic = {}
        count = defaultdict(int)
        for indx , color in queries:
            if indx in dic and dic[indx]:
                count[dic[indx]] -= 1
                if count[dic[indx]] <=0:
                    colors.remove(dic[indx])
                    dic[indx] = 0 
                

            dic[indx] = color
            colors.add(color)
            count[color] += 1

            result.append(len(colors))

        return result


            

        