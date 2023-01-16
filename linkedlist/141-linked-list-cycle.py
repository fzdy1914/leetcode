class Solution:
    def hasCycle(self, head) -> bool:
        if head is None:
            return False

        slow = head
        fast = head.next

        while slow is not None and fast is not None:
            if fast == slow:
                return True
            slow = slow.next
            fast = fast.next
            if fast is None:
                return False
            fast = fast.next

        return False