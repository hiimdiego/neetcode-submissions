class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        #Check if list is empty
        if len(nums) == 0:
            return 0
        #Turn list into set
        vals = set(nums)
        #Keep track of current and longest sequence
        longest = 1
        #Iterate through each value in set
        for val in vals:
            curr = 1
            prev = val - 1
            #Check if value is start of a sequence
            if prev in vals:
                continue
            next_val = val + 1
            #Continue incrementing until sequence ends
            while next_val in vals:
                curr += 1
                next_val += 1
            if curr > longest:
                longest = curr
        #Return longest sequence
        return longest