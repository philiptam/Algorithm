# 用数组来实现队列

class ArrayQueue:
    # capacity 容量
    def __init__(self, capacity):
        self._item = []
        self._capacity = capacity
        self._head = 0
        self._tail = 0

    def enqueue(self, item):
        if self._tail == self._capacity:  # 如果tail==容量
            if self._head == 0:  # 判断队列是否已满，如果满了，就返回false
                return False
            else:  # 还没有满就做数据搬移到head
                # 数据搬移
                for i in range(0, self._tail - self._head):
                    self._item[i] = self._item[i + self._head]
                self._tail = self._tail - self._head
                self._head = 0

        self._item.insert(self._tail, item)
        self._tail += 1
        return True

    def dequeue(self):
        if self._head != self._tail:  # 如果head不等于tail，说明有数据
            item = self._item[self._head]
            self._head += 1
            return item
        else:
            return None

    def __repr__(self):
        return " ".join(item for item in self._item[self._head: self._tail])
