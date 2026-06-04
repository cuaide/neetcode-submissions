class Solution:
    def maxArea(self, heights: List[int]) -> int:
        max_contain = 0
        for i in range(len(heights)):
            for j in range(i+1,len(heights)):
                max_contain = max(max_contain,min(heights[i],heights[j])*(j-i))
        return max_contain