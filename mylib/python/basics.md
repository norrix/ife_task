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
## datetime
timestamp
```
from datetime import datetime
datetime.fromtimestamp(1445680365.0) # 2015-10-24 17:52:45 (本地时间)
datetime.utcfromtimestamp(1429417200.0)
datetime(2015, 10, 24, 17, 52, 45).timestamp() # 1445680365.0
```

timezone
```
from datetime import datetime, timedelta, timezone
tz_utc_5 = timezone(timedelta(hours = 5))
dt = dt.replace(tzinfo = tz_utc_5) # add timezone info

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


logging
```python
import logging
logging.basicConfig(level = logging.INFO) # DEBUG, INFO, WARNING, ERROR
try:
    logging.info('run fun')
    fun()
except Exception as e:
    logging.exception(e) # 继续执行，并正常退出

```
-----
## re/filter

```python
"".join([a for a in s if a.isalpha()]) # find 'CU' from 'CU1505'

import re
pattern = re.compile('^[A-Z]+') # 预编译
match = pattern.search('CU1505.SHF')
match.group()

re.split(r'\s+', 'a   b     c') # ['a', 'b', 'c']

m = re.match(r'^(\d{3})-(\d{3,8})$', '010-12345678')
m.group(0) # '010-12345678'
m.group(1) # '010'
m.group(2) # '12345678'
```

-----
## base64
```
import base64
base64.b64encode(b'string') # b'c3RyaW5n'
base64.b64encode(b'string\x00') # b'c3RyaW5nAA=='
base64.b64decode(b'c3RyaW5nAA==') # b'string\x00'
# base64编码总是4的倍数，有时候encode可以把等号去掉，decode时再加上
```

-----
## hashlib
```
import hashlib
md5 = hashlim.md5() # or sha1 = hashlib.sha1()
md5.update('how to use md5 in '.encode('utf-8'))
md5.update('your python'.encode('utf-8'))
print(md5.hexdigest())
# md5 128bit = 32位16进制数
# sha1 160bit = 40位16进制数
```

-----
## itertools
```
import itertools
natural = itertools.count(1)
abcs = itertools.cycle('ABC')
limited_natural = itertools.takewhile(lambda x: x <= 10, natural)
chains = itertools.chain('ABC', 'XYZ')
```
-----
## HTMLParser
```
from html.parser import HTMLParser
from html.entities import name2codepoint
class MyHTMLParser(HTMLParser):
    def handle_starttag(self, tag, attrs):
        print('<%s>' % tag)

    def handle_endtag(self, tag):
        print('</%s>' % tag)

    def handle_startendtag(self, tag, attrs):
        print('<%s/>' % tag)

    def handle_data(self, data):
        print(data)

    def handle_comment(self, data):
        print('<!--', data, '-->')

    def handle_entityref(self, name):
        print('&%s;' % name)

    def handle_charref(self, name):
        print('&#%s;' % name)
parser = MyHTMLParser()
parser.feed("<html>
<head></head>
<body>
<!-- test html parser -->
    <p>Some <a href=\"#\">html</a> HTML&nbsp;tutorial...<br>END</p>
</body></html>")
```

-----
## urllib
```
from urllib import request
with request.urlopen('https://api.douban.com/v2/book/2129650') as f:
    data = f.read()
    print('Status:', f.status, f.reason)
    for k, v in f.getheaders():
        print('%s: %s' % (k, v))
    print('Data:', data.decode('utf-8'))