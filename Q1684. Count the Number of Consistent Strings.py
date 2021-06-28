class Solution:
    def countConsistentStrings(self, allowed: str, words: List[str]) -> int:
        a=[]
        for i in range(len(words)):
            for j in range(len(words[i])):
                if words[i][j] not in allowed:
                    a.append(i)
                    break
        return (len(words)-len(a))
        
