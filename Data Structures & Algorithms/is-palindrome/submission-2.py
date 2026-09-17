class Solution:
    def isPalindrome(self, s: str) -> bool:
        cleaned = ''.join(re.findall("[A-Za-z0-9]", s.lower().replace(" ", "")))
        reversed = ""
        for char in cleaned:
            reversed = char + reversed
        return cleaned == reversed

