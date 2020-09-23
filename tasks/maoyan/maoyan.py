
import requests
import time
import json
import os
import xlrd
import urllib.request, http.cookiejar
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.options import Options
from lxml import etree


driver = webdriver.Chrome(ChromeDriverManager().install())
# 使用已打开的浏览器窗口
# chrome_options = Options()
# chrome_options.add_experimental_option("debuggerAddress", "127.0.0.1:9222")
# driver = webdriver.Chrome(ChromeDriverManager().install(), options=chrome_options)
# driver = webdriver.Chrome()

def get_films():
    base_dir = os.path.dirname(os.path.abspath(__file__))
    film_tsv = os.path.join(base_dir, 'films.tsv')
    with open(film_tsv) as f:
        content = f.read()
        items = content.split('\n')
    films = []
    for item in items:
        if not item:
            continue
        film_id, name = item.split('\t')
        films.append((film_id, name))
    
    return films

def search_film(name):
    '''
    kw: 关键词
    type: 0: 影视; 1: 影人; 2: 影院;
    offset: 页数偏移
    '''
    url = 'https://maoyan.com/query?kw=%s&type=0' % name
    # resp = requests.get(url)
    # html_str = resp.content.decode('utf-8')
    # html = etree.HTML(html_str)
    # movie_list = html.xpath('//*[@class="search-result-box"]')
    # print(movie_list)
    driver.get(url)
    time.sleep(5)
    element = driver.find_elements_by_class_name('movie-item')
    print(element[0].text)


if __name__ == "__main__":
    search_film('mulan')
