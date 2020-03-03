#!/usr/bin/env python
# coding=utf-8
from bs4 import BeautifulSoup
import requests

resp = requests.get('https://www.geekdigging.com/')
soup = BeautifulSoup(resp.content, 'html5lib')
# print(soup.prettify())

print(soup.title)
print(type(soup.title))
print(soup.title.string)
print(soup.a)

# tag 类
tag = soup.a.img
print(tag.name)
# 获取属性
print(tag.attrs)
print(tag['src'])

# 嵌套
print(soup.a.img)
print(type(soup.a.img))
print(soup.a.img.attrs)

# 子节点
for child in enumerate(soup.a.children):
    print(child)

# 孙子节点
for i, child in enumerate(soup.a.descendants):
    print(i, child)

# 父子节点
print(soup.title.parent)

# 兄弟节点
print(soup.title.next_sibling)
print(soup.title.previous_sibling)
print(soup.title.next_siblings)
print(soup.title.previous_siblings)
