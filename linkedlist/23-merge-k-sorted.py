import queue
from typing import List, Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

        
class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        q = queue.PriorityQueue()

        n = len(lists)
        if n == 0:
            return None

        for i in range(n):
            if lists[i] is not None:
                q.put([lists[i].val, i])
                lists[i] = lists[i].next

        dummy = ListNode(0, None)
        node = dummy

        while not q.empty():
            kv = q.get()
            node.next = ListNode(kv[0], None)
            node = node.next

            if lists[kv[1]] is not None:
                q.put([lists[kv[1]].val, kv[1]])
                lists[kv[1]] = lists[kv[1]].next

        return dummy.next