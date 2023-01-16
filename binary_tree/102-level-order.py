class Solution:
    def levelOrder(self, root):
        if root is None:
            return []

        to_check = []
        next_to_check = [root, ]
        results = []
        while len(next_to_check) > 0:
            to_check = next_to_check
            next_to_check = []

            result = []

            while len(to_check) > 0:
                r = to_check.pop(0)

                result.append(r.val)

                if r.left is not None:
                    next_to_check.append(r.left)

                if r.right is not None:
                    next_to_check.append(r.right)

            results.append(result)

        return results