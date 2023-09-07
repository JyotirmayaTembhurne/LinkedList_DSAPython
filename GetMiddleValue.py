# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def middleNode(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head.next:
            return head
        else:
            curr = head
            length = 0
            while curr:
                length += 1
                curr = curr.next
            curr = head
            i = 0
            if length % 2 == 0:
                while i < (length / 2).__ceil__():
                    curr = curr.next
                    i += 1
            else:
                while i < (length / 2).__floor__():
                    curr = curr.next
                    i += 1
            return curr
