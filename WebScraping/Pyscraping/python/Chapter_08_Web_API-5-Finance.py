# -*- coding: utf-8 -*-
"""
Created on Tue Mar 26 11:49:24 2024

@author: jcp
"""

# ## 8.5 야후 파이낸스에서 주식 데이터 가져오기

# ### 8.5.1 설치 및 기본 사용법

# ### 8.5.2 미국 주식 데이터 가져오기

# [8장: 411페이지]

# In[ ]:


import yfinance as yf

ticker_symbol = "TSLA" # 테슬라 주식 심볼
ticker_data = yf.Ticker(ticker_symbol)

# 해당 종목의 정보 가져오기
# ticker_data.info

df = ticker_data.history(period='5d')
df


# [8장: 412페이지]

# In[ ]:

#
df = ticker_data.history(period='1mo', interval='1d',start='2022-04-18', end='2022-04-22')
df
# period = 1mo로 지정했지만 start와 end를 지정했기 때문에 무시.

# [8장: 413페이지]

# In[ ]:


df = ticker_data.history(start='2022-04-18', end='2022-04-23') # start와 end 모두 지정
# df = ticker_data.history(start='2022-04-18') # start만 지정
df


# In[ ]:
    
    # datetime 이용.


import datetime

start_p = datetime.datetime(2021,5,24) # 시작일 지정
end_p = datetime.datetime(2021,5,29)   # 종료일 지정

df = ticker_data.history(start=start_p, end=end_p) # start와 end 모두 지정
df


# ### 8.5.3 국내 주식 데이터 가져오기

# [8장: 414페이지]

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

    df = pd.read_html(url, header=0, encoding='euc-kr')[0]
    
    # 종목코드 열을 6자리 숫자로 표시된 문자열로 변환
    df['종목코드']= df['종목코드'].apply(lambda x: f"{x:06d}") 
    
    # 회사명과 종목코드 열 데이터만 남김
    df = df[['회사명','종목코드']]
    
    return df


# [8장: 415페이지]

# In[ ]:


def get_ticker_symbol(company_name, maket_type):
    """
    ----------------------------------------------------
      yfinance에 이용할 Ticker 심볼을 반환하는 함수
    ----------------------------------------------------
    """
    df = get_stock_info(maket_type)
    code = df[df['회사명']==company_name]['종목코드'].values
    code = code[0]
    
    if maket_type == 'kospi':
        ticker_symbol = code +".KS" # 코스피 주식의 심볼
    elif maket_type == 'kosdaq':
        ticker_symbol = code +".KQ" # 코스닥 주식의 심볼
    
    return ticker_symbol


# In[ ]:


import yfinance as yf

ticker_symbol = get_ticker_symbol("삼성전자", "kospi") # 삼성전자, 주식 종류는 코스피로 지정
ticker_data = yf.Ticker(ticker_symbol)

df = ticker_data.history(start='2022-06-13', end='2022-06-18') # 시작일과 종료일 지정
# df = ticker_data.history(period='5d') # 기간을 지정

# %%
df = df.reset_index()
df['Date'] = df['Date'].apply(lambda dt: datetime.strptime(str(dt),'%Y-%m-%d'))

df = df.set_index('Date')
# %%
df = df.reset_index()
df['Date'] = df['Date'].dt.strftime('%Y-%m-%d %H:%M:%S')

df = df.set_index('Date')

# [8장: 416페이지]

# In[ ]:


excel_file_name = "./삼성전자_주가_데이터1.xlsx" # 엑셀 파일 이름 지정
df.to_excel(excel_file_name)

print("생성 파일:", excel_file_name)


# ### 8.5.4 여러 주식 데이터 가져오기

# [8장: 417페이지]

# In[ ]:
    
    # download()


ticker_symbols = "MSFT" # 마이크로소프트 주식 심볼
# ticker_symbols = ["MSFT"] # 리스트도 지정해도 됨
df = yf.download(ticker_symbols, start="2020-01-01", end="2022-01-01")
df.tail()


# In[ ]:


# 그래프 그리기
import matplotlib.pyplot as plt

df['Close'].plot(grid=True, figsize=(15, 5), title="Microsoft")
plt.show()


# [8장: 418페이지]

# In[ ]:


ticker_symbols = ["GOOG", "AAPL"] # 주식 심볼 리스트(구글, 애플)
df = yf.download(ticker_symbols,  start="2020-01-01", end="2022-01-01")
df.tail()


# In[ ]:


# 그래프 그리기
import matplotlib.pyplot as plt

df['Close'].plot(grid=True, figsize=(15, 5))
plt.show()


# [8장: 419페이지]

# In[ ]:


# 그래프 그리기
df['Close'].plot(grid=True, figsize=(15, 5), subplots=True, layout=(2,1))
plt.show()

# %%
df['Close'].plot(grid=True, figsize=(15, 5), subplots=True)
plt.show()
# %%
df['Close'].plot(grid=True, figsize=(15, 5), layout=(2,1))
plt.show()

# ## 8.6 정리
