from typing import List


class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def distanceK(self, root: TreeNode, target: TreeNode, k: int) -> List[int]:
        def label_parent(node):
            if node.left is not None:
                node.left.parent = node
                label_parent(node.left)
            if node.right is not None:
                node.right.parent = node
                label_parent(node.right)

        label_parent(root)

        result = []

        def n_below(node, n):
            if n == 0:
                if node is not None:
                    result.append(node.val)
                return
            if node is None or n < 0:
                return

            if node.left is not None:
                n_below(node.left, n - 1)
            if node.right is not None:
                n_below(node.right, n - 1)

        n_below(target, k)

        cur = target
        n = k
        while hasattr(cur, "parent") and n > 0:
            p = cur.parent
            if n == 1:
                result.append(p.val)
                break

            sib = p.left
            if p.left == cur:
                sib = p.right

            n_below(sib, n - 2)
            n -= 1
            cur = p

        return result