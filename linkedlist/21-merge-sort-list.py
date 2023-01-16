class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def mergeTwoLists(self, list1, list2):
        new = None
        h = None
        while list1 is not None and list2 is not None:
            if list1.val < list2.val:
                if new is None:
                    new = ListNode(list1.val, None)
                    h = new
                else:
                    new.next = ListNode(list1.val, None)
                    new = new.next
                list1 = list1.next
            else:
                if new is None:
                    new = ListNode(list2.val, None)
                    h = new
                else:
                    new.next = ListNode(list2.val, None)
                    new = new.next
                list2 = list2.next

        while list1 is not None:
            if new is None:
                new = ListNode(list1.val, None)
                h = new
            else:
                new.next = ListNode(list1.val, None)
                new = new.next
            list1 = list1.next

        while list2 is not None:
            if new is None:
                new = ListNode(list2.val, None)
                h = new
            else:
                new.next = ListNode(list2.val, None)
                new = new.next
            list2 = list2.next
        return h