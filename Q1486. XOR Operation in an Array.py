class Solution:
    def xorOperation(self, n: int, start: int) -> int:
        s=1
        res=start
        start=2+start
        while(s<n):
            res=res^start
            start=2+start
            s+=1
        return res
        
