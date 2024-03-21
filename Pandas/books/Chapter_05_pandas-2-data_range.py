# -*- coding: utf-8 -*-
"""
Created on Thu Mar 21 10:47:27 2024

@author: jcp
"""

# #### 날짜 데이터 자동 생성

# [5장: 160페이지]

# In[ ]:

import pandas as pd
import numpy as np

index_data = pd.date_range(start='2020-02-27', end='2020-03-01') # 날짜 생성
data = [3500, 3579, np.nan, 3782] # 데이터 지정

pd.Series(data, index=index_data) # Series 데이터 생성


# In[ ]:


# 시작일 ~ 종료일 이틀 주기(freq='2D')로 날짜 생성
pd.date_range(start='2020-07-01', end='2020-07-10', freq='2D') 


# In[ ]:


# 시작일 기준으로 설정한 기간(periods=12) 동안 날짜 생성
pd.date_range(start='2020-07-01', periods=12) 


# In[ ]:


# 시작일 기준으로 설정한 기간동안 업무일 기준(freq='B')으로 날짜 생성
pd.date_range(start='2020-07-01', periods=12, freq='B') 


# [5장: 161페이지]

# In[ ]:


# 시작일과 시각 기준으로 설정한 기간동안 날짜 및 시각 생성(freq='30min')
pd.date_range(start='2020-07-01 10:00', periods=5, freq='30min') 


# #### DataFrame 데이터 구조와 생성 

# [5장: 162페이지]

# In[ ]:


import pandas as pd

data = [[1,2,3], [4,5,6], [7,8,9]]
df = pd.DataFrame(data)
df


# [5장: 163페이지]

# In[ ]:


import numpy as np
import pandas as pd

data = np.array([[1, 2, 3], [4, 5, 6], [7, 8 ,9], [10, 11, 12]]) # data 생성
index_data = pd.date_range('2023-01-11', periods=4) # index를 위한 날짜 데이터
columns_data = ['A', 'B', 'C'] # columns를 위한 리스트 데이터

pd.DataFrame(data, index=index_data, columns=columns_data) # DataFrame 데이터 생성


# In[ ]:


dict_data = {'연도': [2021, 2021, 2022, 2022],
             '지사': ['한국', '미국', '한국','미국'],
             '고객 수': [200, np.nan, 250, 450]} # 딕셔너리 데이터

df = pd.DataFrame(dict_data) # 딕셔너리 데이터로부터 DataFrame 데이터 생성
df


# [5장: 164페이지]

# In[ ]:


df.index


# In[ ]:


df.columns


# In[ ]:


df.values


# [5장: 165페이지]

# In[ ]:


df1 = df.set_index("연도")
df1


# In[ ]:


dict_data = {'A': [10, 20, 30, 40,],
             'B': [0.1, 0.2, 0.3, 0.4],
             'C': [100, 200, 300, 400]} # 딕셔너리 데이터

df2 = pd.DataFrame(dict_data) # 딕셔너리 데이터로부터 DataFrame 데이터 생성
df2


# [5장: 166페이지]

# In[ ]:


df2.reindex([2, 0, 3, 1])


# In[ ]:


df2.reindex(columns=['B', 'C', 'A'])


