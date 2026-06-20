class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        pref = ""
        i = 0
        while True:
            found = True
            for j in range(len(strs)):
                
                # Check if string is empty
                if len(strs[j]) == 0 or i == len(strs[j]):
                    found = False
                    break
                
                if j == 0:
                    continue
                
                if strs[j][i] != strs[j-1][i]:
                    found = False
        
            if found:
                pref += strs[0][i]
                i += 1
                
            else:
                break
        return pref
        