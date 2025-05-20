# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeTwoLists(
        self, list1: Optional[ListNode], list2: Optional[ListNode]
    ) -> Optional[ListNode]:
        if list1 is None and list2 is None:
            return None
        elif list1 is None:
            return list2
        elif list2 is None:
            return list1

        head = None
        iterator = None
        while list1 and list2:
            next_value = list1.val if list1.val < list2.val else list2.val
            next_node = ListNode(next_value)

            if head:
                iterator.next = next_node
                iterator = iterator.next
            else:
                head = next_node
                iterator = head

            if next_value == list1.val:
                list1 = list1.next
            else:
                list2 = list2.next

        if list1:
            iterator.next = list1

        if list2:
            iterator.next = list2

        return head
