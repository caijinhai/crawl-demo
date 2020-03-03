#!/usr/bin/env python
# coding=utf-8
import urllib.request, http.cookiejar

filename = 'cookies_mozilla.txt'
cookie = http.cookiejar.MozillaCookieJar(filename)

handler = urllib.request.HTTPCookieProcessor(cookie)
opener = urllib.request.build_opener(handler)
response = opener.open('https://baidu.com/')

cookie.save(ignore_discard=True, ignore_expires=True)
print('cookie save success')

