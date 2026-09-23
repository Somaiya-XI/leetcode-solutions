class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        l, res = 0, 0
        charSet = set()
        for r in range(len(s)): # [l:z x y z x]
            while s[r] in charSet:
                charSet.remove(s[l]) # z-out {x, y} | x-out {y, z}
                l+=1
            charSet.add(s[r]) #{z} {z, x} {z, x, y} {x, y, z} {y, z , x}
            res = max(r - l + 1, res)
        return res