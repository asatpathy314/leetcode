# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(
        self, l1: Optional[ListNode], l2: Optional[ListNode]
    ) -> Optional[ListNode]:
        head_value = (l1.val + l2.val) % 10
        remainder = (l1.val + l2.val) // 10
        head = ListNode(val=head_value)
        i = head
        l1 = l1.next
        l2 = l2.next

        while True:
            if l1 and l2:
                next_val = (l1.val + l2.val + remainder) % 10
                next_node = ListNode(val=next_val)
                remainder = (l1.val + l2.val + remainder) // 10
                l1 = l1.next
                l2 = l2.next
                i.next = next_node
                i = next_node
            elif l1:
                next_val = (l1.val + remainder) % 10
                next_node = ListNode(val=next_val)
                remainder = (l1.val + remainder) // 10
                l1 = l1.next
                i.next = next_node
                i = next_node
            elif l2:
                next_val = (l2.val + remainder) % 10
                next_node = ListNode(val=next_val)
                remainder = (l2.val + remainder) // 10
                l2 = l2.next
                i.next = next_node
                i = next_node
            else:
                break
        if remainder:
            i.next = ListNode(val=remainder)
        return head
