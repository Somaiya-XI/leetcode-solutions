class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        l, r = 0, len(numbers)-1

        while l < r:
            currentSum = numbers[r] + numbers[l]
            if currentSum < target:
                l += 1
            elif currentSum > target:
                r -= 1
            else:
                return [l+1, r+1]
        return []
            