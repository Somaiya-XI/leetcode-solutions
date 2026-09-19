class Solution:
    def maxArea(self, heights: List[int]) -> int:
        l, r = 0, len(heights) - 1
        maxArea = 0
        while l < r:
            area = (r - l) * min(heights[l], heights[r])
            maxArea = max(maxArea, area)

            if heights[l] < heights[r]:
                l+=1
            else: # we have an  option to choose when they are equal thus we also decrement right
                r-=1
        return maxArea