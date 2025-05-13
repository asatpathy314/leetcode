# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right


class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        def find_rec(root, max_value, good_count):
            if root is None:
                return good_count

            if max_value <= root.val:
                good_count += 1

            good_count += find_rec(root.left, max(max_value, root.val), 0)
            good_count += find_rec(root.right, max(max_value, root.val), 0)
            return good_count

        return 1 + find_rec(root.left, root.val, 0) + find_rec(root.right, root.val, 0)
