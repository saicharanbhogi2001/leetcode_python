class Solution:
    def isPowerOfFour(self, n: int) -> bool:
        t=0
        while 1:
            if pow(4,t)==n:
                return True
            if pow(4,t)>n:
                return False
            t+=1
        
