class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        hash_map = {}
        for i in range(len(s)):
            hash_map[s[i]] = hash_map.get(s[i], 0) + 1
        
        for i in range(len(t)):
            hash_map[t[i]] = hash_map.get(t[i], 0) - 1

        for key in hash_map:
            if hash_map[key] != 0:
                return False
        
        return True