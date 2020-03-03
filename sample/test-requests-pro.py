#!/usr/bin/env python
# coding=utf-8
import requests

res = requests.get('https://httpbin.org/get', timeout=1)
print(res.status_code)

proxy = {
    'http': 'http://127.0.0.1:8001',
    'https': 'http://127.0.0.1:8001'
}
res = requests.get('https://httpbin.org/get', proxies=proxy)
print(res.text)

res = requests.get('https://www.csdn.net')
print(type(res.cookies), res.cookies)
for key, value in res.cookies.items():
    print(key + '=' + value)

headers = {
    'cookie': '_zap=5d7acb25-2f70-4599-82d5-3d634f5488d7; d_c0="AJBlXbEDJA-PTtLwxcT93wLfxOdWdp7jJMA=|1552894924"; __utma=51854390.507709168.1556006101.1556006101.1556006101.1; __utmv=51854390.000--|3=entry_date=20190418=1; __gads=ID=6db62c0ba32da440:T=1556541516:S=ALNI_MY1S3wLgWvJA-cnNr0VI1MNMzv4CQ; z_c0="2|1:0|10:1565836482|4:z_c0|92:Mi4xSXZ6b0RBQUFBQUFBa0dWZHNRTWtEeVlBQUFCZ0FsVk53aEpDWGdCam1aV2VMS21udjZDYzBKMm1JVFo5S2hxTXhR|7f5c56dd3d8ee608faf323a88e50b3e77f3dc4870bd4ba88a2aa9a2e4e298c2e"; _xsrf=MPixuOii3uIpXQFqGTij6NS4AXNqFFLi; q_c1=c7f86e3668184fef902314c3f912cbc4|1578898093000|1555570505000; Hm_lvt_98beee57fd2ef70ccdd5ca52b9740c49=1578898093,1578909193,1578987199,1579090237; Hm_lpvt_98beee57fd2ef70ccdd5ca52b9740c49=1579090237; KLBRSID=5430ad6ccb1a51f38ac194049bce5dfe|1579090340|1579090235',
    'user-agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_13_4) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/79.0.3945.117 Safari/537.36',
    'referer': 'https://www.zhihu.com'
}
res = requests.get('https://www.zhihu.com', headers=headers)
print(res.status_code)


# 构造RequestsCookieJar对象
cookies = '_zap=5d7acb25-2f70-4599-82d5-3d634f5488d7; d_c0="AJBlXbEDJA-PTtLwxcT93wLfxOdWdp7jJMA=|1552894924"; __utma=51854390.507709168.1556006101.1556006101.1556006101.1; __utmv=51854390.000--|3=entry_date=20190418=1; __gads=ID=6db62c0ba32da440:T=1556541516:S=ALNI_MY1S3wLgWvJA-cnNr0VI1MNMzv4CQ; z_c0="2|1:0|10:1565836482|4:z_c0|92:Mi4xSXZ6b0RBQUFBQUFBa0dWZHNRTWtEeVlBQUFCZ0FsVk53aEpDWGdCam1aV2VMS21udjZDYzBKMm1JVFo5S2hxTXhR|7f5c56dd3d8ee608faf323a88e50b3e77f3dc4870bd4ba88a2aa9a2e4e298c2e"; _xsrf=MPixuOii3uIpXQFqGTij6NS4AXNqFFLi; q_c1=c7f86e3668184fef902314c3f912cbc4|1578898093000|1555570505000; Hm_lvt_98beee57fd2ef70ccdd5ca52b9740c49=1578898093,1578909193,1578987199,1579090237; Hm_lpvt_98beee57fd2ef70ccdd5ca52b9740c49=1579090237; KLBRSID=5430ad6ccb1a51f38ac194049bce5dfe|1579090340|1579090235'
headers = {
    'user-agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_13_4) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/79.0.3945.117 Safari/537.36',
    'host': 'www.zhihu.com'
}
jar = requests.cookies.RequestsCookieJar()
for cookie in cookies.split(';'):
    key, value = cookie.split('=', 1)
    print(key, value)
    jar.set(key, value)
res = requests.get('https://www.zhihu.com', cookies=jar, headers=headers)
print(res.status_code)


# 会话维持
requests.get('https://httpbin.org/cookies/set/number/123456789')
res = requests.get('https://httpbin.org/cookies')
print(res.text)

req = requests.Session()
req.get('https://httpbin.org/cookies/set/number/123456789')
resp = req.get('https://httpbin.org/cookies')
print(resp.text)
