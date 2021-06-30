class Solution:
    def toLowerCase(self, s: str) -> str:  
        a=[]
        for i in s:
            if ord(i)<91 and ord(i)>64:
                m=chr(ord(i)+32)
                a.append(m)
            else:
                a.append(i)
        return ''.join(a)
        
        
