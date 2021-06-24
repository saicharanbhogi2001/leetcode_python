class Solution:
    def interpret(self, command: str) -> str:
        s=""
        n=""
        for i in command:
            s+=i
            if s=="(al)":
                n+="al"
                s=""
            elif s=="()":
                n+="o"
                s=""
            if s=="G":
                n+="G"
                s=""
        return n
