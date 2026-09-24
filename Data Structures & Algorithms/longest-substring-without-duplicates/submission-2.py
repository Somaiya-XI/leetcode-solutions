class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        charset = set()
        maxlength, l = 0,0

        for r in range(len(s)):
            while s[r] in charset:
                charset.remove(s[l])
                l+=1
            charset.add(s[r])
            maxlength = max(r - l + 1, maxlength)
        return maxlength            
