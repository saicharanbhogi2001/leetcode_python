class Solution:
    def runningSum(self, nums: List[int]) -> List[int]:
        k=[]
        s=0
        for i in nums:
            s=s+i
            k.append(s)
        return k
