class Solution:
    def search(self, nums: List[int], target: int) -> int:
        cnt = len(nums)
        low = 0
        high = cnt-1
        while(low <= high):
            mid = (low+high)//2
            if nums[mid]==target:
                return mid
            elif target<nums[mid]:
                high=mid-1
            else:
                low=mid+1
        return -1
        