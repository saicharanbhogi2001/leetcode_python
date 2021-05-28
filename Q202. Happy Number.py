class Solution:
    def isHappy(self, n: int) -> bool:
        s=0
        if n==1:
            return True
        if n==2 or n==3:
            return False
        while n:
            r=n%10
            n=n//10
            s=s+pow(r,2)
            if n==0 and s>4:
                n=s
                s=0
        if s==1:
            return True

            
