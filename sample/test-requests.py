#!/usr/bin/env python
# coding=utf-8
import requests

res = requests.get('https://httpbin.org/get')
print(res.text)

params= {
    'name': 'cesar',
    'age': 15
}
res = requests.get('https://httpbin.org/get', params)
print(res.text)
print(type(res.text))
print(res.json())
print(type(res.json()))

headers = {
    'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_13_4) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/79.0.3945.117 Safari/537.36',
    'referer': 'https://pixabay.com/'
}

res = requests.get('https://httpbin.org/get', headers=headers)
print(res.text)

res = requests.get('https://www.baidu.com/img/superlogo_c4d7df0a003d3db9b65e9ef0fe6da1ec.png')
with open('baidu_log.png', 'wb') as f:
    f.write(res.content)


parmas = {
    'name': 'cesar',
    'age': 18
}
res = requests.post('https://httpbin.org/post', data=params, headers=headers)
print(res.text)
print(type(res.status_code), res.status_code)
print(type(res.headers), res.headers)
print(type(res.cookies), res.cookies)
print(type(res.url), res.url)
print(type(res.history), res.history)
