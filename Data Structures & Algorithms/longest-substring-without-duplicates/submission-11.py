class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        l, r = 0, 0
        length = 0
        seen = set()
        while r < len(s):
            while s[r] in seen:
                seen.remove(s[l])
                l += 1
            if (r - l + 1) > length:
                length = r - l + 1
            seen.add(s[r])
            r += 1
        return length