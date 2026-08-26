class MedianFinder:

    def __init__(self):
        #initialize heaps
        self.max_heap, self.min_heap = [], []

    def addNum(self, num: int) -> None:
        if not self.min_heap:
            heapq.heappush(self.min_heap, num) #check if heap is initialized
        else:
            if num > self.min_heap[0]: #push to min_heap if greater than min of min_heap
                heapq.heappush(self.min_heap, num)
            else:
                heapq.heappush(self.max_heap, -num)

            if len(self.min_heap) > len(self.max_heap) + 1:
                val = heapq.heappop(self.min_heap)
                heapq.heappush(self.max_heap, -val)
            elif len(self.max_heap) > len(self.min_heap) + 1:
                val = -heapq.heappop(self.max_heap)
                heapq.heappush(self.min_heap, val)

    def findMedian(self) -> float:
        if len(self.min_heap) > len(self.max_heap):
            return self.min_heap[0]
        elif len(self.max_heap) > len(self.min_heap):
            return -self.max_heap[0]
        return (-self.max_heap[0] + self.min_heap[0]) / 2
        