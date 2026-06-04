class Solution:
    def countSubstrings(self, s: str) -> int:
        res = ""
        reslen = 0
        num = 0
        for i in range(len(s)):
            #find about odd palindrome
            l,r = i,i
            while l >= 0 and r < len(s) and s[l] == s[r]:
                num += 1
                l = l-1 
                r = r+1 
            #find about even palindrome
            l,r = i,i+1
            while l >= 0 and r < len(s) and s[l] == s[r]:
                num += 1 
                l = l-1 
                r = r+1
        return num 