class Solution:
    def halvesAreAlike(self, s: str) -> bool:
        
        s=s.lower()
        countA, countB=0 , 0
        mid=len(s)//2
        for i in range(mid):                       
            if s[i]=='a'  or s[i]=='e' or s[i]=='i' or s[i]=='o' or s[i]=='u':
                countA+=1
            if s[i+mid]=='a'  or s[i+mid]=='e' or s[i+mid]=='i' or s[i+mid]=='o' or s[i+mid]=='u': 
                countB+=1
        return(countA==countB)