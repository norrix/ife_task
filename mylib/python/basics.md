# Basics

-----
## Number
NaN, Inf
```python
float('nan') == float('nan') # False
float('Inf') == float('Inf') # True
math.isnan(float('nan')) # True
```
-----
## String
encode, decode
```python
u'hello'.encode('utf-8') == b'hello' # python3
u'hello'.encode('utf-8') == 'hello' # python2


'Hello World'[::-1]
'Hello World'.split(' ')[::-1]

```

-----
## File I/O
exception
```python
f = open('update.log','a')
try:
    fun()
except Exception:
    import traceback
    traceback.print_exc(file = f)
finally:
    f.close()
```

-----
## re/filter

```python
"".join([a for a in s if a.isalpha()]) # find 'CU' from 'CU1505'

import re
pattern = re.compile('^[A-Z]+') # find 'CU' from 'CU1505.SHF'
match = pattern.search(s)
match.group()
```
