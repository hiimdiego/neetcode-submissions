class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        freq = {}
        longest_str = 0
        l = 0
        for r, c in enumerate(s):
            freq[c] = freq.get(c, 0) + 1
            while ((r - l + 1) - max(freq.values())) > k:
                freq[s[l]] -= 1
                l += 1

            longest_str = max(longest_str, r - l + 1)
        
        return longest_str