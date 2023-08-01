from re import sub
class Solution:
    def isPalindrome(self, s: str) -> bool:
        s=sub("[\W_]", "", s.lower())
        for i in range(len(s)):
            if s[i] != s[len(s)-i-1]:
                return False
        return True
        