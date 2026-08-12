class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        n, m = len(s1), len(s2)
        #base case
        if n > m:
            return False
        #create character counts for each string
        s1Count, s2Count = [0] * 26, [0] * 26
        #Iterate through first string and update character counts
        for i in range(n):
            s1Count[ord(s1[i]) - ord('a')] += 1
            s2Count[ord(s2[i]) - ord('a')] += 1
        matches = 0
        #iterate through both arrays and update matches 
        for i in range(26):
            matches += (1 if s1Count[i] == s2Count[i] else 0)
        #Iterate through remainder of second string
        l = 0
        for r in range(n, m):
            #Check match count
            if matches == 26: return True
            #find index
            idx = ord(s2[r]) - ord('a')
            s2Count[idx] += 1
            if s1Count[idx] == s2Count[idx]:
                matches += 1
            elif s1Count[idx] + 1 == s2Count[idx]:
                matches -= 1
            
            idx = ord(s2[l]) - ord('a')
            s2Count[idx] -= 1
            if s1Count[idx] == s2Count[idx]:
                matches += 1
            elif s1Count[idx] - 1 == s2Count[idx]:
                matches -= 1
            l += 1
        return matches == 26