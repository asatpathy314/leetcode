# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None


class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        if not head:
            return False

        seen = set()
        it = head

        while it.next:
            if it in seen:
                return True
            seen.add(it)
            it = it.next

        return False


"""
O(n) ish solution. Proper solution should use rabbit and hare algorithm. 
"""
