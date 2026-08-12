class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        n = len(nums)
        output = []
        for i in range(n):
            curr = 1
            for j in range(n):
                if j != i:
                    print(curr)
                    curr *= nums[j]
            output.append(curr)
        return output