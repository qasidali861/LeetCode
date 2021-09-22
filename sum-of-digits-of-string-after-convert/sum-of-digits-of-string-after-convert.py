class Solution:
    def getLucky(self, s: str, k: int) -> int:
        
        dic = {'a':1, 'b':2, 'c':3, 'd':4, 'e':5, 'f':6, 'g':7, 'h':8, 'i':9, 'j':10, 'k':11, 'l':12, 'm':13, 'n':14, 'o':15, 'p':16, 'q':17, 'r':18, 's':19, 't':20, 'u':21, 'v':22, 'w':23, 'x':24, 'y':25, 'z':26}
        
        n = ''
        for i in s:
            n += str(dic[i])
        n = int(n)
        
        count = 0
        val = 0
        while (1):
            while n != 0:
                rem = n%10
                n = n//10
                val += rem
            count+=1
            if count==k:
                return val
            else:
                n = val
                val = 0  