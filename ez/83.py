# 83. Remove Duplicates from Sorted List
# Definition for singly-linked list.
from typing import Optional

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if(head == None):
            return None
        L = []
        s = set()
        list = head
        while(list):
            if(list.val not in s):
                L.append(list.val)
                s.add(list.val)
            list = list.next
        toReturn = ListNode()
        dummy = toReturn
        for i in L:
            dummy.next = ListNode(i)
            dummy = dummy.next
        return toReturn.next
    
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
# class Solution:
#     def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
#         res = head

#         while head and head.next:
#             if head.val == head.next.val:
#                 head.next = head.next.next
#             else:
#                 head = head.next

        
#         return res