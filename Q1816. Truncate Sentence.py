class Solution:
    def truncateSentence(self, s: str, k: int) -> str:
        c=0
        a=[]
        for i in range(len(s)):
            if s[i]==" ":
                c+=1
            if c==k:
                break
            else:
                a.append(s[i])
        return "".join(a)
        
