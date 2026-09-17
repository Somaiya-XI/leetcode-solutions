class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        
        map_s, map_t = {}, {}
        for index in range(len(s)):
            map_s[s[index]] = map_s.get(s[index], 0) + 1
            map_t[t[index]] = map_t.get(t[index], 0) + 1
        return map_s == map_t