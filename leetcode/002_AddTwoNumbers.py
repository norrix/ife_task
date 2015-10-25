# -*- coding: utf-8 -*-
"""
Created on Sat Sep 12 23:06:00 2015

@author: norrix
"""


class ListNode(object):
    def __init__(self, val):
        self.val = val
        self.next = None


class Solution(object):
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        head = cur = ListNode(None)
        carry = 0
        while l1 or l2:
            if l1:
                carry += l1.val
                l1 = l1.next
            if l2:
                carry += l2.val
                l2 = l2.next
            
            cur.next = ListNode(carry % 10)
            cur = cur.next
            carry = carry // 10
        if carry:
            cur.next = ListNode(1)
        return head.next
        

l1 = ListNode(2)
l1.next = ListNode(4)
l1.next.next = ListNode(3)

l2 = ListNode(5)
l2.next = ListNode(6)
l2.next.next = ListNode(4)

a = Solution()
result = a.addTwoNumbers(l1, l2)
print(result.val, result.next.val, result.next.next.val)