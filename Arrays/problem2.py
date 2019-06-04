# Problem-2: Add Two Numbers
# Link - https://leetcode.com/problems/add-two-numbers/

# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def addTwoNumbers(self, l1, l2, c=0):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        total = l1.val + l2.val + c
        c = total//10
        l3 = ListNode(total%10)
        
        if l1.next!=None or l2.next!=None or c!=0:
            if l1.next == None:
                l1.next = ListNode(0)
            if l2.next == None:
                l2.next = ListNode(0)
            l3.next = self.addTwoNumbers(l1.next,l2.next,c)
        return l3