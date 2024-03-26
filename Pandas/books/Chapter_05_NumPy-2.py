# -*- coding: utf-8 -*-
"""
Created on Thu Mar 21 10:04:26 2024

@author: jcp
"""

# ### 5.1.2 배열 데이터 선택

# #### 배열의 인덱싱

# [5장: 150페이지]

# In[ ]:

# %%
lst = [0, 10, 20, 30, 40, 50]
print(lst[-1]) # 맨 마지막 요소: 50

# 슬라이싱(-1)과 참조(-1)의 차이?
print(lst[0:-1]) # [0, 10, 20, 30, 40]

# %%
import numpy as np

a1 = np.array([0, 10, 20, 30, 40, 50]) # 1차원 배열 생성
[a1[0], a1[3], a1[5], a1[-1], a1[-2]]  # 배열 인덱싱의 다양한 예


# In[ ]:


a1[4] = 90
a1


# In[ ]:


a2 = np.array([0, 10, 20, 30, 40, 50]) # 1차원 배열 생성
a2[[4, 0, 5, -1, -2]]                  # 배열의 위치로 여러 개의 요소를 선택


# [5장: 151페이지]

# In[ ]:


a = np.array([0, 1, 2, 3, 4, 5, 6, 7, 8, 9])
a


# In[ ]:


a[a >= 5] # array([5, 6, 7, 8, 9])


# In[ ]:


a[(a % 2) == 0] # array([0, 2, 4, 6, 8])


# In[ ]:


a[ ((a % 2)==0) & (a > 5) ] # 두 조건을 동시에 만족하는 요소만 선택
# array([6, 8])


# In[ ]:


a[ ((a % 2)==0) | (a > 5) ] # 두 조건 중 하나만 만족해도 요소 선택
# array([0, 2, 4, 6, 7, 8, 9])

# In[ ]:

# 논리부정 : ~

a[ ~((a % 2)==0) ] # 짝수를 찾는 조건의 논리 부정을 이용해 홀수 선택
# array([1, 3, 5, 7, 9])

# #### 배열의 슬라이싱

# [5장: 152페이지]

# In[ ]:


import numpy as np

a1 = np.array([0, 10, 20, 30, 40, 50]) # 1차원 배열 생성

a1[1:4] # start, end를 모두 지정해 슬라이싱. 선택 범위: start ~ end-1


# In[ ]:


a1[:3] # end만 지정해 슬라이싱. 선택 범위: 0 ~ end-1


# In[ ]:


a1[2:] # start만 지정해 슬라이싱. 선택 범위: start ~ 배열의_마지막_위치


# In[ ]:


a1[:] # start, end 모두 지정하지 않으면 배열 전체가 선택됨


# [5장: 153페이지]

# In[ ]:


a1[2:5] = np.array([25, 35, 45]) # 선택한 위치(2, 3, 4)의 요소를 새로운 배열로 변경
a1 # array([ 0, 10, 25, 35, 45, 70])


# In[ ]:


a1[3:6] = 70 # 선택한 위치(3, 4, 5)의 요소를 모두 스칼라 값으로 변경
a1 # array([ 0, 10, 25, 70, 70, 70])


# In[ ]:


a2 = np.array([0, 10, 20, 30, 40, 50, 60, 70, 80, 90]) # 1차원 배열 생성

a2[0:10:2] # 선택 범위: start~end-1, 증가폭(step): 2                             
# array([ 0, 20, 40, 60, 80])

# In[ ]:


a2[2:8:3] # 선택 범위: start~end-1, 증가폭(step): 3
# array([20, 50])

# In[ ]:


a2[0:10:] # 선택 범위: start ~ end-1, 증가폭(step): 1


# [5장: 154페이지]

# In[ ]:


a2[3::] # 선택 범위: start~배열의_마지막_위치, 증가폭(step): 1


# In[ ]:


a2[:5:] # 선택 범위: 0~end-1, 증가폭(step): 1


# In[ ]:


a2[::] # 선택 범위: 0 ~ 배열의_마지막_위치, 증가폭(step): 1


# In[ ]:


a2[::-1] # 선택 범위: 배열의_마지막_위치~0, 증가폭(step): -1 -> 역순으로 선택
# array([90, 80, 70, 60, 50, 40, 30, 20, 10,  0])

# In[ ]:


a2[8:2:-2] # 증가폭(step): -2 -> 역순으로 선택
# array([80, 60, 40])
