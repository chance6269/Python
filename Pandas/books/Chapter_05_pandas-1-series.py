# -*- coding: utf-8 -*-
"""
Created on Thu Mar 21 10:26:13 2024

@author: jcp
"""

# ## 5.2 표 데이터 처리에 강한 판다스(pandas)

# ### 5.1.2 데이터 구조와 생성

# #### Series 데이터의 구조와 생성

# [5장: 156페이지]

# In[ ]:


import pandas as pd

s1 = pd.Series([10, 20, 30, 40, 50]) # 리스트로 Series 데이터 생성
s1


# In[ ]:


s1.index


# [5장: 157페이지]

# In[ ]:


s1.values


# In[ ]:


import numpy as np

# 리스트로 판다스 시리즈 객체 생성
index_data = ['2020-02-27','2020-02-28','2020-02-29','2020-03-01'] # 날짜 지정 
data = [3500, 3579, np.nan, 3782] # 데이터 지정

# np.nan : NaN(Not a Number)

s2 = pd.Series(data, index=index_data) # Series 데이터 생성
s2


# In[ ]:

# 딕셔너리로 시리즈 객체 생성
# 키 -> 인덱스
# 값 -> 값
s3 = pd.Series({'국어': 100, '영어': 95, '수학': 90})
s3


# [5장: 158페이지]

# In[ ]:


s4 = pd.Series({'B': 4.0, 'A': 5.0, 'D': 2.0, 'C': 3.0})
s4


# In[ ]:


s4.reindex(['A', 'B', 'C', 'D'])


