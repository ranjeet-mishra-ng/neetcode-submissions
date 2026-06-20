class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        # Approach 1
        # n = len(s)
        # m = len(t)

        # if n != m:
        #     return False

        # count_s = {}
        # count_t = {}

        # for c in s:
        #     if c not in count_s:
        #         count_s[c] = 1
        #     else:
        #         count_s[c] += 1
        
        # for c in t:
        #     if c not in count_t:
        #         count_t[c] = 1
        #     else:
        #         count_t[c] += 1
        
        # for char in count_s:
        #     if count_s[char] != count_t.get(char, 0):
        #         return False
        # return True

        # Approach 2
        n = len(s)
        m = len(t)

        if n != m:
            return False
        
        count = {}
        for c in s:
            if c not in count:
                count[c] = 1
            else:
                count[c] += 1
        
        for c in t:
            if c not in count:
                count[c] = -1
            else:
                count[c] -= 1
        
        for char in count:
            if count[char] != 0:
                return False
        return True
        




        

        

        