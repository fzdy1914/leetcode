class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def detectCycle(self, head):
        if head is None:
            return None

        slow = head
        fast = head.next

        loop = []
        while slow is not None and fast is not None:
            if fast == slow:
                while slow not in loop:
                    loop.append(slow)
                    slow = slow.next
                while head not in loop:
                    head = head.next
                return head
            slow = slow.next
            fast = fast.next
            if fast is None:
                return None
            fast = fast.next

        return None