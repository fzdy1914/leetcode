class Solution:
    def deleteDuplicates(self, head):
        seen = set()
        if head is None:
            return head

        h = head
        while head.next is not None:
            seen.add(head.val)

            while head.next.val in seen:
                if head.next.next is None:
                    head.next = None
                    break

                head.next = head.next.next

            if head.next is None:
                break
            head = head.next
        return h
