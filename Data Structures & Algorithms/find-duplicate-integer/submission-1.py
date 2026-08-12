class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        #initialize slow and fast pointers
        slow, fast = 0, 0
        #do while loop
        while True:
            #move slow once and fast twice
            slow = nums[slow]
            fast = nums[nums[fast]]
            #if equal, break
            if slow == fast:
                break
        #initialize second slow pointer
        first = slow
        second = 0
        #do while loop
        while True:
            #advance pointers
            first = nums[first]
            second = nums[second]
            #if equal, return 
            if first == second:
                return second

        