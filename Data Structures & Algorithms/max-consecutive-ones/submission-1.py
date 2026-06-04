class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        res = 0
        length = len(nums)
        cnt = 0
        for i in range(length):
            if nums[i] == 1:
                cnt += 1
                if res < cnt:
                    res = cnt
            else:
                cnt = 0
        return res 