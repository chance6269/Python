#!/usr/bin/env python
# coding: utf-8

# # 04-2 분포 요약하기

# <table class="tfo-notebook-buttons" align="left">
#   <td>
#     <a target="_blank" href="https://nbviewer.jupyter.org/github/rickiepark/hg-da/blob/main/04-2.ipynb"><img src="https://jupyter.org/assets/share.png" width="61" />주피터 노트북 뷰어로 보기</a>
#   </td>
#   <td>
#     <a target="_blank" href="https://colab.research.google.com/github/rickiepark/hg-da/blob/main/04-2.ipynb"><img src="https://www.tensorflow.org/images/colab_logo_32px.png" />구글 코랩(Colab)에서 실행하기</a>
#   </td>
# </table>

# ## 산점도 그리기

# 산점도 : 두 변수 혹은 두 특성 값을 직교 좌표계에 점으로 나타내는 그래프

# In[1]:


import gdown

gdown.download('https://bit.ly/3pK7iuu', 'ns_book7.csv', quiet=False)


# In[2]:


import pandas as pd

ns_book7 = pd.read_csv('ns_book7.csv', low_memory=False)
ns_book7.head()


# In[3]:


import matplotlib.pyplot as plt

plt.scatter([1,2,3,4], [1,2,3,4])
plt.show()


# In[4]:


plt.scatter(ns_book7['번호'], ns_book7['대출건수'])
plt.show()


# In[5]:


plt.scatter(ns_book7['도서권수'], ns_book7['대출건수'])
plt.show()


# In[6]:

# alpha= : 투명도 조절 파라미터. 0에 가까울수록 투명하게, 1에 가까울수록 불투명하게

plt.scatter(ns_book7['도서권수'], ns_book7['대출건수'], alpha=0.1)
plt.show()


# In[7]:


average_borrows = ns_book7['대출건수']/ns_book7['도서권수']
plt.scatter(average_borrows, ns_book7['대출건수'], alpha=0.1)
plt.show()


# ## 히스토그램 그리기

# %%
# 히스토그램 : 수치형 특성의 값을 일정한 구간으로 나누어 구간 안에 포함된 데이터 개수를 막대 그래프로 그린 것.
# 도수(frequency) : 구간 안에 속한 데이터 개수
# 도수분포표 : 구간과 도수를 표로 요약한 것

# In[8]:
# hist() : 히스토그램 그리는 함수.
# 1차원 데이터를 입력받아 그림.
# bins= : 데이터를 몇 개의 구간으로 나눌지

plt.hist([0,3,5,6,7,7,9,13], bins=5)
plt.show()


# In[9]:

# np.histogram_bin_edges() :구간을 정확하게 확인할 수 있음.

import numpy as np

np.histogram_bin_edges([0,3,5,6,7,7,9,13], bins=5) # array([ 0. ,  2.6,  5.2,  7.8, 10.4, 13. ])
# 0~2.6, 2.6~5.2, 5.2~7.8, 7.8~10.4, 10.4~13


# In[10]:

# np.randn() : 표준정규분포를 따르는 랜덤한 실수를 생성
# np.randn.seed() : 유사난수 생성
np.random.seed(42) 
random_samples = np.random.randn(1000) # 샘플 갯수 1000개 생성


# In[11]:


print(np.mean(random_samples), np.std(random_samples)) # 0.01933205582232549 0.9787262077473543


# In[12]:


plt.hist(random_samples)
plt.show()


# In[13]:


plt.hist(ns_book7['대출건수'])
plt.show()


# In[14]:

# 구간 조정하기
# log scale : y축에 로그 함수 적용
# plt.yscale('log')
plt.hist(ns_book7['대출건수'])
plt.yscale('log')
plt.show()


# In[15]:

# log=True : 로그 스케일로 그리는 파라미터.
# yscale('log)와 동일한 결과
plt.hist(ns_book7['대출건수'], log=True)
plt.show()


# In[16]:


plt.hist(ns_book7['대출건수'], bins=100) # 구간을 100개로
plt.yscale('log')
plt.show()

# 대출건수가 증가함에 따라 도수가 줄어듬. 정규분포와는 거리가 멀다.

# In[17]:

# 도서명 길이는 정규분포에 가까운지 확인
title_len = ns_book7['도서명'].apply(len)
plt.hist(title_len, bins=100)
plt.show()
# 왼쪽에 편중된 그래프.

# In[18]:

# X축 로그스케일
# xscale('log')
plt.hist(title_len, bins=100)
plt.xscale('log')
plt.show()


# ## 상자 수염 그림 그리기

# %%
# 상자 수염 그림 : 최솟값, 세 개의 사분위수, 최댓값 이렇게 다섯 개의 숫자를 사용해 데이터를 요약하는 그래프
# 1. 사분위수를 계산. 25%와 75% 지점을 밑면과 윗면으로 하는 직사각형을 그린다.
# 2. 중간값에 해당하는 지점에 수평선을 긋는다.
# 3. 사각형의 밑면과 윗면에서 사각형의 높이의 1.5배만큼 떨어진 거리 안에서 가장 멀리 있는 샘플까지 수직선을 긋는다.
# 4. 이 수직선 밖에서 최솟값과 최댓값까지 데이터를 점으로 표시. 이 영역의 데이터를 이상치라고 부른다.

# IQR(Interquartile Range): 25% 와 75% 사이의 거리

# 이상치는 꼭 제거해야 하나요?
# : 단순히 IQR의 1.5배 거리 밖에 데이터를 의미.
 # 데이터의 양이 많을 수록 영향이 줄기 때문에 반드시 제거할 필요는 없다.

# In[19]:


temp = ns_book7[['대출건수','도서권수']]


# In[20]:

# boxplot() : 상자 수염 그림 그리는 함수. 1개 이상의 데이터프레임 열을 인수로 그래프를 그림.

plt.boxplot(temp)
plt.show()


# In[21]:


plt.boxplot(ns_book7[['대출건수','도서권수']])
plt.yscale('log')
plt.show()


# In[22]:

# vert=False : 상자 수염 그림 수평으로 그리기
# x-y축이 바뀌므로 로그스케일도 x축에 지정
plt.boxplot(ns_book7[['대출건수','도서권수']], vert=False)
plt.xscale('log')
plt.show()


# In[23]:

# 수염길이 조정하기
# whis= : 기본값 1.5
plt.boxplot(ns_book7[['대출건수','도서권수']], whis=10)
plt.yscale('log')
plt.show()


# In[24]:

# whis 매개변수를 백분율로 지정하기
plt.boxplot(ns_book7[['대출건수','도서권수']], whis=(0,100)) # 0%, 100%
plt.yscale('log')
plt.show()


# ## 판다스의 그래프 함수

# ### 산점도 그리기

# In[25]:

# pd.plot.scatter(x축 열, y축 열)

ns_book7.plot.scatter('도서권수', '대출건수', alpha=0.1)
plt.show()


# ### 히스토그램 그리기

# In[26]:

# pd.plot.hist()
ns_book7['도서명'].apply(len).plot.hist(bins=100)
plt.show()


# ### 상자 수염 그림 그리기

# In[28]:

# pd.boxplot()
ns_book7[['대출건수','도서권수']].boxplot()
plt.yscale('log')
plt.show()

# 모두 matplotlib을 사용했을 때와 유사함.
# 판다스에서 그래프 출력을 위해 기본적으로 matplotlib를 사용하기 때문.

# ## 확인문제

# #### 4.

# In[29]:


selected_rows = (1980 <= ns_book7['발행년도']) & (ns_book7['발행년도'] <= 2022)
plt.hist(ns_book7.loc[selected_rows, '발행년도'])
plt.show()


# #### 5.

# In[30]:


plt.boxplot(ns_book7.loc[selected_rows, '발행년도'])
plt.show()

