class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def partition(self, head, x: int):
        def append(xx, y):
            if xx is None:
                return ListNode(y, None)
            else:
                xx.next = ListNode(y, None)
                return xx.next

        small = None
        big = None
        big_head = None
        while head is not None:
            if head.val < x:
                if small is None:
                    small = append(small, head.val)
                    small_head = small
                else:
                    small = append(small, head.val)
            else:
                if big is None:
                    big = append(big, head.val)
                    big_head = big
                else:
                    big = append(big, head.val)

            head = head.next

        if small is not None:
            small.next = big_head
            return small_head
        else:
            return big_head