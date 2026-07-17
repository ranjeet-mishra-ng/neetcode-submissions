class Solution:
    def compare(self, source, target):
        for i in range(26):
            if source[i] != target[i]:
                return False
        return True
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s2) < len(s1):
            return False
        target = [0] * 26
        source = [0] * 26

        for char in s1:
            target[ord(char) - ord('a')] += 1
        
        left = 0
        right = 0

        while right < len(s1):
            print(right)
            source[ord(s2[right]) - ord('a')] += 1
            right += 1
        
        
        while right <= len(s2):
            if self.compare(source, target):
                return True
            
            if right == len(s2):
                return False
            source[ord(s2[left]) - ord('a')] -= 1
            left += 1
            source[ord(s2[right]) - ord('a')] += 1
            right += 1
        return False


        