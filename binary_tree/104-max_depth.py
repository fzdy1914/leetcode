class Solution:
    def maxDepth(self, root) -> int:
        def depth(root):
            if root is None:
                return 0
            if root.left is None:
                if root.right is None:
                    return 1
                return 1 + depth(root.right)

            if root.right is None:
                return 1 + depth(root.left)

            return 1 + max(depth(root.left), depth(root.right))

        return depth(root)
