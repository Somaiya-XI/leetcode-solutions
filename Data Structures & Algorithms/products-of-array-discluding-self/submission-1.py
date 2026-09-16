class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        res, count = [0]*len(nums), 0
        # nums[i] = nums[i+1] * nums[i+2]
        for index in range(len(nums)):
            prod = 1
            for j in range(len(nums)):
                if index == j:
                    continue
                prod *= nums[j]
            res[index] = prod
        return res