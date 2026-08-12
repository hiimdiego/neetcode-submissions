class Solution:
    def isPalindrome(self, s: str) -> bool:
        l, r = 0, len(s) - 1

        while l < r:
            while l < r and not s[l].isalnum():
                l += 1
            left = s[l].lower()

            while r > l and not s[r].isalnum():
                r -= 1
            right = s[r].lower()

            if left != right:
                return False
            l += 1
            r -= 1

        return True