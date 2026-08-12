class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        #Initialize pointers, character count, and maxLength
        l = r = 0
        count = {}
        maxLength = 0
        #Traverse string
        for i in range (len(s)):
            count[s[i]] = count.get(s[i], 0) + 1
            while (r - l + 1) - max(count.values()) > k:
                count[s[l]] -= 1
                l += 1
            maxLength = max(maxLength, r - l + 1)
            r += 1
        return maxLength

        