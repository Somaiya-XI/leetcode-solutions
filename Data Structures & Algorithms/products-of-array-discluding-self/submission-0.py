class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        res, count = [1]*len(nums), 0
        # nums[i] = nums[i+1] * nums[i+2]
        while count < len(nums): 
            for index in range(len(nums)):
                if count == index:
                    continue
                res[count] = res[count] * nums[index]
            count +=1
        return res