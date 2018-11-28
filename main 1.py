# coding : UTF-8
import requests
import csv
import random
import time
import socket
import http.client
# import urllib.request
from bs4 import BeautifulSoup

def get_content(url , data = None):
    header={
        'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8',
        'Accept-Encoding': 'gzip, deflate, sdch',
        'Accept-Language': 'EN-US,en;q=0.8',
        'Connection': 'keep-alive',
        'User-Agent': 'Mozilla/5.0 (Windows NT 6.3; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/43.0.235'
    }
    timeout = random.choice(range(80, 180))
    while True:
        try:
            rep = requests.get(url,headers = header,timeout = timeout)
            rep.encoding = 'utf-8'
            # req = urllib.request.Request(url, data, header)
            # response = urllib.request.urlopen(req, timeout=timeout)
            # html1 = response.read().decode('UTF-8', errors='ignore')
            # response.close()
            break
        # except urllib.request.HTTPError as e:
        #         print( '1:', e)
        #         time.sleep(random.choice(range(5, 10)))
        #
        # except urllib.request.URLError as e:
        #     print( '2:', e)
        #     time.sleep(random.choice(range(5, 10)))
        except socket.timeout as e:
            print( '3:', e)
            time.sleep(random.choice(range(8,15)))

        except socket.error as e:
            print( '4:', e)
            time.sleep(random.choice(range(20, 60)))

        except http.client.BadStatusLine as e:
            print( '5:', e)
            time.sleep(random.choice(range(30, 80)))

        except http.client.IncompleteRead as e:
            print( '6:', e)
            time.sleep(random.choice(range(5, 15)))

    return rep.text
    # return html_text

def get_data(html_text):
    final = []
    bs = BeautifulSoup(html_text, "html.parser")  # 创建BeautifulSoup对象
    body = bs.body# 获取body部分
    data = body.find('div', {'class': 'field field--name-body field--type-text-with-summary field--label-hidden'})  # 找到id为7d的div
    #data1 = body.find('div', {'class': 'field__item.even'})
    h2 = data.find_all('h2')
    print(len(h2))
    for aks in h2:

        temp = []
        CollegeName = aks.string  # 找到学院名
        temp.append(CollegeName)
        # if (aks.find('element-invisible')):
        #     print('666666666')
            #info = aks.find('a').string
            #temp.append(info)
        # inf = aks.find_all('p')  # 找到li中的所有p标签
        # temp.append(inf[0].string)  # 第一个p标签中的内容（天气状况）加到temp中
        # if(inf[1].find('strong')):
        #     info = inf[1].find('strong').string
        #     temp.append(info)
        # if inf[0].find('strong'):
        #     temperature_highest = None # 天气预报可能没有当天的最高气温（到了傍晚，就是这样），需要加个判断语句,来输出最低气温
        # else:
        #     temperature_highest = inf[1].find('strong').string  # 找到最高温
        #     temp.append(temperature_highest)
        # temperature_lowest = inf[1].find('i').string  # 找到最低温
        # temperature_lowest = temperature_lowest.replace('℃', '')  # 最低温度后面有个℃，去掉这个符号
        #temp.append(temperature_highest)   # 将最高温添加到temp中
        # temp.append(temperature_lowest)   #将最低温添加到temp中
        final.append(temp)   #将temp加到final中

    return final

def write_data(data, name):
    file_name = name
    with open(file_name, 'a', errors='ignore', newline='') as f:
            f_csv = csv.writer(f)
            f_csv.writerows(data)


if __name__ == '__main__':
    url ='https://admissions.uiowa.edu/academics/first-year-admission'
    html = get_content(url)
    result = get_data(html)
    write_data(result, 'weather.csv')