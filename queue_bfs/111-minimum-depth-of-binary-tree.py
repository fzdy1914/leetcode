from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def minDepth(self, root: Optional[TreeNode]) -> int:
        if root is None:
            return 0

        q = [(root, 1)]

        # TODO: shortest: 1. dp, 2. bfs
        while True:
            first = q.pop(0)
            if first[0].left is None and first[0].right is None:
                return first[1]

            if first[0].left is not None:
                q.append((first[0].left, first[1] + 1))

            if first[0].right is not None:
                q.append((first[0].right, first[1] + 1))