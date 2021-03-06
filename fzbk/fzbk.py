# -*-codeing = utf-8 -*-
# @Time : 2021/3/5
# @Author : 山与河　qq 2900180755
# @FIle ： fuzzbk.py
# @Software : PyCharm
import re
import requests
import random
import argparse
from multiprocessing.dummy import Pool


header = [
    {'User-Agent':"Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.1 (KHTML, like Gecko) Chrome/22.0.1207.1 Safari/537.1"},
     {'User-Agent':"Mozilla/5.0 (X11; CrOS i686 2268.111.0) AppleWebKit/536.11 (KHTML, like Gecko) Chrome/20.0.1132.57 Safari/536.11"},
      {'User-Agent':"Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/536.6 (KHTML, like Gecko) Chrome/20.0.1092.0 Safari/536.6"},
       {'User-Agent':"Mozilla/5.0 (Windows NT 6.2) AppleWebKit/536.6 (KHTML, like Gecko) Chrome/20.0.1090.0 Safari/536.6"},
        {'User-Agent':"Mozilla/5.0 (Windows NT 6.2; WOW64) AppleWebKit/537.1 (KHTML, like Gecko) Chrome/19.77.34.5 Safari/537.1"},
         {'User-Agent':"Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/536.5 (KHTML, like Gecko) Chrome/19.0.1084.9 Safari/536.5"}]

houzhui = ['.gz', '.sql.gz', '.tar.gz','.tar.tgz','.rar','.zip','.tar','.tar.bz2','.sql','.7z','.bak','.txt','.git','.svn','.swp','.mdb','.old','.log']

# 返回文件名
def Name_url(url):
    ex = '[a-zA-Z0-9][-a-zA-Z0-9]{0,62}(\.[a-zA-Z0-9][-a-zA-Z0-9]{0,62})+\.?'
    name = re.search(ex, url, re.S)
    if url != 'None':
        name_list = name[0].split('.')
        name_url = name_list[-2] + '.' + name_list[-1]
        return name_url

# 生成特使特殊路径
def zj(urls_list):   # 生成特殊路径
    urls_dir = []
    txt_list = ['db','1','111','123']
    for url in urls_list:
        for txt in txt_list:
            url_bk = url + txt
            urls_dir.append(url_bk)
    return urls_list+urls_dir

#  分解url
def fuzzdir(url):
    global  file_txt_name
    urls=[]
    ex = '[a-zA-Z0-9][-a-zA-Z0-9]{0,62}(\.[a-zA-Z0-9][-a-zA-Z0-9]{0,62})+\.?'
    name = re.search(ex, url, re.S)
    if url != 'None':
        name_list = name[0].split('.')
        if len(name_list) == 2:  # 分解https://baidu.com
            name_url = name_list[-2] + '.' + name_list[-1]
            urls.append(name_list[0])
            urls.append(name_url)
            urls.append('www.'+name_url)
            name_url = name_list[-2] + '_' + name_list[-1]
            urls.append(name_url)
            name_url = name_list[-2] + '_' + name_list[-1]
            urls.append('www_'+name_url)
            urls = zj(urls)
            return urls
        elif len(name_list) == 3:   # 分解https://www.baidu.com 或 https://pan.baidu.com
            i = name_list.count('www')
            if i == 0:
                name_url = name_list[-2] + '.' + name_list[-1]
                urls.append(name_list[0])
                urls.append(name_list[1])
                urls.append(name_url)
                urls.append('www.' + name_url)
                name_url =  name_list[-3] + '.'+name_list[-2] + '.' + name_list[-1]
                urls.append(name_url)
                urls.append('www.' + name_url)
                name_url = name_list[-2] + '_' + name_list[-1]
                urls.append(name_url)
                name_url = name_list[-2] + '_' + name_list[-1]
                urls.append('www_' + name_url)
                name_url =  name_list[-3] + '_'+name_list[-2] + '_' + name_list[-1]
                urls.append(name_url)
                urls.append('www_' + name_url)
                urls = zj(urls)
                return urls
            else:
                if i != 0:
                    urls.append(name_list[1])
                    name_url = name_list[-2] + '.' + name_list[-1]
                    urls.append(name_url)
                    urls.append('www.' + name_url)
                    name_url = name_list[-2] + '_' + name_list[-1]
                    urls.append(name_url)
                    name_url = name_list[-2] + '_' + name_list[-1]
                    urls.append('www_' + name_url)
                    urls = zj(urls)
                    return urls
        elif len(name_list) == 4:  # 分解https://www.pan.baidu.com
            name_url = name_list[-2] + '.' + name_list[-1]
            urls.append(name_list[1])
            urls.append(name_list[2])
            urls.append(name_url)
            urls.append('www.' + name_url)
            name_url = name_list[-3] + '.' + name_list[-2] + '.' + name_list[-1]
            urls.append(name_url)
            urls.append('www.' + name_url)
            name_url = name_list[-2] + '_' + name_list[-1]
            urls.append(name_url)
            name_url = name_list[-2] + '_' + name_list[-1]
            urls.append('www_' + name_url)
            name_url = name_list[-3] + '_' + name_list[-2] + '_' + name_list[-1]
            urls.append(name_url)
            urls.append('www_' + name_url)
            urls = zj(urls)
            return urls

# 读取rar.txt 并生成 dirs
def flie_txt():
    dir_s = []
    i = 0
    with open('rar.txt', mode='r', encoding='UTF-8-sig') as fp:
        for dir_txt in fp:
            dir = dir_txt.rstrip()
            for hz in houzhui:
                url_dir_hz =  dir + hz
                zj(dir_s)
                dir_s.append(url_dir_hz)
                i += 1
        return dir_s

#　返回urls列表
def ret_list(url):
    if url[-1:] == "/":
        url = url[:-1]
    else:
        url = url
    url_list = fuzzdir(url)
    dir_s = flie_txt()
    for url_dir in url_list:
        for hz in houzhui:
            url_dir_hz = '/' + url_dir + hz
            dir_s.append(url_dir_hz)
    urls = []
    i = 0
    sub = Name_url(url)
    for dir_hz in dir_s:
        i +=1
        url_dic = {}
        url_dir = url + dir_hz
        url_dic.update({'i':str(i),'url':url_dir,'sub':sub})
        urls.append(url_dic)
    return urls

# 请求
def requ(url):
    url_200_list = []
    try:
        i = url['i']
        url_u = url['url']
        sub = url['sub']
        code = requests.head(url=url_u,headers=header[random.randint(0, len(header)-1)]).status_code
        if code == 200:
            if url_200_list.count(sub) <=5 :
                with open("url_rar_200.txt", mode='r', encoding='UTF-8-sig') as fp:
                    url_200_list.append(url_u)
                    fp.write(url_u+'\n')
                    print(i, ' ==> ',url_u, ' ==> ', code)
                    print('==================可能存在备份文件==================')
                    for url_200_list in url_200_list:
                        print(url_200_list)
        else:
            print(i, ' ==> ',url_u, ' ==> ', code)
            if len(url_200_list) != 0:
                print('==================可能存在备份文件==================')
                for url_200_list in url_200_list:
                    print(url_200_list)
    except Exception as a:
        print(a)

# 运行
def run(url):
    try:
        urls = ret_list(url)
        pool = Pool(20)
        pool.map(requ,urls)
        pool.close()
        pool.join()
    except Exception as a:
        print(a)

if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('-u', help='单个扫描')
    parser.add_argument('-f', help='文本批量')
    args = parser.parse_args()
    if (args.u):
        run(args.u)
    if (args.f):
        try:
            with open(args.f, mode='r', encoding='UTF-8-sig') as fp:
                for url_s in fp:
                    url = url_s.rstrip()
                    run(url)
        except Exception as a:
            print(a)