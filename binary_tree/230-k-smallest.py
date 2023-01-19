from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        def count(node):
            if node is None:
                return 0
            # TODO: hasattr
            elif hasattr(node, "count"):
                return node.count
            else:
                node.count = count(node.left) + count(node.right) + 1
                return node.count

        count(root)

        def search(node, k):
            c = count(node.left)
            if c + 1 == k:
                return node.val
            if c + 1 > k:
                return search(node.left, k)
            else:
                return search(node.right, k - c - 1)

        return search(root, k)