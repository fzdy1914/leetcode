import random
from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:

    def __init__(self, head: Optional[ListNode]):
        self.head = head

    def getRandom(self) -> int:
        final = self.head.val

        cnt = 1
        node = self.head
        while node.next is not None:
            node = node.next
            cnt += 1

            if random.random() < 1 / cnt:
                final = node.val

        return final