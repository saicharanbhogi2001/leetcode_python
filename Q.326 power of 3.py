class Solution:
    def isPowerOfThree(self, n: int) -> bool:
       t=0
       while 1:
            if pow(3,t)==n:
                return True
            if pow(3,t)>n:
                return False
            t+=1
