class Solution:
    def trap(self, height: List[int]) -> int:
        if not height:
            return 0

        l, r = 0, len(height) - 1
        max_r, max_l = height[r] , height[l] 
        water_trapped = 0

        while l < r:
            if max_l < max_r:
                l+=1
                max_l = max(height[l], max_l)
                water_trapped += max_l - height[l] # max always first, so then no negative
            else:
                r-=1
                max_r = max(height[r], max_r)
                water_trapped += max_r - height[r]
        return water_trapped