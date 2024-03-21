#!/usr/bin/env python
# coding: utf-8

# # 5장 데이터 처리와 분석을 위한 라이브러리

# ## 5.1 배열 데이터 연산에 효율적인 넘파이(NumPy)

# ### 5.1.1 배열 데이터 생성

# #### 리스트 데이터로부터 배열을 생성

# [5장: 146페이지]

# In[ ]:


import numpy as np

# 정수, 실수 혼합 리스트
list_data = [0, 1, 2, 3, 4, 5.0]
a1 = np.array(list_data)
a1 # 모든 요소를 실수로 변환

print(type(a1), a1)

# [5장: 147페이지]

# In[ ]:


type(a1) # numpy.ndarray


# In[ ]:

# 2차원 배열(행렬)

a2 = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
a2


# #### 범위와 간격을 지정해 배열을 생성

# [5장: 148페이지]

# In[ ]:


np.arange(0, 10, 1) # start, stop, step 모두 지정


# In[ ]:


np.arange(0, 10) # start, stop만 지정(step=1)


# In[ ]:


np.arange(10) # stop만 지정(start=0. step=1)


# In[ ]:


np.arange(0, 5, 0.5) # start, stop, step 모두 지정


# #### 범위와 개수를 지정해 배열을 생성

# [5장: 149페이지]

# In[ ]:

# start, end를 포함하는 num개의 요소를 갖는 numpy 배열
# num : 요소의 갯수, 기본값 50
# step : 요소의 갯수, (stop-start)/(num-1)
# = (10 - 1) / (10 - 1) = 1


lnd = np.linspace(1, 10, 10) # start, stop, num 지정
print(len(lnd)) # 10개
print(lnd)

# In[ ]:

# 간격
st = round(np.pi / 19, 8)
print(st) # 0.16534698176788384

nx = 0
nl = []
for n in range(20):
    nx = round(nx, 8)
    nl.append(nx)
    nx += st
    
print(nl)


# numpy 사용
# 범위와 갯수를 지정해 배열을 생성

# 0부터 원주율까지 동일한 간격으로 나눈 20개의 요소를 갖는 배열을 생성
np.linspace(0, np.pi, 20)


