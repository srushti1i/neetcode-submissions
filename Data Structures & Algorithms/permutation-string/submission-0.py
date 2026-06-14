class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        str1=[0]*26
        str2=[0]*26
        for c in s1:
            str1[ord(c)-ord('a')]+=1
        for r in range(len(s2)):
            str2[ord(s2[r])-ord('a')]+=1
            if r>=len(s1):
                str2[ord(s2[r-len(s1)])-ord('a')]-=1
            if str1==str2:
                return True
        return False