class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        def find(root, i):
            if root is None:
                return None
            if root.val == i.val:
                return [root, ]
            l = find(root.left, i)
            if l is not None:
                l.insert(0, root)
                return l
            l = find(root.right, i)
            if l is not None:
                l.insert(0, root)
                return l
            return None

        l1 = find(root, p)
        l2 = find(root, q)

        for i in range(min(len(l1), len(l2))):
            if l1[i] != l2[i]:
                return l1[i-1]
        return l1[min(len(l1), len(l2)) - 1]
