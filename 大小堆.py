from typing import Optional


class MedianFinder:

    def __init__(self):
        self.big_queue = []
        self.small_queue = []

    def addNum(self, num: int) -> None:
        if len(self.big_queue) == 0:
            self.big_queue.append(num)
            return
        if len(self.big_queue) == len(self.small_queue):
            if num < self.big_queue[-1]:
                self.big_queue.append(num)
            else:
                self.small_queue.append(num)
        elif len(self.big_queue) > len(self.small_queue):
            if num > self.big_queue[-1]:
                self.small_queue.append(num)
            else:
                self.small_queue.append(self.big_queue[-1])
                self.big_queue.pop()
                self.big_queue.append(num)
        elif len(self.big_queue) < len(self.small_queue):
            if num < self.small_queue[-1]:
                self.big_queue.append(num)
            else:
                self.big_queue.append(self.small_queue[-1])
                self.small_queue.pop()
                self.small_queue.append(num)

    def findMedian(self) -> float:
        pass

    def look(self) -> None:
        print(self.small_queue)
        print(self.big_queue)


if __name__ == "__main__":
    m = MedianFinder()
    m.addNum(6)
    m.addNum(3)
    m.addNum(8)
    m.addNum(2)
    m.addNum(1)
    m.addNum(4)
    m.addNum(7)
    m.look()