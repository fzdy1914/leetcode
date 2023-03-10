from typing import Optional, List


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        stack = [root, ]

        result = []
        seen = set()
        while len(stack) > 0:
            cur = stack[-1]
            if cur is None:
                stack.pop()
                continue

            if cur not in seen:
                seen.add(cur)
                stack.append(cur.left)
                continue

            result.append(cur.val)
            stack.pop()
            stack.append(cur.right)
        return result
