class Solution:
    def addDigits(self, num: int) -> int:
        s,r=0,0
        while num:
            r=num%10
            num=num//10
            s=s+r
            if num==0 and s>9:
                num=s
                s=0
        return s
            
            
