class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        n = len(s)
        left = 0
        right = 0
        max_len = 0
        count = 0
        seen = set()
        while right < n:
            if s[right] not in seen:
                seen.add(s[right])
                right += 1
                max_len = max(max_len, right - left)
            else:
                while s[right] in seen:
                    seen.remove(s[left])
                    left += 1
                seen.add(s[right])
                max_len = max(max_len, right - left)
                right += 1
        return max_len