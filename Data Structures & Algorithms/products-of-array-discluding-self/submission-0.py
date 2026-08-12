class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        output = []

        #iterate through array and store prefix products
        output.append(1)
        product = nums[0]
        for i in range (1, len(nums)):
            output.append(product)
            product *= nums[i]
        
        #iterate through array backwards and store suffix products
        product = 1
        for i in range(len(nums) - 1, -1, -1):
            output[i] *= product
            product *= nums[i]
        
        return output
