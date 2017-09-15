import re
import os
import random
import time
import requests
import itertools
from hashlib import md5
from bs4 import BeautifulSoup
from multiprocessing import Pool
from pyquery import PyQuery as pq
from requests.exceptions import RequestException

headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/59.0.3071.115 Safari/537.36',
}


def get_homepage(url):
    try:
        response = requests.get(url, headers=headers)
        if response.status_code == 200:
            response.encoding = 'utf-8'
            return response.text
    except RequestException:
        print('访问页面错误')


def parse_homepage(html):
    # 试用pyquery
    doc = pq(html)
    boxs_result = doc('.boxs li')
    results = re.findall('<a href="(https://www.meitulu.com/item/\d+.*?)".*?alt="(.*?)".*?</a>', str(boxs_result))
    if results:
        return results


def get_modelurls(url):
    # 获取模特照片url
    response = requests.get(url, headers=headers)
    if response.status_code == 200:
        response.encoding = 'utf-8'
        html = response.text
        # 判断该合集总页数
        maxpage = re.search('html">(\d+)</a> <a class', html)
        url_num = re.search('/item/(\d+).html', url).group(1)
        if maxpage:
            # 将该合集所有页码url遍历成一个list
            url_all = ['https://www.meitulu.com/item/' + str(url_num) + '_' + str(num) + '.html' for num in
                       range(2, int(maxpage.group(1)) + 1)]
            url_all.insert(0, url)
            return url_all


def get_modelpage(url):
    time.sleep(random.randint(1, 5))
    response = requests.get(url)
    if response.status_code == 200:
        response.encoding = 'utf-8'
        html = response.text
        return html


def parse_modelpage(html):
    soup = BeautifulSoup(html, 'lxml')
    img_html = soup.find_all('center')[0]
    img_urls = re.findall('.*?alt="(.*?)".*?src="(.*?)"', str(img_html))
    return img_urls


def main(page_num):
    # 爬取20页美图，共1200个作品
    url = 'https://www.meitulu.com/t/qingxin/' + str(page_num) + '.html'
    html_homepage = get_homepage(url)
    html_modelpages = parse_homepage(html_homepage)
    for result in html_modelpages:
        filename = ''.join(itertools.chain(*re.split('/|\\|:|<|>|\?|"|\*| ', result[1])))
        pic_num = re.search('.*?(\d+?)]', filename)
        print('合集名称：', filename, 'URL:', result[0])
        if os.path.exists(filename) is False:
            os.mkdir(os.path.dirname(os.path.abspath(__file__)) + '\\' + filename)
            for url_all in get_modelurls(result[0]):
                for url_pic in parse_modelpage(get_modelpage(url_all)):
                    pic_name = re.search('.*?(第\d+张)', url_pic[0]).group(1)
                    file_path = (
                        os.path.dirname(
                            os.path.abspath(__file__)) + '\\' + filename + '\\' + filename + pic_name + '.jpg')
                    if not os.path.exists(file_path):
                        content = requests.get(url_pic[1]).content
                        with open(file_path, 'wb') as f:
                            f.write(content)
                            print('正在下载：', url_pic[0])

        if int(len([x for x in os.listdir(os.path.dirname(__file__) + '/' + filename)])) < int(
                pic_num.group(1)) * 7 // 10:
            for url_all in get_modelurls(result[0]):
                for url_pic in parse_modelpage(get_modelpage(url_all)):
                    pic_name = re.search('.*?(第\d+张)', url_pic[0]).group(1)
                    file_path = (
                        os.path.dirname(
                            os.path.abspath(__file__)) + '\\' + filename + '\\' + filename + pic_name + '.jpg')
                    if not os.path.exists(file_path):
                        content = requests.get(url_pic[1]).content
                        with open(file_path, 'wb') as f:
                            f.write(content)
                            print('正在下载：', url_pic[0])


if __name__ == '__main__':
    groups = [num for num in range(2, 21)]
    # 进程数量控制
    pool = Pool(3)
    pool.map(main, groups)
