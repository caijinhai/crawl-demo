#!/usr/bin/env python
# coding=utf-8
import urllib.robotparser

rp = urllib.robotparser.RobotFileParser()
rp.set_url('https://www.taobao.com/robots.txt')
rp.read()

print(rp.can_fetch('Googlebot', 'https://www.taobao.com/article'))
print(rp.can_fetch('Googlebot', 'https://s.taobao.com/search?initiative_id=tbindex'))
