class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        vals = set(nums)

        longest = 0

        for val in vals:
            curr = 1
            next_val = val + 1
            
            while next_val in vals:
                next_val += 1
                curr += 1

            if curr > longest:
                longest = curr

        return longest