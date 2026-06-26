class Solution:
    def isPalindrome(self, s: str) -> bool:

        s = s.upper()

        original = ""
        reverse = ""
        for char in s:
            if char.isalnum():
                original += char
                reverse = char + reverse
        
        print(f"original: {original} reverse: {reverse}")
        
        return original == reverse
        