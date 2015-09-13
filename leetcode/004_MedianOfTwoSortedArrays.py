# -*- coding: utf-8 -*-
"""
Created on Sun Sep 13 09:58:56 2015

@author: norrix
"""

class Solution(object):
    def findMedianSortedArrays(self, A, B):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: float
        """
        l = len(A) + len(B)
        if l % 2 == 1:
            return self.findKth(A, B, l//2)
        else:
            return (self.findKth(A, B, l//2-1) + self.findKth(A, B, l//2))/2.0


    def findKth(self, A, B, k): # k = index
        if len(A) > len(B):
            A, B = B, A
        if not A:
            return B[k]
        if k == len(A) + len(B) - 1: # the last number
            return max(A[-1], B[-1])
        i = len(A)//2
        j = k-i
        if A[i] > B[j]:
            return self.findKth(A[:i], B[j:], i) # j numbers dropped, find i-th
        else:
            return self.findKth(A[i:], B[:j], j)

'''
nums1 = [3 ,4, 5]
nums2 = [2, 3, 4, 5]
a = Solution()
# print(a.findKth(nums1, nums2, 2))
print(a.findMedianSortedArrays(nums1, nums2))
'''