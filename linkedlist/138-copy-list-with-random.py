class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random


class Solution:
    # TODO
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        if head is None:
            return head

        node = head
        while node is not None:
            node.next = Node(node.val, node.next, node.random)
            node = node.next.next

        node = head.next
        while node is not None:
            if node.random is not None:
                node.random = node.random.next
            if node.next is None:
                break
            node = node.next.next

        new_head = head.next
        node = Node(0, head)
        while node is not None:
            node.next = node.next.next
            node = node.next
            if node.next is None:
                break

        return new_head
