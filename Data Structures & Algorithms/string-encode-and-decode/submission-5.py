class Solution:

    def encode(self, strs: List[str]) -> str:
        if len(strs) == 0:
            return ""

        res = ""
        for text in strs:
            res += str(len(text)) + "#" + text
        
        return res

       

    def decode(self, s: str) -> List[str]:
        res = []
        if len(s) == 0:
            return res
        
        
        k = 0
        while k < len(s):
            count = ""
            while s[k] != '#':
                count = count + s[k]
                k += 1
            
            count = int(count)
            text = ""
            while count:
                text = text + s[k + 1]
                k = k + 1
                count -= 1
            res.append(text)
            k = k + 1


        return res

        


        
