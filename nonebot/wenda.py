# -*- coding:utf-8 -*-
import os
import re
import json
root = os.path.join(os.path.dirname(__file__), 'wenda_dictionary.json')
a = dict()

def savedir(msg):
    global a
    with open(root,'w',encoding='utf-8') as file:
        json.dump(msg, file, ensure_ascii=False)
    return '已保存~'

def readdir():
    global a
    try:
        with open(root,'r',encoding='utf-8') as file:
            a = json.load(file)
    except:
        savedir(a)
    return '已读取~'

def add(msg):
    global a
    p = '问(.*?)答(.+)'
    msg = re.findall(p,msg)[0]
    a[msg[0]] = msg[1]
    savedir(a)
    return '好的，记住了~'

def delet(msg):
    global a
    msg = re.findall('词条(.+)',msg)[0]
    try:
        del a[msg]
        savedir(a)
        return '已删除~'
    except:
        return '镜华不知道这个词哦~'

def reply(msg):
    global a
    for i in a:
        if i in msg:
            return a[i]

def keys(msg):
    global a
    return ', '.join(a.keys())
