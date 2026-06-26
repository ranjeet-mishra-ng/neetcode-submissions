class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:

        m = len(word1)
        n = len(word2)
        i, j = 0, 0

        res = ''

        while i < m and j < n:
            res = res + word1[i] + word2[j]
            i += 1
            j += 1

        
        while i < m: 
            res = res + word1[i]
            i += 1

        while j < n: 
            res = res + word2[j]
            j += 1
        
        return res

        

        