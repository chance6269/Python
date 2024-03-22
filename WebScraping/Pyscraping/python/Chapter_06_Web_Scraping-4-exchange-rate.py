# -*- coding: utf-8 -*-
"""
Created on Fri Mar 22 15:30:32 2024

@author: jcp
"""

# ### 6.2.3 환율 정보 가져오기

# #### 현재의 환율 정보 가져오기

# [6장: 259페이지]

# In[ ]:


import pandas as pd

url = 'https://finance.naver.com/marketindex/exchangeDetail.naver?marketindexCd=FX_USDKRW'

# url에서 표 데이터를 추출해 DataFrame 데이터의 리스트로 반환
dfs = pd.read_html(url,encoding='cp949')
dfs


# [6장: 260페이지]

# In[ ]:


len(dfs)


# In[ ]:


dfs[0]


# In[ ]:


exchange_rate_df = dfs[0].replace({'전일대비상승': '▲', 
                                   '전일대비하락': '▼'}, regex=True)
exchange_rate_df


# [6장: 262페이지]

# In[ ]:


import pandas as pd

# 네이버 금융의 환율 정보 웹 사이트 주소
url = 'https://finance.naver.com/marketindex/exchangeList.nhn' 

# 웹 사이트의 표 데이터에서 두 번째 줄을 DataFrame 데이터의 columns로 선택
dfs = pd.read_html(url, header=1, encoding='euc-kr') 

dfs[0].head() # 전체 데이터 중 앞의 일부분만 표시


# #### 과거의 환율 정보 가져오기

# [6장: 264페이지]

# In[ ]:


import pandas as pd

base_url = "https://finance.naver.com/marketindex/exchangeDailyQuote.nhn"
currency_code = "FX_USDKRW" # 통화 코드
page_num = 1

url = f"{base_url}?marketindexCd={currency_code}&page={page_num}"
dfs = pd.read_html(url, header=1, encoding='euc-kr')

# # 행과 열의 최대 표시 개수를 임시로 설정
# with pd.option_context('display.max_rows',4, 'display.max_columns',6): 
#     pd.set_option("show_dimensions", False) # 행과 열 개수 정보 숨기기
#     display(dfs[0])


# [6장: 265페이지]

# In[ ]:


import pandas as pd
import time

# 날짜별 환율 데이터를 반환하는 함수
# - 입력 인수: currency_code(통화코드), last_page_num(페이지 수)
# - 반환: 환율 데이터
def get_exchange_rate_data(currency_code, last_page_num):
    base_url = "https://finance.naver.com/marketindex/exchangeDailyQuote.nhn"

    df = pd.DataFrame()

    for page_num in range(1, last_page_num+1):
        url = f"{base_url}?marketindexCd={currency_code}&page={page_num}"
        dfs = pd.read_html(url, header=1, encoding='euc-kr')

        if dfs[0].empty: # 통화 코드가 잘못 지정됐거나 마지막 페이지의 경우 for 문을 빠져나오기 위한 코드
            if (page_num==1):
                print(f"통화 코드({currency_code})가 잘못 지정됐습니다.")
            else:
                print(f"{page_num}가 마지막 페이지입니다.")
            break

        df = pd.concat([df, dfs[0]], ignore_index=True) # page별로 가져온 DataFrame 데이터 연결
        time.sleep(0.1) # 0.1초간 멈춤
        
    return df


# [6장: 266페이지]

# In[ ]:


df_usd = get_exchange_rate_data('FX_USDKRW', 2)

# 행과 열의 최대 표시 개수를 임시로 설정
# with pd.option_context('display.max_rows',4, 'display.max_columns',6):
#     pd.set_option("show_dimensions", False) # 행과 열 개수 정보 숨기기
#     display(df_usd)


# [6장: 267페이지]

# In[ ]:


df_eur = get_exchange_rate_data('FX_EURKRW', 1)

# 행과 열의 최대 표시 개수를 임시로 설정
# with pd.option_context('display.max_rows',4, 'display.max_columns',6):
#     pd.set_option("show_dimensions", False) # 행과 열 개수 정보 숨기기
#     display(df_eur.head())


