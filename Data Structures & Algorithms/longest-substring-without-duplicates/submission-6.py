class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        if len(s) == 0:
            return 0
        maxLength = 1
        l, r = 0, 1
        seen = set()
        seen.add(s[0])

        while r < len(s):
            while s[r] in seen:
                seen.remove(s[l])
                l += 1
            seen.add(s[r])
            maxLength = max(maxLength, r - l + 1)
            r += 1

        return maxLength