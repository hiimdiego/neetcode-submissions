class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        #Initialize slow and fast pointers
        slow = fast = 0
        #do while Loop
        while True:
            slow = nums[slow]
            fast = nums[nums[fast]]
            if slow == fast:
                break
        second = 0
        #do while Loop
        while True:
            second = nums[second]
            slow = nums[slow]
            if slow == second:
                return slow
        