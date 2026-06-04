class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        max_count = 0
        cnt = 0
        for num in nums:
            cnt +=1 if num == 1 else 0
            max_count = max(max_count,cnt)
            if num == 0:
                cnt = 0
        return max_count