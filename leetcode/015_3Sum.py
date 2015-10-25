# -*- coding: utf-8 -*-
"""
Created on Sun Sep  6 11:22:42 2015

@author: norrix
"""

class Solution(object):
    def threeSum(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        res = []
        nums.sort()
        for i in range(len(nums)-2):
            if i > 0 and nums[i] == nums[i-1]:
                continue
            left, right = i+1, len(nums)-1
            while left < right:
                a = nums[i] + nums[left] + nums[right]
                if a < 0:
                    left +=1 
                elif a > 0:
                    right -= 1
                else:
                    res.append([nums[i], nums[left], nums[right]])
                    while left < right and nums[left] == nums[left+1]:
                        left += 1
                    while left < right and nums[right] == nums[right-1]:
                        right -= 1
                    left += 1
                    right -= 1
        return res
                
"""
s = Solution()
print(s.threeSum([-1, 0, 1, 2, -1, -4]))
"""