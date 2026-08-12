class Solution:
    def isPalindrome(self, s: str) -> bool:
        #Assign left and right pointers
        l, r = 0, len(s) - 1
        #While left ptr is less than right ptr, traverse string
        while (l < r):
            #Check if left pointer is valid character
            while (l < r and not self.alphaNum(s[l])):
                l += 1
            #Check if right pointer is valid character
            while (r > l and not self.alphaNum(s[r])):
                r -= 1
            #If left ptr != right ptr, not palindrome
            if (s[l].lower() != s[r].lower()):
                return False
            #Increment left ptr, decrement right ptr
            l, r = l + 1, r - 1
        return True
    #Function to determine whether character is valid
    def alphaNum(self, c):
        return (ord('a') <= ord(c) <= ord('z') or 
        ord('A') <= ord(c) <= ord('Z') or 
        ord('0') <= ord(c) <= ord('9'))