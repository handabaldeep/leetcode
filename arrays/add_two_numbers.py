# Link - https://leetcode.com/problems/add-two-numbers/
from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode], c: int=0) -> Optional[ListNode]:
        pos_total = l1.val + l2.val + c
        c = pos_total // 10
        l3 = ListNode(pos_total % 10)

        if l1.next or l2.next or c:
            if not l1.next:
                l1.next = ListNode(0)
            if not l2.next:
                l2.next = ListNode(0)
            l3.next = self.addTwoNumbers(l1.next, l2.next, c)
        
        return l3
