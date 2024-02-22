class Solution:
    def bestClosingTime(self, customers: str) -> int:
        score=maxx=0
        high_score=-1
        for i in range(len(customers)):
            if customers[i]=="Y":
                score+=1
            else:
                score-=1
            if score>maxx:
                maxx=score
                high_score=i
        return high_score+1

        