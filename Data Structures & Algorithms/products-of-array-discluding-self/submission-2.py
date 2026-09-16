class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        n = len(nums)
        res = [0]*n

        for index in range(n):
            prod = 1
            for j in range(n):
                if index == j:
                    continue
                prod *= nums[j]
                
            res[index] = prod
        return res