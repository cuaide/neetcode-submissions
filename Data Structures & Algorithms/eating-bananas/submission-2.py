from math import ceil
class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        left = 1
        right = max(piles)
        result = right
        while left <= right:
            cnt = 0
            mid = (left+right)//2
            for pile in piles:
                cnt+=ceil(pile/mid)
            if cnt > h:
                left = mid+1
            else:
                result = mid
                right = mid-1
        return result