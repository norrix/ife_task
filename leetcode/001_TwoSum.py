# -*- coding: utf-8 -*-
"""
Created on Sun Sep  6 10:59:51 2015

@author: norrix
"""


class Solution:
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        reindex = {}
        for i, a in enumerate(nums):
            if target-a in reindex:
                return [reindex[target-a], i+1]
            else:
                reindex[a] = i+1
                
"""
s = Solution()
print(s.twoSum([2, 7, 11, 15], 9))
"""