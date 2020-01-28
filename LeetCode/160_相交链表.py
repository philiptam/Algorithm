# Definition for singly-linked list.
from typing import Optional
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> ListNode:
        lenA = self.getlen(headA)
        lenB = self.getlen(headB)
        if lenA > lenB:  # A链表比B链表长
            headA = self.move_link(lenA, lenB, headA)
        else:
            headB = self.move_link(lenA, lenB, headB)

        while headA and headB:
            if headA == headB:
                return headB
            headA = headA.next
            headB = headB.next
        return None

    def move_link(self, lenA: int, lenB: int, head: ListNode) -> ListNode:
        detal = abs(lenA - lenB)
        while head and detal:
            head = head.next
            detal -= 1
        return head

    def getlen(self, head: ListNode) -> int:
        length = 0
        while head:
            length += 1
            head = head.next
        return length