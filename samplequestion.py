# Example 3: Given the head of a linked list and an integer k, return the 
# k th node from the end.

# For example, given the linked list that represents 1 -> 2 -> 3 -> 4 -> 5 and k = 2, 
# return the node with value 4, as it is the 2nd node from the end.

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def find_node(self, head: ListNode, k: int) -> ListNode:
        slow = fast = head

        # Move the 'fast' pointer 'k' steps ahead
        for _ in range(k):
            if fast is None:  # Check if 'k' is out of bounds of the list length
                return None
            fast = fast.next
        
        # Move both pointers until 'fast' reaches the end of the list
        while fast:
            slow = slow.next
            fast = fast.next
        
        # 'slow' will now point to the 'k'-th node from the end
        return slow

# Example Usage
if __name__ == "__main__":
    # Create a simple linked list: 1 -> 2 -> 3 -> 4 -> None
    node1 = ListNode(1)
    node2 = ListNode(2)
    node3 = ListNode(3)
    node4 = ListNode(4)
    node1.next = node2
    node2.next = node3
    node3.next = node4

    # Instantiate the solution object
    sol = Solution()
    
    # Example: Find the 2nd node from the end
    kth_node = sol.find_node(node1, 2)
    print(kth_node.val if kth_node else "No such node")  # Should print 3, the 2nd node from the end
