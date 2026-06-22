# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:    
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        def merge(list1,list2):
            if not list1:
                return list2
            if not list2:
                return list1
            dummy=ListNode()
            new=dummy
            if list1.val>=list2.val:
                new.next=list2
                list2=list2.next
            else:
                new.next=list1
                list1=list1.next
            new=new.next
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
            return dummy.next
        if not lists:
            return None
        k=len(lists)
        result=lists[0]
        for i in range(1,k):
            result=merge(result, lists[i])
        return result
            
