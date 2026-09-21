class Solution:
    def trap(self, h: List[int]) -> int:
        if not h:
            return 0

        l, r = 0, len(h) - 1
        lMax, rMax = h[l], h[r]
        trapped = 0

        while l < r:
            if lMax < rMax:
                l+=1
                lMax = max(lMax, h[l])
                trapped += lMax - h[l]
            else:
                r-=1
                rMax = max(rMax, h[r])
                trapped += rMax - h[r]
        return trapped