class Solution:
    def isPalindrome(self, s: str) -> bool:
        res = []
        cnt = 0
        for ch in s:
            if ch.isalnum():
                res.append(ch.lower())#to convert uppercase letters to lowercase letters 
        left, right = 0, len(res) - 1
        mid = (left + right) // 2
        for i in range(mid + 1): 
            if res[i] == res[right - i]:
                cnt += 1
        return cnt == mid + 1