# -*- coding: utf-8 -*-
"""
Created on Sun Sep 11 11:21:42 2015

@author: norrix
"""

class Solution(object):
    def evalRPN(self, tokens):
        """
        :type tokens: List[str]
        :rtype: int
        """
        result = []
        for i in range(len(tokens)):
            token = tokens[i]
            if token not in ['+', '-', '*', '/']:
                result.append(int(token))
            else:
                b, a = result.pop(), result.pop()
                f = {'+':lambda a, b : a + b, \
                     '-':lambda a, b : a - b, \
                     '*':lambda a, b : a * b, \
                     '/':lambda a, b : (a / b + 1 if a * b < 0 and a % b != 0 else a / b)
                 }[token]
                result.append(f(a, b))
        return result.pop()
        

'''
s = Solution()
print(s.evalRPN(["10","6","9","3","+","-11","*","/","*","17","+","5","+"]))
'''