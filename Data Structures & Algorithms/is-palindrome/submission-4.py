class Solution:
    def isPalindrome(self, s: str) -> bool:
        stat=False
        s= "".join(c.lower() for c in s if c.isalnum())
        if s == "" or s == s[::-1]:
            return True
        n=len(s)
        print(n)
        for i in range(int(n/2)):
            print(s[i]+"+"+s[n-i-1])
            if(s[i]==s[n-i-1]):
                stat=True
            else:
                stat=False
                break
        return stat