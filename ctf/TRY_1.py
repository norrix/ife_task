# -*- coding: utf-8 -*-

import urllib
import urllib.request as urllib2
import re

def myaddr(passwd, result):
    site = 'http://md5.my-addr.com/md5_decrypt-md5_cracker_online/md5_decoder_tool.php'
    para = urllib.parse.urlencode({'md5':passwd})
    para = para.encode('utf-8')
    req = urllib2.Request(site)
    try:
        fd = urllib2.urlopen(req, para)
        data = fd.read()
        data = data.decode('utf-8')
        match = re.search('(Hashed string</span>: )(\w+.\w+)', data)
        if match:
            print('[-] site: %s\t\t\tPassword: %s' % (site, match.group(2)))
            result.append(match.group(2))
        else:
            print('[-] site: %s\t\t\tPassword: Not found' % site)
    except urllib2.URLError:
        print('[+] site: %s \t\t\t[+] Error: seems to be down' % site)

if __name__ == "__main__":
    modifiedPasswd = 'cca9cc444e64c8116a30la00559c042b4'
    result = []
    for i in range(len(modifiedPasswd)):
        passwd = modifiedPasswd[:i] + modifiedPasswd[i+1:]
        print('\nTry %s' % passwd)
        myaddr(passwd, result)
    print('\nResult: %s' % result)