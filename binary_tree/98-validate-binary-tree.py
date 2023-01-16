class Solution:
    def isValidBST(self, root) -> bool:
        def helper(root, mini, maxi):
            if root is None:
                return True
            if root.val <= mini or root.val >= maxi:
                return False
            return helper(root.left, mini, root.val) and helper(root.right, root.val, maxi)

        return helper(root, float('-inf'), float('inf'))