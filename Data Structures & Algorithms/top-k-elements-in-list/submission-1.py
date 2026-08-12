class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        #Create an array that stores the frequency of each value
        count = [[] for i in range(len(nums) + 1)]
        #Create map to find frequency of each number
        freq = {}
        for num in nums:
            freq[num] = freq.get(num, 0) + 1
        #Iterate through map and store frequencies in count array
        for key, value in (freq.items()):
            count[value].append(key)
        #Iterate backwards through count array to find most frequent elements
        output = []
        for i in range (len(count) - 1, 0, -1):
            for val in (count[i]):
                output.append(val)
                if len(output) == k:
                    return output
        return []
