#!/usr/bin/env python
#coding=utf-8

import requests
from bs4 import BeautifulSoup
import csv # 引入csv模块，读写csv文件
import datetime # 引入日期时间模块

base_url = 'https://www.baidu.com'

def shouYeReMen():
    add_url = '' # 先置为空字符串
    title_list = [] # 文章标题列表
    
    for i in range(1): # 首页热门实际为15页，一开始可以设大些让程序自动退出来看到底有多少页
        try:
            first_page = requests.get(base_url+ add_url).content
            #soup = BeautifulSoup(first_page, "lxml")
            soup = BeautifulSoup(first_page, "html.parser")  #不指定解析器，则自动选择
            print(soup)
            title_list += [i.get_text() for i in soup.select("a")]
            print(title_list)
            # 以上和上一个爬虫类同
            try:
                # print(soup.select(".ladda-button"))
                add_url = soup.select(".ladda-button")[-1].get("data-url")
                # 使用get方法获取button的标签属性信息作为额外的url
                # 这里使用try，在最后一页没有button时会抛出异常
            except:
                # 在异常处理中通过break退出循环
                break
        except requests.exceptions.ConnectionError: # 有可能请求过多导致服务器拒绝连接
            status_code = "Connection refused"
            print(status_code)
            time.sleep(60)
            # 我们睡眠一分钟后再爬
    with open(datetime.datetime.now().strftime('%Y_%m_%d-%H_%M_%S')+'.csv', 'w', newline='', encoding='GBK') as f:
    # 在脚本当前文件目录下新建以当前时间命名的csv文件，使用utf8编码
        writer = csv.writer(f)
        # 传入文件描述符构建csv写入器
        writer.writerow(title_list)
        # 将本次爬取的所有文章列表写在一行中
        
    print("have_done!")
    
import time
shouYeReMen()
# 最后，我们循环爬取首页信息，为了减轻服务器负担，也避免爬虫请求被拒绝，我们每隔30秒爬取一次
# while true:
    # time.sleep(30)
    # shouyeremen()