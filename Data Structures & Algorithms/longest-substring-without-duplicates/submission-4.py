class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        #initialize set, pointer, and count
        visited = set()
        l = 0
        count = 0
        for r in range(len(s)):
            while s[r] in visited:
                visited.remove(s[l])
                l += 1
            visited.add(s[r])
            count = max(count, r - l + 1)
        return count
        