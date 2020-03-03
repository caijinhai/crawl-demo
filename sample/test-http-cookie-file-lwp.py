#!/usr/bin/env python
# coding=utf-8

import urllib.request, http.cookiejar

# cookies 保存 LWP 型文件示例
filename = 'cookies_lwp.txt'
cookie = http.cookiejar.LWPCookieJar(filename)
handler = urllib.request.HTTPCookieProcessor(cookie)
opener = urllib.request.build_opener(handler)
response = opener.open('http://www.baidu.com')
cookie.save(ignore_discard=True, ignore_expires=True)
print('cookies_lwp 保存成功')

