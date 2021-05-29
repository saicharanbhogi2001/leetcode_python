class Solution:
    def maximum69Number (self, num: int) -> int:
        def pot(num,c,i):
            h=0
            s=0
            k=1
            while num:
                r=num//pow(10,i-1)
                num=num%pow(10,i-1)
                if k==c:
                    s=s*10+9
                else:
                    s=s*10+r
                k=k+1
                i=i-1
            return s
        c=1
        l=m=i=0
        temp=num
        while temp:
            temp=temp//10
            i+=1
        temp=num
        while num:
            l=pot(num,c,i)
            c=c+1
            if l>m:
                m=l
            if c==i+1:
                break
        if m>temp:
            return m
        else:
            return temp
