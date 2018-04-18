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
url_content = url_content.decode('utf-8')
# file_name = open('tt.txt', "wb")
# file_name.write(url_content)
print(url_content)
# pattern = re.compile(r'(<div class=\"List-item\">).*(<\/div>)')#最小匹配模式
# answers = pattern.findall(url_content)
# limits = len(answers)
# print(answers)#列表
# print(limits)

# while offset < limits:
#     post_url = 'https://www.zhihu.com/question/37787176/answer/81607754'
#     # post_url='https://www.zhihu.com/question/37787176'

#     # params = json.dumps({
#     #     'url_token': 37787176
#     # })
#     # datas = {
#     #     '_xsrf': '',
#     #     'method': 'next',
#     #     'params': params
#     # }
#     headers = {
#         'User-Agent': "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/65.0.3325.181 Safari/537.36",
#         'Host':"www.zhihu.com",
#         'Referer': url
#     }

#     data = urllib.parse.urlencode(datas).encode('utf-8')
#     req = urllib.request.Request(url=post_url, data=data, headers=headers,method = 'POST')
#     response=urllib.request.urlopen(req)
#     html=response.read().decode('utf-8')
#     print(html)

#     answer_list = json.dumps(html)
#     print(answer_list)

#     pattern=re.compile(r'(http|https):\/\/([0-9A-Za-z\._]*\/)*([0-9A-Za-z_]*)\.(jpg|jpeg|png)')

#     img_urls = pattern.findall(''.join(answer_list))
#     for img_url in img_urls:
#         try:
#             img_data = urllib.request.urlopen(img_url).read()
#             file_name = basename(urlsplit(img_url)[2])
#             output = open('images/' + file_name, 'wb')
#             output.write(img_data)
#             output.close()
#         except:
#             pass
#     offset =  offset + 1