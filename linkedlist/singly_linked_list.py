class Node:
    def __init__(self, data, next_node=None):
        # 链表结构的Node节点
        # 参数：data存储的数据
        # next：下一个节点的引用地址
        self.data = data
        self._next = next_node


class SinglyLinkedList:
    def __init__(self):
        # 单向列表初始化方法
        self._head = None

    def find_by_value(self, value):
        p = self._head  # p指针
        while p and p.data != value:  # 如果有p指针并且p指针指向的data里面的内容不等于value值的话就一直找下去，知道p为null为止
            p = p._next
        return p

    # 向head插入新Node
    def insert_node_to_head(self, new_node):
        if new_node:
            # 新节点的Next
            new_node._next = self._head  # 插入的新node指向上head的next的地址
            self._head = new_node  # head指向新node

    # 向head插入新value
    def insert_value_to_head(self, value):
        new_node = Node(value)  # 创建一个新node
        self.insert_node_to_head(new_node)  # 调用向head插入node


if __name__ == "__main__":
    l = SinglyLinkedList()
    l.insert_value_to_head(1)
    l.insert_value_to_head(5)
    node5 = l.find_by_value(5)
    print(node5.__dict__)
