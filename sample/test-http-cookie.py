#!/usr/bin/env python
# coding=utf-8
import http.cookiejar, urllib.request

cookie = http.cookiejar.CookieJar()
handler = urllib.request.HTTPCookieProcessor(cookie)
opener = urllib.request.build_opener(handler)

response = opener.open('https://www.baidu.com/')

print(cookie)

for item in cookie:
    print(item.name + ' = ' + item.value)

