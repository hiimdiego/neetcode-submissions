class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        #Create a map of character count to a list of anagrams 
        hash_map = {}
        #Iterate through strings
        for s in strs:
        #Create character count for each string
            count = [0] * 26
            for char in s:
                count[ord(char) - ord('a')] += 1
            #Check if character count exists in hash_map, else add it
            if tuple(count) in hash_map:
                hash_map[tuple(count)].append(s)
            else:
                hash_map[tuple(count)] = [s]
        return list(hash_map.values())
        
