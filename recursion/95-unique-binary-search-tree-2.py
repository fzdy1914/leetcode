from typing import List, Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def generateTrees(self, n: int) -> List[Optional[TreeNode]]:
        def generate(start, end):
            if start > end:
                return [None]
            if start == end:
                return [TreeNode(start, None, None)]

            rs = []

            for i in range(start, end + 1):
                left = generate(start, i - 1)
                right = generate(i + 1, end)

                for l in left:
                    for r in right:
                        rs.append(TreeNode(i, l, r))

            return rs

        return generate(1, n)
