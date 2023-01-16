class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def reverseBetween(self, head, left: int, right: int):
        idx = 1
        new = None

        h = head
        while head is not None:
            if idx == left - 1:
                keep_left = head
            if idx > left - 1:
                new = ListNode(head.val, new)
                if idx == left:
                    keep_middle = new
            if idx == right:
                keep_right = head.next
                break

            head = head.next
            idx += 1

        if left != 1:
            keep_left.next = new
        else:
            h = new

        keep_middle.next = keep_right
        return h
