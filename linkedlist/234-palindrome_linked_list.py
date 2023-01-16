class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def isPalindrome(self, head) -> bool:
        # TODO
        if head is None:
            return True
        slow = head
        fast = head.next
        while fast is not None and fast.next is not None:
            slow = slow.next
            fast = fast.next.next

        following = slow.next
        slow.next = None
        if fast is None:
            following = ListNode(slow.val, following)

        # TODO
        prev = None
        while following is not None:
            t = following.next
            following.next = prev
            prev = following
            following = t

        while head is not None:
            if head.val != prev.val:
                return False
            head = head.next
            prev = prev.next

        return True
