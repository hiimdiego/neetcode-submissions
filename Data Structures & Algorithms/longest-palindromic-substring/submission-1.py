class Solution:
    def longestPalindrome(self, s: str) -> str:
        output = ""
        outputLen = 0
        for i in range(len(s)):
            l, r = i, i
            #odd length palindromes
            while l >= 0 and r < len(s) and s[l] == s[r]:
                if (r - l + 1) > outputLen:
                    outputLen = r - l + 1
                    output = s[l:r+1]
                l -= 1
                r += 1
            #even length palindromes
            l, r = i, i + 1
            while l >= 0 and r < len(s) and s[l] == s[r]:
                if (r - l + 1) > outputLen:
                    outputLen = r - l + 1
                    output = s[l:r+1]
                l -= 1
                r += 1
        return output
