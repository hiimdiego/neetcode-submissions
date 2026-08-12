class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        #Traverse first string and map characters to their frequency
        s1_count = {chr(i): 0 for i in range(ord('a'), ord('z') + 1)}
        for c in s1:
            s1_count[c] += 1
        #initialize pointer s2 character count
        l = 0
        s2_count = {chr(i): 0 for i in range(ord('a'), ord('z') + 1)}
        #Traverse second string
        for r, c in enumerate(s2):
            #Check if substring length is greater than first string
            while ((r - l + 1) > len(s1)):
                s2_count[s2[l]] -= 1
                l += 1
            #Update character count
            s2_count[c] += 1
            #Check if substring map matches first string map
            if r - l + 1 == len(s1) and s1_count == s2_count:
                return True
        return False