class Solution:
    def maxPathSum(self, root) -> int:
        def half_full_sum(root):
            if root.left is None and root.right is None:
                return root.val, root.val

            if root.left is None:
                rh, rf = half_full_sum(root.right)
                full = max(rf, root.val+rh, root.val, rh)
                half = max(root.val, rh + root.val)

                return half, full

            if root.right is None:
                lh, lf = half_full_sum(root.left)
                full = max(lf, root.val+lh, root.val, lh)
                half = max(root.val, lh + root.val)

                return half, full

            lh, lf = half_full_sum(root.left)
            rh, rf = half_full_sum(root.right)

            full = max(lf, rf, lh + root.val+rh, lh, rh)
            half = max(lh + root.val, root.val, rh + root.val)

            return half, full

        h, f = half_full_sum(root)
        return max(h, f)