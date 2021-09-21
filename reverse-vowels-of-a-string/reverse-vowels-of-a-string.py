class Solution:
    def reverseVowels(self, s: str) -> str:
        i, j = 0, len(s)-1
        s = list(s)
        while i<j:
            if s[i] not in "aeiouAEIOU":
                i += 1

            elif s[j] not in "aeiouAEIOU":
                j -=1

            else:
                s[i], s[j] = s[j], s[i]
                i += 1
                j -=1

        return "".join(s)
        # nList = []
        # l = []
        # for i in range(len(s)):
        #     l.append(s[i])
        # print(l)
        # for i in range(len(s)):
        #     if s[i] == 'a' or s[i] == 'e' or s[i] == 'i' or s[i] == 'o' or s[i] == 'u':
        #         nList.append(s[i])
        # nList.reverse()
        # for i in range(len(s)):
        #     if l[i] == 'a' or l[i] == 'e' or l[i] == 'i' or l[i] == 'o' or l[i] == 'u':
        #         l[i] = nList[i]
        # return nList