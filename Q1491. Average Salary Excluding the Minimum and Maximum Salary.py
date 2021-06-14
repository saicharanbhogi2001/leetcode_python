class Solution:
    def average(self, salary: List[int]) -> float:
        m=0
        s=0
        salary.sort()
        m=max(salary)
        salary.remove(m)
        k=min(salary)
        salary.remove(k)
        for i in range(len(salary)):
            s=s+salary[i]
        l=len(salary)
        m=s/l
        return m
