class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        anagrams = defaultdict(list)
        for s in strs:
            count = [0]*26
            for i in range(len(s)):
                count[ord(s[i]) - ord('a')] += 1
            anagrams[tuple(count)].append(s)
        
        output = []
        for key in anagrams:
            output.append(anagrams[key])
        return output