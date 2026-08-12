class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        n = len(nums)
        output = []

        curr_prefix = 1
        for num in nums:
            output.append(curr_prefix)
            curr_prefix *= num
        
        product = 1
        for i in range(n - 1, -1, -1):
            output[i] *= product
            product *= nums[i] 

        return output
        
            