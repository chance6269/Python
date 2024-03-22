# -*- coding: utf-8 -*-
"""
Created on Fri Mar 22 15:31:09 2024

@author: jcp
"""

# ### 6.2.4 부동산 정보 가져오기

# [6장: 269페이지]

# In[ ]:


import pandas as pd

base_url = "https://land.naver.com/news/trendReport.naver"
page_num = 1

url = f"{base_url}?page={page_num}"
dfs = pd.read_html(url)

df = dfs[0] # 리스트의 첫 번째 항목에 동향 보고서 제목 데이터가 있음

# 행과 열의 최대 표시 개수를 임시로 설정
# with pd.option_context('display.max_rows',4, 'display.max_columns',6): 
#     pd.set_option("show_dimensions", False) # 행과 열 개수 정보 숨기기
#     display(df)


# [6장: 270페이지]

# In[ ]:


import pandas as pd

# 원본 DataFrame의 제목 열에 있는 문자열을 분리해 
# 전국, 서울, 수도권의 매매가 변화율 열이 있는 DataFrame 반환하는 함수
def split_title_to_rates(df_org):
    df_new = df_org.copy()

    df_temp = df_new['제목'].str.replace('%', '') # 제목 문자열에서 % 제거
    df_temp = df_temp.str.replace('보합', '0')    # 제목 문자열에서 보합을 0으로 바꿈
    df_temp = df_temp.str.replace('보합세', '0')  # 제목 문자열에서 보합세를 0으로 바꿈
    
    regions = ['전국', '서울', '수도권']    
    for region in regions:
        df_temp = df_temp.str.replace(region, '') # 문자열에서 전국, 서울, 수도권 제거

    df_temp = df_temp.str.split(']', expand=True) # ]를 기준으로 열 분리
    df_temp = df_temp[1].str.split(',', expand=True) # ,를 기준으로 열 분리
    
    df_temp = df_temp.astype(float)
    
    df_new[regions] = df_temp # 전국, 서울, 수도권 순서대로 DataFrame 데이터에 할당

    return df_new[['등록일'] + regions + ['번호']] # DataFrame에서 필요한 열만 반환


# [6장: 271페이지]

# In[ ]:


df_rate = split_title_to_rates(df) # split_title_to_rates() 함수 호출
df_rate.head()                     # 앞의 일부만 출력


# In[ ]:


import pandas as pd

base_url = "https://land.naver.com/news/trendReport.naver"

df_rates = pd.DataFrame() # 전체 데이터가 담길 DataFrame 데이터
last_page_num = 8 # 가져올 데이터의 마지막 페이지 

for page_num in range(1, last_page_num+1):

    url = f"{base_url}?page={page_num}"
    dfs = pd.read_html(url)

    df_page = dfs[0] # 리스트의 첫 번째 항목에 동향 보고서 제목 데이터가 있음
    df_rate = split_title_to_rates(df_page)
    
    # 세로 방향으로 연결 (기존 index를 무시)
    df_rates = pd.concat([df_rates, df_rate], ignore_index=True) 

# 최신 데이터와 과거 데이터의 순서를 바꿈. index도 초기화함  
df_rates = df_rates[::-1].reset_index(drop=True)
df_rates.head() # 앞의 일부만 출력

# 행과 열의 최대 표시 개수를 임시로 설정
with pd.option_context('display.max_rows',4, 'display.max_columns',6): 
    pd.set_option("show_dimensions", False) # 행과 열 개수 정보 숨기기
    display(df_rates)


# [6장: 273페이지]

# In[ ]:


import matplotlib as mpl

mpl.rcParams['font.family'] = 'Malgun Gothic' # '맑은 고딕'으로 폰트 설정 
mpl.rcParams['axes.unicode_minus'] = False # 마이너스(-) 폰트 깨짐 방지


# In[ ]:


# get_ipython().run_line_magic('matplotlib', 'inline')


# In[ ]:


import pandas as pd
import matplotlib.pyplot as plt

df_rates.tail(40).plot(x='등록일', y=['전국', '서울', '수도권'], 
                       figsize=(10, 8), subplots=True, layout=(3,1),
                       style = '-o', grid=True) # 그래프 그리기
plt.show()


