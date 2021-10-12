class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        j = 0
        strr = ""
        for i in s:
            # print(i)
            while j < len(t):
                # print(t[j])
                if i == t[j]:
                    print(t[j])
                    strr += t[j]
                    j += 1
                    break
                j += 1
        if s == strr:
            return True
        return False