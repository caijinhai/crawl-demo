#!/usr/bin/env python
# coding=utf-8
from urllib import request, error
import socket

try:
    resp = request.urlopen('https://www.geekdigging.com/aa')
except error.URLError as e:
    print(e.reason)


try:
    resp = request.urlopen('https://www.baidu.com', timeout=0.001)
except error.URLError as e:
    print(e.reason)

try:
    resp = request.urlopen('https://www.baidu.com', timeout=0.001)
except error.URLError as e:
    print(type(e.reason))
    if isinstance(e.reason, socket.timeout):
        print('TIME OUT')

try:
    resp = request.urlopen('https://www.geekdigging.com/aa')
except error.HTTPError as e:
    print(e.reason, e.code, e.headers, sep='\n')

try:
    resp = request.urlopen('https://www.geekdigging.com/aa')
except error.HTTPError as e:
    print(e.reason, e.code, e.headers, sep='\n')
except error.URLError as e:
    print(e.reason)
else:
    print('success')
