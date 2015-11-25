# bash

-----
### head
head -n1 file.txt
head -n1 file.txt | wc -w // wc = word count, -w = word num


### find & xargs
find . -type f -mtime +10 -exec rm {} \; // 查找10天以前的文件并删除
find . -name ".log" -exec mv {} /path \; // 查找日志文件并移动
rm `find /path -type f` // 参数列表过长，报错
find /path -type f -print0 | xargs -0 rm //以NULL而不是\n作为间隔符，避免带空格的文件

### seq
seq -f "dir%03g" 1 3 | xargs mkdir // dir001 dir002 dir003 （f格式）
seq -s ', ' 1 5 // 1, 2, 3, 4, 5 （s分隔符）

### cut
echo "a1:a2:a3:a4:a5" | cut -d : -f 2,4 // a2:a4 （d分隔符 f字段）
cut -d ' ' -f 1 file.txt

### awk
head -n 5 file.txt | awk -F ', ' '{print $1"\t"$7}' // 打印第一列和第七列 (F分隔符)
FNR    浏览文件的记录数
NF     浏览记录的域的个数

### expr & let //数学计算
expr 2 + 3
expr $a /* $b
let "a+=1"