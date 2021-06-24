class Solution:
    def balancedStringSplit(self, s: str) -> int:
        l,r,b=0,0,0
        for i in s:
            if i=="L":
                l+=1
            if i=="R":
                r+=1
            if l==r:
                b+=1
        return b
