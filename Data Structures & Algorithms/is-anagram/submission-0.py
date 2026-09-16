class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s.strip()) == len(t.strip()):
            for char in s:
                if not char in t:
                    return False
            return True
        return False