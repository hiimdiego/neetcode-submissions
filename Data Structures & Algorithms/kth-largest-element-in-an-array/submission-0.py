class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        maxHeap = []
        heapq.heapify(maxHeap)
        for num in nums:
            heapq.heappush(maxHeap, -num)
        i = 0
        output = 0
        while i < k:
            output = heapq.heappop(maxHeap)
            i += 1
        return -output
        