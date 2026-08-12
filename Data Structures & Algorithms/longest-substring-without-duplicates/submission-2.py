class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        #initialize set, pointer, and count
        visited = set()
        l = 0
        count = 0
        #traverse list
        for r in range (len(s)):
            #check if current character is in set
            while s[r] in visited:
                visited.remove(s[l])
                l += 1
            visited.add(s[r])
            #update count
            count = max(count, r - l + 1)
        return count