class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        seen = {}
        for number in nums:
            seen[number] = seen.get(number, 0) + 1
        seen = sorted(seen, key= seen.get, reverse=True)
        return seen[:k]



# [1,1,2,3,3,2,2,3,3] seen = {1:2, 2: 3, 3: 4} 
# dict(sorted(seen.items(), key=lambda item:item[1], reverse=True)) --> {3: 4, 2: 3, 1:2}
# seen = sorted(seen, key=seen.get, reverse=True)
# ^ only keys which represents values here, sorted into list