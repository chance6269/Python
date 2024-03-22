# -*- coding: utf-8 -*-
"""
Created on Fri Mar 22 15:30:04 2024

@author: jcp
"""

# ### 6.2.2 주식 정보 가져오기

# #### 주식 현재가 가져오기

# [6장: 248페이지]

# In[ ]:


import requests
from bs4 import BeautifulSoup

base_url = 'https://finance.naver.com/item/main.nhn'
stock_code = "005930"
url = base_url + "?code=" + stock_code

html = requests.get(url).text
soup = BeautifulSoup(html, 'lxml')

print(url)

# HTTP : GET METHOD
# 삼성전자: 'https://finance.naver.com/item/main.nhn?code=005930'
# 카카오: 'https://finance.naver.com/item/main.nhn?code=035720'

# [6장: 250페이지]

# In[ ]:


soup.select_one('p.no_today')


# In[ ]:


stock_price = soup.select_one('p.no_today span.blind').get_text()
stock_price


# In[ ]:


import requests
from bs4 import BeautifulSoup

def get_current_stock_price(stock_code):
    
    base_url = 'https://finance.naver.com/item/main.nhn'
    url = base_url + "?code=" + stock_code
    
    html = requests.get(url).text
    soup = BeautifulSoup(html, 'lxml')
    
    stock_price = soup.select_one('p.no_today span.blind').get_text()
    
    return stock_price


# [6장: 251페이지]

# In[ ]:


stock_code = "005930"
current_stock_price = get_current_stock_price(stock_code)
current_stock_price


# In[ ]:


company_stock_codes = {"삼성전자": "005930", "현대차":"005380", "NAVER":"035420"}

print("[현재 주식 가격(원)]")
for company, stock_code in company_stock_codes.items():
    current_stock_price = get_current_stock_price(stock_code)
    print(f"{company}: {current_stock_price}")


# #### 주식 종목 코드 가져오기

# [6장: 252페이지]

# In[ ]:


import pandas as pd

# 한국 거래소(KRX)에서 전체 상장법인 목록 가져오기
base_url = "http://kind.krx.co.kr/corpgeneral/corpList.do"
method = "download"
url = "{0}?method={1}".format(base_url, method)

df = pd.read_html(url, header=0, encoding='cp949')[0]

with pd.option_context('display.max_columns',4): # 최대 4개까지 열이 표시하도록 설정
    pd.set_option("show_dimensions", False)      # 행과 열 개수 출력 안 하기
    display(df.head())


# In[ ]:


df['종목코드']= df['종목코드'].apply(lambda x: f"{x:06d}")

with pd.option_context('display.max_columns',4): # 최대 4개까지 열이 표시하도록 설정
    pd.set_option("show_dimensions", False)      # 행과 열 개수 출력 안 하기
    display(df.head())


# In[ ]:


df = df[['회사명','종목코드']]
df.head()


# [6장: 254페이지]

# In[ ]:


import pandas as pd

#----------------------------------------------------
# 한국 주식의 종목 이름과 종목 코드를 가져오는 함수
#----------------------------------------------------
def get_stock_info(maket_type=None):
    # 한국거래소(KRX)에서 전체 상장법인 목록 가져오기
    base_url =  "http://kind.krx.co.kr/corpgeneral/corpList.do"
    method = "download"
    if maket_type == 'kospi':
        marketType = "stockMkt"  # 주식 종목이 코스피인 경우
    elif maket_type == 'kosdaq':
        marketType = "kosdaqMkt" # 주식 종목이 코스닥인 경우
    elif maket_type == None:
        marketType = ""
    url = "{0}?method={1}&marketType={2}".format(base_url, method, marketType)

    df = pd.read_html(url, header=0)[0]
    
    # 종목코드 열을 6자리 숫자로 표시된 문자열로 변환
    df['종목코드']= df['종목코드'].apply(lambda x: f"{x:06d}") 
    
    # 회사명과 종목코드 열 데이터만 남김
    df = df[['회사명','종목코드']]
    
    return df


# In[ ]:


df_kospi = get_stock_info('kospi')
df_kospi.head()


# [6장: 255페이지]

# In[ ]:


df_kosdaq = get_stock_info('kosdaq')
df_kosdaq.head()


# In[ ]:


#--------------------------------------------------
# 회사 이름을 입력하면 종목 코드를 가져오는 함수
#--------------------------------------------------
def get_stock_code(company_name, maket_type=None):
    df = get_stock_info(maket_type)
    code = df[df['회사명']==company_name]['종목코드'].values
    
    if(code.size !=0):
        code = code[0]    
        return code
    else:
        print(f"[Error]입력한 [{company_name}]에 대한 종목 코드가 없습니다.")


# In[ ]:


get_stock_code('삼성전자', 'kospi') # 삼성전자 주식 종목 코드 가져오기, 코스피(kospi) 지정


# [6장: 256페이지]

# In[ ]:


get_stock_code('삼성전자') # 삼성전자 주식 종목 코드 가져오기, 주식 종류는 지정 안 함


# In[ ]:


get_stock_code('현대차')


# In[ ]:


get_stock_code('현대자동차')


# In[ ]:


company_names = ["삼성전자", "현대자동차", "NAVER"]

print("[현재 주식 가격(원)]")
for company_name in company_names:
    stock_code = get_stock_code(company_name)
    current_stock_price = get_current_stock_price(stock_code)
    print(f"{company_name}: {current_stock_price}")


# [6장: 257페이지]

# In[ ]:


get_stock_code('CJ 바이오사이언스', 'kosdaq') # 주식 종목 코드 가져오기, 코스닥(kosdaq) 지정


# In[ ]:


get_stock_code('CJ 바이오사이언스') # 주식 종목 코드 가져오기, 주식 종류는 지정 안 함


