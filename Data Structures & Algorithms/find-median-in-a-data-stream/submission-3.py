class MedianFinder:

    def __init__(self):
        #initialize heaps
        self.minHeap, self.maxHeap = [], []

    def addNum(self, num: int) -> None:
        heapq.heappush(self.maxHeap, -num)
        heapq.heappush(self.minHeap, -heapq.heappop(self.maxHeap))
        if len(self.minHeap) > len(self.maxHeap):
            heapq.heappush(self.maxHeap, -heapq.heappop(self.minHeap))

    def findMedian(self) -> float:
        #check if maxHeap > minHeap
        if len(self.maxHeap) > len(self.minHeap):
            return -self.maxHeap[0]
        else:
            return (self.minHeap[0] + -self.maxHeap[0]) / 2

        