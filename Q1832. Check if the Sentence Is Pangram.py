class Solution:
    def checkIfPangram(self, sentence: str) -> bool:
        data=[0]*26
        for i in sentence:
            data[ord(i)-97]=1
        return sum(data)==26
