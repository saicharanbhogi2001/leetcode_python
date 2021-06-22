class Solution:
    def dominantIndex(self, nums: List[int]) -> int:
        m=max(nums)
        s=nums.index(m)
        c=0
        for i in range(len(nums)):
            if s!=i and (nums[i]*2)>m:
                return -1
        return s
           
