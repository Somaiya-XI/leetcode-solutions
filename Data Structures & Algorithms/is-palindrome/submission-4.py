class Solution:
    def isPalindrome(self, s: str) -> bool:
        s = "".join(re.findall("[a-z A-Z 0-9]", s.lower().replace(" ", "")))
        reverse = ""

        for char in s:
            reverse = char + reverse
        return reverse == s