from typing import Optional, List


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def pathSum(self, root: Optional[TreeNode], targetSum: int) -> List[List[int]]:
        result = []

        def backtrack(node, path, target):
            if node is None:
                return

            path.append(node.val)

            if node.left is None and node.right is None:
                if target == node.val:
                    result.append(path.copy())
                path.pop()
                return

            backtrack(node.left, path, target - node.val)
            backtrack(node.right, path, target - node.val)

            path.pop()

        backtrack(root, [], targetSum)

        return result