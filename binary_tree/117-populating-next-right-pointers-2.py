class Node:
    def __init__(self, val: int = 0, left: 'Node' = None, right: 'Node' = None, next: 'Node' = None):
        self.val = val
        self.left = left
        self.right = right
        self.next = next


class Solution:
    def connect(self, root: 'Node') -> 'Node':
        if root is None:
            return None

        q = [root]

        while len(q) > 0:
            cur_level = len(q)
            prev = None
            for i in range(cur_level):
                node = q.pop(0)
                if prev is not None:
                    prev.next = node
                prev = node

                if node.left is not None:
                    q.append(node.left)
                if node.right is not None:
                    q.append(node.right)

        return root
