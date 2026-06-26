class Solution:
    def isPalindrome(self, s, start, end):
        while start < end:
            if s[start] != s[end]:
                return False
            start, end = start + 1, end - 1
        
        return True

    def validPalindrome(self, s: str) -> bool:

        i = 0
        j = len(s) - 1

        while i < j:
            if s[i] != s[j]:
                return self.isPalindrome(s, i + 1, j) or self.isPalindrome(s, i, j-1)
            i, j = i + 1, j - 1
        return True
        