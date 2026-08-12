class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        hash_map = {}
        for i, word in enumerate(strs):
            sorted_word = "".join(sorted(word))
            if sorted_word in hash_map:
                hash_map[sorted_word].append(word)
            else:
                hash_map[sorted_word] = [word]
        
        output = []
        for key in hash_map:
            output.append(hash_map[key])

        return output