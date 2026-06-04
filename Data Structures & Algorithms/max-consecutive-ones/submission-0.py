class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        max = 0
        length = len(nums)
        cnt = 0
        for i in range(length):
            if nums[i] == 1:
                cnt += 1
                if max < cnt:
                    max = cnt
            else:
                cnt = 0
        return max 