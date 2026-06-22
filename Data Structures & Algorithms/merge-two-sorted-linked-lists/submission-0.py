# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        new=ListNode()
        if not list1:
            return list2
        if not list2:
            return list1
        if list1.val>list2.val:
            new=list2
            list2=list2.next
        else:
            new=list1
            list1=list1.next
        cur=new
        while list1 and list2:
            if list1.val>=list2.val:
                new.next=list2
                list2=list2.next
            else:
                new.next=list1
                list1=list1.next
            new=new.next
        if list1:
            new.next=list1
        if list2:
            new.next=list2
        return cur