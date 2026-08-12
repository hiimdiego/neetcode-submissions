class Solution:
    def minWindow(self, s: str, t: str) -> str:
        #base case
        if t == "" : return ""
        #Create hash_maps for each string
        window, countT = {}, {}
        #iterate through t and update character count
        for c in t:
            countT[c] = countT.get(c, 0) + 1
        #initialize have and need
        have, need = 0, len(countT)
        l = 0 
        res, resLen = [-1, -1], float("infinity")
        #Iterate through s 
        for r, c in enumerate(s):
            #update character count for window
            window[c] = window.get(c, 0) + 1
            #Check if character is in t and counts in maps are equal
            if c in countT and window[c] == countT[c]:
                have += 1
            #while have is equal to need
            while have == need:
                #update result 
                if (r-l+1) < resLen:
                    res, resLen = [l, r], r - l + 1
                #pop from the left of our window
                window[s[l]] -= 1
                #check if removing character decreased have
                if s[l] in countT and window[s[l]] < countT[s[l]]:
                    have -= 1
                l += 1
        l, r = res
        return s[l:r+1] if resLen != float("infinity") else ""



        