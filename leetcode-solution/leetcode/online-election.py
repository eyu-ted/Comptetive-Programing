class TopVotedCandidate:

    def __init__(self, persons: List[int], times: List[int]):
        self.times = times
        self.lead = []

        dic=defaultdict(int)

        maxx = 0
        for i in range(len(persons)):
            dic[persons[i]]+=1

            if self.lead == []:
                self.lead.append(persons[i])
                maxx=1
            elif dic[persons[i]]>=maxx:
                maxx=dic[persons[i]]
                self.lead.append(persons[i])
            else:
                self.lead.append(self.lead[i-1])


    def q(self, t: int) -> int:

        index = bisect_right(self.times,t)
        return self.lead[index-1]


        


# Your TopVotedCandidate object will be instantiated and called as such:
# obj = TopVotedCandidate(persons, times)
# param_1 = obj.q(t)