from heapq import heappush, heappop


class RunningMedian():

    def __init__(self):
        self.small = []
        self.big = []

    def median(self):
        if len(self.small) == len(self.big) == 0:
            return None

        med = None

        if len(self.small) > len(self.big):
            med = -self.small[0]
        elif len(self.small) < len(self.big):
            med = self.big[0]
        else:
            med = (self.big[0] - self.small[0]) / 2.0

        return med

    def add_num(self, number):
        median = self.median()

        if not median:
            heappush(self.big, number)
            return number

        if number < median:
            heappush(self.small, -number)
        else:
            heappush(self.big, number)

        if abs(len(self.small) - len(self.big)) > 1:
            if len(self.small) > len(self.big):
                item = -heappop(self.small)
                heappush(self.big, item)
            else:
                item = heappop(self.big)
                heappush(self.small, -item)

if __name__ == '__main__':
    times = int(input())
    med = RunningMedian()

    for i in range(times):
        num = int(input())
        med.add_num(num)
        print(med.median())
