# IDF实验室 CTF练习
======
## 小试牛刀
TRY_1 [被改错的密码](http://ctf.idf.cn/index.php?g=game&m=article&a=index&id=29)
TRY_2 [啥？](http://ctf.idf.cn/index.php?g=game&m=article&a=index&id=30)
TRY_3 [ASCII码而已](http://ctf.idf.cn/index.php?g=game&m=article&a=index&id=32)
TRY_4 [摩斯密码](http://ctf.idf.cn/index.php?g=game&m=article&a=index&id=33)
TRY_5 [聪明的小羊](http://ctf.idf.cn/index.php?g=game&m=article&a=index&id=52)

## 密码
1. 古典密码 http://www.quipqiup.com/index.php

## 编码
1. ASCII为7或8的倍数
2. 平方数可能为二维码
3. 0-9a-zA-Z还有等号为base64

## 隐写
1. jpg结尾为“FF D9”，如果不是可能有隐写
2. Stegsolve -> Frame Browser 通道最低有效位隐写
3. Namo_GIF_gr 动态GIF编辑
4. exif 信息隐藏
5. zlib开头为“78 9C”