#!/usr/bin/env python
# coding=utf-8
# 0, $ 行首，行未
# gg, shift G 页首，页未
# :0, :$ 页首，页未

from urllib.parse import urlparse, urlunparse, urlsplit, urlunsplit, urljoin, parse_qs, parse_qsl, urlencode, quote, unquote

res = urlparse('https://docs.python.org/zh-cn/3.7/library/urllib.parse.html#module-urllib.parse')
print(type(res))
print(res)

res = urlparse('https://docs.python.org/zh-cn/3.7/library/urllib.parse.html#module-urllib.parse', scheme='https', allow_fragments=False)
print(res)
params = ('https', 'www.geekdigging.com', 'index.html', 'people', 'a=1', 'geekdigging')
print(urlunparse(params))

res = urlsplit('https://docs.python.org/zh-cn/3.7/library/urllib.parse.html;people#module-urllib.parse')
print(type(res))
print(res)
params = ('https', 'www.geekdigging.com', 'index.html;people', 'a=1', 'geekdigging')
print(urlunsplit(params))

print(urljoin('https://www.cesar.com/', 'index.html'))
print(urljoin('https://www.cesar.com/', 'https://www.cesar.com/index.html'))

print(parse_qs('a=1&b=1'))
print(parse_qsl('a=1&b=1'))

print('http://www.cesar.com/' + urlencode({ 'name': '凯撒', 'age': 18 }))
print(quote('凯撒'))
print(unquote(quote('凯撒')))
