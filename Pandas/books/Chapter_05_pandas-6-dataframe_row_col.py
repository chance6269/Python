# -*- coding: utf-8 -*-
"""
Created on Thu Mar 21 15:58:29 2024

@author: jcp
"""

# #### 행과 열 데이터 선택

# In[ ]:


dict_data = {'A': [0, 1, 2, 3, 4],
             'B': [10, 11, 12, 13, 14],
             'C': [20, 21, 22, 23, 24]} # 딕셔너리 데이터

index_data = ['a', 'b', 'c', 'd', 'e'] # index 지정용 데이터

df = pd.DataFrame(dict_data, index=index_data) # DataFrame 데이터 생성
df


# [5장: 196페이지]

# In[ ]:


df.loc['a', 'A'] # loc 이용


# In[ ]:


df.iloc[0, 0] # iloc 이용


# In[ ]:


df.loc['a':'c', ['A', 'B']] # loc 이용


# In[ ]:


df.iloc[0:3, 0:2] # iloc 이용


# [5장: 197페이지]

# In[ ]:


df.loc[:, ['A', 'B']] # loc 이용


# In[ ]:


df.iloc[:, 0:2] # iloc 이용


# In[ ]:


df.loc[df['A']>2, ['A', 'B']] # loc 이용


# [5장: 198페이지]

# In[ ]:

# 범위 지정 값 변경
# 행 : 인덱스 레이블
# 열 : ['A','B']

df.loc['a':'c', ['A', 'B']] = 50 # 스칼라 값 지정
df


# In[ ]:


df.iloc[3:5, 1:3] = 100 # 스칼라 값 지정
df


# In[ ]:


df.loc[df['B']<70, 'B'] = 70 # 스칼라 값 지정
df


# [5장: 199페이지]

# In[ ]:

# 조건 칼럼('C')가 30보다 작은 행을 선택
# 칼럼('D')를 새로 생성하여 40을 넣음.
# 해당하지 않는 행은 'NaN'
df.loc[df['C']<30, 'D'] = 40 # loc 이용. 스칼라 값 지정
df


