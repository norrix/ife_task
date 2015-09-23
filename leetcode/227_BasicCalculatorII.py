class Solution:
    def infix2postfix(self, s):
        """
        :type tokens: string
        :rtype: List[str]
        """
        num = ''
        opers = []
        tokens = []
        priority = {'':0, '+':1, '-':1, '*':2, '/':2}
        for c in s:
            if c.isspace():
                continue
            if c.isdigit():
                num += c
            else:
                tokens.append(int(num))
                num = ''
            if c in ['+', '-', '*', '/']:
                if priority[c] > priority[opers[-1] if opers else '']:
                    opers.append(c)
                else:
                    while priority[c] <= priority[opers[-1] if opers else '']:
                        tokens.append(opers.pop())
                    opers.append(c)
        if num:
            tokens.append(int(num))
        while opers:
            tokens.append(opers.pop())
        return tokens

    def postfix2value(self, tokens):
        """
        :type tokens: List[str]
        :rtype: int
        """
        result = []
        for token in tokens:
            if token not in ['+', '-', '*', '/', '^']:
                result.append(token)
            else:
                b, a = result.pop(), result.pop()
                f = {'+':lambda a, b : a + b, \
                     '-':lambda a, b : a - b, \
                     '*':lambda a, b : a * b, \
                     '/':lambda a, b : a / b + 1 if a * b < 0 and a % b else a / b, \
                 }[token]
                result.append(f(a, b))
        return result.pop()

    def calculate(self, s):
        """
        :type s: str
        :rtype: float
        """
        tokens = self.infix2postfix(s)
        return self.postfix2value(tokens)


'''
s = Solution()
text = ' 3+5 / 2 '
print(s.calculate(text))
'''