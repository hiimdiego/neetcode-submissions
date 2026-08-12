class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        #Initialize pointers, character count, and maxLength
        l = 0
        count = {}
        maxLength = 0
        #Traverse string
        for r in range (len(s)):
            #update character count
            count[s[r]] = count.get(s[r], 0) + 1
            #while loop
            while (r - l + 1) - max(count.values()) > k:
                count[s[l]] -= 1
                l += 1
            #update max length and right pointer
            maxLength = max(maxLength, r - l + 1)
        return maxLength

        