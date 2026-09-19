class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        result = []
        nums.sort()

        for i, a in enumerate(nums):
            if i > 0 and a == nums[i - 1]: #if it is first element or a alraedy calculated e.g [-3,-3,1]
                continue
            
            l, r = i + 1, len(nums) - 1
            while l < r:
                currentSum = a + nums[l] + nums[r]
                if currentSum > 0:
                    r -=1
                elif currentSum < 0:
                    l += 1
                else:
                    result.append([a, nums[l], nums[r]])
                    l +=1
                    # check duplicate on left only, right checked by conditions above
                    while nums[l] == nums[l-1] and l < r: 
                        l +=1
        return result