'''
python main.py 1 + 2 -3 + 4
'''
class CalcException:
    def __init__(self, message = "UNIDENTIFIED ERROR"):
        self.message = message
    def getMessage(self):
        return self.message
        

class Solution:
    def infix2postfix(self, s):
        """
        :type tokens: string
        :rtype: List[str/float]
        """
        num = ''
        opers = []
        tokens = []
        lastOper = None
        priority = {'':-1, '(':0, '+':1, '-':1, '*':2, '/':2, '^':3}
        for c in s:
            if c.isspace():
                continue
            if lastOper == 'num' and not (c.isdigit() or c == '.'):
                tokens.append(float(num))
                num = ''
            if c.isdigit() or c == '.':
                if c == '.' and ('.' in num or not len(num)):
                    return CalcException('FORMAT ERROR')
                num += c
                lastOper = 'num'
            elif c == '(':
                if lastOper == 'num':
                    return CalcException('FORMAT ERROR')
                opers.append(c)
                lastOper = 'lpar'
            elif c == ')':
                if lastOper == 'oper':
                    return CalcException('FORMAT ERROR')
                while(opers and opers[-1] != '('):
                    tokens.append(opers.pop())
                if not opers:
                    return CalcException('FORMAT ERROR')
                else:
                    opers.pop()
                lastOper = 'rpar'
            elif c in ['+', '-', '*', '/', '^']:
                if lastOper in ['oper', 'lpar', None]:
                    return CalcException('FORMAT ERROR')
                if priority[c] > priority[opers[-1] if opers else '']:
                    opers.append(c)
                else:
                    while priority[c] <= priority[opers[-1] if opers else '']:
                        tokens.append(opers.pop())
                    opers.append(c)
                lastOper = 'oper'
            else:
                return CalcException('INPUT ERROR')
        if not tokens:
            return CalcException('FORMAT ERROR')
        if num:
            tokens.append(float(num))
        while opers:
            tokens.append(opers.pop())
        return tokens
            
            
        
    def postfix2value(self, tokens):
        """
        :type tokens: List[str/float]
        :rtype: float
        """
        if isinstance(tokens, CalcException):
            return tokens
        result = []
        for token in tokens:
            if token not in ['+', '-', '*', '/', '^']:
                result.append(token)
            else:
                b, a = result.pop(), result.pop()
                f = {'+':lambda a, b : a + b, \
                     '-':lambda a, b : a - b, \
                     '*':lambda a, b : a * b, \
                     '/':lambda a, b : a / b, \
                     '^':lambda a, b : a ** b
                 }[token]
                if token == '/' and b == 0:
                    return CalcException('VALUE ERROR')
                if token == '^' and a == 0 and b == 0:
                    return CalcException('VALUE ERROR')
                result.append(f(a, b))
        return result.pop()

    def calculate(self, s):
        """
        :type s: str
        :rtype: float
        """
        tokens = self.infix2postfix(s)
        result = self.postfix2value(tokens)
        if isinstance(result, CalcException):
            print(result.getMessage())
        else:
            decimal = abs(int(result))
            decimalLen = 0 if not decimal else len(str(decimal))
            print(round(result, 10 - decimalLen) if result % 1 else int(result))


import sys
s = Solution()
text = ''.join(sys.argv[1:])
s.calculate(text)