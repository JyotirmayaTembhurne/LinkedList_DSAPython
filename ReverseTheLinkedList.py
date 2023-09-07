# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head:
            return head
        else:
            arr = list()
            curr = head
            while curr:
                arr.append(curr.val)
                curr = curr.next               
            curr = head
            arr = arr[-1::-1]
            length = len(arr)
            i = 0
            while i<len(arr):
                curr.val = arr[i]
                curr = curr.next
                i+=1
            curr = head
            return curr
            
            
            
                
        
