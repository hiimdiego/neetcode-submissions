class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        #Create a map of character count to a list of anagrams 
        freq = {}
        for s in strs:
            #Iterate through strings & create character count
            count = [0]*26
            for c in s:
                #Iterate through each character in each string
                count[ord(c) - ord('a')] += 1
            #Check if character count exists in hash_map, else add it
            if tuple(count) in freq:
                freq[tuple(count)].append(s)
            else:
                freq[tuple(count)] = [s]

        return list(freq.values())

        
