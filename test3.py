from typing import List

pushed = [1, 2, 3, 4, 5]
popped = [4, 5, 3, 2, 1]


class Solution:
    def validateStackSequences(self, pushed: List[int], popped: List[int]) -> bool:
        # 创建一个队列和一个栈
        queue_order = popped
        stack = []
        for i in range(len(pushed)):  # 遍历push的元素
            stack.append(pushed[i])  # 将每个元素放入栈中
            while len(stack) > 0 and stack[0] == queue_order[0]:
                stack.pop(0)
                queue_order.pop(0)
        if len(stack) > 0:
            return False

        return True


if __name__ == "__main__":
    s = Solution()
    result = s.validateStackSequences(pushed, popped)
    print(result)
