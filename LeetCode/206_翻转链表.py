# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def reverseList(self, head: ListNode) -> ListNode:
        new_head = None

        while head:
            tmp = head.next  # 用临时变量记录指针
            head.next = new_head  # new_head指向新的值
            new_head = head
            head = tmp

        return new_head
