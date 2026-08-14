class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        prod = 1
        prefixArr = [1] * len(nums)
        for i in range(len(nums) - 1):
            prod *= nums[i]
            prefixArr[i + 1] = prod
        #[1, 1, 2, 8]
        prod = 1
        suffixArr = [1] * len(nums)
        for j in range(len(nums) - 1, 0, -1):
            prod *= nums[j]
            suffixArr[j - 1] = prod
        #[48, 24, 6, 1]
        #[1, 1, 1, 1]
        output = [1] * len(nums)
        for k in range(len(nums)):
            output[k] = prefixArr[k]*suffixArr[k]

        return output