# 用数组模拟栈
class ArrayStack:
    def __init__(self):
        self._array = []

    def push(self, value):
        self._array.append(value)  # append 在数组尾部最加元素

    def pop(self):
        return self._array.pop()  # pop 在数组尾部删除元素，并返回被删除的那个值

    def __repr__(self):
        return " ".join(f"{num}]" for num in self._array)


if __name__ == '__main__':
    stack = ArrayStack()
    stack.push(5)
    stack.push(7)
    stack.push(9)
    # stack.prine_code()

    print(stack)

    stack.pop()
    print(stack)
