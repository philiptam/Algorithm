class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

def print_obj(head):
    nums = []
    current = head
    while current:
        nums.append(current.val)
        current = current.next
    return "->".join(str(num) for num in nums)

node1 = ListNode(1)
node1.next = ListNode(4)
node1.next.next = ListNode(3)

less_head = ListNode(0)
print(print_obj(less_head))
less_ptr = less_head
less_ptr.next = node1
less_ptr = node1
print(print_obj(node1))
print(print_obj(less_ptr))
print(print_obj(less_head))


