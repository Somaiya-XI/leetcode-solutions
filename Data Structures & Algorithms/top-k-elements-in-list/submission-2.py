class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        result = {}

        for n in nums:
            result[n] = result.get(n, 0) + 1

        result = sorted(result, key=lambda num: result[num], reverse=True)
        return result[:k]