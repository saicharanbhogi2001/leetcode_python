class Solution:
    def findTheDifference(self, s: str, t: str) -> str:
        dic={}
        for i in t:
            if i not in dic:
                dic[i]=1
            else:
                dic[i]+=1
        for i in s:
            dic[i]-=1
        for k,v in dic.items():
            if v==1:
                return k
        return -1
            
        
