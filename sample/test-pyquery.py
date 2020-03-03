#!/usr/bin/env python
# coding=utf-8
from pyquery import PyQuery
import requests

html = '''
<html><head><title>The Dormouse's story</title></head>
<body>
<p class="title"><b>The Dormouse's story</b></p>

<p class="story">Once upon a time there were three little sisters; and their names were
<a href="http://example.com/elsie" class="sister" id="link1">Elsie</a>,
<a href="http://example.com/lacie" class="sister" id="link2">Lacie</a> and
<a href="http://example.com/tillie" class="sister" id="link3">Tillie</a>;
and they lived at the bottom of a well.</p>

<p class="story">...</p>
'''

res = PyQuery(html)
print(res)

#d_url = PyQuery(url='https://www.geekdigging.com/', encoding='utf-8')
#print(d_url('title'))

#res = requests.get('https://www.geekdigging.com/')
#d_url = PyQuery(res.text)
#print(d_url('title'))

# css 选择器
print(res('.story .sister'))

# 查找子节点
items = res('body')
print(items.find('p'))

# 查找父节点
items = res('#link1')
print(items.parent())

# 查找兄弟节点
items = res('#link1')
print(items.siblings())

# 遍历
items = res('a')
for item in items.items():
    print(item)

# 获取文本信息
items = res('#link1')
print(items.text())

# html
items = res('.story')
print(items.html())

# 获取属性信息
items = res('#link1')
print(items.attr('href'))
print(items.attr.href)
