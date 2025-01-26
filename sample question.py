class ListNode:
    def __init__(self, val):
        self.val = val
        self.next = None
        self.prev = None

node1 = ListNode(1)
node2 = ListNode(2)
node3 = ListNode(3)

node1.next = node2
node2.prev = node1
node2.next = node3
node3.prev = node2

def print_forward(node):
    current = node
    while current:
        print(current.val, end = '<->' if current.next else '\n' )
        current = current.next


def print_backward(node):
    current = node
    while current.next:
        current = current.next

    while current:
        print(current.val, end ='<->' if current.prev else '\n')
        current = current.prev

print("Forward:")
print_forward(node1)

print("Backward:")
print_backward(node1)
