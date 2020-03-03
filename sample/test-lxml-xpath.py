#!/usr/bin/env python
# coding=utf-8
from lxml import etree
import requests


# / 从根节点选取
# // 从当前节点查找子节点，不考虑位置
# . 选取当前节点
# .. 选取父节点 /../ /parent::*/
# @ 选取属性 /div/@src
# div[@class="container"] 属性过滤


resp = requests.get('https://www.geekdigging.com/')
html_str = resp.content.decode('utf-8')
html = etree.HTML(html_str)
result = etree.tostring(html, encoding='utf-8').decode('utf-8')
print(result)


# 浏览器右键copy xpath,快捷生成xpath路径
# text()方法
# html.xpath('//*[@id="juejin"]/div[2]/main/div/div[1]/article/div[4]/p[29]/text()')

# 属性获取
# html.xpath('//*[@id="juejin"]/div[2]/main/div/div[1]/article/div[4]/p[29]/a/@href')

# 属性匹配
# html.xpath('//div[@class="post-head"]')
# html.xpath('//div[contains(@class, "post-head")]')
# html.xpath('//img[@class="img-ajax" and @alt="python"]')


# 按顺序选择
# result1 = html.xpath('//article/div/div/h3[@class="title"]/a/text()')
# result2 = html.xpath('//article[1]/div/div/h3[@class="title"]/a/text()')
# result3 = html.xpath('//article[last()]/div/div/h3[@class="title"]/a/text()')
# result4 = html.xpath('//article[position() < 5]/div/div/h3[@class="title"]/a/text()')

# 节点轴
# ancestor 祖先节点
# attribute 节点属性
# child 子节点
# descendant 后代节点
# following 结束标签后的所有节点
# namespace  当前节点的所有命名空间节点
# parent 父节点
# preceding 当前节点开始标签之前的所有节点
# preceding-sibling 当前节点之前的所有同级节点
# self 当前节点

# 获取所有祖先节点
# result_5 = html.xpath('//article/ancestor::*')
# 获取祖先节点 main 节点
# result_6 = html.xpath('//article/ancestor::main')

