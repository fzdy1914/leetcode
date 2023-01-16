from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def sortList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        def middle(node):
            slow = node
            fast = node.next
            while fast is not None and fast.next is not None:
                slow = slow.next
                fast = fast.next.next

            following = slow.next
            slow.next = None
            return following

        def merge_sort(node):
            if node is None:
                return None
            if node.next is None:
                return node
            mid = middle(node)

            left = merge_sort(node)
            right = merge_sort(mid)

            dummy_head = ListNode(0, None)
            h = dummy_head
            while left is not None and right is not None:
                if left.val < right.val:
                    dummy_head.next = left
                    dummy_head = dummy_head.next
                    left = left.next
                else:
                    dummy_head.next = right
                    dummy_head = dummy_head.next
                    right = right.next

            while left is not None:
                dummy_head.next = left
                dummy_head = dummy_head.next
                left = left.next

            while right is not None:
                dummy_head.next = right
                dummy_head = dummy_head.next
                right = right.next

            return h.next

        return merge_sort(head)
