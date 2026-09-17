class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        numbers = set(nums) # remove duplicate
        longest = 0
        for n in numbers:
            if n - 1 in numbers:
                continue
            length = 1

            while n + length in numbers: #4 -> 4 + 1 = 5 l=2, 4+2 = 6, l=3 etc
                length +=1
            longest = max(longest, length)
        return longest
