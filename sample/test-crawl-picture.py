#!/usr/bin/env python
# coding=utf-8
import urllib.request
import urllib.robotparser
import os
from lxml import etree
import time

# header
headers = {
    'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_13_4) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/79.0.3945.117 Safari/537.36',
    'referer': 'https://pixabay.com/'
}

basedir = os.path.dirname(os.path.abspath(__file__))
save_path = os.path.join(basedir, 'pictures')

def create_file(file_path):
    if os.path.exists(file_path) is False:
        os.makedirs(file_path)
    os.chdir(file_path)


def write_content(file_path, content):
    if os.path.isfile(file_path):
        pass
    else:
        with open(file_path, 'w+') as fp:
            fp.write(content)


def get_keywords(url):
    req = urllib.request.Request(url=url, headers=headers, method='GET')
    resp = urllib.request.urlopen(req)
    html = etree.HTML(resp.read().decode('utf-8'))
    wrap = html.xpath('/html/body/div[1]/div[2]/div[1]/div[3]/div/a')
    tags = []
    for item in wrap:
        tags.append({ 'href': item.xpath('@href')[0], 'name': item.text })
    return tags

def get_keyword_pictures(url, tag):
    tag_url = url + tag.get('href')
    req = urllib.request.Request(url=tag_url, headers=headers, method='GET')
    resp = urllib.request.urlopen(req)
    html = etree.HTML(resp.read().decode('utf-8'))
    wrap = html.xpath('/html/body/div[1]/div[2]/div[1]/div[2]/div/div[3]/div')
    docs = []
    create_file(save_path)
    for item in wrap:
        doc = {
            'category': tag.get('name'),
            'url': item.xpath('a/img/@src')[0]
        }
        docs.append(doc)
        if len(docs) >= 5:
            break
    write_content(os.path.join(save_path, '%s.json' % tag.get('name')), str(docs))


def check_robot_permission(robot_url, check_url):
    rp = urllib.robotparser.RobotFileParser(robot_url)
    rp.read()
    return rp.can_fetch('Googlebot', check_url)

def main():
    url = 'https://pixabay.com/zh/'
    robot_url= 'https://pixabay.com/robots.txt'
    print(url)
    tags = get_keywords(url)
    for tag in tags:
       # print(check_robot_permission(robot_url, url + tag.get('href')))
        get_keyword_pictures('https://pixabay.com', tag)

if __name__ == '__main__':
    main()
