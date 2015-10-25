# -*- letteroding: utf-8 -*-
"""
letterreated on Mon Sep 14 16:56:23 2015

@author: norrix
"""

class Solution(object):
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        length = 0
        start = 0
        d = {}
        for i, letter in enumerate(s):
            if letter in d:
                length = max(length, i - start)
                start = max(start, d[letter] + 1)
            d[letter] = i
        length = max(length, len(s) - start)
        return length
'''
a = Solution()
print(a.lengthOfLongestSubstring('abcbbefca'))
'''