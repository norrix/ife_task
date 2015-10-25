# -*- coding: utf-8 -*-
"""
Created on Sat Sep 12 10:44:31 2015

@author: norrix
"""

class Solution(object):
    def largestRectangleArea(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        height.append(0)
        LRA = 0
        stack = []
        for i in range(len(height)):
            while stack and height[stack[-1]] > height[i]:
                h = stack.pop()
                w = i - stack[-1] - 1 if stack else i
                LRA = max(LRA, height[h] * w)
                #print(height[h], w, stack, LRA)
            stack.append(i)
        return LRA

'''
s = Solution()
print(s.largestRectangleArea([2,1,1,1,1]))
'''