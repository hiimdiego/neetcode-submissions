class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        #Initialize pointers, character count, and maxLength
        l = 0
        freq = {}
        maxLength = 0
        #Traverse string
        for r, c in enumerate (s):
            #update character count
            freq[c] = freq.get(c, 0) + 1
            #while loop
            while (r - l + 1 - max(freq.values()) > k):
                freq[s[l]] -= 1
                l += 1
            #update max length and right pointer
            maxLength = max(maxLength, r - l + 1)
        return maxLength
        