class KthLargest:

    def __init__(self, k: int, nums: List[int]):
        #minHeap with K largest integers
        #initialize minHeap and k
        self.minHeap, self.k = nums, k
        #heapify minHeap
        heapq.heapify(self.minHeap)
        #pop from heap if length > k
        while len(self.minHeap) > k:
            heapq.heappop(self.minHeap)
    def add(self, val: int) -> int:
        #push
        heapq.heappush(self.minHeap, val)
        #check if minHeap has k elements
        if len(self.minHeap) > self.k:
            #pop
            heapq.heappop(self.minHeap)
        return self.minHeap[0]
        
        

