# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        if not p and not q:
            return True
        if not p or not q or p.val != q.val:
            return False
        return self.isSameTree(p.left, q.left) and self.isSameTree(p.right, q.right)


"""
Very simple problem. if both nodes are null then return true
if one node is null and the other isn't then return False
otherwise recursively check the left of the left tree against the left of the right tree
and do the same for the right subtree of each respective tree and then return that 
"""
