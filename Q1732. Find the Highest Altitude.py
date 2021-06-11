class Solution:
    def largestAltitude(self, gain: List[int]) -> int:
        s=[]
        s.append(0)
        l=0
        for i in range(len(gain)):
            for j in range(i+1):
                l=l+gain[j]
            s.append(l)
            l=0
        return max(s)
        
