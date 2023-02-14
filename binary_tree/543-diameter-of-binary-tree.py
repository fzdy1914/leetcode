from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        result = 0

        def traverse(node):
            # TODO: nonlocal
            nonlocal result
            if node is None:
                return 0

            l = traverse(node.left)
            r = traverse(node.right)

            result = max(result, l + r + 1)

            return max(l + 1, r + 1)

        traverse(root)

        return result - 1