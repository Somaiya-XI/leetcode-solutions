class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        n = len(nums)
        result = [1]*n

        prefix = 1 
        for i in range(n): # from 0 -> n
            result[i] = prefix
            prefix *= nums[i]
        
        postfix = 1
        for i in range(n - 1, -1, -1):  # from n -> 0 
            result[i] *= postfix
            postfix *= nums[i]
        return result


        """
        going through the arr from beginning and multiply each in nums
        #[1,2,3,4] -> res[0] = 1
        prefix = 1 * nums_value(1)
        prefix = 1
        res[1] = 1
        prefix = 1 * 2
        res[2] = 2
        prefix = 2 * 3
        res[3] = 6
        now res [1,1,2,6]
        postfix = 1
        res[3] = 6 * 1 , postfix = 1 * nums_value_at_end(4)
        res[2] = 2 * 4 = 8, postfix = 4 * 3
        res[1] = 12, postfix = 12 * 2
        res[0] = 24
        res now = [24, 12, 8, 6]
        """