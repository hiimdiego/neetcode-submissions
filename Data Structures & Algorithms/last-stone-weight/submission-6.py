class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        maxHeap = [-n for n in stones]
        heapq.heapify(maxHeap)
        
        while len(maxHeap) > 1:
            x = -heapq.heappop(maxHeap)
            y = -heapq.heappop(maxHeap)
            if x != y:
                heapq.heappush(maxHeap, -(x - y))

        return 0 if len(maxHeap) == 0 else -maxHeap[0]