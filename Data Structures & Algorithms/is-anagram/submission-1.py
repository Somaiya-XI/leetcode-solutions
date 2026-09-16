class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s.strip()) == len(t.strip()):
            map_s = {}
            map_t = {}
            for char in s:
                map_s[char] = map_s.get(char, 0) + 1  
                if char in t:
                   map_t[char] = map_t.get(char, 0) + 1
            return map_s == map_t
        return False