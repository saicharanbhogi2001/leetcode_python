class Solution:
    def arrangeCoins(self, n: int) -> int:
        i=1
        while True:
            n=n-i
            if n==0:
                return i
            if n<0:
                return i-1
            i+=1
