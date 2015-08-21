# MySQL

------
## JOIN
在使用了Where后再Join时，注意在同一个查询语句中不能同时用Where和Join，需要重生成表并重命名
```SQL
SELECT Close, Time FROM prices WHERE Symbol = 'RB1505.SHF' -- correct

SELECT Close, Time FROM prices WHERE Symbol = 'RB1505.SHF' JOIN
SELECT Close, Time t FROM prices WHERE Symbol = 'RB1510.SHF' ON Time = t -- error

SELECT * FROM (SELECT Close, Time FROM prices WHERE Symbol = 'RB1505.SHF') a JOIN
 (SELECT Close, Time FROM prices WHERE Symbol = 'RB1510.SHF') b on a.Time = b.Time -- correct

```
-----
## Others
```SQL
DATE_FORMAT('%s','%Y-%m-%d')
TRUNCATE TABLE a.b
```
