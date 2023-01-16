class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def deleteDuplicates(self, head):
        total = list()
        dup = set()

        node = head
        while node is not None:
            if node.val in total:
                dup.add(node.val)
            else:
                total.append(node.val)

            node = node.next

        new = None
        for v in reversed(total):
            if v not in dup:
                new = ListNode(v, new)

        return new
