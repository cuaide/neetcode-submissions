class Solution:

    def encode(self, strs: List[str]) -> str:
        res = ""
        for s in strs:
            res += str(len(s)) + "#" + s
        return res 
        
    def decode(self, s: str) -> List[str]:
        res = []
        i = 0

        while i < len(s):
            j = i # j = 0 
            while s[j] != '#':
                j += 1 # j = 1 
            length = int(s[i:j]) #length = 1
            i = j + 1 #i = 2 
            j = i + length # j = 3
            res.append(s[i:j]) # res[2:3]
            i = j # i = 3

        return res