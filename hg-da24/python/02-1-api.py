# -*- coding: utf-8 -*-
"""
Created on Thu Mar 28 12:05:06 2024

@author: jcp
"""

# %%
# ## 파이썬으로 API 호출하기
# 도서관 정보나루

# 20대가 가장 좋아하는 도서 찾기

# In[23]:


import requests


# In[24]:

# 서비스 주소: http://data4library.kr/api/loanItemSrch
# 파라미터:
    # format=json
    # startDt=2021-04-01
    # endDt=2021-04-30
    # age=20
    # authKey=c01ec15e4574f74ee45cba2601bad15b82971e606e3b0740977ee4b363ce2fe2

def get_svc_url2(svcurl):
    url = []
    url.append(svcurl['url'])
    
    options = svcurl['options']
    for k in options.keys():
        url.append('&')
        url.append(k)
        url.append('=')
        url.append(options[k])
        
    url = "".join(url)
    url = url.replace('&', '', 1)
        
    return url


# %%
def get_svc_url(svcurl):
    url = []
    options = svcurl['options']
    for k in options.keys():
        v = options[k]
        kv = f"{k}={v}"
        url.append(kv)
        
    urls = '&'.join(url)
    return svcurl['url'] + urls



# %%


svcurl = {
    "url":"http://data4library.kr/api/loanItemSrch?",
    "options":{
        "format":"json",
        "startDt":"2021-04-01",
        "endDt":"2021-04-30",
        "age":"20",
        "authKey":"c01ec15e4574f74ee45cba2601bad15b82971e606e3b0740977ee4b363ce2fe2"
        }
    }

url2 = get_svc_url(svcurl)

print(url2)
# %%
# 인증키를 발급받아 문자열 맨 끝에 추가해 주세요.
url = "http://data4library.kr/api/loanItemSrch?format=json&startDt=2021-04-01&endDt=2021-04-30&age=20&authKey=c01ec15e4574f74ee45cba2601bad15b82971e606e3b0740977ee4b363ce2fe2"

print(url)

# 파라미터 사이는 & 문자로 연결
# 호출 url과 파라미터는 ? 문자로 연걸.
# HTTP GET 방식.
# 쿼리 스트링 : ? 문자 뒤에 연결된 파라미터와 값들.


# In[25]:

# Response 객체
r = requests.get(url) 


# In[26]:

# Response.json() :
# 응답 받은 json 문자열을 파이썬 객체로 변환하여 반환.
data = r.json()

print(data)


# In[27]:


data


# In[28]:


data['response']['docs']


# In[29]:


books = []
for d in data['response']['docs']:
    books.append(d['doc'])


# In[30]:


books = [d['doc'] for d in data['response']['docs']]

# In[31]:

books

# In[32]:


import pandas as pd
books_df = pd.DataFrame(books)

books_df


# In[33]:

# JSON으로 변환하여 저장
books_df.to_json('20s_best_book.json')

"""
JSON VS XML

JSON : HTML이나 XML보다 사람이 읽기 편하고 간단하게 파이썬 객체로 변환 가능

XML : JSON보다 조금 장황하지만, 사람이 이해하기 쉬운 구조적인 포맷 제공
"""
