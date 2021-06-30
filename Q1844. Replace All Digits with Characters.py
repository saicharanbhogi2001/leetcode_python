class Solution:
    def replaceDigits(self, s: str) -> str:
        a=[]
        for i in range(len(s)):
            if ord(s[i])<97:
                m=chr(ord(s[i-1])+int(s[i]))
                a.append(m)
            else:
                a.append(s[i])
        return ''.join(a)
        
