class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        #Bucketsort
        cnt = [0]*3
        for num in nums:
            cnt[num] += 1
        index= 0
        for i in range(3):
            while cnt[i]:
                cnt[i] -= 1
                nums[index] = i
                index += 1
        return nums