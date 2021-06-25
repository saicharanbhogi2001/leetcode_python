class Solution:
    def reverseWords(self, s: str) -> str:
        a=[]
        data=s.split()
        for i in range(len(data)):
            w=data[i]
            s=w[::-1]
            a.append(s)
            a.append(" ")
        return ''.join(a).rstrip()
            
            
