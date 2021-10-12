class Solution:
    def isPalindrome(self, s: str) -> bool:
        r = ""
        for i in range(len(s)):
            if s[i].isalnum():
                r += s[i].lower()
        print(s)
        print(r)
        if r == r[::-1]:
            return True
        return False
            