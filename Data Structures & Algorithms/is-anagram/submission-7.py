class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        #Check is string lengths are the same
        if len(s) != len(t):
            return False
        
        #Create array to measure frequency of each character
        count = [0]*26

        #Traverse string s and update count
        for i in range (len(s)):
            count[ord(s[i]) - ord('a')] += 1
            count[ord(t[i]) - ord('a')] -= 1

        #Check that count == 0
        for val in count:
            if val != 0:
                return False
        return True