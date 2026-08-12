class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        n = len(nums)
        prefixes = []
        suffixes = []

        curr_prefix = 1
        for num in nums:
            prefixes.append(curr_prefix)
            curr_prefix *= num
        
        curr_suffix = 1
        for num in reversed(nums):
            suffixes.insert(0, curr_suffix)
            curr_suffix *= num
        
        output = []
        for i in range(n):
            output.append(suffixes[i]*prefixes[i])

        return output
        
            