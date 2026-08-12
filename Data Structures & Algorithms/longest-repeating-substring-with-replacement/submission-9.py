class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        freq = {}
        count = 0
        l = 0
        for r, c in enumerate(s):
            freq[c] = freq.get(c, 0) + 1
            length = r - l + 1
            highest_freq = max(freq.values())
            while ((r - l + 1 - max(freq.values())) > k):
                freq[s[l]] -= 1
                l += 1
            count = max(count, r - l + 1)
        return count
