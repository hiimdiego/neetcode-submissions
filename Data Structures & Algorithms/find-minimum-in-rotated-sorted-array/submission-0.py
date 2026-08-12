class Solution:
    def findMin(self, nums: List[int]) -> int:
        #initialize pointers and output
        l, r = 0, len(nums) - 1
        output = nums[0]
        #while loop
        while l <= r:
            #check if left is less than right
            if nums[l] < nums[r]:
                output = min(output, nums[l])
                break
            #compute mid index
            m = (l + r) // 2
            output = min(output, nums[m])
            #check if mid is greater than or equal to left
            if nums[m] >= nums[l]:
                l = m + 1
            else:
                r = m - 1
        return output
        