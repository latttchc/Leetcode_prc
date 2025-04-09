# LeetCode 21. Merge Two Sorted Lists
# https://leetcode.com/problems/merge-two-sorted-lists/

# Definition for singly-linked list.
from typing import Optional

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        # ダミーノードを作成
        dummy = ListNode()
        current = dummy

        # list1とlist2の要素を比較しながらマージ
        while list1 and list2:
            if list1.val < list2.val:
                current.next = list1
                list1 = list1.next
            else:
                current.next = list2
                list2 = list2.next
            current = current.next

        # 残っているノードを追加
        if list1:
            current.next = list1
        elif list2:
            current.next = list2

        return dummy.next