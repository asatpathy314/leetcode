# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSymmetric(self, root: Optional[TreeNode]) -> bool:
        if not root:
            return True
        
        def check_equal_recursive(left, right):
            if (not left or not right):
                if left != right:
                    return False
                return True

            if left.val != right.val:
                print(False, 2)
                return False
            
            if left and right:
                left_equal = check_equal_recursive(left.right, right.left)
                right_equal = check_equal_recursive(left.left, right.right)
                print(left_equal and right_equal)
                return left_equal and right_equal

            return True

        return check_equal_recursive(root.left, root.right)
