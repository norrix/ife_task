#!/usr/bin/env python
# -*- coding: utf-8 -*-
# A Rail-Fence decipher
def decipher(passwd):
    pwlen = len(passwd)
    field = [i for i in range(2, pwlen) if pwlen % i == 0]
    for f in field:
        flen = pwlen // f
        res = ''.join([passwd[f*j+i] for i in range(f) for j in range(flen)])
        print('field = %d, result = %s' % (f, res))
passwd = 'tn c0afsiwal kes,hwit1r  g,npt  ttessfu}ua u  hmqik e {m,  n huiouosarwCniibecesnren.'
decipher(passwd)