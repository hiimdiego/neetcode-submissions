class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        output = []
        for i in range(len(nums) - 2):
            if i != 0 and nums[i - 1] == nums[i]:
                continue
            l, r = i + 1, len(nums) - 1
            while l < r:
                total = nums[i]+nums[l]+nums[r]
                if total == 0:
                    output.append([nums[i], nums[l], nums[r]])
                    l += 1
                    while nums[l-1] == nums[l] and l < r:
                        l += 1
                elif total < 0:
                    l += 1
                else:
                    r -= 1
        return output


