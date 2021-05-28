class Solution:
    def hammingWeight(self, n: int) -> int:
        c=0
        while n:
            r=n%2
            n=n//2
            if r==1:
                c+=1
        return c
