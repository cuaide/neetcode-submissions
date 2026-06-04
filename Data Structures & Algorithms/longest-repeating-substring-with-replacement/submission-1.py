class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        #brutal force #AABBC-> Find the minimum repeating alphabet and change it into maximum alphabet
        res = 0
        seconds = set(s)
        for second in seconds:
            count = l = 0
            for r in range(len(s)):
                if second == s[r]:
                    count += 1
                while (r-l+1)-count > k:
                    if second == s[l]:
                        count -= 1
                    l += 1 
                res = max(res,r-l+1)
        return res

            