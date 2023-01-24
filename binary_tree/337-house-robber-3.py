from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

        
class Solution:
    def rob(self, root: Optional[TreeNode]) -> int:
        def helper(node, status):
            if node is None:
                return 0

            if not hasattr(node, "not_rob"):
                left = helper(node.left, 1)
                right = helper(node.right, 1)
                node.not_rob = left + right

            if status == 0:
                return node.not_rob

            if status == 1:
                if not hasattr(node, "rob"):
                    left = helper(node.left, 0)
                    right = helper(node.right, 0)
                    node.rob = left + right + node.val
                return max(node.rob, node.not_rob)

        return helper(root, 1)