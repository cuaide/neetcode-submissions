class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        n = len(nums)
        second_nums = [1]*n
        for i in range(n):
            for j in range(n):
                if i != j:
                    second_nums[i] *= nums[j]
        return second_nums

