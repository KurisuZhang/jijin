#!/usr/bin/env python
# coding: utf-8

# In[ ]:


'''
获取取环境变量server酱sdk
爬虫天天基金每天估值
将数据通过server酱传给微信
'''


# In[4]:


import requests
import json
import os
import re


# In[5]:


env_dist = os.environ
my_funds = {"易方达蓝筹精选混合":"005827","华宝科技ETF联接C":"007874","华宝券商ETF联接C":"007531","诺安成长混合":"320007","华夏中证5G通信主题ETF联接C":"008087"}
valuation = {}
markdown_format = ""


# In[6]:


for fund_name in my_funds:
    response = requests.get("http://fundgz.1234567.com.cn/js/" + my_funds[fund_name] + ".js")
    fond_re = re.match('jsonpgz\((.*)\)', response.text)
    fond_re = fond_re.group(1)
    fond_dict = json.loads(fond_re)
    valuation[fund_name] = float(fond_dict["gszzl"])
    markdown_format = markdown_format + "**"+ fund_name +"**" + ":  " + fond_dict["gszzl"] + "  \n"


# In[7]:


print(valuation)
print(fond_re)
print(markdown_format)


# In[8]:


data = {"text": "今天基金结果","desp":str(markdown_format)}
url = "https://sc.ftqq.com/" + env_dist["SCKEY"] + ".send"
requests.post(url,params=data)


# In[ ]:




