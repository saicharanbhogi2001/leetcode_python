class Solution:
    def findNumbers(self, nums: List[int]) -> int:
        def count(n):
            e=0
            while n:
                r=n%10
                n=n//10
                e+=1
            return e
        m=0
        for i in range(len(nums)):
            l=count(nums[i])
            if l%2==0:
                m+=1
        return m 
