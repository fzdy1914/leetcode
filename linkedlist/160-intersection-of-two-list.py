from typing import Optional


class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> Optional[ListNode]:
        # Align the length
        lenA = 0
        nodeA = headA
        while nodeA != None:
            lenA += 1
            nodeA = nodeA.next

        lenB = 0
        nodeB = headB
        while nodeB != None:
            lenB += 1
            nodeB = nodeB.next

        while lenA > lenB:
            headA = headA.next
            lenA -= 1

        while lenB > lenA:
            headB = headB.next
            lenB -= 1

        while headA is not None:
            if headA == headB:
                return headA

            headA = headA.next
            headB = headB.next

        return None