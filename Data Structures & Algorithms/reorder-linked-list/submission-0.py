# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        slow, fast = head, head.next
        while fast and fast.next:
            slow=slow.next
            fast=fast.next.next
        second=slow.next
        slow.next=None
        first=head
        prev=None
        cur=second
        while cur:
            nxt=cur.next
            cur.next=prev
            prev=cur
            cur=nxt
        while prev:
            temp1=prev.next
            temp2=first.next
            first.next=prev
            prev.next=temp2
            first=temp2
            prev=temp1