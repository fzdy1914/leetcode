from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        """
        Do not return anything, modify head in-place instead.
        """

        if head is None:
            return head
        slow = head
        fast = head.next
        while fast is not None and fast.next is not None:
            slow = slow.next
            fast = fast.next.next

        following = slow.next
        slow.next = None

        reverse = None
        while following is not None:
            t = following.next
            following.next = reverse
            reverse = following
            following = t

        dummy_new = ListNode(0, None)
        while head is not None and reverse is not None:
            dummy_new.next = head
            dummy_new = dummy_new.next

            head = head.next

            dummy_new.next = reverse
            dummy_new = dummy_new.next

            reverse = reverse.next

        if head is not None:
            dummy_new.next = head

        return dummy_new.next
