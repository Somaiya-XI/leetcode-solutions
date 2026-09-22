class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        counts = {}

        for n in nums:
            counts[n] = counts.get(n, 0) + 1
        
        result = sorted(counts, key=lambda num: counts[num], reverse=True)

        return result[:k]