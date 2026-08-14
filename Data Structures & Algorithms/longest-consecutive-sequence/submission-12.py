class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        #Convert into set
        hash_set = set(nums)
        longest = 0
        #iterate over set
        for val in hash_set:
            curr = 0
            if (val - 1) not in hash_set: #only consider if start of sequence
                while val in hash_set:
                    curr += 1
                    val += 1
            longest = max(curr, longest) #update longest consectutive sequence
        return longest