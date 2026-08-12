class Solution:
    def search(self, nums: List[int], target: int) -> int:
        l, r = 0, len(nums) - 1
        while l <= r:
            m = l + (r - l) // 2
            mid = nums[m]
            if mid == target:
                return m
            #left sorted portion
            if nums[l] <= mid:
                if target < nums[l] or target > mid:
                    l = m + 1
                else:
                    r = m - 1
            #right sorted portion
            else:
                if target < mid or target > nums[r]:
                    r = m - 1
                else:
                    l = m + 1
        return -1
        