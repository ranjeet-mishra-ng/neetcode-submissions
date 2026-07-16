class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        left = 0
        charset = dict()
        max_len = 0
        max_freq = 0

        for right in range(len(s)):
            charset[s[right]] = charset.get(s[right], 0) + 1
            max_freq = max(max_freq, charset[s[right]])

            
            while (right - left + 1) - max_freq > k:
                charset[s[left]] -= 1
                left += 1
            
            max_len = max(max_len, right - left + 1)
        return max_len
        