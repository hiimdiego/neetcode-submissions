class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        if len(s) == 0:
            return 0
        maxLength = 1
        l, r = 0, 1
        stack = []
        stack.append(s[l])

        while r < len(s):
            while s[r] in stack:
                stack.pop(0)
                l += 1
            else:
                maxLength = max(maxLength, r - l + 1)
                stack.append(s[r])
            r += 1
        return maxLength