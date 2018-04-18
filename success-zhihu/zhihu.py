#! /usr/bin/env python
import requests
import os
import json
from bs4 import BeautifulSoup
import re
import time

headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/63.0.3239.108 Safari/537.36',
    "Connection": "keep - alive",
    "Accept": "text/html,application/xhtml+xml,application/xml;",
    "authorization": "Bearer 2|1:0|10:1517365431|4:z_c0|92:Mi4xQlNfQUF3QUFBQUFBWUsxQzBaUVNEU1lBQUFCZ0FsVk50M1plV3dETUxEbXNWRFlTSTMzZmdRbGF2dU4tb3JJenNR|c4e352f19849ea9afa0e2cab8f37137470a38051511cbeb317f31d50543ebed4"
    }

#判断是否存在D:/zhihu文件夹路径
isExists = os.path.exists("D:/y/zhihu")
if not isExists:
    os.makedirs("D:/y/zhihu")
    os.chdir("D:/y/zhihu")
else:
    os.chdir("D:/y/zhihu")

url="https://www.zhihu.com/question/37787176"
html=requests.get(url,headers=headers).text
answer=BeautifulSoup(html,"lxml").find("h4",class_="List-headerText").find("span").get_text()#todo//为什么要写成class_而不是class
print(answer)
answer_num=int(re.sub(',','',re.sub('\s\S+','',answer)))#不捕捉分组,导致换行后返回为“1,534 个回答”,因此必须写在同一行执行,把”1,534 个回答“转化成数字1534,
#总的回答数量
print(answer_num)

url_prefix="https://www.zhihu.com/api/v4/questions/37787176/answers?sort_by=default&include=data%5B%2A%5D.is_normal%2Cis_collapsed%2Ccollapse_reason%2Cis_sticky%2Ccollapsed_by%2Csuggest_edit%2Ccomment_count%2Ccan_comment%2Ccontent%2Ceditable_content%2Cvoteup_count%2Creshipment_settings%2Ccomment_permission%2Cmark_infos%2Ccreated_time%2Cupdated_time%2Creview_info%2Crelationship.is_authorized%2Cis_author%2Cvoting%2Cis_thanked%2Cis_nothelp%2Cupvoted_followees%3Bdata%5B%2A%5D.author.follower_count%2Cbadge%5B%3F%28type%3Dbest_answerer%29%5D.topics&limit=20&offset="
offset=30

header = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/63.0.3239.108 Safari/537.36'
}

while offset < answer_num:
    answer_url=url_prefix+str(offset)
    #服务器返回的响应数据，分为data和paging
    #data为用户回答的内容及用户信息
    #paging(分页记录:上一页和下一页的索引offset值)
    html=requests.get(answer_url,headers=headers).text
    print(html)
    content=json.loads(html)["data"]
    for row in content:
        gender=row["author"]["gender"]
        if gender == 0:#1为男生,0为女生,只抓取女性回答下的照片
            answer=row["content"]
            pic_list=BeautifulSoup(answer,'lxml').find_all("img")
            for pic in pic_list:
                down_url=pic["src"]
                if down_url.startswith("http"):
                    name=re.sub(".*/","",down_url)
                    print(name)
                    file=open(name,"ab")#以二进制格式打开一个文件用于追加
                    print("开始下载：",name)                    
                    file.write(requests.get(down_url,headers=header).content)
                    print("下载完：", name)
                    file.close()
        else:
            pass
    offset+=20
    #sleep()方法暂停给定秒数后执行程序，防止请求太过频繁被知乎屏蔽
    time.sleep(3)