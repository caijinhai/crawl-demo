#!/usr/bin/env python
# coding=utf-8
import urllib.request, http.cookiejar

cookie = http.cookiejar.MozillaCookieJar()
cookie.load('cookies_mozilla.txt', ignore_discard=True, ignore_expires=True)

handler = urllib.request.HTTPCookieProcessor(cookie)
opener = urllib.request.build_opener(handler)
response = opener.open('http://baidu.com/')
print(response.read().decode('utf-8'))
