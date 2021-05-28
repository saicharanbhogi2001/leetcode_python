class Solution:
    def subtractProductAndSum(self, n: int) -> int:
        s,m=0,1
        while n:
            r=n%10
            n=n//10
            s=s+r
            m=m*r
        if m>s or s>m:
            m,s=s,m
        t=s-m
        return t
