class Solution:
    def isAnagram(self, s, t):
        freq = [0] * 26
        for c in s:
            freq[ord(c) - ord('a')] += 1
        
        for c in t:
            freq[ord(c) - ord('a')] -= 1
        
        for i in range(26):
            if freq[i] != 0:
                return False
        return True


    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:

        res = []
        used = [False] * len(strs)

        for i in range(len(strs)):
            if used[i]:
                continue
            s = []
            s.append(strs[i])
            used[i] = True
            for j in range(i + 1, len(strs)):
                if self.isAnagram(strs[i], strs[j]):
                   used[j] = True
                   s.append(strs[j])
            res.append(list(s))
        
        return res
            

        