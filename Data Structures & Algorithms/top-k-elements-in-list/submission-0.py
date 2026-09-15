class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        seen = {}
        for number in nums:
            seen[number] = seen.get(number, 0) + 1
        seen = sorted(seen, key= seen.get, reverse=True)
        return seen[:k]