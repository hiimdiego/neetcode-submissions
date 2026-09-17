class Solution:
    def countSubstrings(self, s: str) -> int:
        numPalindromes = len(s)
        for i in range(len(s)):
            l, r = i, i
            while l >= 0 and r < len(s) and s[l] == s[r]:
                if (r - l + 1) > 1:
                    numPalindromes += 1
                l -= 1
                r += 1
            l, r = i, i + 1
            while l >= 0 and r < len(s) and s[l] == s[r]:
                if (r - l + 1) > 1:
                    numPalindromes += 1
                l -= 1
                r += 1
                
        return numPalindromes