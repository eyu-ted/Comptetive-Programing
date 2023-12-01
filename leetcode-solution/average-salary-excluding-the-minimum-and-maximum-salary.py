class Solution:
    def average(self, salary: List[int]) -> float:
        minn=min(salary)
        maxx=max(salary)
        total=sum(salary)
        return (total-maxx-minn)/float(len(salary)-2)
        