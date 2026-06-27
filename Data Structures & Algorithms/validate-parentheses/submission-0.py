class Solution:
    def isValid(self, s: str) -> bool:
        st = []
        map = {"(":")", "{": "}", "[": "]"}
        for i in range(len(s)):
            n = len(st)
            if s[i] in map.keys():
                st.append(s[i])
            else:
                if n == 0:
                    return False
                last = st[n - 1]
                if s[i] == map[last]:
                    st.pop()
                else:
                    return False
        
        return len(st) == 0
        