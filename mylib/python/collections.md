# Collections

-----
namedtuple

```
from collections import namedtuple
Point = namedtuple('Point', ['x', 'y'])
p = Point(1, 2)
p.x # 1
p.y # 2
isinstance(p, Point) # True
isinstance(p, tuple) # True
```

-----
deque

```
from collections import deque
q = deque(['a', 'b', 'c'])
q.append('x')
q.appendleft('y')
q # deque(['y', 'a', 'b', 'c', 'x'])
```

-----
defaultdict

```
from collections import defaultdict
dd = defaultdict(lambda: 'N/a')
dd['key1'] = 'abc'
dd['key1'] # abc
dd['key2'] # 'N/a'
```

-----
OrderedDict
```
from collections import OrderedDict
od = OrderedDict()
od['z'] = 1
od['y'] = 2
od['x'] = 3
list(od.keys()) # ['z', 'y', 'x'] # 按照插入顺序
```

-----
Counter
```
from collections import Counter
c = Counter()
for ch in 'programming':
    c[ch] = c[ch] + 1
c # Counter({'g': 2, 'm': 2, 'r': 2, 'a': 1, 'i': 1, 'o': 1, 'n': 1, 'p': 1})
```

