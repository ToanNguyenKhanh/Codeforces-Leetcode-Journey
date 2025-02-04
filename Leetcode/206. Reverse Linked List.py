# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        pre = ne = None
        while head:
            ne = pre
            pre = head
            head = head.next
            pre.next = ne
        return pre

