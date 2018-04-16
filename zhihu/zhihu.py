#! /usr/bin/env python
import urllib
import re
import urllib.request
import urllib.parse
import os
import json

url = 'https://www.zhihu.com/question/37787176'

if not os.path.exists('images'):
    os.mkdir("images")

page_size = 50
offset = 0
url_content = urllib.request.urlopen(url).read()
url_content=url_content.decode('utf-8')
pattern=re.compile(r'(h3 data-num="(.*?)")')
answers = pattern.findall(url_content)
print(answers)#列表
limits = len(answers)

while offset < limits:
    post_url = 'https://www.zhihu.com/question/37787176/answer/81607754'
    params = json.dumps({
        'url_token': 37787176,
        'pagesize': page_size,
        'offset': offset
    })
    datas = {
        '_xsrf': '',
        'method': 'next',
        'params': params
    }
    headers = {
        'User-Agent': "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/65.0.3325.181 Safari/537.36",
        'Host': "www.zhihu.com",
        'Referer': url
    }

    data = urllib.parse.urlencode(datas).encode('utf-8')
    req = urllib.request.Request(url=post_url, data=data, headers=headers,method = 'POST')
    response=urllib.request.urlopen(req)
    html=response.read().decode('utf-8')
    print(html)

    answer_list = json.dumps(html)["msg"]
    print(answer_list)

    img_urls = re.findall('img .*?src="(.*?_b.*?)"', ''.join(answer_list))
    for img_url in img_urls:
        try:
            img_data = urllib.request.urlopen(img_url).read()
            file_name = basename(urlsplit(img_url)[2])
            output = open('images/' + file_name, 'wb')
            output.write(img_data)
            output.close()
        except:
            pass
    offset += page_size