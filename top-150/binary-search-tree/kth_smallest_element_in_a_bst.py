class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        elems = []

        def traverse_rec(root):
            if root is not None:
                traverse_rec(root.left)
                elems.append(root.val)
                traverse_rec(root.right)

        traverse_rec(root)
        return elems[k - 1]


"""
DFS utilizes the fact that the in-order traversal of a binary tree is sorted
can make this solution faster by iterating with a stack. 
"""

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:        
        def trav_rec(root, stack):
            if not root:
                return stack

            trav_rec(root.left, stack)
            stack.append(root.val)
            trav_rec(root.right, stack)
            return stack

        stack = trav_rec(root, [])
        return stack[k - 1]
