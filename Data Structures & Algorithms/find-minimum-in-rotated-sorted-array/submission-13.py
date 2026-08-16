class Solution:
    def findMin(self, nums: List[int]) -> int:
        l, r = 0, len(nums) - 1
        min_num = 1000
        while l <= r:
            mid = (l+r) // 2
            min_num = min(min_num, nums[mid])
            if nums[l] < nums[mid] and nums[r] > nums[mid]:
                r = mid - 1
            elif nums[l] > nums[mid] and nums[r] > nums[mid]:
                r = mid - 1
            else:
                l = mid + 1
        return min_num