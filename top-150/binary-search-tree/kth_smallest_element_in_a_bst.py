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
