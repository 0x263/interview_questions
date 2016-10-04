"""
Write two functions:
    * addNum(): adds a number to the current set of numbers. 
    * findMedian(): finds the median of the current set of numbers.
        ** For an even number of elements in the current set,
            median is defined as the average of the two middle-most elements.
"""

from heapq import heappush, heappop

class MedianFinder:
    def __init__(self):
        self.smaller_heap = []
        self.larger_heap = []

    def addNum(self, num):
        median = self.findMedian()
        if num > median:
            heappush(self.larger_heap, num)
        elif num < median:
            heappush(self.smaller_heap, -num)
        else:
            if len(self.smaller_heap) < len(self.larger_heap):
                heappush(self.smaller_heap, -num)
            else:
                heappush(self.larger_heap, num)
            return # don't need to balance heaps
            
        diff = len(self.smaller_heap) - len(self.larger_heap)
        if abs(diff) < 2:
            return
        more_elements = self.smaller_heap if diff > 1 else self.larger_heap
        less_elements = self.larger_heap if diff > 1 else self.smaller_heap
        transfer = -heappop(more_elements)
        heappush(less_elements, transfer)


    def findMedian(self):
        if len(self.smaller_heap) > len(self.larger_heap):
            return -self.smaller_heap[0]
        elif len(self.larger_heap) > len(self.smaller_heap):
            return self.larger_heap[0]
        elif len(self.smaller_heap) == 0 and len(self.larger_heap) == 0:
            return 0
        else:
            return (float(-self.smaller_heap[0]) + float(self.larger_heap[0])) / 2.0


if __name__ == '__main__':
    test1 = [4, 2, 9, 7, 5]
    test2 = [5, 5, 5, 100, 10000, 13]

    finder = MedianFinder()
    for t in test1:
        print("addNum({})".format(t))
        finder.addNum(t)
        print("findMedian(): {}".format(finder.findMedian()))
