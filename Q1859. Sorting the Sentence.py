class Solution:
    def sortSentence(self, s: str) -> str:
        data=s.split()
        n=len(data)
        res=[0]*(n+1)
        for i in data:
            res[int(i[-1])]=i[:-1]
        return ' '.join(res[1:])

                
