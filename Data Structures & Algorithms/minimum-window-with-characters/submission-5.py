class Solution:
    def minWindow(self, s: str, t: str) -> str:
        #base case
        if t == "": return ""
        #Create hash_maps for each string
        countT, window = {}, {}
        #iterate through t and update character count
        for c in t:
            countT[c] = countT.get(c, 0) + 1
        #initialize have and need
        have, need = 0, len(countT)
        #Iterate through s 
        l = 0
        res, lenRes = [-1, -1], float("infinity")
        for r, c in enumerate (s):
            #update character count for window
            window[c] = window.get(c, 0) + 1
            #Check if character is in t and counts in maps are equal
            if c in countT and window[c] == countT[c]:
                have += 1
            #while have is equal to need
            while have == need:
                rem = s[l]
                #update result 
                if (r - l + 1) < lenRes:
                    res, lenRes = [l, r], (r - l + 1)
                #pop from the left of our window
                window[rem] -= 1
                #check if removing character decreased have
                if rem in countT and window[rem] < countT[rem]:
                    have -= 1
                l += 1
        l, r = res
        return s[l:r+1] if lenRes != float("infinity") else ""



        