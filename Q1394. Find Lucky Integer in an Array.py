class Solution:
    def findLucky(self, arr: List[int]) -> int:
        dic={}
        for i in arr:
            if i not in dic.keys():
                dic[i]=1
            else:
                dic[i]+=1
        res=0
        for k,v in dic.items():
            if k==v:
                res=max(res,k)
        if res==0:
            return -1
        return res
