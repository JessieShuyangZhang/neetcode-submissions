class Solution:
    def isPalindrome(self, s: str) -> bool:
        chars = ''.join(c.lower() for c in s if c.isalnum())
        return chars[::-1] == chars