class Solution:
    def findMin(self, nums: List[int]) -> int:
        #initialize pointers and output
        l, r = 0, len(nums) - 1
        output = nums[0]
        #while loop
        while l <= r:
            #check if left is less than right
            if nums[l] < nums[r]:
                output = min(nums[l], output)
            #compute mid index
            mid = l + (r - l) // 2
            output = min(nums[mid], output)
            #check if mid is greater than or equal to left
            if nums[mid] >= nums[l]:
                l = mid + 1
            else:
                r = mid - 1
        return output