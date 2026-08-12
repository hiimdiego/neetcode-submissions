class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        #Create an array that stores the frequency of each value
        freq = [[] for i in range(len(nums) + 1)]
        #Create map to find frequency of each number
        count = {}
        for num in nums:
            count[num] = count.get(num, 0) + 1
        #Iterate through map and store frequencies in count array
        for key, value in count.items():
            freq[value].append(key)

        output = []
        #Iterate backwards through count array to find most frequent elements
        for i in range(len(freq) - 1, 0, -1):
            for num in freq[i]:
                output.append(num)
                if len(output) == k:
                    return output
            
