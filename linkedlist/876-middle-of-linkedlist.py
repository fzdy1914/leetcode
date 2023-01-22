from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def middleNode(self, head: Optional[ListNode]) -> Optional[ListNode]:
        dummy = ListNode(0, head)
        # TODO: fast and slow
        slow = dummy
        fast = dummy

        while fast.next is not None and fast.next.next is not None:
            slow = slow.next
            fast = fast.next.next

        slow = slow.next
        return slow