class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        #Turn list into set
        vals = set(nums)
        #Keep track of longest sequence
        longest = 0
        #Iterate through each value in set
        for val in vals:
            curr = 1
            next_val = val + 1
            #Continue incrementing until sequence ends
            while next_val in vals:
                curr += 1
                next_val += 1
            if curr > longest:
                longest = curr
        #Return longest sequence
        return longest