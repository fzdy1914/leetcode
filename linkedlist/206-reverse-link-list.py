class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def reverseList(self, head):
        new = None

        while head is not None:
            new = ListNode(head.val, new)
            head = head.next

        return new
