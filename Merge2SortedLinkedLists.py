# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeTwoLists(
        self, list1: Optional[ListNode], list2: Optional[ListNode]
    ) -> Optional[ListNode]:
        if not list1:
            return list2
        elif not list2:
            return list1
        else:
            current = list1
            arr = list()
            while current.next:
                current = current.next
            current.next = list2
            current = list1
            while current:
                arr.append(current.val)
                current = current.next
            arr.sort()
            current = list1
            for num in arr:
                current.val = num
                current = current.next
            current = list1
        return current
